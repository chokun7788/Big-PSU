# ภาคผนวกเคสไม่ผ่าน — contact / 40 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 01565](#case-01565), [Case 01568](#case-01568), [Case 01575](#case-01575), [Case 01578](#case-01578), [Case 01585](#case-01585), [Case 01588](#case-01588), [Case 01595](#case-01595), [Case 01598](#case-01598), [Case 01605](#case-01605), [Case 01608](#case-01608), [Case 01615](#case-01615), [Case 01618](#case-01618), [Case 01625](#case-01625), [Case 01628](#case-01628), [Case 01635](#case-01635), [Case 01638](#case-01638), [Case 01645](#case-01645), [Case 01648](#case-01648), [Case 01655](#case-01655), [Case 01658](#case-01658), [Case 01665](#case-01665), [Case 01668](#case-01668), [Case 01675](#case-01675), [Case 01678](#case-01678), [Case 01685](#case-01685), [Case 01688](#case-01688), [Case 01695](#case-01695), [Case 01698](#case-01698), [Case 01705](#case-01705), [Case 01708](#case-01708), [Case 01715](#case-01715), [Case 01718](#case-01718), [Case 01725](#case-01725), [Case 01728](#case-01728), [Case 01735](#case-01735), [Case 01738](#case-01738), [Case 01745](#case-01745), [Case 01748](#case-01748), [Case 01755](#case-01755), [Case 01758](#case-01758)

## Case 01565

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_01`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ดาวเหนือ ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_01**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: fiction01@example.invalid [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction01@example.invalid
เวลาติดต่อ (office_hours): ช่วงทดลอง 09:00–18:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_01'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_01"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_01",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_01"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 32,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 26,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction01@example.invalid"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 09:00–18:00",
      "th": "ช่วงทดลอง 09:00–18:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01568

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_01`

### ผู้ใช้ถามอะไร

