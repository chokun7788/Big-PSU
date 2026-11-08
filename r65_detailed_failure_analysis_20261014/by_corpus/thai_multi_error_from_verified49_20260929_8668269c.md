# data/eval/thai_multi_error_from_verified49_20260929.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 90/110 | 20 | 19 | 0 |

## ตัวอย่าง legacy_offline: 6b5117c4b3d5c7543ffe4220220d63cb66fd3bc57a2aea398276c851d303aab0

คำถาม: กฎของศุนย์มีอะไบร้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"กฎของศูนย์มีอะไรบ้าง","expected_intent":"studio_rules","group":"rules","id":"MULTI-R02","noise":"deletion+transpose","noisy":"กฎของศุนย์มีอะไบร้าง","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"R02","question":"กฎของศุนย์มีอะไบร้าง","locale":"auto"}
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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=13856
| common_offline | 74/110 | 36 | 35 | 0 |

## ตัวอย่าง common_offline: 6b5117c4b3d5c7543ffe4220220d63cb66fd3bc57a2aea398276c851d303aab0

คำถาม: กฎของศุนย์มีอะไบร้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"กฎของศูนย์มีอะไรบ้าง","expected_intent":"studio_rules","group":"rules","id":"MULTI-R02","noise":"deletion+transpose","noisy":"กฎของศุนย์มีอะไบร้าง","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"R02","question":"กฎของศุนย์มีอะไบร้าง","locale":"auto"}
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

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=17337
| legacy_llm | 90/110 | 20 | 19 | 0 |

## ตัวอย่าง legacy_llm: 6b5117c4b3d5c7543ffe4220220d63cb66fd3bc57a2aea398276c851d303aab0

คำถาม: กฎของศุนย์มีอะไบร้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"กฎของศูนย์มีอะไรบ้าง","expected_intent":"studio_rules","group":"rules","id":"MULTI-R02","noise":"deletion+transpose","noisy":"กฎของศุนย์มีอะไบร้าง","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"R02","question":"กฎของศุนย์มีอะไบร้าง","locale":"auto"}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=18075
| common_llm | 56/110 | 54 | 52 | 1 |

## ตัวอย่าง common_llm: 6b5117c4b3d5c7543ffe4220220d63cb66fd3bc57a2aea398276c851d303aab0

คำถาม: กฎของศุนย์มีอะไบร้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"กฎของศูนย์มีอะไรบ้าง","expected_intent":"studio_rules","group":"rules","id":"MULTI-R02","noise":"deletion+transpose","noisy":"กฎของศุนย์มีอะไบร้าง","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"R02","question":"กฎของศุนย์มีอะไบร้าง","locale":"auto"}
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

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=18076

## ตัวอย่าง common_llm: 24ff9fb5e218d5f9db858eed8bf46a767273724cfd69fc669beaae231d51d8a9

คำถาม: นยเปนใคแล้วทำอาไรไดบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"นายเป็นใครแล้วทำอะไรได้บ้าง","expected_intent":"chatbot_identity","group":"identity_compound","id":"MULTI-IDENTITY-02","noise":"multiple_manual_character_errors","noisy":"นยเปนใคแล้วทำอาไรไดบ้าง","review_status":"manually_expected_intent_synthetic_text","question":"นยเปนใคแล้วทำอาไรไดบ้าง","locale":"auto"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

**Ring Fit Adventure**
• ภาคหรือรุ่นของเกม: ยังไม่มีข้อมูลยืนยัน
• แนวเกม: เกมออกกำลังกาย Adventure [S1]
• เกมเกี่ยวกับอะไร: Ring Fit Adventure คือเกมออกกำลังกายที่ใช้ Ring-Con และท่าทางร่างกายเพื่อผจญภัยในเกม [S2]
• วิธีเล่นเบื้องต้นและเป้าหมายของเกม: ใส่ Joy-Con กับ Ring-Con แล้วทำท่าออกกำลังกาย เช่น วิ่ง บีบ ดัน หรือยืด เพื่อโจมตีและผ่านด่าน [S3]
• ลิงก์ข้อมูลจากผู้พัฒนาเกม: ยังไม่มีข้อมูลยืนยัน
• แพลตฟอร์มที่ตัวเกมรองรับ ไม่แปลว่าศูนย์มีให้เล่น: ยังไม่มีข้อมูลยืนยัน
• เรตอายุของตัวเกม (แยกจากกฎรับเด็กของศูนย์): ยังไม่มีข้อมูลยืนยัน

**เกมกับบริการ**
• ศูนย์มีเกมนี้ในบริการที่เลือกหรือไม่: มี/ใช่ [S4]
• เลือกตัวเลือกบริการบนหน้าจอง: Nintendo Switch (1-2 Persons) [S5]

**Nintendo Switch (1-2 Persons)**
• ชื่อบริการตามหน้า WordPress: Nintendo Switch (1-2 Persons) [S6]
• แพลตฟอร์ม เช่น PC หรือ PS5: Nintendo Switch [S7]

**เกมกับบริการ**
• ศูนย์มีเกมนี้ในบริการที่เลือกหรือไม่: มี/ใช่ [S8]
• เลือกตัวเลือกบริการบนหน้าจอง: Nintendo Switch (1-4 Persons) [S9]

**Nintendo Switch (1-4 Persons)**
• ชื่อบริการตามหน้า WordPress: Nintendo Switch (1-4 Persons) [S10]
• แพลตฟอร์ม เช่น PC หรือ PS5:  … [ย่อจาก1,565ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["intent:common_read expected:chatbot_identity","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "game_detail_ring_fit_adventure"
  ],
  "requested_fields": [
    "edition",
    "genre",
    "summary",
    "how_to_play",
    "publisher_url",
    "supported_platforms",
    "age_rating",
    "players_min",
    "players_max",
    "network_requirement",
    "studio_supported"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=18095
