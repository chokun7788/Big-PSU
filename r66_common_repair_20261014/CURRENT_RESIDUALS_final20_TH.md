# สิ่งที่ยังไม่ผ่านหลัง final20 — ไม่ปิดทับด้วยผล targeted gates

39 stages ของรอบยืนยันจบ โค้ด/DB frozen และ selected Ground Truth 223 requests ต่อ flag ไม่มี exception/schema rejection แต่ไม่ได้แปลว่าทุกคำตอบถูกหรือพร้อม production

## 1. ยังตอบไม่สำเร็จเพราะ local model timeout สองคำถาม

- What time is the afternoon session? I need the official answer.
- พกอาหารจากข้างนอกเข้าไปได้ไหม

เป็นข้อผิดพลาดด้านการให้บริการคำตอบจริง: source มีข้อมูล แต่ selector ไม่ทัน deadline และคืนข้อความลองใหม่ ไม่ใช่ข้อยืนยันว่าไม่มีข้อมูล และไม่ใช่คำตอบถูกเพราะเลือก abstain ต้องเก็บไว้เป็น failed service response แยกจาก hallucination/source fabrication

trace ที่มี audit objects: attempted 22, transport_ok 20, transport_not_ok 2, schema_accepted 18 ตัวเลขเหล่านี้ไม่ใช่ traffic count ครบทุก API หรือ accuracy ไม่มีหลักฐานเพียงพอให้ชี้ว่าเกิดจาก GPU/context/cold load อย่างใดอย่างเดียวโดยยังไม่ได้วัด

แนวทางที่ต้องทำต่ออย่างเป็นระบบ: วัด queue/load/prompt token counts ให้ผูก request_id, จำกัด context selector ตามงบ token พร้อมรักษาหัวข้อ/เงื่อนไข, วัด recall ของการคัด candidate ก่อนลดขนาด และเพิ่ม source-based semantic attributes ที่ใช้ร่วมหลาย record แทนเพิ่ม alias ต่อคำถาม ห้ามเปลี่ยน timeout เป็นตอบเดาจาก top score เพียงเพื่อให้ดูว่าตอบสำเร็จ

## 2. เวลาบางเคสยังเกินเพดานในชุดประเมิน

- OFF max 21.36 s, ON max 24.94 s; มี performance_failed grade 1 ต่อ flag
- ค่าเฉลี่ย OFF 0.469 s / ON 1.088 s; p95 OFF 1.228 s / ON 3.887 s
- ตัวอย่างช้าเป็นคำถามอัดวิดีโอที่มีคำเกริ่นและ typo หลายชั้น ซึ่งยังไม่มีนโยบายยืนยัน; การรอนานไม่ได้เพิ่มข้อมูลจริง

ต้องตรวจเวลาตั้งแต่ input/guard/lookup/queue/model/validate/output ว่าขั้นไหนอยู่นอก deadline และบังคับ budget รวมให้ตรง contract โดยไม่ตัดเงื่อนไขตอบ นี่ไม่ใช่ concurrency/load test และไม่ใช่ production SLA; ไม่อนุมานสาเหตุจาก elapsed เพียงอย่างเดียว

## 3. Raw legacy grades ยังไม่ผ่านมาก และไม่ใช่ทั้งหมดเป็น protocol

| รายการ (grades; ซ้อนกันได้) | OFF | ON |
|---|---:|---:|
| strict pass / 503 | 133 | 125 |
| failed grades | 370 | 378 |
| protocol/outcome-only failure | 284 | 290 |
| content-contract failure | 30 | 32 |
| source-alignment failure | 39 | 39 |
| presentation failure | 30 | 30 |

ไม่ใช้ 133/503 หรือ 125/503 เป็น semantic accuracy เพราะ grades รวม route/intent/literal/latency แต่ก็ไม่อ้างว่าคะแนนที่ตกทั้งหมดปลอม ต้องอ่าน ALL_FAILED_GRADES ของ AUDIT_final20 คู่ source/time และคำอธิบาย REMAINING_FAILURE_ANALYSIS_TH.md

ตัวอย่างที่คะแนนลดจาก final19 OFF: คำถามคืนอุปกรณ์ตอบจาก source ได้แล้วใน 0.444 s แต่ grader ต้องการวลี returned after use ขณะที่ actual คือ Please return ... after use พร้อม route ใหม่ knowledge; อีกข้อเป็น latency_ceiling ของคำถามอัดวิดีโอ ซึ่งเป็นปัญหาประสิทธิภาพจริง ไม่ลบทั้งสองออกจาก denominator

Native tests 84 ยังมี raw assertion mismatch 2 ข้อตาม contract เก่า ไม่มี raw errors มี versioned semantic contracts 4 ข้อแยก ไม่เรียก native ทั้งชุดว่าเขียว

## 4. การเผยแพร่ข้อมูลยังไม่เสร็จ

588 candidate records ยัง blocked publication; active release ว่าง approvals 0 ไม่เปลี่ยน default production DB สาเหตุมีทั้ง source factual review, validity ที่ไม่ทราบ และ core fields ที่ migration ยังขาด เช่น facet/completeness, bindings/preset/input_device, audience eligibility, resource operational status และ package units/calculation rules

บาง field เป็น metadata ทางเทคนิคที่เสนอจาก source ต่อได้ ไม่ใช่ทุก field ต้องให้คนมานั่งกรอกใหม่; บาง field เป็น facts ที่ไม่มีหลักฐานจริงห้ามเดา ดู PUBLICATION_BLOCKERS_TH.md ราย record และ OWNER_CONFIRMATION_REQUIRED_TH.md สำหรับคำถามที่ต้องถามเจ้าของอย่างเจาะจง

## 5. คำแปลที่แก้แล้วกับส่วนที่ยังไม่ได้รับรอง

390 missing control notes เติมและ agent source-review แล้ว มี 64 จุดปรับจาก model proposals พร้อม raw/reviewed/source lineage แยก ไม่ใช่งานค้าง 390 แถว แต่ไม่พิสูจน์ว่าทุกคำแปลช่องอื่นใน 588 records ถูกต้องทั้งหมด และไม่ใช่ human/owner approval หรือการตรวจ gameplay ทุก patch

## 6. ขอบเขต deployment

นำโค้ด 31 ไฟล์กลับ ROOT พร้อม before backups และ hash conflict checks; ร่างข้อมูลส่งไว้ใน folder ใหม่ ไม่มีการ publish/approve หรือ restart เว็บที่เปิดค้าง และ portable packages ยังไม่อัปเดต การเปิดเว็บเก่าค้างอยู่จึงไม่พิสูจน์ว่าโหลดโค้ดใหม่แล้ว

รอบนี้ไม่มี legacy arm ใหม่ ไม่มี full sweep 20,554 requests ต่อ flag และไม่มี real WordPress oracle ใหม่ ผู้ใช้ยืนยันสถานะจริงเดิมไว้แล้ว การตรวจครั้งนี้ใช้ saved fixtures/controlled unavailable แยกจากคำยืนยันนั้น
