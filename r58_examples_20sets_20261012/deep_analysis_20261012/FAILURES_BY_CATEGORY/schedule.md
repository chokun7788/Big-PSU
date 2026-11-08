# ภาคผนวกเคสไม่ผ่าน — schedule / 121 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 03362](#case-03362), [Case 03363](#case-03363), [Case 03364](#case-03364), [Case 03365](#case-03365), [Case 03368](#case-03368), [Case 03370](#case-03370), [Case 03372](#case-03372), [Case 03373](#case-03373), [Case 03374](#case-03374), [Case 03375](#case-03375), [Case 03378](#case-03378), [Case 03380](#case-03380), [Case 03382](#case-03382), [Case 03383](#case-03383), [Case 03384](#case-03384), [Case 03385](#case-03385), [Case 03388](#case-03388), [Case 03390](#case-03390), [Case 03392](#case-03392), [Case 03393](#case-03393), [Case 03394](#case-03394), [Case 03395](#case-03395), [Case 03398](#case-03398), [Case 03400](#case-03400), [Case 03402](#case-03402), [Case 03403](#case-03403), [Case 03404](#case-03404), [Case 03405](#case-03405), [Case 03408](#case-03408), [Case 03410](#case-03410), [Case 03412](#case-03412), [Case 03413](#case-03413), [Case 03414](#case-03414), [Case 03415](#case-03415), [Case 03418](#case-03418), [Case 03420](#case-03420), [Case 03422](#case-03422), [Case 03423](#case-03423), [Case 03424](#case-03424), [Case 03425](#case-03425), [Case 03428](#case-03428), [Case 03430](#case-03430), [Case 03432](#case-03432), [Case 03433](#case-03433), [Case 03434](#case-03434), [Case 03435](#case-03435), [Case 03438](#case-03438), [Case 03440](#case-03440), [Case 03442](#case-03442), [Case 03443](#case-03443), [Case 03444](#case-03444), [Case 03445](#case-03445), [Case 03448](#case-03448), [Case 03450](#case-03450), [Case 03452](#case-03452), [Case 03453](#case-03453), [Case 03454](#case-03454), [Case 03455](#case-03455), [Case 03458](#case-03458), [Case 03460](#case-03460), [Case 03462](#case-03462), [Case 03463](#case-03463), [Case 03464](#case-03464), [Case 03465](#case-03465), [Case 03468](#case-03468), [Case 03470](#case-03470), [Case 03472](#case-03472), [Case 03473](#case-03473), [Case 03474](#case-03474), [Case 03475](#case-03475), [Case 03478](#case-03478), [Case 03480](#case-03480), [Case 03482](#case-03482), [Case 03483](#case-03483), [Case 03484](#case-03484), [Case 03485](#case-03485), [Case 03488](#case-03488), [Case 03490](#case-03490), [Case 03492](#case-03492), [Case 03493](#case-03493), [Case 03494](#case-03494), [Case 03495](#case-03495), [Case 03498](#case-03498), [Case 03500](#case-03500), [Case 03502](#case-03502), [Case 03503](#case-03503), [Case 03504](#case-03504), [Case 03505](#case-03505), [Case 03508](#case-03508), [Case 03510](#case-03510), [Case 03512](#case-03512), [Case 03513](#case-03513), [Case 03514](#case-03514), [Case 03515](#case-03515), [Case 03518](#case-03518), [Case 03520](#case-03520), [Case 03522](#case-03522), [Case 03523](#case-03523), [Case 03524](#case-03524), [Case 03525](#case-03525), [Case 03528](#case-03528), [Case 03530](#case-03530), [Case 03532](#case-03532), [Case 03533](#case-03533), [Case 03534](#case-03534), [Case 03535](#case-03535), [Case 03538](#case-03538), [Case 03540](#case-03540), [Case 03542](#case-03542), [Case 03543](#case-03543), [Case 03544](#case-03544), [Case 03545](#case-03545), [Case 03548](#case-03548), [Case 03550](#case-03550), [Case 03552](#case-03552), [Case 03553](#case-03553), [Case 03554](#case-03554), [Case 03555](#case-03555), [Case 03558](#case-03558), [Case 03560](#case-03560), [Case 05046](#case-05046)

