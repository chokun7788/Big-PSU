import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;cfg=json.loads((R/'LIVE_API_PROCESS.json').read_text('utf8'));OUT=Path(cfg['output'])
for attempt in range(35):
 try:
  with urllib.request.urlopen(cfg['url']+'/health',timeout=2) as response:health=json.load(response)
  break
 except OSError:
  if attempt==34:raise
  time.sleep(1)
assert health['runtime']['profile']=='r125-date-context-live'
rows=[];sid='r125-activation-'+uuid.uuid4().hex;last=None
for q in ['วันที่ 26 ตุลาเปิดไหม','วันที่15เปิดไหม','เดือน11']:
 body={'question':q,'locale':'th','debug':True,'client_session_id':sid,'client_turn_id':'t-'+uuid.uuid4().hex,'last_seen_response_id':last,'experimental_rag_fallback':True}
 before=time.perf_counter();req=urllib.request.Request(cfg['url']+'/api/chat',json.dumps(body,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=40) as response:r=json.load(response)
 last=r['request_id'];rows.append({'question':q,'wall_sec':time.perf_counter()-before,'response':r})
checks={'active_port_12422':cfg['url'].endswith(':12422'),'runtime_r125':True,'oct26_monday_open':'วันจันทร์ที่ 26 ตุลาคม' in rows[0]['response']['answer'] and '13:00–16:00' in rows[0]['response']['answer'],'asks_month':'เดือนไหน' in rows[1]['response']['answer'],'month_reply_resumed':'15 พฤศจิกายน' in rows[2]['response']['answer']}
out={'all_passed':all(checks.values()),'checks':checks,'health':health,'rows':rows}
(OUT/'ACTIVATION_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'all_passed':out['all_passed'],'checks':checks,'latencies':[r['wall_sec'] for r in rows]},ensure_ascii=False));assert out['all_passed']
