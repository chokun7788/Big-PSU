# data/eval/real_usage_golden_v1.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 12/24 | 12 | 2 | 9 |

## ตัวอย่าง legacy_offline: 87c8aa36571ba4c176998a9d7f2e8bae1351bb267eb5c0dfb1b848bfaa13e1bb

คำถาม: ราคา PC กับ PS5 ต่างกันเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-SF-004","group":"service_fee","question":"ราคา PC กับ PS5 ต่างกันเท่าไหร่","expected_category":"service_fee","expected_intent":"service_fee_query","must_contain":["ต่างกันดังนี้","PlayStation 5 60 นาที แพงกว่า 25 บาท","PlayStation 5 60 นาที แพงกว่า 80 บาท"],"must_not_contain":["ยังไม่พบราคา","Local LLM"],"source_keywords":["SERVICE-FEE","pc_service_fee_local_update_20260727"],"notes":"comparison question must answer the difference, not only list tables","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_comparison / service_fee / 0.98

ราคาต่อแพ็กเกจของทุกบริการที่ถาม:

PC (1 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท
•    บุคคลทั่วไป (General Adult): 70 บาท

PlayStation 5 (1-2 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท
•    บุคคลทั่วไป (General Adult): 150 บาท
แพ็กเกจมีระยะเวลาและจำนวนผู้เล่นต่างกัน ต้องการเทียบสำหรับกลุ่มผู้ใช้ใด เล่นนานเท่าไร และกี่คนครับ?
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["missing required: ต่างกันดังนี้","missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท","missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท"]

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

raw source: legacy_offline\RESULTS.jsonl record1=76

## ตัวอย่าง legacy_offline: e66e39ac690211e827093b69f911b2dca390f9a5f26e5ab0edb42b12b6677e93

คำถาม: ROV รอบชิงเล่นกี่เกม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-COMP-001","group":"competition_rules","question":"ROV รอบชิงเล่นกี่เกม","expected_category":"competition_rules","expected_intent":"competition_rules_lookup","must_contain":["RoV","BO3"],"must_not_contain":["เกมที่ยืนยันได้ทั้งหมด 44 เกม","Nintendo Switch Zone","Local LLM"],"source_keywords":["competition_rules"],"notes":"competition rule must not become game catalog","locale":"auto"}
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

raw source: legacy_offline\RESULTS.jsonl record1=625
| common_offline | 6/24 | 18 | 1 | 16 |

## ตัวอย่าง common_offline: 87c8aa36571ba4c176998a9d7f2e8bae1351bb267eb5c0dfb1b848bfaa13e1bb

คำถาม: ราคา PC กับ PS5 ต่างกันเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-SF-004","group":"service_fee","question":"ราคา PC กับ PS5 ต่างกันเท่าไหร่","expected_category":"service_fee","expected_intent":"service_fee_query","must_contain":["ต่างกันดังนี้","PlayStation 5 60 นาที แพงกว่า 25 บาท","PlayStation 5 60 นาที แพงกว่า 80 บาท"],"must_not_contain":["ยังไม่พบราคา","Local LLM"],"source_keywords":["SERVICE-FEE","pc_service_fee_local_update_20260727"],"notes":"comparison question must answer the difference, not only list tables","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_comparison / service_fee / 0.98

ราคาต่อแพ็กเกจของทุกบริการที่ถาม:

PC (1 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท
•    บุคคลทั่วไป (General Adult): 70 บาท

PlayStation 5 (1-2 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท
•    บุคคลทั่วไป (General Adult): 150 บาท
แพ็กเกจมีระยะเวลาและจำนวนผู้เล่นต่างกัน ต้องการเทียบสำหรับกลุ่มผู้ใช้ใด เล่นนานเท่าไร และกี่คนครับ?
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["missing required: ต่างกันดังนี้","missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท","missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท"]

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

raw source: common_offline\RESULTS.jsonl record1=76

## ตัวอย่าง common_offline: e66e39ac690211e827093b69f911b2dca390f9a5f26e5ab0edb42b12b6677e93

คำถาม: ROV รอบชิงเล่นกี่เกม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-COMP-001","group":"competition_rules","question":"ROV รอบชิงเล่นกี่เกม","expected_category":"competition_rules","expected_intent":"competition_rules_lookup","must_contain":["RoV","BO3"],"must_not_contain":["เกมที่ยืนยันได้ทั้งหมด 44 เกม","Nintendo Switch Zone","Local LLM"],"source_keywords":["competition_rules"],"notes":"competition rule must not become game catalog","locale":"auto"}
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

raw source: common_offline\RESULTS.jsonl record1=625
| legacy_llm | 12/24 | 12 | 2 | 9 |

## ตัวอย่าง legacy_llm: 87c8aa36571ba4c176998a9d7f2e8bae1351bb267eb5c0dfb1b848bfaa13e1bb

คำถาม: ราคา PC กับ PS5 ต่างกันเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-SF-004","group":"service_fee","question":"ราคา PC กับ PS5 ต่างกันเท่าไหร่","expected_category":"service_fee","expected_intent":"service_fee_query","must_contain":["ต่างกันดังนี้","PlayStation 5 60 นาที แพงกว่า 25 บาท","PlayStation 5 60 นาที แพงกว่า 80 บาท"],"must_not_contain":["ยังไม่พบราคา","Local LLM"],"source_keywords":["SERVICE-FEE","pc_service_fee_local_update_20260727"],"notes":"comparison question must answer the difference, not only list tables","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_comparison / service_fee / 0.98

ราคาต่อแพ็กเกจของทุกบริการที่ถาม:

PC (1 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท
•    บุคคลทั่วไป (General Adult): 70 บาท

PlayStation 5 (1-2 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท
•    บุคคลทั่วไป (General Adult): 150 บาท
แพ็กเกจมีระยะเวลาและจำนวนผู้เล่นต่างกัน ต้องการเทียบสำหรับกลุ่มผู้ใช้ใด เล่นนานเท่าไร และกี่คนครับ?
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["missing required: ต่างกันดังนี้","missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท","missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท"]

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=76

## ตัวอย่าง legacy_llm: e66e39ac690211e827093b69f911b2dca390f9a5f26e5ab0edb42b12b6677e93

คำถาม: ROV รอบชิงเล่นกี่เกม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-COMP-001","group":"competition_rules","question":"ROV รอบชิงเล่นกี่เกม","expected_category":"competition_rules","expected_intent":"competition_rules_lookup","must_contain":["RoV","BO3"],"must_not_contain":["เกมที่ยืนยันได้ทั้งหมด 44 เกม","Nintendo Switch Zone","Local LLM"],"source_keywords":["competition_rules"],"notes":"competition rule must not become game catalog","locale":"auto"}
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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=625
| common_llm | 4/24 | 20 | 1 | 18 |

## ตัวอย่าง common_llm: 87c8aa36571ba4c176998a9d7f2e8bae1351bb267eb5c0dfb1b848bfaa13e1bb

คำถาม: ราคา PC กับ PS5 ต่างกันเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-SF-004","group":"service_fee","question":"ราคา PC กับ PS5 ต่างกันเท่าไหร่","expected_category":"service_fee","expected_intent":"service_fee_query","must_contain":["ต่างกันดังนี้","PlayStation 5 60 นาที แพงกว่า 25 บาท","PlayStation 5 60 นาที แพงกว่า 80 บาท"],"must_not_contain":["ยังไม่พบราคา","Local LLM"],"source_keywords":["SERVICE-FEE","pc_service_fee_local_update_20260727"],"notes":"comparison question must answer the difference, not only list tables","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_comparison / service_fee / 0.98

ราคาต่อแพ็กเกจของทุกบริการที่ถาม:

PC (1 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท
•    บุคคลทั่วไป (General Adult): 70 บาท

PlayStation 5 (1-2 คน), 60 นาที/รอบ
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท
•    บุคคลทั่วไป (General Adult): 150 บาท
แพ็กเกจมีระยะเวลาและจำนวนผู้เล่นต่างกัน ต้องการเทียบสำหรับกลุ่มผู้ใช้ใด เล่นนานเท่าไร และกี่คนครับ?
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["missing required: ต่างกันดังนี้","missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท","missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท"]

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

raw source: model_matrix\common_RESULTS.jsonl.gz record1=76

## ตัวอย่าง common_llm: e93ede3646ad4723e76ff4136930ac469d649d29a64462f9f17f5df8e6b69211

คำถาม: อุปกรณ์ไหนเกมเยอะสุด

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-GM-003","group":"games","question":"อุปกรณ์ไหนเกมเยอะสุด","expected_category":"games","expected_intent":"list","expected_mode_prefix":"pipeline:structured_game_zone_ranking","must_contain":["PlayStation 5 Zone และ Nintendo Switch Zone มีเกมเยอะสุด","17 เกม","PC Zone"],"must_not_contain":["Gaming PC รุ่น","อุปกรณ์ใน PC Zone","Local LLM"],"source_keywords":["our-games"],"notes":"ranking question must calculate current game counts by zone","locale":"auto"}
```

Actual mode/category/confidence: pipeline:request_timeout_no_answer / no_answer / 0.45

ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง
ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ

Failures: ["route:no_answer expected:['games']","missing required: PlayStation 5 Zone และ Nintendo Switch Zone มีเกมเยอะสุด","missing required: 17 เกม","missing required: PC Zone","legacy_mode_prefix:['pipeline:structured_game_zone_ranking']","intent:request_timeout expected:list","latency_ceiling"]

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

raw source: model_matrix\common_RESULTS.jsonl.gz record1=264
