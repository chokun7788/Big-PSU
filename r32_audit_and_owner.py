import json,sys,hashlib,collections
from pathlib import Path
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path((ROOT/'r32_report_path.txt').read_text().strip());sys.path.insert(0,str(P))
from app.pipeline.retrieval import load_curated_rows
from app.knowledge.localization import approved_localization,active_registry_path
rows=[r for r in load_curated_rows() if r.get('id') and not r.get('_canonical_projection')]
competition=[r for r in rows if str(r['id']).startswith('competition_rules_')]
coverage=[]
for row in competition:
 text=approved_localization(row,'text')
 coverage.append(dict(id=row['id'],source_sha256=hashlib.sha256(str(row.get('text','')).encode()).hexdigest(),english_available=text is not None,english_sha256=hashlib.sha256(text.encode()).hexdigest() if text else None,owner_content_validity='not_confirmed_by_this_audit'))
registry=active_registry_path();records=[json.loads(l) for l in registry.read_text(encoding='utf-8').splitlines() if l.strip()]
audit=dict(competition_rows=len(coverage),hash_valid_english=sum(r['english_available'] for r in coverage),missing_or_stale=[r['id'] for r in coverage if not r['english_available']],registry_sha256=hashlib.sha256(registry.read_bytes()).hexdigest(),by_recorded_reviewer=dict(collections.Counter(r.get('approved_by','') for r in records)),scope='approved localization in code means registry status and source hash; this run does not establish human owner approval, edition validity or translation quality for all rows',rows=coverage)
with (R/'R32_ENGLISH_SOURCE_AUDIT.json').open('x',encoding='utf-8') as out:json.dump(audit,out,ensure_ascii=False,indent=2)
owner='''# คำถามที่ต้องให้เจ้าของ/ผู้จัดยืนยัน — r32

## 1. กติกา Tekken 8 การหยุดเกม
- เอกสารมีทั้งห้ามหยุดหลังเริ่มเกม และหยุดได้เมื่อทุกคนยินยอม: ข้อยกเว้นที่ใช้จริงคืออะไร ต้องได้รับอนุญาตจากกรรมการด้วยหรือไม่?
- หยุดโดยไม่ได้รับอนุญาตให้แพ้รอบ แพ้เกม หรือแพ้แมตช์? โปรดระบุข้อกฎฉบับที่ใช้และวันที่มีผล
- ระหว่างรอ ระบบแสดงข้อความขัดกัน ไม่เลือกข้อใดเป็นนโยบายเอง

## 2. ข้อกฎต้นฉบับที่จบไม่ครบ
- โปรดส่งข้อความฉบับเต็มของข้อที่ระบบรายงานว่าไม่ครบ พร้อมชื่อเกม/รายการ/เลขข้อและไฟล์ต้นฉบับ
- ไม่ต่อประโยคส่วนที่หายโดยเดา; ดูเหตุผล source_clause_incomplete ในผลทดสอบเดิม

## 3. ข้อมูลที่ไม่ได้ระบุในกติกา
- แต่ละรายการมีค่าสมัครหรือไม่ เท่าไร? มีอายุขั้นต่ำหรือไม่? ต้องแยกจากคุณสมบัตินักศึกษา
- RoV 5v5 ยืนยันจำนวนผู้เล่นในเกม แต่ลงทะเบียนรวมสำรองได้กี่คนและแก้รายชื่อได้ถึงเมื่อไร?
- โปรดระบุฉบับกติกา/วันที่มีผลสำหรับ CS2 2026, VALORANT 2026, RoV Blueket 2025 ทีมชาย และ Tekken 8 ที่จะนำไปใช้งานจริง

## 4. นโยบายสตูดิโอที่ยังไม่มีหลักฐาน
- ถ่ายรูป/วิดีโอได้หรือไม่ ต้องขอความยินยอมจากใคร และมีบริเวณใดจำกัดการถ่าย?
- การตอบจากเอกสารที่มีไม่ใช่การยืนยันว่าใช้กับทุกรายการในอนาคต

## 5. ตรวจคำแปลภาษาอังกฤษ
- ขอผู้ตรวจยืนยันศัพท์กติกา เงื่อนไขตัวเลข ข้อยกเว้น และขอบเขตรายการจากต้นฉบับเดียวกัน
- การผ่าน source hash หรือ registry ที่ระบุ approved ไม่ใช่หลักฐานว่าผู้จัดได้ยืนยันเนื้อหาทุกรายการ

## 6. สถานะจองจริง — พักตามคำสั่งผู้ใช้
- เมื่อพร้อมจึงเก็บวันที่/เวลาประเทศไทย/เครื่อง/ช่วงเวลา/สถานะที่เจ้าหน้าที่รู้จริง และเวลาที่ดึงข้อมูล
- ส่งเฉพาะสถานะรวมและ hash หลักฐาน ห้ามแนบชื่อ/เบอร์/อีเมลลูกค้า
- การเชื่อม API สำเร็จไม่ได้พิสูจน์ว่าสถานะว่าง/ถูกจองตรงกับของจริง
- รอบนี้เตรียม template และตัวตรวจเท่านั้น ไม่เก็บสถานะจริงและไม่สร้างรายการจอง
'''
with (R/'OWNER_QUESTIONS_TH.md').open('x',encoding='utf-8') as out:out.write(owner)
template=dict(schema_version='booking-oracle-r32-v1',collection_status='paused_by_user',transport=dict(http_ok=None,snapshot_source=None,raw_aggregate_sha256=None,observed_at_bangkok=None),oracle=dict(confirmed_by=None,confirmed_at_bangkok=None,date=None,observed_resources=[]),example_row=dict(resource_id='EXAMPLE_ONLY',start='10:00',end='11:00',expected_status=None,expected_available_count=None),privacy='aggregate resource/slot only; no customer identifiers',grade='pending_no_real_oracle')
with (R/'REAL_BOOKING_ORACLE_PENDING_TEMPLATE.json').open('x',encoding='utf-8') as out:json.dump(template,out,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in audit.items() if k!='rows'},ensure_ascii=False))