## Case 03362

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_01`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ดาวเหนือ จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_01"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03363

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_01`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ดาวเหนือ มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_01"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03364

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_01`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ดาวเหนือ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_01"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03365

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_01`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ดาวเหนือ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_01"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03368

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_01`

### ผู้ใช้ถามอะไร

```text
Demo timetable Northstar Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_01"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03370

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_01`

### ผู้ใช้ถามอะไร

```text
Demo timetable Northstar What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_01**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_01'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_01"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_01",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_01"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03372

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_02`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ดาวเหนือ พลัส จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_02"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03373

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_02`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ดาวเหนือ พลัส มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_02"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03374

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_02`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ดาวเหนือ พลัส ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_02"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03375

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_02`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ดาวเหนือ พลัส เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_02"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03378

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_02`

### ผู้ใช้ถามอะไร

```text
Demo timetable Northstar Plus Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_02"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03380

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_02`

### ผู้ใช้ถามอะไร

```text
Demo timetable Northstar Plus What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_02**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_02'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_02"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_02",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_02"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03382

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_03`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ละอองฝน จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03383

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_03`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ละอองฝน มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03384

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_03`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ละอองฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03385

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_03`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ละอองฝน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03388

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_03`

### ผู้ใช้ถามอะไร

```text
Demo timetable Drizzle Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03390

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_03`

### ผู้ใช้ถามอะไร

```text
Demo timetable Drizzle What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_03**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_03'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_03"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_03",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_03"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03392

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_04`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง สายหมอก จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_04"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03393

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_04`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง สายหมอก มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_04"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03394

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_04`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง สายหมอก ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_04"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03395

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_04`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง สายหมอก เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_04"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03398

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_04`

### ผู้ใช้ถามอะไร

```text
Demo timetable Mist Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_04"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03400

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_04`

### ผู้ใช้ถามอะไร

```text
Demo timetable Mist What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_04**
• maintenance periods: None (confirmed) [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): None (confirmed)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_04'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_04"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_04",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_04"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03402

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_05`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง บัวสีคราม จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_05"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03403

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_05`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง บัวสีคราม มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_05"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03404

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_05`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง บัวสีคราม ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_05"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03405

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_05`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง บัวสีคราม เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_05"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03408

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_05`

### ผู้ใช้ถามอะไร

```text
Demo timetable Indigo Lotus Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_05"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03410

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_05`

### ผู้ใช้ถามอะไร

```text
Demo timetable Indigo Lotus What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_05**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_05'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_05"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_05",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_05"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03412

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_06`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ปะการัง จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_06"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03413

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_06`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ปะการัง มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_06"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03414

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_06`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ปะการัง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_06"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03415

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_06`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ปะการัง เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_06"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03418

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_06`

### ผู้ใช้ถามอะไร

```text
Demo timetable Coral Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_06"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03420

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_06`

### ผู้ใช้ถามอะไร

```text
Demo timetable Coral What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_06**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_06'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_06"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_06",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_06"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03422

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_07`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ตะวันอ่อน จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_07"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03423

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_07`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ตะวันอ่อน มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_07"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03424

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_07`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ตะวันอ่อน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_07"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03425

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_07`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ตะวันอ่อน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_07"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03428

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_07`

### ผู้ใช้ถามอะไร

```text
Demo timetable Gentle Sun Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_07"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03430

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_07`

### ผู้ใช้ถามอะไร

```text
Demo timetable Gentle Sun What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_07**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_07'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_07"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_07",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_07"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03432

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_08`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ฟ้าหลังฝน จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_08"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03433

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_08`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ฟ้าหลังฝน มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_08"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03434

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_08`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ฟ้าหลังฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_08"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03435

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_08`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ฟ้าหลังฝน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_08"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03438

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_08`

### ผู้ใช้ถามอะไร

```text
Demo timetable After Rain Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_08"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03440

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_08`

### ผู้ใช้ถามอะไร

```text
Demo timetable After Rain What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_08**
• maintenance periods: None (confirmed) [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): None (confirmed)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_08'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_08"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_08",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_08"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03442

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_09`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ลมทะเล จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_09"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03443

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_09`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ลมทะเล มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_09"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03444

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_09`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ลมทะเล ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_09"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03445

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_09`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ลมทะเล เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_09"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03448

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_09`

### ผู้ใช้ถามอะไร

```text
Demo timetable Sea Breeze Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_09"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03450

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_09`

### ผู้ใช้ถามอะไร

```text
Demo timetable Sea Breeze What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_09**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_09'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_09"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_09",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_09"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03452

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_10`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ห้องสมุดดาว จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_10"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03453

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_10`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ห้องสมุดดาว มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_10"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03454

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_10`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ห้องสมุดดาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_10"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03455

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_10`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ห้องสมุดดาว เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_10"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03458

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_10`

### ผู้ใช้ถามอะไร

```text
Demo timetable Star Library Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_10"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03460

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_10`

### ผู้ใช้ถามอะไร

```text
Demo timetable Star Library What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_10**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_10'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_10"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_10",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_10"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03462

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_11`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ต้นเฟิร์น จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_11"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03463

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_11`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ต้นเฟิร์น มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_11"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03464

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_11`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ต้นเฟิร์น ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_11"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03465

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_11`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ต้นเฟิร์น เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_11"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03468

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_11`

### ผู้ใช้ถามอะไร

```text
Demo timetable Fern Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_11"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03470

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_11`

### ผู้ใช้ถามอะไร

```text
Demo timetable Fern What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_11**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_11'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_11"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_11",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_11"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03472

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_12`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ทองทราย จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_12"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03473

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_12`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ทองทราย มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_12"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03474

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_12`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง ทองทราย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_12"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03475

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_12`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง ทองทราย เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_12"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03478

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_12`

### ผู้ใช้ถามอะไร

```text
Demo timetable Sand Gold Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_12"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03480

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_12`

### ผู้ใช้ถามอะไร

```text
Demo timetable Sand Gold What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_12**
• maintenance periods: None (confirmed) [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): None (confirmed)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_12'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_12"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_12",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_12"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03482

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_13`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง จันทร์เสี้ยว จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_13"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03483

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_13`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง จันทร์เสี้ยว มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_13"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03484

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_13`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง จันทร์เสี้ยว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_13"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03485

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_13`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง จันทร์เสี้ยว เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_13"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03488

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_13`

### ผู้ใช้ถามอะไร

```text
Demo timetable Crescent Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_13"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03490

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_13`

### ผู้ใช้ถามอะไร

```text
Demo timetable Crescent What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_13**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_13'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_13"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_13",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_13"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03492

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_14`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง แสงอรุณ จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_14"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03493

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_14`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง แสงอรุณ มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_14"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03494

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_14`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง แสงอรุณ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_14"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03495

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_14`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง แสงอรุณ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_14"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03498

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_14`

### ผู้ใช้ถามอะไร

```text
Demo timetable Dawn Light Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_14"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03500

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_14`

### ผู้ใช้ถามอะไร

```text
Demo timetable Dawn Light What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_14**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_14'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_14"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_14",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_14"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03502

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_15`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง กิ่งไผ่ จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_15"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03503

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_15`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง กิ่งไผ่ มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_15"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03504

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_15`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง กิ่งไผ่ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_15"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03505

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_15`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง กิ่งไผ่ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_15"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03508

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_15`

### ผู้ใช้ถามอะไร

```text
Demo timetable Bamboo Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_15"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03510

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_15`

### ผู้ใช้ถามอะไร

```text
Demo timetable Bamboo What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_15**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_15'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_15"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_15",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_15"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03512

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_16`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง เมฆขาว จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_16"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03513

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_16`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง เมฆขาว มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_16"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03514

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_16`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง เมฆขาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_16"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03515

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_16`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง เมฆขาว เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_16"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03518

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_16`

### ผู้ใช้ถามอะไร

```text
Demo timetable White Cloud Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_16"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03520

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_16`

### ผู้ใช้ถามอะไร

```text
Demo timetable White Cloud What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_16**
• maintenance periods: None (confirmed) [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): None (confirmed)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_16'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_16"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_16",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_16"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03522

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_17`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง มะลิ จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_17"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03523

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_17`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง มะลิ มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_17"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03524

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_17`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง มะลิ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_17"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03525

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_17`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง มะลิ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_17"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03528

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_17`

### ผู้ใช้ถามอะไร

```text
Demo timetable Jasmine Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_17"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03530

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_17`

### ผู้ใช้ถามอะไร

```text
Demo timetable Jasmine What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_17**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 18:00; start: 09:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_17'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_17"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_17",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_17"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "18:00",
        "start": "09:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03532

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_18`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง กระเบน จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_18"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03533

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_18`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง กระเบน มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_18"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03534

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_18`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง กระเบน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_18"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03535

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_18`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง กระเบน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_18"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03538

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_18`

### ผู้ใช้ถามอะไร

```text
Demo timetable Ray Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 10:00
• end: 19:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_18"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "10:00"
      },
      {
        "end": "19:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03540

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_18`

### ผู้ใช้ถามอะไร

```text
Demo timetable Ray What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_18**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 19:00; start: 10:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_18'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_18"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_18",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_18"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "19:00",
        "start": "10:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03542

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_19`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง แปะก๊วย จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_19"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03543

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_19`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง แปะก๊วย มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_19"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03544

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_19`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง แปะก๊วย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_19"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03545

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_19`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง แปะก๊วย เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_19"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03548

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_19`

### ผู้ใช้ถามอะไร

```text
Demo timetable Ginkgo Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 11:00
• end: 20:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_19"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "11:00"
      },
      {
        "end": "20:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03550

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_19`

### ผู้ใช้ถามอะไร

```text
Demo timetable Ginkgo What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_19**
• maintenance periods: • end: 13:00; start: 12:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 20:00; start: 11:00
ช่วงบำรุงรักษา (maintenance_periods): • end: 13:00; start: 12:00
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_19'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_19"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_19",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_19"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "20:00",
        "start": "11:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "13:00",
        "start": "12:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03552

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_schedule_20`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง รุ่งเรือง จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_20"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03553

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_20`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง รุ่งเรือง มีช่วงเวลาไหนที่จองเล่นได้
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_20"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03554

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_schedule_20`

### ผู้ใช้ถามอะไร

```text
แล้วจองช่วงไหนได้บ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ตารางทดลอง รุ่งเรือง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_20"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03555

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_20`

### ผู้ใช้ถามอะไร

```text
ตารางทดลอง รุ่งเรือง เปิดช่วงไหนและพักบำรุงรักษาตอนไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): ไม่มี (ยืนยันแล้ว)
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_20"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:open_periods, missing_field:maintenance_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03558

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_schedule_20`

### ผู้ใช้ถามอะไร

```text
Demo timetable Radiance Which time periods can I book?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 17:00; start: 08:00
```

### ทำไมได้คำตอบแบบนี้

หา demo20_schedule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_20"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03560

**หมวด:** schedule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_schedule_20`

