# data/eval/english_shadow_1600_machine_20260908.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 1135/1600 | 465 | 380 | 24 |

## ตัวอย่าง legacy_offline: c9812ca9b4dc2e271883d2cdfcc4b30cf1652b59bb5e8637a0a18a2de22727bb

คำถาม: How many PSU Esports members are there?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0491","suite":"english_shadow","source_case_id":"MB-0491-M-002","question_th":"สมาชิก PSU Esports มีกี่คน","question_en":"How many PSU Esports members are there?","translation_status":"machine_translated_unreviewed","source_question_sha256":"7c1b5622d72fc25b14b61a80d47194d7a03dd1fdaa0085e37332e67768c9643d","expected_category":["members","overview"],"expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180934+0700","translation_at":"2026-09-08T18:13:02+07:00","translation_question_sha256":"8de5e875a0c01c24f70ad98d38f5eb44f7cdbb4f31c18e21b945b424a039c8e9","question":"How many PSU Esports members are there?","locale":"en"}
```

Actual mode/category/confidence: pipeline:structured_members_source_th / overview / 0.98

Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- ผศ.ดร.นิวัติ แก้วประดับ: University President (อธิการบดี) - Prince of Songkla University
- รศ.ดร.พันธ์ ทองชุมนุม: Vice President (รองอธิการบดี) - Prince of Songkla University, Phuket Campus
- รศ.ดร.อซีส นันทอมรพงศ์: Dean (คณบดี) - College of Computing, Prince of Songkla University, Phuket Campus
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: Assistant to the President for Academic Affairs (ผู้ช่วยอธิการบดีฝ่ายวิชาการ) - Prince of Songkla University, Phuket Campus
- นายพฤทธิ์ เกษตรสมบูรณ์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายณัฐวัฒน์ นิธิคุณานนต์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายชนะชัย สิริพันธ์วราภรณ์: Manager (ผู้จัดการ) - PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus
- นายณภัทร เชื้อเหล่าวานิช: Cooperative education student — Game and 3 … [ย่อจาก2,631ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["legacy_english_thai_prose_flag"]

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

raw source: legacy_offline\RESULTS.jsonl record1=4565

## ตัวอย่าง legacy_offline: 1df5a4d079916304e9ccc6f5d6daac578cbf1794a11109d1611e7a47e4c15ba2

คำถาม: Who are the cooperative education participants?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0494","suite":"english_shadow","source_case_id":"MB-0494-M-005","question_th":"cooperative education มีใครบ้าง","question_en":"Who are the cooperative education participants?","translation_status":"machine_translated_unreviewed","source_question_sha256":"594ede2cd37ceaa01d4e5f2483afd090ac42ca4ddea928e083b66b719e6142d1","expected_category":["members","overview"],"expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180934+0700","translation_at":"2026-09-08T18:13:03+07:00","translation_question_sha256":"2829a7844bad3fcc0aad4cb6d1f31a49303c14450f7f73e9dc3ba714188cb226","question":"Who are the cooperative education participants?","locale":"en"}
```

