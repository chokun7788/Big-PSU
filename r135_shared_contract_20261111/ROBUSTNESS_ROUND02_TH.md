# ผลทดลองและแก้ Flow รอบ 02 — 11 พฤศจิกายน 2026

ทำต่อในสำเนา `r135_shared_contract_20261111` จากโค้ดรอบ 01 ที่ commit e9892417 โดยเก็บ parent, full R135 และผลวัดเก่าไว้ ไม่เปลี่ยนข้อมูลเจ้าของหรือ frozen evaluation

## สิ่งที่พบจากการทดลองจริง

1. **คำถามที่มีข้อความซ้ำผูกตำแหน่งผิด**: compiler เคยเลือกตำแหน่งแรกด้วย `find` แม้เป็น task ที่สอง ส่วน observer อาจเพิ่มงานที่สาม ทั้งที่ผู้ใช้ถามสองส่วน ชุดก่อนแก้ 6 checks ล้ม 3 เก็บใน `quote_occurrences_1794413317458781100/RESULT.json`
2. **เกมคนละภาคถูกแทนกัน**: matrix 27 คำถามก่อนแก้ผ่าน 26 แต่ `TEKKEN 9 ปุ่มอะไร` ส่งปุ่มของ TEKKEN 8 เพราะ alias ทั่วไป “Tekken” ผูกกับ record ภาค 8 เก็บใน `robustness_round02_1794413548763844300/RESULT.json`
3. **reader สำรองยังข้ามการผูกชื่อเกมได้**: ตรวจเพิ่มพบ `TEKKEN 9 มีให้เล่นไหม` ตอบบริการของภาค 8 และ `TEKKEN 9 คือเกมอะไร` ตอบคำอธิบายของภาค 8 การแก้ index และ typed receipt อย่างเดียวหยุด availability ได้ แต่ compatibility description ยังหลุด ชุด 18 checks จึงล้ม 1 เก็บใน `numeric_edition_1794414208075423300/RESULT.json` ไม่ถอนกรณีล้มออกจากรายงาน

## วิธีแก้และขอบเขต

- เพิ่ม `task_quote_spans` ใช้ exact raw offsets ร่วมกันระหว่าง compiler, context bindings และ observer หากเป็นประโยคเต็มที่ซ้ำและจำนวน task ในแต่ละครอบครัวตรงกับจำนวน occurrence จึงผูกตามลำดับ หากเป็น substring ซ้ำที่ยังระบุเจ้าของไม่ได้ ให้ error `task_quote_occurrence_ambiguous` และไม่สืบทอด shared slots โดยเดา
- การมีหลาย field ในประโยคเดียวที่มีตำแหน่งเดียว ยังใช้ตำแหน่งร่วมกันได้ การแก้นี้เป็น provenance ของข้อความ ไม่ใช่หลักฐานว่าเข้าใจเจตนาทุกแบบ
- เพิ่ม numeric game-family scope จากชื่อ/alias ของ game records ใน snapshot ปัจจุบัน ไม่ hardcode ว่าภาคใดมีบริการ หากหมายเลขที่ระบุไม่ตรงกับต้นทาง ให้หยุดการแทนด้วย alias ทั่วไป
- ตรวจ C04/C05 ที่ index, control selector, independent receipt และ final compatibility guard เพื่อไม่ให้ reader สำรองส่งคำตอบผิดภาคกลับมา แม้ planner ไม่ระบุ target
- ตัวเลขที่ตามด้วยหน่วยคน ชั่วโมง นาที หรือบาทไม่ถูกใช้เป็นภาคเกมตามกติกาที่ตรวจไว้ แต่ยังไม่ครอบคลุมชื่อภาคแบบคำ, Roman numerals, DLC, ชื่อพิเศษ หรือความสัมพันธ์เกมทุกแบบ
- หยุดและเปิดใหม่เฉพาะ preview ของ candidate ที่พอร์ต 8143 หลังแก้โค้ด ใช้ version `R135-Shared-contract-round02` ไม่หยุดหรือเปลี่ยนโมเดล

## การตรวจรับรอบนี้

ผลและจำนวนสุดท้ายอ่านจาก `ROUND02_MANIFEST.json` และ `ROUND02_TEST_BATCH.json` ซึ่งบันทึกเฉพาะผลที่เกิดขึ้นจริง ผลก่อนแก้และผลที่ล้มระหว่างทางเก็บแยก ไม่เขียนทับ

