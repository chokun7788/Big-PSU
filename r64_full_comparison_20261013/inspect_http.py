import json
from pathlib import Path
B=Path(__file__).resolve().parent
for folder in ('legacy_http','common_http','legacy_http_protocol_fixed'):
 p=B/folder/'RESULTS.jsonl'
 if not p.exists():continue
 print(folder)
 for line in p.open(encoding='utf-8'):
  r=json.loads(line)
  if not r['passed']:
   a=r.get('response',{})
   print(json.dumps({'q':r['question'],'fail':r['failures'],'mode':a.get('mode'),'answer':a.get('answer','')[:300],'error':a.get('error'),'sid':a.get('session_id')},ensure_ascii=False))
