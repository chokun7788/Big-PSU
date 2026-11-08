# Flow r56 · ทำประเด็นค้างจาก r55

1. snapshot/source/owner hashes และตรวจ runtime ก่อนแก้
2. สร้าง contract รายคำถามทั้ง156จาก source และ intent ที่ผู้ใช้ถาม; แยก unknown/live/checked ห้ามรวมเป็น accuracy
3. ตรวจ raw r55 แบบ offline โดยระบุว่าไม่ใช่ pipeline run แล้ว HTTP baseline บนรุ่นเดียว
4. แก้ข้อผิดจริงจากคำถามใหม่: หลายส่วน/negation/entity/filters/context; ไม่เดา owner policies
5. ทดสอบ source fixtures + held-out paraphrases + TH/EN rule coverage ทุกเกม และ legacy expectations ที่มีหลักฐาน
6. วัดคิว/load/fault recovery ของ candidate แยก fast/LLM/fixture live ไม่ยิง burst WordPress
7. ปรับ deadline/queue diagnostics และ lifecycle ที่ไม่ลบ log; refresh anonymous session คงพฤติกรรมเดิม
8. ตรวจ source/data/index/hash และสร้างแพ็กเกจใหม่สองแบบในโฟลเดอร์ใหม่ตาม runtime/dependencies ที่มี
9. เก็บทุกloop ผลไม่ผ่าน/ข้อจำกัด/owner questions; reportสถานะT01–T35ตามหลักฐาน ไม่เรียกทดสอบจำกัดว่าปิดทุกสำนวน

ไม่นำ full20k หรือบทความทั่วไป500คำเป็น gateของร้านเกม ไม่เปิด public ไม่เปลี่ยนแหล่งข้อมูลเจ้าของหรือ approval เพื่อเพิ่มคะแนน
