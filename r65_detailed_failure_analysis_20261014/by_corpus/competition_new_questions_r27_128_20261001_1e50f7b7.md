# data/eval/competition_new_questions_r27_128_20261001.json

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 118/128 | 10 | 0 | 10 |

## ตัวอย่าง legacy_offline: bb275f63996edb17d5900874e03d273506e2008024e2b1a258cf0ade7da69ebf

คำถาม: Under CS2 tournamment rules, are team member changes permitted during the event?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-roster-change-en-1","anchor":"cs2-roster-change-en","locale":"en","game":"cs2","question":"Under CS2 tournamment rules, are team member changes permitted during the event?","required_clauses":["No team member changes are allowed during the competition period"],"source_id":"competition_rules_cs2_psu_phuket_2026_s11_c01","source_sha256":"8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f","status":"answer","first_clause":true,"mutation":"task_duplication","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:service_fact_scope_clarification / clarification / 0.98

Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:No team member changes are allowed during the competition period","first_line_off_topic","wrong_game_evidence"]

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

raw source: legacy_offline\RESULTS.jsonl record1=1320

## ตัวอย่าง legacy_offline: ed31f6cde85df43da32ef2b7ca22170becf7b17c4fb7e6fec62f5309a29797ca

คำถาม: Under CS2 tournamment ruls, are team member changes permitted during the event?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-roster-change-en-2","anchor":"cs2-roster-change-en","locale":"en","game":"cs2","question":"Under CS2 tournamment ruls, are team member changes permitted during the event?","required_clauses":["No team member changes are allowed during the competition period"],"source_id":"competition_rules_cs2_psu_phuket_2026_s11_c01","source_sha256":"8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f","status":"answer","first_clause":true,"mutation":"two_task_errors","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:service_fact_scope_clarification / clarification / 0.98

Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:No team member changes are allowed during the competition period","first_line_off_topic","wrong_game_evidence"]

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

raw source: legacy_offline\RESULTS.jsonl record1=1321
| common_offline | 0/128 | 128 | 0 | 126 |

## ตัวอย่าง common_offline: f02e70f7fea834ea7aff33049cea32130c6a5fd5e9c15f094f29f4b2299cd94d

คำถาม: ตามกติกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-protest-th-0","anchor":"cs2-protest-th","locale":"th","game":"cs2","question":"ตามกติกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร","required_clauses":["2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น"],"source_id":"competition_rules_cs2_psu_phuket_2026_s58_c01","source_sha256":"623c43aa2f79f6a6e1bbbecdff08845436dc50a9e857876d46d53cabd094f09d","status":"answer","first_clause":true,"mutation":"new_clean","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ Counter-Strike 2 เช่น เลขข้อจากเอกสารเดิม / หมวดของกติกาข้อนี้ / หัวข้อกติกา / ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ?

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น","first_line_off_topic","wrong_game_evidence"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "competition_competition_rules_tekken8_psu_esports_section_002",
    "controls_pc_counter_strike_2"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "ตาม โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_offline_resumed\RESULTS.jsonl record1=127

## ตัวอย่าง common_offline: a9df2e668bebbdca5079ae4dec4875bb90cd91c523e88e254f09bce00837b41d

คำถาม: ตามกติกกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-protest-th-1","anchor":"cs2-protest-th","locale":"th","game":"cs2","question":"ตามกติกกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร","required_clauses":["2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น"],"source_id":"competition_rules_cs2_psu_phuket_2026_s58_c01","source_sha256":"623c43aa2f79f6a6e1bbbecdff08845436dc50a9e857876d46d53cabd094f09d","status":"answer","first_clause":true,"mutation":"task_duplication","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ PSU Phuket CS2 2026 Tournament เช่น ชื่อรายการ+ปี+ประเภทให้ตรง / ฉบับกติกาและวันที่ / เอกสารกติกาครบหรือมีเพียงบางส่วน?

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น","first_line_off_topic","wrong_game_evidence"]

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
    "ตามกติกกาการแข่งขัน โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_offline_resumed\RESULTS.jsonl record1=128
