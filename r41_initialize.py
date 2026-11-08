import json,hashlib,shutil,uuid
from datetime import datetime
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/('r41_task_memory_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);OUT.mkdir()
with (BASE/'r41_current_path.txt').open('x',encoding='utf-8') as f:f.write(str(OUT))
manifest={}
for folder in ('app','web_chat','deployment_templates','tests'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            rel=p.relative_to(ROOT);dest=OUT/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
            manifest[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for rel in ('booking_dashboard/center_schedule.json','data/curated/service_policy_answers.json','data/competition_rules/competition_rule_chunks.jsonl',
            'data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','app/calculator/service_fee.py'):
    manifest[rel]=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
with (OUT/'before_manifest.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,indent=2)
flow='''# Flow r41: parent task memory / scope / task coverage

## ขอบเขต

ทำ B007/B008/B010/B011/B055/B062 และเกณฑ์ B041 ต่อจาก r40.3. ไม่รัน full corpus ไม่เปลี่ยน fact เจ้าของ ไม่สลับ calendar D: โดยเดา และไม่เปลี่ยนพฤติกรรม Refresh/Clear. เก็บ backup/raw/release ใหม่ทั้งหมด

## ขั้นทำจริง

1. Baseline multi-turn TH/EN บนเว็บ r40.3: all หลังควบคุม, กลับไปงานเก่า, ordinal choices, ambiguous scope และ partial compound
2. เพิ่ม parent memory schema ของ requested tasks แยก domain/operation/targets/query/price filters/provenance/response ID; bounded ≤8 tasks และใช้ TTL/session/revision เดิม
3. Harvest เฉพาะงานจาก server-completed response + user/resolved query; ไม่อนุมานเป้าหมายจาก assistant examples หรือ client fallback
4. Resume เฉพาะ explicit return-to-domain marker; ถ้าไม่ระบุ operation ชัดหรือมีหลายงานที่ตรง ให้ clarification ไม่เลือกงานแรกตามใจ
5. ใช้ archived question เป็นคำขอใหม่ผ่าน pipeline; ไม่ส่ง cached answer โดยเฉพาะ booking. ตรวจ client acknowledgement ก่อนใช้ generic memory
6. Bare all ใช้ latest eligible task เมื่อ scope ชัด: controls ของเกมที่ผู้ใช้เลือก; catalog ทุกโซนเมื่อขอ all zones; family explicit offered choices ไม่ถือ example list เป็น selected. กรณีหลายมิติ/ไม่มีเป้าหมายให้ถามเฉพาะที่ขาด
7. Ordinal selectors ใช้ได้เฉพาะ explicit offered choices พร้อมลำดับที่ผู้ใช้เห็น; ordinary catalog ที่มีทั้ง zone/game ถามยืนยัน ไม่เดาว่าอันแรกคืออะไร
8. Compound task contract แยก executed/answered/partial/clarification/missing/unavailable/invalid; parent complete ต้องไม่มี child unanswered. Contract นี้พิสูจน์ task execution ไม่ใช่ความครบของ facts ทุก clause
9. API/log/decision artifact ใช้ contract ที่มีชนิดชัด ไม่นำ price contract ไปใช้กับทุก domain; parent adapter และ source harness ต้องใช้เส้นทางเดียวกัน
10. Targeted + negative + regression: new explicit question, negation/edition, expiry, cross-session, late completion, retry, unacknowledged response, ambiguous return, single-vs-compound. ตรวจ contents/child outcomes ไม่ใช้ชื่อในหัวคำถามเป็น gold
11. สร้าง candidate ใหม่, hash/source parity, เปิด local LLM+RAG จริง, ทดสอบ HTTP และแก้จาก failure ที่พบ
12. รายงาน actual results/remaining limits; independent new cases ที่นำมาแก้แล้วต้องเปลี่ยนสถานะเป็น regression

## Review ก่อนลงมือ

- Memory เก็บคำขอไม่ใช่ความจริง; ข้อมูลสดต้อง lookup ใหม่
- Resume ไม่เกิดจาก bare device/game title หลังเปลี่ยนหัวข้อ: ต้องมี explicit return marker
- Price filters แยกจาก generic tasks; ราคา/นโยบายเดิมไม่ถูกแก้
- Client fallback ไม่สามารถสร้าง archived memory และ acknowledgement ไม่เท่ากับ source verification
- unknown targets/edition/partial outcome ต้องถูกเก็บแยกจาก successful lookup
- ไม่มี persistent personal memory หรือ auto-start ใหม่จากคำขอนี้

หลักการจาก CheckList/CheckDST/SGD ที่อ้างใน Flow r40: ทดสอบ invariance/directional behavior และ schema-based state. ใช้ผลโครงการเองเป็นหลักฐาน ไม่ใช้คะแนน paper แทน tests
'''
with (OUT/'FLOW_R41_INITIAL.md').open('x',encoding='utf-8') as f:f.write(flow)
print(OUT,len(manifest))
