# ทบทวนแผนสามรอบและข้อจำกัดก่อนเริ่มพัฒนา

วันที่ 18 ตุลาคม 2026 — เป็น document/code-evidence review ไม่ใช่การรันทดสอบแชทบอท

## รอบ 1: ตรวจเหตุที่ข้อมูลครบแต่ตอบไม่ได้

| จุดที่ทบทวน | ข้อบกพร่องของแนวคิดเริ่มต้น | สิ่งที่ปรับใน Flow |
|---|---|---|
| Early return | คิดว่ามี legacy helpers ใน repo แล้วระบบจะเรียกเอง | ทำ explicit interpreter adapters ก่อน field selection |
| Entity | พบชื่อ exact ถูกใช้เสมือนเข้าใจทั้งคำถาม | แยก entity result กับ task result |
| LLM JSON | ตรวจ schema ผ่านแล้วอาจยังเลือก field ผิด | TaskPlan/Need ledger และ task-compatible field profiles |
| Guard | ปิด guard แก้ over-rejection แต่เพิ่ม wrong-answer risk | แยก guard ชั้น task/qualifier/evidence และ acceptance ของ paraphrase |
| Data migration | นับ records แล้วสรุปความครบ | ตรวจ field/relations/conditions/authority ตาม task |
| Comparison | คิดว่าเดิมชนะทุกหมวด | รักษา competition/control และ validity ที่กลางมีข้อดี |

## รอบ 2: ตรวจความผิดใหม่ที่แผนอาจสร้าง

| Counterexample | ความเสี่ยง | การปรับ |
|---|---|---|
| how to pay / how to play | fuzzy ใกล้แต่เป็นคนละงาน | valid-word/slot protection, ambiguity, task binding |
| ไม่เอา VR / เอา VR | recovery ลบคำปฏิเสธ | protected polarity + excluded IDs |
| PC11 / PC1 | ลบตัวซ้ำผิดหมายเลขเครื่อง | numeric target invariant |
| ทั้งหมด หลังเลือกบริการราคา | ตีความ all fields ทั้งฐาน | scope quantifier ผูก pending need |
| ตอบราคา+ที่อยู่ แต่ราคา expired | เลือกตอบไม่ได้ทั้งก้อนหรือเดาราคา | per-need outcome + dependency graph |
| เกมรองรับ PS5 | ตอบว่าศูนย์มีติดตั้งทุกเครื่อง | แยก platform/offered/installed/live |
| เกมใหม่ไม่มีวิธีเล่น | บังคับทุก field จนตอบแนวเกมไม่ได้ | required_for_task แยก primary/optional |
| FAQ ใกล้เคียงแต่คนละเงื่อนไข | wrong policy แม้มี source | typed subject/action/context/qualifiers |
| all rules ยาวเกิน UI | ตัดข้อมูลแล้วบอกครบ | cardinality, source-order และแบ่งส่วนที่ระบุครบ/ค้าง |

## รอบ 3: ตรวจ owner workflow และการส่งมอบ

| จุด | ช่องว่าง | สิ่งที่เพิ่มในแผน |
|---|---|---|
| Preview vs chat | ใช้คนละ entrypoint | dispatcher contract เดียว ต่างที่ SnapshotProvider |
| Draft vs published | เห็นคำตอบแล้วคิดว่าเผยแพร่แล้ว | publication mode และ revision/hash approval ชัด |
| Price update | history/cache ใช้ค่าราคาเดิม | cache key/version invalidation และ reread evidence |
| Withdraw | pending state คืนรายการที่ถอน | revalidate IDs/authority ต่อคำขอ |
| Relations | form เติมชื่อแต่ไม่มี mapping | dropdown refs + readiness ต่อ task |
| Translation | ไทยแก้แล้วอังกฤษยังยืนยัน review เดิม | translation lineage และ stale status |
| Future date | ฟอร์มอาจสัญญาสลับข้อมูลอัตโนมัติเกิน code | ตรวจ store/scheduler capability ก่อนทำ UI promise |
| Portable | แก้ R78 แล้วคิดว่าแพ็กเกจตามทัน | build/config/dependency manifest ในขั้นส่งมอบ |
| Metrics | full score ปน protocol/transport/content | แยกตารางและรักษาเกณฑ์เก่าทั้งหมด |

## ประเด็นที่ยังต้องตัดสินทางเทคนิคระหว่าง implementation

1. Semantic acceptance ของ LLM paraphrase ที่ไม่เข้า shared grammar: schema/span check อย่างเดียวไม่พิสูจน์ความหมายทั้งหมด ต้องกำหนด task-specific checks และ calibration โดยยังรักษาการ abstain
2. Conflict resolution ของ source ที่มี authority เท่ากัน: ถ้า mapping/เอกสารอธิบายไม่ได้ให้คง conflict ไม่ใช้ timestamp ชนะทุกกรณี
3. Scheduled publication ของราคาใหม่: ตรวจว่าทำด้วย store ปัจจุบันได้อย่างไร ก่อนเลือก scheduler หรือ temporal lookup ที่เพิ่มใหม่
4. Long-answer all coverage: เลือก UI split/pagination ที่รับรองจำนวนและ scope ต่อเนื่อง ไม่ทำให้ผู้ใช้เข้าใจว่า chunk แรกคือทั้งหมด
5. Task registry versioning และแผนจาก state รุ่นเก่า: ต้องมีการ invalidate/upgrade ที่ระบุได้
6. Owner translation review กับ technical validation: เป็นคนละสิทธิ์และหลักฐาน ไม่ยกให้คะแนนเทสแทนการอนุมัติ
7. Generic FAQ/topic retrieval ที่ไม่มี entity: ต้องเพิ่ม recall โดยยังรักษา policy qualifiers และ studio scope

## ข้อที่ไม่ควรใช้เป็นเหตุหยุดงานพัฒนา

- ข้อมูลราคาปัจจุบันยังต้องยืนยัน: พัฒนา interpreter/calculator ด้วย isolated fixtures ภายหลังได้ และรักษา not_current ในข้อมูลจริง
- ไม่มีทุก field ในเกม: พัฒนา task readiness และตอบเฉพาะ known needs ได้
- เจ้าของยังไม่ได้ review English ทุกข้อความ: ปรับ translation lineage และจัดทำร่างแปลได้ โดยไม่แก้สถานะอนุมัติแทน
- ไม่ได้ทดสอบเครื่องปลายทาง: เตรียม build/dependency manifest ได้ แต่ไม่ประกาศว่าทุกเครื่องใช้ได้แล้ว

## สถานะการทำงานเมื่อรับคำสั่ง “วางแผนก่อน”

หยุดที่งานเอกสาร ไม่เริ่ม test ใหม่ ไม่ติดตั้ง candidate ไม่ restart เว็บ ไม่แก้ facts/approval ของ production เก็บ candidate/ผลก่อนคำสั่งไว้แยก การตรวจเอกสาร เช่น ลิงก์ จำนวนหมวด และ hash เป็นการตรวจ artifact ไม่ใช่ทดสอบคำตอบของแชทบอท

แผนนี้ไม่ใช่ production sign-off และไม่มีการรับรองว่า common เท่าหรือดีกว่า legacy แล้ว เป้าหมายคือมีลำดับงานและ acceptance criteria ที่นำไปทำต่อได้โดยไม่ย้อนกลับไป hard-code ข้อมูลรายรายการ
