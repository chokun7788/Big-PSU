# อ้างอิงเว็บเฉพาะข้อความที่ตรวจแล้ว — 11 พฤศจิกายน 2026

เปลี่ยนใน candidate นี้เท่านั้น ไม่แก้ code/DB/ผลของ bounded_eval200 หรือ eval10 ที่วัดแล้ว และไม่เปลี่ยนสถานะเผยแพร่ของ owner records

## พฤติกรรม

1. Reader และ verifier ตรวจ claims/receipts ตามเดิม
2. `CommonAnswerer.finish` ตรวจ public citation registry เพิ่มก่อนส่งผล
3. ต้องตรง record ทั้งฉบับ, field, ข้อความที่ตรวจ, source ID/hash/locator และ hash ของ source snapshot จริง จึงใส่ URL ชื่อหน้าและ section
4. เมื่อแก้ record/revision ถอน record เปลี่ยนข้อความ หรือปลอม source mapping จะไม่ใช้การรับรองเว็บเดิม
5. กรณีไม่ผ่านจะซ่อนเครื่องหมาย `[S#]` และรายการอ้างอิงสาธารณะที่ว่าง แต่เก็บ hits และหลักฐานภายในไว้ ไม่ระงับคำตอบที่ผ่านตัวตรวจเพียงเพราะไม่มี URL
6. เว็บรองรับบางข้อความไม่ได้หมายความว่ารองรับทั้งคำตอบ ไม่เปลี่ยน draft เป็น published หรือรับรองวันมีผล/สถานะว่างจริง

Registry อยู่ `system/data/knowledge/verified_web_citations.json` มี 46 entries แยก field/output บางส่วนซ้ำเพราะรองรับทั้ง native reader และ typed engine ไม่ใช่ 46 requirement ที่เสร็จ

## ต้นทางและข้อจำกัด

- หน้าจอง `https://esports.computing.psu.ac.th/` อ่าน HTTP200 เก็บ HTML/hash ไว้ใน `website_source_audit_20261111`
- หน้า Members ของ `https://esports.phuket.psu.ac.th/about-us/Members` ตรวจได้จาก search cache; เปิดตรงซ้ำได้502 จึงระบุ cached และไม่รับรองตำแหน่งปัจจุบัน
- ไม่ใช้ภาพราคาเก่ารับรอง PC นักศึกษา PSU ราคา0บาท คงราคาที่เจ้าของยืนยันไว้ และไม่ขยายคำยืนยันนักศึกษาไปบริการอื่น
- พบคำตอบเดิมบาง record ว่าจองสูงสุด3sessions แต่เว็บแสดง6sessions จัดเป็น conflict ไม่ผูก URL รับรองคำตอบเดิม รอบนี้ยังไม่เปลี่ยน owner policy หรือแก้ข้อขัดแย้งใน DB
- หน้า entry คู่มือ/แข่งขัน/ดาวน์โหลดไม่ได้พิสูจน์ข้อความในภาพหรือเอกสารแนบทุกฉบับ กรณีเข้าเว็บไม่ได้หรือยังไม่อ่านไฟล์ใช้สถานะยังไม่ตรวจ ไม่อ้างว่าเว็บไม่มีข้อมูล

## ตรวจผลเดิม 200 คำถาม

รายงาน local `website_source_audit_20261111/CITATION_REVIEW_200.html` ครบ200แถว อ่านผลที่บันทึกไว้ ไม่เรียกโมเดลหรือวัดคะแนนใหม่ รวม typed claims กับ known native fields ที่ตรวจย้อนกลับได้ พบ244คู่ record/field:

- 24คู่รองรับข้อความทุก variant ที่พบ และ6คู่รองรับเพียงบาง variant
- 1คู่ขัดกับเว็บเรื่องจำนวนsessions
- 84คู่ต้องตรวจภาพ/เอกสารแนบ,22คู่ยังไม่ผ่านขอบเขตราคา,25คู่ยังไม่ผ่านขอบเขตเกม/อุปกรณ์,29คู่ยังไม่ผ่านขอบเขตบุคลากร,53คู่อื่นยังไม่ยืนยัน
- 31คำถามมีข้อความอย่างน้อยหนึ่งส่วนที่ใส่อ้างอิงได้ ไม่ใช่31คำถามที่รับรองว่าถูกทั้งหมด
- 64คำถามไม่มี observed claim/known native text ที่สกัดได้ใน trace นี้ จึงไม่รับรองอ้างอิงรายclaim ข้อความคำตอบเดิมยังแสดงให้ตรวจในรายงาน

## ผลตรวจใหม่

- `public_citations_1794384479868091300/RESULT.json`: ผ่าน22checks รวม naturalไทย/อังกฤษ,รักษาราคา0บาท,แก้/ถอน/ปลอมค่า และไม่ยกระดับเป็นpublished เป็น source-only
- `price_currency_1794384473154438100/RESULT.json`: affected regression ผ่าน12checks; ไม่มีmodel/HTTP
- `citation_http_1794384609586179900/RESULT.json`: HTTP3คำถามตามลำดับผ่าน9assertions — ยกเลิกการจองไทย/ห้ามสูบบุหรี่อังกฤษมีลิงก์ ส่วนราคาPCนักศึกษาคง0บาทโดยไม่ใส่อ้างอิงภาพราคา
- สำเนาแชตทดลอง `http://127.0.0.1:8139/`, version `R135-Bounded-citations`; ไม่มีการหยุด protected model
- เก็บ harness amendment: PinnedView แรกขาดpath ทำให้ยังไม่เริ่ม natural test; เพิ่มpathแล้วตรวจใหม่ ตัวสร้าง registry แรกใช้ชื่อ field ตารางผิดสองชื่อ ก่อนแก้ให้ตรง `service_slots` และสร้างสำเร็จ ไม่ใช้ผลล้มเหล่านี้อ้างว่าFlowตอบผิด

ยังไม่ผ่าน HTTP owner/editor lifecycle ใหม่ ไม่รับรอง semantic correctnessทั้ง200/ทั้งระบบ ไม่ใช่การ deploy production และไม่รัน200/2111ซ้ำ

## งานต่อ

ตรวจภาพ/เอกสารแนบเมื่อเข้าถึงต้นฉบับได้, แก้ความขัดแย้ง3/6sessionsใน candidate สำเนาพร้อม source receipts, ตรวจข้อมูลราคาและหน่วย/ช่วงคนแยกจากภาพ แล้วค่อยเพิ่ม mappings ที่ผ่านจริง ไม่ใส่ homepage แทนหลักฐานที่ขาด
