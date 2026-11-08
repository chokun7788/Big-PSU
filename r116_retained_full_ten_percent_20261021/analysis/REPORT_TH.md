# R116 — 10% ของแต่ละหมวดใน Full เดิม เทียบ Legacy กับ R115

ใช้คำถามจากชุด Full เดิม R64 ที่เคยทดสอบจริง ครบ 2,108 request keys (5,643 oracle rows) จากประชากร 20,554 คำขอ สุ่มตาม seed โดยหมวดเดิม 104 กลุ่มได้ ceil(10% × จำนวนกลุ่ม) ทุกกลุ่ม ไม่เลือกจากผลผ่าน/ไม่ผ่าน ไม่สร้างคำถามแทนชุด Full

## สรุปคะแนนบนคำถามและเกณฑ์เดียวกัน

| เกณฑ์ | Legacy R64 ผลที่เก็บไว้ | R115 ผ่าน API จริง LLM ON |
|---|---:|---:|
| Positive literal/clause grades | 2,370/2,517 (94.16%) | 1,709/2,517 (67.90%) |
| คำขอที่ผ่าน positive ทุกแถวที่ผูกไว้ | 842/921 (91.42%) | 562/921 (61.02%) |
| Strict รวม route/mode/status/evidence/เวลา | 4,301/5,643 (76.22%) | 183/5,643 (3.24%) |

Strict เป็น compatibility ตาม Flow เดิม ไม่ใช่คะแนนเนื้อหาล้วน ส่วน positive literal/clause เป็นคำ/ข้อความที่ oracle กำหนด ไม่ใช่ semantic accuracy จากมนุษย์ คำตอบที่ไม่ตรงคำอาจถูกความหมาย และการผ่านคำไม่รับรองว่าตอบครบทั้งเรื่อง

**ผลบน benchmark นี้:** R115 ยังต่ำกว่า Legacy ใน positive literal/clause 26.26 จุดเปอร์เซ็นต์บนเกณฑ์ชุดเดียวกัน ความต่างจึงไม่ได้มีแค่ชื่อ route แต่ยังต้องแยก literal/ภาษา/source-version gaps ออกจาก actual content failure รายกรณี

คะแนน 96.46% ใน R115 รอบก่อนเป็น source identity/value/state ของ 960 ข้อที่มี source ในชุดรายหมวด 1,400 ข้อ ไม่ใช่ metric หรือประชากรเดียวกับ Full sample รอบนี้ จึงใช้ตัวเลขนั้นแทนความสามารถบน Full เดิมไม่ได้ แม้ candidate code จะเป็นรุ่นเดียวกัน

## ภาษา requested — cohort คงที่

| ภาษา | คำขอ | Legacy positive grades | R115 positive grades |
|---|---:|---:|---:|
| th | 790 | 1,239/1,314 (94.29%) | 889/1,314 (67.66%) |
| en | 1056 | 936/962 (97.30%) | 649/962 (67.46%) |
| auto | 262 | 195/241 (80.91%) | 171/241 (70.95%) |

## Sampling และข้อจำกัดการเปรียบเทียบ

