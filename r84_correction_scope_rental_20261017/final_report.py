import hashlib,json,statistics,sys
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
web=Path(sys.argv[1]).resolve();w=json.loads((web/'SUMMARY.json').read_text(encoding='utf8'))
assert w['count']==w['expected_count']==w['passed'] and not w['model_failures'] and not w['obstacle']
def rows(p):return [json.loads(s) for s in p.read_text(encoding='utf8').splitlines()]
before=rows(B/'verification/baseline_2/TURNS.jsonl');candidate=rows(B/'verification/candidate_2/TURNS.jsonl');actual=rows(web/'TURNS.jsonl')
audit=json.loads((B/'RENTAL_AUDIT.json').read_text(encoding='utf8'));source=json.loads((B/'WORKBOOK_SOURCE.json').read_text(encoding='utf8'));cells=source['cells']
installation=json.loads((B/'INSTALLATION.json').read_text(encoding='utf8'))
unchanged=installation['database_sha256']==hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()
preserved=all(hashlib.sha256((S/name).read_bytes()).hexdigest()==sha for name,sha in installation['installed_files'].items())
assert unchanged and preserved
lines=['# ผลแก้ไข R84: ขอบเขต correction และราคาเหมา','',
'## สรุป','',
'ติดตั้งในแชท Format กลาง R78 ที่ http://127.0.0.1:8115/ แล้ว เปิด LLM และตรวจ fingerprint ของโค้ดที่โหลดจริงก่อนทดสอบ ไม่ได้ทดสอบ full corpus, legacy หรือ LLM OFF ฐานข้อมูลยังเป็น migration preview ไม่มีการอนุมัติหรือเผยแพร่ราคาแทนเจ้าของ','',
'- ชุดเป้าหมายเดียวกันก่อนแก้ 15/26 → candidate 26/26 → เว็บที่ติดตั้งจริง '+str(w['passed'])+'/'+str(w['count'])+' ข้อ เป็น 20 บทสนทนา มี 6 บทสนทนาที่ถามต่อสองรอบ','- ตรวจสอดคล้องกับ workbook: จำนวนเงิน + audience + ครึ่งวัน/เต็มวัน 24/24 รายการ ไม่ใช่การยืนยันอัตราปัจจุบันโดยเจ้าของ','- Unit/ขอบเขต/เทียบ source 70/70, qualified reply 41/41, rejection/replacement 34/34 สองชุดหลังใช้ model transport ที่ควบคุมไว้ ไม่ใช่คะแนนโมเดลจริง','- generation ของโมเดลจริงผ่าน และ selector จริงใน candidate/web ผ่าน แยกจากการตรวจเนื้อหาข้างต้น','',
'## สิ่งที่ใส่ไว้เรื่องราคาเหมา','',
'ใน DB มี rental_package 24 รายการ = 6 รูปแบบ × 2 ช่วงวัน × 2 กลุ่มหน่วยงาน ได้แก่ทุกโซน, PC, PS5, Nintendo Switch, Cockpit, VR เป็นราคาเหมาโซนสำหรับหน่วยงานภายใน/ภายนอก ไม่ควรแปลงเป็นราคาต่อเครื่องหรือต่อคนเอง','',
'ไฟล์ต้นฉบับ: '+source['source_path'],'เซลล์ราคา: '+audit['sheet']+'!B3:E8','SHA256 ต้นฉบับและไฟล์ที่ติดมากับระบบตรงกัน: `'+source['source_sha256']+'`','',
'| รูปแบบ | ภายนอกเต็มวัน | ภายนอกครึ่งวัน | ภายในเต็มวัน | ภายในครึ่งวัน |','|---|---:|---:|---:|---:|']
for row,name in [(3,'ทุกโซน'),(4,'Cockpit'),(5,'VR'),(6,'Nintendo Switch'),(7,'PS5'),(8,'PC')]:lines.append('| '+name+' | '+' | '.join(f'{cells[c+str(row)]:,}' for c in 'BCDE')+' |')
lines+=['','หน่วย: บาทตาม workbook ประวัติ source เชื่อมกับ records ได้ใน RENTAL_AUDIT.json ไม่คำนวณส่วนลด/ราคาเหมาต่อชั่วโมงจากครึ่งวันเอง','',
'## ทำไมยังตอบผิดทั้งที่ข้อมูลมี','',
'### 1. จับ task ถูก แต่ subject ผิด','',
'คำว่า wrong/incorrect/ผิด ทำให้ candidate เสนอ procedure_wrong_slip ได้ทั้งกรณีรูปสลิป ยอดเงิน และเอกสารตัวตน เมนู confirmation เดิมตรวจ task/context/ownership แต่ไม่ป้องกันวัตถุที่ขัดกัน จึงถามยืนยันหัวข้อสลิปแม้ผู้ใช้ระบุชัดว่าเป็น passport หรือ amount','',
'แก้ด้วย correction_scope ที่แยกประเภทวัตถุชัดเจนจากภาษาของหมวด ใช้ร่วมกันที่ literal profile, retrieval/model candidates และ fallback menu โดย derive ประเภทของ source จาก query_profile.subjects ไม่ผูก record ID และไม่สร้างวิธีแก้รายการเอง','',
'### 2. FAQ ซ้ำที่ไม่มี query_profile ยังถูกเลือกผิดได้','',
'Candidate 1 ปิดเมนูสลิปผิดเรื่องแล้ว แต่ “แนบรูปบัตรนักศึกษาผิด” ยังถูกเลือกเป็นรายการเอกสารเช็กอิน และ “The amount I paid was wrong” ถูกตอบด้วย FAQ สลิปอีก record หนึ่งที่ไม่มี profile นี่เป็น content failure ไม่ใช่ transport failure','',
'แก้ให้ตรวจ known-unconfirmed need ก่อน semantic selection เมื่อยังไม่มี source ที่ระบุได้ตรง ยอดเงินผิด/เอกสารตัวตนผิดจึงระบุสิ่งที่ยังไม่มีวิธีดำเนินการยืนยัน พร้อมช่องทางศูนย์ คำถามยอดเงินผิดยังถามต่อว่าโอนเกินหรือขาด ไม่ยืนยันขั้นตอนคืนเงินเอง ข้อมูลที่ตรง source ชัดเจนยังเข้าสู่เส้นทาง source ปกติก่อน','',
'### 3. ราคาเหมาอยู่ครบ แต่ operation / audience / zone scope ผิด','',
'- How much มี priority สูงกว่า half-day rental จึงค้นราคารายชั่วโมงที่หมดอายุ แก้ priority ให้ rental ที่ระบุชัดทำงานก่อน price ทั่วไป','- External organization ไม่ตรง External organizations ขณะที่ Internal organization ไม่ตรง Internal unit จึงอาจตอบทั้งสองกลุ่ม แก้ grammar ของหน่วยงานแล้ว map เฉพาะ audience ที่ประกาศว่าเป็น internal/external organizational actor ไม่มีการจับ visitor เป็น General Adult หรือหน่วยงานภายนอก','- ทุกโซนภาษาไทยไม่ถูกผูกกับ zone All Zones จึงคืนทุกแพ็กเกจแยกโซน แก้ให้เลือก zone รวมที่มีอยู่จริงใน source','',
'## ผลเว็บจริงแยกภาษา','',
'| ภาษา | ผ่าน | มัธยฐาน HTTP วินาที |','|---|---:|---:|']
for lang in ['th','en']:
 x=w['by_language'][lang];lines.append(f"| {lang} | {x['passed']}/{x['count']} | {x['median_seconds']:.3f} |")
