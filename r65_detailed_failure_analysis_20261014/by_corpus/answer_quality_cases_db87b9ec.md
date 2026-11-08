# data/eval/answer_quality_cases.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 17/26 | 9 | 0 | 9 |

## ตัวอย่าง legacy_offline: 992bb60dca4b6baa9809be59805a8e3391acd8471640839e3685cdec48fd313c

คำถาม: คนนอกเล่น VR กี่บาท

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-003","question":"คนนอกเล่น VR กี่บาท","expected_category":"service_fee","must_contain":["VR 30 นาที","525 บาท","VR 1 ชั่วโมง","1,050 บาท"],"must_not_contain":[],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

VR — 30 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 525 บาท/แพ็กเกจ

VR — 60 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 1,050 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Failures: ["quality_score_or_required_gate_failed","VR 30 นาที","VR 1 ชั่วโมง"]

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

raw source: legacy_offline\RESULTS.jsonl record1=3

## ตัวอย่าง legacy_offline: 0f9e6389e996b71c34b161c6b487d803a631b5c52776018cb0b7c2ac619734c9

คำถาม: ค่าเล่นแต่ละเครื่องมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-005","question":"ค่าเล่นแต่ละเครื่องมีอะไรบ้าง","expected_category":"service_fee","must_contain":["ตาราง Service Fee","PlayStation 5","Nintendo Switch","Cockpit","VR"],"must_not_contain":[],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 140 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ

