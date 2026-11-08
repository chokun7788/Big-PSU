# ผลพัฒนาต่อ R75 — เลือกหัวข้อให้ตรงก่อนตอบ source

## สรุปสิ่งที่ทำแล้ว

พัฒนาในสำเนา `r75_profile_confirmation_20261016` แยกจาก R74 และชุดเดิม เปิด LLM ตามเดิม ไม่มี data migration หรือ owner approval ใหม่

1. ปิดทางที่ unverified semantic profile กลายเป็นคำตอบนโยบาย/ขั้นตอนทันที ให้ผู้ใช้เลือกหัวข้อจาก source ก่อน
2. เมื่อโมเดลไม่พร้อม ยังเสนอหัวข้อที่มีใน task/context นั้นได้ ผู้ใช้ตอบสั้นแล้วอ่าน source จริงต่อได้
3. จำ pending ใน server history และรับ yes/no/ชื่อ subject/ชื่อหัวข้อ/เลขข้อ ไม่อ่านข้อความคำตอบก่อนหน้ามาเป็น facts
4. มี pagination ครั้งละ 6 ไม่ทำให้หัวข้อหลัง top-4/8 หายจากทางเลือกของผู้ใช้ พร้อม audit ว่าโมเดลเห็นและไม่เห็นรายการใด
5. ตรวจข้อมูลถูกถอน ขอบเขตเปลี่ยน เปลี่ยนเรื่อง ยกเลิก และ client-forged state
6. แยก English correct ที่หมายถึง “ถูกต้อง” ออกจาก “แก้ไข” ไม่ให้ correct file format เรียกขั้นตอนแก้แนบสลิปผิดโดย direct profile

## 1. ทำไมต้องเปลี่ยนจาก R74

R74 ควบคุม indices/task/subject spans/ownership/context/coverage ได้ แต่ถ้าโมเดลอ้างผิดว่า proof of identity equivalent กับ payment slip และยกข้อความจาก input จริง รูปแบบก็ยังผ่านได้ นี่คือ semantic error ไม่ใช่ JSON/schema error

R75 ยังคงบันทึก binding เพื่อวิเคราะห์ แต่ไม่ให้ความเห็นของโมเดลเพียงอย่างเดียวออกเป็นคำตอบจาก profile ตัวนั้น เมื่อต้องพึ่ง semantic-only จะถามว่า “หมายถึงหัวข้อนี้ใช่ไหม” ก่อน เมื่อผู้ใช้เลือกแล้วจึงอ่านคำตอบจากฐานปัจจุบัน

นี่เป็นการป้องกันการยืนยันผิดเรื่องด้วยการถามเพิ่ม ไม่ได้แก้ให้โมเดลรู้ synonym ทุกคำ ไม่ได้เปลี่ยน policy และไม่ได้รับรองว่า source ถูกเจ้าของอนุมัติแล้ว

### ตัวอย่างเส้นทางจริงในรอบนี้

ผู้ใช้: `I attached the incorrect proof of payment. How do I fix it?`

บอท: `Do you mean this topic: Correct an incorrect payment-slip image? Reply “yes” or “no”.`

ผู้ใช้: `yes`

บอท: อ่าน steps ของ `procedure_wrong_slip` และตอบวิธีส่งสลิปไปเพจศูนย์จาก source พร้อม citation

สองรอบนี้ผ่าน normal dispatcher ขณะที่การเรียกโมเดลครั้งแรกยังถูกบล็อก จึงพิสูจน์ว่ามีทางไปถึงข้อมูลที่ถูกหลังผู้ใช้เลือกหัวข้อ แต่ไม่ใช่หลักฐานว่าโมเดลตีความ proof of payment ได้ถูกเอง

## 2. ผลตรวจในรอบนี้

| ชุด | ผล | สิ่งที่ตรวจ |
|---|---:|---|
| regression01 | **43/43** | คำถามหลักจาก source ตามชุด R74 |
| scope01 | **50/50** | คำตอบ source, unconfirmed policy และ negative scopes |
| confirmation01 | **28/28** | การถามยืนยัน/ตอบสั้น, wrong semantic proposal, revision/withdraw, 13 profiles และ HTTP handler แบบ memory |
| language01 | **12/12** | แยก adjective/verb และ literal profile rejection |
| language02 | **16/16** | 12 คู่ภาษาเดิม + 4 คำปฏิเสธที่มีรายละเอียดต่อท้าย |

ไม่รวมคะแนนเป็น accuracy เดียว: บางข้อเป็น state/schema/negative checks และ language02 ซ้ำ 12 ข้อเดิม ไม่ใช่เพิ่มเป็น 28 language questions ไม่รัน legacy/OFF/full ชุดใหญ่

### 28 checks มีอะไรบ้าง

