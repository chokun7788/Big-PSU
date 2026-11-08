import json,os,subprocess,sys,time,traceback,urllib.request
from pathlib import Path
import psutil
R=Path(__file__).resolve().parent;OUT=R/'execution01';OUT.mkdir(exist_ok=False);server=None;handles=[]
def status(phase,**kw):
 value={'phase':phase,'pid':os.getpid(),'updated_at':time.time(),**kw}
 with (OUT/'STATUS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(value)+'\n')
 print(json.dumps(value),flush=True)
def spawn(name,python,script,*args):
 log=(OUT/(name+'_STDOUT.log')).open('x',encoding='utf8');err=(OUT/(name+'_STDERR.log')).open('x',encoding='utf8');handles.extend([log,err])
 return subprocess.Popen([python,'-B','-X','utf8',str(R/script),*args],cwd=R.parent,stdout=log,stderr=err,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
try:
 assert json.loads((R.parent/'r121_context_planner_training_20261022/train02/TRAINING_COMPLETE.json').read_text('utf8'))['complete']
 status('loading_same_trained_checkpoint')
 server=spawn('INFERENCE',sys.executable,'serve_planner.py','--output-name','inference01')
 for attempt in range(180):
  if server.poll() is not None:raise RuntimeError('Inference server exited')
  try:
   with urllib.request.urlopen('http://127.0.0.1:12121/health',timeout=2) as h:health=json.load(h)
   assert health['pid']==server.pid or server.pid in [p.pid for p in psutil.Process(health['pid']).parents()]
   old=json.loads((R.parent/'r121_context_planner_training_20261022/inference01/SERVER.json').read_text('utf8'));assert health['digests']==old['digests'] and health['adapter_sha256']==old['adapter_sha256'];break
  except (OSError,ValueError):time.sleep(2)
 else:raise RuntimeError('Inference startup timeout')
 status('api_comparison',same_weights_as_api01=True,grader_python=sys._base_executable)
 api=spawn('API',sys._base_executable,'run_api.py');assert api.wait()==0,'Development guard check failed'
 assert json.loads((R/'api01/TEST_COMPLETE.json').read_text('utf8'))['complete']
 status('measured_complete',requests_per_arm=8,production_installed=False)
 (OUT/'COMPLETE.json').write_text(json.dumps({'complete':True,'api_comparison_complete':True,'production_installed':False},indent=2),'utf8')
except BaseException as exc:
 (OUT/'FAILED.json').write_text(json.dumps({'error':repr(exc),'traceback':traceback.format_exc()},indent=2),'utf8');status('failed',error=repr(exc));raise
finally:
 if server is not None and server.poll() is None:
  try:children=psutil.Process(server.pid).children(recursive=True)
  except psutil.NoSuchProcess:children=[]
  for child in reversed(children):
   try:child.terminate()
   except psutil.NoSuchProcess:pass
  server.terminate()
  try:server.wait(timeout=15)
  except subprocess.TimeoutExpired:server.kill();server.wait(timeout=5)
 for handle in handles:handle.close()
