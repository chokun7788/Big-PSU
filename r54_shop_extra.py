import sys,json,time,uuid,urllib.request,urllib.error
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r54_current_path.txt').read_text());URL='http://127.0.0.1:8093'
cases=[
 ('เปิดกี่โมง ปิดกี่โมง','th','hours'),('What are your opening hours?','en','hours'),
 ('วัน Maintenance ใช้บริการได้ไหม','th','hours'),('Is the studio open on maintenance days?','en','hours'),
 ('วันอาทิตย์เปิดไหม','th','hours'),('Where is the studio and when does it open?','en','multi_topic'),
 ('จองเครื่องยังไง ขอขั้นตอนทั้งหมด','th','booking_process'),('How do I book a PC? Give all the steps.','en','booking_process'),
 ('ชำระเงินยังไง จ่ายเงินสดได้ไหม','th','payment'),('Can I pay cash when I arrive?','en','payment'),
 ('มี 100 บาท เล่น PC ได้กี่รอบ บุคคลทั่วไป','th','budget'),('I have 100 THB and want to play PC as a general adult. How many sessions can I afford?','en','budget'),
 ('ปุ่มยิงกับรีโหลดใน CS2 คืออะไร','th','controls'),('How do I shoot and reload in CS2?','en','controls'),
 ('ขอปุ่มควบคุม Tekken 8 ทั้งหมด','th','controls'),('What are the basic controls for Tekken 8?','en','controls'),
 ('คอมของศูนย์สเปคอะไร','th','equipment_spec'),('What PC specifications does the studio have?','en','equipment_spec'),
 ('ต้องเป็นสมาชิกไหม มีที่จอดรถไหม แล้วต้องเอาบัตรอะไรไป','th','multi_topic'),
 ('Do I need membership, is there parking, and what ID should I bring?','en','multi_topic'),
 ('เอาเมาส์มาเองได้ไหม แล้วจองผิดเครื่องเปลี่ยนยังไง','th','multi_topic'),
 ('Can I bring my own keyboard, and can someone else use my booking?','en','multi_topic'),
 ('วันนี้ VR เวลา 09:00 ถึง 09:30 ว่างไหม','th','live_booking'),
 ('Is VR free today from 09:00 to 09:30?','en','live_booking'),
 ('วันนี้ PC1 เวลา10โมง และ PC2 เวลา11โมงว่างไหม','th','live_booking'),
 ('PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่','th','multi_topic'),
 ('What games are on PC, and how much does two hours cost for a general adult?','en','multi_topic'),
 ('คนจองกับคนเล่นต้องเป็นคนเดียวกันไหม','th','player_identity'),
 ('นั่งดูเพื่อนต้องเสียเงินไหม','th','policy_boundary'),('Is parking free?','en','policy_boundary'),
]
rows=[]
for i,(q,l,cat) in enumerate(cases,127):
 payload=dict(question=q,locale=l,debug=True,experimental_rag_fallback=True,client_session_id='r54extra-'+uuid.uuid4().hex,client_turn_id='r54-'+uuid.uuid4().hex)
 start=time.perf_counter();req=urllib.request.Request(URL+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=35) as s:status=s.status;result=json.load(s)
 except urllib.error.HTTPError as s:status=s.code;result=json.load(s)
 row=dict(case=dict(id=f'c{i:03}',question=q,locale=l,category=cat),http_status=status,elapsed_sec=time.perf_counter()-start,job=dict(status='completed' if result.get('ok') else 'failed',result=result),verdict='REVIEW',checks=[],errors=[])
 rows.append(row)
 with (OUT/'extra_raw.jsonl').open('a',encoding='utf-8') as s:s.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(row['case']['id'],cat,round(row['elapsed_sec'],2),result.get('mode'),flush=True)
with (OUT/'extra_responses.json').open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2)
print('EXTRA',len(rows))
