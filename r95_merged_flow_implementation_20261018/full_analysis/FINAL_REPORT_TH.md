# ผลทดสอบ Flow ใหม่ R95 / Common + LLM ON

รันครบ 20,554 request keys / 55,811 grades ไม่รัน legacy หรือ common เก่าซ้ำ ใช้ผล R88 ที่เก็บไว้เปรียบเทียบ

## คะแนนและขอบเขต

- Positive text/clause contracts: **18,579/24,909 (74.59%)**; retained R88: 17,960/24,909 (72.10%)
- Strict: 5,030/55,811 (9.01%); protocol-only failures 33038 grades ไม่ใช่ semantic accuracy
- Execution exceptions 0; empty answers 0; improved grades 783; regressed grades 164
- Requests ผ่านทุก positive contract ที่มี: 6,162/8,907 (69.18%)
- Local-model HTTP attempts 7492, response opened 7470, open failures 22; ไม่ใช้ transport เป็นความถูกต้องเนื้อหา

## แยกภาษา

| Locale | Requests | R95 positive | Retained R88 positive |
|---|---:|---:|---:|
| auto | 2475 | 1,617/2,301 (70.27%) | 1,585/2,301 (68.88%) |
| en | 10235 | 6,755/9,466 (71.36%) | 6,701/9,466 (70.79%) |
| th | 7844 | 10,207/13,142 (77.67%) | 9,674/13,142 (73.61%) |

## เทียบกับ R93 บนคำถามเดียวกัน

{
  "positive_checked": 1140,
  "current_passed": 795,
  "r93_passed": 765,
  "improved": 40,
  "regressed": 10
}

ตัวเลข cohort นี้แยกจาก full corpus ไม่เทียบคะแนน sample กับ full ตรง ๆ

## หมวดที่ยังไม่ผ่าน positive contracts

