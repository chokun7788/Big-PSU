# ข้อ2 — วินิจฉัยต้นเหตุจากผลเดิมก่อนทดสอบ10%

เอกสารนี้ทำก่อนsample01เริ่ม ไม่มีการแก้runtime/data/weights/prompt และยังไม่อ้างว่าปัญหาถูกแก้หรือคุณภาพดีขึ้น ขอบเขต76หัวข้อ/14หมวดเดิมคงไว้

อ่านผลเดิมครบ20,554requests/55,811grades และทำcase ledgerทุกkey เพิ่มการตรวจsource/traceรายกรณีจาก34เป็น72คำถาม ยืนยันตัวอย่างcontent/scope/omissionfailureได้29คำถาม ส่วนที่ยังไม่ตัดสินคงreview_required ไม่คิดsemanticaccuracyจากตัวอย่าง

## แยกความมั่นใจของหลักฐาน

- confirmed mechanism: มีtraceหรือcode-pathยืนยันเหตุที่เกิด เช่นHTTPtimeout/schema reject/verifierตัดclaim แต่ไม่รับรองว่าทุกคำตอบผิด
- confirmed content/scope/omission: agentตรวจคำถาม คำตอบ และsourceรายkeyแล้ว
- probable: มีหลักฐานเข้าทางสาเหตุ แต่ยังขาดcounterfactualหรือรายละเอียดbindingบางส่วน
- review_required: คงความไม่แน่ชัด เช่นpolicyequivalence, billing, ชื่อทับศัพท์ และข้อที่sourceยังไม่ยืนยัน

## สิ่งที่ทราบลึกกว่ารายงานเดิม

1. GPUไม่ได้หาย: จอในคำว่าการ์ดจอจับmonitor; เครื่องPCซึ่งยาวกว่าpcเลือกservicecapacityและกีดกันequipmentPC; poolไม่ว่างจึงไม่เข้าfallback device_type สองจุดร่วมกันทำให้ไม่เห็นGPUที่มีจริง
2. จอในคำว่าจองยังทำให้คำถามสิทธิ์คนนอกถูกตีเป็นinventorypresenceแล้วตอบวิธีใช้monitor เป็นข้อผิดก่อนโมเดล ไม่ใช่โมเดล4Bตอบไม่ได้เพียงเหตุเดียว
3. CS2streamคำถามแข่งไม่matchsourceclauseชัดก่อน แล้วnativepolicyfallbackเลือกstudio streamingก่อนmeaningreviewที่ควรคงcompetition scope
4. splitคำถามVALORANTแยกอาหารออกจากevent จึงส่งไปC10และทิ้งกฎเฉพาะการแข่งขัน
5. ตรวจsubstantive guardครบ13keys: source033/045/046/058มีสาระครบแต่textซ้ำheading จึงตัดทิ้ง รวมข้อหยุดเทคนิคและประท้วง ไม่ใช่แค่settingsตัวอย่างเดียว
6. seven buttonsของGranTurismoถูกทิ้งconstraint แล้วตอบ14entriesโดยledgerบอกsupported Savedlegacyก็มีปัญหาเดียวกัน จึงต้องตรวจครูกับsource ไม่เลียนแบบทั้งหมด
7. คำถามชดเชยmouseกลับตอบinventoryPCzone แสดงการจับentityแล้วละpredicate แม้ไม่มีmodelreplyที่ผ่าน
8. ผลsavedlegacyยืนยันแนวทางบางข้อ เช่นPC10/game→resource, GPU+ข้อจำกัดsource, CS2clauseเต็ม และoffsite rentalปฏิเสธตรงitem แต่บางkeysเดิมมีexception/ไม่มีคำตอบ จึงไม่ถือlegacyถูกทุกข้อ

## จำนวนอาการจากtraceทั้งชุด — กลุ่มซ้อนทับและไม่ใช่จำนวนตอบผิดทั้งหมด

| กลุ่มหลักฐาน | unique requests | ข้อจำกัดคำตัดสิน |
|---|---:|---|
| legacy_protocol_identity_mismatch | 19221 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| model_admission_denied_reason_not_fully_logged | 7339 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| provider_unavailable_terminal_needs_attribution | 4132 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| model_concurrency_admission_busy | 3971 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| controlled_live_artifact | 1082 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| literal_clause_or_first_line_assertion | 702 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| missing_source_report_requires_source_audit | 573 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| latency_assertion_failed | 376 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| policy_equivalence_or_authority_unresolved | 320 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| model_schema_or_version_rejection | 237 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| rule_dependency_reader_gap | 220 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| actual_http_timeout_or_transport_failure | 153 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| requested_field_not_delivered | 150 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| agent_source_adjudicated_case | 34 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| substantive_clause_guard_rejected_claim | 13 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |
| compiled_scope_rejected | 5 | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |

ค่าจำนวนอาจต่างจากR130auto reportเพราะรอบนี้ตรวจunderstanding.eventบนcompatibility pathด้วย และนับunique requestsแยกจากevent/grade occurrences: schema rejectionพบ237requests เทียบ162ที่รายงานเดิมนับเฉพาะdomain_flow.model_events ทั้งสองนิยามเก็บไว้ ไม่เขียนทับผลเดิม ส่วนlatencyในledgerนี้ตรวจคำว่าlatencyตรงassertionจึง376ไม่ใช่performance388ที่รวมtimeoutด้วย

## ตารางสาเหตุและหลักฐานรายกรณี

### 1. สอบถามครับ PC #10 มี TEKKEN 8 ไหม

Key `db84ae34e47e49d9ab384cd567f4d6b81a734d512bc486ff3dd91298c9b05bad` — first stage `meaning_to_resource_scope`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

**TEKKEN 8**
**โซนที่ยืนยันว่ามีเกมนี้**: PC Zone; PlayStation 5 Zone [S1]

สาเหตุ: ถาม PC #10 แต่ตอบเพียง PC Zone/PS5 Zone ไม่ตอบเครื่องที่ระบุ ทั้งที่ relation ของ TEKKEN 8 ระบุ installed_resource_ids เป็น PC01/PC02 และ PS5 ไม่ใช่ PC10 การไม่มี relation PC10 ยังไม่ใช่หลักฐานว่าเครื่องจริงไม่มีเกม แต่คำตอบนี้ละข้อจำกัดหลักและไม่แจ้งว่าศูนย์ยังไม่ยืนยัน PC10

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

PC #03-#10 ไม่มี TEKKEN 8 ครับ
TEKKEN 8 เล่นได้ที่ PC #01-#02

เกมที่มีใน PC #03-#10:
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Legacy exception: `None`; mode: `pipeline:structured_service_game_availability_no_match`

- `migrated_link_availability_pc_01_02_game_detail_tekken_8` rev1.installed_resource_ids: ["resource_pc_01", "resource_pc_02"] — [{"locator": "/mapped_fields/installed_resource_ids", "source_id": "r63_e7052c75b2767841a51e6dade36a"}]
- `migrated_link_availability_ps5_01_02_game_detail_tekken_8` rev1.installed_resource_ids: ["resource_ps5_01", "resource_ps5_02"] — [{"locator": "/mapped_fields/installed_resource_ids", "source_id": "r63_8328bacbdcca393bd9b93aa9217d"}]

### 2. กติกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม

Key `0c25d981c16244f8fe17020eaa9c404ed3481cb7c21cd832073e36db18f420d5` — first stage `native_policy_precedence`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

สตรีมเกม: คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม [S1]

สาเหตุ: ถามห้ามใช้บัคและดูสตรีมระหว่างแข่ง CS2 แต่เลือกนโยบายอนุญาตให้สตรีมเกมในศูนย์ทั่วไป C10; ถาม watching กลับตอบ broadcasting และทิ้งคำถามเรื่องบัค Source CS2 sections037/038 ระบุห้ามทั้งสองเรื่องอย่างชัดเจน เป็น scope/predicate failure ที่ยืนยันได้ ไม่ใช่ keyword fail อย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

คำตอบ: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
•    3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `r114_q034_owner_policy` rev1.answer: {"en": "The earlier answer permits game streaming; the latest answer says there is no zone restriction. It does not grant permission to install software.", "th": "คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม"} — [{"locator": "/fields/answer", "source_id": "r114_import_654fd6290395b93bd6a3d14f"}]
- `competition_competition_rules_cs2_psu_phuket_2026_section_037` rev4.text: {"en": "2. The use of hacks is strictly prohibited. No hacks related to map or game engine may be used. Any violation will result in a penalty loss for that round/map, or disqualification.", "th": "2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_b1e9f873e74ab4cde07c908a"}]
- `competition_competition_rules_cs2_psu_phuket_2026_section_038` rev4.text: {"en": "3. Watching streams: players are not allowed to watch live streams during competition", "th": "3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_af627ff54ed6a2beecf4c418"}]

### 3. กติกา CS2 ปรับ Brightness Resolution Crosshair ได้ไหมและปรับที่ไหน

Key `eede3e9bc31a8a8dd94a6153a507abdce4b351478660c74791cbdc2f6c8968a5` — first stage `substantive_verifier`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ

สาเหตุ: Source section045 มีประโยคอนุญาตปรับ Brightness/Resolution/Crosshair เฉพาะในเกมและจอครบแล้ว และ reader เลือก source ถูก แต่ verifier ถือว่า text เท่ากับ heading จึงไม่ substantive และซ่อนคำตอบจริง นี่คือ false rejection จาก verifier ไม่ใช่ข้อมูลหาย

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

คำตอบ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_045` rev4.text: {"en": "1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively.", "th": "1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_b047d5c279fb07535dedd2f9"}]

### 4. กติกา CS2 ปรับ Brightness Resolution Crosshair ที่ไหน แล้วใช้สคริปต์หรือมาโครได้ไหม

Key `41bef8792cfe7daa560724d4ca3dc480d18f0a6090298dd5c15e615f893cdb13` — first stage `needs_decomposition_then_verifier`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ

สาเหตุ: ต้องตอบทั้งสถานที่ปรับ setting และข้อห้าม macro แต่แผนรวมทั้งหมดเป็นหนึ่ง task เลือกเพียง045 แล้วถูก substantive guard ตัดทิ้ง ส่วน046เรื่องห้าม macro ไม่ได้ส่งมา ทั้งข้อมูล045และ046อยู่ใน snapshot

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

คำตอบ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

รายละเอียดที่เกี่ยวข้อง:
•    3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_045` rev4.text: {"en": "1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively.", "th": "1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_b047d5c279fb07535dedd2f9"}]
- `competition_competition_rules_cs2_psu_phuket_2026_section_046` rev4.text: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_8300d64c56c48ebbb8d8d003"}]

### 5. Please retrieve the official TEKKEN 8 rulebook evidence for the competition format

Key `cc40820b512274fd674eee1547618e99260a40f3f5815beadc1afb9d06bf75e8` — first stage `rule_clause_selection`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

**PSU Esports ปะทะมันส์ สนั่นจอ**
Competition rules and format for the Tekken 8 event at PSU Esports: Intense clashes, electrifying screens [S1]

