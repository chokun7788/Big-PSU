import json
from pathlib import Path
B=Path(__file__).resolve().parent
r=json.loads((B/'ANALYSIS_LATEST.json').read_text(encoding='utf-8'))
p=json.loads((B/'PAIRED_COMPARISON.json').read_text(encoding='utf-8'))
assert all(v['complete'] and v['counts']['requests']==20554 and v['counts']['grades']==55811 for v in r.values())
lines=['# สรุปผลเมื่อ Full test R64 เสร็จ','',
'จบวันที่ 14 ตุลาคม 2026 เวลา 19:34 น. (ประเทศไทย) ครบทั้งสี่รอบ: 20,554 คำขอและ 55,811 เกณฑ์ต่อรอบ รวม82,216การประมวลผลคำขอและ223,244เกณฑ์ตรวจ จำนวนนี้มีคำถามและ contract ที่ใช้ซ้ำข้าม corpus ไม่ใช่จำนวน user ไม่ซ้ำ','',
'## คะแนนผ่านเกณฑ์เดิม (strict compatibility)','',
'| รูปแบบ / LLM | ไทย | อังกฤษ | รวมทุกภาษา |','|---|---:|---:|---:|']
for key,label in [('legacy_offline','เดิม / ปิด'),('common_offline','กลาง / ปิด'),('legacy_llm','เดิม / เปิด'),('common_llm','กลาง / เปิด')]:
 v=r[key];c=v['counts'];th=v['by_language']['th'];en=v['by_language']['en']
 lines.append(f"| {label} | {th['passed']/th['total']:.1%} ({th['passed']:,}/{th['total']:,}) | {en['passed']/en['total']:.1%} ({en['passed']:,}/{en['total']:,}) | {c['passed']/c['grades']:.1%} ({c['passed']:,}/{c['grades']:,}) |")
lines+=['',
'ไทย/อังกฤษใช้ภาษาที่ result ระบุได้; เคส exception บางส่วนยังเป็น auto และรวมในคอลัมน์คะแนนรวมแล้ว เกณฑ์ strict รวม category/route/mode/status เดิม จึงไม่ใช่คะแนนความถูกต้องเชิงเนื้อหาล้วน และไม่ใช่การรับรองโดยเจ้าของ','',
'## แยก content contract ออกจาก route/mode','',
'ใช้เฉพาะคู่คำถามที่ทั้งสอง format มีผลให้ตรวจ content contract ชุดเดียวกัน (อาจมีทั้ง required content และ forbidden content; ไม่ได้รับรองทุกข้อเท็จจริงในคำตอบ) ไม่รวม exception ที่ไม่มีคำตอบให้ตรวจใน denominator นี้','',
'| รอบ | คู่ contract ที่ตรวจได้ | เดิมผ่านเนื้อหา | กลางผ่านเนื้อหา |','|---|---:|---:|---:|']
for key,label in [('offline','ปิด LLM'),('llm','เปิด LLM')]:
 c=p[key]['counts'];n=c['paired_content_contracts']
 lines.append(f"| {label} | {n:,} | {c['old_content_pass']/n:.1%} ({c['old_content_pass']:,}) | {c['common_content_pass']/n:.1%} ({c['common_content_pass']:,}) |")
audit=r['common_llm']['common_planner_model_audit']
lines+=['','## การเรียกโมเดลกับผลคำตอบ','',
f"Common planner: attempted {audit['attempted']:,}; transport_ok {audit['transport_ok']:,}; schema_accepted {audit['schema_accepted']:,}; final_plan_accepted {audit['final_plan_accepted']:,} เหล่านี้เป็น audit event ต่อ call ไม่ใช่จำนวนคำถามที่ตอบถูกหรือจำนวนผู้ใช้ ผล correctness อยู่ใน contract ข้างบน",
f"TimeoutError {audit.get('error:TimeoutError',0)}; HTTPError {audit.get('error:HTTPError',0)}; circuit-breaker gate {audit.get('gate:circuit breaker cooldown active',0):,} ครั้งที่ไม่ได้เริ่มเรียก ต้องแยกจากคำตอบผิดและการตอบผ่าน API200",'',
'## ปัญหาที่ต้องแก้ก่อนใช้ข้อมูลกลางแทนข้อมูลเดิม','',
'1. retrieval ใช้ตัวแปร ownership_blocked ที่ไม่ได้กำหนด ทำให้บาง branch ล้มก่อนตอบ','2. common เลือก field/facet และเชื่อมข้อกฎการแข่งขันยังไม่ตรงคำถาม; บางคำตอบส่งทุก section หรือขาด clause ที่ถาม','3. migration มี localized slot ภาษาอังกฤษว่าง791จุด; ต้องแปล/เติมจากต้นฉบับและตรวจตัวเลข เงื่อนไข ชื่อเฉพาะ โดยไม่สร้างนโยบายใหม่','4. context/selector ในเว็บ: protocol ที่ถูกต้อง เดิม22/24เทิร์น กลาง13/24เทิร์น','5. fuzzy matcher ของ common ใน production ยังช้า; evaluator ใช้ optimization ที่รักษา candidate เพื่อกวาดชุดใหญ่ ผลนี้รับรอง SLA ของ production ไม่ได้','',
'ไม่มีการ publish/approve draft หรือสลับฐานผู้ใช้ ผล common เป็น draft view สำหรับการทดสอบเท่านั้น Booking ใน corpus sweep จำลอง unavailable; ไม่มี ground truth ใหม่ของการจองลูกค้าจริง การทดสอบครบไม่ได้แปลว่าทุกเคสผ่าน','',
'รายละเอียดครบและ raw evidence ดู FINAL_FULL_TEST_REPORT.md, ANALYSIS_LATEST.json, PAIRED_COMPARISON.json และไฟล์ RESULTS ที่ยังเก็บทุก attemptไว้','']
out=B/'FULL_TEST_COMPLETION_SUMMARY.md'
with out.open('x',encoding='utf-8') as f:f.write('\n'.join(lines))
print('\n'.join(lines[:12]))
