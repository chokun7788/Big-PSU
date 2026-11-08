# ภาคผนวกเคสไม่ผ่าน — equipment_model / 81 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 00402](#case-00402), [Case 00403](#case-00403), [Case 00404](#case-00404), [Case 00405](#case-00405), [Case 00412](#case-00412), [Case 00413](#case-00413), [Case 00414](#case-00414), [Case 00415](#case-00415), [Case 00422](#case-00422), [Case 00423](#case-00423), [Case 00424](#case-00424), [Case 00425](#case-00425), [Case 00432](#case-00432), [Case 00433](#case-00433), [Case 00434](#case-00434), [Case 00435](#case-00435), [Case 00442](#case-00442), [Case 00443](#case-00443), [Case 00444](#case-00444), [Case 00445](#case-00445), [Case 00452](#case-00452), [Case 00453](#case-00453), [Case 00454](#case-00454), [Case 00455](#case-00455), [Case 00462](#case-00462), [Case 00463](#case-00463), [Case 00464](#case-00464), [Case 00465](#case-00465), [Case 00472](#case-00472), [Case 00473](#case-00473), [Case 00474](#case-00474), [Case 00475](#case-00475), [Case 00482](#case-00482), [Case 00483](#case-00483), [Case 00484](#case-00484), [Case 00485](#case-00485), [Case 00492](#case-00492), [Case 00493](#case-00493), [Case 00494](#case-00494), [Case 00495](#case-00495), [Case 00502](#case-00502), [Case 00503](#case-00503), [Case 00504](#case-00504), [Case 00505](#case-00505), [Case 00512](#case-00512), [Case 00513](#case-00513), [Case 00514](#case-00514), [Case 00515](#case-00515), [Case 00522](#case-00522), [Case 00523](#case-00523), [Case 00524](#case-00524), [Case 00525](#case-00525), [Case 00532](#case-00532), [Case 00533](#case-00533), [Case 00534](#case-00534), [Case 00535](#case-00535), [Case 00542](#case-00542), [Case 00543](#case-00543), [Case 00544](#case-00544), [Case 00545](#case-00545), [Case 00552](#case-00552), [Case 00553](#case-00553), [Case 00554](#case-00554), [Case 00555](#case-00555), [Case 00562](#case-00562), [Case 00563](#case-00563), [Case 00564](#case-00564), [Case 00565](#case-00565), [Case 00572](#case-00572), [Case 00573](#case-00573), [Case 00574](#case-00574), [Case 00575](#case-00575), [Case 00582](#case-00582), [Case 00583](#case-00583), [Case 00584](#case-00584), [Case 00585](#case-00585), [Case 00592](#case-00592), [Case 00593](#case-00593), [Case 00594](#case-00594), [Case 00595](#case-00595), [Case 04990](#case-04990)

