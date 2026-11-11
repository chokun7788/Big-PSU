import json,time,uuid,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;url='http://127.0.0.1:8143/'
health=json.load(urllib.request.urlopen(url+'health',timeout=5));assert health['runtime']['version']=='R135-Shared-contract-round02'
out=R/('shared_http_'+str(time.time_ns()));out.mkdir();rows=[];checks={}
qs=['มีเกมอะไรบ้าง; PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองยังไง','PC นักศึกษา PSU ราคาเท่าไหร่; จองยังไง แล้วมีเกมอะไรบ้าง','มีเกมอะไรบ้าง and also PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองยังไง']
for n,q in enumerate(qs):
 data={'question':q,'locale':'th','client_session_id':'shared-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 req=urllib.request.Request(url+'api/chat',data=json.dumps(data,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
 started=time.perf_counter()
 with urllib.request.urlopen(req,timeout=45) as response:result=json.load(response)
 rows.append({'q':q,'response':result,'wall_seconds':time.perf_counter()-started});answer=result.get('answer','')
 checks[f'http_ok_{n}']=result.get('ok') is True
 checks[f'price_{n}']='0 บาท' in answer
 checks[f'booking_{n}']='สลิป' in answer
 checks[f'games_{n}']='TEKKEN 8' in answer or 'Nintendo Switch' in answer
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'scope':'3 sequential natural chat HTTP requests on isolated candidate; not full semantic accuracy or model admission proof'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report},ensure_ascii=False));assert report['all_passed']
