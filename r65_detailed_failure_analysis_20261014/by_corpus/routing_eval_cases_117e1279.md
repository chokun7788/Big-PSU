# data/routing/routing_eval_cases.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 18/40 | 22 | 21 | 0 |

## ตัวอย่าง legacy_offline: 9463d60e2faa6d687131d15452fa14b31b96f50653f7e1803de504b5e9791e95

คำถาม: อยากเล่น Mario Kart ต้องไปโซนไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RT-GM-005","question":"อยากเล่น Mario Kart ต้องไปโซนไหน","expected_category":"games","expected_intent":"game_availability_lookup","expected_domain":"games","expected_operation":"availability","must_not_category":["service_fee"],"notes":"game location","locale":"auto"}
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
| common_offline | 12/40 | 28 | 28 | 0 |

## ตัวอย่าง common_offline: ef4a8586bc0fd2c2df4aba9e2f2988a7c7d7762d7adc81c2bd7618287659a432

คำถาม: PS5 ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RT-SF-003","question":"PS5 ราคาเท่าไหร่","expected_category":"service_fee","expected_intent":"service_fee_query","expected_domain":"service_fee","expected_operation":"price_calculate","must_not_category":["games"],"notes":"simple PS5 price","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Failures: ["intent:conversation_price_lookup expected:service_fee_query"]

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

raw source: common_offline\RESULTS.jsonl record1=1
| legacy_llm | 18/40 | 22 | 21 | 0 |

## ตัวอย่าง legacy_llm: 9463d60e2faa6d687131d15452fa14b31b96f50653f7e1803de504b5e9791e95

คำถาม: อยากเล่น Mario Kart ต้องไปโซนไหน

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RT-GM-005","question":"อยากเล่น Mario Kart ต้องไปโซนไหน","expected_category":"games","expected_intent":"game_availability_lookup","expected_domain":"games","expected_operation":"availability","must_not_category":["service_fee"],"notes":"game location","locale":"auto"}
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
| common_llm | 8/40 | 32 | 31 | 1 |

## ตัวอย่าง common_llm: 6832b41ea09b4ee99789b6ad949e242b10d0f56258bc3c59f03181909ba4ae21

คำถาม: Overcooked ใช้ controller ยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RT-CTRL-003","question":"Overcooked ใช้ controller ยังไง","expected_category":"games","expected_intent":"game_control_lookup","expected_domain":"game_controls","expected_operation":"control","must_not_category":["equipment"],"notes":"controller intent","locale":"auto"}
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
