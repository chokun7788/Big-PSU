import json,hashlib,shutil,subprocess,datetime,uuid
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');W=Path(__file__).parent
old=Path((W/'r33_report_path.txt').read_text().strip());R=P/'reports'/('r34_four_typo_groups_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);R.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
protected=json.loads((old/'protected_manifest.json').read_text());assert all(sha(P/k)==v for k,v in protected.items())
manifest={}
for folder in ('app','tests','tools','web_chat','deployment_templates'):
 for f in (P/folder).rglob('*'):
  if not f.is_file() or '__pycache__' in f.parts or f.suffix=='.pyc':continue
  k=f.relative_to(P).as_posix();manifest[k]=sha(f);dest=R/'before'/k;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest)
for name,data in [('before_manifest.json',manifest),('protected_manifest.json',protected)]:
 with (R/name).open('x',encoding='utf-8') as out:json.dump(data,out,indent=2)
status=subprocess.run(['git','status','--short'],cwd=P,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8').stdout
with (R/'git_status_before.txt').open('x',encoding='utf-8') as out:out.write(status)
with (W/'r34_report_path.txt').open('x',encoding='utf-8') as out:out.write(str(R))
flow='''# Flow r34 — แก้ 4 กลุ่มคำผิดและตรวจวนซ้ำ

## ขอบเขต
แก้ validator ของคำถามราคา, วิธีชำระที่เสียคำจอง, คำพูดกับปฏิเสธที่ผิดพร้อมกัน, และกติกา/จำนวนผู้เล่นที่ผิดพร้อมกัน ใช้แหล่งเดิม ไม่แก้นโยบายหรือ Gold งานเก็บสถานะจองจริงยังพัก

## วิธีทำแต่ละรอบ
1. อ่าน source และ trace ก่อนตั้งคำตอบคาดหวัง; แยกเนื้อหาจาก route/status
2. เตรียม clean/noisy/ประโยคใหม่ และคำจริง/คำปฏิเสธ/เลข/ชื่อ/คำถามหลายส่วนเป็น controls
3. รัน baseline → ระบุว่าหลุดที่ recovery, frame, routing, source หรือ validator
4. เปลี่ยนเฉพาะสาเหตุที่มีหลักฐาน โดยคง validation และบันทึกการแก้ทุก span
5. ทดสอบคำตอบกับเนื้อหาและแหล่งจริง วิเคราะห์ failed ใหม่แล้วปรับ flow ก่อนรอบต่อไป

## ลำดับวงรอบ
A. ราคา: comparative price + ทุกบริการที่ระบุ ต้องใช้ price frame แม้คำนำเสีย; ไม่เปลี่ยนคำถาม compare อุปกรณ์ธรรมดาเป็นราคา
B. ชำระ: วิธีชำระมีหลักฐานอิสระ ไม่สะกดคำจริง ของ เป็น จอง แบบทั่วประโยค แยก bank transfer/booking transfer/deadline/ยอดเงิน
C. คำพูด: กู้คำบอก speech และ spelling ของปฏิเสธเฉพาะกรอบที่รองรับ; ห้ามเพิ่ม/ลบ ไม่ ในข้อความที่ไม่มีหลักฐาน
D. การแข่งขัน: เจอ target ที่ลงทะเบียนก่อนกู้ศัพท์กติกา/จำนวน; ไม่แก้ชื่อหรือปีเพื่อยืมข้อกฎ และไม่แทน roster ด้วย 5v5 เมื่อไม่มี roster source
E. ประโยคใหม่/controlled mutation: ทบทวนข้อผิดใหม่พร้อม negative และ compound controls; แก้เมื่อยืนยันสาเหตุได้

## Gates ก่อนเปลี่ยนเว็บ
source/content fixtures; negative literal/meaning; existing unit + meaningful regression; ทั้ง 2,000 clean/noisy pairs และ affected corpus; HTTP ของ package ใหม่พร้อม LLM/semantic profile; preservation hashes; เปิด8090เฉพาะหลังตรวจผ่าน เก็บผลทุกวงรอบ/failed แยก ไม่อ้าง full fresh หากเป็น replay

## การตรวจ flow
ก่อนแก้แต่ละรอบและหลังผลใหม่ ตรวจ scope/negation/ambiguity/source/edition/compound/grader/provenance/dirty files/deployment รวม 10หัวข้อ บันทึกผลจริง ไม่สร้างชื่อรอบทบทวนที่ไม่ได้ทำ
'''
with (R/'FLOW_R34_INITIAL_TH.md').open('x',encoding='utf-8') as out:out.write(flow)
print(json.dumps(dict(report=str(R),snapshot_files=len(manifest),protected=len(protected)),ensure_ascii=False))
