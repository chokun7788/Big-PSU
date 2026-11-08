# data/eval/intent_trap_bilingual_1000_v1.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 846/1000 | 154 | 125 | 13 |

## ตัวอย่าง legacy_offline: de1f2b3ad4bd70650e0ff06a56b13e5dbfc4ef19df3e3f946f523d0ee0cc3434

คำถาม: จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":["ค่าปรับ","ชดเชย","รับผิดชอบ","fine","compensation","responsible"],"must_not_contain":["โหมดทดลอง RAG","closest information"]},"domain":"damage_responsibility","expected_answer_status":"answer_available","expected_facet":"damage_responsibility","expected_route_categories":["penalty","rules"],"expected_target":"","id":"INTENT-TRAP-TH-0161","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"damage_responsibility_03","style_index":1},"question":"จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["route:service_fee expected:['penalty', 'rules']","missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']"]

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

raw source: legacy_offline\RESULTS.jsonl record1=5763

## ตัวอย่าง legacy_offline: 7a133bdf40f364780795e7e24d019b34937ebabd08c6ef9cc86a0628bea2531a

คำถาม: ขอถามเกี่ยวกับศูนย์หน่อยครับ: จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":["ค่าปรับ","ชดเชย","รับผิดชอบ","fine","compensation","responsible"],"must_not_contain":["โหมดทดลอง RAG","closest information"]},"domain":"damage_responsibility","expected_answer_status":"answer_available","expected_facet":"damage_responsibility","expected_route_categories":["penalty","rules"],"expected_target":"","id":"INTENT-TRAP-TH-0162","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"damage_responsibility_03","style_index":2},"question":"ขอถามเกี่ยวกับศูนย์หน่อยครับ: จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["route:service_fee expected:['penalty', 'rules']","missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']"]

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

raw source: legacy_offline\RESULTS.jsonl record1=5764
| common_offline | 664/1000 | 336 | 204 | 96 |

## ตัวอย่าง common_offline: 609e867f7b3447b8f61f08bec8719459898ab6e630ef8c35fadd24417b99951a

คำถาม: ขอถามเกี่ยวกับศูนย์หน่อยครับ: การจองเครื่องเล่นเกมเปิดจองวันไหนและช่วงเวลาไหนบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":["09:00","13:00","9:00","1 pm"],"must_not_contain":["ขั้นตอนโดยสรุปคือ 1)"]},"domain":"booking_days_hours","expected_answer_status":"answer_available","expected_facet":"booking_days_hours","expected_route_categories":["schedule","reservation"],"expected_target":"","id":"INTENT-TRAP-TH-0052","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"booking_days_hours_01","style_index":2},"question":"ขอถามเกี่ยวกับศูนย์หน่อยครับ: การจองเครื่องเล่นเกมเปิดจองวันไหนและช่วงเวลาไหนบ้าง","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ psu esports.*คืออะไร เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?

Failures: ["route:knowledge expected:['schedule', 'reservation']","status:clarification expected:answer_available","missing all alternatives: ['09:00', '13:00', '9:00', '1 pm']"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_overview_identity"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "ขอถาม หน่อยครับ: การจองเครื่องเล่นเกมเปิดจองวันไหน",
    "ช่วงเวลาไหนบ้าง"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=3219

## ตัวอย่าง common_offline: dac8fd5ca234907884bb37701e3572f521ae1a231485d52076a59bed8f9ae138

คำถาม: ขอถามเกี่ยวกับศูนย์หน่อยครับ: จอง PC ได้วันอะไร ช่วงกี่โมง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":["09:00","13:00","9:00","1 pm"],"must_not_contain":["ขั้นตอนโดยสรุปคือ 1)"]},"domain":"booking_days_hours","expected_answer_status":"answer_available","expected_facet":"booking_days_hours","expected_route_categories":["schedule","reservation"],"expected_target":"","id":"INTENT-TRAP-TH-0057","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"booking_days_hours_02","style_index":2},"question":"ขอถามเกี่ยวกับศูนย์หน่อยครับ: จอง PC ได้วันอะไร ช่วงกี่โมง","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ psu esports.*คืออะไร เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?

Failures: ["route:knowledge expected:['schedule', 'reservation']","status:clarification expected:answer_available","missing all alternatives: ['09:00', '13:00', '9:00', '1 pm']"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_overview_identity"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "ขอถาม หน่อยครับ: จอง pc ได้วันอะไร ช่วงกี่โมง"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=3224
| legacy_llm | 848/1000 | 152 | 126 | 11 |

## ตัวอย่าง legacy_llm: de1f2b3ad4bd70650e0ff06a56b13e5dbfc4ef19df3e3f946f523d0ee0cc3434

คำถาม: จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":["ค่าปรับ","ชดเชย","รับผิดชอบ","fine","compensation","responsible"],"must_not_contain":["โหมดทดลอง RAG","closest information"]},"domain":"damage_responsibility","expected_answer_status":"answer_available","expected_facet":"damage_responsibility","expected_route_categories":["penalty","rules"],"expected_target":"","id":"INTENT-TRAP-TH-0161","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"damage_responsibility_03","style_index":1},"question":"จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["route:service_fee expected:['penalty', 'rules']","missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=4066

