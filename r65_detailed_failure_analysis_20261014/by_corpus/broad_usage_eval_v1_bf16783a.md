# data/eval/broad_usage_eval_v1.json

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 462/651 | 189 | 118 | 16 |

## ตัวอย่าง legacy_offline: ea7c18d808e4d31bd75058b1f40b7b00e341186735cd0204d9d6003d5ffc4f99

คำถาม: Gran Turismo 7 ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"service_fee","question":"Gran Turismo 7 ราคาเท่าไหร่","expected_category":"service_fee","expected_mode_prefix":null,"must_contain":["Gran Turismo 7"],"must_contain_any":[],"must_not_contain":["Local LLM"],"note":"","risk":"high","id":"SF-070","locale":"auto"}
```

Actual mode/category/confidence: pipeline:protected_price_missing_service / clarification / 0.98

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

Failures: ["route:clarification expected:['service_fee']","missing required: Gran Turismo 7"]

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

raw source: legacy_offline\RESULTS.jsonl record1=95

## ตัวอย่าง legacy_offline: df0862cc3989efc95d784dc3e7297aa555ba4805c62dfc0c0c2584db2b7e1c34

คำถาม: Nintendo Switch Sports ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"service_fee","question":"Nintendo Switch Sports ราคาเท่าไหร่","expected_category":"service_fee","expected_mode_prefix":null,"must_contain":["Nintendo Switch Sports"],"must_contain_any":[],"must_not_contain":["Local LLM"],"note":"","risk":"high","id":"SF-083","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

Nintendo Switch — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 140 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Failures: ["missing required: Nintendo Switch Sports"]

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

raw source: legacy_offline\RESULTS.jsonl record1=108
| common_offline | 130/651 | 521 | 252 | 258 |

## ตัวอย่าง common_offline: 79b2401eff53b05f468c364be57a2cb1f7c7529433fac8a88ad592dc639b4298

คำถาม: TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"game_controls","question":"TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง","expected_category":"games","expected_mode_prefix":"pipeline:structured_game_controls","must_contain":["TEKKEN 8","ปุ่ม"],"must_contain_any":[],"must_not_contain":["Local LLM"],"note":"","risk":"medium","id":"GC-125","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**เทคเคน 8**
• ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม: ยังไม่มีข้อมูลยืนยัน
• แพลตฟอร์ม เช่น PC หรือ PS5: PlayStation / PS5 [S1]
• อุปกรณ์ควบคุม: ยังไม่มีข้อมูลยืนยัน
• ชื่อชุดปุ่ม เช่น default: ยังไม่มีข้อมูลยืนยัน

Failures: ["route:knowledge expected:['games']","missing required: TEKKEN 8","legacy_mode_prefix:['pipeline:structured_game_controls']"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_tekken_8",
    "competition_competition_rules_tekken8_psu_esports",
    "controls_ps5_tekken_8",
    "availability_pc_01_02",
    "availability_ps5_01_02"
  ],
  "requested_fields": [
    "bindings"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_offline\RESULTS.jsonl record1=10

## ตัวอย่าง common_offline: dbda06de43cf51b76a922aaa1ee2e86deb601ee1bd51f804b0eee0435b0a564d

คำถาม: General Adult เล่น VR 1 ชั่วโมงกี่บาท

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"service_fee","question":"General Adult เล่น VR 1 ชั่วโมงกี่บาท","expected_category":"service_fee","expected_mode_prefix":null,"must_contain":[],"must_contain_any":["บาท","ต่างกัน","ฟรี","0 บาท"],"must_not_contain":["Local LLM"],"note":"","risk":"medium","id":"SF-057","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

amount_minor: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["route:knowledge expected:['service_fee']","missing all alternatives: ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท']"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "audience_general_adult"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": "VR",
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_offline\RESULTS.jsonl record1=82
| legacy_llm | 458/651 | 193 | 119 | 18 |

## ตัวอย่าง legacy_llm: ea7c18d808e4d31bd75058b1f40b7b00e341186735cd0204d9d6003d5ffc4f99

คำถาม: Gran Turismo 7 ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"service_fee","question":"Gran Turismo 7 ราคาเท่าไหร่","expected_category":"service_fee","expected_mode_prefix":null,"must_contain":["Gran Turismo 7"],"must_contain_any":[],"must_not_contain":["Local LLM"],"note":"","risk":"high","id":"SF-070","locale":"auto"}
```

Actual mode/category/confidence: pipeline:protected_price_missing_service / clarification / 0.98

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

Failures: ["route:clarification expected:['service_fee']","missing required: Gran Turismo 7"]

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=95

## ตัวอย่าง legacy_llm: df0862cc3989efc95d784dc3e7297aa555ba4805c62dfc0c0c2584db2b7e1c34

คำถาม: Nintendo Switch Sports ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"service_fee","question":"Nintendo Switch Sports ราคาเท่าไหร่","expected_category":"service_fee","expected_mode_prefix":null,"must_contain":["Nintendo Switch Sports"],"must_contain_any":[],"must_not_contain":["Local LLM"],"note":"","risk":"high","id":"SF-083","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

Nintendo Switch — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 140 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Failures: ["missing required: Nintendo Switch Sports"]

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=108
| common_llm | 84/651 | 567 | 341 | 214 |

## ตัวอย่าง common_llm: 79b2401eff53b05f468c364be57a2cb1f7c7529433fac8a88ad592dc639b4298

คำถาม: TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"game_controls","question":"TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง","expected_category":"games","expected_mode_prefix":"pipeline:structured_game_controls","must_contain":["TEKKEN 8","ปุ่ม"],"must_contain_any":[],"must_not_contain":["Local LLM"],"note":"","risk":"medium","id":"GC-125","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**เทคเคน 8**
• ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม: ยังไม่มีข้อมูลยืนยัน
• แพลตฟอร์ม เช่น PC หรือ PS5: PlayStation / PS5 [S1]
• อุปกรณ์ควบคุม: ยังไม่มีข้อมูลยืนยัน
• ชื่อชุดปุ่ม เช่น default: ยังไม่มีข้อมูลยืนยัน

Failures: ["route:knowledge expected:['games']","missing required: TEKKEN 8","legacy_mode_prefix:['pipeline:structured_game_controls']"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_tekken_8",
    "competition_competition_rules_tekken8_psu_esports",
    "controls_ps5_tekken_8",
    "availability_pc_01_02",
    "availability_ps5_01_02"
  ],
  "requested_fields": [
    "bindings"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix\common_RESULTS.jsonl.gz record1=10

## ตัวอย่าง common_llm: dbda06de43cf51b76a922aaa1ee2e86deb601ee1bd51f804b0eee0435b0a564d

คำถาม: General Adult เล่น VR 1 ชั่วโมงกี่บาท

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"kind":"single","group":"service_fee","question":"General Adult เล่น VR 1 ชั่วโมงกี่บาท","expected_category":"service_fee","expected_mode_prefix":null,"must_contain":[],"must_contain_any":["บาท","ต่างกัน","ฟรี","0 บาท"],"must_not_contain":["Local LLM"],"note":"","risk":"medium","id":"SF-057","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

**ค่าบริการ**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้

amount_minor: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["route:knowledge expected:['service_fee']","missing all alternatives: ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท']"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "audience_general_adult"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": "VR",
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix\common_RESULTS.jsonl.gz record1=82
