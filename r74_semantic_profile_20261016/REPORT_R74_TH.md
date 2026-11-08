# ผลพัฒนาต่อ R74 — การเลือกหัวข้อ ความหมาย และส่วนคำตอบ

## สถานะสรุป

ลงมือทำในสำเนา **r74_semantic_profile_20261016** ต่อจาก R73 เพิ่มเส้นทาง semantic profile ที่เชื่อมการเลือกรายการกับส่วนคำตอบ แก้การสับสนระหว่างบัญชีรับเงินกับระยะเงินเข้า และแยกข้อความระบบเมื่อเรียกโมเดลไม่ได้ออกจากกรณีตีความคำถามไม่ได้

**ยังไม่ถือว่าเคส proof of payment ผ่านโมเดลจริง** แม้เส้นทางใหม่อ่าน source ได้ถูกต้องเมื่อได้รับแผนเลือกที่ถูกต้องแล้ว การเรียกโมเดลจริงยังติด WinError 10013 หลังขอสิทธิ์ผ่านระบบ และยังต้องตรวจว่าโมเดลแยกคำถามใกล้เคียงได้จริง

## 1. ปัญหาที่วิเคราะห์และสิ่งที่แก้

### 1.1 มีข้อมูล แต่คำเรียก subject ไม่ตรง

คำถาม: `I attached the incorrect proof of payment. How do I fix it?`

ข้อมูลที่ควรอ่านคือ `procedure_wrong_slip` ซึ่งมีขั้นตอนส่งสลิปที่ถูกต้องไปยังเพจศูนย์ตาม source เดิม ปัญหานี้ไม่ได้เกิดจากขั้นตอนนี้ยังไม่ถูกย้ายเข้า format กลาง

R73 ใช้ literal subject `slip` ใน direct profile จึงไม่ match `proof of payment` และแม้ recall backstop เพิ่มรายการนี้เข้า candidate แล้ว ระบบยังต้องเรียก semantic selector อยู่ คะแนน candidate เป็น lexical retrieval score ไม่ใช่ความน่าจะเป็นว่าคำตอบถูก; score 0 ของ backstop ไม่ได้แปลว่าข้อมูลผิด

**แก้ใน R74:** ส่ง profile ที่ประกาศ task/subject/ownership/context ให้ selector พร้อม candidate บังคับคืน binding ระหว่างข้อความผู้ใช้กับ subject ที่เลือก ไม่เพิ่มรหัส procedure หรือ alias ประโยคนี้ใน production router

### 1.2 เลือก record ถูก แต่ยังมี field planner ตีความซ้ำ

R73 มีการใช้ default answer fields สำหรับ direct declared profile และ FAQ ที่เลือกแบบ semantic แต่ยังไม่มีเส้นทางที่ชัดเท่ากันสำหรับ procedure/policy ซึ่งเลือกจากความหมาย จึงเสี่ยงให้ field planner ปฏิเสธคำถาม paraphrase เดิมอีกครั้งว่า intent ยังไม่ยืนยัน

**แก้:** เมื่อ semantic profile ผ่าน contract และเลือกเพียงรายการเดียว ให้ `semantic_question_profile` กำหนดส่วนคำตอบจากชนิดข้อมูล เช่น procedure อ่าน steps/preconditions/required_documents โดยไม่เรียก field planner ซ้ำ ยังคงตรวจ validity, source, authority, evidence และ revision ตามเดิม

โมเดลไม่มีสิทธิ์ส่ง steps/ราคา/decision/ข้อความคำตอบเข้ามา ข้อเท็จจริงอ่านจาก DB ปัจจุบันเท่านั้น ทั้งภาษาไทยและอังกฤษใช้กลไกเดียวกัน

### 1.3 “เข้าบัญชีไหน” ถูกมองเป็น “เงินเข้าบัญชีเมื่อไหร่”

คำถามจริงที่พบใน regression: `โอนเงินเข้าบัญชีไหน`

คำตอบผิดเดิม: ยังยืนยันระยะเวลาที่เงินโอนเข้าถึงบัญชีไม่ได้ แล้วให้ติดต่อเพจ แทนการบอกวิธีชำระ/เลขบัญชีที่มีอยู่แล้ว

