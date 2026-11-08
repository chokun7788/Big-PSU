# data/eval/user_question_bank_400.json

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 318/400 | 82 | 0 | 0 |

## ตัวอย่าง legacy_offline: ebbf7d37ad921cde9faeba4f0cb95ac7f1dd60483d1654951c73f2f30e0b0a0f

คำถาม: VALORANT มีตัวสำรองได้ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"GR-030","category":"game_rules","question_no":30,"question":"VALORANT มีตัวสำรองได้ไหม","expected_support":"competition_rules","note":"มีทั้งข้อมูลเกมและกติกาบางส่วน","locale":"auto"}
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

raw source: legacy_offline\RESULTS.jsonl record1=566

## ตัวอย่าง legacy_offline: 66905e0e99e1e822468a1e8ffa26e008ce4aa774f6360b06f29beb00bfabd7bf

คำถาม: VALORANT ต้องเช็คอินก่อนแข่งไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"GR-045","category":"game_rules","question_no":45,"question":"VALORANT ต้องเช็คอินก่อนแข่งไหม","expected_support":"competition_rules","note":"มีทั้งข้อมูลเกมและกติกาบางส่วน","locale":"auto"}
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

raw source: legacy_offline\RESULTS.jsonl record1=569
| common_offline | 368/400 | 32 | 0 | 3 |

## ตัวอย่าง common_offline: 3cda0c69a1e28556c2fd6534082dc5697d012129a74b8d64fb74813cddf7d2e0

คำถาม: Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"PBC-095","category":"play_booking_controls","question_no":95,"question":"Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง","expected_support":"game_controls_or_clarification","note":"","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

ยังไม่มีข้อมูลยืนยันในส่วน วิธีเล่นและปุ่ม สำหรับขอบเขตนี้

bindings: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_overcooked_2"
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

raw source: common_offline\RESULTS.jsonl record1=367

## ตัวอย่าง common_offline: e66e39ac690211e827093b69f911b2dca390f9a5f26e5ab0edb42b12b6677e93

คำถาม: ROV รอบชิงเล่นกี่เกม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"GR-013","category":"game_rules","question_no":13,"question":"ROV รอบชิงเล่นกี่เกม","expected_support":"competition_rules","note":"มีข้อมูลกติกาการแข่งขัน แต่ไม่ใช่เกมใน catalog เล่นของศูนย์","locale":"auto"}
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
| legacy_llm | 320/400 | 80 | 0 | 0 |

## ตัวอย่าง legacy_llm: ebbf7d37ad921cde9faeba4f0cb95ac7f1dd60483d1654951c73f2f30e0b0a0f

คำถาม: VALORANT มีตัวสำรองได้ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"GR-030","category":"game_rules","question_no":30,"question":"VALORANT มีตัวสำรองได้ไหม","expected_support":"competition_rules","note":"มีทั้งข้อมูลเกมและกติกาบางส่วน","locale":"auto"}
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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=566

## ตัวอย่าง legacy_llm: 66905e0e99e1e822468a1e8ffa26e008ce4aa774f6360b06f29beb00bfabd7bf

คำถาม: VALORANT ต้องเช็คอินก่อนแข่งไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"GR-045","category":"game_rules","question_no":45,"question":"VALORANT ต้องเช็คอินก่อนแข่งไหม","expected_support":"competition_rules","note":"มีทั้งข้อมูลเกมและกติกาบางส่วน","locale":"auto"}
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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=569
| common_llm | 368/400 | 32 | 0 | 19 |

## ตัวอย่าง common_llm: 3cda0c69a1e28556c2fd6534082dc5697d012129a74b8d64fb74813cddf7d2e0

คำถาม: Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"PBC-095","category":"play_booking_controls","question_no":95,"question":"Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง","expected_support":"game_controls_or_clarification","note":"","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

ยังไม่มีข้อมูลยืนยันในส่วน วิธีเล่นและปุ่ม สำหรับขอบเขตนี้

bindings: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_overcooked_2"
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

raw source: model_matrix\common_RESULTS.jsonl.gz record1=367

## ตัวอย่าง common_llm: e66e39ac690211e827093b69f911b2dca390f9a5f26e5ab0edb42b12b6677e93

คำถาม: ROV รอบชิงเล่นกี่เกม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"GR-013","category":"game_rules","question_no":13,"question":"ROV รอบชิงเล่นกี่เกม","expected_support":"competition_rules","note":"มีข้อมูลกติกาการแข่งขัน แต่ไม่ใช่เกมใน catalog เล่นของศูนย์","locale":"auto"}
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

raw source: model_matrix\common_RESULTS.jsonl.gz record1=625
