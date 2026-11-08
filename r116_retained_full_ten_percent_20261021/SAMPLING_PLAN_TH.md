# R116 — แผนสุ่ม Full เดิม หมวดละ 10%

ประชากร 20,554 request keys; สุ่ม 2,108 keys / 5,643 oracle rows จากหมวดและหมวดย่อยเดิม 104 กลุ่ม ด้วย ceil(0.10 × จำนวนกลุ่ม) จึงรวมเป็น 10.256% หลังปัดขึ้นแต่ละกลุ่ม

ไทย 790, อังกฤษ 1,056, auto 262 ตามสัดส่วนในแต่ละหมวด ไม่เลือกจากคำตอบหรือผลผ่าน/ไม่ผ่าน ไม่สร้างคำถามใหม่แทน Full เดิม

R115 คัดลอกแยกไว้และตรึงโค้ด/ข้อมูลก่อนเริ่ม เปิด LLM จริง ผ่าน API และเก็บ actual PipelineAnswer ตาม request_id การเก็บ debug ไม่แก้คำตอบ API

วันที่อ้างอิงปกติ 2026-10-21T12:00:00+07:00 ส่วนโจทย์ที่กำหนดวันเฉพาะเก็บวันเดิมไว้ ผลเก่า Legacy มาจาก source/วันที่ของรอบเก่า จึงไม่ใช่ Flow-only causal comparison

ระบบจองกำหนด controlled unavailable เช่น Full เดิม ไม่มี occupancy oracle ของลูกค้าจริง ไม่ใส่ fake data ลง common DB ไม่ติดตั้ง candidate ทับ R78

Legacy อ่านคำตอบและเกณฑ์เดิมจาก evidence.sqlite แบบ read-only ไม่มีการเรียก Flow เดิมซ้ำ ตรวจ literal definition กับ saved R89 cohort ครบ และคะแนน strict เมื่อใช้ checker กับ saved answer ตรง 4,301/5,643 grades ก่อนเริ่ม

ผลก่อนจบเป็นผลบางส่วนเท่านั้น รายงานสุดท้ายจะอยู่ analysis/REPORT_TH.md หลัง TEST_COMPLETE.json ยืนยันครบ 2,108 keys / 5,643 grades และ hash/source/model ผ่าน

## ทุกหมวดเดิม