สาเหตุมีสองส่วน:

1. `unconfirmed_request.topic` จับคำว่า “โอน…เข้าบัญชี” โดยไม่ต้องมีคำถามด้านเวลา แล้ว `exceptional_payment` ใช้ผลนี้ปิด payment_method
2. ตัวตรวจคำถามวิธีจ่ายรู้ “โอนเงิน”/“บัญชีไหน” แต่ยังพลาด “โอนเข้าธนาคารไหน” และ “บัญชีอะไร”

**แก้:** ระบุ transfer_processing ภาษาไทยเมื่อมีทั้งเหตุการณ์เงินเข้า/ถึงบัญชีและคำด้านเวลา/ความล่าช้า แยก head “บัญชี/ธนาคาร/ช่องทาง” กับคำถาม “ไหน/อะไร” เมื่อมีบริบทชำระหรือโอน ส่วน policy ระยะเงินถึงยังคง unconfirmed ตามเดิม ไม่เดาระยะเวลาใหม่

ตัวอย่างที่แยกได้หลังแก้:

| คำถาม | ประเภทคำตอบที่ควรได้ |
|---|---|
| โอนเงินเข้าบัญชีไหน / โอนเงินเข้าบัญชีอะไร | วิธีชำระ บัญชี และสลิปจาก source |
| ต้องโอนเข้าธนาคารไหน | วิธีชำระจาก FAQ ที่มี intent bank_account |
| โอนแล้วเงินจะเข้าบัญชีเมื่อไหร่ | ยังยืนยัน transfer processing time ไม่ได้ |
| หลังจองต้องจ่ายภายในกี่นาที | กำหนดจ่ายจาก source เดิม ไม่ใช่ processing time |

### 1.4 ข้อความ retry เดิมบอกว่า “ไม่ทัน” แม้จริง ๆ เชื่อมต่อไม่ได้

เดิม error, model busy และการตีความไม่สำเร็จอาจถูกนำเสนอเป็น “could not select … in time” เหมือนกัน และ health cooldown อาจหลุดไปเป็นการตีความว่าไม่มีข้อมูล

**แก้:** เก็บ `availability_failure` เป็น transport/schema/busy/deadline/model_gate ให้ข้อความผู้ใช้ตรงกลุ่มปัญหา ขณะเดียวกัน trace เก็บสาเหตุไว้ เช่น transport ถูกบล็อก ไม่แสดงรายละเอียดเทคนิค WinError ให้ลูกค้าร้านเกมอ่าน และไม่กล่าวว่าฐานไม่มีคำตอบเพราะส่วนตีความใช้งานไม่ได้

### 1.5 ตัวทดสอบระบุ source แคบเกินไป

รอบ boundary แรกมี false failures จาก oracle สองแบบ:

- ระบุ deadline ID เป็น `migrated_faq_rule_payment_timeout` แต่ source จริงคือ `migrated_faq_rule_payment_10_minutes`
- บังคับให้บัญชีต้องตอบจาก `migrated_faq_rule_payment_bank` เพียงรายการเดียว ทั้งที่ `migrated_faq_rule_en_payment_method_natural` มีข้อมูลไทย/อังกฤษและ intent bank_account เดียวกัน จึงตอบถูกเนื้อหาและมี evidence แต่ถูก grader ตัดว่าผิด source

**แก้เฉพาะ harness:** ยอมรับหนึ่งในสอง source ที่ตรวจเนื้อหาแล้ว และใช้ deadline ID ที่มีจริง ข้อกำหนดเลขบัญชี/สลิป/ห้ามตอบ processing ผิดเรื่องยังเดิม เก็บผลดิบทุกชุด แล้วตรวจคะแนนใหม่จากคำตอบเดิมใน `ORACLE_REVIEW.json` ไม่รันคำถามซ้ำเพื่อแก้คะแนนและไม่เขียนทับผลเดิม

## 2. ผลทดสอบ — แยกตามสิ่งที่ตรวจได้

ทุกชุดใช้ format กลาง เปิด LLM ไม่รัน legacy, OFF หรือ full ชุดใหญ่

