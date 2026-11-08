# ภาคผนวกเคสไม่ผ่าน — competition_rule / 102 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 03962](#case-03962), [Case 03964](#case-03964), [Case 03967](#case-03967), [Case 03969](#case-03969), [Case 03970](#case-03970), [Case 03972](#case-03972), [Case 03974](#case-03974), [Case 03977](#case-03977), [Case 03979](#case-03979), [Case 03980](#case-03980), [Case 03982](#case-03982), [Case 03984](#case-03984), [Case 03987](#case-03987), [Case 03989](#case-03989), [Case 03990](#case-03990), [Case 03992](#case-03992), [Case 03994](#case-03994), [Case 03997](#case-03997), [Case 03999](#case-03999), [Case 04000](#case-04000), [Case 04002](#case-04002), [Case 04004](#case-04004), [Case 04007](#case-04007), [Case 04009](#case-04009), [Case 04010](#case-04010), [Case 04012](#case-04012), [Case 04014](#case-04014), [Case 04017](#case-04017), [Case 04019](#case-04019), [Case 04020](#case-04020), [Case 04022](#case-04022), [Case 04024](#case-04024), [Case 04027](#case-04027), [Case 04029](#case-04029), [Case 04030](#case-04030), [Case 04032](#case-04032), [Case 04034](#case-04034), [Case 04037](#case-04037), [Case 04039](#case-04039), [Case 04040](#case-04040), [Case 04042](#case-04042), [Case 04044](#case-04044), [Case 04047](#case-04047), [Case 04049](#case-04049), [Case 04050](#case-04050), [Case 04052](#case-04052), [Case 04054](#case-04054), [Case 04057](#case-04057), [Case 04059](#case-04059), [Case 04060](#case-04060), [Case 04062](#case-04062), [Case 04064](#case-04064), [Case 04067](#case-04067), [Case 04069](#case-04069), [Case 04070](#case-04070), [Case 04072](#case-04072), [Case 04074](#case-04074), [Case 04077](#case-04077), [Case 04079](#case-04079), [Case 04080](#case-04080), [Case 04082](#case-04082), [Case 04084](#case-04084), [Case 04087](#case-04087), [Case 04089](#case-04089), [Case 04090](#case-04090), [Case 04092](#case-04092), [Case 04094](#case-04094), [Case 04097](#case-04097), [Case 04099](#case-04099), [Case 04100](#case-04100), [Case 04102](#case-04102), [Case 04104](#case-04104), [Case 04107](#case-04107), [Case 04109](#case-04109), [Case 04110](#case-04110), [Case 04112](#case-04112), [Case 04114](#case-04114), [Case 04117](#case-04117), [Case 04119](#case-04119), [Case 04120](#case-04120), [Case 04122](#case-04122), [Case 04124](#case-04124), [Case 04127](#case-04127), [Case 04129](#case-04129), [Case 04130](#case-04130), [Case 04132](#case-04132), [Case 04134](#case-04134), [Case 04137](#case-04137), [Case 04139](#case-04139), [Case 04140](#case-04140), [Case 04142](#case-04142), [Case 04144](#case-04144), [Case 04147](#case-04147), [Case 04149](#case-04149), [Case 04150](#case-04150), [Case 04152](#case-04152), [Case 04154](#case-04154), [Case 04157](#case-04157), [Case 04159](#case-04159), [Case 04160](#case-04160), [Case 04978](#case-04978), [Case 04980](#case-04980)

## Case 03962

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ดาวเหนือ ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_01"
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

response_clarification, missing_field:text

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

## Case 03964

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ดาวเหนือ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_01"
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

response_clarification, missing_field:text

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

## Case 03967

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
Demo rule Northstar What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_01"
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

response_clarification, missing_field:text

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

## Case 03969

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Northstar Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_01'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_01"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 03970

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
Demo rule Northstar What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_01"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 03972

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_02`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ดาวเหนือ พลัส ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_02"
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

response_clarification, missing_field:text

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

## Case 03974

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_02`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ดาวเหนือ พลัส ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_02"
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

response_clarification, missing_field:text

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

