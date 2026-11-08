# ลูป O — Return-equipment policy และการทบทวนข้อสันนิษฐานจาก IDs

**แนวทาง underscore ด้านล่างไม่ได้ใช้:** การทดลอง IMPORTED_FAQ_TITLES_1.json ไม่ผ่าน และตรวจ raw record แล้วพบว่า return_equipment_games เป็นส่วนของ record_id ไม่ใช่ FAQ.question ได้ย้อนเฉพาะโค้ดทดลองนั้นออก เก็บผลทดลองไว้ ไม่อ้างว่าปรับ title normalization สำเร็จ

## หลักฐาน

final19 มี model timeout กับ What is the studio policy for return equipment games? ตอนแรกเข้าใจจาก ID ว่าเป็นหัวข้อ underscore แต่ตรวจจริงพบหัวข้อ Return equipment and game discs กับคำตอบคืนอุปกรณ์หลังใช้ ดังนั้นปัญหาคือ policy topic selection ยังไม่มีความหมายเรื่องคืนอุปกรณ์ ไม่ใช่การแทน underscore

## ทบทวน 1

ขยายเฉพาะชื่อที่มาจาก FAQ.question ของ source จริง เมื่อเป็น Latin underscore-separated topic tokens ให้รับช่องว่างแทน underscore ไม่อ่าน record_id มาเป็นคำตอบ ไม่เพิ่มชื่อเกม/ราคาหรือ alias เจาะคำถาม ไม่แก้ source strings

## ทบทวน 2

คงขอบเขตตัวเลข/คำ ไม่เปลี่ยน PC99 เป็น PC9 และไม่ทำ underscore conversion ให้ IDs ทุก kind ถอน record แล้วต้องไม่กลับเข้ามา รักษา ambiguity ถ้าหัวข้อชนกัน ไม่ force เลือกตัวแรก

## ทบทวน 3

ทดสอบคำถามจริงที่ timeout แบบห้าม network model, กรอบคำถาม policy และ negative ใหม่ การตอบยังอ่าน answer/evidence จาก source เดิม ใช้ final20 OFF/ON ตรวจ app/data frozen ใหม่ทั้งหมด ไม่เปลี่ยนผล final19 เดิม

## Flow ที่นำไปใช้จริง — ทบทวนจาก source

### รอบ 1 — แยกความหมาย return

return/returning + equipment/controllers/game discs ในคำถาม policy หมายถึงนโยบายคืนอุปกรณ์ ต้องไม่จับ refund เป็นหัวข้อนี้ และไม่เปลี่ยน tournament rules เป็นนโยบายศูนย์

### รอบ 2 — เลือกหัวข้อจากข้อมูลจริง

ใช้ FAQ.question ที่มี Return equipment/คืนอุปกรณ์ ไม่อ่าน record_id เป็นชื่อหรือคำตอบ ไม่ฝังคำตอบ after use หรือเลขกฎใน router ข้อความตอบมาจาก field.answer และ evidence เดิม ถ้าไม่มีหัวข้อ source ที่ตรงให้คง fallback

### รอบ 3 — ตรวจ negative และรูปประโยค

ทดสอบ policy for return equipment games, policy on returning equipment and game discs, นโยบายการคืนอุปกรณ์และแผ่นเกม โดยห้าม network call รวม refund, competition, ไม่มี source, ID ที่มีข้อความแต่หัวข้อไม่ตรง และ policy ปลั๊กไฟ ต้องไม่ปะปนกัน RETURN_POLICY tests 6 กรณีต่อ flag
