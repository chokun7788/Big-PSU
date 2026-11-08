# ผลพัฒนาต่อจาก R72 — R73

## สรุป

ลงมือแก้การเลือกคำตอบที่มี source ชัดอยู่แล้ว เพิ่ม optional query_profile สำหรับ FAQ/policy/procedure และปรับคำตอบที่ยังยืนยันนโยบายไม่ได้ให้ตรงเรื่อง ทดสอบเฉพาะ format กลาง เปิด LLM ทุกชุด ไม่รัน full/legacy/OFF

**ผลชุดหลัก 50 ข้อ: R72 7/50 → R73 50/50** แต่ 50 ข้อนี้ประกอบด้วยคำตอบจาก source, การแจ้งว่ายังยืนยันไม่ได้ และคู่ลบด้าน scope จึงไม่ใช่ accuracy ของทุกคำถามหรือทุกข้อมูลใหม่

ชุดถ้อยคำใหม่อีก 8 ข้อได้ 6/8 ก่อนปรับ และ 7/8 หลังปรับ ยังเหลือ 1 คำถามที่ใช้ proof of payment แทน slip การแก้ในรอบนี้ทำให้ procedure ที่ถูกเข้าชุด candidate แล้ว แต่ยังยืนยัน end-to-end ไม่ได้เพราะ socket เรียกโมเดลถูกปฏิเสธและ field planner ยังต้องตรวจแผนจริง การเพิ่ม candidate ไม่ถูกนับเป็นคำตอบที่ถูก

[Flow ที่ใช้และปรับจากผลจริง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/FLOW_R73_TH.md) · [วิธีเปิดและตัวอย่างกรอก](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/README_R73_TH.md) · [ข้อมูลผลและ failures](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/ANALYSIS_R73.json)

## 1. สิ่งที่เปลี่ยน

### 1.1 เลือกจาก metadata แทนการเพิ่มรหัสรายการใน router

- เพิ่ม query_profile แบบ optional ใน FAQ/policy/procedure: task, subjects ไทย/อังกฤษ, ownership และ context
- รองรับสอง task: ถามสิทธิ์ใช้/นำมา และถามวิธีแก้สิ่งที่ผิด ไม่ได้อ้างว่าครอบคลุมทุกคำถามทุกหมวด
- selector ใช้ task + subject + ownership + context ไม่อ่าน policy value จากโค้ด ถ้ามี profile ตรงกันหลายชิ้นจะถามเพิ่ม
- metadata ไม่แสดงในคำตอบ “ทั้งหมด” และไม่ให้ field planner เลือกเป็นเนื้อหาคำตอบ
- บันทึก metadata ให้เพียง 2 copied records ที่ตรวจชื่อ/คำตอบ/steps แล้ว: personal keyboard/mouse และ wrong slip ข้อเท็จจริงทุก field เดิมเท่ากันกับ R72 ไม่มี owner approval ใหม่

### 1.2 ให้คำตอบตาม source ที่มี

- “Can I bring my own keyboard?” / “เอาเมาส์ส่วนตัวมาใช้ได้ไหม” อ่านคำตอบห้ามนำอุปกรณ์ส่วนตัวมาใช้จาก FAQ เจ้าของเดิม
- “I uploaded the wrong slip…” / “ส่งสลิปผิดไปแล้ว…” อ่านขั้นตอนและเพจจาก procedure เดิม
- ภายในคำถามผสม เช่น วิธีจ่าย + keyboard / สลิปผิด / ผ่อนจ่าย แยกอ่านและแสดงสถานะแต่ละส่วน
- preconditions ที่เป็นรหัส issue แสดงชื่อสถานการณ์จาก source ให้คนอ่าน โดยยังคงหลักฐาน/เงื่อนไขเดิมใน trace

### 1.3 ตอบตรงเรื่องเมื่อยังยืนยันไม่ได้