สาเหตุ: ถาม competition format ของ Tekken8 แต่ตอบแค่ชื่อเอกสาร section001 ทั้งที่ section002 มี Offline/PS5/1v1/FT2/R3/60S และเกมตัดสินครบ Ledger supported จึงไม่ใช่หลักฐานว่าตอบ format แล้ว; กรณีนี้ grader fail แค่ route ด้วยซ้ำ จึงมี false comfort จาก literal checks

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`

- `competition_competition_rules_tekken8_psu_esports_section_001` rev5.text: {"en": "Competition rules and format for the Tekken 8 event at PSU Esports: Intense clashes, electrifying screens", "th": "กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_642456ddabf813822d00bbb9"}]
- `competition_competition_rules_tekken8_psu_esports_section_002` rev5.text: {"en": "Competition rules\n* Offline competition.\n* PlayStation 5 is used.\n* Singles (1v1).\n* Competition format:\n* FT2: the winner is the first to win 2 games.\n* Each game uses R3 (3 rounds per game) and 60S (60 seconds per round).\n* At a 1-1 tie, a deciding game must be played.", "th": "กติกาการแข่งขัน\n* แข่งขันแบบ ออฟไลน์ (Offline)\n* ใช้เครื่องเกม PlayStation 5\n* แข่งขันแบบ เดี่ยว (1v1)\n* รูปแบบการแข่งขัน:\n* FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน\n* ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)\n* หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_935aabc19087fc3216f81b22"}]

### 6. เครื่อง PC ใช้การ์ดจอรุ่นอะไร

Key `f6a75fef639e6062b4104422c8dc20ff0bd56e3f6401a12a6d2e48e4b65e3433` — first stage `entity_binding`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

พบรายการอุปกรณ์ แต่ยังไม่มีสเปกชิ้นส่วนที่ถามยืนยันไว้ครับ

สาเหตุ: คำตอบบอกไม่มีสเปก GPU แต่ equipment_gaming_pc.specifications มี GPU=NVIDIA GeForce RTX5060 8GB ชัดใน snapshot เป็น binding/projection failure ที่มีข้อมูลอยู่แล้ว ไม่ควรขอให้เจ้าของกรอก GPU ซ้ำ ส่วนสาเหตุย่อยว่า pool ผูกอุปกรณ์ใดต้องตรวจ binding trace เพิ่ม precision.equipment จะ fallback device_type เฉพาะ pool ว่าง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
สเปกนี้เป็นข้อมูลที่บันทึกไว้ในโปรเจกต์ ยังไม่พบหลักฐานในชุดข้อมูลนี้ว่ายืนยันตรงกับเครื่อง PC ที่ใช้งานจริงทุกเครื่อง
เว็บไซต์รายการอุปกรณ์ของศูนย์: https://esports.phuket.psu.ac.th/home
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

Legacy exception: `None`; mode: `pipeline:structured_equipment_item`

- `equipment_gaming_pc` rev11.specifications: [{"key": "zone", "unit": null, "value": "PC Zone"}, {"key": "quantity", "unit": null, "value": "10 Units"}, {"key": "recorded_source_detail", "unit": null, "value": "สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB"}, {"key": "CPU", "unit": null, "value": "Intel Core i5-14400"}, {"key": "RAM", "unit": null, "value": "DDR5 32GB"}, {"key": "GPU", "unit": null, "value": "NVIDIA GeForce RTX 5060 8GB"}] — [{"locator": "/mapped_fields/specifications", "source_id": "r68_specs_6e0321cf25d72b8d6e364a15"}]

### 7. Which game is available in the Cockpit Zone

Key `7e3ed641e480de8e89b3d40a1850766f75ff663563e714dc89d62e96bad82a36` — first stage `static_vs_live_intent_gate`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

For 2026-10-16 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

สาเหตุ: Which game is available in the Cockpit Zone เป็นคำถาม catalog แต่ไป live booking unavailable เพราะ available ถูกตีเป็นความว่างขณะนี้ ทั้งที่ relation Cockpit→GranTurismo7 มีอยู่ เป็นการเรียก dependency ผิดประเภท

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

There are currently 1 verified games in Cockpit Zone.

Cockpit Zone (1 game)
•    Gran Turismo 7
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Legacy exception: `None`; mode: `pipeline:structured_games_catalog_en`

- `migrated_link_availability_cockpit_01_02_game_detail_gran_turismo_7` rev1.installed_resource_ids: ["resource_cockpit_01", "resource_cockpit_02"] — [{"locator": "/mapped_fields/installed_resource_ids", "source_id": "r63_0451c72722b56f3491560d0278fb"}]

### 8. What is the price of Tekken 8 and what buttons does it have?

Key `b9fa6734a2eae9c25a534b5a4d69c7839ae4fa0080e47548dd5e6a76bb984b95` — first stage `binding_to_ambiguity_reconciliation`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

**what is the price of tekken 8**

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
**PlayStation 5 / PSU Student and Staff**
0 THB per person for 60 minutes [S1]
**PlayStation 5 / PSU Alumni and General Student**
50 THB per person for 60 minutes [S2]
**PlayStation 5 / General Adult**
150 THB per person for 60 minutes [S3]
**PC / PSU Student and Staff**
0 THB per person for 60 minutes [S4]
**PC / PSU Alumni and General Student**
25 THB per person for 60 minutes [S5]
**PC / General Adult**
70 THB per person for 60 minutes [S6]

**what buttons does it have?**

Which game do you want controls for? Please give the game and platform.

สาเหตุ: ส่วนแรกถามราคา Tekken8 ส่วนหลัง it อ้างกลับเกมเดียวกัน Compiler เก็บ explicit_anaphor และ bound controls_ps5_tekken_8 แล้ว แต่ยังคง ambiguity legacy_meaning_requires_clarification ส่งผลถามชื่อเกมซ้ำ เป็นการส่งต่อบริบทที่ resolve แล้วไปไม่ถึง reader

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

This question contains several topics. Here are the answers separately:

Question 1: What is the price of Tekken 8
Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

Question 2: what buttons does it have in TEKKEN 8
TEKKEN 8 controls:
- Square: Left Punch
- Triangle: Right Punch
- Cross: Left Kick
- Circle: Right Kick
- D-Pad Up: Jump
- D-Pad Left: Move Backward
- D-Pad Down: Duck
- L (Left Stick): Move
- L1: Special Style
- R1: Heat Activate
- R1 (While in Heat): Heat Smash
- Options: Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/83

Legacy exception: `None`; mode: `pipeline:multi_question_splitter`

- `controls_ps5_tekken_8` rev6.bindings: [{"action": {"en": "Left Punch", "th": "หมัดซ้าย / ต่อยซ้าย"}, "button_label": {"en": "Square", "th": "Square"}, "buttons": ["Square"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Punch or attack with the left hand — primary button to start fast frame combos", "th": "ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว"}, "section": {"en": null, "th": null}, "source_order": 1}, {"action": {"en": "Right Punch", "th": "หมัดขวา / ต่อยขวา"}, "button_label": {"en": "Triangle", "th": "Triangle"}, "buttons": ["Triangle"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Heavy punch or attack with the right hand — often used for high damage or countering (Counter)", "th": "ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter)"}, "section": {"en": null, "th": null}, "source_order": 2}, {"action": {"en": "Left Kick", "th": "ลูกเตะซ้าย"}, "button_label": {"en": "Cross", "th": "Cross"}, "buttons": ["C — [{"locator": "/bindings", "source_id": "r67_buttons_fb135360681ef967ab6036a5"}]
- `controls_ps5_tekken_8` rev6.limitations: {"en": "Square | Left Punch | Punch or attack with the left hand — primary button to start fast frame combos | \nTriangle | Right Punch | Heavy punch or attack with the right hand — often used for high damage or countering (Counter) | \nCross | Left Kick | Kick with the left leg to intercept or attack and create an opening in the opponent's defense. | \nCircle | Right Kick | Deliver a powerful right-leg kick, often for range control or a high-damage low sweep. | \nD-Pad Up | Jump | Jump upward to evade low attacks, or press in combination with mid-air attack button | \nD-Pad Left | Move Backward | Move the character backward to maintain distance or hold to \"Guard\" against high and medium attacks from enemies | \nD-Pad Down | Duck | Lower the character's stance to dodge punches or high attacks, and block low attacks | \nL (Left Stick) | Move | Move the character in general directions, including moving forward and backward. | \nL1 | Special Style | Press to toggle the Smart Assist mode — [{"locator": "/mapped_fields/limitations", "source_id": "r66_control_notes_1fe58e440724570b47083526"}]
- `controls_ps5_tekken_8` rev6.source_coverage: "secondary_needs_manual_verify" — [{"locator": "/mapped_fields/source_coverage", "source_id": "r67_raw_394827ca3d04db5835e5cc7ae1"}]

### 9. Under VALORANT tournamment ruls, are macros permitted and what food or beverages are allowed?

Key `21fe7ed0bd93155810d8d86f323dd7aaeb803b1d731e3b144c9e0c11b515f3dc` — first stage `shared_event_scope`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

**under valorant tournamment ruls, are macros permitted**

**PSU Phuket VALORANT 2026 Tournament**
Competition Rules and Format for VALORANT
PSU Phuket VALORANT Tournament 2026
Update: 17/02/2026
English below
Equipment and Accessories
In LAN competitions, players must strictly adhere to equipment specifications to ensure fairness.
* Self-provided equipment: Keyboard (wired/wireless), Mouse (wired/wireless), Mouse bungee cord, Mouse pad, In-ear headphones (wired), Wired headset
* Equipment provided by organizers: Organizers will provide PCs, monitors, headsets with microphones, tables, and chairs
* Allowed keyboard technologies: Snap Tap, SOCD, or equivalent technologies are permitted, unless otherwise instructed by officials
* Prohibited items:
* Macros (both software- and hardware-programmed) are strictly prohibited
* Installing any unauthorized programs on the provided computers is prohibited
* Accessing social media or any communication websites on competition computers is prohibited except for programs provided by organizers [S1]

**what food or beverages are allowed?**

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Food and beverages: Permitted to consume food and beverages only in designated areas [S2]
Food and drinks are allowed only in designated areas. [S3]

สาเหตุ: คำถามภายใต้ VALORANT tournament ถาม macro และอาหาร ส่วน macro อ่านเอกสารตรง แต่คำถามอาหารที่ละ event ถูกแยกไปกฎศูนย์ทั่วไป designated area ทั้งที่ source tournament002 อนุญาตเฉพาะน้ำภาชนะปิดและหมากฝรั่ง ไม่ถือว่ารวมหลาย tasks แล้วเข้าใจ shared scope ครบ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: Macros (both software- and hardware-based) are strictly prohibited.

Details:
• Food and drinks: Only drinking water in sealed containers and chewing gum are permitted.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_valorant_psu_phuket_2026_section_001` rev5.text: {"en": "Competition Rules and Format for VALORANT\nPSU Phuket VALORANT Tournament 2026\nUpdate: 17/02/2026\nEnglish below\nEquipment and Accessories\nIn LAN competitions, players must strictly adhere to equipment specifications to ensure fairness.\n* Self-provided equipment: Keyboard (wired/wireless), Mouse (wired/wireless), Mouse bungee cord, Mouse pad, In-ear headphones (wired), Wired headset\n* Equipment provided by organizers: Organizers will provide PCs, monitors, headsets with microphones, tables, and chairs\n* Allowed keyboard technologies: Snap Tap, SOCD, or equivalent technologies are permitted, unless otherwise instructed by officials\n* Prohibited items:\n* Macros (both software- and hardware-programmed) are strictly prohibited\n* Installing any unauthorized programs on the provided computers is prohibited\n* Accessing social media or any communication websites on competition computers is prohibited except for programs provided by organizers", "th": "กฎระเบียบและรูปแบบการแข่ — [{"locator": "/mapped_fields/text", "source_id": "r66_en_ef915f1f6c2441249cffc44f"}]
- `migrated_faq_curated_rule_food_drinks` rev4.answer: {"en": "Permitted to consume food and beverages only in designated areas", "th": "อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น"} — [{"locator": "/mapped_fields/answer", "source_id": "r66_en_55855f6eaa546bf1386febc1"}]
- `migrated_faq_rule_en_food_drink_natural` rev4.answer: {"en": "Food and drinks are allowed only in designated areas.", "th": "อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_9d9d2bceeab2eeb22316aa42e7f2"}]
- `competition_competition_rules_valorant_psu_phuket_2026_section_002` rev5.text: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_77eeddb33ca92a4ac795463e"}]

### 10. How many players must a Counter-Strike 2 team have?

Key `bf6817cf60eafe1135e325e4f1e5a5ee60f1f3cfe0797b1426b448f88644fe63` — first stage `team_vs_game_mode_predicate`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

No linked source is recorded for the requested detail of this item.

สาเหตุ: ถามจำนวนผู้เล่นทีม CS2 กลับอ่าน game_detail_cs2 แล้วบอก relation ไม่มี ทั้งที่ competition CS2 section018 มี team5players การใช้คำว่า team ไม่ควรไป players_max ของเกมทั่วไป ต้องตรวจชื่อรายการหากมีหลายฉบับจริง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`

- `competition_competition_rules_cs2_psu_phuket_2026_section_018` rev4.text: {"en": "2. Team composition: Each team consists of 5 players.", "th": "2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_f3415655a43a8241eb169452"}]

### 11. จองแล้วไม่สามารถยกเลิกได้ใช่ไหม ขอรายละเอียดแบบสั้น ๆ

Key `4dc69c73e386a0c78ae08185b7670353a2c754dd39f4f4bc8f322b9630fea34b` — first stage `cancellation_actor_and_polarity`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ

สาเหตุ: ถามยืนยันเชิงปฏิเสธว่ายกเลิกการจองไม่ได้ใช่ไหม แต่ไม่ตอบเงื่อนไขยกเลิก ทั้งที่เลือก FAQ cancel1hour อยู่แล้ว อีก variant กลับอ้างการที่ศูนย์ยกเลิกเพราะผิดกฎ ซึ่งคนละ actor; ข้อสรุปนี้คือ omission/wrong predicate ไม่ใช่การตัดสินว่าทุก policy ปัจจุบันไม่มี conflict

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`

