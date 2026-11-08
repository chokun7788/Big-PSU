"""Source-bound CS2 pre-match and venue clauses; no authority completion claim."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('prematch_scope_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);checks={};details=[]
q='ขอสอบถามหน่อยครับ กติกา CS2 เรื่องข้อกำหนดก่อนแข่งและหน้างาน ว่าอย่างไร'
def run(question,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(question,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 details.append({'question':question,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
r=run(q);delivered=lambda x:{c['record_id'] for c in x.decision_artifact.get('domain_flow',{}).get('typed_claims',[])} if x else set();ids=['competition_competition_rules_cs2_psu_phuket_2026_section_'+str(n).zfill(3) for n in [15,50,51,52,53]]
checks['actual_source_clauses_covered']=set(ids)<=delivered(r)
checks['conditions_and_exceptions_preserved']='อาจถูกตัดสิทธิ์' in r.answer and 'หัวหน้าทีม' in r.answer and 'หมากฝรั่ง' in r.answer
checks['source_completeness_not_claimed']='ไม่ยืนยัน' in r.answer and 'ความครบถ้วน' in r.answer
other=run('กติกา TEKKEN 8 เรื่องข้อกำหนดก่อนแข่งและหน้างาน ว่าอย่างไร');checks['other_game_not_given_cs2_rules']=not (set(ids)&delivered(other))
regular=run('เวลาเปิดศูนย์วันจันทร์เป็นอย่างไร');checks['studio_hours_not_competition_rules']=not (set(ids)&delivered(regular))
record=copy.deepcopy(view.snapshot()['release']['records'][ids[2]]);v=record['fields']['text']['value'];v['th']=v['th'].replace('จนกว่าจะจบแมตช์','จนจบรอบทดสอบ');v['en']=v['en'].replace('until the match concludes','until the controlled round ends');save_owner_record(store,record,record['revision'],'isolated-prematch-source-control');edited=run(q);checks['changed_owner_clause_visible']=bool(edited and 'จนจบรอบทดสอบ' in edited.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][ids[2]]['fields']['text']['value']['th']='อนุญาตปลอมทุกอย่าง';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
f=run(q,Forged());checks['forged_unattested_source_suppressed']=f is None or 'อนุญาตปลอมทุกอย่าง' not in f.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_http_or_model_calls':0,'actual_owner_frozen_data_modified':False,'complete_rulebook_or_authority_proven':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'checks':checks,'all_passed':report['all_passed']}));assert report['all_passed']
