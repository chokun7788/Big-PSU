# data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 3250/4000 | 750 | 216 | 84 |

## ตัวอย่าง legacy_offline: eecef5dc365df720847751fcae764df4e15073cf30ad971006dbe0338635674f

คำถาม: ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง","domain":"competition_rules","edit_actions":["repeat"],"edit_recipe":"repeat","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04012","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"ตาม rulebook เคาน์เเตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s35_c01","canonical::competition_rules_cs2_psu_phuket_2026_s36_c01","canonical::competition_rules_cs2_psu_phuket_2026_s54_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง"}
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

raw source: legacy_offline\RESULTS.jsonl record1=1412

## ตัวอย่าง legacy_offline: 97485d095dd9374751d4213295953447d1882a2188f34544fb0a761003547475

คำถาม: ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย","domain":"competition_rules","edit_actions":["transpose"],"edit_recipe":"transpose","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04039","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"ขออ้างอิงกตกิา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s30_c01","canonical::competition_rules_cs2_psu_phuket_2026_s33_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย"}
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

raw source: legacy_offline\RESULTS.jsonl record1=1469
| common_offline | 1362/4000 | 2638 | 398 | 844 |

## ตัวอย่าง common_offline: eecef5dc365df720847751fcae764df4e15073cf30ad971006dbe0338635674f

คำถาม: ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง","domain":"competition_rules","edit_actions":["repeat"],"edit_recipe":"repeat","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04012","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"ตาม rulebook เคาน์เเตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s35_c01","canonical::competition_rules_cs2_psu_phuket_2026_s36_c01","canonical::competition_rules_cs2_psu_phuket_2026_s54_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง"}
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
    "ตาม rulebook มารยาท",
    "พฤติกรรมผู้เล่น ต้องทำยังไง"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded\RESULTS.jsonl record1=68

## ตัวอย่าง common_offline: bee04018586cf89f2c999924fc82a2f2aac3066b64993c22f4f28a0439a5a368

คำถาม: ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อคุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน หน่อย

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อคุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน หน่อย","domain":"competition_rules","edit_actions":["repeat"],"edit_recipe":"repeat","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04021","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"ขออ้างอิงกติกา เคาน์เตตอร์สไตรก์ 2 ในหัวข้อคุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน หน่อย","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s12_c01","canonical::competition_rules_cs2_psu_phuket_2026_s16_c01","canonical::competition_rules_cs2_psu_phuket_2026_s17_c01","canonical::competition_rules_cs2_psu_phuket_2026_s57_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อคุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน หน่อย"}
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
    "ขออ้างอิงกติกา ในหัวข้อคุณสมบัติ รายชื่อผู้เล่น",
    "การลงทะเบียน หน่อย"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded\RESULTS.jsonl record1=89
| legacy_llm | 3250/4000 | 750 | 220 | 83 |

## ตัวอย่าง legacy_llm: eecef5dc365df720847751fcae764df4e15073cf30ad971006dbe0338635674f

คำถาม: ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง","domain":"competition_rules","edit_actions":["repeat"],"edit_recipe":"repeat","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04012","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"ตาม rulebook เคาน์เเตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s35_c01","canonical::competition_rules_cs2_psu_phuket_2026_s36_c01","canonical::competition_rules_cs2_psu_phuket_2026_s54_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"ตาม rulebook เคาน์เตอร์สไตรก์ 2 มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง"}
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

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=485

## ตัวอย่าง legacy_llm: 97485d095dd9374751d4213295953447d1882a2188f34544fb0a761003547475

คำถาม: ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย","domain":"competition_rules","edit_actions":["transpose"],"edit_recipe":"transpose","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04039","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"ขออ้างอิงกตกิา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s30_c01","canonical::competition_rules_cs2_psu_phuket_2026_s33_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย"}
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

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=542
| common_llm | 982/4000 | 3018 | 1788 | 727 |

## ตัวอย่าง common_llm: 19342d941b926dcbf2ac59b29796fbd0141d1b2d009aff1a2db911275b2a6179

คำถาม: Counter-Strike 2 มีข้อกำหนดเรื่องการแก้ปัญหาข้อพิพาท ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"Counter-Strike 2 มีข้อกำหนดเรื่องการแก้ปัญหาข้อพิพาท ไหม","domain":"competition_rules","edit_actions":["delete"],"edit_recipe":"delete","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04089","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"Counter-Strike 2 มีข้อกำหนดเรื่องการแก้ปัญหาข้อพิพาท หม","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s06_c01","canonical::competition_rules_cs2_psu_phuket_2026_s58_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"Counter-Strike 2 มีข้อกำหนดเรื่องการแก้ปัญหาข้อพิพาท ไหม"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

details: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["route:knowledge expected:['competition_rules']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_cs2",
    "competition_competition_rules_cs2_psu_phuket_2026",
    "competition_competition_rules_tekken8_psu_esports_section_008",
    "controls_pc_counter_strike_2",
    "availability_pc_01_02",
    "availability_pc_03_10"
  ],
  "requested_fields": [
    "details"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=640

## ตัวอย่าง common_llm: 8657d0a9d29d66510d1a4de15deb998edf7e41548df3bff351df821dac275610

คำถาม: Counter-Strike 2 มีข้อกำหนดเรื่องจำนวนผู้เล่นต่อทีม ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":[]},"clean_question":"Counter-Strike 2 มีข้อกำหนดเรื่องจำนวนผู้เล่นต่อทีม ไหม","domain":"competition_rules","edit_actions":["neighbor","delete"],"edit_recipe":"mixed","expected_answer_status":"answer_available","expected_route_categories":["competition_rules"],"expected_target":"cs2","id":"MASTER-GT-TH-04113","latency_ceiling_sec":20.0,"locale":"th","metadata":{"case_type":"facet_targeted_retrieval","rag_required":true,"source_gap_manifest_key":""},"noisy_question":"Counter-Strike 2 มีข้อกำหนดรื่องจำนวรผู้เล่นต่อทีม ไหม","protected_literals":["2"],"review_status":"source_grounded_gold_candidate","source_contract":{"live_dependency":false,"requirement":"target_and_facet_grounded_rulebook","source_ids":["canonical::competition_rules_cs2_psu_phuket_2026_s18_c01","canonical::competition_rules_cs2_psu_phuket_2026_s23_c01","competition_rules_cs2_psu_phuket_2026"],"source_urls":["local://competition_rules/competition_rules_cs2_psu_phuket_2026"]},"source_fixture":"master_ground_truth_bilingual_10000_v2.jsonl","synthetic_seed":20260929,"question":"Counter-Strike 2 มีข้อกำหนดเรื่องจำนวนผู้เล่นต่อทีม ไหม"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

ยังไม่มีข้อมูลยืนยันในส่วน รูปแบบเล่นและเล่นกับเพื่อน สำหรับขอบเขตนี้

**PC #01-#02**
• จำนวนคนสูงสุดของบริการ: 1 [S1]

**PC #01**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S2]

**PC #02**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S3]

**PC Zone**
• จำนวนที่นั่งในพื้นที่ (ไม่ใช่จำนวนผู้เล่นต่อเครื่อง): ยังไม่มีข้อมูลยืนยัน

**PC #03-#10**
• จำนวนคนสูงสุดของบริการ: 1 [S4]

**PC #03**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S5]

**PC #04**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S6]

**PC #05**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S7]

**PC #06**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S8]

**PC #07**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S9]

**PC #08**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S10]

**PC #09**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S11]

**PC #10**
• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S12]

details: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

players_max: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

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
    "details",
    "capacity_max",
    "capacity_persons",
    "room_seats",
    "players_max"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=688
