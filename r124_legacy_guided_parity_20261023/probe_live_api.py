import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;config=json.loads((R/'LIVE_API_PROCESS.json').read_text('utf8'));OUT=Path(config['output'])
for i in range(10):
 try:
  with urllib.request.urlopen(config['url']+'/health',timeout=5) as r:health=json.load(r)
  break
 except OSError:
  if i==9:raise
  time.sleep(1)
assert health['runtime']['profile']=='r124-legacy-guided-live'
assert health['runtime']['live_booking']['fetch_mode']=='wordpress' if 'live_booking' in health['runtime'] else True
(OUT/'HEALTH_VERIFIED.json').write_text(json.dumps(health,ensure_ascii=False,indent=2),'utf8')
rows=[]
for q in ['PC2 ว่างไหม','ตอนนี้ PC กับ VR ว่างไหม','PS5 #1 ว่างไหม']:
 data={'question':q,'locale':'th','debug':True,'client_session_id':'r124-live-'+uuid.uuid4().hex,'experimental_rag_fallback':True}
 req=urllib.request.Request(config['url']+'/api/chat',json.dumps(data,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
 start=time.monotonic()
 with urllib.request.urlopen(req,timeout=160) as r:response=json.load(r)
 rows.append({'question':q,'response':response,'wall_sec':time.monotonic()-start,'actual_provider_read_enabled':True})
 print(json.dumps({'question':q,'answer':response.get('answer'),'mode':response.get('mode'),'elapsed':time.monotonic()-start},ensure_ascii=False),flush=True)
(OUT/'REAL_LIVE_API_PROBE.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
