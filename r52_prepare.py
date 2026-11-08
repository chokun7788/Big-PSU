import hashlib, json, shutil, subprocess, urllib.request
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
ROOT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT = BASE / ('r52_research_flow_' + datetime.now().strftime('%Y%m%d_%H%M%S'))
OUT.mkdir()
(BASE / 'r52_current_path.txt').write_text(str(OUT), encoding='utf-8')
files = []
for folder in ('app', 'web_chat', 'tests', 'data/curated', 'data/rules', 'booking_dashboard'):
    for p in (ROOT / folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc', '.log') and 'logs' not in p.parts:
            files.append(p)
hashes = {}
for p in files:
    rel = p.relative_to(ROOT)
    hashes[rel.as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    dest = OUT / 'before' / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)
(OUT / 'before_hashes.json').write_text(json.dumps(hashes, indent=2), encoding='utf-8')
git = subprocess.run(['git', '-C', str(ROOT), 'status', '--porcelain'], capture_output=True, text=True)
(OUT / 'git_status_before.txt').write_text(git.stdout + git.stderr, encoding='utf-8')
try:
    with urllib.request.urlopen('http://127.0.0.1:8091/health', timeout=5) as r:
        (OUT / 'health_before.json').write_bytes(r.read())
except Exception as exc:
    (OUT / 'health_before_error.txt').write_text(str(exc))
flow = '''# Flow และบันทึกการพัฒนา r52

วันที่ 2026-10-09 · อ้างอิงงานวิจัยใน paper-search-results/20261009_181825_llm-serving-answers

## เกณฑ์วัด

แยก HTTP สำเร็จ, routing ตรงเจตนา, โมเดลจบ, ตอบครบรูปแบบ, เนื้อหาถูก, และเวลาตามเป้าหมายออกจากกัน ทุก loop ต้องมีผลก่อน/หลังและไฟล์ดิบ ไม่รันชุดเต็ม 20,000 เคส ไม่เปลี่ยนข้อมูลเจ้าของโดยเดา

## ลำดับลงมือ

1. Loop 1 — เก็บ baseline ของ frame rate/each box/across/งานเขียนและแปล แล้วแก้ routing และตัวตรวจชนิดคำตอบ ตรวจคำถามราคาจริงเป็น negative control
2. Loop 2 — ตรวจ format ของ steps/สองประโยค/การแปล/คำขอความยาว แก้ budget และ coverage ของรูปแบบ เก็บเหตุผล output ไม่ครบแยกจาก provider ใช้ไม่ได้
3. Loop 3 — ทดสอบผ่าน pipeline และเว็บจริงด้วยคำถามหลายสำนวน ตรวจ metadata เมื่อ timeout และเมื่อ stream ไม่จบ แก้เฉพาะสาเหตุที่ reproduce ได้
4. Loop 4 — ตรวจหลาย worker และ model gate สร้าง shared admission ที่ไม่เพิ่ม GPU concurrency โดยเดา ทดสอบสถานะผิดพลาดและเส้นทางใกล้เคียง สรุปข้อจำกัดพร้อมปรับ Flow

## Flow คำขอ

รับ raw + session/turn → ตรวจบริบท/ขอบเขต → แยกงานทั่วไปออกจากข้อเท็จจริงศูนย์ → อ่านแหล่งข้อมูลที่ตรง → เลือกรูปแบบและ budget ตามคำขอ → admission โมเดล → generate พร้อม deadline/TTFT/provider_done → ตรวจ coverage/ชนิด/ข้อเท็จจริง → ส่งคำตอบหรือเหตุผลที่ไม่สำเร็จ → commit ประวัติตามกลไกเดิม

## แผนรองรับคนพร้อมกัน

เริ่มจากแก้คอขวดที่ยืนยันได้และ admission รวมหลาย worker ก่อน งานคิวแบบ job API ต้องมี persist-before-ACK, idempotency, session ordering, deadline/cancel และ recovery หลัง restart ครบก่อนเปิดใช้ ห้ามเรียกคิวในหน่วยความจำว่า durable หรืออ้างว่าเพิ่ม workers แล้วตอบ LLM พร้อมกันได้บน GPU นี้

## การรักษาไฟล์

snapshot source/tests/data ก่อนแก้ + SHA256 อยู่ใน before/ และ before_hashes.json ผลใหม่อยู่ในโฟลเดอร์นี้เท่านั้น Git status ถ้าใช้ไม่ได้ให้ระบุข้อจำกัด ห้าม reset/revert/ลบ log

## สถานะเริ่มต้น

ยังไม่ถือว่า loop ใดผ่านจนมีผลการทดสอบจริง ขั้นที่ต้องใช้ GPU/หลายคนจะรายงานจำนวนคำตอบที่ผ่านเนื้อหาและจำนวน request ที่เสร็จแยกกัน
'''
(OUT / 'FLOW.md').write_text(flow, encoding='utf-8')
print(OUT)
print('snapshotted', len(files), 'files')
