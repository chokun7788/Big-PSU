import json,hashlib,subprocess,shutil,uuid
from datetime import datetime
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');root=Path(__file__).parent
r=p/'reports'/('r31_question_target_content_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);r.mkdir()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
before={}
for folder in ['app','tests']:
    for f in (p/folder).rglob('*.py'):
        rel=f.relative_to(p).as_posix();before[rel]=sha(f);dest=r/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest)
old=Path((root/'r30_report_path.txt').read_text().strip());protected=json.loads((old/'protected_manifest.json').read_text(encoding='utf-8'))
assert all(sha(p/rel)==digest for rel,digest in protected.items()),'Owner data changed since prior audit; review before implementation.'
for name,data in [('before_manifest.json',before),('protected_manifest.json',protected)]:
    with (r/name).open('x',encoding='utf-8') as out:json.dump(data,out,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=p,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (r/'git_status_before.txt').open('x',encoding='utf-8') as out:out.write(status)
with (root/'r31_report_path.txt').open('x',encoding='utf-8') as out:out.write(str(r)+'\n')
flow='''# Flow r31 — กู้เป้าหมายและตอบสิ่งที่ถามครบ

## ขอบเขตและหลักฐาน

แก้ source-backed venue/timeout และชื่อเกมพิมพ์ผิดจากผล r30 G6 ข้อมูลเจ้าของ 584 ไฟล์/Gold/log เดิมเก็บไว้ Snapshot ทุกไฟล์ app/tests และ Git status ก่อนแก้ ไม่เปลี่ยนนโยบายของเอกสารที่ขาดหรือขัดกัน

## ลำดับลงมือและ gate

1. สร้าง fixtures จากข้อ source เดิม เก็บ baseline พร้อมคำถาม/คำตอบ/trace; ไม่ใช้ source ID เพียงอย่างเดียวรับรองเนื้อหา
2. กู้ชื่อเกมทั้งช่วงจาก registry: bounded edit distance ที่รองรับเบิ้ล/ขาด/สลับ/ผิด เฉพาะบริบทกฎ ใช้ชื่อยาว ไม่แก้ short IDs/เลขภาค/รุ่นโรมัน ชื่อกำกวมต้องถาม ไม่เพิ่ม whole-question aliases
3. กู้ก่อน generic replacement; รักษา raw span, original input, alias, edit count และเหตุผลให้ trace; ไม่สร้างชื่อครึ่งไทยครึ่งอังกฤษ
4. ตีความ venue และ timeout แบบผูกเกม: timeout คือประเด็นหลัก ในวลี during/ตอน Freeze time ให้ Freeze time เป็นเงื่อนไข แต่การถาม round time แยกต้องยังตอบได้ ทั้ง tactical/technical และหลายเกมต้องคงแยก
5. สร้าง requested-clause ledger จากโจทย์ ตรวจจำนวนครั้ง/เวลา/เงื่อนไข/สถานที่กับ literal source และ localization ที่ hash ตรง; คำตอบไม่ครบต้องถูก validator ปฏิเสธ ไม่ใช้ confidence สูงแทนเนื้อหา
6. Focused TH/EN positive + negative/mutation controls → units ทั้งหมด → clean/noisy ชุด 2,000 คู่และ corpus ทั้งหมด 20,327 requests → เปรียบเทียบข้อที่เคยผ่านใหม่ตกและแยก deadline/metadata/content
7. API จริง fixture ใหม่ + strong competition728 + focusedเดิม/locale → package hash/preservation → สลับเฉพาะเว็บของงานนี้ → post-release/API/live-path/idle concurrency ตรวจแยกตามความจำเป็น
8. วิเคราะห์ผลใหม่ ปรับ Flow ตามสิ่งที่พบและเก็บผลเดิมทุกระยะ; ปัญหา source/Gold/load ที่ยังไม่แก้ต้องระบุขอบ ไม่เรียก all-green เป็นความแม่นยำทุกคำถาม

## การทบทวนแผนก่อนทำ

- ไม่ลด threshold ทั้งระบบเพื่อแก้ชื่อไม่กี่คำ: ทำ unique source-name span recovery มีเลขและ unsupported-game controls
- ไม่เพิ่ม alias ให้ทุกประโยค: เพิ่มตัวจับ proposition และรักษา source-bound answer
- Validator ต้องเริ่มจากสิ่งที่ถาม ไม่เริ่มจากสิ่งที่ matcher เลือกตอบเท่านั้น มิฉะนั้นจะไม่เห็นเรื่องที่ตกหล่น
- ไม่ลบเกณฑ์เก่า: เก็บ original scores และ source/content diagnostics แยก
- คิว503: วัด idle/load แยก ไม่เปลี่ยน worker/RAM โดยเดา; real booking oracle ยังพักตามผู้ใช้

## สิ่งที่ต้องให้เจ้าของยืนยัน

Tekken pause exceptions/โทษ, ประโยค RoV 6.1.5.1 ที่ถูกตัด, ความมีผลของ rulebook แต่ละปี, นโยบายภาพ/วิดีโอ/ค่าสมัคร/อายุที่ไม่มี ไม่เติมข้อมูลเหล่านี้เอง

## ผลและการปรับหลังลงมือ

เติมหลังมีผลจริง พร้อมจำนวนตรวจ/ผ่าน/ยังผิดและ trace ไม่อ้างว่าทุกสำนวนหรือทั้ง117คู่ต้องแก้ได้ด้วยสาเหตุเดียว
'''
f=p/'docs/131_question_target_content_r31_flow_20261002.md'
with f.open('x',encoding='utf-8') as out:out.write(flow)
with (r/'flow_initial.md').open('x',encoding='utf-8') as out:out.write(flow)
print(json.dumps({'report':str(r),'snapshots':len(before),'protected':len(protected),'flow':str(f)},ensure_ascii=False))
