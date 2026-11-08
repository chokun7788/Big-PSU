# data/eval/competition_content_contract_r27_320_20261001.json

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 285/320 | 35 | 0 | 9 |

## ตัวอย่าง legacy_offline: 1166c3d0e8cb781ccec82688b55231d587828dad1e548a8939614a12d21a1f66

คำถาม: กติกกา CS2 ใช้เวอร์ชันเกมอะไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-cs2-version-th-2","anchor":"cs2-version-th","locale":"th","game":"cs2","question":"กติกกา CS2 ใช้เวอร์ชันเกมอะไร","required_clauses":["2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด"],"source_id":"competition_rules_cs2_psu_phuket_2026_s05_c01","source_sha256":"ba967cd89a88ae836d050f8abbe816aa69c3d04c09bfdcc02cc1433a9ba54210","status":"answer","first_clause":true,"mutation":"task_typo","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:source_operation_game_list / games / 0.98

ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The  … [ย่อจาก1,357ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route_mismatch","missing_complete_clause:2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด","first_line_off_topic","wrong_game_evidence"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: legacy_offline\RESULTS.jsonl record1=959

## ตัวอย่าง legacy_offline: 67d84999e2b28ba6e5986628893478ffd2e38262e3e62776aa966489914c9580

คำถาม: Which game version do the CS2 tournamment ruls use?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-cs2-version-en-2","anchor":"cs2-version-en","locale":"en","game":"cs2","question":"Which game version do the CS2 tournamment ruls use?","required_clauses":["The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited."],"source_id":"competition_rules_cs2_psu_phuket_2026_s05_c01","source_sha256":"ba967cd89a88ae836d050f8abbe816aa69c3d04c09bfdcc02cc1433a9ba54210","status":"answer","first_clause":true,"mutation":"task_typo","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:user_service_facts / clarification / 0.98

There is no live verification of the game versions on the machines, so the latest update cannot be confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["route_mismatch","missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.","first_line_off_topic","wrong_game_evidence"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: legacy_offline\RESULTS.jsonl record1=962
| common_offline | 17/320 | 303 | 0 | 300 |

## ตัวอย่าง common_offline: c0538500497208e3fde956238ecf0c02be4266b6ecb3caf388e59b002f08ea9f

คำถาม: กติกาแข่งขันมีอะไรบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-safe-no-game-th","anchor":"safe-no-game-th","locale":"th","question":"กติกาแข่งขันมีอะไรบ้าง","status":"clarification","required_clauses":[],"first_clause":false,"mutation":"control"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**ภาพรวมเอกสาร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]
• หัวข้อกติกา: ภาพรวมเอกสาร [S2]
• เลขข้อจากเอกสารเดิม: 1 [S3]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**6. ข้อจำกัด**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 6. ข้อจำกัด [S4]
• หัวข้อกติกา: 6. ข้อจำกัด [S5]
• เลขข้อจากเอกสารเดิม: 10 [S6]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]
• หัวข้อกติกา: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]
• เลขข้อจากเอกสารเดิม: 11 [S9]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]
• หัวข้อกติกา: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]
• เลขข้อจากเอกสารเดิม: 12 [S12]
• ข้อความข้อนี้ครบหรือถูกตัด: ยังไม่มีข้อมูลยืนยัน

