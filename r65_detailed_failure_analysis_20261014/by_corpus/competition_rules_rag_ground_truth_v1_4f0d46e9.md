# data/eval/competition_rules_rag_ground_truth_v1.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 154/548 | 394 | 0 | 20 |

## ตัวอย่าง legacy_offline: 4527ff53a60640b2db7605ecd50162554613874c9d72ae8f10d8e728c10441d7

คำถาม: กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-001","latency_ceiling_sec":20.0,"locale":"th","question":"กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร","question_style":"direct","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
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

raw source: legacy_offline\RESULTS.jsonl record1=1395

## ตัวอย่าง legacy_offline: 671b5cb95553b638f17f29a67b570a686dcdcb62ee41d8bd115d632fc00f3d21

คำถาม: Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-002","latency_ceiling_sec":20.0,"locale":"th","question":"Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน","question_style":"natural_variant","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
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

raw source: legacy_offline\RESULTS.jsonl record1=1396
| common_offline | 22/548 | 526 | 0 | 412 |

## ตัวอย่าง common_offline: 4527ff53a60640b2db7605ecd50162554613874c9d72ae8f10d8e728c10441d7

คำถาม: กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-001","latency_ceiling_sec":20.0,"locale":"th","question":"กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร","question_style":"direct","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**ภาพรวมเอกสาร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]
• หัวข้อกติกา: ภาพรวมเอกสาร [S2]
• เลขข้อจากเอกสารเดิม: 1 [S3]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**6. ข้อจำกัด**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 6. ข้อจำกัด [S4]
• หัวข้อกติกา: 6. ข้อจำกัด [S5]
• เลขข้อจากเอกสารเดิม: 10 [S6]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]
• หัวข้อกติกา: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]
• เลขข้อจากเอกสารเดิม: 11 [S9]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]
• หัวข้อกติกา: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]
• เลขข้อจากเอกสารเดิม: 12 [S12]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**
• ข้อคว … [ย่อจาก20,408ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route expected ['competition_rules'], got knowledge","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded\RESULTS.jsonl record1=51

## ตัวอย่าง common_offline: 671b5cb95553b638f17f29a67b570a686dcdcb62ee41d8bd115d632fc00f3d21

คำถาม: Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-002","latency_ceiling_sec":20.0,"locale":"th","question":"Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน","question_style":"natural_variant","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**ภาพรวมเอกสาร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]
• หัวข้อกติกา: ภาพรวมเอกสาร [S2]
• เลขข้อจากเอกสารเดิม: 1 [S3]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**6. ข้อจำกัด**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 6. ข้อจำกัด [S4]
• หัวข้อกติกา: 6. ข้อจำกัด [S5]
• เลขข้อจากเอกสารเดิม: 10 [S6]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]
• หัวข้อกติกา: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]
• เลขข้อจากเอกสารเดิม: 11 [S9]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]
• หัวข้อกติกา: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]
• เลขข้อจากเอกสารเดิม: 12 [S12]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**
• ข้อคว … [ย่อจาก20,408ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route expected ['competition_rules'], got knowledge","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded\RESULTS.jsonl record1=52
| legacy_llm | 154/548 | 394 | 0 | 20 |

## ตัวอย่าง legacy_llm: 4527ff53a60640b2db7605ecd50162554613874c9d72ae8f10d8e728c10441d7

คำถาม: กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-001","latency_ceiling_sec":20.0,"locale":"th","question":"กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร","question_style":"direct","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
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

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=468

## ตัวอย่าง legacy_llm: 671b5cb95553b638f17f29a67b570a686dcdcb62ee41d8bd115d632fc00f3d21

คำถาม: Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-002","latency_ceiling_sec":20.0,"locale":"th","question":"Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน","question_style":"natural_variant","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
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

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=469
| common_llm | 30/548 | 518 | 0 | 438 |

## ตัวอย่าง common_llm: 4527ff53a60640b2db7605ecd50162554613874c9d72ae8f10d8e728c10441d7

คำถาม: กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-001","latency_ceiling_sec":20.0,"locale":"th","question":"กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร","question_style":"direct","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**ภาพรวมเอกสาร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]
• หัวข้อกติกา: ภาพรวมเอกสาร [S2]
• เลขข้อจากเอกสารเดิม: 1 [S3]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**6. ข้อจำกัด**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 6. ข้อจำกัด [S4]
• หัวข้อกติกา: 6. ข้อจำกัด [S5]
• เลขข้อจากเอกสารเดิม: 10 [S6]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]
• หัวข้อกติกา: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]
• เลขข้อจากเอกสารเดิม: 11 [S9]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]
• หัวข้อกติกา: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]
• เลขข้อจากเอกสารเดิม: 12 [S12]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**
• ข้อคว … [ย่อจาก20,408ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route expected ['competition_rules'], got knowledge","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=468

## ตัวอย่าง common_llm: 671b5cb95553b638f17f29a67b570a686dcdcb62ee41d8bd115d632fc00f3d21

คำถาม: Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"allowed_evidence_fact_ids":[],"allowed_evidence_rule_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01"],"allowed_source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"],"answer_language_requirement":"source_grounded_th","case_type":"facet_targeted_retrieval","evidence_statuses":["pending_owner_review"],"expected_answer_status":"answer_available","expected_facet":"competition_format","expected_game_id":"cs2","expected_route_categories":["competition_rules"],"expected_rulebook_ids":["competition_rules_cs2_psu_phuket_2026"],"id":"COMP-RAG-TH-002","latency_ceiling_sec":20.0,"locale":"th","question":"Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน","question_style":"natural_variant","rag_required":true,"review_status":"retrieval_gold_candidate","suite":"competition_rules_rag_ground_truth_v1","target_locked":true}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**PSU Phuket CS2 2026 Tournament**
• ฉบับกติกาและวันที่: competition_rules_cs2_psu_phuket_2026 [S1]

**ภาพรวมเอกสาร**
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: ภาพรวมเอกสาร [S2]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S3]
• เลขข้อจากเอกสารเดิม: 1 [S4]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**6. ข้อจำกัด**
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: 6. ข้อจำกัด [S5]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 6. ข้อจำกัด [S6]
• เลขข้อจากเอกสารเดิม: 10 [S7]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S9]
• เลขข้อจากเอกสารเดิม: 11 [S10]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: 2. ไม่อนุญาตให้ล … [ย่อจาก23,005ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route expected ['competition_rules'], got knowledge","missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026']","retrieval evidence did not match the allowed canonical fact/rule IDs"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "rulebook_release",
    "facet",
    "heading",
    "text"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=469
