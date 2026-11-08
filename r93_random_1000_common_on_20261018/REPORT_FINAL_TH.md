# ผลสุ่ม 1,000 คำถามจากชุดใหญ่ — Format กลาง R92 / เปิด LLM

รันครบ 1,000 request keys ไม่ซ้ำจาก 20,554 ข้อ รวม 2609 grades ใช้ seed `psu-r93-1000-20261018-v1` ไม่มีการสุ่มใหม่ตามผลผ่าน/ผิด

ชุดหลัก 1,000 requests มีข้อความไม่ซ้ำ 998 ข้อ เพราะมี 2 ข้อความที่ใช้ locale ต่างกัน เก็บผลเดิมไว้ครบเพื่อเทียบ R88 และเพิ่มอีก 2 ข้อความใหม่แยกเป็น supplement รวมเป็น 1,000 ข้อความไม่ซ้ำ / 1,002 requests ตารางคะแนนด้านล่างใช้ชุดหลักเดิม 1,000 requests ไม่คัดผลผ่าน/ผิดออก รายละเอียด supplement อยู่ใน SUPPLEMENT_ANALYSIS.json

## ผลหลัก

- ผ่าน positive content contracts: **765/1,140 (67.11%)**; common R88 ที่บันทึกไว้สำหรับข้อเดียวกัน: 758/1,140 (66.49%)
- ผ่าน strict contracts เดิม: 248/2,609 (9.51%); R88: 248/2,609 (9.51%)
- ผ่าน positive contracts ทุกข้อที่ผูกกับคำถาม: 264/439 (60.14%); คำถามที่ไม่มี positive assertion ไม่ถูกนับเป็นคำตอบถูกทางความหมาย
- Positive grades ดีขึ้น 7 และแย่ลง 0 เทียบผล R88 ของข้อเดียวกัน
- ไม่ผ่านเฉพาะ protocol 1497 grades; execution exceptions 0 requests; grader errors 0 grades

## แยกภาษา requested locale

| ภาษา | คำถาม | Positive content R92 | Positive content R88 | Strict R92 |
|---|---:|---:|---:|---:|
| auto | 140 | 79/124 (63.71%) | 77/124 (62.10%) | 25/203 (12.32%) |
| en | 496 | 240/409 (58.68%) | 240/409 (58.68%) | 123/1,249 (9.85%) |
| th | 364 | 446/607 (73.48%) | 441/607 (72.65%) | 100/1,157 (8.64%) |

## หมวดที่มี positive contracts

| หมวดจาก corpus | คำถาม | R92 | R88 |
|---|---:|---:|---:|
| service_fee | 66 | 20/94 (21.28%) | 20/94 (21.28%) |
| game_detail | 50 | 85/154 (55.19%) | 84/154 (54.55%) |
| games_catalog_availability | 61 | 94/132 (71.21%) | 94/132 (71.21%) |
| equipment | 46 | 53/88 (60.23%) | 53/88 (60.23%) |
| reservation_policy | 49 | 44/59 (74.58%) | 40/59 (67.80%) |
| studio_rules_penalties | 38 | 26/40 (65.00%) | 26/40 (65.00%) |
| compound_context_boundary | 29 | 28/37 (75.68%) | 28/37 (75.68%) |
| game_controls | 75 | 222/231 (96.10%) | 222/231 (96.10%) |
| general_llm | 12 | 3/12 (25.00%) | 3/12 (25.00%) |
| unclassified | 114 | 10/19 (52.63%) | 10/19 (52.63%) |
| booking_days_hours | 6 | 4/12 (33.33%) | 4/12 (33.33%) |
| damage_responsibility | 6 | 4/12 (33.33%) | 4/12 (33.33%) |
| members_overview_contact | 29 | 45/53 (84.91%) | 45/53 (84.91%) |
| schedule_calendar | 38 | 33/39 (84.62%) | 33/39 (84.62%) |
| games | 40 | 8/12 (66.67%) | 8/12 (66.67%) |
| schedule | 6 | 0/4 (0.00%) | 0/4 (0.00%) |
| single | 8 | 4/8 (50.00%) | 4/8 (50.00%) |
| composite | 6 | 3/6 (50.00%) | 3/6 (50.00%) |
| alcohol_rule | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| all_games_scope | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| ambiguity_no_answer | 2 | 2/4 (50.00%) | 2/4 (50.00%) |
| availability_game | 8 | 6/8 (75.00%) | 6/8 (75.00%) |
| availability_service | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| booking | 6 | 2/4 (50.00%) | 2/4 (50.00%) |
| booking_required | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| broad_eligibility | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| competition | 7 | 0/2 (0.00%) | 0/2 (0.00%) |
| competition_rules | 55 | 7/9 (77.78%) | 7/9 (77.78%) |
| food_bring | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| offsite_scope | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| personal_power | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| visit_only_fee | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| alcohol_bringing_scope | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| ambiguity | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| clarification_no_answer | 2 | 0/1 (0.00%) | 0/1 (0.00%) |
| document_facet | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| fee_vs_access | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| fee_vs_booking | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| food_at_desk | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| general | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| group_rate_without_service | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| knowledge | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| members_about_contact | 2 | 1/2 (50.00%) | 1/2 (50.00%) |
| membership_facet | 2 | 1/2 (50.00%) | 1/2 (50.00%) |
| multi_question | 3 | 0/1 (0.00%) | 0/1 (0.00%) |
| multi_studio_rules | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| no_answer | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| reservation | 4 | 2/3 (66.67%) | 2/3 (66.67%) |
| return_equipment_rule | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| rules_penalty | 3 | 2/3 (66.67%) | 2/3 (66.67%) |
| student_only_boundary | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| time_vs_access | 2 | 0/1 (0.00%) | 0/1 (0.00%) |
| visitor_fee | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| age_scope | 1 | 1/1 (100.00%) | 1/1 (100.00%) |
| ambiguous_controls | 1 | 1/1 (100.00%) | 1/1 (100.00%) |
| availability_machine_split | 1 | 1/1 (100.00%) | 1/1 (100.00%) |
| compound | 5 | 5/5 (100.00%) | 5/5 (100.00%) |
| food_consume | 1 | 1/1 (100.00%) | 1/1 (100.00%) |
| food_consumption | 6 | 12/12 (100.00%) | 12/12 (100.00%) |
| live_booking | 42 | 12/12 (100.00%) | 12/12 (100.00%) |
| members | 5 | 8/8 (100.00%) | 8/8 (100.00%) |
| policy_schedule_rules | 1 | 1/1 (100.00%) | 1/1 (100.00%) |
| rules | 3 | 2/2 (100.00%) | 0/2 (0.00%) |
| weekday_live_slots | 6 | 12/12 (100.00%) | 12/12 (100.00%) |

