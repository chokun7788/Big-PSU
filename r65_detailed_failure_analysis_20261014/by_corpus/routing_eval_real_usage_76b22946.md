# data/routing/routing_eval_real_usage.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 62/115 | 53 | 48 | 0 |

## ตัวอย่าง legacy_offline: 9463d60e2faa6d687131d15452fa14b31b96f50653f7e1803de504b5e9791e95

คำถาม: อยากเล่น Mario Kart ต้องไปโซนไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-GA-002","question":"อยากเล่น Mario Kart ต้องไปโซนไหน","expected_category":"games","expected_intent":"game_availability_lookup","expected_domain":"games","expected_operation":"availability","must_not_category":["service_fee"],"notes":"","locale":"auto"}
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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=14566

## ตัวอย่าง legacy_offline: 7971b5efd25e1a34fd2d9757367d535ca7dbd3e1a88188f14359a05eae8eb243

คำถาม: อยากเล่น Gran Turismo ใช้อะไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-GA-007","question":"อยากเล่น Gran Turismo ใช้อะไร","expected_category":"games","expected_intent":"game_detail_lookup","expected_domain":"games","expected_operation":"how_to","must_not_category":["service_fee"],"notes":"","locale":"auto"}
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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=14604
| common_offline | 40/115 | 75 | 73 | 0 |

## ตัวอย่าง common_offline: b99cf7f939571190363fe9d398c54c4836056d56098ab92e5652aa63c934edb1

คำถาม: จองผิดแก้ยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-RSV-012","question":"จองผิดแก้ยังไง","expected_category":"reservation","expected_intent":"how_to","expected_domain":"reservation","expected_operation":"how_to","must_not_category":["games","service_fee"],"notes":"","locale":"auto"}
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

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=18094

## ตัวอย่าง common_offline: c61a2322340023acfc6073f33fb8e45391ddce6f8aef0b7a70993df474691034

คำถาม: เอาน้ำเข้าไปได้ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-RULE-002","question":"เอาน้ำเข้าไปได้ไหม","expected_category":"rules","expected_intent":"studio_rules","expected_domain":"rules","expected_operation":"rule_lookup","must_not_category":["service_fee","games"],"notes":"","locale":"auto"}
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

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=18111
| legacy_llm | 62/115 | 53 | 48 | 0 |

## ตัวอย่าง legacy_llm: 9463d60e2faa6d687131d15452fa14b31b96f50653f7e1803de504b5e9791e95

คำถาม: อยากเล่น Mario Kart ต้องไปโซนไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-GA-002","question":"อยากเล่น Mario Kart ต้องไปโซนไหน","expected_category":"games","expected_intent":"game_availability_lookup","expected_domain":"games","expected_operation":"availability","must_not_category":["service_fee"],"notes":"","locale":"auto"}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=18785

## ตัวอย่าง legacy_llm: 7971b5efd25e1a34fd2d9757367d535ca7dbd3e1a88188f14359a05eae8eb243

คำถาม: อยากเล่น Gran Turismo ใช้อะไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-GA-007","question":"อยากเล่น Gran Turismo ใช้อะไร","expected_category":"games","expected_intent":"game_detail_lookup","expected_domain":"games","expected_operation":"how_to","must_not_category":["service_fee"],"notes":"","locale":"auto"}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=18823
| common_llm | 24/115 | 91 | 88 | 3 |

## ตัวอย่าง common_llm: 80b14a4c061257a87ed043f40f7bc8a66fe12792f9ce50f09cd11ea61e6e4401

คำถาม: Beat Saber อยู่โซนไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-GA-004","question":"Beat Saber อยู่โซนไหน","expected_category":"games","expected_intent":"game_availability_lookup","expected_domain":"games","expected_operation":"availability","must_not_category":["service_fee"],"notes":"","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

zone_id: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["route:knowledge expected:['games']","intent:common_read expected:game_availability_lookup","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_beat_saber",
    "availability_vr_30",
    "availability_vr_60",
    "controls_vr_beat_saber",
    "migrated_faq_rule_vr_specific_games"
  ],
  "requested_fields": [
    "zone_id"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=16891

## ตัวอย่าง common_llm: 6832b41ea09b4ee99789b6ad949e242b10d0f56258bc3c59f03181909ba4ae21

คำถาม: Overcooked ใช้ controller ยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RU-CTRL-004","question":"Overcooked ใช้ controller ยังไง","expected_category":"games","expected_intent":"game_control_lookup","expected_domain":"game_controls","expected_operation":"control","must_not_category":["service_fee"],"notes":"","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

ยังไม่มีข้อมูลยืนยันในส่วน วิธีเล่นและปุ่ม สำหรับขอบเขตนี้

input_device: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

preset: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

bindings: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["route:knowledge expected:['games']","intent:common_read expected:game_control_lookup","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_overcooked_2"
  ],
  "requested_fields": [
    "input_device",
    "preset",
    "bindings"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=18788
