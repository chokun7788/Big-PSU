# เริ่มอ่าน: วิเคราะห์ Full Flow เดิมและ Format กลาง

วันที่จัดทำ: 18 ตุลาคม 2026 — รายงานจากโค้ดและผลทดสอบที่บันทึกไว้แล้ว

## สรุปภาษาง่าย

**ปัญหาหลักไม่ใช่แค่มีข้อมูลไม่ครบ:** การเปลี่ยนเป็น Format กลางเปลี่ยนตัวตีความและตัวเลือกคำตอบด้วย ข้อมูลบางเรื่องอยู่ในฐานแล้ว แต่ระบบยังไม่รู้ว่าคำถามต้องอ่านช่องไหน หรืออ่านแล้วถูกตัวตรวจขอบเขตปฏิเสธ จึงถามซ้ำ/ตอบไม่ตรงเรื่อง

ของเดิมสะสมตัวแก้คำผิด ตัวแยกเจตนา ตัวตอบแต่ละหมวด และตัวสืบต่อบทสนทนาไว้หลายชั้น ของกลางมีข้อดีด้านข้อมูลอ้างอิงและการแก้ไขข้อมูล แต่ยังไม่ได้รับพฤติกรรมเหล่านั้นมาครบ การย้ายข้อมูลอย่างเดียวจึงไม่ทำให้ตอบดีเท่าเดิมทันที

**แนวแก้ที่เสนอ:** ใช้ตัวตีความงานและตัวประกอบคำตอบที่เหมาะกับแต่ละหมวด โดยอ่านข้อเท็จจริงจากฐานกลางปัจจุบัน แล้วตรวจเงื่อนไข แหล่งที่มา และวันมีผล ไม่คัดลอกคำตอบราคา/นโยบายเก่ามาทับฐานใหม่

## อ่านตามลำดับนี้

- [1. Full Flow เดิม — input, session, คำผิด, routing, handlers, retrieval/LLM, output และการแก้ข้อมูล](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/01_FULL_FLOW_LEGACY_TH.md)

- [2. Full Flow กลาง — เจ้าของกรอก/แก้/เผยแพร่, preview, ข้อมูล 21 หมวด, interpretation, LLM/guard, joins และ output](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/02_FULL_FLOW_COMMON_TH.md)

- [3. ปัญหา 37 ประเภท — อาการ เหตุ หลักฐาน ผลที่ควรได้ แนวแก้ วิธีตรวจ และสิ่งที่ต้องใช้มนุษย์](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/03_PROBLEM_ANALYSIS_ALL_TH.md)

- [4. เทียบ Flow และแผนซ่อม — จุดต่างรายชั้น พร้อม target flow และลำดับทำงาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/04_FLOW_GAP_AND_REPAIR_TH.md)

- [5. เจาะคำตอบจริง 12 กรณี — เหตุใดจึงเลือกแบบนี้ สิ่งที่ควรตอบ และข้อจำกัดของคะแนน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/05_CASEBOOK_TH.md)

- [6. ความพร้อมข้อมูล — อะไรทำเองได้ อะไรต้องถามเจ้าของ และคำถามที่เจาะจง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/06_DATA_AND_OWNER_DECISIONS_TH.md)

## ผลเทียบที่ใช้เกณฑ์เดียวกัน

| ตัวชี้วัด | เดิม R64 + LLM ON | กลาง R88 + LLM ON |
|---|---:|---:|
| คำขอไม่ซ้ำ / เกณฑ์ประเมิน |20,554 /55,811|20,554 /55,811|
| Positive literal: มีข้อความที่เกณฑ์กำหนด |94.41%|72.10%|
| เกณฑ์เดิมทั้งหมด รวม route/intent/status |76.33%|9.02%|

**9.02% ไม่ใช่ความถูกต้องของเนื้อหา 9.02%** เพราะรวมสัญญา route/format เดิมซึ่งใหม่ใช้ต่างกัน ส่วน 72.10% ก็ไม่ใช่การรับรองความหมายทั้งคำตอบ: คำแปลต่างสำนวน การป้องกันราคาเก่าที่หมดอายุ หรือเกณฑ์ที่ตรวจแค่คำเดียว ยังต้องอ่านแยก

รายละเอียดไทย/อังกฤษ/auto และข้อจำกัดอยู่ในรายงาน 03 การเปรียบเทียบนี้ใช้คำตอบที่เก็บไว้แล้ว ไม่มีการเรียก chatbot หรือ LLM รอบใหม่

## อ่านคำศัพท์ในรายงาน

