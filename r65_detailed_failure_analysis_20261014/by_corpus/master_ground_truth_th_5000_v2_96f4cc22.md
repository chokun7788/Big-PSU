# data/eval/master_ground_truth_th_5000_v2.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 3620/5000 | 1380 | 647 | 108 |

## ตัวอย่าง legacy_offline: 4527ff53a60640b2db7605ecd50162554613874c9d72ae8f10d8e728c10441d7

คำถาม: กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"competition_format","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04001","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-001","question":"กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
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
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"competition_format","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04002","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-002","question":"Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
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
| common_offline | 1431/5000 | 3569 | 497 | 1432 |

## ตัวอย่าง common_offline: 0adcfdc6fbef22532f9f5dd7b0878f7209190b1d0685b2742851453c3a185769

คำถาม: ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อรูปแบบการแข่งขัน หน่อย

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"competition_format","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04003","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-003","question":"ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อรูปแบบการแข่งขัน หน่อย","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ เคาน์เตอร์สไตรก์ 2 เช่น แพลตฟอร์ม เช่น PC หรือ PS5 / อุปกรณ์ควบคุม / ชื่อชุดปุ่ม เช่น default / ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม?

Failures: ["route:knowledge expected:['competition_rules']","status:clarification expected:answer_available"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "controls_pc_counter_strike_2"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "ขออ้างอิงกติกา ในหัวข้อรูปแบบการแข่งขัน หน่อย"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded\RESULTS.jsonl record1=53

## ตัวอย่าง common_offline: c52e329c36da037a2222b9c071f21f398a6ddcb83718c955fe2bbb27fd80d007

คำถาม: กำลังจะลงแข่ง CS2 อยากรู้เรื่องรูปแบบการแข่งขัน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"competition_format","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04004","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-004","question":"กำลังจะลงแข่ง CS2 อยากรู้เรื่องรูปแบบการแข่งขัน","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ PSU Phuket CS2 2026 Tournament เช่น ชื่อรายการ+ปี+ประเภทให้ตรง / ฉบับกติกาและวันที่ / เอกสารกติกาครบหรือมีเพียงบางส่วน?

Failures: ["route:knowledge expected:['competition_rules']","status:clarification expected:answer_available"]

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
    "กำลังจะลงแข่ง อยากรู้เรื่องรูปแบบการแข่งขัน"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded\RESULTS.jsonl record1=54
| legacy_llm | 3621/5000 | 1379 | 651 | 106 |

## ตัวอย่าง legacy_llm: 4527ff53a60640b2db7605ecd50162554613874c9d72ae8f10d8e728c10441d7

คำถาม: กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"competition_format","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04001","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-001","question":"กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
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
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"competition_format","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04002","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-002","question":"Counter-Strike 2 แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s19_c01","canonical::competition_rules_cs2_psu_phuket_2026_s20_c01","canonical::competition_rules_cs2_psu_phuket_2026_s21_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
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
| common_llm | 1087/5000 | 3913 | 2443 | 1109 |

## ตัวอย่าง common_llm: 911f6dbfa4b3b8ba5724f7a2963f2fdcfb5b063218b953f78d2b03a93f5c4b5e

คำถาม: Counter-Strike 2 มีข้อกำหนดเรื่องมารยาทและพฤติกรรมผู้เล่น ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"conduct","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04011","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-011","question":"Counter-Strike 2 มีข้อกำหนดเรื่องมารยาทและพฤติกรรมผู้เล่น ไหม","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s35_c01","canonical::competition_rules_cs2_psu_phuket_2026_s36_c01","canonical::competition_rules_cs2_psu_phuket_2026_s54_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

**ภาพรวมเอกสาร**
• เลือกรายการแข่งขันและฉบับกติกา: PSU Phuket CS2 2026 Tournament [S1]
• เลขข้อจากเอกสารเดิม: 1 [S2]
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: ภาพรวมเอกสาร [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S4]
• ข้อกติกาที่ต้องอ่านร่วมกัน (ถ้ามี): ยังไม่มีข้อมูลยืนยัน
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**6. ข้อจำกัด**
• เลือกรายการแข่งขันและฉบับกติกา: PSU Phuket CS2 2026 Tournament [S5]
• เลขข้อจากเอกสารเดิม: 10 [S6]
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: 6. ข้อจำกัด [S7]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 6. ข้อจำกัด [S8]
• ข้อกติกาที่ต้องอ่านร่วมกัน (ถ้ามี): ยังไม่มีข้อมูลยืนยัน
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**
• เลือกรายการแข่งขันและฉบับกติกา: PSU Phuket CS2 2026 Tournament [S9]
• เลขข้อจากเอกสารเดิม: 11 [S10]
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S11]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ต้องไม่มีการเปล … [ย่อจาก30,586ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route:knowledge expected:['competition_rules']","validation_rejected"]

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
    "competition_id",
    "section_number",
    "facet",
    "heading",
    "text",
    "depends_on_ids",
    "completeness",
    "details"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=484

## ตัวอย่าง common_llm: a25251c9c366fe21ae56c766cff51c6ebe265f8e6d21785859b9aa8b11d261ec

คำถาม: Counter-Strike 2 มีข้อกำหนดเรื่องการประท้วงและข้อพิพาท ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"critical":true,"domain":"competition_rules","expected_answer_status":"answer_available","expected_facet":"dispute","expected_intent":"","expected_route_categories":["competition_rules"],"expected_target":"cs2","generation_version":"master-gt-builder-v2-20260923","id":"MASTER-GT-TH-04017","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"origin":"competition_rules_rag_ground_truth_v1","origin_id":"COMP-RAG-TH-017","question":"Counter-Strike 2 มีข้อกำหนดเรื่องการประท้วงและข้อพิพาท ไหม","question_style":"source_form","review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s06_c01","canonical::competition_rules_cs2_psu_phuket_2026_s58_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"suite":"psu_esports_master_ground_truth_candidate_v2"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

**ภาพรวมเอกสาร**
• เลือกรายการแข่งขันและฉบับกติกา: PSU Phuket CS2 2026 Tournament [S1]
• เลขข้อจากเอกสารเดิม: 1 [S2]
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: ภาพรวมเอกสาร [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S4]
• ข้อกติกาที่ต้องอ่านร่วมกัน (ถ้ามี): ยังไม่มีข้อมูลยืนยัน
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**6. ข้อจำกัด**
• เลือกรายการแข่งขันและฉบับกติกา: PSU Phuket CS2 2026 Tournament [S5]
• เลขข้อจากเอกสารเดิม: 10 [S6]
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: 6. ข้อจำกัด [S7]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 6. ข้อจำกัด [S8]
• ข้อกติกาที่ต้องอ่านร่วมกัน (ถ้ามี): ยังไม่มีข้อมูลยืนยัน
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**
• เลือกรายการแข่งขันและฉบับกติกา: PSU Phuket CS2 2026 Tournament [S9]
• เลขข้อจากเอกสารเดิม: 11 [S10]
• หมวดของกติกาข้อนี้: ยังไม่มีข้อมูลยืนยัน
• หัวข้อกติกา: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S11]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ต้องไม่มีการเปล … [ย่อจาก30,586ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route:knowledge expected:['competition_rules']","validation_rejected"]

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
    "competition_id",
    "section_number",
    "facet",
    "heading",
    "text",
    "depends_on_ids",
    "completeness",
    "details"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=496
