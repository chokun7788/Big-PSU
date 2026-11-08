# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 360
- PASS: 246
- FAIL: 114
- ERROR: 0
- Pass rate: 68.33%
- Average latency: 0.5296s
- P95 latency: 1.1250s
- Keyword fail: 91
- Source fail: 46
- Quality fail: 30
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 130
- `pipeline:structured_schedule`: 33
- `pipeline:no_answer`: 24
- `pipeline:guard_no_answer`: 24
- `pipeline:structured_reservation_fact`: 17
- `pipeline:structured_service_game_availability`: 17
- `pipeline:rules_fast_path`: 11
- `pipeline:candidate_margin_clarification`: 9
- `pipeline:checkin_fast_path`: 7
- `pipeline:structured_game_detail`: 7
- `pipeline:structured_equipment_item`: 7
- `pipeline:protected_checkin_required`: 5
- `pipeline:schedule_fast_path`: 4
- `pipeline:ambiguity_clarification`: 4
- `pipeline:payment_fast_path`: 4
- `pipeline:structured_members_group_list`: 4
- `pipeline:structured_members_role_lookup`: 4
- `pipeline:rag_direct_curated`: 3
- `pipeline:booking_fast_path`: 3
- `pipeline:structured_schedule_en`: 2
- `pipeline:multi_question_splitter`: 2
- `pipeline:protected_price_missing_service`: 2
- `pipeline:protected_payment_method`: 2
- `pipeline:structured_equipment_catalog`: 2
- `pipeline:protected_food_consumption`: 2
- `pipeline:protected_damage_responsibility`: 2
- `pipeline:penalty_fast_path`: 2
- `pipeline:game_target_unknown`: 2
- `pipeline:hybrid_guarded_rerank`: 2
- `pipeline:protected_studio_rule_direct`: 2
- `pipeline:structured_service_fee_en`: 1
- `pipeline:protected_booking_window`: 1
- `pipeline:booking_session_limit_fast_path`: 1
- `pipeline:english_no_answer`: 1
- `pipeline:protected_payment_deadline`: 1
- `pipeline:competition_source_rag`: 1
- `pipeline:game_target_ambiguous`: 1
- `pipeline:equipment_availability_fast_path`: 1
- `pipeline:protected_food_bring_permission`: 1
- `pipeline:protected_alcohol_rule`: 1
- `pipeline:protected_temporary_suspension`: 1
- `pipeline:overview_fast_path`: 1
- `pipeline:chatbot_identity_fast_path`: 1
- `pipeline:competition_target_clarification`: 1
- `pipeline:news_fast_path`: 1
- `pipeline:mixed_reservation_fast`: 1
- `pipeline:structured_members_game_relation_no_data`: 1
- `pipeline:protected_multi_studio_rules`: 1
- `pipeline:studio_rules_overview_fast_path`: 1
- `pipeline:protected_public_access`: 1
- `pipeline:calendar_schedule_fast_path`: 1

## Route Category Distribution

