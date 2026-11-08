# R123 — ตรวจความสอดคล้องของแบบออกแบบ

สถานะ: **design review เท่านั้น ไม่ใช่ผลทดสอบ implementation หรือผลยืนยัน accuracy**

## รอบที่ 1: ขอบเขตบริบทและการส่งต่องาน

ประเด็นที่ตรวจ: การเลือก “เก็บแต่ข้อความใน task” อาจทิ้ง shared context แต่การส่ง constraints ทั้งคำถามไปทุก task ทำให้ปนกัน

สิ่งที่กำหนดในแบบ:

- แยก local slots จาก shared edges และ trusted-history refs
- shared edge มี source/basis/targets/override ไม่คัดลอกทั้ง array
- entity resolution แยกจากการทำนายของโมเดลและใช้ source relations ปัจจุบัน
- งานจองขึ้นต่อการ resolve ชื่อบริการ ไม่ขึ้นต่อการตอบราคาเสร็จ
- ambiguity ของ input ไม่ถูกลบทิ้งเพียงเพราะแก้ domain ได้

สิ่งที่ยังต้องพิสูจน์ตอน implement: การตรวจ shared prefixes หลาย task, antecedents หลายชื่อ และเงื่อนไขซ้อนทำได้แม่นเพียงใด

## รอบที่ 2: ความครบของ executor ข้อมูล และข้อจำกัด source

ประเด็นที่ตรวจ: แผนถูกแต่ reader ไม่รองรับ operator, ข้อมูลหลายฉบับถูกเลือกโดยโมเดล, unknown ถูกใช้เป็น confirmed และงานหลัง starve เพราะงบ

สิ่งที่กำหนดในแบบ:

- operation vocabulary + capability registry + response contract สำหรับทั้ง C01–C14
- obligation ต่อ task/option ก่อน execute และตรวจหลัง execute
- compare/list/count/calendar มีนิยามความครบเฉพาะ operation
- source authority/validity/applicability เป็น resolver ที่มีหลักฐาน ไม่เป็นความเห็นของโมเดล
- typed reads ของงานอิสระเสร็จก่อนจัด fallback budget
- provider unavailable, missing source, budget exhausted และ unsupported แยก reason
- การเพิ่ม record ภายใต้ schema เดิมต้องอ่านได้โดยไม่ retrain

สิ่งที่ยังต้องพิสูจน์ตอน implement: source compiler diagnostics, ความครบของ capabilities จริง และการสลับ snapshot/index ที่ไม่ทำข้อมูลปน

## รอบที่ 3: Distillation การวัดผล และ version compatibility

ประเด็นที่ตรวจ: ชุดสอนมีป้ายข้าม scope, ชุดทดสอบที่ใช้แก้ซ้ำถูกเรียก holdout, score โครงสร้างถูกเล่าเป็น accuracy และ prompt ด้าน backend อาจไม่ใช่ prompt ที่ API ส่ง

สิ่งที่กำหนดในแบบ:

- review labels ทั้ง corpus พร้อม quarantine และ source-version alignment
- สอน structured plan/slot/shared roles; อ่าน business facts จาก source ตอนตอบ
- แยก train/dev/holdout ตาม family และรักษาประวัติว่าชุดใดเคยใช้พัฒนา
- สามแขนใช้ engine/data/decoding/budget/profile policies เดียวกัน
- เก็บ actual model messages/template, accepted wire versions, compiler และ adapter stage
- R121 checkpoint ไม่ถูกถือว่าเข้าใจ R123 contracts อยู่แล้ว; มี versioned compatibility และรายงาน structural failures แยก
- legacy strict, semantic answer, latency และ transport เป็นคนละตัววัด

สิ่งที่ยังต้องกำหนดก่อนทดลอง: ขนาดและ coverage ของแต่ละ split, metric adjudication, practical latency target และเกณฑ์ยอมรับ regression โดย freeze ก่อนเห็นผล

## ผลของการ review แบบออกแบบ

แบบมี Flow ข้อมูล/Runtime/Training/Evaluation และ contracts ครอบคลุมหมวดที่ระบุแล้ว แต่ยังไม่มี code/readers/planner ใหม่ที่รันตามแบบนี้ จึงไม่อ้างว่าผ่านทุกหมวดหรือทำได้ดีกว่า R122 แล้ว

เอกสารที่เป็นหลัก:

- [Flow หลัก](FLOW_MAIN_TH.md)
- [Data contracts](DATA_CONTRACTS_TH.md)
- [แผนพัฒนาและวัดผล](IMPLEMENTATION_EVALUATION_TH.md)

ลำดับถัดไปของแผนคือ P0/P1: freeze contracts/capability matrix แล้วทำ task graph และ verifiers ใน candidate แยก โดยยังไม่เริ่มฝึกโมเดลหรือทดสอบขนาดใหญ่จากการมีเอกสารเพียงอย่างเดียว
