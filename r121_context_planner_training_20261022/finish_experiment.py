"""Finish this experiment after the already-running trainer releases the GPU."""
import hashlib,json,os,socket,subprocess,sys,time,traceback,urllib.request
from pathlib import Path
import psutil
R=Path(__file__).resolve().parent;OUT=R/'execution01';OUT.mkdir(exist_ok=False)
TRAIN_PID=60584;server=None;handles=[]
def status(phase,**kw):
 record={'phase':phase,'pid':os.getpid(),'updated_at':time.time(),**kw}
 # Append-only telemetry avoids replacement/file-share races on Windows.
 with (OUT/'STATUS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
 print(json.dumps(record,ensure_ascii=False),flush=True)
def read(p):return json.loads(p.read_text('utf8'))
def spawn(name,script):
 log=(OUT/(name+'_STDOUT.log')).open('x',encoding='utf8');err=(OUT/(name+'_STDERR.log')).open('x',encoding='utf8');handles.extend([log,err])
 return subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/script)],cwd=R.parent,stdout=log,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
try:
 status('waiting_for_training',trainer_pid=TRAIN_PID)
 try:trainer=psutil.Process(TRAIN_PID)
 except psutil.NoSuchProcess:trainer=None
 if trainer is not None:
  assert any('train_planner02.py' in x for x in trainer.cmdline()),'PID was reused'
  while trainer.is_running():
   try:
    if trainer.status()==psutil.STATUS_ZOMBIE:break
   except psutil.NoSuchProcess:break
   time.sleep(5)
 assert read(R/'train02/TRAINING_COMPLETE.json')['complete'],'Training stopped without completion'
 status('analyzing_saved_planner_results')
 analyzer=spawn('ANALYSIS','analyze_training.py');assert analyzer.wait()==0,'Planner analysis failed'
 with socket.socket() as sock:sock.bind(('127.0.0.1',12121))
 status('loading_inference_server')
 server=spawn('INFERENCE','serve_planner.py')
 for attempt in range(180):
  if server.poll() is not None:raise RuntimeError('Inference server stopped while loading')
  try:
   with urllib.request.urlopen('http://127.0.0.1:12121/health',timeout=2) as h:health=json.load(h)
   assert health['pid']==server.pid and health['training_complete_verified'];break
  except (OSError,ValueError):time.sleep(2)
 else:raise RuntimeError('Inference startup timeout')
 status('api_comparison',server_pid=server.pid,requests_per_arm=8)
 api=spawn('API','run_api_comparison.py');assert api.wait()==0,'API comparison failed; inspect preserved logs'
 assert read(R/'api01/TEST_COMPLETE.json')['complete']
 status('measured_complete',planner_questions=30,api_questions_per_arm=8,production_installed=False)
 (OUT/'COMPLETE.json').write_text(json.dumps({'complete':True,'planner_comparison_complete':True,'api_comparison_complete':True,'production_installed':False},indent=2),'utf8')
except BaseException as exc:
 (OUT/'FAILED.json').write_text(json.dumps({'error':repr(exc),'traceback':traceback.format_exc()},indent=2),'utf8');status('failed',error=repr(exc));raise
finally:
 if server is not None and server.poll() is None:
  server.terminate()
  try:server.wait(timeout=15)
  except subprocess.TimeoutExpired:server.kill();server.wait(timeout=5)
 for h in handles:h.close()