## ตัวอย่าง legacy_llm: 7a133bdf40f364780795e7e24d019b34937ebabd08c6ef9cc86a0628bea2531a

คำถาม: ขอถามเกี่ยวกับศูนย์หน่อยครับ: จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":["ค่าปรับ","ชดเชย","รับผิดชอบ","fine","compensation","responsible"],"must_not_contain":["โหมดทดลอง RAG","closest information"]},"domain":"damage_responsibility","expected_answer_status":"answer_available","expected_facet":"damage_responsibility","expected_route_categories":["penalty","rules"],"expected_target":"","id":"INTENT-TRAP-TH-0162","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"damage_responsibility_03","style_index":2},"question":"ขอถามเกี่ยวกับศูนย์หน่อยครับ: จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:structured_service_fee_conversation / service_fee / 0.98

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

Failures: ["route:service_fee expected:['penalty', 'rules']","missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=4067
| common_llm | 366/1000 | 634 | 449 | 114 |

## ตัวอย่าง common_llm: b4029a7b17aa505570327212d5c55ca88c3241ba433129d19237736edbec632c

คำถาม: บุคคลภายนอกใช้อุปกรณ์คิดราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["อุปกรณ์บนหน้า Home","Verified equipment:"]},"domain":"fee_without_service","expected_answer_status":"clarification_required","expected_facet":"fee_without_service","expected_route_categories":["clarification","service_fee"],"expected_target":"","id":"INTENT-TRAP-TH-0001","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"fee_without_service_01","style_index":1},"question":"บุคคลภายนอกใช้อุปกรณ์คิดราคาเท่าไหร่","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**public_access / membership**
• คำตอบพร้อมหลักฐานของศูนย์: ไม่ต้องเป็นนักศึกษา PSU ครับ ขั้นตอนจองที่เผยแพร่ไม่ได้ระบุว่าต้องสมัครสมาชิกแยกก่อนจอง คนภายนอกใช้ช่อง National ID และแสดงบัตรประชาชนตอนเช็กอิน ค่าบริการขึ้นกับกลุ่มผู้ใช้และบริการ [S1]
• ขอบเขตคำตอบและข้อจำกัด: ยังไม่มีข้อมูลยืนยัน

Failures: ["route:knowledge expected:['clarification', 'service_fee']","status:answer expected:clarification_required"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_policy_text_public_access_membership"
  ],
  "requested_fields": [
    "answer",
    "scope_note"
  ],
  "all_fields": false,
  "method": "published_semantic_candidates",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=3907

## ตัวอย่าง common_llm: 89f8312f2253dbf2adc96e35c7e30aa9c16a5d77ad27ce5017aa88bdd29c3c55

คำถาม: ขอถามเกี่ยวกับศูนย์หน่อยครับ: บุคคลภายนอกใช้อุปกรณ์คิดราคาเท่าไหร่

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"answer_contract":{"must_contain":[],"must_contain_any":[],"must_not_contain":["อุปกรณ์บนหน้า Home","Verified equipment:"]},"domain":"fee_without_service","expected_answer_status":"clarification_required","expected_facet":"fee_without_service","expected_route_categories":["clarification","service_fee"],"expected_target":"","id":"INTENT-TRAP-TH-0002","latency_ceiling_sec":20.0,"locale":"th","metadata":{"reference_date":"2026-09-24","scenario_id":"fee_without_service_01","style_index":2},"question":"ขอถามเกี่ยวกับศูนย์หน่อยครับ: บุคคลภายนอกใช้อุปกรณ์คิดราคาเท่าไหร่","review_status":"scenario_curated_paraphrase_pending_review","suite":"psu_esports_intent_trap_candidate_v1"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**psu esports.*คืออะไร**
• คำตอบพร้อมหลักฐานของศูนย์: PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ [S1]
• ข้อมูลอื่นที่เกี่ยวข้อง: ยังไม่มีข้อมูลยืนยัน
• ขอบเขตคำตอบและข้อจำกัด: ยังไม่มีข้อมูลยืนยัน

Failures: ["route:knowledge expected:['clarification', 'service_fee']","status:answer expected:clarification_required"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_overview_identity"
  ],
  "requested_fields": [
    "answer",
    "related_ids",
    "scope_note"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=3908