| หมวด | Full | เลือก | ไทย | อังกฤษ | auto |
|---|---:|---:|---:|---:|---:|
| ["clarification", "games", "equipment", "service_fee", "reservation", "no_answer"] | 14 | 2 | 0 | 2 | 0 |
| ["equipment", "clarification"] | 4 | 1 | 0 | 1 | 0 |
| ["equipment", "games"] | 16 | 2 | 0 | 2 | 0 |
| ["games", "clarification", "no_answer"] | 13 | 2 | 0 | 2 | 0 |
| ["games", "clarification"] | 12 | 2 | 0 | 2 | 0 |
| ["games", "multi_question"] | 6 | 1 | 0 | 1 | 0 |
| ["games", "no_answer"] | 11 | 2 | 0 | 2 | 0 |
| ["games", "reservation"] | 49 | 5 | 0 | 5 | 0 |
| ["general", "knowledge"] | 241 | 25 | 0 | 25 | 0 |
| ["members", "overview"] | 47 | 5 | 0 | 5 | 0 |
| ["multi_question", "reservation", "games", "equipment"] | 51 | 6 | 0 | 6 | 0 |
| ["no_answer", "games", "general"] | 10 | 1 | 0 | 1 | 0 |
| ["rules", "penalty"] | 4 | 1 | 0 | 1 | 0 |
| ["schedule", "reservation"] | 10 | 1 | 0 | 1 | 0 |
| age_scope | 1 | 1 | 1 | 0 | 0 |
| alcohol_bringing_scope | 1 | 1 | 0 | 1 | 0 |
| alcohol_rule | 2 | 1 | 0 | 1 | 0 |
| all_games_scope | 2 | 1 | 0 | 1 | 0 |
| ambiguity | 2 | 1 | 0 | 0 | 1 |
| ambiguity_no_answer | 24 | 3 | 0 | 0 | 3 |
| ambiguous_controls | 6 | 1 | 0 | 0 | 1 |
| availability_game | 165 | 17 | 0 | 0 | 17 |
| availability_machine_split | 4 | 1 | 0 | 0 | 1 |
| availability_service | 23 | 3 | 0 | 0 | 3 |
| booking | 99 | 10 | 0 | 8 | 2 |
| booking_days_hours | 100 | 10 | 5 | 5 | 0 |
| booking_required | 2 | 1 | 0 | 1 | 0 |
| broad_eligibility | 3 | 1 | 1 | 0 | 0 |
| clarification | 31 | 4 | 0 | 4 | 0 |
| clarification_no_answer | 15 | 2 | 0 | 2 | 0 |
| competition | 115 | 12 | 4 | 8 | 0 |
| competition_rules | 1272 | 128 | 31 | 66 | 31 |
| composite | 96 | 10 | 5 | 5 | 0 |
| compound | 89 | 9 | 0 | 0 | 9 |
| compound_context_boundary | 642 | 65 | 34 | 31 | 0 |
| contact | 17 | 2 | 0 | 1 | 1 |
| control | 16 | 2 | 1 | 1 | 0 |
| damage_responsibility | 100 | 10 | 5 | 5 | 0 |
| document_facet | 1 | 1 | 1 | 0 | 0 |
| equipment | 1047 | 105 | 44 | 53 | 8 |
| equipment_access_trap | 100 | 10 | 5 | 5 | 0 |
| equipment_game_inside | 77 | 8 | 0 | 0 | 8 |
| fee_vs_access | 1 | 1 | 1 | 0 | 0 |
| fee_vs_booking | 1 | 1 | 1 | 0 | 0 |
| fee_without_service | 100 | 10 | 5 | 5 | 0 |
| food_at_desk | 1 | 1 | 0 | 1 | 0 |
| food_bring | 2 | 1 | 0 | 1 | 0 |
| food_bring_scope | 100 | 10 | 5 | 5 | 0 |
| food_consume | 1 | 1 | 1 | 0 | 0 |
| food_consumption | 100 | 10 | 5 | 5 | 0 |
| game_controls | 1768 | 177 | 73 | 69 | 35 |
| game_detail | 1138 | 114 | 53 | 59 | 2 |
| game_rules | 84 | 9 | 0 | 0 | 9 |
| games | 918 | 92 | 0 | 73 | 19 |
| games_catalog_availability | 1428 | 143 | 68 | 75 | 0 |
| games_list | 18 | 2 | 0 | 0 | 2 |
| general | 2 | 1 | 0 | 0 | 1 |
| general_llm | 275 | 28 | 0 | 0 | 28 |
| greeting | 23 | 3 | 0 | 0 | 3 |
| group_rate_without_service | 1 | 1 | 0 | 1 | 0 |
| identity | 16 | 2 | 0 | 0 | 2 |
| identity_compound | 7 | 1 | 0 | 0 | 1 |
| identity_typo | 100 | 10 | 5 | 5 | 0 |
| input_quality | 4 | 1 | 0 | 1 | 0 |
| knowledge | 2 | 1 | 0 | 0 | 1 |
| live_availability | 16 | 2 | 0 | 2 | 0 |
| live_booking | 966 | 97 | 48 | 49 | 0 |
| live_schedule | 12 | 2 | 0 | 2 | 0 |
| members | 70 | 7 | 0 | 1 | 6 |
| members_about_contact | 25 | 3 | 0 | 3 | 0 |
| members_overview_contact | 646 | 65 | 33 | 32 | 0 |
| membership_facet | 2 | 1 | 0 | 1 | 0 |
| multi_question | 33 | 4 | 0 | 4 | 0 |
| multi_studio_rules | 1 | 1 | 0 | 1 | 0 |
| no_answer | 1 | 1 | 0 | 0 | 1 |
| offsite_scope | 2 | 1 | 0 | 1 | 0 |
| out_of_scope | 107 | 11 | 0 | 1 | 10 |
| outsider_eligibility | 100 | 10 | 5 | 5 | 0 |
| overview | 25 | 3 | 0 | 2 | 1 |
| penalty | 4 | 1 | 0 | 0 | 1 |
| personal_power | 3 | 1 | 0 | 1 | 0 |
| play_booking_controls | 89 | 9 | 0 | 0 | 9 |
| policy_schedule_rules | 6 | 1 | 0 | 0 | 1 |
| price | 18 | 2 | 0 | 0 | 2 |
| protected | 13 | 2 | 0 | 0 | 2 |
| rag_knowledge | 25 | 3 | 0 | 3 | 0 |
| reservation | 53 | 6 | 0 | 2 | 4 |
| reservation_policy | 1162 | 117 | 60 | 57 | 0 |
| return_equipment_rule | 1 | 1 | 0 | 1 | 0 |
| rules | 18 | 2 | 0 | 1 | 1 |
| rules_penalty | 45 | 5 | 0 | 5 | 0 |
| schedule | 98 | 10 | 0 | 6 | 4 |
| schedule_calendar | 864 | 87 | 44 | 43 | 0 |
| service_fee | 1530 | 153 | 48 | 76 | 29 |
| single | 168 | 17 | 8 | 9 | 0 |
| social | 24 | 3 | 0 | 0 | 3 |
| student_only_boundary | 1 | 1 | 0 | 1 | 0 |
| studio_rules_penalties | 866 | 87 | 43 | 44 | 0 |
| time_vs_access | 2 | 1 | 0 | 1 | 0 |
| unclassified | 2725 | 273 | 137 | 136 | 0 |
| unclear_or_outside_scope | 100 | 10 | 5 | 5 | 0 |
| visit_only_fee | 2 | 1 | 0 | 1 | 0 |
| visitor_fee | 1 | 1 | 0 | 1 | 0 |
| weekday_live_slots | 100 | 10 | 5 | 5 | 0 |
