# เหตุไม่ผ่านทุกชนิดจาก logs

เป็น literal reason ที่ evaluator บันทึก ไม่ใช่ root cause ทุกข้อความ เหตุเดียวเกิดได้หลายเกณฑ์ในคำถามเดียว

## ใหม่ R88 common ON

| เหตุ | Grade events |
|---|---:|
| route:knowledge expected:['games'] | 15212 |
| status:clarification expected:answer_available | 9557 |
| route:knowledge expected:['service_fee'] | 4221 |
| route:knowledge expected:['competition_rules'] | 4108 |
| route:knowledge expected:['reservation'] | 3747 |
| route:knowledge expected:['equipment'] | 2855 |
| route expected ['competition_rules'], got knowledge | 2376 |
| retrieval evidence did not match the allowed canonical fact/rule IDs | 2198 |
| route:knowledge expected:['reservation', 'schedule'] | 2010 |
| route:knowledge expected:['rules'] | 1895 |
| route:knowledge expected:['members', 'overview'] | 1691 |
| status:clarification expected:no_answer_expected | 1033 |
| route:knowledge expected:['games', 'reservation'] | 948 |
| route:knowledge expected:['penalty'] | 801 |
| route:knowledge expected:['schedule'] | 789 |
| first_line_off_topic | 704 |
| outcome expected answer_available, got clarification | 590 |
| status:answer expected:no_answer_expected | 582 |
| missing all alternatives: ['บาท', 'บาท', 'ฟรี'] | 576 |
| route:knowledge expected:['competition_rules', 'no_answer'] | 552 |
| route:knowledge expected:['equipment', 'games', 'multi_question', 'reservation'] | 468 |
| route_mismatch | 448 |
| route expected ['competition_rules', 'no_answer'], got knowledge | 416 |
| missing all alternatives: ['Nintendo Switch Zone'] | 416 |
| route:knowledge expected:['overview'] | 390 |
| route:knowledge expected:['multi_question'] | 368 |
| route:knowledge expected:['games', 'reservation', 'schedule'] | 368 |
| missing all alternatives: ['0 บาท', 'บาท', 'ฟรี'] | 360 |
| route:knowledge expected:['overview', 'rules'] | 354 |
| missing rulebook target(s): ['competition_rules_rov_blueket_2025_men'] | 351 |
| route:knowledge expected:['penalty', 'rules'] | 350 |
| route:knowledge expected:['no_answer', 'overview', 'rules'] | 348 |
| missing all alternatives: ['PlayStation 5 Zone'] | 332 |
| legacy_mode_prefix:['pipeline:structured_game_controls'] | 329 |
| status:clarification expected:localization_pending | 328 |
| outcome expected no_answer_expected, got answer | 307 |
| route:knowledge expected:['schedule', 'reservation'] | 284 |
| wrong_category | 280 |
| status:answer expected:clarification_required | 259 |
| route:knowledge expected:['no_answer'] | 241 |
| missing required: THB | 239 |
| route:knowledge expected:['games', 'no_answer'] | 238 |
| status:clarification expected:live_lookup_required | 236 |
| legacy_mode_prefix:['pipeline:competition_fact_card'] | 228 |
| route:knowledge expected:['rules', 'no_answer', 'clarification'] | 200 |
| route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification'] | 200 |
| route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee'] | 200 |
| route:knowledge expected:['clarification', 'service_fee'] | 200 |
| missing rulebook target(s): ['competition_rules_tekken8_psu_esports'] | 197 |
| route:knowledge expected:['equipment', 'games'] | 190 |
| route:knowledge expected:['contact'] | 182 |
| route:knowledge expected:['reservation', 'service_fee'] | 176 |
| status:answer expected:live_lookup_required | 174 |
| missing all alternatives: ['0 บาท', '0 บาท'] | 174 |
| missing required: Verified equipment | 170 |
| missing required: prohibited | 160 |
| route:knowledge expected:['contact', 'overview'] | 150 |
| missing all alternatives: ['PlayStation 5', 'PlayStation 5 #01-#02'] | 147 |
| missing all alternatives: ['Nintendo Switch', 'เล่นได้ที่'] | 146 |
| missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026'] | 130 |
| route:knowledge expected:['clarification', 'schedule'] | 130 |
| missing all alternatives: ['PC Zone'] | 130 |
| missing all alternatives: ['09:00', '13:00', '9:00', '1 pm'] | 128 |
| missing all alternatives: ['PlayStation 5', 'เล่นได้ที่'] | 128 |
| missing all alternatives: ['Nintendo Switch', 'Nintendo Switch (1-2 Persons)'] | 126 |
| route:knowledge expected:['clarification', 'equipment', 'games', 'no_answer', 'reservation', 'service_fee'] | 126 |
| missing required: Wednesday | 119 |
| missing required: 09:00-12:00 | 119 |
| missing required: 13:00-16:00 | 119 |
| missing required: Student ID | 118 |
| missing required: phone number | 118 |
| missing required: 30 minutes | 111 |
| missing all alternatives: ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก'] | 110 |
| outcome expected no_answer_expected, got clarification | 109 |
| route:knowledge expected:['multi_question', 'reservation', 'games', 'equipment'] | 102 |
| route:knowledge expected:['general', 'overview', 'home'] | 100 |
| missing all alternatives: ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด'] | 98 |
| missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible'] | 96 |
| route:knowledge expected:['equipment', 'rules'] | 96 |
| missing required: PC Zone | 93 |
| route:knowledge expected:['general', 'clarification', 'no_answer', 'overview'] | 91 |
| missing all alternatives: ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท'] | 90 |
| route:knowledge expected:['games', 'general', 'no_answer'] | 90 |
| missing all alternatives: ['Gaming Monitor', 'Gaming Monitors'] | 89 |
| route:knowledge expected:['equipment', 'game_controls'] | 88 |
| route:knowledge expected:['clarification', 'equipment'] | 87 |
| route:knowledge expected:['equipment', 'no_answer'] | 85 |
| source-gap no-answer attached evidence or did not abstain safely | 84 |
| missing required: VR Zone | 83 |
| route:knowledge expected:['general', 'no_answer', 'unknown'] | 78 |
| route:knowledge expected:['games', 'multi_question'] | 74 |
| route:input_guard expected:['clarification', 'general', 'no_answer', 'unknown'] | 74 |
| intent:common_read expected:service_fee_query | 73 |
| missing required: 2 sessions | 73 |
| route:knowledge expected:['clarification', 'competition_rules', 'general'] | 72 |
| missing required: 0 THB | 69 |
| status:clarification expected:safe_no_answer | 69 |
| route:knowledge expected:['clarification', 'games'] | 68 |
| route:knowledge expected:['clarification', 'games', 'no_answer'] | 66 |
| missing all alternatives: ['latency', 'หน่วง'] | 66 |
| missing all alternatives: ['VR Zone'] | 66 |
| intent:common_read expected:list | 65 |
| missing all alternatives: ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล'] | 64 |
| route:knowledge expected:['clarification', 'general', 'reservation'] | 64 |
| missing all alternatives: ['PC', 'เล่นได้ที่'] | 64 |
| missing all alternatives: ['VALORANT', 'Counter-Strike 2'] | 63 |
| route:knowledge expected:['games', 'service_fee'] | 62 |
| missing required: 0 บาท | 61 |
| missing required: English localization | 61 |
| missing all alternatives: ['เฟรม', 'ความละเอียด'] | 60 |
| missing all alternatives: ['server', 'client'] | 59 |
| missing rulebook target(s): ['competition_rules_valorant_psu_phuket_2026'] | 58 |
| missing all alternatives: ['GPU', 'กราฟิก'] | 57 |
| missing all alternatives: ['คีย์บอร์ด', 'mechanical'] | 57 |
| missing all alternatives: ['กิจกรรม'] | 55 |
| missing all alternatives: ['ขอบคุณ'] | 54 |
| missing all alternatives: ['API', 'เชื่อมต่อ'] | 54 |
| missing required: refund | 54 |
| missing required: not open 24 hours | 54 |
| missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา'] | 52 |
| legacy_mode_prefix:['pipeline:multi_question_splitter'] | 51 |
| intent:common_read expected:booking_policy | 51 |
| missing all alternatives: ['PC', 'PC #01-#02'] | 49 |
| legacy_mode_prefix:['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'] | 48 |
| missing required: No information | 46 |
| intent:common_read expected:schedule_query | 45 |
| intent:common_read expected:chatbot_greeting | 44 |
| route:knowledge expected:['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'] | 43 |
| missing required: psuesportspkt@gmail.com | 40 |
| missing all alternatives: ['ยังไม่แน่ใจ', 'ยังไม่พบ', 'ขอ', 'ไม่มี'] | 38 |
| missing all alternatives: ['พื้นที่ที่กำหนด', 'designated area'] | 38 |
| missing all alternatives: ['Call of Duty', 'หลายเกม', 'ยังไม่ชัด'] | 38 |
| route expected ['competition_rules', 'clarification'], got knowledge | 38 |
| legacy_english_thai_prose_flag | 37 |
| route:no_answer expected:['general', 'knowledge'] | 36 |
| intent:common_read expected:chatbot_identity | 36 |
| route:knowledge expected:['clarification', 'general', 'unknown'] | 36 |
| route:knowledge expected:['clarification', 'general', 'service_fee'] | 36 |
| missing required: 70 THB | 35 |
| missing required: Verified game catalog | 35 |
| route:knowledge expected:['games', 'clarification', 'no_answer'] | 33 |
| route:knowledge expected:['clarification', 'equipment', 'games', 'general'] | 32 |
| route:knowledge expected:['clarification', 'general', 'schedule'] | 30 |
| route:knowledge expected:['no_answer', 'games', 'general'] | 30 |
| missing required: Minecraft | 30 |
| missing required: There are currently 42 verified games available. | 30 |
| route:knowledge expected:['clarification', 'games', 'general'] | 30 |
| missing all alternatives: ['Cockpit Zone', 'PlayStation 5 Zone'] | 28 |
| missing required: College of Computing | 28 |
| outcome_mismatch | 27 |
| route:knowledge expected:['clarification', 'reservation'] | 26 |
| missing all alternatives: ['Gaming PC รุ่น MSI MAG Infinite S3 14th'] | 26 |
| quality_score_or_required_gate_failed | 25 |
| missing required: esports learning development studio | 25 |
| route:knowledge expected:['games', 'clarification'] | 24 |
| status:no_answer expected:answer_available | 23 |
| missing all alternatives: ['PC Zone', 'PlayStation 5 Zone'] | 22 |
| missing required: Example Quest | 21 |
| missing all alternatives: ['TV 86 นิ้ว'] | 21 |
| missing all alternatives: ['TV 65 นิ้ว'] | 20 |
| wrong_game_evidence | 20 |
| missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026', 'competition_rules_valorant_psu_phuket_2026'] | 20 |
| missing all alternatives: ['Overcooked! 2', 'ยังไม่พบข้อมูลปุ่ม', 'ไม่มีข้อมูลปุ่ม'] | 20 |
| missing required: 50 บาท | 20 |
| missing all alternatives: ['ไม่ได้', 'ไม่พบ', 'closed', 'weekend', 'not open'] | 20 |
| missing all alternatives: ['VR', 'เล่นได้ที่'] | 20 |
| route:knowledge expected:['clarification', 'competition_rules'] | 18 |
| missing all alternatives: ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง'] | 18 |
| missing all alternatives: ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 18 |
| route:reservation expected:['no_answer'] | 18 |
| missing required: not connected | 18 |
| missing all alternatives: ['PlayStation Zone', 'อุปกรณ์'] | 18 |
| missing all alternatives: ['Gaming Mouse'] | 16 |
| route:knowledge expected:['general', 'unknown', 'no_answer'] | 16 |
| intent:common_read expected:social_thanks | 16 |
| route:input_guard expected:['general', 'unknown', 'clarification', 'no_answer'] | 16 |
| status:answer expected:safe_clarification | 16 |
| route:knowledge expected:['overview', 'members'] | 16 |
| route:knowledge expected:['competition_rules', 'general', 'clarification'] | 16 |
| missing all alternatives: ['Sofa 2 seats'] | 15 |
| missing required: 190 บาท | 15 |
| intent:common_read expected:studio_rules | 14 |
| missing all alternatives: ['Gaming Monitor'] | 14 |
| intent:common_read expected:game_control_lookup | 14 |
| route:knowledge expected:['equipment', 'clarification'] | 14 |
| missing rulebook target(s): ['competition_rules_rov_blueket_2025_men', 'competition_rules_tekken8_psu_esports'] | 14 |
| legacy_mode_prefix:['pipeline:structured_game_controls_no_current_game', 'pipeline:no_answer'] | 14 |
| intent:common_read expected:equipment_item_lookup | 14 |
| missing all alternatives: ['Pulse Elite Wireless Headset'] | 14 |
| missing all alternatives: ['Sony PlayStation VR2'] | 14 |
| missing all alternatives: ['Gaming Keyboard'] | 14 |
| missing all alternatives: ['Racezone Full Cockpit V3'] | 14 |
| intent:common_read expected:detail | 13 |
| missing_complete_clause:Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid. | 13 |
| missing all alternatives: ['Driving Force Shifter'] | 13 |
| missing required: 25 บาท | 12 |
| missing all alternatives: ['Nintendo Switch OLED'] | 12 |
| missing all alternatives: ['PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive'] | 12 |
| missing all alternatives: ['Logitech G923 TRUEFORCE Racing Wheel'] | 12 |
| missing all alternatives: ['Gaming Headset'] | 12 |
| missing all alternatives: ['Gaming Chair'] | 12 |
| intent:common_read expected:game_availability_lookup | 11 |
| missing all alternatives: ['PC #03-#10', 'PC', 'Call of Duty'] | 11 |
| missing all alternatives: ['TV 65 นิ้ว', 'TV 65-inch'] | 10 |
| missing_complete_clause:Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only. | 10 |
| missing all alternatives: ['Cockpit', 'เล่นได้ที่'] | 10 |
| missing required: Nintendo Switch Sports | 10 |
| wrong_outcome:answer | 10 |
| missing all alternatives: ['Call of Duty: Modern Warfare III', 'Delta Force', 'EA Sports FC 24', '60'] | 10 |
| missing all alternatives: ['1-5 คน', 'คน'] | 10 |
| missing all alternatives: ['VR', 'VR Station 30 นาที'] | 10 |
| intent:common_read expected:how_to | 10 |
| missing_complete_clause:Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset. | 10 |
| missing all alternatives: ['TEKKEN 8', 'Counter-Strike 2', 'League of Legends', '60'] | 10 |
| route:knowledge expected:['schedule', 'reservation', 'clarification'] | 10 |
| missing required: 2026-09-25 | 10 |
| missing all alternatives: ['13:00', 'maintenance', 'Maintenance'] | 10 |
| missing required: 65 บาท | 10 |
| missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่'] | 9 |
| route:knowledge expected:['no_answer', 'service_fee'] | 9 |
| missing all alternatives: ['PC', 'PC #03-#10'] | 9 |
| missing all alternatives: ['Pokémon Champions', 'Animal Crossing: New Horizons', 'It Takes Two'] | 9 |
| missing all alternatives: ['Call of Duty: Modern Warfare III', 'Delta Force', 'EA Sports FC 24'] | 9 |
| missing_complete_clause:No scripts or macros are allowed at all. | 9 |
| route:reservation expected:['clarification', 'equipment'] | 9 |
| missing all alternatives: ['TEKKEN 8', 'Counter-Strike 2', 'League of Legends'] | 9 |
| missing all alternatives: ['1-2 คน', 'คน'] | 9 |
| pipeline_exception | 8 |
| route:knowledge expected:['schedule', 'general', 'clarification'] | 8 |
| intent:common_read expected:social_farewell | 8 |
| missing all alternatives: ['Right Mouse Button', 'ยิง/เล็งแบบรอง'] | 8 |
| legacy_mode_prefix:['pipeline:structured_game_controls_no_data', 'pipeline:no_answer', 'pipeline:answer_contract_no_answer'] | 8 |
| missing required: PlayStation 5 Zone | 8 |
| route:knowledge expected:['service_fee', 'games'] | 8 |
| route:knowledge expected:['general', 'reservation', 'clarification'] | 8 |
| route:knowledge expected:['rules', 'overview', 'no_answer'] | 8 |
| route:knowledge expected:['rules', 'overview'] | 8 |
| route:knowledge expected:['reservation', 'general', 'clarification'] | 8 |
| route:knowledge expected:['general', 'unknown', 'clarification'] | 8 |
| route:knowledge expected:['clarification', 'no_answer', 'service_fee'] | 8 |
| route:knowledge expected:['service_fee', 'general', 'clarification'] | 8 |
| route:knowledge expected:['equipment', 'games', 'general', 'clarification'] | 8 |
| route:knowledge expected:['schedule', 'clarification'] | 8 |
| route:knowledge expected:['games', 'general', 'clarification'] | 8 |
| missing all alternatives: ['Pokémon Champions', 'Animal Crossing: New Horizons', 'It Takes Two', '60'] | 8 |
| intent:common_read expected:social_apology | 8 |
| missing all alternatives: ['Super Smash Bros. Ultimate', 'ปุ่ม', 'จอย', 'คอนโทรล'] | 8 |
| missing all alternatives: ['Gran Turismo 7', '60'] | 8 |
| missing all alternatives: ['Left Mouse Button', 'Fire'] | 8 |
| missing all alternatives: ['Left Mouse Button', 'ยิง'] | 8 |
| missing all alternatives: ['The Last of Us Part II (Remastered)', 'PlayStation / PS5'] | 8 |
| missing_complete_clause:5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers. | 7 |
| missing_complete_clause:4.2.1. All participants must have at least 18 heroes for the "5v5" mode (formerly known as Tournament Mode). | 7 |
| missing_complete_clause:การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0 | 7 |
| missing_complete_clause:Assist buttons or special assist systems are allowed | 7 |
| missing_complete_clause:The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs. | 7 |
| missing_complete_clause:3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้ | 7 |
| route:knowledge expected:['rules', 'penalty'] | 7 |
| missing_complete_clause:4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay. | 7 |
| missing_complete_clause:If a forfeit is imposed, the result for that map is recorded as 13-0. | 7 |
| missing_complete_clause:No team member changes are allowed during the competition period | 7 |
| missing_complete_clause:New agents may not be used for approximately 2 weeks after release in Competitive mode. | 7 |
| missing_complete_clause:New maps may not be used for approximately 4 weeks after release in Competitive mode. | 7 |
| route:reservation expected:['multi_question'] | 7 |
| missing_complete_clause:Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must hand them to the referees before every match. | 7 |
| missing_complete_clause:If a bug occurs before either side deals damage, officials may roll back the round. | 7 |
| missing_complete_clause:If damage has already been dealt, no rollback is allowed unless through the Challenge process. | 7 |
| missing_complete_clause:4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game. | 7 |
| missing_complete_clause:4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate. | 7 |
| missing_complete_clause:Round time: 1:55 minutes / Freeze time: 15 seconds | 7 |
| missing_complete_clause:Personnel: During Match Prep, no more than 6 players may be present. | 6 |
| missing_complete_clause:2 requests per map during regulation (first 24 rounds), 60 seconds each. | 6 |
| missing all alternatives: ['Gaming Mouse', 'Gaming Mouse'] | 6 |
| missing_complete_clause:Initial money: $800 / Bomb time: 40 seconds | 6 |
| missing_complete_clause:Overtime: 3 rounds per side (6 rounds total). The first team to win 4 of the 6 rounds wins. Starting money is $10,000, and overtime may be played without limit. | 6 |
| missing_complete_clause:Food and drinks: Only drinking water in sealed containers and chewing gum are permitted. | 6 |
| intent:common_read expected:multi_question_split | 6 |
| missing_complete_clause:4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side. | 6 |
| missing_complete_clause:4.2.2. Use Global Ban/Pick hero selection. | 6 |
| missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification. | 6 |
| missing_complete_clause:Watching streams: Players are prohibited from watching live streams during competition. | 6 |
| missing_complete_clause:4.1.4. If a team starts the match more than 15 minutes after the scheduled time, the delayed team will be immediately forfeited. | 6 |
| missing all alternatives: ['L3 (Click Left Stick)', 'Look at'] | 6 |
| missing all alternatives: ['Cockpit Zone'] | 6 |
| missing required: Super Smash Bros. Ultimate | 6 |
| missing_complete_clause:4. Do not install your own software on the provided computers. | 6 |
| route:knowledge expected:['clarification', 'no_answer'] | 6 |
| missing_complete_clause:1. โหมด Competitive (5v5) | 6 |
| missing_complete_clause:Players are responsible for the quality and readiness of their own equipment. | 6 |
| missing_complete_clause:Match schedule: The tournament bracket will be announced at least 1 day in advance. Entry must be confirmed before the match starts. Late arrivals may be disqualified. | 6 |
| missing_complete_clause:Macros (both software- and hardware-based) are strictly prohibited. | 6 |
| missing_complete_clause:No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.) | 6 |
| missing all alternatives: ["Luigi's Mansion 3"] | 6 |
| missing all alternatives: ['Touch Pad', 'สัมภาระ / เมนูกระเป๋าเก็บของ'] | 6 |
| missing_complete_clause:Judgment authority: The referees' decisions and the organizers' rulings are final. The organizing side reserves the right to amend rules as appropriate for fairness. | 6 |
| missing_complete_clause:During preparation phase, the number of personnel shall not exceed 6 players. | 6 |
| missing_complete_clause:Abilities must not be used outside map boundaries to obtain information or an advantage. | 6 |
| missing_complete_clause:4.2.3. Runes and enhancement systems may be used as desired. | 6 |
| missing all alternatives: ['L (Left Stick)', 'Move'] | 6 |
| missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor. | 6 |
| missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping. | 6 |
| missing_complete_clause:No use of bugs or glitches that provide an advantage | 6 |
| intent:common_read expected:members_lookup | 6 |
| missing all alternatives: ['Right Mouse Button', 'Alternate Fire'] | 6 |
| missing_complete_clause:Advantage: No advantage | 6 |
| missing_complete_clause:Stage: Random | 6 |
| missing all alternatives: ['Call of Duty: Warzone', 'PC #03-#10'] | 5 |
| intent:common_read expected:penalty_policy | 5 |
| missing required: 375 บาท | 5 |
| missing all alternatives: ['Call of Duty: Modern Warfare III คือเกมยิงมุมมองบุคคลที่หนึ่งที่เน้นภารกิจและการยิงต่อสู้แบบรวดเร็ว'] | 5 |
| missing all alternatives: ['R (Right Stick)', 'มุมกล้อง'] | 5 |
| outcome expected clarification_required, got answer | 5 |
| missing all alternatives: ['Beat Saber', 'Horizon Call of the Mountain', 'Resident Evil 4'] | 5 |
| missing all alternatives: ['TEKKEN 8', 'PC #01-#02'] | 5 |
| missing all alternatives: ['Nintendo Switch (1-2 Persons)', 'Nintendo Switch', 'Overcooked! 2'] | 5 |
| missing all alternatives: ['Gran Turismo 7'] | 5 |
| missing all alternatives: ['Cockpit', 'Cockpit #01-#02'] | 5 |
| missing all alternatives: ['1-4 คน', 'คน'] | 5 |
| missing all alternatives: ['L3 (Click Left Stick)', 'หันมองจุดสนใจ'] | 4 |
| missing all alternatives: ['Circle', 'ย่อตัว / หมอบคลาน'] | 4 |
| missing all alternatives: ['Options', 'หยุดเกม'] | 4 |
| missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ'] | 4 |
| missing all alternatives: ['R3 (Click Right Stick)', 'ไฟฉาย'] | 4 |
| missing all alternatives: ['L1', 'หลบหลีก'] | 4 |
| missing all alternatives: ['R2', 'Shoot (While aiming) / Reload'] | 4 |
| missing all alternatives: ['R (Right Stick)', 'Camera'] | 4 |
| intent:common_read expected:social_ack | 4 |
| missing all alternatives: ['R1', 'Listen mode (Hold) / Switch Weapon'] | 4 |
| missing all alternatives: ['Triangle', 'Interact'] | 4 |
| missing all alternatives: ['Cross', 'Jump'] | 4 |
| missing all alternatives: ['L1', 'Dodge'] | 4 |
| missing all alternatives: ['Touch Pad', 'Inventory'] | 4 |
| missing all alternatives: ['R3 (Click Right Stick)', 'Flashlight'] | 4 |
| missing all alternatives: ['L2', 'Aim (Hold)'] | 4 |
| missing all alternatives: ['R1', 'โหมดฟังเสียง (กดค้าง) / สลับอาวุธด่วน'] | 4 |
| missing all alternatives: ['Cross', 'กระโดด'] | 4 |
| missing all alternatives: ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 4 |
| missing all alternatives: ['L2', 'เล็งเป้า (กดค้าง)'] | 4 |
| missing all alternatives: ['Square', 'Melee'] | 4 |
| missing all alternatives: ['Square', 'โจมตีประชิด'] | 4 |
| missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอุปกรณ์ด่วน'] | 4 |
| missing all alternatives: ['Circle', 'Crouch'] | 4 |
| missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Tool selection (Up / Down / Left / Right)'] | 4 |
| missing all alternatives: ['Options', 'Pause'] | 4 |
| missing all alternatives: ['Right Mouse Button', 'Secondary Fire'] | 4 |
| missing all alternatives: ['R2', 'ยิงปืน (ขณะเล็ง) / รีโหลดกระสุน'] | 4 |
| missing_complete_clause:Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception. | 3 |
| missing_complete_clause:Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception. | 3 |
| missing_complete_clause:General eligibility: Open only to students currently enrolled at Prince of Songkla University, Phuket Campus. | 3 |
| latency_ceiling | 3 |
| missing_complete_clause:Check-in: arrive at least 30 minutes before the scheduled match time. | 3 |
| missing_complete_clause:Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time. | 3 |
| missing_complete_clause:Registration of players is not permitted after the registration period has closed. | 3 |
| route:knowledge expected:['no_answer', 'games'] | 3 |
| missing_complete_clause:Players may compete under only one team. | 3 |
| intent:common_read expected:group_count | 3 |
| missing_complete_clause:If any member withdraws, the team may be disqualified. | 3 |
| missing_complete_clause:4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally. | 3 |
| missing_complete_clause:Referees may reconsider decisions as appropriate to ensure fairness. | 3 |
| missing_complete_clause:Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited. | 3 |
| route:knowledge expected:['general'] | 3 |
| missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited. | 3 |
| missing_complete_clause:In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over. | 3 |
| missing_complete_clause:4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion. | 3 |
| missing_complete_clause:Side selection: a knife round is used to choose sides. | 3 |
| missing_complete_clause:PlayStation 5 console used | 3 |
| missing_complete_clause:Using teammates to jump higher than the normal jump range is prohibited. | 3 |
| missing required: 150 บาท | 3 |
| missing_complete_clause:Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees. | 3 |
| missing_complete_clause:4.2.5. Regarding skins, only Default skins may be used. | 3 |
| missing_complete_clause:Allowed keyboard technology: Snap Tap, SOCD, or equivalent technologies, unless otherwise instructed by officials. | 3 |
| missing required: 3 sessions | 3 |
| missing_complete_clause:Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket. | 3 |
| missing_complete_clause:One request per map is allowed. | 3 |
| missing_complete_clause:Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute. | 3 |
| route:knowledge expected:['clarification'] | 3 |
| missing_complete_clause:3.1. Offline Mode | 3 |
| missing_complete_clause:3.2. Each round played as Best of 3 (BO3) | 3 |
| missing_complete_clause:Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match. | 3 |
| missing_complete_clause:Any character can be selected (except DLC characters) | 3 |
| missing_complete_clause:In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice. | 3 |
| missing_complete_clause:4.4.3. A 5-minute break follows every two games. | 3 |
| missing required: Key studio rules | 3 |
| missing_complete_clause:Turn OFF Blood and Bodies displays. Displaying FPS or Latency graphs during competition is prohibited. | 3 |
| missing_complete_clause:Used when there are device malfunctions, disconnections, or software issues | 3 |
| intent:common_read expected:game_detail_lookup | 3 |
| missing all alternatives: ['General Adult', '0 บาท'] | 3 |
| missing_complete_clause:Maximum of 24 rounds (12 rounds per side). The winner is the first team to win 13 rounds. | 3 |
| missing_complete_clause:จำนวนรอบต่อเกม (Round): 3 | 3 |
| missing_complete_clause:เวลาแข่งขันต่อรอบ (Timer): 60 วินาที | 3 |
| missing_complete_clause:If tied at 1-1, a deciding game will be played | 3 |
| missing_complete_clause:5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification. | 3 |
| missing_complete_clause:Rounds per game (Round): 3 | 3 |
| missing_complete_clause:Time per round (Timer): 60 seconds | 3 |
| missing_complete_clause:4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game. | 3 |
| missing_complete_clause:Semifinals and finals: Best of 3 (BO3) | 3 |
| missing all alternatives: ['Fortnite'] | 2 |
| intent:common_read expected:competition_rules_lookup | 2 |
| missing required: permission | 2 |
| intent:common_read expected:competition_game_list | 2 |
| missing all alternatives: ['นายชนะชัย สิริพันธ์วราภรณ์', 'ผู้จัดการ'] | 2 |
| missing required: alcohol consumption | 2 |
| intent:common_read expected:general_knowledge_query | 2 |
| missing all alternatives: ['นายนพัทธ์ ฝอยทอง', 'รองประธาน'] | 2 |
| missing required: Tekken 8 ราคาเท่าไหร่ | 2 |
| route:knowledge expected:['no_answer', 'reservation', 'schedule'] | 2 |
| missing all alternatives: ['Moving Out 2'] | 2 |
| missing required: 10 minutes | 2 |
| missing all alternatives: ['ไม่มี', 'PC #03-#10'] | 2 |
| missing all alternatives: ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 2 |
| missing all alternatives: ['เก็บอาวุธ เคลื่อนตามวง ต่อสู้กับผู้เล่นอื่น และใช้การสร้างหรือโหมดไม่สร้างตามรูปแบบที่เลือก'] | 2 |
| missing required: บุคคลทั่วไป | 2 |
| missing all alternatives: ['Mario Party Superstars'] | 2 |
| missing all alternatives: ['Beat Saber'] | 2 |
| missing required: PS5 ราคาเท่าไหร่ | 2 |
| legacy_mode_prefix:['pipeline:ambiguity_clarification'] | 2 |
| intent:common_read expected:ambiguity_gate_clarification | 2 |
| route:knowledge expected:['clarification', 'multi_question'] | 2 |
| missing all alternatives: ['League of Legends'] | 2 |
| missing all alternatives: ['New Super Mario Bros. U Deluxe'] | 2 |
| route:input_guard expected:['general', 'clarification', 'no_answer', 'overview'] | 2 |
| route:input_guard expected:['general', 'clarification', 'no_answer', 'overview', 'knowledge'] | 2 |
| route:knowledge expected:['equipment', 'games', 'multi_question', 'reservation', 'service_fee'] | 2 |
| silently_omitted_unknown_fee | 2 |
| missing required: บาท | 2 |
| PC Zone | 2 |
| PlayStation 5 Zone | 2 |
| Nintendo Switch Zone | 2 |
| VR Zone | 2 |
| missing all alternatives: ['God of War Ragnarok'] | 2 |
| missing all alternatives: ['Mario Kart 8 Deluxe'] | 2 |
| missing all alternatives: ['It Takes Two คือเกมผจญภัยสำหรับเล่นร่วมกันสองคน ที่ต้องช่วยกันแก้ปริศนาและผ่านด่าน'] | 2 |
| missing all alternatives: ['นายปัณณวิชญ์ หนูเรือง', 'เลขานุการ'] | 2 |
| missing required: 140 บาท | 2 |
| missing required: 2 session | 2 |
| missing all alternatives: ['เล่นตามเนื้อเรื่อง ต่อสู้ด้วยสกิล/คอมโบ ทำภารกิจ และพัฒนาความสามารถของตัวละคร'] | 2 |
| missing required: 70 บาท | 2 |
| missing all alternatives: ['Animal Crossing: New Horizons'] | 2 |
| missing required: designated areas | 2 |
| missing all alternatives: ['Counter-Strike 2'] | 2 |
| missing all alternatives: ['PUBG: BATTLEGROUNDS คือเกมเอาชีวิตรอดที่ผู้เล่นลงสนาม ค้นหาอาวุธและอุปกรณ์ แล้วพยายามอยู่รอดเป็นคนหรือทีมสุดท้าย'] | 2 |
| wrong_outcome:clarification | 2 |
| legacy_mode_prefix:['pipeline:structured_game_detail'] | 2 |
| missing all alternatives: ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 2 |
| missing all alternatives: ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 2 |
| missing all alternatives: ['The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ'] | 1 |
| missing all alternatives: ['นายภูจิตร', 'เหรัญญิก'] | 1 |
| 0 บาท | 1 |
| missing required: Tomorrow | 1 |
| missing required: Siam Commercial Bank | 1 |
| missing required: 795-276244-1 | 1 |
| missing required: PS5 มีเกมอะไรบ้าง | 1 |
| ตาราง Service Fee | 1 |
| missing required: power outlets | 1 |
| 3-4 Persons | 1 |
| missing all alternatives: ['R1', 'เปิดใช้งาน Heat'] | 1 |
| missing all alternatives: ['นายณภัทร เชื้อเหล่าวานิช', 'นักศึกษาสหกิจ Game and 3D Developer'] | 1 |
| missing required: Public visitors can book | 1 |
| missing all alternatives: ['R2', 'Heavy Attack / Heavy Runic Attack (While blocking)'] | 1 |
| missing all alternatives: ['นายพฤทธิ์ เกษตรสมบูรณ์', 'นักวิชาการคอมพิวเตอร์'] | 1 |
| missing required: ต้องเช็กอินครับ | 1 |
| missing required: 30 นาที | 1 |
| missing required: does not separately confirm whether carrying alcohol | 1 |
| missing required: Tekken 8 มีปุ่มอะไรบ้าง | 1 |
| missing required: TEKKEN 8 มีข้อมูลปุ่ม | 1 |
| missing required: Square | 1 |
| missing required: Mario มีปุ่มอะไรบ้าง | 1 |
| missing all alternatives: ['Options', 'Open game menu'] | 1 |
| missing all alternatives: ['นายปัณณวิชญ์', 'เลขานุการ'] | 1 |
| missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Weapon Cross (Up / Down / Left / Right)'] | 1 |
| missing required: does not confirm whether a visit just to look around is free | 1 |
| missing all alternatives: ['รศ.ดร.พันธ์', 'รองอธิการบดี'] | 1 |
| missing required: ต้องจองผ่านระบบก่อน | 1 |
| missing required: เลือกบริการหรือโซน | 1 |
| missing required: เลือกวันและรอบเวลา | 1 |
| missing required: ขออนุญาต | 1 |
| Local LLM | 1 |
| ยังไม่ได้เปิด | 1 |
| missing required: Public visitors | 1 |
| missing all alternatives: ['D-Pad Left / Right', 'สลับเครื่องมือ'] | 1 |
| missing required: พื้นที่ที่ศูนย์กำหนด | 1 |
| legacy_mode_prefix:['pipeline:structured_booking_game_service_selection'] | 1 |
| missing all alternatives: ['แนวเกม', 'เกม Battle Royale'] | 1 |
| missing all alternatives: ['God of War Ragnarok คือเกมแอ็กชันผจญภัยที่เน้นเนื้อเรื่อง การต่อสู้ และการสำรวจในโลกตำนานนอร์ส'] | 1 |
| missing required: Nintendo Switch | 1 |
| missing required: PC Zone มีอุปกรณ์อะไร | 1 |
| missing_conflict_notice | 1 |
| missing all alternatives: ['จอง'] | 1 |
| missing all alternatives: ['R1 + Circle', 'ยิงปั่นโค้ง'] | 1 |
| missing all alternatives: ['Ctrl', 'Walk'] | 1 |
| missing required: ยังยืนยันไม่ได้ว่าเล่นได้ทุกเกม | 1 |
| missing required: General Student | 1 |
| missing required: จะเล่น Tekken 8 ต้องจองยังไง | 1 |
| route:input_guard expected:['equipment', 'no_answer'] | 1 |
| missing_complete_clause:1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket | 1 |
| missing all alternatives: ['รศ.ดร.พันธ์ ทองชุมนุม', 'รองอธิการบดี'] | 1 |
| missing all alternatives: ['Touch Pad', 'แผนที่'] | 1 |
| missing required: โดยไม่จองล่วงหน้าไม่ได้ | 1 |
| missing required: 1 ชั่วโมง | 1 |
| missing required: ต่างกันดังนี้ | 1 |
| missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท | 1 |
| missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท | 1 |
| missing all alternatives: ['Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย'] | 1 |
| missing required: สมัครสมาชิก | 1 |
| missing required: National ID | 1 |
| wrong_game_source | 1 |
| missing required: Which service | 1 |
| missing required: ใช้บัตรประชาชน | 1 |
| missing all alternatives: ['PlayStation 5 Zone / VR Zone'] | 1 |
| missing required: ขอรู้บริการหรือโซนก่อน | 1 |
| missing required: 4.8 | 1 |
| missing all alternatives: ['R1 / R2', 'Grab'] | 1 |
| missing all alternatives: ['Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง'] | 1 |
| missing required: does not establish access to every game | 1 |
| 100-500 | 1 |
| 500-2,000 | 1 |
| missing all alternatives: ['New Super Mario Bros. U Deluxe คือเกมมาริโอแบบเดินลุยด่าน กระโดด หลบศัตรู และเก็บเหรียญ'] | 1 |
| วันจันทร์ | 1 |
| 09:00-12:00 | 1 |
| 13:00-16:00 | 1 |
| missing all alternatives: ['Resident Evil 4 คือเกมเอาตัวรอดสยองขวัญที่เน้นการต่อสู้ การสำรวจ และการบริหารกระสุน/ไอเทม'] | 1 |
| missing_complete_clause:4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) / ผู้ชนะคือทีมที่ได้ 13 รอบก่อน | 1 |
| missing all alternatives: ['ขอ', 'เกม', 'ปุ่ม', 'ยังไม่'] | 1 |
| missing all alternatives: ['Beat Saber', 'Horizon Call of the Mountain', 'Resident Evil 4', '30'] | 1 |
| missing all alternatives: ['Little Nightmares II คือเกมผจญภัยบรรยากาศสยองที่เน้นการหลบหนี แก้ปริศนา และผ่านฉากอันตราย'] | 1 |
| missing required: คำตอบ: | 1 |
| missing required: you may bring | 1 |
| missing all alternatives: ['Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม'] | 1 |
| รอบเวลา | 1 |
| missing required: คำถามนี้ยังกว้างเกินไป | 1 |
| missing required: มีเกมอะไรบ้าง | 1 |
| missing required: มีอุปกรณ์อะไรบ้าง | 1 |
| missing required: ราคา PS5 เท่าไหร่ | 1 |
| missing all alternatives: ['ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา'] | 1 |
| missing all alternatives: ['L1', 'ยกการ์ด / ป้องกัน'] | 1 |
| missing required: full compensation | 1 |
| missing all alternatives: ['เล่นแบบสบาย ๆ โดยเก็บทรัพยากร ตกปลา จับแมลง ตกแต่งเกาะ และทำกิจกรรมประจำวัน'] | 1 |
| missing required: Booking steps | 1 |
| missing required: upload the payment slip | 1 |
| missing required: cannot confirm that this gaming station | 1 |
| missing required: ไม่รับผิดชอบ | 1 |
| missing required: ห้าม | 1 |
| missing required: แอลกอฮอล์ | 1 |
| missing required: returned after use | 1 |
| missing all alternatives: ['F', 'โต้ตอบ'] | 1 |
| Gaming PC | 1 |
| Cockpit Zone | 1 |
| route:reservation expected:['equipment', 'clarification'] | 1 |
| VR 30 นาที | 1 |
| 525 บาท | 1 |
| VR 1 ชั่วโมง | 1 |
| 1,050 บาท | 1 |
| missing all alternatives: ['TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง'] | 1 |
| intent:common_read expected:count | 1 |
| missing required: TEKKEN 8 ไม่มีราคาแยกตามชื่อเกม | 1 |
| legacy_mode_prefix:['pipeline:structured_service_fee_by_game'] | 1 |
| missing all alternatives: ['เล็ง ยิง เคลื่อนที่ ใช้อุปกรณ์ และทำ objective ของโหมดเกมหรือภารกิจให้สำเร็จ'] | 1 |
| missing required: Overcooked | 1 |
| missing required: Overcooked! 2 | 1 |
| missing required: Nintendo Switch Zone | 1 |
| legacy_mode_prefix:['pipeline:structured_games_family'] | 1 |
| missing all alternatives: ['EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล'] | 1 |
| 150 บาท | 1 |
| route:input_guard expected:['schedule'] | 1 |
| intent:keyboard_layout_mismatch expected:schedule_query | 1 |
| missing required: PS5 มีเกมอะไร | 1 |
| missing required: PlayStation 5 Zone และ Nintendo Switch Zone มีเกมเยอะสุด | 1 |
| missing required: 17 เกม | 1 |
| legacy_mode_prefix:['pipeline:structured_game_zone_ranking'] | 1 |
| Logitech G923 | 1 |
| Driving Force Shifter | 1 |
| missing required: 10 นาที | 1 |
| missing all alternatives: ["Marvel's Spider-Man 2 คือเกมแอ็กชันผจญภัยที่ผู้เล่นรับบท Spider-Man ต่อสู้กับศัตรูและสำรวจเมือง"] | 1 |
| missing required: PC 1 ชั่วโมง | 1 |
| missing required: local service fee update 2026-07-27 | 1 |
| legacy_mode_prefix:['pipeline:deterministic_calculator_fast'] | 1 |
| missing all alternatives: ['L (Left Stick)', 'เลี้ยว / ควบคุมทิศทาง'] | 1 |
| 3 หมวด | 1 |
| missing all alternatives: ['Head/body movement', 'หลบและจัดตำแหน่งร่างกาย'] | 1 |
| Intel Core i5-14400 | 1 |
| DDR5 32GB | 1 |
| RTX 5060 | 1 |
| missing required: Intel Core i5-14400 | 1 |
| missing required: DDR5 32GB | 1 |
| missing required: RTX 5060 | 1 |
| missing all alternatives: ['นายสุพศิน อะนะฝรั่ง', 'นักศึกษาสหกิจ Web & AI Developer'] | 1 |
| missing required: 100-500 THB | 1 |
| missing all alternatives: ['แนวเกม', 'เกมยิง Tactical FPS'] | 1 |
| missing all alternatives: ['Button controls', 'เล่นบอร์ดและมินิเกมด้วยปุ่ม'] | 1 |
| missing required: Tekken 8 เล่นที่ไหน | 1 |
| missing required: Tekken 8 มีปุ่มอะไร | 1 |
| นายณภัทร เชื้อเหล่าวานิช | 1 |
| Game and 3D Developer | 1 |
| missing required: No, you cannot use the studio without booking first | 1 |
| missing required: one hour | 1 |
| missing all alternatives: ["Luigi's Mansion 3 คือเกมผจญภัยจับผีที่ผู้เล่นสำรวจโรงแรมและแก้ปริศนา"] | 1 |
| missing all alternatives: ['FINAL FANTASY XVI คือเกมแอ็กชัน RPG แฟนตาซีที่เน้นเนื้อเรื่อง การต่อสู้ และการพัฒนาตัวละคร'] | 1 |
| missing required: เกมต่อสู้ | 1 |
| missing all alternatives: ['นายภูจิตร จิรวิริยาภรณ์', 'เหรัญญิก'] | 1 |
| missing required: cannot confirm permission to remove this equipment | 1 |
| missing all alternatives: ['นายธนชาติ เอ่งฉ้วน', 'ประชาสัมพันธ์'] | 1 |
| PSU Esports Assistant | 1 |
| missing all alternatives: ['X', 'Horn'] | 1 |
| missing all alternatives: ['นายภาสวุฒิ ชูติประชากิจ', 'นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer'] | 1 |
| missing required: ดูเฉย ๆ | 1 |
| missing required: ยังไม่พบข้อมูลยืนยัน | 1 |
| missing required: ห้ามพูดจาดูหมิ่น | 1 |
| missing required: วิธีเล่นโดยสรุป | 1 |
| missing required: ไม่พบข้อมูล | 1 |
| intent:common_read expected:guard_no_answer | 1 |
| missing all alternatives: ['L1', 'ใช้อุปกรณ์ยุทธวิธี'] | 1 |
| ยังไม่พบ | 1 |
| Minecraft | 1 |
| 2 ชั่วโมง | 1 |
| 2 session | 1 |
| 09:00-10:00 | 1 |
| 10:00-11:00 | 1 |
| missing required: ไม่ได้ยืนยันสิทธิ์ยืมอุปกรณ์กลับบ้าน | 1 |
| missing required: 2 ชั่วโมง | 1 |
| missing required: 70 บาท/session | 1 |