- `migrated_faq_curated_cancel_1_hour` rev3.answer: {"en": "Cancellation of reservations must be made at least 1 hour in advance.", "th": "การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง"} — [{"locator": "/mapped_fields/answer", "source_id": "r66_en_f816f54a79926f69db6b589a"}]
- `migrated_faq_rule_cancel_advance` rev4.answer: {"en": "Cancellations must be made at least 1 hour in advance.", "th": "การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_0354143739cc458fb68202e567d8"}]
- `migrated_faq_rule_booking_cancel_invalid_info` rev4.answer: {"en": "A booking may be cancelled without prior notice if the provided information is incorrect or if the rules are violated.", "th": "การจองอาจถูกยกเลิกโดยไม่ต้องแจ้งให้ทราบล่วงหน้า หากข้อมูลไม่ถูกต้องหรือไม่ปฏิบัติตามกฎ"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_2d85787a4d58cfa5231def3e5cbd"}]

### 12. Can members of the public use the studio? Please answer only that point.

Key `f44d6445c66cb19efd3225d5eb996afaed0c67dbad9db4a3fd382126d106b566` — first stage `public_phrase_vs_person_entity`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

The source does not confirm the requested conditions: conditional_task_scope

สาเหตุ: members of the public หมายถึงผู้ใช้ทั่วไป แต่ระบบเลือก person records และแจ้ง conditional_task_scope ทั้งที่ r114_q037_owner_policy ยืนยันบุคคลภายนอกใช้บริการทั่วไปได้ ข้อความ answer only that point เป็น style instruction ไม่ควรถูกเป็นเงื่อนไขข้อเท็จจริง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Yes. Public visitors can book and use studio services. Fees depend on the service and user group. Book through the reservation system and present a national ID card at check-in.
Source: https://esports.computing.psu.ac.th/

Legacy exception: `None`; mode: `pipeline:protected_public_access`

- `member_17d23bd43ffdcfb0` rev5.role: {"en": "Manager", "th": "ผู้จัดการ"} — [{"locator": "/mapped_fields/role", "source_id": "r66_en_5670b7f0f4d5f6c859b5f1c6"}]
- `member_2035485e1198bd6d` rev5.role: {"en": "Computer technical officer", "th": "นักวิชาการคอมพิวเตอร์"} — [{"locator": "/mapped_fields/role", "source_id": "r66_person_review_3b101b0adc35f45731437fa7"}]
- `member_453ecaf47e840388` rev5.role: {"en": "Dean", "th": "คณบดี"} — [{"locator": "/mapped_fields/role", "source_id": "r66_en_c9a91dbf806b96d050bd5200"}]
- `member_4e005eeca4b538a1` rev5.role: {"en": "Vice president", "th": "รองอธิการบดี"} — [{"locator": "/mapped_fields/role", "source_id": "r66_person_review_865e801a34fbee919f32c28f"}]
- `member_832e24bbcd11737e` rev5.role: {"en": "Assistant to the president for academic affairs", "th": "ผู้ช่วยอธิการบดีฝ่ายวิชาการ"} — [{"locator": "/mapped_fields/role", "source_id": "r66_person_review_ae8ab02be3c7a29b0d5ee850"}]

### 13. What is the studio policy for rent laptop home

Key `4a52eaf23327daefe6e8adc391b5eb94d7365113e48fa2dabf2eac918a9b0aaa` — first stage `offsite_vs_onsite_scope`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

**PSU Esports Studio - Phuket - All Zones / external / full day**
Package price: 12,000.00 THB [S1]

**PSU Esports Studio - Phuket - All Zones / external / half day**
Package price: 6,000.00 THB [S5]

**PSU Esports Studio - Phuket - All Zones / internal / full day**
Package price: 6,000.00 THB [S9]

**PSU Esports Studio - Phuket - All Zones / internal / half day**
Package price: 3,000.00 THB [S13]

**PSU Esports Studio - Phuket - Cockpit Zone / external / full day**
Package price: 2,000.00 THB [S17]

**PSU Esports Studio - Phuket - Cockpit Zone / external / half day**
Package price: 1,000.00 THB [S21]

**PSU Esports Studio - Phuket - Cockpit Zone / internal / full day**
Package price: 1,000.00 THB [S25]

**PSU Esports Studio - Phuket - Cockpit Zone / internal / half day**
Package price: 500.00 THB [S29]

**PSU Esports Studio - Phuket - VR Zone / external / full day**
Package price: 6,000.00 THB [S33]

**PSU Esports Studio - Phuket - VR Zone / external / half day**
Package price: 3,000.00 THB [S37]

**PSU Esports Studio - Phuket - VR Zone / internal / full day**
Package price: 3,000.00 THB [S41]

**PSU Esports Studio - Phuket - VR Zone / internal / half day**
Package price: 1,500.00 THB [S45]

**PSU Esports Studio - Phuket - Nintendo Switch Zone / external / full day**
Package price: 2,000.00 THB [S49]

**PSU Esports Studio - Phuket - Nintendo Switch Zone / external / half day**

สาเหตุ: ถามเช่า laptop กลับบ้าน แต่ตอบราคาเหมาโซน24แพ็กเกจ เป็น scope substitution ระหว่าง offsite equipment rental กับ onsite venue rental ข้อมูลราคา package อ้างถูก source ก็ยังตอบผิดเรื่อง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Zone rental fees for organizations

No rental rate is recorded for these requested targets: laptop home

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

Legacy exception: `None`; mode: `pipeline:zone_rental_fee`


### 14. Please check: How many starting players must a VALORANT team field? please.

Key `864bd598097acf52516da1f737b8ea89803aee391e4e161ecf307091c5f8ecb8` — first stage `competition_predicate_to_procedure`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

Booking steps
1. select the desired service
2. choose the date and time
3. enter customer information
4. verify the details
5. pay by transferring funds to a bank account,
6. attach the transfer slip.
[S1]

สาเหตุ: ถาม starting players ของ VALORANT แต่ตอบขั้นตอนจองบริการ6ขั้น เป็น actual off-topic answer แม้เกณฑ์เดิมจะคาด no_answer; ไม่สรุปจำนวนผู้เล่นจริงจาก Match Prep6ซึ่งคนละ predicate

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`

- `migrated_faq_curated_booking_steps` rev3.answer: {"en": "The booking procedure is: select the desired service, choose the date and time, enter customer information, verify the details, pay by transferring funds to a bank account, and attach the transfer slip.", "th": "ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน"} — [{"locator": "/mapped_fields/answer", "source_id": "r66_en_240dd7619c2cdce6429ad607"}]
- `competition_competition_rules_valorant_psu_phuket_2026_section_002` rev5.text: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_77eeddb33ca92a4ac795463e"}]

### 15. Under CS2 tournament rules, are scripts or macros allowed?

Key `06563f1ae9408da58022051f3e726807ac1c5a10ef93d93b6c5c0822c9d9ba17` — first stage `substantive_verifier`; confidence `confirmed_source_case`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ถาม CS2 scripts/macros แต่ไม่ตอบทั้งที่ section046 ระบุห้ามชัดเจน สาเหตุเดียวกับ substantive guard false rejection พบใน traceการเลือก clause; ไม่ต้องเพิ่มข้อมูลหรือน้ำหนักเพื่อทดแทนประโยคที่มีอยู่

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: No scripts or macros are allowed at all.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_046` rev4.text: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_8300d64c56c48ebbb8d8d003"}]

### 16. ใครเป็นประธาน

Key `7dc03c3b0e66f7715b048135bee92796f7043e0cb9f126d22a2f0fddafbbdd9b` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_supported_fact_protocol_mismatch`

คำตอบR130:

**นายษุภากรณ์ จิราจินดากุล**
• ชื่อที่อนุญาตให้เผยแพร่: นายษุภากรณ์ จิราจินดากุล [S1]
• ทีม/หน่วยงาน: PSU Phuket Esports Club - PSU Phuket [S2]
• ตำแหน่ง/หน้าที่: ประธาน [S3]

สาเหตุ: ชื่อ/ทีม/บทบาทประธานที่ตอบตรง person fields ใน snapshot แต่ route knowledge ไม่เหมือน legacy members/overview; ไม่ใช้ route fail ตัดสินว่าชื่อผิด ทั้งนี้ sourceเป็นร่างและไม่ยืนยันว่าบุคคลนี้ยังดำรงตำแหน่งจริง ณวันนี้

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ตำแหน่ง ประธาน มี 1 คนครับ
•    นายษุภากรณ์ จิราจินดากุล: ประธาน
  ◦    หมวด: PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

Legacy exception: `None`; mode: `pipeline:structured_members_role_lookup`

- `member_1d884f11f3890dea` rev4.role: {"en": "Chair", "th": "ประธาน"} — [{"locator": "/mapped_fields/role", "source_id": "r66_person_review_06a15a8e9bce9275b3e25033"}]

### 17. Fortnite ราคาเท่าไหร่

Key `c42fafb19394b0b1b06620bfc90cfce671ddc9f1083a43f6eab8bfa1ce151b35` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_supported_fact_with_presentation_and_validity_review`

คำตอบR130:

อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
**PlayStation 5 / PSU Student and Staff**
0 บาทต่อคน สำหรับ 60 นาที [S1]
**PlayStation 5 / PSU Alumni and General Student**
50 บาทต่อคน สำหรับ 60 นาที [S2]
**PlayStation 5 / General Adult**
150 บาทต่อคน สำหรับ 60 นาที [S3]

สาเหตุ: ตัวเลขPS5 0/50/150 ต่อ60นาทีตรง rate fields และมี Fortnite→PS5 offering จึงไม่ถือ missingFortnite keyword ว่าราคาผิด แต่คำตอบไม่เขียนว่าเป็นค่าใช้บริการเล่นเกม ไม่ใช่ราคาซื้อเกม และ owner reaffirmed10/20ช้ากว่า workloadclock10/16 ความใช้ได้ตามเวลายังต้องreview

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Fortnite ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

PlayStation 5 Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน
PlayStation 5 1 ชั่วโมง (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท/1 ชั่วโมง
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/1 ชั่วโมง
•    บุคคลทั่วไป (General Adult): 150 บาท/1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Legacy exception: `None`; mode: `pipeline:structured_service_fee_by_game`

- `migrated_link_availability_ps5_01_02_game_detail_fortnite` rev1.installed_resource_ids: ["resource_ps5_01", "resource_ps5_02"] — [{"locator": "/mapped_fields/installed_resource_ids", "source_id": "r63_a4efd2fa29bc3343bab82de589ee"}]

### 18. Under RoV tournament rules, which team is blue in game one, who chooses later sides and what hero ban/pick system is used?

Key `6307201593efdde5e48452d6cd6739610d18d4355e90d0b9ae4355e02df29368` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_supported_requested_clauses_literal_mismatch`

คำตอบR130:

**Blueket Games 2025 Men's Team**
4. Competition regulations and rules
4.1. Basic rules
4.1.1. Character names or language that are rude or mock others are prohibited.
4.1.2. In the first game, the team at the top of the bracket takes the blue side. In subsequent games, the loser of the previous game chooses the side.
4.1.3. The referee announces the room number, and both teams must enter that room.
* The blue team is at the top.
* The red team is at the bottom.
4.1.4. If a side delays the start by more than 15 minutes beyond the scheduled time, it immediately loses the competition.
4.2. Competition rules
4.2.1. Every competitor must have at least 18 heroes to enter the competition 5v5 mode (formerly Tournament Mode).
4.2.2. Global Ban/Pick is used for hero bans and picks.
4.2.3. Runes and enhancements may be configured as desired.
4.2.4. All heroes may be selected during the competition.
4.2.5. Skins other than Default are prohibited.
4.2.6. Repeating a hero selection in the competition, or any other action causing a system problem, is prohibited in all cases.
4.3. Disconnect and Rematch
4.3.1. If a competitor disconnects, temporarily pause the game. Each team may pause 5 times, no more than 1 minute each. Beyond that time, the other team may immediately press Resume and continue normally. [S1]

สาเหตุ: คำตอบ RoV ระบุ upper bracketทีมblue เกมแรก ผู้แพ้เลือกข้างเกมถัดไป และGlobalBan/Pickครบตามsource006 แต่ wordingภาษาอังกฤษไม่ตรงcomplete_clauseที่graderกำหนด การขึ้นหัวเอกสารยาวทำfirst_lineไม่ตรง ไม่พบความหมายผิดในสามpredicateที่ตรวจนี้ ข้อความส่วนเกินอื่นไม่ถือว่าผ่านอัตโนมัติ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: 4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side.

Details:
• 4.2.2. Use Global Ban/Pick hero selection.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_rov_blueket_2025_men_section_006` rev5.text: {"en": "4. Competition regulations and rules\n4.1. Basic rules\n4.1.1. Character names or language that are rude or mock others are prohibited.\n4.1.2. In the first game, the team at the top of the bracket takes the blue side. In subsequent games, the loser of the previous game chooses the side.\n4.1.3. The referee announces the room number, and both teams must enter that room.\n* The blue team is at the top.\n* The red team is at the bottom.\n4.1.4. If a side delays the start by more than 15 minutes beyond the scheduled time, it immediately loses the competition.\n4.2. Competition rules\n4.2.1. Every competitor must have at least 18 heroes to enter the competition 5v5 mode (formerly Tournament Mode).\n4.2.2. Global Ban/Pick is used for hero bans and picks.\n4.2.3. Runes and enhancements may be configured as desired.\n4.2.4. All heroes may be selected during the competition.\n4.2.5. Skins other than Default are prohibited.\n4.2.6. Repeating a hero selection in the competition, or any o — [{"locator": "/mapped_fields/text", "source_id": "r66_en_5219ef5d00510358fb0f8d3b"}]

### 19. Who is the manager?

Key `38b729fbcfc1140b09a3313a5e07e73baea258036b7d75f26d597ca910f35220` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_supported_fact_localization_review`

คำตอบR130:

**นายชนะชัย สิริพันธ์วราภรณ์**
• Name: นายชนะชัย สิริพันธ์วราภรณ์ [S1]
• Group: Members [S2]
• Role: Manager [S3]

English translation is machine generated and has not been reviewed by the owner.

สาเหตุ: ตอบmanagerชื่อไทยภายใต้requested English ไม่ถือว่าชื่อเฉพาะภาษาไทยเป็นThai proseผิดทั้งหมด แต่ยังมี machine-translation disclaimer และกลุ่มMembersที่ควรตรวจภาษา/ขอบเขต ไม่ยืนยันชื่อปัจจุบันนอกsnapshot

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Verified PSU Esports Studio - Phuket member record(s) for the requested role:
Names retain the exact spelling in the official Thai source; role labels are translated.
- นายชนะชัย สิริพันธ์วราภรณ์: Manager (ผู้จัดการ) - PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)

Legacy exception: `None`; mode: `pipeline:structured_members_source_th`

- `member_17d23bd43ffdcfb0` rev5.role: {"en": "Manager", "th": "ผู้จัดการ"} — [{"locator": "/mapped_fields/role", "source_id": "r66_en_5670b7f0f4d5f6c859b5f1c6"}]

### 20. What buttons does this game have

Key `43fd5b841f40fa4e2abc9b639a8528a1281327c3d004b5e65ae7a64f2dc19d91` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `appropriate_clarification_in_saved_context`

คำตอบR130:

Which game do you want controls for? Please give the game and platform.

สาเหตุ: ถาม this game โดยไม่มีชื่อเกมในข้อความ และ saved jobไม่มีประวัติที่ระบุตัวเกม จึงถามเกมและplatformได้ ไม่บังคับตอบมั่วเพราะold outcomeคาดanswer

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

I could not identify a verified game title with matching control information for this request. Please confirm the spelling and exact game edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Legacy exception: `None`; mode: `pipeline:game_controls_target_unconfirmed_en`


### 21. Alumni เล่น VR 1 ชั่วโมง 3 ชั่วโมง เสียกี่บาท

Key `22979a6fedf7e9b5439e3496c1b1fba262c4c729acb97fc7cd83379acf4f458c` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `ambiguity_review_required`

คำตอบR130:

ระยะเวลาที่ระบุแต่ละช่วงหมายถึงอะไรครับ ต้องการเล่นนานเท่าไร และช่วงใดเป็นเวลาต่อรอบ?

สาเหตุ: มี1ชั่วโมงและ3ชั่วโมงโดยไม่บอกว่าเปรียบเทียบหรือเล่นรวม/แบ่งsession การถามให้ระบุมีเหตุผล แต่ยังตัดสินไม่ได้ว่าควรตีเป็นcompareโดยอัตโนมัติ; ไม่ให้ oldgraderที่คาดanswerเป็นคำสั่งเลือกเลขแรก

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

VR — 60 นาที/แพ็กเกจ (1-5 คน)
ระยะเวลาที่ถาม 60 นาที (1 ชั่วโมง) คิดเป็น 1 session (แพ็กเกจ)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Legacy exception: `None`; mode: `pipeline:structured_service_fee_conversation`


### 22. ช่วยอ้างอิงข้อมูลที่ยืนยันได้: ศุกร์นี้ 10:00 VR มีรอบว่างหรือไม่

Key `ddbd104be6c965c98394d227ca03c9c7b4110d9822c25d8930cd26b2e597b94e` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `controlled_live_unavailable_not_real_provider_verdict`

คำตอบR130:

วันที่ 2026-09-25 (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะการเชื่อมต่อระบบจองยังไม่พร้อมใช้งานครับ
ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

สาเหตุ: คำถามมีเวลา/บริการจึงต้องlive; targetศุกร์2026-09-25ถูกตามjobreference2026-09-24 ไม่ใช่วันที่วันนี้ ตัวharnessคืนfixture_offlineโดยตั้งใจ จึงยังพิสูจน์ไม่ได้ว่าWordPressจริงเสียหรือslotจริงว่าง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

วันที่ 2026-09-25 (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะการเชื่อมต่อระบบจองยังไม่พร้อมใช้งานครับ
ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

Legacy exception: `None`; mode: `pipeline:live_booking_status_unavailable`


### 23. JSON คืออะไร ตอบแบบเด็กปีหนึ่งเข้าใจได้

Key `a47addbf963dea532888367209ebee84fbbd5844b09083051924cc50b64767ca` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `confirmed_model_execution_failure_unanswered`

คำตอบR130:

ระบบตีความคำถามไม่พร้อมชั่วคราว กรุณาลองอีกครั้งครับ

สาเหตุ: JSONทั่วไปไม่ได้ต้องการbusinessdataที่หาย แต่ admissionไม่พร้อมก่อนcontext/generic answer ทำให้ตอบretry ผลผู้ใช้คือไม่ได้คำตอบ; ไม่ใช่คำอธิบายJSONผิดและไม่ใช่เหตุให้ย้ายข้อมูลศูนย์เพิ่ม

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ยังไม่ได้ยืนยันข้อกำหนดอายุและการมีผู้ปกครองสำหรับเด็กครับ การเปิดให้บุคคลทั่วไปใช้บริการยังใช้ยืนยันข้อนี้ไม่ได้

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Legacy exception: `None`; mode: `pipeline:user_service_facts`


### 24. Where is Uncharted located?

Key `6da6641fc3b56427cb0b06cc3d306ed217b70a523f9599e045f7cb74853661e2` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `confirmed_model_protocol_failure_unanswered`

คำตอบR130:

The checking service is unavailable; this detail cannot be confirmed.

สาเหตุ: selectorHTTPสำเร็จและactualbaseprofileถูก แต่คืนarray i/question/evidence แทนplans schema จึงplans_not_array ตอบไม่ได้ ไม่มีหลักฐานว่าผู้ใช้ได้รับsourceถูกต้อง แม้โมเดลคืนJSONที่อ่านได้

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Uncharted: Legacy of Thieves Collection is available on: PlayStation 5 #01-#02. Studio zone(s): PlayStation 5 Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Legacy exception: `None`; mode: `pipeline:structured_game_availability_en`


### 25. VALORANT แข่งขันใช้ผู้เล่นกี่คน

Key `ae8098286a5469a7e212ddaa6b50fe731420e34eda66c680d150b5d219c35dd4` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `confirmed_model_protocol_failure_unanswered`

คำตอบR130:

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

สาเหตุ: ถามจำนวนผู้เล่นแข่งขันVALORANT selectorใช้เวลาราว46sแล้วส่งevidenceechoที่ไม่ผ่านplans schema และยก MatchPrep6ซึ่งไม่ใช่startingteamcount; outputถูกreject จึงไม่เรียกว่าระบบให้จำนวน6ผิดแก่ผู้ใช้ แต่คำถามไม่ได้รับคำตอบ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`

- `competition_competition_rules_valorant_psu_phuket_2026_section_002` rev5.text: {"en": "Competition area and regulations\n* During Match Prep, no more than 6 players are allowed.\n* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.\n* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.\n* Only drinking water in a sealed container and chewing gum are allowed.\nCompetition process", "th": "พื้นที่การแข่งขันและกฎระเบียบ\n* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน\n* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์\n* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง\n* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น\nกระบวนการแข่งขัน"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_77eeddb33ca92a4ac795463e"}]

### 26. What games are available on Nintendo Switch (1-2 Players)?

Key `473dd47b5ea9cc6a5ab941163db2469c3d1daf99da16b7c20cc6a5bc1145b534` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_gap_with_qualified_owner_recommendations`

คำตอบR130:

Confirmed player counts by game and mode are not recorded, so games matching this player count cannot yet be listed.

สาเหตุ: ถามNintendo1–2players ระบบไม่ยืนยันรายการตามmode ข้อมูลเจ้าของมีrecommendationsสำหรับมา2คน แต่ไม่มีgame_mode/maxplayersที่ยืนยันทุกเกม คำตอบควรแยกแนะนำจากรับรองโหมด ไม่ถือว่าrecommendationเท่ากับmode proof และไม่บอกว่าไม่มีข้อมูลเกมเลย

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

There are currently 17 verified games in Nintendo Switch Zone.

Nintendo Switch Zone (17 games)
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
•    The Legend of Zelda: Breath of The Wild
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Legacy exception: `None`; mode: `pipeline:source_operation_game_list`


### 27. Horizon Call of the Mountain: What buttons are available?

Key `db4984496f3d774117a27fe6ddb988a241f15a2daa33e5eced0f3f1972362ed9` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `appropriate_partial_source_coverage`

คำตอบR130:

**Horizon Call of the Mountain / PlayStation VR2 / PS5**
| Input | Action |
|---|---|
| Gesture control scheme | Move using physical movements — Gesture mode lets players move through the game world by moving their bodies [S1] |
| Analogue control scheme | Move using sticks — Analogue mode uses sticks on PS VR2 Sense controllers to move in games [S2] |
| PS VR2 Sense grip button | Grab objects — The official game page states that PS VR2 Sense controllers have a grip button for grabbing in-game objects. [S3] |
The source describes only part of the controls; a complete button layout is not confirmed.
Note: Official PlayStation support confirms Gesture and Analogue control schemes. The public support page does not provide a full per-button mapping.

สาเหตุ: HorizonVRมีเพียงGesture/Analogue/gripที่sourceยืนยัน คำตอบบอกว่าไม่ครบlayoutชัดเจน จึงไม่ถือpartialหรือcomplete-clausefailทั้งหมดเป็นcontentwrong และไม่เอาจำนวน3แถวเป็นจำนวนปุ่มทั้งหมด

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Horizon Call of the Mountain controls:
- Gesture control scheme: Move using physical movements
- Analogue control scheme: Move using sticks
- PS VR2 Sense grip button: Grab objects
Source: https://www.playstation.com/en-us/support/games/horizon-call-of-the-mountain/

Legacy exception: `None`; mode: `pipeline:structured_game_controls_en`

- `controls_vr_horizon_call_of_the_mountain` rev7.bindings: [{"action": {"en": "Move using physical movements", "th": "เคลื่อนที่ด้วยท่าทางร่างกาย"}, "button_label": {"en": "Gesture control scheme", "th": "Gesture control scheme"}, "buttons": ["Gesture control scheme"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Gesture mode lets players move through the game world by moving their bodies", "th": "โหมด Gesture ให้ผู้เล่นเคลื่อนที่ในโลกของเกมผ่านการขยับร่างกาย"}, "section": {"en": null, "th": null}, "source_order": 1}, {"action": {"en": "Move using sticks", "th": "เคลื่อนที่ด้วยอนาล็อก"}, "button_label": {"en": "Analogue control scheme", "th": "Analogue control scheme"}, "buttons": ["Analogue control scheme"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Analogue mode uses sticks on PS VR2 Sense controllers to move in games", "th": "โหมด Analogue ใช้ sticks บน PS VR2 Sense controllers เพื่อเคลื่อนที่ในเกม"}, "section": {"en": null, "th": null}, "source_order": 2}, {"action": {"en": " — [{"locator": "/bindings", "source_id": "r67_buttons_306fc7621e69de45030a63d6"}]
- `controls_vr_horizon_call_of_the_mountain` rev7.limitations: {"en": "Gesture control scheme | Move using physical movements | Gesture mode lets players move through the game world by moving their bodies | \nAnalogue control scheme | Move using sticks | Analogue mode uses sticks on PS VR2 Sense controllers to move in games | \nPS VR2 Sense grip button | Grab objects | The official game page states that PS VR2 Sense controllers have a grip button for grabbing in-game objects. | ", "th": "Gesture control scheme | เคลื่อนที่ด้วยท่าทางร่างกาย | โหมด Gesture ให้ผู้เล่นเคลื่อนที่ในโลกของเกมผ่านการขยับร่างกาย | \nAnalogue control scheme | เคลื่อนที่ด้วยอนาล็อก | โหมด Analogue ใช้ sticks บน PS VR2 Sense controllers เพื่อเคลื่อนที่ในเกม | \nPS VR2 Sense grip button | จับวัตถุในเกม | หน้าเกมทางการระบุว่า PS VR2 Sense controllers มี grip button สำหรับจับวัตถุในเกม | "} — [{"locator": "/mapped_fields/limitations", "source_id": "r66_control_notes_e1a691fbeb5658076460b122"}]
- `controls_vr_horizon_call_of_the_mountain` rev7.source_coverage: "partial_official" — [{"locator": "/mapped_fields/source_coverage", "source_id": "r67_raw_88eab3781e9978f0efb3ef95ad"}]

### 28. อยากรู้ว่า กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า อัดวิดีโอในศูนย์ได้ไหม

Key `5fe497661b76afe4b1c911e44f9a7646c52c4d68d5af0ba617b18a4f1b158ce2` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `appropriate_scope_boundary_with_presentation_review`

คำตอบR130:

ยังไม่ยืนยันสิทธิ์ถ่ายสถานที่หรือบุคคลจากนโยบายการบันทึกในเกม กรุณาตรวจขอบเขตข้อมูลด้านล่างครับ
บันทึกภาพในเกม: capture ภาพหรือวิดีโอในเกมได้ เมื่อเสร็จให้ลบ; ไม่ครอบคลุมการถ่ายบุคคลหรือสถานที่ [S1]

สาเหตุ: สิทธิ์captureในเกมไม่ครอบคลุมการถ่ายบุคคล/สถานที่ คำถามอัดวิดีโอในศูนย์กว้างกว่าข้อมูล จึงระบุscopeและข้อที่ยังไม่ยืนยันเหมาะสม ไม่ถือว่าownerตอบYesแล้วแปลว่าYesทุกแบบ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`

- `r114_q033_owner_policy` rev1.answer: {"en": "In-game screenshots and video capture are allowed; delete them when finished. This does not confirm filming people or the premises.", "th": "capture ภาพหรือวิดีโอในเกมได้ เมื่อเสร็จให้ลบ; ไม่ครอบคลุมการถ่ายบุคคลหรือสถานที่"} — [{"locator": "/fields/answer", "source_id": "r114_import_8f63628c6c98653b14270500"}]

### 29. Can I cancel my booking? Could you check this for me

Key `689469bad5ec835fb8bb63f64e1d03faa35cde6a172edb15ff08fa9a0aa42b07` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `overcautious_equivalence_review_required`

คำตอบR130:

Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.
Cancellations must be made at least 1 hour in advance. [S1]
Cancel reservation: Cancellation of reservations must be made at least 1 hour in advance. [S2]

สาเหตุ: แหล่งยกเลิกสองฉบับในตัวอย่างนี้ต่างwordingอังกฤษแต่เงื่อนไขไทยล่วงหน้า1ชั่วโมงตรงกัน การเตือนconflictทุกกรณีดูเกินจำเป็น อย่างไรก็ดีไม่ใช้ความเหมือนข้อความยืนยันsupersession/validityทั้งชุด ต้องตรวจactor/condition/version

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Cancellations must be made at least 1 hour in advance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Legacy exception: `None`; mode: `pipeline:rule_en`

- `migrated_faq_rule_cancel_advance` rev4.answer: {"en": "Cancellations must be made at least 1 hour in advance.", "th": "การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_0354143739cc458fb68202e567d8"}]
- `migrated_faq_curated_cancel_1_hour` rev3.answer: {"en": "Cancellation of reservations must be made at least 1 hour in advance.", "th": "การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง"} — [{"locator": "/mapped_fields/answer", "source_id": "r66_en_f816f54a79926f69db6b589a"}]

### 30. Can I use an unknown game called Example Quest

Key `95e77247fc9958fad966e8b846c8f2766628dfaa3081b76a92579b93791ffcb2` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `appropriate_unknown_named_item`

คำตอบR130:

No game record matching “Example Quest” was found in this data set, so its studio offering is not confirmed.

สาเหตุ: ExampleQuestไม่อยู่ในrecords จึงบอกไม่ยืนยันofferingได้ ไม่อนุมานว่าเกมไม่มีอยู่จริงทั่วโลก

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

I could not find Example Quest in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Legacy exception: `None`; mode: `pipeline:games_unknown_target_en`


### 31. รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ วันอังคารศูนย์เปิดกี่โมง

Key `05880449d8e01435c710c4e401a2e5e133eb7d3b827315831071d25c030e339b` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_supported_regular_calendar_not_live`

คำตอบR130:

วันอังคาร **เปิดให้บริการ** เวลา 09:00–12:00, 13:00–16:00 น. ตามตารางบริการครับ [S1]

สาเหตุ: ตอบอังคาร09–12/13–16ตรงservice timetableที่บันทึก ใช้regular play serviceไม่ใช่อาคารเปิดหรือเครื่องว่าง; ไม่สรุปจากข้อนี้ว่าตรวจวัน/วันหยุดทุกกรณีถูกครบ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

วันอังคาร: เปิดให้เล่น 09:00-12:00 และ 13:00-16:00

รายละเอียดจากตาราง:
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Legacy exception: `None`; mode: `pipeline:structured_schedule`


### 32. How to book Nintendo Switch and what days are they opening

Key `ca7b611979f8b5c24dd7ddb6c821da52df9b2cd85eda74e040498ce608c32880` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_supported_independent_needs_with_limits`

คำตอบR130:

1. how to book nintendo switch
Booking steps
1. select the desired service
2. choose the date and time
3. enter customer information
4. verify the details
5. pay by transferring funds to a bank account,
6. attach the transfer slip.
[S1]

2. what days are they opening
Recorded regular play-service timetable, not live machine availability or building access hours. Special closures override this timetable.
**Monday**
**regular play-service timetable**: 09:00–12:00 maintenance; 13:00–16:00 open for play [S2]
**Tuesday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S3]
**Wednesday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S4]
**Thursday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S5]
**Friday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 maintenance [S6]
**Saturday**
**regular play-service timetable**: Closed for play under the regular timetable [S7]
**Sunday**
**regular play-service timetable**: Closed for play under the regular timetable [S8]

