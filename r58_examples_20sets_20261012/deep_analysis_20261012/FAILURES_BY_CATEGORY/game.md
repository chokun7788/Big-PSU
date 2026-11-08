# ภาคผนวกเคสไม่ผ่าน — game / 42 เคส

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

อ่านคำตอบเดิมเทียบค่าที่ควรตอบ พร้อม plan, lexical triggers, สาเหตุ และ code links ทุกเคส ไม่ใช้เป็นข้อมูลศูนย์จริง

รายการเคส: [Case 01083](#case-01083), [Case 01089](#case-01089), [Case 01095](#case-01095), [Case 01098](#case-01098), [Case 01101](#case-01101), [Case 01107](#case-01107), [Case 01113](#case-01113), [Case 01119](#case-01119), [Case 01125](#case-01125), [Case 01131](#case-01131), [Case 01137](#case-01137), [Case 01143](#case-01143), [Case 01149](#case-01149), [Case 01155](#case-01155), [Case 01161](#case-01161), [Case 01167](#case-01167), [Case 01173](#case-01173), [Case 01179](#case-01179), [Case 01185](#case-01185), [Case 01191](#case-01191), [Case 01197](#case-01197), [Case 01203](#case-01203), [Case 01209](#case-01209), [Case 01215](#case-01215), [Case 01221](#case-01221), [Case 01227](#case-01227), [Case 01233](#case-01233), [Case 01239](#case-01239), [Case 01245](#case-01245), [Case 01251](#case-01251), [Case 01257](#case-01257), [Case 01263](#case-01263), [Case 01269](#case-01269), [Case 01275](#case-01275), [Case 01281](#case-01281), [Case 01287](#case-01287), [Case 01293](#case-01293), [Case 01299](#case-01299), [Case 01305](#case-01305), [Case 01311](#case-01311), [Case 01317](#case-01317), [Case 01320](#case-01320)

## Case 01083

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_01`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ดาวเหนือ เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ปลูกต้นไม้ร่วมกันและแบ่งหน้าที่เก็บเมล็ด; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_01"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Plant together and split seed collecting tasks; follow the demonstration controls",
      "th": "ปลูกต้นไม้ร่วมกันและแบ่งหน้าที่เก็บเมล็ด; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01089

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_01`

### ผู้ใช้ถามอะไร

```text
Fictional game Northstar What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Plant together and split seed collecting tasks; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_01 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_01"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_01"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Plant together and split seed collecting tasks; follow the demonstration controls",
      "th": "ปลูกต้นไม้ร่วมกันและแบ่งหน้าที่เก็บเมล็ด; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_01.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01095

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_02`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ดาวเหนือ พลัส เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_02"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Two players coordinate buttons to fly through rings; follow the demonstration controls",
      "th": "ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01098

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_game_02`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ดาาวเหนือ พลัส เล่นยังไง
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
[CommonAnswerer returned None]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

original CommonAnswerer คืน None ที่บรรทัด 138; name_unresolved_and_kind_fallback_not_applicable; ไม่มี fallback legacy ถูกเรียกใน core test นี้

- **R08 — fuzzy ปฏิเสธชื่อที่ยังคลุมเครือ**: SequenceMatcher ต้องได้ >=0.88 และอันดับแรกห่างอันดับสอง >=0.06 นี่เป็น guard เลือกผิดรายการ ไม่ใช่ probability; ดู score จริงใน replay ก่อนตัดสินลด threshold • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:88)

แผนและ obligations ที่อยู่ใน log:
```json
null
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "how_to_play",
      "term": "เล่นยังไง",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

การตรวจ return branch/คะแนน fuzzy ด้วยตัวเดิม:
```json
{
  "id": "01098",
  "question": "เกมสมมุติ ดาาวเหนือ พลัส เล่นยังไง",
  "style": "name_repeat",
  "lang": "th",
  "kind_expected": "game",
  "record_expected": "demo20_game_02",
  "history": [],
  "replayed_none": true,
  "observed": {
    "return_line": 138,
    "locals": {
      "q": "เกมสมมุติ ดาาวเหนือ พลัส เล่นยังไง",
      "ids": [],
      "method": "none",
      "kind": null,
      "requested": [
        "how_to_play"
      ],
      "broad": false
    }
  },
  "diagnostic": "name_unresolved_and_kind_fallback_not_applicable",
  "fuzzy": {
    "threshold": 0.88,
    "margin_required": 0.06,
    "accepted_candidates": 2,
    "best_two_margin": 0.005750431282346091,
    "top5": [
      {
        "record_id": "demo20_game_02",
        "score": 0.9787234042553191,
        "alias": "เกมสมมุติ ดาวเหนือ พลัส",
        "span": "เกมสมมุติ ดาาวเหนือ พลัส"
      },
      {
        "record_id": "demo20_game_01",
        "score": 0.972972972972973,
        "alias": "เกมสมมุติ ดาวเหนือ",
        "span": "เกมสมมุติ ดาาวเหนือ"
      },
      {
        "record_id": "demo20_game_16",
        "score": 0.7741935483870968,
        "alias": "เกมสมมุติ เมฆขาว",
        "span": "เกมสมมุติ ดาาวเ"
      },
      {
        "record_id": "demo20_person_02",
        "score": 0.7547169811320755,
        "alias": "ผู้ดูแลสมมุติ ดาวเหนือ พลัส",
        "span": "เกมสมมุติ ดาาวเหนือ พลัส เ"
      },
      {
        "record_id": "demo20_game_07",
        "score": 0.7428571428571429,
        "alias": "เกมสมมุติ ทีมดาวตก",
        "span": "เกมสมมุติ ดาาวเหน"
      }
    ],
    "expected_record_score": 0.9787234042553191,
    "rejection": "margin_below_0.06"
  }
}
```

### ทำไมคะแนนจึงตก/ผ่าน

no_common_answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Two players coordinate buttons to fly through rings; follow the demonstration controls",
      "th": "ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01101

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_02`

### ผู้ใช้ถามอะไร

```text
Fictional game Northstar Plus What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Two players coordinate buttons to fly through rings; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_02 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_02"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_02"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Two players coordinate buttons to fly through rings; follow the demonstration controls",
      "th": "ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_02.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01107

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_03`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ละอองฝน เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ใช้มือเสมือนจัดแสงนำทางเรือ; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_03"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Use motion inputs to arrange lights guiding ships; follow the demonstration controls",
      "th": "ใช้มือเสมือนจัดแสงนำทางเรือ; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01113

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_03`

### ผู้ใช้ถามอะไร

```text
Fictional game Drizzle What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Use motion inputs to arrange lights guiding ships; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_03 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_03"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_03"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Use motion inputs to arrange lights guiding ships; follow the demonstration controls",
      "th": "ใช้มือเสมือนจัดแสงนำทางเรือ; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_03.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01119

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_04`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ สายหมอก เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ฝึกเบรกและเข้าโค้งด้วยพวงมาลัย; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_04"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Practise braking and cornering with a wheel; follow the demonstration controls",
      "th": "ฝึกเบรกและเข้าโค้งด้วยพวงมาลัย; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01125

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_04`

### ผู้ใช้ถามอะไร

```text
Fictional game Mist What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Practise braking and cornering with a wheel; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_04 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_04"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_04"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Practise braking and cornering with a wheel; follow the demonstration controls",
      "th": "ฝึกเบรกและเข้าโค้งด้วยพวงมาลัย; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_04.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01131

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_05`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ บัวสีคราม เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): จัดบล็อกตามตัวอย่างโดยไม่มีการแข่งขัน; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_05"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Arrange blocks to match examples without competing; follow the demonstration controls",
      "th": "จัดบล็อกตามตัวอย่างโดยไม่มีการแข่งขัน; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01137

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_05`

### ผู้ใช้ถามอะไร

```text
Fictional game Indigo Lotus What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Arrange blocks to match examples without competing; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_05 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_05"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_05"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Arrange blocks to match examples without competing; follow the demonstration controls",
      "th": "จัดบล็อกตามตัวอย่างโดยไม่มีการแข่งขัน; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_05.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01143

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_06`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ปะการัง เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ร่วมกันวางสะพานให้ตัวละครข้ามแม่น้ำ; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_06"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Place bridges together to cross a river; follow the demonstration controls",
      "th": "ร่วมกันวางสะพานให้ตัวละครข้ามแม่น้ำ; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01149

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_06`

### ผู้ใช้ถามอะไร

```text
Fictional game Coral What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Place bridges together to cross a river; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_06 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_06"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_06"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Place bridges together to cross a river; follow the demonstration controls",
      "th": "ร่วมกันวางสะพานให้ตัวละครข้ามแม่น้ำ; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_06.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01155

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_07`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ตะวันอ่อน เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ทีมสองฝั่งแข่งขันเก็บจุดพลังงาน; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_07"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Two teams compete to collect energy points; follow the demonstration controls",
      "th": "ทีมสองฝั่งแข่งขันเก็บจุดพลังงาน; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01161

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_07`

### ผู้ใช้ถามอะไร

```text
Fictional game Gentle Sun What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Two teams compete to collect energy points; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_07 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_07"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_07"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Two teams compete to collect energy points; follow the demonstration controls",
      "th": "ทีมสองฝั่งแข่งขันเก็บจุดพลังงาน; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_07.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01167

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_08`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ฟ้าหลังฝน เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ส่งจดหมายให้ครบโดยเลือกเส้นทางสั้น; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_08"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Deliver letters by selecting short routes; follow the demonstration controls",
      "th": "ส่งจดหมายให้ครบโดยเลือกเส้นทางสั้น; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01173

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_08`

### ผู้ใช้ถามอะไร

```text
Fictional game After Rain What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Deliver letters by selecting short routes; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_08 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_08"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_08"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Deliver letters by selecting short routes; follow the demonstration controls",
      "th": "ส่งจดหมายให้ครบโดยเลือกเส้นทางสั้น; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_08.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01179

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_09`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ลมทะเล เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): จัดคิวเรือโดยเล่นเป็นกลุ่มใหญ่; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_09"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Arrange vessel queues as a large group; follow the demonstration controls",
      "th": "จัดคิวเรือโดยเล่นเป็นกลุ่มใหญ่; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01185

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_09`

### ผู้ใช้ถามอะไร

```text
Fictional game Sea Breeze What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Arrange vessel queues as a large group; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_09 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_09"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_09"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Arrange vessel queues as a large group; follow the demonstration controls",
      "th": "จัดคิวเรือโดยเล่นเป็นกลุ่มใหญ่; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_09.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01191

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_10`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ห้องสมุดดาว เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): กดปุ่มตามสีและจังหวะเพื่อสร้างเพลง; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_10"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Press to match colours and rhythms and create music; follow the demonstration controls",
      "th": "กดปุ่มตามสีและจังหวะเพื่อสร้างเพลง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01197

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_10`

### ผู้ใช้ถามอะไร

```text
Fictional game Star Library What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Press to match colours and rhythms and create music; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_10 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_10"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_10"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Press to match colours and rhythms and create music; follow the demonstration controls",
      "th": "กดปุ่มตามสีและจังหวะเพื่อสร้างเพลง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_10.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01203

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_11`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ต้นเฟิร์น เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): หาทางออกโดยบอกเส้นทางให้เพื่อนฟัง; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_11"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Find an exit by describing paths to teammates; follow the demonstration controls",
      "th": "หาทางออกโดยบอกเส้นทางให้เพื่อนฟัง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01209

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_11`

