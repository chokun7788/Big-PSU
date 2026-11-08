# ผลพัฒนาต่อ R76 — ปฏิเสธหัวข้อแล้วถามใหม่ได้ในข้อความเดียว

## สรุป

แก้ flow หลัง R75 ให้ `No, I mean how do I pay?` และ `ไม่ใช่ครับ หมายถึงจ่ายค่าจองยังไง` ไปอ่านคำตอบเรื่องจ่ายเงินทันที ไม่ทิ้งข้อความหลังคำปฏิเสธแล้วขอให้พิมพ์ใหม่อีกครั้ง

ทำในสำเนา **r76_rejection_rephrase_20261016** เปิด LLM เหมือนเดิม ข้อมูลจริง 602 heads, schema, ราคา, นโยบาย, evidence, revisions, approvals และ publication ไม่เปลี่ยน ไม่รัน legacy/OFF/full ชุดใหญ่ ไม่อัปเดตเว็บที่เปิดอยู่หรือ portable package ให้อัตโนมัติ

## 1. สาเหตุที่ผิดเดิม

### 1.1 ส่วนคำถามใหม่ถูกทิ้ง

ใน R75 `profile_confirmation.resolve` ตรวจ no/ไม่ใช่ แล้วคืน action cancel ทันที ทำให้ไม่แยก `I mean…` / `หมายถึง…` และ `CommonAnswerer` ตอบขอให้ระบุเรื่องใหม่ แม้ผู้ใช้ระบุครบแล้ว

ตรวจ baseline ด้วย 6 ข้อที่มีเนื้อหาควรตอบจาก source: วิธีจ่าย TH/EN, กำหนดจ่าย TH/EN, ที่จอดรถ EN และจำนวนรอบ TH ได้ **0/6** ส่วน initial-pending และ source-preservation checks ผ่าน จึงเห็น summary รวม 2/8 ซึ่งไม่ใช่ accuracy ของแชททั้งระบบ

### 1.2 การลบ no แบบกว้างอาจทำความหมายเปลี่ยน

`No refund is needed. How do I pay?` ไม่ใช่การปฏิเสธหัวข้อเช่นเดียวกับ `No, I mean…` และ `ไม่เอาเลขบัญชี` เป็นเงื่อนไขที่ต้องคงไว้ การตัดคำปฏิเสธออกอย่างเดียวอาจทำให้บอทบอกเลขบัญชีทั้งที่ผู้ใช้ไม่ต้องการ

### 1.3 Fallback ทำสถานะปฏิเสธหาย

เมื่อปฏิเสธหัวข้อแล้วถามเรื่องที่ยังไม่พบคำตอบ Generic fallback เดิมไม่มี common_read_state จึงอาจไม่เก็บว่าผู้ใช้ปฏิเสธอะไรและเปิดทางวนเสนอหัวข้อเดิม

รอบ rephrase01 ของ harness หยุดเมื่อพยายามอ่าน state ที่เป็น None ไม่ถือว่ารอบนั้นผ่านครบ การตรวจจุดนี้พบทั้งข้อจำกัดของ harness และช่องว่างการเก็บ state จริง จึงแก้ให้ fallback เก็บ barrier/declined IDs ต่อเมื่อยังไม่มี source context ใหม่

## 2. สิ่งที่เปลี่ยน

### 2.1 แยก acknowledgement กับ replacement query

เพิ่ม `reply_repair.py` อ่าน prefix ปฏิเสธและกรอบภาษา เช่น I mean/I meant/I'm asking about/หมายถึง/ขอถาม แล้วคืน substring ของคำถามใหม่จริง ไม่สร้างคำถามใหม่จากคำตอบเก่า ไม่ใส่ราคา/กฎหรือรหัส source ของโจทย์ไว้ใน parser

ตรวจว่าคำปฏิเสธ ตัวเลข ชื่อ วัน และเวลาภายใน replacement ยังอยู่ครบ เช่น `PC #01 on 2026-10-16 at 15:00 for 30 minutes` และ `do not show bank details; when must I pay?`

### 2.2 เข้าตัวอ่านข้อมูลตามปกติ

เมื่อมี pending ล่าสุดจาก server ที่ส่งแล้ว ให้ replacement ผ่าน dispatcher ปกติด้วย locale/LLM flag เดิม จึงอ่าน static knowledge หรือเข้า live adapter ได้ ไม่จำกัดให้วนอยู่แค่ CommonAnswerer

มี context barrier ป้องกันไม่ให้อุปกรณ์/ราคา/fields ของหัวข้อเก่ามาเติมในคำถามใหม่เอง ขอบเขตผลิตภัณฑ์ถูกตรวจซ้ำ: การเปลี่ยนเป็น write a fantasy story หรือเย็นนี้กินอะไรดีไม่เปิด general generation

