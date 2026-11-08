import json,sys,time,urllib.request,runpy
from pathlib import Path
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());port=sys.argv[1];run=sys.argv[2]
start=time.monotonic();last=''
while time.monotonic()-start<60:
 try:
  with urllib.request.urlopen('http://127.0.0.1:'+port+'/health',timeout=3) as response:health=json.load(response)
  workers=health.get('pipeline_workers',{})
  if health.get('ok') and (not workers.get('enabled') or (workers.get('workers') and all(x.get('alive') and x.get('ready') for x in workers['workers']))):break
 except Exception as exc:last=repr(exc)
 time.sleep(.5)
else:raise RuntimeError('Chatbot did not become ready: '+last)
with (R/(run+'_readiness.json')).open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
print('Server and pipeline workers are ready.',flush=True)