**3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**
• ข้อคว … [ย่อจาก51,019ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["outcome_mismatch","route_mismatch"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026",
    "competition_competition_rules_tekken8_psu_esports",
    "competition_competition_rules_valorant_psu_phuket_2026",
    "competition_competition_rules_rov_blueket_2025_men"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "none",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_offline\RESULTS.jsonl record1=912

## ตัวอย่าง common_offline: 341fa03d41432888cc6b632ef47f91e340f124869a848e2bbdc5459a1403c0b0

คำถาม: What is the Tekken 8 tournament minimum age?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-safe-age-en","anchor":"safe-age-en","locale":"en","question":"What is the Tekken 8 tournament minimum age?","status":"no_answer","required_clauses":[],"first_clause":false,"mutation":"control"}
```

Actual mode/category/confidence: pipeline:common_clarification / knowledge / 0.0

The requested topic is unclear. Which part of [Thai source] PSU Esports ปะทะมันส์ สนั่นจอ do you need: event name / rulebook release / coverage?

Failures: ["outcome_mismatch","route_mismatch"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_tekken8_psu_esports"
  ],
  "requested_fields": [],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [
    "what is the tournament minimum age"
  ],
  "semantic_plan_accepted": false
}
```

raw source: common_offline\RESULTS.jsonl record1=917
| legacy_llm | 285/320 | 35 | 0 | 9 |

## ตัวอย่าง legacy_llm: 1166c3d0e8cb781ccec82688b55231d587828dad1e548a8939614a12d21a1f66

คำถาม: กติกกา CS2 ใช้เวอร์ชันเกมอะไร

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-cs2-version-th-2","anchor":"cs2-version-th","locale":"th","game":"cs2","question":"กติกกา CS2 ใช้เวอร์ชันเกมอะไร","required_clauses":["2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด"],"source_id":"competition_rules_cs2_psu_phuket_2026_s05_c01","source_sha256":"ba967cd89a88ae836d050f8abbe816aa69c3d04c09bfdcc02cc1433a9ba54210","status":"answer","first_clause":true,"mutation":"task_typo","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:source_operation_game_list / games / 0.98

ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The  … [ย่อจาก1,357ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["route_mismatch","missing_complete_clause:2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด","first_line_off_topic","wrong_game_evidence"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=32

## ตัวอย่าง legacy_llm: 67d84999e2b28ba6e5986628893478ffd2e38262e3e62776aa966489914c9580

คำถาม: Which game version do the CS2 tournamment ruls use?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-cs2-version-en-2","anchor":"cs2-version-en","locale":"en","game":"cs2","question":"Which game version do the CS2 tournamment ruls use?","required_clauses":["The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited."],"source_id":"competition_rules_cs2_psu_phuket_2026_s05_c01","source_sha256":"ba967cd89a88ae836d050f8abbe816aa69c3d04c09bfdcc02cc1433a9ba54210","status":"answer","first_clause":true,"mutation":"task_typo","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:user_service_facts / clarification / 0.98

There is no live verification of the game versions on the machines, so the latest update cannot be confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["route_mismatch","missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.","first_line_off_topic","wrong_game_evidence"]

แผนที่เลือก:
```json
{
  "record_ids": null,
  "requested_fields": null,
  "all_fields": null,
  "method": null,
  "platform": null,
  "unresolved_clauses": null,
  "semantic_plan_accepted": null
}
```

raw source: model_matrix_cached\legacy_RESULTS.jsonl.gz record1=35
| common_llm | 46/320 | 274 | 0 | 268 |

## ตัวอย่าง common_llm: 316982845bf38a6da065973b87d6f257e3f4770a3c1a541de4443a2a2c31cc80

คำถาม: กติกา CS2 ฉบับนี้ใช้กับใครบ้าง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-cs2-scope-th-0","anchor":"cs2-scope-th","locale":"th","game":"cs2","question":"กติกา CS2 ฉบับนี้ใช้กับใครบ้าง","required_clauses":["1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket"],"source_id":"competition_rules_cs2_psu_phuket_2026_s04_c01","source_sha256":"80114f6fde3b5244569ffb7850f8f177337a9a318ed44914186af5c718fc6c6d","status":"answer","first_clause":true,"mutation":"clean","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:common_answer / knowledge / 0.8

**PSU Phuket CS2 2026 Tournament**
• เอกสารกติกาครบหรือมีเพียงบางส่วน: ยังไม่มีข้อมูลยืนยัน

Failures: ["route_mismatch","missing_complete_clause:1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket","first_line_off_topic","wrong_game_evidence"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "coverage"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=25

## ตัวอย่าง common_llm: 272f2e514d94ad7e13d8e32f70ee59b3ea30d8514b23942f4e498513cff33171

คำถาม: สอบถามหน่อยครับ กติกา CS2 ฉบับนี้ใช้กับใครบ้าง หน่อย

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"id":"R27-cs2-scope-th-1","anchor":"cs2-scope-th","locale":"th","game":"cs2","question":"สอบถามหน่อยครับ กติกา CS2 ฉบับนี้ใช้กับใครบ้าง หน่อย","required_clauses":["1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket"],"source_id":"competition_rules_cs2_psu_phuket_2026_s04_c01","source_sha256":"80114f6fde3b5244569ffb7850f8f177337a9a318ed44914186af5c718fc6c6d","status":"answer","first_clause":true,"mutation":"wrapper","review":"assistant source-clause contract; not organizer approved"}
```

Actual mode/category/confidence: pipeline:common_partial_answer / knowledge / 0.0

**PSU Phuket CS2 2026 Tournament**
• ประเภทหรือกลุ่มการแข่งขัน: ยังไม่มีข้อมูลยืนยัน
• ฉบับกติกาและวันที่: competition_rules_cs2_psu_phuket_2026 [S1]
• เอกสารกติกาครบหรือมีเพียงบางส่วน: ยังไม่มีข้อมูลยืนยัน

competition_id: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง

Failures: ["route_mismatch","missing_complete_clause:1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket","first_line_off_topic","validation_rejected","validation_rejected"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "competition_id",
    "division",
    "rulebook_release",
    "coverage"
  ],
  "all_fields": false,
  "method": "bounded_llm_schema_fields",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": true
}
```

raw source: model_matrix_cached\common_RESULTS.jsonl.gz record1=26