```text
Demo help channel Northstar Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_01**
• channel: email [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction01@example.invalid
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_01'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_01"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_01",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_01"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 28,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction01@example.invalid"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01575

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_02`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ดาวเหนือ พลัส ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_02**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/social/2 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/2
เวลาติดต่อ (office_hours): ช่วงทดลอง 10:00–19:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_02'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_02"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_02",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_02"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 37,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/2"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 10:00–19:00",
      "th": "ช่วงทดลอง 10:00–19:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01578

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_02`

### ผู้ใช้ถามอะไร

```text
Demo help channel Northstar Plus Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_02**
• channel: facebook [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/2
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_02'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_02"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_02",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_02"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 33,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/2"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01585

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_03`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ละอองฝน ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_03**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/contact/3 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/3
เวลาติดต่อ (office_hours): ช่วงทดลอง 11:00–20:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_03'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_03"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_03",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_03"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/3"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 11:00–20:00",
      "th": "ช่วงทดลอง 11:00–20:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01588

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_03`

### ผู้ใช้ถามอะไร

```text
Demo help channel Drizzle Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_03**
• channel: website [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/3
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_03'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_03"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_03",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_03"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/3"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01595

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_04`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ สายหมอก ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_04**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO-NON-DIALABLE-04 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-04
เวลาติดต่อ (office_hours): ช่วงทดลอง 08:00–17:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_04'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_04"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_04",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_04"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-04"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 08:00–17:00",
      "th": "ช่วงทดลอง 08:00–17:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01598

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_04`

### ผู้ใช้ถามอะไร

```text
Demo help channel Mist Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_04**
• channel: phone [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-04
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_04'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_04"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_04",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_04"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-04"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01605

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_05`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ บัวสีคราม ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_05**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO desk Indigo Lotus [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Indigo Lotus
เวลาติดต่อ (office_hours): ช่วงทดลอง 09:00–18:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_05'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_05"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_05",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_05"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 33,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 27,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Indigo Lotus"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 09:00–18:00",
      "th": "ช่วงทดลอง 09:00–18:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01608

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_05`

### ผู้ใช้ถามอะไร

```text
Demo help channel Indigo Lotus Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_05**
• channel: onsite [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Indigo Lotus
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_05'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_05"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_05",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_05"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 31,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Indigo Lotus"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01615

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_06`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ปะการัง ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_06**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: fiction06@example.invalid [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction06@example.invalid
เวลาติดต่อ (office_hours): ช่วงทดลอง 10:00–19:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_06'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_06"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_06",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_06"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction06@example.invalid"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 10:00–19:00",
      "th": "ช่วงทดลอง 10:00–19:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01618

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_06`

### ผู้ใช้ถามอะไร

```text
Demo help channel Coral Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_06**
• channel: email [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction06@example.invalid
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_06'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_06"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_06",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_06"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction06@example.invalid"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01625

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_07`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ตะวันอ่อน ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_07**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/social/7 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/7
เวลาติดต่อ (office_hours): ช่วงทดลอง 11:00–20:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_07'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_07"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_07",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_07"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 33,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 27,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/7"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 11:00–20:00",
      "th": "ช่วงทดลอง 11:00–20:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01628

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_07`

### ผู้ใช้ถามอะไร

```text
Demo help channel Gentle Sun Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_07**
• channel: facebook [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/7
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_07'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_07"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_07",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_07"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/7"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01635

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_08`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ฟ้าหลังฝน ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_08**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/contact/8 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/8
เวลาติดต่อ (office_hours): ช่วงทดลอง 08:00–17:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_08'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_08"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_08",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_08"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 33,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 27,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/8"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 08:00–17:00",
      "th": "ช่วงทดลอง 08:00–17:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01638

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_08`

### ผู้ใช้ถามอะไร

```text
Demo help channel After Rain Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_08**
• channel: website [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/8
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_08'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_08"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_08",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_08"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/8"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01645

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_09`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ลมทะเล ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_09**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO-NON-DIALABLE-09 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-09
เวลาติดต่อ (office_hours): ช่วงทดลอง 09:00–18:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_09'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_09"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_09",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_09"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 30,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 24,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-09"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 09:00–18:00",
      "th": "ช่วงทดลอง 09:00–18:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01648

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_09`

### ผู้ใช้ถามอะไร

```text
Demo help channel Sea Breeze Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_09**
• channel: phone [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-09
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_09'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_09"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_09",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_09"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-09"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01655

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_10`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ห้องสมุดดาว ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_10**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO desk Star Library [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Star Library
เวลาติดต่อ (office_hours): ช่วงทดลอง 10:00–19:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_10'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_10"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_10",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_10"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 35,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 29,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 44,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Star Library"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 10:00–19:00",
      "th": "ช่วงทดลอง 10:00–19:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01658

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_10`

### ผู้ใช้ถามอะไร

```text
Demo help channel Star Library Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_10**
• channel: onsite [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Star Library
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_10'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_10"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_10",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_10"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 31,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Star Library"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01665

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_11`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ต้นเฟิร์น ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_11**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: fiction11@example.invalid [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction11@example.invalid
เวลาติดต่อ (office_hours): ช่วงทดลอง 11:00–20:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_11'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_11"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_11",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_11"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 33,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 27,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction11@example.invalid"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 11:00–20:00",
      "th": "ช่วงทดลอง 11:00–20:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01668

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_11`

### ผู้ใช้ถามอะไร

```text
Demo help channel Fern Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_11**
• channel: email [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction11@example.invalid
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_11'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_11"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_11",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_11"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction11@example.invalid"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01675

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_12`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ ทองทราย ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_12**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/social/12 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/12
เวลาติดต่อ (office_hours): ช่วงทดลอง 08:00–17:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_12'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_12"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_12",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_12"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/12"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 08:00–17:00",
      "th": "ช่วงทดลอง 08:00–17:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01678

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_12`

### ผู้ใช้ถามอะไร

```text
Demo help channel Sand Gold Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_12**
• channel: facebook [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/12
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_12'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_12"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_12",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_12"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 28,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/12"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01685

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_13`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ จันทร์เสี้ยว ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_13**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/contact/13 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/13
เวลาติดต่อ (office_hours): ช่วงทดลอง 09:00–18:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_13'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_13"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_13",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_13"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 36,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 30,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 45,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/13"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 09:00–18:00",
      "th": "ช่วงทดลอง 09:00–18:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01688

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_13`

### ผู้ใช้ถามอะไร

```text
Demo help channel Crescent Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_13**
• channel: website [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/13
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_13'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_13"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_13",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_13"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/13"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01695

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_14`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ แสงอรุณ ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_14**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO-NON-DIALABLE-14 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-14
เวลาติดต่อ (office_hours): ช่วงทดลอง 10:00–19:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_14'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_14"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_14",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_14"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-14"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 10:00–19:00",
      "th": "ช่วงทดลอง 10:00–19:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01698

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_14`

### ผู้ใช้ถามอะไร

```text
Demo help channel Dawn Light Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_14**
• channel: phone [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-14
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_14'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_14"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_14",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_14"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-14"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01705

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_15`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ กิ่งไผ่ ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_15**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO desk Bamboo [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Bamboo
เวลาติดต่อ (office_hours): ช่วงทดลอง 11:00–20:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_15'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_15"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_15",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_15"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Bamboo"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 11:00–20:00",
      "th": "ช่วงทดลอง 11:00–20:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01708

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_15`

### ผู้ใช้ถามอะไร

```text
Demo help channel Bamboo Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_15**
• channel: onsite [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Bamboo
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_15'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_15"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_15",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_15"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Bamboo"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01715

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_16`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ เมฆขาว ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_16**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: fiction16@example.invalid [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction16@example.invalid
เวลาติดต่อ (office_hours): ช่วงทดลอง 08:00–17:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_16'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_16"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_16",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_16"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 30,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 24,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction16@example.invalid"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 08:00–17:00",
      "th": "ช่วงทดลอง 08:00–17:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01718

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_16`

### ผู้ใช้ถามอะไร

```text
Demo help channel White Cloud Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_16**
• channel: email [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): fiction16@example.invalid
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_16'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_16"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_16",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_16"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 30,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "fiction16@example.invalid"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01725

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_17`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ มะลิ ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_17**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/social/17 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/17
เวลาติดต่อ (office_hours): ช่วงทดลอง 09:00–18:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_17'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_17"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_17",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_17"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 28,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 22,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 37,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/17"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 09:00–18:00",
      "th": "ช่วงทดลอง 09:00–18:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01728

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_17`

### ผู้ใช้ถามอะไร

```text
Demo help channel Jasmine Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_17**
• channel: facebook [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/social/17
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_17'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_17"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_17",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_17"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/social/17"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01735

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_18`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ กระเบน ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_18**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/contact/18 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/18
เวลาติดต่อ (office_hours): ช่วงทดลอง 10:00–19:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_18'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_18"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_18",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_18"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 30,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 24,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/18"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 10:00–19:00",
      "th": "ช่วงทดลอง 10:00–19:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01738

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_18`

### ผู้ใช้ถามอะไร

```text
Demo help channel Ray Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_18**
• channel: website [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): https://example.invalid/demo20/contact/18
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_18'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_18"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_18",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_18"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 22,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "https://example.invalid/demo20/contact/18"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01745

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_19`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ แปะก๊วย ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_19**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO-NON-DIALABLE-19 [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-19
เวลาติดต่อ (office_hours): ช่วงทดลอง 11:00–20:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_19'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_19"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_19",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_19"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 31,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-19"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 11:00–20:00",
      "th": "ช่วงทดลอง 11:00–20:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01748

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_19`

### ผู้ใช้ถามอะไร

```text
Demo help channel Ginkgo Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_19**
• channel: phone [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO-NON-DIALABLE-19
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_19'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_19"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_19",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_19"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO-NON-DIALABLE-19"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01755

**หมวด:** contact • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_contact_20`

### ผู้ใช้ถามอะไร

```text
ช่องทางช่วยเหลือ รุ่งเรือง ติดต่อที่ไหนและติดต่อได้ช่วงไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`), เวลาติดต่อ (`office_hours`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_20**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: DEMO desk Radiance [S1]

address: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Radiance
เวลาติดต่อ (office_hours): ช่วงทดลอง 08:00–17:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_20'] และหัวข้อ ['address', 'value']; field ของ target ที่ยังไม่มี obligation คือ ['office_hours']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_20"
    ],
    "requested_fields": [
      "address",
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_20",
      "field": "value",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/value",
          "source_id": "fixture20_demo20_contact_20"
        }
      ]
    },
    {
      "record_id": null,
      "field": "address",
      "status": "unknown"
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
      "field": "address",
      "term": "ที่ไหน",
      "offset": 33,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 27,
      "inside_named_entity": false
    },
    {
      "field": "value",
      "term": "ติดต่อ",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:office_hours

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Radiance"
  },
  "office_hours": {
    "evidence_refs": [
      {
        "locator": "/values/office_hours",
        "source_id": "fixture20_demo20_contact_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Demo hours 08:00–17:00",
      "th": "ช่วงทดลอง 08:00–17:00"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01758

**หมวด:** contact • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_contact_20`

### ผู้ใช้ถามอะไร

```text
Demo help channel Radiance Where can I reach the operator?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่องทางติดต่อ (`value`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_contact_20**
• channel: onsite [S1]

supported platforms: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่องทางติดต่อ (value): DEMO desk Radiance
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_contact_20'] และหัวข้อ ['supported_platforms', 'channel']; field ของ target ที่ยังไม่มี obligation คือ ['value']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_contact_20"
    ],
    "requested_fields": [
      "supported_platforms",
      "channel"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_contact_20",
      "field": "channel",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/channel",
          "source_id": "fixture20_demo20_contact_20"
        }
      ]
    },
    {
      "record_id": null,
      "field": "supported_platforms",
      "status": "unknown"
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
      "field": "supported_platforms",
      "term": "where can",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "channel",
      "kind": "contact",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:value

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "value": {
    "evidence_refs": [
      {
        "locator": "/values/value",
        "source_id": "fixture20_demo20_contact_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO desk Radiance"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

