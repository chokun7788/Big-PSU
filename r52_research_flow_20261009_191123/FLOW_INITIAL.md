# Flow และบันทึกการพัฒนา r52

วันที่ 2026-10-09 · อ้างอิงงานวิจัยใน paper-search-results/20261009_181825_llm-serving-answers

## เกณฑ์วัด

แยก HTTP สำเร็จ, routing ตรงเจตนา, โมเดลจบ, ตอบครบรูปแบบ, เนื้อหาถูก, และเวลาตามเป้าหมายออกจากกัน ทุก loop ต้องมีผลก่อน/หลังและไฟล์ดิบ ไม่รันชุดเต็ม 20,000 เคส ไม่เปลี่ยนข้อมูลเจ้าของโดยเดา

## ลำดับลงมือ

1. Loop 1 — เก็บ baseline ของ frame rate/each box/across/งานเขียนและแปล แล้วแก้ routing และตัวตรวจชนิดคำตอบ ตรวจคำถามราคาจริงเป็น negative control
2. Loop 2 — ตรวจ format ของ steps/สองประโยค/การแปล/คำขอความยาว แก้ budget และ coverage ของรูปแบบ เก็บเหตุผล output ไม่ครบแยกจาก provider ใช้ไม่ได้
3. Loop 3 — ทดสอบผ่าน pipeline และเว็บจริงด้วยคำถามหลายสำนวน ตรวจ metadata เมื่อ timeout และเมื่อ stream ไม่จบ แก้เฉพาะสาเหตุที่ reproduce ได้
4. Loop 4 — ตรวจหลาย worker และ model gate สร้าง shared admission ที่ไม่เพิ่ม GPU concurrency โดยเดา ทดสอบสถานะผิดพลาดและเส้นทางใกล้เคียง สรุปข้อจำกัดพร้อมปรับ Flow

## Flow คำขอ

รับ raw + session/turn → ตรวจบริบท/ขอบเขต → แยกงานทั่วไปออกจากข้อเท็จจริงศูนย์ → อ่านแหล่งข้อมูลที่ตรง → เลือกรูปแบบและ budget ตามคำขอ → admission โมเดล → generate พร้อม deadline/TTFT/provider_done → ตรวจ coverage/ชนิด/ข้อเท็จจริง → ส่งคำตอบหรือเหตุผลที่ไม่สำเร็จ → commit ประวัติตามกลไกเดิม

## แผนรองรับคนพร้อมกัน

เริ่มจากแก้คอขวดที่ยืนยันได้และ admission รวมหลาย worker ก่อน งานคิวแบบ job API ต้องมี persist-before-ACK, idempotency, session ordering, deadline/cancel และ recovery หลัง restart ครบก่อนเปิดใช้ ห้ามเรียกคิวในหน่วยความจำว่า durable หรืออ้างว่าเพิ่ม workers แล้วตอบ LLM พร้อมกันได้บน GPU นี้

## การรักษาไฟล์

snapshot source/tests/data ก่อนแก้ + SHA256 อยู่ใน before/ และ before_hashes.json ผลใหม่อยู่ในโฟลเดอร์นี้เท่านั้น Git status ถ้าใช้ไม่ได้ให้ระบุข้อจำกัด ห้าม reset/revert/ลบ log

## สถานะเริ่มต้น

ยังไม่ถือว่า loop ใดผ่านจนมีผลการทดสอบจริง ขั้นที่ต้องใช้ GPU/หลายคนจะรายงานจำนวนคำตอบที่ผ่านเนื้อหาและจำนวน request ที่เสร็จแยกกัน
