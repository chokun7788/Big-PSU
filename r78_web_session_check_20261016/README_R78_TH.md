# สำเนาทดลอง R78

แก้คำถามต่อสั้นหลัง profile, เลือกเกมหลังถามเรื่องแข่งขัน และราคา → ทั้งหมด/all → ชื่ออุปกรณ์ ทั้งไทยและอังกฤษ

## วิธีเปิด

เปิด **Open-New-Chat.cmd** ในโฟลเดอร์นี้ พอร์ตแชท **8115** ปิดด้วย **Stop-New-Chat.cmd** ของโฟลเดอร์นี้ ฟอร์มข้อมูลใช้ **Open-Data-Editor.cmd** พอร์ต **8116**

ใช้ Python runtime จาก PSU_Esports_Chat_New_R69 ข้างกัน และ Ollama/โมเดลตามการตั้งค่าเดิม ยังเป็น draft preview ไม่ใช่ portable release ไม่แทนเว็บเดิมอัตโนมัติ

รอบนี้ลองเปิด R77 แล้ว health/model connection จากเครื่องมือติด WinError 10013 จึงยังไม่ได้ยืนยันว่า R78 เปิดผ่าน TCP/browser ได้ ไม่ควรตีความผล handler ภายในเป็นผลทดสอบหน้าเว็บจริง

## ตัวอย่างลอง

1. Can I bring my own input peripheral? → Yes, but it is my own keyboard. → And my mouse?
2. ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม → ใช่ แต่เป็นเมาส์ของผม → คีย์บอร์ดด้วยได้ไหม
3. คำถามแรกเหมือนข้อ 2 → ใช่ แต่ใช้ตอนแข่ง → VALORANT
4. ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก → ทั้งหมด → PC
5. What are the service prices for visitors? → all → PC

## ผลและข้อจำกัด

- บทสนทนา 38/38, qualification regression 41/41, ชุดหลัก 43/43, scope 50/50
- ยังไม่มี model transport/generation success จึงไม่ใช่ model accuracy
- ราคาบางแถวมีช่วงมีผลสิ้นสุดแล้ว จะแจ้งว่ายังยืนยันราคาปัจจุบันไม่ได้ ไม่เอาราคาเก่ามารับรองใหม่
- ข้อมูลเดิม 602 heads และ R77 system เดิมอยู่ครบ

อ่าน REPORT_R78_TH.md และ FLOW_R78_TH.md สำหรับ log สาเหตุและงานที่ยังเหลือ
