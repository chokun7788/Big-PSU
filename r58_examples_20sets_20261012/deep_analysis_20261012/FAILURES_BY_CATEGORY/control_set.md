# ภาคผนวกเคสไม่ผ่าน — control_set / 20 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 02765](#case-02765), [Case 02775](#case-02775), [Case 02785](#case-02785), [Case 02795](#case-02795), [Case 02805](#case-02805), [Case 02815](#case-02815), [Case 02825](#case-02825), [Case 02835](#case-02835), [Case 02845](#case-02845), [Case 02855](#case-02855), [Case 02865](#case-02865), [Case 02875](#case-02875), [Case 02885](#case-02885), [Case 02895](#case-02895), [Case 02905](#case-02905), [Case 02915](#case-02915), [Case 02925](#case-02925), [Case 02935](#case-02935), [Case 02945](#case-02945), [Case 02955](#case-02955)

## Case 02765

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_01`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ดาวเหนือ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_01**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ สวนเมฆ)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ สวนเมฆ) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): Nintendo Switch
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ สวนเมฆ
เคลื่อนที่ → DEMO_gamepad_2 / press / คำสั่งสมมุติของ สวนเมฆ
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_01'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_01"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_01",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_01"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 55,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "Nintendo Switch"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Cloud Garden",
          "th": "คำสั่งสมมุติของ สวนเมฆ"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Cloud Garden",
          "th": "คำสั่งสมมุติของ สวนเมฆ"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02775

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_02`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ดาวเหนือ พลัส ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_02**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ วงโคจรคู่)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ วงโคจรคู่)
• ย้อนกลับ → DEMO_gamepad_3 (press; คำสั่งสมมุติของ วงโคจรคู่) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PS5
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ วงโคจรคู่
เคลื่อนที่ → DEMO_gamepad_2 / press / คำสั่งสมมุติของ วงโคจรคู่
ย้อนกลับ → DEMO_gamepad_3 / press / คำสั่งสมมุติของ วงโคจรคู่
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_02'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_02"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_02",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_02"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 60,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PS5"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Orbit Duo",
          "th": "คำสั่งสมมุติของ วงโคจรคู่"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Orbit Duo",
          "th": "คำสั่งสมมุติของ วงโคจรคู่"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Back",
          "th": "ย้อนกลับ"
        },
        "buttons": [
          "DEMO_gamepad_3"
        ],
        "context": {
          "en": "Fictional input for Orbit Duo",
          "th": "คำสั่งสมมุติของ วงโคจรคู่"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02785

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_03`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ละอองฝน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_03**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_vr_motion_1 (press; คำสั่งสมมุติของ ประภาคารเสมือน) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): VR
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_vr_motion_1 / press / คำสั่งสมมุติของ ประภาคารเสมือน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_03'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_03"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_03",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_03"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 54,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "VR"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_vr_motion_1"
        ],
        "context": {
          "en": "Fictional input for Virtual Beacon",
          "th": "คำสั่งสมมุติของ ประภาคารเสมือน"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02795

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_04`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง สายหมอก ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_04**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_racing_wheel_1 (press; คำสั่งสมมุติของ ทางโค้งสีเงิน)
• เคลื่อนที่ → DEMO_racing_wheel_2 (press; คำสั่งสมมุติของ ทางโค้งสีเงิน) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): Cockpit
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_racing_wheel_1 / press / คำสั่งสมมุติของ ทางโค้งสีเงิน
เคลื่อนที่ → DEMO_racing_wheel_2 / press / คำสั่งสมมุติของ ทางโค้งสีเงิน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_04'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_04"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_04",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_04"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 54,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "Cockpit"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_racing_wheel_1"
        ],
        "context": {
          "en": "Fictional input for Silver Curve",
          "th": "คำสั่งสมมุติของ ทางโค้งสีเงิน"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_racing_wheel_2"
        ],
        "context": {
          "en": "Fictional input for Silver Curve",
          "th": "คำสั่งสมมุติของ ทางโค้งสีเงิน"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02805

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_05`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง บัวสีคราม ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_05**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ ก้อนบล็อกสี)
• เคลื่อนที่ → DEMO_keyboard_mouse_2 (press; คำสั่งสมมุติของ ก้อนบล็อกสี)
• ย้อนกลับ → DEMO_keyboard_mouse_3 (press; คำสั่งสมมุติของ ก้อนบล็อกสี) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ ก้อนบล็อกสี
เคลื่อนที่ → DEMO_keyboard_mouse_2 / press / คำสั่งสมมุติของ ก้อนบล็อกสี
ย้อนกลับ → DEMO_keyboard_mouse_3 / press / คำสั่งสมมุติของ ก้อนบล็อกสี
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_05'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_05"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_05",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_05"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 56,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Colour Blocks",
          "th": "คำสั่งสมมุติของ ก้อนบล็อกสี"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_keyboard_mouse_2"
        ],
        "context": {
          "en": "Fictional input for Colour Blocks",
          "th": "คำสั่งสมมุติของ ก้อนบล็อกสี"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Back",
          "th": "ย้อนกลับ"
        },
        "buttons": [
          "DEMO_keyboard_mouse_3"
        ],
        "context": {
          "en": "Fictional input for Colour Blocks",
          "th": "คำสั่งสมมุติของ ก้อนบล็อกสี"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02815

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_06`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ปะการัง ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_06**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ สะพานเพื่อน) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): Nintendo Switch
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ สะพานเพื่อน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_06'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_06"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_06",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_06"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 54,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "Nintendo Switch"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Friend Bridge",
          "th": "คำสั่งสมมุติของ สะพานเพื่อน"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02825

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_07`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ตะวันอ่อน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_07**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ ทีมดาวตก)
• เคลื่อนที่ → DEMO_keyboard_mouse_2 (press; คำสั่งสมมุติของ ทีมดาวตก) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ ทีมดาวตก
เคลื่อนที่ → DEMO_keyboard_mouse_2 / press / คำสั่งสมมุติของ ทีมดาวตก
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_07'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_07"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_07",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_07"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 56,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Meteor Team",
          "th": "คำสั่งสมมุติของ ทีมดาวตก"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_keyboard_mouse_2"
        ],
        "context": {
          "en": "Fictional input for Meteor Team",
          "th": "คำสั่งสมมุติของ ทีมดาวตก"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02835

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_08`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ฟ้าหลังฝน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_08**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ ผู้ส่งจดหมาย)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ ผู้ส่งจดหมาย)
• ย้อนกลับ → DEMO_gamepad_3 (press; คำสั่งสมมุติของ ผู้ส่งจดหมาย) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PS5
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ ผู้ส่งจดหมาย
เคลื่อนที่ → DEMO_gamepad_2 / press / คำสั่งสมมุติของ ผู้ส่งจดหมาย
ย้อนกลับ → DEMO_gamepad_3 / press / คำสั่งสมมุติของ ผู้ส่งจดหมาย
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_08'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_08"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_08",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_08"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 56,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PS5"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Letter Runner",
          "th": "คำสั่งสมมุติของ ผู้ส่งจดหมาย"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Letter Runner",
          "th": "คำสั่งสมมุติของ ผู้ส่งจดหมาย"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Back",
          "th": "ย้อนกลับ"
        },
        "buttons": [
          "DEMO_gamepad_3"
        ],
        "context": {
          "en": "Fictional input for Letter Runner",
          "th": "คำสั่งสมมุติของ ผู้ส่งจดหมาย"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02845

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_09`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ลมทะเล ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_09**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ ท่าเรือดิจิทัล) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ ท่าเรือดิจิทัล
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_09'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_09"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_09",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_09"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 53,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Digital Harbour",
          "th": "คำสั่งสมมุติของ ท่าเรือดิจิทัล"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02855

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_10`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ห้องสมุดดาว ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_10**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ บทเพลงลูกบาศก์)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ บทเพลงลูกบาศก์) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PS5
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ บทเพลงลูกบาศก์
เคลื่อนที่ → DEMO_gamepad_2 / press / คำสั่งสมมุติของ บทเพลงลูกบาศก์
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_10'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_10"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_10",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_10"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 58,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PS5"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Cube Melody",
          "th": "คำสั่งสมมุติของ บทเพลงลูกบาศก์"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Cube Melody",
          "th": "คำสั่งสมมุติของ บทเพลงลูกบาศก์"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02865

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_11`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ต้นเฟิร์น ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_11**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ เขาวงกตเงา)
• เคลื่อนที่ → DEMO_keyboard_mouse_2 (press; คำสั่งสมมุติของ เขาวงกตเงา)
• ย้อนกลับ → DEMO_keyboard_mouse_3 (press; คำสั่งสมมุติของ เขาวงกตเงา) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ เขาวงกตเงา
เคลื่อนที่ → DEMO_keyboard_mouse_2 / press / คำสั่งสมมุติของ เขาวงกตเงา
ย้อนกลับ → DEMO_keyboard_mouse_3 / press / คำสั่งสมมุติของ เขาวงกตเงา
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_11'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_11"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_11",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_11"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 56,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Shadow Maze",
          "th": "คำสั่งสมมุติของ เขาวงกตเงา"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_keyboard_mouse_2"
        ],
        "context": {
          "en": "Fictional input for Shadow Maze",
          "th": "คำสั่งสมมุติของ เขาวงกตเงา"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Back",
          "th": "ย้อนกลับ"
        },
        "buttons": [
          "DEMO_keyboard_mouse_3"
        ],
        "context": {
          "en": "Fictional input for Shadow Maze",
          "th": "คำสั่งสมมุติของ เขาวงกตเงา"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02875

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_12`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง ทองทราย ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_12**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_vr_motion_1 (press; คำสั่งสมมุติของ ห้องทดลองลอยฟ้า) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): VR
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_vr_motion_1 / press / คำสั่งสมมุติของ ห้องทดลองลอยฟ้า
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_12'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_12"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_12",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_12"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 54,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "VR"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_vr_motion_1"
        ],
        "context": {
          "en": "Fictional input for Sky Laboratory",
          "th": "คำสั่งสมมุติของ ห้องทดลองลอยฟ้า"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02885

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_13`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง จันทร์เสี้ยว ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_13**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_racing_wheel_1 (press; คำสั่งสมมุติของ ขบวนรถจิ๋ว)
• เคลื่อนที่ → DEMO_racing_wheel_2 (press; คำสั่งสมมุติของ ขบวนรถจิ๋ว) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): Cockpit
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_racing_wheel_1 / press / คำสั่งสมมุติของ ขบวนรถจิ๋ว
เคลื่อนที่ → DEMO_racing_wheel_2 / press / คำสั่งสมมุติของ ขบวนรถจิ๋ว
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_13'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_13"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_13",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_13"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 59,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "Cockpit"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_racing_wheel_1"
        ],
        "context": {
          "en": "Fictional input for Tiny Convoy",
          "th": "คำสั่งสมมุติของ ขบวนรถจิ๋ว"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_racing_wheel_2"
        ],
        "context": {
          "en": "Fictional input for Tiny Convoy",
          "th": "คำสั่งสมมุติของ ขบวนรถจิ๋ว"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02895

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_14`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง แสงอรุณ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_14**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ ครัวสายรุ้ง)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ ครัวสายรุ้ง)
• ย้อนกลับ → DEMO_gamepad_3 (press; คำสั่งสมมุติของ ครัวสายรุ้ง) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): Nintendo Switch
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ ครัวสายรุ้ง
เคลื่อนที่ → DEMO_gamepad_2 / press / คำสั่งสมมุติของ ครัวสายรุ้ง
ย้อนกลับ → DEMO_gamepad_3 / press / คำสั่งสมมุติของ ครัวสายรุ้ง
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_14'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_14"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_14",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_14"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 54,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "Nintendo Switch"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Rainbow Kitchen",
          "th": "คำสั่งสมมุติของ ครัวสายรุ้ง"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Rainbow Kitchen",
          "th": "คำสั่งสมมุติของ ครัวสายรุ้ง"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Back",
          "th": "ย้อนกลับ"
        },
        "buttons": [
          "DEMO_gamepad_3"
        ],
        "context": {
          "en": "Fictional input for Rainbow Kitchen",
          "th": "คำสั่งสมมุติของ ครัวสายรุ้ง"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02905

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_15`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง กิ่งไผ่ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_15**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ กล่องปริศนา) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ กล่องปริศนา
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_15'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_15"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_15",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_15"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 54,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Puzzle Box",
          "th": "คำสั่งสมมุติของ กล่องปริศนา"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02915

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_16`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง เมฆขาว ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_16**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ บันไดเสียง)
• เคลื่อนที่ → DEMO_keyboard_mouse_2 (press; คำสั่งสมมุติของ บันไดเสียง) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ บันไดเสียง
เคลื่อนที่ → DEMO_keyboard_mouse_2 / press / คำสั่งสมมุติของ บันไดเสียง
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_16'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_16"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_16",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_16"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 53,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Sound Ladder",
          "th": "คำสั่งสมมุติของ บันไดเสียง"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_keyboard_mouse_2"
        ],
        "context": {
          "en": "Fictional input for Sound Ladder",
          "th": "คำสั่งสมมุติของ บันไดเสียง"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02925

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_17`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง มะลิ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_17**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ เมืองกระดาษ)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ เมืองกระดาษ)
• ย้อนกลับ → DEMO_gamepad_3 (press; คำสั่งสมมุติของ เมืองกระดาษ) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PS5
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ เมืองกระดาษ
เคลื่อนที่ → DEMO_gamepad_2 / press / คำสั่งสมมุติของ เมืองกระดาษ
ย้อนกลับ → DEMO_gamepad_3 / press / คำสั่งสมมุติของ เมืองกระดาษ
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_17'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_17"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_17",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_17"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 51,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PS5"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Paper Town",
          "th": "คำสั่งสมมุติของ เมืองกระดาษ"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Paper Town",
          "th": "คำสั่งสมมุติของ เมืองกระดาษ"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Back",
          "th": "ย้อนกลับ"
        },
        "buttons": [
          "DEMO_gamepad_3"
        ],
        "context": {
          "en": "Fictional input for Paper Town",
          "th": "คำสั่งสมมุติของ เมืองกระดาษ"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02935

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_18`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง กระเบน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_18**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ ดาวเทียมหลงทาง) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ ดาวเทียมหลงทาง
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_18'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_18"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_18",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_18"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 53,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Lost Satellite",
          "th": "คำสั่งสมมุติของ ดาวเทียมหลงทาง"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02945

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_19`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง แปะก๊วย ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_19**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_gamepad_1 (press; คำสั่งสมมุติของ ลานนักสำรวจ)
• เคลื่อนที่ → DEMO_gamepad_2 (press; คำสั่งสมมุติของ ลานนักสำรวจ) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): Nintendo Switch
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_gamepad_1 / press / คำสั่งสมมุติของ ลานนักสำรวจ
เคลื่อนที่ → DEMO_gamepad_2 / press / คำสั่งสมมุติของ ลานนักสำรวจ
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_19'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_19"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_19",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_19"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 54,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "Nintendo Switch"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_gamepad_1"
        ],
        "context": {
          "en": "Fictional input for Explorer Yard",
          "th": "คำสั่งสมมุติของ ลานนักสำรวจ"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_gamepad_2"
        ],
        "context": {
          "en": "Fictional input for Explorer Yard",
          "th": "คำสั่งสมมุติของ ลานนักสำรวจ"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 02955

**หมวด:** control_set • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_control_set_20`

