# data/eval/thai_multi_error_holdout25_20260929.jsonl

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 38/50 | 12 | 9 | 0 |

## ตัวอย่าง legacy_offline: a5805e3ec48850f365f5c6e14b4cbfb0be72aec119b5f4a75c66a43e2ff4dd00

คำถาม: พลย์ห้าคิดตังเท่าไหรอ่าา

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"ราคา PS5 เท่าไหร่","expected_intent":"service_fee_query","group":"price","id":"MULTI-H06","noise":"slang_repetition+delete","noisy":"พลย์ห้าคิดตังเท่าไหรอ่าา","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"H06","question":"พลย์ห้าคิดตังเท่าไหรอ่าา","locale":"auto"}
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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=13888

## ตัวอย่าง legacy_offline: 58bc0f7b9902d15a25a990ba50054630ec99e72bba4b837b37714d7f6734101c

คำถาม: จองคอมยังงไงง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"จอง PC ยังไง","expected_intent":"booking_policy","group":"booking","id":"MULTI-H12","noise":"repetition+transpose","noisy":"จองคอมยังงไงง","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"H12","question":"จองคอมยังงไงง","locale":"auto"}
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

raw source: legacy_offline_resumed\RESULTS.jsonl record1=13895
| common_offline | 34/50 | 16 | 13 | 0 |

## ตัวอย่าง common_offline: a5805e3ec48850f365f5c6e14b4cbfb0be72aec119b5f4a75c66a43e2ff4dd00

คำถาม: พลย์ห้าคิดตังเท่าไหรอ่าา

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"ราคา PS5 เท่าไหร่","expected_intent":"service_fee_query","group":"price","id":"MULTI-H06","noise":"slang_repetition+delete","noisy":"พลย์ห้าคิดตังเท่าไหรอ่าา","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"H06","question":"พลย์ห้าคิดตังเท่าไหรอ่าา","locale":"auto"}
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

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=17369

## ตัวอย่าง common_offline: 58bc0f7b9902d15a25a990ba50054630ec99e72bba4b837b37714d7f6734101c

คำถาม: จองคอมยังงไงง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"จอง PC ยังไง","expected_intent":"booking_policy","group":"booking","id":"MULTI-H12","noise":"repetition+transpose","noisy":"จองคอมยังงไงง","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"H12","question":"จองคอมยังงไงง","locale":"auto"}
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

raw source: common_bounded_memo_counter\RESULTS.jsonl record1=17376
| legacy_llm | 38/50 | 12 | 9 | 0 |

## ตัวอย่าง legacy_llm: a5805e3ec48850f365f5c6e14b4cbfb0be72aec119b5f4a75c66a43e2ff4dd00

คำถาม: พลย์ห้าคิดตังเท่าไหรอ่าา

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"ราคา PS5 เท่าไหร่","expected_intent":"service_fee_query","group":"price","id":"MULTI-H06","noise":"slang_repetition+delete","noisy":"พลย์ห้าคิดตังเท่าไหรอ่าา","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"H06","question":"พลย์ห้าคิดตังเท่าไหรอ่าา","locale":"auto"}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=18107

## ตัวอย่าง legacy_llm: 58bc0f7b9902d15a25a990ba50054630ec99e72bba4b837b37714d7f6734101c

คำถาม: จองคอมยังงไงง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"จอง PC ยังไง","expected_intent":"booking_policy","group":"booking","id":"MULTI-H12","noise":"repetition+transpose","noisy":"จองคอมยังงไงง","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"H12","question":"จองคอมยังงไงง","locale":"auto"}
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

raw source: model_matrix_memo_counter\legacy_RESULTS.jsonl.gz record1=18114
| common_llm | 24/50 | 26 | 25 | 0 |

## ตัวอย่าง common_llm: a5805e3ec48850f365f5c6e14b4cbfb0be72aec119b5f4a75c66a43e2ff4dd00

คำถาม: พลย์ห้าคิดตังเท่าไหรอ่าา

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"clean":"ราคา PS5 เท่าไหร่","expected_intent":"service_fee_query","group":"price","id":"MULTI-H06","noise":"slang_repetition+delete","noisy":"พลย์ห้าคิดตังเท่าไหรอ่าา","review_status":"synthetic_route_probe_not_human_reviewed","source_id":"H06","question":"พลย์ห้าคิดตังเท่าไหรอ่าา","locale":"auto"}
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

raw source: model_matrix_memo_counter\common_RESULTS.jsonl.gz record1=18108
