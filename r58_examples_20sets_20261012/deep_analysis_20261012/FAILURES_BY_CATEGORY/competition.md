# ภาคผนวกเคสไม่ผ่าน — competition / 101 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 03762](#case-03762), [Case 03763](#case-03763), [Case 03764](#case-03764), [Case 03765](#case-03765), [Case 03768](#case-03768), [Case 03772](#case-03772), [Case 03773](#case-03773), [Case 03774](#case-03774), [Case 03775](#case-03775), [Case 03778](#case-03778), [Case 03782](#case-03782), [Case 03783](#case-03783), [Case 03784](#case-03784), [Case 03785](#case-03785), [Case 03788](#case-03788), [Case 03792](#case-03792), [Case 03793](#case-03793), [Case 03794](#case-03794), [Case 03795](#case-03795), [Case 03798](#case-03798), [Case 03802](#case-03802), [Case 03803](#case-03803), [Case 03804](#case-03804), [Case 03805](#case-03805), [Case 03808](#case-03808), [Case 03812](#case-03812), [Case 03813](#case-03813), [Case 03814](#case-03814), [Case 03815](#case-03815), [Case 03818](#case-03818), [Case 03822](#case-03822), [Case 03823](#case-03823), [Case 03824](#case-03824), [Case 03825](#case-03825), [Case 03828](#case-03828), [Case 03832](#case-03832), [Case 03833](#case-03833), [Case 03834](#case-03834), [Case 03835](#case-03835), [Case 03838](#case-03838), [Case 03842](#case-03842), [Case 03843](#case-03843), [Case 03844](#case-03844), [Case 03845](#case-03845), [Case 03848](#case-03848), [Case 03852](#case-03852), [Case 03853](#case-03853), [Case 03854](#case-03854), [Case 03855](#case-03855), [Case 03858](#case-03858), [Case 03862](#case-03862), [Case 03863](#case-03863), [Case 03864](#case-03864), [Case 03865](#case-03865), [Case 03868](#case-03868), [Case 03872](#case-03872), [Case 03873](#case-03873), [Case 03874](#case-03874), [Case 03875](#case-03875), [Case 03878](#case-03878), [Case 03882](#case-03882), [Case 03883](#case-03883), [Case 03884](#case-03884), [Case 03885](#case-03885), [Case 03888](#case-03888), [Case 03892](#case-03892), [Case 03893](#case-03893), [Case 03894](#case-03894), [Case 03895](#case-03895), [Case 03898](#case-03898), [Case 03902](#case-03902), [Case 03903](#case-03903), [Case 03904](#case-03904), [Case 03905](#case-03905), [Case 03908](#case-03908), [Case 03912](#case-03912), [Case 03913](#case-03913), [Case 03914](#case-03914), [Case 03915](#case-03915), [Case 03918](#case-03918), [Case 03922](#case-03922), [Case 03923](#case-03923), [Case 03924](#case-03924), [Case 03925](#case-03925), [Case 03928](#case-03928), [Case 03932](#case-03932), [Case 03933](#case-03933), [Case 03934](#case-03934), [Case 03935](#case-03935), [Case 03938](#case-03938), [Case 03942](#case-03942), [Case 03943](#case-03943), [Case 03944](#case-03944), [Case 03945](#case-03945), [Case 03948](#case-03948), [Case 03952](#case-03952), [Case 03953](#case-03953), [Case 03954](#case-03954), [Case 03955](#case-03955), [Case 03958](#case-03958), [Case 04974](#case-04974)

