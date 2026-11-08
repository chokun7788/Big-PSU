import json,time,uuid,urllib.request,urllib.error,datetime,hashlib,sys,re
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');URL='http://127.0.0.1:8093'
OUT=BASE/('r54_shop_cases_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));OUT.mkdir();(BASE/'r54_current_path.txt').write_text(str(OUT),encoding='utf-8')
facts=json.loads((ROOT/'data/curated/user_service_facts_20261008.json').read_text(encoding='utf-8'))
cases=[]
def add(q,locale='th',category='policy',claim=None,expect=None,scenario=None,live=False):
 cases.append(dict(id=f'c{len(cases)+1:03}',question=q,locale=locale,category=category,claim=claim,expect=expect,scenario=scenario,live=live))
policy=[
 ('university','ที่นี่เป็นร้านเกมทั่วไปหรือของมหาวิทยาลัย','Is this a university facility or a regular gaming cafe?'),
 ('membership','ต้องเป็นสมาชิกก่อนเล่นไหม','Do I need membership to use the studio?'),
 ('spectators','ไปนั่งดูเพื่อนเล่นเฉยๆได้ไหม','Can I sit and watch my friend play?'),
 ('walk_in','เดินเข้าไปเล่นเลยได้ไหม ต้องจองไหม','Can I walk in without booking?'),
 ('location','ศูนย์อยู่ตึกไหน ชั้นอะไร','Which building and floor is the studio in?'),
 ('map','ขอลิงก์แผนที่ศูนย์หน่อย','Can I have the studio map link?'),
 ('parking','มีที่จอดรถยนต์กับมอเตอร์ไซค์ไหม','Is there parking for cars and motorcycles?'),
 ('contact','หาศูนย์ไม่เจอ ติดต่อใครได้','Who can I contact if I cannot find the studio?'),
 ('four_people','มากันสี่คนควรเลือกเครื่องไหน','What should a group of four choose?'),
 ('player_identity','จองชื่อเราแต่ให้เพื่อนที่ไม่มีชื่อเล่นแทนได้ไหม','Can a friend who is not named in my booking play instead?'),
 ('checkin_documents','ตอนมาถึงต้องแสดงบัตรอะไร','What ID should I show when I arrive?'),
 ('change_machine','จองผิดเครื่องต้องแก้ยังไง','How do I change a booking for the wrong machine?'),
 ('change_time','เปลี่ยนเวลาจองทำยังไง','How can I change my booking time?'),
 ('personal_keyboard_mouse','เอาคีย์บอร์ดหรือเมาส์ตัวเองมาใช้ได้ไหม','Can I bring my own keyboard or mouse?'),
 ('wrong_slip','แนบสลิปผิดรูปต้องทำยังไง','What should I do if I uploaded the wrong payment slip?'),
 ('combined_transfer','จองหลายเครื่องโอนครั้งเดียวได้ไหม','Can I make one bank transfer for several machines?'),
 ('group_checkin','มาถึงก่อนเพื่อนเช็กอินแทนทั้งกลุ่มได้ไหม','Can I check in for my whole group before my friends arrive?'),
 ('rest_seating','มีที่นั่งพักรอเพื่อนไหม','Is there seating where I can rest while waiting for friends?'),
]
for claim,th,en in policy:
 add(th,claim=claim);add(en,'en',claim=claim)
variants=[
 ('membership','ต้องสมัคสมาชิกก่อนไหม','th'),('membership','do i need a memebrship first','en'),
 ('spectators','แค่มาดูเพื่อนได้ปะ ไม่เล่น','th'),('spectators','can i just watch my freind','en'),
 ('walk_in','ไม่ได้จองมา เดินเข้าได้ปะ','th'),('walk_in','can i walkin and play straight away','en'),
 ('location','อยู่ตึกไร ชั้นไหนอ่ะ','th'),('parking','มอไซจอดไหน มีที่จอดปะ','th'),
 ('four_people','มา4คน เล่นอันไหนดี','th'),('four_people','we are 4 ppl what can we play','en'),
 ('player_identity','เพื่อนไม่มีชื่อในจอง เล่นแทนได้มะ','th'),
 ('checkin_documents','ไปถึงต้องเอาบัตรไรไปมั่ง','th'),('checkin_documents','which documnts do i bring for checkin','en'),
 ('change_machine','จองผืดเครื่อง เปลี่ยนไง','th'),('change_time','อยากเปลี่ยนรอบที่จอง ต้องทำไง','th'),
 ('personal_keyboard_mouse','เอาเม้าส์ตัวเองไปเสียบได้ปะ','th'),('personal_keyboard_mouse','can i use my own keybaord','en'),
 ('wrong_slip','อัพสลิปผืด ส่งใหม่ทางไหน','th'),('combined_transfer','จอง3เครื่อง จ่ายรวมทีเดียวได้ปะ','th'),
 ('group_checkin','เพื่อนยังมาไม่ถึง เช็คอินให้ทั้งแก๊งได้ไหม','th'),('rest_seating','มีตรงให้นั่งรอมั้ย','th'),
]
for claim,q,l in variants:add(q,l,'policy_variant',claim)
for q,l,e in [
 ('ราคา PC บุคคลทั่วไป','th',{'contains':['70'],'not_general_model':True}),
 ('PC prices for general adults','en',{'contains':['70'],'not_general_model':True}),
 ('เป็นบุคคลทั่วไป เล่น PC 2 ชั่วโมงเท่าไหร่','th',{'contains':['140'],'not_general_model':True}),
 ('General adult PC for two hours, how much?','en',{'contains':['140'],'not_general_model':True}),
 ('มี 100 บาท เป็นบุคคลทั่วไป เล่น PC ได้กี่ชั่วโมง','th',None),
 ('I am a general adult with 100 baht. What can I play?','en',None),
 ('มา4คนเล่น Nintendo 1 ชั่วโมง บุคคลทั่วไปเท่าไหร่','th',None),
 ('ขอตารางราคาทุกบริการบุคคลภายนอก','th',{'contains':['PC','Cockpit','VR'],'not_general_model':True}),
 ('All service prices for external users','en',{'contains':['PC','Cockpit','VR'],'not_general_model':True}),
]:add(q,l,'price_budget',expect=e)
for q,l,e in [
 ('หน่วยงานภายนอกเหมา PC เต็มวันราคาเท่าไหร่','th',{'contains':['4,000'],'not_general_model':True}),
 ('PC whole-day rental price for external organizations','en',{'contains':['4,000'],'not_general_model':True}),
 ('หน่วยงานภายนอกเหมาทุกโซน ครึ่งวันกับเต็มวันราคาเท่าไหร่','th',{'contains':['6,000','12,000'],'not_general_model':True}),
 ('Compare PC full-day rental external organizations with VR half-day internal organizations','en',{'contains':['4,000','1,500'],'not_general_model':True}),
 ('เหมาครึ่งวันคือกี่ชั่วโมง','th',None),
 ('Can I rent PS55 for a full day?','en',None),
]:add(q,l,'rental',expect=e)
for q,l,e in [
 ('PC มีเกมอะไรบ้าง ขอทั้งหมด','th',{'contains':['VALORANT','Counter-Strike'],'not_general_model':True}),
 ('What games are available on PC? List all of them.','en',{'contains':['VALORANT','Counter-Strike'],'not_general_model':True}),
 ('Nintendo มีเกมไรมั่ง','th',None),('What games can I play on Nintendo Switch?','en',None),
 ('PS5 มีเกมไรบ้าง','th',None),('Cockpit เล่นเกมอะไร','th',{'contains':['Gran Turismo'],'not_general_model':True}),
 ('VR มีเกมอะไรบ้าง','th',{'contains':['Beat Saber'],'not_general_model':True}),
 ('ที่ศูนย์มีเกมให้เล่นทั้งหมดกี่เกม','th',None),
]:add(q,l,'games',expect=e)
for q,l,e in [
 ('กฏตอนเเข่ง cs2 มีอะไรมั่ง','th',{'contains':['Counter-Strike'],'forbid':['PSU Phuket VALORANT 2026 Tournament']}),
 ('กฏตอนเเข่ง rov มีอะไรมั่ง','th',{'contains':['ROV'],'forbid':['PSU Phuket VALORANT 2026 Tournament']}),
 ('กฏตอนเเข่ง tekken 8 มีอะไรมั่ง','th',{'contains':['TEKKEN'],'forbid':['PSU Phuket VALORANT 2026 Tournament']}),
 ('กฏตอนแข่งวาโลมีอะไรมั่ง','th',{'contains':['VALORANT']}),
 ('ขอกฎการแข่งขัน CS2 ทั้งหมดทุกหัวข้อ','th',{'contains':['Counter-Strike']}),
 ('All documented competition rules for Tekken 8','en',{'contains':['TEKKEN']}),
 ('What are the ROV tournament rules?','en',{'contains':['ROV']}),
 ('กฎแข่ง CS2 ปี 2030','th',None),
]:add(q,l,'competition',expect=e)
for q,l in [
 ('ตอนนี้ PC ว่างไหม','th'),('cockpik ว่างไหม','th'),('วันนี้ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง','th'),
 ('Which equipment is free today at 3 pm?','en'),('Is PC1 free today at 10 am?','en'),('วันนี้ VR 9:00-9:30 ว่างไหม','th'),
]:add(q,l,'live_booking',live=True)
for q,l in [
 ('เครื่องค้างระหว่างเล่น คืนเวลาให้ไหม','th'),('Can I install a game that is not in your list?','en'),
 ('เอา Steam ตัวเองล็อกอินได้ไหม','th'),('If I arrive 15 minutes late, can I still play?','en'),
 ('เด็กอายุ10ขวบเล่นได้ไหม ต้องมีผู้ปกครองไหม','th'),('May I stream from a studio computer?','en'),
 ('จ่ายแล้วจองผิดวัน เปลี่ยนวันกับขอเลื่อนแทนคืนเงินได้ไหม','th'),
 ('เกมต้องอัปเดตตอนมาถึง เวลานับยังไง','th'),
]:add(q,l,'policy_boundary',expect={'no_unverified_policy':True})
dialogs=[
 ('price_pc_th','th',['ราคาของบุคคลภายนอก','PC'],[None,{'contains':['70','25'],'not_general_model':True}]),
 ('price_all_th','th',['ต้องการราคาของบุคคลภายนอก','ทั้งหมด'],[None,{'contains':['PC','Cockpit','VR'],'not_general_model':True}]),
 ('price_pc_en','en',['Service prices for external users','PC'],[None,{'contains':['70','25'],'not_general_model':True}]),
 ('price_all_en','en',['Service prices for external users','all of them'],[None,{'contains':['PC','Cockpit','VR'],'not_general_model':True}]),
 ('game_scope','th',['PC มีเกมอะไรบ้าง','ทั้งหมด'],[None,{'contains':['VALORANT','Counter-Strike'],'forbid':['Nintendo Switch Zone']}]),
 ('rules_choose','th',['ขอกฎการแข่งขัน','CS2'],[None,{'contains':['Counter-Strike'],'forbid':['PSU Phuket VALORANT 2026 Tournament']}]),
 ('rules_choose_en','en',['I want the competition rules','Tekken 8'],[None,{'contains':['TEKKEN']}]),
 ('rental_capacity','en',['PC full-day rental price for external organizations','How many people can it accommodate?'],[None,None]),
 ('rental_booking','en',['PC full-day rental price for external organizations','How can I reserve it?'],[None,None]),
 ('price_switch_group','th',['ราคา PC บุคคลทั่วไป','แล้ว VR ล่ะ'],[None,{'contains':['VR'],'not_general_model':True}]),
 ('topic_shift','th',['ราคา PC บุคคลทั่วไป','กฎแข่ง ROV ล่ะ'],[None,{'contains':['ROV'],'forbid':['70 บาท/แพ็กเกจ']}]),
 ('booking_scope','th',['วันนี้ PC1 ตอน10โมงว่างไหม','แล้ว PC2 ล่ะ'],[None,None]),
]
for name,l,questions,expects in dialogs:
 for q,e in zip(questions,expects):add(q,l,'dialogue',expect=e,scenario=name,live=name=='booking_scope')
(OUT/'cases.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2),encoding='utf-8')
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('data/curated','data/rules','booking_dashboard') for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and 'logs' not in p.parts}
(OUT/'owner_hashes_before.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
def request(path,payload=None):
 req=urllib.request.Request(URL+path,data=json.dumps(payload,ensure_ascii=False).encode() if payload is not None else None,headers={'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=35) as response:return response.status,json.load(response)
 except urllib.error.HTTPError as e:return e.code,json.load(e)
health=request('/health')[1];assert health['runtime']['version']=='2026.10.09-semantic-r53.3';(OUT/'health_before.json').write_text(json.dumps(health,indent=2),encoding='utf-8')
sessions={};seen={};rows=[]
for c in cases:
 key=c['scenario'] or c['id'];session=sessions.setdefault(key,'r54-'+uuid.uuid4().hex);start=time.perf_counter()
 status,job=request('/api/chat/jobs',dict(question=c['question'],locale=c['locale'],debug=True,experimental_rag_fallback=True,client_session_id=session,client_turn_id='r54-'+uuid.uuid4().hex,last_seen_response_id=seen.get(key,'')))
 if status==202:
  deadline=time.monotonic()+60
  while job['status'] in ('queued','running') and time.monotonic()<deadline:
   time.sleep(.25);_,job=request('/api/chat/jobs/'+job['job_id']+'?session_id='+session)
 result=job.get('result') or {};seen[key]=result.get('request_id',seen.get(key,''));answer=result.get('answer','');mode=result.get('mode','');errors=[];checks=[]
 def require(ok,label):checks.append(label);errors.extend([] if ok else [label])
 require(job.get('status')=='completed','transport_complete')
 if c['claim']:
  require(facts['claims'][c['claim']]['answers'][c['locale']] in answer,'canonical_owner_answer_present')
 if c['expect']:
  e=c['expect']
  for word in e.get('contains',[]):require(word.casefold() in answer.casefold(),'contains:'+word)
  for word in e.get('forbid',[]):require(word.casefold() not in answer.casefold(),'forbids:'+word)
  if e.get('not_general_model'):require('general_llm_direct' not in mode,'owner_route_not_general_model')
 verdict='REVIEW' if errors or c['live'] or not(c['claim'] or c['expect'] and c['expect'].get('contains')) else 'PASS_BOUNDED'
 row=dict(case=c,http_status=status,session_id=session,elapsed_sec=time.perf_counter()-start,job=job,checks=checks,errors=errors,verdict=verdict)
 rows.append(row)
 with (OUT/'responses_raw.jsonl').open('a',encoding='utf-8') as s:s.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(c['id'],c['category'],round(row['elapsed_sec'],2),mode,verdict,errors,flush=True)
with (OUT/'responses.json').open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2)
changed=[p for p,h in hashes.items() if not(ROOT/p).exists() or hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
with (OUT/'preservation.json').open('x',encoding='utf-8') as s:json.dump({'owner_files':len(hashes),'changed':changed,'source_edits':False,'old_logs_overwritten':False},s,indent=2)
print('TOTAL',len(rows),'bounded pass',sum(r['verdict']=='PASS_BOUNDED' for r in rows),'review',sum(r['verdict']=='REVIEW' for r in rows),'output',OUT,flush=True)
