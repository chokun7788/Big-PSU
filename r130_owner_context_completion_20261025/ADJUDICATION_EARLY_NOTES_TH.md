# บันทึกอ่าน execution ระหว่างรอ R130 ครบ330 — ยังไม่ตัดสินเลือก

อ่านเฉพาะผลที่บันทึกแล้ว ไม่รันคำถามหรือโมเดลเพิ่ม ไม่แก้ candidate ที่ตรึงไว้ บันทึกนี้ไม่ใช่คะแนน semantic และไม่แทนการอ่านทุก regression/critical group เมื่อ replay ครบ

## จุดที่ต้องตามตรวจในผลครบ

- `2a729438da53f233061c6c765da72d9b1735bccabf9f95d04f3096c03e7d0856` — “What is PSU Esports Studio - Phuket? I need the official answer”: retained fallback อ่าน `migrated_faq_rule_overview_identity` ได้คำอธิบายศูนย์ที่อ้าง source `r63_72e506b291dbbde37f164906b0f8#/mapped_fields/answer` แต่ new execution กลับ missing_source/entityไม่ชัด ทั้งที่ข้อมูลมี เป็นการเสีย coverage จริงในชั้น engine นี้ ต้องนับเป็น regression ไม่เอา schema gain กลบ
- `eca9a6816e9e5627bedd41f819355b4c325185fefbeac56ae5174b6489e2ab83` — “ช่วง Maintenance จองได้ไหม”: new แสดง maintenance จันทร์09–12/ศุกร์13–16ครบ7วัน แต่ยังไม่ได้ตอบสิทธิ์จองตรงคำถาม การมี maintenance receipts ถูกต้องไม่เท่ากับตอบ bookable predicate ครบ ต้องอ่าน ledger และ native calendar API path แยกก่อนสรุป ไม่อนุมานว่าช่วงเหล่านี้เปิดหรือปิดบริการทั้งหมด
- `398170d78be93ba876e72c7d26080cd049b1d32a01b1532a52ca34514a5cf0ea` — service days/hours for reservations: ทั้งretained/new engine executionตอบไม่ระบุเป้าหมาย ทั้งที่คำถามขอ timetableรวม ต้องตรวจว่าคือ reader/plan gap ไม่สรุปว่าไม่มีข้อมูลเวลา
- `2fe50255e1804a59bbcac8aacf797072089fe2b4d5d3150a412ffe78b89bc3ab` — คำถามสะกดการ์ดจอคลาดเคลื่อน: new อ่าน `equipment_gaming_pc` พร้อม GPU RTX5060 8GB ได้ แต่ rendererยังแสดง zone/quantity/recorded_source_detailปะปน Source-supported value gain แยกจากปัญหาความตรงประเด็นและรูปแบบข้อความ
- `cb250317c45d865e08185cf9e739928a4ca3703ff8e39ab6b05926cd8194250b` — “กติกา Valorant งานล่าสุดใช้อะไร”: goldระบุ ambiguity แต่ผลengineออกunavailableทั้งคู่ ต้องแยกการขอระบุรายการ/ฉบับจาก model selector failure ไม่อ้างว่าแหล่งกติกาหรือliveproviderล่ม

## ตัวอย่างที่อ่านได้ตรงกันแล้ว

- `8570a28b...` — TEKKEN8อยู่PC/PS5 zones มี typed game/service/zone relations อ้างอิงได้ทั้งสองแขน
- `43d4deaf...` — Fortnite buttons ตอบเฉพาะแหล่งบางส่วนพร้อม partial note ไม่แต่งfull controller mapping
- `04a134cf...` — PSU Nintendo120นาที0บาท ตามrate/source affirmation พร้อมบอกวันที่ยืนยันและ effective intervalที่ยังไม่ทราบ ไม่ขยายความเป็นราคาทุกปี
- `89b39aa8...` — VR120นาทีสำหรับPSUพร้อมขั้นตอนจอง ทั้งสองส่วนยังถูกเก็บ แต่อัตราทางเลือก0บาทซ้ำควรแยกปัญหาการแสดงผลจากคำนวณผิด
- `fe55f25a...` — newอ่านตำแหน่งผู้ช่วยอธิการบดีฝ่ายวิชาการจากrecordที่มีแล้วได้ ในขณะที่retained fallbackไม่ตอบ

## เกณฑ์การอ่านต่อ

1. ต้องใช้ replayครบ330 และ source snapshotR130 ชุดเดียวกันก่อนเขียน PLANNER_ADJUDICATION_R130.json
2. อ่านทุกกรณีที่คำตอบ/status/claimsเปลี่ยน โดยเน้น reservation/payment/service_fee/rules/calendar/live อิสระจาก raw schema metrics
3. คะแนนtyped obligation ratioมีdenominatorขึ้นกับcompiled proposal ต้องอ่านgold needsที่อาจตกหล่นด้วย ไม่ใช้ratioสูงขึ้นเป็นหลักฐานว่าทุกneedดีขึ้น
4. Engine replayไม่ครอบคลุม preprocessing/native adaptersทุกเส้นทางของCommonAnswerer/API ต้องระบุขอบเขตนี้และใช้ final API readiness/Full Test ตรวจต่อ ไม่ยืมผลAPIที่ยังไม่รันมาลบregression
5. แยก known-source refusal, requested-predicate omission, unresolved source scope, transport, source-verifier rejection และ genuine wrong-content ห้ามรวมทุก missing_source ว่าเจ้าของยังไม่ให้ข้อมูล
