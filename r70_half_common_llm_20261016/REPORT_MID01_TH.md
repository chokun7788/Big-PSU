# ผลทดสอบครึ่งชุด — Format กลาง / เปิด LLM / R70

สถานะ: ผลบางส่วน ยังไม่ครบ

เลือก 10,277/20,554 คำถาม (50%) แบบแบ่งตามภาษา คลัง หมวด และรูปแบบคำถาม เก็บทุกเกณฑ์ที่ผูกกับคำถามที่เลือก รวม 27,923 grades

## ขอบเขต

- ใช้สำเนาแชทใหม่ R69 กับข้อมูล 602 รายการ เปิด LLM assistance ตลอดรอบ ไม่มีแขน Format เดิมหรือปิด LLM
- เรียก pipeline จริงผ่าน subprocess ที่แยกกัน 4 ตัว จำกัดช่องเรียกโมเดลร่วมกัน 1 ช่อง ไม่มีการเร่งด้วยการแทนค่าคำตอบหรือเปลี่ยนตัวเลือกข้อมูล
- สถานะจองเป็น controlled unavailable ไม่มีการยืนยันสถานะ WordPress สดหรือ browser/TCP ในรอบนี้
- เกณฑ์เดิมยังอยู่ครบ การแยก protocol และตรวจข้อความเพิ่มเติมเป็นการวิเคราะห์ผล ไม่แก้ oracle เดิมให้คะแนนสูงขึ้น

## สรุปผล

- คำถามที่ได้ผล: 4,465; grades: 12,264
- ผ่านเกณฑ์เดิมทุกข้อ: 1,151/12,264 (9.39%)
- ข้อสอบที่มีข้อความเชิงบวกต้องปรากฏและผ่าน: 3,882/5,511 (70.44%)
- ข้อสอบที่ไม่ตรวจข้อความโดยตรง: 5,067 grades — ไม่นับเป็นหลักฐานว่าตอบครบ
- ไม่ผ่านเฉพาะชื่อ route/intent/protocol: 6,540 grades
- exception: 0 คำถาม; คำตอบว่าง: 0

## แยกภาษา

| ภาษาในคำตอบ | คำถาม | ผ่านทุกเกณฑ์เดิม | ผ่านข้อความเชิงบวกที่กำหนด |
|---|---:|---:|---:|
| en | 2,215 | 558/6,015 (9.28%) | 1,334/2,071 (64.41%) |
| th | 2,250 | 593/6,249 (9.49%) | 2,548/3,440 (74.07%) |

การผ่านข้อความเป็น literal/source contract ตามชุดทดสอบ ไม่ใช่การตรวจความหมายทุกประโยคโดยมนุษย์ ตัวเลข route mismatch ไม่เท่ากับจำนวนคำตอบผิดเนื้อหา และ literal mismatch บางรายการอาจเป็นตัวเลข/ถ้อยคำ/นโยบายใน oracle ที่ต้องตรวจเทียบแหล่งอีกครั้ง

## โมเดล

- HTTP model attempts ที่สังเกตได้: 110
- transport สำเร็จ: 0; ล้มเหลว: 110
- audit ที่รับ schema ของโมเดล: 0
- หาก transport/schema ยังไม่สำเร็จ ผลรอบนี้เป็น ON ภายใต้โมเดลไม่พร้อมใช้งาน ห้ามใช้รับรองคุณภาพ inference/การแปลของ LLM

## ประเภทความไม่ผ่าน

| ประเภท | grades ที่พบ |
|---|---:|
| protocol | 10,964 |
| outcome | 3,264 |
| content_or_format | 1,739 |
| evidence_identifier | 529 |
| performance | 21 |
| native_quality_composite | 4 |

แต่ละ grade อาจอยู่ได้หลายประเภท evidence_identifier เป็นการเทียบรหัสอ้างอิงตามชุดเดิม ต้องตรวจ lineage ก่อนสรุปว่าอ้างเกมผิดจริง ส่วน outcome ต้องแยกการจำแนก mode เก่าจากการปฏิเสธ/ขอรายละเอียดที่ผู้ใช้ได้รับจริง

