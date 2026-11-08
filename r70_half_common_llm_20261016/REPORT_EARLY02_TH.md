# ผลทดสอบครึ่งชุด — Format กลาง / เปิด LLM / R70

สถานะ: ผลบางส่วน ยังไม่ครบ

เลือก 10,277/20,554 คำถาม (50%) แบบแบ่งตามภาษา คลัง หมวด และรูปแบบคำถาม เก็บทุกเกณฑ์ที่ผูกกับคำถามที่เลือก รวม 27,923 grades

## ขอบเขต

- ใช้สำเนาแชทใหม่ R69 กับข้อมูล 602 รายการ เปิด LLM assistance ตลอดรอบ ไม่มีแขน Format เดิมหรือปิด LLM
- เรียก pipeline จริงผ่าน subprocess ที่แยกกัน 4 ตัว จำกัดช่องเรียกโมเดลร่วมกัน 1 ช่อง ไม่มีการเร่งด้วยการแทนค่าคำตอบหรือเปลี่ยนตัวเลือกข้อมูล
- สถานะจองเป็น controlled unavailable ไม่มีการยืนยันสถานะ WordPress สดหรือ browser/TCP ในรอบนี้
- เกณฑ์เดิมยังอยู่ครบ การแยก protocol และตรวจข้อความเพิ่มเติมเป็นการวิเคราะห์ผล ไม่แก้ oracle เดิมให้คะแนนสูงขึ้น

## สรุปผล

- คำถามที่ได้ผล: 1,635; grades: 4,407
- ผ่านเกณฑ์เดิมทุกข้อ: 439/4,407 (9.96%)
- ข้อสอบที่มีข้อความเชิงบวกต้องปรากฏและผ่าน: 1,398/2,004 (69.76%)
- ข้อสอบที่ไม่ตรวจข้อความโดยตรง: 1,805 grades — ไม่นับเป็นหลักฐานว่าตอบครบ
- ไม่ผ่านเฉพาะชื่อ route/intent/protocol: 2,359 grades
- exception: 0 คำถาม; คำตอบว่าง: 0

## แยกภาษา

| ภาษาในคำตอบ | คำถาม | ผ่านทุกเกณฑ์เดิม | ผ่านข้อความเชิงบวกที่กำหนด |
|---|---:|---:|---:|
| en | 790 | 210/2,131 (9.85%) | 460/729 (63.10%) |
| th | 845 | 229/2,276 (10.06%) | 938/1,275 (73.57%) |

การผ่านข้อความเป็น literal/source contract ตามชุดทดสอบ ไม่ใช่การตรวจความหมายทุกประโยคโดยมนุษย์ ตัวเลข route mismatch ไม่เท่ากับจำนวนคำตอบผิดเนื้อหา และ literal mismatch บางรายการอาจเป็นตัวเลข/ถ้อยคำ/นโยบายใน oracle ที่ต้องตรวจเทียบแหล่งอีกครั้ง

## โมเดล

- HTTP model attempts ที่สังเกตได้: 47
- transport สำเร็จ: 0; ล้มเหลว: 47
- audit ที่รับ schema ของโมเดล: 0
- หาก transport/schema ยังไม่สำเร็จ ผลรอบนี้เป็น ON ภายใต้โมเดลไม่พร้อมใช้งาน ห้ามใช้รับรองคุณภาพ inference/การแปลของ LLM

## ประเภทความไม่ผ่าน

| ประเภท | grades ที่พบ |
|---|---:|
| protocol | 3,888 |
| outcome | 1,067 |
| content_or_format | 657 |
| evidence_identifier | 201 |
| performance | 7 |

แต่ละ grade อาจอยู่ได้หลายประเภท evidence_identifier เป็นการเทียบรหัสอ้างอิงตามชุดเดิม ต้องตรวจ lineage ก่อนสรุปว่าอ้างเกมผิดจริง ส่วน outcome ต้องแยกการจำแนก mode เก่าจากการปฏิเสธ/ขอรายละเอียดที่ผู้ใช้ได้รับจริง

## หมวดที่ควรตรวจต่อ

