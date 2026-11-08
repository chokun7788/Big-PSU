# data/eval/rag_robustness_ground_truth_v1.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 415/600 | 185 | 64 | 0 |

## ตัวอย่าง legacy_offline: c7c9f58029af3e17b77ff34284842689f4687472a606ab28be71a101c5363d45

คำถาม: How much does TEKKEN 8 cost?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":["game_to_zone"],"critical":false,"difficulty":"hard","expected_answer_status":"answer_available","expected_route_categories":["service_fee","games"],"expected_source_requirement":"service_fee","expected_target":"TEKKEN 8","group":"service_fee","id":"RAG-ROBUST-EN-097","latency_ceiling_sec":20.0,"locale":"en","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"How much does TEKKEN 8 cost?","review_status":"gold_candidate","scenario_id":"price_game_zone","suite":"rag_robustness_ground_truth_v1","variant":"direct"}
```

Actual mode/category/confidence: pipeline:price_service_clarification_en / service_fee / 0.96

TEKKEN 8 is available on more than one service (PC, PlayStation 5). Which service and duration should I price?
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Failures: ["status:clarification expected:answer_available"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: legacy_offline\RESULTS.jsonl record1=4140

## ตัวอย่าง legacy_offline: 76a9f80b813fea070a3cb2449f5589c40e7b8acf13471a747ca9164e644e35e3

คำถาม: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":["calculation"],"critical":false,"difficulty":"hard","expected_answer_status":"answer_available","expected_route_categories":["service_fee"],"expected_source_requirement":"service_fee","expected_target":"PC Zone","group":"service_fee","id":"RAG-ROBUST-TH-087","latency_ceiling_sec":20.0,"locale":"th","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง","review_status":"gold_candidate","scenario_id":"price_pc_two_hours","suite":"rag_robustness_ground_truth_v1","variant":"contextual"}
```

Actual mode/category/confidence: None / None / None

NameError:name 'ownership_blocked' is not defined

