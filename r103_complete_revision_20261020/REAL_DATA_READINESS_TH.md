# สถานะข้อมูลจริง: ตรวจแบบอ่านอย่างเดียว

รายงานนี้เป็น data readiness ไม่ใช่ผลการถามแชท ไม่ได้แก้ราคา/วันมีผล/approval เพื่อเปลี่ยนคะแนน

Heads ที่ไม่ถอน: 602; approval rows: 0; release rows: 0

| หมวด | จำนวน |
|---|---:|
| audience | 5 |
| center | 1 |
| closure | 3 |
| competition | 4 |
| competition_rule | 104 |
| contact | 1 |
| control_set | 43 |
| equipment_model | 16 |
| facility | 2 |
| faq | 190 |
| game | 51 |
| game_service | 70 |
| person | 25 |
| policy | 1 |
| procedure | 3 |
| rate | 24 |
| rental_package | 24 |
| resource | 14 |
| schedule | 7 |
| service | 8 |
| zone | 6 |

## วันที่มีผลยังไม่ยืนยัน

37 รายการในหมวดราคา/ราคาเหมา/ตารางเวลา

แม้เนื้อหามีตัวเลข ระบบยังต้องแยกระหว่าง “ตัวเลขที่ต้นทางเคยระบุ” กับ “อัตราที่ใช้ได้ในวันที่ถาม” การให้ผล unknown ในกรณีนี้อาจไม่ผ่าน keyword oracle เก่าที่ต้องการคำว่าบาท แต่ไม่ควรแก้ด้วยการสร้างวันมีผลเอง

รายละเอียด record IDs อยู่ใน REAL_DATA_READINESS.json; ฐานข้อมูลไม่เปลี่ยนจากการอ่าน
