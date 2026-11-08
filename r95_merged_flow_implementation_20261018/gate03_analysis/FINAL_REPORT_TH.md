# ผลทดสอบ Flow ใหม่ R95 / Common + LLM ON

รันครบ 80 request keys / 231 grades ไม่รัน legacy หรือ common เก่าซ้ำ ใช้ผล R88 ที่เก็บไว้เปรียบเทียบ

## คะแนนและขอบเขต

- Positive text/clause contracts: **87/120 (72.50%)**; retained R88: 87/120 (72.50%)
- Strict: 18/231 (7.79%); protocol-only failures 125 grades ไม่ใช่ semantic accuracy
- Execution exceptions 0; empty answers 0; improved grades 0; regressed grades 0
- Requests ผ่านทุก positive contract ที่มี: 26/40 (65.00%)
- Local-model HTTP attempts 29, response opened 29, open failures 0; ไม่ใช้ transport เป็นความถูกต้องเนื้อหา

## แยกภาษา

| Locale | Requests | R95 positive | Retained R88 positive |
|---|---:|---:|---:|
| auto | 8 | 6/10 (60.00%) | 6/10 (60.00%) |
| en | 43 | 35/47 (74.47%) | 35/47 (74.47%) |
| th | 29 | 46/63 (73.02%) | 46/63 (73.02%) |

## เทียบกับ R93 บนคำถามเดียวกัน

{
  "positive_checked": 13,
  "current_passed": 11,
  "r93_passed": 11,
  "improved": 0,
  "regressed": 0
}

ตัวเลข cohort นี้แยกจาก full corpus ไม่เทียบคะแนน sample กับ full ตรง ๆ

## หมวดที่ยังไม่ผ่าน positive contracts

| Domain label | Requests | R95 | R88 |
|---|---:|---:|---:|
| service_fee | 7 | 0/10 (0.00%) | 0/10 (0.00%) |
| games_catalog_availability | 4 | 0/7 (0.00%) | 0/7 (0.00%) |
| reservation_policy | 6 | 0/4 (0.00%) | 0/4 (0.00%) |
| compound_context_boundary | 2 | 5/9 (55.56%) | 5/9 (55.56%) |
| food_consumption | 1 | 0/2 (0.00%) | 0/2 (0.00%) |
| equipment | 3 | 3/5 (60.00%) | 3/5 (60.00%) |
| studio_rules_penalties | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| unclassified | 16 | 3/4 (75.00%) | 3/4 (75.00%) |
| schedule | 1 | 2/3 (66.67%) | 2/3 (66.67%) |
| general_llm | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| members_overview_contact | 2 | 10/10 (100.00%) | 10/10 (100.00%) |
| game_detail | 4 | 13/13 (100.00%) | 13/13 (100.00%) |
| weekday_live_slots | 1 | 2/2 (100.00%) | 2/2 (100.00%) |
| schedule_calendar | 2 | 8/8 (100.00%) | 8/8 (100.00%) |
| game_controls | 11 | 36/36 (100.00%) | 36/36 (100.00%) |
| members | 1 | 2/2 (100.00%) | 2/2 (100.00%) |
| damage_responsibility | 1 | 2/2 (100.00%) | 2/2 (100.00%) |
| availability_game | 1 | 1/1 (100.00%) | 1/1 (100.00%) |

## เส้นทางที่ใช้งานจริง

{
  "guard_or_dispatcher": 19,
  "compatibility_common_domain": 40,
  "deterministic:typed_directory": 2,
  "deterministic:whole_task_contract": 4,
  "deterministic:typed_action": 10,
  "deterministic:typed_schema_attributes": 1,
  "deterministic:typed_equipment_location": 1,
  "semantic:bounded_task_contract": 2,
  "deterministic:typed_platform": 1
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