| คำ | ความหมายในระบบนี้ |
|---|---|
| entity / target | สิ่งที่ถามถึง เช่น PC, VR, เกม Tekken 8 |
| task / intent / operation | ต้องการทำอะไรกับสิ่งนั้น เช่น ถามราคา ปุ่ม กติกา สิทธิ์เข้าใช้ |
| field | ช่องข้อมูล เช่น summary, answer, amount_minor |
| relation / join | ความสัมพันธ์ เช่น เกมนี้มีบนบริการใด หรือโซนนี้มีอุปกรณ์ใด |
| clause / need | ส่วนย่อยของคำถาม หรือเนื้อหาหนึ่งข้อที่คำตอบต้องครอบคลุม |
| contract | เงื่อนไขที่ต้องรักษา เช่น เกมถูกตัว กลุ่มราคาถูก ระยะเวลาถูก ต้องไม่ตอบเกิน source |
| schema accepted | รูปแบบ/ชื่อช่องถูกกฎ ยังไม่แปลว่าความหมายถูก |
| semantic accepted | ยอมรับการตีความตาม guard ของระบบ ยังไม่เท่ากับมนุษย์รับรองคำตอบ |
| projection | เลือกว่าจะแสดง field หรือ related records ใดเพื่อให้ตรงคำถาม |
| guard / veto | ตัวตรวจที่หยุดหรือเปลี่ยนผลเมื่อไม่ผ่านเงื่อนไข |
| source / evidence | ข้อมูลต้นทางและจุดที่ตรวจย้อนยืนยันค่าได้ |
| validity | ช่วงวันที่ข้อมูลมีผล เช่น ราคาถึงก่อนวันที่กำหนด |
| protocol mismatch | ชื่อ route/intent/status/รูปแบบไม่ตรงเกณฑ์เดิม ต้องแยกจากสาระ |
| grade / request / call / audit event | หน่วยต่างกัน: เกณฑ์หนึ่งข้อ / คำขอไม่ซ้ำ / การเรียกโมเดล / เหตุการณ์ตรวจแผน |

## หลักฐานทุกกรณี ไม่ได้เลือกเฉพาะตัวอย่าง

- [ดัชนี raw-failed requests กลางทั้งหมด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/COMMON_FAILURE_INDEX_ALL.md)

- [ดัชนี raw-failed requests เดิมทั้งหมด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/LEGACY_FAILURE_INDEX_ALL.md)

- [เหตุไม่ผ่านทุกข้อความ: กลาง 620 ชนิด / เดิม 318 ชนิด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/ALL_FAILURE_REASON_TYPES.md)

- [คำตอบเต็มและ trace ของตัวอย่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/CASE_EVIDENCE.json)

- [บัญชีปัญหารุ่นตรวจทาน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/PROBLEM_CATALOG_REVIEWED.json)

- [รายการข้อมูล/ข้อขัดแย้ง/จุดภาษาอังกฤษที่ยังว่าง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/DATA_INVENTORY.json)

- [ผลตรวจทานเอกสารและข้อจำกัด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/DOCUMENT_REVIEW.md)

ดัชนีเก็บทุก request ที่ไม่ผ่านอย่างน้อยหนึ่ง raw grade: กลาง 18,824 และเดิม 5,689 รายการ เหล่านี้ไม่ใช่จำนวนคำตอบผิดสาระที่มนุษย์ยืนยันแล้ว แต่ใช้ตาม key กลับไปตรวจคำถาม คำตอบ และเกณฑ์ได้ครบ

## ระดับข้อสรุปและขอบเขต

- **ยืนยันแล้ว:** เห็นเงื่อนไขในโค้ด ค่าในฐาน หรือแผน/คำตอบใน log ตรงกัน
- **สมมติฐานรายกลุ่ม:** อาการที่จัดอัตโนมัติ ยังต้องอ่าน source/trace ก่อนตัดสินรายคำถาม
- **การป้องกันที่อาจถูกต้อง:** ข้อมูลหมดอายุ ไม่ทราบ หรือ fixture ตั้งใจปิด live
- **ความเสี่ยงที่ยังไม่ตรวจ:** package/published deployment/ขอบเขตใหม่ที่ยังไม่มีผลรองรับ

Flow 01/02 อธิบาย **ระบบที่มีอยู่จริงใน snapshot** ส่วน Flow 04 เป็น **ข้อเสนอการซ่อม** ยังไม่ได้ติดตั้งจากงานเอกสารนี้ รายงานไม่อนุมัติ draft แทนเจ้าของ และไม่สร้างนโยบายที่ไม่มีแหล่งข้อมูล

งานนี้สร้างเอกสารและดัชนีใหม่ในโฟลเดอร์ R90 เท่านั้น ไม่รันชุดทดสอบใหม่ ไม่แก้ production code/data/approval และไม่เขียนทับ log เดิม Source hashes และการตรวจเอกสารดู DELIVERY_QA.json / DOCUMENT_REVIEW.md
