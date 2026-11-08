# R88 Full test: Format กลางล่าสุด + LLM ON

ใช้สำเนาที่ตรึงจาก R78 หลังติดตั้ง R87 stage 2; ฐานข้อมูล 602 records ไม่สร้าง approval/release และไม่แก้ข้อมูลศูนย์

- Full corpus เดิม: 20,554 unique request keys และ 55,811 grades ไม่มีแขน legacy หรือ LLM OFF
- มีทั้งไทย อังกฤษ auto และ clean/noisy ตามข้อมูลเดิม ไม่เลือกเฉพาะข้อที่เคยผ่าน
- 2 evaluator workers, model admission 1 ช่อง เช่นข้อจำกัดการเรียกโมเดลในระบบ; เปิด assistance ตลอด ไม่บังคับทุกคำถามให้ใช้โมเดล
- ก่อนเริ่มต้องยืนยัน generation จริงและตรวจ pilot ว่าการเรียก selector ใช้งานได้ ไม่แทนโมเดลด้วย mock/fallback OFF
- แต่ละคำถามหลักเริ่ม history ว่าง; แยก 12 session cases และ 500 guard diagnostics ต่างหาก พร้อมส่ง trusted common_read_state สำหรับ session
- สถานะจองใช้ controlled unavailable ไม่ใช่การตรวจ WordPress occupancy สด ไม่ใช้ผลนี้ยืนยัน slot ว่าง/ถูกจองจริง
- คง reference clock เดียวกับ R70 (16 ต.ค. 2026 12:00 ไทย) เพื่อเทียบ subset ได้; reference_date เฉพาะโจทย์มีสิทธิ์เหนือกว่า ไม่แก้ effective dates ในข้อมูลราคา
- เก็บ raw answers, decision_artifact, selected source hits, model HTTP diagnostics, grades และ exceptions แบบ append-only แยกโฟลเดอร์ใหม่
- วิเคราะห์ protocol/outcome/evidence identifier/content/validation/performance/grader/model transport แยกกัน; raw fail ไม่เท่ากับเนื้อหาผิดทุกกรณี
- ทุกเกณฑ์เดิมเก็บครบ มีการตรวจ literal/source content เพิ่มโดยไม่แก้ oracle ให้คะแนนสูงขึ้น คำตอบไม่มี positive contract จะไม่อ้างว่าตอบครบ
- ตัว supervisor จะตรวจ coverage/hash แล้วสร้างรายงานอัตโนมัติเมื่อครบเท่านั้น หากหยุดจริงเก็บ partial/error ไว้ ไม่อ้างว่าเสร็จ

ขอบเขตนี้ไม่รวม unit/smoke ที่รัน profile เดิม และไม่ใช่ production/owner approval หรือ load benchmark
