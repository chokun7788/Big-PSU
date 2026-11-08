# ภาคผนวกเคสไม่ผ่าน — faq / 101 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 04562](#case-04562), [Case 04563](#case-04563), [Case 04564](#case-04564), [Case 04565](#case-04565), [Case 04570](#case-04570), [Case 04572](#case-04572), [Case 04573](#case-04573), [Case 04574](#case-04574), [Case 04575](#case-04575), [Case 04580](#case-04580), [Case 04582](#case-04582), [Case 04583](#case-04583), [Case 04584](#case-04584), [Case 04585](#case-04585), [Case 04590](#case-04590), [Case 04592](#case-04592), [Case 04593](#case-04593), [Case 04594](#case-04594), [Case 04595](#case-04595), [Case 04600](#case-04600), [Case 04602](#case-04602), [Case 04603](#case-04603), [Case 04604](#case-04604), [Case 04605](#case-04605), [Case 04610](#case-04610), [Case 04612](#case-04612), [Case 04613](#case-04613), [Case 04614](#case-04614), [Case 04615](#case-04615), [Case 04620](#case-04620), [Case 04622](#case-04622), [Case 04623](#case-04623), [Case 04624](#case-04624), [Case 04625](#case-04625), [Case 04630](#case-04630), [Case 04632](#case-04632), [Case 04633](#case-04633), [Case 04634](#case-04634), [Case 04635](#case-04635), [Case 04640](#case-04640), [Case 04642](#case-04642), [Case 04643](#case-04643), [Case 04644](#case-04644), [Case 04645](#case-04645), [Case 04650](#case-04650), [Case 04652](#case-04652), [Case 04653](#case-04653), [Case 04654](#case-04654), [Case 04655](#case-04655), [Case 04660](#case-04660), [Case 04662](#case-04662), [Case 04663](#case-04663), [Case 04664](#case-04664), [Case 04665](#case-04665), [Case 04670](#case-04670), [Case 04672](#case-04672), [Case 04673](#case-04673), [Case 04674](#case-04674), [Case 04675](#case-04675), [Case 04680](#case-04680), [Case 04682](#case-04682), [Case 04683](#case-04683), [Case 04684](#case-04684), [Case 04685](#case-04685), [Case 04690](#case-04690), [Case 04692](#case-04692), [Case 04693](#case-04693), [Case 04694](#case-04694), [Case 04695](#case-04695), [Case 04700](#case-04700), [Case 04702](#case-04702), [Case 04703](#case-04703), [Case 04704](#case-04704), [Case 04705](#case-04705), [Case 04710](#case-04710), [Case 04712](#case-04712), [Case 04713](#case-04713), [Case 04714](#case-04714), [Case 04715](#case-04715), [Case 04720](#case-04720), [Case 04722](#case-04722), [Case 04723](#case-04723), [Case 04724](#case-04724), [Case 04725](#case-04725), [Case 04730](#case-04730), [Case 04732](#case-04732), [Case 04733](#case-04733), [Case 04734](#case-04734), [Case 04735](#case-04735), [Case 04740](#case-04740), [Case 04742](#case-04742), [Case 04743](#case-04743), [Case 04744](#case-04744), [Case 04745](#case-04745), [Case 04750](#case-04750), [Case 04752](#case-04752), [Case 04753](#case-04753), [Case 04754](#case-04754), [Case 04755](#case-04755), [Case 04760](#case-04760), [Case 04998](#case-04998)

