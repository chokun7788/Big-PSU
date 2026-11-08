# data/eval/thai_noisy_input_holdout_20260929.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 40/50 | 10 | 10 | 0 |

## ตัวอย่าง legacy_offline: 156ac1d75e2b17300c0499d41db91259eb16df502eebf1d8b27ee1a1d5826770

คำถาม: PC ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"H08","group":"price","noise":"repetition","clean":"PC ราคาเท่าไหร่","noisy":"คอมคิดตังงเท่าไหร่","expected_intent":"service_fee_query","question":"PC ราคาเท่าไหร่","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

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

raw source: legacy_offline\RESULTS.jsonl record1=27
| common_offline | 34/50 | 16 | 16 | 0 |

## ตัวอย่าง common_offline: 156ac1d75e2b17300c0499d41db91259eb16df502eebf1d8b27ee1a1d5826770

คำถาม: PC ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"H08","group":"price","noise":"repetition","clean":"PC ราคาเท่าไหร่","noisy":"คอมคิดตังงเท่าไหร่","expected_intent":"service_fee_query","question":"PC ราคาเท่าไหร่","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

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

raw source: common_offline\RESULTS.jsonl record1=27
| legacy_llm | 40/50 | 10 | 10 | 0 |

## ตัวอย่าง legacy_llm: 156ac1d75e2b17300c0499d41db91259eb16df502eebf1d8b27ee1a1d5826770

คำถาม: PC ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"H08","group":"price","noise":"repetition","clean":"PC ราคาเท่าไหร่","noisy":"คอมคิดตังงเท่าไหร่","expected_intent":"service_fee_query","question":"PC ราคาเท่าไหร่","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=27
| common_llm | 22/50 | 28 | 28 | 0 |

## ตัวอย่าง common_llm: 156ac1d75e2b17300c0499d41db91259eb16df502eebf1d8b27ee1a1d5826770

คำถาม: PC ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"H08","group":"price","noise":"repetition","clean":"PC ราคาเท่าไหร่","noisy":"คอมคิดตังงเท่าไหร่","expected_intent":"service_fee_query","question":"PC ราคาเท่าไหร่","locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

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

raw source: model_matrix\common_RESULTS.jsonl.gz record1=27