### ผู้ใช้ถามอะไร

```text
Fictional game Fern What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Find an exit by describing paths to teammates; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_11 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_11"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_11"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Find an exit by describing paths to teammates; follow the demonstration controls",
      "th": "หาทางออกโดยบอกเส้นทางให้เพื่อนฟัง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_11.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01215

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_12`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ ทองทราย เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): หยิบวัตถุเสมือนประกอบเครื่องจักร; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_12"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Assemble virtual machines using motion inputs; follow the demonstration controls",
      "th": "หยิบวัตถุเสมือนประกอบเครื่องจักร; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01221

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_12`

### ผู้ใช้ถามอะไร

```text
Fictional game Sand Gold What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Assemble virtual machines using motion inputs; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_12 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_12"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_12"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Assemble virtual machines using motion inputs; follow the demonstration controls",
      "th": "หยิบวัตถุเสมือนประกอบเครื่องจักร; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_12.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01227

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_13`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ จันทร์เสี้ยว เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ควบคุมรถหลายคันให้วิ่งถึงปลายทาง; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_13"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Steer a convoy to its destination; follow the demonstration controls",
      "th": "ควบคุมรถหลายคันให้วิ่งถึงปลายทาง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01233

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_13`

### ผู้ใช้ถามอะไร

```text
Fictional game Crescent What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Steer a convoy to its destination; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_13 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_13"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_13"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Steer a convoy to its destination; follow the demonstration controls",
      "th": "ควบคุมรถหลายคันให้วิ่งถึงปลายทาง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_13.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01239

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_14`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ แสงอรุณ เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): แบ่งหน้าที่ทำอาหารสมมุติให้ทันเวลา; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_14"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Split tasks to prepare fictional meals on time; follow the demonstration controls",
      "th": "แบ่งหน้าที่ทำอาหารสมมุติให้ทันเวลา; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01245

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_14`

### ผู้ใช้ถามอะไร

```text
Fictional game Dawn Light What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Split tasks to prepare fictional meals on time; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_14 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_14"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_14"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Split tasks to prepare fictional meals on time; follow the demonstration controls",
      "th": "แบ่งหน้าที่ทำอาหารสมมุติให้ทันเวลา; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_14.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01251

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_15`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ กิ่งไผ่ เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ผลัดกันแก้ปริศนาและบันทึกรหัส; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_15"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Take turns solving puzzles and recording codes; follow the demonstration controls",
      "th": "ผลัดกันแก้ปริศนาและบันทึกรหัส; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01257

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_15`

