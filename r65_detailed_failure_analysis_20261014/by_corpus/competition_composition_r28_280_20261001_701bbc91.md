# data/eval/competition_composition_r28_280_20261001.json

รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม

| รอบ | pass | fail | protocol-only | content/source/language/gate |
|---|---:|---:|---:|---:|
| legacy_offline | 265/280 | 15 | 0 | 15 |

## ตัวอย่าง legacy_offline: 7053ba2337ed5c86f8b15ce24efc447ac78caa6239d4a764c6a1908401528f73

คำถาม: กติกกา CS2 ประกาศสายล่วงหน้ากี่วันและมาสายเป็นยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"กติกกา CS2 ประกาศสายล่วงหน้ากี่วันและมาสายเป็นยังไง","clauses":["7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์"],"sources":["competition_rules_cs2_psu_phuket_2026_s15_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s15_c01":"e8cd893c7817cfc261bf0b10f845b2163be1141c04905b8bc974872008a17deb"},"kind":"single","id":"R28-cs2-bracket-th-2","anchor":"cs2-bracket","locale":"th","mutation":"task-typo","status":"answer"}
```

Actual mode/category/confidence: pipeline:user_service_facts / reservation / 0.98

กฎการจองที่บันทึกไว้เดิม: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน
https://esports.computing.psu.ac.th/

ยังไม่ได้ยืนยันเวลาผ่อนผันหรือข้อยกเว้นสำหรับการมาสาย 15 นาทีครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["wrong_category","missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์","first_line_off_topic","wrong_game_source"]

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

raw source: legacy_offline\RESULTS.jsonl record1=686

## ตัวอย่าง legacy_offline: 68b1dc040d6cc0b8f930e2f30e3650718bacb63ac56205e1dc0356830f1b84b3

คำถาม: Under CS2 tournamment ruls, may players use map or engine bugs?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"Under CS2 tournamment ruls, may players use map or engine bugs?","clauses":["Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification."],"sources":["competition_rules_cs2_psu_phuket_2026_s37_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s37_c01":"63ee9b7e8d210a8cdc1bd2cc3c12472b87d602b907379e91b93e8d75a3afa93c"},"kind":"single","id":"R28-cs2-bugs-en-2","anchor":"cs2-bugs","locale":"en","mutation":"task-typo","status":"answer"}
```

Actual mode/category/confidence: pipeline:user_service_facts / contact / 0.98

Studio map: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["wrong_category","missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification.","first_line_off_topic","wrong_game_source"]

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

raw source: legacy_offline\RESULTS.jsonl record1=695
| common_offline | 12/280 | 268 | 2 | 265 |

## ตัวอย่าง common_offline: 89f466c0f7eb04cfa5de64623bc149938d8cb1cc2453c55a6a82cbdb74c99e39

