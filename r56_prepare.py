import datetime,hashlib,json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/('r56_remaining_fixes_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'));OUT.mkdir()
with (BASE/'r56_current_path.txt').open('x',encoding='utf-8') as f:f.write(str(OUT))
hashes={}
for folder in ('app','web_chat','tests','tools','data/curated','booking_dashboard'):
 for p in (ROOT/folder).rglob('*'):
  if p.is_file() and p.suffix in ('.py','.js','.css','.html','.json','.jsonl','.md','.ps1','.cmd','.bat') and not any(x in p.parts for x in ('__pycache__','logs','state','.git')):
   rel=p.relative_to(ROOT);dest=OUT/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest);hashes[str(rel)]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'hashes_before.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
owners=json.loads((BASE/'r54_shop_cases_20261009_235038/owner_hashes_before.json').read_text())
(OUT/'owner_hashes_before.json').write_text(json.dumps({k:hashlib.sha256((ROOT/k).read_bytes()).hexdigest() for k in owners},indent=2),encoding='utf-8')
(OUT/'FLOW_INITIAL.md').write_text('''# Flow r56 · ทำประเด็นค้างจาก r55

1. snapshot/source/owner hashes และตรวจ runtime ก่อนแก้
2. สร้าง contract รายคำถามทั้ง156จาก source และ intent ที่ผู้ใช้ถาม; แยก unknown/live/checked ห้ามรวมเป็น accuracy
3. ตรวจ raw r55 แบบ offline โดยระบุว่าไม่ใช่ pipeline run แล้ว HTTP baseline บนรุ่นเดียว
4. แก้ข้อผิดจริงจากคำถามใหม่: หลายส่วน/negation/entity/filters/context; ไม่เดา owner policies
5. ทดสอบ source fixtures + held-out paraphrases + TH/EN rule coverage ทุกเกม และ legacy expectations ที่มีหลักฐาน
6. วัดคิว/load/fault recovery ของ candidate แยก fast/LLM/fixture live ไม่ยิง burst WordPress
7. ปรับ deadline/queue diagnostics และ lifecycle ที่ไม่ลบ log; refresh anonymous session คงพฤติกรรมเดิม
8. ตรวจ source/data/index/hash และสร้างแพ็กเกจใหม่สองแบบในโฟลเดอร์ใหม่ตาม runtime/dependencies ที่มี
9. เก็บทุกloop ผลไม่ผ่าน/ข้อจำกัด/owner questions; reportสถานะT01–T35ตามหลักฐาน ไม่เรียกทดสอบจำกัดว่าปิดทุกสำนวน

ไม่นำ full20k หรือบทความทั่วไป500คำเป็น gateของร้านเกม ไม่เปิด public ไม่เปลี่ยนแหล่งข้อมูลเจ้าของหรือ approval เพื่อเพิ่มคะแนน
''',encoding='utf-8')
print(OUT);print('snapshot',len(hashes))
