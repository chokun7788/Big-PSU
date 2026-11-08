import json,time,urllib.request,uuid,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(c['output'])
for attempt in range(40):
 try:
  with urllib.request.urlopen(c['url']+'/health',timeout=2) as r:health=json.load(r)
  break
 except OSError:
  if attempt==39:raise
  time.sleep(1)
cases=[
 ('date_explicit','วันที่ 26 ตุลาเปิดไหม'),('date_english','Is the studio open on October 26?'),('date_paraphrase','ถ้าแวะไปวันจันทร์หน้าจะเข้าไปเล่นได้ช่วงไหนบ้าง'),('date_relative','อีกสามวันศูนย์เปิดไหม'),
 ('catalog_direct','มีเกมอะไรมั่ง'),('catalog_paraphrase','ที่ศูนย์มีอะไรให้เลือกเล่นบนเครื่องเพลย์ห้าบ้างครับ'),('catalog_filter','มีเกมไหนที่เล่นพร้อมกันสี่คนได้บ้าง'),
 ('equipment_direct','Nintendo Switch OLED คืออะไร'),('equipment_paraphrase','ถ้ามามือเปล่าตรงโซนคอมมีของอะไรเตรียมไว้ให้ใช้บ้าง'),('hardware','คอมของที่นี่ใช้การ์ดจอรุ่นอะไรครับ'),
 ('price_digits','บุคคลทั่วไป เล่น PC 1 ชั่วโมง เสียกี่บาท'),('price_words','ถ้าเป็นคนนอกอยากเล่นคอมสองชั่วโมงต้องเตรียมเงินเท่าไร'),('price_compare','เป็นนักศึกษา PSU อยากเทียบราคา PC กับ PS5 เล่นอย่างละสองชั่วโมง'),('price_multi_audience','นักศึกษา PSU 1 คนกับบุคคลทั่วไป 2 คน เล่น PC 2 ชั่วโมง รวมกี่บาท'),
 ('booking_direct','จองเครื่องทำยังไง'),('booking_paraphrase','ถ้าจะเข้าไปเล่นต้องเริ่มตรงไหนก่อนครับ'),('booking_compound','How to book Cockpit and what days is it open?'),('cancel','Can I cancel my booking? Please use verified information'),
 ('policy_direct','ถือขวดน้ำเข้าไปได้ไหม ไม่ได้ถามเรื่องกิน'),('policy_paraphrase','พาเพื่อนมานั่งดูเฉย ๆ ได้หรือเปล่า'),('policy_personal_device','Can I bring my own mouse?'),('documents','What ID does an external visitor need to use the studio?'),
 ('controls_direct','God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง'),('controls_paraphrase','ใน God of War Ragnarök ถ้าต้องการตีแรงบน PS5 ต้องกดตรงไหน'),('compound_controls_price','What are the 8 buttons in Tekken 8, and what is the PC price?'),
 ('rules','แข่ง VALORANT ถ้าทำผิดกฎจะโดนลงโทษอะไรบ้าง'),('ambiguous','แล้วอันนั้นล่ะ'),('unknown_game','Do you have Hades II?'),
 ('live_current','PC2 ว่างไหม'),('live_day','PC2 วันที่27 ว่างช่วงไหน'),('live_missing_scope','วันนี้มีตารางว่างรึเปล่า'),
 ('repeat_fast','วันที่ 26 ตุลาเปิดไหม'),('repeat_slow','Is the studio open on October 26?'),('repeat_compound','How to book Cockpit and what days is it open?')]
(OUT/'CASES.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2),'utf8');rows=[]
for i,(category,q) in enumerate(cases,1):
 before=time.perf_counter();started=time.time();payload={'question':q,'locale':'auto','debug':True,'experimental_rag_fallback':True,'client_session_id':'latency-'+uuid.uuid4().hex,'client_turn_id':'turn-'+uuid.uuid4().hex}
 request=urllib.request.Request(c['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(request,timeout=190) as response:body=json.load(response)
  row={'i':i,'category':category,'question':q,'started_at':started,'wall_sec':time.perf_counter()-before,'response':body}
 except Exception as e:row={'i':i,'category':category,'question':q,'started_at':started,'wall_sec':time.perf_counter()-before,'error':repr(e)}
 rows.append(row)
 with (OUT/'HTTP_RESULTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 (OUT/'PROGRESS.json').write_text(json.dumps({'completed':i,'total':len(cases),'latest':category,'elapsed_total':time.time()-rows[0]['started_at']},indent=2),'utf8')
 print(json.dumps({'i':i,'category':category,'seconds':round(row['wall_sec'],3),'answer':row.get('response',{}).get('answer','')[:120],'error':row.get('error')},ensure_ascii=False),flush=True)
 try:
  sample=subprocess.run(['nvidia-smi','--query-gpu=memory.used,memory.total,utilization.gpu,temperature.gpu','--format=csv,noheader'],capture_output=True,text=True,timeout=3)
  with (OUT/'GPU_AFTER_REQUEST.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'i':i,'measurement':'post_request_only_not_peak','gpu':sample.stdout.strip()})+'\n')
 except OSError:pass
(OUT/'COMPLETE.json').write_text(json.dumps({'complete':True,'requests':len(rows),'fresh_accuracy':None,'full_test':False},indent=2),'utf8')
