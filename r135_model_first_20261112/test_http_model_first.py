"""One sequential actual HTTP/model request against this candidate only."""
import json,time,urllib.request,uuid
from verification_support import R
base='http://127.0.0.1:8145/'
health=json.load(urllib.request.urlopen(base+'health',timeout=5))
assert health['runtime']['version']=='R135-Model-first-trial01'
q='Tekken 8 อยู่โซนไหน แล้ว Tekken 8 มีให้เล่นบนเครื่องอะไรบ้าง'
payload={'question':q,'locale':'th','client_session_id':'model-first-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
req=urllib.request.Request(base+'api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
started=time.perf_counter()
with urllib.request.urlopen(req,timeout=65) as response:result=json.load(response)
out=R/('http_model_first_'+str(time.time_ns()));out.mkdir()
(out/'RESPONSE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
checks={'http_ok':result.get('ok') is True,'zones_delivered':'PC Zone' in result.get('answer',''),'services_delivered':'PC #01-#02' in result.get('answer',''),'not_live_disclaimer':'ไม่ใช่สถานะว่าเครื่องว่าง' in result.get('answer','')}
report={'seconds':time.perf_counter()-started,'checks':checks,'all_passed':all(checks.values()),'scope':'one focused HTTP delivery; inspect persisted planner trace separately, not semantic accuracy'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
