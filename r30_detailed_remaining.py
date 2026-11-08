import json,collections
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());examples=[]
qs={'CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม','CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ','RoV ใช้สกินพิเศษได้หรือเปล่า','เทคเคนแต่ละเกมแข่งกี่รอบ'}
for line in (r/'FINAL_G_EXTRA_CORPUS_RESULTS.jsonl').open(encoding='utf-8'):
    x=json.loads(line)
    if x['question'] in qs:examples.append(x)
assert len(examples)==4,len(examples)
with (r/'CONFIRMED_REMAINING_CASES.json').open('x',encoding='utf-8') as f:json.dump(examples,f,ensure_ascii=False,indent=2)
notes={
'CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม':('target และ context หายหลัง splitter', 'ควรตอบเวอร์ชันล่าสุดบน Steam และข้อห้ามดัดแปลงตัวเกมจาก rulebook CS2 โดยรักษา target ของทุก proposition ข้อเสียงดังไม่ตอบการดัดแปลงเกม', 'shared competition signal ยังไม่ครอบคลุม proposition เวอร์ชัน/ดัดแปลงตัวเกมในประโยค implicit จึงแยกคำถามก่อน target-bound detail ส่วนหลังไม่มีเกม; route/source validator ผ่านคำตอบกฎทั่วไปโดยไม่ได้ตรวจ proposition ของส่วนหลัง'),
'CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ':('qualifier เวลาและ action ถูกกลบด้วย noun roster','ควรดึงข้อไม่อนุญาตลงทะเบียนหลังปิดรับสมัคร ไม่ใช้จำนวน 5 คนตอบการเพิ่มรายชื่อ','late_registration รองรับลำดับ หลัง...ปิดรับสมัคร แต่ไม่รองรับ ปิดรับสมัครแล้ว...; roster concept จับ noun roster และเลือกองค์ประกอบทีมได้ literal จริง แต่ไม่มีข้อห้ามตาม action; confidence .97 เป็นค่าจับเส้นทางตามโค้ด ไม่พิสูจน์ว่าตอบ action ครบ'),
'RoV ใช้สกินพิเศษได้หรือเปล่า':('implicit facet ไม่เข้าสู่ detail source','ควรอ้างข้อ 4.2.5 ห้ามใช้สกินนอกจาก Default โดยบอก rulebook RoV/Blueket 2025 ชาย','source-detail มี concept skins แต่ gate ต้อง looks_like_competition_rule_query ก่อน; คำถาม permission สกินที่ไม่กล่าว แข่ง/กฎ ยังไม่ครอบคลุม แล้ว fallback ไม่ยืนยัน facet นี้ จึง no_answer แม้มี source'),
'เทคเคนแต่ละเกมแข่งกี่รอบ':('ชื่อเกมย่อและ facet จำนวนรอบยังไม่ผูก literal settings','ควรยืนยันว่าเป็น Tekken 8 แล้วอ้าง settings จำนวนรอบต่อเกม 3 รอบ หากเป้าหมายยังไม่ชัดให้ถาม ไม่ส่งหัวข้อกติกา/แพลตฟอร์มแทน','target resolver ยึดชื่อ registered edition; fallback ยังเลือก source กว้างและใช้หัวข้อ/รูปแบบนำหน้า ไม่มี proposition count ที่บังคับ source clause 3 รอบ ทุกกรณี')}
lines=['# ข้อผิดจริงที่ยังต้องแก้หลัง r30-G2','', 'ตรวจจากคำตอบ/trace และข้อความ source ที่มี ใช้เป็นงานรอบถัดไป ไม่เปลี่ยน expected เดิมเพื่อทำให้ผ่าน และไม่เหมารวมทุก fail เป็นสาเหตุเดียว','']
for x in examples:
    q=x['question'];kind,expected,cause=notes[q];res=x['result']
    traces=[t for t in res['trace'] if not t['stage'].startswith('timing:') and any(k in t['stage'] for k in ('split','competition','router','universal_intent','source_grounding','question_frame'))]
    lines+=['## '+q,'','ประเภท: '+kind,'','คำตอบจริง:','',res['answer'],'','ควรตอบ: '+expected,'','สาเหตุและคะแนน: '+cause,'',f"Mode: `{res['mode']}`; confidence: `{res['confidence']}`; route: `{json.dumps(res['route'],ensure_ascii=False)}`",'', 'Trace ที่เกี่ยวข้อง:','', '```json',json.dumps(traces,ensure_ascii=False,indent=2),'```','', 'Expected/trace/hits ทั้งหมดเก็บใน CONFIRMED_REMAINING_CASES.json','']
lines+=['## Flow แก้ร่วม','', '1. ให้ parser ส่ง target/edition/scope ไปทุก proposition ก่อน split และล็อกข้อที่ยังอ้างถึงเกมเดียวกัน', '2. ใช้ action + qualifier เวลา + negation เป็นตัวเลือก concept ก่อน noun ทั่วไป/สถานที่', '3. เพิ่ม target-bound implicit permission signals และ negative controls เรื่อง gameplay/catalog/ราคา/จอง', '4. Validator ต้องตรวจว่าคำตอบแรกและข้อเสริมครอบคลุมทุก proposition ไม่ใช้ source ID/count เป็นตัวแทน', '5. Oracle ใหม่อ้าง clause/source hash แบบ overlay แยกจาก frozen Gold; ไทย/อังกฤษใช้ semantic contract เดียวกัน', '6. ตรวจชุดยากเก่าทั้ง 861 grades, strong content/composition 728 และทุก corpus; diff ก่อน/หลังและเก็บข้อผิดแยก','', 'รายละเอียดลำดับรวมและ owner questions อยู่ใน docs/130_full_improvement_r30_flow_20261002.md']
with (r/'REMAINING_ERRORS_AND_NEXT_FLOW_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps({'confirmed_remaining_examples':len(examples)}))