- ดึงจาก R88 SELECTED_JOBS ซึ่งตรวจแล้วว่าข้อความ/locale/reference_date/entries ตรงกับ R64 JOBS ทุก key ก่อนสุ่ม หมวดใช้ชื่อดั้งเดิม r70_stratum.domain รวม compound/noise/unclassified ไม่ย้ายชื่อหมวดให้คะแนนดูดี
- จำนวนเกิน 2,055 เล็กน้อยเพราะปัดขึ้นทุกหมวดเล็ก ไม่อ้างว่าเป็น 10.000% หรือผล Full ครบ 20,554 และไม่อ้าง blind holdout เพราะเป็น corpus ที่เคยใช้พัฒนาในโครงการ
- เป็น Full เดิมที่เคยใช้ทดสอบจริง แต่ตัวคลังรวมคำถามที่สร้าง/แปลง/ทำคำสะกดผิดสำหรับทดสอบ และบาง oracle มี review_status เป็น candidate ไม่ได้หมายความว่าทุกข้อเป็นคำถามลูกค้าจริงหรือเจ้าของตรวจยืนยันทุก expected แล้ว
- กระจาย locale ภายในแต่ละหมวดตามสัดส่วนด้วย largest remainder; ข้อความ/การสะกดผิด/เกณฑ์ทุกแถวคงเดิม เก็บ SAMPLE_ALLOCATION.json และ SELECTED_JOBS.jsonl
- Legacy อ่านผลจริงเดิมจาก evidence.sqlite แบบ read-only ไม่รัน Flow เดิมใหม่ ตรวจ definition positive กับผล R89 ครบทั้ง sample และ native strict บน saved output ตรงคะแนนเก่าก่อนเริ่มใหม่
- R115 ใช้ source รุ่นใหม่ จึงเปรียบเทียบผลการตอบภายใต้คนละ source/runtime ได้ แต่ความต่างไม่ใช่ causal effect ของ Flow ล้วน ๆ วันที่ปกติของรอบนี้ 2026-10-21; job ที่ระบุวันอ้างอิงเดิมเก็บ override เดิมครบ ส่วน baseline มีวันที่เดิมของรอบเก่า
- รัน serial ผ่าน /api/chat จริง เปิด LLM, session ใหม่ทุก key, ไม่มี category hint ไม่แก้ R115 ระหว่างทดสอบ จับ actual PipelineAnswer ตาม request_id เพื่อไม่เอาการซ่อน private source ใน HTTP มาปนเป็น source failure
- Booking เป็น controlled unavailable เช่น Full เดิม ไม่มีการยืนยัน occupancy ลูกค้าจริง และไม่ใส่ fake live/news data ลง native DB
- จำนวน grades ให้น้ำหนักคำถามที่มีหลาย oracle/หลายคลังมากกว่า จึงแสดงทั้งระดับ grade และระดับ request และไม่ตีความ missing-source/no-answer ว่าตอบเนื้อหาสำเร็จ

## หมวดเดิมทุกกลุ่ม — ตรวจ coverage 10%

