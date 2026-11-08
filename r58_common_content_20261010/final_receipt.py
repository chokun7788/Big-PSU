import json,hashlib,sqlite3
from pathlib import Path
OUT=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');PACK=OUT/'ready_package/PSU_Esports_Chatbot_Local'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((OUT/'source_hashes_before.json').read_text());plan=json.loads((OUT/'source_apply_plan.json').read_text())
changed=[];unexpected=[];missing=[]
for rel,h in baseline.items():
    p=ROOT/rel
    if not p.is_file():missing.append(rel)
    elif sha(p)!=h:(changed if rel in plan['existing_files'] else unexpected).append(rel)
common_mismatch=[]
for p in (PACK/'app/knowledge/common').rglob('*'):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc':continue
    rel=p.relative_to(PACK)
    if not (ROOT/rel).is_file() or sha(p)!=sha(ROOT/rel):common_mismatch.append(rel.as_posix())
db=sqlite3.connect((PACK/'data/knowledge/approved.sqlite').as_uri()+'?mode=ro',uri=True)
receipt={'runtime':'2026.10.10-common-r58.2','project':str(ROOT),'package':str(PACK),'chat_url':'http://127.0.0.1:8098/','owner_url_without_capability':'http://127.0.0.1:8097/','owner_open':'Open-Owner-Content.cmd','schema_kinds':24,'schema_fields':155,'tests':{'targeted_units':164,'unit_passed':True,'web_fixtures':25,'web_passed':True,'ready_smoke':6,'ready_smoke_passed':True},'production_db':{'active':db.execute("SELECT value FROM cc_meta WHERE key='active'").fetchone()[0],'drafts':db.execute('SELECT count(*) FROM cc_heads').fetchone()[0],'demo':db.execute("SELECT value FROM cc_meta WHERE key='demo'").fetchone()[0]},'source_check':{'changed_existing':changed,'unexpected_changes':unexpected,'missing':missing,'common_package_source_mismatch':common_mismatch},'notes':['Prior dirty source backed up; no Git commit/reset','Original logs retained; baseline hash excludes logs/state/vector/eval/ground_truth','Synthetic test database remains isolated in fixtures; real deployment starts with unpublished drafts','English, live occupancy, policy factual approval and concurrency have distinct evidence; not inferred from structural tests']};db.close()
(OUT/'FINAL_DELIVERY_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
md=f'''# ส่งมอบ r58.2 — ข้อมูลกลาง

## เริ่มใช้งานบนเครื่องนี้

- เว็บแชทที่เปิดพร้อมแล้ว: http://127.0.0.1:8098/
- หน้าเจ้าของข้อมูลเปิดไว้ในแท็บของแอป หากเปิดใหม่ใช้ `Open-Owner-Content.cmd` ใน `{PACK}` (ต้องมี local capability จาก launcher)
- มี Python 3.12 x64 และ validator ในโฟลเดอร์ ใช้ Ollama/โมเดลเดิมของเครื่องนี้ เครื่องอื่นยังต้องติดตั้ง Ollama และโหลดโมเดล
- `OWNER_CONTENT_GUIDE_TH.md` และโฟลเดอร์ `owner_content_docs` อยู่ในชุดใช้งาน

## ผลตรวจ

- targeted units **164/164**, เว็บ fixture **25/25**, smoke ของแพ็กเกจจริง **6/6**
- 24 หมวด / 155 fields; เพิ่มรายการผ่านฟอร์มแล้ว approve/publish อ่านได้โดยไม่เพิ่มชื่อในโค้ด
- ร่างจากข้อมูลจริง **41** รายการ, active release ยังว่าง ไม่เอาร่างไปใช้เป็นคำตอบหรืออนุมัติแทนเจ้าของ
- ตรวจ source hash: เปลี่ยนของเดิมเฉพาะ engine, supervisor, server และ builder; unexpected={unexpected}, missing={missing}; common module ในแพ็กเกจตรง source={not common_mismatch}
- รายงานความผิดพลาดทุก round เก็บไว้ รวม combined unit ครั้งแรกที่พลาดจากฐานรุ่นต้น ไม่ลบผลผิด

## ข้อจำกัดที่ยังเหลือ

คิว canonical 270 รายการย้ายเกมเป็นร่างแล้ว36 ยังมี234รายการรอ typed mapping; calculator/calendar/live ยังใช้ operational adapter เดิมในจุดที่ไม่ได้ย้าย; semantic LLM planner ยังถามเพิ่มกับบางประโยค ไม่กล่าวว่าทุกรูปแบบภาษาทำได้แล้ว ดู REMAINING_AND_DECISIONS_TH.md

ความถูกต้องจริงของสถานะสดที่ผู้ใช้ยืนยันก่อนหน้า แยกจาก fixture รอบนี้; เรื่องนโยบาย/วันที่มีผลที่ไม่มีหลักฐานยังรอตัดสินใจตามคำถามในคู่มือ

อ่าน Flow/คู่มือ/field reference/ผลทดสอบ ใน docs ของงานนี้หรือ owner_content_docs ของชุดใช้งาน ส่วน code และ schema อยู่ใน app/knowledge/common ของโปรเจกต์จริงแล้ว
'''
(OUT/'DELIVERY_TH.md').write_text(md,encoding='utf-8')
(PACK/'owner_content_docs/DELIVERY_TH.md').write_text(md,encoding='utf-8')
print(json.dumps({'unexpected':unexpected,'missing':missing,'package_source_mismatch':common_mismatch,'ready_checks':6},ensure_ascii=False))
if unexpected or missing or common_mismatch:raise SystemExit(1)