- โอนเกิน/โอนขาด/ยอดผิด/ผ่อน/ระยะเงินถึง/อายุผู้ใช้ แจ้งข้อจำกัดเฉพาะเรื่อง พร้อมเพจศูนย์จาก contact record จริง
- ถ้าระบุเพียงยอดผิด ถามว่าเกินหรือขาด และไม่รับปากคืนเงิน/แก้รายการ/ให้โอนเพิ่มเอง
- สถานะ unconfirmed ไม่ใช่ no_data ทั้งฐาน และไม่ใช่การอนุญาต/ห้าม เป็นสิ่งที่ข้อมูลซึ่งอ่านได้ยังยืนยันไม่ได้
- การตรวจรูปแบบคำถามไม่ได้เติมคำตอบของเจ้าของลงไป คำถามให้เจ้าของตัดสินใจแยกไว้ท้ายรายงาน

### 1.4 ฟอร์มเจ้าของ

- เพิ่มชื่อช่อง ตัวเลือก และตัวอย่างเป็นภาษาคน กรอกเรื่องไทย/อังกฤษทีละแถว ไม่ต้องเขียนคำถามทุกประโยค
- ข้อมูลเก่าที่ไม่มี field ใหม่ยัง validate ได้ และเมื่อเปิดใน editor ให้ unknown envelope ที่ถูก schema
- ทดสอบ widget จริงด้วย DOM adapter ได้ 3/3 เป็นการตรวจค่าที่กรอก/ข้อความช่วย ไม่ใช่ visual/browser certification

## 2. ผลทดสอบแยกรอบ

| ชุด | ผ่าน/ทั้งหมด | ไทย | อังกฤษ |
|---|---:|---:|---:|
| scope_baseline01 | 7/50 | 3/24 | 4/26 |
| scope01 | 46/50 | 21/24 | 25/26 |
| scope02 | 49/50 | 24/24 | 25/26 |
| scope03 | 50/50 | 24/24 | 26/26 |
| scope_final | 50/50 | 24/24 | 26/26 |
| ownership02 | 6/6 | 2/2 | 4/4 |
| regression01 | 43/43 | 19/19 | 24/24 |
| unseen01 | 6/8 | 2/2 | 4/6 |
| unseen02 | 7/8 | 2/2 | 5/6 |

- Actual HTTP handler + pipeline แบบ connection ใน memory: **52/52** รวมบริบทสองรอบ ราคา เกม กฎ source ใหม่ที่ผูก profile และ live fixture
- เพิ่ม subject/ID ใหม่ แก้ revision ถอนข้อมูล conflict และ schema ใน SQLite fixture แยก: **20/20**
- Candidate recall + ไม่ตอบเองเมื่อ noun ไม่ตรง: **2/2**
- Owner editor widget: **3/3**; syntax JavaScript/PowerShell ผ่าน

ไม่รวมผลทั้งหมดเป็น accuracy เดียว เพราะมีทั้งคำถาม ข้อกำหนดเนื้อหา fixture assertions และการตรวจ protocol ทดสอบ API แบบ memory ไม่ใช่ TCP/browser จริงหรือ WordPress สด

### องค์ประกอบชุด 50 ข้อ

| กลุ่ม | ผ่าน/ทั้งหมด | ประเภทเกณฑ์ |
|---|---:|---|
| personal_permission | 10/10 | source_content |
| wrong_slip | 8/8 | source_content |
| wrong_amount | 2/2 | unconfirmed_topic |
| overpayment | 4/4 | unconfirmed_topic |
| underpayment | 2/2 | unconfirmed_topic |
| installments | 4/4 | unconfirmed_topic |
| processing | 4/4 | unconfirmed_topic |
| age | 4/4 | unconfirmed_topic |
| compound | 4/4 | source_content |
| negative_scope | 7/7 | safety_scope |
| unknown_extra_object | 1/1 | safety_scope |