## Case 04562

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_01`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ดาวเหนือ คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_01'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_01"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 28,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04563

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_01`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ดาวเหนือ ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_01"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04564

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_01`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ดาวเหนือ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_01'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_01"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04565

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_01`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ดาวเหนือ คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_01'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_01"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 28,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Northstar scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04570

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_01`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Northstar What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Northstar**
• answer: Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Northstar scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_01'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_01"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_01",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_01"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Northstar scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04572

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_02`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ดาวเหนือ พลัส คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_02'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_02"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 33,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04573

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_02`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ดาวเหนือ พลัส ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_02"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04574

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_02`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ดาวเหนือ พลัส ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_02'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_02"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04575

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_02`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ดาวเหนือ พลัส คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ พลัส
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_02'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_02"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 33,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Northstar Plus scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ พลัส"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04580

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_02`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Northstar Plus What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Northstar Plus**
• answer: Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Northstar Plus scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_02'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_02"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_02",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_02"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 28,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Northstar Plus scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ พลัส"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04582

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_03`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ละอองฝน คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_03'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04583

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_03`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ละอองฝน ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_03"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04584

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_03`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ละอองฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_03'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04585

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_03`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ละอองฝน คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ละอองฝน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_03'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Drizzle scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ละอองฝน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04590

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_03`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Drizzle What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Drizzle**
• answer: Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Drizzle scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_03'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_03"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_03",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_03"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 21,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Drizzle scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ละอองฝน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04592

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_04`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง สายหมอก คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_04'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_04"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04593

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_04`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง สายหมอก ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_04"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04594

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_04`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง สายหมอก ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_04'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_04"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04595

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_04`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง สายหมอก คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ สายหมอก
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_04'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_04"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Mist scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ สายหมอก"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04600

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_04`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Mist What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Mist**
• answer: Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Mist scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_04'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_04"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_04",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_04"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 18,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Mist scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ สายหมอก"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04602

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_05`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง บัวสีคราม คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_05'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_05"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04603

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_05`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง บัวสีคราม ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_05"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04604

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_05`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง บัวสีคราม ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_05'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_05"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04605

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_05`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง บัวสีคราม คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ บัวสีคราม
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_05'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_05"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Indigo Lotus scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ บัวสีคราม"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04610

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_05`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Indigo Lotus What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Indigo Lotus**
• answer: Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Indigo Lotus scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_05'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_05"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_05",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_05"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Indigo Lotus scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ บัวสีคราม"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04612

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_06`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ปะการัง คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_06'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_06"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04613

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_06`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ปะการัง ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_06"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04614

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_06`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ปะการัง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_06'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_06"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04615

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_06`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ปะการัง คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ปะการัง
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_06'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_06"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Coral scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ปะการัง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04620

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_06`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Coral What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Coral**
• answer: Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Coral scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_06'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_06"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_06",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_06"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 19,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Coral scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ปะการัง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04622

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_07`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ตะวันอ่อน คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_07'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_07"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04623

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_07`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ตะวันอ่อน ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_07"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04624

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_07`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ตะวันอ่อน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_07'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_07"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04625

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_07`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ตะวันอ่อน คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ตะวันอ่อน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_07'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_07"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Gentle Sun scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ตะวันอ่อน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04630

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_07`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Gentle Sun What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Gentle Sun**
• answer: Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Gentle Sun scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_07'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_07"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_07",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_07"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Gentle Sun scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ตะวันอ่อน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04632

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_08`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ฟ้าหลังฝน คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_08'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_08"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04633

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_08`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ฟ้าหลังฝน ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_08"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04634

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_08`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ฟ้าหลังฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_08'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_08"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04635

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_08`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ฟ้าหลังฝน คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ฟ้าหลังฝน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_08'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_08"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional After Rain scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ฟ้าหลังฝน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04640

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_08`

### ผู้ใช้ถามอะไร