| ชุด | ผล | ขอบเขตหลักฐาน |
|---|---:|---|
| R73 baseline payment boundary หลังตรวจ oracle | 11/14 | คำตอบจาก dispatcher ปกติ ไทย 6/9 อังกฤษ 5/5 |
| R74 boundary02 หลังตรวจ oracle เดียวกัน | **14/14** | ไทย 9/9 อังกฤษ 5/5; source/unknown topic ถูกตาม contracts |
| R74 regression01 → regression02 | 42/43 → **43/43** | ซ่อมคำถามบัญชีที่หลุดไป processing; source content contracts |
| R74 scope01 | **50/50** | คำถามจาก source, unknown policy และ negative scopes ตามชุด R73 |
| R73 baseline unseen01 | 7/8 | ผลจากการเรียกจริงในสภาพเครื่องมือปัจจุบัน |
| R74 unseen01 | **7/8** | ยังเหลือ proof of payment; transport ไม่สำเร็จ |
| Controlled semantic fixtures semantic01 → semantic02 | 28/28 → **32/32** | ทดสอบ wiring/contract/source projection ด้วย model outputs ที่กำหนดไว้ ไม่ใช่ model accuracy |

**ห้ามรวมตัวเลขทุกแถวเป็น accuracy เดียว** มีคำถามซ้ำข้ามชุด มีทั้ง content, abstention, contract, transport behavior และข้อมูล fixture

### สิ่งที่ 32 controlled checks พิสูจน์ได้

- ถูกต้องตามแผนที่ป้อน: English proof of payment, bank transfer image และไทยหลักฐานชำระเงิน อ่าน source ขั้นตอนที่มี Facebook และ evidence โดยไม่เรียก field planner ซ้ำ
- โครงสร้างผิด, index ผิด/boolean, quote ไม่มีจริง, subject different/uncertain, task/context ผิด, coverage หาย และการส่งคำตอบ/field เพิ่ม ต้องถูกปฏิเสธ
- ถ้าไม่ครอบคลุมทั้งคำถาม ห้ามปล่อยขั้นตอนจาก source นั้นเป็นคำตอบเต็ม
- transport failure, schema failure และ health gate แยก trace/ข้อความ retry ได้
- เปลี่ยน steps ใน SQLite fixture แล้วอ่าน revision ใหม่ทันที ประวัติเดิมยังอยู่ ถอน record แล้วไม่อยู่ใน candidate universe
- fixture ไม่แก้ DB ที่แชท R74 ใช้จริง

### สิ่งที่ 32 checks ไม่ได้พิสูจน์

ไม่ได้ให้โมเดลสร้างแผนเองในชุดนี้ จึงไม่ได้พิสูจน์ว่าโมเดลจะตัดสิน equivalence ได้ถูก และไม่ได้พิสูจน์ throughput/latency ของการสร้าง JSON แบบใหม่ UI/browser/TCP หรือ WordPress สด

## 3. ความเสี่ยงที่ยังยืนยันว่ามี

### P0 — binding ถูกโครงสร้างยังไม่ใช่ semantic correctness

ตรวจกรณีควบคุมเพิ่มเติม: ถ้าป้อนแผนที่อ้างผิดว่า `proof of identity` equivalent กับ subject ของสลิป แต่ใช้ quote จาก input จริงและกรอก task/context/coverage ครบ contract validator ยังรับได้

บันทึกไว้ใน `verification/semantic02/SEMANTIC_LIMITATION.json` แยกจาก 32 checks ไม่ซ่อนเป็นเคสผ่าน และไม่ได้อ้างว่าโมเดลจริงเคยส่งแผนผิดนี้

นี่คือขอบเขตสำคัญ: quote validation ป้องกันการแต่งข้อความอ้าง แต่ไม่ใช่ independent semantic judge โค้ดยังคง `independent_semantic_verification=false` และ `human_intent_correctness_verified=false` ต้องรัน positive/contrast questions กับโมเดลจริง ก่อนรับรองเส้นทางนี้เพื่อส่ง production หากโมเดลสับสนจริง จึงพิจารณาเพิ่ม typed subject constraints/definition ใน format กลางและปรับจาก log ที่พบ ไม่เพิ่ม alias ไปเรื่อย ๆ

### P0 — ยังเรียกโมเดลจริงไม่ได้จากเครื่องมือนี้