| หมวดจากชุดคำถาม | คำถาม | ผ่านข้อความเชิงบวก | ไม่ตรวจข้อความ |
|---|---:|---:|---:|
| service_fee | 133 | 39/182 (21.43%) | 61 |
| game_detail | 95 | 189/282 (67.02%) | 4 |
| reservation_policy | 88 | 56/132 (42.42%) | 143 |
| games_catalog_availability | 110 | 163/228 (71.49%) | 55 |
| equipment | 74 | 107/146 (73.29%) | 52 |
| schedule_calendar | 70 | 83/110 (75.45%) | 114 |
| studio_rules_penalties | 65 | 47/72 (65.28%) | 160 |
| compound_context_boundary | 42 | 51/74 (68.92%) | 53 |
| games | 70 | 16/30 (53.33%) | 56 |
| booking_days_hours | 9 | 4/18 (22.22%) | 0 |
| unclassified | 226 | 22/35 (62.86%) | 309 |
| game_controls | 138 | 395/408 (96.81%) | 1 |
| general_llm | 13 | 2/13 (15.38%) | 0 |
| damage_responsibility | 8 | 6/16 (37.50%) | 0 |
| single | 19 | 10/19 (52.63%) | 0 |
| food_consumption | 7 | 10/14 (71.43%) | 0 |
| composite | 8 | 4/8 (50.00%) | 0 |
| availability_game | 15 | 12/15 (80.00%) | 0 |
| members_overview_contact | 61 | 124/126 (98.41%) | 54 |
| competition_rules | 99 | 4/6 (66.67%) | 291 |
| weekday_live_slots | 10 | 18/20 (90.00%) | 0 |
| rules_penalty | 4 | 3/5 (60.00%) | 1 |
| ambiguity_no_answer | 1 | 0/2 (0.00%) | 0 |
| compound | 6 | 5/7 (71.43%) | 0 |
| booking | 6 | 0/1 (0.00%) | 6 |
| competition | 10 | 0/1 (0.00%) | 9 |
| reservation | 4 | 6/7 (85.71%) | 1 |
| ambiguity | 1 | 0/1 (0.00%) | 0 |
| alcohol_rule | 1 | 0/1 (0.00%) | 0 |
| booking_required | 1 | 0/1 (0.00%) | 0 |
| members_about_contact | 1 | 0/1 (0.00%) | 0 |
| visit_only_fee | 1 | 0/1 (0.00%) | 0 |
| social | 3 | ไม่มีเกณฑ์ให้ตรวจ | 3 |
| ["general", "knowledge"] | 22 | ไม่มีเกณฑ์ให้ตรวจ | 39 |
| live_booking | 82 | 8/8 (100.00%) | 281 |
| food_bring_scope | 11 | ไม่มีเกณฑ์ให้ตรวจ | 7 |
| ["games", "clarification", "no_answer"] | 3 | ไม่มีเกณฑ์ให้ตรวจ | 3 |
| play_booking_controls | 10 | ไม่มีเกณฑ์ให้ตรวจ | 11 |
| price | 3 | ไม่มีเกณฑ์ให้ตรวจ | 3 |
| availability_service | 1 | 1/1 (100.00%) | 0 |
| identity_typo | 8 | ไม่มีเกณฑ์ให้ตรวจ | 16 |
| ["members", "overview"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| members | 4 | 6/6 (100.00%) | 0 |
| out_of_scope | 12 | ไม่มีเกณฑ์ให้ตรวจ | 12 |
| fee_without_service | 12 | ไม่มีเกณฑ์ให้ตรวจ | 0 |
| unclear_or_outside_scope | 8 | ไม่มีเกณฑ์ให้ตรวจ | 4 |
| policy_schedule_rules | 2 | 2/2 (100.00%) | 1 |
| game_rules | 11 | ไม่มีเกณฑ์ให้ตรวจ | 11 |
| outsider_eligibility | 6 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| equipment_access_trap | 5 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| live_schedule | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| equipment_game_inside | 3 | ไม่มีเกณฑ์ให้ตรวจ | 3 |
| schedule | 5 | 4/4 (100.00%) | 7 |
| rules | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| ["games", "no_answer"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| overview | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| ["multi_question", "reservation", "games", "equipment"] | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| games_list | 2 | ไม่มีเกณฑ์ให้ตรวจ | 5 |
| control | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| multi_question | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| ["games", "multi_question"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| ["schedule", "reservation"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| greeting | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| ["games", "reservation"] | 3 | ไม่มีเกณฑ์ให้ตรวจ | 3 |
| ["equipment", "clarification"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| clarification | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| ["clarification", "games", "equipment", "service_fee", "reservation", "no_answer"] | 2 | ไม่มีเกณฑ์ให้ตรวจ | 2 |
| ["no_answer", "games", "general"] | 1 | ไม่มีเกณฑ์ให้ตรวจ | 1 |
| ambiguous_controls | 1 | 1/1 (100.00%) | 0 |

## การรักษาไฟล์

- ฐานต้นทาง R69 ไม่เปลี่ยน: True
- โค้ดต้นทาง R69 ไม่เปลี่ยน: True
- โค้ดชุดทดสอบตรง snapshot: True
- ฐานชุดทดสอบไม่เปลี่ยน: True

## หลักฐานอ่านต่อ

- ANALYSIS_EARLY02.json: คะแนนแยกภาษา/หมวด/คลังและ model diagnostics
- FAILURE_SAMPLES_EARLY02.json: คำถาม คำตอบจริง เกณฑ์ที่คาด เหตุผลที่ไม่ผ่าน แผนเลือกข้อมูล และ sources
- FAILURE_COUNTS_EARLY02.json: เหตุผลไม่ผ่านทั้งหมดพร้อมจำนวน
- full01/RESULTS_*.jsonl.gz: คำตอบและ trace ของทุกคำถามที่รัน
- SELECTED_JOBS.jsonl / STRATA.json / CONFIG.json: รายการเลือก วิธีแบ่ง และ hash ของข้อมูล/โค้ด
