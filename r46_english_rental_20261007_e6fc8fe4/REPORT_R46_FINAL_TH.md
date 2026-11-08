# สรุป r46: รองรับคำถามเช่าเหมาเป็นภาษาอังกฤษ

## ทำแล้ว
- เพิ่ม 33 เคสอังกฤษ: คำถามสุภาพ สำนวนหลายแบบ พิมพ์ผิด follow-up การเลือกช่วง/กลุ่ม การตัดรายการ และการเปรียบเทียบราคาเงื่อนไขต่างกัน
- รอบแรกผ่าน 22/33; วิเคราะห์และแก้ 11 จุดที่พบ โดยแก้ไฟล์เดิมเฉพาะ app/pipeline/zone_rental.py และเพิ่ม tests/test_english_rental_r46.py
- whole-day จับเป็นเต็มวัน; คำถาม how many people/how long/reserve/booking procedure/take effect ใช้บริบทและ field ถูกต้อง
- typo token ในประโยคยาวใช้ fuzzy service matcher เดิม; PS55/Xbox ยังไม่ถูกเดาเป็นเครื่องที่มี
- versus และ compare...with รักษา target/group/period ของแต่ละ clause ราคาคนละเงื่อนไขไม่ปนกัน
- ยกเว้น VR ไม่กลับเข้ามาตอนใช้ defaults; per machine เป็น field ที่ไม่มีราคายืนยัน

## ผลอัตโนมัติ
- อังกฤษใหม่: **33/33** ผ่าน HTTP จริงหลังแก้ (ก่อนแก้ **22/33**)
- Regression ไทย+อังกฤษเกี่ยวข้องรวม: **181/181** ผ่าน ทั้ง source และ HTTP; HTTP **239 requests**
- Unit tests: **86/86** ผ่านใน 5 ไฟล์
- Source/release: **155/155** ไฟล์ตรงกัน; Git diff --check exit 0
- ราคาตรวจ ID/ค่าโดยเทียบเซลล์จาก workbook เดิมและ SHA256 ไม่ใช่แค่ API เชื่อมสำเร็จ
- HTTP rental ในชุดอังกฤษ median 0.0956s, max 0.2625s; ไม่รวมการวาดหน้าเว็บ/การดึง WordPress
- Source workbook hash ยังเดิม: bbcc850c1b348e79b9c65577ebf2a284f26fc81674c1d44de9e8e846653b8894

## เกณฑ์ผ่านมีขอบเขต
- เคสเปลี่ยนหัวข้อบางข้อเช็คเพียงว่าไม่ตอบราคาเหมา เช่น en-venue-location ยังเป็น english_no_answer ไม่ใช่ผ่านความถูกต้องเรื่องสถานที่
- เคส missing เช่นขั้นตอนจอง/ชั่วโมง/วันที่มีผล ผ่านเมื่อแจ้งว่าไฟล์ไม่ระบุ ไม่ได้หมายถึงข้อมูลนั้นได้รับการยืนยันแล้ว
- ไม่ได้รัน full suite 20k หรือยืนยันสถานะว่างจริงจาก WordPress ในรอบนี้
- ตัวเลข confidence 0.99 เป็น route constant ไม่ใช่ความน่าจะเป็นว่าคำตอบถูกทุกประโยค

## เจ้าของยังต้องยืนยัน
จำนวนชั่วโมง/ช่วงเวลาเช่าครึ่งวันและเต็มวัน; วันที่มีผล; วิธีจองเหมา; ค่าเจ้าหน้าที่และการรวมราคา; สิทธิ์บุคคล; รายชั่วโมง/หลายวัน/ส่วนลด/แพ็กเกจตัดโซน ยังไม่มีใน workbook และไม่เดาเพิ่ม

## ใช้งาน
เว็บ http://127.0.0.1:8091/ ใช้ **2026.10.07-english-rental-r46.1**; เปิดภาษาอังกฤษก่อนถาม
release: C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r46_english_rental_20261007_e6fc8fe4\release_r46_1\PSU_Esports_Chatbot_Local
release นี้เป็น local runtime อ้าง Python/Ollama บนเครื่องเดิม ยังไม่ได้ปรับแพ็กแจกจ่ายพร้อม/ไม่พร้อมโมเดลสองแบบ

## หลักฐาน
- FLOW_R46_ENGLISH.md: flow และเกณฑ์ตรวจ
- CASE_ANALYSIS_R46_ENGLISH_TH.md: ทุกคำถาม expected/plan/คำตอบก่อนและหลัง
- R46_INITIAL_WEB*, R46_SECOND_SOURCE*, R46_SOURCE_REGRESSION*, R46_FINAL_WEB*: raw responses/trace/checks ทุก run ไม่ทับผลเดิม
- FINAL_AUTOMATED_GATES_R46.json, FINAL_HEALTH_R46.json, SOURCE_AND_RELEASE_AUDIT_R46.json, SOURCE_CHANGE_R46.diff
- before/: snapshot งานเดิม; GIT_STATUS_R46.txt และ GIT_DIFF_CHECK_R46.txt เก็บสถานะ
