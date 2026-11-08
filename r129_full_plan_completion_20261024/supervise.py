"""Durable staged execution. Fails closed and never reruns a completed stage."""
import hashlib,json,os,subprocess,sys,time,traceback,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;PY=Path(sys.executable);GPU=Path('D:/CodexTraining/psu-r121-20261022/venv/Scripts/python.exe');START=time.time()
def load(p):return json.loads(Path(p).read_text('utf-8-sig'))
def write(n,v):
 p=R/n;tmp=p.with_name(p.name+'.new');tmp.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8');os.replace(tmp,p)
def status(phase,**kw):
 state={'phase':phase,'pid':os.getpid(),'updated_at':time.time(),'elapsed_sec':time.time()-START,'complete':False,**kw};write('STATUS.json',state)
 with (R/'SUPERVISOR_EVENTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(state,ensure_ascii=False)+'\n')
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def run(script,*,exe=PY,args=(),env=None):
 name=Path(script).stem;path=R/script
 with (R/(name+'.supervised.stdout.log')).open('x',encoding='utf8') as out,(R/(name+'.supervised.stderr.log')).open('x',encoding='utf8') as err:
  p=subprocess.Popen([str(exe),'-B','-u',str(path),*map(str,args)],cwd=R.parent,env=env,stdout=out,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  while p.poll() is None:
   status(name,child_pid=p.pid,script=str(path));time.sleep(15)
  assert p.returncode==0,(name,p.returncode)
 return True
def health(url):
 with urllib.request.urlopen(url+'/health',timeout=4) as f:return json.load(f)
def start_model():
 outname='model_'+str(time.time_ns());log=(R/(outname+'.log')).open('x',encoding='utf8')
 p=subprocess.Popen([str(GPU),'-B','-u',str(R/'serve_model.py'),'--port','12921','--output-name',outname],cwd=R.parent,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 write('MODEL_PROCESS.json',{'pid':p.pid,'script':str(R/'serve_model.py'),'url':'http://127.0.0.1:12921','output':str(R/outname)})
 for _ in range(60):
  assert p.poll() is None,'model_server_exited'
  try:
   h=health('http://127.0.0.1:12921')
   assert h['serving_protocol']=='r129-multi-profile-v2' and h['actual_weight_updates_verified'];return h
  except OSError:time.sleep(3)
 raise TimeoutError('model_server_startup_timeout')
def verify_actual_profiles():
 sys.path.insert(0,str(R/'system'))
 from app.knowledge.common.domain_flow.graph_protocol import messages
 from app.knowledge.common.domain_flow.understanding import schema
 from app.knowledge.common.domain_flow.model_gateway import digest
 x=json.loads((R/'training_v2/test.jsonl').read_text('utf8').splitlines()[0]);wire=messages(x['question']);sch=schema();probes=[]
 for arm in ['base','retained','new']:
  p={'model':'psu-r129:latest','stage':'context_understanding','planner_profile':arm,'messages':wire,'format':sch,'options':{'temperature':0,'num_predict':1},'request_timeout_sec':45}
  req=urllib.request.Request('http://127.0.0.1:12921/api/chat',data=json.dumps(p).encode(),headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=50) as f:result=json.load(f)
  prov=result['provenance'];assert prov['effective_profile']==arm and prov['effective_messages_sha256']==digest(wire) and prov['effective_schema_sha256']==digest(sch) and result['eval_count']<=1
  probes.append({'arm':arm,'provenance':prov,'eval_count':result['eval_count'],'one_token_identity_probe_not_accuracy':True})
 assert len({x['provenance']['profile_digest'] for x in probes})==3
 write('MODEL_VERIFICATION.json',{'all_passed':True,'actual_model_inferences':3,'probes':probes,'answer_accuracy_claimed':False})
try:
 status('waiting_for_reviewed_training_v2')
 train=R/'training_v2/train01'
 while not (train/'TRAINING_COMPLETE.json').exists():
  assert not (train/'FAILED.json').exists(),load(train/'FAILED.json') if (train/'FAILED.json').exists() else ''
  progress=load(train/'PROGRESS.json') if (train/'PROGRESS.json').exists() else {}
  if progress.get('pid'):
   # Windows process existence check. A stale PROGRESS file is not progress.
   check=subprocess.run(['powershell','-NoProfile','-Command',f"if (Get-Process -Id {int(progress['pid'])} -ErrorAction SilentlyContinue) {{ exit 0 }} else {{ exit 1 }}"],capture_output=True)
   assert check.returncode==0,'training_process_stopped_without_completion'
  status('waiting_for_reviewed_training_v2',training_progress=progress);time.sleep(15)
 proof=load(train/'OPTIMIZATION_PROOF.json');assert proof['actual_weight_updates'] and proof['base_parameter_hash_unchanged'] and proof['optimizer_steps']>0
 for p,h in load(train/'RUN_FREEZE.json').items():assert sha(p)==h,('training_input_changed',p)
 status('final_runtime_gates')
 for script in ['verify_retained_foundation.py','verify_graph_runtime.py','verify_gateway.py','verify_comparisons.py','verify_extended.py','verify_source_guards.py','verify_live.py','audit_source_data.py']:run(script)
 # Freeze code/data before actual model comparisons. No code changes are
 # allowed during comparison or full test; analysis writes outside system.
 freeze={str(p.resolve()):sha(p) for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.sqlite-wal','.sqlite-shm'}}
 for p in [R/'serve_model.py',R/'compare_planners.py',R/'EVALUATION_PROTOCOL.json',R/'EVALUATION_GATE_ADDENDUM.json',R/'run_common.py',R/'reference_grader.py',R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl']:freeze[str(p.resolve())]=sha(p)
 write('EXECUTION_FREEZE.json',freeze)
 status('starting_actual_multi_profile_model');h=start_model();write('MODEL_IDENTITY_BEFORE.json',h);verify_actual_profiles()
 run('compare_planners.py')
 comparison=load(R/'three_arm01/SUMMARY.json');assert comparison['complete'] and comparison['coverage_keys_identical'] and comparison['source_unchanged']
 arm=load(R/'three_arm01/SELECTED_PROFILE.json')['profile']
 if arm=='new':
  # Structural improvement is insufficient to install weights automatically.
  # The agent must review paired regressions and source-backed execution first.
  write('PLANNER_REVIEW_NEEDED.json',{'paired_results_ready':True,'provisional_profile':'new','human_user_approval_required':False,'agent_source_adjudication_required':True,'production_approvals_untouched':True})
  while not (R/'PLANNER_ADJUDICATION.json').exists():status('paired_results_ready_agent_review_required',paired_report=str(R/'three_arm01/SUMMARY.json'));time.sleep(15)
  decision=load(R/'PLANNER_ADJUDICATION.json');assert decision['source_execution_review_complete'] and decision['profile'] in {'new','retained'}
  arm=decision['profile']
 env=os.environ.copy();env.update(PSU_PLANNER_PROFILE=arm,R129_PORT='12924')
 assert all(sha(p)==v for p,v in freeze.items()),'source_changed_before_readiness'
 run('start_candidate.py',env=env)
 run('run_acceptance.py');run('run_context_acceptance.py')
 api=load(R/'PROCESS.json');accept=load(Path(api['output'])/'COMPLETE.json');context=load(Path(api['output'])/'CONTEXT_COMPLETE.json')
 assert accept['completed'] and not accept['http_errors'] and context.get('all_passed',context.get('completed',False)),'API_readiness_failed'
 write('READINESS.json',{'ready_for_authorized_full_test':True,'selected_profile':arm,'controlled_implementation_checks_only':True,'answer_accuracy_not_inferred_from_readiness':True,'api_output':api['output'],'actual_profile_identity_verified':True})
 # The user already authorized this full run. Verify expected coverage now;
 # never substitute a partial workload, legacy arm or LLM-OFF arm.
 jobs=R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl';xs=[json.loads(s) for s in jobs.read_text('utf8').splitlines()]
 assert len(xs)==len({x['key'] for x in xs})==20554 and sum(len(x['entries']) for x in xs)==55811
 assert not (R/'full01').exists(),'never_run_full_workload_twice'
 run('run_common.py',args=['--workers','2','--tag','full01','--jobs',jobs],env=env)
 assert all(sha(p)==v for p,v in freeze.items()),'source_or_inputs_changed_during_full_test'
 h2=health('http://127.0.0.1:12921');assert h2['profiles']==h['profiles'] and h2['profile_digests']==h['profile_digests'];write('MODEL_IDENTITY_AFTER.json',h2)
 run('analyze_full.py')
 status('full_test_complete_root_cause_review_required',full_test_complete=True,analysis_complete=False,selected_profile=arm,source_unchanged=True,model_identity_verified=True,report=str(R/'full_analysis/FINAL_REPORT_TH.md'))
except BaseException as exc:
 error={'error':repr(exc),'traceback':traceback.format_exc(),'elapsed_sec':time.time()-START};write('SUPERVISOR_FAILED.json',error);status('failed',error=repr(exc));raise