## Case 03977

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_02`

### ผู้ใช้ถามอะไร

```text
Demo rule Northstar Plus What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 2: for Player substitution, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_02"
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

response_clarification, missing_field:text

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

## Case 03979

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_02`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Northstar Plus Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 2: for Player substitution, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_02'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_02"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 03980

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_02`

### ผู้ใช้ถามอะไร

```text
Demo rule Northstar Plus What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 2: for Player substitution, follow decision prohibited; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_02"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 03982

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_03`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ละอองฝน ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
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

response_clarification, missing_field:text

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

## Case 03984

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_03`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ละอองฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
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

response_clarification, missing_field:text

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

## Case 03987

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_03`

### ผู้ใช้ถามอะไร

```text
Demo rule Drizzle What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
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

response_clarification, missing_field:text

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

## Case 03989

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_03`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Drizzle Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_03'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 03990

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_03`

### ผู้ใช้ถามอะไร

```text
Demo rule Drizzle What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 03992

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_04`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง สายหมอก ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_04"
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

response_clarification, missing_field:text

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

## Case 03994

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_04`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง สายหมอก ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_04"
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

response_clarification, missing_field:text

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

## Case 03997

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_04`

### ผู้ใช้ถามอะไร

```text
Demo rule Mist What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 4: for Seat adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_04"
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

response_clarification, missing_field:text

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

## Case 03999

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_04`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Mist Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 4: for Seat adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_04'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_04"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04000

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_04`

### ผู้ใช้ถามอะไร

```text
Demo rule Mist What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 4: for Seat adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_04"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04002

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_05`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง บัวสีคราม ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_05"
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

response_clarification, missing_field:text

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

## Case 04004

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_05`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง บัวสีคราม ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_05"
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

response_clarification, missing_field:text

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

## Case 04007

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_05`

### ผู้ใช้ถามอะไร

```text
Demo rule Indigo Lotus What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 5: for Free learning activity, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_05"
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

response_clarification, missing_field:text

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

## Case 04009

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_05`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Indigo Lotus Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 5: for Free learning activity, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_05'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_05"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04010

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_05`

### ผู้ใช้ถามอะไร

```text
Demo rule Indigo Lotus What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 5: for Free learning activity, follow decision allowed; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_05"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04012

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_06`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ปะการัง ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_06"
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

response_clarification, missing_field:text

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

## Case 04014

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_06`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ปะการัง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_06"
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

response_clarification, missing_field:text

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

## Case 04017

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_06`

### ผู้ใช้ถามอะไร

```text
Demo rule Coral What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 6: for Food in the zone, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_06"
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

response_clarification, missing_field:text

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

## Case 04019

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_06`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Coral Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 6: for Food in the zone, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_06'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_06"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04020

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_06`

### ผู้ใช้ถามอะไร

```text
Demo rule Coral What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 6: for Food in the zone, follow decision prohibited; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_06"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04022

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_07`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ตะวันอ่อน ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_07"
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

response_clarification, missing_field:text

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

## Case 04024

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_07`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ตะวันอ่อน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_07"
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

response_clarification, missing_field:text

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

## Case 04027

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_07`

### ผู้ใช้ถามอะไร

```text
Demo rule Gentle Sun What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 7: for Team roster, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_07"
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

response_clarification, missing_field:text

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

## Case 04029

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_07`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Gentle Sun Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 7: for Team roster, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_07'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_07"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04030

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_07`

### ผู้ใช้ถามอะไร

```text
Demo rule Gentle Sun What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 7: for Team roster, follow decision required; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_07"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04032

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_08`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ฟ้าหลังฝน ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_08"
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

response_clarification, missing_field:text

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

## Case 04034

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_08`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ฟ้าหลังฝน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_08"
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

response_clarification, missing_field:text

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

## Case 04037

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_08`

### ผู้ใช้ถามอะไร

```text
Demo rule After Rain What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 8: for Player accounts, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_08"
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

response_clarification, missing_field:text

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

## Case 04039

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_08`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule After Rain Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 8: for Player accounts, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_08'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_08"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04040

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_08`

### ผู้ใช้ถามอะไร

```text
Demo rule After Rain What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 8: for Player accounts, follow decision conditional; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_08"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04042

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_09`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ลมทะเล ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_09"
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

