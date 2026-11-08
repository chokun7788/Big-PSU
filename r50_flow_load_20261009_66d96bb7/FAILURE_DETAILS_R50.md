# คำถามที่ผิดก่อนแก้และคำตอบหลังแก้ r50

### th-roster-cs2

- คำถาม: สมาชิกทีม CS2 ต้องมีกี่คน
- ก่อนแก้: `pipeline:service_fact_scope_clarification` — เงื่อนไขสมาชิกของศูนย์ใช้แทนข้อกำหนดบัญชีเกมหรือสมาชิกทีมไม่ได้ครับ ต้องตรวจข้อกำหนดของบัญชีเกมหรือรายการแข่งขันนั้นแยกกัน
- หลังแก้: `pipeline:competition_rule_detail_source` — คำตอบ: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- เกณฑ์ที่ไม่ผ่านก่อนแก้: content, rule_target

### th-roster-valo-gap

- คำถาม: สมาชิกทีม VALORANT ต้องมีกี่คน
- ก่อนแก้: `pipeline:service_fact_scope_clarification` — เงื่อนไขสมาชิกของศูนย์ใช้แทนข้อกำหนดบัญชีเกมหรือสมาชิกทีมไม่ได้ครับ ต้องตรวจข้อกำหนดของบัญชีเกมหรือรายการแข่งขันนั้นแยกกัน
- หลังแก้: `pipeline:competition_facet_not_covered_no_answer` — ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- เกณฑ์ที่ไม่ผ่านก่อนแก้: explicit_source_gap

### th-team-timeout

- คำถาม: VALORANT ทีมขอเวลานอกได้กี่ครั้ง
- ก่อนแก้: `pipeline:no_answer` — ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ
- หลังแก้: `pipeline:competition_rule_detail_source` — คำตอบ: ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- เกณฑ์ที่ไม่ผ่านก่อนแก้: content, rule_target

### th-different-date-guard

- คำถาม: ที่จอดรถศูนย์ที่กรุงเทพมีไหม
- ก่อนแก้: `pipeline:user_service_facts` — มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
- หลังแก้: `pipeline:service_fact_scope_clarification` — ข้อมูลบริการที่ยืนยันเป็นของ PSU Esports Studio วิทยาเขตภูเก็ต ยังใช้ยืนยันที่จอดรถของศูนย์ในกรุงเทพไม่ได้ครับ
- เกณฑ์ที่ไม่ผ่านก่อนแก้: no_phuket_parking

### en-roster-cs2

- คำถาม: How many members are in a CS2 team?
- ก่อนแก้: `pipeline:service_fact_scope_clarification` — Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.
- หลังแก้: `pipeline:competition_rule_detail_source` — Answer: Team composition Each team consists of 5 players

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
- เกณฑ์ที่ไม่ผ่านก่อนแก้: content, rule_target

### en-roster-valo-gap

- คำถาม: How many members are in a VALORANT team?
- ก่อนแก้: `pipeline:service_fact_scope_clarification` — Studio membership requirements do not establish game-account or team membership requirements. Please specify the account service or competition rule you want to check.
- หลังแก้: `pipeline:competition_facet_not_covered_no_answer_en` — I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- เกณฑ์ที่ไม่ผ่านก่อนแก้: explicit_source_gap

### en-different-date-guard

- คำถาม: Is there parking in Bangkok?
- ก่อนแก้: `pipeline:user_service_facts` — Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
- หลังแก้: `pipeline:service_fact_scope_clarification` — The verified service facts cover PSU Esports Studio in Phuket. They do not confirm parking in Bangkok.
- เกณฑ์ที่ไม่ผ่านก่อนแก้: no_phuket_parking
