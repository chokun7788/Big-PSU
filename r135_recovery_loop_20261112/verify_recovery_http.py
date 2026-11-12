"""Five serial live chat requests on the isolated recovery candidate."""
import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;URL='http://127.0.0.1:8144/'
health=json.load(urllib.request.urlopen(URL+'health',timeout=5));assert health['runtime']['version']=='R135-Recovery-loop02'
out=R/('recovery_http_'+str(time.time_ns()));out.mkdir();rows=[];checks={}
cases=[('นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท','th'),('PSU Student plays PC for 30 minutes, how much does it cost?','en'),('นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง','th'),('นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท; Andaman Hotel อยู่ที่ไหน','th'),('PC นักศึกษา PSU ราคาเท่าไหร่','th')]
for n,(q,locale) in enumerate(cases):
 body={'question':q,'locale':locale,'client_session_id':'recovery-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 req=urllib.request.Request(URL+'api/chat',data=json.dumps(body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST');started=time.perf_counter()
 with urllib.request.urlopen(req,timeout=45) as response:result=json.load(response)
 answer=result.get('answer','');rows.append({'question':q,'response':result,'wall_seconds':time.perf_counter()-started})
 checks[f'ok_{n}']=result.get('ok') is True
 checks[f'positive_price_{n}']='0 บาท' in answer or '0 THB' in answer
 checks[f'no_false_duration_notice_{n}']='ยังยืนยันการใช้เงื่อนไขต่อไปนี้' not in answer and 'Application of these requested constraints remains unverified' not in answer
 checks[f'authority_caveat_retained_{n}']='2026-10-20' in answer
 if n==2:checks['booking_survives']='สลิป' in answer
 if n==3:checks['unknown_sibling_not_complete']='partial' in result.get('mode','')
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'scope':'sequential natural HTTP candidate chat; not model availability, authority or broad semantic acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