response_clarification, missing_field:text

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

## Case 04044

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_09`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ลมทะเล ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_09"
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

response_clarification, missing_field:text

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

## Case 04047

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_09`

### ผู้ใช้ถามอะไร

```text
Demo rule Sea Breeze What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 9: for Group reservations, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_09"
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

response_clarification, missing_field:text

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

## Case 04049

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_09`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Sea Breeze Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 9: for Group reservations, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_09'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_09"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04050

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_09`

### ผู้ใช้ถามอะไร

```text
Demo rule Sea Breeze What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 9: for Group reservations, follow decision required; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_09"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04052

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_10`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ห้องสมุดดาว ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_10"
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

response_clarification, missing_field:text

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

## Case 04054

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_10`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ห้องสมุดดาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_10"
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

response_clarification, missing_field:text

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

## Case 04057

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_10`

### ผู้ใช้ถามอะไร

```text
Demo rule Star Library What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 10: for Volume adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_10"
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

response_clarification, missing_field:text

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

## Case 04059

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_10`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Star Library Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 10: for Volume adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_10'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_10"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04060

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_10`

### ผู้ใช้ถามอะไร

```text
Demo rule Star Library What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 10: for Volume adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_10"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04062

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_11`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ต้นเฟิร์น ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_11"
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

response_clarification, missing_field:text

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

## Case 04064

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_11`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ต้นเฟิร์น ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_11"
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

response_clarification, missing_field:text

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

## Case 04067

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_11`

### ผู้ใช้ถามอะไร

```text
Demo rule Fern What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 11: for Personal devices, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_11"
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

response_clarification, missing_field:text

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

## Case 04069

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_11`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Fern Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 11: for Personal devices, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_11'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_11"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04070

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_11`

### ผู้ใช้ถามอะไร

```text
Demo rule Fern What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 11: for Personal devices, follow decision allowed; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_11"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04072

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_12`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง ทองทราย ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_12"
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

response_clarification, missing_field:text

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

## Case 04074

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_12`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง ทองทราย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_12"
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

response_clarification, missing_field:text

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

## Case 04077

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_12`

### ผู้ใช้ถามอะไร

```text
Demo rule Sand Gold What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 12: for Safety boundary, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_12"
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

response_clarification, missing_field:text

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

## Case 04079

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_12`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Sand Gold Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 12: for Safety boundary, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_12'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_12"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04080

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_12`

### ผู้ใช้ถามอะไร

```text
Demo rule Sand Gold What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 12: for Safety boundary, follow decision required; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_12"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04082

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_13`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง จันทร์เสี้ยว ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_13"
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

response_clarification, missing_field:text

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

## Case 04084

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_13`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง จันทร์เสี้ยว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_13"
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

response_clarification, missing_field:text

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

## Case 04087

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_13`

### ผู้ใช้ถามอะไร

```text
Demo rule Crescent What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 13: for Practice before starting, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_13"
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

response_clarification, missing_field:text

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

## Case 04089

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_13`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Crescent Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 13: for Practice before starting, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_13'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_13"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04090

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_13`

### ผู้ใช้ถามอะไร

```text
Demo rule Crescent What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 13: for Practice before starting, follow decision allowed; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_13"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04092

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_14`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง แสงอรุณ ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_14"
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

response_clarification, missing_field:text

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

## Case 04094

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_14`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง แสงอรุณ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_14"
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

response_clarification, missing_field:text

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

## Case 04097

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_14`

### ผู้ใช้ถามอะไร

```text
Demo rule Dawn Light What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 14: for Photography, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_14"
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

response_clarification, missing_field:text

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

## Case 04099

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_14`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Dawn Light Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 14: for Photography, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_14'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_14"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04100

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_14`

### ผู้ใช้ถามอะไร

```text
Demo rule Dawn Light What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 14: for Photography, follow decision conditional; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_14"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04102

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_15`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง กิ่งไผ่ ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_15"
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

response_clarification, missing_field:text

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

## Case 04104

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_15`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง กิ่งไผ่ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_15"
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

response_clarification, missing_field:text

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

## Case 04107

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_15`