## Case 03762

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_01`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ดาวเหนือ ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_1
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_01"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_1"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03763

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_01`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ดาวเหนือ รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_1
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_01'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_01"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 35,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_1"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03764

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_01`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ดาวเหนือ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_1
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_01"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_1"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03765

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_01`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ดาวเหนือ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ดาวเหนือ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ดาวเหนือ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: eligibility_registration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ดาวเหนือ [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.1 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_1
วันที่แข่ง (competition_dates): • 2026-12-01
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_01'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_01"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 47,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_1"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-01"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03768

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_01`

### ผู้ใช้ถามอะไร

```text
Demo event Northstar What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Northstar**
• competition id: Demo event Northstar [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: eligibility_registration [S4]
• heading: Demo rule Northstar [S5]
• section number: 2.1 [S6]
• text: Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_1
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_01'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_01"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_1"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03772

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_02`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ดาวเหนือ พลัส ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_2
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_02"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_2"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03773

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_02`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ดาวเหนือ พลัส รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_2
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_02'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_02"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_2"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03774

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_02`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ดาวเหนือ พลัส ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_2
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_02"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_2"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03775

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_02`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ดาวเหนือ พลัส ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ดาวเหนือ พลัส**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ดาวเหนือ พลัส [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: roster_composition [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ดาวเหนือ พลัส [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.2 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_2
วันที่แข่ง (competition_dates): • 2026-12-02
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_02'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_02"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 52,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_2"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-02"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03778

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_02`

### ผู้ใช้ถามอะไร

```text
Demo event Northstar Plus What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Northstar Plus**
• competition id: Demo event Northstar Plus [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: roster_composition [S4]
• heading: Demo rule Northstar Plus [S5]
• section number: 3.2 [S6]
• text: Fictional clause 2: for Player substitution, follow decision prohibited; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_2
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_02'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_02"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_2"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03782

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_03`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ละอองฝน ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_3
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_03"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_3"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03783

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_03`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ละอองฝน รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_3
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_03'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_03"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 34,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_3"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03784

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_03`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ละอองฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_3
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_03"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_3"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03785

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_03`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ละอองฝน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ละอองฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ละอองฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ละอองฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.3 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_3
วันที่แข่ง (competition_dates): • 2026-12-03
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_03'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_03"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_3"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-03"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03788

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_03`

### ผู้ใช้ถามอะไร

```text
Demo event Drizzle What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Drizzle**
• competition id: Demo event Drizzle [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: competition_format [S4]
• heading: Demo rule Drizzle [S5]
• section number: 4.3 [S6]
• text: Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_3
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_03'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_03"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_3"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03792

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_04`

### ผู้ใช้ถามอะไร

```text
รายการฝึก สายหมอก ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_4
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_04"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_4"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03793

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_04`

### ผู้ใช้ถามอะไร

```text
รายการฝึก สายหมอก รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_4
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_04'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_04"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 34,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_4"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03794

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_04`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก สายหมอก ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_4
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_04"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_4"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03795

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_04`

### ผู้ใช้ถามอะไร

```text
รายการฝึก สายหมอก ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง สายหมอก**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก สายหมอก [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: match_configuration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง สายหมอก [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.4 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_4
วันที่แข่ง (competition_dates): • 2026-12-04
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_04'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_04"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_4"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-04"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03798

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_04`

### ผู้ใช้ถามอะไร

```text
Demo event Mist What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Mist**
• competition id: Demo event Mist [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: match_configuration [S4]
• heading: Demo rule Mist [S5]
• section number: 5.4 [S6]
• text: Fictional clause 4: for Seat adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_4
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_04'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_04"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_4"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03802

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_05`

### ผู้ใช้ถามอะไร

```text
รายการฝึก บัวสีคราม ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_5
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_05"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_5"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03803

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_05`

### ผู้ใช้ถามอะไร

```text
รายการฝึก บัวสีคราม รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_5
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_05'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_05"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_5"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03804

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_05`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก บัวสีคราม ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_5
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_05"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_5"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03805

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_05`

### ผู้ใช้ถามอะไร

```text
รายการฝึก บัวสีคราม ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง บัวสีคราม**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก บัวสีคราม [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: pre_match_on_site [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง บัวสีคราม [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.5 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_5
วันที่แข่ง (competition_dates): • 2026-12-05
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_05'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_05"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 48,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_5"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-05"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03808

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_05`

### ผู้ใช้ถามอะไร

```text
Demo event Indigo Lotus What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Indigo Lotus**
• competition id: Demo event Indigo Lotus [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: pre_match_on_site [S4]
• heading: Demo rule Indigo Lotus [S5]
• section number: 1.5 [S6]
• text: Fictional clause 5: for Free learning activity, follow decision allowed; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_5
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_05'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_05"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 44,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_5"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03812

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_06`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ปะการัง ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_6
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_06"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_6"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03813

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_06`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ปะการัง รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_6
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_06'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_06"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 34,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_6"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03814

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_06`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ปะการัง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_6
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_06"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_6"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03815

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_06`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ปะการัง ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ปะการัง**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ปะการัง [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: in_match_operations [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ปะการัง [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.6 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_6
วันที่แข่ง (competition_dates): • 2026-12-06
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_06'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_06"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_6"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-06"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03818

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_06`

### ผู้ใช้ถามอะไร

```text
Demo event Coral What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Coral**
• competition id: Demo event Coral [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: in_match_operations [S4]
• heading: Demo rule Coral [S5]
• section number: 2.6 [S6]
• text: Fictional clause 6: for Food in the zone, follow decision prohibited; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_6
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_06'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_06"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 37,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_6"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03822

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_07`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ตะวันอ่อน ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_7
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_07"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_7"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03823

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_07`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ตะวันอ่อน รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_7
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_07'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_07"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_7"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03824

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_07`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ตะวันอ่อน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_7
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_07"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_7"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03825

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_07`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ตะวันอ่อน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ตะวันอ่อน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ตะวันอ่อน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: fair_play_conduct [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ตะวันอ่อน [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.7 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_7
วันที่แข่ง (competition_dates): • 2026-12-07
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_07'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_07"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 48,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_7"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-07"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03828

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_07`

### ผู้ใช้ถามอะไร

```text
Demo event Gentle Sun What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Gentle Sun**
• competition id: Demo event Gentle Sun [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: fair_play_conduct [S4]
• heading: Demo rule Gentle Sun [S5]
• section number: 3.7 [S6]
• text: Fictional clause 7: for Team roster, follow decision required; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_7
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_07'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_07"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_7"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03832

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_08`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ฟ้าหลังฝน ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_8
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_08"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_8"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03833

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_08`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ฟ้าหลังฝน รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_8
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_08'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_08"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_8"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03834

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_08`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ฟ้าหลังฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_8
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_08"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_8"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03835

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_08`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ฟ้าหลังฝน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ฟ้าหลังฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ฟ้าหลังฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: penalty_matrix [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ฟ้าหลังฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.8 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_8
วันที่แข่ง (competition_dates): • 2026-12-08
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_08'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_08"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 48,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_8"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-08"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03838

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_08`

### ผู้ใช้ถามอะไร

```text
Demo event After Rain What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule After Rain**
• competition id: Demo event After Rain [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: penalty_matrix [S4]
• heading: Demo rule After Rain [S5]
• section number: 4.8 [S6]
• text: Fictional clause 8: for Player accounts, follow decision conditional; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_8
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_08'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_08"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_8"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03842

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_09`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ลมทะเล ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_9
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_09"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_9"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03843

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_09`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ลมทะเล รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_9
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_09'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_09"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 33,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_9"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03844

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_09`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ลมทะเล ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_9
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_09"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_9"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03845

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_09`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ลมทะเล ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ลมทะเล**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ลมทะเล [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: protest_dispute [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ลมทะเล [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.9 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_9
วันที่แข่ง (competition_dates): • 2026-12-09
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_09'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_09"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 45,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_9"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-09"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03848

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_09`

### ผู้ใช้ถามอะไร

```text
Demo event Sea Breeze What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Sea Breeze**
• competition id: Demo event Sea Breeze [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: protest_dispute [S4]
• heading: Demo rule Sea Breeze [S5]
• section number: 5.9 [S6]
• text: Fictional clause 9: for Group reservations, follow decision required; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_9
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_09'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_09"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_9"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03852

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_10`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ห้องสมุดดาว ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_10
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_10"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_10"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03853

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_10`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ห้องสมุดดาว รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_10
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_10'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_10"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 38,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_10"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03854

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_10`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ห้องสมุดดาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_10
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_10"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_10"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03855

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_10`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ห้องสมุดดาว ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ห้องสมุดดาว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ห้องสมุดดาว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: identity [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ห้องสมุดดาว [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.10 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_10
วันที่แข่ง (competition_dates): • 2026-12-10
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_10'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_10"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 50,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_10"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-10"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03858

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_10`

### ผู้ใช้ถามอะไร

```text
Demo event Star Library What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Star Library**
• competition id: Demo event Star Library [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: identity [S4]
• heading: Demo rule Star Library [S5]
• section number: 1.10 [S6]
• text: Fictional clause 10: for Volume adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_10
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_10'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_10"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 44,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_10"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03862

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_11`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ต้นเฟิร์น ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_11
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_11"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_11"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03863

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_11`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ต้นเฟิร์น รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_11
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_11'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_11"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_11"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03864

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_11`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ต้นเฟิร์น ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_11
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_11"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_11"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03865

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_11`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ต้นเฟิร์น ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ต้นเฟิร์น**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ต้นเฟิร์น [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: eligibility_registration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ต้นเฟิร์น [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.11 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_11
วันที่แข่ง (competition_dates): • 2026-12-11
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_11'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_11"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 48,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_11"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-11"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03868

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_11`

### ผู้ใช้ถามอะไร

```text
Demo event Fern What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Fern**
• competition id: Demo event Fern [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: eligibility_registration [S4]
• heading: Demo rule Fern [S5]
• section number: 2.11 [S6]
• text: Fictional clause 11: for Personal devices, follow decision allowed; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_11
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_11'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_11"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_11"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03872

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_12`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ทองทราย ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_12
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_12"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_12"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03873

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_12`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ทองทราย รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_12
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_12'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_12"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 34,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_12"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03874

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_12`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก ทองทราย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_12
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_12"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_12"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03875

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_12`

### ผู้ใช้ถามอะไร

```text
รายการฝึก ทองทราย ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง ทองทราย**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ทองทราย [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: roster_composition [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ทองทราย [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.12 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_12
วันที่แข่ง (competition_dates): • 2026-12-12
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_12'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_12"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_12"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-12"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03878

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_12`

### ผู้ใช้ถามอะไร

```text
Demo event Sand Gold What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Sand Gold**
• competition id: Demo event Sand Gold [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: roster_composition [S4]
• heading: Demo rule Sand Gold [S5]
• section number: 3.12 [S6]
• text: Fictional clause 12: for Safety boundary, follow decision required; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_12
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_12'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_12"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 41,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_12"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03882

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_13`

### ผู้ใช้ถามอะไร

```text
รายการฝึก จันทร์เสี้ยว ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_13
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_13"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_13"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03883

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_13`

### ผู้ใช้ถามอะไร

```text
รายการฝึก จันทร์เสี้ยว รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_13
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_13'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_13"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_13"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03884

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_13`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก จันทร์เสี้ยว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_13
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_13"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_13"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03885

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_13`

### ผู้ใช้ถามอะไร

```text
รายการฝึก จันทร์เสี้ยว ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง จันทร์เสี้ยว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก จันทร์เสี้ยว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง จันทร์เสี้ยว [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.13 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_13
วันที่แข่ง (competition_dates): • 2026-12-13
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_13'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_13"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 51,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_13"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-13"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03888

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_13`

### ผู้ใช้ถามอะไร

```text
Demo event Crescent What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Crescent**
• competition id: Demo event Crescent [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: competition_format [S4]
• heading: Demo rule Crescent [S5]
• section number: 4.13 [S6]
• text: Fictional clause 13: for Practice before starting, follow decision allowed; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_13
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_13'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_13"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_13"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03892

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_14`

### ผู้ใช้ถามอะไร

```text
รายการฝึก แสงอรุณ ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_14
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_14"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_14"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03893

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_14`

### ผู้ใช้ถามอะไร

```text
รายการฝึก แสงอรุณ รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_14
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_14'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_14"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 34,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_14"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03894

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_14`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก แสงอรุณ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_14
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_14"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_14"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03895

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_14`

### ผู้ใช้ถามอะไร

```text
รายการฝึก แสงอรุณ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง แสงอรุณ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก แสงอรุณ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: match_configuration [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง แสงอรุณ [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.14 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_14
วันที่แข่ง (competition_dates): • 2026-12-14
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_14'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_14"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_14"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-14"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03898

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_14`

### ผู้ใช้ถามอะไร

```text
Demo event Dawn Light What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Dawn Light**
• competition id: Demo event Dawn Light [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: match_configuration [S4]
• heading: Demo rule Dawn Light [S5]
• section number: 5.14 [S6]
• text: Fictional clause 14: for Photography, follow decision conditional; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_14
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_14'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_14"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 42,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_14"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03902

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_15`

### ผู้ใช้ถามอะไร

```text
รายการฝึก กิ่งไผ่ ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_15
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_15"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_15"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03903

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_15`

### ผู้ใช้ถามอะไร

```text
รายการฝึก กิ่งไผ่ รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_15
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_15'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_15"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 34,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_15"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03904

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_15`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก กิ่งไผ่ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_15
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_15"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_15"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03905

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_15`

### ผู้ใช้ถามอะไร

```text
รายการฝึก กิ่งไผ่ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง กิ่งไผ่**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก กิ่งไผ่ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: pre_match_on_site [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง กิ่งไผ่ [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.15 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_15
วันที่แข่ง (competition_dates): • 2026-12-15
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_15'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_15"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_15"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-15"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03908

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_15`

### ผู้ใช้ถามอะไร

```text
Demo event Bamboo What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Bamboo**
• competition id: Demo event Bamboo [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: pre_match_on_site [S4]
• heading: Demo rule Bamboo [S5]
• section number: 1.15 [S6]
• text: Fictional clause 15: for Software installation, follow decision prohibited; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_15
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_15'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_15"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 38,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_15"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03912

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_16`

### ผู้ใช้ถามอะไร

```text
รายการฝึก เมฆขาว ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_16
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_16"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_16"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03913

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_16`

### ผู้ใช้ถามอะไร

```text
รายการฝึก เมฆขาว รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_16
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_16'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_16"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 33,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_16"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03914

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_16`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก เมฆขาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_16
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_16"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_16"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03915

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_16`

### ผู้ใช้ถามอะไร

```text
รายการฝึก เมฆขาว ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง เมฆขาว**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก เมฆขาว [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: in_match_operations [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง เมฆขาว [S5]
• เลขข้อเดิม เช่น 6.1.5: 2.16 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_16
วันที่แข่ง (competition_dates): • 2026-12-16
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_16'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_16"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 45,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_16"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-16"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03918

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_16`

### ผู้ใช้ถามอะไร

```text
Demo event White Cloud What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule White Cloud**
• competition id: Demo event White Cloud [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: in_match_operations [S4]
• heading: Demo rule White Cloud [S5]
• section number: 2.16 [S6]
• text: Fictional clause 16: for Accessibility assistance, follow decision allowed; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_16
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_16'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_16"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 43,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_16"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03922

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_17`

### ผู้ใช้ถามอะไร

```text
รายการฝึก มะลิ ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_17
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_17"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_17"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03923

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_17`

### ผู้ใช้ถามอะไร

```text
รายการฝึก มะลิ รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_17
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_17'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_17"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 31,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_17"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03924

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_17`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก มะลิ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_17
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_17"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_17"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03925

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_17`

### ผู้ใช้ถามอะไร

```text
รายการฝึก มะลิ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง มะลิ**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก มะลิ [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: fair_play_conduct [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง มะลิ [S5]
• เลขข้อเดิม เช่น 6.1.5: 3.17 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_17
วันที่แข่ง (competition_dates): • 2026-12-17
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_17'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_17"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 43,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_17"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-17"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03928

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_17`

### ผู้ใช้ถามอะไร

```text
Demo event Jasmine What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Jasmine**
• competition id: Demo event Jasmine [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: fair_play_conduct [S4]
• heading: Demo rule Jasmine [S5]
• section number: 3.17 [S6]
• text: Fictional clause 17: for Changing dates, follow decision conditional; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_17
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_17'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_17"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 39,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_17"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03932

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_18`

### ผู้ใช้ถามอะไร

```text
รายการฝึก กระเบน ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_18
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_18"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_18"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03933

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_18`

### ผู้ใช้ถามอะไร

```text
รายการฝึก กระเบน รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_18
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_18'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_18"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 33,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_18"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03934

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_18`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก กระเบน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_18
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_18"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_18"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03935

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_18`

### ผู้ใช้ถามอะไร

```text
รายการฝึก กระเบน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง กระเบน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก กระเบน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: penalty_matrix [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง กระเบน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.18 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_18
วันที่แข่ง (competition_dates): • 2026-12-18
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_18'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_18"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 45,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_18"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-18"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03938

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_18`

### ผู้ใช้ถามอะไร

```text
Demo event Ray What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Ray**
• competition id: Demo event Ray [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: penalty_matrix [S4]
• heading: Demo rule Ray [S5]
• section number: 4.18 [S6]
• text: Fictional clause 18: for Refund requests, follow decision prohibited; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_18
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_18'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_18"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 35,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_18"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03942

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_19`

### ผู้ใช้ถามอะไร

```text
รายการฝึก แปะก๊วย ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_19
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_19"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_19"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03943

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_19`

### ผู้ใช้ถามอะไร

```text
รายการฝึก แปะก๊วย รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_19
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_19'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_19"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 34,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_19"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03944

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_19`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก แปะก๊วย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_19
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_19"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_19"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03945

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_19`

### ผู้ใช้ถามอะไร

```text
รายการฝึก แปะก๊วย ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง แปะก๊วย**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก แปะก๊วย [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: protest_dispute [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง แปะก๊วย [S5]
• เลขข้อเดิม เช่น 6.1.5: 5.19 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_19
วันที่แข่ง (competition_dates): • 2026-12-19
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_19'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_19"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 46,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_19"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-19"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03948

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_19`

### ผู้ใช้ถามอะไร

```text
Demo event Ginkgo What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Ginkgo**
• competition id: Demo event Ginkgo [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: protest_dispute [S4]
• heading: Demo rule Ginkgo [S5]
• section number: 5.19 [S6]
• text: Fictional clause 19: for Check-in proof, follow decision required; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_19
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_19'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_19"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 38,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_19"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03952

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_20`

### ผู้ใช้ถามอะไร

```text
รายการฝึก รุ่งเรือง ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_20
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_20"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_20"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03953

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_20`

### ผู้ใช้ถามอะไร

```text
รายการฝึก รุ่งเรือง รายการนี้อ้างอิงกฎเวอร์ชันอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

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

details: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_20
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_20'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_20"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "กฎ",
      "offset": 36,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_20"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03954

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_20`

### ผู้ใช้ถามอะไร

```text
แล้วใช้กติกาฉบับไหน
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "รายการฝึก รุ่งเรือง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_20
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_20"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_20"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03955

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_20`

### ผู้ใช้ถามอะไร

```text
รายการฝึก รุ่งเรือง ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`), วันที่แข่ง (`competition_dates`)

### คำตอบที่ระบบส่งจริง

```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

**ข้อการแข่งขันทดลอง รุ่งเรือง**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก รุ่งเรือง [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: identity [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง รุ่งเรือง [S5]
• เลขข้อเดิม เช่น 6.1.5: 1.20 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_20
วันที่แข่ง (competition_dates): • 2026-12-20
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_20'] และหัวข้อ ['amount_minor']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release', 'competition_dates']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_20"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "amount_minor",
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
      "field": "amount_minor",
      "term": "เท่าไหร่",
      "offset": 48,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release, missing_field:competition_dates

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_20"
  },
  "competition_dates": {
    "evidence_refs": [
      {
        "locator": "/values/competition_dates",
        "source_id": "fixture20_demo20_competition_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": [
      "2026-12-20"
    ]
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 03958

**หมวด:** competition • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_competition_20`

### ผู้ใช้ถามอะไร

```text
Demo event Radiance What version of the rules is used?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
**Demo rule Radiance**
• competition id: Demo event Radiance [S1]
• completeness: complete [S2]
• depends on ids:  [S3]
• facet: identity [S4]
• heading: Demo rule Radiance [S5]
• section number: 1.20 [S6]
• text: Fictional clause 20: for Result appeals, follow decision conditional; exception requires written demo operator approval; not actual rules [S7]

details: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO20_REV_20
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_20'] และหัวข้อ ['details']; field ของ target ที่ยังไม่มี obligation คือ ['rulebook_release']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_20"
    ],
    "requested_fields": [
      "details"
    ],
    "all_fields": false,
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
    },
    {
      "record_id": null,
      "field": "details",
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
      "field": "details",
      "term": "rules",
      "offset": 40,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture20_demo20_competition_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": "DEMO20_REV_20"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04974

**หมวด:** competition • **ภาษา:** th • **รูปแบบ:** old_control_natural • **record ที่ควรตอบ:** `demo_competition_01`

### ผู้ใช้ถามอะไร

```text
ตัวอย่าง รายการแข่งขันและฉบับกติกา 01 ใช้กติกาฉบับไหน
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ฉบับกติกา (`rulebook_release`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ฉบับกติกา (rulebook_release): DEMO_RULEBOOK_01
```

### ทำไมได้คำตอบแบบนี้

หา demo_competition_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo_competition_01"
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

response_clarification, missing_field:rulebook_release

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "rulebook_release": {
    "evidence_refs": [
      {
        "locator": "/values/rulebook_release",
        "source_id": "fixture_source_demo_competition_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": "DEMO_RULEBOOK_01"
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/records/competition/demo_competition_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

