# R100 — ลงมือจาก R99/R97 ของ Astra

สถานะเริ่มต้น: implementation candidate แยกจาก R98 และระบบติดตั้งจริง

## ลำดับและเกณฑ์ตรวจรับ

1. Freeze R98 source แล้วคัดลอก runtime; เก็บ baseline manifest และข้อมูลทดสอบคนละฐาน
2. Canonical task IDs/predicates และ status mapping ร่วม;ทุก final business response ต้องมี RequestPlan/NeedResults แม้ fallback หรือ rejection
3. PendingSlotBinder ที่คืน origin ราย slot จาก binding จริง;ไม่ใช้ความสั้นของคำถามเป็นเหตุผลสืบทอดบริบท
4. Discovery ambiguity ของหลาย edition และ unknown mentions;คำตอบสั้นต่อจาก targeted question ต้องคง task
5. Claim coverage ตรวจ predicate/subject/required fields ของ path ที่มี contract;legacy adapters ที่ยังพิสูจน์ไม่ได้ต้องระบุ scope unverified
6. Policy action scope และ error provenance;รักษาข้อเท็จจริงส่วนที่ตอบได้และไม่อนุมาน permission/negative facts
7. ใช้ deadline/admission ledger เดิม;ทดสอบ nested calls ไม่เริ่มงบใหม่
8. Focused customer/source/lifecycle tests ทั้ง LLM ON และ OFF;เก็บ first result, failures, fixes และรายงานขอบเขตที่ยังไม่ทำ

## สิ่งที่ไม่ถือเป็นความสำเร็จเพียงลำพัง

- JSON valid / field receipt มี source / 24 kinds readiness ไม่เท่ากับ semantic correctness
- source ขาดจริงไม่แก้ด้วยการสร้าง fact หรือขยายวันมีผล
- ไม่แก้ expected answer เก่าให้สอดคล้องกับโค้ดใหม่เพื่อผ่านคะแนน
- focused test ไม่ใช่ full-corpus หรือ production concurrency benchmark

แผนรายละเอียดอ้างอิง `../r99_flow_review_20261019/RECOMMENDED_FLOW_TH.md` ผลจริงและข้อที่ทำได้บางส่วนจะลงในรายงานเมื่อทดสอบเสร็จ