## เดิม R64 legacy ON

| เหตุ | Grade events |
|---|---:|
| pipeline_exception | 5894 |
| route:game_controls expected:['games'] | 2702 |
| status:no_answer expected:answer_available | 694 |
| status:clarification expected:answer_available | 602 |
| route:service_fee expected:['equipment', 'games', 'multi_question', 'reservation'] | 400 |
| route:schedule expected:['reservation'] | 306 |
| legacy_mode_prefix:['pipeline:structured_game_controls'] | 222 |
| status:answer expected:clarification_required | 161 |
| status:answer expected:no_answer_expected | 151 |
| status:no_answer expected:localization_pending | 130 |
| route:no_answer expected:['general', 'knowledge'] | 102 |
| legacy_mode_prefix:['pipeline:competition_fact_card'] | 97 |
| route:clarification expected:['service_fee'] | 96 |
| route:knowledge expected:['general', 'overview', 'home'] | 95 |
| route:contact expected:['competition_rules'] | 93 |
| retrieval evidence did not match the allowed canonical fact/rule IDs | 89 |
| status:clarification expected:no_answer_expected | 88 |
| route:service_fee expected:['multi_question', 'reservation', 'games', 'equipment'] | 86 |
| route:input_guard expected:['clarification', 'general', 'no_answer', 'unknown'] | 74 |
| missing required: 2 sessions | 72 |
| route:clarification expected:['reservation'] | 72 |
| route:clarification expected:['no_answer', 'overview', 'rules'] | 68 |
| missing all alternatives: ['latency', 'หน่วง'] | 66 |
| route:reservation expected:['members', 'overview'] | 62 |
| missing required: English localization | 61 |
| missing all alternatives: ['เฟรม', 'ความละเอียด'] | 60 |
| missing all alternatives: ['server', 'client'] | 59 |
| intent:conversation_price_lookup expected:service_fee_query | 58 |
| missing all alternatives: ['คีย์บอร์ด', 'mechanical'] | 57 |
| missing all alternatives: ['GPU', 'กราฟิก'] | 57 |
| route expected ['competition_rules'], got contact | 56 |
| missing all alternatives: ['กิจกรรม'] | 55 |
| missing all alternatives: ['ขอบคุณ'] | 54 |
| missing all alternatives: ['API', 'เชื่อมต่อ'] | 54 |
| status:answer expected:live_lookup_required | 54 |
| route:reservation expected:['overview'] | 51 |
| route:service_fee expected:['multi_question'] | 49 |
| missing all alternatives: ['จอง'] | 47 |
| route:clarification expected:['games'] | 44 |
| missing rulebook target(s): ['competition_rules_cs2_psu_phuket_2026'] | 44 |
| route:clarification expected:['members', 'overview'] | 43 |
| route:clarification expected:['competition_rules'] | 43 |
| missing required: psuesportspkt@gmail.com | 41 |
| missing rulebook target(s): ['competition_rules_valorant_psu_phuket_2026'] | 38 |
| missing required: Verified game catalog | 35 |
| latency_ceiling | 33 |
| first_line_off_topic | 32 |
| status:no_answer expected:clarification_required | 31 |
| status:clarification expected:localization_pending | 30 |
| route:no_answer expected:['penalty', 'rules'] | 28 |
| missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา'] | 27 |
| route:no_answer expected:['overview'] | 25 |
| legacy_english_thai_prose_flag | 23 |
| route:games expected:['competition_rules'] | 23 |
| missing all alternatives: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible'] | 22 |
| route:general expected:['reservation'] | 22 |
| route:clarification expected:['games', 'reservation'] | 21 |
| route:clarification expected:['reservation', 'schedule'] | 20 |
| route:contact expected:['rules', 'no_answer', 'clarification'] | 20 |
| route:knowledge expected:['general', 'clarification', 'no_answer', 'overview'] | 19 |
| missing all alternatives: ['เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง'] | 18 |
| missing all alternatives: ['ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน'] | 18 |
| route:reservation expected:['competition_rules'] | 18 |
| route:schedule expected:['no_answer'] | 18 |
| missing required: not connected | 18 |
| route:clarification expected:['games', 'service_fee'] | 18 |
| route:clarification expected:['no_answer'] | 18 |
| route:game_controls expected:['games', 'no_answer'] | 17 |
| route_mismatch | 16 |
| wrong_game_evidence | 16 |
| route:clarification expected:['general', 'knowledge'] | 16 |
| legacy_mode_prefix:['pipeline:multi_question_splitter'] | 16 |
| route:input_guard expected:['general', 'unknown', 'clarification', 'no_answer'] | 16 |
| route:schedule expected:['competition_rules'] | 16 |
| route:no_answer expected:['reservation'] | 15 |
| route:service_fee expected:['no_answer'] | 15 |
| route:general expected:['no_answer'] | 15 |
| missing all alternatives: ['ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม'] | 14 |
| route:general expected:['penalty'] | 14 |
| route:games expected:['no_answer'] | 14 |
| route:games expected:['clarification', 'equipment'] | 14 |
| wrong_category | 12 |
| wrong_game_source | 12 |
| missing all alternatives: ['Gaming PC รุ่น MSI MAG Infinite S3 14th'] | 12 |
| missing all alternatives: ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก'] | 12 |
| route:clarification expected:['contact'] | 12 |
| route expected ['competition_rules'], got clarification | 12 |
| route:no_answer expected:['competition_rules'] | 11 |
| missing all alternatives: ['PlayStation 5', 'PlayStation 5 #01-#02'] | 11 |
| missing all alternatives: ['L (Left Stick)', 'เคลื่อนที่'] | 11 |
| missing all alternatives: ['L3 (Click Left Stick)', 'หันมองจุดสนใจ'] | 11 |
| intent:game_list expected:list | 11 |
| missing required: Nintendo Switch Sports | 10 |
| missing required: Gran Turismo 7 | 10 |
| missing all alternatives: ['PC #03-#10', 'PC', 'Call of Duty'] | 10 |
| route:service_fee expected:['penalty', 'rules'] | 10 |
| route:contact expected:['penalty', 'rules'] | 10 |
| route:general expected:['rules'] | 10 |
| route:no_answer expected:['general', 'knowledge', 'overview'] | 10 |
| route:knowledge expected:['overview'] | 10 |
| quality_score_or_required_gate_failed | 9 |
| route:clarification expected:['multi_question'] | 9 |
| route:clarification expected:['general', 'knowledge', 'overview'] | 9 |
| route:schedule expected:['clarification', 'equipment'] | 9 |
| intent:control_lookup expected:game_control_lookup | 9 |
| route:clarification expected:['no_answer', 'service_fee'] | 9 |
| legacy_mode_prefix:['pipeline:structured_game_controls_no_current_game', 'pipeline:no_answer'] | 9 |
| route:equipment expected:['rules'] | 9 |
| missing all alternatives: ['The Last of Us Part II (Remastered)', 'PlayStation / PS5'] | 8 |
| missing all alternatives: ['TV 65 นิ้ว'] | 8 |
| missing all alternatives: ['TV 86 นิ้ว'] | 8 |
| missing required: Resident Evil 4 (Remake) | 8 |
| route:contact expected:['competition_rules', 'no_answer'] | 8 |
| route:clarification expected:['overview'] | 8 |
| route:reservation expected:['no_answer'] | 8 |
| route expected ['competition_rules', 'no_answer'], got contact | 8 |
| outcome expected no_answer_expected, got answer | 8 |
| source-gap no-answer attached evidence or did not abstain safely | 8 |
| legacy_mode_prefix:['pipeline:structured_game_controls_no_data', 'pipeline:no_answer', 'pipeline:answer_contract_no_answer'] | 8 |
| intent:user_service_facts expected:how_to | 8 |
| route:no_answer expected:['games'] | 7 |
| missing all alternatives: ['RS (Right Stick) Left/Right', 'เปลี่ยนตัวละครหลัก'] | 7 |
| route:schedule expected:['games'] | 7 |
| missing all alternatives: ['Y', 'Assist'] | 6 |
| missing all alternatives: ['L (Left Stick)', 'Move'] | 6 |
| missing all alternatives: ['L3 (Click Left Stick)', 'Look at'] | 6 |
| missing all alternatives: ['Touch Pad', 'สัมภาระ / เมนูกระเป๋าเก็บของ'] | 6 |
| missing required: ปุ่ม | 6 |
| route:games expected:['reservation', 'schedule'] | 6 |
| route:games expected:['equipment'] | 6 |
| route:rules expected:['no_answer'] | 6 |
| route:clarification expected:['games', 'no_answer'] | 6 |
| route expected ['competition_rules'], got schedule | 6 |
| missing all alternatives: ['TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง'] | 5 |
| route:no_answer expected:['rules'] | 5 |
| missing all alternatives: ['R (Right Stick)', 'มุมกล้อง'] | 5 |
| missing all alternatives: ['R3 (Click Right Stick)', 'ไฟฉาย'] | 5 |
| intent:booking_how_to expected:booking_policy | 5 |
| route:clarification expected:['general', 'overview', 'home'] | 5 |
| route:clarification expected:['general', 'overview', 'home', 'knowledge'] | 5 |
| route:competition_rules expected:['games'] | 5 |
| route:game_controls expected:['games', 'multi_question'] | 5 |
| outcome_mismatch | 4 |
| missing all alternatives: ['Left Stick', 'Steer'] | 4 |
| missing all alternatives: ['D-Pad', 'License'] | 4 |
| missing all alternatives: ['R (Right Stick)', 'Camera'] | 4 |
| missing all alternatives: ['R3 (Click Right Stick)', 'Flashlight'] | 4 |
| missing all alternatives: ['L1', 'Dodge'] | 4 |
| missing all alternatives: ['L2', 'Aim (Hold)'] | 4 |
| missing all alternatives: ['R1', 'Listen mode (Hold) / Switch Weapon'] | 4 |
| missing all alternatives: ['R2', 'Shoot (While aiming) / Reload'] | 4 |
| missing all alternatives: ['Triangle', 'Interact'] | 4 |
| missing all alternatives: ['Circle', 'Crouch'] | 4 |
| missing all alternatives: ['Square', 'Melee'] | 4 |
| missing all alternatives: ['Cross', 'Jump'] | 4 |
| missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'Tool selection (Up / Down / Left / Right)'] | 4 |
| missing all alternatives: ['Touch Pad', 'Inventory'] | 4 |
| missing all alternatives: ['Options', 'Pause'] | 4 |
| missing all alternatives: ['Super Smash Bros. Ultimate', 'Nintendo Switch'] | 4 |
| missing all alternatives: ['God of War Ragnarök', 'PlayStation / PS5'] | 4 |
| missing all alternatives: ['L1', 'หลบหลีก'] | 4 |
| missing all alternatives: ['L2', 'เล็งเป้า (กดค้าง)'] | 4 |
| missing all alternatives: ['R1', 'โหมดฟังเสียง (กดค้าง) / สลับอาวุธด่วน'] | 4 |
| missing all alternatives: ['R2', 'ยิงปืน (ขณะเล็ง) / รีโหลดกระสุน'] | 4 |
| missing all alternatives: ['Triangle', 'โต้ตอบ / สำรวจ'] | 4 |
| missing all alternatives: ['Circle', 'ย่อตัว / หมอบคลาน'] | 4 |
| missing all alternatives: ['Square', 'โจมตีประชิด'] | 4 |
| missing all alternatives: ['Cross', 'กระโดด'] | 4 |
| missing all alternatives: ['D-Pad (Up / Down / Left / Right)', 'แผงเลือกอุปกรณ์ด่วน'] | 4 |
| missing all alternatives: ['Options', 'หยุดเกม'] | 4 |
| missing all alternatives: ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 4 |
| missing all alternatives: ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 4 |
| missing all alternatives: ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 4 |
| missing all alternatives: ['Left Stick', 'เลี้ยว'] | 4 |
| missing all alternatives: ['D-Pad', 'ดูใบขับขี่และสถิติ'] | 4 |
| route:service_fee expected:['games'] | 4 |
| missing all alternatives: ['Cross (กากบาท)', 'Jump'] | 4 |
| route:equipment expected:['no_answer'] | 4 |
| route:clarification expected:['rules', 'overview', 'no_answer'] | 4 |
| intent:game_detail_lookup expected:game_availability_lookup | 4 |
| route:knowledge expected:['games'] | 4 |
| route:penalty expected:['rules'] | 4 |
| missing_complete_clause:No team member changes are allowed during the competition period | 3 |
| missing required: PlayStation 5 Zone | 3 |
| wrong_outcome:answer | 3 |
| route:no_answer expected:['multi_question'] | 3 |
| route:clarification expected:['overview', 'members'] | 3 |
| status:clarification expected:live_lookup_required | 3 |
| route:no_answer expected:['members', 'overview'] | 3 |
| intent:user_service_facts expected:group_count | 3 |
| intent:chatbot_identity expected:detail | 3 |
| route:clarification expected:['no_answer', 'games'] | 3 |
| route:games expected:['service_fee'] | 3 |
| intent:user_service_facts expected:detail | 3 |
| intent:ambiguity_gate_clarification expected:game_control_lookup | 3 |
| harness_timeout_30s | 2 |
| missing all alternatives: ['Call of Duty', 'ปุ่ม', 'จอย', 'คอนโทรล'] | 2 |
| route:no_answer expected:['equipment', 'games'] | 2 |
| missing all alternatives: ['Nintendo Switch', 'Zone'] | 2 |
| legacy_mode_prefix:['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'] | 2 |
| route:no_answer expected:['reservation', 'schedule'] | 2 |
| route:no_answer expected:['games', 'reservation'] | 2 |
| missing_complete_clause:5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง | 2 |
| missing_complete_clause:Map selection uses MAPBAN.GG | 2 |
| missing_complete_clause:If a forfeit is imposed, the result for that map is recorded as 13-0. | 2 |
| missing_complete_clause:New agents may not be used for approximately 2 weeks after release in Competitive mode. | 2 |
| missing_complete_clause:New maps may not be used for approximately 4 weeks after release in Competitive mode. | 2 |
| missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ | 2 |
| missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification. | 2 |
| missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ | 2 |
| missing_complete_clause:Abilities must not be used outside map boundaries to obtain information or an advantage. | 2 |
| missing_complete_clause:Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid. | 2 |
| missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping. | 2 |
| route:clarification expected:['penalty', 'rules'] | 2 |
| missing required: Phuket Campus | 2 |
| missing all alternatives: ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 2 |
| missing all alternatives: ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ'] | 2 |
| missing required: TEKKEN 8 | 2 |
| missing required: 150 บาท | 2 |
| missing required: PC Zone | 2 |
| route:clarification expected:['service_fee', 'games'] | 2 |
| route:clarification expected:['general', 'overview', 'knowledge'] | 2 |
| route:no_answer expected:['general', 'overview', 'knowledge'] | 2 |
| route:clarification expected:['contact', 'overview'] | 2 |
| intent:equipment_item_lookup expected:list | 2 |
| intent:food_bring_permission expected:studio_rules | 2 |
| route:games expected:['equipment', 'clarification'] | 2 |
| route:no_answer expected:['rules', 'penalty'] | 2 |
| route:games expected:['general', 'knowledge'] | 2 |
| route:reservation expected:['general', 'knowledge'] | 2 |
| route:input_guard expected:['general', 'clarification', 'no_answer', 'overview'] | 2 |
| route:input_guard expected:['general', 'clarification', 'no_answer', 'overview', 'knowledge'] | 2 |
| intent:checkin_required expected:booking_policy | 2 |
| intent:studio_rule_direct expected:studio_rules | 2 |
| missing_complete_clause:2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด | 1 |
| missing_complete_clause:The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited. | 1 |
| missing_complete_clause:3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ | 1 |
| missing_complete_clause:If any member withdraws, the team may be disqualified. | 1 |
| missing_complete_clause:อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ | 1 |
| missing_complete_clause:เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ | 1 |
| missing_complete_clause:If a bug occurs before either side deals damage, officials may roll back the round. | 1 |
| missing_complete_clause:If damage has already been dealt, no rollback is allowed unless through the Challenge process. | 1 |
| missing_complete_clause:หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที | 1 |
| missing_complete_clause:ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด | 1 |
| missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด | 1 |
| missing_complete_clause:3. เงินเริ่มต้น $800 / เวลาของระเบิด: 40 วินาที | 1 |
| missing_complete_clause:1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN | 1 |
| missing_complete_clause:Watching streams: Players are prohibited from watching live streams during competition. | 1 |
| missing_complete_clause:1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม | 1 |
| missing required: ต่างกันดังนี้ | 1 |
| missing required: PlayStation 5 60 นาที แพงกว่า 25 บาท | 1 |
| missing required: PlayStation 5 60 นาที แพงกว่า 80 บาท | 1 |
| missing required: PC #01-#02 | 1 |
| missing required: PC #03-#10 | 1 |
| missing required: ขั้นตอนจอง | 1 |
| missing required: สมัครสมาชิก | 1 |
| missing required: National ID | 1 |
| missing required: โดยไม่จองล่วงหน้าไม่ได้ | 1 |
| missing required: 1 ชั่วโมง | 1 |
| VR 30 นาที | 1 |
| VR 1 ชั่วโมง | 1 |
| ตาราง Service Fee | 1 |
| NARUTO X BORUTO | 1 |
| เร่ง | 1 |
| 1-2 Persons | 1 |
| 3-4 Persons | 1 |
| 3 หมวด | 1 |
| Members | 1 |
| cooperative education | 1 |
| PSU Phuket Esports Club | 1 |
| พื้นที่ที่กำหนด | 1 |
| Local LLM | 1 |
| ยังไม่ได้เปิด | 1 |
| route:clarification expected:['general', 'knowledge', 'no_answer'] | 1 |
| route:equipment expected:['general', 'knowledge', 'no_answer'] | 1 |
| missing required: Overcooked 2 | 1 |
| missing required: PS5 มีเกมอะไร | 1 |
| missing required: PS5 ราคาเท่าไหร่ | 1 |
| intent:conversation_price_lookup expected:multi_question_split | 1 |
| missing all alternatives: ['The Legend of Zelda', 'วิธีเล่น', 'เล่น'] | 1 |
| missing all alternatives: ['The Legend of Zelda', 'ปุ่ม', 'controller', 'จอย'] | 1 |
| missing required: PC 1 ชั่วโมง | 1 |
| missing required: local service fee update 2026-07-27 | 1 |
| legacy_mode_prefix:['pipeline:deterministic_calculator_fast'] | 1 |
| missing required: 70 บาท/session | 1 |
| legacy_mode_prefix:['pipeline:structured_booking_game_service_selection'] | 1 |
| missing required: จะเล่น Tekken 8 ต้องจองยังไง | 1 |
| missing required: Tekken 8 ราคาเท่าไหร่ | 1 |
| intent:price_missing_service expected:multi_question_split | 1 |
| missing required: ไม่พบข้อมูล | 1 |
| intent:zone_rental_fee expected:guard_no_answer | 1 |
| route expected ['competition_rules', 'clarification'], got no_answer | 1 |
| outcome expected clarification_required, got no_answer | 1 |
| route:general expected:['contact'] | 1 |
| route:reservation expected:['games', 'general', 'no_answer'] | 1 |
| route:input_guard expected:['equipment', 'no_answer'] | 1 |
| intent:count expected:booking_policy | 1 |
| route:schedule expected:['equipment', 'clarification'] | 1 |
| route:equipment expected:['games', 'clarification'] | 1 |
| route:game_controls expected:['games', 'clarification', 'no_answer'] | 1 |
| legacy_mode_prefix:['pipeline:structured_game_detail'] | 1 |
| intent:how_to expected:game_detail_lookup | 1 |
| intent:chatbot_greeting expected:detail | 1 |
| intent:ambiguity_gate_clarification expected:detail | 1 |
| route:clarification expected:['equipment'] | 1 |
| intent:ambiguity_gate_clarification expected:list | 1 |
| intent:price_missing_service expected:service_fee_query | 1 |
| intent:competition_rulebook_catalog expected:competition_game_list | 1 |
| intent:competition_rules_lookup expected:competition_game_list | 1 |
| intent:public_access expected:booking_policy | 1 |
| intent:booking_policy expected:how_to | 1 |
| intent:user_service_facts expected:list | 1 |
| route:input_guard expected:['schedule'] | 1 |
| intent:keyboard_layout_mismatch expected:schedule_query | 1 |
| intent:damage_responsibility expected:penalty_policy | 1 |
| intent:alcohol_rule expected:studio_rules | 1 |
| route:no_answer expected:['general'] | 1 |
| intent:freshness_live_source_required expected:detail | 1 |
