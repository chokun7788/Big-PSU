import hashlib,json,shutil,uuid,subprocess
from datetime import datetime
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/('r43_readiness_schedule_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);OUT.mkdir()
with (BASE/'r43_current_path.txt').open('x',encoding='utf-8') as f:f.write(str(OUT))
hashes={}
for folder in ('app','web_chat','deployment_templates','tests'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            rel=p.relative_to(ROOT);dest=OUT/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
            hashes[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for rel in ('booking_dashboard/center_schedule.json','data/curated/service_policy_answers.json','data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','app/calculator/service_fee.py'):
    hashes[rel]=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
with (OUT/'before_manifest.json').open('x',encoding='utf-8') as f:json.dump(hashes,f,indent=2)
result=subprocess.run(['git','-c','safe.directory='+ROOT.parent.as_posix(),'-C',str(ROOT),'status','--short'],capture_output=True,text=True)
with (OUT/'git_status_before.txt').open('x',encoding='utf-8') as f:f.write(result.stdout+result.stderr)
with (OUT/'FLOW_R43_INITIAL.md').open('x',encoding='utf-8') as f:f.write('''# Flow r43: เปิดระบบแล้วตอบได้จริง + ตารางอังกฤษครบ

1. สำรองไฟล์และ hash ก่อนแก้ เก็บสถานะ Git; ไม่ทับ log/release เดิม
2. เลือก Python ครั้งเดียว: explicit path → bundled runtime → manifest local binding → PATH/fallback; ตรวจรุ่น/64-bit แล้วส่ง path เดิมตลอด launcher chain
3. ตรวจเว็บเก่า: version + installation + Python identity + warmup + LLM preflight + workers + POST คำถามจริงที่มี oracle ใน source
4. HTTP 200/health ok ไม่ใช่หลักฐานตอบถูก ต้องตอบจำนวนชั่วโมง/ข้อความที่ถูกและไม่ใช่ timeout/no-answer
5. เว็บเดิมที่ผิด identity/ไม่พร้อมต้องรายงานเหตุผล ไม่หยุด process ของผู้ใช้หรือสร้างอีก instance โดยเงียบ
6. Startup ใหม่เก็บ stdout/stderr และ readiness result แยก run ID; เปิด browser หลัง gates ผ่าน
7. ตารางอังกฤษแบบกว้าง render ทุกวันจาก regular_service_slots; ระบุพักกลางวัน maintenance และเงื่อนไข special closure ไม่อ้างความว่างสด
8. Fixture launcher failure/reuse + คำถามตารางหลายรูปแบบ + date/maintenance guards + regressions บริบทเดิมที่เกี่ยวข้อง
9. สร้าง release local ใหม่ immutable; ทดสอบ HTTP จริง และเปิด launcher ซ้ำตรวจ reuse
10. บันทึกผล/ข้อผิดพลาด/ข้อจำกัดและอัปเดต backlog; แยก automated pass จากข้อมูลที่ต้องเจ้าของยืนยัน

## สิ่งที่ไม่ได้รับการพิสูจน์ใน gates นี้

MemoryError มีหลักฐานทรัพยากรระบบตึงและ interpreter ต่างกัน แต่ยังสรุปไม่ได้ว่า Python รุ่นใดเป็นสาเหตุเดียว; readiness ไม่รับรองโหลดพร้อมกันหรือความถูกต้องทุกคำถาม การจองสดยังต้อง oracle จริง และ portable clean-machine ยังต้องเครื่องทดสอบ
''')
print(OUT,len(hashes))
