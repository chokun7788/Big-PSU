# R83 — แก้ selector เฉพาะจุด ก่อนทดสอบใหญ่

## ขอบเขตที่อนุญาต

แก้ timeout ของคำถามไทยกับ binding ผิดของอังกฤษ แล้วทดสอบเฉพาะส่วนด้วย LLM จริงหลายสำนวน เทสใหญ่/full corpus รอคำสั่งผู้ใช้เพิ่มเติม ไม่รัน legacy หรือแขนปิด LLM

## หลักฐาน

รอบ R82 `20261017T074528Z-4c2b1f` มี 14/14 answer contracts ผ่านด้วยการถามยืนยัน แต่ selector 3 ครั้งมี timeout ไทย 2 ครั้ง และอังกฤษ 1 ครั้งเลือก procedure ถูกแต่คัด task_span/subject จากคำถามไม่ผ่าน การโหลดโมเดลเริ่มต้นใช้เวลามาก แยกจากเวลาประมวลผลคำถามที่ warm แล้ว

โปรโตคอล profile ปัจจุบันสร้าง binding หลายช่อง มีเพดาน output 420 tokens และใส่ candidate snippets สูงสุด 650 characters × 8 รายการ ทั้งที่ CommonAnswerer ต้องถามยืนยันหัวข้อก่อนอ่านข้อเท็จจริงอยู่แล้ว

## Flow ที่จะใช้

1. สำรองไฟล์ R78 ปัจจุบัน เก็บ hash, strict validator, R80 opening reply และฐานข้อมูลไว้เทียบ
2. ดึง candidate ตามเดิม แล้วตัดเฉพาะรายการที่ไม่มี profile และไม่ผ่าน independent-topic guard เดิม การเลือก subset นี้จะไม่ตัดรายการที่ผ่านเงื่อนไขรับเดิมโดยเกณฑ์นั้น
3. คงทางลัด R81 เมื่อผู้สมัครที่เหลือเป็น eligible profiles ทั้งหมด: ถามยืนยันทันที ไม่อ้างว่าโมเดลพิสูจน์ความหมายแล้ว
4. กรณีมี eligible profile ปนกับหัวข้ออื่น และผู้เรียกเป็นขั้นถามยืนยัน: ให้โมเดลเสนอ indices/ambiguous เท่านั้น ใช้ชื่อหัวข้อ, profile metadata และข้อความสั้น จำกัด output 70 tokens ไม่ให้สร้างคำตอบหรือคัด quote
5. หากเสนอ profile ให้สร้าง pending topic confirmation ผ่านตัวสร้างเดิม ทุกหัวข้อ profile ที่เข้าเกณฑ์ยังเปิดดูได้ ไม่สร้าง factual projection ไม่บันทึกว่า semantic truth หรือ binding ผ่าน
6. หากเสนอรายการทั่วไป ใช้ independent-topic guard และการอ่าน source/field ตามเดิม หากผลไม่ชัดหรือผิดรูปแบบ ให้ fallback/retry ที่ตรวจสอบได้
7. หลังผู้ใช้เลือกหัวข้อ จึงอ่าน revision ปัจจุบันผ่าน fingerprint, ownership/context/qualification/rejection guard เดิม
8. ผู้เรียกที่ต้องใช้ semantic binding จริงยังใช้โปรโตคอลเข้มเดิม ไม่ผ่อน quoted-span validator ไม่ยอมรับคำที่ไม่มีใน input
9. เก็บ timing, input/output tokens, candidate ที่ตัดและเหตุผล, model HTTP/schema/proposal/binding แยกจาก answer accuracy
10. ทดสอบ controlled contracts และบทสนทนาที่เกี่ยวข้อง จากนั้นทดสอบ LLM จริงใน candidate overlay ก่อนลง R78
11. หลังผลเพียงพอ ลงเฉพาะไฟล์ที่ผ่านด้วย hash guard รีสตาร์ต R78 ที่ตรวจตัวตนได้ แล้วทดสอบผ่านเว็บจริงชุดเล็กไทย/อังกฤษและกรณีสับสน

### เพิ่มจาก loop ทดสอบหลายสำนวน

คำว่า “โอนเงิน” ในคำถามแก้รูปหลักฐานไปตรง alias ของ FAQ เลขบัญชี ระบบเดิมเลือก FAQ ก่อนถึง entity selector แล้ว field coverage ล้ม จึงไม่มี pending state ให้ตอบ “ใช่” ต่อได้ เพิ่ม recovery เฉพาะเมื่อ validation เดิมปฏิเสธด้วย unresolved_query_clause: ยังคงไม่แสดงข้อเท็จจริงของ FAQ ที่ถูกปฏิเสธ แต่หากมี declared topic ที่เข้า task/context/ownership ให้ถามยืนยันหัวข้อนั้นจาก snapshot ปัจจุบัน รักษารายละเอียด rejected candidate ไว้ใน audit หากไม่มี topic หรือเป็น validation error ประเภทอื่น คง clarification เดิม

## ตรวจทาน Flow สามรอบ

- รอบ 1: ถ้าลด guard เพื่อให้ quote ผ่านจะทำให้รับหลักฐานแต่ง → คง strict validator เดิม เปลี่ยนหน้าที่ model เป็น topic proposal เฉพาะเส้นทางที่ยังไม่ให้ข้อเท็จจริง
- รอบ 2: ถ้าตัด candidate ตามคะแนนอย่างเดียวอาจเสียแหล่งถูก → ตัดเฉพาะแหล่งที่ guard เดิมจะปฏิเสธอยู่แล้ว บันทึกทุก ID และเหตุผล พร้อมทดสอบ invariant
- รอบ 3: ถ้าใช้ JSON success นับเป็น semantic success จะซ่อนปัญหา → topic proposal มีสถานะแยก ไม่อ้าง binding/equivalence ผ่าน และวัดผลคำตอบ/การเรียกโมเดล/การยืนยันคนละชุด

## เกณฑ์หยุดของรอบนี้

แก้เท่าที่มีหลักฐานและทดสอบเฉพาะส่วน ห้ามรัน full test แม้ชุดเล็กผ่าน รักษาข้อมูล/นโยบาย/ราคา/approvals/ไฟล์เก่าและ raw log ทุก attempt