สาเหตุ: ตอบขั้นตอนจองและตารางทั้ง7วันโดยไม่ทิ้งงานหลัง แม้labelpartial; เป็นตัวอย่างว่ากลไกmulti-taskทำได้บางเคส ไม่ใช่หลักฐานว่าบริบทเชื่อมโยงถูกทุกเคส

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

This question contains several topics. Here are the answers separately:

Question 1: How to book Nintendo Switch
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

Question 2: what days are they opening
Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public h

Legacy exception: `None`; mode: `pipeline:multi_question_splitter`

- `migrated_faq_curated_booking_steps` rev3.answer: {"en": "The booking procedure is: select the desired service, choose the date and time, enter customer information, verify the details, pay by transferring funds to a bank account, and attach the transfer slip.", "th": "ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน"} — [{"locator": "/mapped_fields/answer", "source_id": "r66_en_240dd7619c2cdce6429ad607"}]

### 33. a student from another university plays Nintendo Switch for 30 minutes, how much does it cost, and how to book

Key `ed0be633e5cdca49e047b59e7c029213edb4b0fe8da3dfbae8bf1d0289d542ed` — first stage `billing_labels_and_compiled_scope`; confidence `see_individual_decision`; decision `review_required_billing_and_compiled_scope`

คำตอบR130:

