"""One actual HTTP/model context case, independent from mocked source checks."""
import json,sqlite3,time,urllib.request,uuid
from verification_support import R
base='http://127.0.0.1:8145/'
health=json.load(urllib.request.urlopen(base+'health',timeout=5));assert health['runtime']['version']=='R135-Model-first-trial02'
q='นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง'
payload={'question':q,'locale':'th','client_session_id':'context-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
req=urllib.request.Request(base+'api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST');started=time.perf_counter()
with urllib.request.urlopen(req,timeout=65) as response:result=json.load(response)
out=R/('http_context_'+str(time.time_ns()));out.mkdir()
(out/'RESPONSE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
row=None;trace_deadline=time.monotonic()+5
while row is None and time.monotonic()<trace_deadline:
 conn=sqlite3.connect((R/'preview/runtime/logs/transcripts.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
 row=conn.execute("select metadata_json from chat_messages where session_id=? and role='assistant' order by id desc limit 1",(result['session_id'],)).fetchone();conn.close()
 if row is None:time.sleep(.1)
artifact=json.loads(row[0])['decision_artifact'] if row else {};audit=artifact.get('model_first',{});c=artifact.get('execution_contract',{});answer=result.get('answer','')
checks={'http_ok':result.get('ok') is True,'actual_model_completed':audit.get('transport_completed') is True,'two_model_tasks':len(audit.get('validated_needs',[]))==2,'source_zero_price':'0 บาท' in answer,'booking_steps':'สลิป' in answer,'currentness_caveat_retained':'ยังไม่ยืนยันวันเริ่ม' in answer,'no_false_unplanned_notice':'ส่วนที่ยังไม่มีแผนประมวลผล' not in answer,'no_false_duration_notice':'ยังยืนยันการใช้เงื่อนไข' not in answer,'parent_tasks_preserved':len(c.get('request_plan',{}).get('tasks',[]))==2}
report={'seconds':time.perf_counter()-started,'checks':checks,'all_passed':all(checks.values()),'scope':'one development HTTP price/booking request; not semantic accuracy or full acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'ARTIFACT.json').write_text(json.dumps(artifact,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
