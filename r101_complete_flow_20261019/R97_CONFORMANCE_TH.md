# R97 Flow V2 → สิ่งที่ทำจริงใน R101

เอกสารนี้ใช้แยกการเชื่อมโค้ด การตรวจพฤติกรรมเฉพาะทาง และการรับรองคุณภาพการตอบ ห้ามนำจำนวนหมวดหรือจำนวน assertions ไปเรียกว่าความแม่นยำทุกคำถาม

## งานตามแผน

| งาน R97 | สิ่งที่เชื่อมแล้ว | หลักฐานตรวจล่าสุด |
|---|---|---|
| W0 ตรึงต้นฉบับ | สำเนา R100 แยก candidate, hash ต้นฉบับและฐานข้อมูล, manifest ก่อน/หลัง | INTEGRITY.json, release_subset09_INTEGRITY.json |
| W1 แผนและผลราย need | CommonAnswerer เข้า complete_flow, request context ร่วม, need ledger, origins และ receipts | gate_contracts05 59 assertions |
| W2 candidates และการตีความ | ชื่อจาก common snapshot, กรอง subject ตาม task, ไม่อ่าน facts จาก Legacy | gate_semantic04, gate_rental03, gate_rules02 |
| W3 ทั้งหมด/คำถามต่อ | เก็บเฉพาะ state ที่ส่งจริง, เลือกรายการ/ลำดับ, รักษา task/audience/duration, ไม่แย่ง specialized pending | gate_contracts05, gate_v203 |
| W4 กราฟอ่าน | executable definitions 32 tasks, any_of/optional, FK สองทิศ, cycle/depth bounds, field receipts | gate_categories03, gate_semantic04 |
| W5 ราคา/เหมา/ปฏิทิน/นโยบาย | ใช้ calculators/adapters เดิมผ่านแกนร่วม, validity และ qualifier guards, ไม่เทียบช่องจองกับเปิดศูนย์ | gate_rental03, gate_conflicts02, gate_contracts05 |
| W6 กติกา/ปุ่ม/หลาย subject/live | lock เกมและฉบับ, condition clauses เดิม, game/control relations, แยก static/live needs, time slot ตามที่ถาม | gate_rules02, gate_live04, gate_v203 |
| W7 semantic planner/ภาษา | เสนอแผนทั้งคำขอหนึ่งครั้ง, ตรวจ spans/IDs/qualifiers, เข้า executor โดยไม่โดน fullmatch เดิม veto, แยก transport/schema/semantic | gate_semantic04 (จำลอง protocol); real_planner03 (โมเดลจริง 3 คำถาม) |
| W8 owner lifecycle | ฟอร์ม 24 หมวดใช้ readiness จากกราฟ, draft/approved release แยก, เพิ่ม/แก้/ถอน reread จริง | gate_categories03 48 คำถามแชทและ lifecycle; gate_published03 |
| W9 focused review | เก็บ failed runs, ชุดตรวจ 361 assertions, เปรียบเทียบ 91 request keys กับผล R100 เดิม | SELECTED_GATES.json, RESULTS_TH.md |

## สิ่งที่คำว่า “ครอบคลุม 24 หมวด” ยืนยัน

มีการสร้างข้อมูลสมมุติผ่าน owner path ทั้ง 24 หมวด ถาม all-details ภาษาไทยและอังกฤษรวม 48 คำขอ แล้วตรวจการแก้ revision และถอนรายการทุกหมวด กรณีเหล่านี้ยืนยัน lifecycle และการอ่านค่าผ่านแกนร่วมตามข้อมูลที่ฟอร์มรองรับ

ไม่ได้แปลว่าทุก task ย่อยของหมวดนั้นผ่านทุก paraphrase เช่น การอ่านข้อมูล game_mode สำเร็จไม่เท่ากับการแนะนำเกมที่เหมาะกับเด็กได้เมื่อไม่มี eligibility

## ขอบเขต acceptance ที่ยังต้องแยก

- C01–C37 ใน FLOW_SPEC.json เดิมยังเป็น design registry ต้นฉบับ ไม่แก้ executed=false ให้ดูผ่านโดยไม่มี runner ที่สร้าง precondition ตรงกรณีทุกข้อ
- focused suites ตรวจหลาย invariants ที่สัมพันธ์กับ C01–C37 แต่ไม่ได้ถือเป็นการรัน exact scenario ครบ 37 ข้อโดยอัตโนมัติ
- typed conflicts ตรวจราคาที่ billing tuple เดียวกันและตารางที่ scope เดียวกันได้ การพิสูจน์ว่า FAQ ร้อยแก้วขัดกับ structured rate ทุกแบบ (C23) ยังไม่มีตัวตัดสินความหมายทั่วไป จึงไม่รับรองว่าแก้ semantic conflict ทุกชนิดแล้ว
- การตรวจคำแปลป้องกัน critical slots บางชนิด ไม่ใช่การประเมินโดยผู้เชี่ยวชาญภาษาในทุกประโยค
- ความครบของกฎจาก adapter เดิมขึ้นกับ completeness และ clauses ที่ต้นฉบับระบุ ไม่ถือว่าสรุปเลือกบางข้อคือ rulebook ครบ
- live fixtures ใช้ provider จำลอง ไม่ใช่การตรวจสถานะจองจริงหรือ load test ของ booking API
- ยังไม่มี untouched holdout, full 20,554 requests, performance/load test ใหม่ หรือการติดตั้งแทน production ในรอบนี้

## สิ่งที่เจ้าของเติมได้โดยไม่ต้องเพิ่ม case ในโค้ด

ชื่อใหม่/aliases, รายละเอียดเกม, modes, controls, รายการให้บริการและเครื่อง, ราคาในสูตรที่รองรับ, ราคาแพ็กเกจ, ตาราง/วันปิด, ขั้นตอน/กติกา/FAQ และ live mapping ตาม schema ที่มี เมื่อกรอก relations และหลักฐานเพียงพอ แชทจะอ่านจาก release เดียวกัน

การเพิ่ม business operator ใหม่ เช่นสูตรโปรโมชันที่ executor ยังไม่รองรับ ยังต้องพัฒนา operator และตรวจสูตร การใส่คำอธิบายในฟอร์มไม่ทำให้โมเดลได้รับสิทธิ์คำนวณสูตรใหม่เอง

## ก่อนเปิดใช้จริง

1. ใช้ Preview ตรวจข้อมูลชุดย้ายกับโค้ด R101
2. แก้ข้อเท็จจริงที่ต้นฉบับขาด เช่นวันมีผลราคาและ scope การเปิดศูนย์ โดยใช้ข้อมูลที่ยืนยันแล้ว
3. อนุมัติและ publish ชุดข้อมูลจริง: ฐานสำเนาปัจจุบันยังไม่มี active published release หรือ approvals
4. ตรวจ live connection กับระบบจริง และ acceptance ที่ตรงกับบริการที่จะเปิดใช้
5. พิจารณา rollout จากผลที่เกี่ยวข้อง ห้ามใช้ 361/361 แทนคะแนนตอบคำถามลูกค้าจริง

คู่มือ: [README_TH.md](README_TH.md) · Flow: [IMPLEMENTED_FLOW_TH.md](IMPLEMENTED_FLOW_TH.md) · ผล: [RESULTS_TH.md](RESULTS_TH.md)
