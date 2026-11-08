# Flow R75 — เมื่อความหมายยังไม่แน่ชัด ให้เลือกหัวข้อก่อนอ่านคำตอบ

## สิ่งที่ต้องแก้ต่อจาก R74

R74 ตรวจว่า JSON/quote/index ถูกต้องแล้วอ่านคำตอบได้ แต่ยังรับแผนควบคุมที่อ้างผิดว่า proof of identity เท่ากับ payment slip ได้ การตรวจรูปแบบจึงไม่พอรับรองความหมาย อีกปัญหาคือ task backstop ส่งได้เพียง 4 profiles และ candidate สูงสุด 8 เมื่อเพิ่มข้อมูลจึงมีหัวข้อที่โมเดลไม่เห็น

R75 ป้องกันการนำ proposal ที่ยังไม่ยืนยันมาแสดงเป็นคำตอบเต็ม โดยให้ผู้ใช้เลือก **หัวข้อที่ต้องการถาม** ก่อนอ่าน source วิธีนี้เพิ่มหนึ่งรอบสนทนาในกรณี semantic-only; ไม่ใช่การอนุมัติราคา/นโยบาย และไม่ได้อ้างว่าโมเดลเข้าใจ paraphrase ได้ถูกแล้ว

## ขั้นตอนพัฒนาและใช้งาน

1. สร้างสำเนา system/DB แยกจาก R74 ใช้ SQLite backup พร้อม manifest เก็บผลทุกชุดในโฟลเดอร์ใหม่ ห้ามแก้ original/old logs/approvals
2. Direct profile ที่ตรง task+subject+ownership+context ชัดแบบเดิมยังอ่าน source ได้ตามเดิม ไม่ถามยืนยันเพิ่มทุกคำถาม
3. ถ้าใช้ semantic model จนได้ profile binding ให้เก็บเป็นข้อเสนอหัวข้อเท่านั้น ยังไม่ render steps/decision/answer
4. ถ้าโมเดลไม่พร้อมหรือไม่เลือกรายการ แต่จำแนก task ได้ ให้เสนอหัวข้อจาก profile metadata ที่มีและยัง effective ในบริบทนั้น ไม่อ้างว่าฐานไม่มีคำตอบ และไม่รับปากเรื่องที่ไม่มี policy
5. ให้ unconfirmed topic ที่รู้ชัด เช่น โอนเกิน/ขาด/ผ่อน/ระยะเงินถึง/อายุ ใช้ข้อความเฉพาะเรื่องเดิมก่อน ไม่เสนอขั้นตอนสลิปผิดทับคำถามยอดเงิน
6. ถ้ามีหัวข้อเดียว ถามว่า “หมายถึงหัวข้อนี้ใช่ไหม” พร้อมชื่อจาก source; ถ้ามีหลายหัวข้อ แสดงครั้งละ 6 และให้เลือกเลข/ชื่อหัวข้อ พร้อม next/ถัดไป
7. เก็บ pending ใน common_read_state ของ server: record IDs, routing fingerprints, page ไม่เก็บคำตอบ/ราคา/steps จากข้อความก่อนหน้า
8. รับคำตอบสั้นเฉพาะ pending ล่าสุดที่ server ส่งแล้ว ถ้า yes กับหลายข้อห้ามเลือกข้อแรก ถ้าเลขไม่อยู่หน้าที่แสดงห้ามเลือกหัวข้อซ่อน ถ้า no ให้ปิด pending ถ้าเปลี่ยนเรื่องให้ดำเนินคำถามใหม่
9. รับ bare subject ที่ประกาศใน metadata หรือชื่อ source แบบ exact เมื่อชี้ได้หนึ่งรายการ ไม่ใช้การพบคำหนึ่งในประโยคใหม่เพื่อสืบทอด task เก่า
10. ก่อนอ่านคำตอบ ตรวจว่ารายการยังอยู่/effective และ kind/query_profile ยังมี fingerprint เดิม ถ้า scope เปลี่ยนหรือถูกถอนให้ถามหัวข้อใหม่ ถ้าเปลี่ยนเฉพาะ steps ให้ใช้ steps ฉบับปัจจุบัน
11. หลังผู้ใช้เลือก ใช้ default fields ของ kind ผ่าน source renderer/authority/validity/evidence ตามเดิม ไม่เรียก field planner แปลคำว่า yes ซ้ำ และไม่สร้าง owner approval
12. เปิดทางดู profiles ทั้งหมดที่เข้ากับ task/context แยกจาก top-k ของโมเดล จัด backstop ด้วย score+ID ให้ deterministic พร้อม audit จำนวนที่ส่ง/ตกหล่น ไม่เรียกว่าแก้ semantic retrieval recall ครบแล้ว
13. ตรวจคำว่า correct ที่เป็น adjective กับ verb แยกกัน เช่น correct file format ไม่ใช่คำขอแก้สลิป แต่ how do I correct the slip เป็น correction task
14. ทดสอบ dispatcher, source revision/withdraw, client spoof, session isolation และ HTTP handler แบบ memory แยกจาก TCP/browser/โมเดลจริง ไม่รัน legacy/OFF/full ชุดใหญ่
15. ตรวจ logical DB ทุกตารางและ source manifest พร้อมเขียนรายงานและรายการงานที่ยังเหลือ ห้ามรวมคะแนน controlled checks กับ accuracy ของโมเดล

## ทบทวนสามรอบ

### รอบ 1 — กันผิดเรื่องจาก semantic proposal

R74 binding ที่ผ่านโครงสร้างยังรับ false equivalence ได้ จึงย้ายอำนาจจาก “โมเดลกล่าวว่า equivalent” เป็น “ผู้ใช้เลือกหัวข้อที่แสดงจริง” ก่อนตอบ source เส้นทาง literal เดิมยังคงเดิม ไม่ใช้ model-written facts

### รอบ 2 — ป้องกัน state ผิดและข้อมูลเก่า

เพิ่ม latest-turn barrier, server_written/client_acknowledged, cancel, new topic, visible-page numbers และ routing fingerprint ไม่ให้ client history ที่ส่งมาเองหรือข้อมูลถอนแล้วทำให้ yes กลายเป็นคำตอบจาก source ผิด การยืนยันหัวข้อไม่ยืนยันนโยบายหรือความถูกต้องของ source

### รอบ 3 — เพิ่มข้อมูลและตรวจ trade-off

เมนู 13 หัวข้อยังเลือกได้ทุกข้อ แม้โมเดลเห็นไม่ครบ ไม่อ้างว่าโมเดลค้นครบหรือ ranking ดีที่สุด ยังต้องพัฒนาการค้น/คำจำกัดความ subject และวัด real-model accuracy/latency ภายหลัง การถามเพิ่มช่วยลดการยืนยันผิดเรื่อง แต่มีต้นทุนหนึ่งรอบสนทนาและอาจเสนอหัวข้อไม่ตรง จึงต้องติดตาม UX และการยกเลิกหัวข้อด้วย