**a student from another university plays nintendo switch for 30 minutes, how much does it cost**

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
**Nintendo Switch / PSU Alumni and General Student**
50 THB for 30 minutes [S1]
**Nintendo Switch / PSU Alumni and General Student**
100 THB for 30 minutes [S2]

**how to book**

Please specify the item and requested time.

สาเหตุ: มีคำถามNintendo30นาที/กลุ่มนักศึกษาต่างมหาวิทยาลัย แต่แสดงสองrateของขนาดกลุ่มโดยไม่labelและส่วนจองinvalidscope ต้องตรวจbillingruleเต็มก่อนตัดสินจำนวนเงินผิด; ยืนยันได้ว่าคำตอบยังไม่ครบและคลุมเครือ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

This question contains several topics. Here are the answers separately:

Question 1: a student from another university plays Nintendo Switch for 30 minutes, how much does it cost
Service prices (recorded package rates):

Nintendo Switch — 60 minutes/package (1-2 people)
Requested duration: 30 minutes (0.5 hours); 1 session(s).
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 50 THB/package

Nintendo Switch — 60 minutes/package (3-4 people)
Requested duration: 30 minutes (0.5 hours); 1 session(s).
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 100 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Question 2: how to book
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://es

Legacy exception: `None`; mode: `pipeline:multi_question_splitter`


### 34. ข่าวการเมืองล่าสุดคืออะไร

Key `527eab962311af7453d4a20d77d9b03dfd46d584ba107a8a40a38562ddc4df4e` — first stage `no_confirmed_failing_stage_or_separate_evaluation_issue`; confidence `see_individual_decision`; decision `source_gap_and_wrong_clarification_wording`

คำตอบR130:

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

สาเหตุ: ไม่มีrecordชนิดnewsจริงในsnapshot การไม่ยืนยันข่าวการเมืองล่าสุดจึงไม่ใช่ย้ายข้อมูลเกมไม่ครบ แต่ข้อความให้ระบุเกม/เครื่องไม่ตรงคำถาม ควรบอกข้อจำกัดข่าวล่าสุดหรือใช้general/current-sourcecapabilityที่แยกชัด

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้

Legacy exception: `None`; mode: `pipeline:freshness_live_source_required`


### 35. TEKKEN 8 กับ Resident Evil Village มีปุ่มอะไรบ้าง

Key `5070c43c2755d2994c0c0dd04a1018e80e9a857b5f26b72c01c14f5c7137e202` — first stage `needs_decomposition`; confidence `probable`; decision `probable`

คำตอบR130:

ต้องการปุ่มของเกมนี้บนแพลตฟอร์มใดครับ?

สาเหตุ: ถามcontrolsของสองเกม แต่แผนเหลือtaskเดียวไม่มีtargetและถามแพลตฟอร์มของเกมนี้แบบเอกพจน์ ข้อมูลมีหลายแพลตฟอร์มจึงอาจต้องถามกลับจริง แต่ยังควรรักษาทั้งสองเกมและตอบส่วนที่ยืนยันได้ ต้องแยกความกำกวมแพลตฟอร์มจากการทำtargetหาย

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: TEKKEN 8 มีปุ่มอะไรบ้าง
TEKKEN 8 มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว
•    Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter)
•    Cross: ลูกเตะซ้าย - ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู
•    Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง
•    D-Pad Up: กระโดด - ควบคุมให้ตัวละครกระโดดขึ้นด้านบนเพื่อหลบการโจมตีล่าง หรือใช้กดร่วมกับปุ่มโจมตีกลางอากาศ
•    D-Pad Left: ถอยหลัง / บล็อก - บังคับตัวละครให้เดินถอยหลังเพื่อรักษาระยะ หรือใช้กดค้างเพื่อ "บล็อก (Guard)" การโจมตีระดับสูงและระดับกลางของศัตรู
•    D-Pad Down: ย่อตัว / ก้มหลบ - สั่งให้ตัวละครย่อตัวต่ำ ใช้ก้มหลบหมัดหรือการโจมตีระดับสูง (High) และใช้บล็อกการโจมตีระดับต่ำ (Low)
•    L (Left Stick): เคลื่อนที่ - ขยับทิศทางของตัวละครทั่วไป หรือใช้โยกทิศทางในการเคลื่อนที่และเดินหน้าถอยหลัง
•    L1: สเปเชียลสไตล์ - กดเพื่อเปิด/ปิดโหมดช่วยเหลืออัจฉริยะ ช่วยให้กดคอมโบแ

Legacy exception: `None`; mode: `pipeline:multi_question_splitter`


### 36. Ring Fit Adventure utton confirmation for selecting an option

Key `6efd22288f8fd67b5959977ff028d3c0fac2523d146989f94c01eadffa2865eb` — first stage `understanding_and_model_admission`; confidence `probable`; decision `probable`

คำตอบR130:

The checking service is unavailable; this detail cannot be confirmed.

สาเหตุ: uttonในคำถามRingFitไม่ถูกกู้เป็นbuttonในnativeframe จึงไปC04แล้วโมเดลไม่พร้อม ข้อมูลcontrolมีอยู่ ต้องตรวจการกู้surfaceคำและสาเหตุadmissionแยกกัน คำตอบคือยังไม่ได้ตอบ ไม่ใช่factเกี่ยวกับปุ่มผิด

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Ring Fit Adventure controls:
- Joy-Con (R) Control Stick: Move cursor
- X Button: Confirm selection
- A Button: Cancel selection
- Ring-Con tilt: Move menu cursor
- Press Ring-Con inward: Confirm with Ring-Con
- Pull Ring-Con outward: Cancel with Ring-Con
Source: https://en-americas-support.nintendo.com/app/answers/detail/a_id/47833/~/how-do-i-control-the-game%3F-%28ring-fit-adventure%29

Legacy exception: `None`; mode: `pipeline:structured_game_controls_en`


### 37. How much does it cost for a general visiror to play Cockpit for 30 minutes and how do I boo

Key `adabcf3a2ca3d695a117988e02e1a5d00467f9748ec8580c159142c2058ab6f4` — first stage `needs_decomposition`; confidence `probable`; decision `probable`

คำตอบR130:

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
**Cockpit / PSU Student and Staff**
0 THB for 30 minutes [S1]
**Cockpit / PSU Alumni and General Student**
65 THB for 30 minutes [S2]
**Cockpit / General Adult**
200 THB for 30 minutes [S3]

สาเหตุ: คำถามท้ายhow do I booมีแนวโน้มถามbook แต่ไม่ได้เกิดbookingtask ส่วนราคาที่แสดง30นาทีต้องระบุว่าคิดminimumหนึ่งsession60นาทีตามกฎ ไม่สรุปว่าตัวเลขผิดก่อนตรวจbillingrule และคำว่าgeneral visirorยังต้องตรวจaudience

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Service prices (recorded package rates):

Cockpit — 60 minutes/package (1 person)
Requested duration: 30 minutes (0.5 hours); 1 session(s).
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 65 THB/package
• General adults: 200 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

Legacy exception: `None`; mode: `pipeline:structured_service_fee_conversation`


### 38. What is นายณัฐพนธ์ อินทรสังขนาวิน's roke

Key `a0092e36e5a400f295eb03605a158a30c213a1580d62316e1ca90caad975bcc8` — first stage `understanding_and_model_admission`; confidence `probable`; decision `probable`

คำตอบR130:

The checking service is unavailable; this detail cannot be confirmed.

สาเหตุ: ชื่อบุคคลมีในsource แต่rokeไม่ใช่roleตามsurface ระบบไปmodel/admissionแล้วไม่ตอบ ต้องแยกnamebindingจากroleintentและtransport ไม่สรุปว่าไม่มีperson record

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- นายณัฐพนธ์ อินทรสังขนาวิน: Committee member (กรรมการ)
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)

Legacy exception: `None`; mode: `pipeline:structured_members_source_th`


### 39. Hello, could you help? What conduct and etiquette do Tekken 8 tournament players follow?

Key `ed920c5962389f0a735cda26e46615e40a01037708c074b3858de0cc02e3ce19` — first stage `model_admission_or_transport`; confidence `confirmed_event`; decision `confirmed_event`

คำตอบR130:

The checking service is unavailable; this detail cannot be confirmed.

สาเหตุ: ถามconductTekkenที่มีruleclauses แต่terminalmodel_transport_failureและไม่ส่งfactsให้ผู้ใช้ ในsavedlegacycaseนี้ไม่มีคำตอบเช่นกัน จึงไม่ใช้Flowเดิมเป็นครูที่ถูกโดยอัตโนมัติ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`


### 40. ขอข้อมูลเรื่องคนอื่น ใช้ booking ขอรายละเอียดแบบสั้น ๆ

Key `94acbf684b8e3559c20eeab053cf8c1956d37ec6bbc4606e8dd59493d7dc6bc5` — first stage `evaluation_contract`; confidence `source_supported`; decision `source_supported`

คำตอบR130:

โอนสิทธิ์: ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้ [S1]

สาเหตุ: ข้อห้ามโอนสิทธิ์ตรงFAQและsavedlegacy ภายใต้scopeผู้รับสิทธิ์ภายนอกรายการจอง ไม่ขยายไปห้ามผู้เล่นร่วมที่ลงชื่อถูกต้องอยู่แล้ว คงvalidity/publicationreviewแยก

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Legacy exception: `None`; mode: `pipeline:structured_reservation_fact`

- `migrated_faq_rule_booking_non_transferable` rev4.answer: {"en": "A booking cannot be transferred to another person.", "th": "ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_9508764d24ffe87dcc11bafdb0e8"}]

### 41. ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ขอข้อมูลเรื่องคอมพิวเตอร์พัง

Key `a36b9e88ec74d2dbe7a01d75868bb6aca56e7f0450197e11b1884c4f400afb10` — first stage `understanding`; confidence `review_required`; decision `review_required`

คำตอบR130:

จอแตก: ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง [S1]

สาเหตุ: คำถามคอมพิวเตอร์พังกว้าง แต่เลือกpolicyความเสียหายร้ายแรงและชดเชยเต็ม บทความsourceมีจริงและFlowเดิมตอบแบบเดียวกัน ยังต้องแยกสาเหตุผู้ใช้ทำเสียกับเครื่องเสียเองก่อนยืนยันความเหมาะสมของpolicyที่ใช้

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Legacy exception: `None`; mode: `pipeline:category_rule_fast_path`

- `migrated_faq_rule_severe_damage` rev4.answer: {"en": "Severe damage such as broken screens, computer failure, unusable furniture, or unusable equipment requires full compensation based on the market price.", "th": "ความเสียหายร้ายแรง เช่น จอแตก คอมพิวเตอร์พัง เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_84760d29a4140c8d16b3e72d969c"}]
- `migrated_faq_rule_damage_responsibility` rev6.answer: {"en": "If equipment is damaged, users are responsible for fines or compensation depending on severity: minor damage is 100-500 THB, moderate damage is the actual cost or 500-2,000 THB, and severe damage requires full compensation for the property.", "th": "ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต็มจำนวน"} — [{"locator": "/mapped_fields/answer", "source_id": "r66_damage_translation_6ee8c58c68d5540952460906"}]

### 42. Could you please help me with this: Please retrieve the official RoV rulebook evidence for the rulebook scope and tournament identity

Key `e19a83adbd101ce3e83cf77511418342471c50be9b801bc76035562e65c48387` — first stage `rule_reader`; confidence `probable`; decision `probable`

คำตอบR130:

**Blueket Games 2025 Men's Team**
6. Misconduct and Penalties
6.1. No competitor shall engage in any of the following acts:
6.1.1. No player shall use inappropriate language or gestures, or make offensive remarks about others.
6.1.1.1. Penalty: Immediate game loss for any violation detected.
6.1.2. No competitor shall submit false results or manipulate outcomes.
6.1.2.1. Penalty: Immediate game loss and disqualification of the offending team from the competition upon detection of misconduct.
6.1.3. No team may allow any individual not listed on their official roster to participate in the competition. If it is discovered that a competitor’s name does not match the registered list, evidence must be recorded and the match shall be terminated immediately. However, if the match proceeds to completion, both teams shall be deemed to have consented to the participation; no appeals will be entertained by the organizing committee.
6.1.3.1. Penalty: Immediate game loss and disqualification of the offending team from the competition upon detection of misconduct.
6.1.4. No competitor may permit any other individual to play in their place during a match.
6.1.4.1. Penalty: Immediate game loss and disqualification of the offending team from the competition upon detection of misconduct.
6.1.5. No competitor shall consume, trade, or engage in any activity relating to narcotics, tobacco, weapons,

สาเหตุ: ถามscopeและidentityเอกสาร แต่ได้sectionบทลงโทษยาว แม้ชื่อรายการถูก ยังไม่เห็นว่าคำถามscopeได้รับคำตอบครบ traceแสดงevent_clause_dependency_readจึงต้องตรวจการเลือกtopic ไม่ใช่ถือsupportedว่าsemanticครบ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`

