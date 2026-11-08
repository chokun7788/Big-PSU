"""Latest-candidate-only execution. Reuse raw profiles, then agent adjudication.

The review is a task for this chat/heartbeat, not a request for user approval.
No context inference is regenerated and no baseline is rerun.
"""
import hashlib,json,os,subprocess,sys,time,traceback,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r129_full_plan_completion_20261024';PY=sys.executable;START=time.time()
def load(p):return json.loads(Path(p).read_text('utf-8-sig'))
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(name,value):
 p=R/name;t=p.with_name(p.name+'.new');t.write_text(json.dumps(value,ensure_ascii=False,indent=2),'utf8');os.replace(t,p)
def state(phase,**kw):
 write('STATUS.json',{'phase':phase,'pid':os.getpid(),'updated_at':time.time(),'elapsed_sec':time.time()-START,'complete':False,'production_installed':False,**kw})
def health():
 with urllib.request.urlopen('http://127.0.0.1:12921/health',timeout=5) as f:return json.load(f)
def source_identity():
 sys.path.insert(0,str(R/'system'))
 from app.knowledge.common.migrated_view import MigratedView
 s=MigratedView(R/'system/data/knowledge/common.sqlite').snapshot()
 payload={'active':s['active'],'epoch':s['epoch'],'records':s['release']['records'],'sources':s['release']['sources'],'source_pairs':s.get('source_pairs',{}),'withdrawn':s.get('withdrawn',[])}
 encoded=json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
 return {'sha256':hashlib.sha256(encoded).hexdigest(),'active':s['active'],'epoch':s['epoch'],'active_records':len(payload['records']),'withdrawn_records':len(payload['withdrawn']),'includes_source_bodies_and_record_revisions':True,'sqlite_wal_writes_not_hidden_by_main_file_hash':True}
