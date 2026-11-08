import json,sys
from pathlib import Path
from collections import Counter
root=Path(__file__).parent
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
sys.path.insert(0,str(project))
from tools.run_competition_composition_r28 import check
cases=json.loads((report/'composition_fixture_v3.json').read_text(encoding='utf-8'))['cases']
case_by_id={c['id']:c for c in cases}
def rows(name):return [json.loads(x) for x in (report/name).read_text(encoding='utf-8').splitlines() if x.strip()]
baseline=rows('baseline_r27_details.jsonl')+rows('baseline_extra24_details.jsonl')
candidate=rows('candidate_B_details.jsonl')
after={r['id']:r for r in candidate}
rescored=[]
for r in baseline:
    errors=check(case_by_id[r['id']],r['response'])
    rescored.append(dict(r,failures_v3=errors,passed_v3=not errors))
audit={'total':len(rescored),'passed':sum(r['passed_v3'] for r in rescored),'original_passed':sum(r['passed'] for r in baseline),'failure_types':dict(Counter(f.split(':')[0] for r in rescored for f in r['failures_v3'])),'oracle':'v3 frozen source clauses; original logs retained; no rerunning old engine with changed code'}
with (report/'baseline_v3_rescore.json').open('x',encoding='utf-8') as f:json.dump(dict(audit,records=rescored),f,ensure_ascii=False,indent=2)
lines=['# วิเคราะห์สาเหตุ r28 จากคำถามจริงในชุดทดสอบ','', '## การอ่านผล','',f"Baseline r27 เมื่อใช้เกณฑ์ v3 เดียวกัน: {audit['passed']}/{audit['total']}; หลังแก้ Candidate B: 280/280. เกณฑ์ 3 ข้อถูกแก้เพราะเดิมเรียก clause Cypher ที่คำถามไม่ได้ถาม ไม่ใช่แก้เกณฑ์ตามคำตอบผิด; ดู oracle_revision_audit.json. การทดสอบเป็นคำถามที่สร้างเพื่อพัฒนา ไม่ใช่คำถามผู้ใช้จริงหรือ owner signoff.",'','## สาเหตุและลำดับแก้','',
'1. เลือกหัวข้อหรือ clause ผิด: ค่าสมัครถูกตีเป็น late_registration, final decision ถูกตีเป็น final match; เสี่ยงตอบข้อมูลผิดแม้มีแหล่งอ้างอิงของเกมถูกต้อง.',
'2. ตอบขัดกันหรือยืมข้ออื่น: Tekken pause เริ่มด้วยอนุญาตก่อนเห็นข้อห้าม, RoV ข้อที่ขาดใช้บทลงโทษข้างเคียง; เพิ่มสถานะ conflict และจับเลขข้อแบบ exact.',
'3. คำถามหลายเรื่องตกหล่น: exclude ตรวจทั้งประโยคแล้วตัดหัวข้อ normal money/overtime, language/protest, map pool/mapban; แยกเงื่อนไขตามประเด็นที่ถาม.',
'4. ประเด็นเฉพาะไม่มีตัวเลือก clause: เพิ่มแนวคิดทั่วไปสองภาษา เช่น bug, stream, install, macro, prep, drinks, custom settings จาก source เดิม ไม่ใช้ alias ทั้งประโยค.',
'5. คำอังกฤษของ source แตกต่างกับ pattern: clause macro/customization มีข้อความอังกฤษที่ถูกต้องแต่ไม่ผ่าน pattern จึงตกไปหัวข้อกว้าง; ขยายตามข้อความที่อนุมัติและ hash ตรง.',
'6. การตรวจคำตอบ: ประโยค no-answer ใหม่ต้องเข้า contract; คำตอบ partial ยังต้องตรวจ source ของเกม ไม่ให้ข้อความ “ไม่พบ” ทำให้ข้าม evidence gate.',
'7. เกณฑ์ตรวจละเอียด: source presence หรือ route ถูกไม่ได้ยืนยันเงื่อนไขครบ; ใช้ complete clauses + first line + game evidence และบันทึก raw/source-grade แยก.',
'','## คะแนนและเหตุผลที่เลือก','',
'เส้นทางรายละเอียดใช้เงื่อนไขจับแนวคิดและรูปประโยค ไม่ได้ให้ LLM สุ่มเลือก clause. ค่า confidence 0.97 ใน trace เป็นค่าที่ตั้งให้เส้นทางนี้เมื่อผ่านเงื่อนไข ไม่ใช่ความน่าจะเป็นที่สอบเทียบแล้ว. การเลือก row ใช้จำนวน clause ที่ตรงแนวคิดและลำดับ source; เมื่อไม่มีรายละเอียดครอบคลุมจะตกไปเส้นทาง facet/retrieval ซึ่งอาจได้หัวข้อกว้าง. การเปลี่ยนค่า confidence อย่างเดียวจึงแก้ความผิดของการตีประเด็นไม่ได้. ด้านล่างเก็บ trace ที่นำไปสู่คำตอบจริงพร้อมคำที่ควรปรากฏ.',
'','## แยกทุก anchor ที่ผิดใน baseline','']
seen=set()
for r in rescored:
    if r['passed_v3'] or r['anchor'] in seen:continue
    seen.add(r['anchor']);c=case_by_id[r['id']];a=after[r['id']]
    lines += [f"### {r['anchor']} ({c['locale']})",'',f"คำถาม: {r['question']}",'',f"ชนิด: {c['kind']} / ผลที่ควรเป็น: {c['status']}",'','เกณฑ์ที่ขาด: '+', '.join(r['failures_v3']),'','คำตอบก่อนแก้:','','```text',r['response'].get('answer',''),'```','']
    if c.get('clauses'):
        lines+=['เนื้อหาที่ควรปรากฏครบจาก source:','']+['- '+x for x in c['clauses']]+['']
    if c.get('sources'):lines+=['Source IDs: '+', '.join(c['sources']),'']
    selected=[t for t in r['response'].get('trace',[]) if any(w in str(t.get('stage','')) for w in ('competition','retriev','route','validator'))]
    lines+=['Trace ที่เกี่ยวข้อง:','','```json',json.dumps(selected,ensure_ascii=False,indent=2),'```','', 'คำตอบหลังแก้:','','```text',a['response'].get('answer',''),'```','',f"ผลหลังแก้: {'ผ่าน' if a['passed'] else a['failures']}",'']