| หมวดเดิม | ประชากร | สุ่ม | สัดส่วน | Legacy positive | R115 positive |
|---|---:|---:|---:|---:|---:|
| ["clarification", "games", "equipment", "service_fee", "reservation", "no_answer"] | 14 | 2 | 14.29% | 0/0 (N/A) | 0/0 (N/A) |
| ["equipment", "clarification"] | 4 | 1 | 25.00% | 0/0 (N/A) | 0/0 (N/A) |
| ["equipment", "games"] | 16 | 2 | 12.50% | 0/0 (N/A) | 0/0 (N/A) |
| ["games", "clarification", "no_answer"] | 13 | 2 | 15.38% | 0/0 (N/A) | 0/0 (N/A) |
| ["games", "clarification"] | 12 | 2 | 16.67% | 0/0 (N/A) | 0/0 (N/A) |
| ["games", "multi_question"] | 6 | 1 | 16.67% | 0/0 (N/A) | 0/0 (N/A) |
| ["games", "no_answer"] | 11 | 2 | 18.18% | 0/0 (N/A) | 0/0 (N/A) |
| ["games", "reservation"] | 49 | 5 | 10.20% | 0/0 (N/A) | 0/0 (N/A) |
| ["general", "knowledge"] | 241 | 25 | 10.37% | 0/0 (N/A) | 0/0 (N/A) |
| ["members", "overview"] | 47 | 5 | 10.64% | 0/0 (N/A) | 0/0 (N/A) |
| ["multi_question", "reservation", "games", "equipment"] | 51 | 6 | 11.76% | 0/0 (N/A) | 0/0 (N/A) |
| ["no_answer", "games", "general"] | 10 | 1 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| ["rules", "penalty"] | 4 | 1 | 25.00% | 0/0 (N/A) | 0/0 (N/A) |
| ["schedule", "reservation"] | 10 | 1 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| age_scope | 1 | 1 | 100.00% | 1/1 (100.00%) | 1/1 (100.00%) |
| alcohol_bringing_scope | 1 | 1 | 100.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| alcohol_rule | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| all_games_scope | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| ambiguity | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| ambiguity_no_answer | 24 | 3 | 12.50% | 6/6 (100.00%) | 4/6 (66.67%) |
| ambiguous_controls | 6 | 1 | 16.67% | 1/1 (100.00%) | 1/1 (100.00%) |
| availability_game | 165 | 17 | 10.30% | 17/17 (100.00%) | 16/17 (94.12%) |
| availability_machine_split | 4 | 1 | 25.00% | 1/1 (100.00%) | 1/1 (100.00%) |
| availability_service | 23 | 3 | 13.04% | 3/3 (100.00%) | 3/3 (100.00%) |
| booking | 99 | 10 | 10.10% | 4/4 (100.00%) | 3/4 (75.00%) |
| booking_days_hours | 100 | 10 | 10.00% | 20/20 (100.00%) | 8/20 (40.00%) |
| booking_required | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| broad_eligibility | 3 | 1 | 33.33% | 1/1 (100.00%) | 0/1 (0.00%) |
| clarification | 31 | 4 | 12.90% | 0/0 (N/A) | 0/0 (N/A) |
| clarification_no_answer | 15 | 2 | 13.33% | 0/0 (N/A) | 0/0 (N/A) |
| competition | 115 | 12 | 10.43% | 0/6 (0.00%) | 0/6 (0.00%) |
| competition_rules | 1272 | 128 | 10.06% | 4/20 (20.00%) | 14/20 (70.00%) |
| composite | 96 | 10 | 10.42% | 10/10 (100.00%) | 0/10 (0.00%) |
| compound | 89 | 9 | 10.11% | 10/10 (100.00%) | 10/10 (100.00%) |
| compound_context_boundary | 642 | 65 | 10.12% | 56/107 (52.34%) | 56/107 (52.34%) |
| contact | 17 | 2 | 11.76% | 0/0 (N/A) | 0/0 (N/A) |
| control | 16 | 2 | 12.50% | 0/0 (N/A) | 0/0 (N/A) |
| damage_responsibility | 100 | 10 | 10.00% | 18/20 (90.00%) | 8/20 (40.00%) |
| document_facet | 1 | 1 | 100.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| equipment | 1047 | 105 | 10.03% | 229/233 (98.28%) | 195/233 (83.69%) |
| equipment_access_trap | 100 | 10 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| equipment_game_inside | 77 | 8 | 10.39% | 0/0 (N/A) | 0/0 (N/A) |
| fee_vs_access | 1 | 1 | 100.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| fee_vs_booking | 1 | 1 | 100.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| fee_without_service | 100 | 10 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| food_at_desk | 1 | 1 | 100.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| food_bring | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| food_bring_scope | 100 | 10 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| food_consume | 1 | 1 | 100.00% | 1/1 (100.00%) | 1/1 (100.00%) |
| food_consumption | 100 | 10 | 10.00% | 20/20 (100.00%) | 16/20 (80.00%) |
| game_controls | 1768 | 177 | 10.01% | 550/555 (99.10%) | 477/555 (85.95%) |
| game_detail | 1138 | 114 | 10.02% | 283/289 (97.92%) | 179/289 (61.94%) |
| game_rules | 84 | 9 | 10.71% | 0/0 (N/A) | 0/0 (N/A) |
| games | 918 | 92 | 10.02% | 40/40 (100.00%) | 38/40 (95.00%) |
| games_catalog_availability | 1428 | 143 | 10.01% | 284/292 (97.26%) | 229/292 (78.42%) |
| games_list | 18 | 2 | 11.11% | 0/0 (N/A) | 0/0 (N/A) |
| general | 2 | 1 | 50.00% | 0/1 (0.00%) | 0/1 (0.00%) |
| general_llm | 275 | 28 | 10.18% | 3/28 (10.71%) | 7/28 (25.00%) |
| greeting | 23 | 3 | 13.04% | 0/0 (N/A) | 0/0 (N/A) |
| group_rate_without_service | 1 | 1 | 100.00% | 1/1 (100.00%) | 1/1 (100.00%) |
| identity | 16 | 2 | 12.50% | 0/0 (N/A) | 0/0 (N/A) |
| identity_compound | 7 | 1 | 14.29% | 0/0 (N/A) | 0/0 (N/A) |
| identity_typo | 100 | 10 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| input_quality | 4 | 1 | 25.00% | 0/0 (N/A) | 0/0 (N/A) |
| knowledge | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| live_availability | 16 | 2 | 12.50% | 0/0 (N/A) | 0/0 (N/A) |
| live_booking | 966 | 97 | 10.04% | 14/14 (100.00%) | 14/14 (100.00%) |
| live_schedule | 12 | 2 | 16.67% | 0/0 (N/A) | 0/0 (N/A) |
| members | 70 | 7 | 10.00% | 11/11 (100.00%) | 2/11 (18.18%) |
| members_about_contact | 25 | 3 | 12.00% | 2/3 (66.67%) | 1/3 (33.33%) |
| members_overview_contact | 646 | 65 | 10.06% | 126/127 (99.21%) | 83/127 (65.35%) |
| membership_facet | 2 | 1 | 50.00% | 1/1 (100.00%) | 1/1 (100.00%) |
| multi_question | 33 | 4 | 12.12% | 0/0 (N/A) | 0/0 (N/A) |
| multi_studio_rules | 1 | 1 | 100.00% | 1/1 (100.00%) | 1/1 (100.00%) |
| no_answer | 1 | 1 | 100.00% | 0/1 (0.00%) | 0/1 (0.00%) |
| offsite_scope | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| out_of_scope | 107 | 11 | 10.28% | 0/0 (N/A) | 0/0 (N/A) |
| outsider_eligibility | 100 | 10 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| overview | 25 | 3 | 12.00% | 0/1 (0.00%) | 0/1 (0.00%) |
| penalty | 4 | 1 | 25.00% | 0/0 (N/A) | 0/0 (N/A) |
| personal_power | 3 | 1 | 33.33% | 1/1 (100.00%) | 0/1 (0.00%) |
| play_booking_controls | 89 | 9 | 10.11% | 0/0 (N/A) | 0/0 (N/A) |
| policy_schedule_rules | 6 | 1 | 16.67% | 1/1 (100.00%) | 0/1 (0.00%) |
| price | 18 | 2 | 11.11% | 0/0 (N/A) | 0/0 (N/A) |
| protected | 13 | 2 | 15.38% | 0/0 (N/A) | 0/0 (N/A) |
| rag_knowledge | 25 | 3 | 12.00% | 0/0 (N/A) | 0/0 (N/A) |
| reservation | 53 | 6 | 11.32% | 5/6 (83.33%) | 4/6 (66.67%) |
| reservation_policy | 1162 | 117 | 10.07% | 117/122 (95.90%) | 90/122 (73.77%) |
| return_equipment_rule | 1 | 1 | 100.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| rules | 18 | 2 | 11.11% | 0/0 (N/A) | 0/0 (N/A) |
| rules_penalty | 45 | 5 | 11.11% | 5/5 (100.00%) | 4/5 (80.00%) |
| schedule | 98 | 10 | 10.20% | 6/6 (100.00%) | 1/6 (16.67%) |
| schedule_calendar | 864 | 87 | 10.07% | 114/122 (93.44%) | 44/122 (36.07%) |
| service_fee | 1530 | 153 | 10.00% | 222/223 (99.55%) | 117/223 (52.47%) |
| single | 168 | 17 | 10.12% | 16/17 (94.12%) | 0/17 (0.00%) |
| social | 24 | 3 | 12.50% | 0/0 (N/A) | 0/0 (N/A) |
| student_only_boundary | 1 | 1 | 100.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| studio_rules_penalties | 866 | 87 | 10.05% | 85/85 (100.00%) | 73/85 (85.88%) |
| time_vs_access | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| unclassified | 2725 | 273 | 10.02% | 43/46 (93.48%) | 5/46 (10.87%) |
| unclear_or_outside_scope | 100 | 10 | 10.00% | 0/0 (N/A) | 0/0 (N/A) |
| visit_only_fee | 2 | 1 | 50.00% | 1/1 (100.00%) | 0/1 (0.00%) |
| visitor_fee | 1 | 1 | 100.00% | 1/1 (100.00%) | 1/1 (100.00%) |
| weekday_live_slots | 100 | 10 | 10.00% | 20/20 (100.00%) | 0/20 (0.00%) |