- `service_fee`: 133
- `reservation`: 46
- `schedule`: 43
- `games`: 31
- `no_answer`: 25
- `rules`: 19
- `clarification`: 15
- `general`: 10
- `equipment`: 10
- `overview`: 9
- `penalty`: 8
- `knowledge`: 5
- `competition_rules`: 3
- `multi_question`: 2
- `events_news`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| v2_016 | reservation | `schedule` | Monday; Friday | เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:0... |
| v2_017 | reservation | `schedule` | Monday; Friday | เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:0... |
| v2_018 | reservation | `general` | 09:00; 16:00; Monday; Friday; Maintenance; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_019 | reservation | `general` | 09:00; 16:00; Monday; Friday; Maintenance; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_020 | reservation | `schedule` | Monday; Friday | เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:0... |
| v2_021 | reservation | `schedule` | Monday; Friday | ไม่ได้เปิด 24 ชั่วโมงครับ ศูนย์ใช้รอบ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมี Maintenance บางช่วง รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร:... |
| v2_022 | reservation | `schedule` | Monday; Friday | รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_023 | reservation | `schedule` | Monday; Friday | รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_024 | reservation | `schedule` | Monday; Friday | รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_025 | reservation | `schedule` | Monday; Friday | รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_026 | reservation | `schedule` | Monday; Friday | เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:0... |
| v2_027 | reservation | `schedule` | Monday; Friday | รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_028 | reservation | `schedule` | Monday; Friday | รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_029 | reservation | `schedule` | Monday; Friday | รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_030 | reservation | `schedule` | Monday; Friday | รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_031 | reservation | `schedule` | Monday; Friday | รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_032 | reservation | `schedule` | Monday; Friday | รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_033 | reservation | `schedule` | Monday; Friday | รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_034 | reservation | `schedule` | Monday; Friday | รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_035 | reservation | `schedule` | Monday; Friday | รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_036 | reservation | `schedule` | Monday; Friday | รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:... |
| v2_037 | reservation | `general` | 13:00; 16:00; Maintenance; Weekly hardware inspection; cleaning; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_039 | reservation | `general` | 13:00; 16:00; Maintenance; Weekly hardware inspection; cleaning; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_040 | reservation | `schedule` | 13:00; 16:00; Maintenance; Weekly hardware inspection; cleaning | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด schedule ตอนนี้ครับ |
| v2_041 | reservation | `schedule` | 13:00; 16:00; Maintenance; Weekly hardware inspection; cleaning | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด schedule ตอนนี้ครับ |
| v2_074 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 1-2 คน 60 นาที แบ่งช่วงเวลาเป็น: 01:00-02:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_075 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 1-2 คน 60 นาที แบ่งช่วงเวลาเป็น: 01:00-02:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_076 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 1-2 คน 60 นาที แบ่งช่วงเวลาเป็น: 01:00-02:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_077 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 1-2 คน 60 นาที แบ่งช่วงเวลาเป็น: 01:00-02:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_092 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 3-4 คน 60 นาที แบ่งช่วงเวลาเป็น: 03:00-04:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_093 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 3-4 คน 60 นาที แบ่งช่วงเวลาเป็น: 03:00-04:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_094 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 3-4 คน 60 นาที แบ่งช่วงเวลาเป็น: 03:00-04:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_095 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ Nintendo Switch 3-4 คน 60 นาที แบ่งช่วงเวลาเป็น: 03:00-04:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท... |
| v2_128 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ VR 30 นาที ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท • PSU Alumni and General Student / นักศึกษาหรือนักเร... |
| v2_130 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ VR 30 นาที ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท • PSU Alumni and General Student / นักศึกษาหรือนักเร... |
| v2_146 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ VR 1 ชั่วโมง ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท • PSU Alumni and General Student / นักศึกษาหรือน... |
| v2_147 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ VR 1 ชั่วโมง ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท • PSU Alumni and General Student / นักศึกษาหรือน... |
| v2_148 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ VR 1 ชั่วโมง ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท • PSU Alumni and General Student / นักศึกษาหรือน... |
| v2_149 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ VR 1 ชั่วโมง ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 1 = 0 บาท • PSU Alumni and General Student / นักศึกษาหรือน... |
| v2_150 | service_fee | `service_fee` | ไม่พบ; service_fee direct answer missing: ไม่พบ | ราคา PC 1 ชั่วโมง (1 คน) • PSU Student and Staff: 0 บาท • PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท • General Adult / บุคคลทั่วไป: 70 บาท หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fe... |
| v2_151 | service_fee | `service_fee` | ไม่พบ; service_fee direct answer missing: ไม่พบ | ราคา PC 1 ชั่วโมง สำหรับ PSU Student and Staff: 0 บาท กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27 แหล่งข้อมูล: https://esports.computing.psu.ac.th/... |
| v2_152 | service_fee | `service_fee` | ไม่พบ; service_fee direct answer missing: ไม่พบ | ราคา PC 1 ชั่วโมง (1 คน) • PSU Student and Staff: 0 บาท • PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท • General Adult / บุคคลทั่วไป: 70 บาท หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fe... |
| v2_153 | service_fee | `service_fee` | ไม่พบ; service_fee direct answer missing: ไม่พบ | ราคา PC 1 ชั่วโมง (1 คน) • PSU Student and Staff: 0 บาท • PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท • General Adult / บุคคลทั่วไป: 70 บาท หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fe... |
| v2_154 | service_fee | `service_fee` | ไม่พบ; service_fee direct answer missing: ไม่พบ | ราคา PC 1 ชั่วโมง (1 คน) • PSU Student and Staff: 0 บาท • PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท • General Adult / บุคคลทั่วไป: 70 บาท หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fe... |
| v2_155 | service_fee | `service_fee` | ไม่พบ; quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้; service_fee direct answer missing: ไม่พบ, Service Fee | ระยะเวลาที่ถามคือ 2 ชั่วโมง ใช้ 2 session ตามแพ็กเกจ PC 1 ชั่วโมง แบ่งช่วงเวลาเป็น: 09:00-10:00, 10:00-11:00 ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 2 = 0 บาท • PSU... |
| v2_156 | service_fee | `service_fee` | ไม่พบ; service_fee direct answer missing: ไม่พบ, Service Fee | ระยะเวลาที่ถามคือ 2 ชั่วโมง ใช้ 2 session ตามแพ็กเกจ PC 1 ชั่วโมง ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน: • PSU Student and Staff: 0 บาท/session x 2 = 0 บาท • PSU Alumni and General Student / นักศึกษาหรือน... |
| v2_157 | service_fee | `service_fee` | ไม่พบ; service_fee direct answer missing: ไม่พบ | PC - 1 hour (1 people) - PSU alumni and students from other institutions: 25 THB Prices are calculated deterministically from the Service Fee 2026 table. Source: https://esports.computing.psu.ac.th/wp-content/uploads/202... |
| v2_158 | service_fee | `clarification` | PlayStation 5; Nintendo Switch; Cockpit; service_fee; service_fee direct answer missing: PlayStation 5, Nintendo Switch, Cockpit | ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่` |
| v2_159 | service_fee | `clarification` | service_fee | ต้องการทราบค่าบริการของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? ราคาแตกต่างตามบริการและกลุ่มผู้ใช้ จึงยังระบุราคาเดียวไม่ได้ครับ |
| v2_160 | service_fee | `clarification` | PlayStation 5; Nintendo Switch; Cockpit; service_fee; service_fee direct answer missing: PlayStation 5, Nintendo Switch, Cockpit | ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่` |
| v2_161 | service_fee | `service_fee` | PlayStation 5; Nintendo Switch; Cockpit; VR; service_fee direct answer missing: PlayStation 5, Nintendo Switch, Cockpit, VR | บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/upl... |
| v2_162 | service_fee | `clarification` | service_fee | Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR? The rate depends on the service and user group. |
| v2_165 | reservation | `schedule` | 1 ชั่วโมง | วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด): • วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00 • วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00 • วันศุกร์: เปิด 09:00-12:00; Maintenance 13:0... |
| v2_166 | reservation | `reservation` | 1 ชั่วโมง | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_171 | reservation | `no_answer` | 3 Sessions; Reservation | I could not find verified PSU Esports Studio - Phuket information for reservation. |
| v2_173 | reservation | `reservation` | 3 Sessions | เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_180 | reservation | `reservation` | ยกเลิก; 1 ชั่วโมง; จองใหม่ | ขั้นตอนจองโดยสรุป: • เลือกบริการหรือโซนที่ต้องการใช้ • เลือกวันและรอบเวลาที่ต้องการ • กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ • ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง • หลั... |
| v2_182 | reservation | `reservation` | ยกเลิก; 1 ชั่วโมง; จองใหม่ | ขั้นตอนจองโดยสรุป: • เลือกบริการหรือโซนที่ต้องการใช้ • เลือกวันและรอบเวลาที่ต้องการ • กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ • ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง • หลั... |
| v2_183 | reservation | `reservation` | ยกเลิก; 1 ชั่วโมง; จองใหม่ | ขั้นตอนจองโดยสรุป: • เลือกบริการหรือโซนที่ต้องการใช้ • เลือกวันและรอบเวลาที่ต้องการ • กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ • ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง • หลั... |
| v2_184 | reservation | `reservation` | ไม่สามารถโอนสิทธิ์ | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_192 | reservation | `reservation` | ยกเลิก; ไม่มีการคืนเงิน | เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_201 | games | `games` | PlayStation 5; TEKKEN 8 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| v2_206 | games | `games` | Overcooked 2 | ได้ครับ Overcooked! 2 เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons) แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_207 | games | `equipment` | Mario Kart; Reservation | อุปกรณ์ใน Nintendo Switch Zone: Nintendo Switch Zone • Nintendo Switch OLED (1 Unit) • TV 86 นิ้ว (1 Unit) • Sofa 2 seats (2 Sets) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home |
| v2_208 | games | `games` | Reservation | Super Smash Bros Ultimate: Super Smash Bros Ultimate คือเกมต่อสู้ที่ใช้ตัวละครจากหลายเกม ผลักคู่ต่อสู้ออกจากฉากเพื่อทำคะแนน แนวเกม: เกมต่อสู้แบบ Platform Fighter วิธีเล่นโดยสรุป: เลือกตัวละคร ใช้ท่าโจมตี หลบ กระโดด และพย... |
| v2_211 | games | `competition_rules` | PC; Reservation | คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026 |
| v2_218 | games | `games` | Cockpit; Gran Turismo 7 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| v2_219 | games | `games` | Reservation | Gran Turismo 7: Gran Turismo 7 คือเกมแข่งรถที่เน้นการขับรถสมจริง การเลือกสนาม รถ และการควบคุมจังหวะเข้าโค้ง แนวเกม: เกมแข่งรถ / Driving Simulator วิธีเล่นโดยสรุป: ใน Cockpit Zone เล่นโดยใช้พวงมาลัย คันเร่ง เบรก และชุดเบา... |
| v2_223 | equipment | `games` | Gaming Chair; 10 Units; home | ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง |
| v2_227 | equipment | `equipment` | Units | TV 86 นิ้ว: จอทีวีขนาด 86 นิ้วสำหรับเล่นเกม Nintendo Switch เป็นกลุ่ม จำนวน: 1 Unit อยู่ที่: Nintendo Switch Zone ใช้สำหรับ: • แสดงผลเกม Nintendo Switch เช่น Mario Kart, Overcooked, Super Smash Bros และ Switch Sports แหล... |
| v2_229 | equipment | `equipment` | Units | Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone จำนวน: 1 Unit อยู่ที่: VR Zone ใช้สำหรับ: • เล่น Beat Saber • เล่น Horizon Call of the Mountain แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home |
| v2_230 | rules | `rules` | พื้นที่ที่กำหนด | นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_233 | rules | `general` | งด; เสียงดัง; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_234 | rules | `general` | ห้าม; เสียดสี; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_238 | rules | `general` | ห้าม; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_239 | rules | `general` | ห้าม; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_240 | rules | `general` | ห้าม; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_244 | penalty | `clarification` | Reservation | ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่` |
| v2_247 | penalty | `penalty` | ชดเชย; เต็มจำนวน | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ |
| v2_248 | penalty | `penalty` | ระงับสิทธิ์ | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ |
| v2_250 | penalty | `competition_rules` | ระงับสิทธิ์; ถาวร | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ |
| v2_251 | penalty | `penalty` | 7 วัน | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ |
| v2_252 | penalty | `knowledge` | บันทึก; ประวัติ | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด knowledge ตอนนี้ครับ |
| v2_253 | overview | `overview` | มหาวิทยาลัยสงขลานครินทร์; วิทยาลัยการคอมพิวเตอร์; home | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members |
| v2_255 | overview | `overview` | มหาวิทยาลัยสงขลานครินทร์; วิทยาลัยการคอมพิวเตอร์; home | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •... |
| v2_256 | overview | `overview` | มหาวิทยาลัยสงขลานครินทร์; วิทยาลัยการคอมพิวเตอร์; home | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •... |
| v2_257 | overview | `games` | มหาวิทยาลัยสงขลานครินทร์; วิทยาลัยการคอมพิวเตอร์; home | ยังไม่พบชื่อเกมที่ตรงกับข้อมูลที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ กรุณาตรวจสอบชื่อเกมหรือพิมพ์ชื่อเกมที่ต้องการถามอีกครั้ง |
| v2_258 | contact | `clarification` | PSU; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_259 | contact | `clarification` | PSU; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_260 | contact | `clarification` | PSU; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_261 | contact | `knowledge` | Contact | ผมคือ PSU Esports Assistant แชทบอทผู้ช่วยของ PSU Esports Studio - Phuket ครับ ผมช่วยตอบคำถามเกี่ยวกับ: • เกมที่มีให้เล่นและเกมที่เกี่ยวข้องกับการแข่งขัน • ปุ่มควบคุมและวิธีเล่นของเกมที่มีข้อมูลยืนยัน • อุปกรณ์และโซนบริกา... |
| v2_262 | contact | `reservation` | Contact | ตอนจองต้องกรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล, เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี จากนั้นชำระเงินโดยโอนเข้าบัญชีธนาคารและแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_263 | knowledge | `general` | อีสปอร์ต; Knowledge | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_264 | knowledge | `clarification` | Stanford; 1972; Knowledge | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_266 | knowledge | `games` | MOBA; Knowledge | ยังไม่พบชื่อเกมที่ตรงกับข้อมูลที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ กรุณาตรวจสอบชื่อเกมหรือพิมพ์ชื่อเกมที่ต้องการถามอีกครั้ง |
| v2_268 | knowledge | `games` | การทำงานเป็นทีม; Knowledge | Overcooked! 2: Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย แนวเกม: เกม Co-op ทำอาหาร วิธีเล่นโดยสรุป: ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีม... |
| v2_269 | knowledge | `games` | ไหวพริบ; การตัดสินใจ; Knowledge | Mario Kart 8 Deluxe: Mario Kart 8 Deluxe คือเกมแข่งรถสไตล์ปาร์ตี้ที่ใช้ตัวละคร Nintendo ขับรถแข่งกันในสนามหลากหลายแบบ แนวเกม: เกมแข่งรถ Party Racing วิธีเล่นโดยสรุป: เลือกตัวละครและรถ ขับเข้าเส้นชัย ใช้ไอเทมช่วยโจมตี/ป้อ... |
| v2_270 | events_news | `competition_rules` | PSU; News | ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT |
| v2_271 | events_news | `games` | News | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| v2_272 | events_news | `games` | News | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| v2_274 | events_news | `clarification` | PSU; News | คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: เวลาเปิด-ปิด, สมาชิกทีม |
| v2_281 | no_answer | `rules` | ไม่พบข้อมูล | ยังยืนยันไม่ได้ว่าโต๊ะเล่นเกมเป็นพื้นที่รับประทานที่กำหนดครับ อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_299 | reservation | `reservation` | ไม่มีการคืนเงิน | หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_300 | reservation | `reservation` | 30 นาที; ยกเลิก | ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_304 | service_fee | `service_fee` | บาท; service_fee; service_fee direct answer missing: บาท | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด service_fee ตอนนี้ครับ |
| v2_307 | service_fee | `overview` | บาท; service_fee; service_fee direct answer missing: บาท | ยังไม่พบข้อมูลที่ยืนยันได้ว่าสมาชิกหรือสตาฟแต่ละคนเล่นเกม/ดูแลเกมหรือโซนไหนครับ ข้อมูลที่มีตอนนี้ยืนยันได้เฉพาะรายชื่อสมาชิก หมวด และตำแหน่งในหน้า Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members |
| v2_315 | service_fee | `service_fee` | PlayStation 5; service_fee direct answer missing: PlayStation 5 | ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png |
| v2_316 | service_fee | `service_fee` | VR; service_fee direct answer missing: VR | ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png |
| v2_321 | contact | `clarification` | facebook.com/psuesportsphuket; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_329 | contact | `clarification` | facebook.com/psuesportsphuket; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_337 | contact | `clarification` | facebook.com/psuesportsphuket; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_340 | service_fee | `reservation` | 190; service_fee; service_fee direct answer missing: 190 | ได้ครับ บุคคลทั่วไปสามารถจองใช้บริการ VR ได้ ค่าบริการขึ้นกับประเภทบริการและกลุ่มผู้ใช้ ต้องจองผ่านระบบและแสดงบัตรประชาชนเมื่อเช็กอิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_345 | contact | `clarification` | facebook.com/psuesportsphuket; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| v2_353 | contact | `clarification` | facebook.com/psuesportsphuket; Contact | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_base_360_current.jsonl`
