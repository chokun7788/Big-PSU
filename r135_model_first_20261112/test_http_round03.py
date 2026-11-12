"""Two serial real HTTP requests after final source/guard fixes."""
import json,sqlite3,time,urllib.request,uuid
from verification_support import R
base='http://127.0.0.1:8145/';health=json.load(urllib.request.urlopen(base+'health',timeout=5));assert health['runtime']['version']=='R135-Model-first-trial03'
cases=[('two_prices','นักศึกษา PSU เล่น PC 30 นาทีราคาเท่าไหร่ และบุคคลทั่วไปเล่น PS5 30 นาทีราคาเท่าไหร่'),('conflict','Tekken 8 อยู่โซนไหน แล้ว Tekken 8 มีให้เล่นบนเครื่องอะไรบ้าง')]
out=R/('http_round03_'+str(time.time_ns()));out.mkdir();rows=[]
for name,q in cases:
 payload={'question':q,'locale':'th','client_session_id':'round03-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 req=urllib.request.Request(base+'api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST');start=time.perf_counter()
 with urllib.request.urlopen(req,timeout=65) as response:result=json.load(response)
 row=None;deadline=time.monotonic()+5
 while row is None and time.monotonic()<deadline:
  c=sqlite3.connect((R/'preview/runtime/logs/transcripts.sqlite').resolve().as_uri()+'?mode=ro',uri=True);row=c.execute("select metadata_json from chat_messages where session_id=? and role='assistant' order by id desc limit 1",(result['session_id'],)).fetchone();c.close()
  if row is None:time.sleep(.1)
 a=json.loads(row[0])['decision_artifact'] if row else {};audit=a.get('model_first',{});contract=a.get('execution_contract',{});answer=result.get('answer','')
 checks={'http_ok':result.get('ok') is True,'actual_base_model':audit.get('transport_completed') is True and audit.get('returned_provenance',{}).get('effective_profile')=='base','no_second_model_call':audit.get('plan_review',{}).get('attempted') is False,'two_tasks_preserved':len(contract.get('tasks',[]))==2}
 if name=='two_prices':
  durations=[x for x in contract.get('verifier_result',{}).get('constraint_coverage',{}).get('constraints',[]) if x['kind']=='duration']
  checks.update(pc_price_retained='0 บาท' in answer,no_false_booking_notice='ส่วนที่ยังไม่มีแผนประมวลผล' not in answer,second_duration_not_borrowed=len(durations)==2 and durations[1]['status']=='review_required',unverified_condition_visible='ยังยืนยันการใช้เงื่อนไข' in answer)
 else:
  conflict=any(n.get('ambiguity')=='model_plan_conflict' for n in audit.get('validated_needs',[]))
  checks.update(zone_retained='PC Zone' in answer,model_error_not_missing_data=('โมเดลยังตีความส่วนนี้ไม่ผ่านการตรวจ' in answer and 'ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม' not in answer) if conflict else 'PC #01-#02' in answer,failed_part_not_delivered=not any(e.get('claims') for e,l in zip(contract.get('executor_results',[]),contract.get('tasks',[])) if l.get('terminal_state')=='invalid_plan'))
 rows.append({'id':name,'question':q,'seconds':time.perf_counter()-start,'checks':checks,'answer':answer,'response':result,'artifact':a});(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'id':name,'checks':checks,'seconds':rows[-1]['seconds'],'answer':answer},ensure_ascii=False),flush=True)
report={'requests':len(rows),'all_passed':all(all(x['checks'].values()) for x in rows),'cases':[{k:r[k] for k in ['id','seconds','checks']} for r in rows],'scope':'two final guard/source HTTP cases; not an intent accuracy score; model conflict is a known unresolved intent failure'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