### 2.3 ไม่วนเสนอหัวข้อที่เพิ่งปฏิเสธ

เก็บ IDs ของหัวข้อที่แสดงอยู่และถูกปฏิเสธไว้ใน server state กรองออกจาก semantic candidates/เมนูระหว่างยังแก้ความเข้าใจไม่สำเร็จ ไม่แก้ KB ว่าเป็นข้อมูลถอนแล้ว และไม่ถือว่าเจ้าของยกเลิกนโยบาย

เมื่อคำถามใหม่ได้คำตอบจาก source แล้ว context ของหัวข้อใหม่ใช้ถามต่อได้ เช่น เปลี่ยนไปเรื่องจ่ายเงิน → `And when?` ตอบกำหนดจ่ายจากข้อมูลปัจจุบัน

ถ้าผู้ใช้ถาม task/subject ของหัวข้อเดิมใหม่อย่างชัดเจนแบบ direct ระบบยังอ่าน source นั้นได้ การปฏิเสธตัวเลือกไม่ใช่การ blacklist เนื้อหานั้นตลอดไป

### 2.4 เก็บเหตุผลให้ตรวจย้อนหลังได้

เพิ่ม artifact `dialogue_repair` ระบุ original_input, active_query, rejected_profile_ids, previous_answer_facts_used=false และ old_context_inherited=false เก็บ trace ภายในที่เลือก source ไว้

ปรับ query debug ให้ active_query เป็นคำถามที่ใช้ค้นจริงหลัง repair ขณะที่ original_question/resolved_question ของ request ยังเก็บข้อความต้นทางไว้ การปรับนี้เป็นข้อมูล debug ไม่ใส่รายละเอียดระบบลงในคำตอบลูกค้าปกติ

## 3. ผลทดสอบ

ทุกชุดใช้ format กลาง เปิด LLM ไม่รวมคะแนนทุกแถวเป็น accuracy เดียว

| ชุด | ผ่าน/ทั้งหมด | สิ่งที่ตรวจ |
|---|---:|---|
| baseline01 บนโค้ด R75 | 2/8 | 6 content replacements ล้มเหลว; 2 auxiliary checks ผ่าน |
| parser01 | **32/32** | แยก raw substring/คำปฏิเสธ/ตัวเลขและ boundary ของ acknowledgement |
| rephrase02 | **34/34** | 15 paired content questions และ checks เรื่อง context/source/state/adapter/handler |
| regression01 | **43/43** | source contracts ชุดหลักเดิม |
| scope01 | **50/50** | source, unconfirmed policies และ negative scopes เดิม |
| debug01 | **3/3** | debug extraction จากผล dispatcher ที่เก็บแล้ว ไม่มี request ใหม่ |

6 content replacements ของ baseline อยู่ในชุด rephrase02 และผ่าน 6/6 แล้ว ชุดใหม่มีทั้งหมด 15 paired content questions ซึ่งผ่าน 15/15 ที่เหลือของ 34 checks เป็นการตรวจพฤติกรรม/fixture ไม่ใช่คำถามคนใช้ใหม่อีก 19 ข้อ

### กลุ่มคำถามใหม่ที่ทดสอบ

- วิธีชำระ TH/EN ต้องมีเลขบัญชีและการแนบสลิปจาก source
- กำหนดจ่าย TH/EN ต้องมี 10 นาที/ผลยกเลิก และไม่ใส่เลขบัญชีเมื่อไม่ได้ขอ
- จำนวนรอบต่อการจอง TH/EN ต้องได้ข้อกำหนด 3 รอบจาก source ไม่สับสนเป็นจำนวนรอบต่อวัน
- เกม PC/PS5 ต้อง list ตามหมวดและไม่ปนเกมอีกหมวด
- กฎอุปกรณ์ส่วนตัว TH/EN ต้องอ่านคำตอบห้ามจาก source เดิม ไม่รับปากอนุญาตใหม่
- โอนเกิน/ขาดยังตอบ unconfirmed ตรงเรื่อง ไม่ให้ผู้ใช้โอนเพิ่มหรือสัญญาคืนเงินเอง
- เงื่อนไข “ไม่เอาเลขบัญชี” / “do not show bank details” คงอยู่หลังแยก replacement

### สิ่งที่ checks เพิ่มเติมยืนยัน

