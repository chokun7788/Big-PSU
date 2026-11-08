# data/eval/master_ground_truth_en_5000_v2.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 4394/5000 | 606 | 75 | 45 |

## ตัวอย่าง legacy_offline: 26449f04f2236c63b224994a5c9d7a8e28db1767666faaa9e2bc0c3b96f88d45

คำถาม: Horizon Call of the Mountain price

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["Local LLM"]},"critical":true,"domain":"service_fee","expected_answer_status":"answer_available","expected_facet":"","expected_intent":"","expected_route_categories":["service_fee"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-00135","latency_ceiling_sec":20.0,"locale":"en","metadata":{"group":"service_fee","quality_bucket":"psu_fact","risk":"high"},"origin":"model_benchmark_1600","origin_id":"EN-SHADOW-0069","question":"Horizon Call of the Mountain price","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"inherited_answer_contract","source_ids":["broad_usage_eval_v1"],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:english_clarification / clarification / 0.96

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

Failures: ["route:clarification expected:['service_fee']","status:clarification expected:answer_available"]

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

raw source: legacy_offline\RESULTS.jsonl record1=4145

## ตัวอย่าง legacy_offline: 42ddd41b9ab3c9e5bf79dd592944e7fbf6fba0d339232848b13ab5a2a962d9a0

คำถาม: How much does Gran Turismo 7 cost

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["Local LLM"]},"critical":true,"domain":"service_fee","expected_answer_status":"answer_available","expected_facet":"","expected_intent":"","expected_route_categories":["service_fee"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-00136","latency_ceiling_sec":20.0,"locale":"en","metadata":{"group":"service_fee","quality_bucket":"psu_fact","risk":"high"},"origin":"model_benchmark_1600","origin_id":"EN-SHADOW-0070","question":"How much does Gran Turismo 7 cost","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"inherited_answer_contract","source_ids":["broad_usage_eval_v1"],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:protected_price_missing_service / clarification / 0.98

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

Failures: ["route:clarification expected:['service_fee']","status:clarification expected:answer_available"]

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

raw source: legacy_offline\RESULTS.jsonl record1=4146
| common_offline | 1590/5000 | 3410 | 751 | 1005 |

## ตัวอย่าง common_offline: fc3b8732bcb0f71a458f292f526839483eb880efab598a655bf6d829eb1e8477

คำถาม: Please tell me: Tell me about VALORANT

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":false,"domain":"games_catalog_availability","expected_answer_status":"localization_pending","expected_facet":"","expected_intent":"","expected_route_categories":["games"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-01675","latency_ceiling_sec":20.0,"locale":"en","metadata":{},"origin":"english_gold_400","origin_id":"EN-GOLD-0148","question":"Please tell me: Tell me about VALORANT","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"reviewed_english_answer_contract","source_ids":[],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of [Thai source] VALORANT do you need: event name / rulebook release / coverage / platform?

Failures: ["route:knowledge expected:['games']","status:clarification expected:localization_pending"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_valorant",
    "competition_competition_rules_valorant_psu_phuket_2026",
    "controls_pc_valorant",
    "availability_pc_01_02",
    "availability_pc_03_10"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "please tell me: tell me about"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=1389

## ตัวอย่าง common_offline: 1412d5904d99a387ae93ff92befbdabd957b7ed7485517dd7bd99a3225f7335e

คำถาม: What is VALORANT

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["Local LLM"]},"critical":false,"domain":"game_detail","expected_answer_status":"localization_pending","expected_facet":"","expected_intent":"","expected_route_categories":["games"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-02311","latency_ceiling_sec":20.0,"locale":"en","metadata":{"group":"games","quality_bucket":"psu_fact","risk":"medium"},"origin":"model_benchmark_1600","origin_id":"EN-SHADOW-0089","question":"What is VALORANT","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"inherited_answer_contract","source_ids":["broad_usage_eval_v1"],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of [Thai source] VALORANT do you need: event name / rulebook release / coverage / platform?

Failures: ["route:knowledge expected:['games']","status:clarification expected:localization_pending"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_valorant",
    "competition_competition_rules_valorant_psu_phuket_2026",
    "controls_pc_valorant",
    "availability_pc_01_02",
    "availability_pc_03_10"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "what is"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=1730
| legacy_llm | 4393/5000 | 607 | 75 | 44 |

## ตัวอย่าง legacy_llm: 26449f04f2236c63b224994a5c9d7a8e28db1767666faaa9e2bc0c3b96f88d45

คำถาม: Horizon Call of the Mountain price

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["Local LLM"]},"critical":true,"domain":"service_fee","expected_answer_status":"answer_available","expected_facet":"","expected_intent":"","expected_route_categories":["service_fee"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-00135","latency_ceiling_sec":20.0,"locale":"en","metadata":{"group":"service_fee","quality_bucket":"psu_fact","risk":"high"},"origin":"model_benchmark_1600","origin_id":"EN-SHADOW-0069","question":"Horizon Call of the Mountain price","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"inherited_answer_contract","source_ids":["broad_usage_eval_v1"],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:english_clarification / clarification / 0.96

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

Failures: ["route:clarification expected:['service_fee']","status:clarification expected:answer_available"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=2448

## ตัวอย่าง legacy_llm: 42ddd41b9ab3c9e5bf79dd592944e7fbf6fba0d339232848b13ab5a2a962d9a0

คำถาม: How much does Gran Turismo 7 cost

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["Local LLM"]},"critical":true,"domain":"service_fee","expected_answer_status":"answer_available","expected_facet":"","expected_intent":"","expected_route_categories":["service_fee"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-00136","latency_ceiling_sec":20.0,"locale":"en","metadata":{"group":"service_fee","quality_bucket":"psu_fact","risk":"high"},"origin":"model_benchmark_1600","origin_id":"EN-SHADOW-0070","question":"How much does Gran Turismo 7 cost","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"inherited_answer_contract","source_ids":["broad_usage_eval_v1"],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:protected_price_missing_service / clarification / 0.98

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

Failures: ["route:clarification expected:['service_fee']","status:clarification expected:answer_available"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=2449
| common_llm | 1095/5000 | 3905 | 2132 | 984 |

## ตัวอย่าง common_llm: 36e77377ca3e4461954e52cc40d8b8e733366aa5a9b91f598499a7307e758329

คำถาม: What genre is Call of Duty: Modern Warfare III

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["Local LLM"]},"critical":false,"domain":"game_detail","expected_answer_status":"localization_pending","expected_facet":"","expected_intent":"","expected_route_categories":["games"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-02343","latency_ceiling_sec":20.0,"locale":"en","metadata":{"group":"games","quality_bucket":"psu_fact","risk":"medium"},"origin":"model_benchmark_1600","origin_id":"EN-SHADOW-0140","question":"What genre is Call of Duty: Modern Warfare III","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"inherited_answer_contract","source_ids":["broad_usage_eval_v1"],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of Call of Duty: Modern Warfare III do you need: platform / input device / preset / bindings?

Failures: ["route:knowledge expected:['games']","status:clarification expected:localization_pending"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "controls_ps5_call_of_duty_modern_warfare_iii",
    "availability_ps5_01_02"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "what genre is"
  ],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=2520

## ตัวอย่าง common_llm: e9bef77f9495bb0918d400e452f68baa1d8da56c443cf555760a0efe3d9f1a78

คำถาม: Where can Luigi's Mansion 3 be played

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["Local LLM"]},"critical":false,"domain":"games_catalog_availability","expected_answer_status":"answer_available","expected_facet":"","expected_intent":"","expected_route_categories":["games"],"expected_target":"","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-EN-01742","latency_ceiling_sec":20.0,"locale":"en","metadata":{"group":"games","quality_bucket":"psu_fact","risk":"medium"},"origin":"model_benchmark_1600","origin_id":"EN-SHADOW-0198","question":"Where can Luigi's Mansion 3 be played","question_style":"source_form","review_status":"inherited_gold_candidate","source_contract":{"live_dependency":false,"requirement":"inherited_answer_contract","source_ids":["broad_usage_eval_v1"],"source_urls":[]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

location: This attribute is outside the selected record scope; please specify the related service or record.

Failures: ["route:knowledge expected:['games']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_luigis_mansion_3",
    "availability_nintendo_1_2",
    "availability_nintendo_1_4",
    "controls_nintendo_luigi_s_mansion_3"
  ],
  "requested_fields": [
    "location"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=2578
