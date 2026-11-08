# ลูป J — เปรียบเทียบราคาให้ครบ operands

## หลักฐาน

final15 OFF มี validation rejected 1 request: “Do guests pay the same rate as PSU students?” ตัว resolver จับ PSU students ได้ แต่ guests ยังไม่บอกว่าเป็นนักเรียน/ศิษย์เก่าหรือ General Adult และไม่มีบริการ จึงหลุดไปตอบเรต PSU หลายเครื่องพร้อม unresolved clause ไม่ใช่การเปรียบเทียบที่ผู้ใช้ถาม

## Flow และทบทวน 3 รอบ

### รอบ 1

ราคา + same/different/compare ต้องมีอย่างน้อยสองกลุ่มและ scope บริการ หากขาดให้ถามส่วนที่ขาด ไม่เลือกเรตของ operand ฝั่งเดียวมาตอบเป็นผลเปรียบเทียบ และไม่ตั้ง visitors เป็น General Adult

### รอบ 2

อ่าน rates ตาม declared service/audience เช่นเดิม เปรียบเทียบได้เมื่อแต่ละกลุ่มมี current known-validity rate เดียวและฐานหน่วย/ระยะเวลา/จำนวนคน/สกุลเงิน/สูตรเหมือนกัน ไม่เปรียบเทียบ 30 นาทีต่อคนกับ 60 นาทีทั้งเครื่องหรือข้ามอัตราหมดอายุ

### รอบ 3

เก็บ raw final15 ที่หยุดตามเหตุผลแยก เพิ่ม tests ไทย/อังกฤษเรื่อง missing audience/service, current equal/different, unknown/expired validity และ incompatible unit; ไม่ลด validation gate หรือเขียนราคาทับเพื่อให้ผ่าน; reader ยังแสดง source-backed rates ตามจริงและผลที่เทียบไม่ได้เป็น partial

## ผลทบทวนระหว่าง implementation

เปรียบเทียบมีทั้งสองกลุ่มในบริการเดียวและสองบริการสำหรับกลุ่มเดียว จึงต้องเก็บ axis และ operands ใน typed state หากถามส่วนที่ขาด ผู้ใช้ตอบแค่ PC/ชื่อกลุ่มแล้วต้องเติม slot ได้ ไม่สูญเสียอีกฝั่งหรือเดา visitors เป็น General Adult

พบชื่อ target สองตัวหายเหลือหนึ่งเพราะ named() ใช้ alias ที่ไม่ปรากฏในคำถามมาตรวจ nested match: สองบริการมี platform alias PC ร่วมกัน แต่คำถามระบุชื่อสองบริการคนละตำแหน่ง จึงแก้ให้ suppress เฉพาะ span ที่ปรากฏจริงและถูกชื่อยาวกว่าครอบอยู่ ทดสอบทั้ง shared unobserved alias และ PC ที่อยู่ใน Gaming PC จริง
