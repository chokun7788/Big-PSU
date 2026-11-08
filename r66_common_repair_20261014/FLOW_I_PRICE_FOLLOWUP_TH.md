# ลูป I — ข้อกำหนดราคาในบทสนทนาต่อเนื่อง

## หลักฐาน

หลังถามบุคคลทั่วไป PC 2 ชั่วโมง ถาม “แล้ว 1 ชั่วโมงล่ะ” ยังคำนวณ 70 ได้แต่ validation บอก unresolved_query_clause ส่วน “ถ้าเป็นศิษย์เก่าล่ะ” ได้ None เพราะชื่อ audience ภาษาไทย resolve เฉพาะ price operation ที่ explicit ไม่มี context ของราคาเข้ามาช่วย

## Flow และทบทวน

### รอบ 1

เก็บ duration constraint จาก requested_minutes ที่ consistent ของแผนคำนวณ ไม่เก็บยอดรวม/ราคาเป็น facts สำหรับตอบครั้งถัดไป ผู้ใช้เปลี่ยน duration ต้องชนะค่าเก่า; เปลี่ยน audience ต้องคง service และ duration ที่ถามไว้ แล้วอ่าน rate ใหม่

### รอบ 2

รับ bare audience follow-up เฉพาะหลัง amount_minor และรูปประโยคเลือกกลุ่มสั้น ไม่มีเจตนาใหม่แทรก; ความเป็นคนนอกหรือการปฏิเสธกลุ่มไม่ถือว่าได้อีกกลุ่มอัตโนมัติ; ไม่เอา duration ข้ามไปเรื่องเปิด-ปิด/live/เกม/นโยบาย

### รอบ 3

state เก็บ constraints แบบชนิดข้อมูลและขอบเขตจำกัด; single duration เท่านั้น; inherited constraint มี trace; explicit quantities และ semantic clauses อื่นไม่ถูกตัดทิ้ง; validity/withdrawal/calculation_rule ของ rate ยังตรวจทุกครั้ง ตรวจ TH/EN, เปลี่ยนกลุ่ม/เวลา, เปลี่ยนเรื่อง และ extra clause ที่ไม่ควรถูกยอมรับเป็น selection

เก็บ final14 ที่หยุดเพราะพบข้อนี้แยก ไม่อ้างเป็น complete OFF/ON ไม่มีการแก้ app ระหว่าง matrix ทำงาน

## ผลจาก implementation

- state เก็บเฉพาะ duration_minutes ที่ผู้ใช้ขอและมีค่าเดียว ขอบเขต 1–1440 นาที ไม่เก็บยอดเงินเดิมเป็นข้อเท็จจริง
- short audience/quantity follow-up มี query interpretation แยกจากข้อความดิบ; audit ระบุ inherited_constraints; explicit quantity ใหม่ชนะค่าเดิม
- Thai/English 3-turn tests เปลี่ยน General Adult→alumni→duration ใหม่ และมี negative new-topic/extra-clause
- พบ Owner preview JS ประกอบ state เองจน scope/operation/duration หาย จึงเพิ่ม common_read_state ใน preview API และให้ browser ใช้ state จาก backend เดียวกับ Chatbot ตรวจ actual HTTP ทั้งสองภาษาโดยไม่เขียน approvals
