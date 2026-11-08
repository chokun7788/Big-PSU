"""Resume after the rejected two-row harness pilot; reuse all valid evidence."""
import hashlib,json,os,subprocess,sys,time,traceback,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;START=time.time();PY=sys.executable
def load(p):return json.loads(Path(p).read_text('utf-8-sig'))
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(name,obj):
 p=R/name;t=p.with_name(p.name+'.new');t.write_text(json.dumps(obj,ensure_ascii=False,indent=2),'utf8');os.replace(t,p)
def state(phase,**kw):
 value={'controller_version':'r129-execution-v2','pid':os.getpid(),'phase':phase,'complete':False,'updated_at':time.time(),'elapsed_sec':time.time()-START,**kw};write('STATUS.json',value)
 with (R/'SUPERVISOR_V2_EVENTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(value,ensure_ascii=False)+'\n')
def run(script,args=(),env=None):
 with (R/(Path(script).stem+'.v2.stdout.log')).open('x',encoding='utf8') as out,(R/(Path(script).stem+'.v2.stderr.log')).open('x',encoding='utf8') as err:
  p=subprocess.Popen([PY,'-B','-u',str(R/script),*map(str,args)],cwd=R.parent,env=env,stdout=out,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  while p.poll() is None:state(Path(script).stem,child_pid=p.pid,script=str(R/script));time.sleep(15)
  assert p.returncode==0,(script,p.returncode)
def health():
 with urllib.request.urlopen('http://127.0.0.1:12921/health',timeout=5) as f:return json.load(f)
try:
 state('verifying_preserved_readiness_and_model')
 freeze=load(R/'EXECUTION_FREEZE.json');assert all(sha(p)==h for p,h in freeze.items()),'Frozen source or original experimental inputs changed'
 assert load(R/'training_v2/train01/TRAINING_COMPLETE.json')['complete'] and load(R/'MODEL_VERIFICATION.json')['all_passed']
 for pattern,name in [('verification_*','VERIFICATION.json'),('graph_verification_*','RESULT.json'),('gateway_verification_*','RESULT.json'),('comparison_verification_*','RESULT.json'),('extended_*','RESULTS.json'),('source_guard_verification_*','VERIFICATION.json'),('live_verification_*','VERIFICATION.json'),('harness_verification_*','RESULT.json')]:
  valid=[]
  for p in R.glob(pattern):
   if not (p/name).exists():continue
   result=load(p/name);summary=result.get('summary',result)
   if summary.get('all_passed'):valid.append(p/name)
  assert valid,('Missing gate',pattern)
 h=health();assert h['profile_digests']==load(R/'MODEL_IDENTITY_BEFORE.json')['profile_digests']
 for p in [R/'compare_planners_v2.py',R/'continue_execution.py',R/'analyze_full_v2.py',R/'verify_comparison_harness_v2.py',R/'EVALUATION_GATE_ADDENDUM.json']:freeze[str(p.resolve())]=sha(p)
 write('EXECUTION_FREEZE_V2.json',freeze)
 run('compare_planners_v2.py')
 paired=load(R/'three_arm02/SUMMARY.json');assert paired['complete'] and paired['coverage_keys_identical'] and paired['source_unchanged']
 decision=load(R/'PLANNER_ADJUDICATION.json');assert decision['source_execution_review_complete'];arm=decision['profile'];assert arm in {'new','retained'}
 assert all(sha(p)==h for p,h in freeze.items()),'Frozen source changed before final API readiness'
 env=os.environ.copy();env.update(PSU_PLANNER_PROFILE=arm,R129_PORT='12924')
 run('start_candidate.py',env=env);run('run_acceptance.py');run('run_context_acceptance.py')
 api=load(R/'PROCESS.json');a=load(Path(api['output'])/'COMPLETE.json');c=load(Path(api['output'])/'CONTEXT_COMPLETE.json');assert a['completed'] and not a['http_errors'] and c['all_passed']
 write('READINESS.json',{'ready_for_authorized_full_test':True,'profile':arm,'runtime_checks_passed':True,'actual_profile_identity_verified':True,'api_output':api['output'],'semantics_not_inferred_from_readiness_score':True,'no_production_deployment':True})
 master=R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl';jobs=[json.loads(s) for s in master.read_text('utf8').splitlines()];assert len(jobs)==len({j['key'] for j in jobs})==20554 and sum(len(j['entries']) for j in jobs)==55811
 assert not (R/'full01').exists(),'Never duplicate the full run'
 run('run_common.py',['--workers','2','--tag','full01','--jobs',master],env=env)
 assert all(sha(p)==h for p,h in freeze.items()),'Frozen system/input changed during full test'
 after=health();assert after['profiles']==h['profiles'] and after['profile_digests']==h['profile_digests'];write('MODEL_IDENTITY_AFTER.json',after)
 run('analyze_full_v2.py')
 state('full_test_complete_root_cause_review_required',full_test_complete=True,analysis_complete=False,selected_profile=arm,source_unchanged=True,model_identity_verified=True,report=str(R/'full_analysis/FINAL_REPORT_TH.md'))
except BaseException as exc:
 err={'error':repr(exc),'traceback':traceback.format_exc()};name='SUPERVISOR_V2_FAILED_'+str(time.time_ns())+'.json';write(name,err);state('failed',error=repr(exc),failure_record=name);raise
