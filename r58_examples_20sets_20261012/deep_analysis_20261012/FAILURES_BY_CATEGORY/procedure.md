# ภาคผนวกเคสไม่ผ่าน — procedure / 20 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 01765](#case-01765), [Case 01775](#case-01775), [Case 01785](#case-01785), [Case 01795](#case-01795), [Case 01805](#case-01805), [Case 01815](#case-01815), [Case 01825](#case-01825), [Case 01835](#case-01835), [Case 01845](#case-01845), [Case 01855](#case-01855), [Case 01865](#case-01865), [Case 01875](#case-01875), [Case 01885](#case-01885), [Case 01895](#case-01895), [Case 01905](#case-01905), [Case 01915](#case-01915), [Case 01925](#case-01925), [Case 01935](#case-01935), [Case 01945](#case-01945), [Case 01955](#case-01955)

## Case 01765

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_01`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ดาวเหนือ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_01**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ดาวเหนือ
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_01 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ดาวเหนือ
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — email: fiction01@example.invalid
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Northstar
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_01'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_01"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_01",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_01"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Northstar service",
          "th": "เลือกบริการสมมุติ ดาวเหนือ"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_01",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Northstar"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01775

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_02`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ดาวเหนือ พลัส มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_02**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ดาวเหนือ พลัส
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_02 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ดาวเหนือ พลัส
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — facebook: https://example.invalid/demo20/social/2
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Northstar Plus
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_02'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_02"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_02",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_02"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Northstar Plus service",
          "th": "เลือกบริการสมมุติ ดาวเหนือ พลัส"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_02",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Northstar Plus"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01785

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_03`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ละอองฝน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_03**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ละอองฝน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_03
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — demo20_contact_03 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ละอองฝน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — website: https://example.invalid/demo20/contact/3
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — website: https://example.invalid/demo20/contact/3
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Drizzle
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_03'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_03"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_03",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Drizzle service",
          "th": "เลือกบริการสมมุติ ละอองฝน"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_03",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      },
      {
        "contact_id": "demo20_contact_03",
        "instruction": {
          "en": "Ask the demo operator for session-specific help",
          "th": "แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง"
        },
        "order": 3
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Drizzle"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01795

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_04`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง สายหมอก มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_04**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ สายหมอก
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_04 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ สายหมอก
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — phone: DEMO-NON-DIALABLE-04
เอกสารที่ต้องใช้ (required_documents): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_04'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_04"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_04",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_04"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Mist service",
          "th": "เลือกบริการสมมุติ สายหมอก"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_04",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01805

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_05`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง บัวสีคราม มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_05**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ บัวสีคราม
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_05 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ บัวสีคราม
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — onsite: DEMO desk Indigo Lotus
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Indigo Lotus
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_05'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_05"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_05",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_05"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Indigo Lotus service",
          "th": "เลือกบริการสมมุติ บัวสีคราม"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_05",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Indigo Lotus"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01815

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_06`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ปะการัง มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_06**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ปะการัง
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_06
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — demo20_contact_06 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ปะการัง
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — email: fiction06@example.invalid
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — email: fiction06@example.invalid
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Coral
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_06'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_06"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_06",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_06"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Coral service",
          "th": "เลือกบริการสมมุติ ปะการัง"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_06",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      },
      {
        "contact_id": "demo20_contact_06",
        "instruction": {
          "en": "Ask the demo operator for session-specific help",
          "th": "แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง"
        },
        "order": 3
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Coral"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01825

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_07`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ตะวันอ่อน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_07**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ตะวันอ่อน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_07 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ตะวันอ่อน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — facebook: https://example.invalid/demo20/social/7
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Gentle Sun
• DEMO group list 7
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_07'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_07"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_07",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_07"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Gentle Sun service",
          "th": "เลือกบริการสมมุติ ตะวันอ่อน"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_07",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Gentle Sun",
      "DEMO group list 7"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01835

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_08`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ฟ้าหลังฝน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_08**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ฟ้าหลังฝน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_08 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ฟ้าหลังฝน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — website: https://example.invalid/demo20/contact/8
เอกสารที่ต้องใช้ (required_documents): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_08'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_08"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_08",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_08"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional After Rain service",
          "th": "เลือกบริการสมมุติ ฟ้าหลังฝน"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_08",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01845

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_09`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ลมทะเล มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_09**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ลมทะเล
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_09
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — demo20_contact_09 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ลมทะเล
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — phone: DEMO-NON-DIALABLE-09
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — phone: DEMO-NON-DIALABLE-09
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Sea Breeze
• DEMO group list 9
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_09'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_09"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_09",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_09"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 22,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Sea Breeze service",
          "th": "เลือกบริการสมมุติ ลมทะเล"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_09",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      },
      {
        "contact_id": "demo20_contact_09",
        "instruction": {
          "en": "Ask the demo operator for session-specific help",
          "th": "แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง"
        },
        "order": 3
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Sea Breeze",
      "DEMO group list 9"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01855

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_10`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ห้องสมุดดาว มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_10**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ห้องสมุดดาว
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_10 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ห้องสมุดดาว
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — onsite: DEMO desk Star Library
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Star Library
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_10'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_10"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_10",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_10"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Star Library service",
          "th": "เลือกบริการสมมุติ ห้องสมุดดาว"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_10",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Star Library"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01865

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_11`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ต้นเฟิร์น มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_11**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ต้นเฟิร์น
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_11 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ต้นเฟิร์น
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — email: fiction11@example.invalid
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Fern
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_11'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_11"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_11",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_11"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Fern service",
          "th": "เลือกบริการสมมุติ ต้นเฟิร์น"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_11",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Fern"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01875

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_12`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง ทองทราย มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_12**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ ทองทราย
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_12
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — demo20_contact_12 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ ทองทราย
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — facebook: https://example.invalid/demo20/social/12
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — facebook: https://example.invalid/demo20/social/12
เอกสารที่ต้องใช้ (required_documents): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_12'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_12"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_12",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_12"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Sand Gold service",
          "th": "เลือกบริการสมมุติ ทองทราย"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_12",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      },
      {
        "contact_id": "demo20_contact_12",
        "instruction": {
          "en": "Ask the demo operator for session-specific help",
          "th": "แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง"
        },
        "order": 3
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01885

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_13`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง จันทร์เสี้ยว มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_13**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ จันทร์เสี้ยว
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_13 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ จันทร์เสี้ยว
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — website: https://example.invalid/demo20/contact/13
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Crescent
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_13'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_13"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_13",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_13"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 28,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Crescent service",
          "th": "เลือกบริการสมมุติ จันทร์เสี้ยว"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_13",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Crescent"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01895

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_14`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง แสงอรุณ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_14**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ แสงอรุณ
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_14 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ แสงอรุณ
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — phone: DEMO-NON-DIALABLE-14
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Dawn Light
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_14'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_14"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_14",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_14"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Dawn Light service",
          "th": "เลือกบริการสมมุติ แสงอรุณ"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_14",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Dawn Light"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01905

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_15`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง กิ่งไผ่ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_15**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ กิ่งไผ่
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_15
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — demo20_contact_15 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ กิ่งไผ่
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — onsite: DEMO desk Bamboo
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — onsite: DEMO desk Bamboo
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Bamboo
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_15'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_15"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_15",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_15"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Bamboo service",
          "th": "เลือกบริการสมมุติ กิ่งไผ่"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_15",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      },
      {
        "contact_id": "demo20_contact_15",
        "instruction": {
          "en": "Ask the demo operator for session-specific help",
          "th": "แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง"
        },
        "order": 3
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Bamboo"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01915

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_16`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง เมฆขาว มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_16**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ เมฆขาว
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_16 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ เมฆขาว
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — email: fiction16@example.invalid
เอกสารที่ต้องใช้ (required_documents): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_16'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_16"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_16",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_16"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 22,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional White Cloud service",
          "th": "เลือกบริการสมมุติ เมฆขาว"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_16",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01925

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_17`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง มะลิ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_17**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ มะลิ
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_17 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ มะลิ
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — facebook: https://example.invalid/demo20/social/17
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Jasmine
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_17'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_17"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_17",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_17"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 20,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Jasmine service",
          "th": "เลือกบริการสมมุติ มะลิ"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_17",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Jasmine"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01935

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_18`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง กระเบน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_18**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ กระเบน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_18
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — demo20_contact_18 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ กระเบน
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — website: https://example.invalid/demo20/contact/18
3. แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง — website: https://example.invalid/demo20/contact/18
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Ray
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_18'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_18"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_18",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_18"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 22,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Ray service",
          "th": "เลือกบริการสมมุติ กระเบน"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_18",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      },
      {
        "contact_id": "demo20_contact_18",
        "instruction": {
          "en": "Ask the demo operator for session-specific help",
          "th": "แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง"
        },
        "order": 3
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Ray"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01945

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_19`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง แปะก๊วย มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_19**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ แปะก๊วย
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_19 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ แปะก๊วย
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — phone: DEMO-NON-DIALABLE-19
เอกสารที่ต้องใช้ (required_documents): • DEMO pass Ginkgo
• DEMO group list 19
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_19'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_19"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_19",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_19"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Ginkgo service",
          "th": "เลือกบริการสมมุติ แปะก๊วย"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_19",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "DEMO pass Ginkgo",
      "DEMO group list 19"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01955

**หมวด:** procedure • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_procedure_20`

### ผู้ใช้ถามอะไร

```text
ขั้นตอนทดลอง รุ่งเรือง มีขั้นตอนอะไรและต้องใช้เอกสารอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ขั้นตอน (`steps`), เอกสารที่ต้องใช้ (`required_documents`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_procedure_20**
• ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production: 1. เลือกบริการสมมุติ รุ่งเรือง
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — demo20_contact_20 [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ขั้นตอน (steps): 1. เลือกบริการสมมุติ รุ่งเรือง
2. ตรวจชื่อและเงื่อนไขก่อนยืนยัน — onsite: DEMO desk Radiance
เอกสารที่ต้องใช้ (required_documents): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_procedure_20'] และหัวข้อ ['steps']; field ของ target ที่ยังไม่มี obligation คือ ['required_documents']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R10 — คำในชื่อรายการหรือ alias ถูกนับเป็นคำถามด้วย**: field_requests รับ q ทั้งประโยคก่อนตัดชื่อออก; ขั้นตอนตัด alias อยู่เฉพาะ remainder หลังเลือก fields จึงอาจได้หัวข้อจากชื่อและยังไม่รู้ส่วนที่ผู้ใช้ถาม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_procedure_20"
    ],
    "requested_fields": [
      "steps"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_procedure_20",
      "field": "steps",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/steps",
          "source_id": "fixture20_demo20_procedure_20"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 0,
      "inside_named_entity": true
    },
    {
      "field": "steps",
      "term": "ขั้นตอน",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:required_documents

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "steps": {
    "evidence_refs": [
      {
        "locator": "/values/steps",
        "source_id": "fixture20_demo20_procedure_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "contact_id": null,
        "instruction": {
          "en": "Select the fictional Radiance service",
          "th": "เลือกบริการสมมุติ รุ่งเรือง"
        },
        "order": 1
      },
      {
        "contact_id": "demo20_contact_20",
        "instruction": {
          "en": "Check names and conditions before confirming",
          "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
        },
        "order": 2
      }
    ]
  },
  "required_documents": {
    "evidence_refs": [
      {
        "locator": "/values/required_documents",
        "source_id": "fixture20_demo20_procedure_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