### ผู้ใช้ถามอะไร

```text
Fictional game Bamboo What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Take turns solving puzzles and recording codes; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_15 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_15"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_15"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Take turns solving puzzles and recording codes; follow the demonstration controls",
      "th": "ผลัดกันแก้ปริศนาและบันทึกรหัส; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_15.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01263

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_16`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ เมฆขาว เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ฟังสัญญาณเสียงและเลือกตำแหน่งบนบันได; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_16"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Listen to audio cues and select ladder positions; follow the demonstration controls",
      "th": "ฟังสัญญาณเสียงและเลือกตำแหน่งบนบันได; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01269

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_16`

### ผู้ใช้ถามอะไร

```text
Fictional game White Cloud What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Listen to audio cues and select ladder positions; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_16 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_16"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_16"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Listen to audio cues and select ladder positions; follow the demonstration controls",
      "th": "ฟังสัญญาณเสียงและเลือกตำแหน่งบนบันได; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_16.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01275

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_17`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ มะลิ เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): ต่อชิ้นส่วนเมืองแล้วแลกเปลี่ยนทรัพยากร; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_17"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Build a town and trade resources; follow the demonstration controls",
      "th": "ต่อชิ้นส่วนเมืองแล้วแลกเปลี่ยนทรัพยากร; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01281

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_17`

