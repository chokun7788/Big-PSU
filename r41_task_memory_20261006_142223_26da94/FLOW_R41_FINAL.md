# Flow r41: parent task memory / scope / task coverage

## ขอบเขต

ทำ B007/B008/B010/B011/B055/B062 และเกณฑ์ B041 ต่อจาก r40.3. ไม่รัน full corpus ไม่เปลี่ยน fact เจ้าของ ไม่สลับ calendar D: โดยเดา และไม่เปลี่ยนพฤติกรรม Refresh/Clear. เก็บ backup/raw/release ใหม่ทั้งหมด

## ขั้นทำจริง

1. Baseline multi-turn TH/EN บนเว็บ r40.3: all หลังควบคุม, กลับไปงานเก่า, ordinal choices, ambiguous scope และ partial compound
2. เพิ่ม parent memory schema ของ requested tasks แยก domain/operation/targets/query/price filters/provenance/response ID; bounded ≤8 tasks และใช้ TTL/session/revision เดิม
3. Harvest เฉพาะงานจาก server-completed response + user/resolved query; ไม่อนุมานเป้าหมายจาก assistant examples หรือ client fallback
4. Resume เฉพาะ explicit return-to-domain marker; ถ้าไม่ระบุ operation ชัดหรือมีหลายงานที่ตรง ให้ clarification ไม่เลือกงานแรกตามใจ
5. ใช้ archived question เป็นคำขอใหม่ผ่าน pipeline; ไม่ส่ง cached answer โดยเฉพาะ booking. ตรวจ client acknowledgement ก่อนใช้ generic memory
6. Bare all ใช้ latest eligible task เมื่อ scope ชัด: controls ของเกมที่ผู้ใช้เลือก; catalog ทุกโซนเมื่อขอ all zones; family explicit offered choices ไม่ถือ example list เป็น selected. กรณีหลายมิติ/ไม่มีเป้าหมายให้ถามเฉพาะที่ขาด
7. Ordinal selectors ใช้ได้เฉพาะ explicit offered choices พร้อมลำดับที่ผู้ใช้เห็น; ordinary catalog ที่มีทั้ง zone/game ถามยืนยัน ไม่เดาว่าอันแรกคืออะไร
8. Compound task contract แยก executed/answered/partial/clarification/missing/unavailable/invalid; parent complete ต้องไม่มี child unanswered. Contract นี้พิสูจน์ task execution ไม่ใช่ความครบของ facts ทุก clause
9. API/log/decision artifact ใช้ contract ที่มีชนิดชัด ไม่นำ price contract ไปใช้กับทุก domain; parent adapter และ source harness ต้องใช้เส้นทางเดียวกัน
10. Targeted + negative + regression: new explicit question, negation/edition, expiry, cross-session, late completion, retry, unacknowledged response, ambiguous return, single-vs-compound. ตรวจ contents/child outcomes ไม่ใช้ชื่อในหัวคำถามเป็น gold
11. สร้าง candidate ใหม่, hash/source parity, เปิด local LLM+RAG จริง, ทดสอบ HTTP และแก้จาก failure ที่พบ
12. รายงาน actual results/remaining limits; independent new cases ที่นำมาแก้แล้วต้องเปลี่ยนสถานะเป็น regression

## Review ก่อนลงมือ

- Memory เก็บคำขอไม่ใช่ความจริง; ข้อมูลสดต้อง lookup ใหม่
- Resume ไม่เกิดจาก bare device/game title หลังเปลี่ยนหัวข้อ: ต้องมี explicit return marker
- Price filters แยกจาก generic tasks; ราคา/นโยบายเดิมไม่ถูกแก้
- Client fallback ไม่สามารถสร้าง archived memory และ acknowledgement ไม่เท่ากับ source verification
- unknown targets/edition/partial outcome ต้องถูกเก็บแยกจาก successful lookup
- ไม่มี persistent personal memory หรือ auto-start ใหม่จากคำขอนี้

หลักการจาก CheckList/CheckDST/SGD ที่อ้างใน Flow r40: ทดสอบ invariance/directional behavior และ schema-based state. ใช้ผลโครงการเองเป็นหลักฐาน ไม่ใช้คะแนน paper แทน tests

