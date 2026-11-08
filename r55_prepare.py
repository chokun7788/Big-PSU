import datetime,hashlib,json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/('r55_service_fixes_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));OUT.mkdir()
(BASE/'r55_current_path.txt').write_text(str(OUT),encoding='utf-8')
hashes={}
for folder in ('app','tests','data/curated','booking_dashboard'):
    source=ROOT/folder
    if not source.exists():continue
    for p in source.rglob('*'):
        if p.is_file() and not any(x in p.parts for x in ('__pycache__','logs','state','.git')) and p.suffix in ('.py','.json','.jsonl','.md'):
            rel=p.relative_to(ROOT);dest=OUT/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
            hashes[str(rel)]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'hashes_before.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
flow='''# Flow แก้บริการและประวัติสนทนา r55

## หลักฐานและขอบเขต
อ้าง r54: 156 คำถามและการต่อหน้ากฎ 2 ครั้ง ไม่แก้นโยบายที่ไม่มีคำตอบ ไม่เขียนทับ source snapshot หรือ log เก่า สำรอง source และ hash ก่อนแก้

## ขั้นตอนและการตรวจทาน
1. แยกเลขเวลา/ระยะเวลา/เลขเครื่อง ตรวจขอบเลขและหน่วยทั้งภาษาไทยอังกฤษ
2. ขยายการอ่าน subject + operation ของข้อมูลที่เจ้าของตอบแล้ว รักษาปฏิเสธและขอบเขตนโยบาย เพิ่ม unknown เฉพาะค่าใช้จ่ายที่ยังไม่ทราบ
3. เก็บ customer group และจำนวนที่เขียนด้วยคำ ส่งต่อ duration เข้าตัวคิดราคาจากตารางเดิม
4. สร้าง affordability จากแพ็กเกจเดิม คำนวณเต็มแพ็กเกจและเงินเหลือ แยกราคาบันทึกจากราคาปัจจุบัน ไม่แปลงแพ็กเกจฟรีเป็นเวลาไม่จำกัด
5. แยกคำถามหลาย operation ก่อน early return ราคาหรือ policy; มี target/filter รายส่วน
6. ต่องานจากประวัติที่ใช้ได้เท่านั้น เก็บเวลา/วันที่และ scope เกมเดิม เก็บ cursor กฎที่ผู้ใช้ได้รับแล้ว
7. ตรวจ domain guards ของเกม/เวลา/สเปก/ปุ่ม ใช้ข้อมูลเดิมและ English rendering ที่ตรวจได้
8. ทดสอบ unit + fixture และคำถามเว็บที่เกี่ยวข้อง รวม negative controls วิเคราะห์ผลตาม expected content และ trace
9. วนแก้จากข้อผิดจริง ไม่เปลี่ยน expected เพื่อให้ผ่าน และตรวจ hash ไฟล์เจ้าของท้ายรอบ

## เกณฑ์รับ
transport สำเร็จไม่เท่ากับคำตอบถูก; live fixture ไม่เท่ากับสถานะจริงที่เวลาอื่น; source policy unknown ต้องแสดงว่าไม่ทราบ; full rules ต้องรวม returned IDs จนครบและไม่ซ้ำ; ภาษาอังกฤษต้องรักษาตัวเลข เงื่อนไข และ source validity

## การปรับปรุงหลังตรวจทาน
ไม่ขยาย concurrency โมเดลในรอบนี้ และไม่ใช้ LLM เดาราคา/นโยบาย เป้าหมายคือ domain/slot/coverage ที่หายจาก flow เดิม ใช้เงื่อนไข grammar + source handler ไม่ทำ alias คำถามหนึ่งต่อหนึ่ง
'''
(OUT/'FLOW.md').write_text(flow,encoding='utf-8')
print(OUT);print('snapshots',len(hashes))
