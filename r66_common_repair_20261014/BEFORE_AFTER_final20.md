# ตัวอย่างก่อน/หลังจากคำถามเดียวกัน

ใช้ matrix pipeline แบบ serialized บนเครื่องนี้ และ fixture booking เดียวกัน frozen clock 2026-10-14 ไม่ใช่ browser end-to-end/load test และไม่ควรอนุมานความเร็วทุกคำถามจากเวลาเพียงหนึ่งครั้ง คำตอบใหม่ยังเป็น evaluation draft ไม่มีการ owner approve

## What happens if I damage equipment?

**สาเหตุ/การแก้:** คำแปลขาดช่วงค่าปรับจริง → source-bound revision คืนตัวเลขและเงื่อนไขครบ

### ก่อน — final16

เวลา 0.324 s; mode pipeline:common_answer

**Causing damage to equipment. Responsible**
• Confirmed information: If equipment is damaged, users are responsible for fines or compensation depending on severity, from minor damage fines to full compensation for severe damage. [S1]

English translation is machine generated and has not been reviewed by the owner.

### หลัง — final20

เวลา 0.348 s; mode pipeline:common_answer

**Causing damage to equipment. Responsible**
• Confirmed information: If equipment is damaged, users are responsible for fines or compensation depending on severity: minor damage is 100-500 THB, moderate damage is the actual cost or 500-2,000 THB, and severe damage requires full compensation for the property. [S1]

English translation is machine generated and has not been reviewed by the owner.

### Query plan หลังแก้

```json
{
  "record_ids": [
    "migrated_faq_rule_damage_responsibility"
  ],
  "requested_fields": [
    "answer"
  ],
  "all_fields": false,
  "method": "common_faq_topic",
  "scope": "common_published",
  "platform": null,
  "query_without_entity": "what happens if i damage equipment?",
  "operation": "policy",
  "scope_ids": [],
  "field_selection": [],
  "confidence_calibrated": false,
  "request_focus": null,
  "schema_language_recoveries": [],
  "authority": {
    "decision": "common",
    "reason": "published_target_owned",
    "record_ids": [
      "migrated_faq_rule_damage_responsibility"
    ],
    "release_id": "EVAL_DRAFT_ONLY",
    "epoch": 1140
  },
  "field_authority": [
    {
      "record_id": "migrated_faq_rule_damage_responsibility",
      "field": "answer",
      "authority": "common",
      "status": "known",
      "revision": 3
    }
  ],
  "unresolved_clauses": [],
  "semantic_review_needed": false,
  "semantic_plan_accepted": false,
  "read_contract": {
    "schema_version": "common_read_plan_v1",
    "needs": [
      {
        "id": "n1",
        "field_refs": [
          {
            "kind": "faq",
            "key": "answer"
          }
        ],
        "source_span": "What happens if I damage equipment?",
        "resolution": "typed_supported",
        "ambiguous_kind": false
      }
    ],
    "unresolved_spans": [],
    "semantic_correctness_verified": false
  },
  "response_projection": [
    {
      "record_id": "migrated_faq_rule_damage_responsibility",
      "fields": {
        "answer": "explicit"
      }
    }
  ]
}
```

## Can a visitor plug in their own laptop?

**สาเหตุ/การแก้:** source มีอยู่ แต่รอ model selector จน timeout → policy topic selection จาก FAQ heading

### ก่อน — final18

เวลา 6.423 s; mode pipeline:common_retry

ระบบยังเลือกข้อมูลให้คำถามนี้ไม่ทัน กรุณาลองอีกครั้ง / The model could not select the relevant data in time; please retry.

### หลัง — final20

เวลา 0.392 s; mode pipeline:common_answer

**Prohibited to use power plugs without authorization**
• Confirmed information: No personal electronic devices are allowed to be plugged into power outlets without prior authorization. [S1]

English translation is machine generated and has not been reviewed by the owner.

### Query plan หลังแก้

