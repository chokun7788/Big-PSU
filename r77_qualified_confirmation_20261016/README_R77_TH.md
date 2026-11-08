# ทดลองสำเนา R77

เปิด **Open-New-Chat.cmd** ในโฟลเดอร์นี้ แชทใช้พอร์ต **8113** ปิดด้วย **Stop-New-Chat.cmd** ของโฟลเดอร์นี้ ฟอร์มข้อมูลใช้ **Open-Data-Editor.cmd** ที่พอร์ต **8114**

ต้องมีโฟลเดอร์ PSU_Esports_Chat_New_R69 ข้างกันสำหรับ Python runtime และ Ollama/โมเดลตามการตั้งค่าเดิม เปิด LLM อยู่ ชุดนี้ยังเป็น draft development copy ไม่ใช่ portable/release ใหม่ และไม่แทนเว็บที่เปิดอยู่โดยอัตโนมัติ การตรวจในรอบนี้ยังไม่ได้เปิด server/browser จริง

## ตัวอย่างที่แก้รอบนี้

1. ถาม `Can I bring my own input peripheral?`
2. เมื่อบอทถามว่าหมายถึงหัวข้อคีย์บอร์ด/เมาส์ส่วนตัวหรือไม่ ลองตอบต่อ:

| คำตอบผู้ใช้ | สิ่งที่ควรเกิด |
|---|---|
| Yes, but it is my own keyboard. | อ่านกฎอุปกรณ์ส่วนตัวที่มี source |
| ใช่ แต่เป็นคีย์บอร์ดของศูนย์ | ไม่ใช้คำห้ามของส่วนตัวมาตอบแทน; แจ้งว่ายังยืนยันกรณีนี้ไม่ได้ |
| Yes, but it is for a tournament. | ขอเกม/รายการแข่งขัน ถ้ายังไม่มี source scope นี้ |
| ใช่ แต่ผ่อนชำระได้ไหม | แจ้งว่านโยบายผ่อนยังไม่ยืนยัน ไม่ตอบกฎอุปกรณ์แทน |
| Yes, but how do I pay for my booking? | ใช้ source เรื่องชำระเงินใหม่; ถาม And when? ต่อได้ |

ถ้าตอบ yes ล้วนยังยืนยันหัวข้อเดิมตามปกติ หากเพิ่มเงื่อนไขที่ยังตีความไม่ได้ ระบบจะไม่ตัดส่วนนั้นทิ้งแล้วสรุปคำตอบเอง

## ผลและข้อจำกัด

- qualified02 41/41; ชุดหลัก 43/43; scope 50/50; rephrase regression 34/34
- เป็นคะแนน targeted contracts มีทั้งตอบจาก source/ถามเพิ่ม/unknown และ fixtures แยก ไม่ใช่ model accuracy ทั้งระบบ
- actual model attempt ยังได้ WinError 10013 / successes=0; จึงยังไม่ยืนยันการอนุมานจริง
- ข้อมูลจริง 602 heads เหมือน R76 ทุก logical table/hash; ไม่มี fixture แทรกหรือ owner approval ใหม่

อ่าน REPORT_R77_TH.md, FLOW_R77_TH.md และ NEXT_STEPS_R77_TH.md สำหรับรายละเอียด
