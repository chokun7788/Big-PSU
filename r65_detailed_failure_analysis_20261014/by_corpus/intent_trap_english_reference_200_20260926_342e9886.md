# data/eval/intent_trap_english_reference_200_20260926.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 200/200 | 0 | 0 | 0 |
| common_offline | 200/200 | 0 | 0 | 0 |
| legacy_llm | 200/200 | 0 | 0 | 0 |
| common_llm | 187/200 | 13 | 0 | 13 |

## ตัวอย่าง common_llm: ffbfe8375e5f9c11237f5572ef65cead456732314b5b3a9adabbfb122d27b7b0

คำถาม: A question about the studio: Can an outsider without a student ID reserve a station?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"INTENT-TRAP-EN-0127","paired_thai_id":"INTENT-TRAP-TH-0127","scenario_start":126,"domain":"outsider_eligibility","facet":"booking_without_psu_id","question_en":"A question about the studio: Can an outsider without a student ID reserve a station?","question_th":"ขอถามเกี่ยวกับศูนย์หน่อยครับ: คนนอกที่ไม่มีรหัสนักศึกษาจองเครื่องได้ไหม","reference_answer_en":"Yes. A PSU student ID is not required for a public visitor to reserve a station. Use the National ID field when booking and present a national ID card at check-in; the applicable fee may vary.","reference_kind":"english_answer_candidate_from_user_thai_review","reference_status":"pending_owner_policy_confirmation","source_basis":"reviewer_interpretation_with_site_context","source_url":"https://esports.computing.psu.ac.th/","thai_review":{"origin":"user_manual","decision_on_old_answer":"incorrect","note_th":"สามารถใช้ได้หมด แต่อาจมีค่าบริการตามสถานะต่างๆ","note_en_literal":"Visitors may use the services, though fees may vary by user group."},"english_existing_manual_decision_on_old_answer":null,"translation_analysis":{"paired_question_same_intent":true,"issues":["english_not_manually_reviewed"],"old_english_route":"no_answer","old_english_status":"no_answer"},"question":"A question about the studio: Can an outsider without a student ID reserve a station?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

No confirmed game_mode data for this scope.

**Game on this service**
• account policy id: Not yet confirmed

studio supported: This attribute is outside the selected record scope; please specify the related service or record.

conditions all: This attribute is outside the selected record scope; please specify the related service or record.

exceptions: This attribute is outside the selected record scope; please specify the related service or record.

Failures: ["validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_spider_man_2"
  ],
  "requested_fields": [
    "studio_supported",
    "account_policy_id",
    "conditions_all",
    "exceptions"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=4533

## ตัวอย่าง common_llm: 208a6b61784a99b214832622d4d2b382d729d8fad390a86d6ec02c9e770af676

คำถาม: Before visiting, I need to know: Can an outsider without a student ID reserve a station?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"INTENT-TRAP-EN-0128","paired_thai_id":"INTENT-TRAP-TH-0128","scenario_start":126,"domain":"outsider_eligibility","facet":"booking_without_psu_id","question_en":"Before visiting, I need to know: Can an outsider without a student ID reserve a station?","question_th":"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนนอกที่ไม่มีรหัสนักศึกษาจองเครื่องได้ไหม","reference_answer_en":"Yes. A PSU student ID is not required for a public visitor to reserve a station. Use the National ID field when booking and present a national ID card at check-in; the applicable fee may vary.","reference_kind":"english_answer_candidate_from_user_thai_review","reference_status":"pending_owner_policy_confirmation","source_basis":"reviewer_interpretation_with_site_context","source_url":"https://esports.computing.psu.ac.th/","thai_review":{"origin":"user_manual","decision_on_old_answer":"incorrect","note_th":"สามารถใช้ได้หมด แต่อาจมีค่าบริการตามสถานะต่างๆ","note_en_literal":"Visitors may use the services, though fees may vary by user group."},"english_existing_manual_decision_on_old_answer":null,"translation_analysis":{"paired_question_same_intent":true,"issues":["english_not_manually_reviewed"],"old_english_route":"no_answer","old_english_status":"no_answer"},"question":"Before visiting, I need to know: Can an outsider without a student ID reserve a station?","locale":"en"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

decision: This attribute is outside the selected record scope; please specify the related service or record.

conditions all: This attribute is outside the selected record scope; please specify the related service or record.

exceptions: This attribute is outside the selected record scope; please specify the related service or record.

consequence: This attribute is outside the selected record scope; please specify the related service or record.

details: This attribute is outside the selected record scope; please specify the related service or record.

Failures: ["validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_spider_man_2"
  ],
  "requested_fields": [
    "decision",
    "conditions_all",
    "exceptions",
    "consequence",
    "details"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=4534
