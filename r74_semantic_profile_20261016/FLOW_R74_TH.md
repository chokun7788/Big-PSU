# Flow R74 — เชื่อมความหมายคำถามกับข้อมูลกลาง โดยรักษาขอบเขตคำตอบ

## เป้าหมายและข้อจำกัด

ต่อจาก R73 ซึ่งคำถาม “I attached the incorrect proof of payment. How do I fix it?” ยังไม่ตอบขั้นตอนแก้แนบสลิปผิด ทั้งที่ procedure มีอยู่จริง เป้าหมายคือแก้เส้นทางเลือกหัวข้อและส่วนคำตอบร่วมกัน ไม่เพิ่ม alias ประโยคนี้ลงใน router และไม่เขียนคำตอบจากความจำของโมเดล

ทำในสำเนา R74 แยกจาก R73 และโปรเจกต์ต้นฉบับ ข้อมูลจริงทุก field, evidence, validity, revisions, approval และ active release ต้องคงเดิม ไม่ย้ายข้อมูลตัวอย่างเข้า DB ที่แชทใช้จริง ไม่ทดสอบ legacy/OFF/full ชุดใหญ่

## ขั้นตอนทำงาน

### 1. เก็บฐานก่อนแก้

- สำเนา system และใช้ SQLite backup API เพื่อได้ snapshot ที่สอดคล้องกัน ไม่คัดลอก WAL/SHM เก่าทับฐานใหม่
- เก็บ manifest ของไฟล์ R73 และผล baseline ของคำถามเดิมไว้ใน results ของ R74
- เปรียบเทียบ logical tables/records ด้วย ไม่ใช้ byte hash เท่ากันเป็นเงื่อนไขเดียว เพราะ SQLite backup อาจจัดหน้าไฟล์ใหม่

### 2. จำแนกความผิดพลาดตาม stage

| Stage | สิ่งที่ต้องตรวจ | สิ่งที่ห้ามสรุปข้าม |
|---|---|---|
| Direct selection | task/subject/ownership/context ตรงหรือไม่ | literal ไม่ตรงไม่ได้แปลว่าไม่มีข้อมูล |
| Candidate retrieval | source ที่ถูกอยู่ในรายการหรือไม่ | มี candidate ไม่ได้แปลว่าเลือกถูก |
| Model transport | เรียกได้และรับ response จริงหรือไม่ | เปิด LLM ไม่ได้แปลว่ามี inference สำเร็จ |
| Output contract | schema, indices, quotes และ coverage ถูกหรือไม่ | JSON ถูกไม่รับรองความหมายถูก |
| Semantic selection | subject และ task ที่โมเดลตีความตรงเรื่องหรือไม่ | คำเกี่ยวข้องกันไม่จำเป็นต้องใช้ policy เดียวกัน |
| Field projection | เลือก steps/conditions หรือ field ที่ตอบ task จริง | record ถูกแต่ field ผิดยังตอบผิดได้ |
| Source rendering | อ่าน revision ปัจจุบันพร้อมหลักฐาน/เงื่อนไข | ห้ามใช้ factual text จาก model response |

### 3. ใช้ direct profile เดิมก่อน

ถ้า task + literal subject + ownership/context ตรงแบบ unique ให้ใช้เส้นทาง R73 เดิม ไม่เพิ่มการเรียกโมเดลให้ทุกคำถาม ถ้า profile ชนกันหรือมี coordinated object ที่ไม่ได้ครอบคลุม ให้ถามเพิ่มตามเดิม

### 4. ส่ง candidate และ metadata ให้ bounded selector

- ยังคงจำกัดจำนวน candidate ไม่เกิน 8 และส่งเฉพาะข้อความ source ที่คัดไว้
- ส่ง query_profile แบบมีโครงสร้างและ clause IDs เพิ่มโดยไม่ตัด metadata นี้ออกตาม excerpt ของเนื้อหา
- โมเดลคืน indices กับ profile binding เท่านั้น ไม่คืนราคา นโยบาย ขั้นตอน คำตอบ SQL หรือ field names ที่ตัดสินเอง
- คำสั่งเลือกใช้กับทุก profile ที่มี ไม่อ้างอิงรหัส wrong_slip ใน production code
- การยกเลิก lexical overlap guard ใช้ได้เฉพาะ selected profile ที่ผ่าน binding contract ไม่ยกเลิกให้รายการทั่วไป

### 5. ตรวจ profile binding แบบ atomic

ต้องมีครบทุก selected profile: candidate index, task, task_span จาก input จริง, subject_index, subject span จาก input จริง, relation, ownership, context และ coverage ของทุก clause

ปฏิเสธเมื่อ:

- index/subject index ไม่อยู่ในชุด, boolean แอบแทน integer, binding ซ้ำหรือหาย, มี key คำตอบ/field แทรก
- task ไม่ตรง metadata หรือ span ไม่แสดง task ที่ตรวจได้
- quote ถูกสร้างขึ้นเองหรือหยิบจาก source แทน input
- relation เป็น different/uncertain, context ไม่ตรง, ownership ไม่ตรง
- มี clause หาย/ไม่ครอบคลุม หรือเลือกหลาย records แบบ profile ปะปนโดยไม่แจ้ง ambiguity