| Domain label | Requests | R95 | R88 |
|---|---:|---:|---:|
| service_fee | 1530 | 705/2,331 (30.24%) | 705/2,331 (30.24%) |
| game_detail | 1138 | 2,180/3,196 (68.21%) | 2,121/3,196 (66.36%) |
| games_catalog_availability | 1428 | 2,127/2,614 (81.37%) | 1,767/2,614 (67.60%) |
| reservation_policy | 1162 | 1,060/1,458 (72.70%) | 1,079/1,458 (74.01%) |
| compound_context_boundary | 642 | 510/878 (58.09%) | 510/878 (58.09%) |
| equipment | 1047 | 1,837/2,181 (84.23%) | 1,618/2,181 (74.19%) |
| schedule_calendar | 864 | 820/1,162 (70.57%) | 858/1,162 (73.84%) |
| game_controls | 1768 | 5,125/5,349 (95.81%) | 5,077/5,349 (94.91%) |
| unclassified | 2725 | 217/440 (49.32%) | 220/440 (50.00%) |
| general_llm | 275 | 55/275 (20.00%) | 54/275 (19.64%) |
| studio_rules_penalties | 866 | 855/1,038 (82.37%) | 877/1,038 (84.49%) |
| booking_days_hours | 100 | 42/200 (21.00%) | 42/200 (21.00%) |
| members_overview_contact | 646 | 1,292/1,400 (92.29%) | 1,301/1,400 (92.93%) |
| games | 918 | 291/398 (73.12%) | 280/398 (70.35%) |
| damage_responsibility | 100 | 104/200 (52.00%) | 104/200 (52.00%) |
| single | 168 | 88/168 (52.38%) | 90/168 (53.57%) |
| composite | 96 | 51/96 (53.12%) | 51/96 (53.12%) |
| food_consumption | 100 | 156/200 (78.00%) | 162/200 (81.00%) |
| competition_rules | 1272 | 112/152 (73.68%) | 123/152 (80.92%) |
| competition | 115 | 0/35 (0.00%) | 0/35 (0.00%) |
| booking | 99 | 34/56 (60.71%) | 34/56 (60.71%) |
| ambiguity_no_answer | 24 | 28/48 (58.33%) | 28/48 (58.33%) |
| schedule | 98 | 49/68 (72.06%) | 50/68 (73.53%) |
| members_about_contact | 25 | 6/25 (24.00%) | 10/25 (40.00%) |
| weekday_live_slots | 100 | 188/200 (94.00%) | 190/200 (95.00%) |
| reservation | 53 | 34/45 (75.56%) | 35/45 (77.78%) |
| rules_penalty | 45 | 35/46 (76.09%) | 35/46 (76.09%) |
| availability_service | 23 | 15/23 (65.22%) | 12/23 (52.17%) |
| compound | 89 | 98/105 (93.33%) | 100/105 (95.24%) |
| clarification_no_answer | 15 | 0/6 (0.00%) | 0/6 (0.00%) |
| availability_game | 165 | 160/165 (96.97%) | 123/165 (74.55%) |
| broad_eligibility | 3 | 0/3 (0.00%) | 0/3 (0.00%) |
| personal_power | 3 | 0/3 (0.00%) | 0/3 (0.00%) |
| live_booking | 966 | 176/178 (98.88%) | 176/178 (98.88%) |
| alcohol_rule | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| multi_question | 33 | 0/2 (0.00%) | 0/2 (0.00%) |
| policy_schedule_rules | 6 | 4/6 (66.67%) | 4/6 (66.67%) |
| overview | 25 | 3/5 (60.00%) | 3/5 (60.00%) |
| all_games_scope | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| membership_facet | 2 | 0/2 (0.00%) | 1/2 (50.00%) |
| visit_only_fee | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| booking_required | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| ambiguity | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| offsite_scope | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| food_bring | 2 | 0/2 (0.00%) | 0/2 (0.00%) |
| penalty | 4 | 1/2 (50.00%) | 1/2 (50.00%) |
| visitor_fee | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| group_rate_without_service | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| food_at_desk | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| return_equipment_rule | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| time_vs_access | 2 | 0/1 (0.00%) | 0/1 (0.00%) |
| knowledge | 2 | 0/1 (0.00%) | 0/1 (0.00%) |
| no_answer | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| fee_vs_access | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| ambiguous_controls | 6 | 5/6 (83.33%) | 5/6 (83.33%) |
| alcohol_bringing_scope | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| general | 2 | 0/1 (0.00%) | 0/1 (0.00%) |
| multi_studio_rules | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| document_facet | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| fee_vs_booking | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| student_only_boundary | 1 | 0/1 (0.00%) | 0/1 (0.00%) |
| members | 70 | 108/108 (100.00%) | 108/108 (100.00%) |
| rules | 18 | 2/2 (100.00%) | 0/2 (0.00%) |
| availability_machine_split | 4 | 4/4 (100.00%) | 4/4 (100.00%) |
| age_scope | 1 | 1/1 (100.00%) | 1/1 (100.00%) |
| food_consume | 1 | 1/1 (100.00%) | 1/1 (100.00%) |

## เส้นทางที่ใช้งานจริง

{
  "compatibility_common_domain": 11632,
  "deterministic:typed_action": 1676,
  "deterministic:whole_task_contract": 875,
  "guard_or_dispatcher": 4452,
  "deterministic:typed_overview": 323,
  "deterministic:typed_how_to": 74,
  "deterministic:typed_equipment_explain": 186,
  "deterministic:typed_operator": 13,
  "deterministic:typed_schema_attributes": 281,
  "deterministic:typed_offering": 325,
  "semantic:bounded_task_contract": 234,
  "typed_rental_adapter": 5,
  "deterministic:typed_platform": 127,
  "deterministic:typed_duration": 27,
  "deterministic:typed_directory": 63,
  "deterministic:typed_location": 27,
  "typed_calendar_adapter": 41,
  "deterministic:typed_equipment_location": 113,
  "deterministic:typed_capacity": 40,
  "deterministic:typed_contact": 33,
  "deterministic:typed_specs": 4,
  "deterministic:typed_version": 2,
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