### ผู้ใช้ถามอะไร

```text
Demo rule Bamboo What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 15: for Software installation, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_15"
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

response_clarification, missing_field:text

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

## Case 04109

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_15`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Bamboo Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 15: for Software installation, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_15'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_15"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04110

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_15`

### ผู้ใช้ถามอะไร

```text
Demo rule Bamboo What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 15: for Software installation, follow decision prohibited; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_15"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04112

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_16`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง เมฆขาว ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_16"
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

response_clarification, missing_field:text

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

## Case 04114

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_16`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง เมฆขาว ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_16"
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

response_clarification, missing_field:text

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

## Case 04117

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_16`

### ผู้ใช้ถามอะไร

```text
Demo rule White Cloud What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 16: for Accessibility assistance, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_16"
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

response_clarification, missing_field:text

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

## Case 04119

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_16`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule White Cloud Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 16: for Accessibility assistance, follow decision allowed; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_16'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_16"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04120

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_16`

### ผู้ใช้ถามอะไร

```text
Demo rule White Cloud What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 16: for Accessibility assistance, follow decision allowed; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_16"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04122

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_17`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง มะลิ ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_17"
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

response_clarification, missing_field:text

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

## Case 04124

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_17`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง มะลิ ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_17"
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

response_clarification, missing_field:text

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

## Case 04127

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_17`

### ผู้ใช้ถามอะไร

```text
Demo rule Jasmine What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 17: for Changing dates, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_17"
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

response_clarification, missing_field:text

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

## Case 04129

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_17`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Jasmine Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 17: for Changing dates, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_17'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_17"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04130

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_17`

### ผู้ใช้ถามอะไร

```text
Demo rule Jasmine What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 17: for Changing dates, follow decision conditional; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_17"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04132

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_18`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง กระเบน ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_18"
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

response_clarification, missing_field:text

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

## Case 04134

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_18`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง กระเบน ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_18"
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

response_clarification, missing_field:text

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

## Case 04137

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_18`

### ผู้ใช้ถามอะไร

```text
Demo rule Ray What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 18: for Refund requests, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_18"
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

response_clarification, missing_field:text

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

## Case 04139

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_18`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Ray Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 18: for Refund requests, follow decision prohibited; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_18'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_18"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04140

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_18`

### ผู้ใช้ถามอะไร

```text
Demo rule Ray What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 18: for Refund requests, follow decision prohibited; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_18"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04142

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_19`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง แปะก๊วย ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_19"
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

response_clarification, missing_field:text

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

## Case 04144

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_19`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง แปะก๊วย ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_19"
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

response_clarification, missing_field:text

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

## Case 04147

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_19`

### ผู้ใช้ถามอะไร

```text
Demo rule Ginkgo What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 19: for Check-in proof, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_19"
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

response_clarification, missing_field:text

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

## Case 04149

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_19`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Ginkgo Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 19: for Check-in proof, follow decision required; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_19'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_19"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04150

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_19`

### ผู้ใช้ถามอะไร

```text
Demo rule Ginkgo What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 19: for Check-in proof, follow decision required; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_19"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04152

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_20`

### ผู้ใช้ถามอะไร

```text
ข้อการแข่งขันทดลอง รุ่งเรือง ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_20"
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

response_clarification, missing_field:text

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

## Case 04154

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_20`

### ผู้ใช้ถามอะไร

```text
แล้วข้อนี้กำหนดอะไร
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "ข้อการแข่งขันทดลอง รุ่งเรือง ขอรายละเอียด"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R06 — หัวข้อก่อนหน้ากับหัวข้อใหม่ยังไม่ผูกเป็น dialogue state**: context_query คืน record_ids เท่านั้น และ pending_fields สแกนคำในข้อความ user ก่อนหน้า ไม่มี typed pending slot; ที่ record ถูกแต่ field ว่างยังเป็น intent failure • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:101)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_20"
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

response_clarification, missing_field:text

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

## Case 04157

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** natural • **record ที่ควรตอบ:** `demo20_competition_rule_20`

### ผู้ใช้ถามอะไร