## กลุ่มไม่ผ่าน strict

```json
{
  "protocol": 5372,
  "outcome": 1135,
  "content_or_format": 841,
  "performance": 19,
  "evidence_identifier": 318,
  "native_quality_composite": 7
}
```

หนึ่ง grade มีได้หลาย failure group จึงห้ามรวม event counts เป็นจำนวนคำถามผิดจริง Protocol/ชื่อ route/ชื่อ evidence, outcome, literal/complete-clause, validity/source gaps, performance และ grader errors ต้องอ่านแยก

## ตรวจ source และ projection เพิ่ม

```json
{
  "response_type:unavailable": 111,
  "requests_with_unknown_refs": 0,
  "internal_metadata_visible": 34,
  "service_zone_projection_gap_requests": 17,
  "all_controls_source_set_gap_requests": 6,
  "need_reason:store_or_snapshot_unavailable": 1,
  "response_type:answer": 1353,
  "need_reason:bounded_model_selection": 776,
  "need_reason:typed_requested_fields": 349,
  "response_type:unconfirmed": 252,
  "response_type:partial_answer": 40,
  "need_reason:explicit_partial_response": 27,
  "response_type:None": 197,
  "need_reason:no_accepted_interpretation": 160,
  "need_reason:exact_action_binding": 41,
  "need_reason:typed_graph_and_delivered_claims": 101,
  "need_reason:dependency_not_supported": 40,
  "need_reason:live_binding_or_provider_not_confirmed": 108,
  "need_reason:provider_unavailable": 12,
  "response_type:clarification": 146,
  "need_reason:event_or_rule_not_bound": 45,
  "need_reason:person_public_scope_not_confirmed": 17,
  "need_reason:rule_dependency_incomplete": 28,
  "need_reason:action_condition_policy": 19,
  "need_reason:r101_accepted_need_executor": 7,
  "need_reason:offering_requires_matching_game_service": 2,
  "need_reason:entity_not_bound": 10,
  "need_reason:compatibility_scope_not_migrated": 99,
  "need_reason:duration_arithmetic_not_declared": 49,
  "need_reason:explicit_pending_selection": 32,
  "need_reason:domain_not_bound": 12,
  "need_reason:unresolved_query_clause": 16,
  "need_reason:model_invalid_choice": 2,
  "need_reason:calendar_interval_adapter_required": 6,
  "need_reason:assistant_interface": 24,
  "response_type:list": 4,
  "need_reason:event_clause_dependency_read": 7,
  "need_reason:financial_subject_not_bound": 12,
  "need_reason:common_calendar_open_status": 6,
  "need_reason:booking_steps_require_procedure_source": 10,
  "need_reason:game_summary_required": 1,
  "response_type:unsupported": 5,
  "need_reason:outside_supported_capability": 5,
  "need_reason:source_excerpt_without_complete_required_claims": 5,
  "need_reason:r104_required_relation_missing": 13,
  "need_reason:r101_qualifier_source_gap": 4,
  "need_reason:installed_version_or_entitlement_not_recorded": 1,
  "need_reason:complete_equipment_set": 11,
  "need_reason:r103_inventory_scope_unknown": 2,
  "need_reason:r102_universal_eligibility_gap": 1,
  "need_reason:unknown_exact_resource": 1,
  "need_reason:missing_requested_field:details": 1,
  "need_reason:schedule_predicate_requires_schedule_source": 1,
  "need_reason:requested_predicate_not_declared_by_source": 4,
  "need_reason:current_rate_effective_period_required": 2,
  "need_reason:r103_rule_dependency_gap": 1,
  "need_reason:missing_requested_field:specifications": 1,
  "need_reason:missing_requested_field:usage": 3,
  "need_reason:r101_catalog_subject_gap": 1,
  "need_reason:missing_requested_field:decision": 1,
  "need_reason:exact": 1
}
```