Actual mode/category/confidence: pipeline:structured_members_source_th / overview / 0.98

Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- ผศ.ดร.นิวัติ แก้วประดับ: University President (อธิการบดี) - Prince of Songkla University
- รศ.ดร.พันธ์ ทองชุมนุม: Vice President (รองอธิการบดี) - Prince of Songkla University, Phuket Campus
- รศ.ดร.อซีส นันทอมรพงศ์: Dean (คณบดี) - College of Computing, Prince of Songkla University, Phuket Campus
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: Assistant to the President for Academic Affairs (ผู้ช่วยอธิการบดีฝ่ายวิชาการ) - Prince of Songkla University, Phuket Campus
- นายพฤทธิ์ เกษตรสมบูรณ์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายณัฐวัฒน์ นิธิคุณานนต์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายชนะชัย สิริพันธ์วราภรณ์: Manager (ผู้จัดการ) - PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus
- นายณภัทร เชื้อเหล่าวานิช: Cooperative education student — Game and 3 … [ย่อจาก2,631ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["legacy_english_thai_prose_flag"]

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

raw source: legacy_offline\RESULTS.jsonl record1=4568
| common_offline | 347/1600 | 1253 | 1060 | 183 |

## ตัวอย่าง common_offline: 0ba0f5d12086458cd0a9bd7cb474bc497cb05b055e8933ba977847f8322049ee

คำถาม: Does PSU staff have to pay to play PC games?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0058","suite":"english_shadow","source_case_id":"MB-0058-SF-058","question_th":"PSU Staff เล่น PC ต้องเสียเงินไหม","question_en":"Does PSU staff have to pay to play PC games?","translation_status":"machine_translated_unreviewed","source_question_sha256":"31a6b95a5a72a676ba0ac73e99c89e42948db147c77d844379960024313eb718","expected_category":"service_fee","expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180255+0700","translation_at":"2026-09-08T18:04:25+07:00","translation_question_sha256":"861dbde86b7b9d53f8e942b9d8c502af7bfbc528040c4ab7daebb09d2dcac78f","question":"Does PSU staff have to pay to play PC games?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of [Thai source] pc.*เกม do you need: question / answer / topic?

Failures: ["route:knowledge expected:['service_fee']","legacy_english_thai_prose_flag"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_pc_games"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "does psu staff have to pay to play"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=1699

## ตัวอย่าง common_offline: 5b82e5e0490cd4523dc86c7e7326f921c23cfb2e9ec12913b1230710b6ae09f3

คำถาม: What is the price of VALORANT?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0059","suite":"english_shadow","source_case_id":"MB-0059-SF-059","question_th":"VALORANT ราคาเท่าไหร่","question_en":"What is the price of VALORANT?","translation_status":"machine_translated_unreviewed","source_question_sha256":"c7094f85c5e31a495f63b46645d5efe8067ed382bcd5d397aa357e47e7fbe495","expected_category":"service_fee","expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"high","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180255+0700","translation_at":"2026-09-08T18:04:25+07:00","translation_question_sha256":"bf70c6e603b6e08db3da77ef0b07e4161d9bf2a73e93d0de592cae78cbd9e7d1","question":"What is the price of VALORANT?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

No confirmed price in this scope.

No confirmed price in this scope.

No confirmed price in this scope.

No confirmed price in this scope.

No confirmed price in this scope.

amount minor: This attribute is outside the selected record scope; please specify the related service or record.

Failures: ["route:knowledge expected:['service_fee']","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_valorant",
    "competition_competition_rules_valorant_psu_phuket_2026",
    "controls_pc_valorant",
    "availability_pc_01_02",
    "availability_pc_03_10"
  ],
  "requested_fields": [
    "amount_minor"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=1700
| legacy_llm | 1323/1600 | 277 | 196 | 23 |

## ตัวอย่าง legacy_llm: c9812ca9b4dc2e271883d2cdfcc4b30cf1652b59bb5e8637a0a18a2de22727bb

คำถาม: How many PSU Esports members are there?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0491","suite":"english_shadow","source_case_id":"MB-0491-M-002","question_th":"สมาชิก PSU Esports มีกี่คน","question_en":"How many PSU Esports members are there?","translation_status":"machine_translated_unreviewed","source_question_sha256":"7c1b5622d72fc25b14b61a80d47194d7a03dd1fdaa0085e37332e67768c9643d","expected_category":["members","overview"],"expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180934+0700","translation_at":"2026-09-08T18:13:02+07:00","translation_question_sha256":"8de5e875a0c01c24f70ad98d38f5eb44f7cdbb4f31c18e21b945b424a039c8e9","question":"How many PSU Esports members are there?","locale":"en"}
```

Actual mode/category/confidence: pipeline:structured_members_source_th / overview / 0.98

Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- ผศ.ดร.นิวัติ แก้วประดับ: University President (อธิการบดี) - Prince of Songkla University
- รศ.ดร.พันธ์ ทองชุมนุม: Vice President (รองอธิการบดี) - Prince of Songkla University, Phuket Campus
- รศ.ดร.อซีส นันทอมรพงศ์: Dean (คณบดี) - College of Computing, Prince of Songkla University, Phuket Campus
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: Assistant to the President for Academic Affairs (ผู้ช่วยอธิการบดีฝ่ายวิชาการ) - Prince of Songkla University, Phuket Campus
- นายพฤทธิ์ เกษตรสมบูรณ์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายณัฐวัฒน์ นิธิคุณานนต์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายชนะชัย สิริพันธ์วราภรณ์: Manager (ผู้จัดการ) - PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus
- นายณภัทร เชื้อเหล่าวานิช: Cooperative education student — Game and 3 … [ย่อจาก2,631ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["legacy_english_thai_prose_flag"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=2868

## ตัวอย่าง legacy_llm: 1df5a4d079916304e9ccc6f5d6daac578cbf1794a11109d1611e7a47e4c15ba2

คำถาม: Who are the cooperative education participants?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0494","suite":"english_shadow","source_case_id":"MB-0494-M-005","question_th":"cooperative education มีใครบ้าง","question_en":"Who are the cooperative education participants?","translation_status":"machine_translated_unreviewed","source_question_sha256":"594ede2cd37ceaa01d4e5f2483afd090ac42ca4ddea928e083b66b719e6142d1","expected_category":["members","overview"],"expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180934+0700","translation_at":"2026-09-08T18:13:03+07:00","translation_question_sha256":"2829a7844bad3fcc0aad4cb6d1f31a49303c14450f7f73e9dc3ba714188cb226","question":"Who are the cooperative education participants?","locale":"en"}
```

Actual mode/category/confidence: pipeline:structured_members_source_th / overview / 0.98

Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- ผศ.ดร.นิวัติ แก้วประดับ: University President (อธิการบดี) - Prince of Songkla University
- รศ.ดร.พันธ์ ทองชุมนุม: Vice President (รองอธิการบดี) - Prince of Songkla University, Phuket Campus
- รศ.ดร.อซีส นันทอมรพงศ์: Dean (คณบดี) - College of Computing, Prince of Songkla University, Phuket Campus
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: Assistant to the President for Academic Affairs (ผู้ช่วยอธิการบดีฝ่ายวิชาการ) - Prince of Songkla University, Phuket Campus
- นายพฤทธิ์ เกษตรสมบูรณ์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายณัฐวัฒน์ นิธิคุณานนต์: Computer technical officer (นักวิชาการคอมพิวเตอร์) - College of Computing, Prince of Songkla University, Phuket Campus
- นายชนะชัย สิริพันธ์วราภรณ์: Manager (ผู้จัดการ) - PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus
- นายณภัทร เชื้อเหล่าวานิช: Cooperative education student — Game and 3 … [ย่อจาก2,631ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["legacy_english_thai_prose_flag"]

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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=2871
| common_llm | 460/1600 | 1140 | 741 | 393 |

## ตัวอย่าง common_llm: 9cd5ed0cfc987fe1932ba864196ff4439f146844142095e7a3c16adfbc8efe7a

คำถาม: How much does it cost for a general visitor to play VR for 30 minutes?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0048","suite":"english_shadow","source_case_id":"MB-0048-SF-048","question_th":"บุคคลทั่วไป เล่น VR 30 นาที เสียกี่บาท","question_en":"How much does it cost for a general visitor to play VR for 30 minutes?","translation_status":"machine_translated_unreviewed","source_question_sha256":"7896e530c19f05fff48ccd9f808d67e95609b705977360a066c8f12c4e4b40b4","expected_category":"service_fee","expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180255+0700","translation_at":"2026-09-08T18:04:12+07:00","translation_question_sha256":"d65d3d2dc6aabf8b8de61e9f3c1f922aa638bbd459299839b91f76b897012b75","question":"How much does it cost for a general visitor to play VR for 30 minutes?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] Service Fee 2026 - VR 30 minutes rates**
• answer: [Thai source] ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท [S1]
• scope note: Not yet confirmed

Failures: ["route:knowledge expected:['service_fee']","legacy_english_thai_prose_flag"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_curated_service_fee_vr_30_rates"
  ],
  "requested_fields": [
    "answer",
    "scope_note"
  ],
  "all_fields": false,
  "method": "published_semantic_candidates",
  "platform": "VR",
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=2428

## ตัวอย่าง common_llm: 9cd5ed0cfc987fe1932ba864196ff4439f146844142095e7a3c16adfbc8efe7a

คำถาม: How much does it cost for a general visitor to play VR for 30 minutes?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-1183","suite":"english_shadow","source_case_id":"MB-1183-SF-214","question_th":"คนทั่วไป เล่น VR 30 นาที 30 นาที เสียกี่บาท","question_en":"How much does it cost for a general visitor to play VR for 30 minutes?","translation_status":"machine_translated_unreviewed","source_question_sha256":"5b412567a368006519c037f27db41c21ef07960c02e6e794f905dafc99331af1","expected_category":"service_fee","expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"service_fee","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T181817+0700","translation_at":"2026-09-08T18:24:26+07:00","translation_question_sha256":"d65d3d2dc6aabf8b8de61e9f3c1f922aa638bbd459299839b91f76b897012b75","question":"How much does it cost for a general visitor to play VR for 30 minutes?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] Service Fee 2026 - VR 30 minutes rates**
• answer: [Thai source] ค่าบริการ VR 30 นาที: นักศึกษา/บุคลากร PSU 0 บาท, ศิษย์เก่า PSU หรือ General Student 190 บาท, บุคคลทั่วไป 525 บาท [S1]
• scope note: Not yet confirmed

Failures: ["route:knowledge expected:['service_fee']","legacy_english_thai_prose_flag"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_curated_service_fee_vr_30_rates"
  ],
  "requested_fields": [
    "answer",
    "scope_note"
  ],
  "all_fields": false,
  "method": "published_semantic_candidates",
  "platform": "VR",
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=2428
