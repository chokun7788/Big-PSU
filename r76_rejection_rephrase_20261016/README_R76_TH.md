# ทดลองสำเนา R76

เปิด **Open-New-Chat.cmd** ในโฟลเดอร์นี้ แชทใช้พอร์ต **8111** ปิดด้วย **Stop-New-Chat.cmd** ของโฟลเดอร์นี้ ฟอร์มข้อมูลใช้ **Open-Data-Editor.cmd** ที่พอร์ต **8112**

ใช้ Python runtime จากโฟลเดอร์ `PSU_Esports_Chat_New_R69` ข้างกัน และ Ollama/โมเดลตามการตั้งค่าเดิม เปิด LLM อยู่ ยังเป็น draft development copy ไม่ใช่ portable/release ใหม่ และไม่แทนเว็บที่เปิดอยู่โดยอัตโนมัติ

## ตัวอย่างที่แก้ในรอบนี้

1. ถาม `I attached incorrect proof of payment. How do I fix it?`
2. เมื่อบอทถามว่าหมายถึงแก้แนบสลิปผิดหรือไม่ ให้ตอบ `No, I mean how do I pay?`
3. บอทอ่านวิธีชำระจาก source ทันที ไม่ขอให้พิมพ์คำถามใหม่ซ้ำ
4. ถามต่อ `And when?` จะใช้เรื่องชำระเงินที่เพิ่งเปลี่ยนมาถาม

ภาษาไทยเช่น `ไม่ใช่ครับ หมายถึงจ่ายค่าจองยังไง` หรือ `ไม่ใช่ค่ะ หมายถึงหลังจองต้องจ่ายภายในกี่นาที`

ใช้ได้ในช่วงที่มีหัวข้อ profile รอให้เลือกตาม flow นี้ ไม่ได้ครอบคลุมคำแก้คำถามทุกชนิดแล้ว ถ้าพิมพ์แค่ `ไม่ใช่` จะยกเลิกหัวข้อเดิม ส่วนข้อมูลที่ยังไม่มีนโยบายยืนยัน เช่น โอนเกิน ยังไม่ถูกแต่งคำตอบเพิ่ม

## ผลและข้อจำกัด

อ่าน `REPORT_R76_TH.md`, `FLOW_R76_TH.md` และ `NEXT_STEPS_R76_TH.md`

- Parser 32/32; paired dialogue/fixture/state checks 34/34
- ชุดหลัก 43/43; scope 50/50; debug extraction 3/3
- ไม่รวมคะแนนเหล่านี้เป็น model accuracy; actual model attempt จากเครื่องมือยังติด WinError 10013
- HTTP handler ใน memory/live fixture ไม่ใช่ผลตรวจ browser/TCP/WordPress สด

ข้อมูลเดิม 602 heads และทุก logical table เหมือน R75; ข้อมูลตัวอย่างอยู่แยกใน verification ไม่ปนในฐานแชทจริง