### ผู้ใช้ถามอะไร

```text
ชุดควบคุมทดลอง รุ่งเรือง ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: แพลตฟอร์ม (`platform`), ปุ่มควบคุม (`bindings`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_control_set_20**
• ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record: • ยืนยัน → DEMO_keyboard_mouse_1 (press; คำสั่งสมมุติของ เวทีฝึกฝน)
• เคลื่อนที่ → DEMO_keyboard_mouse_2 (press; คำสั่งสมมุติของ เวทีฝึกฝน)
• ย้อนกลับ → DEMO_keyboard_mouse_3 (press; คำสั่งสมมุติของ เวทีฝึกฝน) [S1]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
แพลตฟอร์ม (platform): PC
ปุ่มควบคุม (bindings): ยืนยัน → DEMO_keyboard_mouse_1 / press / คำสั่งสมมุติของ เวทีฝึกฝน
เคลื่อนที่ → DEMO_keyboard_mouse_2 / press / คำสั่งสมมุติของ เวทีฝึกฝน
ย้อนกลับ → DEMO_keyboard_mouse_3 / press / คำสั่งสมมุติของ เวทีฝึกฝน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_control_set_20'] และหัวข้อ ['bindings']; field ของ target ที่ยังไม่มี obligation คือ ['platform']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_control_set_20"
    ],
    "requested_fields": [
      "bindings"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_control_set_20",
      "field": "bindings",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/bindings",
          "source_id": "fixture20_demo20_control_set_20"
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
      "field": "bindings",
      "term": "ปุ่ม",
      "offset": 56,
      "inside_named_entity": false
    },
    {
      "field": "bindings",
      "term": "ควบคุม",
      "offset": 3,
      "inside_named_entity": true
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:platform

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "platform": {
    "evidence_refs": [
      {
        "locator": "/values/platform",
        "source_id": "fixture20_demo20_control_set_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "PC"
  },
  "bindings": {
    "evidence_refs": [
      {
        "locator": "/values/bindings",
        "source_id": "fixture20_demo20_control_set_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "action": {
          "en": "Confirm",
          "th": "ยืนยัน"
        },
        "buttons": [
          "DEMO_keyboard_mouse_1"
        ],
        "context": {
          "en": "Fictional input for Practice Arena",
          "th": "คำสั่งสมมุติของ เวทีฝึกฝน"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Move",
          "th": "เคลื่อนที่"
        },
        "buttons": [
          "DEMO_keyboard_mouse_2"
        ],
        "context": {
          "en": "Fictional input for Practice Arena",
          "th": "คำสั่งสมมุติของ เวทีฝึกฝน"
        },
        "gesture": "press"
      },
      {
        "action": {
          "en": "Back",
          "th": "ย้อนกลับ"
        },
        "buttons": [
          "DEMO_keyboard_mouse_3"
        ],
        "context": {
          "en": "Fictional input for Practice Arena",
          "th": "คำสั่งสมมุติของ เวทีฝึกฝน"
        },
        "gesture": "press"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