### ผู้ใช้ถามอะไร

```text
Fictional game Jasmine What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Build a town and trade resources; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_17 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_17"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_17"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Build a town and trade resources; follow the demonstration controls",
      "th": "ต่อชิ้นส่วนเมืองแล้วแลกเปลี่ยนทรัพยากร; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_17.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01287

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_18`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ กระเบน เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): เลือกคำสั่งนำดาวเทียมกลับสถานี; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_18"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Choose commands to guide a satellite back; follow the demonstration controls",
      "th": "เลือกคำสั่งนำดาวเทียมกลับสถานี; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01293

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_18`

### ผู้ใช้ถามอะไร

```text
Fictional game Ray What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Choose commands to guide a satellite back; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_18 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_18"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_18"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Choose commands to guide a satellite back; follow the demonstration controls",
      "th": "เลือกคำสั่งนำดาวเทียมกลับสถานี; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_18.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01299

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_19`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ แปะก๊วย เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): รวมกลุ่มเก็บเบาะแสและสรุปเส้นทาง; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_19"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Collect clues as a group and agree on a route; follow the demonstration controls",
      "th": "รวมกลุ่มเก็บเบาะแสและสรุปเส้นทาง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01305

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_19`

### ผู้ใช้ถามอะไร

```text
Fictional game Ginkgo What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Collect clues as a group and agree on a route; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_19 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_19"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_19"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Collect clues as a group and agree on a route; follow the demonstration controls",
      "th": "รวมกลุ่มเก็บเบาะแสและสรุปเส้นทาง; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_19.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01311

**หมวด:** game • **ภาษา:** th • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_20`

