"""Source-bound conditional forfeits; no blanket penalty or invented authority."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('conditional_forfeit_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);checks={};details=[]
q='TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม'
def run(question,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(question,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 assert r is not None
 details.append({'question':question,'answer':r.answer,'artifact':r.decision_artifact});return r
r=run(q);a=json.dumps(r.decision_artifact);ids=['competition_competition_rules_tekken8_psu_esports_section_'+str(n).zfill(3) for n in [3,5,7]]
checks['source_conditions_survive_with_distinct_penalty_units']=all(rid in a for rid in ids) and 'ปรับแพ้ 1 รอบ' in r.answer and 'หากออกจากเกมโดยไม่ได้รับอนุญาต' in r.answer
checks['does_not_claim_all_violations_certainly_forfeit']='ยังยืนยันการใช้เงื่อนไข' in r.answer and 'ความครบถ้วน' in r.answer
checks['source_pause_conditions_are_not_silently_reconciled']='ห้ามหยุดเกม' in r.answer and 'ผู้เล่นทุกคนยินยอม' in r.answer
r=run('ถ้าผิดกติกา VALORANT จะโดนปรับแพ้ไหม');checks['different_game_does_not_borrow_tekken_clauses']='ตัวละคร DLC' not in r.answer and 'TEKKEN' not in r.answer
r=run('TEKKEN 8 มีปุ่มจอยอะไรบ้าง');checks['control_predicate_does_not_become_forfeit_lookup']='TEKKEN' in r.answer and 'ปรับแพ้ 1 รอบ' not in r.answer
record=copy.deepcopy(view.snapshot()['release']['records'][ids[1]])
for lang,text in record['fields']['text']['value'].items():record['fields']['text']['value'][lang]=text.replace('ทันทีโดยไม่มีข้อยกเว้น','หลังคำตัดสินทดสอบ').replace('immediate loss with no exceptions','loss after controlled review')
save_owner_record(store,record,record['revision'],'isolated-forfeit-source-control');r=run(q);checks['actual_owner_source_edit_is_visible']='หลังคำตัดสินทดสอบ' in r.answer and ids[1] in json.dumps(r.decision_artifact)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][ids[0]]['fields']['text']['value']={'th':'ปรับแพ้ปลอมโดยไม่มีเงื่อนไข','en':'Forged unconditional forfeit'};s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run(q,Forged());checks['unattested_changed_clause_not_delivered']='ปรับแพ้ปลอมโดยไม่มีเงื่อนไข' not in r.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_http_or_model_calls':0,'actual_owner_frozen_data_modified':False,'whole_rulebook_authority_or_conflict_resolved':False}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