lines+=['','เวลาจากชุดเล็กหลังเตรียมโมเดล ไม่ใช่ latency guarantee หรือผล load test โมเดลเปิดอยู่ แต่คำถามที่อ่านข้อมูลตรง/known-unconfirmed ไม่จำเป็นต้องเรียกโมเดลทุกครั้ง','',
'## เทียบทุกคำถามในชุดเดียวกัน','',
'| ภาษา | คำถาม | ก่อน | หลัง candidate | เว็บจริง |','|---|---|---|---|---|']
for a,c,z in zip(before,candidate,actual):
 assert a['question']==c['question']==z['question']
 lines.append('| '+a['locale']+' | '+a['question'].replace('|','/')+' | '+('ผ่าน' if a['passed'] else ', '.join(a['errors']))+' | '+('ผ่าน' if c['passed'] else ', '.join(c['errors']))+' | '+('ผ่าน' if z['passed'] else ', '.join(z['errors']))+' |')
lines+=['','## ตัวอย่างคำตอบหลังแก้','']
for name in ['en-amount-order','th-student-id','en-rental-ps5','th-rental-all']:
 r=next(r for r in actual if r['case']==name)
 lines+=['### '+r['question'],'',r['body']['answer'],'']
lines+=['## ข้อจำกัดและข้อมูลที่ต้องถามเจ้าของ','',
'1. ครึ่งวันและเต็มวันของการเหมาเริ่ม/สิ้นสุดกี่โมง และนับเป็นกี่ชั่วโมง? source ยังไม่ให้ข้อมูล ไม่กำหนด 4/8 ชั่วโมงเอง','2. ต้องการขายราคาเหมาต่อชั่วโมงด้วยหรือไม่? ถ้ามี ต้องระบุราคา/โซน/กลุ่มผู้ใช้/ขั้นต่ำจากเจ้าของ ไม่หารราคาเหมาวันเอง','3. ราคาเหมา 24 รายการนี้มีผลเริ่มวันไหนและสิ้นสุดวันไหน? validity ปัจจุบันยัง unknown ไม่เติมวันที่แทนเจ้าของ','4. การจองแบบเหมาทำช่องทางใด ชำระ/มัดจำ/เปลี่ยน/ยกเลิกอย่างไร และค่าเจ้าหน้าที่นอกเวลาคิดกับผู้ขอใช้แบบไหน? workbook มีเพียงข้อความเบิกตามระเบียบ ไม่สรุปว่าอยู่ในราคาหรือใครเป็นผู้จ่าย','5. ถ้ายอดเงินผิดหรือเอกสารตัวตนแนบผิด เจ้าหน้าที่ให้ดำเนินการอย่างไร? รอบนี้ตอบสถานะยังไม่ทราบอย่างจำเพาะ ไม่เพิ่มนโยบาย','6. เป็นชุดทดสอบเฉพาะจุด ไม่พิสูจน์ประโยคหลายเงื่อนไข/การปฏิเสธ/คำผิดทุกรูปแบบ ประเภทที่ไม่มี grammar ยังต้องใช้การถามยืนยัน/อ่าน source ตามกลไกเดิม ไม่มี claim ว่าแก้ NLP ครบทุกความหมาย','7. ข้อความอังกฤษที่เพิ่ม/แปลใหม่ยังเป็น machine/agent translated ตาม metadata ไม่อ้างว่าเจ้าของตรวจรอบนี้แล้ว','',
'## การรักษาข้อมูลและหลักฐาน','',
'- เปลี่ยนโค้ดเฉพาะ 8 ไฟล์ใน R78 มี before/candidate และ CHANGESET.patch ฐานข้อมูลไม่เปลี่ยน strict binding และ compact opening ไม่เปลี่ยน ตรวจไฟล์ app/UI อื่น '+str(installation['other_application_ui_files_unchanged'])+' ไฟล์ไม่เปลี่ยน','- ไม่เขียนทับโครงการ Downloads, workbook, approvals, releases หรือ log รอบก่อน ผลทดลองที่ล้มและ candidate 1 ยังอยู่','- baseline_1 ยังไม่ถาม chatbot เพราะ model-list timeout 4 วินาที ตรวจซ้ำ endpoint ปกติภายใน 0.5 วินาที ไม่อ้างว่า timeout เป็นข้อผิดพลาดเนื้อหา และไม่ปิด LLM เพื่อให้คะแนนผ่าน','',
'หลักฐาน:','- BASELINE_MANIFEST*.json, INSTALLATION.json, SOURCE_INVENTORY_BEFORE.json, CHANGESET.patch','- RENTAL_AUDIT.json, verification/unit_2/UNIT_RESULTS.json','- verification/baseline_2/SUMMARY.json และ TURNS.jsonl','- verification/candidate_1/SUMMARY.json และ verification/candidate_2/SUMMARY.json','- verification/qualified_final/RESULTS.json และ verification/rephrase_final/RESULTS.json','- เว็บจริง: '+str(web),'',
'เทสใหญ่ยังพักไว้จนกว่าผู้ใช้สั่งใหม่']
with (B/'REPORT_R84_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines)+'\n')
qa={'installed_source_hashes_match':preserved,'database_unchanged':unchanged,'actual_web_summary':w,'report':str(B/'REPORT_R84_TH.md'),'full_test_executed':False}
with (B/'DELIVERY_QA.json').open('x',encoding='utf8') as f:json.dump(qa,f,ensure_ascii=False,indent=2)
print(json.dumps({'report':qa['report'],'web':w,'database_unchanged':unchanged},ensure_ascii=False))
