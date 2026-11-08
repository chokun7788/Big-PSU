# 20 ชุดข้อมูลหลากหลาย — DEMO แยก

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เพิ่ม 20 ชุดสถานการณ์ที่ต่างกัน ชุดละ 24 หมวด รวม 480 รายการใหม่ รักษาฐานเดิม 240 รายการในโฟลเดอร์เดิม ชุดใหม่นี้ใช้สำเนาฐาน DEMO ที่รวม 720 รายการ ไม่เกี่ยวกับ Product จริง

เกมใหม่ทั้ง 20 เกมเป็นเกมแต่งขึ้นเพื่อกำหนดผลที่ควรตอบได้แน่นอน ราคา นโยบาย สถานที่ บุคคล ตาราง และการจับคู่ API สมมุติทั้งหมด คำแปลยังไม่ผ่านมนุษย์

## ผลล่าสุด

ทดสอบคำถามหลัก 5056 เคส ผ่านเกณฑ์เนื้อหาที่ต้องมี 2653 ไม่ผ่าน 2403 รวม control เดิม 96 เคส; ผลละเอียดแยกรูปแบบและสาเหตุอยู่ในรายงาน

ในเคสที่ผ่านมี 26 เคสพิมพ์ซ้ำซึ่งยังไม่เลือกหัวข้อ แต่ตอบหลายช่องจนมีข้อมูลที่ต้องการอยู่ด้วย แยก audit ใน SCORING_REVIEW.json จึงยังไม่ถือว่าผ่านด้านเข้าใจคำถามทุกเคส

HTTP 200 224/224 แต่ตอบผ่าน 116/224; บทสนทนา 160 ชุด/480 turns ผ่าน 360; LLM ตัวอย่าง 48 เคสผ่าน 5

[รายงานผลและสาเหตุอย่างละเอียด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/REPORT_TH.md)

## เปิดข้อมูลแต่ละชุด

ทุกไฟล์มีทั้ง 24 หมวด พร้อมค่าที่กรอก สถานะ known/unknown/not_applicable, ตัวอย่างคำถามไทย–อังกฤษ และ JSON อ้างอิง

| ชุด | ชื่อ | แพลตฟอร์ม | คน | เล่น / ใช้ช่องจอง | ดูข้อมูล |
|---|---|---|---|---|---|
| 01 | ดาวเหนือ / Northstar | Nintendo Switch | 1–4 | 60 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_01.md) |
| 02 | ดาวเหนือ พลัส / Northstar Plus | PS5 | 2–2 | 90 / 90 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_02.md) |
| 03 | ละอองฝน / Drizzle | VR | 1–1 | 30 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_03.md) |
| 04 | สายหมอก / Mist | Cockpit | 1–1 | 45 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_04.md) |
| 05 | บัวสีคราม / Indigo Lotus | PC | 1–1 | 60 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_05.md) |
| 06 | ปะการัง / Coral | Nintendo Switch | 2–4 | 120 / 120 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_06.md) |
| 07 | ตะวันอ่อน / Gentle Sun | PC | 5–10 | 120 / 120 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_07.md) |
| 08 | ฟ้าหลังฝน / After Rain | PS5 | 1–2 | 30 / 30 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_08.md) |
| 09 | ลมทะเล / Sea Breeze | PC | 3–12 | 180 / 180 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_09.md) |
| 10 | ห้องสมุดดาว / Star Library | PS5 | 1–4 | 60 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_10.md) |
| 11 | ต้นเฟิร์น / Fern | PC | 2–3 | 90 / 90 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_11.md) |
| 12 | ทองทราย / Sand Gold | VR | 1–1 | 20 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_12.md) |
| 13 | จันทร์เสี้ยว / Crescent | Cockpit | 1–1 | 60 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_13.md) |
| 14 | แสงอรุณ / Dawn Light | Nintendo Switch | 1–4 | 45 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_14.md) |
| 15 | กิ่งไผ่ / Bamboo | PC | 1–2 | 75 / 75 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_15.md) |
| 16 | เมฆขาว / White Cloud | PC | 1–1 | 60 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_16.md) |
| 17 | มะลิ / Jasmine | PS5 | 1–4 | 120 / 120 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_17.md) |
| 18 | กระเบน / Ray | PC | 1–1 | 60 / 60 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_18.md) |
| 19 | แปะก๊วย / Ginkgo | Nintendo Switch | 2–6 | 180 / 180 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_19.md) |
| 20 | รุ่งเรือง / Radiance | PC | 2–8 | 240 / 240 นาที | [เปิดชุด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/SET_20.md) |

## โครงสร้างไฟล์

- `records/`: JSON ใหม่ 480 รายการ
- `DEMO_720_ONLY.sqlite`: สำเนา DEMO รวมเก่า+ใหม่
- `content_final/`: ผลหลักครบ ไม่ใช้ log รอบที่ยังรันไม่ครบเป็นผลสรุป
- `experiment.py`: สร้างและรันทดสอบครั้งแรก
- `resume_content.py`: รันต่อจาก log ที่เก็บไว้
- `integration.py`: HTTP handler จริงและทางเข้า pipeline
- `extra_checks.py`: LLM จริงและบทสนทนา 3 รอบ

สคริปต์ปฏิเสธการเขียนทับผลเดิม ถ้าจะรันใหม่ให้สร้างโฟลเดอร์ผลใหม่ก่อน; ใช้ Python ที่มีใน r58 เดิม ไม่มีการติดตั้งเพิ่ม ผลทดสอบนี้ยังไม่ยืนยันว่าคำถามทุกสำนวนตอบได้ และไม่ได้เปิดข้อมูลตัวอย่างบนเว็บ Product จริง

