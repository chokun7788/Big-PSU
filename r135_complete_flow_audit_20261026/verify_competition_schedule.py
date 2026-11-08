"""Competition schedule selection must retain source timing conditions."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('competition_schedule_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
q='Counter-Strike 2 แข่งจริง กฎเกี่ยวกับตารางและเวลาแข่งขัน เป็นแบบไหน';rid='competition_competition_rules_cs2_psu_phuket_2026_section_015';x=run(q);claims=lambda r:{c['record_id'] for c in r.decision_artifact.get('domain_flow',{}).get('typed_claims',[])} if r else set();checks['correct_source_schedule_clause']=rid in claims(x);checks['schedule_conditions_and_late_conditional_preserved']=all(t in x.answer for t in ['อย่างน้อย 1 วัน','ยืนยันการเข้าแข่งขัน','อาจถูกตัดสิทธิ์']);checks['does_not_claim_full_rulebook']='ความครบถ้วน' in x.answer
other=run('TEKKEN 8 กติกาเรื่องเวลาแข่งขันคืออะไร');checks['different_game_does_not_use_cs2_schedule']=rid not in claims(other)
regular=run('เวลาเปิดศูนย์วันจันทร์เป็นอย่างไร');checks['studio_hours_not_competition_schedule']=rid not in claims(regular)
record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['text']['value']['th']=record['fields']['text']['value']['th'].replace('อย่างน้อย 1 วัน','อย่างน้อย 2 วัน');record['fields']['text']['value']['en']=record['fields']['text']['value']['en'].replace('at least 1 day','at least 2 days');save_owner_record(store,record,record['revision'],'isolated-competition-schedule-control');z=run(q);checks['edited_source_used']=bool(z and 'อย่างน้อย 2 วัน' in z.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['text']['value']['th']='เวลาการแข่งขัน สายการแข่งขันประกาศปลอม 999 วัน';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
f=run(q,Forged());checks['unattested_schedule_suppressed']=f is None or '999 วัน' not in f.answer
report={'checks':checks,'all_passed':all(checks.values()),'actual_model_calls':0,'owner_data_modified':False,'event_authority_and_complete_semantics_proven':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
