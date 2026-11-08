# งานต่อหลัง R76

## 1. โมเดลจริงและความหมายของ subject — ยังสำคัญสุด

R76 แก้ flow ปฏิเสธ/ถามใหม่ ไม่ได้ทำให้โมเดลเข้าใจทุก paraphrase การเรียกจากเครื่องมือยังได้ WinError 10013 ใน actual attempt ของ regression รอบนี้ ต้องมีสิทธิ์เชื่อมต่อที่อนุญาตก่อนทดสอบ semantic contrast/latency จริง ไม่ใช้ fixture แทนคะแนนโมเดล

ระหว่างนั้น agent ทำเองได้: ออกแบบ optional subject definition/typed constraints และ prototype ในข้อมูลตัวอย่างแยก ตรวจ update/withdraw/contradiction ให้ format กลางรับข้อมูลใหม่ได้โดยไม่เพิ่ม alias ประโยคถามทุกแบบ ข้อจำกัดที่ source ไม่ชัดต้องคง unknown

## 2. ขยาย dialogue repair อย่างมีขอบเขต

เสร็จใน R76: pending profile → no/ไม่ใช่ + คำถามใหม่ → source ใหม่ในข้อความเดียว, ถามต่อจาก context ใหม่ และไม่วนเสนอ declined profile ระหว่างยัง unresolved

ยังต้องทำ: that's not what I meant/จริง ๆ หมายถึง, yes-but/ใช่แต่มีเงื่อนไข, replacement เป็น fragment ที่ยังขาดหัวข้อ, typo ในคำตอบสั้น, การแก้คำถามหลัง generic name ambiguity/price selection และการแก้หลายหัวข้อในข้อความเดียว ควรแยก acknowledgement/qualification/new request ไม่สืบทอด facts จาก assistant prose

ทำเองได้ด้วย targeted fixtures และ actual handler แบบ memory จากนั้นตรวจ browser/state หลัง restart เมื่อเชื่อมต่อได้ ไม่จำเป็นต้องรัน full ชุดใหญ่ระหว่างปรับ parser

## 3. Retrieval และการเสนอหัวข้อเมื่อข้อมูลเพิ่มมาก

R75 เปิดทางเลือกครบ 13 profiles ผ่าน pagination และ R76 กรองหัวข้อที่ปฏิเสธแล้ว แต่โมเดลยังมี top-k/backstop จำกัด ต้องวัด recall@k/omission เมื่อเพิ่มหลายหมวดและคำเรียกใหม่ ปรับ indexing/reranking/definitions/prompt budget พร้อม domain/context guard ไม่ถือว่ามีคำว่า wrong/แก้ แล้วทุกปัญหาเกี่ยวกับสลิป

ทำเองได้: สร้างข้อมูลตัวอย่างแยกหลายขนาด วัดการเลือกและความครบของเมนู ไม่เอา fixtures เข้า production DB

## 4. เงื่อนไขย่อยและ source consistency

ตรวจ property question vs procedure, payment amount vs proof, ownership, competition vs studio, cancellation vs paid reschedule, ข้อปฏิเสธและคำถามหลายเงื่อนไข และตรวจ duplicate/validity/คำแปลที่ขัดกัน

ทำเองได้: source/relationship/coverage audits และแก้ส่วนที่หลักฐานยืนยัน ถ้าต้นทางให้ policy ขัดกันจริงหรือไม่มีคำตอบ ต้องให้เจ้าของตัดสินใจ ห้ามใช้คะแนน retrieval ตัดสินแทน

## 5. ข้อมูลที่ยังต้องเจ้าของ

การจัดการโอนเกิน/ขาด, ผ่อนชำระ, ระยะเงินถึง/ตรวจจ่าย และอายุ/ผู้ปกครอง ยังมีสถานะเดิม ดูคำถามเฉพาะใน `r73_scope_completion_20261016/OWNER_QUESTIONS_R73_TH.md`

ไม่เปิดประเด็น 12:00–13:00 หรือ occupancy VR 30 นาทีซ้ำ และไม่เปลี่ยนนโยบายที่ผู้ใช้ยืนยันแล้ว

## 6. ส่งใช้งานและวัดหลายผู้ใช้

R76 ยังเป็น development copy ใช้ runtime R69, common DB เป็น draft และไม่ได้อัปเดตเว็บ/portable เดิม ต้องตรวจ real model/browser/TCP, publish/rollback/update data, state หลัง restart และชุดภาษาไทย/อังกฤษที่เกี่ยวข้องก่อนจัดแพ็กเกจใหม่

หลังเรียกโมเดลจริงได้ จึงวัด concurrent requests แบบเพิ่มทีละระดับ แยก source-only/semantic/field planner/live และเวลารอคิว/สร้างคำตอบ/รวม ห้ามใช้เวลา controlled fixture เป็นเวลาตอบจริงหรือจำนวนคนสูงสุด