## Flow หลังแก้และตรวจทาน

### A. รับคำถามและสถานะ

1. ตรวจ session/turn fingerprint: turn ID เดิมกับคำถามใหม่เป็น conflict; duplicate เดิม replay ไม่เพิ่ม revision
2. Parent store ตรวจ TTL/session/revision และ acknowledgement ของคำตอบก่อนหน้า
3. Explicit return-to-topic → หา requested task ของ operation นั้นที่ server ทำเสร็จและ client แจ้งว่าได้รับแล้ว
4. ถ้าตัวกลับเรื่องมีชื่อเป้าหมายใหม่ ตัวเลข หรือคำปฏิเสธ → ใช้ตัวแก้บริบทปกติ รักษาคำถามใหม่; เงื่อนไขส่วนเกินที่ยังรวมไม่ได้ → ถาม scope
5. Bare all → ตรวจว่ามี operation เดียวหรือหลายเรื่อง; หลายเรื่องถามว่าหมายถึงส่วนใด
6. Controls ของเกมที่เลือก → ตอบปุ่มจากแหล่งเดิมใหม่; unresolved child ยังอยู่ใน scope; ห้ามเหลือแต่ known titles
7. Catalog มีทั้งโซนและเกม → bare all/ordinal ถามแกนที่ต้องการ; all zones ชัดเจนแล้วจึงแสดงทุกโซน
8. Family menu → ใช้ตัว resolver ที่มีอยู่ตรวจว่าคำถามมี family ambiguity จริง แล้วเก็บเฉพาะ candidates ที่แสดงในคำตอบตามลำดับ; generic example list ไม่ใช่ menu
9. ราคาใช้ schema ราคาเดิม รักษา customer_group_ids/packages/duration/exclusions; resume ไม่ใช้ราคาที่เคยตอบเป็นแหล่งใหม่

### B. แผนและการ execute

1. Parent ส่ง context_resolution และ request_plan มีชนิดชัดถึง worker
2. dialogue_state_clarification_v1 → deterministic clarification TH/EN ไม่เรียก intent model
3. dialogue_selection_v1 → execute 1–4 requests ตามลำดับ; เกินขอบเขตถามแบ่งคำขอ ไม่ตัด subset
4. Compound เดียวกันหลาย targets ต้องรวม memory โดยรักษา child queries และ request labels แม้บาง target ไม่มีข้อมูล
5. Deadline ระหว่าง children → เก็บ executed/pending IDs แต่ระบุ unavailable และ output_withheld; ไม่รายงานคำตอบทั้งหมดสำเร็จ
6. Final language/source validator veto → schema_rejected แม้ children เคย execute; ไม่ให้ parent complete ค้างอยู่
7. Memory ไม่เก็บ answer/hits/prices/status availability เพื่อ replay facts; เก็บคำขอเพื่อให้ execute ใหม่เท่านั้น

### C. Contract ที่อ่านได้

| ค่า | ความหมาย | สิ่งที่ไม่ได้พิสูจน์ |
|---|---|---|
| answered | มีคำตอบของ task ที่ผ่าน validator ปัจจุบัน | ไม่ยืนยัน semantic accuracy ทุกข้อหรือนโยบายล่าสุด |
| partial | full-rule coverage ยังมี remaining/missing clauses | ไม่ยืนยันว่าอ่านเอกสารครบ |
| clarification | ต้องเลือกเป้าหมาย/ขอบเขต | ไม่ใช่ข้อมูลในฐานสูญหาย |
| missing | no_answer/unconfirmed/unverified/source gap | ไม่แปลว่า API ล่ม |
| unavailable | เส้นทาง timeout/backend unavailable | ไม่แปลว่าเครื่องถูกจอง |
| rejected | validator ไม่ยอมส่ง draft | ไม่ใช้ validator ok ของข้อความ fallback เป็นหลักฐานว่า draft ถูก |