- `competition_competition_rules_rov_blueket_2025_men_section_011` rev4.text: {"en": "6. Misconduct and Penalties\n6.1. No competitor shall engage in any of the following acts:\n6.1.1. No player shall use inappropriate language or gestures, or make offensive remarks about others.\n6.1.1.1. Penalty: Immediate game loss for any violation detected.\n6.1.2. No competitor shall submit false results or manipulate outcomes.\n6.1.2.1. Penalty: Immediate game loss and disqualification of the offending team from the competition upon detection of misconduct.\n6.1.3. No team may allow any individual not listed on their official roster to participate in the competition. If it is discovered that a competitor’s name does not match the registered list, evidence must be recorded and the match shall be terminated immediately. However, if the match proceeds to completion, both teams shall be deemed to have consented to the participation; no appeals will be entertained by the organizing committee.\n6.1.3.1. Penalty: Immediate game loss and disqualification of the offending team fro — [{"locator": "/mapped_fields/text", "source_id": "r66_en_57f03020296e157988f38dbb"}]

### 43. ช่วยดูหน่อย กำลังจะลงแข่ง CS2 อยากรู้เรื่องขั้นตอนระหว่างการเเข่งขัน ครับ

Key `dc5e988db700686f3b77ba8bb6bc1235e95105659371e2cfe8e1cababd3715fb` — first stage `model_admission_or_transport`; confidence `confirmed_event`; decision `confirmed_event`

คำตอบR130:

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

สาเหตุ: ถามขั้นตอนระหว่างแข่งCS2 แต่โมเดลไม่พร้อมและไม่ตอบ ไม่ยืนยันว่าข้อมูลขั้นตอนหายจากterminalนี้

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`


### 44. Is thr stdio open 24 hours

Key `27adcc11a7e698ee95718e20f6da72ddb857dc944e9a29c32fff56495c4560e8` — first stage `evaluation_contract`; confidence `source_supported`; decision `source_supported`

คำตอบR130:

**24 hours**
**recorded source answer**: It is not open 24 hours. Use the service timeline instead: Monday morning 09:00-12:00 is Maintenance* and Monday afternoon 13:00-16:00 is open; Tuesday-Thursday are open in the regular slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable. [S1]

สาเหตุ: แม้stdio/openสะกดผิด คำตอบไม่เปิด24ชั่วโมงและตารางบริการตรงsourceFAQ เป็นตัวอย่างข้อที่มีสาระถูกแม้routeต่าง ไม่ยืนยันoccupancyหรืออาคารเปิดจริง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

The studio is not open 24 hours. Regular service periods are listed between 09:00 and 16:00 on weekdays, with maintenance periods on Monday morning and Friday afternoon.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Legacy exception: `None`; mode: `pipeline:structured_schedule_en`

- `migrated_faq_rule_schedule_not_24_hours` rev5.answer: {"en": "It is not open 24 hours. Use the service timeline instead: Monday morning 09:00-12:00 is Maintenance* and Monday afternoon 13:00-16:00 is open; Tuesday-Thursday are open in the regular slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable.", "th": "ไม่ได้เปิด 24 ชั่วโมง ให้ยึดตาม timeline การให้บริการ: วันจันทร์ (Monday) เช้า 09:00–12:00 เป็น Maintenance* และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิด 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_6f7240a74998f3490f9e83d16778"}]

### 45. What are the seven buttons in Gran Turismo 7?

Key `45854a28add95ce2327b3caef4e1307a173bc1f532c10d4e026ddfa5aec85feb` — first stage `constraint_extraction`; confidence `confirmed`; decision `confirmed_actual_content_failure`

คำตอบR130:

**Gran Turismo 7 / PlayStation / PS5**
| Input | Action |
|---|---|
| L (Left Stick) | Steer — Steering controls [S1] |
| R2 | Accelerate — Press to accelerate [S2] |
| L2 | Brake — Press to brake [S3] |
| Cross | Shift Up — Shift up gear (Manual mode) [S4] |
| Square | Shift Down — Shift down gear (Manual mode) [S5] |
| Circle | Hand Brake — Pull the handbrake to slide or drift. [S6] |
| Triangle | Reverse — Shift into reverse gear [S7] |
| D-Pad | MFD Controls — Switch and adjust Multi-Function Display settings such as Traction Control or Fuel Map [S8] |
| R1 | Change View — Switch camera angles during driving [S9] |
| L1 | Look Back — Switch camera angle to view rear momentarily [S10] |
| R3 | Nitro / Overtake — Use the boost system available in certain vehicles [S11] |
| L3 | Headlights — Toggle or flash headlights [S12] |
| Touch Pad | Flash Hazards — Activate hazard flashers [S13] |
| Options | Pause — Enter pause menu [S14] |
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.
Note: For realism, R2 and L2 use the DualSense controller’s Adaptive Triggers to simulate resistance from the accelerator and brake pedals.

สาเหตุ: ถามseven buttons แต่ตอบ14entriesโดยไม่ระบุว่าชุด7ปุ่มยังไม่ยืนยัน ตัวเลข7ในชื่อเกมไม่ใช่จำนวนที่ถาม และคำว่าsevenไม่ถูกเก็บในconstraints การเป็นcomplete_source_binding_setจึงไม่พิสูจน์ว่าครบตามrequest Flowเดิมก็ลิสต์14เช่นกัน ต้องวิจารณ์ทั้งสองฝั่ง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Gran Turismo 7 controls:
- L (Left Stick): Steer
- R2: Accelerate
- L2: Brake
- Cross: Shift Up
- Square: Shift Down
- Circle: Hand Brake
- Triangle: Reverse
- D-Pad: MFD Controls
- R1: Change View
- L1: Look Back
- R3: Nitro / Overtake
- L3: Headlights
- Touch Pad: Flash Hazards
- Options: Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/135

Legacy exception: `None`; mode: `pipeline:structured_game_controls_en`

- `controls_ps5_gran_turismo_7` rev7.bindings: [{"action": {"en": "Steer", "th": "เลี้ยว / ควบคุมพวงมาลัย"}, "button_label": {"en": "L (Left Stick)", "th": "L (Left Stick)"}, "buttons": ["L (Left Stick)"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Steering controls", "th": "บังคับทิศทางรถ"}, "section": {"en": null, "th": null}, "source_order": 1}, {"action": {"en": "Accelerate", "th": "คันเร่ง"}, "button_label": {"en": "R2", "th": "R2"}, "buttons": ["R2"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Press to accelerate", "th": "กดเพื่อเร่งเครื่อง"}, "section": {"en": null, "th": null}, "source_order": 2}, {"action": {"en": "Brake", "th": "เบรก"}, "button_label": {"en": "L2", "th": "L2"}, "buttons": ["L2"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Press to brake", "th": "กดเพื่อชะลอความเร็วรถ"}, "section": {"en": null, "th": null}, "source_order": 3}, {"action": {"en": "Shift Up", "th": "เพิ่มเกียร์"}, "button_label": {"en": "Cross", — [{"locator": "/bindings", "source_id": "r67_buttons_f9248d86fc4b7a02499b1b54"}]
- `controls_ps5_gran_turismo_7` rev7.limitations: {"en": "L (Left Stick) | Steer | Steering controls | \nR2 | Accelerate | Press to accelerate | \nL2 | Brake | Press to brake | \nCross | Shift Up | Shift up gear (Manual mode) | \nSquare | Shift Down | Shift down gear (Manual mode) | \nCircle | Hand Brake | Pull the handbrake to slide or drift. | \nTriangle | Reverse | Shift into reverse gear | \nD-Pad | MFD Controls | Switch and adjust Multi-Function Display settings such as Traction Control or Fuel Map | \nR1 | Change View | Switch camera angles during driving | \nL1 | Look Back | Switch camera angle to view rear momentarily | \nR3 | Nitro / Overtake | Use the boost system available in certain vehicles | \nL3 | Headlights | Toggle or flash headlights | \nTouch Pad | Flash Hazards | Activate hazard flashers | \nOptions | Pause | Enter pause menu | ", "th": "L (Left Stick) | เลี้ยว / ควบคุมพวงมาลัย | บังคับทิศทางรถ | \nR2 | คันเร่ง | กดเพื่อเร่งเครื่อง | \nL2 | เบรก | กดเพื่อชะลอความเร็วรถ | \nCross | เพิ่มเกียร์ | เปลี่ยนเกียร์สูงขึ้น — [{"locator": "/mapped_fields/limitations", "source_id": "r66_control_notes_4fc5d0ee66ca0b1220c61c7a"}]
- `controls_ps5_gran_turismo_7` rev7.source_coverage: "secondary_needs_manual_verify" — [{"locator": "/mapped_fields/source_coverage", "source_id": "r67_raw_ec8e70896afcc3455835d017c2"}]

### 46. Resident Evil Village ราคเท่าไหร่

Key `b59d525cecb3762f0833e0cd0d5c3f26aa2ef477da2b90d0aa7db6de53d95e24` — first stage `understanding_and_model_admission`; confidence `probable`; decision `probable`

คำตอบR130:

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

สาเหตุ: ราคสะกดขาดา ทำให้การอ่านราคาเกมที่สัมพันธ์บริการไม่ทำงานจนไปmodel/admission แม้savedlegacyจับเจตนาและอธิบายgame→serviceได้ ต้องแก้surface/intentโดยไม่ฝังราคาในโมเดล

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Resident Evil Village ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

PlayStation 5 Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน
PlayStation 5 1 ชั่วโมง (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท/1 ชั่วโมง
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/1 ชั่วโมง
•    บุคคลทั่วไป (General Adult): 150 บาท/1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

VR Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคา VR ทุกกลุ่มให้เทียบก่อน

VR 30 นาที (1-5 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท
•    บุคคลทั่วไป (General Adult): 525 บาท

VR 1 ชั่วโมง (1-5 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท
•    บุคคลทั่วไป (General Adult): 1,050 บาท
หมายเหตุ: คำถามยังไม่ระบุระยะเวลา จึงแสดงทั้งราคา 30 นาทีและ 1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-

Legacy exception: `None`; mode: `pipeline:structured_service_fee_by_game`


### 47. Which VR Zone units are free from 14:00 to 15:00 Please keep te answer concise

Key `aaab519016996e4c64b64ababa72fb005cded3514f5b8b8134d0089570284a62` — first stage `controlled_live_dependency`; confidence `confirmed_fixture`; decision `confirmed_fixture`

คำตอบR130:

For 2026-10-16 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

สาเหตุ: ถามVRเวลาชัดและfixtureถูกควบคุมunavailable การไม่ยืนยันว่างตรงscope Savedlegacyตอบunavailableเหมือนกันแต่clockเก่า จึงไม่ใช่providerจริงล่มหรือFlowใหม่ไม่เชื่อมlive

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

For 2026-10-14 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

Legacy exception: `None`; mode: `pipeline:live_booking_status_unavailable`


### 48. ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ช่วง 14:00-15:00 Nintendo Switch Zone เครื่องไหนว่างบ้าง

Key `302d49fb1d85fb7b944cfcb4feef2563cd7a62cd91fa8fbc29035c0758d8f108` — first stage `controlled_live_dependency`; confidence `confirmed_fixture`; decision `confirmed_fixture`

คำตอบR130:

วันที่ 2026-10-16 (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะการเชื่อมต่อระบบจองยังไม่พร้อมใช้งานครับ
ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

สาเหตุ: ถามNintendoช่วง14–15จริง เป็นlivefixtureเหมือนold ต่างวันอ้างอิง ต้องรักษาresourceและwindowโดยไม่อ้างผลmockเป็นสถานะจริง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

วันที่ 2026-10-14 (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะการเชื่อมต่อระบบจองยังไม่พร้อมใช้งานครับ
ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

Legacy exception: `None`; mode: `pipeline:live_booking_status_unavailable`


### 49. ช่วยอ้างอิงข้อมูลที่ยืนยันได้: คนนอกเข้าใช้เก้าอี้กับเครื่องเล่นได้ไหม

Key `19e27fae03c262703221d148d5cf27a65e64efd83308a0498a82f9cf9873bc91` — first stage `model_admission`; confidence `confirmed_event`; decision `confirmed_event`

คำตอบR130:

ระบบตีความคำถามไม่พร้อมชั่วคราว กรุณาลองอีกครั้งครับ

สาเหตุ: มีsourceการใช้บริการทั่วไปของคนนอก แต่requestนี้จบretryจากr101_model_unavailable ไม่ใช่sourceยืนยันว่าคนนอกใช้ไม่ได้ ยังต้องตรวจreadereligibilityก่อนfallback

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ได้ครับ บุคคลทั่วไปสามารถจองใช้บริการของศูนย์ได้ ค่าบริการขึ้นกับประเภทบริการและกลุ่มผู้ใช้ ต้องจองผ่านระบบและแสดงบัตรประชาชนเมื่อเช็กอิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Legacy exception: `None`; mode: `pipeline:protected_public_access`

- `r114_q037_owner_policy` rev1.answer: {"en": "External visitors may use all general studio services. Tournament eligibility is separate.", "th": "บุคคลภายนอกใช้บริการทั่วไปได้ทั้งหมด; ไม่ขยายไปเป็นคุณสมบัติแข่ง CS2 ซึ่งเอกสารกำหนดนักศึกษา PSU ภูเก็ต"} — [{"locator": "/fields/answer", "source_id": "r114_import_a11924b4cb9036660d34c1cc"}]

### 50. Could you check the studio information for me? Is Cockpit #01-#02 available right now

Key `21cdc3f63444f2532e372cd3ec64247d71c894c6874bfaf4c58c5b321c971ec3` — first stage `controlled_live_dependency`; confidence `confirmed_fixture`; decision `confirmed_fixture`

คำตอบR130:

For 2026-10-16 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

สาเหตุ: ถามCockpitตอนนี้ตรงlivepathและไม่ยืนยันslotจากfixtureoffline เหมาะกับเงื่อนไขทดสอบ ไม่ใช่คะแนนความพร้อมproviderจริง

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

For 2026-10-14 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

Legacy exception: `None`; mode: `pipeline:live_booking_status_unavailable`


### 51. Will VR Station be available tomorrow at 13:00

Key `f83e7aa62861d88b414adbfdbe5e35bf6b19db29a5bfd8b7208933ebb3a71580` — first stage `controlled_live_dependency`; confidence `confirmed_fixture`; decision `confirmed_fixture`

คำตอบR130:

For 2026-10-17 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

สาเหตุ: วันที่พรุ่งนี้คำนวณจากfixedclock2026-10-16เป็น10-17 ไม่เท่ากับวันนี้ที่ตรวจ และไม่ถือsavedlegacyที่clock10-14เป็นคำตอบวันที่ที่ต้องเลียนแบบ

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

For 2026-10-15 (Asia/Bangkok), I cannot confirm the live opening or booking status because the booking connection is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

Legacy exception: `None`; mode: `pipeline:live_booking_status_unavailable`


### 52. Under CS2 tournament rules, list the equiment that organizers provide.

Key `6b55634a8f5ecc0fd3f2efddcf577cce3445e749cefe737d4d1c18adfd64bda5` — first stage `model_admission_or_transport`; confidence `confirmed_event`; decision `confirmed_event`

คำตอบR130:

The checking service is unavailable; this detail cannot be confirmed.

สาเหตุ: sourceCS2section043ระบุPC/จอ/หูฟังไมค์/โต๊ะ/เก้าอี้ครบ แต่readerจบmodel_transport_failure savedlegacyเลือกclauseนี้ตรงคำถาม ตรวจแล้วเป็นsourceมีแต่การอ่านไม่สำเร็จ ไม่ใช่metadatawronggameทุกแถว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_043` rev4.text: {"en": "3. The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs.", "th": "3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_805e25f3040efc0d59084835"}]

