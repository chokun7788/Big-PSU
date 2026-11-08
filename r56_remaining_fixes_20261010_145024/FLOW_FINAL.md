# Flow ฉบับตรวจทานและลงมือทำ · r56.7

## เป้าหมายและขอบเขต

แก้ข้อผิดที่มีหลักฐานจาก inventory r55 และการทดลองคำถามบริการจริง โดยเก็บต้นฉบับ นโยบายเจ้าของ ประวัติ และผลที่ไม่ผ่านไว้ ไม่รัน full20k ไม่เรียก HTTP สำเร็จว่าข้อเท็จจริงถูกต้อง และไม่ตีความ owner policy ที่ยังไม่ได้ตอบเอง

## Flow ต่อคำถาม

1. รับข้อความ/locale/session/turn/last_seen_response_id; job ใช้ idempotency ของ session+turn ป้องกันการประมวลผลซ้ำ ข้อความเดิมคนละ turn ยังเป็นคำขอใหม่ได้
2. คืน job ID และสถานะคิว แยกเวลานับจากรับคำขอ เวลารอก่อน dispatch ล่าสุด และเวลาของ dispatch ล่าสุด ไม่เรียกช่วงนี้ว่า GPU inference ทั้งหมด
3. โหลดบริบทที่ผู้ใช้ได้รับคำตอบแล้ว; การรีเฟรช anonymous session เริ่มใหม่ตามพฤติกรรมเดิม
4. แยก translation data ออกจากคำสั่ง; งานเขียนชัดเจนเกี่ยวกับเกมไม่ใช่การขอ catalog แต่คำขอราคา/กฎ/ข้อมูลจริงของศูนย์ต้องใช้ source
5. ถ้าผู้ใช้ปฏิเสธงานเดิมแล้วขอเรื่องใหม่ ให้เน้นคำขอใหม่และเก็บข้อความเดิมใน trace; อย่าลบ negation ทั่วไปหรือข้อความที่ขอแปล
6. แยก clause ที่มีหัวข้อชัด 2–6 ส่วน เก็บทุกส่วน/target/outcome/source evidence ของ child; เกิน 6 หรือเงื่อนไขซ้อนยังไม่ถือว่ารองรับครบ
7. เลือก typed operation: ราคา/รายการเกม/นโยบายบริการ/กฎ/สถานะสด/unknown/clarification/general creation
8. ราคา: ผูก service+user_group+unit+duration+rate+total จาก source; คำสั้น PC/ทั้งหมด สืบทอดเฉพาะ context ที่เกี่ยวข้อง; การเปลี่ยน filter ต้องแทนค่าก่อนคำนวณ ไม่สะสมราคาเดิม
9. Catalog/กฎ: canonical target ต้องตรง; ทั้งหมดตีความตาม scope ที่ยืนยันในบริบท กฎยาวแบ่งหน้าพร้อม returned/remaining IDs; ถ้าต้นฉบับขาดให้ตอบ partial และระบุ gap
10. Booking: อ่าน WordPress ตามคำถาม ใช้ snapshot ของวัน/transport เดียวร่วมกันในคำตอบเดียว คำถามใหม่ fetch ใหม่; timeout/HTML/401/wrong date/missing structure ไม่ใช่ unavailable equipment และห้ามเปลี่ยนเป็นว่าง
11. Source ที่เจ้าของไม่ได้ยืนยัน: ใช้ unknown policy ที่ตรงหัวข้อ ไม่อนุมานจากร้านอื่นหรือกฎการแข่งขัน
12. LLM: shared admission 1, bounded deadline/token budget; งานเขียนต้องตามรูปแบบ/ความยาว ไม่เติมวันเวลา/สถานที่เอง หาก output contract ไม่ผ่านและมี budget ให้ repair ครั้งเดียว เก็บ rejected draft และเหตุผล ไม่แอบผ่อน validator ให้คะแนนผ่าน
13. รวมคำตอบโดยคงสถานะของแต่ละส่วน; source execution coverage ไม่รับรอง factual completeness ข้อความทุกประโยค
14. คืน final result และ client acknowledgement; ไม่มีการ replay หลัง network ambiguity โดยอัตโนมัติ เก็บผลเดิมสำหรับตรวจสอบ

## วงรอบที่ทำจริง

