# รอบแก้ข้อมูลเว็บและเป้าหมาย — 11 พฤศจิกายน 2026

## เปลี่ยนจริง

- ทำ SQLite backup จาก `common.sqlite` เป็น `system/data/knowledge/verified_sources.sqlite` แล้วแก้เฉพาะสำเนา ไม่เปลี่ยนฐานเดิม/owner/live/frozen
- กฎจำนวนsessionsเดิม3ปรากฏในFAQ3รายการ แก้ทั้งกลุ่มเป็น6ตามหน้าเว็บจองปัจจุบัน พร้อมเก็บ revision เก่าไว้ในฐานสำเนา
- source ใหม่เป็น `official_page` มี snapshot JSON, HTML SHA256, URL, เวลาที่ตรวจ, section1.2/1.3 และ JSON pointersต่อfield ไม่ทำเป็นคำยืนยันเจ้าของ ไม่กดapprove/publishและไม่เดาวันเริ่มใช้
- ผูก related_idsกับ `center_psu_phuket` ใน3รายการนั้น พร้อม source pointerของความสัมพันธ์และscope note
- public citation registryเพิ่ม6entries (รวม52) สำหรับanswer/owner_policyของ3revisionใหม่ ไม่ใช้ลิงก์หน้าแรกกับข้อมูลทุกช่อง
- ตัวตรวจเพิ่มตรวจความสัมพันธ์จากsourceจริงและปฏิเสธชื่อสถานที่อื่นที่ตรวจจับได้ ทั้ง typed verifier และ compatibility guard บอกเหตุผลเรื่องสถานที่ แทนข้อความไม่มีข้อมูลรวม ๆ
- FAQ owner_policy ขึ้นต้นด้วยคำตอบ ไม่ใช้ข้อความคำถามเดิมเช่น “Book how many session pay” เป็นหัวข้อ
- PCนักศึกษาPSUยัง0บาทตามคำยืนยันเจ้าของ ไม่เปลี่ยนราคาบริการอื่น ไม่อ้างภาพเก่าพิสูจน์0

## ก่อน–หลังและข้อจำกัด

`verified_source_probe_1794393076209142900/DETAILS.json` เก็บก่อนแก้ตัวตรวจ: ถามโรงแรมอันดามันแล้วระบบตอบกฎ6sessionsของศูนย์พร้อมลิงก์ เป็นข้อผิดพลาดจริง จึงยังไม่เริ่มรอบ200 ณ ตอนนั้น

หลังแก้ `verified_source_probe_1794393249346166400` ไม่ส่งกฎให้โรงแรมอีก จากนั้นปรับข้อความเหตุผลให้ตรงกรณีและเพิ่มผลตรวจความสัมพันธ์ในledger

ตัวตรวจสถานที่เป็น bounded rejection ของ explicit location spans และความสัมพันธ์จากsource ไม่ใช่ตัวพิสูจน์เจตนาภาษาธรรมชาติทุกกรณี ใช้กับFAQที่มี center relationship/source declaration ไม่ถือว่าปิดช่องว่างทุกหมวดหรือทุกFAQ โดยเฉพาะชื่อสถานที่รูปแบบใหม่หรือความหมายซับซ้อนยังต้องตรวจเพิ่ม

ไม่ได้เพิ่มหลักฐานให้ภาพปุ่มควบคุม/เอกสารแข่งขันที่ยังไม่ได้อ่าน ไม่เปลี่ยน registryทั้งก้อนจากการค้นชื่อเกม ไม่ใช้คำตอบFlowเก่าเป็นgold

## Gates ที่ผ่านก่อนรอบ200

- `verified_sources_controls_1794393487397226300/RESULT.json`:22checks ไทย/อังกฤษ,ชื่อศูนย์ที่ถูกต้อง,จำนวนรอบ+ชำระเงิน,ราคา+จอง,สถานที่อื่นและคำปฏิเสธ,ผิดplatformราคา,relationshipหาย/ปลอม/centerหาย,actual isolated edit/withdraw
- ค่า5sessionsใน lifecycle เป็น fixtureบนDBสำเนาแยก ไม่ใช่นโยบายจริง;หลังแก้ไม่ใช้webcitationเก่า และหลังถอนไม่ส่งclaimsจาก3recordsที่ถอน
- `price_currency_1794393513035533100/RESULT.json`:12 affected currency checks
- `bounded_response_1794393520199470300/RESULT.json`:6 budget/typed sibling regression checks
- ทั้งหมดนี้เป็นsource-only ไม่ใช่การรับรองโมเดลหรืออำนาจเผยแพร่ทั้งระบบ
- รอบเตรียมนำเข้าครั้งแรกurllib defaultUAได้HTTP403 ยังไม่สร้างDB เก็บเป็นattempt01;ตรวจเว็บผ่านเครื่องมือเว็บได้และใช้headerแบบเดียวกับarchiveเดิมแล้วได้HTMLเพื่อเก็บhashและนำเข้าต่อ ไม่ใช่Flowตอบผิด

## รอบ200

สำเนาวัด `r135_verified_eval200_20261111` port8140 version `R135-Verified-eval200` ใช้manifest200เดิม byte-identical SHA256 `11e15688009e46982346d76d2d0fdf36d8a843f2fa46658af0059b4c27c961f0`

ตรึงcode,registryและDBใน `evaluation/PREPARED_MANIFEST.json`;ก่อนวัดมีHTTPpreflight4requestsแยก ไม่รวมตัวหาร200 ใช้worker1รอแต่ละคำถามจบก่อนส่งข้อถัดไป ไม่แก้สำเนาที่กำลังวัด ไม่restart/retry/rerunอัตโนมัติ

ดู `evaluation/PROGRESS.json`, `PID.txt`, `LAUNCH_PID.txt`, `runner.err.log`, `RUN_FAILED.txt` และprocessจริง เมื่อจบตรวจ200keysและไม่ซ้ำก่อนให้คะแนนliteralจากเกณฑ์ที่รองรับ แยกunassessed/unsupported ไม่ถือHTTP200เท่ากับตอบถูก

ชุดนี้เป็นregressionที่เคยเปิดดูแล้ว ไม่ใช่การทดสอบsemanticแบบไม่เคยเห็น เกณฑ์บางข้ออาจคาดpolicyเดิม3รอบ จึงต้องแยกผลliteralออกจากสิ่งที่sourceปัจจุบันรองรับ เวลา/source/backendเทียบย้อนหลังต่างกัน ไม่regradeR132

## งานค้าง

รอผลรอบ200และจัดกลุ่มปัญหาจากผลจริง ตรวจsource bindingsของกลุ่มอื่นต่อ ไม่ประกาศครบ48/76หรือพร้อมproduction ภาพและเอกสารแนบที่เว็บเข้าไม่ได้ยังเปิดอยู่

อย่าใช้ตัวสร้าง registryเก่าซึ่งอ่าน `common.sqlite` เขียนทับ52entries:รอบนี้การเพิ่มentriesใหม่มีหลักฐานใน `source_update_20261111/IMPORT_RECEIPT.json` และ `SOURCE_SNAPSHOT.json` ต้องรักษาmappingของrevisionใหม่ไว้
