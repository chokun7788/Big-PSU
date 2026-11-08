# ลูป N — ใช้ trace แก้ timeout ที่ยังพบ

## หลักฐานรอบ final18

matrix ON มี 3 transport timeouts: esports learning, คำไร้ความหมาย asdfghjkl ที่มีคำเกริ่นไทย, และ personal laptop/power outlet คำถามสุดท้ายมี source ตรงกันสองรายการอยู่จริงว่าใช้ปลั๊กไฟอุปกรณ์ส่วนตัวต้องขออนุญาตก่อน (ข้อ 4.8) แต่ไปเสียเวลากับ model selector

## ทบทวน 1 — ไม่เอา success ของ API มาแทนคำตอบถูก

หัวข้อปลั๊กไฟใช้ semantic operation/policy และเลือก FAQ จาก heading/topic ที่มี source จริง เหมือน damage policy ไม่ฝังคำตอบหรือเลขข้อใน routing ขอบเขตการแข่งขันยังอยู่ใน rules path ไม่ทำ keyboard/mouse permission เหมารวมเป็น power policy

## ทบทวน 2 — เงื่อนไขที่ตรวจอยู่แล้วควรเกิดก่อนเรียก model

selector ปัจจุบันตรวจ independent topic alignment หลังได้ indices; ถ้าไม่มี candidate ใดผ่านเงื่อนไขนั้นตั้งแต่ต้น ไม่ควรเรียก model ให้เสีย deadline ตรวจล่วงหน้าเฉพาะกรณีไม่มี candidate ที่มี anchor เลย เมื่อยังมี anchor ให้กระบวนการเดิมตรวจทุก index ต่อ ไม่ลด semantic guard หรือยกระดับ raw ranking score เป็น confidence

## ทบทวน 3 — ตรวจ negative และขอบเขตเดิม

ทดสอบ permission ไทย/อังกฤษหลายรูป, personal laptop vs device peripherals vs competition, ไม่มี source ต้องไม่สร้างกฎขึ้นเอง และใช้ mock ยืนยันข้อความไร้ topic anchor ไม่เรียก network model ตรวจ actual pipeline ของ esports learning อีกครั้งโดยไม่มีการไปแต่ง source ใหม่

ลงมือหลัง final18 code freeze จบเท่านั้น; ทดสอบรวมกับร่างคำแปล M ใน final19 OFF/ON ไม่เรียกแขน legacy ใหม่
