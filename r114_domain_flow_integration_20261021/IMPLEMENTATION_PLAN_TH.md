# R114 — พัฒนาและตรวจครบ 5 ขั้น

คำขอเจ้าของ 21 ตุลาคม 2569: ทำทั้งห้าขั้นทีละส่วน เน้นโค้ดและผลลัพธ์ที่ตรวจสอบได้

## 1. Scope guards

แยก entity/resource/service, ปี/ช่วงมีผล และ field ก่อนค้น ห้ามเลือกเครื่องอื่นแทนเครื่องที่ไม่มี ห้ามใช้ราคาหรือกติกาคนละปี unknown, missing input และ transport failure เป็นคนละสถานะ

Gate: source-backed tests ของ wrong entity, future validity, missing field และหลาย need โดยไม่รวมคำถามหน่วยโทษ Tekken ที่เจ้าของสั่งงด

## 2. ตัวอ่านเฉพาะงาน

- C01/C02: location/contact และ public personnel fields
- C03: equipment/resource/zone และหน่วยจำนวน
- C04/C05: offerings/catalog/detail กับ exact action bindings
- C06/C07: typed rate calculator และ rental tuple/terms
- C08/C09/C10: action/condition policies แยกสถานการณ์ พร้อม source และ unknown qualifiers
- C11: date/weekday/closure/open/bookable/maintenance intervals
- C12: exact resource/time + provider/freshness contract แบบอ่านอย่างเดียว
- C13/C14: event/year/clause dependencies และ news applicability

Gate: แต่ละตัวอ่านต้องใช้ข้อมูล ไม่ใช้ mapping คำถามทดสอบ→คำตอบ; หลาย needs ต้องรักษา scope ของแต่ละส่วน

## 3. LLM protocol

ใช้ bounded evidence selection พร้อม JSON schema, item identity, per-item validation และ budget ต่อ request ใช้ผลที่ดีเป็นรายข้อ ไม่ทิ้งทั้ง batch; ไม่ให้ model เขียน facts/ราคา/สถานะเอง และไม่ให้ทับ explicit unknown/scope guards

Gate: deterministic malformed-response checks และ real model integration แยก transport/schema/selection correctness

## 4. เชื่อม Flow กลาง

Candidate copy ของ R106 ใช้ CommonStore/owner editor/dispatcher ที่มีอยู่ เชื่อม domain router และ new readers เข้าจุดตอบจริง owner draft/published isolation คงเดิม เริ่มจาก candidate preview และไม่ติดตั้งทับ R78

เพิ่ม/แก้/ถอนข้อมูลใน schema กลางต้อง compile จาก snapshot ใหม่และเปลี่ยนคำตอบโดยไม่แก้ answer code ทดสอบ lifecycle ด้วย synthetic records เท่านั้น ข้อมูล owner ที่มีหลักฐานนำเข้าได้ใน candidate draft แต่ไม่สร้าง approvals แทนเจ้าของ

Gate: actual dispatcher + HTTP owner/chat tests, data-only add/edit/withdraw และ multi-domain request

## 5. เปรียบเทียบผล

ใช้คำถาม R113 effective 1,400 ข้อเทียบ saved winner ของแต่ละหมวดโดยไม่รัน baseline ใหม่ พร้อมชุดอิสระที่ตรึงก่อนดูผล candidate สำหรับ routing, situation, entity/time, lifecycle และ model protocol

คะแนน source-contract strict, answer-state only, content coverage, wrong scope และ model transport/protocol ต้องแยกกัน C12/C14 fixtures ต้องติดป้าย ไม่อ้างเป็น semantic accuracy ทั้งระบบหรือ causal comparison กับ Legacy คนละชุดข้อมูล

หากพบ regression ให้แก้สาเหตุ เก็บผลรอบเดิมและตรึง revision ใหม่ก่อนตรวจซ้ำ ไม่แก้ oracle เพื่อทำคะแนนดีขึ้น; การแก้ข้อกำหนดที่ผิดจริงต้องมี source-backed erratum แยก

## หลักฐาน/การรักษาข้อมูล

- R113 results, original source/approvals และ frozen R106 ไม่แก้
- source และ implementation hashes พร้อม before/after audit
- ไม่มี production deployment ในงานนี้
- เก็บ test outputs, failures, model events และรายงานทุกขั้น
