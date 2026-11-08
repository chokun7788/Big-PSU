"""Run all lanes once against the same frozen system; preserve every result."""
import os,sys,json,subprocess,time,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;tag=sys.argv[1] if len(sys.argv)>1 else 'integrated01';T=R/tag;T.mkdir(exist_ok=False)
def manifest():return {p.relative_to(R/'system').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
frozen=json.loads((R/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'));inputs=json.loads((R/'FROZEN_INPUTS.json').read_text('utf8'))
def unchanged():return manifest()==frozen and all((R/path).is_file() and hashlib.sha256((R/path).read_bytes()).hexdigest()==h for path,h in inputs.items())
if not unchanged():raise SystemExit('Candidate/input differs from frozen version')
env=os.environ.copy();env.update(PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_MAX_CONCURRENCY='1',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'conversation.sqlite'))
lanes=[('model_readiness_lane.py','model_readiness'),('test_r102_contracts.py','new_contracts'),('test_contract_flow.py','retained_contracts'),('flow_contracts.py','retained_flow'),
 ('test_all_categories.py','owner_24'),('test_semantic_flow.py','semantic_protocol'),('test_live_bindings.py','simulated_live'),
 ('test_published.py','published_profiles'),('test_conflicts.py','typed_conflicts'),('test_existing_fixture.py','rental'),
 ('test_existing_competition_fixture.py','competition'),('test_flow_v2.py','retained_v2'),('test_task_matrix.py','task_matrix'),
 ('test_http_contracts.py','actual_http'),('test_real_planner.py','real_new_game'),('run_acceptance.py','r97_acceptance'),
 ('live_integration_lane.py','real_live'),('run_common.py','retained_holdout192')]
rows=[];started=time.perf_counter();status={'status':'running','run_id':tag,'source_unchanged':True,'lanes_complete':0,'lanes_total':len(lanes)+1}
def save():
 (T/'STATUS.json').write_text(json.dumps({**status,'elapsed_sec':round(time.perf_counter()-started,2),'lanes':rows},ensure_ascii=False,indent=2),'utf8')
save()
for script,name in lanes+[('run_common.py','retained_91')]:
 if not unchanged():status.update(status='invalid_source_changed',source_unchanged=False);save();raise SystemExit('Source/input changed during integrated batch')
 lane_tag=tag+'_'+name;status.update(current_lane=name);save();log=T/(name+'.log')
 args=[sys.executable,'-B','-X','utf8',str(R/script),lane_tag]
 if script=='run_common.py':args=[sys.executable,'-B','-X','utf8',str(R/script),'--workers','2','--tag',lane_tag,'--jobs',str(R/'RETAINED_HOLDOUT_JOBS.jsonl') if name=='retained_holdout192' else str(R.parent/'r98_flow_v2_implementation_20261019/FOCUSED_JOBS.jsonl')]
 print('Starting',name,flush=True);t=time.perf_counter()
 with log.open('x',encoding='utf8') as out:
  result=subprocess.run(args,cwd=R.parent,env=env,stdout=out,stderr=subprocess.STDOUT)
 path=R/'verification'/lane_tag/'SUMMARY.json'
 if script=='run_common.py':path=R/lane_tag/'PROGRESS.json'
 summary=json.loads(path.read_text('utf8')) if path.exists() else {}
 rows.append({'lane':name,'script':script,'tag':lane_tag,'exit_code':result.returncode,'elapsed_sec':round(time.perf_counter()-t,2),
  'summary_path':str(path.relative_to(R)),'count':summary.get('count',summary.get('total')),'passed':summary.get('passed',summary.get('raw_passed')),
  'failed':summary.get('failed',[]),'exceptions':summary.get('exceptions',0),'integration_blocked':summary.get('integration_blocked',False)})
 status.update(lanes_complete=len(rows),source_unchanged=unchanged());save();print('Finished',name,result.returncode,flush=True)
status.update(status='complete_with_failures' if any(x['exit_code'] for x in rows) else 'complete',current_lane=None,source_unchanged=unchanged())
save();(T/'BATCH_COMPLETE.json').write_text(json.dumps({**status,'lanes':rows,'elapsed_sec':time.perf_counter()-started,'all_lanes_executed':len(rows)==len(lanes)+1,'large_20554_test_executed':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in status.items() if k!='lanes'},ensure_ascii=False));sys.exit(any(x['exit_code'] for x in rows) or not status['source_unchanged'])
