# ส่งมอบ r58.2 — ข้อมูลกลาง

## เริ่มใช้งานบนเครื่องนี้

- เว็บแชทที่เปิดพร้อมแล้ว: http://127.0.0.1:8098/
- หน้าเจ้าของข้อมูลเปิดไว้ในแท็บของแอป หากเปิดใหม่ใช้ `Open-Owner-Content.cmd` ใน `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\ready_package\PSU_Esports_Chatbot_Local` (ต้องมี local capability จาก launcher)
- มี Python 3.12 x64 และ validator ในโฟลเดอร์ ใช้ Ollama/โมเดลเดิมของเครื่องนี้ เครื่องอื่นยังต้องติดตั้ง Ollama และโหลดโมเดล
- `OWNER_CONTENT_GUIDE_TH.md` และโฟลเดอร์ `owner_content_docs` อยู่ในชุดใช้งาน

## ผลตรวจ

- targeted units **164/164**, เว็บ fixture **25/25**, smoke ของแพ็กเกจจริง **6/6**
- 24 หมวด / 155 fields; เพิ่มรายการผ่านฟอร์มแล้ว approve/publish อ่านได้โดยไม่เพิ่มชื่อในโค้ด
- ร่างจากข้อมูลจริง **41** รายการ, active release ยังว่าง ไม่เอาร่างไปใช้เป็นคำตอบหรืออนุมัติแทนเจ้าของ
- ตรวจ source hash: เปลี่ยนของเดิมเฉพาะ engine, supervisor, server และ builder; unexpected=[], missing=[]; common module ในแพ็กเกจตรง source=True
- รายงานความผิดพลาดทุก round เก็บไว้ รวม combined unit ครั้งแรกที่พลาดจากฐานรุ่นต้น ไม่ลบผลผิด

## ข้อจำกัดที่ยังเหลือ

คิว canonical 270 รายการย้ายเกมเป็นร่างแล้ว36 ยังมี234รายการรอ typed mapping; calculator/calendar/live ยังใช้ operational adapter เดิมในจุดที่ไม่ได้ย้าย; semantic LLM planner ยังถามเพิ่มกับบางประโยค ไม่กล่าวว่าทุกรูปแบบภาษาทำได้แล้ว ดู REMAINING_AND_DECISIONS_TH.md

ความถูกต้องจริงของสถานะสดที่ผู้ใช้ยืนยันก่อนหน้า แยกจาก fixture รอบนี้; เรื่องนโยบาย/วันที่มีผลที่ไม่มีหลักฐานยังรอตัดสินใจตามคำถามในคู่มือ

อ่าน Flow/คู่มือ/field reference/ผลทดสอบ ใน docs ของงานนี้หรือ owner_content_docs ของชุดใช้งาน ส่วน code และ schema อยู่ใน app/knowledge/common ของโปรเจกต์จริงแล้ว