| รอบ | พบ/ตรวจ | การแก้ | หลักฐานและข้อจำกัด |
|---|---|---|---|
| 0 | snapshot + r55 contract audit | frozen source contract v2, mutation oracle | offline audit ไม่ใช่รัน pipeline ใหม่; v1 เก็บไว้ |
| 1 | คำถามหลายส่วน, negation, topic correction, location+parking | 2–6 clauses, scoped exclusions, request_focus, parking regex | targeted baseline/targeted1; มี oracle 3 จุดที่ต้องแก้ตาม source |
| 2 | คนเล่นไม่มีชื่อ word order | service fact cue | targeted2: 38 เคสผ่าน; ไม่รับประกันทุกคำเสีย |
| 3 | คิว elapsed, child source binding, booking atomicity | timing+trace+ContextVar request snapshot | targeted3, units3, web3 ผ่านเกณฑ์ |
| 4 | หน้าเว็บ ternary precedence | elapsed แสดง queued/running ตามที่ตั้งใจ | Node mock protocol checks 4 ผ่าน |
| 5 | RoV EN 11/12, source fragment | hash-bound labelled translation + partial/source gap | rulebooks 28 requests, 8 game/locale checks; RoV source policy ยังไม่ครบ |
| 6 | invitation EN ถูกเลือกเป็น catalog, 80 words ใช้ short_creation cap | explicit creation route + word profile ≥30 | units6/web_final6 ผ่าน; load6 ยัง output rejection 4 |
| 7 | ระหว่าง ถูกมองเป็น ว่าง, invented days และไม่มี repair สำหรับ long writing | scoped regex, prompt constraint, one bounded repair | ดูผล units7/web_final7/targeted_final7/load_final7; ไม่อ้างทุก LLM draft ถูกต้อง |
| แพ็กเกจหลังรอบ7 | worker2ถูกทับกลับ1 และ Stop อ่าน ISO ด้วยThai cultureเป็นปี1483 | ค่าworker2เพียงครั้งเดียว, ParseExact invariant helper | package_process_identity_tests4checks Thai/English, wrong/malformed time rejected; actualstop/restart/smoke7c |

## เกณฑ์ผ่านและการเก็บผล

- ตรวจ mandatory content + source binding + target/units/conditions ที่กำหนดต่อเคส ไม่ใช้เพียง mode หรือ HTTP 200
- ใช้ mutation ลบข้อเท็จจริง/เปลี่ยนราคา/target/เงื่อนไขเพื่อพิสูจน์ว่า validator จับผิดตามขอบเขตได้
- Fixtures มีผลจริงที่กำหนดล่วงหน้า: VR ครึ่งชั่วโมงกินชั่วโมงเต็ม, พัก 12–13, Maintenance/ปิดพิเศษ, parse/API faults ทั้ง TH/EN
- Live WordPress ผ่าน transport/format แยกจาก independent truth verification; ผู้ใช้ยืนยันของจริงเดิมแล้ว ไม่ขอซ้ำโดยไร้เหตุ
- ทดสอบคิวแบบจำกัด 1/2/4/6/8 งาน แยก fast/LLM/mixed; ไม่ใช้แทน sustained load, fairness, capacity หรือ clean Windows
- Source change ต้องส่งต่อไป candidate และแพ็กเกจใหม่ทั้งสอง ตรวจ hash; ไม่แก้ R50 เดิม ไม่ย้าย state/log ของผู้ใช้โดยเดา
- หน่วยทดสอบและ raw web/trace/error/draft เก็บในรอบใหม่ อ่านผลก่อนสรุปปัญหาคงเหลือ

## การทบทวน flow หลังทดสอบ

ผลที่ยังไม่ผ่านต้องแยก transport / routing / source gap / context / generation / validator / oracle ผิด ก่อนแก้ ถ้า source gap ให้ระบุคำถามเจ้าของและไม่สร้างนโยบาย ถ้า validator ผิดให้เก็บข้อผิดกับ oracle เดิม ไม่เปลี่ยนคะแนนย้อนกลับแบบเงียบ ถ้า source/route ถูกแต่ LLM เติมรายละเอียดให้แก้ prompt/repair ภายใต้ deadline ไม่ปล่อย draft ที่ไม่ผ่าน หากเพียง coverage ID ครบแต่ต้นฉบับขาด ให้คง answered_partial

สิ่งที่ยังต้องพัฒนาเป็นขั้นต่อไปอยู่ใน REMAINING_AFTER_R56.md; ไม่อ้างว่า flow นี้แก้ทุกสำนวนหรืออนุญาต deployment สาธารณะแล้ว