```json
{
  "record_ids": [
    "migrated_faq_curated_rule_power_outlet"
  ],
  "requested_fields": [
    "answer"
  ],
  "all_fields": false,
  "method": "common_faq_topic",
  "scope": "common_published",
  "platform": null,
  "query_without_entity": "can a visitor plug in their own laptop?",
  "operation": "policy",
  "scope_ids": [],
  "field_selection": [],
  "confidence_calibrated": false,
  "request_focus": null,
  "schema_language_recoveries": [],
  "authority": {
    "decision": "common",
    "reason": "published_target_owned",
    "record_ids": [
      "migrated_faq_curated_rule_power_outlet"
    ],
    "release_id": "EVAL_DRAFT_ONLY",
    "epoch": 1140
  },
  "field_authority": [
    {
      "record_id": "migrated_faq_curated_rule_power_outlet",
      "field": "answer",
      "authority": "common",
      "status": "known",
      "revision": 2
    }
  ],
  "unresolved_clauses": [],
  "semantic_review_needed": false,
  "semantic_plan_accepted": false,
  "read_contract": {
    "schema_version": "common_read_plan_v1",
    "needs": [
      {
        "id": "n1",
        "field_refs": [
          {
            "kind": "faq",
            "key": "answer"
          }
        ],
        "source_span": "Can a visitor plug in their own laptop?",
        "resolution": "typed_supported",
        "ambiguous_kind": false
      }
    ],
    "unresolved_spans": [],
    "semantic_correctness_verified": false
  },
  "response_projection": [
    {
      "record_id": "migrated_faq_curated_rule_power_outlet",
      "fields": {
        "answer": "explicit"
      }
    }
  ]
}
```

## What is the studio policy for return equipment games?

**สาเหตุ/การแก้:** source มีนโยบายคืนอุปกรณ์ แต่ต้องรอ model → เลือก return-equipment policy ตามความหมายและ scope

### ก่อน — final19

เวลา 6.352 s; mode pipeline:common_retry

ระบบยังเลือกข้อมูลให้คำถามนี้ไม่ทัน กรุณาลองอีกครั้ง / The model could not select the relevant data in time; please retry.

### หลัง — final20

เวลา 0.348 s; mode pipeline:common_answer

**Return equipment and game discs**
• Confirmed information: Please return all equipment and game cards you have borrowed after use. [S1]

English translation is machine generated and has not been reviewed by the owner.

### Query plan หลังแก้

```json
{
  "record_ids": [
    "migrated_faq_curated_rule_return_equipment"
  ],
  "requested_fields": [
    "answer"
  ],
  "all_fields": false,
  "method": "common_faq_topic",
  "scope": "common_published",
  "platform": null,
  "query_without_entity": "what is the studio policy for return equipment games?",
  "operation": "policy",
  "scope_ids": [],
  "field_selection": [],
  "confidence_calibrated": false,
  "request_focus": null,
  "schema_language_recoveries": [],
  "authority": {
    "decision": "common",
    "reason": "published_target_owned",
    "record_ids": [
      "migrated_faq_curated_rule_return_equipment"
    ],
    "release_id": "EVAL_DRAFT_ONLY",
    "epoch": 1140
  },
  "field_authority": [
    {
      "record_id": "migrated_faq_curated_rule_return_equipment",
      "field": "answer",
      "authority": "common",
      "status": "known",
      "revision": 2
    }
  ],
  "unresolved_clauses": [],
  "semantic_review_needed": false,
  "semantic_plan_accepted": false,
  "read_contract": {
    "schema_version": "common_read_plan_v1",
    "needs": [
      {
        "id": "n1",
        "field_refs": [
          {
            "kind": "faq",
            "key": "answer"
          }
        ],
        "source_span": "What is the studio policy for return equipment games?",
        "resolution": "typed_supported",
        "ambiguous_kind": false
      }
    ],
    "unresolved_spans": [],
    "semantic_correctness_verified": false
  },
  "response_projection": [
    {
      "record_id": "migrated_faq_curated_rule_return_equipment",
      "fields": {
        "answer": "explicit"
      }
    }
  ]
}
```

