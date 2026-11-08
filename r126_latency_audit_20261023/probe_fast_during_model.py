import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(c['output']);before_progress=json.loads((OUT/'PROGRESS.json').read_text('utf8'))
payload={'question':'วันที่ 28 ตุลาคมเปิดไหม','locale':'th','debug':True,'experimental_rag_fallback':True,'client_session_id':'concurrent-fast-'+uuid.uuid4().hex}
request=urllib.request.Request(c['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'});started=time.time();before=time.perf_counter()
with urllib.request.urlopen(request,timeout=30) as r:body=json.load(r)
row={'scenario':'deterministic_calendar_while_sequential_model_test_in_progress','started_at':started,'wall_sec':time.perf_counter()-before,'progress_at_dispatch':before_progress,'response':body}
(OUT/'CONCURRENT_FAST.json').write_text(json.dumps(row,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'seconds':row['wall_sec'],'answer':body['answer'],'progress':before_progress},ensure_ascii=False))