### ผู้ใช้ถามอะไร

```text
เกมสมมุติ รุ่งเรือง เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): จับคู่ผู้เล่นฝึกกลยุทธ์โดยไม่จัดอันดับ; ใช้คำสั่งตามชุดควบคุมทดลอง
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_20"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Pair players for unranked strategy practice; follow the demonstration controls",
      "th": "จับคู่ผู้เล่นฝึกกลยุทธ์โดยไม่จัดอันดับ; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01317

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** paraphrase • **record ที่ควรตอบ:** `demo20_game_20`

### ผู้ใช้ถามอะไร

```text
Fictional game Radiance What do I do to play this game?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Pair players for unranked strategy practice; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

หา demo20_game_20 ถูกแล้ว แต่ requested_fields=[]; ชื่อช่องที่ต้องอ่านยังไม่ได้เลือก จึงเข้า clarification; ข้อความถามกลับถูก hardcode และไม่เจาะหมวด

- **R01 — สำนวนยังไม่ถูกแปลงเป็นชื่อช่องข้อมูล**: field_requests ใช้ 13 กลุ่ม keyword กับการเทียบ key/label แบบ literal จึงยังไม่เข้าใจทุกสำนวนของ 122 field keys; หา record เจอไม่ได้แปลว่าเลือก field ได้ • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:90)

แผนและ obligations ที่อยู่ใน log:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_20"
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

response_clarification, missing_field:how_to_play

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Pair players for unranked strategy practice; follow the demonstration controls",
      "th": "จับคู่ผู้เล่นฝึกกลยุทธ์โดยไม่จัดอันดับ; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

## Case 01320

**หมวด:** game • **ภาษา:** en • **รูปแบบ:** name_repeat • **record ที่ควรตอบ:** `demo20_game_20`

### ผู้ใช้ถามอะไร

```text
Fictional gaame Radiance How do I play it?
```

สิ่งที่ผู้ใช้ควรได้รับตาม fixture: วิธีเล่น (`how_to_play`)

### คำตอบที่ระบบส่งจริง

```text
[CommonAnswerer returned None]
```

### คำตอบที่ควรได้จากชุดตัวอย่าง

คำตอบต่อไปนี้เรียบเรียงจาก field ที่กำหนดไว้ ไม่ใช่ข้อเท็จจริงของ PSU และควรแนบ evidence ของ field เหล่านี้:

```text
วิธีเล่น (how_to_play): Pair players for unranked strategy practice; follow the demonstration controls
```

### ทำไมได้คำตอบแบบนี้

original CommonAnswerer คืน None ที่บรรทัด 138; name_unresolved_and_kind_fallback_not_applicable; ไม่มี fallback legacy ถูกเรียกใน core test นี้