```text
Demo enquiry After Rain What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry After Rain**
• answer: Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional After Rain scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_08'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_08"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_08",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_08"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional After Rain scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ฟ้าหลังฝน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04642

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_09`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ลมทะเล คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_09'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_09"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04643

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_09`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ลมทะเล ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_09"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04644

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_09`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ลมทะเล ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_09'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_09"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04645

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_09`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ลมทะเล คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ลมทะเล
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_09'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_09"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Sea Breeze scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ลมทะเล"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04650

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_09`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Sea Breeze What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Sea Breeze**
• answer: Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Sea Breeze scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_09'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_09"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_09",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_09"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Sea Breeze scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ลมทะเล"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04652

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_10`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ห้องสมุดดาว คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_10'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_10"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 31,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04653

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_10`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ห้องสมุดดาว ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_10"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04654

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_10`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ห้องสมุดดาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_10'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_10"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04655

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_10`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ห้องสมุดดาว คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ห้องสมุดดาว
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_10'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_10"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 31,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Star Library scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ห้องสมุดดาว"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04660

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_10`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Star Library What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Star Library**
• answer: Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Star Library scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_10'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_10"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_10",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_10"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Star Library scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ห้องสมุดดาว"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04662

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_11`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ต้นเฟิร์น คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_11'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_11"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04663

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_11`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ต้นเฟิร์น ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_11"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04664

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_11`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ต้นเฟิร์น ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_11'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_11"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04665

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_11`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ต้นเฟิร์น คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ต้นเฟิร์น
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_11'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_11"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Fern scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ต้นเฟิร์น"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04670

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_11`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Fern What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Fern**
• answer: Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Fern scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_11'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_11"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_11",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_11"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 18,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Fern scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ต้นเฟิร์น"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04672

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_12`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ทองทราย คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_12'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_12"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04673

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_12`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ทองทราย ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_12"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04674

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_12`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง ทองทราย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_12'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_12"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04675

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_12`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง ทองทราย คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ ทองทราย
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_12'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_12"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Sand Gold scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ทองทราย"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04680

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_12`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Sand Gold What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Sand Gold**
• answer: Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Sand Gold scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_12'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_12"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_12",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_12"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 23,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Sand Gold scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ทองทราย"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04682

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_13`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง จันทร์เสี้ยว คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_13'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_13"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 32,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04683

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_13`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง จันทร์เสี้ยว ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_13"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04684

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_13`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง จันทร์เสี้ยว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_13'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_13"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04685

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_13`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง จันทร์เสี้ยว คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ จันทร์เสี้ยว
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_13'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_13"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 32,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Crescent scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ จันทร์เสี้ยว"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04690

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_13`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Crescent What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Crescent**
• answer: Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Crescent scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_13'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_13"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_13",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_13"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 22,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Crescent scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ จันทร์เสี้ยว"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04692

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_14`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง แสงอรุณ คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_14'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_14"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04693

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_14`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง แสงอรุณ ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_14"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04694

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_14`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง แสงอรุณ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_14'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_14"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04695

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_14`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง แสงอรุณ คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ แสงอรุณ
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_14'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_14"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Dawn Light scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ แสงอรุณ"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04700

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_14`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Dawn Light What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Dawn Light**
• answer: Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Dawn Light scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_14'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_14"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_14",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_14"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Dawn Light scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ แสงอรุณ"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04702

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_15`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง กิ่งไผ่ คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_15'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_15"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04703

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_15`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง กิ่งไผ่ ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_15"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04704

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_15`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง กิ่งไผ่ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_15'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_15"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04705

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_15`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง กิ่งไผ่ คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ กิ่งไผ่
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_15'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_15"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Bamboo scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ กิ่งไผ่"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04710

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_15`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Bamboo What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Bamboo**
• answer: Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Bamboo scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_15'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_15"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_15",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_15"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 20,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Bamboo scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ กิ่งไผ่"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04712

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_16`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง เมฆขาว คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_16'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_16"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04713

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_16`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง เมฆขาว ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_16"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04714

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_16`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง เมฆขาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_16'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_16"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04715

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_16`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง เมฆขาว คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ เมฆขาว
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_16'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_16"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional White Cloud scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ เมฆขาว"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04720

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_16`

### ผู้ใช้ถามอะไร

```text
Demo enquiry White Cloud What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry White Cloud**
• answer: Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional White Cloud scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_16'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_16"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_16",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_16"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional White Cloud scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ เมฆขาว"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04722

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_17`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง มะลิ คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_17'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_17"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04723

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_17`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง มะลิ ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_17"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04724

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_17`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง มะลิ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_17'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_17"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04725

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_17`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง มะลิ คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ มะลิ
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_17'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_17"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 24,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Jasmine scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ มะลิ"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04730

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_17`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Jasmine What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Jasmine**
• answer: Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Jasmine scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_17'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_17"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_17",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_17"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 21,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Jasmine scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ มะลิ"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04732

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_18`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง กระเบน คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_18'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_18"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04733

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_18`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง กระเบน ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_18"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04734

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_18`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง กระเบน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_18'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_18"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04735

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_18`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง กระเบน คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ กระเบน
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_18'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_18"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 26,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Ray scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ กระเบน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04740

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_18`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Ray What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Ray**
• answer: Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Ray scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_18'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_18"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_18",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_18"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 17,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Ray scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ กระเบน"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04742

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_19`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง แปะก๊วย คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_19'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_19"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04743

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_19`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง แปะก๊วย ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_19"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04744

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_19`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง แปะก๊วย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_19'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_19"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04745

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_19`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง แปะก๊วย คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ แปะก๊วย
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_19'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_19"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 27,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Ginkgo scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ แปะก๊วย"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04750

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_19`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Ginkgo What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Ginkgo**
• answer: Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Ginkgo scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_19'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_19"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_19",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_19"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 20,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Ginkgo scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ แปะก๊วย"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04752

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_faq_20`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง รุ่งเรือง คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_20'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_20"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04753

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_faq_20`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง รุ่งเรือง ช่วยตอบคำถามรายการนี้หน่อย
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo20_faq_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_20"
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

response_clarification, missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04754

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_faq_20`

### ผู้ใช้ถามอะไร

