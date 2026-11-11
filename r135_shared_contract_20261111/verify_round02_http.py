"""Natural serial chat requests for repaired repetition and numeric edition scope."""
import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;url='http://127.0.0.1:8143/'
health=json.load(urllib.request.urlopen(url+'health',timeout=5));assert health['runtime']['version']=='R135-Shared-contract-round02'
out=R/('round02_http_'+str(time.time_ns()));out.mkdir();checks={};rows=[]
cases=[('PC นักศึกษา PSU ราคาเท่าไหร่; PC นักศึกษา PSU ราคาเท่าไหร่','0 บาท',False),('TEKKEN 8 ปุ่มอะไร','',True),('TEKKEN 9 ปุ่มอะไร','',False),('TEKKEN 8 มีให้เล่นไหม','TEKKEN 8',True),('TEKKEN 9 มีให้เล่นไหม','',False),('TEKKEN 9 คือเกมอะไร','',False),('tekken9 controls','',False)]
for n,(q,expected,positive) in enumerate(cases):
 body={'question':q,'locale':'th','client_session_id':'round02-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 req=urllib.request.Request(url+'api/chat',data=json.dumps(body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
 started=time.perf_counter()
 with urllib.request.urlopen(req,timeout=45) as response:result=json.load(response)
 rows.append({'q':q,'response':result,'wall_seconds':time.perf_counter()-started})
 checks[f'ok_{n}']=result.get('ok') is True
 answer=result.get('answer','');checks[f'expected_{n}']=expected in answer
 # Unknown editions must not receive the source facts or text of TEKKEN 8.
 if n>=2 and not positive:checks[f'wrong_edition_not_delivered_{n}']='TEKKEN 8' not in answer and 'PS5' not in answer
 if n==1:checks['normal_control_answer_nonempty']=bool(answer) and ('12' in answer or 'ปุ่ม' in answer)
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'scope':'serial natural HTTP output checks, positives and wrong numeric edition negatives; not full semantic or model acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