### ผู้ใช้ถามอะไร

```text
Demo timetable Radiance What are the opening and maintenance periods?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเปิด (`open_periods`), ช่วงบำรุงรักษา (`maintenance_periods`)

### คำตอบที่ระบบส่งจริง

```text
**demo20_schedule_20**
• maintenance periods: None (confirmed) [S1]

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเปิด (open_periods): • end: 17:00; start: 08:00
ช่วงบำรุงรักษา (maintenance_periods): None (confirmed)
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_schedule_20'] และหัวข้อ ['maintenance_periods']; field ของ target ที่ยังไม่มี obligation คือ ['open_periods']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_schedule_20"
    ],
    "requested_fields": [
      "maintenance_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_schedule_20",
      "field": "maintenance_periods",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/maintenance_periods",
          "source_id": "fixture20_demo20_schedule_20"
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
  "catalog_matches": [
    {
      "field": "maintenance_periods",
      "kind": "schedule",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:open_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "open_periods": {
    "evidence_refs": [
      {
        "locator": "/values/open_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "end": "17:00",
        "start": "08:00"
      }
    ]
  },
  "maintenance_periods": {
    "evidence_refs": [
      {
        "locator": "/values/maintenance_periods",
        "source_id": "fixture20_demo20_schedule_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": []
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 05046

**หมวด:** schedule • **ภาษา:** th • **รูปแบบ:** old_control_natural • **record ที่ควรตอบ:** `demo_schedule_01`

### ผู้ใช้ถามอะไร

```text
ตัวอย่าง ตารางบริการ 01 จองช่วงไหนได้บ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ช่วงเวลาที่จองได้ (`bookable_periods`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ช่วงเวลาที่จองได้ (bookable_periods): • end: 12:00; start: 09:00
• end: 18:00; start: 13:00
```

### ทำไมได้คำตอบแบบนี้

หา demo_schedule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo_schedule_01"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
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

response_clarification, missing_field:bookable_periods

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "bookable_periods": {
    "evidence_refs": [
      {
        "locator": "/values/bookable_periods",
        "source_id": "fixture_source_demo_schedule_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": [
      {
        "end": "12:00",
        "start": "09:00"
      },
      {
        "end": "18:00",
        "start": "13:00"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/records/schedule/demo_schedule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

