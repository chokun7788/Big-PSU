# ทบทวนตัวเร่งการประเมินก่อน matrix final13

## ปัญหาที่พบ

โค้ด named() จริงมี Latin word-boundary guard ใน bounded fuzzy เพื่อไม่ให้คำปกติที่มีชื่อเกมเป็นส่วนหนึ่งถูกแก้ไปเป็นชื่อเกม ตัวช่วย equivalent_name_pruning ใน harness ซึ่งรวมหน้าต่างคำเพื่อประหยัดเวลา เคยขาดเงื่อนไขนี้ จึงไม่ควรอ้างว่าตัวเร่งเทียบเท่าทุก branch จากชื่อฟังก์ชันอย่างเดียว

## วิธีแก้

เก็บตำแหน่งเริ่มของ span ใน grouped windows แล้วตรวจ ASCII alphanumeric ก่อน/หลังตาม alias แบบเดียวกับ production ภายในลูป alias ไม่กรองตามตัวอักษรใน span เพราะจะเปลี่ยน semantics ของ alias ไทยที่มีข้อความผิดภาษาแทรก

## หลักฐาน

EVALUATOR_EQUIVALENCE_1.json: 654 ข้อความแบบ deterministic seed รวมชื่อจริง/คำปกติ/เติม-ลบ-แทน-สลับตัว/คำหุ้มชื่อ/หมายเลขรุ่นและหมายเลขเครื่อง เปรียบเทียบ original named กับตัวเร่ง ไม่พบผลต่างในชุดนี้ ไม่ใช่ mathematical proof สำหรับทุกข้อความ

แก้เฉพาะ harness ก่อน matrix worker final13 เริ่ม โค้ด app ที่กำลังทดสอบไม่ถูกแก้ matrix ทุก request บันทึก SHA256 ของ harness และ verifier ต้องเห็น hash เดียวกันทั้ง OFF/ON ผลรอบก่อนเก็บไว้ ไม่ rewrite คะแนนย้อนหลัง

ผล timing ของ matrix ใช้ evaluator pruning จึงไม่ควรถือว่าเป็น production SLA; actual HTTP gates ใช้ session/ACK จริงและมีขอบเขตการทดสอบแยกในรายงาน