| legacy_llm | 117/128 | 11 | 0 | 11 |

## ตัวอย่าง legacy_llm: bb275f63996edb17d5900874e03d273506e2008024e2b1a258cf0ade7da69ebf

คำถาม: Under CS2 tournamment rules, are team member changes permitted during the event?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-roster-change-en-1","anchor":"cs2-roster-change-en","locale":"en","game":"cs2","question":"Under CS2 tournamment rules, are team member changes permitted during the event?","required_clauses":["No team member changes are allowed during the competition period"],"source_id":"competition_rules_cs2_psu_phuket_2026_s11_c01","source_sha256":"8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f","status":"answer","first_clause":true,"mutation":"task_duplication","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:service_fact_scope_clarification / clarification / 0.98

Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:No team member changes are allowed during the competition period","first_line_off_topic","wrong_game_evidence"]

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

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=393

## ตัวอย่าง legacy_llm: ed31f6cde85df43da32ef2b7ca22170becf7b17c4fb7e6fec62f5309a29797ca

คำถาม: Under CS2 tournamment ruls, are team member changes permitted during the event?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-roster-change-en-2","anchor":"cs2-roster-change-en","locale":"en","game":"cs2","question":"Under CS2 tournamment ruls, are team member changes permitted during the event?","required_clauses":["No team member changes are allowed during the competition period"],"source_id":"competition_rules_cs2_psu_phuket_2026_s11_c01","source_sha256":"8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f","status":"answer","first_clause":true,"mutation":"two_task_errors","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:service_fact_scope_clarification / clarification / 0.98

Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:No team member changes are allowed during the competition period","first_line_off_topic","wrong_game_evidence"]

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

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=394
| common_llm | 12/128 | 116 | 0 | 116 |

## ตัวอย่าง common_llm: f02e70f7fea834ea7aff33049cea32130c6a5fd5e9c15f094f29f4b2299cd94d

คำถาม: ตามกติกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-protest-th-0","anchor":"cs2-protest-th","locale":"th","game":"cs2","question":"ตามกติกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร","required_clauses":["2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น"],"source_id":"competition_rules_cs2_psu_phuket_2026_s58_c01","source_sha256":"623c43aa2f79f6a6e1bbbecdff08845436dc50a9e857876d46d53cabd094f09d","status":"answer","first_clause":true,"mutation":"new_clean","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ Counter-Strike 2 เช่น เลขข้อจากเอกสารเดิม / หมวดของกติกาข้อนี้ / หัวข้อกติกา / ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ?

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น","first_line_off_topic","wrong_game_evidence"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "competition_competition_rules_tekken8_psu_esports_section_002",
    "controls_pc_counter_strike_2"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "ตาม โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร"
  ],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=340

## ตัวอย่าง common_llm: a9df2e668bebbdca5079ae4dec4875bb90cd91c523e88e254f09bce00837b41d

คำถาม: ตามกติกกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-new-cs2-protest-th-1","anchor":"cs2-protest-th","locale":"th","game":"cs2","question":"ตามกติกกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร","required_clauses":["2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น"],"source_id":"competition_rules_cs2_psu_phuket_2026_s58_c01","source_sha256":"623c43aa2f79f6a6e1bbbecdff08845436dc50a9e857876d46d53cabd094f09d","status":"answer","first_clause":true,"mutation":"task_duplication","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ PSU Phuket CS2 2026 Tournament เช่น ชื่อรายการ+ปี+ประเภทให้ตรง / ฉบับกติกาและวันที่ / เอกสารกติกาครบหรือมีเพียงบางส่วน?

Failures: ["outcome_mismatch","route_mismatch","missing_complete_clause:2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น","first_line_off_topic","wrong_game_evidence"]

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
    "ตามกติกกาการแข่งขัน โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร"
  ],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=341