```text
Demo rule Radiance What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 20: for Result appeals, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_20"
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

response_clarification, missing_field:text

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

## Case 04159

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** followup • **record ที่ควรตอบ:** `demo20_competition_rule_20`

### ผู้ใช้ถามอะไร

```text
And What does this rule require?
```

ประวัติที่ส่งจริง:
```json
[
  {
    "role": "user",
    "content": "Demo rule Radiance Tell me about it"
  }
]
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 20: for Result appeals, follow decision conditional; exception requires written demo operator approval; not actual rules
```

### ทำไมได้คำตอบแบบนี้

เลือก record ['demo20_competition_rule_20'] และหัวข้อ ['summary']; field ของ target ที่ยังไม่มี obligation คือ ['text']. ข้อมูล gold มีอยู่ใน release เดียวกัน การมี evidence ของ field อื่นไม่ชดเชยส่วนที่ขาด

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
      "demo20_competition_rule_20"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
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
  "term_matches": [],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

### ทำไมคะแนนจึงตก/ผ่าน

missing_field:text

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

## Case 04160

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** multi_field • **record ที่ควรตอบ:** `demo20_competition_rule_20`

### ผู้ใช้ถามอะไร

```text
Demo rule Radiance What does the rule say and is its content complete?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`), สถานะความครบของข้อกติกา (`completeness`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 20: for Result appeals, follow decision conditional; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

### ทำไมได้คำตอบแบบนี้

หา demo20_competition_rule_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)
- **R05 — ถามหลายหัวข้อแต่ plan ไม่เก็บครบทุกหัวข้อ**: list ของ requested_fields เก็บเพียงหัวข้อที่ literal matcher พบ ไม่มีข้อผูกพันว่าทุกส่วนคำถามต้องถูก resolve จึงตอบบางส่วนแล้วจบ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_20"
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

response_clarification, missing_field:text, missing_field:completeness

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

## Case 04978

**หมวด:** competition_rule • **ภาษา:** th • **รูปแบบ:** old_control_natural • **record ที่ควรตอบ:** `demo_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
ตัวอย่าง ข้อกติกาการแข่งขัน 01 ข้อนี้กำหนดอะไร
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): กติกาสมมุติหัวข้อ เช็กอิน: แจ้งผู้ดูแลตัวอย่างก่อนเริ่มรอบ 01; ไม่ใช่กฎทางการของเกมหรือ PSU
```

### ทำไมได้คำตอบแบบนี้

หา demo_competition_rule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo_competition_rule_01"
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

response_clarification, missing_field:text

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture_source_demo_competition_rule_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional rule for Check-in: notify the demo operator before round 01; not an official game or PSU rule",
      "th": "กติกาสมมุติหัวข้อ เช็กอิน: แจ้งผู้ดูแลตัวอย่างก่อนเริ่มรอบ 01; ไม่ใช่กฎทางการของเกมหรือ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/records/competition_rule/demo_competition_rule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 04980

**หมวด:** competition_rule • **ภาษา:** en • **รูปแบบ:** old_control_natural • **record ที่ควรตอบ:** `demo_competition_rule_01`

### ผู้ใช้ถามอะไร

```text
Demo competition rule 01 What does this rule require?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: ข้อความข้อกติกาเต็ม (`text`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
ข้อความข้อกติกาเต็ม (text): Fictional rule for Check-in: notify the demo operator before round 01; not an official game or PSU rule
```

### ทำไมได้คำตอบแบบนี้

หา demo_competition_rule_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo_competition_rule_01"
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

response_clarification, missing_field:text

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "text": {
    "evidence_refs": [
      {
        "locator": "/values/text",
        "source_id": "fixture_source_demo_competition_rule_01"
      }
    ],
    "note": "ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA",
    "status": "known",
    "value": {
      "en": "Fictional rule for Check-in: notify the demo operator before round 01; not an official game or PSU rule",
      "th": "กติกาสมมุติหัวข้อ เช็กอิน: แจ้งผู้ดูแลตัวอย่างก่อนเริ่มรอบ 01; ไม่ใช่กฎทางการของเกมหรือ PSU"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_240_20261012/records/competition_rule/demo_competition_rule_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