Compound มี expected_task_ids/executed_task_ids/tasks/answered_task_ids/pending_task_ids/missing_task_ids/outcome. API, log และ decision artifact บันทึก contract เดียวกัน

### D. ทำจริง 4 รอบตรวจและปรับ

1. Baseline แสดงช่องว่าง request memory ข้ามหมวด และ absence ของ coverage metadata; แยก metadata-only failure จากคำตอบผิด
2. เพิ่ม memory + scoped all + per-task contract → source และ HTTP หลัก 25/25
3. Variation 16 เคสพบ family menu ยังไม่ harvest และ Thai unknown target inherit old game; พบ grader catalog ใช้ mode เดียว และเฉลย second option ไม่ตรงลำดับจริง → แก้โค้ดและ oracle แยกกัน
4. Regression พบ guard กว้างไปจน bare unknown selections ไม่เก็บ pending operation → จำกัดเฉพาะ complete controls question; เพิ่ม partial-all เพื่อกัน missing child ถูกตัด; final variants 18/18 พร้อม unit/HTTP เดิม

ไม่ถือจำนวนรอบเป็นหลักฐานความถูกต้อง ผลผ่านต้องมี raw และ oracle ที่ตรวจ operation/content/scope/outcome ตามชนิด task

## หลักการประกอบและข้อจำกัดหลักฐาน

- CheckList: ใช้ minimum functionality/invariance/directional expectation ตรวจ all/resume/new target โดยไม่เหมารวมคะแนนชุดใหญ่: https://aclanthology.org/2020.acl-main.442/
- CheckDST: แยกการรักษา dialogue state จากการตอบภาษาได้: https://aclanthology.org/2022.findings-emnlp.391/
- Schema Guided Dialogue: ใช้ domain/operation/slots แยกชัด: https://arxiv.org/abs/1909.05855
- ใช้แนวคิดประกอบการออกแบบ ไม่อ้างว่า implementation นี้เหมือนระบบใน paper หรือได้คะแนนเดียวกัน ไม่ค้น paper เพิ่มในรอบนี้

## งานที่ยังทำเองต่อได้

1. Generalize clarification/return selectors ไปยังสมาชิก เวลา และ booking พร้อม fixture; รอบนี้ยังไม่ได้เปิด explicit resume ของทุกหมวด
2. วัด retrieval candidate quality + content completeness ต่อ fact/section แยกจาก task execution; semantic accuracy ไม่ได้เกิดจาก contract อย่างเดียว
3. เพิ่ม typo/paraphrase holdout ที่อิสระจากการแก้ครั้งนี้; fresh variants ที่ถูกใช้แก้แล้วถือเป็น regression
4. สร้าง WithModels/DownloadModels ตาม source ใหม่และตรวจบนเครื่องสะอาด; candidate รอบนี้เป็นแพ็กเกจทดลองในเครื่องนี้
5. ตรวจ booking stale/error/count/timezone ด้วย fixture เพิ่ม แล้วค่อย real slot oracle เมื่อมีข้อมูลจริง
6. ตรวจ recovery/latency under concurrency และ source update/translation gap; เก็บ rate/owner policy ไม่แก้โดยเดา

## จุดที่ต้องให้มนุษย์ยืนยัน

- อัตราค่าบริการปัจจุบันหลังตารางเก่าหมดอายุ 31/03/2026
- Tekken pause conditions ที่เอกสารขัดกัน; RoV ข้อที่ต้นฉบับไม่ครบ; competition roster/check-in/VALORANT source gaps
- สถานะจองจริงรายเครื่องและช่วงเวลาเทียบ booking ของเจ้าของ ไม่อนุมานจาก connect API สำเร็จ
- นโยบายถ่ายภาพ/อาหาร/ผู้ใช้ภายนอก และศัพท์ชื่อทางการที่แหล่งยังไม่ยืนยัน

## เกณฑ์ส่งมอบ

Passed targeted automated checks + unchanged protected files + frozen local release/source parity. ไม่เท่ากับ backlog 66 ข้อหมด ไม่รับรองภาษาแปรรูปทุกแบบ ไม่รับรอง current owner facts หรือ fresh-machine installation
