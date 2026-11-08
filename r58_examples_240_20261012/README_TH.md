# ชุดทดลอง format กลาง — 240 รายการ / 24 หมวด

**ข้อมูลแยกสำหรับสาธิตเท่านั้น ไม่เกี่ยวกับ Product จริงของ PSU**

วันที่อ้างอิง 12 ตุลาคม 2026 เวลาไทย ชุดนี้ตั้งใจใช้ทดลองเพิ่มข้อมูล ถามคำถาม และแก้ข้อมูลเดิม ไม่ใช่การยืนยันบริการของศูนย์

## เปิดลองใช้

1. เปิด `Open-DEMO-ONLY.cmd` ในโฟลเดอร์นี้
2. จะเปิดหน้าเว็บที่มีแถบ “DEMO ONLY — NOT PRODUCTION” ด้านบน ใช้ฐาน `DEMO_ONLY.sqlite` เท่านั้น
3. เลือกหมวดทางซ้าย จะพบข้อมูลตัวอย่าง 10 รายการต่อหมวด กดรายการเพื่อดูช่องที่กรอกแล้ว
4. ส่วน “ทดลองคำตอบจากข้อมูลที่เผยแพร่” ด้านล่าง ใช้ถามข้อมูลชุดนี้ เลือกไทยหรือ English ได้
5. ถ้าจะแก้ตัวอย่าง: แก้ช่อง → บันทึกร่าง → ตรวจทานและอนุมัติ → เผยแพร่ ฉบับร่างและฉบับอนุมัติยังไม่เปลี่ยนคำตอบจนกว่าจะเผยแพร่

ใช้ Python ที่มีอยู่ใน `../r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/runtime/python` จึงต้องวางชุด r58 เดิมข้างโฟลเดอร์นี้ ยังไม่ใช่แพ็กเกจพกพาที่มี runtime ของตัวเอง

ตัวเปิดใช้งานเลือกพอร์ตว่างเอง เปิดซ้ำจะเปิดหน้าเดิม ไม่ต้องกำหนด URL หรือคัดลอก token หน้า preview อ่านฐานกลางโดยตรงและไม่เรียก WordPress สด

## คำถามเริ่มต้น

```text
ตัวอย่าง Minecraft เล่นยังไง
ตัวอย่าง ข้อมูลศูนย์ 01 ขอข้อมูลทั้งหมดทุกส่วน
ตัวอย่าง ราคาต่อบริการ 01 ขอข้อมูลทั้งหมดทุกส่วน
ตัวอย่าง ราคาเหมาโซน/ห้อง 01 ขอข้อมูลทั้งหมดทุกส่วน
Demo game 05 What is this game about?
Demo rate 01 Show all information
```

สำหรับหมวดอื่น ใช้ชื่อหรือ alias ในไฟล์คำถามที่เก็บไว้ แล้วเติม “ขอข้อมูลทั้งหมดทุกส่วน” ตัวอย่างใช้ `01` ถึง `10` เพื่อแยกรายการที่ชื่อคล้ายกัน

**คำถามทั่วไปยังมีส่วนตอบผิด:** อย่าใช้การเปิดหน้าได้หรือการนำเข้าผ่านเป็นหลักฐานว่าคำถามทุกแบบตอบถูก ผลจริง 5,020 คำถามผ่าน 4,250 ผิด 770 เคส เก็บไว้โดยไม่ลบ

## ข้อมูลมาจากไหน

คำอธิบายเกม 10 เกมค้นจากหน้าผู้พัฒนา/ผู้จัดจำหน่าย ใช้ชื่อ ประเภท เนื้อหา และวิธีเล่นเบื้องต้น แปลและเรียบเรียงสั้น ๆ ส่วนชื่อศูนย์ เครื่อง การติดตั้ง จำนวนคน ราคา ข้อกำหนด ตาราง ปุ่มควบคุม รายการแข่ง ข่าว ทีมงาน และการจับคู่สถานะ API เป็นข้อมูลสมมุติที่เขียนเพื่อทดสอบ

ตัวอย่างปุ่ม `DEMO_KEY_01` ไม่ใช่ปุ่มเล่นเกมจริง URL `example.invalid` และอีเมลตัวอย่างไม่ใช่ช่องทางติดต่อจริง ไม่ได้ตรวจเวอร์ชันล่าสุดหรือเรตอายุ จึงคงเรตอายุเป็น “ไม่ทราบ” คำแปลยังไม่ได้ตรวจโดยมนุษย์

ทุก record มีรหัสขึ้นต้น `demo_` ทุก source ใช้ `fixture/synthetic` และมีคำเตือน ระบบ production ปฏิเสธ source ชนิดนี้ ฐานทดลองต้องเปิดใช้ DEMO อย่างชัดเจนก่อนอ่าน

## เลือกดูตัวอย่างแต่ละหมวด

| หมวด | จำนวน | ตัวอย่างที่กรอกครบ |
|---|---:|---|
| ข้อมูลศูนย์ (`center`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_center.md) |
| โซนบริการ (`zone`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_zone.md) |
| รุ่นและสเปกอุปกรณ์ (`equipment_model`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_equipment_model.md) |
| เครื่องหรือทรัพยากรจริง (`resource`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_resource.md) |
| รายการที่เลือกในระบบจอง (`service`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_service.md) |
| ข้อมูลเกม (`game`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_game.md) |
| กลุ่มผู้ใช้ (`audience`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_audience.md) |
| ติดต่อ (`contact`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_contact.md) |
| ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_procedure.md) |
| นโยบายและกฎศูนย์ (`policy`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_policy.md) |
| สิ่งอำนวยความสะดวก (`facility`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_facility.md) |
| เกมที่ศูนย์มีให้เล่นจริง (`game_service`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_game_service.md) |
| รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_game_mode.md) |
| วิธีเล่นและปุ่ม (`control_set`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_control_set.md) |
| ราคาต่อบริการ (`rate`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_rate.md) |
| ราคาเหมาโซน/ห้อง (`rental_package`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_rental_package.md) |
| ตารางบริการ (`schedule`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_schedule.md) |
| วันปิด/ข้อยกเว้น (`closure`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_closure.md) |
| รายการแข่งขันและฉบับกติกา (`competition`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_competition.md) |
| ข้อกติกาการแข่งขัน (`competition_rule`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_competition_rule.md) |
| ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_news.md) |
| บุคลากร/ทีมที่เปิดเผยได้ (`person`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_person.md) |
| คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_faq.md) |
| การเชื่อมสถานะสด (`live_binding`) | 10 | [เปิดตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/EXAMPLES_live_binding.md) |

## ผลและหลักฐาน

- [รายงานผลและวิเคราะห์ปัญหา](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/REPORT_TH.md)
- [รายการคำถามพร้อมสิ่งที่ควรตอบ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/QUESTIONS_EXPECTED.json)
- [คำตอบและเหตุผลที่เลือกครบ 5,020 เคส](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/ANSWERS_AND_DECISIONS.jsonl)
- [770 เคสที่ยังผิด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/content_final/FAILURES.json)
- [แหล่งข้อมูลเกม 10 เกม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/RESEARCH_SOURCES.json)
- [หลักฐานข้อมูลจริงไม่เปลี่ยน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/FINAL_PRESERVATION_RECEIPT_V2.json)

การแก้ตัวอย่างบนเว็บหลังวันนี้อาจทำให้ผลต่างจากรายงานเดิม ผลทดสอบนี้อ้างอิง release ใน MANIFEST และ record JSON ที่ส่งออกก่อนแก้ไข

