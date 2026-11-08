# Failure reasonทุกชนิดที่พบ

นับgradeevents ข้อหนึ่งมีได้หลายreason รายการนี้เก็บexactstrings ไม่ใช่เพียง8bucketของรายงานR64


## legacy_offline

| จำนวน | reasonตามraw |
|---:|---|
| 5894 | pipeline_exception |
| 2702 | route:game_controls expected:['games'] |
| 690 | status:no_answer expected:answer_available |
| 621 | status:clarification expected:answer_available |
| 396 | route:service_fee expected:['equipment', 'games', 'multi_question', 'reservation'] |
| 348 | route:no_answer expected:['general', 'knowledge'] |
| 308 | route:schedule expected:['reservation'] |
| 222 | legacy_mode_prefix:['pipeline:structured_game_controls'] |
| 161 | status:answer expected:clarification_required |
| 151 | status:answer expected:no_answer_expected |
| 130 | status:no_answer expected:localization_pending |
| 105 | status:clarification expected:no_answer_expected |
| 97 | legacy_mode_prefix:['pipeline:competition_fact_card'] |
| 96 | route:clarification expected:['service_fee'] |
| 94 | route:knowledge expected:['general', 'overview', 'home'] |
| 93 | route:contact expected:['competition_rules'] |
| 89 | retrieval evidence did not match the allowed canonical fact/rule IDs |
| 86 | route:service_fee expected:['multi_question', 'reservation', 'games', 'equipment'] |
| 80 | route:clarification expected:['reservation'] |
| 74 | route:input_guard expected:['clarification', 'general', 'no_answer', 'unknown'] |
| 72 | missing required: 2 sessions |
| 68 | route:clarification expected:['no_answer', 'overview', 'rules'] |
| 66 | missing all alternatives: ['latency', 'หน่วง'] |
| 62 | route:reservation expected:['members', 'overview'] |
| 61 | missing required: English localization |
| 60 | missing all alternatives: ['เฟรม', 'ความละเอียด'] |
| 59 | missing all alternatives: ['server', 'client'] |
| 58 | intent:conversation_price_lookup expected:service_fee_query |
| 57 | missing all alternatives: ['GPU', 'กราฟิก'] |
| 57 | missing all alternatives: ['คีย์บอร์ด', 'mechanical'] |
| 56 | route expected ['competition_rules'], got contact |
| 55 | missing all alternatives: ['กิจกรรม'] |
| 54 | missing all alternatives: ['API', 'เชื่อมต่อ'] |
| 54 | missing all alternatives: ['ขอบคุณ'] |
| 54 | status:answer expected:live_lookup_required |
| 51 | route:reservation expected:['overview'] |
| 49 | route:service_fee expected:['multi_question'] |
| 47 | missing all alternatives: ['จอง'] |
| 47 | route:clarification expected:['members', 'overview'] |
| 44 | missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026'] |
| 43 | route:clarification expected:['competition_rules'] |
| 43 | route:clarification expected:['games'] |
| 41 | missing required: psuesportspkt@gmail.com |
| 38 | missing rulebook target(s): ['competition_rules_valorant_psu_phuket_2026'] |
| 35 | missing required: Verified game catalog |
| 35 | route:clarification expected:['no_answer'] |
| 31 | first_line_off_topic |
| 29 | status:clarification expected:localization_pending |
| 28 | route:no_answer expected:['penalty', 'rules'] |
| 27 | missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา'] |
| 25 | route:no_answer expected:['overview'] |
| 24 | latency_ceiling |
| 24 | legacy_english_thai_prose_flag |
| 24 | status:no_answer expected:clarification_required |
| 23 | route:games expected:['competition_rules'] |
| 22 | missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible'] |
| 21 | route:clarification expected:['games', 'reservation'] |
| 20 | route:clarification expected:['reservation', 'schedule'] |
| 20 | route:contact expected:['rules', 'no_answer', 'clarification'] |
| 19 | route:knowledge expected:['general', 'clarification', 'no_answer', 'overview'] |
| 18 | missing all alternatives: ['ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน'] |
| 18 | missing all alternatives: ['เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง'] |
| 18 | missing required: not connected |
| 18 | route:clarification expected:['games', 'service_fee'] |
| 18 | route:reservation expected:['competition_rules'] |
| 18 | route:schedule expected:['no_answer'] |
| 17 | route:game_controls expected:['games', 'no_answer'] |
| 16 | legacy_mode_prefix:['pipeline:multi_question_splitter'] |
| 16 | route:clarification expected:['general', 'knowledge'] |
| 16 | route:input_guard expected:['general', 'unknown', 'clarification', 'no_answer'] |
| 16 | route:schedule expected:['competition_rules'] |
| 15 | route:service_fee expected:['no_answer'] |
| 15 | route_mismatch |
| 15 | wrong_game_evidence |
| 14 | missing all alternatives: ['ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม'] |
| 14 | route:games expected:['clarification', 'equipment'] |
| 14 | route:games expected:['no_answer'] |
| 14 | route:general expected:['penalty'] |
| 14 | route:general expected:['reservation'] |
| 13 | route:clarification expected:['contact'] |
| 13 | route:clarification expected:['overview'] |
| 13 | route:no_answer expected:['reservation'] |
| 12 | missing all alternatives: ['Gaming PC รุ่น MSI MAG Infinite S3 14th'] |
| 12 | missing all alternatives: ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก'] |
| 12 | route expected ['competition_rules'], got clarification |
| 12 | wrong_category |
| 12 | wrong_game_source |
| 11 | intent:game_list expected:list |
| 11 | missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'หันมองจุดสนใจ'] |
| 11 | missing all alternatives: ['PlayStation 5', 'PlayStation 5 #01-#02'] |
| 11 | route:no_answer expected:['competition_rules'] |
| 10 | missing all alternatives: ['PC #03-#10', 'PC', 'Call of Duty'] |
| 10 | missing required: Gran Turismo 7 |
| 10 | missing required: Nintendo Switch Sports |
| 10 | route:contact expected:['penalty', 'rules'] |
| 10 | route:general expected:['rules'] |
| 10 | route:knowledge expected:['overview'] |
| 10 | route:no_answer expected:['general', 'knowledge', 'overview'] |
| 10 | route:service_fee expected:['penalty', 'rules'] |
| 9 | intent:control_lookup expected:game_control_lookup |
| 9 | legacy_mode_prefix:['pipeline:structured_game_controls_no_current_game', 'pipeline:no_answer'] |
| 9 | quality_score_or_required_gate_failed |
| 9 | route:clarification expected:['general', 'knowledge', 'overview'] |
| 9 | route:clarification expected:['multi_question'] |
| 9 | route:clarification expected:['no_answer', 'service_fee'] |
| 9 | route:schedule expected:['clarification', 'equipment'] |
| 8 | intent:user_service_facts expected:how_to |
| 8 | legacy_mode_prefix:['pipeline:structured_game_controls_no_data', 'pipeline:no_answer', 'pipeline:answer_contract_no_answer'] |
| 8 | missing all alternatives: ['TV 65 นิ้ว'] |
| 8 | missing all alternatives: ['TV 86 นิ้ว'] |
| 8 | missing all alternatives: ['The Last of Us Part II (Remastered)', 'PlayStation / PS5'] |
| 8 | missing required: Resident Evil 4 (Remake) |
| 8 | outcome expected no_answer_expected, got answer |
| 8 | route expected ['competition_rules', 'no_answer'], got contact |
| 8 | route:contact expected:['competition_rules', 'no_answer'] |
| 8 | route:no_answer expected:['games'] |
| 8 | route:reservation expected:['no_answer'] |
| 8 | source-gap no-answer attached evidence or did not abstain safely |
| 7 | missing all alternatives: ['RS (Right Stick) Left/Right', 'เปลี่ยนตัวละครหลัก'] |
| 7 | route:no_answer expected:['members', 'overview'] |
| 7 | route:schedule expected:['games'] |
| 6 | missing all alternatives: ['L (Left Stick)', 'Move'] |
| 6 | missing all alternatives: ['L3 (Click Left Stick)', 'Look at'] |
| 6 | missing all alternatives: ['Touch Pad', 'สัมภาระ / เมนูกระเป๋าเก็บของ'] |
| 6 | missing all alternatives: ['Y', 'Assist'] |
| 6 | missing required: ปุ่ม |
| 6 | route expected ['competition_rules'], got schedule |
| 6 | route:clarification expected:['games', 'no_answer'] |
| 6 | route:games expected:['equipment'] |
| 6 | route:games expected:['reservation', 'schedule'] |
| 6 | route:rules expected:['no_answer'] |
| 5 | intent:booking_how_to expected:booking_policy |
| 5 | missing all alternatives: ['R (Right Stick)', 'มุมกล้อง'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ไฟฉาย'] |
| 5 | route:clarification expected:['general', 'overview', 'home', 'knowledge'] |
| 5 | route:clarification expected:['general', 'overview', 'home'] |
| 5 | route:competition_rules expected:['games'] |
| 5 | route:game_controls expected:['games', 'multi_question'] |
| 5 | route:service_fee expected:['games'] |
| 4 | intent:game_detail_lookup expected:game_availability_lookup |
| 4 | missing all alternatives: ['Circle', 'Crouch'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบคลาน'] |
| 4 | missing all alternatives: ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Cross (กากบาท)', 'Jump'] |
| 4 | missing all alternatives: ['Cross', 'Interact'] |
| 4 | missing all alternatives: ['Cross', 'Jump'] |
| 4 | missing all alternatives: ['Cross', 'กระโดด'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Tool selection (Up / Down / Left / Right)'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอุปกรณ์ด่วน'] |
| 4 | missing all alternatives: ['D-Pad', 'License'] |
| 4 | missing all alternatives: ['D-Pad', 'ดูใบขับขี่และสถิติ'] |
| 4 | missing all alternatives: ['God of War Ragnarök', 'PlayStation / PS5'] |
| 4 | missing all alternatives: ['L1', 'Dodge'] |
| 4 | missing all alternatives: ['L1', 'หลบหลีก'] |
| 4 | missing all alternatives: ['L2', 'Aim (Hold)'] |
| 4 | missing all alternatives: ['L2', 'เล็งเป้า (กดค้าง)'] |
| 4 | missing all alternatives: ['Left Stick', 'Steer'] |
| 4 | missing all alternatives: ['Left Stick', 'เลี้ยว'] |
| 4 | missing all alternatives: ['Options', 'Pause'] |
| 4 | missing all alternatives: ['Options', 'หยุดเกม'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'Camera'] |
| 4 | missing all alternatives: ['R1', 'Listen mode (Hold) / Switch Weapon'] |
| 4 | missing all alternatives: ['R1', 'โหมดฟังเสียง (กดค้าง) / สลับอาวุธด่วน'] |
| 4 | missing all alternatives: ['R2', 'Shoot (While aiming) / Reload'] |
| 4 | missing all alternatives: ['R2', 'ยิงปืน (ขณะเล็ง) / รีโหลดกระสุน'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Flashlight'] |
| 4 | missing all alternatives: ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Square', 'Melee'] |
| 4 | missing all alternatives: ['Square', 'โจมตีประชิด'] |
| 4 | missing all alternatives: ['Super Smash Bros. Ultimate', 'Nintendo Switch'] |
| 4 | missing all alternatives: ['TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง'] |
| 4 | missing all alternatives: ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Touch Pad', 'Inventory'] |
| 4 | missing all alternatives: ['Triangle', 'Interact'] |
| 4 | missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ'] |
| 4 | missing all alternatives: ['จอง', 'เลือก', 'บริการ'] |
| 4 | missing all alternatives: ['นายณภัทร เชื้อเหล่าวานิช', 'นักศึกษาสหกิจ Game and 3D Developer'] |
| 4 | missing required: 2026-09-30 |
| 4 | route:clarification expected:['overview', 'members'] |
| 4 | route:clarification expected:['rules', 'overview', 'no_answer'] |
| 4 | route:equipment expected:['no_answer'] |
| 4 | route:equipment expected:['rules'] |
| 4 | route:general expected:['no_answer'] |
| 4 | route:knowledge expected:['equipment', 'games', 'multi_question', 'reservation'] |
| 4 | route:no_answer expected:['overview', 'rules'] |
| 4 | route:no_answer expected:['schedule', 'reservation', 'clarification'] |
| 4 | route:penalty expected:['rules'] |
| 4 | status:no_answer expected:live_lookup_required |
| 3 | intent:ambiguity_gate_clarification expected:game_control_lookup |
| 3 | intent:chatbot_identity expected:detail |
| 3 | intent:user_service_facts expected:detail |
| 3 | intent:user_service_facts expected:group_count |
| 3 | missing required: PlayStation 5 Zone |
| 3 | missing_complete_clause:No team member changes are allowed during the competition period |
| 3 | outcome_mismatch |
| 3 | route:clarification expected:['no_answer', 'games'] |
| 3 | route:games expected:['service_fee'] |
| 3 | route:no_answer expected:['multi_question'] |
| 3 | status:clarification expected:live_lookup_required |
| 3 | wrong_outcome:answer |
| 2 | intent:checkin_required expected:booking_policy |
| 2 | intent:equipment_item_lookup expected:list |
| 2 | intent:food_bring_permission expected:studio_rules |
| 2 | intent:studio_rule_direct expected:studio_rules |
| 2 | missing all alternatives: ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 2 | missing all alternatives: ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 2 | missing required: 13:00-16:00 |
| 2 | missing required: 150 บาท |
| 2 | missing required: PC Zone |
| 2 | missing required: Phuket Campus |
| 2 | missing required: TEKKEN 8 |
| 2 | missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ |
| 2 | missing_complete_clause:5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง |
| 2 | missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ |
| 2 | missing_complete_clause:Abilities must not be used outside map boundaries to obtain information or an advantage. |
| 2 | missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping. |
| 2 | missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification. |
| 2 | missing_complete_clause:If a forfeit is imposed, the result for that map is recorded as 13-0. |
| 2 | missing_complete_clause:Map selection uses MAPBAN.GG |
| 2 | missing_complete_clause:New agents may not be used for approximately 2 weeks after release in Competitive mode. |
| 2 | missing_complete_clause:New maps may not be used for approximately 4 weeks after release in Competitive mode. |
| 2 | missing_complete_clause:Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid. |
| 2 | route:clarification expected:['contact', 'overview'] |
| 2 | route:clarification expected:['general', 'overview', 'knowledge'] |
| 2 | route:clarification expected:['penalty', 'rules'] |
| 2 | route:clarification expected:['service_fee', 'games'] |
| 2 | route:games expected:['equipment', 'clarification'] |
| 2 | route:games expected:['general', 'knowledge'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview', 'knowledge'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview'] |
| 2 | route:no_answer expected:['general', 'overview', 'knowledge'] |
| 2 | route:no_answer expected:['reservation', 'schedule'] |
| 2 | route:no_answer expected:['rules', 'penalty'] |
| 2 | route:reservation expected:['general', 'knowledge'] |
| 1 | 1-2 Persons |
| 1 | 3 หมวด |
| 1 | 3-4 Persons |
| 1 | Local LLM |
| 1 | Members |
| 1 | NARUTO X BORUTO |
| 1 | PSU Phuket Esports Club |
| 1 | VR 1 ชั่วโมง |
| 1 | VR 30 นาที |
| 1 | cooperative education |
| 1 | intent:alcohol_rule expected:studio_rules |
| 1 | intent:ambiguity_gate_clarification expected:detail |
| 1 | intent:ambiguity_gate_clarification expected:list |
| 1 | intent:booking_policy expected:how_to |
| 1 | intent:chatbot_greeting expected:detail |
| 1 | intent:competition_rulebook_catalog expected:competition_game_list |
| 1 | intent:competition_rules_lookup expected:competition_game_list |
| 1 | intent:conversation_price_lookup expected:multi_question_split |
| 1 | intent:count expected:booking_policy |
| 1 | intent:damage_responsibility expected:penalty_policy |
| 1 | intent:freshness_live_source_required expected:detail |
| 1 | intent:how_to expected:game_detail_lookup |
| 1 | intent:keyboard_layout_mismatch expected:schedule_query |
| 1 | intent:price_missing_service expected:multi_question_split |
| 1 | intent:price_missing_service expected:service_fee_query |
| 1 | intent:public_access expected:booking_policy |
| 1 | intent:user_service_facts expected:list |
| 1 | intent:zone_rental_fee expected:guard_no_answer |
| 1 | legacy_mode_prefix:['pipeline:deterministic_calculator_fast'] |
| 1 | legacy_mode_prefix:['pipeline:structured_booking_game_service_selection'] |
| 1 | legacy_mode_prefix:['pipeline:structured_game_detail'] |
| 1 | missing all alternatives: ['Moving Out 2'] |
| 1 | missing all alternatives: ['The Legend of Zelda', 'ปุ่ม', 'controller', 'จอย'] |
| 1 | missing all alternatives: ['The Legend of Zelda', 'วิธีเล่น', 'เล่น'] |
| 1 | missing all alternatives: ['ไม่มี', 'PC #01-#02'] |
| 1 | missing required: 1 ชั่วโมง |
| 1 | missing required: 70 บาท/session |
| 1 | missing required: National ID |
| 1 | missing required: Overcooked 2 |
| 1 | missing required: PC #01-#02 |
| 1 | missing required: PC #03-#10 |
| 1 | missing required: PC 1 ชั่วโมง |
| 1 | missing required: PS5 มีเกมอะไร |
| 1 | missing required: PS5 ราคาเท่าไหร่ |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท |
| 1 | missing required: Tekken 8 ราคาเท่าไหร่ |
| 1 | missing required: local service fee update 2026-07-27 |
| 1 | missing required: ขั้นตอนจอง |
| 1 | missing required: จะเล่น Tekken 8 ต้องจองยังไง |
| 1 | missing required: ต่างกันดังนี้ |
| 1 | missing required: สมัครสมาชิก |
| 1 | missing required: โดยไม่จองล่วงหน้าไม่ได้ |
| 1 | missing required: ไม่พบข้อมูล |
| 1 | missing_complete_clause:1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN |
| 1 | missing_complete_clause:1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม |
| 1 | missing_complete_clause:2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด |
| 1 | missing_complete_clause:3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ |
| 1 | missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด |
| 1 | missing_complete_clause:3. เงินเริ่มต้น $800  /  เวลาของระเบิด: 40 วินาที |
| 1 | missing_complete_clause:If any member withdraws, the team may be disqualified. |
| 1 | missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited. |
| 1 | missing_complete_clause:Watching streams: Players are prohibited from watching live streams during competition. |
| 1 | missing_complete_clause:หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที |
| 1 | missing_complete_clause:อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ |
| 1 | missing_complete_clause:เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ |
| 1 | missing_complete_clause:ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด |
| 1 | outcome expected clarification_required, got no_answer |
| 1 | route expected ['competition_rules', 'clarification'], got no_answer |
| 1 | route:clarification expected:['equipment'] |
| 1 | route:clarification expected:['general', 'knowledge', 'no_answer'] |
| 1 | route:equipment expected:['games', 'clarification'] |
| 1 | route:equipment expected:['general', 'knowledge', 'no_answer'] |
| 1 | route:game_controls expected:['games', 'clarification', 'no_answer'] |
| 1 | route:input_guard expected:['equipment', 'no_answer'] |
| 1 | route:input_guard expected:['schedule'] |
| 1 | route:knowledge expected:['games', 'clarification'] |
| 1 | route:no_answer expected:['games', 'reservation', 'schedule'] |
| 1 | route:no_answer expected:['general', 'overview', 'home', 'knowledge'] |
| 1 | route:no_answer expected:['general', 'overview', 'home'] |
| 1 | route:no_answer expected:['general'] |
| 1 | route:reservation expected:['games', 'general', 'no_answer'] |
| 1 | route:schedule expected:['equipment', 'clarification'] |
| 1 | ตาราง Service Fee |
| 1 | พื้นที่ที่กำหนด |
| 1 | ยังไม่ได้เปิด |
| 1 | เร่ง |

## common_offline

| จำนวน | reasonตามraw |
|---:|---|
| 16253 | status:clarification expected:answer_available |
| 14881 | route:knowledge expected:['games'] |
| 3155 | route:knowledge expected:['competition_rules'] |
| 3140 | validation_rejected |
| 2534 | route:knowledge expected:['equipment'] |
| 1930 | route:knowledge expected:['reservation', 'schedule'] |
| 1820 | pipeline_exception |
| 1748 | route expected ['competition_rules'], got knowledge |
| 1606 | retrieval evidence did not match the allowed canonical fact/rule IDs |
| 1405 | route:knowledge expected:['reservation'] |
| 1146 | status:clarification expected:live_lookup_required |
| 929 | route:knowledge expected:['games', 'reservation'] |
| 927 | outcome expected answer_available, got clarification |
| 822 | missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026'] |
| 802 | route:knowledge expected:['rules'] |
| 795 | route:knowledge expected:['service_fee'] |
| 753 | route:knowledge expected:['members', 'overview'] |
| 745 | status:clarification expected:localization_pending |
| 677 | first_line_off_topic |
| 533 | missing rulebook target(s): ['competition_rules_valorant_psu_phuket_2026'] |
| 520 | missing rulebook target(s): ['competition_rules_tekken8_psu_esports'] |
| 494 | route:knowledge expected:['penalty'] |
| 486 | missing all alternatives: ['Nintendo Switch Zone'] |
| 456 | status:no_answer expected:answer_available |
| 426 | route_mismatch |
| 418 | route:knowledge expected:['competition_rules', 'no_answer'] |
| 412 | status:answer expected:no_answer_expected |
| 368 | route:knowledge expected:['games', 'reservation', 'schedule'] |
| 353 | status:answer expected:clarification_required |
| 347 | route:no_answer expected:['general', 'knowledge'] |
| 332 | missing all alternatives: ['PlayStation 5 Zone'] |
| 328 | legacy_mode_prefix:['pipeline:structured_game_controls'] |
| 308 | validation errors: ['unresolved_query_clause'] |
| 299 | route expected ['competition_rules', 'no_answer'], got knowledge |
| 299 | route:knowledge expected:['multi_question'] |
| 299 | route:knowledge expected:['schedule'] |
| 299 | status:clarification expected:no_answer_expected |
| 294 | wrong_game_evidence |
| 281 | outcome_mismatch |
| 268 | route:knowledge expected:['equipment', 'games', 'multi_question', 'reservation'] |
| 268 | wrong_category |
| 262 | missing all alternatives: ['PC Zone'] |
| 190 | route:knowledge expected:['equipment', 'games'] |
| 180 | legacy_mode_prefix:['pipeline:competition_fact_card'] |
| 170 | missing required: Verified equipment |
| 167 | legacy_english_thai_prose_flag |
| 167 | outcome expected no_answer_expected, got answer |
| 166 | missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่'] |
| 160 | route:schedule expected:['reservation'] |
| 160 | route:service_fee expected:['equipment', 'games', 'multi_question', 'reservation'] |
| 147 | missing all alternatives: ['PlayStation 5', 'PlayStation 5 #01-#02'] |
| 141 | route:knowledge expected:['contact'] |
| 132 | outcome expected no_answer_expected, got clarification |
| 130 | status:no_answer expected:localization_pending |
| 128 | missing all alternatives: ['PlayStation 5', 'เล่นได้ที่'] |
| 128 | missing all alternatives: ['บาท', 'บาท', 'ฟรี'] |
| 123 | backend_wall_watchdog_20s |
| 122 | route:knowledge expected:['schedule', 'reservation'] |
| 120 | missing all alternatives: ['Cockpit Zone'] |
| 119 | missing required: Wednesday |
| 114 | missing all alternatives: ['Nintendo Switch', 'เล่นได้ที่'] |
| 109 | wrong_game_source |
| 108 | route:knowledge expected:['overview'] |
| 105 | status:answer expected:live_lookup_required |
| 104 | validation errors: ['unresolved_query_clause', 'missing_requested_field:details'] |
| 99 | route:knowledge expected:['clarification', 'schedule'] |
| 98 | missing all alternatives: ['Nintendo Switch', 'Nintendo Switch (1-2 Persons)'] |
| 96 | missing all alternatives: ['ไม่มี', 'PC #03-#10'] |
| 96 | route:knowledge expected:['clarification', 'equipment'] |
| 96 | route:knowledge expected:['general', 'overview', 'home'] |
| 94 | missing all alternatives: ['R (Right Stick)', 'มุมกล้อง'] |
| 91 | missing required: 09:00-12:00 |
| 90 | wrong_outcome |
| 89 | missing all alternatives: ['Gaming Monitor', 'Gaming Monitors'] |
| 88 | missing all alternatives: ['VR Zone'] |
| 87 | latency_ceiling |
| 86 | missing all alternatives: ['ไม่มี', 'PC #01-#02'] |
| 76 | route:knowledge expected:['contact', 'overview'] |
| 74 | route:input_guard expected:['clarification', 'general', 'no_answer', 'unknown'] |
| 74 | route:knowledge expected:['games', 'multi_question'] |
| 72 | missing required: 2 sessions |
| 72 | route:knowledge expected:['penalty', 'rules'] |
| 69 | source-gap no-answer attached evidence or did not abstain safely |
| 68 | route:clarification expected:['no_answer', 'overview', 'rules'] |
| 66 | missing all alternatives: ['L (Left Stick)', 'Move'] |
| 66 | missing all alternatives: ['latency', 'หน่วง'] |
| 66 | missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible'] |
| 66 | missing required: PlayStation 5 |
| 63 | missing required: 3 sessions |
| 62 | route:knowledge expected:['equipment', 'rules'] |
| 62 | route:knowledge expected:['games', 'service_fee'] |
| 62 | route:reservation expected:['members', 'overview'] |
| 61 | missing required: English localization |
| 60 | missing all alternatives: ['Options', 'Pause'] |
| 60 | missing all alternatives: ['เฟรม', 'ความละเอียด'] |
| 60 | route:knowledge expected:['games', 'no_answer'] |
| 59 | missing all alternatives: ['server', 'client'] |
| 59 | route:knowledge expected:['multi_question', 'reservation', 'games', 'equipment'] |
| 58 | route:knowledge expected:['clarification', 'service_fee'] |
| 57 | missing all alternatives: ['GPU', 'กราฟิก'] |
| 57 | missing all alternatives: ['คีย์บอร์ด', 'mechanical'] |
| 56 | validation errors: ['missing_requested_field:details'] |
| 55 | intent:conversation_price_lookup expected:service_fee_query |
| 55 | missing all alternatives: ['กิจกรรม'] |
| 54 | missing all alternatives: ['API', 'เชื่อมต่อ'] |
| 54 | missing all alternatives: ['ขอบคุณ'] |
| 54 | missing required: not open 24 hours |
| 54 | missing required: refund |
| 53 | missing required: 13:00-16:00 |
| 53 | missing required: Phuket Campus |
| 51 | route:reservation expected:['overview'] |
| 50 | missing all alternatives: ['R (Right Stick)', 'Camera'] |
| 48 | legacy_mode_prefix:['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'] |
| 48 | route:clarification expected:['reservation'] |
| 48 | route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee'] |
| 47 | missing all alternatives: ['จอง'] |
| 47 | route:clarification expected:['members', 'overview'] |
| 46 | missing all alternatives: ['พื้นที่ที่กำหนด', 'designated area'] |
| 44 | missing all alternatives: ['Options', 'หยุดเกม'] |
| 44 | missing all alternatives: ['แนวเกม', 'เกม Action-Adventure'] |
| 43 | validation errors: ['missing_requested_field:steps'] |
| 42 | legacy_mode_prefix:['pipeline:multi_question_splitter'] |
| 42 | missing all alternatives: ['09:00', '13:00', '9:00', '1 pm'] |
| 41 | missing required: psuesportspkt@gmail.com |
| 40 | missing required: maintenance |
| 40 | route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification'] |
| 38 | missing required: Call of Duty |
| 36 | missing all alternatives: ['VALORANT', 'Counter-Strike 2'] |
| 35 | missing all alternatives: ['W / A / S / D', 'เคลื่อนที่'] |
| 35 | missing required: 70 THB |
| 35 | missing required: Verified game catalog |
| 35 | route:clarification expected:['no_answer'] |
| 34 | missing all alternatives: ['Pokémon Champions', 'Animal Crossing: New Horizons', 'It Takes Two', '60'] |
| 34 | missing all alternatives: ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก'] |
| 34 | route:service_fee expected:['multi_question', 'reservation', 'games', 'equipment'] |
| 33 | missing all alternatives: ['L3', 'วิ่งสปรินต์'] |
| 32 | missing all alternatives: ['Animal Crossing: New Horizons'] |
| 32 | route:knowledge expected:['clarification', 'competition_rules', 'general'] |
| 29 | missing required: There are currently 42 verified games available. |
| 28 | missing all alternatives: ['+ (Plus)', 'Pause'] |
| 28 | missing all alternatives: ['Cockpit Zone', 'PlayStation 5 Zone'] |
| 28 | missing all alternatives: ['New Super Mario Bros. U Deluxe'] |
| 28 | route:knowledge expected:['general', 'clarification', 'no_answer', 'overview'] |
| 28 | route:knowledge expected:['rules', 'no_answer', 'clarification'] |
| 28 | route:no_answer expected:['penalty', 'rules'] |
| 26 | missing all alternatives: ['Left Shift', 'เดินช้า'] |
| 26 | missing all alternatives: ['Left Stick', 'เคลื่อนที่'] |
| 25 | route:knowledge expected:['no_answer'] |
| 25 | route:service_fee expected:['multi_question'] |
| 24 | missing all alternatives: ['The Legend of Zelda: Breath of the Wild'] |
| 24 | missing all alternatives: ['Touch Pad', 'แผนที่'] |
| 24 | status:no_answer expected:clarification_required |
| 23 | intent:common_read expected:list |
| 23 | missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา'] |
| 22 | intent:common_read expected:booking_policy |
| 22 | intent:common_read expected:schedule_query |
| 22 | missing all alternatives: ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 22 | missing all alternatives: ['L3 (Click Left Stick)', 'หันมองจุดสนใจ'] |
| 22 | missing all alternatives: ['PC Zone', 'PlayStation 5 Zone'] |
| 22 | missing all alternatives: ['PlayStation 5 Zone / VR Zone'] |
| 22 | missing all alternatives: ['The Last of Us Part I / Part II'] |
| 22 | missing all alternatives: ['แนวเกม', 'เกม Battle Royale'] |
| 21 | missing all alternatives: ['+ (Plus)', 'หยุดเกม'] |
| 21 | validation errors: ['unresolved_query_clause', 'missing_requested_field:details', 'missing_requested_field:conditions_all'] |
| 20 | missing all alternatives: ['Call of Duty: Modern Warfare III', 'Delta Force', 'EA Sports FC 24', '60'] |
| 20 | missing all alternatives: ['Cross', 'Jump'] |
| 20 | missing all alternatives: ['Cross', 'กระโดด'] |
| 20 | missing all alternatives: ['FINAL FANTASY XVI คือเกมแอ็กชัน RPG แฟนตาซีที่เน้นเนื้อเรื่อง การต่อสู้ และการพัฒนาตัวละคร'] |
| 20 | missing all alternatives: ['Horizon Call of the Mountain คือเกม VR ผจญภัยในโลก Horizon ที่เน้นการปีนป่าย สำรวจ และต่อสู้กับจักรกล'] |
| 20 | missing all alternatives: ['It Takes Two คือเกมผจญภัยสำหรับเล่นร่วมกันสองคน ที่ต้องช่วยกันแก้ปริศนาและผ่านด่าน'] |
| 20 | missing all alternatives: ['Little Nightmares II คือเกมผจญภัยบรรยากาศสยองที่เน้นการหลบหนี แก้ปริศนา และผ่านฉากอันตราย'] |
| 20 | missing all alternatives: ['Overcooked! 2', 'ยังไม่พบข้อมูลปุ่ม', 'ไม่มีข้อมูลปุ่ม'] |
| 20 | missing all alternatives: ['PlayStation 5 #01-#02', 'PlayStation 5', 'NARUTO X BORUTO Ultimate Ninja Storm Connections'] |
| 20 | missing all alternatives: ['Touch Pad', 'Map'] |
| 20 | missing all alternatives: ['VR', 'เล่นได้ที่'] |
| 20 | missing all alternatives: ['เล็ง ยิง เคลื่อนที่ ใช้อุปกรณ์ และทำ objective ของโหมดเกมหรือภารกิจให้สำเร็จ'] |
| 20 | missing all alternatives: ['เล่นแบบสบาย ๆ โดยเก็บทรัพยากร ตกปลา จับแมลง ตกแต่งเกาะ และทำกิจกรรมประจำวัน'] |
| 20 | missing all alternatives: ['แนวเกม', 'เกม Survival Horror'] |
| 20 | missing required: Animal Crossing |
| 20 | missing required: Monster Hunter Rise |
| 20 | missing required: PUBG |
| 20 | missing required: Uncharted |
| 20 | missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026', 'competition_rules_valorant_psu_phuket_2026'] |
| 20 | route:clarification expected:['reservation', 'schedule'] |
| 20 | validation errors: ['unresolved_query_clause', 'missing_requested_field:steps'] |
| 19 | missing required: Resident Evil Village |
| 19 | validation errors: ['missing_requested_field:consequence'] |
| 18 | missing all alternatives: ["Luigi's Mansion 3 คือเกมผจญภัยจับผีที่ผู้เล่นสำรวจโรงแรมและแก้ปริศนา"] |
| 18 | missing all alternatives: ['13:00', 'maintenance', 'Maintenance'] |
| 18 | missing all alternatives: ['Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง'] |
| 18 | missing all alternatives: ['Call of Duty: Modern Warfare III คือเกมยิงมุมมองบุคคลที่หนึ่งที่เน้นภารกิจและการยิงต่อสู้แบบรวดเร็ว'] |
| 18 | missing all alternatives: ['Call of Duty: Warzone', 'Counter-Strike 2', 'League of Legends', '60'] |
| 18 | missing all alternatives: ['Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม'] |
| 18 | missing all alternatives: ['EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล'] |
| 18 | missing all alternatives: ['Fortnite คือเกมต่อสู้เอาชีวิตรอดที่ผู้เล่นแข่งกันในแผนที่ขนาดใหญ่และพยายามอยู่เป็นคนสุดท้าย'] |
| 18 | missing all alternatives: ['God of War Ragnarok คือเกมแอ็กชันผจญภัยที่เน้นเนื้อเรื่อง การต่อสู้ และการสำรวจในโลกตำนานนอร์ส'] |
| 18 | missing all alternatives: ['Gran Turismo 7 คือเกมแข่งรถที่เน้นการขับรถสมจริง การเลือกสนาม รถ และการควบคุมจังหวะเข้าโค้ง'] |
| 18 | missing all alternatives: ['Gran Turismo 7', '60'] |
| 18 | missing all alternatives: ['League of Legends คือเกมวางแผนต่อสู้แบบทีม ผู้เล่นเลือก Champion และร่วมกันทำลายฐานหลักของฝ่ายตรงข้าม'] |
| 18 | missing all alternatives: ['PlayStation Zone', 'อุปกรณ์'] |
| 18 | missing required: Counter-Strike 2 |
| 18 | missing required: Luigi's Mansion 3 |
| 18 | missing required: Marvel's Spider-Man 2 |
| 18 | missing required: The Last of Us Part I |
| 18 | missing required: not connected |
| 18 | route:contact expected:['rules', 'no_answer', 'clarification'] |
| 18 | route:knowledge expected:['games', 'general', 'no_answer'] |
| 18 | route:schedule expected:['no_answer'] |
| 17 | missing all alternatives: ['TEKKEN 8', 'Counter-Strike 2', 'League of Legends', '60'] |
| 17 | missing required: Fortnite |
| 17 | missing required: Mario Party Superstars |
| 17 | missing required: No information |
| 17 | missing required: VALORANT |
| 17 | route:clarification expected:['games', 'reservation'] |
| 16 | missing all alternatives: ['Animal Crossing: New Horizons คือเกมใช้ชีวิตบนเกาะ ผู้เล่นตกแต่งบ้าน เก็บของ สร้างพื้นที่ และพูดคุยกับชาวเกาะ'] |
| 16 | missing all alternatives: ['Hogwarts Legacy คือเกมผจญภัยในโลกเวทมนตร์ ผู้เล่นเรียนคาถา สำรวจ และทำภารกิจในฮอกวอตส์และพื้นที่รอบ ๆ'] |
| 16 | missing all alternatives: ['L2 (Hold)', 'Aim'] |
| 16 | missing all alternatives: ['Mario Kart 8 Deluxe คือเกมแข่งรถสไตล์ปาร์ตี้ที่ใช้ตัวละคร Nintendo ขับรถแข่งกันในสนามหลากหลายแบบ'] |
| 16 | missing all alternatives: ['Mario Party Superstars คือเกมปาร์ตี้ที่เล่นบนกระดานและแข่งมินิเกมกับเพื่อน'] |
| 16 | missing all alternatives: ['New Super Mario Bros. U Deluxe คือเกมมาริโอแบบเดินลุยด่าน กระโดด หลบศัตรู และเก็บเหรียญ'] |
| 16 | missing all alternatives: ['PUBG: BATTLEGROUNDS คือเกมเอาชีวิตรอดที่ผู้เล่นลงสนาม ค้นหาอาวุธและอุปกรณ์ แล้วพยายามอยู่รอดเป็นคนหรือทีมสุดท้าย'] |
| 16 | missing all alternatives: ['TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง'] |
| 16 | missing all alternatives: ['เลือกจุดลง หาอาวุธ เข้าโซนปลอดภัย วางตำแหน่ง และต่อสู้กับทีมอื่นจนเหลือผู้ชนะท้ายเกม'] |
| 16 | missing required: Beat Saber |
| 16 | missing required: EA Sports FC 24 |
| 16 | missing required: FINAL FANTASY XVI |
| 16 | missing required: Gran Turismo 7 |
| 16 | missing required: Hogwarts Legacy |
| 16 | missing required: Horizon Call of the Mountain |
| 16 | missing required: It Takes Two |
| 16 | missing required: League of Legends |
| 16 | missing required: Mario Kart 8 Deluxe |
| 16 | missing required: Nintendo Switch Sports |
| 16 | route:input_guard expected:['general', 'unknown', 'clarification', 'no_answer'] |
| 16 | status:answer expected:safe_clarification |
| 15 | missing all alternatives: ['Beat Saber', 'Horizon Call of the Mountain', 'Resident Evil 4'] |
| 15 | missing all alternatives: ['Button controls', 'เล่นบอร์ดและมินิเกมด้วยปุ่ม'] |
| 15 | missing all alternatives: ['L3', 'เกาะคอน / พุ่งหลาว'] |
| 15 | missing required: esports learning development studio |
| 15 | route:knowledge expected:['equipment', 'clarification'] |
| 15 | route:no_answer expected:['overview'] |
| 15 | route:service_fee expected:['no_answer'] |
| 14 | legacy_mode_prefix:['pipeline:structured_game_controls_no_current_game', 'pipeline:no_answer'] |
| 14 | missing all alternatives: ["Marvel's Spider-Man 2 คือเกมแอ็กชันผจญภัยที่ผู้เล่นรับบท Spider-Man ต่อสู้กับศัตรูและสำรวจเมือง"] |
| 14 | missing all alternatives: ['Cross', 'Interact'] |
| 14 | missing all alternatives: ['Left Stick', 'Move'] |
| 14 | missing all alternatives: ['NARUTO X BORUTO Ultimate Ninja Storm Connections คือเกมต่อสู้ที่ใช้ตัวละครจากจักรวาล Naruto/Boruto'] |
| 14 | missing all alternatives: ['Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย'] |
| 14 | missing all alternatives: ['Resident Evil 4 คือเกมเอาตัวรอดสยองขวัญที่เน้นการต่อสู้ การสำรวจ และการบริหารกระสุน/ไอเทม'] |
| 14 | missing all alternatives: ['The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ'] |
| 14 | missing all alternatives: ['ลงพื้นที่ หาอาวุธ ใช้ loadout/อุปกรณ์ช่วยทีม เคลื่อนตามวง และพยายามอยู่รอดจนจบเกม'] |
| 14 | missing all alternatives: ['เลือกตัวละคร ใช้คอมโบ สกิลนินจา และจังหวะหลบ/สวนกลับเพื่อเอาชนะคู่ต่อสู้'] |
| 14 | missing rulebook target(s): ['competition_rules_rov_blueket_2025_men', 'competition_rules_tekken8_psu_esports'] |
| 14 | quality_score_or_required_gate_failed |
| 14 | route:clarification expected:['general', 'knowledge'] |
| 14 | route:knowledge expected:['clarification', 'games', 'general'] |
| 13 | missing all alternatives: ['Joy-Con (R) Control Stick', 'เลื่อนเคอร์เซอร์'] |
| 13 | missing all alternatives: ['Joy-Con motion', 'เล่นท่ากีฬาด้วยการขยับ Joy-Con'] |
| 13 | missing all alternatives: ['L (Left Stick)', 'เลี้ยว / ควบคุมทิศทาง'] |
| 13 | missing all alternatives: ['L3 (Click Left Stick)', 'วิ่งสปรินต์'] |
| 13 | missing all alternatives: ['RS (Right Stick) Left/Right', 'เปลี่ยนตัวละครหลัก'] |
| 13 | missing all alternatives: ['Simple controls', 'วิ่ง กระโดด และเหยียบศัตรู'] |
| 13 | missing all alternatives: ['Single Joy-Con / Joy-Con grip / Pro Controller', 'รูปแบบคอนโทรลเลอร์ที่รองรับ'] |
| 13 | missing required: Overcooked 2 |
| 13 | missing_complete_clause:Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid. |
| 13 | route:no_answer expected:['reservation'] |
| 13 | validation errors: ['missing_requested_field:decision'] |
| 12 | intent:common_read expected:game_control_lookup |
| 12 | missing all alternatives: ['Call of Duty: Warzone คือเกมยิงแนว Battle Royale ที่เน้นการยิงรวดเร็ว การเก็บอุปกรณ์ และการเอาตัวรอดในแผนที่ขนาดใหญ่'] |
| 12 | missing all alternatives: ['Circle', 'Crouch'] |
| 12 | missing all alternatives: ['L3', 'Sprint'] |
| 12 | missing all alternatives: ['Left Mouse Button', 'ยิง'] |
| 12 | missing all alternatives: ['Monster Hunter Rise คือเกมล่ามอนสเตอร์ที่ผู้เล่นเลือกอาวุธ ทำภารกิจ และเก็บวัตถุดิบมาสร้างอุปกรณ์'] |
| 12 | missing all alternatives: ['Moving Out 2 คือเกมย้ายของแบบร่วมมือกันที่ต้องช่วยกันขนของผ่านฉากวุ่น ๆ'] |
| 12 | missing all alternatives: ['Nintendo Switch Sports คือเกมกีฬาที่ใช้การขยับ Joy-Con จำลองการเล่นกีฬาหลายประเภท'] |
| 12 | missing all alternatives: ['R', 'รีโหลด'] |
| 12 | missing all alternatives: ['Resident Evil Village คือเกมสยองขวัญเอาตัวรอดที่เน้นบรรยากาศ การสำรวจ และการต่อสู้กับศัตรูหลากหลายรูปแบบ'] |
| 12 | missing all alternatives: ['Ring Fit Adventure คือเกมออกกำลังกายที่ใช้ Ring-Con และท่าทางร่างกายเพื่อผจญภัยในเกม'] |
| 12 | missing all alternatives: ['Square', 'Reload'] |
| 12 | missing all alternatives: ['Super Mario Odyssey คือเกมผจญภัย 3D ที่ Mario สำรวจโลกต่าง ๆ และเก็บ Power Moon'] |
| 12 | missing all alternatives: ['Super Smash Bros Ultimate คือเกมต่อสู้ที่ใช้ตัวละครจากหลายเกม ผลักคู่ต่อสู้ออกจากฉากเพื่อทำคะแนน'] |
| 12 | missing all alternatives: ['The Last of Us คือเกมผจญภัยเอาตัวรอดที่เน้นเนื้อเรื่อง การลอบเร้น และการจัดการทรัพยากร'] |
| 12 | missing all alternatives: ['Uncharted คือเกมผจญภัยแนวล่าสมบัติที่เน้นปีนป่าย สำรวจ แก้ปริศนา และฉากแอ็กชัน'] |
| 12 | missing all alternatives: ['VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ'] |
| 12 | missing all alternatives: ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล'] |
| 12 | missing all alternatives: ['วิ่ง กระโดด ใช้ power-up ผ่านด่าน และร่วมมือกับเพื่อนได้หลายคน'] |
| 12 | missing all alternatives: ['สำรวจ ฉวยโอกาสลอบเร้น ต่อสู้ เก็บทรัพยากร และดำเนินเรื่องผ่านภารกิจต่าง ๆ'] |
| 12 | missing all alternatives: ['สำรวจฉาก ปีนป่าย แก้ปริศนา ยิงต่อสู้ และดำเนินเรื่องผ่านภารกิจ'] |
| 12 | missing all alternatives: ['สำรวจแผนที่ เก็บอาวุธ/อาหาร แก้ shrine ต่อสู้ และเลือกเส้นทางการผจญภัยเองได้มาก'] |
| 12 | missing all alternatives: ['แนวเกม', 'เกม Puzzle Platform'] |
| 12 | missing all alternatives: ['แนวเกม', 'เกม VR Rhythm'] |
| 12 | missing all alternatives: ['แนวเกม', 'เกมยิง Battle Royale'] |
| 12 | missing all alternatives: ['แนวเกม', 'เกมยิง Tactical FPS'] |
| 12 | missing all alternatives: ['ไม่ได้', 'ไม่พบ', 'closed', 'weekend', 'not open'] |
| 12 | missing required: NARUTO X BORUTO Ultimate Ninja Storm Connections |
| 12 | missing required: Resident Evil 4 |
| 12 | route:knowledge expected:['clarification', 'games'] |
| 12 | status:clarification expected:safe_no_answer |
| 12 | validation errors: ['missing_requested_field:players_max'] |
| 11 | intent:common_read expected:studio_rules |
| 11 | missing all alternatives: ['Analogue control scheme', 'เคลื่อนที่ด้วยอนาล็อก'] |
| 11 | missing all alternatives: ['Controller Mapping page', 'เปลี่ยน preset จอย'] |
| 11 | missing all alternatives: ['Cross', 'ส่งบอลเลียด / โหม่ง'] |
| 11 | missing all alternatives: ['Gesture control scheme', 'เคลื่อนที่ด้วยท่าทางร่างกาย'] |
| 11 | missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่ / เดินสไลด์ข้าง'] |
| 11 | missing all alternatives: ['L (Left Stick)', 'เลี้ยว / ควบคุมพวงมาลัย'] |
| 11 | missing all alternatives: ['L / ZL / R / ZR', 'จับ / ยก'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'มาร์กตำแหน่งศัตรู'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'ย่อตัว'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'วิ่งเร็ว / สปรินต์'] |
| 11 | missing all alternatives: ['LS (Left Stick)', 'เคลื่อนที่'] |
| 11 | missing all alternatives: ['Left PS VR2 Sense controller motion', 'ฟันบล็อกด้วยดาบมือซ้าย'] |
| 11 | missing all alternatives: ['One Joy-Con', 'ควบคุมตัวละครด้วย Joy-Con เดี่ยว'] |
| 11 | missing all alternatives: ['Options', 'เปิดเมนูเกม'] |
| 11 | missing all alternatives: ['PlayStation 5 #01-#02', 'PlayStation 5', 'Call of Duty'] |
| 11 | missing all alternatives: ['PlayStation 5 #01-#02', 'PlayStation 5', 'Uncharted'] |
| 11 | missing all alternatives: ['Pokémon Champions', 'Animal Crossing: New Horizons', 'It Takes Two'] |
| 11 | missing all alternatives: ['Q / W / E / R', 'ใช้สกิล'] |
| 11 | missing all alternatives: ['R (Right Stick)', 'หันหน้า / เล็ง'] |
| 11 | missing all alternatives: ['R (Right Stick)', 'โจมตีสแมช'] |
| 11 | missing all alternatives: ['R2', 'คันเร่ง'] |
| 11 | missing all alternatives: ['Right Mouse Button', 'เดิน / โจมตีเป้าหมาย'] |
| 11 | missing all alternatives: ['Right PS VR2 Sense controller motion', 'ฟันบล็อกด้วยดาบมือขวา'] |
| 11 | missing all alternatives: ['Right Stick', 'ควบคุมมุมกล้อง'] |
| 11 | missing all alternatives: ['Square', 'ส่งบอลโด่ง / เปิดบอล / โหม่ง'] |
| 11 | missing all alternatives: ['Square', 'หมัดซ้าย / ต่อยซ้าย'] |
| 11 | missing all alternatives: ['Triangle', 'หมัดขวา / ต่อยขวา'] |
| 11 | missing all alternatives: ['X Button on sport-selection screen', 'เลือกโหมดสายรัดขาใน Soccer ตอน Play Globally'] |
| 11 | missing all alternatives: ['X Button', 'ยืนยันการเลือก'] |
| 11 | route:knowledge expected:['clarification', 'games', 'no_answer'] |
| 10 | missing all alternatives: ['- (Minus)', 'Map'] |
| 10 | missing all alternatives: ['- (Minus)', 'แผนที่'] |
| 10 | missing all alternatives: ['Call of Duty: Modern Warfare III', 'Delta Force', 'EA Sports FC 24'] |
| 10 | missing all alternatives: ['Circle', 'Dodge'] |
| 10 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบ / สไลด์'] |
| 10 | missing all alternatives: ['Cockpit', 'เล่นได้ที่'] |
| 10 | missing all alternatives: ['Cross', 'กระโดด / ปีนป่าย'] |
| 10 | missing all alternatives: ['L1', 'กระโดด / ปีนป่าย'] |
| 10 | missing all alternatives: ['L3 (Click Left Stick)', 'Look at'] |
| 10 | missing all alternatives: ['L3', 'Animal Instinct'] |
| 10 | missing all alternatives: ['Left Ctrl', 'ย่อตัว'] |
| 10 | missing all alternatives: ['M', 'เปิดแผนที่'] |
| 10 | missing all alternatives: ['Options', 'หยุดเกมชั่วคราว'] |
| 10 | missing all alternatives: ['PC #03-#10', 'PC', 'Call of Duty'] |
| 10 | missing all alternatives: ['PC', 'Zone'] |
| 10 | missing all alternatives: ['R1', 'Use Lethal Equipment'] |
| 10 | missing all alternatives: ['R3 (Click Right Stick)', 'ไฟฉาย'] |
| 10 | missing all alternatives: ['R3', 'เปลี่ยนท่า / สไลด์ / พุ่งหลบ'] |
| 10 | missing all alternatives: ['TEKKEN 8', 'Counter-Strike 2', 'League of Legends'] |
| 10 | missing all alternatives: ['VR', 'VR Station 30 นาที'] |
| 10 | missing all alternatives: ['W / A / S / D', 'Move'] |
| 10 | missing all alternatives: ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Action Puzzle'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Action RPG ล่ามอนสเตอร์'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Action RPG'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Co-op Adventure'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Co-op Puzzle'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Co-op ทำอาหาร'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Life Simulation'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม MOBA แบบทีม 5v5'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Open-world Action RPG'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Open-world Adventure'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Party'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Platformer 2D'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Platformer 3D'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม VR Action-Adventure'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมกีฬา Motion Control'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมต่อสู้ 1v1'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมต่อสู้จากอนิเมะ'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมต่อสู้แบบ Platform Fighter'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมฟุตบอล'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมยิง FPS'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมยิง Tactical FPS แบบทีม 5v5'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมออกกำลังกาย Adventure'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมแข่งรถ Party Racing'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมแข่งรถ'] |
| 10 | missing required: God of War Ragnarok |
| 10 | missing required: Super Smash Bros Ultimate |
| 10 | missing required: TEKKEN 8 |
| 10 | missing_complete_clause:Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset. |
| 10 | missing_complete_clause:Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only. |
| 10 | route:games expected:['no_answer'] |
| 10 | route:no_answer expected:['general', 'knowledge', 'overview'] |
| 9 | missing all alternatives: ['B', 'ยกเลิก'] |
| 9 | missing all alternatives: ['B', 'เบรก / ถอยหลัง'] |
| 9 | missing all alternatives: ['Call of Duty', 'PlayStation 5 #01-#02', 'PlayStation 5'] |
| 9 | missing all alternatives: ['L2 (Hold)', 'เล็ง'] |
| 9 | missing all alternatives: ['NARUTO X BORUTO Ultimate Ninja Storm Connections', 'PlayStation 5 #01-#02', 'PlayStation 5'] |
| 9 | missing all alternatives: ['R3', 'ล็อกเป้าหมาย'] |
| 9 | missing all alternatives: ['Uncharted', 'PlayStation 5 #01-#02', 'PlayStation 5'] |
| 9 | missing required: Nintendo Switch |
| 9 | missing_complete_clause:Advantage: No advantage |
| 9 | missing_complete_clause:No scripts or macros are allowed at all. |
| 9 | missing_complete_clause:Stage: Random |
| 9 | route:clarification expected:['general', 'knowledge', 'overview'] |
| 9 | route:clarification expected:['no_answer', 'service_fee'] |
| 9 | validation errors: ['missing_requested_field:details', 'missing_requested_field:steps'] |
| 8 | intent:common_read expected:game_availability_lookup |
| 8 | intent:user_service_facts expected:how_to |
| 8 | legacy_mode_prefix:['pipeline:structured_game_controls_no_data', 'pipeline:no_answer', 'pipeline:answer_contract_no_answer'] |
| 8 | missing all alternatives: ['1 / 2 / 3', 'เลือกอาวุธ'] |
| 8 | missing all alternatives: ['Cockpit', 'Zone'] |
| 8 | missing all alternatives: ['Cross', 'โต้ตอบ'] |
| 8 | missing all alternatives: ['D-Pad Down', 'Heal'] |
| 8 | missing all alternatives: ['D-Pad Down', 'ฟื้นฟูเลือด'] |
| 8 | missing all alternatives: ['Delta Force', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['L (Left Stick) / R (Right Stick)', 'เคลื่อนที่'] |
| 8 | missing all alternatives: ['L (Left Stick)', 'Steer'] |
| 8 | missing all alternatives: ['L2', 'Aim (Hold)'] |
| 8 | missing all alternatives: ['L2', 'Aim Down Sight'] |
| 8 | missing all alternatives: ['L2', 'เล็งเป้า (กดค้าง)'] |
| 8 | missing all alternatives: ['L3 (Click Left Stick)', 'Sprint'] |
| 8 | missing all alternatives: ['L3', 'วิ่ง / กลั้นหายใจ'] |
| 8 | missing all alternatives: ['Left Mouse Button', 'Fire'] |
| 8 | missing all alternatives: ['Left Shift', 'Walk'] |
| 8 | missing all alternatives: ['Options', 'เมนูหลัก'] |
| 8 | missing all alternatives: ['Pokémon Champions', 'Nintendo Switch'] |
| 8 | missing all alternatives: ['R1', 'ใช้อุปกรณ์ทำลายล้าง'] |
| 8 | missing all alternatives: ['R2', 'Fire Weapon'] |
| 8 | missing all alternatives: ['R3 (Click Right Stick)', 'Flashlight'] |
| 8 | missing all alternatives: ['R3', 'Lock-On'] |
| 8 | missing all alternatives: ['Right Mouse Button', 'ยิง/เล็งแบบรอง'] |
| 8 | missing all alternatives: ['Square', 'Melee'] |
| 8 | missing all alternatives: ['Square', 'โจมตีประชิด'] |
| 8 | missing all alternatives: ['Square', 'โต้ตอบ / รีโหลด'] |
| 8 | missing all alternatives: ['THE FINALS', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['Tab', 'Scoreboard'] |
| 8 | missing all alternatives: ['Tab', 'ดูตารางคะแนน'] |
| 8 | missing all alternatives: ['The Last of Us Part II (Remastered)', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['Triangle', 'Emote'] |
| 8 | missing all alternatives: ['Triangle', 'Interact'] |
| 8 | missing all alternatives: ['Triangle', 'Inventory'] |
| 8 | missing all alternatives: ['Triangle', 'Switch Weapon'] |
| 8 | missing all alternatives: ['Triangle', 'สลับอาวุธ'] |
| 8 | missing all alternatives: ['Triangle', 'แสดงอารมณ์'] |
| 8 | missing all alternatives: ['eFootball', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['maintenance', 'Maintenance', '09:00'] |
| 8 | missing required: Little Nightmares II |
| 8 | missing required: New Super Mario Bros. U Deluxe |
| 8 | missing required: PlayStation 5 Zone |
| 8 | missing required: Resident Evil 4 (Remake) |
| 8 | missing required: The Legend of Zelda |
| 8 | route:contact expected:['penalty', 'rules'] |
| 8 | route:general expected:['reservation'] |
| 8 | route:knowledge expected:['competition_rules', 'general', 'clarification'] |
| 8 | route:knowledge expected:['service_fee', 'games'] |
| 8 | route:reservation expected:['no_answer'] |
| 8 | route:service_fee expected:['penalty', 'rules'] |
| 8 | validation errors: ['missing_requested_field:details', 'missing_requested_field:conditions_all'] |
| 7 | missing all alternatives: ['Cross', 'กระโดด / ขว้าง / โจมตี'] |
| 7 | missing all alternatives: ['Cross', 'ลูกเตะซ้าย'] |
| 7 | missing all alternatives: ['Mario Kart Live: Home Circuit', 'รายการเกมปัจจุบัน', 'ยังไม่พบ'] |
| 7 | missing all alternatives: ['R3 (Click Right Stick)', 'มุมมองบุคคลที่หนึ่ง'] |
| 7 | missing all alternatives: ['R3 (Click Right Stick)', 'ล็อกเป้าหมาย'] |
| 7 | missing_complete_clause:4.2.1. All participants must have at least 18 heroes for the "5v5" mode (formerly known as Tournament Mode). |
| 7 | missing_complete_clause:4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game. |
| 7 | missing_complete_clause:4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่ |
| 7 | missing_complete_clause:4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate. |
| 7 | missing_complete_clause:4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ |
| 7 | missing_complete_clause:4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม |
| 7 | missing_complete_clause:5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers. |
| 7 | missing_complete_clause:Assist buttons or special assist systems are allowed |
| 7 | missing_complete_clause:If a bug occurs before either side deals damage, officials may roll back the round. |
| 7 | missing_complete_clause:If a forfeit is imposed, the result for that map is recorded as 13-0. |
| 7 | missing_complete_clause:If damage has already been dealt, no rollback is allowed unless through the Challenge process. |
| 7 | missing_complete_clause:New agents may not be used for approximately 2 weeks after release in Competitive mode. |
| 7 | missing_complete_clause:New maps may not be used for approximately 4 weeks after release in Competitive mode. |
| 7 | missing_complete_clause:No team member changes are allowed during the competition period |
| 7 | missing_complete_clause:Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must hand them to the referees before every match. |
| 7 | missing_complete_clause:Round time: 1:55 minutes  /  Freeze time: 15 seconds |
| 7 | missing_complete_clause:Rounds per game (Round): 3 |
| 7 | missing_complete_clause:The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs. |
| 7 | missing_complete_clause:Time per round (Timer): 60 seconds |
| 7 | missing_complete_clause:ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง |
| 7 | route:no_answer expected:['competition_rules'] |
| 7 | validation errors: ['missing_requested_field:details', 'missing_requested_field:players_max'] |
| 6 | missing all alternatives: ['1 / 2 / 3 / 4 / 5', 'Select weapon slots'] |
| 6 | missing all alternatives: ['4', 'Equip/Use Spike'] |
| 6 | missing all alternatives: ['4', 'หยิบ/ใช้ Spike'] |
| 6 | missing all alternatives: ['A / B', 'Jump'] |
| 6 | missing all alternatives: ['Analogue control scheme', 'Move using sticks'] |
| 6 | missing all alternatives: ['B', 'เก็บอาวุธ / วิ่งเร็ว'] |
| 6 | missing all alternatives: ['Circle (วงกลม)', 'Cancel'] |
| 6 | missing all alternatives: ['Circle', 'Crouch / Slide'] |
| 6 | missing all alternatives: ['Circle', 'Eikonic Feat'] |
| 6 | missing all alternatives: ['Circle', 'Hand Brake'] |
| 6 | missing all alternatives: ['Circle', 'โต้ตอบ'] |
| 6 | missing all alternatives: ['Circle', 'ไฟฉาย / รีโมท'] |
| 6 | missing all alternatives: ['Cross / Square / L1 / R1', 'หยิบ / วาง'] |
| 6 | missing all alternatives: ['Cross', 'Ground Pass / Header'] |
| 6 | missing all alternatives: ['Ctrl', 'Walk'] |
| 6 | missing all alternatives: ['D / F', 'ใช้ Summoner Spell'] |
| 6 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Weapon Cross (Up / Down / Left / Right)'] |
| 6 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'ติดตั้งอาวุธด่วน'] |
| 6 | missing all alternatives: ['D-Pad Left / Right', 'สลับเครื่องมือ'] |
| 6 | missing all alternatives: ['D-Pad Left', 'ติดตั้งอาวุธรอง'] |
| 6 | missing all alternatives: ['D-Pad Right', 'Spell Menu'] |
| 6 | missing all alternatives: ['D-Pad Up / Down', 'แถบแอคชั่น: เลือก/ใช้งาน'] |
| 6 | missing all alternatives: ['D-Pad Up', 'Swap Arrow Type'] |
| 6 | missing all alternatives: ['D-Pad Up', 'เปลี่ยนชนิดลูกธนู'] |
| 6 | missing all alternatives: ['D-Pad', 'Use Battle Item (Ninja Tools)'] |
| 6 | missing all alternatives: ['D-Pad', 'ควบคุมจอ MFD'] |
| 6 | missing all alternatives: ['D-Pad', 'ใช้อุปกรณ์นินจา'] |
| 6 | missing all alternatives: ['F1 / F2 / F3 / F4 / F5', 'Camera to allies'] |
| 6 | missing all alternatives: ['G', 'ทิ้งอาวุธ'] |
| 6 | missing all alternatives: ['Gran Turismo 7'] |
| 6 | missing all alternatives: ['L1', 'ยกการ์ด / ป้องกัน'] |
| 6 | missing all alternatives: ['L1', 'ใช้อุปกรณ์ยุทธวิธี'] |
| 6 | missing all alternatives: ['L2 (Hold)', 'เล็ง (กดค้าง)'] |
| 6 | missing all alternatives: ['L2', 'บังบอล'] |
| 6 | missing all alternatives: ['L2', 'เล็งเป้า / เบรกรถ'] |
| 6 | missing all alternatives: ['L3 (Click Left Stick)', 'Crouch'] |
| 6 | missing all alternatives: ['L3 + R3', 'Spartan rage'] |
| 6 | missing all alternatives: ['L3', 'Headlights'] |
| 6 | missing all alternatives: ['LS (Left Stick)', 'Move'] |
| 6 | missing all alternatives: ['Options', 'Open game menu'] |
| 6 | missing all alternatives: ['Q / E / C / X', 'Use abilities'] |
| 6 | missing all alternatives: ['R', 'ขว้าง'] |
| 6 | missing all alternatives: ['R', 'แชทพิมพ์ข้อความ'] |
| 6 | missing all alternatives: ['R1 (While in Heat)', 'ฮีทสแมช'] |
| 6 | missing all alternatives: ['R1 + Circle', 'ยิงปั่นโค้ง'] |
| 6 | missing all alternatives: ['R1 / R2', 'Grab'] |
| 6 | missing all alternatives: ['R1', 'Change View'] |
| 6 | missing all alternatives: ['R1', 'Web-Shooter / Gadget (Hold)'] |
| 6 | missing all alternatives: ['R1', 'สลับอาวุธด่วน / โหมดฟังเสียง (กดค้าง)'] |
| 6 | missing all alternatives: ['R1', 'เปิดใช้งาน Heat'] |
| 6 | missing all alternatives: ['R2 (Hold)', 'Swing / Parkour'] |
| 6 | missing all alternatives: ['R2', 'Accelerate'] |
| 6 | missing all alternatives: ['R2', 'Attack'] |
| 6 | missing all alternatives: ['R2', 'Heavy Attack / Heavy Runic Attack (While blocking)'] |
| 6 | missing all alternatives: ['R2', 'ป้องกัน'] |
| 6 | missing all alternatives: ['R2', 'ยิงหลัก'] |
| 6 | missing all alternatives: ['R3 (Click Right Stick)', '1st Person view'] |
| 6 | missing all alternatives: ['R3 (Click Right Stick)', 'Crouch'] |
| 6 | missing all alternatives: ['R3 (Click Right Stick)', 'Zoom (with scope)'] |
| 6 | missing all alternatives: ['R3', 'Nitro / Overtake'] |
| 6 | missing all alternatives: ['Right Mouse Button', 'Alternate Fire'] |
| 6 | missing all alternatives: ['Right Mouse Button', 'Soft Aim / ADS'] |
| 6 | missing all alternatives: ['Shift', 'วิ่ง / กลั้นหายใจ'] |
| 6 | missing all alternatives: ['Square', 'Chop / Throw'] |
| 6 | missing all alternatives: ['Square', 'Shift Down'] |
| 6 | missing all alternatives: ['Square', 'Use Item'] |
| 6 | missing all alternatives: ['Square', 'คู่หูโจมตี'] |
| 6 | missing all alternatives: ['Square', 'ดาวกระจาย'] |
| 6 | missing all alternatives: ['Tab', 'Show Scoreboard'] |
| 6 | missing all alternatives: ['Touch Pad', 'กระเป๋าเป้ / เมนูคราฟต์ของ'] |
| 6 | missing all alternatives: ['Touch Pad', 'สัมภาระ / เมนูกระเป๋าเก็บของ'] |
| 6 | missing all alternatives: ['Triangle', 'ชักอาวุธ'] |
| 6 | missing all alternatives: ['X Button', 'Confirm selection'] |
| 6 | missing all alternatives: ['X', 'Horn'] |
| 6 | missing all alternatives: ['Y', 'สลับล็อกกล้อง'] |
| 6 | missing all alternatives: ['ZL', 'เป่าลม'] |
| 6 | missing all alternatives: ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง'] |
| 6 | missing required: God of War Ragnarök |
| 6 | missing required: Moving Out 2 |
| 6 | missing required: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS |
| 6 | missing required: Ring Fit Adventure |
| 6 | missing required: Super Mario Odyssey |
| 6 | missing required: Super Smash Bros. Ultimate |
| 6 | missing required: The Last of Us Part II |
| 6 | missing rulebook target(s): ['competition_rules_rov_blueket_2025_men'] |
| 6 | missing_complete_clause:1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN |
| 6 | missing_complete_clause:1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้ |
| 6 | missing_complete_clause:2 requests per map during regulation (first 24 rounds), 60 seconds each. |
| 6 | missing_complete_clause:2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น |
| 6 | missing_complete_clause:4. Do not install your own software on the provided computers. |
| 6 | missing_complete_clause:4. Only drinking water in sealed containers and chewing gum are permitted. |
| 6 | missing_complete_clause:4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side. |
| 6 | missing_complete_clause:4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง |
| 6 | missing_complete_clause:4.1.4. If a team starts the match more than 15 minutes after the scheduled time, the delayed team will be immediately forfeited. |
| 6 | missing_complete_clause:4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode) |
| 6 | missing_complete_clause:4.2.2. Use Global Ban/Pick hero selection. |
| 6 | missing_complete_clause:4.2.3. Runes and enhancement systems may be used as desired. |
| 6 | missing_complete_clause:Abilities must not be used outside map boundaries to obtain information or an advantage. |
| 6 | missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping. |
| 6 | missing_complete_clause:Competitive mode (5v5) |
| 6 | missing_complete_clause:During preparation phase, the number of personnel shall not exceed 6 players. |
| 6 | missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification. |
| 6 | missing_complete_clause:Food and drinks: Only drinking water in sealed containers and chewing gum are permitted. |
| 6 | missing_complete_clause:Initial money: $800  /  Bomb time: 40 seconds |
| 6 | missing_complete_clause:Judgment authority: The referees' decisions and the organizers' rulings are final. The organizing side reserves the right to amend rules as appropriate for fairness. |
| 6 | missing_complete_clause:Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified. |
| 6 | missing_complete_clause:Macros (both software- and hardware-based) are strictly prohibited. |
| 6 | missing_complete_clause:Map selection uses MAPBAN.GG |
| 6 | missing_complete_clause:Match schedule: The tournament bracket will be announced at least 1 day in advance. Entry must be confirmed before the match starts. Late arrivals may be disqualified. |
| 6 | missing_complete_clause:No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.) |
| 6 | missing_complete_clause:No use of bugs or glitches that provide an advantage |
| 6 | missing_complete_clause:Overtime: 3 rounds per side (6 rounds total). The first team to win 4 of the 6 rounds wins. Starting money is $10,000, and overtime may be played without limit. |
| 6 | missing_complete_clause:Personnel: During Match Prep, no more than 6 players may be present. |
| 6 | missing_complete_clause:Players are responsible for the quality and readiness of their own equipment. |
| 6 | missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor. |
| 6 | missing_complete_clause:Tournament format: Single Elimination |
| 6 | missing_complete_clause:Watching streams: Players are prohibited from watching live streams during competition. |
| 6 | route:games expected:['reservation', 'schedule'] |
| 6 | route:knowledge expected:['games', 'clarification', 'no_answer'] |
| 6 | route:knowledge expected:['no_answer', 'games', 'general'] |
| 6 | route:rules expected:['no_answer'] |
| 5 | intent:common_read expected:multi_question_split |
| 5 | missing all alternatives: ['+ Button on controller-holding screen', 'เลือกโหมดสายรัดขาใน Soccer ตอนเล่น Local/Friends'] |
| 5 | missing all alternatives: ['A / B', 'กระโดด'] |
| 5 | missing all alternatives: ['A Button', 'ยกเลิกการเลือก'] |
| 5 | missing all alternatives: ['Alt + Q / W / E / R', 'ใช้สกิลใส่ตัวเอง'] |
| 5 | missing all alternatives: ['B', 'โจมตีพิเศษ'] |
| 5 | missing all alternatives: ['Builder Pro / Combat Pro / Custom', 'ชุดปุ่มควบคุม'] |
| 5 | missing all alternatives: ['Circle / D-Pad Right', 'พุ่งตัว'] |
| 5 | missing all alternatives: ['Circle', 'ยิงประตู / วอลเลย์ / โหม่ง'] |
| 5 | missing all alternatives: ['Circle', 'ลูกเตะขวา'] |
| 5 | missing all alternatives: ['Circle', 'โจมตีระยะประชิด'] |
| 5 | missing all alternatives: ['Cockpit', 'Cockpit #01-#02'] |
| 5 | missing all alternatives: ['Cross', 'เพิ่มเกียร์'] |
| 5 | missing all alternatives: ['D-Pad', 'แสดงอารมณ์'] |
| 5 | missing all alternatives: ['Gaming Mouse', 'Gaming Mouse'] |
| 5 | missing all alternatives: ['Head/body movement', 'หลบและจัดตำแหน่งร่างกาย'] |
| 5 | missing all alternatives: ['L1', 'รีเซ็ตมุมกล้อง / เมนูลัด (กดค้าง)'] |
| 5 | missing all alternatives: ['L2 / R2', 'หั่น / ขว้าง'] |
| 5 | missing all alternatives: ['L2', 'เบรก'] |
| 5 | missing all alternatives: ['L3 + R3', 'พลังสปาร์ตัน'] |
| 5 | missing all alternatives: ['PS VR2 Sense grip button', 'จับวัตถุในเกม'] |
| 5 | missing all alternatives: ['R (Right Stick)', 'ควบคุมมุมมอง / หันกล้อง'] |
| 5 | missing all alternatives: ['R', 'มุมกล้อง'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'กล้องส่องทางไกล'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ค้นหาผู้เล่นอื่น'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ซูมกล้องเล็ง'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ย่อตัว'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ระบบกูอิจิ'] |
| 5 | missing all alternatives: ['R3', 'แสดงเป้าหมาย / สแกนพื้นที่'] |
| 5 | missing all alternatives: ['Ring-Con tilt', 'เลื่อนเคอร์เซอร์ด้วย Ring-Con'] |
| 5 | missing all alternatives: ['Shift + Q / W / E / R', 'ใช้สกิลแบบ quick cast'] |
| 5 | missing all alternatives: ['Space Bar', 'กระโดด'] |
| 5 | missing all alternatives: ['Spacebar', 'กระโดด'] |
| 5 | missing all alternatives: ['Square', 'วิ่งเร็ว'] |
| 5 | missing all alternatives: ['Square', 'โจมตีด้วยดาบ / โจมตีระยะประชิด'] |
| 5 | missing all alternatives: ['Triangle', 'คาถานินจา / จักระ'] |
| 5 | missing all alternatives: ['Triangle', 'จ่ายบอลทะลุช่อง'] |
| 5 | missing all alternatives: ['Triangle', 'โจมตีเวทมนตร์'] |
| 5 | missing all alternatives: ['X', 'มองหลัง'] |
| 5 | missing all alternatives: ['Z', 'หมอบ'] |
| 5 | missing required: PC Zone |
| 5 | missing_complete_clause:1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน |
| 5 | missing_complete_clause:2. เวลาต่อรอบ 1:55 นาที  /  Freeze time: 15 วินาที |
| 5 | missing_complete_clause:3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้ |
| 5 | missing_complete_clause:3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง |
| 5 | missing_complete_clause:4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay. |
| 5 | missing_complete_clause:5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ |
| 5 | missing_complete_clause:การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0 |
| 5 | missing_complete_clause:จำนวนรอบต่อเกม (Round): 3 |
| 5 | missing_complete_clause:หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge |
| 5 | missing_complete_clause:หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้ |
| 5 | missing_complete_clause:อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ |
| 5 | missing_complete_clause:เวลาแข่งขันต่อรอบ (Timer): 60 วินาที |
| 5 | missing_complete_clause:เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive |
| 5 | missing_complete_clause:แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive |
| 5 | route:no_answer expected:['members', 'overview'] |
| 5 | status:answer expected:safe_no_answer |
| 4 | intent:common_read expected:detail |
| 4 | intent:common_read expected:service_fee_query |
| 4 | missing all alternatives: ['+ (Plus)', 'หยุดเกมชั่วคราว'] |
| 4 | missing all alternatives: ['+ (Plus)', 'เปิดช่องเก็บของ'] |
| 4 | missing all alternatives: ['+ Button on controller-holding screen', 'Select Soccer Leg-Strap Mode locally'] |
| 4 | missing all alternatives: ['- (Minus)', 'Save & Quit'] |
| 4 | missing all alternatives: ['- (Minus)', 'Skip'] |
| 4 | missing all alternatives: ['- (Minus)', 'ข้าม'] |
| 4 | missing all alternatives: ['- (Minus)', 'บันทึกและออกจากเกม'] |
| 4 | missing all alternatives: ['1 / 2 / 3 / 4 / 5 / 6 / 7', 'Use items / trinket'] |
| 4 | missing all alternatives: ['1 / 2 / 3 / 4 / 5 / 6 / 7', 'ใช้ไอเทมหรือ trinket'] |
| 4 | missing all alternatives: ['1 / 2 / 3 / 4 / 5', 'เลือกอาวุธ'] |
| 4 | missing all alternatives: ['1 / 2 / 3', 'Equip weapons'] |
| 4 | missing all alternatives: ['1 / 2 / 3', 'Select weapons'] |
| 4 | missing all alternatives: ['4', 'Cycle Grenades'] |
| 4 | missing all alternatives: ['4', 'เลือก/วนระเบิด'] |
| 4 | missing all alternatives: ['A Button', 'Cancel selection'] |
| 4 | missing all alternatives: ['Alt + Q / W / E / R', 'Self cast abilities'] |
| 4 | missing all alternatives: ['Alt', 'Free look'] |
| 4 | missing all alternatives: ['Alt', 'มองอิสระ'] |
| 4 | missing all alternatives: ['B', 'กลับฐาน'] |
| 4 | missing all alternatives: ['B', 'เปลี่ยนการเคลื่อนที่'] |
| 4 | missing all alternatives: ['B', 'เปลี่ยนโหมดยิง'] |
| 4 | missing all alternatives: ['B', 'เปิดร้านซื้ออาวุธ'] |
| 4 | missing all alternatives: ['B', 'เปิดเมนูซื้อของ'] |
| 4 | missing all alternatives: ['Builder Pro / Combat Pro / Custom', 'Controller binding presets'] |
| 4 | missing all alternatives: ['Button controls', 'Play boards and minigames'] |
| 4 | missing all alternatives: ['Call of Duty', 'วิธีเล่น', 'เล่นได้ที่'] |
| 4 | missing all alternatives: ['Circle (วงกลม)', 'ยกเลิก'] |
| 4 | missing all alternatives: ['Circle / D-Pad Right', 'Sprint'] |
| 4 | missing all alternatives: ['Circle', 'Cancel'] |
| 4 | missing all alternatives: ['Circle', 'Close-Range Attack'] |
| 4 | missing all alternatives: ['Circle', 'Crouch/Prone/Slide'] |
| 4 | missing all alternatives: ['Circle', 'Dash'] |
| 4 | missing all alternatives: ['Circle', 'Flashlight / Remote'] |
| 4 | missing all alternatives: ['Circle', 'Interact / Activate Relic (While blocking)'] |
| 4 | missing all alternatives: ['Circle', 'Interact'] |
| 4 | missing all alternatives: ['Circle', 'Melee'] |
| 4 | missing all alternatives: ['Circle', 'Right Kick'] |
| 4 | missing all alternatives: ['Circle', 'Roll / Evade / Take Cover'] |
| 4 | missing all alternatives: ['Circle', 'Shoot / Shoulder Charge'] |
| 4 | missing all alternatives: ['Circle', 'Shoot / Volley / Header'] |
| 4 | missing all alternatives: ['Circle', 'กลิ้งหลบ / เข้าที่กำบัง'] |
| 4 | missing all alternatives: ['Circle', 'กลิ้งหลบ'] |
| 4 | missing all alternatives: ['Circle', 'พุ่งตัว'] |
| 4 | missing all alternatives: ['Circle', 'ยกเลิก / ย้อนกลับ'] |
| 4 | missing all alternatives: ['Circle', 'ยิง / เบียดแย่งบอล'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / สไลด์'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบ'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบคลาน'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว'] |
| 4 | missing all alternatives: ['Circle', 'หลบหลีก'] |
| 4 | missing all alternatives: ['Circle', 'เบรกมือ'] |
| 4 | missing all alternatives: ['Circle', 'โจมตีประชิด'] |
| 4 | missing all alternatives: ['Circle', 'โต้ตอบ / ใช้งานรีลิค'] |
| 4 | missing all alternatives: ['Circle', 'ใช้ Eikonic Feat'] |
| 4 | missing all alternatives: ['Controller Mapping page', 'Change controller preset'] |
| 4 | missing all alternatives: ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Cross (กากบาท)', 'Jump'] |
| 4 | missing all alternatives: ['Cross (กากบาท)', 'กระโดด'] |
| 4 | missing all alternatives: ['Cross / Square / L1 / R1', 'Pick Up / Drop'] |
| 4 | missing all alternatives: ['Cross', 'Crouch / Dodge / Jump'] |
| 4 | missing all alternatives: ['Cross', 'Jump / Climb / Scope (While aiming)'] |
| 4 | missing all alternatives: ['Cross', 'Jump / Climb / Shoulder Swap'] |
| 4 | missing all alternatives: ['Cross', 'Jump / Throw / Attack'] |
| 4 | missing all alternatives: ['Cross', 'Jump/Mantle'] |
| 4 | missing all alternatives: ['Cross', 'Left Kick'] |
| 4 | missing all alternatives: ['Cross', 'Low Pass / Press'] |
| 4 | missing all alternatives: ['Cross', 'Pick Up / Drop'] |
| 4 | missing all alternatives: ['Cross', 'Shift Up'] |
| 4 | missing all alternatives: ['Cross', 'Sidestep / Dodge (double tap)'] |
| 4 | missing all alternatives: ['Cross', 'Use Tactical Equipment'] |
| 4 | missing all alternatives: ['Cross', 'กระโดด / ปีนป่าย / ซูมสโคป (ขณะเล็ง)'] |
| 4 | missing all alternatives: ['Cross', 'กระโดด / ปีนป่าย / สลับมุมกล้อง'] |
| 4 | missing all alternatives: ['Cross', 'ย่อตัว / กลิ้งหลบ / กระโดด'] |
| 4 | missing all alternatives: ['Cross', 'สเตปหลบ / กลิ้งหลบ'] |
| 4 | missing all alternatives: ['Cross', 'ส่งบอลเลียด / เพรสซิง'] |
| 4 | missing all alternatives: ['Cross', 'หยิบ / วาง'] |
| 4 | missing all alternatives: ['Cross', 'โต้ตอบ / สำรวจ'] |
| 4 | missing all alternatives: ['Cross', 'ใช้อุปกรณ์ยุทธวิธี'] |
| 4 | missing all alternatives: ['Ctrl', 'เดิน'] |
| 4 | missing all alternatives: ['D / F', 'Summoner Spells'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Equip Quick Slot weapons'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Tool selection (Up / Down / Left / Right)'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอาวุธกากบาท'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอุปกรณ์ด่วน'] |
| 4 | missing all alternatives: ['D-Pad (Up / Left / Right)', 'Select Weapon'] |
| 4 | missing all alternatives: ['D-Pad (Up / Left / Right)', 'เลือกอาวุธ'] |
| 4 | missing all alternatives: ['D-Pad (Up, Down, Left, Right)', 'Taunt'] |
| 4 | missing all alternatives: ['D-Pad (Up, Down, Left, Right)', 'ยั่วยุ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Duck'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Equip Tertiary Weapon'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Locate Vehicle'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Photo mode'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Store Tool'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Whistle'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ตรวจสอบตำแหน่งรถ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ติดตั้งอาวุธที่สาม'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ผิวปากเรียกม้า'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ย่อตัว / ก้มหลบ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'เก็บเครื่องมือ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'โหมดถ่ายภาพ'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Action Bar: Scroll Left / Right'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Change Shield/Arrow / Change Weapon/Bow'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Change Tool'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Shortcut 1 / Shortcut 2'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'คีย์ลัด 1 / 2'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'เปลี่ยนอุปกรณ์สวมใส่'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'แถบแอคชั่น: เลื่อนซ้าย/ขวา'] |
| 4 | missing all alternatives: ['D-Pad Left', 'Equip Secondary Weapon'] |
| 4 | missing all alternatives: ['D-Pad Left', 'Move Backward'] |
| 4 | missing all alternatives: ['D-Pad Left', 'Revelio'] |
| 4 | missing all alternatives: ['D-Pad Left', 'ถอยหลัง / บล็อก'] |
| 4 | missing all alternatives: ['D-Pad Left', 'เรเวลิโอ'] |
| 4 | missing all alternatives: ['D-Pad Right', 'Equip Primary Weapon'] |
| 4 | missing all alternatives: ['D-Pad Right', 'amiibo'] |
| 4 | missing all alternatives: ['D-Pad Right', 'ติดตั้งอาวุธหลัก'] |
| 4 | missing all alternatives: ['D-Pad Right', 'สแกนอะมีโบ'] |
| 4 | missing all alternatives: ['D-Pad Right', 'เมนูคาถา'] |
| 4 | missing all alternatives: ['D-Pad Up / Down', 'Action Bar: Select/Perform Action'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Camouflage (Miles)'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Change Rune'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Charmed Compass / Quest Info (Hold)'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Jump'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Map'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Tool Ring'] |
| 4 | missing all alternatives: ['D-Pad Up', 'กระโดด'] |
| 4 | missing all alternatives: ['D-Pad Up', 'พรางตัว (ไมลส์)'] |
| 4 | missing all alternatives: ['D-Pad Up', 'วงล้อเครื่องมือ'] |
| 4 | missing all alternatives: ['D-Pad Up', 'เข็มทิศ / ข้อมูลเควสต์'] |
| 4 | missing all alternatives: ['D-Pad Up', 'เปลี่ยนรูน'] |
| 4 | missing all alternatives: ['D-Pad Up', 'แผนที่'] |
| 4 | missing all alternatives: ['D-Pad', 'Campaign, Multiplayer or Co-Op specific'] |
| 4 | missing all alternatives: ['D-Pad', 'Change Weapon'] |
| 4 | missing all alternatives: ['D-Pad', 'Emote'] |
| 4 | missing all alternatives: ['D-Pad', 'License'] |
| 4 | missing all alternatives: ['D-Pad', 'MFD Controls'] |
| 4 | missing all alternatives: ['D-Pad', 'คำสั่งเฉพาะโหมด'] |
| 4 | missing all alternatives: ['D-Pad', 'ดูใบขับขี่และสถิติ'] |
| 4 | missing all alternatives: ['D-Pad', 'เปลี่ยนอาวุธ'] |
| 4 | missing all alternatives: ['Directional Button Left', 'Switch Items and Torgal Commands'] |
| 4 | missing all alternatives: ['Directional Button Left', 'สลับระหว่างไอเทมกับคำสั่ง Torgal'] |
| 4 | missing all alternatives: ['Directional Buttons Up / Right / Down', 'Item Shortcuts / Torgal Commands'] |
| 4 | missing all alternatives: ['Directional Buttons Up / Right / Down', 'ทางลัดไอเทมหรือคำสั่ง Torgal'] |
| 4 | missing all alternatives: ['F1 / F2 / F3 / F4 / F5', 'เลื่อนกล้องไปหาเพื่อนร่วมทีม'] |
| 4 | missing all alternatives: ['Gaming Mouse'] |
| 4 | missing all alternatives: ['Gesture control scheme', 'Move using physical movements'] |
| 4 | missing all alternatives: ['Head/body movement', 'Dodge and position body'] |
| 4 | missing all alternatives: ['Joy-Con (R) Control Stick', 'Move cursor'] |
| 4 | missing all alternatives: ['Joy-Con motion', 'Play sport actions'] |
| 4 | missing all alternatives: ['L (Left Stick) / R (Right Stick)', 'Move'] |
| 4 | missing all alternatives: ['L (Left Stick)', 'Move / Strafe (While locked)'] |
| 4 | missing all alternatives: ['L / R', 'Grab'] |
| 4 | missing all alternatives: ['L / R', 'จับทุ่ม'] |
| 4 | missing all alternatives: ['L / ZL / R / ZR', 'Grab'] |
| 4 | missing all alternatives: ['L1 (Hold)', 'Block'] |
| 4 | missing all alternatives: ['L1 (Hold)', 'ป้องกัน (กดค้าง)'] |
| 4 | missing all alternatives: ['L1 + Triangle', 'Lobbed Through Pass'] |
| 4 | missing all alternatives: ['L1 + Triangle', 'ยกบอลทะลุช่อง'] |
| 4 | missing all alternatives: ['L1 / L2', 'Crouch / Slide'] |
| 4 | missing all alternatives: ['L1 / L2', 'ย่อตัว / สไลด์'] |
| 4 | missing all alternatives: ['L1', 'Change Player'] |
| 4 | missing all alternatives: ['L1', 'Dodge / Ability (Hold)'] |
| 4 | missing all alternatives: ['L1', 'Dodge'] |
| 4 | missing all alternatives: ['L1', 'Equipment Wheel'] |
| 4 | missing all alternatives: ['L1', 'Guard'] |
| 4 | missing all alternatives: ['L1', 'Jump/Mantle'] |
| 4 | missing all alternatives: ['L1', 'Lock On'] |
| 4 | missing all alternatives: ['L1', 'Look Back'] |
| 4 | missing all alternatives: ['L1', 'Parry'] |
| 4 | missing all alternatives: ['L1', 'Reset Camera / Radial Menu (Hold)'] |
| 4 | missing all alternatives: ['L1', 'Rope'] |
| 4 | missing all alternatives: ['L1', 'Special Style'] |
| 4 | missing all alternatives: ['L1', 'Sprint (Hold)'] |
| 4 | missing all alternatives: ['L1', 'Support 1'] |
| 4 | missing all alternatives: ['L1', 'Use Tactical Equipment'] |
| 4 | missing all alternatives: ['L1', 'Use Tool / Open Tool Wheel (Hold)'] |
| 4 | missing all alternatives: ['L1', 'กำลังเสริม 1'] |
| 4 | missing all alternatives: ['L1', 'ปัดป้อง'] |
| 4 | missing all alternatives: ['L1', 'มองหลัง'] |
| 4 | missing all alternatives: ['L1', 'ล็อกเป้าหมาย'] |
| 4 | missing all alternatives: ['L1', 'วงล้ออุปกรณ์'] |
| 4 | missing all alternatives: ['L1', 'วิ่งสปรินต์ (กดค้าง)'] |
| 4 | missing all alternatives: ['L1', 'สเปเชียลสไตล์'] |
| 4 | missing all alternatives: ['L1', 'หลบหลีก'] |
| 4 | missing all alternatives: ['L1', 'หลบหลีก(ปัดป้อง) / สกิล'] |
| 4 | missing all alternatives: ['L1', 'เปลี่ยนตัวผู้เล่น'] |
| 4 | missing all alternatives: ['L1', 'ใช้เชือกสลิง / โหนสลิง'] |
| 4 | missing all alternatives: ['L1', 'ใช้ไอเทม / วงล้อเครื่องมือ'] |
| 4 | missing all alternatives: ['L2 (Hold)', 'เล็งเป้าหมาย'] |
| 4 | missing all alternatives: ['L2 (hold) + Direction', 'Shield / Jockey'] |
| 4 | missing all alternatives: ['L2 (hold) + Direction', 'บังบอล / คุมเชิง'] |
| 4 | missing all alternatives: ['L2 / R2', 'Chop / Throw'] |
| 4 | missing all alternatives: ['L2', 'Aim / Brake'] |
| 4 | missing all alternatives: ['L2', 'Aim Down Sight Behavior'] |
| 4 | missing all alternatives: ['L2', 'Aim'] |
| 4 | missing all alternatives: ['L2', 'Brake'] |
| 4 | missing all alternatives: ['L2', 'Chapter Abilities'] |
| 4 | missing all alternatives: ['L2', 'Cycle / Switch Eikons'] |
| 4 | missing all alternatives: ['L2', 'Protect Ball'] |
| 4 | missing all alternatives: ['L2', 'Substitution Ninjutsu'] |
| 4 | missing all alternatives: ['L2', 'ความสามารถประจำด่าน (ซ้าย)'] |
| 4 | missing all alternatives: ['L2', 'คาถาสลับร่าง'] |
| 4 | missing all alternatives: ['L2', 'สลับ Eikon'] |
| 4 | missing all alternatives: ['L2', 'เล็งปืน (ADS)'] |
| 4 | missing all alternatives: ['L2', 'เล็งผ่านศูนย์'] |
| 4 | missing all alternatives: ['L2', 'เล็งผ่านศูนย์เล็ง'] |
| 4 | missing all alternatives: ['L2', 'เล็งเป้า / เล็งปืน'] |
| 4 | missing all alternatives: ['L3 (Click Left Stick)', 'Mark Enemy'] |
| 4 | missing all alternatives: ['L3 + R3', 'Limit Break'] |
| 4 | missing all alternatives: ['L3 + R3', 'ใช้ Limit Break'] |
| 4 | missing all alternatives: ['L3', 'Perch / Dive'] |
| 4 | missing all alternatives: ['L3', 'Sprint (Hold)'] |
| 4 | missing all alternatives: ['L3', 'Sprint/Tactical Sprint/Focus'] |
| 4 | missing all alternatives: ['L3', 'Sprint/Tactical Sprint/Steady Aim'] |
| 4 | missing all alternatives: ['L3', 'วิ่ง (กดค้าง)'] |
| 4 | missing all alternatives: ['L3', 'ไฟหน้า'] |
| 4 | missing all alternatives: ['Left Ctrl', 'Crouch'] |
| 4 | missing all alternatives: ['Left Ctrl', 'Duck'] |
| 4 | missing all alternatives: ['Left Mouse Button', 'Shoot'] |
| 4 | missing all alternatives: ['Left PS VR2 Sense controller motion', 'Left-hand saber slash'] |
| 4 | missing all alternatives: ['Left Stick', 'Move / Dribble'] |
| 4 | missing all alternatives: ['Left Stick', 'Steer'] |
| 4 | missing all alternatives: ['Left Stick', 'เคลื่อนที่ / เลี้ยงบอล'] |
| 4 | missing all alternatives: ['Left Stick', 'เลี้ยว'] |
| 4 | missing all alternatives: ['Nintendo Switch', 'Zone'] |
| 4 | missing all alternatives: ['One Joy-Con', 'Play character'] |
| 4 | missing all alternatives: ['Options', 'Main Menu / Pause'] |
| 4 | missing all alternatives: ['Options', 'เปิดเมนูหลัก / หยุดเกม'] |
| 4 | missing all alternatives: ['PS VR2 Sense grip button', 'Grab objects'] |
| 4 | missing all alternatives: ['Press Ring-Con inward', 'Confirm with Ring-Con'] |
| 4 | missing all alternatives: ['Press Ring-Con inward', 'ยืนยันด้วย Ring-Con'] |
| 4 | missing all alternatives: ['Pull Ring-Con outward', 'Cancel with Ring-Con'] |
| 4 | missing all alternatives: ['Pull Ring-Con outward', 'ยกเลิกด้วย Ring-Con'] |
| 4 | missing all alternatives: ['Q / E / C / X', 'ใช้สกิล Agent'] |
| 4 | missing all alternatives: ['Q / E', 'Lean Left / Lean Right'] |
| 4 | missing all alternatives: ['Q / E', 'เอียงซ้าย / เอียงขวา'] |
| 4 | missing all alternatives: ['Q / W / E / R', 'Cast abilities'] |
| 4 | missing all alternatives: ['Q', 'สลับกลับอาวุธล่าสุด'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'Smash Attack'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'Turn'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'View'] |
| 4 | missing all alternatives: ['R', 'ดริฟต์'] |
| 4 | missing all alternatives: ['R', 'รีเซ็ตกล้อง'] |
| 4 | missing all alternatives: ['R1 (While in Heat)', 'Heat Smash'] |
| 4 | missing all alternatives: ['R1 + Circle', 'Finesse Shot'] |
| 4 | missing all alternatives: ['R1 + Cross', 'Driven Ground Pass'] |
| 4 | missing all alternatives: ['R1 + Cross', 'ส่งเลียดแบบพุ่งแรง'] |
| 4 | missing all alternatives: ['R1 / R2', 'จับ'] |
| 4 | missing all alternatives: ['R1', 'Ancient Magic Throw'] |
| 4 | missing all alternatives: ['R1', 'Evade'] |
| 4 | missing all alternatives: ['R1', 'Grenade'] |
| 4 | missing all alternatives: ['R1', 'Heal'] |
| 4 | missing all alternatives: ['R1', 'Heat Activate'] |
| 4 | missing all alternatives: ['R1', 'Light Attack / Light Runic Attack (While blocking) / Throw (While aiming)'] |
| 4 | missing all alternatives: ['R1', 'Listen mode (Hold) / Switch Weapon'] |
| 4 | missing all alternatives: ['R1', 'Rope Grapple'] |
| 4 | missing all alternatives: ['R1', 'Specialization'] |
| 4 | missing all alternatives: ['R1', 'Sprint (Hold)'] |
| 4 | missing all alternatives: ['R1', 'Sprint / Quick Turn'] |
| 4 | missing all alternatives: ['R1', 'Support 2'] |
| 4 | missing all alternatives: ['R1', 'Weapon Swap / Listen (Hold)'] |
| 4 | missing all alternatives: ['R1', 'กำลังเสริม 2'] |
| 4 | missing all alternatives: ['R1', 'ขว้างระเบิดมือ'] |
| 4 | missing all alternatives: ['R1', 'ขว้างเวทมนตร์โบราณ'] |
| 4 | missing all alternatives: ['R1', 'ความสามารถพิเศษ'] |
| 4 | missing all alternatives: ['R1', 'ฟื้นฟูพลังชีวิต / ใช้ยา'] |
| 4 | missing all alternatives: ['R1', 'ยิงใย / อุปกรณ์แก็ดเจ็ต'] |
| 4 | missing all alternatives: ['R1', 'วิ่ง / กลับหลังหัน'] |
| 4 | missing all alternatives: ['R1', 'วิ่งเร็ว (กดค้าง)'] |
| 4 | missing all alternatives: ['R1', 'หลบหลีก'] |
| 4 | missing all alternatives: ['R1', 'เปลี่ยนมุมมอง'] |
| 4 | missing all alternatives: ['R1', 'โจมตีเบา / รูนเบา / ขว้าง'] |
| 4 | missing all alternatives: ['R1', 'โหนเชือก / สลิง'] |
| 4 | missing all alternatives: ['R1', 'โหมดฟังเสียง (กดค้าง) / สลับอาวุธด่วน'] |
| 4 | missing all alternatives: ['R2 (Hold)', 'โหนใย / ปากัวร์'] |
| 4 | missing all alternatives: ['R2 (hold) + Direction', 'Sprint'] |
| 4 | missing all alternatives: ['R2 (hold) + Direction', 'วิ่งสปรินต์'] |
| 4 | missing all alternatives: ['R2 + Square / Triangle / Cross / Circle', 'Use Eikonic Ability'] |
| 4 | missing all alternatives: ['R2 + Square / Triangle / Cross / Circle', 'ใช้ Eikonic Ability ที่ผูกไว้'] |
| 4 | missing all alternatives: ['R2 + Touch Pad', 'Taunt'] |
| 4 | missing all alternatives: ['R2 + Touch Pad', 'ยั่วยุ'] |
| 4 | missing all alternatives: ['R2', 'Basic Cast / Activate Spell Set (Hold)'] |
| 4 | missing all alternatives: ['R2', 'Chapter Abilities'] |
| 4 | missing all alternatives: ['R2', 'Dash'] |
| 4 | missing all alternatives: ['R2', 'Fire / Accelerate'] |
| 4 | missing all alternatives: ['R2', 'Guard'] |
| 4 | missing all alternatives: ['R2', 'Primary Fire'] |
| 4 | missing all alternatives: ['R2', 'Ready Eikonic Abilities'] |
| 4 | missing all alternatives: ['R2', 'Reload / Use (Hold) / Fire (While aiming)'] |
| 4 | missing all alternatives: ['R2', 'Shoot (While aiming) / Reload'] |
| 4 | missing all alternatives: ['R2', 'Shoot / Knife attack'] |
| 4 | missing all alternatives: ['R2', 'ความสามารถประจำด่าน (ขวา)'] |
| 4 | missing all alternatives: ['R2', 'ยิง / โจมตีด้วยมีด'] |
| 4 | missing all alternatives: ['R2', 'ยิง'] |
| 4 | missing all alternatives: ['R2', 'ยิงปืน (ขณะเล็ง) / รีโหลดกระสุน'] |
| 4 | missing all alternatives: ['R2', 'ยิงปืน / เหยียบคันเร่ง'] |
| 4 | missing all alternatives: ['R2', 'ยิงอาวุธ'] |
| 4 | missing all alternatives: ['R2', 'รีโหลด / ใช้ไอเทม (กดค้าง) / ยิงปืน (ขณะเล็ง)'] |
| 4 | missing all alternatives: ['R2', 'เปิดชุด Eikonic Abilities'] |
| 4 | missing all alternatives: ['R2', 'เร่งความเร็ว'] |
| 4 | missing all alternatives: ['R2', 'โจมตี / ยิงปืน'] |
| 4 | missing all alternatives: ['R2', 'โจมตีพื้นฐาน / เปิดชุดคาถา'] |
| 4 | missing all alternatives: ['R2', 'โจมตีหนัก / รูนหนัก'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Find Other Player'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Gooigi'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Lock-On'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Scope'] |
| 4 | missing all alternatives: ['R3', 'Change Stance/Slide/Dive'] |
| 4 | missing all alternatives: ['R3', 'Melee'] |
| 4 | missing all alternatives: ['R3', 'Quick Melee'] |
| 4 | missing all alternatives: ['R3', 'Reset Camera'] |
| 4 | missing all alternatives: ['R3', 'Show Objective / Scan Environment'] |
| 4 | missing all alternatives: ['R3', 'รีเซ็ตมุมกล้อง'] |
| 4 | missing all alternatives: ['R3', 'โจมตีประชิด'] |
| 4 | missing all alternatives: ['R3', 'โจมตีระยะประชิด'] |
| 4 | missing all alternatives: ['R3', 'ไนตรัส / เร่งแซง'] |
| 4 | missing all alternatives: ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['RS (Right Stick) Left/Right', 'Change Leader'] |
| 4 | missing all alternatives: ['Right Mouse Button', 'Move / Attack target'] |
| 4 | missing all alternatives: ['Right Mouse Button', 'Secondary Fire'] |
| 4 | missing all alternatives: ['Right Mouse Button', 'เล็ง'] |
| 4 | missing all alternatives: ['Right PS VR2 Sense controller motion', 'Right-hand saber slash'] |
| 4 | missing all alternatives: ['Right Stick', 'Camera Movement'] |
| 4 | missing all alternatives: ['Ring-Con tilt', 'Move menu cursor'] |
| 4 | missing all alternatives: ['Shift + Q / W / E / R', 'Quick cast abilities'] |
| 4 | missing all alternatives: ['Shift', 'Sprint / Hold Breath'] |
| 4 | missing all alternatives: ['Simple controls', 'Run, leap, and stomp'] |
| 4 | missing all alternatives: ['Single Joy-Con / Joy-Con grip / Pro Controller', 'Supported controller styles'] |
| 4 | missing all alternatives: ['Space Bar', 'Jump'] |
| 4 | missing all alternatives: ['Space', 'Jump'] |
| 4 | missing all alternatives: ['Space', 'กระโดด'] |
| 4 | missing all alternatives: ['Spacebar', 'Center camera on champion'] |
| 4 | missing all alternatives: ['Spacebar', 'Jump'] |
| 4 | missing all alternatives: ['Spacebar', 'ล็อก/ดึงกล้องกลับมาตัวเอง'] |
| 4 | missing all alternatives: ['Square (สี่เหลี่ยม)', 'Dash'] |
| 4 | missing all alternatives: ['Square (สี่เหลี่ยม)', 'พุ่งตัว'] |
| 4 | missing all alternatives: ['Square', 'Attack'] |
| 4 | missing all alternatives: ['Square', 'Companion Attack'] |
| 4 | missing all alternatives: ['Square', 'Interact'] |
| 4 | missing all alternatives: ['Square', 'Interact/Reload'] |
| 4 | missing all alternatives: ['Square', 'Left Punch'] |
| 4 | missing all alternatives: ['Square', 'Lob Pass / Cross / Header'] |
| 4 | missing all alternatives: ['Square', 'Lofted Pass / Cross / Sliding Tackle'] |
| 4 | missing all alternatives: ['Square', 'Melee / Shoulder Swap (While aiming)'] |
| 4 | missing all alternatives: ['Square', 'Melee / Sword Attack'] |
| 4 | missing all alternatives: ['Square', 'Shuriken'] |
| 4 | missing all alternatives: ['Square', 'Sprint'] |
| 4 | missing all alternatives: ['Square', 'Use/Reload'] |
| 4 | missing all alternatives: ['Square', 'บรรจุกระสุน'] |
| 4 | missing all alternatives: ['Square', 'รีโหลด / บรรจุกระสุน'] |
| 4 | missing all alternatives: ['Square', 'รีโหลด'] |
| 4 | missing all alternatives: ['Square', 'ลดเกียร์'] |
| 4 | missing all alternatives: ['Square', 'ส่งโด่ง / เปิดบอล / สไลด์แท็กเกิล'] |
| 4 | missing all alternatives: ['Square', 'หั่น / ขว้าง'] |
| 4 | missing all alternatives: ['Square', 'โจมตี'] |
| 4 | missing all alternatives: ['Square', 'โจมตีประชิด / สลับฝั่งมุมกล้อง (ขณะเล็ง)'] |
| 4 | missing all alternatives: ['Square', 'โต้ตอบ'] |
| 4 | missing all alternatives: ['Square', 'ใช้ไอเทม'] |
| 4 | missing all alternatives: ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Tab / I', 'Inventory'] |
| 4 | missing all alternatives: ['Tab / I', 'เปิดกระเป๋า'] |
| 4 | missing all alternatives: ['Tab', 'ดู scoreboard'] |
| 4 | missing all alternatives: ['Touch Pad', 'Backpack'] |
| 4 | missing all alternatives: ['Touch Pad', 'Flash Hazards'] |
| 4 | missing all alternatives: ['Touch Pad', 'Inventory'] |
| 4 | missing all alternatives: ['Touch Pad', 'Journal'] |
| 4 | missing all alternatives: ['Touch Pad', 'Map (Press) / FNSM App (Swipe)'] |
| 4 | missing all alternatives: ['Touch Pad', 'Menu'] |
| 4 | missing all alternatives: ['Touch Pad', 'Scoreboard'] |
| 4 | missing all alternatives: ['Touch Pad', 'ตารางคะแนน / แผนที่'] |
| 4 | missing all alternatives: ['Touch Pad', 'เปิดสมุดบันทึก'] |
| 4 | missing all alternatives: ['Touch Pad', 'เมนู'] |
| 4 | missing all alternatives: ['Touch Pad', 'แผนที่ / แอป FNSM'] |
| 4 | missing all alternatives: ['Touch Pad', 'ไฟฉุกเฉิน'] |
| 4 | missing all alternatives: ['Triangle (สามเหลี่ยม)', 'Interact'] |
| 4 | missing all alternatives: ['Triangle (สามเหลี่ยม)', 'โต้ตอบ'] |
| 4 | missing all alternatives: ['Triangle', 'Call'] |
| 4 | missing all alternatives: ['Triangle', 'Magic Attack'] |
| 4 | missing all alternatives: ['Triangle', 'Ninjutsu'] |
| 4 | missing all alternatives: ['Triangle', 'Protego / Block (Hold)'] |
| 4 | missing all alternatives: ['Triangle', 'Ready Weapon'] |
| 4 | missing all alternatives: ['Triangle', 'Reload'] |
| 4 | missing all alternatives: ['Triangle', 'Return axe / Furious Immolation and Glacial Permafrost (While blocking)'] |
| 4 | missing all alternatives: ['Triangle', 'Reverse'] |
| 4 | missing all alternatives: ['Triangle', 'Right Punch'] |
| 4 | missing all alternatives: ['Triangle', 'Through Ball / Clear'] |
| 4 | missing all alternatives: ['Triangle', 'Through Pass'] |
| 4 | missing all alternatives: ['Triangle', 'Weapon'] |
| 4 | missing all alternatives: ['Triangle', 'Web Strike / Web Wings'] |
| 4 | missing all alternatives: ['Triangle', 'คลังไอเทม'] |
| 4 | missing all alternatives: ['Triangle', 'จ่ายทะลุช่อง / เคลียร์บอล'] |
| 4 | missing all alternatives: ['Triangle', 'ดึงตัวพุ่งโจมตี / ปีกใยแมงมุม'] |
| 4 | missing all alternatives: ['Triangle', 'ถอยหลัง'] |
| 4 | missing all alternatives: ['Triangle', 'ป้องกัน / บล็อกคาถา'] |
| 4 | missing all alternatives: ['Triangle', 'รีโหลด / บรรจุกระสุน'] |
| 4 | missing all alternatives: ['Triangle', 'อาวุธ'] |
| 4 | missing all alternatives: ['Triangle', 'เปิดกระเป๋าเก็บของ'] |
| 4 | missing all alternatives: ['Triangle', 'เรียก'] |
| 4 | missing all alternatives: ['Triangle', 'เรียกขวานกลับ / ชาร์จพลังอาวุธ'] |
| 4 | missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ / เก็บของ'] |
| 4 | missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ'] |
| 4 | missing all alternatives: ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['W / A / S / D', 'Move Character'] |
| 4 | missing all alternatives: ['X / Y', 'Jump'] |
| 4 | missing all alternatives: ['X / Y', 'Throw cap / Dash (Hold)'] |
| 4 | missing all alternatives: ['X / Y', 'กระโดด'] |
| 4 | missing all alternatives: ['X / Y', 'ขว้างหมวก / วิ่งเร็ว'] |
| 4 | missing all alternatives: ['X Button on sport-selection screen', 'Select Soccer Leg-Strap Mode in Play Globally'] |
| 4 | missing all alternatives: ['X', 'Dark Light'] |
| 4 | missing all alternatives: ['X', 'Hints'] |
| 4 | missing all alternatives: ['X', 'Inventory'] |
| 4 | missing all alternatives: ['X', 'Jump / Dodge (While locked)'] |
| 4 | missing all alternatives: ['X', 'Unequip weapon'] |
| 4 | missing all alternatives: ['X', 'กระเป๋าช่องเก็บของ'] |
| 4 | missing all alternatives: ['X', 'กระโดด / หลบหลีก'] |
| 4 | missing all alternatives: ['X', 'คำใบ้'] |
| 4 | missing all alternatives: ['X', 'บีบแตร'] |
| 4 | missing all alternatives: ['X', 'เก็บ/ถอดอาวุธ'] |
| 4 | missing all alternatives: ['X', 'ไฟดาร์กไลต์'] |
| 4 | missing all alternatives: ['Y / B', 'Throw / Slap'] |
| 4 | missing all alternatives: ['Y / B', 'ขว้าง / ตบ'] |
| 4 | missing all alternatives: ['Y / U', 'Chat'] |
| 4 | missing all alternatives: ['Y / U', 'แชท'] |
| 4 | missing all alternatives: ['Y', 'ยิงจุกยาง'] |
| 4 | missing all alternatives: ['Y', 'หยิบไอเทม'] |
| 4 | missing all alternatives: ['Y', 'เปิด/ปิดระบบช่วยขับ'] |
| 4 | missing all alternatives: ['Y', 'โจมตี'] |
| 4 | missing all alternatives: ['Z', 'Prone'] |
| 4 | missing all alternatives: ['ZL / ZR', 'Shield'] |
| 4 | missing all alternatives: ['ZL / ZR', 'โล่ป้องกัน'] |
| 4 | missing all alternatives: ['ZL', 'Blow'] |
| 4 | missing all alternatives: ['ZL', 'Crouch'] |
| 4 | missing all alternatives: ['ZL', 'Lock-On (Hold)'] |
| 4 | missing all alternatives: ['ZL', 'NookPhone'] |
| 4 | missing all alternatives: ['ZL', 'Use Item / Horn'] |
| 4 | missing all alternatives: ['ZL', 'ย่อตัว'] |
| 4 | missing all alternatives: ['ZL', 'ล็อกเป้าหมาย'] |
| 4 | missing all alternatives: ['ZL', 'สมาร์ทโฟน'] |
| 4 | missing all alternatives: ['ZL', 'ใช้ไอเทม / บีบแตร'] |
| 4 | missing all alternatives: ['ZR', 'Drift'] |
| 4 | missing all alternatives: ['ZR', 'Reactions'] |
| 4 | missing all alternatives: ['ZR', 'Suck'] |
| 4 | missing all alternatives: ['ZR', 'Use bow'] |
| 4 | missing all alternatives: ['ZR', 'ดริฟต์'] |
| 4 | missing all alternatives: ['ZR', 'ดูดลม / ดูดผี'] |
| 4 | missing all alternatives: ['ZR', 'แสดงอารมณ์'] |
| 4 | missing all alternatives: ['ZR', 'ใช้ธนู'] |
| 4 | missing_complete_clause:4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick |
| 4 | route:clarification expected:['general', 'overview', 'home', 'knowledge'] |
| 4 | route:clarification expected:['general', 'overview', 'home'] |
| 4 | route:clarification expected:['overview', 'members'] |
| 4 | route:clarification expected:['rules', 'overview', 'no_answer'] |
| 4 | route:equipment expected:['no_answer'] |
| 4 | route:general expected:['no_answer'] |
| 4 | route:knowledge expected:['games', 'general', 'clarification'] |
| 4 | route:knowledge expected:['schedule', 'clarification'] |
| 4 | validation errors: ['missing_requested_field:steps', 'missing_requested_field:players_max'] |
| 4 | wrong_outcome:clarification |
| 3 | intent:chatbot_identity expected:detail |
| 3 | intent:common_read expected:game_detail_lookup |
| 3 | intent:user_service_facts expected:detail |
| 3 | intent:user_service_facts expected:group_count |
| 3 | missing required: 150 บาท |
| 3 | missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด |
| 3 | missing_complete_clause:4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally. |
| 3 | missing_complete_clause:4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion. |
| 3 | missing_complete_clause:4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่ |
| 3 | missing_complete_clause:4.4.3. A 5-minute break follows every two games. |
| 3 | missing_complete_clause:4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game. |
| 3 | missing_complete_clause:Allowed keyboard technology: Snap Tap, SOCD, or equivalent technologies, unless otherwise instructed by officials. |
| 3 | missing_complete_clause:Any character can be selected (except DLC characters) |
| 3 | missing_complete_clause:Check-in: arrive at least 30 minutes before the scheduled match time. |
| 3 | missing_complete_clause:Communication: All participants must use the Discord server designated by the Center. |
| 3 | missing_complete_clause:Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception. |
| 3 | missing_complete_clause:Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match. |
| 3 | missing_complete_clause:General eligibility: Open only to students currently enrolled at Prince of Songkla University, Phuket Campus. |
| 3 | missing_complete_clause:If any member withdraws, the team may be disqualified. |
| 3 | missing_complete_clause:If tied at 1-1, a deciding game will be played |
| 3 | missing_complete_clause:In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over. |
| 3 | missing_complete_clause:In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice. |
| 3 | missing_complete_clause:Maximum of 24 rounds (12 rounds per side). The winner is the first team to win 13 rounds. |
| 3 | missing_complete_clause:Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes. |
| 3 | missing_complete_clause:One request per map is allowed. |
| 3 | missing_complete_clause:PlayStation 5 console used |
| 3 | missing_complete_clause:Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited. |
| 3 | missing_complete_clause:Players may compete under only one team. |
| 3 | missing_complete_clause:Referees may reconsider decisions as appropriate to ensure fairness. |
| 3 | missing_complete_clause:Registration of players is not permitted after the registration period has closed. |
| 3 | missing_complete_clause:Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket. |
| 3 | missing_complete_clause:Semifinals and finals: Best of 3 (BO3) |
| 3 | missing_complete_clause:Side selection: a knife round is used to choose sides. |
| 3 | missing_complete_clause:Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time. |
| 3 | missing_complete_clause:Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees. |
| 3 | missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited. |
| 3 | missing_complete_clause:Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute. |
| 3 | missing_complete_clause:Turn OFF Blood and Bodies displays. Displaying FPS or Latency graphs during competition is prohibited. |
| 3 | missing_complete_clause:Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception. |
| 3 | missing_complete_clause:Used when there are device malfunctions, disconnections, or software issues |
| 3 | missing_complete_clause:Using teammates to jump higher than the normal jump range is prohibited. |
| 3 | route:contact expected:['competition_rules'] |
| 3 | route:knowledge expected:['games', 'clarification'] |
| 3 | route:knowledge expected:['no_answer', 'games'] |
| 3 | route:no_answer expected:['multi_question'] |
| 3 | route:reservation expected:['competition_rules'] |
| 3 | validation errors: ['missing_requested_field:details', 'missing_requested_field:consequence'] |
| 3 | validation errors: ['unresolved_query_clause', 'missing_requested_field:details', 'missing_requested_field:specifications'] |
| 3 | wrong_outcome:answer |
| 2 | Nintendo Switch |
| 2 | Nintendo Switch Zone |
| 2 | PC Zone |
| 2 | PlayStation 5 Zone |
| 2 | VR Zone |
| 2 | intent:checkin_required expected:booking_policy |
| 2 | intent:equipment_item_lookup expected:list |
| 2 | intent:food_bring_permission expected:studio_rules |
| 2 | intent:game_list expected:list |
| 2 | legacy_mode_prefix:['pipeline:structured_game_detail'] |
| 2 | missing all alternatives: ['Animal Crossing', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['NARUTO X BORUTO Ultimate Ninja Storm Connections', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['New Super Mario Bros. U Deluxe', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['PUBG', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['PlayStation 5 / VR', 'Zone'] |
| 2 | missing all alternatives: ['The Legend of Zelda', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['Uncharted', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['นายภาสวุฒิ', 'นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer'] |
| 2 | missing all alternatives: ['เก็บอาวุธ เคลื่อนตามวง ต่อสู้กับผู้เล่นอื่น และใช้การสร้างหรือโหมดไม่สร้างตามรูปแบบที่เลือก'] |
| 2 | missing all alternatives: ['เล่นตามเนื้อเรื่อง ต่อสู้ด้วยสกิล/คอมโบ ทำภารกิจ และพัฒนาความสามารถของตัวละคร'] |
| 2 | missing required: Square |
| 2 | missing required: The Last of Us Part I / Part II |
| 2 | missing_complete_clause:1. การเลือกแผนที่ ใช้ MAPBAN.GG |
| 2 | missing_complete_clause:1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน |
| 2 | missing_complete_clause:1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น |
| 2 | missing_complete_clause:1. รูปแบบทัวร์นาเมนต์ Single Elimination |
| 2 | missing_complete_clause:1. โหมด Competitive (5v5) |
| 2 | missing_complete_clause:2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ |
| 2 | missing_complete_clause:2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง |
| 2 | missing_complete_clause:3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง |
| 2 | missing_complete_clause:3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น |
| 2 | missing_complete_clause:3. เงินเริ่มต้น $800  /  เวลาของระเบิด: 40 วินาที |
| 2 | missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ |
| 2 | missing_complete_clause:4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น |
| 2 | missing_complete_clause:4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที |
| 2 | missing_complete_clause:4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ |
| 2 | missing_complete_clause:4.2.5. Regarding skins, only Default skins may be used. |
| 2 | missing_complete_clause:5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง |
| 2 | missing_complete_clause:5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification. |
| 2 | missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ |
| 2 | missing_complete_clause:ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที |
| 2 | missing_complete_clause:จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน |
| 2 | missing_complete_clause:ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ) |
| 2 | missing_complete_clause:ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่ |
| 2 | missing_complete_clause:ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ |
| 2 | missing_complete_clause:ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์ |
| 2 | missing_complete_clause:ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ |
| 2 | missing_complete_clause:อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น |
| 2 | route:clarification expected:['general', 'overview', 'knowledge'] |
| 2 | route:clarification expected:['penalty', 'rules'] |
| 2 | route:competition_rules expected:['games'] |
| 2 | route:games expected:['general', 'knowledge'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview', 'knowledge'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview'] |
| 2 | route:knowledge expected:['clarification', 'multi_question'] |
| 2 | route:no_answer expected:['general', 'overview', 'knowledge'] |
| 2 | route:no_answer expected:['rules', 'penalty'] |
| 2 | route:reservation expected:['general', 'knowledge'] |
| 1 | 09:00-12:00 |
| 1 | 1-2 Persons |
| 1 | 13:00-16:00 |
| 1 | 3 หมวด |
| 1 | 3-4 Persons |
| 1 | Circle |
| 1 | Cockpit Zone |
| 1 | Cross |
| 1 | Gaming PC |
| 1 | Local LLM |
| 1 | Mario Kart |
| 1 | Members |
| 1 | NARUTO X BORUTO |
| 1 | PSU Phuket Esports Club |
| 1 | PlayStation 5 |
| 1 | Square |
| 1 | TEKKEN 8 |
| 1 | Triangle |
| 1 | VR |
| 1 | VR 1 ชั่วโมง |
| 1 | VR 30 นาที |
| 1 | cooperative education |
| 1 | intent:ambiguity_gate_clarification expected:game_control_lookup |
| 1 | intent:booking_policy expected:how_to |
| 1 | intent:chatbot_greeting expected:detail |
| 1 | intent:common_read expected:competition_game_list |
| 1 | intent:common_read expected:competition_rules_lookup |
| 1 | intent:common_read expected:count |
| 1 | intent:common_read expected:equipment_item_lookup |
| 1 | intent:common_read expected:penalty_policy |
| 1 | intent:competition_rules_lookup expected:competition_game_list |
| 1 | intent:conversation_price_lookup expected:multi_question_split |
| 1 | intent:freshness_live_source_required expected:detail |
| 1 | intent:keyboard_layout_mismatch expected:schedule_query |
| 1 | intent:price_missing_service expected:service_fee_query |
| 1 | intent:public_access expected:booking_policy |
| 1 | intent:user_service_facts expected:list |
| 1 | intent:zone_rental_fee expected:guard_no_answer |
| 1 | legacy_mode_prefix:['pipeline:deterministic_calculator_fast'] |
| 1 | legacy_mode_prefix:['pipeline:structured_booking_game_service_selection'] |
| 1 | legacy_mode_prefix:['pipeline:structured_service_fee_by_game'] |
| 1 | missing all alternatives: ['Beat Saber', 'Horizon Call of the Mountain', 'Resident Evil 4', '30'] |
| 1 | missing all alternatives: ['Call of Duty', 'หลายเกม', 'ยังไม่ชัด'] |
| 1 | missing all alternatives: ['Call of Duty: Warzone', 'Counter-Strike 2', 'League of Legends'] |
| 1 | missing all alternatives: ['ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา'] |
| 1 | missing required: 1 ชั่วโมง |
| 1 | missing required: 10 นาที |
| 1 | missing required: 13:00 |
| 1 | missing required: 16:00 |
| 1 | missing required: 70 บาท |
| 1 | missing required: 70 บาท/session |
| 1 | missing required: Gaming PC |
| 1 | missing required: Maintenance |
| 1 | missing required: Mario มีปุ่มอะไรบ้าง |
| 1 | missing required: National ID |
| 1 | missing required: PC #01-#02 |
| 1 | missing required: PC #03-#10 |
| 1 | missing required: PC 1 ชั่วโมง |
| 1 | missing required: PC Zone มีอุปกรณ์อะไร |
| 1 | missing required: PS5 มีเกมอะไร |
| 1 | missing required: PS5 มีเกมอะไรบ้าง |
| 1 | missing required: PS5 ราคาเท่าไหร่ |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท |
| 1 | missing required: TEKKEN 8 มีข้อมูลปุ่ม |
| 1 | missing required: TEKKEN 8 ไม่มีราคาแยกตามชื่อเกม |
| 1 | missing required: Tekken 8 มีปุ่มอะไร |
| 1 | missing required: Tekken 8 มีปุ่มอะไรบ้าง |
| 1 | missing required: Tekken 8 ราคาเท่าไหร่ |
| 1 | missing required: Tekken 8 เล่นที่ไหน |
| 1 | missing required: alcohol consumption |
| 1 | missing required: local service fee update 2026-07-27 |
| 1 | missing required: permission |
| 1 | missing required: power outlets |
| 1 | missing required: prohibited |
| 1 | missing required: returned after use |
| 1 | missing required: ขั้นตอนจอง |
| 1 | missing required: คำตอบ: |
| 1 | missing required: จองยังไง |
| 1 | missing required: จะเล่น Tekken 8 ต้องจองยังไง |
| 1 | missing required: ต่างกันดังนี้ |
| 1 | missing required: มีเกมอะไรบ้าง |
| 1 | missing required: วันจันทร์ |
| 1 | missing required: วิธีเล่นโดยสรุป |
| 1 | missing required: สมัครสมาชิก |
| 1 | missing required: ห้ามพูดจาดูหมิ่น |
| 1 | missing required: เกมต่อสู้ |
| 1 | missing required: โดยไม่จองล่วงหน้าไม่ได้ |
| 1 | missing required: ไม่พบข้อมูล |
| 1 | missing required: ไม่รับผิดชอบ |
| 1 | missing_complete_clause:1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket |
| 1 | missing_complete_clause:1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น |
| 1 | missing_complete_clause:1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา |
| 1 | missing_complete_clause:1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3) |
| 1 | missing_complete_clause:1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม |
| 1 | missing_complete_clause:2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง |
| 1 | missing_complete_clause:2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ |
| 1 | missing_complete_clause:2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด |
| 1 | missing_complete_clause:2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร |
| 1 | missing_complete_clause:3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที |
| 1 | missing_complete_clause:3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ |
| 1 | missing_complete_clause:3.1. Offline Mode |
| 1 | missing_complete_clause:3.1. แข่งแบบออฟไลน์ |
| 1 | missing_complete_clause:3.2. Each round played as Best of 3 (BO3) |
| 1 | missing_complete_clause:3.2. แข่ง Best of 3 (BO3) ทุกรอบ |
| 1 | missing_complete_clause:4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time |
| 1 | missing_complete_clause:4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ)  /  ผู้ชนะคือทีมที่ได้ 13 รอบก่อน |
| 1 | missing_complete_clause:4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น |
| 1 | missing_complete_clause:4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น |
| 1 | missing_complete_clause:4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ |
| 1 | missing_complete_clause:4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม |
| 1 | missing_complete_clause:4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร |
| 1 | missing_complete_clause:5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด |
| 1 | missing_complete_clause:5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที |
| 1 | missing_complete_clause:กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม |
| 1 | missing_complete_clause:การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ |
| 1 | missing_complete_clause:ขอได้ 1 ครั้งต่อแผนที่ |
| 1 | missing_complete_clause:ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น |
| 1 | missing_complete_clause:ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies) |
| 1 | missing_complete_clause:รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน |
| 1 | missing_complete_clause:สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC) |
| 1 | missing_complete_clause:หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที |
| 1 | missing_complete_clause:หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน |
| 1 | missing_complete_clause:ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน |
| 1 | missing_complete_clause:ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น |
| 1 | missing_complete_clause:เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น |
| 1 | missing_complete_clause:เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ |
| 1 | missing_complete_clause:เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง |
| 1 | missing_complete_clause:เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง |
| 1 | missing_complete_clause:ใช้เครื่องเกม PlayStation 5 |
| 1 | missing_complete_clause:ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์ |
| 1 | missing_complete_clause:ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด |
| 1 | outcome expected clarification_required, got no_answer |
| 1 | route expected ['competition_rules', 'clarification'], got no_answer |
| 1 | route:clarification expected:['games'] |
| 1 | route:clarification expected:['general', 'knowledge', 'no_answer'] |
| 1 | route:clarification expected:['overview'] |
| 1 | route:clarification expected:['service_fee'] |
| 1 | route:equipment expected:['games', 'clarification'] |
| 1 | route:games expected:['service_fee'] |
| 1 | route:input_guard expected:['equipment', 'no_answer'] |
| 1 | route:input_guard expected:['schedule'] |
| 1 | route:knowledge expected:['rules', 'penalty'] |
| 1 | route:no_answer expected:['general'] |
| 1 | silently_omitted_unknown_fee |
| 1 | ตาราง Service Fee |
| 1 | พื้นที่ที่กำหนด |
| 1 | ยังไม่ได้เปิด |
| 1 | วันจันทร์ |
| 1 | เร่ง |

## legacy_llm

| จำนวน | reasonตามraw |
|---:|---|
| 5894 | pipeline_exception |
| 2702 | route:game_controls expected:['games'] |
| 694 | status:no_answer expected:answer_available |
| 602 | status:clarification expected:answer_available |
| 400 | route:service_fee expected:['equipment', 'games', 'multi_question', 'reservation'] |
| 306 | route:schedule expected:['reservation'] |
| 222 | legacy_mode_prefix:['pipeline:structured_game_controls'] |
| 161 | status:answer expected:clarification_required |
| 151 | status:answer expected:no_answer_expected |
| 130 | status:no_answer expected:localization_pending |
| 102 | route:no_answer expected:['general', 'knowledge'] |
| 97 | legacy_mode_prefix:['pipeline:competition_fact_card'] |
| 96 | route:clarification expected:['service_fee'] |
| 95 | route:knowledge expected:['general', 'overview', 'home'] |
| 93 | route:contact expected:['competition_rules'] |
| 89 | retrieval evidence did not match the allowed canonical fact/rule IDs |
| 88 | status:clarification expected:no_answer_expected |
| 86 | route:service_fee expected:['multi_question', 'reservation', 'games', 'equipment'] |
| 74 | route:input_guard expected:['clarification', 'general', 'no_answer', 'unknown'] |
| 72 | missing required: 2 sessions |
| 72 | route:clarification expected:['reservation'] |
| 68 | route:clarification expected:['no_answer', 'overview', 'rules'] |
| 66 | missing all alternatives: ['latency', 'หน่วง'] |
| 62 | route:reservation expected:['members', 'overview'] |
| 61 | missing required: English localization |
| 60 | missing all alternatives: ['เฟรม', 'ความละเอียด'] |
| 59 | missing all alternatives: ['server', 'client'] |
| 58 | intent:conversation_price_lookup expected:service_fee_query |
| 57 | missing all alternatives: ['GPU', 'กราฟิก'] |
| 57 | missing all alternatives: ['คีย์บอร์ด', 'mechanical'] |
| 56 | route expected ['competition_rules'], got contact |
| 55 | missing all alternatives: ['กิจกรรม'] |
| 54 | missing all alternatives: ['API', 'เชื่อมต่อ'] |
| 54 | missing all alternatives: ['ขอบคุณ'] |
| 54 | status:answer expected:live_lookup_required |
| 51 | route:reservation expected:['overview'] |
| 49 | route:service_fee expected:['multi_question'] |
| 47 | missing all alternatives: ['จอง'] |
| 44 | missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026'] |
| 44 | route:clarification expected:['games'] |
| 43 | route:clarification expected:['competition_rules'] |
| 43 | route:clarification expected:['members', 'overview'] |
| 41 | missing required: psuesportspkt@gmail.com |
| 38 | missing rulebook target(s): ['competition_rules_valorant_psu_phuket_2026'] |
| 35 | missing required: Verified game catalog |
| 33 | latency_ceiling |
| 32 | first_line_off_topic |
| 31 | status:no_answer expected:clarification_required |
| 30 | status:clarification expected:localization_pending |
| 28 | route:no_answer expected:['penalty', 'rules'] |
| 27 | missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา'] |
| 25 | route:no_answer expected:['overview'] |
| 23 | legacy_english_thai_prose_flag |
| 23 | route:games expected:['competition_rules'] |
| 22 | missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible'] |
| 22 | route:general expected:['reservation'] |
| 21 | route:clarification expected:['games', 'reservation'] |
| 20 | route:clarification expected:['reservation', 'schedule'] |
| 20 | route:contact expected:['rules', 'no_answer', 'clarification'] |
| 19 | route:knowledge expected:['general', 'clarification', 'no_answer', 'overview'] |
| 18 | missing all alternatives: ['ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน'] |
| 18 | missing all alternatives: ['เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง'] |
| 18 | missing required: not connected |
| 18 | route:clarification expected:['games', 'service_fee'] |
| 18 | route:clarification expected:['no_answer'] |
| 18 | route:reservation expected:['competition_rules'] |
| 18 | route:schedule expected:['no_answer'] |
| 17 | route:game_controls expected:['games', 'no_answer'] |
| 16 | legacy_mode_prefix:['pipeline:multi_question_splitter'] |
| 16 | route:clarification expected:['general', 'knowledge'] |
| 16 | route:input_guard expected:['general', 'unknown', 'clarification', 'no_answer'] |
| 16 | route:schedule expected:['competition_rules'] |
| 16 | route_mismatch |
| 16 | wrong_game_evidence |
| 15 | route:general expected:['no_answer'] |
| 15 | route:no_answer expected:['reservation'] |
| 15 | route:service_fee expected:['no_answer'] |
| 14 | missing all alternatives: ['ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม'] |
| 14 | route:games expected:['clarification', 'equipment'] |
| 14 | route:games expected:['no_answer'] |
| 14 | route:general expected:['penalty'] |
| 12 | missing all alternatives: ['Gaming PC รุ่น MSI MAG Infinite S3 14th'] |
| 12 | missing all alternatives: ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก'] |
| 12 | route expected ['competition_rules'], got clarification |
| 12 | route:clarification expected:['contact'] |
| 12 | wrong_category |
| 12 | wrong_game_source |
| 11 | intent:game_list expected:list |
| 11 | missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'หันมองจุดสนใจ'] |
| 11 | missing all alternatives: ['PlayStation 5', 'PlayStation 5 #01-#02'] |
| 11 | route:no_answer expected:['competition_rules'] |
| 10 | missing all alternatives: ['PC #03-#10', 'PC', 'Call of Duty'] |
| 10 | missing required: Gran Turismo 7 |
| 10 | missing required: Nintendo Switch Sports |
| 10 | route:contact expected:['penalty', 'rules'] |
| 10 | route:general expected:['rules'] |
| 10 | route:knowledge expected:['overview'] |
| 10 | route:no_answer expected:['general', 'knowledge', 'overview'] |
| 10 | route:service_fee expected:['penalty', 'rules'] |
| 9 | intent:control_lookup expected:game_control_lookup |
| 9 | legacy_mode_prefix:['pipeline:structured_game_controls_no_current_game', 'pipeline:no_answer'] |
| 9 | quality_score_or_required_gate_failed |
| 9 | route:clarification expected:['general', 'knowledge', 'overview'] |
| 9 | route:clarification expected:['multi_question'] |
| 9 | route:clarification expected:['no_answer', 'service_fee'] |
| 9 | route:equipment expected:['rules'] |
| 9 | route:schedule expected:['clarification', 'equipment'] |
| 8 | intent:user_service_facts expected:how_to |
| 8 | legacy_mode_prefix:['pipeline:structured_game_controls_no_data', 'pipeline:no_answer', 'pipeline:answer_contract_no_answer'] |
| 8 | missing all alternatives: ['TV 65 นิ้ว'] |
| 8 | missing all alternatives: ['TV 86 นิ้ว'] |
| 8 | missing all alternatives: ['The Last of Us Part II (Remastered)', 'PlayStation / PS5'] |
| 8 | missing required: Resident Evil 4 (Remake) |
| 8 | outcome expected no_answer_expected, got answer |
| 8 | route expected ['competition_rules', 'no_answer'], got contact |
| 8 | route:clarification expected:['overview'] |
| 8 | route:contact expected:['competition_rules', 'no_answer'] |
| 8 | route:reservation expected:['no_answer'] |
| 8 | source-gap no-answer attached evidence or did not abstain safely |
| 7 | missing all alternatives: ['RS (Right Stick) Left/Right', 'เปลี่ยนตัวละครหลัก'] |
| 7 | route:no_answer expected:['games'] |
| 7 | route:schedule expected:['games'] |
| 6 | missing all alternatives: ['L (Left Stick)', 'Move'] |
| 6 | missing all alternatives: ['L3 (Click Left Stick)', 'Look at'] |
| 6 | missing all alternatives: ['Touch Pad', 'สัมภาระ / เมนูกระเป๋าเก็บของ'] |
| 6 | missing all alternatives: ['Y', 'Assist'] |
| 6 | missing required: ปุ่ม |
| 6 | route expected ['competition_rules'], got schedule |
| 6 | route:clarification expected:['games', 'no_answer'] |
| 6 | route:games expected:['equipment'] |
| 6 | route:games expected:['reservation', 'schedule'] |
| 6 | route:rules expected:['no_answer'] |
| 5 | intent:booking_how_to expected:booking_policy |
| 5 | missing all alternatives: ['R (Right Stick)', 'มุมกล้อง'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ไฟฉาย'] |
| 5 | missing all alternatives: ['TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง'] |
| 5 | route:clarification expected:['general', 'overview', 'home', 'knowledge'] |
| 5 | route:clarification expected:['general', 'overview', 'home'] |
| 5 | route:competition_rules expected:['games'] |
| 5 | route:game_controls expected:['games', 'multi_question'] |
| 5 | route:no_answer expected:['rules'] |
| 4 | intent:game_detail_lookup expected:game_availability_lookup |
| 4 | missing all alternatives: ['Circle', 'Crouch'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบคลาน'] |
| 4 | missing all alternatives: ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Cross (กากบาท)', 'Jump'] |
| 4 | missing all alternatives: ['Cross', 'Jump'] |
| 4 | missing all alternatives: ['Cross', 'กระโดด'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Tool selection (Up / Down / Left / Right)'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอุปกรณ์ด่วน'] |
| 4 | missing all alternatives: ['D-Pad', 'License'] |
| 4 | missing all alternatives: ['D-Pad', 'ดูใบขับขี่และสถิติ'] |
| 4 | missing all alternatives: ['God of War Ragnarök', 'PlayStation / PS5'] |
| 4 | missing all alternatives: ['L1', 'Dodge'] |
| 4 | missing all alternatives: ['L1', 'หลบหลีก'] |
| 4 | missing all alternatives: ['L2', 'Aim (Hold)'] |
| 4 | missing all alternatives: ['L2', 'เล็งเป้า (กดค้าง)'] |
| 4 | missing all alternatives: ['Left Stick', 'Steer'] |
| 4 | missing all alternatives: ['Left Stick', 'เลี้ยว'] |
| 4 | missing all alternatives: ['Options', 'Pause'] |
| 4 | missing all alternatives: ['Options', 'หยุดเกม'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'Camera'] |
| 4 | missing all alternatives: ['R1', 'Listen mode (Hold) / Switch Weapon'] |
| 4 | missing all alternatives: ['R1', 'โหมดฟังเสียง (กดค้าง) / สลับอาวุธด่วน'] |
| 4 | missing all alternatives: ['R2', 'Shoot (While aiming) / Reload'] |
| 4 | missing all alternatives: ['R2', 'ยิงปืน (ขณะเล็ง) / รีโหลดกระสุน'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Flashlight'] |
| 4 | missing all alternatives: ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Square', 'Melee'] |
| 4 | missing all alternatives: ['Square', 'โจมตีประชิด'] |
| 4 | missing all alternatives: ['Super Smash Bros. Ultimate', 'Nintendo Switch'] |
| 4 | missing all alternatives: ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Touch Pad', 'Inventory'] |
| 4 | missing all alternatives: ['Triangle', 'Interact'] |
| 4 | missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ'] |
| 4 | outcome_mismatch |
| 4 | route:clarification expected:['rules', 'overview', 'no_answer'] |
| 4 | route:equipment expected:['no_answer'] |
| 4 | route:knowledge expected:['games'] |
| 4 | route:penalty expected:['rules'] |
| 4 | route:service_fee expected:['games'] |
| 3 | intent:ambiguity_gate_clarification expected:game_control_lookup |
| 3 | intent:chatbot_identity expected:detail |
| 3 | intent:user_service_facts expected:detail |
| 3 | intent:user_service_facts expected:group_count |
| 3 | missing required: PlayStation 5 Zone |
| 3 | missing_complete_clause:No team member changes are allowed during the competition period |
| 3 | route:clarification expected:['no_answer', 'games'] |
| 3 | route:clarification expected:['overview', 'members'] |
| 3 | route:games expected:['service_fee'] |
| 3 | route:no_answer expected:['members', 'overview'] |
| 3 | route:no_answer expected:['multi_question'] |
| 3 | status:clarification expected:live_lookup_required |
| 3 | wrong_outcome:answer |
| 2 | harness_timeout_30s |
| 2 | intent:checkin_required expected:booking_policy |
| 2 | intent:equipment_item_lookup expected:list |
| 2 | intent:food_bring_permission expected:studio_rules |
| 2 | intent:studio_rule_direct expected:studio_rules |
| 2 | legacy_mode_prefix:['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'] |
| 2 | missing all alternatives: ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 2 | missing all alternatives: ['Call of Duty', 'ปุ่ม', 'จอย', 'คอนโทรล'] |
| 2 | missing all alternatives: ['Nintendo Switch', 'Zone'] |
| 2 | missing all alternatives: ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 2 | missing required: 150 บาท |
| 2 | missing required: PC Zone |
| 2 | missing required: Phuket Campus |
| 2 | missing required: TEKKEN 8 |
| 2 | missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ |
| 2 | missing_complete_clause:5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง |
| 2 | missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ |
| 2 | missing_complete_clause:Abilities must not be used outside map boundaries to obtain information or an advantage. |
| 2 | missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping. |
| 2 | missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification. |
| 2 | missing_complete_clause:If a forfeit is imposed, the result for that map is recorded as 13-0. |
| 2 | missing_complete_clause:Map selection uses MAPBAN.GG |
| 2 | missing_complete_clause:New agents may not be used for approximately 2 weeks after release in Competitive mode. |
| 2 | missing_complete_clause:New maps may not be used for approximately 4 weeks after release in Competitive mode. |
| 2 | missing_complete_clause:Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid. |
| 2 | route:clarification expected:['contact', 'overview'] |
| 2 | route:clarification expected:['general', 'overview', 'knowledge'] |
| 2 | route:clarification expected:['penalty', 'rules'] |
| 2 | route:clarification expected:['service_fee', 'games'] |
| 2 | route:games expected:['equipment', 'clarification'] |
| 2 | route:games expected:['general', 'knowledge'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview', 'knowledge'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview'] |
| 2 | route:no_answer expected:['equipment', 'games'] |
| 2 | route:no_answer expected:['games', 'reservation'] |
| 2 | route:no_answer expected:['general', 'overview', 'knowledge'] |
| 2 | route:no_answer expected:['reservation', 'schedule'] |
| 2 | route:no_answer expected:['rules', 'penalty'] |
| 2 | route:reservation expected:['general', 'knowledge'] |
| 1 | 1-2 Persons |
| 1 | 3 หมวด |
| 1 | 3-4 Persons |
| 1 | Local LLM |
| 1 | Members |
| 1 | NARUTO X BORUTO |
| 1 | PSU Phuket Esports Club |
| 1 | VR 1 ชั่วโมง |
| 1 | VR 30 นาที |
| 1 | cooperative education |
| 1 | intent:alcohol_rule expected:studio_rules |
| 1 | intent:ambiguity_gate_clarification expected:detail |
| 1 | intent:ambiguity_gate_clarification expected:list |
| 1 | intent:booking_policy expected:how_to |
| 1 | intent:chatbot_greeting expected:detail |
| 1 | intent:competition_rulebook_catalog expected:competition_game_list |
| 1 | intent:competition_rules_lookup expected:competition_game_list |
| 1 | intent:conversation_price_lookup expected:multi_question_split |
| 1 | intent:count expected:booking_policy |
| 1 | intent:damage_responsibility expected:penalty_policy |
| 1 | intent:freshness_live_source_required expected:detail |
| 1 | intent:how_to expected:game_detail_lookup |
| 1 | intent:keyboard_layout_mismatch expected:schedule_query |
| 1 | intent:price_missing_service expected:multi_question_split |
| 1 | intent:price_missing_service expected:service_fee_query |
| 1 | intent:public_access expected:booking_policy |
| 1 | intent:user_service_facts expected:list |
| 1 | intent:zone_rental_fee expected:guard_no_answer |
| 1 | legacy_mode_prefix:['pipeline:deterministic_calculator_fast'] |
| 1 | legacy_mode_prefix:['pipeline:structured_booking_game_service_selection'] |
| 1 | legacy_mode_prefix:['pipeline:structured_game_detail'] |
| 1 | missing all alternatives: ['The Legend of Zelda', 'ปุ่ม', 'controller', 'จอย'] |
| 1 | missing all alternatives: ['The Legend of Zelda', 'วิธีเล่น', 'เล่น'] |
| 1 | missing required: 1 ชั่วโมง |
| 1 | missing required: 70 บาท/session |
| 1 | missing required: National ID |
| 1 | missing required: Overcooked 2 |
| 1 | missing required: PC #01-#02 |
| 1 | missing required: PC #03-#10 |
| 1 | missing required: PC 1 ชั่วโมง |
| 1 | missing required: PS5 มีเกมอะไร |
| 1 | missing required: PS5 ราคาเท่าไหร่ |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท |
| 1 | missing required: Tekken 8 ราคาเท่าไหร่ |
| 1 | missing required: local service fee update 2026-07-27 |
| 1 | missing required: ขั้นตอนจอง |
| 1 | missing required: จะเล่น Tekken 8 ต้องจองยังไง |
| 1 | missing required: ต่างกันดังนี้ |
| 1 | missing required: สมัครสมาชิก |
| 1 | missing required: โดยไม่จองล่วงหน้าไม่ได้ |
| 1 | missing required: ไม่พบข้อมูล |
| 1 | missing_complete_clause:1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN |
| 1 | missing_complete_clause:1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม |
| 1 | missing_complete_clause:2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด |
| 1 | missing_complete_clause:3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ |
| 1 | missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด |
| 1 | missing_complete_clause:3. เงินเริ่มต้น $800  /  เวลาของระเบิด: 40 วินาที |
| 1 | missing_complete_clause:If a bug occurs before either side deals damage, officials may roll back the round. |
| 1 | missing_complete_clause:If any member withdraws, the team may be disqualified. |
| 1 | missing_complete_clause:If damage has already been dealt, no rollback is allowed unless through the Challenge process. |
| 1 | missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited. |
| 1 | missing_complete_clause:Watching streams: Players are prohibited from watching live streams during competition. |
| 1 | missing_complete_clause:หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที |
| 1 | missing_complete_clause:อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ |
| 1 | missing_complete_clause:เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ |
| 1 | missing_complete_clause:ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด |
| 1 | outcome expected clarification_required, got no_answer |
| 1 | route expected ['competition_rules', 'clarification'], got no_answer |
| 1 | route:clarification expected:['equipment'] |
| 1 | route:clarification expected:['general', 'knowledge', 'no_answer'] |
| 1 | route:equipment expected:['games', 'clarification'] |
| 1 | route:equipment expected:['general', 'knowledge', 'no_answer'] |
| 1 | route:game_controls expected:['games', 'clarification', 'no_answer'] |
| 1 | route:general expected:['contact'] |
| 1 | route:input_guard expected:['equipment', 'no_answer'] |
| 1 | route:input_guard expected:['schedule'] |
| 1 | route:no_answer expected:['general'] |
| 1 | route:reservation expected:['games', 'general', 'no_answer'] |
| 1 | route:schedule expected:['equipment', 'clarification'] |
| 1 | ตาราง Service Fee |
| 1 | พื้นที่ที่กำหนด |
| 1 | ยังไม่ได้เปิด |
| 1 | เร่ง |

## common_llm

| จำนวน | reasonตามraw |
|---:|---|
| 15007 | route:knowledge expected:['games'] |
| 3718 | validation_rejected |
| 3287 | route:knowledge expected:['competition_rules'] |
| 2915 | status:clarification expected:answer_available |
| 2605 | route:knowledge expected:['reservation'] |
| 2599 | route:knowledge expected:['equipment'] |
| 2425 | route:knowledge expected:['reservation', 'schedule'] |
| 1828 | route expected ['competition_rules'], got knowledge |
| 1683 | retrieval evidence did not match the allowed canonical fact/rule IDs |
| 1456 | route:knowledge expected:['rules'] |
| 1370 | pipeline_exception |
| 1326 | route:knowledge expected:['service_fee'] |
| 1014 | route:knowledge expected:['members', 'overview'] |
| 960 | status:clarification expected:live_lookup_required |
| 944 | route:knowledge expected:['games', 'reservation'] |
| 822 | missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026'] |
| 790 | route:knowledge expected:['penalty'] |
| 768 | status:answer expected:no_answer_expected |
| 641 | missing rulebook target(s): ['competition_rules_valorant_psu_phuket_2026'] |
| 620 | first_line_off_topic |
| 587 | route:knowledge expected:['schedule'] |
| 538 | missing rulebook target(s): ['competition_rules_tekken8_psu_esports'] |
| 532 | status:answer expected:clarification_required |
| 463 | status:answer expected:live_lookup_required |
| 458 | missing all alternatives: ['Nintendo Switch Zone'] |
| 450 | legacy_english_thai_prose_flag |
| 426 | route:knowledge expected:['competition_rules', 'no_answer'] |
| 384 | route_mismatch |
| 368 | route:knowledge expected:['games', 'reservation', 'schedule'] |
| 345 | status:no_answer expected:answer_available |
| 328 | legacy_mode_prefix:['pipeline:structured_game_controls'] |
| 327 | route expected ['competition_rules', 'no_answer'], got knowledge |
| 315 | route:knowledge expected:['multi_question'] |
| 310 | outcome expected no_answer_expected, got answer |
| 275 | route:knowledge expected:['equipment', 'games', 'multi_question', 'reservation'] |
| 256 | wrong_category |
| 227 | route:knowledge expected:['schedule', 'reservation'] |
| 190 | route:knowledge expected:['equipment', 'games'] |
| 187 | legacy_mode_prefix:['pipeline:competition_fact_card'] |
| 185 | wrong_game_evidence |
| 182 | route:knowledge expected:['overview'] |
| 170 | missing required: Verified equipment |
| 166 | missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่'] |
| 163 | route:knowledge expected:['contact'] |
| 162 | route:knowledge expected:['penalty', 'rules'] |
| 156 | status:clarification expected:no_answer_expected |
| 153 | route:service_fee expected:['equipment', 'games', 'multi_question', 'reservation'] |
| 136 | route:knowledge expected:['rules', 'no_answer', 'clarification'] |
| 135 | status:clarification expected:localization_pending |
| 134 | route:schedule expected:['reservation'] |
| 133 | route:knowledge expected:['no_answer', 'overview', 'rules'] |
| 130 | route:knowledge expected:['clarification', 'schedule'] |
| 130 | route:knowledge expected:['overview', 'rules'] |
| 128 | missing all alternatives: ['บาท', 'บาท', 'ฟรี'] |
| 128 | route:knowledge expected:['clarification', 'service_fee'] |
| 126 | route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee'] |
| 120 | outcome_mismatch |
| 120 | route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification'] |
| 119 | missing required: Wednesday |
| 115 | missing all alternatives: ['Nintendo Switch', 'Nintendo Switch (1-2 Persons)'] |
| 108 | validation errors: ['missing_requested_field:details'] |
| 108 | validation errors: ['unresolved_query_clause'] |
| 102 | status:no_answer expected:localization_pending |
| 101 | route:knowledge expected:['reservation', 'service_fee'] |
| 96 | route:knowledge expected:['clarification', 'equipment'] |
| 96 | route:knowledge expected:['general', 'overview', 'home'] |
| 95 | route:knowledge expected:['games', 'no_answer'] |
| 94 | missing all alternatives: ['R (Right Stick)', 'มุมกล้อง'] |
| 91 | missing required: Nintendo Switch |
| 91 | route:knowledge expected:['contact', 'overview'] |
| 89 | missing all alternatives: ['Gaming Monitor', 'Gaming Monitors'] |
| 88 | missing rulebook target(s): ['competition_rules_rov_blueket_2025_men'] |
| 80 | missing all alternatives: ['VR Zone'] |
| 80 | missing required: PC Zone |
| 80 | route:no_answer expected:['general', 'knowledge'] |
| 78 | missing required: VR Zone |
| 76 | missing all alternatives: ['Cockpit Zone'] |
| 75 | missing all alternatives: ['PC Zone'] |
| 75 | missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone'] |
| 75 | route:knowledge expected:['no_answer'] |
| 74 | outcome expected answer_available, got clarification |
| 74 | route:input_guard expected:['clarification', 'general', 'no_answer', 'unknown'] |
| 74 | route:knowledge expected:['games', 'multi_question'] |
| 72 | missing required: 2 sessions |
| 70 | source-gap no-answer attached evidence or did not abstain safely |
| 69 | wrong_game_source |
| 68 | route:knowledge expected:['equipment', 'rules'] |
| 66 | missing all alternatives: ['L (Left Stick)', 'Move'] |
| 66 | missing all alternatives: ['latency', 'หน่วง'] |
| 66 | missing required: PlayStation 5 |
| 64 | route:clarification expected:['no_answer', 'overview', 'rules'] |
| 62 | route:knowledge expected:['games', 'service_fee'] |
| 61 | missing required: 09:00-12:00 |
| 61 | missing required: English localization |
| 60 | missing all alternatives: ['Options', 'Pause'] |
| 60 | missing all alternatives: ['เฟรม', 'ความละเอียด'] |
| 60 | route:knowledge expected:['multi_question', 'reservation', 'games', 'equipment'] |
| 59 | missing all alternatives: ['server', 'client'] |
| 58 | missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible'] |
| 57 | missing all alternatives: ['GPU', 'กราฟิก'] |
| 56 | missing all alternatives: ['คีย์บอร์ด', 'mechanical'] |
| 55 | missing all alternatives: ['กิจกรรม'] |
| 54 | missing all alternatives: ['API', 'เชื่อมต่อ'] |
| 54 | missing all alternatives: ['ขอบคุณ'] |
| 50 | missing all alternatives: ['R (Right Stick)', 'Camera'] |
| 48 | legacy_mode_prefix:['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'] |
| 48 | missing required: 3 sessions |
| 47 | legacy_mode_prefix:['pipeline:multi_question_splitter'] |
| 47 | missing required: Phuket Campus |
| 46 | route:reservation expected:['overview'] |
| 45 | intent:common_read expected:schedule_query |
| 45 | latency_ceiling |
| 45 | missing required: upload the payment slip |
| 44 | intent:common_read expected:list |
| 44 | intent:conversation_price_lookup expected:service_fee_query |
| 44 | missing all alternatives: ['Options', 'หยุดเกม'] |
| 44 | missing required: refund |
| 44 | route:knowledge expected:['schedule', 'reservation', 'clarification'] |
| 44 | route:reservation expected:['members', 'overview'] |
| 43 | missing all alternatives: ['ไม่มี', 'PC #01-#02'] |
| 43 | missing required: 795-276244-1 |
| 43 | missing required: Siam Commercial Bank |
| 43 | route:knowledge expected:['clarification', 'competition_rules', 'general'] |
| 43 | validation errors: ['missing_requested_field:steps'] |
| 42 | missing all alternatives: ['จอง'] |
| 42 | missing all alternatives: ['พื้นที่ที่กำหนด', 'designated area'] |
| 42 | missing required: not open 24 hours |
| 41 | missing all alternatives: ['ไม่มี', 'PC #03-#10'] |
| 40 | route:knowledge expected:['general', 'clarification', 'no_answer', 'overview'] |
| 38 | missing required: Key studio rules |
| 36 | intent:common_read expected:booking_policy |
| 36 | missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา'] |
| 36 | route:knowledge expected:['clarification', 'games'] |
| 35 | missing all alternatives: ['W / A / S / D', 'เคลื่อนที่'] |
| 35 | missing required: 13:00-16:00 |
| 35 | missing required: 70 THB |
| 35 | missing required: Verified game catalog |
| 35 | missing required: psuesportspkt@gmail.com |
| 34 | missing all alternatives: ['09:00', '13:00', '9:00', '1 pm'] |
| 34 | missing required: Call of Duty |
| 34 | validation errors: ['missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence', 'missing_requested_field:details', 'missing_requested_field:procedure_id'] |
| 33 | missing all alternatives: ['L3', 'วิ่งสปรินต์'] |
| 33 | route:service_fee expected:['multi_question', 'reservation', 'games', 'equipment'] |
| 32 | missing required: maintenance |
| 32 | validation errors: ['missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence', 'missing_requested_field:details'] |
| 31 | route:knowledge expected:['clarification', 'games', 'no_answer'] |
| 30 | missing required: 1 hour |
| 29 | missing required: There are currently 42 verified games available. |
| 28 | missing all alternatives: ['+ (Plus)', 'Pause'] |
| 28 | route:clarification expected:['reservation'] |
| 27 | harness_timeout_30s |
| 27 | missing required: Gran Turismo 7 |
| 26 | missing all alternatives: ['Left Shift', 'เดินช้า'] |
| 26 | missing all alternatives: ['Left Stick', 'เคลื่อนที่'] |
| 25 | missing all alternatives: ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก'] |
| 25 | missing required: 30 minutes |
| 24 | missing all alternatives: ['Touch Pad', 'แผนที่'] |
| 24 | missing required: Minecraft |
| 24 | missing required: select a service |
| 24 | status:answer expected:safe_no_answer |
| 23 | route:no_answer expected:['penalty', 'rules'] |
| 22 | missing all alternatives: ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 22 | missing all alternatives: ['L3 (Click Left Stick)', 'หันมองจุดสนใจ'] |
| 22 | missing all alternatives: ['PlayStation 5 Zone'] |
| 22 | missing all alternatives: ['The Last of Us Part I / Part II'] |
| 22 | missing all alternatives: ['นายพฤทธิ์ เกษตรสมบูรณ์', 'นักวิชาการคอมพิวเตอร์'] |
| 22 | missing required: No information |
| 21 | missing all alternatives: ['+ (Plus)', 'หยุดเกม'] |
| 21 | missing required: Booking steps |
| 21 | route:knowledge expected:['clarification', 'equipment', 'games', 'no_answer', 'reservation', 'service_fee'] |
| 21 | status:answer expected:safe_clarification |
| 20 | missing all alternatives: ['Cross', 'Jump'] |
| 20 | missing all alternatives: ['Cross', 'กระโดด'] |
| 20 | missing all alternatives: ['Overcooked! 2', 'ยังไม่พบข้อมูลปุ่ม', 'ไม่มีข้อมูลปุ่ม'] |
| 20 | missing all alternatives: ['Touch Pad', 'Map'] |
| 20 | missing all alternatives: ['นายนพัทธ์ ฝอยทอง', 'รองประธาน'] |
| 20 | missing all alternatives: ['เล็ง ยิง เคลื่อนที่ ใช้อุปกรณ์ และทำ objective ของโหมดเกมหรือภารกิจให้สำเร็จ'] |
| 20 | missing all alternatives: ['เล่นแบบสบาย ๆ โดยเก็บทรัพยากร ตกปลา จับแมลง ตกแต่งเกาะ และทำกิจกรรมประจำวัน'] |
| 20 | missing required: 2026-09-25 |
| 20 | missing required: Animal Crossing |
| 20 | missing required: Monster Hunter Rise |
| 20 | missing required: Resident Evil Village |
| 20 | missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026', 'competition_rules_valorant_psu_phuket_2026'] |
| 20 | quality_score_or_required_gate_failed |
| 20 | route:service_fee expected:['multi_question'] |
| 20 | status:no_answer expected:clarification_required |
| 19 | route:clarification expected:['members', 'overview'] |
| 19 | validation errors: ['missing_requested_field:competition_id'] |
| 18 | intent:common_read expected:service_fee_query |
| 18 | missing all alternatives: ['Call of Duty: Modern Warfare III คือเกมยิงมุมมองบุคคลที่หนึ่งที่เน้นภารกิจและการยิงต่อสู้แบบรวดเร็ว'] |
| 18 | missing all alternatives: ['Nintendo Switch', 'เล่นได้ที่'] |
| 18 | missing all alternatives: ['VALORANT', 'Counter-Strike 2'] |
| 18 | missing required: Counter-Strike 2 |
| 18 | missing required: Fortnite |
| 18 | missing required: Luigi's Mansion 3 |
| 18 | missing required: Marvel's Spider-Man 2 |
| 18 | missing required: PUBG |
| 18 | missing required: The Last of Us Part I |
| 18 | missing required: Uncharted |
| 18 | missing required: not connected |
| 18 | route:knowledge expected:['games', 'general', 'no_answer'] |
| 18 | route:schedule expected:['no_answer'] |
| 17 | missing all alternatives: ['Pokémon Champions', 'Animal Crossing: New Horizons', 'It Takes Two', '60'] |
| 17 | missing required: Mario Party Superstars |
| 17 | missing required: VALORANT |
| 17 | outcome expected no_answer_expected, got clarification |
| 17 | route:knowledge expected:['games', 'clarification', 'no_answer'] |
| 17 | validation errors: ['missing_requested_field:consequence'] |
| 17 | validation errors: ['missing_requested_field:details', 'missing_requested_field:conditions_all'] |
| 16 | missing all alternatives: ['Animal Crossing: New Horizons คือเกมใช้ชีวิตบนเกาะ ผู้เล่นตกแต่งบ้าน เก็บของ สร้างพื้นที่ และพูดคุยกับชาวเกาะ'] |
| 16 | missing all alternatives: ['L2 (Hold)', 'Aim'] |
| 16 | missing all alternatives: ['New Super Mario Bros. U Deluxe คือเกมมาริโอแบบเดินลุยด่าน กระโดด หลบศัตรู และเก็บเหรียญ'] |
| 16 | missing all alternatives: ['Nintendo Switch Zone', 'อุปกรณ์'] |
| 16 | missing all alternatives: ['PUBG: BATTLEGROUNDS คือเกมเอาชีวิตรอดที่ผู้เล่นลงสนาม ค้นหาอาวุธและอุปกรณ์ แล้วพยายามอยู่รอดเป็นคนหรือทีมสุดท้าย'] |
| 16 | missing all alternatives: ['VR Zone', 'อุปกรณ์'] |
| 16 | missing all alternatives: ['เลือกจุดลง หาอาวุธ เข้าโซนปลอดภัย วางตำแหน่ง และต่อสู้กับทีมอื่นจนเหลือผู้ชนะท้ายเกม'] |
| 16 | missing required: Beat Saber |
| 16 | missing required: EA Sports FC 24 |
| 16 | missing required: FINAL FANTASY XVI |
| 16 | missing required: Hogwarts Legacy |
| 16 | missing required: Horizon Call of the Mountain |
| 16 | missing required: It Takes Two |
| 16 | missing required: League of Legends |
| 16 | missing required: Mario Kart 8 Deluxe |
| 16 | missing required: Nintendo Switch Sports |
| 16 | route:input_guard expected:['general', 'unknown', 'clarification', 'no_answer'] |
| 15 | missing all alternatives: ['Beat Saber', 'Horizon Call of the Mountain', 'Resident Evil 4'] |
| 15 | missing all alternatives: ['Call of Duty: Modern Warfare III', 'Delta Force', 'EA Sports FC 24', '60'] |
| 15 | missing all alternatives: ['L3', 'เกาะคอน / พุ่งหลาว'] |
| 15 | route:knowledge expected:['equipment', 'clarification'] |
| 15 | route:knowledge expected:['equipment', 'no_answer'] |
| 15 | route:no_answer expected:['overview'] |
| 15 | route:service_fee expected:['no_answer'] |
| 14 | intent:common_read expected:game_control_lookup |
| 14 | intent:common_read expected:studio_rules |
| 14 | legacy_mode_prefix:['pipeline:structured_game_controls_no_current_game', 'pipeline:no_answer'] |
| 14 | missing all alternatives: ['Button controls', 'เล่นบอร์ดและมินิเกมด้วยปุ่ม'] |
| 14 | missing all alternatives: ['Cross', 'Interact'] |
| 14 | missing all alternatives: ['Gran Turismo 7', '60'] |
| 14 | missing all alternatives: ['Left Stick', 'Move'] |
| 14 | missing all alternatives: ['NARUTO X BORUTO Ultimate Ninja Storm Connections คือเกมต่อสู้ที่ใช้ตัวละครจากจักรวาล Naruto/Boruto'] |
| 14 | missing all alternatives: ['PlayStation 5 Zone / VR Zone'] |
| 14 | missing all alternatives: ['The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ'] |
| 14 | missing all alternatives: ['ลงพื้นที่ หาอาวุธ ใช้ loadout/อุปกรณ์ช่วยทีม เคลื่อนตามวง และพยายามอยู่รอดจนจบเกม'] |
| 14 | missing all alternatives: ['เลือกตัวละคร ใช้คอมโบ สกิลนินจา และจังหวะหลบ/สวนกลับเพื่อเอาชนะคู่ต่อสู้'] |
| 14 | missing rulebook target(s): ['competition_rules_rov_blueket_2025_men', 'competition_rules_tekken8_psu_esports'] |
| 14 | route:clarification expected:['reservation', 'schedule'] |
| 14 | route:knowledge expected:['clarification', 'games', 'general'] |
| 14 | validation errors: ['unresolved_query_clause', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence', 'missing_requested_field:details'] |
| 13 | missing all alternatives: ['Call of Duty: Warzone', 'Counter-Strike 2', 'League of Legends', '60'] |
| 13 | missing all alternatives: ['Joy-Con (R) Control Stick', 'เลื่อนเคอร์เซอร์'] |
| 13 | missing all alternatives: ['Joy-Con motion', 'เล่นท่ากีฬาด้วยการขยับ Joy-Con'] |
| 13 | missing all alternatives: ['L (Left Stick)', 'เลี้ยว / ควบคุมทิศทาง'] |
| 13 | missing all alternatives: ['L3 (Click Left Stick)', 'วิ่งสปรินต์'] |
| 13 | missing all alternatives: ['RS (Right Stick) Left/Right', 'เปลี่ยนตัวละครหลัก'] |
| 13 | missing all alternatives: ['Simple controls', 'วิ่ง กระโดด และเหยียบศัตรู'] |
| 13 | missing all alternatives: ['Single Joy-Con / Joy-Con grip / Pro Controller', 'รูปแบบคอนโทรลเลอร์ที่รองรับ'] |
| 13 | missing all alternatives: ['TEKKEN 8', 'Counter-Strike 2', 'League of Legends', '60'] |
| 13 | missing all alternatives: ['รศ.ดร.พันธ์ ทองชุมนุม', 'รองอธิการบดี'] |
| 13 | missing required: Overcooked 2 |
| 13 | missing_complete_clause:Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid. |
| 13 | route:clarification expected:['general', 'knowledge'] |
| 13 | route:no_answer expected:['reservation'] |
| 13 | validation errors: ['missing_requested_field:decision'] |
| 13 | validation errors: ['unresolved_query_clause', 'missing_requested_field:details'] |
| 12 | missing all alternatives: ['Call of Duty: Warzone คือเกมยิงแนว Battle Royale ที่เน้นการยิงรวดเร็ว การเก็บอุปกรณ์ และการเอาตัวรอดในแผนที่ขนาดใหญ่'] |
| 12 | missing all alternatives: ['Circle', 'Crouch'] |
| 12 | missing all alternatives: ['L3', 'Sprint'] |
| 12 | missing all alternatives: ['Left Mouse Button', 'ยิง'] |
| 12 | missing all alternatives: ['Mr. Amine Abidellaoui', 'Internship Student'] |
| 12 | missing all alternatives: ['R', 'รีโหลด'] |
| 12 | missing all alternatives: ['Square', 'Reload'] |
| 12 | missing all alternatives: ['The Last of Us คือเกมผจญภัยเอาตัวรอดที่เน้นเนื้อเรื่อง การลอบเร้น และการจัดการทรัพยากร'] |
| 12 | missing all alternatives: ['Uncharted คือเกมผจญภัยแนวล่าสมบัติที่เน้นปีนป่าย สำรวจ แก้ปริศนา และฉากแอ็กชัน'] |
| 12 | missing all alternatives: ['ยังไม่แน่ใจ', 'ยังไม่พบ', 'ขอ', 'ไม่มี'] |
| 12 | missing all alternatives: ['วิ่ง กระโดด ใช้ power-up ผ่านด่าน และร่วมมือกับเพื่อนได้หลายคน'] |
| 12 | missing all alternatives: ['สำรวจ ฉวยโอกาสลอบเร้น ต่อสู้ เก็บทรัพยากร และดำเนินเรื่องผ่านภารกิจต่าง ๆ'] |
| 12 | missing all alternatives: ['สำรวจฉาก ปีนป่าย แก้ปริศนา ยิงต่อสู้ และดำเนินเรื่องผ่านภารกิจ'] |
| 12 | missing all alternatives: ['สำรวจแผนที่ เก็บอาวุธ/อาหาร แก้ shrine ต่อสู้ และเลือกเส้นทางการผจญภัยเองได้มาก'] |
| 12 | missing all alternatives: ['หมายถึง', 'พิมพ์', 'ยังไม่', 'เกม', 'อุปกรณ์', 'ราคา', 'จอง'] |
| 12 | missing all alternatives: ['แนวเกม', 'เกม Action-Adventure'] |
| 12 | missing all alternatives: ['แนวเกม', 'เกม Battle Royale'] |
| 12 | missing all alternatives: ['แนวเกม', 'เกมยิง Battle Royale'] |
| 12 | missing all alternatives: ['ไม่ได้', 'ไม่พบ', 'closed', 'weekend', 'not open'] |
| 12 | missing required: 0 บาท |
| 12 | missing required: Resident Evil 4 |
| 12 | validation errors: ['missing_requested_field:details', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence'] |
| 12 | validation errors: ['missing_requested_field:players_max'] |
| 12 | validation errors: ['missing_requested_field:players_min', 'missing_requested_field:players_max'] |
| 11 | missing all alternatives: ['Analogue control scheme', 'เคลื่อนที่ด้วยอนาล็อก'] |
| 11 | missing all alternatives: ['Controller Mapping page', 'เปลี่ยน preset จอย'] |
| 11 | missing all alternatives: ['Cross', 'ส่งบอลเลียด / โหม่ง'] |
| 11 | missing all alternatives: ['Gesture control scheme', 'เคลื่อนที่ด้วยท่าทางร่างกาย'] |
| 11 | missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่ / เดินสไลด์ข้าง'] |
| 11 | missing all alternatives: ['L (Left Stick)', 'เลี้ยว / ควบคุมพวงมาลัย'] |
| 11 | missing all alternatives: ['L / ZL / R / ZR', 'จับ / ยก'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'มาร์กตำแหน่งศัตรู'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'ย่อตัว'] |
| 11 | missing all alternatives: ['L3 (Click Left Stick)', 'วิ่งเร็ว / สปรินต์'] |
| 11 | missing all alternatives: ['LS (Left Stick)', 'เคลื่อนที่'] |
| 11 | missing all alternatives: ['Left PS VR2 Sense controller motion', 'ฟันบล็อกด้วยดาบมือซ้าย'] |
| 11 | missing all alternatives: ['One Joy-Con', 'ควบคุมตัวละครด้วย Joy-Con เดี่ยว'] |
| 11 | missing all alternatives: ['Options', 'เปิดเมนูเกม'] |
| 11 | missing all alternatives: ['PlayStation 5', 'PlayStation 5 #01-#02'] |
| 11 | missing all alternatives: ['Pokémon Champions', 'Animal Crossing: New Horizons', 'It Takes Two'] |
| 11 | missing all alternatives: ['Q / W / E / R', 'ใช้สกิล'] |
| 11 | missing all alternatives: ['R (Right Stick)', 'หันหน้า / เล็ง'] |
| 11 | missing all alternatives: ['R (Right Stick)', 'โจมตีสแมช'] |
| 11 | missing all alternatives: ['Right Mouse Button', 'เดิน / โจมตีเป้าหมาย'] |
| 11 | missing all alternatives: ['Right PS VR2 Sense controller motion', 'ฟันบล็อกด้วยดาบมือขวา'] |
| 11 | missing all alternatives: ['Right Stick', 'ควบคุมมุมกล้อง'] |
| 11 | missing all alternatives: ['Square', 'ส่งบอลโด่ง / เปิดบอล / โหม่ง'] |
| 11 | missing all alternatives: ['Square', 'หมัดซ้าย / ต่อยซ้าย'] |
| 11 | missing all alternatives: ['Triangle', 'หมัดขวา / ต่อยขวา'] |
| 11 | missing all alternatives: ['X Button on sport-selection screen', 'เลือกโหมดสายรัดขาใน Soccer ตอน Play Globally'] |
| 11 | missing all alternatives: ['X Button', 'ยืนยันการเลือก'] |
| 11 | missing required: designated areas |
| 11 | outcome expected clarification_required, got answer |
| 11 | route expected ['competition_rules', 'clarification'], got knowledge |
| 10 | intent:common_read expected:detail |
| 10 | intent:common_read expected:how_to |
| 10 | missing all alternatives: ['- (Minus)', 'Map'] |
| 10 | missing all alternatives: ['- (Minus)', 'แผนที่'] |
| 10 | missing all alternatives: ['13:00', 'maintenance', 'Maintenance'] |
| 10 | missing all alternatives: ['Call of Duty: Modern Warfare III', 'Delta Force', 'EA Sports FC 24'] |
| 10 | missing all alternatives: ['Circle', 'Dodge'] |
| 10 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบ / สไลด์'] |
| 10 | missing all alternatives: ['Cross', 'กระโดด / ปีนป่าย'] |
| 10 | missing all alternatives: ['L1', 'กระโดด / ปีนป่าย'] |
| 10 | missing all alternatives: ['L3 (Click Left Stick)', 'Look at'] |
| 10 | missing all alternatives: ['L3', 'Animal Instinct'] |
| 10 | missing all alternatives: ['Left Ctrl', 'ย่อตัว'] |
| 10 | missing all alternatives: ['M', 'เปิดแผนที่'] |
| 10 | missing all alternatives: ['Options', 'หยุดเกมชั่วคราว'] |
| 10 | missing all alternatives: ['R1', 'Use Lethal Equipment'] |
| 10 | missing all alternatives: ['R3 (Click Right Stick)', 'ไฟฉาย'] |
| 10 | missing all alternatives: ['R3', 'เปลี่ยนท่า / สไลด์ / พุ่งหลบ'] |
| 10 | missing all alternatives: ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 10 | missing all alternatives: ['TEKKEN 8', 'Counter-Strike 2', 'League of Legends'] |
| 10 | missing all alternatives: ['VR', 'VR Station 30 นาที'] |
| 10 | missing all alternatives: ['W / A / S / D', 'Move'] |
| 10 | missing all alternatives: ['นายธนชาติ', 'ประชาสัมพันธ์'] |
| 10 | missing all alternatives: ['นายนพัทธ์', 'รองประธาน'] |
| 10 | missing all alternatives: ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Life Simulation'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Open-world Adventure'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกม Platformer 2D'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมต่อสู้จากอนิเมะ'] |
| 10 | missing all alternatives: ['แนวเกม', 'เกมยิง FPS'] |
| 10 | missing required: 2026-09-30 |
| 10 | missing required: 2026-10-01 |
| 10 | missing required: God of War Ragnarok |
| 10 | missing required: NARUTO X BORUTO Ultimate Ninja Storm Connections |
| 10 | missing required: Super Smash Bros Ultimate |
| 10 | missing required: TEKKEN 8 |
| 10 | missing required: THB |
| 10 | missing_complete_clause:Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset. |
| 10 | missing_complete_clause:Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only. |
| 10 | route:clarification expected:['no_answer'] |
| 10 | route:knowledge expected:['clarification', 'reservation'] |
| 10 | route:knowledge expected:['games', 'clarification'] |
| 10 | route:no_answer expected:['general', 'knowledge', 'overview'] |
| 10 | wrong_outcome:answer |
| 9 | intent:common_read expected:chatbot_identity |
| 9 | missing all alternatives: ['B', 'ยกเลิก'] |
| 9 | missing all alternatives: ['B', 'เบรก / ถอยหลัง'] |
| 9 | missing all alternatives: ['L2 (Hold)', 'เล็ง'] |
| 9 | missing all alternatives: ['R3', 'ล็อกเป้าหมาย'] |
| 9 | missing all alternatives: ['TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง'] |
| 9 | missing_complete_clause:No scripts or macros are allowed at all. |
| 9 | route:clarification expected:['general', 'knowledge', 'overview'] |
| 9 | route:clarification expected:['no_answer', 'service_fee'] |
| 9 | route:knowledge expected:['clarification', 'general', 'reservation'] |
| 9 | route:knowledge expected:['competition_rules', 'general', 'clarification'] |
| 9 | validation errors: ['missing_requested_field:details', 'missing_requested_field:steps'] |
| 8 | intent:common_read expected:game_availability_lookup |
| 8 | legacy_mode_prefix:['pipeline:structured_game_controls_no_data', 'pipeline:no_answer', 'pipeline:answer_contract_no_answer'] |
| 8 | missing all alternatives: ['1 / 2 / 3', 'เลือกอาวุธ'] |
| 8 | missing all alternatives: ['Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง'] |
| 8 | missing all alternatives: ['Cockpit', 'Zone'] |
| 8 | missing all alternatives: ['Cross', 'โต้ตอบ'] |
| 8 | missing all alternatives: ['D-Pad Down', 'Heal'] |
| 8 | missing all alternatives: ['D-Pad Down', 'ฟื้นฟูเลือด'] |
| 8 | missing all alternatives: ['Delta Force', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['L (Left Stick) / R (Right Stick)', 'เคลื่อนที่'] |
| 8 | missing all alternatives: ['L (Left Stick)', 'Steer'] |
| 8 | missing all alternatives: ['L2', 'Aim (Hold)'] |
| 8 | missing all alternatives: ['L2', 'Aim Down Sight'] |
| 8 | missing all alternatives: ['L2', 'เล็งเป้า (กดค้าง)'] |
| 8 | missing all alternatives: ['L3 (Click Left Stick)', 'Sprint'] |
| 8 | missing all alternatives: ['L3', 'วิ่ง / กลั้นหายใจ'] |
| 8 | missing all alternatives: ['Left Mouse Button', 'Fire'] |
| 8 | missing all alternatives: ['Left Shift', 'Walk'] |
| 8 | missing all alternatives: ['Options', 'เมนูหลัก'] |
| 8 | missing all alternatives: ['PC Zone', 'PlayStation 5 Zone'] |
| 8 | missing all alternatives: ['Pokémon Champions', 'Nintendo Switch'] |
| 8 | missing all alternatives: ['R1', 'ใช้อุปกรณ์ทำลายล้าง'] |
| 8 | missing all alternatives: ['R2', 'Fire Weapon'] |
| 8 | missing all alternatives: ['R3 (Click Right Stick)', 'Flashlight'] |
| 8 | missing all alternatives: ['R3', 'Lock-On'] |
| 8 | missing all alternatives: ['Right Mouse Button', 'ยิง/เล็งแบบรอง'] |
| 8 | missing all alternatives: ['Square', 'Melee'] |
| 8 | missing all alternatives: ['Square', 'โจมตีประชิด'] |
| 8 | missing all alternatives: ['Square', 'โต้ตอบ / รีโหลด'] |
| 8 | missing all alternatives: ['THE FINALS', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['Tab', 'Scoreboard'] |
| 8 | missing all alternatives: ['Tab', 'ดูตารางคะแนน'] |
| 8 | missing all alternatives: ['The Last of Us Part II (Remastered)', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['Triangle', 'Emote'] |
| 8 | missing all alternatives: ['Triangle', 'Interact'] |
| 8 | missing all alternatives: ['Triangle', 'Inventory'] |
| 8 | missing all alternatives: ['Triangle', 'Switch Weapon'] |
| 8 | missing all alternatives: ['Triangle', 'สลับอาวุธ'] |
| 8 | missing all alternatives: ['Triangle', 'แสดงอารมณ์'] |
| 8 | missing all alternatives: ['eFootball', 'PlayStation / PS5'] |
| 8 | missing all alternatives: ['ผศ.ดร.ณัฐพงศ์ ทองเทพ', 'ผู้ช่วยอธิการบดีฝ่ายวิชาการ'] |
| 8 | missing required: 0 THB |
| 8 | missing required: Little Nightmares II |
| 8 | missing required: PlayStation 5 Zone |
| 8 | missing required: Resident Evil 4 (Remake) |
| 8 | route:general expected:['reservation'] |
| 8 | route:knowledge expected:['service_fee', 'games'] |
| 7 | missing all alternatives: ['Cross', 'กระโดด / ขว้าง / โจมตี'] |
| 7 | missing all alternatives: ['Cross', 'ลูกเตะซ้าย'] |
| 7 | missing all alternatives: ['Gaming Mouse', 'Gaming Mouse'] |
| 7 | missing all alternatives: ['Mario Kart Live: Home Circuit', 'รายการเกมปัจจุบัน', 'ยังไม่พบ'] |
| 7 | missing all alternatives: ['R2', 'คันเร่ง'] |
| 7 | missing all alternatives: ['R3 (Click Right Stick)', 'มุมมองบุคคลที่หนึ่ง'] |
| 7 | missing all alternatives: ['R3 (Click Right Stick)', 'ล็อกเป้าหมาย'] |
| 7 | missing_complete_clause:5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers. |
| 7 | missing_complete_clause:Assist buttons or special assist systems are allowed |
| 7 | missing_complete_clause:If a bug occurs before either side deals damage, officials may roll back the round. |
| 7 | missing_complete_clause:If a forfeit is imposed, the result for that map is recorded as 13-0. |
| 7 | missing_complete_clause:If damage has already been dealt, no rollback is allowed unless through the Challenge process. |
| 7 | missing_complete_clause:New agents may not be used for approximately 2 weeks after release in Competitive mode. |
| 7 | missing_complete_clause:New maps may not be used for approximately 4 weeks after release in Competitive mode. |
| 7 | missing_complete_clause:No team member changes are allowed during the competition period |
| 7 | missing_complete_clause:Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must hand them to the referees before every match. |
| 7 | missing_complete_clause:Round time: 1:55 minutes  /  Freeze time: 15 seconds |
| 7 | missing_complete_clause:Rounds per game (Round): 3 |
| 7 | missing_complete_clause:The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs. |
| 7 | missing_complete_clause:Time per round (Timer): 60 seconds |
| 7 | route:knowledge expected:['no_answer', 'games', 'general'] |
| 7 | route:knowledge expected:['rules', 'penalty'] |
| 7 | route:no_answer expected:['competition_rules'] |
| 7 | validation errors: ['missing_requested_field:details', 'missing_requested_field:players_max'] |
| 7 | validation errors: ['unresolved_query_clause', 'missing_requested_field:competition_id'] |
| 7 | wrong_outcome |
| 6 | intent:common_read expected:equipment_item_lookup |
| 6 | missing all alternatives: ['1 / 2 / 3 / 4 / 5', 'Select weapon slots'] |
| 6 | missing all alternatives: ['4', 'Equip/Use Spike'] |
| 6 | missing all alternatives: ['4', 'หยิบ/ใช้ Spike'] |
| 6 | missing all alternatives: ['A / B', 'Jump'] |
| 6 | missing all alternatives: ['Analogue control scheme', 'Move using sticks'] |
| 6 | missing all alternatives: ['B', 'เก็บอาวุธ / วิ่งเร็ว'] |
| 6 | missing all alternatives: ['Circle (วงกลม)', 'Cancel'] |
| 6 | missing all alternatives: ['Circle', 'Crouch / Slide'] |
| 6 | missing all alternatives: ['Circle', 'Eikonic Feat'] |
| 6 | missing all alternatives: ['Circle', 'Hand Brake'] |
| 6 | missing all alternatives: ['Circle', 'โต้ตอบ'] |
| 6 | missing all alternatives: ['Circle', 'ไฟฉาย / รีโมท'] |
| 6 | missing all alternatives: ['Cross / Square / L1 / R1', 'หยิบ / วาง'] |
| 6 | missing all alternatives: ['Cross', 'Ground Pass / Header'] |
| 6 | missing all alternatives: ['Ctrl', 'Walk'] |
| 6 | missing all alternatives: ['D / F', 'ใช้ Summoner Spell'] |
| 6 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Weapon Cross (Up / Down / Left / Right)'] |
| 6 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'ติดตั้งอาวุธด่วน'] |
| 6 | missing all alternatives: ['D-Pad Left / Right', 'สลับเครื่องมือ'] |
| 6 | missing all alternatives: ['D-Pad Left', 'ติดตั้งอาวุธรอง'] |
| 6 | missing all alternatives: ['D-Pad Right', 'Spell Menu'] |
| 6 | missing all alternatives: ['D-Pad Up / Down', 'แถบแอคชั่น: เลือก/ใช้งาน'] |
| 6 | missing all alternatives: ['D-Pad Up', 'Swap Arrow Type'] |
| 6 | missing all alternatives: ['D-Pad Up', 'เปลี่ยนชนิดลูกธนู'] |
| 6 | missing all alternatives: ['D-Pad', 'Use Battle Item (Ninja Tools)'] |
| 6 | missing all alternatives: ['D-Pad', 'ควบคุมจอ MFD'] |
| 6 | missing all alternatives: ['D-Pad', 'ใช้อุปกรณ์นินจา'] |
| 6 | missing all alternatives: ['F1 / F2 / F3 / F4 / F5', 'Camera to allies'] |
| 6 | missing all alternatives: ['G', 'ทิ้งอาวุธ'] |
| 6 | missing all alternatives: ['Gaming Mouse'] |
| 6 | missing all alternatives: ['Gran Turismo 7'] |
| 6 | missing all alternatives: ['L1', 'ยกการ์ด / ป้องกัน'] |
| 6 | missing all alternatives: ['L1', 'ใช้อุปกรณ์ยุทธวิธี'] |
| 6 | missing all alternatives: ['L2 (Hold)', 'เล็ง (กดค้าง)'] |
| 6 | missing all alternatives: ['L2', 'บังบอล'] |
| 6 | missing all alternatives: ['L2', 'เล็งเป้า / เบรกรถ'] |
| 6 | missing all alternatives: ['L3 (Click Left Stick)', 'Crouch'] |
| 6 | missing all alternatives: ['L3 + R3', 'Spartan rage'] |
| 6 | missing all alternatives: ['L3', 'Headlights'] |
| 6 | missing all alternatives: ['LS (Left Stick)', 'Move'] |
| 6 | missing all alternatives: ['Options', 'Open game menu'] |
| 6 | missing all alternatives: ['Q / E / C / X', 'Use abilities'] |
| 6 | missing all alternatives: ['R', 'ขว้าง'] |
| 6 | missing all alternatives: ['R', 'แชทพิมพ์ข้อความ'] |
| 6 | missing all alternatives: ['R1 (While in Heat)', 'ฮีทสแมช'] |
| 6 | missing all alternatives: ['R1 + Circle', 'ยิงปั่นโค้ง'] |
| 6 | missing all alternatives: ['R1 / R2', 'Grab'] |
| 6 | missing all alternatives: ['R1', 'Change View'] |
| 6 | missing all alternatives: ['R1', 'Web-Shooter / Gadget (Hold)'] |
| 6 | missing all alternatives: ['R1', 'สลับอาวุธด่วน / โหมดฟังเสียง (กดค้าง)'] |
| 6 | missing all alternatives: ['R1', 'เปิดใช้งาน Heat'] |
| 6 | missing all alternatives: ['R2 (Hold)', 'Swing / Parkour'] |
| 6 | missing all alternatives: ['R2', 'Accelerate'] |
| 6 | missing all alternatives: ['R2', 'Attack'] |
| 6 | missing all alternatives: ['R2', 'Heavy Attack / Heavy Runic Attack (While blocking)'] |
| 6 | missing all alternatives: ['R2', 'ป้องกัน'] |
| 6 | missing all alternatives: ['R2', 'ยิงหลัก'] |
| 6 | missing all alternatives: ['R3 (Click Right Stick)', '1st Person view'] |
| 6 | missing all alternatives: ['R3 (Click Right Stick)', 'Crouch'] |
| 6 | missing all alternatives: ['R3 (Click Right Stick)', 'Zoom (with scope)'] |
| 6 | missing all alternatives: ['R3', 'Nitro / Overtake'] |
| 6 | missing all alternatives: ['Right Mouse Button', 'Alternate Fire'] |
| 6 | missing all alternatives: ['Right Mouse Button', 'Soft Aim / ADS'] |
| 6 | missing all alternatives: ['Shift', 'วิ่ง / กลั้นหายใจ'] |
| 6 | missing all alternatives: ['Square', 'Chop / Throw'] |
| 6 | missing all alternatives: ['Square', 'Shift Down'] |
| 6 | missing all alternatives: ['Square', 'Use Item'] |
| 6 | missing all alternatives: ['Square', 'คู่หูโจมตี'] |
| 6 | missing all alternatives: ['Square', 'ดาวกระจาย'] |
| 6 | missing all alternatives: ['Tab', 'Show Scoreboard'] |
| 6 | missing all alternatives: ['Touch Pad', 'กระเป๋าเป้ / เมนูคราฟต์ของ'] |
| 6 | missing all alternatives: ['Touch Pad', 'สัมภาระ / เมนูกระเป๋าเก็บของ'] |
| 6 | missing all alternatives: ['Triangle', 'ชักอาวุธ'] |
| 6 | missing all alternatives: ['X Button', 'Confirm selection'] |
| 6 | missing all alternatives: ['X', 'Horn'] |
| 6 | missing all alternatives: ['Y', 'สลับล็อกกล้อง'] |
| 6 | missing all alternatives: ['ZL', 'เป่าลม'] |
| 6 | missing all alternatives: ['นายณภัทร เชื้อเหล่าวานิช', 'นักศึกษาสหกิจ Game and 3D Developer'] |
| 6 | missing required: God of War Ragnarök |
| 6 | missing required: Moving Out 2 |
| 6 | missing required: NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS |
| 6 | missing required: New Super Mario Bros. U Deluxe |
| 6 | missing required: Ring Fit Adventure |
| 6 | missing required: Super Mario Odyssey |
| 6 | missing required: Super Smash Bros. Ultimate |
| 6 | missing required: The Last of Us Part II |
| 6 | missing required: The Legend of Zelda |
| 6 | missing_complete_clause:1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN |
| 6 | missing_complete_clause:2 requests per map during regulation (first 24 rounds), 60 seconds each. |
| 6 | missing_complete_clause:2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น |
| 6 | missing_complete_clause:4. Do not install your own software on the provided computers. |
| 6 | missing_complete_clause:4. Only drinking water in sealed containers and chewing gum are permitted. |
| 6 | missing_complete_clause:Abilities must not be used outside map boundaries to obtain information or an advantage. |
| 6 | missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping. |
| 6 | missing_complete_clause:Competitive mode (5v5) |
| 6 | missing_complete_clause:During preparation phase, the number of personnel shall not exceed 6 players. |
| 6 | missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification. |
| 6 | missing_complete_clause:Food and drinks: Only drinking water in sealed containers and chewing gum are permitted. |
| 6 | missing_complete_clause:Initial money: $800  /  Bomb time: 40 seconds |
| 6 | missing_complete_clause:Judgment authority: The referees' decisions and the organizers' rulings are final. The organizing side reserves the right to amend rules as appropriate for fairness. |
| 6 | missing_complete_clause:Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified. |
| 6 | missing_complete_clause:Macros (both software- and hardware-based) are strictly prohibited. |
| 6 | missing_complete_clause:Map selection uses MAPBAN.GG |
| 6 | missing_complete_clause:Match schedule: The tournament bracket will be announced at least 1 day in advance. Entry must be confirmed before the match starts. Late arrivals may be disqualified. |
| 6 | missing_complete_clause:No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.) |
| 6 | missing_complete_clause:No use of bugs or glitches that provide an advantage |
| 6 | missing_complete_clause:Overtime: 3 rounds per side (6 rounds total). The first team to win 4 of the 6 rounds wins. Starting money is $10,000, and overtime may be played without limit. |
| 6 | missing_complete_clause:Personnel: During Match Prep, no more than 6 players may be present. |
| 6 | missing_complete_clause:Players are responsible for the quality and readiness of their own equipment. |
| 6 | missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor. |
| 6 | missing_complete_clause:Tournament format: Single Elimination |
| 6 | missing_complete_clause:Watching streams: Players are prohibited from watching live streams during competition. |
| 6 | route:contact expected:['penalty', 'rules'] |
| 6 | route:contact expected:['rules', 'no_answer', 'clarification'] |
| 6 | route:games expected:['no_answer'] |
| 6 | route:games expected:['reservation', 'schedule'] |
| 6 | route:knowledge expected:['clarification', 'competition_rules'] |
| 6 | route:knowledge expected:['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'] |
| 6 | route:service_fee expected:['penalty', 'rules'] |
| 6 | validation errors: ['missing_requested_field:consequence', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:details'] |
| 6 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:steps', 'missing_requested_field:required_documents', 'missing_requested_field:deadline_minutes', 'missing_requested_field:outcome'] |
| 5 | intent:common_read expected:multi_question_split |
| 5 | missing all alternatives: ['+ Button on controller-holding screen', 'เลือกโหมดสายรัดขาใน Soccer ตอนเล่น Local/Friends'] |
| 5 | missing all alternatives: ['A / B', 'กระโดด'] |
| 5 | missing all alternatives: ['A Button', 'ยกเลิกการเลือก'] |
| 5 | missing all alternatives: ['Alt + Q / W / E / R', 'ใช้สกิลใส่ตัวเอง'] |
| 5 | missing all alternatives: ['B', 'โจมตีพิเศษ'] |
| 5 | missing all alternatives: ['Builder Pro / Combat Pro / Custom', 'ชุดปุ่มควบคุม'] |
| 5 | missing all alternatives: ['Call of Duty', 'PlayStation 5 #01-#02', 'PlayStation 5'] |
| 5 | missing all alternatives: ['Call of Duty', 'หลายเกม', 'ยังไม่ชัด'] |
| 5 | missing all alternatives: ['Circle / D-Pad Right', 'พุ่งตัว'] |
| 5 | missing all alternatives: ['Circle', 'ยิงประตู / วอลเลย์ / โหม่ง'] |
| 5 | missing all alternatives: ['Circle', 'ลูกเตะขวา'] |
| 5 | missing all alternatives: ['Circle', 'โจมตีระยะประชิด'] |
| 5 | missing all alternatives: ['Cross', 'เพิ่มเกียร์'] |
| 5 | missing all alternatives: ['D-Pad', 'แสดงอารมณ์'] |
| 5 | missing all alternatives: ['Head/body movement', 'หลบและจัดตำแหน่งร่างกาย'] |
| 5 | missing all alternatives: ['L1', 'รีเซ็ตมุมกล้อง / เมนูลัด (กดค้าง)'] |
| 5 | missing all alternatives: ['L2 / R2', 'หั่น / ขว้าง'] |
| 5 | missing all alternatives: ['L2', 'เบรก'] |
| 5 | missing all alternatives: ['L3 + R3', 'พลังสปาร์ตัน'] |
| 5 | missing all alternatives: ['NARUTO X BORUTO Ultimate Ninja Storm Connections', 'PlayStation 5 #01-#02', 'PlayStation 5'] |
| 5 | missing all alternatives: ['PS VR2 Sense grip button', 'จับวัตถุในเกม'] |
| 5 | missing all alternatives: ['R (Right Stick)', 'ควบคุมมุมมอง / หันกล้อง'] |
| 5 | missing all alternatives: ['R', 'มุมกล้อง'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'กล้องส่องทางไกล'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ค้นหาผู้เล่นอื่น'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ซูมกล้องเล็ง'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ย่อตัว'] |
| 5 | missing all alternatives: ['R3 (Click Right Stick)', 'ระบบกูอิจิ'] |
| 5 | missing all alternatives: ['R3', 'แสดงเป้าหมาย / สแกนพื้นที่'] |
| 5 | missing all alternatives: ['Ring-Con tilt', 'เลื่อนเคอร์เซอร์ด้วย Ring-Con'] |
| 5 | missing all alternatives: ['Shift + Q / W / E / R', 'ใช้สกิลแบบ quick cast'] |
| 5 | missing all alternatives: ['Space Bar', 'กระโดด'] |
| 5 | missing all alternatives: ['Spacebar', 'กระโดด'] |
| 5 | missing all alternatives: ['Square', 'วิ่งเร็ว'] |
| 5 | missing all alternatives: ['Square', 'โจมตีด้วยดาบ / โจมตีระยะประชิด'] |
| 5 | missing all alternatives: ['Triangle', 'คาถานินจา / จักระ'] |
| 5 | missing all alternatives: ['Triangle', 'จ่ายบอลทะลุช่อง'] |
| 5 | missing all alternatives: ['Triangle', 'โจมตีเวทมนตร์'] |
| 5 | missing all alternatives: ['Uncharted', 'PlayStation 5 #01-#02', 'PlayStation 5'] |
| 5 | missing all alternatives: ['X', 'มองหลัง'] |
| 5 | missing all alternatives: ['Z', 'หมอบ'] |
| 5 | missing required: College of Computing |
| 5 | missing required: esports learning development studio |
| 5 | missing required: prohibited |
| 5 | missing_complete_clause:2. เวลาต่อรอบ 1:55 นาที  /  Freeze time: 15 วินาที |
| 5 | missing_complete_clause:3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้ |
| 5 | missing_complete_clause:4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง |
| 5 | missing_complete_clause:Advantage: No advantage |
| 5 | missing_complete_clause:Stage: Random |
| 5 | missing_complete_clause:หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge |
| 5 | missing_complete_clause:หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้ |
| 5 | route:general expected:['no_answer'] |
| 5 | route:no_answer expected:['members', 'overview'] |
| 4 | intent:common_read expected:penalty_policy |
| 4 | missing all alternatives: ['+ (Plus)', 'หยุดเกมชั่วคราว'] |
| 4 | missing all alternatives: ['+ (Plus)', 'เปิดช่องเก็บของ'] |
| 4 | missing all alternatives: ['+ Button on controller-holding screen', 'Select Soccer Leg-Strap Mode locally'] |
| 4 | missing all alternatives: ['- (Minus)', 'Save & Quit'] |
| 4 | missing all alternatives: ['- (Minus)', 'Skip'] |
| 4 | missing all alternatives: ['- (Minus)', 'ข้าม'] |
| 4 | missing all alternatives: ['- (Minus)', 'บันทึกและออกจากเกม'] |
| 4 | missing all alternatives: ['1 / 2 / 3 / 4 / 5 / 6 / 7', 'Use items / trinket'] |
| 4 | missing all alternatives: ['1 / 2 / 3 / 4 / 5 / 6 / 7', 'ใช้ไอเทมหรือ trinket'] |
| 4 | missing all alternatives: ['1 / 2 / 3 / 4 / 5', 'เลือกอาวุธ'] |
| 4 | missing all alternatives: ['1 / 2 / 3', 'Equip weapons'] |
| 4 | missing all alternatives: ['1 / 2 / 3', 'Select weapons'] |
| 4 | missing all alternatives: ['4', 'Cycle Grenades'] |
| 4 | missing all alternatives: ['4', 'เลือก/วนระเบิด'] |
| 4 | missing all alternatives: ['A Button', 'Cancel selection'] |
| 4 | missing all alternatives: ['Alt + Q / W / E / R', 'Self cast abilities'] |
| 4 | missing all alternatives: ['Alt', 'Free look'] |
| 4 | missing all alternatives: ['Alt', 'มองอิสระ'] |
| 4 | missing all alternatives: ['B', 'กลับฐาน'] |
| 4 | missing all alternatives: ['B', 'เปลี่ยนการเคลื่อนที่'] |
| 4 | missing all alternatives: ['B', 'เปลี่ยนโหมดยิง'] |
| 4 | missing all alternatives: ['B', 'เปิดร้านซื้ออาวุธ'] |
| 4 | missing all alternatives: ['B', 'เปิดเมนูซื้อของ'] |
| 4 | missing all alternatives: ['Builder Pro / Combat Pro / Custom', 'Controller binding presets'] |
| 4 | missing all alternatives: ['Button controls', 'Play boards and minigames'] |
| 4 | missing all alternatives: ['Call of Duty', 'วิธีเล่น', 'เล่นได้ที่'] |
| 4 | missing all alternatives: ['Circle (วงกลม)', 'ยกเลิก'] |
| 4 | missing all alternatives: ['Circle / D-Pad Right', 'Sprint'] |
| 4 | missing all alternatives: ['Circle', 'Cancel'] |
| 4 | missing all alternatives: ['Circle', 'Close-Range Attack'] |
| 4 | missing all alternatives: ['Circle', 'Crouch/Prone/Slide'] |
| 4 | missing all alternatives: ['Circle', 'Dash'] |
| 4 | missing all alternatives: ['Circle', 'Flashlight / Remote'] |
| 4 | missing all alternatives: ['Circle', 'Interact / Activate Relic (While blocking)'] |
| 4 | missing all alternatives: ['Circle', 'Interact'] |
| 4 | missing all alternatives: ['Circle', 'Melee'] |
| 4 | missing all alternatives: ['Circle', 'Right Kick'] |
| 4 | missing all alternatives: ['Circle', 'Roll / Evade / Take Cover'] |
| 4 | missing all alternatives: ['Circle', 'Shoot / Shoulder Charge'] |
| 4 | missing all alternatives: ['Circle', 'Shoot / Volley / Header'] |
| 4 | missing all alternatives: ['Circle', 'กลิ้งหลบ / เข้าที่กำบัง'] |
| 4 | missing all alternatives: ['Circle', 'กลิ้งหลบ'] |
| 4 | missing all alternatives: ['Circle', 'พุ่งตัว'] |
| 4 | missing all alternatives: ['Circle', 'ยกเลิก / ย้อนกลับ'] |
| 4 | missing all alternatives: ['Circle', 'ยิง / เบียดแย่งบอล'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / สไลด์'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบ'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว / หมอบคลาน'] |
| 4 | missing all alternatives: ['Circle', 'ย่อตัว'] |
| 4 | missing all alternatives: ['Circle', 'หลบหลีก'] |
| 4 | missing all alternatives: ['Circle', 'เบรกมือ'] |
| 4 | missing all alternatives: ['Circle', 'โจมตีประชิด'] |
| 4 | missing all alternatives: ['Circle', 'โต้ตอบ / ใช้งานรีลิค'] |
| 4 | missing all alternatives: ['Circle', 'ใช้ Eikonic Feat'] |
| 4 | missing all alternatives: ['Controller Mapping page', 'Change controller preset'] |
| 4 | missing all alternatives: ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Cross (กากบาท)', 'Jump'] |
| 4 | missing all alternatives: ['Cross (กากบาท)', 'กระโดด'] |
| 4 | missing all alternatives: ['Cross / Square / L1 / R1', 'Pick Up / Drop'] |
| 4 | missing all alternatives: ['Cross', 'Crouch / Dodge / Jump'] |
| 4 | missing all alternatives: ['Cross', 'Jump / Climb / Scope (While aiming)'] |
| 4 | missing all alternatives: ['Cross', 'Jump / Climb / Shoulder Swap'] |
| 4 | missing all alternatives: ['Cross', 'Jump / Throw / Attack'] |
| 4 | missing all alternatives: ['Cross', 'Jump/Mantle'] |
| 4 | missing all alternatives: ['Cross', 'Left Kick'] |
| 4 | missing all alternatives: ['Cross', 'Low Pass / Press'] |
| 4 | missing all alternatives: ['Cross', 'Pick Up / Drop'] |
| 4 | missing all alternatives: ['Cross', 'Shift Up'] |
| 4 | missing all alternatives: ['Cross', 'Sidestep / Dodge (double tap)'] |
| 4 | missing all alternatives: ['Cross', 'Use Tactical Equipment'] |
| 4 | missing all alternatives: ['Cross', 'กระโดด / ปีนป่าย / ซูมสโคป (ขณะเล็ง)'] |
| 4 | missing all alternatives: ['Cross', 'กระโดด / ปีนป่าย / สลับมุมกล้อง'] |
| 4 | missing all alternatives: ['Cross', 'ย่อตัว / กลิ้งหลบ / กระโดด'] |
| 4 | missing all alternatives: ['Cross', 'สเตปหลบ / กลิ้งหลบ'] |
| 4 | missing all alternatives: ['Cross', 'ส่งบอลเลียด / เพรสซิง'] |
| 4 | missing all alternatives: ['Cross', 'หยิบ / วาง'] |
| 4 | missing all alternatives: ['Cross', 'โต้ตอบ / สำรวจ'] |
| 4 | missing all alternatives: ['Cross', 'ใช้อุปกรณ์ยุทธวิธี'] |
| 4 | missing all alternatives: ['Ctrl', 'เดิน'] |
| 4 | missing all alternatives: ['D / F', 'Summoner Spells'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Equip Quick Slot weapons'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Tool selection (Up / Down / Left / Right)'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอาวุธกากบาท'] |
| 4 | missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอุปกรณ์ด่วน'] |
| 4 | missing all alternatives: ['D-Pad (Up / Left / Right)', 'Select Weapon'] |
| 4 | missing all alternatives: ['D-Pad (Up / Left / Right)', 'เลือกอาวุธ'] |
| 4 | missing all alternatives: ['D-Pad (Up, Down, Left, Right)', 'Taunt'] |
| 4 | missing all alternatives: ['D-Pad (Up, Down, Left, Right)', 'ยั่วยุ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Duck'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Equip Tertiary Weapon'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Locate Vehicle'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Photo mode'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Store Tool'] |
| 4 | missing all alternatives: ['D-Pad Down', 'Whistle'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ตรวจสอบตำแหน่งรถ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ติดตั้งอาวุธที่สาม'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ผิวปากเรียกม้า'] |
| 4 | missing all alternatives: ['D-Pad Down', 'ย่อตัว / ก้มหลบ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'เก็บเครื่องมือ'] |
| 4 | missing all alternatives: ['D-Pad Down', 'โหมดถ่ายภาพ'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Action Bar: Scroll Left / Right'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Change Shield/Arrow / Change Weapon/Bow'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Change Tool'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'Shortcut 1 / Shortcut 2'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'คีย์ลัด 1 / 2'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'เปลี่ยนอุปกรณ์สวมใส่'] |
| 4 | missing all alternatives: ['D-Pad Left / Right', 'แถบแอคชั่น: เลื่อนซ้าย/ขวา'] |
| 4 | missing all alternatives: ['D-Pad Left', 'Equip Secondary Weapon'] |
| 4 | missing all alternatives: ['D-Pad Left', 'Move Backward'] |
| 4 | missing all alternatives: ['D-Pad Left', 'Revelio'] |
| 4 | missing all alternatives: ['D-Pad Left', 'ถอยหลัง / บล็อก'] |
| 4 | missing all alternatives: ['D-Pad Left', 'เรเวลิโอ'] |
| 4 | missing all alternatives: ['D-Pad Right', 'Equip Primary Weapon'] |
| 4 | missing all alternatives: ['D-Pad Right', 'amiibo'] |
| 4 | missing all alternatives: ['D-Pad Right', 'ติดตั้งอาวุธหลัก'] |
| 4 | missing all alternatives: ['D-Pad Right', 'สแกนอะมีโบ'] |
| 4 | missing all alternatives: ['D-Pad Right', 'เมนูคาถา'] |
| 4 | missing all alternatives: ['D-Pad Up / Down', 'Action Bar: Select/Perform Action'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Camouflage (Miles)'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Change Rune'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Charmed Compass / Quest Info (Hold)'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Jump'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Map'] |
| 4 | missing all alternatives: ['D-Pad Up', 'Tool Ring'] |
| 4 | missing all alternatives: ['D-Pad Up', 'กระโดด'] |
| 4 | missing all alternatives: ['D-Pad Up', 'พรางตัว (ไมลส์)'] |
| 4 | missing all alternatives: ['D-Pad Up', 'วงล้อเครื่องมือ'] |
| 4 | missing all alternatives: ['D-Pad Up', 'เข็มทิศ / ข้อมูลเควสต์'] |
| 4 | missing all alternatives: ['D-Pad Up', 'เปลี่ยนรูน'] |
| 4 | missing all alternatives: ['D-Pad Up', 'แผนที่'] |
| 4 | missing all alternatives: ['D-Pad', 'Campaign, Multiplayer or Co-Op specific'] |
| 4 | missing all alternatives: ['D-Pad', 'Change Weapon'] |
| 4 | missing all alternatives: ['D-Pad', 'Emote'] |
| 4 | missing all alternatives: ['D-Pad', 'License'] |
| 4 | missing all alternatives: ['D-Pad', 'MFD Controls'] |
| 4 | missing all alternatives: ['D-Pad', 'คำสั่งเฉพาะโหมด'] |
| 4 | missing all alternatives: ['D-Pad', 'ดูใบขับขี่และสถิติ'] |
| 4 | missing all alternatives: ['D-Pad', 'เปลี่ยนอาวุธ'] |
| 4 | missing all alternatives: ['Directional Button Left', 'Switch Items and Torgal Commands'] |
| 4 | missing all alternatives: ['Directional Button Left', 'สลับระหว่างไอเทมกับคำสั่ง Torgal'] |
| 4 | missing all alternatives: ['Directional Buttons Up / Right / Down', 'Item Shortcuts / Torgal Commands'] |
| 4 | missing all alternatives: ['Directional Buttons Up / Right / Down', 'ทางลัดไอเทมหรือคำสั่ง Torgal'] |
| 4 | missing all alternatives: ['F1 / F2 / F3 / F4 / F5', 'เลื่อนกล้องไปหาเพื่อนร่วมทีม'] |
| 4 | missing all alternatives: ['Fortnite คือเกมต่อสู้เอาชีวิตรอดที่ผู้เล่นแข่งกันในแผนที่ขนาดใหญ่และพยายามอยู่เป็นคนสุดท้าย'] |
| 4 | missing all alternatives: ['Fortnite', 'PlayStation 5 #01-#02', 'PlayStation 5'] |
| 4 | missing all alternatives: ['Gaming Chair', 'Gaming Chair'] |
| 4 | missing all alternatives: ['Gesture control scheme', 'Move using physical movements'] |
| 4 | missing all alternatives: ['Head/body movement', 'Dodge and position body'] |
| 4 | missing all alternatives: ['Joy-Con (R) Control Stick', 'Move cursor'] |
| 4 | missing all alternatives: ['Joy-Con motion', 'Play sport actions'] |
| 4 | missing all alternatives: ['L (Left Stick) / R (Right Stick)', 'Move'] |
| 4 | missing all alternatives: ['L (Left Stick)', 'Move / Strafe (While locked)'] |
| 4 | missing all alternatives: ['L / R', 'Grab'] |
| 4 | missing all alternatives: ['L / R', 'จับทุ่ม'] |
| 4 | missing all alternatives: ['L / ZL / R / ZR', 'Grab'] |
| 4 | missing all alternatives: ['L1 (Hold)', 'Block'] |
| 4 | missing all alternatives: ['L1 (Hold)', 'ป้องกัน (กดค้าง)'] |
| 4 | missing all alternatives: ['L1 + Triangle', 'Lobbed Through Pass'] |
| 4 | missing all alternatives: ['L1 + Triangle', 'ยกบอลทะลุช่อง'] |
| 4 | missing all alternatives: ['L1 / L2', 'Crouch / Slide'] |
| 4 | missing all alternatives: ['L1 / L2', 'ย่อตัว / สไลด์'] |
| 4 | missing all alternatives: ['L1', 'Change Player'] |
| 4 | missing all alternatives: ['L1', 'Dodge / Ability (Hold)'] |
| 4 | missing all alternatives: ['L1', 'Dodge'] |
| 4 | missing all alternatives: ['L1', 'Equipment Wheel'] |
| 4 | missing all alternatives: ['L1', 'Guard'] |
| 4 | missing all alternatives: ['L1', 'Jump/Mantle'] |
| 4 | missing all alternatives: ['L1', 'Lock On'] |
| 4 | missing all alternatives: ['L1', 'Look Back'] |
| 4 | missing all alternatives: ['L1', 'Parry'] |
| 4 | missing all alternatives: ['L1', 'Reset Camera / Radial Menu (Hold)'] |
| 4 | missing all alternatives: ['L1', 'Rope'] |
| 4 | missing all alternatives: ['L1', 'Special Style'] |
| 4 | missing all alternatives: ['L1', 'Sprint (Hold)'] |
| 4 | missing all alternatives: ['L1', 'Support 1'] |
| 4 | missing all alternatives: ['L1', 'Use Tactical Equipment'] |
| 4 | missing all alternatives: ['L1', 'Use Tool / Open Tool Wheel (Hold)'] |
| 4 | missing all alternatives: ['L1', 'กำลังเสริม 1'] |
| 4 | missing all alternatives: ['L1', 'ปัดป้อง'] |
| 4 | missing all alternatives: ['L1', 'มองหลัง'] |
| 4 | missing all alternatives: ['L1', 'ล็อกเป้าหมาย'] |
| 4 | missing all alternatives: ['L1', 'วงล้ออุปกรณ์'] |
| 4 | missing all alternatives: ['L1', 'วิ่งสปรินต์ (กดค้าง)'] |
| 4 | missing all alternatives: ['L1', 'สเปเชียลสไตล์'] |
| 4 | missing all alternatives: ['L1', 'หลบหลีก'] |
| 4 | missing all alternatives: ['L1', 'หลบหลีก(ปัดป้อง) / สกิล'] |
| 4 | missing all alternatives: ['L1', 'เปลี่ยนตัวผู้เล่น'] |
| 4 | missing all alternatives: ['L1', 'ใช้เชือกสลิง / โหนสลิง'] |
| 4 | missing all alternatives: ['L1', 'ใช้ไอเทม / วงล้อเครื่องมือ'] |
| 4 | missing all alternatives: ['L2 (Hold)', 'เล็งเป้าหมาย'] |
| 4 | missing all alternatives: ['L2 (hold) + Direction', 'Shield / Jockey'] |
| 4 | missing all alternatives: ['L2 (hold) + Direction', 'บังบอล / คุมเชิง'] |
| 4 | missing all alternatives: ['L2 / R2', 'Chop / Throw'] |
| 4 | missing all alternatives: ['L2', 'Aim / Brake'] |
| 4 | missing all alternatives: ['L2', 'Aim Down Sight Behavior'] |
| 4 | missing all alternatives: ['L2', 'Aim'] |
| 4 | missing all alternatives: ['L2', 'Brake'] |
| 4 | missing all alternatives: ['L2', 'Chapter Abilities'] |
| 4 | missing all alternatives: ['L2', 'Cycle / Switch Eikons'] |
| 4 | missing all alternatives: ['L2', 'Protect Ball'] |
| 4 | missing all alternatives: ['L2', 'Substitution Ninjutsu'] |
| 4 | missing all alternatives: ['L2', 'ความสามารถประจำด่าน (ซ้าย)'] |
| 4 | missing all alternatives: ['L2', 'คาถาสลับร่าง'] |
| 4 | missing all alternatives: ['L2', 'สลับ Eikon'] |
| 4 | missing all alternatives: ['L2', 'เล็งปืน (ADS)'] |
| 4 | missing all alternatives: ['L2', 'เล็งผ่านศูนย์'] |
| 4 | missing all alternatives: ['L2', 'เล็งผ่านศูนย์เล็ง'] |
| 4 | missing all alternatives: ['L2', 'เล็งเป้า / เล็งปืน'] |
| 4 | missing all alternatives: ['L3 (Click Left Stick)', 'Mark Enemy'] |
| 4 | missing all alternatives: ['L3 + R3', 'Limit Break'] |
| 4 | missing all alternatives: ['L3 + R3', 'ใช้ Limit Break'] |
| 4 | missing all alternatives: ['L3', 'Perch / Dive'] |
| 4 | missing all alternatives: ['L3', 'Sprint (Hold)'] |
| 4 | missing all alternatives: ['L3', 'Sprint/Tactical Sprint/Focus'] |
| 4 | missing all alternatives: ['L3', 'Sprint/Tactical Sprint/Steady Aim'] |
| 4 | missing all alternatives: ['L3', 'วิ่ง (กดค้าง)'] |
| 4 | missing all alternatives: ['L3', 'ไฟหน้า'] |
| 4 | missing all alternatives: ['Left Ctrl', 'Crouch'] |
| 4 | missing all alternatives: ['Left Ctrl', 'Duck'] |
| 4 | missing all alternatives: ['Left Mouse Button', 'Shoot'] |
| 4 | missing all alternatives: ['Left PS VR2 Sense controller motion', 'Left-hand saber slash'] |
| 4 | missing all alternatives: ['Left Stick', 'Move / Dribble'] |
| 4 | missing all alternatives: ['Left Stick', 'Steer'] |
| 4 | missing all alternatives: ['Left Stick', 'เคลื่อนที่ / เลี้ยงบอล'] |
| 4 | missing all alternatives: ['Left Stick', 'เลี้ยว'] |
| 4 | missing all alternatives: ['Monster Hunter Rise คือเกมล่ามอนสเตอร์ที่ผู้เล่นเลือกอาวุธ ทำภารกิจ และเก็บวัตถุดิบมาสร้างอุปกรณ์'] |
| 4 | missing all alternatives: ['Nintendo Switch', 'Zone'] |
| 4 | missing all alternatives: ['One Joy-Con', 'Play character'] |
| 4 | missing all alternatives: ['Options', 'Main Menu / Pause'] |
| 4 | missing all alternatives: ['Options', 'เปิดเมนูหลัก / หยุดเกม'] |
| 4 | missing all alternatives: ['PC', 'Zone'] |
| 4 | missing all alternatives: ['PS VR2 Sense grip button', 'Grab objects'] |
| 4 | missing all alternatives: ['Press Ring-Con inward', 'Confirm with Ring-Con'] |
| 4 | missing all alternatives: ['Press Ring-Con inward', 'ยืนยันด้วย Ring-Con'] |
| 4 | missing all alternatives: ['Pull Ring-Con outward', 'Cancel with Ring-Con'] |
| 4 | missing all alternatives: ['Pull Ring-Con outward', 'ยกเลิกด้วย Ring-Con'] |
| 4 | missing all alternatives: ['Q / E / C / X', 'ใช้สกิล Agent'] |
| 4 | missing all alternatives: ['Q / E', 'Lean Left / Lean Right'] |
| 4 | missing all alternatives: ['Q / E', 'เอียงซ้าย / เอียงขวา'] |
| 4 | missing all alternatives: ['Q / W / E / R', 'Cast abilities'] |
| 4 | missing all alternatives: ['Q', 'สลับกลับอาวุธล่าสุด'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'Smash Attack'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'Turn'] |
| 4 | missing all alternatives: ['R (Right Stick)', 'View'] |
| 4 | missing all alternatives: ['R', 'ดริฟต์'] |
| 4 | missing all alternatives: ['R', 'รีเซ็ตกล้อง'] |
| 4 | missing all alternatives: ['R1 (While in Heat)', 'Heat Smash'] |
| 4 | missing all alternatives: ['R1 + Circle', 'Finesse Shot'] |
| 4 | missing all alternatives: ['R1 + Cross', 'Driven Ground Pass'] |
| 4 | missing all alternatives: ['R1 + Cross', 'ส่งเลียดแบบพุ่งแรง'] |
| 4 | missing all alternatives: ['R1 / R2', 'จับ'] |
| 4 | missing all alternatives: ['R1', 'Ancient Magic Throw'] |
| 4 | missing all alternatives: ['R1', 'Evade'] |
| 4 | missing all alternatives: ['R1', 'Grenade'] |
| 4 | missing all alternatives: ['R1', 'Heal'] |
| 4 | missing all alternatives: ['R1', 'Heat Activate'] |
| 4 | missing all alternatives: ['R1', 'Light Attack / Light Runic Attack (While blocking) / Throw (While aiming)'] |
| 4 | missing all alternatives: ['R1', 'Listen mode (Hold) / Switch Weapon'] |
| 4 | missing all alternatives: ['R1', 'Rope Grapple'] |
| 4 | missing all alternatives: ['R1', 'Specialization'] |
| 4 | missing all alternatives: ['R1', 'Sprint (Hold)'] |
| 4 | missing all alternatives: ['R1', 'Sprint / Quick Turn'] |
| 4 | missing all alternatives: ['R1', 'Support 2'] |
| 4 | missing all alternatives: ['R1', 'Weapon Swap / Listen (Hold)'] |
| 4 | missing all alternatives: ['R1', 'กำลังเสริม 2'] |
| 4 | missing all alternatives: ['R1', 'ขว้างระเบิดมือ'] |
| 4 | missing all alternatives: ['R1', 'ขว้างเวทมนตร์โบราณ'] |
| 4 | missing all alternatives: ['R1', 'ความสามารถพิเศษ'] |
| 4 | missing all alternatives: ['R1', 'ฟื้นฟูพลังชีวิต / ใช้ยา'] |
| 4 | missing all alternatives: ['R1', 'ยิงใย / อุปกรณ์แก็ดเจ็ต'] |
| 4 | missing all alternatives: ['R1', 'วิ่ง / กลับหลังหัน'] |
| 4 | missing all alternatives: ['R1', 'วิ่งเร็ว (กดค้าง)'] |
| 4 | missing all alternatives: ['R1', 'หลบหลีก'] |
| 4 | missing all alternatives: ['R1', 'เปลี่ยนมุมมอง'] |
| 4 | missing all alternatives: ['R1', 'โจมตีเบา / รูนเบา / ขว้าง'] |
| 4 | missing all alternatives: ['R1', 'โหนเชือก / สลิง'] |
| 4 | missing all alternatives: ['R1', 'โหมดฟังเสียง (กดค้าง) / สลับอาวุธด่วน'] |
| 4 | missing all alternatives: ['R2 (Hold)', 'โหนใย / ปากัวร์'] |
| 4 | missing all alternatives: ['R2 (hold) + Direction', 'Sprint'] |
| 4 | missing all alternatives: ['R2 (hold) + Direction', 'วิ่งสปรินต์'] |
| 4 | missing all alternatives: ['R2 + Square / Triangle / Cross / Circle', 'Use Eikonic Ability'] |
| 4 | missing all alternatives: ['R2 + Square / Triangle / Cross / Circle', 'ใช้ Eikonic Ability ที่ผูกไว้'] |
| 4 | missing all alternatives: ['R2 + Touch Pad', 'Taunt'] |
| 4 | missing all alternatives: ['R2 + Touch Pad', 'ยั่วยุ'] |
| 4 | missing all alternatives: ['R2', 'Basic Cast / Activate Spell Set (Hold)'] |
| 4 | missing all alternatives: ['R2', 'Chapter Abilities'] |
| 4 | missing all alternatives: ['R2', 'Dash'] |
| 4 | missing all alternatives: ['R2', 'Fire / Accelerate'] |
| 4 | missing all alternatives: ['R2', 'Guard'] |
| 4 | missing all alternatives: ['R2', 'Primary Fire'] |
| 4 | missing all alternatives: ['R2', 'Ready Eikonic Abilities'] |
| 4 | missing all alternatives: ['R2', 'Reload / Use (Hold) / Fire (While aiming)'] |
| 4 | missing all alternatives: ['R2', 'Shoot (While aiming) / Reload'] |
| 4 | missing all alternatives: ['R2', 'Shoot / Knife attack'] |
| 4 | missing all alternatives: ['R2', 'ความสามารถประจำด่าน (ขวา)'] |
| 4 | missing all alternatives: ['R2', 'ยิง / โจมตีด้วยมีด'] |
| 4 | missing all alternatives: ['R2', 'ยิง'] |
| 4 | missing all alternatives: ['R2', 'ยิงปืน (ขณะเล็ง) / รีโหลดกระสุน'] |
| 4 | missing all alternatives: ['R2', 'ยิงปืน / เหยียบคันเร่ง'] |
| 4 | missing all alternatives: ['R2', 'ยิงอาวุธ'] |
| 4 | missing all alternatives: ['R2', 'รีโหลด / ใช้ไอเทม (กดค้าง) / ยิงปืน (ขณะเล็ง)'] |
| 4 | missing all alternatives: ['R2', 'เปิดชุด Eikonic Abilities'] |
| 4 | missing all alternatives: ['R2', 'เร่งความเร็ว'] |
| 4 | missing all alternatives: ['R2', 'โจมตี / ยิงปืน'] |
| 4 | missing all alternatives: ['R2', 'โจมตีพื้นฐาน / เปิดชุดคาถา'] |
| 4 | missing all alternatives: ['R2', 'โจมตีหนัก / รูนหนัก'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Find Other Player'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Gooigi'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Lock-On'] |
| 4 | missing all alternatives: ['R3 (Click Right Stick)', 'Scope'] |
| 4 | missing all alternatives: ['R3', 'Change Stance/Slide/Dive'] |
| 4 | missing all alternatives: ['R3', 'Melee'] |
| 4 | missing all alternatives: ['R3', 'Quick Melee'] |
| 4 | missing all alternatives: ['R3', 'Reset Camera'] |
| 4 | missing all alternatives: ['R3', 'Show Objective / Scan Environment'] |
| 4 | missing all alternatives: ['R3', 'รีเซ็ตมุมกล้อง'] |
| 4 | missing all alternatives: ['R3', 'โจมตีประชิด'] |
| 4 | missing all alternatives: ['R3', 'โจมตีระยะประชิด'] |
| 4 | missing all alternatives: ['R3', 'ไนตรัส / เร่งแซง'] |
| 4 | missing all alternatives: ['RS (Right Stick) Left/Right', 'Change Leader'] |
| 4 | missing all alternatives: ['Right Mouse Button', 'Move / Attack target'] |
| 4 | missing all alternatives: ['Right Mouse Button', 'Secondary Fire'] |
| 4 | missing all alternatives: ['Right Mouse Button', 'เล็ง'] |
| 4 | missing all alternatives: ['Right PS VR2 Sense controller motion', 'Right-hand saber slash'] |
| 4 | missing all alternatives: ['Right Stick', 'Camera Movement'] |
| 4 | missing all alternatives: ['Ring-Con tilt', 'Move menu cursor'] |
| 4 | missing all alternatives: ['Shift + Q / W / E / R', 'Quick cast abilities'] |
| 4 | missing all alternatives: ['Shift', 'Sprint / Hold Breath'] |
| 4 | missing all alternatives: ['Simple controls', 'Run, leap, and stomp'] |
| 4 | missing all alternatives: ['Single Joy-Con / Joy-Con grip / Pro Controller', 'Supported controller styles'] |
| 4 | missing all alternatives: ['Space Bar', 'Jump'] |
| 4 | missing all alternatives: ['Space', 'Jump'] |
| 4 | missing all alternatives: ['Space', 'กระโดด'] |
| 4 | missing all alternatives: ['Spacebar', 'Center camera on champion'] |
| 4 | missing all alternatives: ['Spacebar', 'Jump'] |
| 4 | missing all alternatives: ['Spacebar', 'ล็อก/ดึงกล้องกลับมาตัวเอง'] |
| 4 | missing all alternatives: ['Square (สี่เหลี่ยม)', 'Dash'] |
| 4 | missing all alternatives: ['Square (สี่เหลี่ยม)', 'พุ่งตัว'] |
| 4 | missing all alternatives: ['Square', 'Attack'] |
| 4 | missing all alternatives: ['Square', 'Companion Attack'] |
| 4 | missing all alternatives: ['Square', 'Interact'] |
| 4 | missing all alternatives: ['Square', 'Interact/Reload'] |
| 4 | missing all alternatives: ['Square', 'Left Punch'] |
| 4 | missing all alternatives: ['Square', 'Lob Pass / Cross / Header'] |
| 4 | missing all alternatives: ['Square', 'Lofted Pass / Cross / Sliding Tackle'] |
| 4 | missing all alternatives: ['Square', 'Melee / Shoulder Swap (While aiming)'] |
| 4 | missing all alternatives: ['Square', 'Melee / Sword Attack'] |
| 4 | missing all alternatives: ['Square', 'Shuriken'] |
| 4 | missing all alternatives: ['Square', 'Sprint'] |
| 4 | missing all alternatives: ['Square', 'Use/Reload'] |
| 4 | missing all alternatives: ['Square', 'บรรจุกระสุน'] |
| 4 | missing all alternatives: ['Square', 'รีโหลด / บรรจุกระสุน'] |
| 4 | missing all alternatives: ['Square', 'รีโหลด'] |
| 4 | missing all alternatives: ['Square', 'ลดเกียร์'] |
| 4 | missing all alternatives: ['Square', 'ส่งโด่ง / เปิดบอล / สไลด์แท็กเกิล'] |
| 4 | missing all alternatives: ['Square', 'หั่น / ขว้าง'] |
| 4 | missing all alternatives: ['Square', 'โจมตี'] |
| 4 | missing all alternatives: ['Square', 'โจมตีประชิด / สลับฝั่งมุมกล้อง (ขณะเล็ง)'] |
| 4 | missing all alternatives: ['Square', 'โต้ตอบ'] |
| 4 | missing all alternatives: ['Square', 'ใช้ไอเทม'] |
| 4 | missing all alternatives: ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['Tab / I', 'Inventory'] |
| 4 | missing all alternatives: ['Tab / I', 'เปิดกระเป๋า'] |
| 4 | missing all alternatives: ['Tab', 'ดู scoreboard'] |
| 4 | missing all alternatives: ['Touch Pad', 'Backpack'] |
| 4 | missing all alternatives: ['Touch Pad', 'Flash Hazards'] |
| 4 | missing all alternatives: ['Touch Pad', 'Inventory'] |
| 4 | missing all alternatives: ['Touch Pad', 'Journal'] |
| 4 | missing all alternatives: ['Touch Pad', 'Map (Press) / FNSM App (Swipe)'] |
| 4 | missing all alternatives: ['Touch Pad', 'Menu'] |
| 4 | missing all alternatives: ['Touch Pad', 'Scoreboard'] |
| 4 | missing all alternatives: ['Touch Pad', 'ตารางคะแนน / แผนที่'] |
| 4 | missing all alternatives: ['Touch Pad', 'เปิดสมุดบันทึก'] |
| 4 | missing all alternatives: ['Touch Pad', 'เมนู'] |
| 4 | missing all alternatives: ['Touch Pad', 'แผนที่ / แอป FNSM'] |
| 4 | missing all alternatives: ['Touch Pad', 'ไฟฉุกเฉิน'] |
| 4 | missing all alternatives: ['Triangle (สามเหลี่ยม)', 'Interact'] |
| 4 | missing all alternatives: ['Triangle (สามเหลี่ยม)', 'โต้ตอบ'] |
| 4 | missing all alternatives: ['Triangle', 'Call'] |
| 4 | missing all alternatives: ['Triangle', 'Magic Attack'] |
| 4 | missing all alternatives: ['Triangle', 'Ninjutsu'] |
| 4 | missing all alternatives: ['Triangle', 'Protego / Block (Hold)'] |
| 4 | missing all alternatives: ['Triangle', 'Ready Weapon'] |
| 4 | missing all alternatives: ['Triangle', 'Reload'] |
| 4 | missing all alternatives: ['Triangle', 'Return axe / Furious Immolation and Glacial Permafrost (While blocking)'] |
| 4 | missing all alternatives: ['Triangle', 'Reverse'] |
| 4 | missing all alternatives: ['Triangle', 'Right Punch'] |
| 4 | missing all alternatives: ['Triangle', 'Through Ball / Clear'] |
| 4 | missing all alternatives: ['Triangle', 'Through Pass'] |
| 4 | missing all alternatives: ['Triangle', 'Weapon'] |
| 4 | missing all alternatives: ['Triangle', 'Web Strike / Web Wings'] |
| 4 | missing all alternatives: ['Triangle', 'คลังไอเทม'] |
| 4 | missing all alternatives: ['Triangle', 'จ่ายทะลุช่อง / เคลียร์บอล'] |
| 4 | missing all alternatives: ['Triangle', 'ดึงตัวพุ่งโจมตี / ปีกใยแมงมุม'] |
| 4 | missing all alternatives: ['Triangle', 'ถอยหลัง'] |
| 4 | missing all alternatives: ['Triangle', 'ป้องกัน / บล็อกคาถา'] |
| 4 | missing all alternatives: ['Triangle', 'รีโหลด / บรรจุกระสุน'] |
| 4 | missing all alternatives: ['Triangle', 'อาวุธ'] |
| 4 | missing all alternatives: ['Triangle', 'เปิดกระเป๋าเก็บของ'] |
| 4 | missing all alternatives: ['Triangle', 'เรียก'] |
| 4 | missing all alternatives: ['Triangle', 'เรียกขวานกลับ / ชาร์จพลังอาวุธ'] |
| 4 | missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ / เก็บของ'] |
| 4 | missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ'] |
| 4 | missing all alternatives: ['VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ'] |
| 4 | missing all alternatives: ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] |
| 4 | missing all alternatives: ['W / A / S / D', 'Move Character'] |
| 4 | missing all alternatives: ['X / Y', 'Jump'] |
| 4 | missing all alternatives: ['X / Y', 'Throw cap / Dash (Hold)'] |
| 4 | missing all alternatives: ['X / Y', 'กระโดด'] |
| 4 | missing all alternatives: ['X / Y', 'ขว้างหมวก / วิ่งเร็ว'] |
| 4 | missing all alternatives: ['X Button on sport-selection screen', 'Select Soccer Leg-Strap Mode in Play Globally'] |
| 4 | missing all alternatives: ['X', 'Dark Light'] |
| 4 | missing all alternatives: ['X', 'Hints'] |
| 4 | missing all alternatives: ['X', 'Inventory'] |
| 4 | missing all alternatives: ['X', 'Jump / Dodge (While locked)'] |
| 4 | missing all alternatives: ['X', 'Unequip weapon'] |
| 4 | missing all alternatives: ['X', 'กระเป๋าช่องเก็บของ'] |
| 4 | missing all alternatives: ['X', 'กระโดด / หลบหลีก'] |
| 4 | missing all alternatives: ['X', 'คำใบ้'] |
| 4 | missing all alternatives: ['X', 'บีบแตร'] |
| 4 | missing all alternatives: ['X', 'เก็บ/ถอดอาวุธ'] |
| 4 | missing all alternatives: ['X', 'ไฟดาร์กไลต์'] |
| 4 | missing all alternatives: ['Y / B', 'Throw / Slap'] |
| 4 | missing all alternatives: ['Y / B', 'ขว้าง / ตบ'] |
| 4 | missing all alternatives: ['Y / U', 'Chat'] |
| 4 | missing all alternatives: ['Y / U', 'แชท'] |
| 4 | missing all alternatives: ['Y', 'ยิงจุกยาง'] |
| 4 | missing all alternatives: ['Y', 'หยิบไอเทม'] |
| 4 | missing all alternatives: ['Y', 'เปิด/ปิดระบบช่วยขับ'] |
| 4 | missing all alternatives: ['Y', 'โจมตี'] |
| 4 | missing all alternatives: ['Z', 'Prone'] |
| 4 | missing all alternatives: ['ZL / ZR', 'Shield'] |
| 4 | missing all alternatives: ['ZL / ZR', 'โล่ป้องกัน'] |
| 4 | missing all alternatives: ['ZL', 'Blow'] |
| 4 | missing all alternatives: ['ZL', 'Crouch'] |
| 4 | missing all alternatives: ['ZL', 'Lock-On (Hold)'] |
| 4 | missing all alternatives: ['ZL', 'NookPhone'] |
| 4 | missing all alternatives: ['ZL', 'Use Item / Horn'] |
| 4 | missing all alternatives: ['ZL', 'ย่อตัว'] |
| 4 | missing all alternatives: ['ZL', 'ล็อกเป้าหมาย'] |
| 4 | missing all alternatives: ['ZL', 'สมาร์ทโฟน'] |
| 4 | missing all alternatives: ['ZL', 'ใช้ไอเทม / บีบแตร'] |
| 4 | missing all alternatives: ['ZR', 'Drift'] |
| 4 | missing all alternatives: ['ZR', 'Reactions'] |
| 4 | missing all alternatives: ['ZR', 'Suck'] |
| 4 | missing all alternatives: ['ZR', 'Use bow'] |
| 4 | missing all alternatives: ['ZR', 'ดริฟต์'] |
| 4 | missing all alternatives: ['ZR', 'ดูดลม / ดูดผี'] |
| 4 | missing all alternatives: ['ZR', 'แสดงอารมณ์'] |
| 4 | missing all alternatives: ['ZR', 'ใช้ธนู'] |
| 4 | missing all alternatives: ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง'] |
| 4 | missing all alternatives: ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล'] |
| 4 | missing all alternatives: ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด'] |
| 4 | missing required: 190 บาท |
| 4 | missing required: 2026-09-29 |
| 4 | missing required: 50 บาท |
| 4 | missing required: 65 บาท |
| 4 | missing_complete_clause:1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้ |
| 4 | missing_complete_clause:3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง |
| 4 | missing_complete_clause:4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode) |
| 4 | missing_complete_clause:4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick |
| 4 | missing_complete_clause:4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่ |
| 4 | missing_complete_clause:4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ |
| 4 | missing_complete_clause:4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม |
| 4 | missing_complete_clause:อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ |
| 4 | route:clarification expected:['games', 'reservation'] |
| 4 | route:clarification expected:['general', 'overview', 'home', 'knowledge'] |
| 4 | route:clarification expected:['general', 'overview', 'home'] |
| 4 | route:clarification expected:['rules', 'overview', 'no_answer'] |
| 4 | route:knowledge expected:['games', 'general', 'clarification'] |
| 4 | route:knowledge expected:['general', 'reservation', 'clarification'] |
| 4 | route:knowledge expected:['schedule', 'clarification'] |
| 4 | route:reservation expected:['no_answer'] |
| 4 | validation errors: ['missing_requested_field:players_min', 'missing_requested_field:players_max', 'missing_requested_field:network_requirement', 'missing_requested_field:studio_supported'] |
| 4 | validation errors: ['missing_requested_field:steps', 'missing_requested_field:players_max'] |
| 4 | validation errors: ['unresolved_query_clause', 'missing_requested_field:steps'] |
| 3 | Nintendo Switch |
| 3 | intent:common_read expected:game_detail_lookup |
| 3 | intent:user_service_facts expected:group_count |
| 3 | missing required: 150 บาท |
| 3 | missing_complete_clause:1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket |
| 3 | missing_complete_clause:2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด |
| 3 | missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด |
| 3 | missing_complete_clause:4.1.4. If a team starts the match more than 15 minutes after the scheduled time, the delayed team will be immediately forfeited. |
| 3 | missing_complete_clause:4.2.3. Runes and enhancement systems may be used as desired. |
| 3 | missing_complete_clause:4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่ |
| 3 | missing_complete_clause:Allowed keyboard technology: Snap Tap, SOCD, or equivalent technologies, unless otherwise instructed by officials. |
| 3 | missing_complete_clause:Any character can be selected (except DLC characters) |
| 3 | missing_complete_clause:Check-in: arrive at least 30 minutes before the scheduled match time. |
| 3 | missing_complete_clause:Communication: All participants must use the Discord server designated by the Center. |
| 3 | missing_complete_clause:Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception. |
| 3 | missing_complete_clause:Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match. |
| 3 | missing_complete_clause:General eligibility: Open only to students currently enrolled at Prince of Songkla University, Phuket Campus. |
| 3 | missing_complete_clause:If any member withdraws, the team may be disqualified. |
| 3 | missing_complete_clause:If tied at 1-1, a deciding game will be played |
| 3 | missing_complete_clause:In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over. |
| 3 | missing_complete_clause:In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice. |
| 3 | missing_complete_clause:Maximum of 24 rounds (12 rounds per side). The winner is the first team to win 13 rounds. |
| 3 | missing_complete_clause:Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes. |
| 3 | missing_complete_clause:One request per map is allowed. |
| 3 | missing_complete_clause:PlayStation 5 console used |
| 3 | missing_complete_clause:Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited. |
| 3 | missing_complete_clause:Players may compete under only one team. |
| 3 | missing_complete_clause:Referees may reconsider decisions as appropriate to ensure fairness. |
| 3 | missing_complete_clause:Registration of players is not permitted after the registration period has closed. |
| 3 | missing_complete_clause:Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket. |
| 3 | missing_complete_clause:Semifinals and finals: Best of 3 (BO3) |
| 3 | missing_complete_clause:Side selection: a knife round is used to choose sides. |
| 3 | missing_complete_clause:Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time. |
| 3 | missing_complete_clause:Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees. |
| 3 | missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited. |
| 3 | missing_complete_clause:Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute. |
| 3 | missing_complete_clause:Turn OFF Blood and Bodies displays. Displaying FPS or Latency graphs during competition is prohibited. |
| 3 | missing_complete_clause:Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception. |
| 3 | missing_complete_clause:Used when there are device malfunctions, disconnections, or software issues |
| 3 | missing_complete_clause:Using teammates to jump higher than the normal jump range is prohibited. |
| 3 | missing_complete_clause:เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive |
| 3 | missing_complete_clause:แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive |
| 3 | route:contact expected:['competition_rules'] |
| 3 | route:knowledge expected:['general', 'no_answer', 'unknown'] |
| 3 | route:knowledge expected:['no_answer', 'games'] |
| 3 | route:no_answer expected:['games'] |
| 3 | route:no_answer expected:['multi_question'] |
| 3 | route:reservation expected:['competition_rules'] |
| 3 | validation errors: ['missing_requested_field:consequence', 'missing_requested_field:details', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions'] |
| 3 | validation errors: ['missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:consequence', 'missing_requested_field:details'] |
| 3 | validation errors: ['missing_requested_field:details', 'missing_requested_field:consequence'] |
| 3 | validation errors: ['missing_requested_field:details', 'missing_requested_field:specifications'] |
| 3 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:details', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence'] |
| 3 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:details'] |
| 3 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:required_documents', 'missing_requested_field:outcome'] |
| 3 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:steps', 'missing_requested_field:preconditions'] |
| 2 | Nintendo Switch Zone |
| 2 | PC Zone |
| 2 | PlayStation 5 Zone |
| 2 | VR Zone |
| 2 | intent:common_read expected:members_lookup |
| 2 | legacy_mode_prefix:['pipeline:structured_game_detail'] |
| 2 | missing all alternatives: ['Animal Crossing', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['Gaming Chair'] |
| 2 | missing all alternatives: ['Gaming Headset', 'Gaming Headset'] |
| 2 | missing all alternatives: ['Gaming Headset'] |
| 2 | missing all alternatives: ['NARUTO X BORUTO Ultimate Ninja Storm Connections', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['New Super Mario Bros. U Deluxe', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['PUBG', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['PlayStation 5 / VR', 'Zone'] |
| 2 | missing all alternatives: ['The Legend of Zelda', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['Uncharted', 'วิธีเล่น', 'เล่นได้ที่'] |
| 2 | missing all alternatives: ['maintenance', 'Maintenance', '09:00'] |
| 2 | missing all alternatives: ['นายพฤทธิ์', 'นักวิชาการคอมพิวเตอร์'] |
| 2 | missing all alternatives: ['นายภาสวุฒิ', 'นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer'] |
| 2 | missing all alternatives: ['นายสุพศิน อะนะฝรั่ง', 'นักศึกษาสหกิจ Web & AI Developer'] |
| 2 | missing all alternatives: ['เล่นตามเนื้อเรื่อง ต่อสู้ด้วยสกิล/คอมโบ ทำภารกิจ และพัฒนาความสามารถของตัวละคร'] |
| 2 | missing all alternatives: ['แนวเกม', 'เกม Open-world Action RPG'] |
| 2 | missing required: Example Quest |
| 2 | missing required: Square |
| 2 | missing required: The Last of Us Part I / Part II |
| 2 | missing required: alcohol consumption |
| 2 | missing required: บาท |
| 2 | missing required: บุคคลทั่วไป |
| 2 | missing_complete_clause:1. การเลือกแผนที่ ใช้ MAPBAN.GG |
| 2 | missing_complete_clause:1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน |
| 2 | missing_complete_clause:1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น |
| 2 | missing_complete_clause:1. รูปแบบทัวร์นาเมนต์ Single Elimination |
| 2 | missing_complete_clause:2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง |
| 2 | missing_complete_clause:3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น |
| 2 | missing_complete_clause:3. เงินเริ่มต้น $800  /  เวลาของระเบิด: 40 วินาที |
| 2 | missing_complete_clause:3.1. แข่งแบบออฟไลน์ |
| 2 | missing_complete_clause:3.2. แข่ง Best of 3 (BO3) ทุกรอบ |
| 2 | missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ |
| 2 | missing_complete_clause:4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game. |
| 2 | missing_complete_clause:5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง |
| 2 | missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ |
| 2 | missing_complete_clause:การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0 |
| 2 | missing_complete_clause:ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง |
| 2 | route:clarification expected:['general', 'overview', 'knowledge'] |
| 2 | route:clarification expected:['overview', 'members'] |
| 2 | route:clarification expected:['penalty', 'rules'] |
| 2 | route:competition_rules expected:['games'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview', 'knowledge'] |
| 2 | route:input_guard expected:['general', 'clarification', 'no_answer', 'overview'] |
| 2 | route:knowledge expected:['clarification', 'general', 'unknown'] |
| 2 | route:knowledge expected:['clarification', 'multi_question'] |
| 2 | route:knowledge expected:['clarification', 'no_answer'] |
| 2 | route:knowledge expected:['overview', 'members'] |
| 2 | route:knowledge expected:['rules', 'overview'] |
| 2 | route:knowledge expected:['schedule', 'general', 'clarification'] |
| 2 | route:no_answer expected:['general', 'overview', 'knowledge'] |
| 2 | validation errors: ['missing_requested_field:consequence', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:details'] |
| 2 | validation errors: ['missing_requested_field:decision', 'missing_requested_field:procedure_id', 'missing_requested_field:steps', 'missing_requested_field:required_documents', 'missing_requested_field:deadline_minutes', 'missing_requested_field:outcome'] |
| 2 | validation errors: ['missing_requested_field:details', 'missing_requested_field:consequence', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions'] |
| 2 | validation errors: ['missing_requested_field:mode_name', 'missing_requested_field:players_min', 'missing_requested_field:players_max', 'missing_requested_field:network_requirement', 'missing_requested_field:studio_supported'] |
| 2 | validation errors: ['missing_requested_field:preconditions', 'missing_requested_field:steps', 'missing_requested_field:required_documents', 'missing_requested_field:deadline_minutes', 'missing_requested_field:outcome', 'missing_requested_field:details', 'missing_requested_field:conditions_all'] |
| 2 | validation errors: ['missing_requested_field:preconditions', 'missing_requested_field:steps', 'missing_requested_field:required_documents', 'missing_requested_field:deadline_minutes'] |
| 2 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:steps', 'missing_requested_field:preconditions', 'missing_requested_field:deadline_minutes'] |
| 2 | validation errors: ['missing_requested_field:usage'] |
| 1 | 0 บาท |
| 1 | 09:00-12:00 |
| 1 | 1,050 บาท |
| 1 | 1-2 Persons |
| 1 | 100-500 |
| 1 | 13:00-16:00 |
| 1 | 3 หมวด |
| 1 | 3-4 Persons |
| 1 | 500-2,000 |
| 1 | 525 บาท |
| 1 | Circle |
| 1 | Cockpit Zone |
| 1 | Cross |
| 1 | Gaming PC |
| 1 | Local LLM |
| 1 | Mario Kart |
| 1 | Members |
| 1 | NARUTO X BORUTO |
| 1 | PSU Esports Assistant |
| 1 | PSU Esports Studio - Phuket |
| 1 | PSU Phuket Esports Club |
| 1 | PSU Student and Staff |
| 1 | PlayStation 5 |
| 1 | Square |
| 1 | TEKKEN 8 |
| 1 | Triangle |
| 1 | VR |
| 1 | VR 1 ชั่วโมง |
| 1 | VR 30 นาที |
| 1 | cooperative education |
| 1 | intent:chatbot_greeting expected:detail |
| 1 | intent:chatbot_identity expected:detail |
| 1 | intent:common_read expected:competition_game_list |
| 1 | intent:common_read expected:competition_rules_lookup |
| 1 | intent:common_read expected:count |
| 1 | intent:competition_rules_lookup expected:competition_game_list |
| 1 | intent:conversation_price_lookup expected:multi_question_split |
| 1 | intent:equipment_item_lookup expected:list |
| 1 | intent:freshness_live_source_required expected:detail |
| 1 | intent:keyboard_layout_mismatch expected:schedule_query |
| 1 | intent:price_missing_service expected:service_fee_query |
| 1 | intent:request_timeout expected:list |
| 1 | intent:user_service_facts expected:list |
| 1 | intent:zone_rental_fee expected:guard_no_answer |
| 1 | latency 27.019s exceeds 20.0s |
| 1 | legacy_mode_prefix:['pipeline:deterministic_calculator_fast'] |
| 1 | legacy_mode_prefix:['pipeline:structured_booking_game_service_selection'] |
| 1 | legacy_mode_prefix:['pipeline:structured_game_zone_ranking'] |
| 1 | legacy_mode_prefix:['pipeline:structured_service_fee_by_game'] |
| 1 | missing all alternatives: ['Beat Saber', 'Horizon Call of the Mountain', 'Resident Evil 4', '30'] |
| 1 | missing all alternatives: ['Call of Duty: Warzone', 'Counter-Strike 2', 'League of Legends'] |
| 1 | missing all alternatives: ['Cockpit', 'บาท', 'เกม'] |
| 1 | missing all alternatives: ['EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล'] |
| 1 | missing all alternatives: ['It Takes Two คือเกมผจญภัยสำหรับเล่นร่วมกันสองคน ที่ต้องช่วยกันแก้ปริศนาและผ่านด่าน'] |
| 1 | missing all alternatives: ['League of Legends คือเกมวางแผนต่อสู้แบบทีม ผู้เล่นเลือก Champion และร่วมกันทำลายฐานหลักของฝ่ายตรงข้าม'] |
| 1 | missing all alternatives: ['PlayStation 5 #01-#02', 'PlayStation 5', 'Uncharted'] |
| 1 | missing all alternatives: ['PlayStation 5', 'เล่นได้ที่'] |
| 1 | missing all alternatives: ['PlayStation Zone', 'อุปกรณ์'] |
| 1 | missing all alternatives: ['Resident Evil 4 คือเกมเอาตัวรอดสยองขวัญที่เน้นการต่อสู้ การสำรวจ และการบริหารกระสุน/ไอเทม'] |
| 1 | missing all alternatives: ['ขอ', 'เกม', 'ปุ่ม', 'ยังไม่'] |
| 1 | missing all alternatives: ['เก็บอาวุธ เคลื่อนตามวง ต่อสู้กับผู้เล่นอื่น และใช้การสร้างหรือโหมดไม่สร้างตามรูปแบบที่เลือก'] |
| 1 | missing all alternatives: ['แนวเกม', 'เกม VR Rhythm'] |
| 1 | missing all alternatives: ['แนวเกม', 'เกมยิง Tactical FPS'] |
| 1 | missing required: 1 ชั่วโมง |
| 1 | missing required: 100-500 THB |
| 1 | missing required: 13:00 |
| 1 | missing required: 16:00 |
| 1 | missing required: 17 เกม |
| 1 | missing required: 70 บาท |
| 1 | missing required: 70 บาท/session |
| 1 | missing required: DDR5 32GB |
| 1 | missing required: Gaming PC |
| 1 | missing required: Intel Core i5-14400 |
| 1 | missing required: Maintenance |
| 1 | missing required: Mario มีปุ่มอะไรบ้าง |
| 1 | missing required: PC 1 ชั่วโมง |
| 1 | missing required: PC Zone มีอุปกรณ์อะไร |
| 1 | missing required: PS5 มีเกมอะไร |
| 1 | missing required: PS5 มีเกมอะไรบ้าง |
| 1 | missing required: PS5 ราคาเท่าไหร่ |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท |
| 1 | missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท |
| 1 | missing required: PlayStation 5 Zone และ Nintendo Switch Zone มีเกมเยอะสุด |
| 1 | missing required: Public visitors |
| 1 | missing required: Public visitors can book |
| 1 | missing required: RTX 5060 |
| 1 | missing required: TEKKEN 8 มีข้อมูลปุ่ม |
| 1 | missing required: TEKKEN 8 ไม่มีราคาแยกตามชื่อเกม |
| 1 | missing required: Tekken 8 มีปุ่มอะไร |
| 1 | missing required: Tekken 8 มีปุ่มอะไรบ้าง |
| 1 | missing required: Tekken 8 ราคาเท่าไหร่ |
| 1 | missing required: Tekken 8 เล่นที่ไหน |
| 1 | missing required: cannot confirm that this gaming station |
| 1 | missing required: does not establish access to every game |
| 1 | missing required: does not separately confirm whether carrying alcohol |
| 1 | missing required: full compensation |
| 1 | missing required: local service fee update 2026-07-27 |
| 1 | missing required: permission |
| 1 | missing required: power outlets |
| 1 | missing required: คำตอบ: |
| 1 | missing required: จองยังไง |
| 1 | missing required: จะเล่น Tekken 8 ต้องจองยังไง |
| 1 | missing required: ดูเฉย ๆ |
| 1 | missing required: ต่างกันดังนี้ |
| 1 | missing required: พื้นที่ที่กำหนด |
| 1 | missing required: มีเกมอะไรบ้าง |
| 1 | missing required: ยังไม่พบข้อมูลยืนยัน |
| 1 | missing required: วันจันทร์ |
| 1 | missing required: วิธีเล่นโดยสรุป |
| 1 | missing required: ห้าม |
| 1 | missing required: ห้ามพูดจาดูหมิ่น |
| 1 | missing required: เกมต่อสู้ |
| 1 | missing required: แอลกอฮอล์ |
| 1 | missing required: โดยไม่จองล่วงหน้าไม่ได้ |
| 1 | missing required: ไม่พบข้อมูล |
| 1 | missing_complete_clause:1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น |
| 1 | missing_complete_clause:1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน |
| 1 | missing_complete_clause:1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา |
| 1 | missing_complete_clause:1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3) |
| 1 | missing_complete_clause:1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม |
| 1 | missing_complete_clause:1. โหมด Competitive (5v5) |
| 1 | missing_complete_clause:2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง |
| 1 | missing_complete_clause:2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ |
| 1 | missing_complete_clause:2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร |
| 1 | missing_complete_clause:3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที |
| 1 | missing_complete_clause:3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ |
| 1 | missing_complete_clause:4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time |
| 1 | missing_complete_clause:4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ)  /  ผู้ชนะคือทีมที่ได้ 13 รอบก่อน |
| 1 | missing_complete_clause:4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น |
| 1 | missing_complete_clause:4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side. |
| 1 | missing_complete_clause:4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที |
| 1 | missing_complete_clause:4.2.2. Use Global Ban/Pick hero selection. |
| 1 | missing_complete_clause:4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ |
| 1 | missing_complete_clause:4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion. |
| 1 | missing_complete_clause:5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด |
| 1 | missing_complete_clause:5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ |
| 1 | missing_complete_clause:กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม |
| 1 | missing_complete_clause:การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ |
| 1 | missing_complete_clause:ขอได้ 1 ครั้งต่อแผนที่ |
| 1 | missing_complete_clause:จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน |
| 1 | missing_complete_clause:จำนวนรอบต่อเกม (Round): 3 |
| 1 | missing_complete_clause:ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น |
| 1 | missing_complete_clause:ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies) |
| 1 | missing_complete_clause:รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน |
| 1 | missing_complete_clause:ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่ |
| 1 | missing_complete_clause:ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน |
| 1 | missing_complete_clause:ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น |
| 1 | missing_complete_clause:ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ |
| 1 | missing_complete_clause:ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์ |
| 1 | missing_complete_clause:ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ |
| 1 | missing_complete_clause:เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น |
| 1 | missing_complete_clause:เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ |
| 1 | missing_complete_clause:เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง |
| 1 | missing_complete_clause:เวลาแข่งขันต่อรอบ (Timer): 60 วินาที |
| 1 | missing_complete_clause:เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง |
| 1 | missing_complete_clause:ใช้เครื่องเกม PlayStation 5 |
| 1 | outcome expected clarification_required, got no_answer |
| 1 | route expected ['competition_rules', 'clarification'], got no_answer |
| 1 | route:clarification expected:['service_fee'] |
| 1 | route:equipment expected:['games', 'clarification'] |
| 1 | route:games expected:['general', 'knowledge'] |
| 1 | route:games expected:['service_fee'] |
| 1 | route:input_guard expected:['equipment', 'no_answer'] |
| 1 | route:input_guard expected:['schedule'] |
| 1 | route:knowledge expected:['clarification', 'equipment', 'games', 'general'] |
| 1 | route:knowledge expected:['clarification', 'general', 'schedule'] |
| 1 | route:knowledge expected:['clarification', 'general', 'service_fee'] |
| 1 | route:no_answer expected:['general'] |
| 1 | route:reservation expected:['general', 'knowledge'] |
| 1 | silently_omitted_unknown_fee |
| 1 | validation errors: ['missing_requested_field:consequence', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions'] |
| 1 | validation errors: ['missing_requested_field:consequence', 'missing_requested_field:details'] |
| 1 | validation errors: ['missing_requested_field:deadline_minutes'] |
| 1 | validation errors: ['missing_requested_field:details', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:consequence'] |
| 1 | validation errors: ['missing_requested_field:details', 'missing_requested_field:topic', 'missing_requested_field:subject', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence'] |
| 1 | validation errors: ['missing_requested_field:platform', 'missing_requested_field:studio_supported'] |
| 1 | validation errors: ['missing_requested_field:players_max', 'missing_requested_field:players_min'] |
| 1 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:deadline_minutes', 'missing_requested_field:required_documents', 'missing_requested_field:steps', 'missing_requested_field:preconditions', 'missing_requested_field:outcome'] |
| 1 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:preconditions', 'missing_requested_field:steps', 'missing_requested_field:required_documents', 'missing_requested_field:deadline_minutes', 'missing_requested_field:outcome'] |
| 1 | validation errors: ['missing_requested_field:procedure_id', 'missing_requested_field:steps', 'missing_requested_field:preconditions', 'missing_requested_field:required_documents', 'missing_requested_field:deadline_minutes', 'missing_requested_field:outcome'] |
| 1 | validation errors: ['missing_requested_field:required_documents', 'missing_requested_field:deadline_minutes', 'missing_requested_field:outcome', 'missing_requested_field:steps', 'missing_requested_field:preconditions', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence', 'missing_requested_field:details'] |
| 1 | validation errors: ['missing_requested_field:required_documents', 'missing_requested_field:steps', 'missing_requested_field:preconditions', 'missing_requested_field:deadline_minutes', 'missing_requested_field:outcome'] |
| 1 | validation errors: ['missing_requested_field:required_documents'] |
| 1 | validation errors: ['missing_requested_field:topic', 'missing_requested_field:subject', 'missing_requested_field:decision', 'missing_requested_field:conditions_all', 'missing_requested_field:exceptions', 'missing_requested_field:consequence', 'missing_requested_field:details'] |
| 1 | validation errors: ['unresolved_query_clause', 'missing_requested_field:competition_id', 'missing_requested_field:section_number', 'missing_requested_field:facet', 'missing_requested_field:heading'] |
| 1 | validation errors: ['unresolved_query_clause', 'missing_requested_field:consequence'] |
| 1 | validation errors: ['unresolved_query_clause', 'missing_requested_field:details', 'missing_requested_field:consequence'] |
| 1 | ค่าปรับ |
| 1 | ตาราง Service Fee |
| 1 | พื้นที่ที่กำหนด |
| 1 | ยังไม่ได้เปิด |
| 1 | วันจันทร์ |
| 1 | เร่ง |
