# R66 — วิธีใช้ผลการแก้และตรวจต่อ

## แยกสิ่งที่ส่งมอบ

- `system/app` เป็นสำเนาโค้ดที่ใช้ทดสอบ ก่อนนำไฟล์ที่เปลี่ยนกลับไปโปรเจกต์จริงด้วย hash compare
- `common.sqlite` เป็น **ร่างข้อมูลกลาง** ที่เก็บ 582 รายการเดิมและเพิ่ม PC rates จาก source เก่า 6 รายการ ไม่มีการ publish/approve แทนเจ้าของ
- `FINAL_<tag>/CODE_MANIFEST.json` และ database snapshots ระบุโค้ด/ข้อมูลที่ทดสอบจริง
- `AUDIT_<tag>/ALL_FAILED_GRADES.md` แสดงคำตอบจริง แผนเลือกข้อมูล และเหตุผลที่ไม่ผ่านทุก grade ในชุดนั้น ห้ามอ่าน strict score เป็น accuracy
- `RELEASE_AUDIT_*.json` ระบุ field/source/time/references ที่ยังบล็อก publication ราย record

## การแก้ข้อมูลหลังส่งงาน

1. ใช้รหัสรายการเดิมเมื่อแก้ข้อมูลเดิม เพื่อสร้าง revision ถัดไป เช่นปรับราคา/ข้อความกฎ อย่าสร้าง ID ใหม่เพื่อกลบรายการที่ถอน
2. ข้อมูลใหม่เลือกรูปแบบหมวดให้ตรง และเชื่อม ID ตาม Flow เช่น game_service เชื่อม game/service ส่วน rate เชื่อม service/audience
3. ไม่ทราบช่องใดให้ใช้ unknown อย่าใส่ราคาหรือวันมีผลสมมุติเพื่อผ่าน validation
4. บันทึกหลักฐานแต่ละช่อง เป็น URL/snapshot/ข้อความเจ้าของที่ตรวจที่มาได้ แยก receipt date จาก effective date
5. EN ที่โมเดลแปลมีสถานะ agent_translated ไม่เท่ากับเจ้าของตรวจแล้ว การแก้ Thai ต้องตรวจ English revision ตามด้วย
6. publication ใช้ release gate จริง ไม่เปิด evaluation draft view ใน production

## คำเตือนจากหลักฐานรอบนี้

โมเดลเคยแปล Treasurer เป็น Priest และ gum เป็น checkers ทั้งที่ตัวเลขไม่เปลี่ยน การผ่าน structural/literal checks ยังไม่พอให้เรียกคำแปลทั้งหมดว่าถูก การสะกดชื่อบุคคลอังกฤษไม่มีใน source จะเก็บชื่อไทยไว้ ไม่ตั้งชื่อทางการเอง

กฎคิดราคา `session_ceil` เป็น schema extension สำหรับกฎปัดเต็มรอบที่มีใน calculator เดิม ไม่ได้สร้างกฎใหม่ให้แพ็กเกจอื่นใช้ตามอัตโนมัติ ข้อมูลที่ไม่ระบุสูตรยังไม่ถูกคูณ/หารเอง

## โค้ดที่นำกลับโปรเจกต์จริง

ดู `DEPLOY_<tag>/APPLIED.json` เท่านั้นจึงยืนยันว่า copy แล้ว รายการ backup อยู่ที่ `DEPLOY_<tag>/before/app` การนำโค้ดกลับไม่เปลี่ยน `data/knowledge/approved.sqlite` หรือ migration R63 เดิม

โปรเซส Chatbot ที่เปิดค้างและ portable packages อาจยังใช้โค้ดอีกชุด ต้องตรวจ path/version และเริ่มโปรเซสจาก checkout ที่ได้รับการแก้ก่อน การแก้ source checkout ไม่ได้ยืนยันว่า package ทุกโฟลเดอร์ถูกอัปเดตแล้ว

## รันตรวจซ้ำอย่างระบุขอบเขต

ตัวรัน `run_final.py <new_tag>` สร้างโฟลเดอร์ใหม่ ห้ามใช้ tag เดิมเพราะต้องเก็บผลก่อนหน้าไว้ ตัวทดสอบนี้ใช้ frozen clock และ mock booking-unavailable จึงไม่ใช่การเช็กจองจริงหรือหน้า production

Python ที่ใช้ในเครื่องนี้:

`C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\python.exe`

ต้องมี Ollama กับ model เดิมสำหรับ ON; ไม่มีการดาวน์โหลดโมเดลใหม่ในรอบ R66 ห้ามรัน model benchmarks ซ้อนหลายแขนแล้วใช้ latency เป็นการใช้งานหนึ่งคน

## ย้อนโค้ด R66

`rollback_verified_code.py <tag>` ตรวจแผนโดยยังไม่แก้ไฟล์ เพิ่ม `--apply` เฉพาะเมื่อต้องการย้อนจริง ตัวช่วยจะปฏิเสธทันทีหากมีคนแก้โค้ดต่อจาก hash ของ R66 ไม่ย้อนข้อมูล/approvals และไม่ลบโฟลเดอร์แบบ recursive

## งานที่ยังไม่ควรข้ามก่อน production

- อัตรา/เวลามีผล/นโยบายที่ไม่มีหลักฐาน ใช้คำถามเฉพาะใน OWNER_CONFIRMATION_REQUIRED_TH.md
- source factual review และ core field ที่ไม่ผ่านใน release audit ต้องจัดการ ไม่ปิด gate
- ทดสอบคำถามกับ release ที่อนุมัติจริงและเครื่องที่จะส่ง ไม่ถือว่าร่างใน harness คือ runtime production
- new arbitrary live_binding ยังต้องมี provider adapter/resource identity/freshness/oracle ที่พิสูจน์ได้ การอ่าน metadata ผ่านไม่ใช่สถานะว่างถูกต้อง
