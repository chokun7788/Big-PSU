"""One full common/ON run, then reproducible offline analysis of its own logs."""
import json,os,subprocess,sys,time,traceback
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parent
def status(phase,**details):
 row={'updated_at_utc':datetime.now(timezone.utc).isoformat(),'supervisor_pid':os.getpid(),'phase':phase,**details};p=R/'SUPERVISOR_STATUS.new.json';p.write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf8');os.replace(p,R/'SUPERVISOR_STATUS.json')
 with (R/'SUPERVISOR_EVENTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
def run(name,args):
 with (R/(name+'.out.log')).open('x',encoding='utf8') as out,(R/(name+'.err.log')).open('x',encoding='utf8') as err:
  p=subprocess.Popen([sys.executable,'-B','-X','utf8',*args],cwd=R,stdout=out,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0));status(name,child_pid=p.pid,running=True)
  while p.poll() is None:
   time.sleep(10)
  status(name,child_pid=p.pid,exit_code=p.returncode,running=False)
  if p.returncode:raise RuntimeError(name+' failed with exit '+str(p.returncode)+'; inspect preserved '+name+' logs')
def main():
 assert not (R/'FULL_TEST_COMPLETE.json').exists(),'Completed run preserved'
 try:
  if (R/'PREFLIGHT_RESULT.json').exists():
   pre=json.loads((R/'PREFLIGHT_RESULT.json').read_text('utf8'));assert pre['passed'] and pre['real_generation_verified'] and pre['source_frozen_hashes_verified'] and pre['database_matches_source']
   status('preflight_verified',running=False,reused_verified_preflight=True)
  else:run('preflight',[str(R/'preflight.py')])
  run('full_common_on',[str(R/'run_common.py'),'--workers','2','--tag','full01'])
  run('sessions_guards',[str(R/'sessions_guards.py')])
  run('analyze_final',[str(R/'analyze.py'),'--run','full01','--tag','FINAL'])
  run('deep_analysis',[str(R/'deep_analysis.py')])
  analysis=json.loads((R/'ANALYSIS_FINAL.json').read_text('utf8'));assert analysis['complete'] and analysis['actual_model_inference_confirmed']
  complete={'complete':True,'format':'common','llm_enabled':True,'requests':analysis['totals']['requests'],'grades':analysis['totals']['grades'],'actual_model_inference_confirmed':True,'preservation':analysis['preservation'],'completed_at_utc':datetime.now(timezone.utc).isoformat(),'report':str(R/'REPORT_FINAL_TH.md'),'deep_analysis':str(R/'DEEP_FAILURE_ANALYSIS_TH.md')}
  with (R/'FULL_TEST_COMPLETE.json').open('x',encoding='utf8') as f:json.dump(complete,f,ensure_ascii=False,indent=2)
  status('complete',running=False,**complete)
 except BaseException as e:
  with (R/'SUPERVISOR_FAILURE.txt').open('x',encoding='utf8') as f:f.write(traceback.format_exc())
  status('failed',running=False,error=str(e),complete=False)
  raise
if __name__=='__main__':main()