- Matrix เดิมตรึง 27 คำถาม: คำผิดข้างแป้น/ตัวขาด/ตัวเบิ้ล/สลับตัวอักษร, คำถามหลายส่วน, ข้อความซ้ำ, ข้อมูลไม่พอ, ปฏิเสธ, คนละหน่วยงาน, ราคา 0 บาท, ยอดรวม Cockpit, การจอง, อุปกรณ์ และข้อมูล 6 sessions
- ชุด quote occurrence 6 checks และ forced stale-context 3 checks แยกจากจำนวนคำถาม matrix
- ชุด numeric edition ตรวจทั้งกรณีปกติ, ภาคที่ไม่มีต้นทางรองรับ, ภาษาไทย/อังกฤษ/ติดกัน, จำนวนคน/ระยะเวลา และบังคับส่ง receipt/compatibility answer ผิดภาค
- Affected regressions: shared contract, control/platform/preset/version, verified sources และ isolated edit/withdraw, typo recovery, bounded budget
- HTTP ผ่านเส้นทางแชตจริงแบบส่งทีละคำถาม รวมกรณีใหม่และ compound/typo regressions เก็บคำตอบฉบับเต็มใน DETAILS ที่เครื่องเท่านั้น

ชุดนี้มีทั้งกรณีที่รู้แล้วและกรณีที่ใช้พัฒนา จึงไม่ใช่ unseen accuracy และไม่ใช้แทนคะแนน 200/2,111 ข้อเดิม การผ่าน HTTP ไม่ได้แปลว่าความหมายถูกทั้งหมด

## สิ่งที่ยังไม่ปิด

- ยังไม่มีคะแนน semantic accuracy ใหม่ หรือการตรวจรับครบ 48/76 requirements
- ยังไม่แก้ root cause ของ context timeout/cooldown และไม่พิสูจน์ hard cancellation หรือ model admission ทุกเส้นทาง
- คำชี้แจงของ unknown sibling บางแบบยังซ้ำ และ catalog/currentness มีข้อจำกัดเดิม
- พบข้อความอาหรับ `بشكل` ปนอยู่ในคำอธิบาย TEKKEN 8 ภาษาไทย ตรวจ read-only แล้วมีอยู่ใน payload ของ `controls_ps5_tekken_8` จริง จึงเป็นปัญหาคุณภาพข้อมูลต้นทางที่ยังไม่แก้ ไม่ใช้ผลผ่าน scope check ไปอ้างว่าข้อความทุกบรรทัดถูกต้อง
- ยังต้อง owner/editor HTTP lifecycle, attachment/source-scope และกรณีหลายหน่วย/หลาย audience ตามแผนเดิม
- ถ้าคำถามหลายเกมใน task เดียวระบุภาคหลายค่าของ family เดียวกัน ระบบยังรักษาความกำกวม ไม่อ้างว่าทำ comparison ได้แล้ว
- ไม่ฝึก weights จาก eval holdout และไม่ติดตั้งแทน production

ขั้นถัดไปเลือกกลุ่มความผิดจริงจากผล/trace เช่นข้อความ partial ซ้ำและ timeout admission แล้วแก้เป็นกลุ่มก่อนรันทดสอบรวม ไม่วนรันชุดใหญ่โดยไม่มีการเปลี่ยนที่เกี่ยวข้อง

## ผลสุดท้ายที่ตรวจแล้ว

Matrix ผ่าน 27/27 คำถามตามความคาดหวังที่ตรึงไว้; focused checks อื่น 149 checks ผ่าน; แชตจริง 21 คำขอ / 52 assertions ผ่าน ตัวเลขเหล่านี้เป็นคนละตัวหารและมีการตรวจพฤติกรรมซ้ำกัน จึงไม่บวกเป็นจำนวนคำถามหรือเปอร์เซ็นต์ความแม่นยำ

| ชุดตรวจ | คำขอ | Checks | สถานะ |
|---|---:|---:|---|
| `robustness_round02_final_1794414342305908300` | 27 | 0 | ผ่าน |
| `shared_contract_1794414420173088800` | 0 | 33 | ผ่าน |
| `control_scope_1794414444933402900` | 0 | 25 | ผ่าน |
| `verified_sources_controls_1794414458437140400` | 0 | 22 | ผ่าน |
| `typo_controls_1794414500287005300` | 0 | 35 | ผ่าน |
| `bounded_response_1794414540143098800` | 0 | 6 | ผ่าน |
| `quote_occurrences_1794413470435201900` | 0 | 6 | ผ่าน |
| `context_recheck_1794414031653355900` | 0 | 3 | ผ่าน |
| `numeric_edition_1794414312565486300` | 0 | 19 | ผ่าน |
| `round02_http_1794414374973870200` | 7 | 19 | ผ่าน |
| `shared_http_1794414407708643500` | 3 | 12 | ผ่าน |
| `typo_http_1794414415780459100` | 11 | 21 | ผ่าน |
