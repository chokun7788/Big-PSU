# R95 — สิ่งที่เติมหลังทบทวน R94 และการลงมือจริง

สถานะเอกสารระหว่างพัฒนา: ต้องอ่านผลรุ่นสุดท้าย/manifest ประกอบ ไม่ใช่การรับรองว่า full test เสร็จ

## สิ่งที่แบบ R94 ยังไม่ระบุพอ และเติมแล้ว

1. **Executor seam:** ตัวอ่าน common เดิมผูก local variables กับตัวตีความทั้งฟังก์ชัน ต้องแยก `execute_task` รับ accepted plan + snapshot + explicit execution context ไม่เพียงเพิ่ม TaskPlan แล้วกลับไปเลือก field ใหม่ ขณะนี้เส้นทางใหม่และ compatibility ใช้ตัวอ่านที่แยกร่วมกัน
2. **Raw span lineage:** การ normalize ต้องมี offsets/edits/protected spans และเก็บ raw input ใน dispatcher ไม่ใช่ลบคำเกริ่นแล้วไม่รู้ว่าลบอะไร `normalized_query.py` ใช้ร่วมทั้ง dispatcher และ common reader
3. **Task readiness กับ runtime capability:** แยก runtime task catalog ออกจาก data-readiness registry เดิม มี task kinds/operations/fields ที่ต้องใช้จริง แต่การมี catalog ไม่ใช่หลักฐานว่าทุก task/ทุกสำนวนผ่าน
4. **Task-plan acceptance:** เพิ่ม proposer ที่เลือก task/candidate พร้อม quote bindings ไม่สร้าง facts และไม่ส่ง fields อิสระให้โมเดลเลือกทั้งหมด การตีความที่มี negation/age/version/เงิน/เงื่อนไขหรือแผนที่ยืนยันไม่ครบไม่ยกระดับด้วย JSON ผ่านอย่างเดียว
5. **Withdrawn references:** ต้องตรวจ candidate IDs ก่อนอ่าน kind เพราะ names/context อาจยังอ้างรายการถอนแล้ว การทดสอบ owner lifecycle พบ KeyError จริงและเพิ่ม guard ให้คืนทางจัดการ withdrawn โดยไม่คืน facts เก่า
6. **Slot errors แยก validity:** เพิ่ม grammar นักศึกษามหาวิทยาลัยอื่น → general-student concept ที่มีใน labels ไม่เปลี่ยนวันหมดอายุ ไม่อนุมานบุคคลภายนอกทุกคนว่าเป็น General Adult
7. **Model/runtime gate ก่อน full:** ตรวจจริงทั้ง deterministic path และ LLM ON พร้อม model response/error logs ไม่เริ่ม full ด้วยรุ่นที่มี execution exception หรือการเพิ่ม model work ซ้ำที่ยังไม่ตรวจ
8. **Evaluator scope:** คะแนน keyword ที่ผ่านไม่ใช่ semantic correctness; ตัวอย่าง owner/operator ใน source ยืนยันระดับมหาวิทยาลัย ขณะที่ GT บางไฟล์คาดระดับ College of Computing ต้องเก็บ mismatch ไว้ ไม่แก้ business fact หรือ GT เพื่อคะแนน

## สิ่งที่ใช้จากกลางเดิมอย่างตั้งใจ

- store/schema/evidence/pointers, revision/approval/publish lifecycle
- billing/rental/current-rate/qualifier checks และ competition clause/dependency logic
- controls/relations/projection/localization และ compact date opening
- qualified confirmation/pending slots และ precise unconfirmed policy outcomes

Price/rules/บาง qualifier paths ยังใช้ parser เฉพาะหมวด common ผ่าน compatibility adapter ตาม R94 rollout plan และรายงาน path ตามจริง ไม่เรียกว่าเปลี่ยนทุกหมวดเป็น generic semantic planner แล้ว ความสามารถเหล่านี้ต้องเก็บไว้ระหว่างยืนยัน replacement ไม่ปลด guard เพื่อให้คะแนนสูง

## บันทึกข้อผิดพลาดจากการพัฒนา

- focused01: executor ยังอ้าง `method` จาก local scope เดิม → เพิ่ม explicit context/plan source; ผลรอบแรกเก็บไว้
- focused02/03: operator assertion คาด College of Computing แต่ current `center.operator` เป็น Prince of Songkla University → ปรับเฉพาะ focused test ให้ตรวจ field/evidence ที่ต้นฉบับมี; GT เดิมไม่ได้แก้
- owner01: withdrawn name/context เข้า interpreter แล้วอ่าน record ที่ไม่อยู่ → เพิ่ม reference guard; owner02 ผ่าน 13 checks
- Stage gate 240 requests เป็นการตรวจรุ่นระหว่างพัฒนา แยกจาก full test; ผลและ timeout ทั้งหมดคงไว้ ห้ามนำผลบางส่วนมาเรียกว่า full complete

## ขอบเขตที่จะรันใหญ่

เฉพาะ common Flow ใหม่ + LLM ON ตามการเลือกใช้งานของระบบ ไม่บังคับทุกคำถามให้ generate ด้วยโมเดล ใช้ request population เดิม 20,554 keys / 55,811 grades ไทย/อังกฤษ/auto และเวลาอ้างอิงเดียวกับผลเก็บเดิม พร้อม controlled live-unavailable เดิมเพื่อเทียบได้

การทดสอบนี้ไม่รับรองสถานะจองจริงวันนี้หรือทุก multi-turn conversation ต้องรายงาน owner/multi-turn fixtures และการตรวจ API/transport แยกต่างหาก ไม่มีการรัน legacy ซ้ำ ไม่มีการแก้ production facts/approvals