lines+=['## ขอบเขตและสิ่งที่ยังไม่ยืนยัน','',
'- 280 ข้อนี้ตรวจ 28 ประเด็นเดี่ยว, 16 คู่ประเด็น, 8 controls ต่อภาษา. ไทย/อังกฤษมี clean, คำสุภาพ และ task typo; ไม่ได้พิสูจน์ typo ทุกคำหรือทุกคำถามหลายเรื่อง.',
'- คำถามหลายเกม,หลายข้อที่ระบุเลข,เงื่อนไขมากกว่าสองส่วน และรายละเอียดที่ยังไม่มีตัวจับ ต้องทดสอบเพิ่มจาก log ผู้ใช้จริง. กรณี missing age ปัจจุบันยังตอบ no-answer ตาม guard เดิมเมื่อคำถามมี age ร่วมกับ eligibility.',
'- การอ่านเลข/ราคาในอนาคตมีขอบเขต: parser ยังต้องมีตัวเลขชัดเจน ไม่ได้ยืนยันเงื่อนไขทุกแบบของค่าธรรมเนียม waived/free. source ปัจจุบันไม่มีราคาเหล่านี้.',
'- ค่า 0.97 ไม่ใช่คะแนนความถูกต้องจริง; complete-clause pass ก็ไม่ใช่ owner approval ของนโยบายหรือผลเทียบผู้ตัดสิน.',
'- Tekken pause, RoV 6.1.5–6.1.5.1 และ V2 104 ต้องให้ผู้จัดส่งข้อมูล/ยืนยัน. รูปแบบจอย, นโยบายภาพ, ชื่ออังกฤษทางการยังเป็น owner pending; booking oracle เก็บภายหลังตามคำสั่งผู้ใช้.',
'- ชุด Gold 2,000 มีเกณฑ์ legacy และ source-grade ที่ต้องอ่านแยก ไม่ใช้ source-grade เป็น semantic correctness ทั้งชุด.']
with (report/'CAUSE_ANALYSIS_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps(audit,ensure_ascii=False))
