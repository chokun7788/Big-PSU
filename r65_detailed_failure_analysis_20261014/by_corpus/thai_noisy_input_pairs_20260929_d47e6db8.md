# data/eval/thai_noisy_input_pairs_20260929.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 79/98 | 19 | 19 | 0 |

## ตัวอย่าง legacy_offline: ef4a8586bc0fd2c2df4aba9e2f2988a7c7d7762d7adc81c2bd7618287659a432

คำถาม: PS5 ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"P01","group":"price","noise":"repeat","clean":"PS5 ราคาเท่าไหร่","noisy":"PS5 ราาคาเท่าไหร่","expected_intent":"service_fee_query","protected":["PS5"],"question":"PS5 ราคาเท่าไหร่","locale":"auto"}
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

raw source: legacy_offline\RESULTS.jsonl record1=1
| common_offline | 58/98 | 40 | 40 | 0 |

## ตัวอย่าง common_offline: ef4a8586bc0fd2c2df4aba9e2f2988a7c7d7762d7adc81c2bd7618287659a432

คำถาม: PS5 ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"P01","group":"price","noise":"repeat","clean":"PS5 ราคาเท่าไหร่","noisy":"PS5 ราาคาเท่าไหร่","expected_intent":"service_fee_query","protected":["PS5"],"question":"PS5 ราคาเท่าไหร่","locale":"auto"}
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
| legacy_llm | 79/98 | 19 | 19 | 0 |

## ตัวอย่าง legacy_llm: ef4a8586bc0fd2c2df4aba9e2f2988a7c7d7762d7adc81c2bd7618287659a432

คำถาม: PS5 ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"P01","group":"price","noise":"repeat","clean":"PS5 ราคาเท่าไหร่","noisy":"PS5 ราาคาเท่าไหร่","expected_intent":"service_fee_query","protected":["PS5"],"question":"PS5 ราคาเท่าไหร่","locale":"auto"}
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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=1
| common_llm | 44/98 | 54 | 54 | 0 |

## ตัวอย่าง common_llm: ef4a8586bc0fd2c2df4aba9e2f2988a7c7d7762d7adc81c2bd7618287659a432

คำถาม: PS5 ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"P01","group":"price","noise":"repeat","clean":"PS5 ราคาเท่าไหร่","noisy":"PS5 ราาคาเท่าไหร่","expected_intent":"service_fee_query","protected":["PS5"],"question":"PS5 ราคาเท่าไหร่","locale":"auto"}
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

raw source: model_matrix\common_RESULTS.jsonl.gz record1=1