คำถาม: กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง","clauses":["1. รูปแบบทัวร์นาเมนต์ Single Elimination"],"sources":["competition_rules_cs2_psu_phuket_2026_s20_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s20_c01":"1339343b43374e1293d695f53415de6d06a32ce61c5f4d51802f6fc081f16f32"},"kind":"single","id":"R28-cs2-format-th-0","anchor":"cs2-format","locale":"th","mutation":"clean","status":"answer"}
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
• ข้อคว … [ย่อจาก20,408ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["wrong_category","first_line_off_topic"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_offline\RESULTS.jsonl record1=672

## ตัวอย่าง common_offline: 8cf54b3af4d34d3567de110806b196f9337e963df5994b69db499001eff149bc

คำถาม: สอบถามหน่อยครับ กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง ครับ

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"สอบถามหน่อยครับ กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง ครับ","clauses":["1. รูปแบบทัวร์นาเมนต์ Single Elimination"],"sources":["competition_rules_cs2_psu_phuket_2026_s20_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s20_c01":"1339343b43374e1293d695f53415de6d06a32ce61c5f4d51802f6fc081f16f32"},"kind":"single","id":"R28-cs2-format-th-1","anchor":"cs2-format","locale":"th","mutation":"polite","status":"answer"}
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
• ข้อคว … [ย่อจาก20,408ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["wrong_category","first_line_off_topic"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: common_offline\RESULTS.jsonl record1=673
| legacy_llm | 265/280 | 15 | 0 | 15 |

## ตัวอย่าง legacy_llm: 7053ba2337ed5c86f8b15ce24efc447ac78caa6239d4a764c6a1908401528f73

คำถาม: กติกกา CS2 ประกาศสายล่วงหน้ากี่วันและมาสายเป็นยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"กติกกา CS2 ประกาศสายล่วงหน้ากี่วันและมาสายเป็นยังไง","clauses":["7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์"],"sources":["competition_rules_cs2_psu_phuket_2026_s15_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s15_c01":"e8cd893c7817cfc261bf0b10f845b2163be1141c04905b8bc974872008a17deb"},"kind":"single","id":"R28-cs2-bracket-th-2","anchor":"cs2-bracket","locale":"th","mutation":"task-typo","status":"answer"}
```

Actual mode/category/confidence: pipeline:user_service_facts / reservation / 0.98

กฎการจองที่บันทึกไว้เดิม: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน
https://esports.computing.psu.ac.th/

ยังไม่ได้ยืนยันเวลาผ่อนผันหรือข้อยกเว้นสำหรับการมาสาย 15 นาทีครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["wrong_category","missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์","first_line_off_topic","wrong_game_source"]

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=686

## ตัวอย่าง legacy_llm: 68b1dc040d6cc0b8f930e2f30e3650718bacb63ac56205e1dc0356830f1b84b3

คำถาม: Under CS2 tournamment ruls, may players use map or engine bugs?

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"Under CS2 tournamment ruls, may players use map or engine bugs?","clauses":["Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification."],"sources":["competition_rules_cs2_psu_phuket_2026_s37_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s37_c01":"63ee9b7e8d210a8cdc1bd2cc3c12472b87d602b907379e91b93e8d75a3afa93c"},"kind":"single","id":"R28-cs2-bugs-en-2","anchor":"cs2-bugs","locale":"en","mutation":"task-typo","status":"answer"}
```

Actual mode/category/confidence: pipeline:user_service_facts / contact / 0.98

Studio map: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

Failures: ["wrong_category","missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification.","first_line_off_topic","wrong_game_source"]

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

raw source: model_matrix\legacy_RESULTS.jsonl.gz record1=695
| common_llm | 10/280 | 270 | 3 | 253 |

## ตัวอย่าง common_llm: 89f466c0f7eb04cfa5de64623bc149938d8cb1cc2453c55a6a82cbdb74c99e39

คำถาม: กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง","clauses":["1. รูปแบบทัวร์นาเมนต์ Single Elimination"],"sources":["competition_rules_cs2_psu_phuket_2026_s20_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s20_c01":"1339343b43374e1293d695f53415de6d06a32ce61c5f4d51802f6fc081f16f32"},"kind":"single","id":"R28-cs2-format-th-0","anchor":"cs2-format","locale":"th","mutation":"clean","status":"answer"}
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
• ข้อคว … [ย่อจาก20,408ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["wrong_category","first_line_off_topic"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix\common_RESULTS.jsonl.gz record1=672

## ตัวอย่าง common_llm: 8cf54b3af4d34d3567de110806b196f9337e963df5994b69db499001eff149bc

คำถาม: สอบถามหน่อยครับ กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง ครับ

Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):
```json
{"game":"cs2","question":"สอบถามหน่อยครับ กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง ครับ","clauses":["1. รูปแบบทัวร์นาเมนต์ Single Elimination"],"sources":["competition_rules_cs2_psu_phuket_2026_s20_c01"],"source_sha256":{"competition_rules_cs2_psu_phuket_2026_s20_c01":"1339343b43374e1293d695f53415de6d06a32ce61c5f4d51802f6fc081f16f32"},"kind":"single","id":"R28-cs2-format-th-1","anchor":"cs2-format","locale":"th","mutation":"polite","status":"answer"}
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
• ข้อคว … [ย่อจาก20,408ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]

Failures: ["wrong_category","first_line_off_topic"]

แผนที่เลือก:
```json
{
  "record_ids": [
    "competition_competition_rules_cs2_psu_phuket_2026"
  ],
  "requested_fields": [
    "text"
  ],
  "all_fields": false,
  "method": "exact",
  "platform": null,
  "unresolved_clauses": [],
  "semantic_plan_accepted": false
}
```

raw source: model_matrix\common_RESULTS.jsonl.gz record1=673