เกณฑ์ source_content ตรวจเนื้อหาและ source record จริง ไม่ใช้เพียงห้ามตอบข้อความเดิม เกณฑ์ unconfirmed ตรวจว่าระบุเรื่องที่ยังยืนยันไม่ได้ถูก พร้อมไม่รับปาก policy ส่วน safety_scope กันการเลือกข้อมูลผิดเรื่อง แต่ไม่ได้รับรองคำตอบเต็มของเรื่องอื่น

## 3. สิ่งที่ผิดระหว่างทำ และสาเหตุ

| จุดผิด | สาเหตุใน flow | สิ่งที่ปรับ |
|---|---|---|
| ส่งสลิปผิดไปแล้วต้องทำอย่างไร | semantic_clauses แยก “แล้ว” แล้วคิดว่าส่วนท้ายเป็นสิ่งของอีกชิ้น | ตรวจ coordinated objects เฉพาะ และ/and แยก temporal connective |
| โอนเงินกี่วันถึงบัญชี | alias โอนเงินเลือก FAQ ธนาคาร แม้ duration ไม่อยู่ใน source | เก็บ rejected scope plan และตอบ unconfirmed เฉพาะ processing แทน candidate ผิด รวมในคำถามผสม |
| วิธีจ่าย + ผ่อน/สลิปผิด | exception ทั้งประโยคปิด role วิธีจ่ายก่อน composition | แยก independently requested tasks ก่อน filter ของแต่ละส่วน |
| minimum age and guardian | ถูกแยกเป็นสอง unknown ซ้ำกัน แล้ว mode partial ผิด need เดียว | รวมเมื่อทั้งสองส่วนเป็น unconfirmed topic เดียว |
| my booking กับ studio keyboard | personal เคยจับ my จากบริบทอื่น | ผูก my กับ subject และกัน studio-owned noun |
| ซื้อ/ทำความสะอาด keyboard | can I อย่างเดียวไม่พิสูจน์ว่าเป็นสิทธิ์นำมาใช้ | permission task ใช้ action ที่ตรง use/bring/allowed ไม่ใช้ can I ทั่วไป |
| แก้ข้อมูลเก่าหลังเพิ่ม optional field | editor สร้าง unknown note ว่าง ซึ่งไม่ผ่าน schema | default unknown envelope มี note ที่ถูกต้อง |
| payment was too low | classifier รู้ underpaid/โอนขาด แต่ไม่รู้การเปรียบเทียบยอด | เพิ่ม semantic comparator low/high ภายใต้ payment/amount anchor; ยังคง unknown policy |
| proof of payment | noun ไม่ตรง slip และ record ถูกตัดออกจาก candidates | เพิ่ม declared task เป็น recall backstop อย่างเดียว ห้ามตอบอัตโนมัติเมื่อ subject ไม่ตรง |

ความล้มเหลวของตัว fixture runner ครั้งแรกเกิดจากการเรียก get() บน ID ที่ยังไม่มี ซึ่งยก ValueError แก้เฉพาะ harness และเก็บโฟลเดอร์ profiles01 เดิมไว้ ไม่ใช่ production routing defect และไม่ใช้ผลที่รันไม่จบเป็นผลผ่าน

## 4. คำถามที่ยังไม่ผ่านจริง

### I attached the incorrect proof of payment. How do I fix it?

- ควรตอบ: วิธีแก้แนบหลักฐานชำระผิดตาม procedure_wrong_slip และเพจศูนย์
- คำตอบจริง: The model could not select the relevant data in time; please retry.
- Stage ที่พบ: direct query_profile ไม่มี subject ตรง; recall backstop เพิ่ม procedure ถูกเข้าชุด candidate แล้ว; model selector เรียกไม่ได้ (transport ไม่สำเร็จ)
- ก่อนแก้ recall มีเพียง group check-in / CS2 ซึ่งไม่ใช่ข้อมูลที่ต้องการ จึงไม่ใช่ปัญหาโมเดลอย่างเดียว
- ยังต้องตรวจ semantic selection และ field planner เมื่อโมเดลเรียกได้จริง ไม่เพิ่ม alias ของประโยคทดสอบเพื่อทำให้คะแนนดูผ่าน

