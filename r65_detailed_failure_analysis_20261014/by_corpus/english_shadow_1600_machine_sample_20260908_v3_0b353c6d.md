# data/eval/english_shadow_1600_machine_sample_20260908_v3.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 3/3 | 0 | 0 | 0 |
| common_offline | 3/3 | 0 | 0 | 0 |
| legacy_llm | 3/3 | 0 | 0 | 0 |
| common_llm | 2/3 | 1 | 0 | 1 |

## ตัวอย่าง common_llm: 14c35076ac7b8b54d4c9cad09f16034cd5ef56e39e67bae6137b83a6a7266081

คำถาม: What is the PC price?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"EN-SHADOW-0001","suite":"english_shadow","source_case_id":"MB-0001-SF-001","question_th":"PC ราคาเท่าไหร่","question_en":"What is the PC price?","translation_status":"machine_translated_unreviewed","source_question_sha256":"c2e271a95c0fa3d760c26c142591deb70f891e286139b720c856dbe74ff5e499","expected_category":"service_fee","expected_mode_prefix":null,"quality_bucket":"psu_fact","risk":"medium","source":"broad_usage_eval_v1","translation_method":"local_ollama_batch","translation_model":"scb10x/typhoon2.5-qwen3-4b","translation_run_id":"20260908T175948+0700","translation_at":"2026-09-08T17:59:54+07:00","translation_question_sha256":"01a2036af7e0c7cf894167074c476ba4a2a711cbbccb66e2045b665f22391df6","question":"What is the PC price?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**[Thai source] Service Fee 2026 - PC price status**
• answer: [Thai source] บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง [S1]
• scope note: Not yet confirmed

Failures: ["route:knowledge expected:['service_fee']","legacy_english_thai_prose_flag"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "migrated_faq_curated_service_fee_pc_unknown"
  ],
  "requested_fields": [
    "answer",
    "scope_note"
  ],
  "all_fields": false,
  "method": "published_semantic_candidates",
  "platform": "PC",
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=3902