```text
แล้วคำตอบคืออะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "คำถามตัวอย่าง รุ่งเรือง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_20'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_faq_20"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 9,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04755

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_20`

### ผู้ใช้ถามอะไร

```text
คำถามตัวอย่าง รุ่งเรือง คำตอบคืออะไรและใช้กับกรณีไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU
ขอบเขตที่คำตอบใช้ได้ (scope_note): ใช้ได้เฉพาะสถานการณ์สมมุติ รุ่งเรือง
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_20'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer', 'scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_20"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 29,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer, missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Radiance scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ รุ่งเรือง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04760

**หมวด:** faq • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_faq_20`

### ผู้ใช้ถามอะไร

```text
Demo enquiry Radiance What is the answer and its scope?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`), ขอบเขตที่คำตอบใช้ได้ (`scope_note`)

### คำตอบที่ระบบส่งจริง

```text
**Demo enquiry Radiance**
• answer: Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy. [S1]

summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.
ขอบเขตที่คำตอบใช้ได้ (scope_note): Only applies to fictional Radiance scenario
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_faq_20'] และหัวข้อ ['summary', 'answer']; field ของ target ที่ยังไม่มี obligation คือ ['scope_note']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
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
      "demo20_faq_20"
    ],
    "requested_fields": [
      "summary",
      "answer"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_faq_20",
      "field": "answer",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/answer",
          "source_id": "fixture20_demo20_faq_20"
        }
      ]
    },
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "what is",
      "offset": 22,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [
    {
      "field": "answer",
      "kind": "faq",
      "match": "canonical key"
    }
  ],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:scope_note

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture20_demo20_faq_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
      "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
    }
  },
  "scope_note": {
    "evidence_refs": [
      {
        "locator": "/values/scope_note",
        "source_id": "fixture20_demo20_faq_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Only applies to fictional Radiance scenario",
      "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ รุ่งเรือง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04998

**หมวด:** faq • **ภาษา:** th • **รูปแบบ:** old_control_natural • **record ที่ควรตอบ:** `demo_faq_01`

### ผู้ใช้ถามอะไร

```text
ตัวอย่าง คำถามเสริมและเอกสารทั่วไปของศูนย์ 01 คำตอบคืออะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: คำตอบ FAQ (`answer`)

### คำตอบที่ระบบส่งจริง

```text
summary: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
คำตอบ FAQ (answer): คำตอบสมมุติ: เรื่อง เช็กอิน ให้ใช้ขั้นตอน C01 และติดต่อช่องทางตัวอย่าง
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo_faq_01'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['answer']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

- **R03 — ช่องที่เลือกใช้ไม่ได้กับ kind ที่พบ**: TERMS กลางไม่ถูกกรองด้วย kind แม้ fallback catalog labels ถูกกรอง requested_fields จึงมี summary/players_min/steps ฯลฯ ซึ่งไม่มีใน target; add ข้าม field และตอนท้ายสร้าง unknown ของ scope • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R04 — What is/about/description ถูกตีเป็น summary เกินบริบท**: คำทั่วไปไม่ได้หมายถึงเนื้อหาเกมเสมอ แต่ TERMS summary ใช้ทุกหมวด ทำให้คำถาม role/status/contact/version เป็นต้นเลือก summary และละเลยหัวข้อจริง • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:12)
- **R12 — ประตูเรียก LLM ไม่ครอบคลุม field ผิดหรือ field ไม่ครบ**: planner ถูกเรียกเมื่อไม่มี requested หรือ special steps; ถ้ามี players_min/summary/amount_minor แม้ผิดหมวดก็ไม่เรียก และ multi-field ที่ได้บางส่วนไม่ถูกเติม • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:162)
- **R18 — ข้อความยังไม่มีข้อมูลอาจเกิดจาก field ผิด ไม่ใช่ source unknown**: ท้าย answer ใส่ obligation record_id=None สำหรับ requested ที่ไม่มีใครตอบ ทำให้ผู้ใช้เห็น no information ทั้งที่ข้อมูลที่เขาต้องการมีในอีก field • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:254)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo_faq_01"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
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
      "field": "summary",
      "term": "คืออะไร",
      "offset": 51,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "answer": {
    "evidence_refs": [
      {
        "locator": "/values/answer",
        "source_id": "fixture_source_demo_faq_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional answer: for Check-in, use procedure C01 and the demo contact",
      "th": "คำตอบสมมุติ: เรื่อง เช็กอิน ให้ใช้ขั้นตอน C01 และติดต่อช่องทางตัวอย่าง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/records/faq/demo_faq_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

