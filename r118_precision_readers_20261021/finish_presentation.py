"""Archive HTTP revision02, then verify one renderer-only public text fix."""
import copy,hashlib,json,os,shutil,sys
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';run=R/'http02'
assert json.loads((run/'TEST_COMPLETE.json').read_text('utf8'))['complete']
shutil.copytree('\\\\?\\'+str(S.resolve()),'\\\\?\\'+str((run/'FROZEN_SYSTEM').resolve()),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
freeze=json.loads((run/'RUN_FREEZE.json').read_text('utf8'))['files'];checked=0
for name,h in freeze.items():
 p=Path(name)
 if p.is_relative_to(S):
  assert hashlib.sha256((run/'FROZEN_SYSTEM'/p.relative_to(S)).read_bytes()).hexdigest()==h;checked+=1
(run/'ARCHIVED_CODE_VERIFIED.json').write_text(json.dumps({'verified':True,'files':checked,'revision':'R118 revision02','run_freeze_paths_resolve_via':'FROZEN_SYSTEM for system/*'}),'utf8')
p=S/'app/knowledge/common/answer.py';before=p.read_text('utf8');old="key in {'question','intent_key','scope_note','source_variants'}"
assert before.count(old)==1;p.write_text(before.replace(old,"key in {'question','topic','intent_key','scope_note','source_variants'}"),'utf8')
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';os.environ['PSU_ESPORTS_NOW']='2026-10-21T12:00:00+07:00'
sys.path.insert(0,str(S))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import value
rows=[json.loads(s) for s in (run/'RESULTS.jsonl').open(encoding='utf8')]
saved=next(r for r in rows if 'ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว' in r['question'])
store=MigratedView(S/'data/knowledge/common.sqlite');snap=store.snapshot();plan=copy.deepcopy(saved['response']['decision_artifact']['query_plan'])
result=CommonAnswerer(store).execute_task(saved['question'],snap=snap,at=datetime.fromisoformat('2026-10-21T12:00:00+07:00'),lang='th',plan=plan)
facts=[value(snap['release']['records'][rid],'answer') for rid in plan['record_ids']]
facts=[v.get('th') if isinstance(v,dict) else v for v in facts]
checks=[{'name':'routing_topic_hidden_from_customer_text','passed':'หัวข้อเชิงความหมาย' not in result.answer and 'knowledge' not in result.answer},
 {'name':'all_selected_policy_answers_preserved','passed':all(v in result.answer for v in facts)},
 {'name':'hidden_metadata_evidence_retained_in_audit','passed':any(o['field']=='topic' and o['evidence_refs'] for o in result.decision_artifact['obligations'])}]
out={'passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks,'question':saved['question'],'key':saved['key'],
 'before':saved['response']['answer'],'after':result.answer,'network_calls':0,'new_benchmark_questions':0,'method':'saved_accepted_plan_replay_through_actual_CommonAnswerer.execute_task',
 'full_http_scores_apply_to':'R118 revision02','final_revision':'R118 revision03 (topic field visibility only)',
 'changed_file':str(p.resolve()),'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(R/'RENDER_REGRESSION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
assert all(c['passed'] for c in checks)
print(json.dumps({'passed':out['passed'],'total':out['total'],'after':result.answer},ensure_ascii=False))
