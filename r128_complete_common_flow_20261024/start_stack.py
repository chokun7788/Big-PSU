"""Start or reuse the verified local R128 preview without replacing other services."""
import json,os,socket,subprocess,sys,time,urllib.error,urllib.request,webbrowser
from pathlib import Path
R=Path(__file__).resolve().parent
def health(port):
 try:
  with urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=3) as f:return json.load(f)
 except (OSError,ValueError):return None
def available(port):
 with socket.socket() as s:
  try:s.bind(('127.0.0.1',port));return True
  except OSError:return False
def wait_for(port,condition,seconds):
 deadline=time.monotonic()+seconds
 while time.monotonic()<deadline:
  data=health(port)
  if data and condition(data):return data
  time.sleep(1)
 raise RuntimeError(f'Service {port} is not ready. Inspect R128 PROCESS.json / MODEL_PROCESS.json and their logs.')
model=health(12421)
if model and model.get('serving_protocol')!='r128-bounded-context-v1':raise RuntimeError('Port 12421 has another model service. Keep it intact; select a free port/configuration before starting R128.')
if not model:
 if not available(12421):raise RuntimeError('Port 12421 is occupied by a service that is not ready; no process was stopped.')
 print('Loading the saved model and adapter; first startup can take several minutes.',flush=True)
 subprocess.run([sys.executable,str(R/'start_model.py')],check=True)
 model=wait_for(12421,lambda h:h.get('serving_protocol')=='r128-bounded-context-v1',300)
if model.get('adapter_sha256')!='e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8':raise RuntimeError('Unexpected saved adapter identity; inspect model manifest.')
api=health(12422)
if api and api.get('runtime',{}).get('version')!='R128':raise RuntimeError('Port 12422 is running another chat version; no process was stopped.')
if not api:
 if not available(12422):raise RuntimeError('Port 12422 is occupied; inspect its current process before starting R128.')
 subprocess.run([sys.executable,str(R/'start_candidate.py')],check=True,env={**os.environ,'R128_PORT':'12422'})
 api=wait_for(12422,lambda h:h.get('runtime',{}).get('version')=='R128',60)
print('R128 common draft preview ready: http://127.0.0.1:12422/',flush=True)
if '--no-open' not in sys.argv:webbrowser.open('http://127.0.0.1:12422/')
