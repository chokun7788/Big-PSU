# data/eval/english_shadow_1600_machine_sample_20260908_v4.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 6/6 | 0 | 0 | 0 |
| common_offline | 5/6 | 1 | 0 | 1 |

## ตัวอย่าง common_offline: d3903621c899772a7e97012f876c9192b2041ba708dc99c61d688976cac2837d

คำถาม: How much does it cost for a student from another university to play PC games for one hour?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0006","suite":"english_shadow","source_case_id":"MB-0006-SF-006","question_th":"นักศึกษาต่างมหาลัย เล่น PC 1 ชั่วโมง เสียกี่บาท","question_en":"How much does it cost for a student from another university to play PC games for one hour?","translation_status":"machine_translated_unreviewed","source_question_sha256":"f355ad113bda2e09f5fa5d6ea93cdddd99c4e48eec09d824cafd75eb1ed730a5","expected_category":"service_fee","expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180152+0700","translation_at":"2026-09-08T18:02:02+07:00","translation_question_sha256":"64f7f90bee65413fd6eeea658479ba100528edafcf61d2980df27067df638c9c","question":"How much does it cost for a student from another university to play PC games for one hour?","locale":"en"}
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
    "how much does it cost for a student from another university to play for one hour"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=3167
| legacy_llm | 6/6 | 0 | 0 | 0 |
| common_llm | 5/6 | 1 | 0 | 1 |

## ตัวอย่าง common_llm: d3903621c899772a7e97012f876c9192b2041ba708dc99c61d688976cac2837d

คำถาม: How much does it cost for a student from another university to play PC games for one hour?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0006","suite":"english_shadow","source_case_id":"MB-0006-SF-006","question_th":"นักศึกษาต่างมหาลัย เล่น PC 1 ชั่วโมง เสียกี่บาท","question_en":"How much does it cost for a student from another university to play PC games for one hour?","translation_status":"machine_translated_unreviewed","source_question_sha256":"f355ad113bda2e09f5fa5d6ea93cdddd99c4e48eec09d824cafd75eb1ed730a5","expected_category":"service_fee","expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T180152+0700","translation_at":"2026-09-08T18:02:02+07:00","translation_question_sha256":"64f7f90bee65413fd6eeea658479ba100528edafcf61d2980df27067df638c9c","question":"How much does it cost for a student from another university to play PC games for one hour?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] pc.*เกม**
• question: [Thai source] pc.*เกม [S1]

Failures: ["route:knowledge expected:['service_fee']","legacy_english_thai_prose_flag"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_rule_pc_games"
  ],
  "requested_fields": [
    "question"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=3906
