"""Receive ten submitted owner clarifications into a separate intake version."""
import copy,hashlib,json,shutil,urllib.request
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;F=B/'r107_owner_questions_20261020';P=B/'r108_owner_intake_20261020'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
submission_path=F/'responses/submissions/PSU-owner-answers-20261020-233634-baac31.json'
submission=read(submission_path);answers={x['id']:x for x in submission['answers']}
questions=read(F/'simple_questions.json')['questions'];responses=read(F/'responses/simple_answers.json')
assert len(answers)==10 and set(answers)=={x['id'] for x in questions}
for key,a in answers.items():
 assert responses['answers'][key]['text']==a['answer'] and responses['answers'][key]['submitted_at']==submission['submitted_at']
protected=[F/'responses/simple_answers.json',F/'responses/simple_events.jsonl',F/'responses/answers.json',F/'simple_questions.json',P/'SERVICE_STATEMENTS.json',P/'TOURNAMENT_SOURCE_UNITS.json',P/'RENTAL_SOURCE_RECONCILIATION.json',B/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite']
before={str(p):sha(p) for p in protected}
target=R/'SOURCE_SUBMISSION.json'
if target.exists():assert target.read_bytes()==submission_path.read_bytes()
else:shutil.copy2(submission_path,target)
write(R/'SOURCE_STATE.json',{'read_at':datetime.now().astimezone().isoformat(),'responses':responses,'submission_path':str(submission_path),'submission_sha256':sha(submission_path)})

values={
'R108_OPEN_16_18':('เวลาเปิดพื้นที่',{'weekdays':[0,1,2,3,4],'closed_interval':{'start':'16:00','end':'18:00'},'timezone':'Asia/Bangkok'},'วันจันทร์–ศุกร์ ช่วง 16:00–18:00 ศูนย์ปิดแล้ว','ไม่สร้างช่วงเปิด 09:00–16:00 ทุกนาทีจากคำตอบนี้; ตารางพัก/บำรุงรักษา/วันหยุดเดิมยังต้องแยก'),
'R108_RENT_HALF_HOURS':('ระยะเหมาแบบครึ่งวัน',{'duration_minutes':180,'period_options':[{'start':'09:00','end':'12:00'},{'start':'13:00','end':'16:00'}]},'เหมาครึ่งวัน 3 ชั่วโมง เลือกช่วง 09:00–12:00 หรือ 13:00–16:00','เงื่อนไขเหมา ไม่ใช่การเปิดจองเครื่องทั่วไปในช่วง maintenance; การจัดเวลาอื่นที่เคยบอกว่าเลือกได้ให้ประสานเพจ ไม่ยืนยันว่าทุกเวลาใช้ราคาเดิมอัตโนมัติ'),
'R108_RENT_FULL_HOURS':('ระยะเหมาแบบเต็มวัน',{'duration_minutes':420,'period':{'start':'09:00','end':'16:00'},'includes_noon_interval':True},'เหมาเต็มวัน 09:00–16:00 รวม 7 ชั่วโมง ครอบคลุมช่วงเที่ยง','ไม่เปลี่ยนกฎจองเล่นรายชั่วโมงที่ 12:00–13:00 ไม่มีรอบ; ห้ามคำนวณเหลือ 6 ชั่วโมงหรือเดาเป็น 8 ชั่วโมง'),
'R108_PS5_CONTROLLERS':('จำนวนจอย PS5',{'controllers_per_console':2},'PS5 หนึ่งเครื่องมีจอยให้ 2 จอย','ไม่ยืนยันรุ่นจอยหรือจำนวนผู้เล่นสูงสุดของทุกเกม'),
'R108_MIXED_RATE':('ผู้เล่นต่างกลุ่มราคา',{'individual_rate_by_own_audience':True},'นักศึกษา PSU กับบุคคลภายนอกที่มาเล่นด้วยกัน แต่ละคนจ่ายตามกลุ่มราคาของตัวเอง','ขอบเขตราคาบริการรายคน ไม่ใช่ราคาเหมาโซน'),
'R108_PAYER':('ผู้โอนเงิน',{'payer_must_be_named_in_booking':True},'ผู้โอนเงินต้องเป็นผู้ที่มีชื่อลงไว้ในรายการจอง','ใช้เงื่อนไขผู้มีชื่อ ไม่แต่งเพิ่มว่าต้องเป็นผู้จองหลักเท่านั้น; ไม่อนุญาตบุคคลนอกชื่อรายการ'),
'R108_TEKKEN_PAUSE':('Tekken — อนุญาต Pause',{'allowed_if_all_agree':True,'appropriate_reason_required':True,'event':'PSU Esports ปะทะมันส์ สนั่นจอ'},'Pause ได้เมื่อผู้เล่นทุกคนยินยอมและมีเหตุผลเหมาะสม','คำยืนยันเจ้าของเลือกกฎอนุญาตแบบมีเงื่อนไขเหนือข้อความห้ามทุกกรณี; ไม่ได้ยืนยันหน่วยบทลงโทษ'),
'R108_ROV_615':('RoV — ข้อ 6.1.5',{'owner_reaffirmed_original_wording':True},answers['R108_ROV_615']['answer'].strip(),'เจ้าของส่งถ้อยคำเดิมมาอีกครั้ง จึงคงข้อความตามต้นทาง ไม่อ้างว่าแก้ไวยากรณ์ที่กำกวมแล้ว และไม่สร้างบทลงโทษใหม่จากประโยคนี้'),
'R108_ROV_6151':('RoV — ข้อ 6.1.5.1',{'completion':'ออกจากการแข่งขันทันที'},'บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที','คำตอบเป็นข้อความท้ายที่มีคำว่าออกจากซ้ำ ต้องแทน suffix ไม่ต่อออกจากออกจาก'),
}
new=[]
for key,(topic,value,text,limit) in values.items():
 a=answers[key]
 new.append({'id':'owner109:'+key,'kind':'scoped_owner_statement','topic':topic,'value':value,'answer_th':text,'source_question_id':key,'source_question':a['question'],'source_text':a['answer'],'submitted_at':submission['submitted_at'],'source_ref':{'path':'SOURCE_SUBMISSION.json','answer_id':key},'limits':limit,'production_applied':False})
write(R/'OWNER_CLARIFICATIONS.json',{'statements':new,'production_applied':False})
exclusion={'id':'tekken_pause_penalty_unit_unconfirmed','source_question_id':'R108_TEKKEN_PENALTY','source_text':answers['R108_TEKKEN_PENALTY']['answer'],'status':'owner_requested_defer_and_no_test','scope':{'event':'PSU Esports ปะทะมันส์ สนั่นจอ','topic':'unit_of_pause_penalty','unknown_values':['round','game','match']},'future_test_handling':'Do not test or grade the unresolved penalty unit; do not remove other Tekken tests. Preserve any affected excluded keys and report exclusions separately from coverage. Existing frozen workloads/results stay unchanged.','answer_handling':'ไม่ยืนยันว่าโทษคือ Round/Game/Match เมื่อไม่มีข้อมูลที่เจ้าของให้; แจ้งว่ายังไม่มีข้อมูลยืนยันหากถูกถาม','applied_to_existing_tests':False}
write(R/'FUTURE_TEST_EXCLUSIONS.json',{'exclusions':[exclusion],'tests_run':0,'note':'บันทึกคำสั่งสำหรับการจัด workload ในรอบอนาคต ไม่ได้แก้ test/log เดิม และไม่นับข้อที่งดเป็นผ่าน'})

merged=copy.deepcopy(read(P/'SERVICE_STATEMENTS.json'));merged['statements']+=new;merged['revision']='r109';merged['source_intake']='r108_owner_intake_20261020';merged['instruction_records']=[exclusion]
write(R/'MERGED_SERVICE_STATEMENTS.json',merged)
rental=copy.deepcopy(read(P/'RENTAL_SOURCE_RECONCILIATION.json'))
for p in rental['packages']:
 k='R108_RENT_HALF_HOURS' if p['period_label']=='half_day' else 'R108_RENT_FULL_HOURS'
 p['duration_minutes']=values[k][1]['duration_minutes'];p['duration_evidence']={'path':'SOURCE_SUBMISSION.json','answer_id':k}
 p['time_windows']=values[k][1].get('period_options',[values[k][1].get('period')])
 p['includes_noon_interval']=p['period_label']=='full_day'
rental['duration_hours_missing_in_workbook']=True;rental['duration_resolved_from_owner_submission']=True
write(R/'RENTAL_PACKAGES_RECONCILED.json',rental)

rules=copy.deepcopy(read(P/'TOURNAMENT_SOURCE_UNITS.json'))
for d in rules['documents']:
 for u in d['units']:
  if d['game']=='tekken' and u['paragraph'] in [16,34]:
   u['owner_resolution']={'answer_id':'R108_TEKKEN_PAUSE','answer_th':values['R108_TEKKEN_PAUSE'][2],'status':'use_owner_clarification_for_permission','original_text_preserved':True}
   u['quality_hold']=None
   u['usage']='superseded_for_pause_permission' if u['paragraph']==16 else 'consistent_with_owner_clarification'
  if d['game']=='tekken' and u['paragraph'] in [17,35]:u['owner_resolution']={'answer_id':'R108_TEKKEN_PENALTY','status':'deferred_no_test','do_not_infer_penalty_unit':True}
  if d['game']=='rov' and u['paragraph']==85:u['owner_resolution']={'answer_id':'R108_ROV_615','status':'original_wording_reaffirmed_not_rewritten','do_not_infer_missing_meaning':True}
  if d['game']=='rov' and u['paragraph']==86:
   assert u['text'].endswith('ออกจาก')
   u['candidate_text']=u['text']+answers['R108_ROV_6151']['answer'].strip()[len('ออกจาก'):]
   u['quality_hold']=None;u['owner_resolution']={'answer_id':'R108_ROV_6151','status':'tail_completed_from_owner','original_text_preserved':True}
rules['revision']='r109';rules['production_applied']=False
write(R/'TOURNAMENT_SOURCE_UNITS_RECONCILED.json',rules)
known=copy.deepcopy(read(P/'UNKNOWN_FACETS_NOT_REASKED.json'));known['additional_limits']=[{'id':'tekken_penalty_unit','status':'deferred','source':'FUTURE_TEST_EXCLUSIONS.json'},{'id':'rov_615_wording','status':'owner_reaffirmed_original_still_awkward','do_not_invent_revision':True}]
write(R/'REMAINING_LIMITS.json',known)
active=[q for q in questions if not responses['answers'].get(q['id'],{}).get('submitted_at')]
write(R/'REMAINING_OWNER_QUESTIONS.json',{'questions':active,'count':len(active),'note':'ไม่มีคำถามค้างในรอบแบบฟอร์มนี้ ไม่ใช่คำยืนยันว่าทุก unknown ในระบบได้รับคำตอบแล้ว'})

checks=[]
def check(name,ok):checks.append({'check':name,'passed':bool(ok)});assert ok,name
check('all 10 submitted replies matched live storage',len(answers)==10)
check('no unanswered prompts in this form',len(active)==0)
check('all 24 rental durations updated',len(rental['packages'])==24 and {p['duration_minutes'] for p in rental['packages']}=={180,420})
check('whole-day arithmetic includes noon',(16-9)*60==values['R108_RENT_FULL_HOURS'][1]['duration_minutes'])
rov=next(u for d in rules['documents'] if d['game']=='rov' for u in d['units'] if u['paragraph']==86)
check('RoV suffix not duplicated',rov['candidate_text'].endswith('ออกจากการแข่งขันทันที') and 'ออกจากออกจาก' not in rov['candidate_text'])
check('pause permission not blanket unconditional',values['R108_TEKKEN_PAUSE'][1]['allowed_if_all_agree'] and values['R108_TEKKEN_PAUSE'][1]['appropriate_reason_required'])
check('penalty skip stored as instruction not answer',not any(x['source_question_id']=='R108_TEKKEN_PENALTY' for x in new) and exclusion['status']=='owner_requested_defer_and_no_test')
with urllib.request.urlopen('http://127.0.0.1:8120/api/simple-state',timeout=5) as response:state=json.load(response)
check('live page has no unsubmitted prompts',not any(not state['responses']['answers'].get(q['id'],{}).get('submitted_at') for q in state['questions']['questions']))
check('old response/source/database files untouched',all(sha(Path(path))==h for path,h in before.items()))
check('frozen database still original',sha(B/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite')==read(F/'questions.json')['source_database_sha256'])
write(R/'VERIFICATION.json',{'checks':checks,'passed':len(checks),'total':len(checks),'protected_hashes':before,'llm_calls':0,'tests_run':0,'production_applied':False,'browser_visual_verified':False})
write(R/'SUMMARY.json',{'received':10,'normalized_statements':9,'owner_wording_retained_without_grammar_change':1,'deferred_no_test':1,'remaining_form_questions':0,'rental_packages_with_hours':24,'production_applied':False,'verification_passed':len(checks)})
lines=['# รับคำตอบเพิ่มเติม R109','',f"เจ้าของส่งจริงเมื่อ {submission['submitted_at']} รวม 10 ข้อ อ่านจากไฟล์ submission และตรวจตรงกับ state เว็บ ไม่เปลี่ยนคำตอบ/ประวัติเดิม",'',
'## ข้อมูลที่อัปเดตในชุดเตรียมนำเข้า','',
'| เรื่อง | คำตอบที่ใช้ |','|---|---|',
'| เวลาเปิดพื้นที่ | จันทร์–ศุกร์ 16:00–18:00 ปิดแล้ว ไม่สรุปช่วงเปิดอื่นแทนตารางเดิม |',
'| เหมาครึ่งวัน | 3 ชั่วโมง: 09:00–12:00 หรือ 13:00–16:00 |',
'| เหมาเต็มวัน | 09:00–16:00 รวม 7 ชั่วโมงและช่วงเที่ยง แยกจากกฎจองเครื่องทั่วไป |',
'| จอย PS5 | 2 จอยต่อเครื่อง |',
'| ผู้ใช้ต่างกลุ่ม | แต่ละคนจ่ายราคาตามกลุ่มของตัวเอง |',
'| ผู้โอนเงิน | ต้องเป็นผู้มีชื่อลงในรายการ ไม่กำหนดเพิ่มว่าต้องเป็นผู้จองหลักเพียงคนเดียว |',
'| Pause Tekken | ได้เมื่อทุกคนยินยอมและมีเหตุผลเหมาะสม เฉพาะรายการที่เอกสารระบุ |',
'| RoV 6.1.5 | เก็บถ้อยคำที่เจ้าของส่งมาเดิม ไม่อ้างว่าแก้ประโยคกำกวมเรียบร้อย |',
'| RoV 6.1.5.1 | เติมท้ายให้ครบว่าออกจากการแข่งขันทันที โดยไม่ซ้ำคำว่าออกจาก |','',
'## ข้อที่ให้ข้าม','',
'หน่วยโทษ Pause ของ Tekken ว่าแพ้ Round/Game/Match ยังไม่มีข้อมูล เจ้าของให้ข้ามและไม่ทดสอบ บันทึกไว้ใน FUTURE_TEST_EXCLUSIONS.json เฉพาะหัวข้อนี้ ไม่ตัดการทดสอบ Tekken ทั้งหมด ไม่แปลคำสั่งว่าไม่มีโทษ และไม่นับข้อที่ข้ามเป็นผ่านหรือแก้ workload/log ผลทดสอบเก่า','',
'## ความเข้ากันกับข้อมูลเดิม','',
'- ช่วงเที่ยงที่รวมในราคาเหมาเต็มวันไม่ใช่คำยืนยันเปิดรอบรายชั่วโมง 12:00–13:00',
'- ชั่วโมงเหมาอัปเดตครบ 24 ราคา โดยใช้จำนวนเงิน/ที่นั่ง/อุปกรณ์จากชุด R108 เดิม ไม่คูณราคาต่อคนซ้ำ',
'- ช่วงเริ่มครึ่งวันปกติตามคำตอบใหม่คือเช้า/บ่าย การจัดเวลาอื่นให้ประสานเพจตามช่องทางเหมาเดิม ไม่รับรองเวลาอื่นเป็นมาตรฐานโดยอัตโนมัติ',
'- คำยืนยัน Pause แก้ข้อขัดแย้งด้านอนุญาตเฉพาะ candidate; DOCX ต้นฉบับและ frozen system ไม่ได้แก้',
'- RoV ข้อ 6.1.5 ยังมีถ้อยคำเดิมที่ไม่ลื่นไหล เก็บตามเจ้าของ ไม่แต่งส่วนที่ไม่ได้ให้หรือขยายความเป็นโทษอื่น','',
'## สถานะ','',
'- แบบฟอร์มรอบนี้ไม่มีคำถามค้างแล้ว: ส่งครบทั้ง 10 ข้อ (หนึ่งข้อเป็นคำสั่งข้าม)',
'- ข้อมูลที่ยังไม่ยืนยันนอกแบบฟอร์ม เช่นผังปุ่มบางเกม บัญชี console/DLC และเงื่อนไขบางอย่างยังคงจำกัดขอบเขตตาม REMAINING_LIMITS.json ไม่สรุปว่าข้อมูลครบทุกชนิด',
'- รวมข้อมูลใน MERGED_SERVICE_STATEMENTS.json / RENTAL_PACKAGES_RECONCILED.json / TOURNAMENT_SOURCE_UNITS_RECONCILED.json พร้อม provenance สำหรับนำเข้าเวอร์ชันถัดไป',
'- ยังไม่ได้ติดตั้งทับแชท R78 ไม่เปลี่ยน frozen R106 ไม่รัน LLM/test ใหม่',
f'- ตรวจความสอดคล้องไฟล์และ HTTP state ผ่าน {len(checks)}/{len(checks)} รายการ ไม่ใช่ผลทดสอบความถูกต้องของคำตอบแชทหรือการตรวจภาพหน้าเว็บ',
]
(R/'RECEIPT_AND_UPDATES_TH.md').write_text('\n'.join(lines),'utf8')
print(json.dumps(read(R/'SUMMARY.json'),ensure_ascii=False))
