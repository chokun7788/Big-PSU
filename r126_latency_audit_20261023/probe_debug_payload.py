import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));rows=[]
for debug in [False,True]:
 payload={'question':'มีเกมอะไรมั่ง','locale':'th','debug':debug,'experimental_rag_fallback':True,'client_session_id':'debug-audit-'+uuid.uuid4().hex};req=urllib.request.Request(c['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'});before=time.perf_counter()
 with urllib.request.urlopen(req,timeout=20) as response:
  headers=time.perf_counter();raw=response.read();read_done=time.perf_counter()
 data=json.loads(raw);done=time.perf_counter()
 rows.append({'debug':debug,'response_bytes':len(raw),'wall_sec':done-before,'until_headers_sec':headers-before,'body_read_sec':read_done-headers,'client_json_parse_sec':done-read_done,'answer':data['answer']})
out={'rows':rows,'answers_identical':rows[0]['answer']==rows[1]['answer'],'not_a_browser_paint_benchmark':True}
(R/'DEBUG_PAYLOAD_PROBE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8');print(json.dumps([{k:v for k,v in r.items() if k!='answer'} for r in rows],indent=2))