## สัญญาณวินิจฉัยจาก trace — นับคำถาม และทับซ้อนกันได้

```json
{
  "known_subject_unresolved_task": 101,
  "semantic_unverified_intent": 125,
  "unresolved_clause_veto": 35,
  "controlled_live_no_occupancy_oracle": 53,
  "not_current_needs_validity_review": 48,
  "english_thai_prose_flag_requires_review": 28,
  "model_http_open_failure": 1,
  "model_availability_or_body_failure": 1
}
```

known_subject_unresolved_task หมายถึงพบ target แต่ field/task ยังไม่ลงตัว; semantic_unverified_intent หมายถึง guard ไม่รับ intent ของแผน; not_current ต้องตรวจ validity และ oracle ประกอบ ไม่ถือว่าผิดหรือถูกโดยอัตโนมัติ

## LLM และเวลา

- Model preflight สร้าง response จบแล้วก่อนเริ่มชุดสุ่ม เปิดสิทธิ์ LLM ทุกคำถาม แต่ typed paths ไม่จำเป็นต้องเรียกโมเดล
- HTTP model attempts 220, response opened 219, open failures 1 — response opened เป็นหลักฐานระดับเปิด HTTP ไม่รับรอง body/schema/เนื้อหา
- Distinct audit records ต่อ request: schema accepted 213, accepted plans 32; audit records ไม่เท่ากับจำนวน model calls
- p50 0.48s / p95 2.97s / p99 4.25s; รวมการตรวจเกณฑ์และข้อจำกัดคิวสอง workers ไม่ใช่เวลาตอบผู้ใช้พร้อมกันที่รับรอง

## ขอบเขตการแปลผล

- เป็นการสุ่มแบบกระจาย locale/domain อย่างน้อยหนึ่งต่อ 156 cells; rare cells ถูกเพิ่มสัดส่วนเพื่อ coverage คะแนน sample จึงไม่ใช่ estimate แบบ simple-random ของทั้ง population
- ใช้วันอ้างอิงเดิม 16 ต.ค. 2026 และ per-job dates ตาม corpus เพื่อเทียบ retained R88; ไม่เลื่อนเวลาให้ราคาเก่ากลับมามีผล
- Booking provider เป็น controlled unavailable เหมือน R88 ไม่มี live occupancy oracle จึงไม่ใช้คะแนนนี้วินิจฉัยความถูกต้อง WordPress สด
- ทั้ง 1,000 เป็น single-turn เพราะ corpus jobs ไม่มี history ไม่รับรอง multi-turn ทั้งระบบจากชุดนี้
- Positive literal/complete-clause contracts ยังอาจมี false mismatch จากคำแปลหรือสำนวน และบาง contract อ่อนเกินตรวจทุก claim; strict รวม route/mode/source protocol เดิม ไม่ใช่ semantic accuracy
- ไม่แก้ code/data/approval ระหว่างรัน และไม่รัน Flow เดิมซ้ำ

## หลักฐาน

- [ผลตัวเลขทั้งหมด](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/ANALYSIS_FINAL.json>)
- [วิเคราะห์ทุกคำถามและเกณฑ์ที่พลาด](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/PER_REQUEST_ANALYSIS.jsonl>)
- [ตัวอย่างพร้อม old/new answers และ plans](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/EXAMPLE_CASES.json>)
- [จำนวนเหตุที่ไม่ผ่านทั้งหมด](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/FAILURE_COUNTS.json>)
- [สัดส่วนการสุ่มและ seed](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/SAMPLE_ALLOCATION.json>)
- [รายการโจทย์ที่สุ่ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/SELECTED_JOBS.jsonl>)
- [ผลดิบ worker 0](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/sample01/RESULTS_0.jsonl.gz>)
- [ผลดิบ worker 1](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/sample01/RESULTS_1.jsonl.gz>)

## วิเคราะห์เคสและ coverage เพิ่มเติม

- [วิเคราะห์ตัวอย่างแบบเจาะสาเหตุ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/CASE_REVIEW_TH.md>)
- [ผลสองข้อความเพิ่ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/SUPPLEMENT_ANALYSIS.json>)
- [ยืนยันจำนวนคำขอและข้อความไม่ซ้ำ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/COVERAGE_COMPLETE.json>)

- [แยก model transport failure](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/MODEL_TRANSPORT_FAILURES.json>)
