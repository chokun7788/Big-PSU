# ลูป K — ลำดับ intent ที่คำเดียวมีหลายหน้าที่

## หลักฐานที่ตรวจซ้ำจากคำตอบจริง

1. “ถ้าทำ PS5 เสียหาย ต้องเสียค่าปรับกี่บาท” และ English “how much is the fine” ได้ตารางค่าบริการแทนค่าปรับ เพราะ price cue มาก่อน damage policy
2. “How do I cancel a paid booking?” ได้กำหนดชำระเงิน 10 นาที เพราะ paid ถูกจับก่อน cancel action
3. “Is PC #03 available for Warzone today at 15:00?” ได้ข้อมูล installed games พร้อมข้อความว่าไม่ใช่ booking คำตอบไม่ได้อ้างว่าว่างแต่ยังไม่ตอบเวลาที่ถาม เพราะ live regex รับ available ตามด้วยเวลาโดยตรง และ presence reader จบก่อน live adapter

## ทบทวน 1 — ความหมายก่อนคำร่วม

damage + fine/pay เป็น policy; หาก target เป็นอุปกรณ์จริงให้เงินที่ถามเกี่ยวกับความเสียหายได้มาก่อนราคาใช้บริการ ไม่เปลี่ยน game damage/กฎแข่งให้เป็นนโยบายศูนย์; cancelled automatically due to unpaid กับผู้ใช้ต้องการ cancel เป็นคนละเจตนา

## ทบทวน 2 — เวลาและแหล่งข้อมูลสด

availability + explicit temporal cue แม้มีชื่อเกมคั่น ต้องไป live adapter ก่อน installation facts; static “does PC have Warzone installed” ยังใช้ source installation graph แยกจาก booking; อย่าสร้างสถานะว่างเมื่อ API unavailable

## ทบทวน 3 — ตรวจย้อนและสถานะร่าง

ทดสอบ TH/EN, damage fine vs normal hourly price vs competition penalties, manual paid cancellation vs payment timeout, timed availability vs static installation และ source-unavailable pipeline ใช้ fixture เดิม ไม่มีการเก็บ real booking oracle ใหม่; trace label ต้องไม่เรียกร่างหรือ synthetic view ว่า approved

เพิ่มเฉพาะ semantic priority และตรวจเงื่อนไข ไม่มีการเปลี่ยนนโยบาย ตัวเลข หรือ approvals งานรอบนี้แก้ technical route ได้ ส่วนข้อมูลที่ไม่ทราบยังรายงาน unknown
