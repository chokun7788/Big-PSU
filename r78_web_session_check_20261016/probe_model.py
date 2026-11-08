import json,os,time,urllib.request,urllib.error
from pathlib import Path
B=Path(__file__).resolve().parent
base=os.getenv('OLLAMA_URL','http://127.0.0.1:11434').rstrip('/')
# Local configured service only. No download, fallback host or alternate channel.
from urllib.parse import urlparse
p=urlparse(base)
if p.scheme not in {'http','https'} or p.hostname not in {'127.0.0.1','localhost','::1'}:raise SystemExit('Configured model endpoint is not loopback; not probed')
row={'endpoint':base+'/api/tags','transport_ok':False,'generation_verified':False};t=time.perf_counter()
try:
 with urllib.request.urlopen(row['endpoint'],timeout=3) as r:row.update(transport_ok=True,http_status=r.status,body=json.loads(r.read()))
except Exception as e:row.update(error_type=type(e).__name__,error=str(e))
row['elapsed_ms']=round((time.perf_counter()-t)*1000,2)
with (B/'MODEL_PREFLIGHT.json').open('x',encoding='utf8') as f:json.dump(row,f,ensure_ascii=False,indent=2)
print(json.dumps(row,ensure_ascii=False))