source refs ที่พบใน snapshot แสดงว่ามีหลักฐานของค่าที่พูด ไม่ได้พิสูจน์ว่าค่านั้นตอบ predicate ของคำถาม ตัวอย่าง service-vs-zone เก็บเส้นทาง game→offer→service→resource→zone ที่มีจริงใน PER_REQUEST_REVIEW และแยกเป็น projection gap ที่ต้องตรวจ ไม่เหมารวมว่าข้อมูลอยู่ผิดโซน
Literal ที่ไม่ผ่านและยังตัดสินความหมายไม่ได้ต้อง review ต่อ ไม่ถือเป็น actual content failure ทั้งหมด รายละเอียดกรณีและคำตอบก่อน/หลังอยู่ CASEBOOK_TH.md

## โมเดล การส่งคำขอ และเวลา

```json
{
  "observed_model_http": {
    "attempts": 1056,
    "transport_ok": 1055,
    "transport_failure": 1,
    "endpoint:generate": 278,
    "endpoint:chat": 778
  },
  "domain_selector_schema": {
    "domain_selector_events": 778,
    "transport_ok": 778,
    "schema_ok": 776,
    "identity_verified": 778
  },
  "latency": {
    "median_sec": 1.422,
    "p95_sec": 10.625,
    "max_sec": 32.703
  }
}
```

