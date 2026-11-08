# ผลทดสอบ Flow ใหม่ R95 / Common + LLM ON

รันครบ 240 request keys / 657 grades ไม่รัน legacy หรือ common เก่าซ้ำ ใช้ผล R88 ที่เก็บไว้เปรียบเทียบ

## คะแนนและขอบเขต

- Positive text/clause contracts: **246/326 (75.46%)**; retained R88: 242/326 (74.23%)
- Strict: 52/657 (7.91%); protocol-only failures 394 grades ไม่ใช่ semantic accuracy
- Execution exceptions 0; empty answers 0; improved grades 4; regressed grades 0
- Requests ผ่านทุก positive contract ที่มี: 77/111 (69.37%)
- Local-model HTTP attempts 89, response opened 78, open failures 11; ไม่ใช้ transport เป็นความถูกต้องเนื้อหา

## แยกภาษา

| Locale | Requests | R95 positive | Retained R88 positive |
|---|---:|---:|---:|
| auto | 26 | 18/27 (66.67%) | 18/27 (66.67%) |
| en | 120 | 93/123 (75.61%) | 89/123 (72.36%) |
| th | 94 | 135/176 (76.70%) | 135/176 (76.70%) |

## เทียบกับ R93 บนคำถามเดียวกัน

{
  "positive_checked": 26,
  "current_passed": 23,
  "r93_passed": 23,
  "improved": 0,
  "regressed": 0
}

ตัวเลข cohort นี้แยกจาก full corpus ไม่เทียบคะแนน sample กับ full ตรง ๆ

## หมวดที่ยังไม่ผ่าน positive contracts

| Domain label | Requests | R95 | R88 |
|---|---:|---:|---:|
| service_fee | 17 | 2/27 (7.41%) | 2/27 (7.41%) |
| games_catalog_availability | 24 | 41/53 (77.36%) | 37/53 (69.81%) |
| schedule_calendar | 8 | 8/17 (47.06%) | 8/17 (47.06%) |
| game_controls | 25 | 73/78 (93.59%) | 73/78 (93.59%) |
| compound_context_boundary | 4 | 5/9 (55.56%) | 5/9 (55.56%) |
| reservation_policy | 16 | 9/13 (69.23%) | 9/13 (69.23%) |
| equipment | 9 | 8/11 (72.73%) | 8/11 (72.73%) |
| general_llm | 3 | 0/3 (0.00%) | 0/3 (0.00%) |
| food_consumption | 1 | 0/2 (0.00%) | 0/2 (0.00%) |
| damage_responsibility | 3 | 4/6 (66.67%) | 4/6 (66.67%) |
| competition_rules | 14 | 2/4 (50.00%) | 2/4 (50.00%) |
| game_detail | 12 | 38/40 (95.00%) | 38/40 (95.00%) |
| unclassified | 36 | 5/6 (83.33%) | 5/6 (83.33%) |
| studio_rules_penalties | 10 | 9/10 (90.00%) | 9/10 (90.00%) |
| games | 10 | 2/3 (66.67%) | 2/3 (66.67%) |
| visitor_fee | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| schedule | 1 | 2/3 (66.67%) | 2/3 (66.67%) |
| single | 2 | 1/2 (50.00%) | 1/2 (50.00%) |
| competition | 2 | 0/1 (0.00%) | 0/1 (0.00%) |
| live_booking | 11 | 4/4 (100.00%) | 4/4 (100.00%) |
| availability_game | 2 | 2/2 (100.00%) | 2/2 (100.00%) |
| members_overview_contact | 7 | 20/20 (100.00%) | 20/20 (100.00%) |
| members | 1 | 2/2 (100.00%) | 2/2 (100.00%) |
| weekday_live_slots | 3 | 6/6 (100.00%) | 6/6 (100.00%) |
| composite | 1 | 1/1 (100.00%) | 1/1 (100.00%) |
| booking_days_hours | 1 | 2/2 (100.00%) | 2/2 (100.00%) |

## เส้นทางที่ใช้งานจริง

{
  "deterministic:typed_action": 22,
  "guard_or_dispatcher": 52,
  "deterministic:typed_platform": 2,
  "compatibility_common_domain": 137,
  "deterministic:typed_directory": 4,
  "semantic:bounded_task_contract": 6,
  "deterministic:typed_overview": 2,
  "deterministic:typed_offering": 1,
  "deterministic:whole_task_contract": 9,
  "deterministic:typed_how_to": 3,
  "deterministic:typed_equipment_explain": 1,
  "deterministic:typed_equipment_list": 1
}

compatibility_common_domain หมายถึงยังใช้ parser เฉพาะหมวดของ common ผ่าน executor ร่วม ไม่อ้างว่าทุกหมวดถูกแทนด้วย semantic TaskPlan แล้ว

## ข้อจำกัด

- Positive literal/clause checks do not establish full semantic accuracy.
- Raw strict contracts include legacy protocol identifiers.
- Controlled booking unavailable: no real occupancy oracle.
- Reference clock 2026-10-16 with per-job overrides, not current live truth.
- Full corpus contains single-turn requests; multi-turn fixtures reported separately.
- Model response opened does not establish body/semantic success.

รายละเอียดทุกคำถามอยู่ PER_REQUEST_ANALYSIS.jsonl พร้อม query plan, rejected candidate และผลตรวจดิบ การจัด semantic root causes ต้องอ่านสาระ/ต้นฉบับเพิ่ม ไม่เรียกทุก literal failure ว่าคำตอบผิดข้อเท็จจริง