- คำถามสั้น `And when?` หลัง replacement ใช้บริบทใหม่
- คำถามใหม่ที่ยังไม่ชัดและ yes ถัดไปไม่รื้อหัวข้อสลิปที่เพิ่งถูกปฏิเสธ
- Plain cancel และการถาม unknown ซ้ำยังเก็บ declined-topic barrier
- `No, I mean` ที่ไม่มีรายละเอียดไม่ถูกแต่งเป็นคำถามใหม่
- ไม่เอาข้อความ assistant เก่าที่ใส่เลขบัญชีปลอมมาทับ source จริง
- เปลี่ยนไปเรื่องนอก scope ไม่สร้างคำตอบนอกข้อมูลศูนย์
- Live fixture รับ active query พร้อม PC1 และ 15:00 ตามเดิม พิสูจน์การส่งต่อ ไม่ใช่สถานะ WordPress จริง
- เพิ่ม FAQ ใหม่ใน SQLite fixture แล้ว replacement อ่านได้ แก้เป็น V2 แล้วอ่าน V2 ถอนแล้วไม่คืนคำตอบเก่า
- HTTP handler แบบ connection ใน memory ใช้ server history เพื่อทำ repair ใน request เดียวและเก็บบริบทใหม่ถามต่อได้ Client-only history ไม่เปิดใช้ repair metadata

## 4. สิ่งที่ผลนี้ยังไม่ได้รับรอง

1. **โมเดลจริง:** ชุด rephrase ใช้ controlled transport-unavailable fixture เพื่อตรวจ flow ไม่ใช่ผล inference ส่วน regression รอบนี้ยังมี actual attempt ที่ WinError 10013, successes=0 บันทึกใน MODEL_HEALTH.json ไม่สรุปจาก LLM flag ว่าโมเดลทำงานสำเร็จ
2. **TCP/browser/WordPress:** HTTP handler และ live fixture ไม่ใช่การรับรองการเชื่อมต่อสด การตรวจสถานะจริงที่ผู้ใช้ยืนยันไว้ก่อนหน้ายังเป็นข้อสรุปเดิม ไม่เปิดให้เจ้าของยืนยันซ้ำจากรอบนี้
3. **ขอบเขต repair:** รองรับเมื่อมี pending ของ profile ล่าสุดที่ server ส่งแล้ว ไม่ได้แก้ทุก `No, I mean…` ในทุกส่วนของระบบ เช่น generic name ambiguity หรือ price selector ที่มี state คนละประเภท
4. **ประโยคอื่น:** `that's not what I meant`, คำยืนยันมีเงื่อนไข `yes but…`, fragment ที่ต้องสืบทอดข้อมูลบางส่วน และ typo ในคำตอบสั้นยังต้องพัฒนาต่อ ไม่บังคับ yes-but ให้เป็น yes
5. **ความหมายของข้อมูล:** source subject definitions, model recall/top-k, conditions/exceptions และความขัดแย้งข้อมูลยังเป็นงานต่อ ไม่อ้างว่าการแยก prefix แก้ semantic correctness ของทุกหมวด
6. **นโยบายเจ้าของ:** โอนเกิน/ขาด ผ่อน ระยะตรวจชำระ อายุ/ผู้ปกครองยังคง unknown/unconfirmed ตามหลักฐานเดิม ไม่มี owner fact ใหม่ในรอบนี้
7. **ความเร็ว/หลายคน/ส่ง production:** ไม่วัดความเร็วจาก mock และไม่อัปเดต portable/release draft นี้แทนชุดใช้งานจริง

## 5. รักษาต้นทางและข้อมูล

ตรวจ manifest R75 **1,424 ไฟล์ เปลี่ยน 0 ไฟล์**; heads **602**; logical tables ของ R75/R76 เหมือนกันทั้งหมด; approvals **0** และ active/publication metadata เดิมไม่เปลี่ยน

DB SHA256 ต้นทาง/สำเนาเท่ากัน: `4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d`

ข้อมูลตัวอย่าง การแก้ V1→V2 และ withdrawal อยู่เฉพาะ `verification/*/system/data/knowledge/common.sqlite` แยกจาก DB แชท R76 ไม่ทับ result/log เก่า รอบ rephrase01 ที่หยุดก่อนจบยังเก็บไว้

## 6. ไฟล์ส่งต่อ

- `FLOW_R76_TH.md`: flow และทบทวนสามรอบ
- `README_R76_TH.md`: วิธีเปิดสำเนานี้และตัวอย่างสนทนา
- `NEXT_STEPS_R76_TH.md`: งานที่ยังต้องทำเรียงลำดับ
- `DELIVERY_QA_REVIEWED.json`, `CHANGESET_REVIEWED.patch`: source/data audit และ diff หลังปรับ debug
- `verification/parser01`, `verification/baseline01`, `verification/rephrase01`, `verification/rephrase02`, `verification/debug01`: หลักฐานแยกแต่ละรอบ