Failures: ["pipeline_exception"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: legacy_offline_resumed\RESULTS.jsonl record1=693
| common_offline | 272/600 | 328 | 81 | 13 |

## ตัวอย่าง common_offline: b3412afec8542214a19ba73437ca5a20085cb6613b1d9522e60171489cfe0b2a

คำถาม: Is the studio open on Monday morning?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":["maintenance"],"critical":false,"difficulty":"hard","expected_answer_status":"answer_available","expected_route_categories":["schedule"],"expected_source_requirement":"service_schedule","expected_target":"Monday morning","group":"schedule","id":"RAG-ROBUST-EN-161","latency_ceiling_sec":20.0,"locale":"en","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"Is the studio open on Monday morning?","review_status":"gold_candidate","scenario_id":"schedule_monday_am","suite":"rag_robustness_ground_truth_v1","variant":"direct"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of [Thai source] วันจันทร์.*ช่วงเช้า do you need: question / answer / topic?

Failures: ["route:knowledge expected:['schedule']","status:clarification expected:answer_available"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_schedule_monday_morning"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "bounded_fuzzy",
  "platform": null,
  "unresolved_clauses": [
    "is the studio open on monday morning"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=1292

## ตัวอย่าง common_offline: dfda1c46e1278bfe7d761b0183885d7f336566aad654478893d06be568e93e3b

คำถาม: What equipment is available in the VR Zone?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":[],"critical":false,"difficulty":"medium","expected_answer_status":"answer_available","expected_route_categories":["equipment"],"expected_source_requirement":"verified_equipment","expected_target":"VR Zone","group":"equipment","id":"RAG-ROBUST-EN-053","latency_ceiling_sec":20.0,"locale":"en","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"What equipment is available in the VR Zone?","review_status":"gold_candidate","scenario_id":"equipment_vr","suite":"rag_robustness_ground_truth_v1","variant":"direct"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of VR Zone do you need: name / platform / Play time (minutes) / Reserved time (minutes)?

Failures: ["route:knowledge expected:['equipment']","status:clarification expected:answer_available"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "zone_vr",
    "availability_vr_30",
    "availability_vr_60"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "what equipment is available in the"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=1398
| legacy_llm | 414/600 | 186 | 64 | 0 |

## ตัวอย่าง legacy_llm: c7c9f58029af3e17b77ff34284842689f4687472a606ab28be71a101c5363d45

คำถาม: How much does TEKKEN 8 cost?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":["game_to_zone"],"critical":false,"difficulty":"hard","expected_answer_status":"answer_available","expected_route_categories":["service_fee","games"],"expected_source_requirement":"service_fee","expected_target":"TEKKEN 8","group":"service_fee","id":"RAG-ROBUST-EN-097","latency_ceiling_sec":20.0,"locale":"en","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"How much does TEKKEN 8 cost?","review_status":"gold_candidate","scenario_id":"price_game_zone","suite":"rag_robustness_ground_truth_v1","variant":"direct"}
```

Actual mode/category/confidence: pipeline:price_service_clarification_en / service_fee / 0.96

TEKKEN 8 is available on more than one service (PC, PlayStation 5). Which service and duration should I price?
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Failures: ["status:clarification expected:answer_available"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=2443

## ตัวอย่าง legacy_llm: 76a9f80b813fea070a3cb2449f5589c40e7b8acf13471a747ca9164e644e35e3

คำถาม: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":["calculation"],"critical":false,"difficulty":"hard","expected_answer_status":"answer_available","expected_route_categories":["service_fee"],"expected_source_requirement":"service_fee","expected_target":"PC Zone","group":"service_fee","id":"RAG-ROBUST-TH-087","latency_ceiling_sec":20.0,"locale":"th","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง","review_status":"gold_candidate","scenario_id":"price_pc_two_hours","suite":"rag_robustness_ground_truth_v1","variant":"contextual"}
```

Actual mode/category/confidence: None / None / None

NameError:name 'ownership_blocked' is not defined

Failures: ["pipeline_exception"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=4912
| common_llm | 211/600 | 389 | 232 | 50 |

## ตัวอย่าง common_llm: dfda1c46e1278bfe7d761b0183885d7f336566aad654478893d06be568e93e3b

คำถาม: What equipment is available in the VR Zone?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":[],"critical":false,"difficulty":"medium","expected_answer_status":"answer_available","expected_route_categories":["equipment"],"expected_source_requirement":"verified_equipment","expected_target":"VR Zone","group":"equipment","id":"RAG-ROBUST-EN-053","latency_ceiling_sec":20.0,"locale":"en","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"What equipment is available in the VR Zone?","review_status":"gold_candidate","scenario_id":"equipment_vr","suite":"rag_robustness_ground_truth_v1","variant":"direct"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

equipment model ids: This attribute is outside the selected record scope; please specify the related service or record.

Failures: ["route:knowledge expected:['equipment']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "zone_vr",
    "availability_vr_30",
    "availability_vr_60"
  ],
  "requested_fields": [
    "equipment_model_ids"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=2137

## ตัวอย่าง common_llm: c6097f760a82afc496a6be975ea07ecf1a2969845ff7f8aecfa21ddd0bbbbe41

คำถาม: What are the competition rules?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"behavior_tags":["competition","missing_game_event"],"critical":true,"difficulty":"hard","expected_answer_status":"clarification_required","expected_route_categories":["competition_rules","general","clarification"],"expected_source_requirement":"competition_rag","expected_target":"","group":"clarification","id":"RAG-ROBUST-EN-225","latency_ceiling_sec":20.0,"locale":"en","notes":"Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.","question":"What are the competition rules?","review_status":"gold_candidate","scenario_id":"comp_broad","suite":"rag_robustness_ground_truth_v1","variant":"direct"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] damage_responsibility**
• answer: If equipment is damaged, users are responsible for fines or compensation depending on severity: minor damage is 100-500 THB, moderate damage is the actual cost or 500-2,000 THB, and severe damage requires full compensation for the property. [S1]
• scope note: Not yet confirmed

**[Thai source] damage_penalty_summary**
• answer: Damage penalties depend on severity: minor damage is 100-500 THB, moderate damage is the actual cost or 500-2,000 THB, and severe damage requires full compensation for the property. [S2]
• scope note: Not yet confirmed

**[Thai source] ของหาย.*อุปกรณ์.*เปียก**
• answer: For lost personal belongings, the center reserves the right not to be responsible. If equipment is damaged or made wet, the user is responsible for fines or compensation depending on the damage level. [S3]
• scope note: Not yet confirmed

Failures: ["route:knowledge expected:['competition_rules', 'general', 'clarification']","status:answer expected:clarification_required"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_en_damage_responsibility_natural",
    "migrated_faq_rule_en_general_damage_penalties",
    "migrated_faq_rule_mixed_lost_and_damage"
  ],
  "requested_fields": [
    "answer",
    "scope_note"
  ],
  "all_fields": false,
  "method": "published_semantic_candidates",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=2281
