# data/ground_truth/ground_truth_competition_rules_v1_228.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 0/228 | 228 | 97 | 0 |

## ตัวอย่าง legacy_offline: 35e997ccc7addf358b42c750545c91bd6c3b991d9adfdca5e12b21e48bb88593

คำถาม: CS2 แข่งทีมละกี่คน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_001","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"CS2 แข่งทีมละกี่คน","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=14335

## ตัวอย่าง legacy_offline: e690992b840535f89972f494b7b4a656a39002131b7368a71b85f53dc21f581c

คำถาม: Counter-Strike 2 ทีมละกี่คนตามกติกา

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_002","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"Counter-Strike 2 ทีมละกี่คนตามกติกา","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=14336
| common_offline | 0/228 | 228 | 162 | 18 |

## ตัวอย่าง common_offline: fb5d450e2ed6a333742588038f8adf3bafcdac2e4ba2953e65b48ab496bd1023

คำถาม: CS2 สมาชิกทีมต้องมีกี่คน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_004","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"CS2 สมาชิกทีมต้องมีกี่คน","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

ยังไม่มีข้อมูลยืนยันในส่วน รูปแบบเล่นและเล่นกับเพื่อน สำหรับขอบเขตนี้

players_max: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["legacy_mode_prefix:['pipeline:competition_fact_card']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "controls_pc_counter_strike_2"
  ],
  "requested_fields": [
    "players_max"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=17819

## ตัวอย่าง common_offline: 8860421991693c0866be24c9cdd34a07051c91135902771cbc9b79fe7a86f1d5

คำถาม: CS2 roster ผู้เล่นหลักมีกี่คน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_006","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"CS2 roster ผู้เล่นหลักมีกี่คน","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

ยังไม่มีข้อมูลยืนยันในส่วน รูปแบบเล่นและเล่นกับเพื่อน สำหรับขอบเขตนี้

players_max: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["legacy_mode_prefix:['pipeline:competition_fact_card']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "controls_pc_counter_strike_2"
  ],
  "requested_fields": [
    "players_max"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=17821
| legacy_llm | 0/228 | 228 | 96 | 0 |

## ตัวอย่าง legacy_llm: 35e997ccc7addf358b42c750545c91bd6c3b991d9adfdca5e12b21e48bb88593

คำถาม: CS2 แข่งทีมละกี่คน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_001","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"CS2 แข่งทีมละกี่คน","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=18554

## ตัวอย่าง legacy_llm: e690992b840535f89972f494b7b4a656a39002131b7368a71b85f53dc21f581c

คำถาม: Counter-Strike 2 ทีมละกี่คนตามกติกา

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_002","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"Counter-Strike 2 ทีมละกี่คนตามกติกา","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=18555
| common_llm | 0/228 | 228 | 155 | 32 |

## ตัวอย่าง common_llm: fb5d450e2ed6a333742588038f8adf3bafcdac2e4ba2953e65b48ab496bd1023

คำถาม: CS2 สมาชิกทีมต้องมีกี่คน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_004","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"CS2 สมาชิกทีมต้องมีกี่คน","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

ยังไม่มีข้อมูลยืนยันในส่วน รูปแบบเล่นและเล่นกับเพื่อน สำหรับขอบเขตนี้

players_max: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["legacy_mode_prefix:['pipeline:competition_fact_card']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "controls_pc_counter_strike_2"
  ],
  "requested_fields": [
    "players_max"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=18558

## ตัวอย่าง common_llm: 38517cb1370173bfcb1950c771fcf1f84fe31e47ef3b85ceb6516ccd888e2e55

คำถาม: CS2 ลงแข่งพร้อมกันกี่คน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"competition_v1_005","category":"competition_rules","game":"Counter-Strike 2","intent":"team_size","question":"CS2 ลงแข่งพร้อมกันกี่คน","expected_keywords":["CS2","ผู้เล่น 5 คน"],"expected_source_keywords":["competition_rules_cs2_psu_phuket_2026"],"answer_type":"fact","difficulty":"medium","variant_type":"competition_team_size","source_fact_key":"cs2_team_size","expected_mode_prefix":"pipeline:competition_fact_card","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

**PSU Phuket CS2 2026 Tournament**
• ประเภทหรือกลุ่มการแข่งขัน: ยังไม่มีข้อมูลยืนยัน
• ฉบับกติกาและวันที่: competition_rules_cs2_psu_phuket_2026 [S1]
• วันที่จัดการแข่งขันตามต้นทาง: ยังไม่มีข้อมูลยืนยัน
• เอกสารกติกาครบหรือมีเพียงบางส่วน: ยังไม่มีข้อมูลยืนยัน
• เลือกฉบับกติกาก่อนหน้า (ถ้ามี): ยังไม่มีข้อมูลยืนยัน

competition_id: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["legacy_mode_prefix:['pipeline:competition_fact_card']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "competition_id",
    "division",
    "rulebook_release",
    "competition_dates",
    "coverage",
    "supersedes_id"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=18559
