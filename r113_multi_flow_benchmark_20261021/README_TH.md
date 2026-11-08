# R113 — จุดเริ่มอ่านผลทดลอง Flow รายหมวด

## สถานะ

ชุดหลัก **main_natural เสร็จครบ 4,200 ผล** = 14 หมวด × 3 configurations × 100 คำถามร่วมกันต่อหมวด ตรวจคู่ Flow–คำถามครบ ไม่ซ้ำ frozen source/code ตรงเดิม และ model digest ก่อน–หลังตรงกัน ดู `AUDIT_FINAL.json` และ `main_natural/TEST_COMPLETE.json`

งานนี้เป็นการทดลองตัวอ่านรายหมวดจาก 3 algorithm families ที่ใช้ source projection ร่วมกัน ยังไม่ได้ติดตั้งทับ R78 และไม่ได้ทดสอบ global category router หรือยืนยันว่า graph/solver ในแนวคิดทั้งหมดเป็น production-complete แล้ว

## อ่านตามลำดับ

1. `01_DESIGNS_AND_SELECTION_TH.md` — 10 แนวคิดต่อหมวด รวม140 แบบ พร้อมคะแนน heuristic และ42ตัวที่เลือกก่อนรัน
2. `01B_ALL_FLOW_STEPS_AND_IMPLEMENTATION_SCOPE_TH.md` — ขั้นตอนของทุกแนวคิด ข้อบกพร่องที่ต้องคุม และขอบเขตที่ prototype ทำจริง
3. `02_BENCHMARK_REPORT_TH.md` — คะแนนทั้ง42ตัว ผู้ได้คะแนนสูงสุดรายหมวด ผลภาษา/strata และตัวอย่างข้อพลาด
4. `03_ROOT_CAUSE_AND_NEXT_FLOW_TH.md` — สาเหตุรายหมวด ตัวอย่างพร้อม expected/source evidence และ Flow ที่ควรเสริมจากผลจริง

คะแนนออกแบบไม่ใช่เปอร์เซ็นต์ตอบถูก และไม่ใช่การประเมินอิสระเชิงประจักษ์ครบ140แบบ คะแนน benchmark ตรวจ source-claim/ค่า/ที่มา/ขอบเขต/answer-state จากชุดพัฒนา ไม่ใช่ human semantic accuracy หรือคะแนนของแชทจริงทั้งระบบ

## ชุดข้อมูลและหลักฐาน

- `EFFECTIVE_QUESTIONS_1400.jsonl` — คำถามที่ใช้จริง คำถามเดียวกันทั้งสามตัวในแต่ละหมวด
- `EXCLUSION_ADDENDUM.json` — แทน7คำถามหน่วยโทษ Tekken ที่เจ้าของสั่งงด ก่อน C13 execute โดยเก็บต้นฉบับทั้งหมด
- `main_natural/RESULTS.jsonl` — ทุกคำถาม คำตอบ claim/evidence และผลตรวจ
- `main_natural/MODEL_EVENTS.jsonl` —308 HTTP events ที่บันทึกสำเร็จ;308 transport successes,60 batches มี schema/แผนไม่ครบ กระทบ176คำถาม
- `SCORES_42.json`, `RANKING_BY_CATEGORY.json`, `ALL_FAILED_CASES.jsonl` —คะแนนและข้อไม่ผ่านครบ
- `WINNER_CANDIDATE_CONFIG.json` —ข้อเสนอประกอบตัวอ่าน ยังไม่ติดตั้งจริง
- `AUDIT_FINAL.json` —ผลตรวจความครบ hashes และ trace linkage

C12ใช้ controlled live fixtures และ C14ใช้ synthetic news จึงไม่ยืนยันสถานะลูกค้าหรือข่าวจริง C13บางคำตอบภาษาอังกฤษยังใช้ข้อความต้นฉบับไทย C06มี31คำถามที่ยังใช้ internal record ID แทนชื่อแสดงผล และ unknown cases รอบนี้เป็นภาษาไทยทั้งหมด

## แยก pilot ให้ชัด

`pilot_field_contract/` และไฟล์ `RESULTS.jsonl`, `TEST_COMPLETE.json`, `STATUS.json` ที่รากโฟลเดอร์ R113 เป็น pilot แบบถามชื่อฟิลด์ตรง ซึ่งเก็บไว้ตามเดิม **คะแนนสรุปครั้งนี้ใช้ main_natural เท่านั้น** ไม่รวม pilot เพื่อเลือกคำตอบที่ดีกว่า

## รันตัวอ่านด้วยตนเอง

`flow_engine.py --flow C05-F04 --question "ข้อความคำถาม" --locale th`

ระบุ Python interpreter ที่ใช้ก่อนชื่อไฟล์ รันจากโฟลเดอร์งานได้ ตัวเลือกที่มีทั้งหมดอยู่ใน `SELECTED_42.json` และ `flows/` โดย engine ไม่อ่าน workload หรือ expected answers เพื่อเลือกคำตอบ
