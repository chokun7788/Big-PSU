# data/eval/review_grounded_novel_20260925.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 39/41 | 2 | 0 | 2 |

## ตัวอย่าง legacy_offline: 84601c51da3d3b16f8f5bc346502b1c2e799c371bc0045580c4c007f577b8d55

คำถาม: คนทั่วไปต้องสมัครสมาชิกก่อนจองหรือเปล่า

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-TH-05","locale":"th","domain":"membership_facet","question":"คนทั่วไปต้องสมัครสมาชิกก่อนจองหรือเปล่า","review_status":"scenario_curated_pending_review","expected_route_categories":["reservation"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["สมัครสมาชิก","National ID"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:user_service_facts / reservation / 0.98

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["missing required: สมัครสมาชิก","missing required: National ID"]

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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=13772

## ตัวอย่าง legacy_offline: 6bc1f2980ce8b0013830593355c1e99830fde169394cb1a426a0f27a11f71305

คำถาม: ถ้าเป็นคนนอกเดินเข้าไปเล่นเลยโดยไม่จองได้ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-TH-06","locale":"th","domain":"booking_required","question":"ถ้าเป็นคนนอกเดินเข้าไปเล่นเลยโดยไม่จองได้ไหม","review_status":"scenario_curated_pending_review","expected_route_categories":["reservation"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["โดยไม่จองล่วงหน้าไม่ได้","1 ชั่วโมง"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:user_service_facts / reservation / 0.98

Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["missing required: โดยไม่จองล่วงหน้าไม่ได้","missing required: 1 ชั่วโมง"]

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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=13773
| common_offline | 33/41 | 8 | 0 | 8 |

## ตัวอย่าง common_offline: 911db61829c91d36ee299f0c280a84811d7f61dae95aa6ad1645a74db35ab170

คำถาม: ขอข้อมูลเรื่องชำระเงินหลัง booking ขอรายละเอียดแบบสั้น ๆ

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-TH-18","locale":"th","domain":"payment_deadline","question":"ขอข้อมูลเรื่องชำระเงินหลัง booking ขอรายละเอียดแบบสั้น ๆ","review_status":"scenario_curated_pending_review","expected_route_categories":["reservation"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["10 นาที"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ หลังจอง.*จ่าย เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?

Failures: ["route:knowledge expected:['reservation']","status:clarification expected:answer_available","missing required: 10 นาที"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_payment_10_minutes"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "ขอข้อมูลเรื่อง ขอรายละเอียดแบบสั้น ๆ"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=4948

## ตัวอย่าง common_offline: 8ace63877eef6cb850b5820ae51030afee591f80d0c690bd0b2acb2eb98991e2

คำถาม: ขอข้อมูลเรื่องทรัพย์สินส่วนตัว สูญหาย

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-TH-20","locale":"th","domain":"lost_property_rule","question":"ขอข้อมูลเรื่องทรัพย์สินส่วนตัว สูญหาย","review_status":"scenario_curated_pending_review","expected_route_categories":["rules"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["ไม่รับผิดชอบ"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ ทรัพย์สินส่วนตัว.*สูญหาย เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?

Failures: ["route:knowledge expected:['rules']","status:clarification expected:answer_available","missing required: ไม่รับผิดชอบ"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_lost_personal_items"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "bounded_fuzzy",
  "platform": null,
  "unresolved_clauses": [
    "ขอข้อมูลเรื่องทรัพย์สินส่วนตัว สูญหาย"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=7820
| legacy_llm | 39/41 | 2 | 0 | 2 |

## ตัวอย่าง legacy_llm: 84601c51da3d3b16f8f5bc346502b1c2e799c371bc0045580c4c007f577b8d55

คำถาม: คนทั่วไปต้องสมัครสมาชิกก่อนจองหรือเปล่า

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-TH-05","locale":"th","domain":"membership_facet","question":"คนทั่วไปต้องสมัครสมาชิกก่อนจองหรือเปล่า","review_status":"scenario_curated_pending_review","expected_route_categories":["reservation"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["สมัครสมาชิก","National ID"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:user_service_facts / reservation / 0.98

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["missing required: สมัครสมาชิก","missing required: National ID"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=17991

## ตัวอย่าง legacy_llm: 6bc1f2980ce8b0013830593355c1e99830fde169394cb1a426a0f27a11f71305

คำถาม: ถ้าเป็นคนนอกเดินเข้าไปเล่นเลยโดยไม่จองได้ไหม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-TH-06","locale":"th","domain":"booking_required","question":"ถ้าเป็นคนนอกเดินเข้าไปเล่นเลยโดยไม่จองได้ไหม","review_status":"scenario_curated_pending_review","expected_route_categories":["reservation"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["โดยไม่จองล่วงหน้าไม่ได้","1 ชั่วโมง"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:user_service_facts / reservation / 0.98

Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["missing required: โดยไม่จองล่วงหน้าไม่ได้","missing required: 1 ชั่วโมง"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=17992
| common_llm | 11/41 | 30 | 11 | 18 |

## ตัวอย่าง common_llm: 68e563aa545ad952b5fa9330b0aea189c14063a5b0221829c710972a769756ac

คำถาม: How do I pay for my booking?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-EN-17","locale":"en","domain":"payment_method","question":"How do I pay for my booking?","review_status":"scenario_curated_pending_review","expected_route_categories":["reservation"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["Siam Commercial Bank","795-276244-1"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] payment_timeout**
• answer: Payment must be made immediately after booking. If payment is not made within 10 minutes, the booking is cancelled and a new booking is required. [S1]
• scope note: Not yet confirmed

Failures: ["route:knowledge expected:['reservation']","missing required: Siam Commercial Bank","missing required: 795-276244-1"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_en_payment_deadline_natural"
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

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=2183

## ตัวอย่าง common_llm: 560339bb5061b26d709366977304586d003eab347d4b22b97925b88fa5bdbffa

คำถาม: ขอข้อมูลเรื่องคำพูดไม่เหมาะสม

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"RG-NOVEL-TH-21","locale":"th","domain":"offensive_language_rule","question":"ขอข้อมูลเรื่องคำพูดไม่เหมาะสม","review_status":"scenario_curated_pending_review","expected_route_categories":["rules"],"expected_answer_status":"answer_available","answer_contract":{"must_contain":["ห้ามพูดจาดูหมิ่น"]},"latency_ceiling_sec":20}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ เสียงดัง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?

Failures: ["route:knowledge expected:['rules']","status:clarification expected:answer_available","missing required: ห้ามพูดจาดูหมิ่น"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_noise_language"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "ขอข้อมูลเรื่อง"
  ],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=8564