Cockpit — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU St … [ย่อจาก2,093ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["quality_score_or_required_gate_failed","ตาราง Service Fee"]

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

raw source: legacy_offline\RESULTS.jsonl record1=5
| common_offline | 12/26 | 14 | 0 | 14 |

## ตัวอย่าง common_offline: 992bb60dca4b6baa9809be59805a8e3391acd8471640839e3685cdec48fd313c

คำถาม: คนนอกเล่น VR กี่บาท

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-003","question":"คนนอกเล่น VR กี่บาท","expected_category":"service_fee","must_contain":["VR 30 นาที","525 บาท","VR 1 ชั่วโมง","1,050 บาท"],"must_not_contain":[],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

VR — 30 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 525 บาท/แพ็กเกจ

VR — 60 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 1,050 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Failures: ["quality_score_or_required_gate_failed","VR 30 นาที","VR 1 ชั่วโมง"]

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

raw source: common_offline\RESULTS.jsonl record1=3

## ตัวอย่าง common_offline: 0f9e6389e996b71c34b161c6b487d803a631b5c52776018cb0b7c2ac619734c9

คำถาม: ค่าเล่นแต่ละเครื่องมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-005","question":"ค่าเล่นแต่ละเครื่องมีอะไรบ้าง","expected_category":"service_fee","must_contain":["ตาราง Service Fee","PlayStation 5","Nintendo Switch","Cockpit","VR"],"must_not_contain":[],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_list / knowledge / 0.8

รายการที่เผยแพร่ในฐานข้อมูลกลาง: 14
• Cockpit #01
• Cockpit #02
• PC #01
• PC #02
• PC #03
• PC #04
• PC #05
• PC #06
• PC #07
• PC #08
• PC #09
• PC #10
• PlayStation 5 #01
• PlayStation 5 #02

รายการเดิมที่ยังไม่ได้ย้ายและอนุมัติในฐานข้อมูลกลางไม่รวมในรายการนี้

Failures: ["quality_score_or_required_gate_failed","ตาราง Service Fee","Nintendo Switch","VR"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "resource_cockpit_01",
    "resource_cockpit_02",
    "resource_pc_01",
    "resource_pc_02",
    "resource_pc_03",
    "resource_pc_04",
    "resource_pc_05",
    "resource_pc_06",
    "resource_pc_07",
    "resource_pc_08",
    "resource_pc_09",
    "resource_pc_10",
    "resource_ps5_01",
    "resource_ps5_02"
  ],
  "requested_fields": [],
  "all_fields": true,
  "method": "none",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_offline\RESULTS.jsonl record1=5
| legacy_llm | 17/26 | 9 | 0 | 9 |

## ตัวอย่าง legacy_llm: 992bb60dca4b6baa9809be59805a8e3391acd8471640839e3685cdec48fd313c

คำถาม: คนนอกเล่น VR กี่บาท

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-003","question":"คนนอกเล่น VR กี่บาท","expected_category":"service_fee","must_contain":["VR 30 นาที","525 บาท","VR 1 ชั่วโมง","1,050 บาท"],"must_not_contain":[],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

VR — 30 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 525 บาท/แพ็กเกจ

VR — 60 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 1,050 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Failures: ["quality_score_or_required_gate_failed","VR 30 นาที","VR 1 ชั่วโมง"]

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=3

## ตัวอย่าง legacy_llm: 0f9e6389e996b71c34b161c6b487d803a631b5c52776018cb0b7c2ac619734c9

คำถาม: ค่าเล่นแต่ละเครื่องมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-005","question":"ค่าเล่นแต่ละเครื่องมีอะไรบ้าง","expected_category":"service_fee","must_contain":["ตาราง Service Fee","PlayStation 5","Nintendo Switch","Cockpit","VR"],"must_not_contain":[],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 140 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ

Cockpit — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU St … [ย่อจาก2,093ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["quality_score_or_required_gate_failed","ตาราง Service Fee"]

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=5
| common_llm | 6/26 | 20 | 0 | 20 |

## ตัวอย่าง common_llm: 50b511eb7bab6b00caadaa326829717c36afeecf5d08f8f789a1d8cbb41c746b

คำถาม: นักศึกษา PSU เล่น Nintendo Switch ราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-002","question":"นักศึกษา PSU เล่น Nintendo Switch ราคาเท่าไหร่","expected_category":"service_fee","must_contain":["Nintendo Switch","PSU Student and Staff","0 บาท"],"must_not_contain":["Nintendo Switch Zone มีเกม"],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_retry / knowledge / 0.0

ระบบยังเลือกข้อมูลให้คำถามนี้ไม่ทัน กรุณาลองอีกครั้ง / The model could not select the relevant data in time; please retry.

Failures: ["quality_score_or_required_gate_failed","Nintendo Switch","PSU Student and Staff","0 บาท"]

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

raw source: model_matrix\common_RESULTS.jsonl.gz record1=2

## ตัวอย่าง common_llm: 992bb60dca4b6baa9809be59805a8e3391acd8471640839e3685cdec48fd313c

คำถาม: คนนอกเล่น VR กี่บาท

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"AQ-SF-003","question":"คนนอกเล่น VR กี่บาท","expected_category":"service_fee","must_contain":["VR 30 นาที","525 บาท","VR 1 ชั่วโมง","1,050 บาท"],"must_not_contain":[],"source_keywords":["SERVICE-FEE"],"format_rules":["bullet"],"notes":"","min_score":8.0,"locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**Sony PlayStation VR2**
• ประเภทอุปกรณ์: ยังไม่มีข้อมูลยืนยัน
• สเปกทีละค่า พร้อมหน่วย/รุ่น: • key: zone; unit: None; value: VR Zone
• key: quantity; unit: None; value: 1 Unit [S1]
• วิธีใช้อุปกรณ์/ข้อควรทราบจากแหล่งข้อมูล: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone
จอง VR Zone แล้วสวมแว่น PlayStation VR2 และใช้คอนโทรลเลอร์ตามคำแนะนำของเจ้าหน้าที่หรือเกม
เล่น Beat Saber
เล่น Horizon Call of the Mountain [S2]

Failures: ["quality_score_or_required_gate_failed","VR 30 นาที","525 บาท","VR 1 ชั่วโมง","1,050 บาท"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "equipment_sony_playstation_vr2"
  ],
  "requested_fields": [
    "device_type",
    "specifications",
    "usage"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": "VR",
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix\common_RESULTS.jsonl.gz record1=3
