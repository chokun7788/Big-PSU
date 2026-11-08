# ลูป G — กลุ่มผู้ใช้และนโยบายที่ไม่มีหลักฐาน

## หลักฐาน

คำถาม “เล่น PC 2 ชั่วโมง บุคคลทั่วไปกี่บาท” คืนทั้งกลุ่ม General Adult/PSU Alumni and General Student/PSU Student and Staff แม้ยอด 140 ของกลุ่มที่ถามมีอยู่ สาเหตุ name.th ของ audience ใน R63 เป็นชื่ออังกฤษและ aliases ว่าง ตัวกรอง rate ทำงานเมื่อ resolve audience ได้ แต่ input ไทยไม่ได้ระบุ ID กลุ่ม

คำถามอายุเด็กและยืมกลับบ้านยังได้ตัวเลือก service fields ซึ่งไม่ได้ช่วยตอบข้อสงสัย ผู้ใช้ต้องได้คำตอบว่าขาดนโยบายเรื่องนั้น มิใช่ชวนเลือก platform/เวลาเล่นแทน

## Flow

1. Resolve audience จากชื่อ/aliases ที่ owner กรอกก่อน ตามด้วย bilingual semantic concepts ของชื่อกลุ่มที่มีอยู่เท่านั้น ไม่สร้าง audience ใหม่ ไม่ฝังราคา/ID/สิทธิ์
2. เฉพาะกลุ่มที่ผู้ใช้ระบุชัด เช่นบุคคลทั่วไป→กลุ่มชื่อ General Adult ถ้ามีใน source; “คนนอก/ไม่ใช่นักศึกษา” ยังไม่พอแยก adult/student จึงไม่ให้สิทธิ์ราคากลุ่มใดโดยเดา
3. กรอง rates ด้วย audience IDs ที่ resolve ได้และคง source/validity gate; สำหรับ budget ห้ามนำเรตราคาของอีกกลุ่มมาแสดงเป็นราคาของผู้ถาม
4. Policy question ที่ไม่มี source ตรงหลังค้นแล้ว ให้ระบุ unknown policy พร้อม scope/หัวข้อ แทน service-field picker; ถ้า source มีคำตอบตรงต้องตอบก่อน fallback

## ตรวจทานรอบ 1

ห้าม negative affiliation เช่นไม่ใช่นักศึกษา/ไม่ใช่บุคลากร กลายเป็น positive selector; ห้ามคนนอกทุกคนถูกตั้งเป็น General Adult; ไม่เพิ่มสิทธิ์หรือส่วนลด

## ตรวจทานรอบ 2

source สามารถตั้ง ID อะไรก็ได้ การจับคู่ใช้ชื่อ/semantics ไม่ตรวจชื่อ ID; กลุ่มที่ไม่มีใน catalog ต้องไม่ถูกสร้าง; ถ้ากลุ่มชื่อคล้ายหลายตัวต้องยังไม่เลือกอันเดียวโดยเดา

## ตรวจทานรอบ 3

ทดสอบไทย/อังกฤษ, คนทั่วไป/ศิษย์เก่า/PSU staff, คนนอกไม่ทราบกลุ่ม, negation, synthetic unrelated group, known damage/booking policies ต้องไม่ถูก unknown fallback แย่ง และ scope ของ unknown policy ต้องไม่กลบราคา/live/rules

เริ่มใช้หลัง final13 จบและเก็บ manifest เดิมแล้วเท่านั้น รอบยืนยันถัดไปต้องสร้าง app manifest และ snapshots ใหม่