## Case 00402

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_01`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ดาวเหนือ สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_01"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00403

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_01`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ดาวเหนือ มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_01"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00404

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_01`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ดาวเหนือ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_01"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00405

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_01`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ดาวเหนือ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_01"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00412

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_02`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ดาวเหนือ พลัส สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_02"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00413

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_02`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ดาวเหนือ พลัส มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_02"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00414

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_02`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ดาวเหนือ พลัส ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_02"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00415

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_02`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ดาวเหนือ พลัส เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_02"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00422

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_03`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ละอองฝน สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_03"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00423

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_03`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ละอองฝน มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_03"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00424

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_03`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ละอองฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_03"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00425

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_03`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ละอองฝน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): vr
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_03"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "vr"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00432

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_04`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ สายหมอก สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_04"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00433

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_04`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ สายหมอก มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_04"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00434

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_04`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ สายหมอก ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_04"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00435

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_04`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ สายหมอก เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): wheel
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_04"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "wheel"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00442

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_05`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ บัวสีคราม สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_05"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00443

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_05`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ บัวสีคราม มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_05"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00444

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_05`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ บัวสีคราม ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_05"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00445

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_05`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ บัวสีคราม เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_05"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00452

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_06`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ปะการัง สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_06"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00453

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_06`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ปะการัง มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_06"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00454

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_06`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ปะการัง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_06"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00455

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_06`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ปะการัง เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_06"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00462

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_07`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ตะวันอ่อน สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_07"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00463

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_07`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ตะวันอ่อน มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_07"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00464

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_07`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ตะวันอ่อน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_07"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00465

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_07`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ตะวันอ่อน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_07"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00472

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_08`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ฟ้าหลังฝน สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_08"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00473

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_08`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ฟ้าหลังฝน มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_08"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00474

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_08`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ฟ้าหลังฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_08"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00475

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_08`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ฟ้าหลังฝน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_08"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00482

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_09`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ลมทะเล สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_09"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00483

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_09`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ลมทะเล มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_09"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00484

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_09`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ลมทะเล ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_09"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00485

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_09`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ลมทะเล เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_09"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00492

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_10`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ห้องสมุดดาว สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_10"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00493

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_10`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ห้องสมุดดาว มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_10"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00494

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_10`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ห้องสมุดดาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_10"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00495

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_10`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ห้องสมุดดาว เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_10"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00502

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_11`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ต้นเฟิร์น สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_11"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00503

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_11`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ต้นเฟิร์น มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_11"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00504

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_11`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ต้นเฟิร์น ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_11"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00505

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_11`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ต้นเฟิร์น เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_11"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00512

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_12`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ทองทราย สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_12"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00513

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_12`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ทองทราย มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_12"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00514

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_12`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ ทองทราย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_12"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00515

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_12`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ ทองทราย เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): vr
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: vr_motion
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_12"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "vr"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "vr_motion"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00522

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_13`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ จันทร์เสี้ยว สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_13"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00523

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_13`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ จันทร์เสี้ยว มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_13"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00524

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_13`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ จันทร์เสี้ยว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_13"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00525

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_13`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ จันทร์เสี้ยว เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): wheel
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: racing_wheel
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_13"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "wheel"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "racing_wheel"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00532

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_14`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ แสงอรุณ สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_14"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00533

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_14`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ แสงอรุณ มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_14"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00534

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_14`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ แสงอรุณ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_14"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00535

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_14`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ แสงอรุณ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_14"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00542

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_15`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ กิ่งไผ่ สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_15"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00543

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_15`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ กิ่งไผ่ มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_15"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00544

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_15`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ กิ่งไผ่ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_15"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00545

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_15`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ กิ่งไผ่ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_15"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00552

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_16`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ เมฆขาว สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_16"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00553

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_16`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ เมฆขาว มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_16"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00554

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_16`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ เมฆขาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_16"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00555

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_16`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ เมฆขาว เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): • key: DEMO screen; unit: inch; value: 27
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_16"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "27"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00562

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_17`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ มะลิ สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_17"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00563

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_17`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ มะลิ มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_17"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00564

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_17`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ มะลิ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_17"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00565

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_17`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ มะลิ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): • key: DEMO screen; unit: inch; value: 30
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_17"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "30"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00572

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_18`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ กระเบน สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_18"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00573

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_18`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ กระเบน มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_18"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00574

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_18`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ กระเบน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_18"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00575

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_18`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ กระเบน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): • key: DEMO screen; unit: inch; value: 33
• key: DEMO input; unit: ; value: keyboard_mouse
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_18"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "33"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "keyboard_mouse"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00582

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_19`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ แปะก๊วย สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_19"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00583

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_19`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ แปะก๊วย มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_19"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00584

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_19`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ แปะก๊วย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_19"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00585

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_19`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ แปะก๊วย เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): console
สเปก (specifications): • key: DEMO screen; unit: inch; value: 36
• key: DEMO input; unit: ; value: gamepad
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_19"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "console"
  },
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture20_demo20_equipment_model_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      {
        "key": "DEMO screen",
        "unit": "inch",
        "value": "36"
      },
      {
        "key": "DEMO input",
        "unit": "",
        "value": "gamepad"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00592

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_equipment_model_20`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ รุ่งเรือง สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_20"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00593

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_equipment_model_20`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ รุ่งเรือง มีรายละเอียดสเปกเครื่องยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_20"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00594

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_equipment_model_20`

### ผู้ใช้ถามอะไร

```text
แล้วสเปกมีอะไรบ้าง
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รุ่นอุปกรณ์ รุ่งเรือง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_20"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 00595

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_equipment_model_20`

### ผู้ใช้ถามอะไร

```text
รุ่นอุปกรณ์ รุ่งเรือง เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ประเภทอุปกรณ์ (`device_type`), สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ประเภทอุปกรณ์ (device_type): pc
สเปก (specifications): ยังไม่มีข้อมูลยืนยันในช่องนี้ / Not yet confirmed
```

### ทำไมได้คำตอบแบบนี้

หา demo20_equipment_model_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_equipment_model_20"
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

response_clarification, missing_field:device_type, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "device_type": {
    "evidence_refs": [
      {
        "locator": "/values/device_type",
        "source_id": "fixture20_demo20_equipment_model_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "pc"
  },
  "specifications": {
    "evidence_refs": [],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์",
    "status": "unknown",
    "value": null
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04990

**หมวด:** equipment_model • **ภาษา:** th • **รูปแบบ:** old_control_natural • **record ที่ควรตอบ:** `demo_equipment_model_01`

### ผู้ใช้ถามอะไร

```text
ตัวอย่าง รุ่นและสเปกอุปกรณ์ 01 สเปกมีอะไรบ้าง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: สเปก (`specifications`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
สเปก (specifications): • key: demo_memory; unit: GB; value: 12
• key: demo_storage; unit: GB; value: 384
```

### ทำไมได้คำตอบแบบนี้

หา demo_equipment_model_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo_equipment_model_01"
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

response_clarification, missing_field:specifications

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "specifications": {
    "evidence_refs": [
      {
        "locator": "/values/specifications",
        "source_id": "fixture_source_demo_equipment_model_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": [
      {
        "key": "demo_memory",
        "unit": "GB",
        "value": "12"
      },
      {
        "key": "demo_storage",
        "unit": "GB",
        "value": "384"
      }
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/records/equipment_model/demo_equipment_model_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

