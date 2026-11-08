"""P7: verify interfaces/inputs and freeze one complete integrated candidate."""
import ast,json,hashlib,os,sys,subprocess,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';B=R.parent/'r101_complete_flow_20261019'
if (R/'FINAL_SOURCE_MANIFEST.json').exists():raise SystemExit('Freeze exists; create a new version instead of replacing evidence')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((R/'BASELINE_MANIFEST.json').read_text('utf8'))
bad=[p for p,h in baseline.items() if not (B/'system'/p).is_file() or sha(B/'system'/p)!=h]
if bad:raise SystemExit('R101 source changed: '+repr(bad))
errors=[]
for p in [*(S/'app').rglob('*.py'),*R.glob('*.py')]:
 try:ast.parse(p.read_text('utf8'),filename=str(p))
 except (SyntaxError,UnicodeDecodeError) as e:errors.append(str(e))
if errors:raise SystemExit(json.dumps(errors))
for p in [S/'app/knowledge/common/ui/owner.js',S/'web_chat/app.js']:
 x=subprocess.run(['node','--check',str(p)],capture_output=True,text=True)
 if x.returncode:raise SystemExit(x.stderr)
sys.path[:0]=[str(S),str(R)]
from app.knowledge.common.registry import CATALOG,SCHEMAS,VERSION
from app.knowledge.common.task_contracts import TASKS
from app.knowledge.common.read_graph import REQUIRED
assert set(TASKS)==set(REQUIRED) and len(TASKS)==32 and len(CATALOG)==24
from app.knowledge.common import complete_flow,claim_bindings,flow_audit,financial_scope,temporal_query
model={'name':os.getenv('PSU_KNOWLEDGE_LLM_MODEL','scb10x/typhoon2.5-qwen3-4b'),'num_ctx':3072,'temperature':0,'max_concurrent_generation':1,'model_generation_run_before_freeze':False}
base=os.getenv('OLLAMA_URL','http://127.0.0.1:11434').rstrip('/')
try:
 with urllib.request.urlopen(base+'/api/version',timeout=3) as h:model['ollama_version']=json.load(h)
 with urllib.request.urlopen(base+'/api/tags',timeout=3) as h:tags=json.load(h)
 model['installed_candidates']=[{k:m.get(k) for k in ['name','model','digest','size','details']} for m in tags.get('models',[]) if str(m.get('name','')).removesuffix(':latest')==model['name'].removesuffix(':latest') or str(m.get('model','')).removesuffix(':latest')==model['name'].removesuffix(':latest')]
 model['endpoint_reachable']=True
except (OSError,ValueError) as e:model.update(endpoint_reachable=False,error_type=type(e).__name__)
(R/'MODEL_CONFIG_MANIFEST.json').write_text(json.dumps(model,ensure_ascii=False,indent=2),'utf8')
current={p.relative_to(S).as_posix():sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
if current['data/knowledge/common.sqlite']!=baseline['data/knowledge/common.sqlite']:raise SystemExit('Real knowledge DB changed')
(R/'FINAL_SOURCE_MANIFEST.json').write_text(json.dumps(current,indent=2),'utf8')
paths=[*R.glob('*.py'),R/'BATCH_JOBS.json',R/'RETAINED_HOLDOUT_JOBS.jsonl',R/'MODEL_CONFIG_MANIFEST.json',R/'fixtures/BASE_SYNTHETIC.sqlite',
 R.parent/'r98_flow_v2_implementation_20261019/FOCUSED_JOBS.jsonl',R.parent/'r58_examples_240_20261012/DEMO_ONLY.sqlite']
inputs={os.path.relpath(p,R).replace('\\','/'):sha(p) for p in paths}
(R/'FROZEN_INPUTS.json').write_text(json.dumps(inputs,indent=2),'utf8')
plan=json.loads((R/'FLOW_COVERAGE_PLAN.json').read_text('utf8'))
for c in plan['cases']:
 c.update(status='implemented_pending_integrated_verification',runner_case_id=[j['id'] for j in json.loads((R/'BATCH_JOBS.json').read_text('utf8')) if j['scenario']==c['id']],
  implementation_paths=['system/app/knowledge/common/complete_flow.py','system/app/knowledge/common/read_graph.py','acceptance_cases.py'])
for task in plan['tasks']:task.update(status='implemented_pending_integrated_verification',runner_case_id='test_task_matrix.py:'+task['task'])
for kind in plan['owner_kinds']:kind.update(status='implemented_pending_integrated_verification',runner_case_id='test_all_categories.py:'+kind['kind'])
plan.update(status='implementation_frozen_tests_not_started',runtime_edited=True,chatbot_tests_run=False)
(R/'IMPLEMENTATION_COVERAGE.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),'utf8')
report={'phase':'P7_frozen','reference_r101_unchanged':True,'real_database_unchanged':True,'source_files':len(current),'syntax_errors':[],
 'javascript_syntax_valid':True,'schemas':len(SCHEMAS),'tasks':len(TASKS),'r97_scenarios':37,'acceptance_variants':444,'retained_91_requests':91,
 'additional_retained_questions':192,'behavioral_tests_before_freeze':0,'candidate_not_installed_over_R78':True,'real_approvals_created':False,
 'model_endpoint_reachable':model.get('endpoint_reachable'),'model_installed_match':bool(model.get('installed_candidates'))}
(R/'FREEZE_STATUS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps(report,ensure_ascii=False))