**ขอบเขตการรับรอง:** quoted input ตรวจได้ว่ามาจากคำถามจริง แต่ยังพิสูจน์ไม่ได้ว่า subject equivalent ตามที่โมเดลอ้างจริง จึงเก็บ independent_semantic_verification=false เสมอ ต้องทดสอบ contrast set กับโมเดลจริงก่อนรับรองความแม่นของ paraphrase

### 6. ใช้ผลเลือก task เพื่อกำหนดส่วนคำตอบครั้งเดียว

เมื่อเลือก profile ได้หนึ่งรายการและผ่าน contract ให้ใช้ method semantic_question_profile แล้วอ่าน DEFAULT_FIELDS ของ kind นั้น เช่น procedure → steps, preconditions, required_documents ตามสถานะข้อมูล ไม่ส่งคำถามเดิมไปให้ field planner ตีความซ้ำอีกครั้ง

การข้าม field planner ไม่ข้าม source validity, withdrawal, authority, field/evidence validation, epoch หรือ renderer คำตอบยังต้องผูกกับ record/revision ที่อ่านจริง

### 7. แยกความพร้อมของโมเดลออกจากข้อมูลที่ไม่มี

- transport failure → แจ้งว่าเชื่อมต่อส่วนตีความไม่ได้ ไม่อ้างว่าฐานไม่มีคำตอบและไม่เรียกรวมว่า timeout
- schema rejection → แจ้งว่ายังตีความได้ไม่แน่ชัด
- busy/deadline/health gate → retry พร้อมเก็บสาเหตุใน trace
- semantic mismatch → ไม่ให้ source นั้นตอบแทนเรื่องอื่น
- unknown owner policy ที่ระบุ topic ได้ → คงคำตอบ unconfirmed เฉพาะเรื่องตามข้อมูลเดิม

### 8. ตรวจ regression และซ่อมจุดที่มีหลักฐาน

พบจาก regression ว่า “โอนเงินเข้าบัญชีไหน” ถูก topic transfer_processing จับเพราะมี “เข้าบัญชี” เพียงอย่างเดียว แก้ให้ถาม arrival time/delay จึงเข้าหัวข้อนี้ ส่วน bank/account destination ต้องใช้ payment_method เดิม ไม่สร้างข้อมูลบัญชีใหม่

ตรวจทั้ง destination, arrival, deadline, wrong amount และ wrong attachment แยกกัน ถ้าเจอ test oracle อ้าง record ID ผิด ให้แก้ harness และแยกจาก code defect ไม่เอาคะแนนรอบนั้นไปอ้างว่าเป็น content failure ทั้งหมด

### 9. ทดสอบเฉพาะที่เกี่ยวข้องและแยกหลักฐาน

1. Source contracts ไทย/อังกฤษผ่าน dispatcher ปกติ เปิด LLM เหมือนระบบใช้งาน
2. Controlled model responses ผ่าน serializer, selector validator และ dispatcher จริง เพื่อพิสูจน์ wiring และการไม่เรียก field planner ซ้ำ ต้องติดป้ายว่าไม่ใช่ model accuracy
3. Contrast output tests ที่โมเดลรายงาน different/uncertain และ malicious/invalid structure ต้องถูกปฏิเสธ
4. เปลี่ยน revision/ถอน source ใน SQLite fixture แยก ต้องอ่านฉบับใหม่และไม่คืนข้อมูลถอนแล้ว
5. ผลเรียกโมเดลจริงแยกออกมา หากติดสิทธิ์ ห้ามนับ fixture เป็นการผ่านแทน

### 10. เกณฑ์หยุดและส่งต่อ

- ซ่อมจุดที่ยืนยันได้และชุดที่เกี่ยวข้องไม่ถอยหลัง
- เก็บแต่ละรอบ ไม่ทับ log เดิม
- รายงานปัญหาที่ยังอยู่: real semantic inference, retrieval เมื่อ profiles มากกว่าขอบเขต candidate, โจทย์นอกสอง task, ความขัดแย้งใน source และ policy เจ้าของที่ยังไม่ทราบ
- ไม่ประกาศ production-ready จากชุด targeted หรือ controlled fixtures; publication/draft และ package มีสถานะเดิม

## ทบทวน Flow สามรอบ

### รอบ 1: ความหมายและที่มาของคำตอบ

การเพิ่ม candidate อย่างเดียวไม่แก้การเลือก field; เพิ่ม binding และ projection ร่วมกัน คำตอบไม่มาจาก model-generated text และไม่เพิ่ม alias ของโจทย์ที่ล้มเหลว

### รอบ 2: ขอบเขตและคำถามใกล้เคียง

เพิ่มเงื่อนไข quotes/ownership/context/all-clause coverage และแยก destination กับ arrival การตรวจคำอ้างไม่ใช่ independent semantic judge จึงต้องแยก fixture correctness ออกจาก model correctness และต้องยังมีคู่ลบจริงสำหรับทดสอบโมเดลภายหลัง

### รอบ 3: การส่งใช้งานและรักษาหลักฐาน

ตรวจ logical DB ไม่ใช้ file hash อย่างเดียว แยก test oracle defect จาก routing defect, เก็บ baseline/ทุก round และไม่เปลี่ยน approvals/active release การเปิดแชท R74 สำหรับพัฒนายังไม่ใช่การเปลี่ยน production โดยอัตโนมัติ