ขอ network permission ผ่านระบบแล้วไม่ได้รับสิทธิ์เพิ่ม ผลจริงยังมี `<urlopen error [WinError 10013] ... access permissions>` จึงไม่อ้างว่า proof of payment ผ่าน end-to-end ด้วยโมเดลจริง ไม่เปลี่ยน firewall หรือไปเรียกผ่านช่องทางอื่นเพื่อข้ามข้อจำกัด

คำตอบ source ที่ระบบควรส่งยังเป็นขั้นตอนแก้แนบสลิปผิดและเพจเดิม การปรับในรอบนี้ซ่อมเส้นทางอ่าน source หลังเลือก task ถูก แต่ยังไม่รับรองความแม่นของตัวเลือกโมเดล

### P1 — recall backstop และจำนวน profile

การค้นยังใช้ candidate สูงสุด 8 และ task backstop สูงสุด 4 จาก R73 เมื่อเจ้าของเพิ่มหลาย profiles หรือใช้ subject ที่ไม่ทับกันเลย ยังมีโอกาสที่ source ถูกตัดออกก่อนโมเดลเห็น รอบนี้ไม่ทดสอบการขยายจำนวน profiles และไม่ได้แก้ข้อจำกัดนี้

### P1 — task และขอบเขตข้อมูลยังไม่ครบทุกสถานการณ์

query_profile รองรับ permission/correction เท่านั้น ไม่ได้ทำให้หมวดเกม ราคา กติกา ปฏิทิน หรือทุกเงื่อนไขใหม่ใช้ตัวตีความนี้ได้ทันที บทสนทนาหลายขั้น ข้อปฏิเสธซับซ้อน เงื่อนไขใหม่ และคำถามผสมยังต้องตรวจจากกรณีจริงเพิ่มเติม

### ต้องข้อมูลเจ้าของ — policy ที่ยังไม่มีข้อสรุป

โอนเกิน/ขาด, ผ่อนชำระ, ระยะเงินถึง, อายุ/ผู้ปกครองยังมีสถานะตาม R73 ไม่สร้างคำตอบแทนเจ้าของ รายละเอียดคำถามเดิมอยู่ใน `r73_scope_completion_20261016/OWNER_QUESTIONS_R73_TH.md` รอบนี้ไม่มี owner fact หรือ approval ใหม่

## 4. รักษาข้อมูลเดิม

- ตรวจ manifest ต้นทาง R73 **1,422 ไฟล์ เปลี่ยน 0 ไฟล์**
- DB heads **602 รายการ**; schema validation ผ่านทั้งหมด
- ทุก logical table ของ DB R73/R74 เหมือนกัน รวม facts, query_profile เดิม, sources, revisions, audit, approval และ publication metadata
- approvals **0**; actual active release **ว่าง** ตามเดิม ไม่ใช่ production publication
- R73 SHA256: `6948a91aa13d6f6688c4f8002d61068320bbb76e8fa8da5b38d935b0251957f3`
- R74 SHA256: `4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d`
- byte hash ต่างเพราะ SQLite backup จัดเก็บไฟล์ใหม่ แต่การตรวจข้อมูลทุกตารางตรงกัน ไม่อ้างว่าเกิด data migration หรือเนื้อหาถูกแก้

## 5. ไฟล์และการใช้งาน

- `FLOW_R74_TH.md`: ขั้นตอนและทบทวน 3 รอบ
- `CHANGESET.patch`: diff เฉพาะ system เทียบ R73
- `DELIVERY_QA.json`: preservation/schema/table audit
- `results/*/ANSWERS.jsonl`: คำตอบและ trace จริง; `ORACLE_REVIEW.json` ตรวจเกณฑ์โดยไม่ยิงคำถามใหม่
- `verification/semantic02`: controlled outputs, ผล checks และ semantic limitation
- `README_R74_TH.md`: วิธีเปิดสำเนาพัฒนานี้

R74 ยังเป็นสำเนาสำหรับพัฒนา ไม่แทนชุด production/portable เดิมและไม่เปลี่ยนเว็บที่เปิดอยู่ให้อัตโนมัติ Runtime ใช้ R69 ข้างกัน ทดสอบเปิด socket/browser จริงจากเครื่องมือนี้ยังไม่ได้