## 5. Source/data preservation

ตรวจไฟล์เนื้อหาต้นทาง R72 1420 ไฟล์ เปลี่ยน 0 ไฟล์; heads เดิม/ใหม่ 602/602; factual fields เปลี่ยน 0 รายการ; immutable revision payload เดิมเปลี่ยน 0 รายการ

R73 มี metadata field เพิ่มใน 2 ระเบียนและมี 2 revisions ใหม่ตาม audit จึงมี database hash ใหม่ตามคาด ไม่ได้อ้างว่า DB byte hash เท่า R72 แต่ค่าข้อเท็จจริง หลักฐานเดิม ราคา นโยบาย และ validity เท่าเดิมทั้งหมด

- R72 database SHA256: `c3a3684a31bb4ddbb7c2107a1c4201f2e54c4ebf17c5c5c9a9f608e72dac7ab8`
- R73 database SHA256: `6948a91aa13d6f6688c4f8002d61068320bbb76e8fa8da5b38d935b0251957f3`
- Approvals เดิม/ใหม่: 0/0; active release เดิม/ใหม่: ว่าง/ว่าง

[Audit metadata ก่อน/หลัง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/PROFILE_MIGRATION_AUDIT.json) · [QA และ manifest](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/DELIVERY_QA.json) · [Diff โค้ด/ฟอร์ม/schema](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/CHANGESET.patch)

## 6. สิ่งที่ยังไม่ได้ยืนยัน

1. Real model inference/schema/semantic selection: เปิด LLM และมี actual attempts แต่ยัง WinError 10013 หลังขอสิทธิ์ผ่านระบบ ไม่มี success จากการสร้างคำตอบของโมเดลในรอบนี้
2. Generic paraphrase ที่เปลี่ยน concept noun/เงื่อนไขซับซ้อน ยังต้องทำ planner/metadata ต่อ พร้อมโมเดลจริง ไม่ถือว่า profile สอง task แก้ครบทุกหมวด
3. นโยบายโอนเกิน/ขาด ผ่อน ระยะเงินถึง และอายุ ยังต้องเจ้าของตัดสินใจ ไม่มี policy ใหม่ที่ agent ตัดสินแทน
4. ข้อมูลร่าง คำแปลเดิมที่ยังไม่ผ่านเจ้าของ และ source ambiguity อื่นยังมีสถานะเดิม
5. Browser/TCP/WordPress สดและ production publication gate ยังไม่ได้รับรองจากรอบนี้; live เป็น fixture ที่รู้ผลเท่านั้น
6. query_profile ช่วยความแม่นเมื่อ metadata/เนื้อหากรอกตรง ไม่สามารถรับรองข้อมูลที่กรอกขัดกันหรือย้าย scope ผิดได้โดยอัตโนมัติทุกสถานการณ์

[คำถามเฉพาะที่ให้เจ้าของตอบ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/OWNER_QUESTIONS_R73_TH.md)

## 7. วิธีลองและ rollback

เปิด Open-New-Chat.cmd ของ R73 → พอร์ต8105 ป้ายR73 ใช้ runtime จาก R69 ข้างกัน เปิด editor ที่8106 เก็บ log/state และ DB ใน R73 ของตัวเอง
กลับชุดก่อนหน้าโดยปิด R73 ด้วย Stop-New-Chat.cmd ของ R73 แล้วเปิด launcher R72 เดิม ข้อมูลของแต่ละสำเนาแยกกัน หากแก้ข้อมูลผ่าน editor ต้องเลือกสำเนาให้ถูก

นี่เป็น working copy สำหรับลองบนเครื่องนี้ ยังไม่ได้แทนแพ็กเกจ production/portable เดิมโดยอัตโนมัติ
