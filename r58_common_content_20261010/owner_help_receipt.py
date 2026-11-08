from pathlib import Path
import json,hashlib,sqlite3,sys,shutil
OUT=Path(__file__).resolve().parent
p=json.loads((OUT/'owner_help_latest.json').read_text(encoding='utf-8'));RUN=Path(p['run'])
PACK=OUT/'ready_package/PSU_Esports_Chatbot_Local';ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def db_status(base):
    db=base/'data/knowledge/approved.sqlite';con=sqlite3.connect(db.as_uri()+'?mode=ro',uri=True)
    tables=[r[0] for r in con.execute("select name from sqlite_master where type='table' and name like 'cc_%'")]
    counts={t:con.execute('select count(*) from '+t).fetchone()[0] for t in tables};con.close();return counts
counts={str(base):db_status(base) for base in (PACK,ROOT)}
files={name:{'ready':hashlib.sha256((PACK/'app/knowledge/common/ui'/name).read_bytes()).hexdigest(),'source':hashlib.sha256((ROOT/'app/knowledge/common/ui'/name).read_bytes()).hexdigest()} for name in ('index.html','owner.js','owner.css')}
checks=json.loads((RUN/'browser_form_checks.json').read_text(encoding='utf-8'));ser=json.loads((RUN/'serialization_checks.json').read_text(encoding='utf-8'))
report={'changed_files':files,'ready_matches_source':all(v['ready']==v['source'] for v in files.values()),'examples':json.loads((RUN/'example_validation.json').read_text(encoding='utf-8')),'ui_checks':checks,'serialization_checks':ser,'database_counts':counts,'no_owner_save_approve_publish_performed':True,'source_guide_previous_hash':hashlib.sha256((ROOT/'docs/common_content_r58/OWNER_EASY_GUIDE_TH.md').read_bytes()).hexdigest()}
(RUN/'FINAL_OWNER_HELP_RECEIPT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
txt='''# ผลปรับหน้ากรอกข้อมูลให้อ่านง่าย

## สิ่งที่เปลี่ยน

- แบ่ง 24 หมวดเป็นกลุ่มงาน และเปลี่ยนชื่อหมวด/ช่องย่อยให้เป็นภาษาหน้ากรอก
- ทุกหมวดมีคำอธิบายว่าใช้เมื่อไร ช่วยตอบคำถามใด ข้อมูลใดต้องสร้างก่อน และรายการช่องที่จำเป็นก่อนเผยแพร่
- มีตัวอย่างประกอบครบ 155 ช่อง เป็นตัวอย่างแสดงอย่างเดียว ไม่กรอกลงข้อมูลจริงอัตโนมัติ
- ช่องราคาหน้าเว็บกรอกเป็นบาท เช่น 35.50; เก็บข้อมูลเดิมเป็น 3550 สตางค์ ไม่เปลี่ยน schema ราคา
- ช่องชื่อวันเลือกเป็นชื่อไทย ไม่ต้องจำเลข 0–6
- ช่องข้อมูลอ้างอิงเลือกจากชื่อรายการ และแจ้งเมื่อยังไม่มีรายการให้เลือก
- เปลี่ยนหมวดแล้วมีร่างไม่บันทึก จะถามก่อนออก; ยกเลิกแล้วเก็บค่าที่กรอกไว้
- เพิ่มคู่มือภาษาใช้งานพร้อมตัวอย่างทุกหมวดและงานที่ต้องใช้หลายหมวด

## ผลตรวจอัตโนมัติและหน้าจอ

- ตัวอย่างตรง schema ของค่า: 155/155 ช่อง ไม่มีข้อผิดพลาด (ไม่ใช่การยืนยันว่าเป็นข้อเท็จจริงของศูนย์)
- ตรวจหน้าเว็บจริง 24/24 หมวด: จำนวนช่องและตัวอย่างตรงกัน สถานะเริ่มต้นไม่ทราบ ช่องข้อความและราคายังว่าง ไม่มีตัวอย่างถูกเติมเป็นข้อเท็จจริง
- ทดสอบตัวแปลงราคา/รักษาค่าเดิม/ชื่อวัน 25/25: 35→3500, 35.50→3550, 4000→400000, ค่าศูนย์เดิมไม่เปลี่ยน, ไม่ทราบยังว่าง; ปฏิเสธจำนวนลบ/ทศนิยมเกิน/comma ผิดตำแหน่ง/ค่าล้น
- ตรวจ JavaScript syntax ผ่าน
- ลองกรอก 35.50 ในหน้าเว็บและยกเลิกการเปลี่ยนหมวด ค่าและหมวดเดิมยังอยู่
- สำรองไฟล์เดิมก่อนแก้ และใช้ hash ตรวจความเปลี่ยนแปลงก่อนลงโปรเจกต์จริง ไฟล์ UI ในพร้อมใช้กับโปรเจกต์จริงตรงกัน

## สิ่งที่ยังไม่อ้างว่าผ่าน

- คำสั่งรอเหตุการณ์ดาวน์โหลด JSON ในเบราว์เซอร์หมดเวลา จึงไม่อ้างว่าดาวน์โหลดไฟล์ผ่าน UI ได้แล้ว ตัวแปลงหน่วยทดสอบแยกผ่าน แต่การดาวน์โหลดต้องตรวจอีกครั้งหากผู้ดูแลต้องใช้
- ความง่ายในการใช้สำหรับเจ้าของจริงยังไม่ได้ทดลองกับมนุษย์ ผลด้านบนเป็นการตรวจโดยระบบและการดูหน้าจอ
- ไม่ได้บันทึก อนุมัติ หรือเผยแพร่ข้อมูลสมมุติในฐานจริง จำนวนร่างยัง 41 รายการ ไม่มี release ใหม่
- ไม่ได้รัน full Ground Truth รอบนี้ เพราะเปลี่ยนหน้ากรอกและหน่วยรับราคาของ UI เท่านั้น
- ตารางเวลา/เครื่องคิดราคา/สถานะสดบางเส้นทางยังใช้ตัวอ่านเดิมร่วมด้วยตามข้อจำกัด r58.2 เดิม

## ไฟล์และหลักฐาน

สำเนาเดิมอยู่ใน before/ready, before/candidate, before/source ของรอบนี้ ผลละเอียดอยู่ใน browser_form_checks.json, example_validation.json, serialization_checks.json, FINAL_OWNER_HELP_RECEIPT.json และภาพ owner_guide_screen.png / owner_example_screen.png
'''
(RUN/'OWNER_HELP_CHANGES_AND_CHECKS_TH.md').write_text(txt,encoding='utf-8')
if '--sync-docs' in sys.argv:
    dest=ROOT/'docs/common_content_r58/OWNER_EASY_GUIDE_TH.md'
    if hashlib.sha256(dest.read_bytes()).hexdigest()!=report['source_guide_previous_hash']:raise SystemExit('Guide changed during review')
    backup=RUN/'source_guide_before_readability_revision.md'
    if backup.exists():raise SystemExit('Backup already exists; do not overwrite')
    shutil.copy2(dest,backup);shutil.copy2(RUN/'OWNER_EASY_GUIDE_TH.md',dest)
print(json.dumps({'matches':report['ready_matches_source'],'heads':{k:v.get('cc_heads') for k,v in counts.items()},'releases':{k:v.get('cc_releases') for k,v in counts.items()},'run':str(RUN)},ensure_ascii=False))