- **R08 — fuzzy ปฏิเสธชื่อที่ยังคลุมเครือ**: SequenceMatcher ต้องได้ >=0.88 และอันดับแรกห่างอันดับสอง >=0.06 นี่เป็น guard เลือกผิดรายการ ไม่ใช่ probability; ดู score จริงใน replay ก่อนตัดสินลด threshold • [app/knowledge/common/answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/app/knowledge/common/answer.py:88)

แผนและ obligations ที่อยู่ใน log:
```json
null
```

คำที่ matcher เดิมจับได้ (คำนวณจาก q และ TERMS/catalog เดิม ไม่ได้เป็น log ที่เคยบันทึกไว้):
```json
{
  "term_matches": [
    {
      "field": "how_to_play",
      "term": "how do i play",
      "offset": 25,
      "inside_named_entity": false
    },
    {
      "field": "steps",
      "term": "how do",
      "offset": 25,
      "inside_named_entity": false
    }
  ],
  "catalog_matches": [],
  "normalization": "NFC + casefold + collapse spaces only"
}
```

การตรวจ return branch/คะแนน fuzzy ด้วยตัวเดิม:
```json
{
  "id": "01320",
  "question": "Fictional gaame Radiance How do I play it?",
  "style": "name_repeat",
  "lang": "en",
  "kind_expected": "game",
  "record_expected": "demo20_game_20",
  "history": [],
  "replayed_none": true,
  "observed": {
    "return_line": 138,
    "locals": {
      "q": "Fictional gaame Radiance How do I play it?",
      "ids": [],
      "method": "none",
      "kind": null,
      "requested": [
        "how_to_play",
        "steps"
      ],
      "broad": false
    }
  },
  "diagnostic": "name_unresolved_and_kind_fallback_not_applicable",
  "fuzzy": {
    "threshold": 0.88,
    "margin_required": 0.06,
    "accepted_candidates": 2,
    "best_two_margin": 0.0342789598108747,
    "top5": [
      {
        "record_id": "demo20_game_20",
        "score": 0.9787234042553191,
        "alias": "fictional game radiance",
        "span": "fictional gaame radiance"
      },
      {
        "record_id": "demo20_game_18",
        "score": 0.9444444444444444,
        "alias": "fictional game ray",
        "span": "fictional gaame ra"
      },
      {
        "record_id": "demo20_game_06",
        "score": 0.8717948717948718,
        "alias": "fictional game coral",
        "span": "fictional gaame rad"
      },
      {
        "record_id": "demo20_game_11",
        "score": 0.8648648648648649,
        "alias": "fictional game fern",
        "span": "fictional gaame ra"
      },
      {
        "record_id": "demo20_game_04",
        "score": 0.8205128205128205,
        "alias": "fictional game mist",
        "span": "fictional gaame radi"
      }
    ],
    "expected_record_score": 0.9787234042553191,
    "rejection": "margin_below_0.06"
  }
}
```

### ทำไมคะแนนจึงตก/ผ่าน

no_common_answer

สถานะและค่าที่เป็น ground truth พร้อม evidence refs:
```json
{
  "how_to_play": {
    "evidence_refs": [
      {
        "locator": "/values/how_to_play",
        "source_id": "fixture20_demo20_game_20"
      }
    ],
    "note": "ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION",
    "status": "known",
    "value": {
      "en": "Pair players for unranked strategy practice; follow the demonstration controls",
      "th": "จับคู่ผู้เล่นฝึกกลยุทธ์โดยไม่จัดอันดับ; ใช้คำสั่งตามชุดควบคุมทดลอง"
    }
  }
}
```

[record JSON เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_20.json)

การแก้สำหรับเคสนี้ต้องแก้การตีความ/เลือก field/guard ตามรหัสสาเหตุข้างบน ไม่ต้องให้เจ้าของเปลี่ยนค่า fixture เพื่อให้ตอบผ่าน; การยืนยันข้อมูลจริงและภาษาเป็นคนละขั้นตอน