def run(name,args=(),env=None):
 out=R/(Path(name).stem+'.controller.stdout.log');err=R/(Path(name).stem+'.controller.stderr.log')
 with out.open('x',encoding='utf8') as stdout,err.open('x',encoding='utf8') as stderr:
  child=subprocess.Popen([PY,'-B','-u',str(R/name),*map(str,args)],cwd=R.parent,env=env,stdout=stdout,stderr=stderr,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  while child.poll() is None:state(Path(name).stem,child_pid=child.pid,stdout=str(out),stderr=str(err));time.sleep(15)
  assert child.returncode==0,(name,child.returncode,str(err))
try:
 assert load(R/'OWNER50_REVIEW_FINAL.json')['source_scope_review_complete']
 assert load(R/'OWNER50_MAPPING.json')['original_records_unchanged']
 for pattern,file in [('graph_verification_*','RESULT.json'),('gateway_verification_*','RESULT.json'),('comparison_verification_*','RESULT.json'),('extended_*','RESULTS.json'),('source_guard_verification_*','VERIFICATION.json'),('live_verification_*','VERIFICATION.json'),('owner_scope_verification_*','RESULT.json'),('source_match_metadata_*','RESULT.json')]:
  candidates=[p/file for p in R.glob(pattern) if (p/file).exists()]
  assert candidates and load(max(candidates,key=lambda p:p.stat().st_mtime)).get('summary',load(max(candidates,key=lambda p:p.stat().st_mtime))).get('all_passed'),('Latest gate not passed',pattern)
 h=health();assert h['profile_digests']==load(P/'MODEL_IDENTITY_BEFORE.json')['profile_digests']
 source_before=source_identity();write('SOURCE_SNAPSHOT_BEFORE.json',source_before)
 freeze={str(p.resolve()):sha(p) for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.sqlite-wal','.sqlite-shm'}}
 for name in ['replay_planners.py','continue_execution.py','run_common.py','reference_grader.py','analyze_full.py','reconcile_saved_scores.py','start_candidate.py','serve_api.py','run_acceptance.py','run_context_acceptance.py','run_owner_api_acceptance.py','EVALUATION_PROTOCOL.json','EVALUATION_GATE_ADDENDUM.json','EVALUATION_LINEAGE.json','OWNER50_MAPPING.json','OWNER50_REVIEW_FINAL.json']:
  freeze[str((R/name).resolve())]=sha(R/name)
 # Model code, adapter weights, retained labels and source jobs were already
 # frozen by the parent. Their hashes remain part of this run's provenance.
 parent_freeze=load(P/'EXECUTION_FREEZE_V2.json');assert all(sha(p)==v for p,v in parent_freeze.items())
 for folder in [R.parent/'r121_context_planner_training_20261022/train02/adapter',P/'training_v2/train01/adapter',Path('D:/CodexTraining/psu-r121-20261022/model')]:
  for path in folder.rglob('*'):
   if path.is_file():freeze[str(path.resolve())]=sha(path)
 assert sha(P/'training_v2/train01/adapter/adapter_model.safetensors')==h['profiles']['new']
 assert sha(R.parent/'r121_context_planner_training_20261022/train02/adapter/adapter_model.safetensors')==h['profiles']['retained']
 freeze.update(parent_freeze);write('EXECUTION_FREEZE_R130.json',freeze);write('MODEL_IDENTITY_BEFORE.json',h)
 while True:
  try:parent_progress=load(P/'three_arm02/PROGRESS.json')
  except (FileNotFoundError,json.JSONDecodeError):parent_progress={'being_written':True}
  state('waiting_for_existing_330_raw_planner_outputs',parent_progress=parent_progress,no_duplicate_raw_inference=True)
  try:ready=load(P/'three_arm02/SUMMARY.json')
  except (FileNotFoundError,json.JSONDecodeError):ready={}
  if ready.get('complete'):
   assert ready['coverage_keys_identical'] and ready['source_unchanged'];break
  time.sleep(30)
 assert all(sha(p)==v for p,v in freeze.items()),'Source/model/input changed before replay'
 assert source_identity()==source_before,'Logical source changed before replay'
 run('replay_planners.py') # waits for PLANNER_ADJUDICATION_R130.json from agent
 paired=load(R/'paired_replay03/COMPLETE.json');decision=load(R/'PLANNER_ADJUDICATION_R130.json')
 assert paired['complete'] and decision['source_execution_review_complete'] and decision['profile'] in {'new','retained'}
 assert all(sha(p)==v for p,v in freeze.items()),'Source/model/input changed before final readiness'
 assert source_identity()==source_before,'Logical source changed during replay'
 env=os.environ.copy();env.update(PSU_PLANNER_PROFILE=decision['profile'],R130_PORT='13024')
 run('start_candidate.py',env=env);run('run_acceptance.py');run('run_context_acceptance.py');run('run_owner_api_acceptance.py')
 api=load(R/'PROCESS.json');output=Path(api['output'])
 assert load(output/'COMPLETE.json')['completed'] and not load(output/'COMPLETE.json')['http_errors'] and load(output/'CONTEXT_COMPLETE.json')['all_passed'] and load(output/'OWNER50_API_COMPLETE.json')['all_passed']
 write('READINESS.json',{'ready_for_authorized_full_test':True,'selected_profile':decision['profile'],'api_output':str(output),'scope_review_complete':True,'accuracy_not_inferred_from_readiness':True})
 master=R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl';jobs=[json.loads(s) for s in master.read_text('utf8').splitlines()]
 assert len(jobs)==len({x['key'] for x in jobs})==20554 and sum(len(x['entries']) for x in jobs)==55811
 assert not (R/'full01').exists(),'Never duplicate a full run'
 assert source_identity()==source_before,'Source changed during API readiness'
 run('run_common.py',['--workers','2','--tag','full01','--jobs',master],env=env)
 assert all(sha(p)==v for p,v in freeze.items()),'Frozen system or original input changed during full test'
 after=health();assert after['profile_digests']==h['profile_digests'] and after['profiles']==h['profiles'];write('MODEL_IDENTITY_AFTER.json',after)
 source_after=source_identity();assert source_after==source_before,'Logical source changed during full test';write('SOURCE_SNAPSHOT_AFTER.json',source_after)
 run('analyze_full.py');run('reconcile_saved_scores.py')
 state('full_coverage_complete_root_cause_review_required',full_test_complete=True,analysis_complete=False,selected_profile=decision['profile'])
except BaseException as exc:
 name='CONTROLLER_FAILURE_'+str(time.time_ns())+'.json';write(name,{'error':repr(exc),'traceback':traceback.format_exc()});state('controller_failed',failure_record=name,error=repr(exc));raise
