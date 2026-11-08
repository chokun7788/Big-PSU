# เคสผ่านเนื้อหาแต่มีประเด็นเพิ่มเติม — 86 เคส

ไม่ใช่การย้ายทุกเคสเหล่านี้ไปเป็นผิดโดยอัตโนมัติ: domain bundles บางแบบจำเป็นต่อราคา/กฎ แต่การเลือกหัวข้อยังต้องแยกจากการพิมพ์ค่าไว้ครบ

## Case 00203

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_01`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ดาวเหนือ รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ดาวเหนือ**
• โซนนี้ใช้ทำอะไร: โซนจำลอง Nintendo Switch สำหรับสวนเมฆ [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 2 ห้อง 101 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ดาวเหนือ [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 7 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 7
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_01"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_01",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_01"
        }
      ]
    },
    {
      "record_id": "demo20_zone_01",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_01"
        }
      ]
    },
    {
      "record_id": "demo20_zone_01",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_01"
        }
      ]
    },
    {
      "record_id": "demo20_zone_01",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_01"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 7
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00213

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_02`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ดาวเหนือ พลัส รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ดาวเหนือ พลัส**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PS5 สำหรับวงโคจรคู่ [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 3 ห้อง 102 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ดาวเหนือ พลัส [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 6 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 6
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_02"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_02",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_02"
        }
      ]
    },
    {
      "record_id": "demo20_zone_02",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_02"
        }
      ]
    },
    {
      "record_id": "demo20_zone_02",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_02"
        }
      ]
    },
    {
      "record_id": "demo20_zone_02",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_02"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 45,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 6
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00223

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_03`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ละอองฝน รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ละอองฝน**
• โซนนี้ใช้ทำอะไร: โซนจำลอง VR สำหรับประภาคารเสมือน [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 4 ห้อง 103 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ละอองฝน [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 3 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 3
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_03",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_03"
        }
      ]
    },
    {
      "record_id": "demo20_zone_03",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_03"
        }
      ]
    },
    {
      "record_id": "demo20_zone_03",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_03"
        }
      ]
    },
    {
      "record_id": "demo20_zone_03",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_03"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 3
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00233

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_04`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง สายหมอก รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง สายหมอก**
• โซนนี้ใช้ทำอะไร: โซนจำลอง Cockpit สำหรับทางโค้งสีเงิน [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 5 ห้อง 104 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง สายหมอก [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 4 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 4
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_04"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_04",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_04"
        }
      ]
    },
    {
      "record_id": "demo20_zone_04",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_04"
        }
      ]
    },
    {
      "record_id": "demo20_zone_04",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_04"
        }
      ]
    },
    {
      "record_id": "demo20_zone_04",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_04"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 4
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00243

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_05`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง บัวสีคราม รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง บัวสีคราม**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับก้อนบล็อกสี [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 1 ห้อง 105 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง บัวสีคราม [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 5 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 5
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_05"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_05",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_05"
        }
      ]
    },
    {
      "record_id": "demo20_zone_05",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_05"
        }
      ]
    },
    {
      "record_id": "demo20_zone_05",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_05"
        }
      ]
    },
    {
      "record_id": "demo20_zone_05",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_05"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 5
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00253

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_06`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ปะการัง รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ปะการัง**
• โซนนี้ใช้ทำอะไร: โซนจำลอง Nintendo Switch สำหรับสะพานเพื่อน [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 2 ห้อง 106 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ปะการัง [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 6 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 6
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_06"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_06",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_06"
        }
      ]
    },
    {
      "record_id": "demo20_zone_06",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_06"
        }
      ]
    },
    {
      "record_id": "demo20_zone_06",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_06"
        }
      ]
    },
    {
      "record_id": "demo20_zone_06",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_06"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 6
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00263

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_07`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ตะวันอ่อน รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ตะวันอ่อน**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับทีมดาวตก [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 3 ห้อง 107 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ตะวันอ่อน [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 13 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 13
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_07"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_07",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_07"
        }
      ]
    },
    {
      "record_id": "demo20_zone_07",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_07"
        }
      ]
    },
    {
      "record_id": "demo20_zone_07",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_07"
        }
      ]
    },
    {
      "record_id": "demo20_zone_07",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_07"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 13
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00273

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_08`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ฟ้าหลังฝน รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ฟ้าหลังฝน**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PS5 สำหรับผู้ส่งจดหมาย [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 4 ห้อง 108 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ฟ้าหลังฝน [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 6 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 6
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_08"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_08",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_08"
        }
      ]
    },
    {
      "record_id": "demo20_zone_08",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_08"
        }
      ]
    },
    {
      "record_id": "demo20_zone_08",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_08"
        }
      ]
    },
    {
      "record_id": "demo20_zone_08",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_08"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 6
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00283

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_09`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ลมทะเล รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ลมทะเล**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับท่าเรือดิจิทัล [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 5 ห้อง 109 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ลมทะเล [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 14 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 14
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_09"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_09",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_09"
        }
      ]
    },
    {
      "record_id": "demo20_zone_09",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_09"
        }
      ]
    },
    {
      "record_id": "demo20_zone_09",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_09"
        }
      ]
    },
    {
      "record_id": "demo20_zone_09",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_09"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 38,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 14
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00293

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_10`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ห้องสมุดดาว รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ห้องสมุดดาว**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PS5 สำหรับบทเพลงลูกบาศก์ [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 1 ห้อง 110 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ห้องสมุดดาว [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 7 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 7
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_10"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_10",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_10"
        }
      ]
    },
    {
      "record_id": "demo20_zone_10",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_10"
        }
      ]
    },
    {
      "record_id": "demo20_zone_10",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_10"
        }
      ]
    },
    {
      "record_id": "demo20_zone_10",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_10"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 43,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 7
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00303

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_11`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ต้นเฟิร์น รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ต้นเฟิร์น**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับเขาวงกตเงา [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 2 ห้อง 111 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ต้นเฟิร์น [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 7 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 7
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_11"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_11",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_11"
        }
      ]
    },
    {
      "record_id": "demo20_zone_11",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_11"
        }
      ]
    },
    {
      "record_id": "demo20_zone_11",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_11"
        }
      ]
    },
    {
      "record_id": "demo20_zone_11",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_11"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 7
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00313

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_12`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง ทองทราย รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง ทองทราย**
• โซนนี้ใช้ทำอะไร: โซนจำลอง VR สำหรับห้องทดลองลอยฟ้า [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 3 ห้อง 112 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง ทองทราย [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 3 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 3
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_12"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_12",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_12"
        }
      ]
    },
    {
      "record_id": "demo20_zone_12",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_12"
        }
      ]
    },
    {
      "record_id": "demo20_zone_12",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_12"
        }
      ]
    },
    {
      "record_id": "demo20_zone_12",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_12"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 3
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00323

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_13`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง จันทร์เสี้ยว รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง จันทร์เสี้ยว**
• โซนนี้ใช้ทำอะไร: โซนจำลอง Cockpit สำหรับขบวนรถจิ๋ว [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 4 ห้อง 113 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง จันทร์เสี้ยว [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 4 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 4
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_13"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_13",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_13"
        }
      ]
    },
    {
      "record_id": "demo20_zone_13",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_13"
        }
      ]
    },
    {
      "record_id": "demo20_zone_13",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_13"
        }
      ]
    },
    {
      "record_id": "demo20_zone_13",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_13"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 44,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 4
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00333

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_14`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง แสงอรุณ รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง แสงอรุณ**
• โซนนี้ใช้ทำอะไร: โซนจำลอง Nintendo Switch สำหรับครัวสายรุ้ง [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 5 ห้อง 114 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง แสงอรุณ [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 8 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 8
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_14"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_14",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_14"
        }
      ]
    },
    {
      "record_id": "demo20_zone_14",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_14"
        }
      ]
    },
    {
      "record_id": "demo20_zone_14",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_14"
        }
      ]
    },
    {
      "record_id": "demo20_zone_14",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_14"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 8
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00343

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_15`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง กิ่งไผ่ รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง กิ่งไผ่**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับกล่องปริศนา [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 1 ห้อง 115 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง กิ่งไผ่ [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 4 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 4
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_15"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_15",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_15"
        }
      ]
    },
    {
      "record_id": "demo20_zone_15",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_15"
        }
      ]
    },
    {
      "record_id": "demo20_zone_15",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_15"
        }
      ]
    },
    {
      "record_id": "demo20_zone_15",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_15"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 4
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00353

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_16`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง เมฆขาว รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง เมฆขาว**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับบันไดเสียง [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 2 ห้อง 116 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง เมฆขาว [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 4 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 4
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_16"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_16",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_16"
        }
      ]
    },
    {
      "record_id": "demo20_zone_16",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_16"
        }
      ]
    },
    {
      "record_id": "demo20_zone_16",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_16"
        }
      ]
    },
    {
      "record_id": "demo20_zone_16",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_16"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 38,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 4
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00363

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_17`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง มะลิ รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง มะลิ**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PS5 สำหรับเมืองกระดาษ [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 3 ห้อง 117 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง มะลิ [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 8 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 8
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_17"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_17",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_17"
        }
      ]
    },
    {
      "record_id": "demo20_zone_17",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_17"
        }
      ]
    },
    {
      "record_id": "demo20_zone_17",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_17"
        }
      ]
    },
    {
      "record_id": "demo20_zone_17",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_17"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 8
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00373

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_18`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง กระเบน รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง กระเบน**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับดาวเทียมหลงทาง [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 4 ห้อง 118 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง กระเบน [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 3 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 3
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_18"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_18",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_18"
        }
      ]
    },
    {
      "record_id": "demo20_zone_18",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_18"
        }
      ]
    },
    {
      "record_id": "demo20_zone_18",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_18"
        }
      ]
    },
    {
      "record_id": "demo20_zone_18",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_18"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 38,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 3
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00383

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_19`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง แปะก๊วย รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง แปะก๊วย**
• โซนนี้ใช้ทำอะไร: โซนจำลอง Nintendo Switch สำหรับลานนักสำรวจ [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 5 ห้อง 119 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง แปะก๊วย [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 9 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 9
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_19"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_19",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_19"
        }
      ]
    },
    {
      "record_id": "demo20_zone_19",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_19"
        }
      ]
    },
    {
      "record_id": "demo20_zone_19",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_19"
        }
      ]
    },
    {
      "record_id": "demo20_zone_19",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_19"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 9
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00393

**หมวด:** zone • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_zone_20`

### ผู้ใช้ถามอะไร

```text
โซนทดลอง รุ่งเรือง รองรับคนนั่งทั้งหมดได้กี่คน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: จำนวนที่นั่งในห้อง (`room_seats`)

### คำตอบที่ระบบส่งจริง

```text
**โซนทดลอง รุ่งเรือง**
• โซนนี้ใช้ทำอะไร: โซนจำลอง PC สำหรับเวทีฝึกฝน [S1]
• ตำแหน่งในศูนย์: อาคารทดสอบ ชั้น 1 ห้อง 120 [S2]
• PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ: โซนทดลอง รุ่งเรือง [S3]
• จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน: 12 [S4]

players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
จำนวนที่นั่งในห้อง (room_seats): 12
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_zone_20"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_zone_20",
      "field": "description",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/description",
          "source_id": "fixture20_demo20_zone_20"
        }
      ]
    },
    {
      "record_id": "demo20_zone_20",
      "field": "location",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/location",
          "source_id": "fixture20_demo20_zone_20"
        }
      ]
    },
    {
      "record_id": "demo20_zone_20",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_zone_20"
        }
      ]
    },
    {
      "record_id": "demo20_zone_20",
      "field": "room_seats",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/room_seats",
          "source_id": "fixture20_demo20_zone_20"
        }
      ]
    },
    {
      "record_id": null,
      "field": "players_min",
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
      "field": "players_min",
      "term": "กี่คน",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "room_seats": {
    "evidence_refs": [
      {
        "locator": "/values/room_seats",
        "source_id": "fixture20_demo20_zone_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 12
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00852

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_01`

### ผู้ใช้ถามอะไร

```text
Demo sessionn Northstar How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Northstar**
• name: Demo session Northstar [S1]
• resource ids: Demo station Northstar [S2]
• platform: Nintendo Switch [S3]
• session minutes: 60 [S4]
• occupancy minutes: 60 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_01 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_01"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_01",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_01"
        }
      ]
    },
    {
      "record_id": "demo20_service_01",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_01"
        }
      ]
    },
    {
      "record_id": "demo20_service_01",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_01"
        }
      ]
    },
    {
      "record_id": "demo20_service_01",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_01"
        }
      ]
    },
    {
      "record_id": "demo20_service_01",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_01"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00876

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_03`

### ผู้ใช้ถามอะไร

```text
Demo sessioon Drizzle How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Drizzle**
• name: Demo session Drizzle [S1]
• resource ids: Demo station Drizzle [S2]
• platform: VR [S3]
• session minutes: 30 [S4]
• occupancy minutes: 60 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_03 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_03",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_03"
        }
      ]
    },
    {
      "record_id": "demo20_service_03",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_03"
        }
      ]
    },
    {
      "record_id": "demo20_service_03",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_03"
        }
      ]
    },
    {
      "record_id": "demo20_service_03",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_03"
        }
      ]
    },
    {
      "record_id": "demo20_service_03",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_03"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 30
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00888

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_04`

### ผู้ใช้ถามอะไร

```text
Demo sesssion Mist How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Mist**
• name: Demo session Mist [S1]
• resource ids: Demo station Mist [S2]
• platform: Cockpit [S3]
• session minutes: 45 [S4]
• occupancy minutes: 60 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 45
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_04 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_04"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_04",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_04"
        }
      ]
    },
    {
      "record_id": "demo20_service_04",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_04"
        }
      ]
    },
    {
      "record_id": "demo20_service_04",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_04"
        }
      ]
    },
    {
      "record_id": "demo20_service_04",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_04"
        }
      ]
    },
    {
      "record_id": "demo20_service_04",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_04"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 45
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00894

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_05`

### ผู้ใช้ถามอะไร

```text
รอบทดลอง บบัวสีคราม หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง บัวสีคราม**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง บัวสีคราม [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง บัวสีคราม [S2]
• แพลตฟอร์มของบริการ: PC [S3]
• ระยะเวลาเล่นของบริการ: 60 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 60 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_05 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_05"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_05",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_05"
        }
      ]
    },
    {
      "record_id": "demo20_service_05",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_05"
        }
      ]
    },
    {
      "record_id": "demo20_service_05",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_05"
        }
      ]
    },
    {
      "record_id": "demo20_service_05",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_05"
        }
      ]
    },
    {
      "record_id": "demo20_service_05",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_05"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00912

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_06`

### ผู้ใช้ถามอะไร

```text
Demo sessiion Coral How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Coral**
• name: Demo session Coral [S1]
• resource ids: Demo station Coral [S2]
• platform: Nintendo Switch [S3]
• session minutes: 120 [S4]
• occupancy minutes: 120 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 120
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_06 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_06"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_06",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_06"
        }
      ]
    },
    {
      "record_id": "demo20_service_06",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_06"
        }
      ]
    },
    {
      "record_id": "demo20_service_06",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_06"
        }
      ]
    },
    {
      "record_id": "demo20_service_06",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_06"
        }
      ]
    },
    {
      "record_id": "demo20_service_06",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_06"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 120
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00918

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_07`

### ผู้ใช้ถามอะไร

```text
รอบทดลอง ตตะวันอ่อน หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง ตะวันอ่อน**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง ตะวันอ่อน [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง ตะวันอ่อน [S2]
• แพลตฟอร์มของบริการ: PC [S3]
• ระยะเวลาเล่นของบริการ: 120 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 120 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 120
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_07 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_07"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_07",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_07"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 120
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00924

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_07`

### ผู้ใช้ถามอะไร

```text
Demo sessionn Gentle Sun How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Gentle Sun**
• name: Demo session Gentle Sun [S1]
• resource ids: Demo station Gentle Sun [S2]
• platform: PC [S3]
• session minutes: 120 [S4]
• occupancy minutes: 120 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 120
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_07 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_07"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_07",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_07"
        }
      ]
    },
    {
      "record_id": "demo20_service_07",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_07"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 120
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00930

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_08`

### ผู้ใช้ถามอะไร

```text
รอบทดลอง ฟฟ้าหลังฝน หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง ฟ้าหลังฝน**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง ฟ้าหลังฝน [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง ฟ้าหลังฝน [S2]
• แพลตฟอร์มของบริการ: PS5 [S3]
• ระยะเวลาเล่นของบริการ: 30 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 30 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_08 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_08"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_08",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_08"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 30
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00936

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_08`

### ผู้ใช้ถามอะไร

```text
Demo sessionn After Rain How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session After Rain**
• name: Demo session After Rain [S1]
• resource ids: Demo station After Rain [S2]
• platform: PS5 [S3]
• session minutes: 30 [S4]
• occupancy minutes: 30 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_08 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_08"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_08",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_08"
        }
      ]
    },
    {
      "record_id": "demo20_service_08",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_08"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 30
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00942

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_09`

### ผู้ใช้ถามอะไร

```text
รอบทดลองง ลมทะเล หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง ลมทะเล**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง ลมทะเล [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง ลมทะเล [S2]
• แพลตฟอร์มของบริการ: PC [S3]
• ระยะเวลาเล่นของบริการ: 180 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 180 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 180
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_09 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_09"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_09",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_09"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 180
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00948

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_09`

### ผู้ใช้ถามอะไร

```text
Demo sessionn Sea Breeze How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Sea Breeze**
• name: Demo session Sea Breeze [S1]
• resource ids: Demo station Sea Breeze [S2]
• platform: PC [S3]
• session minutes: 180 [S4]
• occupancy minutes: 180 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 180
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_09 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_09"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_09",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_09"
        }
      ]
    },
    {
      "record_id": "demo20_service_09",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_09"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 180
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00954

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_10`

### ผู้ใช้ถามอะไร

```text
รอบทดลอง ห้้องสมุดดาว หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง ห้องสมุดดาว**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง ห้องสมุดดาว [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง ห้องสมุดดาว [S2]
• แพลตฟอร์มของบริการ: PS5 [S3]
• ระยะเวลาเล่นของบริการ: 60 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 60 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_10 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_10"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_10",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_10"
        }
      ]
    },
    {
      "record_id": "demo20_service_10",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_10"
        }
      ]
    },
    {
      "record_id": "demo20_service_10",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_10"
        }
      ]
    },
    {
      "record_id": "demo20_service_10",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_10"
        }
      ]
    },
    {
      "record_id": "demo20_service_10",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_10"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00966

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_11`

### ผู้ใช้ถามอะไร

```text
รอบทดลอง ตต้นเฟิร์น หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง ต้นเฟิร์น**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง ต้นเฟิร์น [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง ต้นเฟิร์น [S2]
• แพลตฟอร์มของบริการ: PC [S3]
• ระยะเวลาเล่นของบริการ: 90 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 90 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 90
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_11 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_11"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_11",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_11"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 90
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00972

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_11`

### ผู้ใช้ถามอะไร

```text
Demo sesssion Fern How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Fern**
• name: Demo session Fern [S1]
• resource ids: Demo station Fern [S2]
• platform: PC [S3]
• session minutes: 90 [S4]
• occupancy minutes: 90 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 90
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_11 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_11"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_11",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_11"
        }
      ]
    },
    {
      "record_id": "demo20_service_11",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_11"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 90
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00984

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_12`

### ผู้ใช้ถามอะไร

```text
Demo sessionn Sand Gold How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Sand Gold**
• name: Demo session Sand Gold [S1]
• resource ids: Demo station Sand Gold [S2]
• platform: VR [S3]
• session minutes: 20 [S4]
• occupancy minutes: 60 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 20
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_12 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_12"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_12",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_12"
        }
      ]
    },
    {
      "record_id": "demo20_service_12",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_12"
        }
      ]
    },
    {
      "record_id": "demo20_service_12",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_12"
        }
      ]
    },
    {
      "record_id": "demo20_service_12",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_12"
        }
      ]
    },
    {
      "record_id": "demo20_service_12",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_12"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 20
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00990

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_13`

### ผู้ใช้ถามอะไร

```text
รอบทดลอง จัันทร์เสี้ยว หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง จันทร์เสี้ยว**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง จันทร์เสี้ยว [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง จันทร์เสี้ยว [S2]
• แพลตฟอร์มของบริการ: Cockpit [S3]
• ระยะเวลาเล่นของบริการ: 60 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 60 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_13 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_13"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_13",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_13"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00996

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_13`

### ผู้ใช้ถามอะไร

```text
Demo sessioon Crescent How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Crescent**
• name: Demo session Crescent [S1]
• resource ids: Demo station Crescent [S2]
• platform: Cockpit [S3]
• session minutes: 60 [S4]
• occupancy minutes: 60 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_13 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_13"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_13",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_13"
        }
      ]
    },
    {
      "record_id": "demo20_service_13",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_13"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01008

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_14`

### ผู้ใช้ถามอะไร

```text
Demo sessionn Dawn Light How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Dawn Light**
• name: Demo session Dawn Light [S1]
• resource ids: Demo station Dawn Light [S2]
• platform: Nintendo Switch [S3]
• session minutes: 45 [S4]
• occupancy minutes: 60 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 45
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_14 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_14"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_14",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_14"
        }
      ]
    },
    {
      "record_id": "demo20_service_14",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_14"
        }
      ]
    },
    {
      "record_id": "demo20_service_14",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_14"
        }
      ]
    },
    {
      "record_id": "demo20_service_14",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_14"
        }
      ]
    },
    {
      "record_id": "demo20_service_14",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_14"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 45
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01020

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_15`

### ผู้ใช้ถามอะไร

```text
Demo sessiion Bamboo How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Bamboo**
• name: Demo session Bamboo [S1]
• resource ids: Demo station Bamboo [S2]
• platform: PC [S3]
• session minutes: 75 [S4]
• occupancy minutes: 75 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 75
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_15 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_15"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_15",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_15"
        }
      ]
    },
    {
      "record_id": "demo20_service_15",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_15"
        }
      ]
    },
    {
      "record_id": "demo20_service_15",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_15"
        }
      ]
    },
    {
      "record_id": "demo20_service_15",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_15"
        }
      ]
    },
    {
      "record_id": "demo20_service_15",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_15"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 75
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01026

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_16`

### ผู้ใช้ถามอะไร

```text
รอบทดลองง เมฆขาว หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง เมฆขาว**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง เมฆขาว [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง เมฆขาว [S2]
• แพลตฟอร์มของบริการ: PC [S3]
• ระยะเวลาเล่นของบริการ: 60 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 60 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_16 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_16"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_16",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_16"
        }
      ]
    },
    {
      "record_id": "demo20_service_16",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_16"
        }
      ]
    },
    {
      "record_id": "demo20_service_16",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_16"
        }
      ]
    },
    {
      "record_id": "demo20_service_16",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_16"
        }
      ]
    },
    {
      "record_id": "demo20_service_16",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_16"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01038

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_17`

### ผู้ใช้ถามอะไร

```text
รอบทดลออง มะลิ หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง มะลิ**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง มะลิ [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง มะลิ [S2]
• แพลตฟอร์มของบริการ: PS5 [S3]
• ระยะเวลาเล่นของบริการ: 120 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 120 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 120
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_17 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_17"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_17",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_17"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 120
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01044

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_17`

### ผู้ใช้ถามอะไร

```text
Demo sessioon Jasmine How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Jasmine**
• name: Demo session Jasmine [S1]
• resource ids: Demo station Jasmine [S2]
• platform: PS5 [S3]
• session minutes: 120 [S4]
• occupancy minutes: 120 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 120
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_17 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_17"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_17",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_17"
        }
      ]
    },
    {
      "record_id": "demo20_service_17",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_17"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 120
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01050

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_18`

### ผู้ใช้ถามอะไร

```text
รอบทดลองง กระเบน หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง กระเบน**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง กระเบน [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง กระเบน [S2]
• แพลตฟอร์มของบริการ: PC [S3]
• ระยะเวลาเล่นของบริการ: 60 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 60 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_18 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_18"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_18",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_18"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01056

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_18`

### ผู้ใช้ถามอะไร

```text
Demo sesssion Ray How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Ray**
• name: Demo session Ray [S1]
• resource ids: Demo station Ray [S2]
• platform: PC [S3]
• session minutes: 60 [S4]
• occupancy minutes: 60 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 60
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_18 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_18"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_18",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_18"
        }
      ]
    },
    {
      "record_id": "demo20_service_18",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_18"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 60
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01068

**หมวด:** service • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_19`

### ผู้ใช้ถามอะไร

```text
Demo sessiion Ginkgo How many minutes does one session last?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**Demo session Ginkgo**
• name: Demo session Ginkgo [S1]
• resource ids: Demo station Ginkgo [S2]
• platform: Nintendo Switch [S3]
• session minutes: 180 [S4]
• occupancy minutes: 180 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 180
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_19 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_19"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_19",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_19"
        }
      ]
    },
    {
      "record_id": "demo20_service_19",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_19"
        }
      ]
    },
    {
      "record_id": "demo20_service_19",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_19"
        }
      ]
    },
    {
      "record_id": "demo20_service_19",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_19"
        }
      ]
    },
    {
      "record_id": "demo20_service_19",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_19"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 180
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01074

**หมวด:** service • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_service_20`

### ผู้ใช้ถามอะไร

```text
รอบทดลอง รรุ่งเรือง หนึ่งรอบเล่นได้กี่นาที
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: เวลาเล่นต่อรอบ (นาที) (`session_minutes`)

### คำตอบที่ระบบส่งจริง

```text
**รอบทดลอง รุ่งเรือง**
• ชื่อบริการตามหน้า WordPress: รอบทดลอง รุ่งเรือง [S1]
• เครื่องจริงที่บริการใช้: เครื่องทดลอง รุ่งเรือง [S2]
• แพลตฟอร์มของบริการ: PC [S3]
• ระยะเวลาเล่นของบริการ: 240 [S4]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 240 [S5]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 240
```

### ทำไมได้คำตอบแบบนี้

หา demo20_service_20 ถูกแล้ว แต่ requested_fields=[]; bounded_fuzzy ข้ามถามกลับแล้วตอบ default core fields จึงผ่านการมีค่าโดยที่ไม่ resolve intent

- **R09 — พิมพ์ซ้ำแล้วข้าม clarification โดยที่ field ยังว่าง**: method=bounded_fuzzy ถูกยกเว้น remainder clarification แล้วใช้ publish_core/default fields จึงมีคำตอบที่ควรมีโดยบังเอิญและ content scorer ให้ผ่าน • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:171)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_20"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "bounded_fuzzy",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_service_20",
      "field": "name",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/name",
          "source_id": "fixture20_demo20_service_20"
        }
      ]
    },
    {
      "record_id": "demo20_service_20",
      "field": "resource_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/resource_ids",
          "source_id": "fixture20_demo20_service_20"
        }
      ]
    },
    {
      "record_id": "demo20_service_20",
      "field": "platform",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/platform",
          "source_id": "fixture20_demo20_service_20"
        }
      ]
    },
    {
      "record_id": "demo20_service_20",
      "field": "session_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/session_minutes",
          "source_id": "fixture20_demo20_service_20"
        }
      ]
    },
    {
      "record_id": "demo20_service_20",
      "field": "occupancy_minutes",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/occupancy_minutes",
          "source_id": "fixture20_demo20_service_20"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "session_minutes": {
    "evidence_refs": [
      {
        "locator": "/values/session_minutes",
        "source_id": "fixture20_demo20_service_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": 240
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03963

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ดาวเหนือ อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ดาวเหนือ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ดาวเหนือ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: eligibility_registration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ดาวเหนือ [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.1 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_01"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_01",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_01"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03965

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ดาวเหนือ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ดาวเหนือ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ดาวเหนือ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: eligibility_registration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ดาวเหนือ [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.1 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_01"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_01",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_01"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_01",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_01"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03973

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_02`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ดาวเหนือ พลัส อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ดาวเหนือ พลัส**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ดาวเหนือ พลัส [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: roster_composition [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ดาวเหนือ พลัส [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.2 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_02"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_02",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_02"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 2: for Player substitution, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03975

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_02`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ดาวเหนือ พลัส กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ดาวเหนือ พลัส**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ดาวเหนือ พลัส [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: roster_composition [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ดาวเหนือ พลัส [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.2 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_02"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_02",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_02"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_02",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_02"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 2: for Player substitution, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03983

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_03`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ละอองฝน อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ละอองฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ละอองฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ละอองฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.3 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_03",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_03"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03985

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_03`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ละอองฝน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ละอองฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ละอองฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ละอองฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.3 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_03",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_03"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03993

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_04`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง สายหมอก อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง สายหมอก**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก สายหมอก [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: match_configuration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง สายหมอก [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.4 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_04"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_04",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_04"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 4: for Seat adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03995

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_04`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง สายหมอก กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง สายหมอก**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก สายหมอก [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: match_configuration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง สายหมอก [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.4 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_04"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_04",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_04"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_04",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_04"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 4: for Seat adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04003

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_05`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง บัวสีคราม อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง บัวสีคราม**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก บัวสีคราม [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: pre_match_on_site [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง บัวสีคราม [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.5 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_05"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_05",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_05"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 5: for Free learning activity, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04005

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_05`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง บัวสีคราม กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง บัวสีคราม**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก บัวสีคราม [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: pre_match_on_site [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง บัวสีคราม [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.5 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_05"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_05",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_05"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_05",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_05"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 5: for Free learning activity, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04013

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_06`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ปะการัง อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ปะการัง**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ปะการัง [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: in_match_operations [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ปะการัง [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.6 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_06"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_06",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_06"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 6: for Food in the zone, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04015

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_06`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ปะการัง กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ปะการัง**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ปะการัง [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: in_match_operations [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ปะการัง [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.6 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_06"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_06",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_06"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_06",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_06"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 6: for Food in the zone, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04023

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_07`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ตะวันอ่อน อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ตะวันอ่อน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ตะวันอ่อน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: fair_play_conduct [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ตะวันอ่อน [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.7 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_07"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_07",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_07"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 7: for Team roster, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04025

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_07`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ตะวันอ่อน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ตะวันอ่อน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ตะวันอ่อน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: fair_play_conduct [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ตะวันอ่อน [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.7 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_07"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_07",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_07"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_07",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_07"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 7: for Team roster, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04033

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_08`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ฟ้าหลังฝน อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ฟ้าหลังฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ฟ้าหลังฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: penalty_matrix [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ฟ้าหลังฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.8 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_08"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_08",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_08"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 8: for Player accounts, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04035

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_08`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ฟ้าหลังฝน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ฟ้าหลังฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ฟ้าหลังฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: penalty_matrix [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ฟ้าหลังฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.8 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_08"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_08",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_08"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_08",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_08"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 8: for Player accounts, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04043

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_09`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ลมทะเล อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ลมทะเล**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ลมทะเล [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: protest_dispute [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ลมทะเล [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.9 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_09"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_09",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_09"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 9: for Group reservations, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04045

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_09`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ลมทะเล กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ลมทะเล**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ลมทะเล [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: protest_dispute [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ลมทะเล [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.9 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_09"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_09",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_09"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_09",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_09"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 9: for Group reservations, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04053

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_10`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ห้องสมุดดาว อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ห้องสมุดดาว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ห้องสมุดดาว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: identity [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ห้องสมุดดาว [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.10 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_10"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_10",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_10"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 10: for Volume adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04055

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_10`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ห้องสมุดดาว กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ห้องสมุดดาว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ห้องสมุดดาว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: identity [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ห้องสมุดดาว [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.10 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_10"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_10",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_10"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_10",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_10"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 10: for Volume adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04063

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_11`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ต้นเฟิร์น อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ต้นเฟิร์น**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ต้นเฟิร์น [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: eligibility_registration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ต้นเฟิร์น [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.11 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_11"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_11",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_11"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 11: for Personal devices, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04065

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_11`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ต้นเฟิร์น กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ต้นเฟิร์น**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ต้นเฟิร์น [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: eligibility_registration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ต้นเฟิร์น [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.11 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_11"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_11",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_11"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_11",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_11"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 11: for Personal devices, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04073

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_12`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ทองทราย อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ทองทราย**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ทองทราย [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: roster_composition [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ทองทราย [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.12 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_12"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_12",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_12"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 12: for Safety boundary, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04075

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_12`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ทองทราย กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง ทองทราย**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ทองทราย [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: roster_composition [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ทองทราย [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.12 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_12"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_12",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_12"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_12",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_12"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 12: for Safety boundary, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04083

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_13`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง จันทร์เสี้ยว อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง จันทร์เสี้ยว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก จันทร์เสี้ยว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง จันทร์เสี้ยว [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.13 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_13"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_13",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_13"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 13: for Practice before starting, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04085

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_13`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง จันทร์เสี้ยว กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง จันทร์เสี้ยว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก จันทร์เสี้ยว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง จันทร์เสี้ยว [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.13 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_13"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_13",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_13"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_13",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_13"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 13: for Practice before starting, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04093

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_14`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง แสงอรุณ อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง แสงอรุณ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก แสงอรุณ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: match_configuration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง แสงอรุณ [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.14 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_14"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_14",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_14"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 14: for Photography, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04095

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_14`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง แสงอรุณ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง แสงอรุณ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก แสงอรุณ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: match_configuration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง แสงอรุณ [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.14 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_14"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_14",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_14"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_14",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_14"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 14: for Photography, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04103

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_15`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง กิ่งไผ่ อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง กิ่งไผ่**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก กิ่งไผ่ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: pre_match_on_site [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง กิ่งไผ่ [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.15 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_15"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_15",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_15"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 15: for Software installation, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04105

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_15`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง กิ่งไผ่ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง กิ่งไผ่**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก กิ่งไผ่ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: pre_match_on_site [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง กิ่งไผ่ [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.15 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_15"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_15",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_15"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_15",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_15"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 15: for Software installation, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04113

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_16`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง เมฆขาว อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง เมฆขาว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก เมฆขาว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: in_match_operations [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง เมฆขาว [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.16 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_16"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_16",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_16"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 16: for Accessibility assistance, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04115

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_16`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง เมฆขาว กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง เมฆขาว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก เมฆขาว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: in_match_operations [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง เมฆขาว [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.16 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_16"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_16",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_16"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_16",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_16"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 16: for Accessibility assistance, follow decision allowed; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04123

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_17`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง มะลิ อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง มะลิ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก มะลิ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: fair_play_conduct [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง มะลิ [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.17 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_17"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_17",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_17"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 17: for Changing dates, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04125

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_17`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง มะลิ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง มะลิ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก มะลิ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: fair_play_conduct [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง มะลิ [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.17 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_17"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_17",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_17"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_17",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_17"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 17: for Changing dates, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04133

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_18`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง กระเบน อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง กระเบน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก กระเบน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: penalty_matrix [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง กระเบน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.18 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_18"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_18",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_18"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 18: for Refund requests, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04135

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_18`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง กระเบน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง กระเบน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก กระเบน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: penalty_matrix [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง กระเบน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.18 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_18"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_18",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_18"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_18",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_18"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 18: for Refund requests, follow decision prohibited; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04143

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_19`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง แปะก๊วย อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง แปะก๊วย**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก แปะก๊วย [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: protest_dispute [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง แปะก๊วย [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.19 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_19"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_19",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_19"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 19: for Check-in proof, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04145

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_19`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง แปะก๊วย กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง แปะก๊วย**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก แปะก๊วย [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: protest_dispute [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง แปะก๊วย [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.19 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_19"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_19",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_19"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_19",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_19"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 19: for Check-in proof, follow decision required; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04153

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_rule_20`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง รุ่งเรือง อยากอ่านข้อความกติกาข้อนี้ให้ครบ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง รุ่งเรือง**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก รุ่งเรือง [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: identity [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง รุ่งเรือง [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.20 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_20"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_20",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_20"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 20: for Result appeals, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04155

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_20`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง รุ่งเรือง กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
**ข้อการแข่งขันทดลอง รุ่งเรือง**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก รุ่งเรือง [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: identity [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง รุ่งเรือง [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.20 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

broad=True ทำให้ตอบหลาย/ทุก field จน gold field อยู่ในผล แม้คำถามไม่ได้ขอทุก field ชัดเจน ต้องแยก completeness intent กับ all intent

- **R13 — คำว่าครบ/ส่วนท้าย all ทำให้ขยายเป็นขอทั้งหมด**: all_query ตรวจครบแบบ substring และ all\b ไม่กันขอบต้น; ครบไหม/ไม่ต้องทั้งหมด/football/small/install จึงเข้ากลุ่ม broad แม้เจตนาต่าง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:34)
- **R17 — คะแนนผ่านตรวจการมีข้อมูล แต่ไม่ได้พิสูจน์ความเข้าใจครบ**: score ตรวจ obligations/content/evidence/known-state ไม่ตรวจทุกเรื่องที่ตอบเกิน ภาษาที่เป็นธรรมชาติ หรือ mapping ของทุก gold field ไป requested_fields; domain bundles อาจผ่านได้อย่างเหมาะสมหรือบังเอิญ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:216)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_20"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_20",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_20"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_20",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_20"
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

ผ่านเกณฑ์เนื้อหาที่ต้องมี แต่มีข้อสังเกต semantic เพิ่ม; ไม่ใช่สรุปว่าคำตอบถูกทุกมิติ

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture20_demo20_competition_rule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Fictional clause 20: for Result appeals, follow decision conditional; exception requires written demo operator approval; not actual rules",
      "th": "ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
    }
  },
  "completeness": {
    "evidence_refs": [
      {
        "locator": "/values/completeness",
        "source_id": "fixture20_demo20_competition_rule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "complete"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