### 53. Can I get a refund?

Key `f3055a6db384a10326720cf45e1390ec8cab8ab852122b9d744850d2190956df` — first stage `evaluation_contract`; confidence `source_supported`; decision `source_supported`

คำตอบR130:

In general, refunds are not issued except when the studio is at fault, such as equipment malfunction or force majeure that causes the center to close. [S1]

สาเหตุ: ข้อความrefundและข้อยกเว้นcenterfaultตรงsourceกับsavedlegacyในคำถามทั่วไปนี้ แต่ไม่ถือว่าครอบทุกscenarioเครดิต/โอนเกิน/เลื่อนวัน

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

In general, refunds are not issued except when the studio is at fault, such as equipment malfunction or force majeure that causes the center to close.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Legacy exception: `None`; mode: `pipeline:rule_en`

- `migrated_faq_rule_refund_policy` rev4.answer: {"en": "In general, refunds are not issued except when the studio is at fault, such as equipment malfunction or force majeure that causes the center to close.", "th": "โดยทั่วไปไม่มีการคืนเงิน ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_974b1159a0b7bb3c763706bf7278"}]

### 54. What does the L3 button do in Call of Duty: Modern Warfare III on PlayStation / PS5

Key `439fa27aa2aa79065ecd4218780c07b0b05aeafff6cce3d3e9376f13a7142d54` — first stage `evaluation_contract`; confidence `source_supported`; decision `source_supported`

คำตอบR130:

**Call of Duty: Modern Warfare III / PlayStation / PS5**
- **Sprint/Tactical Sprint/Focus**: L3 — Press to sprint faster or hold breath while aiming sniper scope [S1]
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.
Note: This layout moves the jump and slide buttons so players can move while aiming with the analog stick without lifting their thumb.

สาเหตุ: L3ของModernWarfareIIIตรงbindingในsourceและsavedlegacy พร้อมคำเตือนsecondarysource/installedpreset ข้อroutefailไม่ใช่ข้อผิดด้านปุ่ม

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Call of Duty: Modern Warfare III controls:
- L3: Sprint/Tactical Sprint/Focus
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.gamepur.com/guides/best-modern-warfare-3-controller-settings-aim-assist-deadzones-button-layout

Legacy exception: `None`; mode: `pipeline:structured_game_controls_en`

- `controls_ps5_call_of_duty_modern_warfare_iii` rev7.bindings: [{"action": {"en": "Jump/Mantle", "th": "กระโดด / ปีนป่าย"}, "button_label": {"en": "L1", "th": "L1"}, "buttons": ["L1"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Jump over obstacles (Bumper Jumper's standout feature)", "th": "กระโดดข้ามสิ่งกีดขวาง (จุดเด่นของ Bumper Jumper)"}, "section": {"en": null, "th": null}, "source_order": 1}, {"action": {"en": "Change Stance/Slide/Dive", "th": "เปลี่ยนท่า / สไลด์ / พุ่งหลบ"}, "button_label": {"en": "R3", "th": "R3"}, "buttons": ["R3"], "context": {"en": null, "th": null}, "gesture": "unknown", "notes": {"en": "Slide or dash while running by pressing or holding down (Tactical's standout feature)", "th": "กดหรือกดค้างขณะวิ่งเพื่อสไลด์หรือพุ่ง (จุดเด่นของ Tactical)"}, "section": {"en": null, "th": null}, "source_order": 2}, {"action": {"en": "Use Tactical Equipment", "th": "ใช้อุปกรณ์ยุทธวิธี"}, "button_label": {"en": "Cross", "th": "Cross"}, "buttons": ["Cross"], "context": {"en": null, "th": null}, "gesture": " — [{"locator": "/bindings", "source_id": "r67_buttons_3dd70161cb3b5a7a53dd24e7"}]
- `controls_ps5_call_of_duty_modern_warfare_iii` rev7.limitations: {"en": "L1 | Jump/Mantle | Jump over obstacles (Bumper Jumper's standout feature) | \nR3 | Change Stance/Slide/Dive | Slide or dash while running by pressing or holding down (Tactical's standout feature) | \nCross | Use Tactical Equipment | Use flashbang or stun grenade | \nCircle | Melee | Use knife to slash or kick enemy with the rifle butt | \nL2 | Aim Down Sight | Hold to raise weapon and aim | \nR2 | Fire Weapon | Press fire | \nR1 | Use Lethal Equipment | Throw hand grenade, incendiary or knife | \nSquare | Interact/Reload | Reload weapon or collect item | \nTriangle | Switch Weapon | Switch primary and secondary weapon | \nL3 | Sprint/Tactical Sprint/Focus | Press to sprint faster or hold breath while aiming sniper scope | ", "th": "L1 | กระโดด / ปีนป่าย | กระโดดข้ามสิ่งกีดขวาง (จุดเด่นของ Bumper Jumper) | \nR3 | เปลี่ยนท่า / สไลด์ / พุ่งหลบ | กดหรือกดค้างขณะวิ่งเพื่อสไลด์หรือพุ่ง (จุดเด่นของ Tactical) | \nCross | ใช้อุปกรณ์ยุทธวิธี | ปาระเบิดแฟลชหรือสตัน | \nCircle | โจมตีประชิ — [{"locator": "/mapped_fields/limitations", "source_id": "r66_control_notes_b809d625d0c5c1f8a4c1fd84"}]
- `controls_ps5_call_of_duty_modern_warfare_iii` rev7.source_coverage: "secondary_needs_manual_verify" — [{"locator": "/mapped_fields/source_coverage", "source_id": "r67_raw_1b6b9f8a464ada69a0e614cb2c"}]

### 55. Before visiting, I need to know: Would I owe compensation for damaging a gaming mouse?

Key `9749c57fb492f9b003462acb9a482e6b10c85e2761e243e5a13535e80233bd41` — first stage `predicate_selection`; confidence `confirmed`; decision `confirmed_actual_content_failure`

คำตอบR130:

**confirmed answer**: The PC Zone has 10 Gaming Monitors, 10 Gaming Chairs, Gaming Keyboards, Gaming Headsets, Gaming Mice, and 10 MSI MAG Infinite S3 14th Gaming PCs. [S1]

สาเหตุ: ถามชดเชยความเสียหายgamingmouse แต่fallbackเลือกequipmentinventoryPCzone ไม่ตอบความรับผิดชอบ แม้factsรายการอุปกรณ์ถูกต้อง มีกฎdamage_responsibilityในsourceและsavedlegacyตอบตรง predicate ต้องตรวจactionก่อนหยิบชื่ออุปกรณ์

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

If equipment is damaged through improper or negligent use, users are responsible according to severity: minor damage carries a 100-500 THB fine; moderate damage costs the actual repair amount or 500-2,000 THB; severe damage requires full compensation based on the property's market value.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

Legacy exception: `None`; mode: `pipeline:protected_damage_responsibility`

- `migrated_faq_rule_equipment_pc_zone` rev4.answer: {"en": "The PC Zone has 10 Gaming Monitors, 10 Gaming Chairs, Gaming Keyboards, Gaming Headsets, Gaming Mice, and 10 MSI MAG Infinite S3 14th Gaming PCs.", "th": "ใน PC Zone มี Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Headset, Gaming Mouse และ Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_69cc7bc988c828da68ddfe3d5513"}]
- `migrated_faq_rule_damage_responsibility` rev6.answer: {"en": "If equipment is damaged, users are responsible for fines or compensation depending on severity: minor damage is 100-500 THB, moderate damage is the actual cost or 500-2,000 THB, and severe damage requires full compensation for the property.", "th": "ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต็มจำนวน"} — [{"locator": "/mapped_fields/answer", "source_id": "r66_damage_translation_6ee8c58c68d5540952460906"}]

### 56. What is ผศ.ดร.ณัฐพงศ์ ทองเทพ's role

Key `000520a444d45c2d201e84d1ea7640b0e5c742388dea01515dc4be324ab89226` — first stage `evaluation_contract`; confidence `source_supported`; decision `source_supported`

คำตอบR130:

According to the recorded source profile:
**ผศ.ดร.ณัฐพงศ์ ทองเทพ**
**role**: Assistant to the president for academic affairs [S1]

สาเหตุ: ชื่อและroleตรงrecord/sourceและsavedlegacy ไม่อ้างสถานะดำรงตำแหน่งปัจจุบันนอกvalidityที่ยืนยัน

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: Assistant to the President for Academic Affairs (ผู้ช่วยอธิการบดีฝ่ายวิชาการ) - Prince of Songkla University, Phuket Campus
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)

Legacy exception: `None`; mode: `pipeline:structured_members_source_th`

- `member_832e24bbcd11737e` rev5.role: {"en": "Assistant to the president for academic affairs", "th": "ผู้ช่วยอธิการบดีฝ่ายวิชาการ"} — [{"locator": "/mapped_fields/role", "source_id": "r66_person_review_ae8ab02be3c7a29b0d5ee850"}]

### 57. What position does Assoc. Prof. Dr. Nattapon Tongthes play

Key `b72e8ca2d15894d09a2a5362a6f7a968b301ff149c513a070a4985721a72b536` — first stage `entity_binding`; confidence `review_required`; decision `review_required`

คำตอบR130:

The requested game, machine or topic is not identified. Please specify the target.

สาเหตุ: ชื่ออังกฤษNattaponTongthesไม่ตรงชื่อที่ยืนยัน การถามชื่อที่แน่นอนมีเหตุผล Savedlegacyก็ไม่รับรองคนนี้ จึงไม่ควรบังคับจับชื่อใกล้เพื่อให้ผ่านgold ข้อความถามเกม/เครื่องเป็นUXไม่ตรงdomain

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

I could not verify a member record for Assoc. Prof. Dr. Nattapon Tongthes play. Please provide the exact name from the official member directory; I cannot infer an official identity from an unverified English spelling.

Legacy exception: `None`; mode: `pipeline:member_person_not_found_en`


### 58. ช่วยอ้างอิงข้อมูลที่ยืนยันได้: แขกจากมหาวิทยาลัยอื่นมีสิทธิ์จองไหม

Key `934b6162fa5dd7fe4221bd6d5fe8d639f6e39a9000f4f2f4d1f9db2912f18b04` — first stage `entity_binding_then_intent_override`; confidence `confirmed`; decision `confirmed_actual_content_failure`

คำตอบR130:

**Gaming Monitor**
**การใช้งาน**
- จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone
- ใช้งานพร้อมเครื่อง PC ที่จองไว้ โดยปกติผู้ใช้ไม่ต้องตั้งค่าฮาร์ดแวร์เอง หากจอหรือภาพมีปัญหาควรแจ้งเจ้าหน้าที่
- แสดงผลเกมและโปรแกรมบน PC Zone [S1]

สาเหตุ: จอในจองจับaliasจอภาพ ทำให้native_inventory_presence_recordเลือกequipmentusage แล้วตอบGamingMonitorแทนสิทธิ์คนนอกจอง มีกฎr114_q037_owner_policyยืนยันบริการทั่วไป และsavedlegacyตอบeligibilityตรงเรื่อง เป็นsource/predicatefailureที่ทำงานก่อนเรียกโมเดล

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

จองได้ครับ บุคคลทั่วไปสามารถจองบริการของศูนย์ผ่านระบบออนไลน์ล่วงหน้าอย่างน้อย 1 ชั่วโมง ชำระค่าบริการตามที่ระบบแจ้งภายใน 10 นาที และแสดงบัตรประชาชนเมื่อเช็กอิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

Legacy exception: `None`; mode: `pipeline:protected_public_access`

- `equipment_gaming_monitor` rev6.specifications: [{"key": "zone", "unit": null, "value": "PC Zone"}, {"key": "quantity", "unit": null, "value": "10 Units"}] — [{"locator": "/mapped_fields/specifications", "source_id": "r63_5af80ccff359cadb665af2160ab0"}]
- `r114_q037_owner_policy` rev1.answer: {"en": "External visitors may use all general studio services. Tournament eligibility is separate.", "th": "บุคคลภายนอกใช้บริการทั่วไปได้ทั้งหมด; ไม่ขยายไปเป็นคุณสมบัติแข่ง CS2 ซึ่งเอกสารกำหนดนักศึกษา PSU ภูเก็ต"} — [{"locator": "/fields/answer", "source_id": "r114_import_a11924b4cb9036660d34c1cc"}]

### 59. Could you plaese help me with this: I am planning a visit and need to know: Who manages the studio

Key `22b8cace486a354fd5f325db81beed0005334fa6141fe846bfcc9638ae8e6be9` — first stage `no_confirmed_failing_stage`; confidence `review_required`; decision `review_required`

คำตอบR130:

The studio was established by Prince of Songkla University and is operated by the College of Computing. [S1]

สาเหตุ: Who manages the studioอาจถามหน่วยงานหรือบุคคล ระบบกับsavedlegacyตอบCollegeofComputingเหมือนกันและsourceรองรับoperator จึงยังไม่ตัดสินผิดคนโดยไม่มีบริบทเพิ่ม

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

The studio was established by Prince of Songkla University and is operated by the College of Computing.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

Legacy exception: `None`; mode: `pipeline:rule_en`

- `migrated_faq_rule_en_overview_operator` rev4.answer: {"en": "The studio was established by Prince of Songkla University and is operated by the College of Computing.", "th": "ศูนย์ก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_4a102ab45603aa61c74632624b8c"}]

### 60. ขอขอมูลเรื้องเช่า notebook กลับบ้าน

Key `5f7c86238075717ae274dd067b0f76e6bab6e973b20efb07a40f78b942aeb787` — first stage `service_scope_selection`; confidence `confirmed`; decision `confirmed_actual_content_failure`

คำตอบR130:

ต้องการเหมาโซนใด สำหรับหน่วยงานภายในหรือภายนอก และครึ่งวันหรือเต็มวันครับ?

สาเหตุ: ผู้ใช้ระบุnotebookกลับบ้าน แต่ถามต่อว่าจะเหมาโซนใด แสดงว่าoffsiteequipmentถูกเปลี่ยนเป็นonsitevenueแม้ยังไม่ให้ราคา ไม่มีsourceให้สรุปบริการเช่ากลับบ้าน ควรบอกส่วนที่ไม่ยืนยันตรงitem

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

ราคาเช่าเหมาโซนสำหรับหน่วยงาน

ยังไม่มีราคาเช่าเหมาในไฟล์สำหรับรายการที่ระบุ: notebook กลับบ้าน

อัตรานี้เป็นราคาเช่าเหมาโซนของหน่วยงาน ไม่ใช่ราคาต่อผู้เล่น/เครื่อง ไฟล์ไม่ได้ระบุจำนวนชั่วโมงของช่วงเช่าหรือวันที่มีผลของอัตรา

แหล่งข้อมูล: ไฟล์ค่าบริการครึ่งวันและเต็มวันที่ผู้ใช้ส่งให้
local://service_fee/zone_rental_fees_20261006

Legacy exception: `None`; mode: `pipeline:zone_rental_fee`


### 61. PS5 Zone เหมาะกับเกมแนวไหน

Key `3f00783cc8b1161e1d229abad00231f290a1d9493c9e18f9ea1d2781690ec50c` — first stage `model_admission_or_transport`; confidence `confirmed_event`; decision `confirmed_event`

คำตอบR130:

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

สาเหตุ: คำว่าเหมาะเป็นrecommendationไม่ใช่เหมา sourceยังต้องแยกรายการ/genreจากคำแนะนำที่ยืนยัน การไม่ตอบในrequestนี้เป็นmodel_transport_failure ไม่ใช้เป็นหลักฐานว่าrentalreaderขาด

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

None

Legacy exception: `NameError:name 'ownership_blocked' is not defined`; mode: `None`


### 62. ถ้าแนบสลิปผิดต้องทำยังไง

Key `94170c022b12c3e843f10e9c5df599f9d34539628fc2762c8ef6f989ead4684e` — first stage `evaluation_contract`; confidence `source_supported`; decision `source_supported`

คำตอบR130:

แนบสลิปผิดรูป เปลี่ยนได้ไหม?: กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket [S1]

สาเหตุ: คำตอบส่งสลิปทางเพจตรงownerclaimและsavedlegacy ใช้URLตามsource ไม่ได้ตรวจavailabilityของFacebookสด

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

Legacy exception: `None`; mode: `pipeline:user_service_facts`

- `migrated_owner_claim_wrong_slip` rev3.answer: {"en": "If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket", "th": "กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket"} — [{"locator": "/mapped_fields/answer", "source_id": "r63_784ae09334e8fba45ef84850d4b5"}]

### 63. How many technical pauses and minutes per pause are allowed in the CS2 tournament?

Key `1b22d51eddf1b41db74ffa7349ce0dbe843e90829388159ace9977e63692291e` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_033` rev4.text: {"en": "3. Technical pauses: 2 per team, no more than 10 minutes each. Any issue must be reported to the referee immediately.", "th": "3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_ae638f788a7e221da1e62d48"}]

### 64. How many technical pauses and minutes per pause are allowed in the CS2 tournamment?

Key `e4bea8ad9ae377ad7401869f64733087b705e826cfc3db5d2cd57b8415f8138e` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_033` rev4.text: {"en": "3. Technical pauses: 2 per team, no more than 10 minutes each. Any issue must be reported to the referee immediately.", "th": "3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_ae638f788a7e221da1e62d48"}]

