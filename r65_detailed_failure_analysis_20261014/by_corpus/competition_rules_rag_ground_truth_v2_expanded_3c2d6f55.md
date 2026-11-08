# data/eval/competition_rules_rag_ground_truth_v2_expanded.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 39/282 | 243 | 0 | 23 |

## ตัวอย่าง legacy_offline: 05d336251e6483e895e6168fd303787d34d6f47692ddca763dc3291dec56382f

คำถาม: What competition format does Counter-Strike 2 use?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":1},"id":"COMP-RAG-V2-EN-001","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"What competition format does Counter-Strike 2 use?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
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

raw source: legacy_offline\RESULTS.jsonl record1=1943

## ตัวอย่าง legacy_offline: 11f28567af8c26f25b97dfddecbb67bd11d16a2dc9d4afa24f680ca18061828e

คำถาม: How many games are played in a Counter-Strike 2 match?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":2},"id":"COMP-RAG-V2-EN-002","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"How many games are played in a Counter-Strike 2 match?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
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

raw source: legacy_offline\RESULTS.jsonl record1=1944
| common_offline | 18/282 | 264 | 0 | 217 |

## ตัวอย่าง common_offline: 05d336251e6483e895e6168fd303787d34d6f47692ddca763dc3291dec56382f

คำถาม: What competition format does Counter-Strike 2 use?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":1},"id":"COMP-RAG-V2-EN-001","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"What competition format does Counter-Strike 2 use?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of [Thai source] PSU Phuket CS2 2026 Tournament do you need: event name / rulebook release / coverage?

Failures: ["route expected ['competition_rules'], got knowledge","outcome expected answer_available, got clarification","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "what competition format does use"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_cached\RESULTS.jsonl record1=295

## ตัวอย่าง common_offline: 11f28567af8c26f25b97dfddecbb67bd11d16a2dc9d4afa24f680ca18061828e

คำถาม: How many games are played in a Counter-Strike 2 match?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":2},"id":"COMP-RAG-V2-EN-002","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"How many games are played in a Counter-Strike 2 match?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of [Thai source] Counter-Strike 2 do you need: event name / rulebook release / coverage / platform?

Failures: ["route expected ['competition_rules'], got knowledge","outcome expected answer_available, got clarification","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "competition_competition_rules_cs2_psu_phuket_2026",
    "controls_pc_counter_strike_2",
    "availability_pc_01_02",
    "availability_pc_03_10"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "how many games are played in a match"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_cached\RESULTS.jsonl record1=296
| legacy_llm | 39/282 | 243 | 0 | 23 |

## ตัวอย่าง legacy_llm: 05d336251e6483e895e6168fd303787d34d6f47692ddca763dc3291dec56382f

คำถาม: What competition format does Counter-Strike 2 use?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":1},"id":"COMP-RAG-V2-EN-001","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"What competition format does Counter-Strike 2 use?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=246

## ตัวอย่าง legacy_llm: 11f28567af8c26f25b97dfddecbb67bd11d16a2dc9d4afa24f680ca18061828e

คำถาม: How many games are played in a Counter-Strike 2 match?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":2},"id":"COMP-RAG-V2-EN-002","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"How many games are played in a Counter-Strike 2 match?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=247
| common_llm | 13/282 | 269 | 0 | 223 |

## ตัวอย่าง common_llm: 05d336251e6483e895e6168fd303787d34d6f47692ddca763dc3291dec56382f

คำถาม: What competition format does Counter-Strike 2 use?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":1},"id":"COMP-RAG-V2-EN-001","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"What competition format does Counter-Strike 2 use?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] PSU Phuket CS2 2026 Tournament**
• competition dates: Not yet confirmed
• division: Not yet confirmed
• rulebook release: competition_rules_cs2_psu_phuket_2026 [S1]
• coverage: Not yet confirmed

Failures: ["route expected ['competition_rules'], got knowledge","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "competition_dates",
    "division",
    "rulebook_release",
    "coverage"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=247

## ตัวอย่าง common_llm: 11f28567af8c26f25b97dfddecbb67bd11d16a2dc9d4afa24f680ca18061828e

คำถาม: How many games are played in a Counter-Strike 2 match?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":["cs2_format_single_elim_bo3"],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s01_c01","canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_en_or_translation_pending","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"generation":{"strategy":"facet_prompt_v2","variant":2},"id":"COMP-RAG-V2-EN-002","latency_ceiling_sec":20.0,"locale":"en","parent_gold_id":"COMP-RAG-EN-001","question":"How many games are played in a Counter-Strike 2 match?","question_style":"participant_natural_paraphrase","rag_required":true,"review_status":"source_preserving_paraphrase_candidate","suite":"competition_rules_rag_ground_truth_v2_expanded","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] Counter-Strike 2**
• edition: Not yet confirmed
• genre: [Thai source] เกมยิง Tactical FPS [S1]
• summary: [Thai source] Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม [S2]
• how to play: [Thai source] เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ [S3]
• publisher url: Not yet confirmed
• supported platforms: Not yet confirmed
• age rating: Not yet confirmed

**Game on this service**
• game id: [Thai source] Counter-Strike 2 [S4]
• offered: Yes [S5]
• service id: PC #01-#02 [S6]

**PC #01-#02**
• name: PC #01-#02 [S7]
• platform: PC [S8]

**Game on this service**
• game id: [Thai source] Counter-Strike 2 [S9]
• offered: Yes [S10]
• service id: PC #03-#10 [S11]

**PC #03-#10**
• name: PC #03-#10 [S12]
• platform: PC [S13]

**[Thai source] PSU Phuket CS2 2026 Tournament**
• game id: [Thai source] Counter-Strike 2 [S14]

**Counter-Strike 2**
• game id: [Thai source] Counter-Strike 2 [S15]

Failures: ["route expected ['competition_rules'], got knowledge","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "competition_competition_rules_cs2_psu_phuket_2026",
    "controls_pc_counter_strike_2",
    "availability_pc_01_02",
    "availability_pc_03_10"
  ],
  "requested_fields": [
    "game_id",
    "edition",
    "genre",
    "summary",
    "how_to_play",
    "publisher_url",
    "supported_platforms",
    "age_rating"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=248