## หมวดที่ควรตรวจต่อ

| หมวดจากชุดคำถาม | คำถาม | ผ่านข้อความเชิงบวก | ไม่ตรวจข้อความ |
|---|---:|---:|---:|
| service_fee | 321 | 154/475 (32.42%) | 159 |
| game_detail | 262 | 512/736 (69.57%) | 17 |
| reservation_policy | 249 | 191/373 (51.21%) | 445 |
| games_catalog_availability | 306 | 429/593 (72.34%) | 207 |
| equipment | 233 | 335/494 (67.81%) | 165 |
| studio_rules_penalties | 199 | 140/232 (60.34%) | 492 |
| schedule_calendar | 189 | 200/273 (73.26%) | 325 |
| compound_context_boundary | 138 | 108/174 (62.07%) | 172 |
| game_controls | 380 | 1,081/1,135 (95.24%) | 1 |
| unclassified | 601 | 53/96 (55.21%) | 862 |
| general_llm | 53 | 10/53 (18.87%) | 0 |
| damage_responsibility | 24 | 14/48 (29.17%) | 0 |
| booking_days_hours | 25 | 16/50 (32.00%) | 0 |
| games | 190 | 53/80 (66.25%) | 157 |
| single | 33 | 16/33 (48.48%) | 0 |
| members_overview_contact | 153 | 326/340 (95.88%) | 140 |
| food_consumption | 20 | 30/40 (75.00%) | 0 |
| composite | 19 | 10/19 (52.63%) | 0 |
| competition_rules | 273 | 22/30 (73.33%) | 755 |
| booking | 19 | 5/12 (41.67%) | 11 |
| rules_penalty | 10 | 4/11 (36.36%) | 1 |
| competition | 26 | 0/6 (0.00%) | 20 |
| weekday_live_slots | 23 | 40/46 (86.96%) | 0 |
| availability_game | 34 | 28/34 (82.35%) | 0 |
| ambiguity_no_answer | 4 | 4/8 (50.00%) | 0 |
| members_about_contact | 4 | 1/4 (25.00%) | 0 |
| schedule | 18 | 10/12 (83.33%) | 12 |
| compound | 18 | 19/21 (90.48%) | 0 |
| live_booking | 220 | 32/33 (96.97%) | 737 |
| availability_service | 3 | 2/3 (66.67%) | 0 |
| reservation | 9 | 12/13 (92.31%) | 3 |
| multi_question | 10 | 0/1 (0.00%) | 9 |
| ambiguity | 1 | 0/1 (0.00%) | 0 |
| all_games_scope | 1 | 0/1 (0.00%) | 0 |
| clarification_no_answer | 1 | 0/1 (0.00%) | 0 |
| alcohol_rule | 1 | 0/1 (0.00%) | 0 |
| booking_required | 1 | 0/1 (0.00%) | 0 |
| ambiguous_controls | 2 | 1/2 (50.00%) | 0 |
| visit_only_fee | 1 | 0/1 (0.00%) | 0 |
| no_answer | 1 | 0/1 (0.00%) | 0 |
| social | 5 | ไม่มีเกณฑ์ให้ตรวจ | 5 |
| ["general", "knowledge"] | 49 | ไม่มีเกณฑ์ให้ตรวจ | 70 |
| food_bring_scope | 20 | ไม่มีเกณฑ์ให้ตรวจ | 11 |
| ["games", "clarification", "no_answer"] | 5 | ไม่มีเกณฑ์ให้ตรวจ | 5 |
| play_booking_controls | 20 | ไม่มีเกณฑ์ให้ตรวจ | 21 |
| price | 5 | ไม่มีเกณฑ์ให้ตรวจ | 6 |
| identity_typo | 20 | ไม่มีเกณฑ์ให้ตรวจ | 46 |
| ["members", "overview"] | 8 | ไม่มีเกณฑ์ให้ตรวจ | 8 |
| members | 12 | 21/21 (100.00%) | 0 |
| out_of_scope | 24 | ไม่มีเกณฑ์ให้ตรวจ | 24 |
| fee_without_service | 28 | ไม่มีเกณฑ์ให้ตรวจ | 0 |
| unclear_or_outside_scope | 17 | ไม่มีเกณฑ์ให้ตรวจ | 11 |
| policy_schedule_rules | 2 | 2/2 (100.00%) | 1 |
| game_rules | 20 | ไม่มีเกณฑ์ให้ตรวจ | 20 |
| outsider_eligibility | 18 | ไม่มีเกณฑ์ให้ตรวจ | 8 |
| equipment_access_trap | 24 | ไม่มีเกณฑ์ให้ตรวจ | 13 |
| live_schedule | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| equipment_game_inside | 21 | ไม่มีเกณฑ์ให้ตรวจ | 21 |
| rag_knowledge | 4 | ไม่มีเกณฑ์ให้ตรวจ | 4 |
| identity | 4 | ไม่มีเกณฑ์ให้ตรวจ | 5 |
| ["games", "reservation"] | 12 | ไม่มีเกณฑ์ให้ตรวจ | 12 |
| ["equipment", "clarification"] | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| protected | 1 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| greeting | 8 | ไม่มีเกณฑ์ให้ตรวจ | 15 |
| ["multi_question", "reservation", "games", "equipment"] | 7 | ไม่มีเกณฑ์ให้ตรวจ | 7 |
| contact | 6 | ไม่มีเกณฑ์ให้ตรวจ | 8 |
| control | 5 | ไม่มีเกณฑ์ให้ตรวจ | 6 |
| games_list | 3 | ไม่มีเกณฑ์ให้ตรวจ | 6 |
| clarification | 8 | ไม่มีเกณฑ์ให้ตรวจ | 8 |
| rules | 4 | ไม่มีเกณฑ์ให้ตรวจ | 4 |
| ["games", "no_answer"] | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| overview | 5 | ไม่มีเกณฑ์ให้ตรวจ | 6 |
| ["no_answer", "games", "general"] | 3 | ไม่มีเกณฑ์ให้ตรวจ | 3 |
| ["games", "multi_question"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| ["schedule", "reservation"] | 4 | ไม่มีเกณฑ์ให้ตรวจ | 4 |
| live_availability | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| ["equipment", "games"] | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| ["rules", "penalty"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| ["clarification", "games", "equipment", "service_fee", "reservation", "no_answer"] | 3 | ไม่มีเกณฑ์ให้ตรวจ | 3 |
| availability_machine_split | 1 | 1/1 (100.00%) | 0 |
| ["games", "clarification"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| input_quality | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |

## การรักษาไฟล์

- ฐานต้นทาง R69 ไม่เปลี่ยน: True
- โค้ดต้นทาง R69 ไม่เปลี่ยน: True
- โค้ดชุดทดสอบตรง snapshot: True
- ฐานชุดทดสอบไม่เปลี่ยน: True

## หลักฐานอ่านต่อ

- ANALYSIS_MID01.json: คะแนนแยกภาษา/หมวด/คลังและ model diagnostics
- FAILURE_SAMPLES_MID01.json: คำถาม คำตอบจริง เกณฑ์ที่คาด เหตุผลที่ไม่ผ่าน แผนเลือกข้อมูล และ sources
- FAILURE_COUNTS_MID01.json: เหตุผลไม่ผ่านทั้งหมดพร้อมจำนวน
- full01/RESULTS_*.jsonl.gz: คำตอบและ trace ของทุกคำถามที่รัน
- SELECTED_JOBS.jsonl / STRATA.json / CONFIG.json: รายการเลือก วิธีแบ่ง และ hash ของข้อมูล/โค้ด