### 65. Who may file a CS2 tournament protest and within how many minutes?

Key `8f4fc4a116a8f9f276750722d9d2f8062197fd55bce28fcddbc704cd44f79656` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_058` rev4.text: {"en": "2. Objections must be submitted within 15 minutes after the match ends, by only the team captain or coach.", "th": "2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_df3808751da331f7901b1885"}]

### 66. สอบถามหน่อยครับ กติกา CS2 ปรับ Brightness Resolution Crosshair ได้ไหมและปรับที่ไหน ครับ

Key `4b72528ef2d7044c1a78c5842694d1c6e6a97214bb934d14588155b6bca197de` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

คำตอบ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_045` rev4.text: {"en": "1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively.", "th": "1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_b047d5c279fb07535dedd2f9"}]

### 67. Could you help me? Under CS2 tournament rules, are scripts or macros allowed?

Key `56cc3e8baa62279c21f71c3ff28b57cb4c966edb072bfc1cd667f2a5f3d3c278` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: No scripts or macros are allowed at all.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_046` rev4.text: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_8300d64c56c48ebbb8d8d003"}]

### 68. สอบถามหน่อยครับ กติกา CS2 ปรับ Brightness Resolution Crosshair ที่ไหน แล้วใช้สคริปต์หรือมาโครได้ไหม ครับ

Key `216d0c21fd4c3fde9419196b2bb44d64bd2909992d28fcfde864d78898925d81` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

คำตอบ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

รายละเอียดที่เกี่ยวข้อง:
•    3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_045` rev4.text: {"en": "1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively.", "th": "1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_b047d5c279fb07535dedd2f9"}]

### 69. Hello, could you help? How many technical pauses and minutes per pause are allowed in the CS2 tournament?

Key `a973f24f00781857c4aa97c8c16676cce715f609c031bc1aec3e04bfa25b10ce` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_033` rev4.text: {"en": "3. Technical pauses: 2 per team, no more than 10 minutes each. Any issue must be reported to the referee immediately.", "th": "3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_ae638f788a7e221da1e62d48"}]

### 70. Under CS2 tournamment ruls, are scripts or macros allowed?

Key `3a56419e962770e45628b70609c39e612cfecda7fcef289f146ec1993c5670fd` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: No scripts or macros are allowed at all.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_046` rev4.text: {"en": "3. Strictly prohibited to use scripts or macros.", "th": "3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_8300d64c56c48ebbb8d8d003"}]

### 71. Who may file a CS2 tournamment protest and within how many minutes?

Key `c3f2e89e360122ec401f4b96a045006b45fbdce84cf35e680eaf3ed99559d6af` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_058` rev4.text: {"en": "2. Objections must be submitted within 15 minutes after the match ends, by only the team captain or coach.", "th": "2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_df3808751da331f7901b1885"}]

### 72. Hello, could you help? Who may file a CS2 tournament protest and within how many minutes?

Key `aaa3765033af915f411c67becefbe13be9850a23d7e381ec4ff1b1eba108ac31` — first stage `substantive_verifier`; confidence `confirmed_source_and_trace`; decision `confirmed_actual_content_failure`

คำตอบR130:

Related records exist, but the requested detail is not established.

สาเหตุ: ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว

คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):

Answer: Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

Legacy exception: `None`; mode: `pipeline:competition_rule_detail_source`

- `competition_competition_rules_cs2_psu_phuket_2026_section_058` rev4.text: {"en": "2. Objections must be submitted within 15 minutes after the match ends, by only the team captain or coach.", "th": "2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น"} — [{"locator": "/mapped_fields/text", "source_id": "r66_en_df3808751da331f7901b1885"}]

## ลำดับแก้ที่ได้จากการวินิจฉัย

เริ่มbindingและpredicate gateที่ให้sourceผิดเรื่อง, แก้C13scope/clause/verifier, reconcileanaphorและconstraints, แล้วแก้protocol/admission/latencyควบคู่กับsourceauthorityที่ยังreview แต่ละงานต้องมีcaseและacceptance ไม่แก้จากชื่อterminalเพียงอย่างเดียว งานรอบนี้ยังเป็นวินิจฉัยจึงไม่เปลี่ยนfrozenR130

## แผน10%ที่ตรึงก่อนยิงคำถาม

เลือก2111unique requests/5584gradesจากFULL_JOBSเดิม 10%ปัดขึ้นทุกoriginalstratumและเติมหมวดตามinputให้ครบC01–C14 ไม่มีคำถามใหม่ ไม่เลือกตามคะแนน/ผลตอบ ได้มากกว่า10%บางหมวดเพราะการปัดขึ้น/คำถามหลายหมวด

| หมวด | ประชากรตามinput | จำนวนที่เลือกในหมวด | หมายเหตุ |
|---|---:|---:|---|
| C00 ทั่วไป/กำกวม/นอกขอบเขต | 1048 | 111 | membershipsซ้อนทับได้ |
| C01 ศูนย์/ติดต่อ | 1266 | 135 | membershipsซ้อนทับได้ |
| C02 บุคลากร | 796 | 81 | membershipsซ้อนทับได้ |
| C03 อุปกรณ์ | 1568 | 172 | membershipsซ้อนทับได้ |
| C04 เกม | 4617 | 475 | membershipsซ้อนทับได้ |
| C05 การควบคุม | 2228 | 223 | membershipsซ้อนทับได้ |
| C06 ราคาปกติ | 1880 | 197 | membershipsซ้อนทับได้ |
| C07 เหมา | 6 | 1 | membershipsซ้อนทับได้ |
| C08 จอง | 3969 | 414 | membershipsซ้อนทับได้ |
| C09 ชำระเงิน | 92 | 10 | membershipsซ้อนทับได้ |
| C10 กฎศูนย์ | 1546 | 166 | membershipsซ้อนทับได้ |
| C11 ตาราง | 2346 | 246 | membershipsซ้อนทับได้ |
| C12 สถานะจริง | 1106 | 113 | membershipsซ้อนทับได้ |
| C13 แข่งขัน | 4508 | 452 | membershipsซ้อนทับได้ |
| C14 ข่าว/กิจกรรม | 63 | 11 | membershipsซ้อนทับได้ |

ข้อจำกัดสำคัญ: C07มีเพียง6คำถามในfullinputเดิมและส่วนใหญ่ถามoffsite; เลือก1ตามceil10%ยังไม่ยืนยันคุณภาพราคาเหมาonsiteทั้งหมด C14ไม่มีrealnewsrecords การไม่ยืนยันข้อมูลล่าสุดต้องแยกจากreaderเสีย ไม่อ้างว่าทั้ง14หมวดผ่านเพราะมีsample

sample01จะใช้R130เดิม/retained/base/2workers/clock/budget/livefixtureเดิม เป็นการตรวจความเกิดซ้ำและความต่างของdiagnostic ไม่ใช่post-fix improvementหรือfreshholdout ไม่มีlegacy inference/regradingใหม่

## หลักฐาน

- CASE_DIAGNOSTICS_REVIEWED.jsonl.gz: ทุก20,554keysพร้อมobservedmechanismsและsemanticstatusที่ไม่เดา
- INDIVIDUAL_SOURCE_REVIEW.json: คำตัดสินรายกรณี/firststage/confidence/source/savedoldtrace
- SOURCE_CAUSAL_EVIDENCE.json: source77+recordsตามcaseและbody/locator/revision
- DETERMINISTIC_CAUSAL_PROBES.json:8localcodeprobes ไม่มีHTTP/model requests
- ROOT_CAUSE_REGISTER.json / ISSUE_COUNTS.json: สาเหตุที่reviewแล้วแยกจากcohortอาการทั้งหมด
- SELECTION_FREEZE.json / SAMPLE_ALLOCATION.json: วิธีเลือกและhashก่อนทดสอบ

การทำข้อ2ระดับวินิจฉัยทุกกลุ่มและcase ledgerครบ ไม่เท่ากับsemanticjudgmentทุก20,554คำตอบ รายการที่ยังไม่ยืนยันคงreview_required และไม่ประกาศFlowครบ100%