Transport success คือได้รับ HTTP response ไม่รับรอง schema หรือเนื้อหาถูก Domain selector schema เป็นเฉพาะ events ที่มีหลักฐานใน artifact ไม่ใช่จำนวน generation สำเร็จทั้งหมด Model identity ตรวจ tag/digest ก่อนและหลังรัน ไฟล์ MODEL_TRANSPORT เก็บ endpoint และข้อผิดพลาดจริง
- Chat HTTP สำเร็จ 2108/2,108; validation 2108/2,108; ไม่มีการ retry ซ่อนคำตอบแรก
- เป็น correctness benchmark serial บนเครื่องนี้ ไม่ใช่ load/capacity certification และมี cold-start รวมในรอบ

## หลักฐาน

- [สรุปสาเหตุที่ตรวจยืนยันและลำดับแก้หลังทดสอบ](ROOT_CAUSE_REVIEW_TH.md)
- [คะแนน JSON](COMPARISON.json)
- [ทุกคำขอ: คำตอบเดิม/ใหม่และ source review](PER_REQUEST_REVIEW.jsonl)
- [ทุก grade คู่เดิม/ใหม่](GRADE_COMPARISON.jsonl.gz)
- [กรณีไม่ผ่านและโจทย์เดิม](CASEBOOK_TH.md)
- [Manifest การเลือก](../SELECTION_MANIFEST.json)
- [ยืนยันจบรอบและ hash](../full01/TEST_COMPLETE.json)
- [Raw HTTP และ PipelineAnswer](../full01/RESULTS.jsonl)
- [กรณีที่ตรวจ source/code ระหว่างรัน](../PRELIMINARY_FINDINGS_TH.md)

R115 ยังเป็น candidate ไม่ติดตั้งทับ R78 ไม่เปลี่ยน source/approvals/oracle/log เก่า และไม่แก้ Flow จากผลระหว่าง benchmark นี้