- Real probe: แชทถามหัวข้อเพิ่มเมื่อโมเดลใช้งานไม่ได้ และคำว่า yes อ่าน source ที่ถูกผ่าน dispatcher ได้
- Controlled model output: จงใจอ้างผิดว่า proof of identity equivalent กับสลิป ห้ามปล่อย steps/decision เป็นคำตอบเต็ม; no ยกเลิกและ yes ทีหลังไม่รื้อหัวข้อเดิม
- ไทย/อังกฤษ: yes, slip, ใช่ครับ, สลิป เชื่อม source ได้; ข้อความแรกเป็น clarification ไม่มี factual-answer hits
- Fresh session ไม่รับ pending จากอีก session; เปลี่ยนไปถาม Parking อ่าน Building 5 ไม่สืบทอดสลิป
- history ที่ยังไม่ส่งถึงผู้ใช้หรือมาจาก client-only ไม่ยืนยันหัวข้อ
- เปลี่ยน steps ใน fixture แล้ว yes อ่านฉบับใหม่; เปลี่ยน query_profile หรือถอน record แล้ว yes เก่าใช้ไม่ได้
- เพิ่ม procedure ตัวอย่าง 13 หัวข้อใน SQLite fixture แยก: ดูครบสามหน้า เลือกข้อ 13 แล้วตอบ STEP_12 ที่มีหลักฐานจริงใน fixture; เลขจากหน้าที่ซ่อนหรือ yes กับหลายตัวเลือกไม่เลือกแทน
- HTTP handler จริงผ่าน connection ใน memory เก็บ common_read_state ใน server history และไม่รับ client-forged state มายืนยันหัวข้อ
- DB ที่แชท R75 ใช้จริงไม่เปลี่ยนจากการทดสอบ fixture

### ขอบเขตของผลภาษา

ก่อนแก้ `What is the correct file format for a slip?` ได้ task correction เช่นเดียวกับ `How do I correct the slip?` เพราะ regex จับคำว่า correct ทุกตำแหน่ง แก้ให้แยก grammar ของ verb และ adjective แล้วตรวจ 12 ประโยค ผลนี้พิสูจน์ task classification/literal-profile rejection ไม่ได้พิสูจน์คำตอบเรื่องชนิดไฟล์ ซึ่ง source อาจไม่มี

คำตอบปฏิเสธที่มีรายละเอียดต่อท้าย เช่น `No, I mean proof of identity.` ปิดหัวข้อเก่าได้ แต่ยังไม่ได้ตอบรายละเอียดใหม่นั้นอัตโนมัติ การต่อคำถามใหม่ในเทิร์นเดียวเป็นงานที่ยังต้องทำ

## 3. สิ่งที่ยังไม่ได้ผ่าน

### โมเดลจริง

ขอ network permission ผ่านระบบแล้วไม่ได้รับสิทธิ์เพิ่ม Real probe ยังได้ WinError 10013, model successes=0 เก็บใน `verification/confirmation01/REAL_MODEL_PROBE.json` ไม่ใช้ controlled outputs แทนผลโมเดลจริง

ข้อจำกัดนี้เกิดจากการเรียกผ่านเครื่องมือทดสอบในสภาพแวดล้อมนี้ ไม่พิสูจน์ว่าเว็บซึ่งผู้ใช้เปิดอยู่หรือ Ollama ของเครื่องใช้งานจริงล้มทั้งหมด

### ความแม่นแบบตอบทันทีหนึ่งรอบ

R75 แลกความเร็วในการคุยหนึ่งรอบเพิ่มกับการไม่ assert จาก semantic-only profile ที่ยังไม่ยืนยัน จึงไม่อ้างว่าชุด unseen ของ R74 จาก 7/8 กลายเป็น 8/8 แบบถามครั้งเดียว ให้ประเมิน flow สองรอบแยกกัน หากต้องการตอบ paraphrase ทันที ต้องวัดโมเดลจริง/contrast set และพัฒนา subject definitions/constraints ต่อ

### การค้นหา

โมเดลยังเห็น candidate สูงสุด 8 และ backstop 4 แม้การจัดอันดับ deterministic ขึ้นและผู้ใช้เปิดดู compatible profiles ทั้งหมดได้ การทดสอบ 13 profiles เป็นหลักฐานความครบของทางเลือกผ่านเมนู ไม่ใช่ semantic recall หรือ ranking ของโมเดล และไม่ใช่ load test ข้อมูลหลายพันรายการ

### ขอบเขต feature

query_profile ยังมีเพียง permission/correction และมี profile ที่ผูกจริงอยู่ 2 records ดังเดิม รายการอื่นใช้ตัวอ่านตามหมวดเดิม ไม่ได้ถูกอ้างว่าตอบทุกหมวดด้วยกลไกใหม่นี้แล้ว

## 4. ข้อมูลและไฟล์เดิม

- ตรวจต้นทาง R74 1,423 ไฟล์ ไม่เปลี่ยนเนื้อหาเดิม
- DB heads 602 รายการ; logical tables ของ R74/R75 เหมือนกันทั้งหมด รวม source, revision, metadata, audit และ approval
- DB SHA256 ทั้งสองสำเนา: `4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d`
- approvals=0; publication/active เดิมไม่เปลี่ยน
- ตัวอย่าง 13 profiles และการแก้/ถอนรายการอยู่ใน `verification/confirmation01/system` เท่านั้น ไม่ปนใน DB แชทจริง

## 5. ไฟล์ที่ควรอ่านต่อ

- `FLOW_R75_TH.md`: flow และทบทวนสามรอบ
- `REMAINING_WORK_R75_TH.md`: งานที่ยังต้องทำเรียงความสำคัญ พร้อมสิ่งที่ agent ทำเองได้/สิ่งที่ต้องมีข้อมูลหรือสิทธิ์เพิ่ม
- `DELIVERY_QA_FINAL.json` และ `CHANGESET_FINAL.patch`: audit/diff ฉบับหลังปรับสุดท้าย
- `verification/confirmation01/RESULTS.json`: ผลและคำตอบทุก check
- `verification/language02/RESULTS.json`: grammar/negative-reply checks
- `README_R75_TH.md`: วิธีเปิดสำเนาพัฒนานี้

ยังไม่แทนชุด production/portable เดิมและไม่เปลี่ยนเว็บที่กำลังเปิดอยู่ให้อัตโนมัติ
