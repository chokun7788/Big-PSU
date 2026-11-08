# เทียบ Flow เดิมกับ R124 รายข้อ

61 unique retained development questions; ตารางนี้รวมหลักฐานต่าง revision ไม่ใช่ผลรัน61ข้อครั้งเดียวของR05 และไม่ใช้แทนเปอร์เซ็นต์ความถูกต้องทั้งระบบ

ฐานเปรียบเทียบ: teacher02 กับ candidate04_final(R03) ใช้reference clock21ตุลาคม12:00; focused14ใช้R04ก่อนแก้mapbodyขั้นสุดท้าย; APIล่าสุดใช้R05และเวลาจริง23ตุลาคม รายข้อระบุ provenance เสมอ

## 1. ef5c0b5a

Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?

**วิเคราะห์:** อ่าน CS2 clause เต็มเรื่อง brightness/resolution/crosshair; สะกดผิดไม่ควรเปลี่ยนเจตนาหรือขยายสิทธิ์นอกเกม/จอ

**ผลใหม่ที่แสดง:** candidate05_final_checks / R04 targeted CLI

**คำตอบเดิมจริง**

```text
Answer: Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
PSU Phuket CS2 2026 Tournament — 1. Players may customize brightness, resolution, and crosshair settings exclusively within the game and computer screen only: 1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively. [S1]
```

**Source IDs ที่เลือก:** C13:competition_competition_rules_cs2_psu_phuket_2026_section_045:rule_clause:0, C13:competition_competition_rules_cs2_psu_phuket_2026_section_045:rule_clause:1, competition_competition_rules_cs2_psu_phuket_2026_section_045

**เส้นทางเดิม:** pipeline:competition_rule_detail_source; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate05_final_checks/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 2. 2d97cb1b

ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง

**วิเคราะห์:** teacher ไปตอบแนวเกม Sports; ใหม่ผูกอุปกรณ์ Nintendo ได้ แต่ความครบทั้งโซนยังไม่พิสูจน์ จึงคง partial

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:

Nintendo Switch Sports
•    แนวเกม: เกมกีฬา Motion Control
•    เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
ตอบได้เฉพาะส่วนที่มีหลักฐาน ความครบตามรูปแบบที่ขอยังยืนยันไม่ได้
Nintendo Switch OLED — การใช้งาน: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ
เล่น Mario Kart 8 Deluxe
เล่น Overcooked 2
เล่น Super Smash Bros Ultimate
เล่น Nintendo Switch Sports [S1]
```

**Source IDs ที่เลือก:** C03:equipment_nintendo_switch_oled:usage:0, equipment_nintendo_switch_oled

**เส้นทางเดิม:** pipeline:structured_games_genre_list; **เส้นทางใหม่:** pipeline:common_partial_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 3. d91ee50a

What are the 8 buttons in Tekken 8, ans what is the PC price

**วิเคราะห์:** แยกปุ่ม Tekken กับราคา PC; source มี 12 entries ไม่ระบุ subset 8 ปุ่ม จึงถามเพิ่มเฉพาะส่วนปุ่ม; teacher ตกส่วน controls

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Service prices (recorded package rates):

PC — 60 minutes/package (1 person)
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
The source records 12 control entries but does not identify the requested subset of 8 buttons. Known entries are listed below; please specify the button group.
TEKKEN 8 / PlayStation / PS5 — Left Punch: Square — Punch or attack with the left hand — primary button to start fast frame combos [S1]
TEKKEN 8 / PlayStation / PS5 — Right Punch: Triangle — Heavy punch or attack with the right hand — often used for high damage or countering (Counter) [S2]
TEKKEN 8 / PlayStation / PS5 — Left Kick: Cross — Kick with the left leg to intercept or attack and create an opening in the opponent's defense. [S3]
TEKKEN 8 / PlayStation / PS5 — Right Kick: Circle — Deliver a powerful right-leg kick, often for range control or a high-damage low sweep. [S4]
TEKKEN 8 / PlayStation / PS5 — Jump: D-Pad Up — Jump upward to evade low attacks, or press in combination with mid-air attack button [S5]
TEKKEN 8 / PlayStation / PS5 — Move Backward: D-Pad Left — Move the character backward to maintain distance or hold to "Guard" against high and medium attacks from enemies [S6]
TEKKEN 8 / PlayStation / PS5 — Duck: D-Pad Down — Lower the character's stance to dodge punches or high attacks, and block low attacks [S7]
TEKKEN 8 / PlayStation / PS5 — Move: L (Left Stick) — Move the character in general directions, including moving forward and backward. [S8]
TEKKEN 8 / PlayStation / PS5 — Special Style: L1 — Press to toggle the Smart Assist mode, allowing one-button combo and special move execution [S9]
TEKKEN 8 / PlayStation / PS5 — Heat Activate: R1 — Activate the Heat System to enter Overdrive state, buffing attacks and enhancing character abilities [S10]
TEKKEN 8 / PlayStation / PS5 — Heat Smash: R1 (While in Heat) — Release the powerful final move to end a combo, using all remaining Heat gauge at once. [S11]
TEKKEN 8 / PlayStation / PS5 — Pause: Options — Pause the game briefly to enter a menu window, such as checking Move List (move list) or other settings. [S12]
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S13]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S14]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S15]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S16]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S17]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S18]
```

**Source IDs ที่เลือก:** C05:controls_ps5_tekken_8:binding_0:0, C05:controls_ps5_tekken_8:binding_0:1, C05:controls_ps5_tekken_8:binding_1:2, C05:controls_ps5_tekken_8:binding_1:3, C05:controls_ps5_tekken_8:binding_2:4, C05:controls_ps5_tekken_8:binding_2:5, C05:controls_ps5_tekken_8:binding_3:6, C05:controls_ps5_tekken_8:binding_3:7, C05:controls_ps5_tekken_8:binding_4:8, C05:controls_ps5_tekken_8:binding_4:9, C05:controls_ps5_tekken_8:binding_5:10, C05:controls_ps5_tekken_8:binding_5:11, C05:controls_ps5_tekken_8:binding_6:12, C05:controls_ps5_tekken_8:binding_6:13, C05:controls_ps5_tekken_8:binding_7:14, C05:controls_ps5_tekken_8:binding_7:15, C05:controls_ps5_tekken_8:binding_8:16, C05:controls_ps5_tekken_8:binding_8:17, C05:controls_ps5_tekken_8:binding_9:18, C05:controls_ps5_tekken_8:binding_9:19, C05:controls_ps5_tekken_8:binding_10:20, C05:controls_ps5_tekken_8:binding_10:21, C05:controls_ps5_tekken_8:binding_11:22, C05:controls_ps5_tekken_8:binding_11:23, C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:amount:24, C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:amount:25, C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:amount:26, C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:amount:27, C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:amount:28, C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:amount:29, C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:amount:30, C06:rate_recovered_pc_availability_pc_01_02_general_student:amount:31, C06:rate_recovered_pc_availability_pc_01_02_general_student:amount:32, C06:rate_recovered_pc_availability_pc_01_02_general_student:amount:33, C06:rate_recovered_pc_availability_pc_01_02_general_student:amount:34, C06:rate_recovered_pc_availability_pc_01_02_general_student:amount:35, C06:rate_recovered_pc_availability_pc_01_02_general_student:amount:36, C06:rate_recovered_pc_availability_pc_01_02_general_student:amount:37, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:38, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:39, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:40, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:41, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:42, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:43, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:44, C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount:45, C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount:46, C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount:47, C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount:48, C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount:49, C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount:50, C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount:51, C06:rate_recovered_pc_availability_pc_03_10_general_student:amount:52, C06:rate_recovered_pc_availability_pc_03_10_general_student:amount:53, C06:rate_recovered_pc_availability_pc_03_10_general_student:amount:54, C06:rate_recovered_pc_availability_pc_03_10_general_student:amount:55, C06:rate_recovered_pc_availability_pc_03_10_general_student:amount:56, C06:rate_recovered_pc_availability_pc_03_10_general_student:amount:57, C06:rate_recovered_pc_availability_pc_03_10_general_student:amount:58, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:59, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:60, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:61, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:62, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:63, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:64, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:65, controls_ps5_tekken_8, rate_recovered_pc_availability_pc_01_02_psu_student_staff, rate_recovered_pc_availability_pc_01_02_general_student, rate_recovered_pc_availability_pc_01_02_general_adult, rate_recovered_pc_availability_pc_03_10_psu_student_staff, rate_recovered_pc_availability_pc_03_10_general_student, rate_recovered_pc_availability_pc_03_10_general_adult

**เส้นทางเดิม:** pipeline:structured_service_fee_conversation; **เส้นทางใหม่:** pipeline:common_partial_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 4. 490a5b13

ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า

**วิเคราะห์:** สิทธิ์ผู้ใช้ภายนอกทั่วไปต้องไม่เอา eligibility แข่ง CS2 มาปน

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ได้ครับ บุคคลทั่วไปสามารถจองใช้บริการของศูนย์ได้ ค่าบริการขึ้นกับประเภทบริการและกลุ่มผู้ใช้ ต้องจองผ่านระบบและแสดงบัตรประชาชนเมื่อเช็กอิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
ผู้ใช้ภายนอก: บุคคลภายนอกใช้บริการทั่วไปได้ทั้งหมด; ไม่ขยายไปเป็นคุณสมบัติแข่ง CS2 ซึ่งเอกสารกำหนดนักศึกษา PSU ภูเก็ต [S1]
```

**Source IDs ที่เลือก:** C10:r114_q037_owner_policy:owner_policy:0, r114_q037_owner_policy

**เส้นทางเดิม:** pipeline:protected_public_access; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 5. e57f0296

ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน

**วิเคราะห์:** คำตอบนำอาหาร/เครื่องดื่มเข้าได้มีอยู่เดิม; projection/topic ทำให้เข้าไม่ถึง แก้แล้วและทดสอบถอน/แก้ source แบบ memory

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม [S1]
```

**Source IDs ที่เลือก:** C10:migrated_policy_text_food_bring_general:owner_policy:0, migrated_policy_text_food_bring_general

**เส้นทางเดิม:** pipeline:protected_food_bring_permission; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 6. 0a00000d

What do you need to book to paly FINAL FANTASY XVI

**วิเคราะห์:** โจทย์ถามต้องเลือกบริการใดเพื่อเล่น FF16 ไม่ใช่ขั้นตอนจอง; ใช้ game→offering

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
FINAL FANTASY XVI — studio services offering this game: PlayStation 5 #01-#02 [S1]
```

**Source IDs ที่เลือก:** C04:game_detail_final_fantasy_xvi:studio_services:0, game_detail_final_fantasy_xvi

**เส้นทางเดิม:** pipeline:rule_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 7. a603ab1a

How to book Cockpit and what days is it open?

**วิเคราะห์:** สอง task booking+weekly calendar; อ่าน typed calendar ก่อน model selection; weekly list ยังมี completeness qualification

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
This question contains several topics. Here are the answers separately:

Question 1: How to book Cockpit
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

Question 2: what days is it open
Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
1. how to book cockpit
How to book: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S1]

2. what days is it open
Recorded regular play-service timetable, not live machine availability or building access hours. Special closures override this timetable.
Monday — regular play-service timetable: 09:00–12:00 maintenance; 13:00–16:00 open for play [S2]
Tuesday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S3]
Wednesday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S4]
Thursday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S5]
Friday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 maintenance [S6]
Saturday — regular play-service timetable: Closed for play under the regular timetable [S7]
Sunday — regular play-service timetable: Closed for play under the regular timetable [S8]
```

**Source IDs ที่เลือก:** C08:migrated_faq_rule_booking_steps:owner_policy:0, C11:migrated_schedule_0:service_periods:0, C11:migrated_schedule_1:service_periods:1, C11:migrated_schedule_2:service_periods:2, C11:migrated_schedule_3:service_periods:3, C11:migrated_schedule_4:service_periods:4, C11:migrated_schedule_5:service_periods:5, C11:migrated_schedule_6:service_periods:6, migrated_faq_rule_booking_steps, migrated_schedule_0, migrated_schedule_1, migrated_schedule_2, migrated_schedule_3, migrated_schedule_4, migrated_schedule_5, migrated_schedule_6

**เส้นทางเดิม:** pipeline:multi_question_splitter; **เส้นทางใหม่:** pipeline:common_partial_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 8. 1cf7db38

Please use verified studio information: What ID does an external visitor need to use the studio?

**วิเคราะห์:** เจตนาถามเอกสาร ไม่ใช่สิทธิ์บุคคลภายนอก; source หลายรุ่นให้รายการเอกสารไม่เหมือนกันทั้งหมด เก็บ scope ไม่แต่งรวมสิทธิ์

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Check-in document: When checking in to use the service, you must present your student ID card, staff ID card, or national identification card. [S1]
What documents must I present upon arrival?: At arrival, present a national ID card, university student card, school student card, or passport. [S2]
```

**Source IDs ที่เลือก:** C08:migrated_faq_curated_checkin_id_required:owner_policy:0, C08:migrated_owner_claim_checkin_documents:owner_policy:1, migrated_faq_curated_checkin_id_required, migrated_owner_claim_checkin_documents

**เส้นทางเดิม:** pipeline:user_service_facts; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 9. 044f6671

ขอสอบถามหน่อยยครับ บุคคลทั่วไป เล่น PS5 2 ชั่วโมง เสียกี่บาท

**วิเคราะห์:** เลือก General Adult/PS5/120 นาที คำนวณจาก rate และ owner confirmation วันที่20 ไม่สร้าง effective interval ใหม่

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
ระยะเวลาที่ถาม 120 นาที (2 ชั่วโมง) คิดเป็น 2 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ × 2 = 300 บาท
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PlayStation 5 #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 300 บาท สำหรับ 120 นาที [S1]
```

**Source IDs ที่เลือก:** C06:migrated_rate_playstation_5_60_1_2_general_adult:amount:0, C06:migrated_rate_playstation_5_60_1_2_general_adult:amount:1, C06:migrated_rate_playstation_5_60_1_2_general_adult:amount:2, C06:migrated_rate_playstation_5_60_1_2_general_adult:amount:3, C06:migrated_rate_playstation_5_60_1_2_general_adult:amount:4, C06:migrated_rate_playstation_5_60_1_2_general_adult:amount:5, migrated_rate_playstation_5_60_1_2_general_adult

**เส้นทางเดิม:** pipeline:structured_service_fee_conversation; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 10. 1806def7

เกมไหนเล่นได้หลายโซน

**วิเคราะห์:** filter เกมหลายโซนจาก explicit relations; ไม่เอาทั้ง catalogue มาตอบ; ความครบทุกเกมยังไม่พิสูจน์

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
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
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
Gran Turismo 7 — โซนที่ยืนยันว่ามีเกมนี้: Cockpit Zone; PlayStation 5 Zone [S1]
Resident Evil 4 — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S2]
Resident Evil Village — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S3]
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S4]
```

**Source IDs ที่เลือก:** C04:game_detail_gran_turismo_7:zone:0, C04:game_detail_gran_turismo_7:zone:1, C04:game_detail_gran_turismo_7:zone:2, C04:game_detail_gran_turismo_7:zone:3, C04:game_detail_gran_turismo_7:zone:4, C04:game_detail_gran_turismo_7:zone:5, C04:game_detail_gran_turismo_7:zone:6, C04:game_detail_gran_turismo_7:zone:7, C04:game_detail_gran_turismo_7:zone:8, C04:game_detail_gran_turismo_7:zone:9, C04:game_detail_gran_turismo_7:zone:10, C04:game_detail_resident_evil_4:zone:11, C04:game_detail_resident_evil_4:zone:12, C04:game_detail_resident_evil_4:zone:13, C04:game_detail_resident_evil_4:zone:14, C04:game_detail_resident_evil_4:zone:15, C04:game_detail_resident_evil_4:zone:16, C04:game_detail_resident_evil_4:zone:17, C04:game_detail_resident_evil_4:zone:18, C04:game_detail_resident_evil_4:zone:19, C04:game_detail_resident_evil_4:zone:20, C04:game_detail_resident_evil_4:zone:21, C04:game_detail_resident_evil_4:zone:22, C04:game_detail_resident_evil_4:zone:23, C04:game_detail_resident_evil_4:zone:24, C04:game_detail_resident_evil_4:zone:25, C04:game_detail_resident_evil_4:zone:26, C04:game_detail_resident_evil_4:zone:27, C04:game_detail_resident_evil_4:zone:28, C04:game_detail_resident_evil_4:zone:29, C04:game_detail_resident_evil_village:zone:30, C04:game_detail_resident_evil_village:zone:31, C04:game_detail_resident_evil_village:zone:32, C04:game_detail_resident_evil_village:zone:33, C04:game_detail_resident_evil_village:zone:34, C04:game_detail_resident_evil_village:zone:35, C04:game_detail_resident_evil_village:zone:36, C04:game_detail_resident_evil_village:zone:37, C04:game_detail_resident_evil_village:zone:38, C04:game_detail_resident_evil_village:zone:39, C04:game_detail_resident_evil_village:zone:40, C04:game_detail_resident_evil_village:zone:41, C04:game_detail_resident_evil_village:zone:42, C04:game_detail_resident_evil_village:zone:43, C04:game_detail_resident_evil_village:zone:44, C04:game_detail_resident_evil_village:zone:45, C04:game_detail_resident_evil_village:zone:46, C04:game_detail_resident_evil_village:zone:47, C04:game_detail_resident_evil_village:zone:48, C04:game_detail_tekken_8:zone:49, C04:game_detail_tekken_8:zone:50, C04:game_detail_tekken_8:zone:51, C04:game_detail_tekken_8:zone:52, C04:game_detail_tekken_8:zone:53, C04:game_detail_tekken_8:zone:54, C04:game_detail_tekken_8:zone:55, C04:game_detail_tekken_8:zone:56, C04:game_detail_tekken_8:zone:57, C04:game_detail_tekken_8:zone:58, C04:game_detail_tekken_8:zone:59, C04:game_detail_tekken_8:zone:60, C04:game_detail_tekken_8:zone:61, C04:game_detail_tekken_8:zone:62, C04:game_detail_tekken_8:zone:63, C04:game_detail_tekken_8:zone:64, C04:game_detail_tekken_8:zone:65, C04:game_detail_tekken_8:zone:66, game_detail_gran_turismo_7, game_detail_resident_evil_4, game_detail_resident_evil_village, game_detail_tekken_8

**เส้นทางเดิม:** pipeline:source_operation_game_list; **เส้นทางใหม่:** pipeline:common_partial_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 11. 8570a28b

Please answer from verified studio information: Which studio zone has TEKKEN 8

**วิเคราะห์:** เลือก zone relation ของ Tekken8 เท่านั้น ไม่ใช่ catalogue ทั้งโซน

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
TEKKEN 8 is available on: PC #01-#02, PlayStation 5 #01-#02. Studio zone(s): PC Zone, PlayStation 5 Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
TEKKEN 8 — confirmed studio zones offering this game: PC Zone; PlayStation 5 Zone [S1]
```

**Source IDs ที่เลือก:** C04:game_detail_tekken_8:zone:0, C04:game_detail_tekken_8:zone:1, C04:game_detail_tekken_8:zone:2, C04:game_detail_tekken_8:zone:3, C04:game_detail_tekken_8:zone:4, C04:game_detail_tekken_8:zone:5, C04:game_detail_tekken_8:zone:6, C04:game_detail_tekken_8:zone:7, C04:game_detail_tekken_8:zone:8, C04:game_detail_tekken_8:zone:9, C04:game_detail_tekken_8:zone:10, C04:game_detail_tekken_8:zone:11, C04:game_detail_tekken_8:zone:12, C04:game_detail_tekken_8:zone:13, C04:game_detail_tekken_8:zone:14, C04:game_detail_tekken_8:zone:15, C04:game_detail_tekken_8:zone:16, C04:game_detail_tekken_8:zone:17, game_detail_tekken_8

**เส้นทางเดิม:** pipeline:structured_game_availability_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 12. 9813e160

What are all the buttons in Call of Duty: Warzone

**วิเคราะห์:** รายการ controls จาก source binding set; complete ในขอบเขตข้อมูลที่บันทึก ไม่ใช่ยืนยัน installed preset

**ผลใหม่ที่แสดง:** candidate05_final_checks / R04 targeted CLI

**คำตอบเดิมจริง**

```text
Call of Duty: Warzone controls:
- Cross: Jump/Mantle
- Circle: Crouch/Prone/Slide
- Square: Use/Reload
- Triangle: Switch Weapon
- D-Pad: Campaign, Multiplayer or Co-Op specific
- Touch Pad: Scoreboard
- Options: Pause
- L1: Use Tactical Equipment
- R1: Use Lethal Equipment
- L2: Aim Down Sight Behavior
- R2: Fire Weapon
- L3: Sprint/Tactical Sprint/Steady Aim
- R3: Melee
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameaccess.info/call-of-duty-warzone-battle-royale-mode-controls/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Call of Duty: Warzone / PlayStation / PS5 — Jump/Mantle: Cross — Jump or climb obstacles [S1]
Call of Duty: Warzone / PlayStation / PS5 — Crouch/Prone/Slide: Circle — Press to change stance or slide your knee while running [S2]
Call of Duty: Warzone / PlayStation / PS5 — Use/Reload: Square — Pick up items, open boxes, farm items, or reload ammunition [S3]
Call of Duty: Warzone / PlayStation / PS5 — Switch Weapon: Triangle — Swap weapons [S4]
Call of Duty: Warzone / PlayStation / PS5 — Campaign, Multiplayer or Co-Op specific: D-Pad — Optional commands depending on game mode such as ping or kill streak [S5]
Call of Duty: Warzone / PlayStation / PS5 — Scoreboard: Touch Pad — Open leaderboard and tactics map [S6]
Call of Duty: Warzone / PlayStation / PS5 — Pause: Options — Open settings menu and pause game [S7]
Call of Duty: Warzone / PlayStation / PS5 — Use Tactical Equipment: L1 — Use smoke grenades, flashbangs, or support devices [S8]
Call of Duty: Warzone / PlayStation / PS5 — Use Lethal Equipment: R1 — Use destruction explosives [S9]
Call of Duty: Warzone / PlayStation / PS5 — Aim Down Sight Behavior: L2 — Raise the weapon to aim down its sights. [S10]
Call of Duty: Warzone / PlayStation / PS5 — Fire Weapon: R2 — Pull the trigger to fire the weapon. [S11]
Call of Duty: Warzone / PlayStation / PS5 — Sprint/Tactical Sprint/Steady Aim: L3 — Press to sprint or hold breath while aiming through scope [S12]
Call of Duty: Warzone / PlayStation / PS5 — Melee: R3 — Strike with the butt of the weapon. [S13]
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.
Note: Battle Royale mode provides an option in the menu to swap L1/L2 and R1/R2 to suit the player.
```

**Source IDs ที่เลือก:** C05:controls_ps5_call_of_duty_warzone:binding_0:0, C05:controls_ps5_call_of_duty_warzone:binding_0:1, C05:controls_ps5_call_of_duty_warzone:binding_0:2, C05:controls_ps5_call_of_duty_warzone:binding_1:3, C05:controls_ps5_call_of_duty_warzone:binding_1:4, C05:controls_ps5_call_of_duty_warzone:binding_1:5, C05:controls_ps5_call_of_duty_warzone:binding_2:6, C05:controls_ps5_call_of_duty_warzone:binding_2:7, C05:controls_ps5_call_of_duty_warzone:binding_2:8, C05:controls_ps5_call_of_duty_warzone:binding_3:9, C05:controls_ps5_call_of_duty_warzone:binding_3:10, C05:controls_ps5_call_of_duty_warzone:binding_3:11, C05:controls_ps5_call_of_duty_warzone:binding_4:12, C05:controls_ps5_call_of_duty_warzone:binding_4:13, C05:controls_ps5_call_of_duty_warzone:binding_4:14, C05:controls_ps5_call_of_duty_warzone:binding_5:15, C05:controls_ps5_call_of_duty_warzone:binding_5:16, C05:controls_ps5_call_of_duty_warzone:binding_5:17, C05:controls_ps5_call_of_duty_warzone:binding_6:18, C05:controls_ps5_call_of_duty_warzone:binding_6:19, C05:controls_ps5_call_of_duty_warzone:binding_6:20, C05:controls_ps5_call_of_duty_warzone:binding_7:21, C05:controls_ps5_call_of_duty_warzone:binding_7:22, C05:controls_ps5_call_of_duty_warzone:binding_7:23, C05:controls_ps5_call_of_duty_warzone:binding_8:24, C05:controls_ps5_call_of_duty_warzone:binding_8:25, C05:controls_ps5_call_of_duty_warzone:binding_8:26, C05:controls_ps5_call_of_duty_warzone:binding_9:27, C05:controls_ps5_call_of_duty_warzone:binding_9:28, C05:controls_ps5_call_of_duty_warzone:binding_9:29, C05:controls_ps5_call_of_duty_warzone:binding_10:30, C05:controls_ps5_call_of_duty_warzone:binding_10:31, C05:controls_ps5_call_of_duty_warzone:binding_10:32, C05:controls_ps5_call_of_duty_warzone:binding_11:33, C05:controls_ps5_call_of_duty_warzone:binding_11:34, C05:controls_ps5_call_of_duty_warzone:binding_11:35, C05:controls_ps5_call_of_duty_warzone:binding_12:36, C05:controls_ps5_call_of_duty_warzone:binding_12:37, C05:controls_ps5_call_of_duty_warzone:binding_12:38, controls_ps5_call_of_duty_warzone

**เส้นทางเดิม:** pipeline:structured_game_controls_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate05_final_checks/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 13. 9efbf2ac

Please answer from verified studio information: May I record video inside the studio

**วิเคราะห์:** permission ถ่ายคน/ห้องยังไม่มี source ยืนยัน; คำอนุญาต capture ภาพในเกมไม่ได้ให้สิทธิ์ filming ภายในศูนย์โดยอัตโนมัติ

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Permission and conditions for photography or video recording in the studio have not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
No confirmed source is available for the requested detail.
```

**Source IDs ที่เลือก:** ไม่มี selected claim; ดูเหตุผล bounded response ใน JSON

**เส้นทางเดิม:** pipeline:user_service_facts; **เส้นทางใหม่:** pipeline:common_unconfirmed

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 14. a9ecf2e1

กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลที่ยืนยันได้หน่อยครับ: Maintenance คือช่วงไหน

**วิเคราะห์:** maintenance เป็น facet แยกจาก open_periods conflict; ไม่ทิ้งตาราง maintenance ที่ยืนยันได้

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
จันทร์ — ช่วงบำรุงรักษา: 09:00–12:00 [S1]
อังคาร — ช่วงบำรุงรักษา: ไม่มี / None [S2]
พุธ — ช่วงบำรุงรักษา: ไม่มี / None [S3]
พฤหัสบดี — ช่วงบำรุงรักษา: ไม่มี / None [S4]
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S5]
เสาร์ — ช่วงบำรุงรักษา: ไม่มี / None [S6]
อาทิตย์ — ช่วงบำรุงรักษา: ไม่มี / None [S7]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_0:maintenance_periods:0, C11:migrated_schedule_1:maintenance_periods:1, C11:migrated_schedule_2:maintenance_periods:2, C11:migrated_schedule_3:maintenance_periods:3, C11:migrated_schedule_4:maintenance_periods:4, C11:migrated_schedule_5:maintenance_periods:5, C11:migrated_schedule_6:maintenance_periods:6, migrated_schedule_0, migrated_schedule_1, migrated_schedule_2, migrated_schedule_3, migrated_schedule_4, migrated_schedule_5, migrated_schedule_6

**เส้นทางเดิม:** pipeline:source_operation_schedule_query; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 15. b2ff4f05

God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง

**วิเคราะห์:** อ่าน bindings ทั้งชุดพร้อม source coverage note; ไม่อ้างว่าได้ตรวจ preset เครื่องจริง

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
God of War Ragnarök มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    L: เคลื่อนที่ - บังคับทิศทางการเดิน
•    L3: วิ่งสปรินต์ - กดเพื่อวิ่ง
•    L3 + R3: พลังสปาร์ตัน - ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต
•    R: มุมกล้อง - ควบคุมการหมุนมุมกล้อง
•    R3: ล็อกเป้าหมาย - ล็อกเป้าหมายศัตรู
•    L2 (Hold): เล็ง (กดค้าง) - ง้างอาวุธเตรียมขว้าง
•    L1 (Hold): ป้องกัน (กดค้าง) - ยกโล่ขึ้นป้องกันการโจมตี และใช้เป็นปุ่มร่วมสำหรับคำสั่ง Runic/Relic
•    R1: โจมตีเบา / รูนเบา / ขว้าง - โจมตีปกติเบา, ขว้างอาวุธเมื่อกดเล็ง, หรือใช้ท่ารูนเบาเมื่อกดค้าง L1
•    R2: โจมตีหนัก / รูนหนัก - โจมตีปกติหนัก หรือใช้ท่ารูนหนักเมื่อกดค้าง L1
•    Triangle: เรียกขวานกลับ / ชาร์จพลังอาวุธ - เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1
•    Circle: โต้ตอบ / ใช้งานรีลิค - สำรวจสภาพแวดล้อม หรือใช้งานไอเทม Relic เมื่อกดค้าง L1
•    Square: คู่หูโจมตี - สั่งคู่หูยิงธนูสนับสนุน
•    Cross: สเตปหลบ / กลิ้งหลบ - กด 1 ครั้งเพื่อโยกตัวหลบ หรือกด 2 ครั้งติดเพื่อกลิ้งหลบ
•    D-Pad Right: ติดตั้งอาวุธหลัก - ชักขวาน Leviathan
•    D-Pad Left: ติดตั้งอาวุธรอง - ชักดาบโซ่ Blades of Chaos
•    D-Pad Down: ติดตั้งอาวุธที่สาม - ชักหอก Draupnir Spear
•    D-Pad Up: เปลี่ยนชนิดลูกธนู - สลับลูกธนูของคู่หู
•    Options: หยุดเกม - หยุดเกมและเปิดเมนูหลัก
•    Touch Pad: แผนที่ - เปิดแผนที่โลก
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/14
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
God of War Ragnarök / PlayStation / PS5 — เคลื่อนที่: L — บังคับทิศทางการเดิน [S1]
God of War Ragnarök / PlayStation / PS5 — วิ่งสปรินต์: L3 — กดเพื่อวิ่ง [S2]
God of War Ragnarök / PlayStation / PS5 — พลังสปาร์ตัน: L3 + R3 — ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต [S3]
God of War Ragnarök / PlayStation / PS5 — มุมกล้อง: R — ควบคุมการหมุนมุมกล้อง [S4]
God of War Ragnarök / PlayStation / PS5 — ล็อกเป้าหมาย: R3 — ล็อกเป้าหมายศัตรู [S5]
God of War Ragnarök / PlayStation / PS5 — เล็ง (กดค้าง): L2 (Hold) — ง้างอาวุธเตรียมขว้าง [S6]
God of War Ragnarök / PlayStation / PS5 — ป้องกัน (กดค้าง): L1 (Hold) — ยกโล่ขึ้นป้องกันการโจมตี และใช้เป็นปุ่มร่วมสำหรับคำสั่ง Runic/Relic [S7]
God of War Ragnarök / PlayStation / PS5 — โจมตีเบา / รูนเบา / ขว้าง: R1 — โจมตีปกติเบา, ขว้างอาวุธเมื่อกดเล็ง, หรือใช้ท่ารูนเบาเมื่อกดค้าง L1 [S8]
God of War Ragnarök / PlayStation / PS5 — โจมตีหนัก / รูนหนัก: R2 — โจมตีปกติหนัก หรือใช้ท่ารูนหนักเมื่อกดค้าง L1 [S9]
God of War Ragnarök / PlayStation / PS5 — เรียกขวานกลับ / ชาร์จพลังอาวุธ: Triangle — เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1 [S10]
God of War Ragnarök / PlayStation / PS5 — โต้ตอบ / ใช้งานรีลิค: Circle — สำรวจสภาพแวดล้อม หรือใช้งานไอเทม Relic เมื่อกดค้าง L1 [S11]
God of War Ragnarök / PlayStation / PS5 — คู่หูโจมตี: Square — สั่งคู่หูยิงธนูสนับสนุน [S12]
God of War Ragnarök / PlayStation / PS5 — สเตปหลบ / กลิ้งหลบ: Cross — กด 1 ครั้งเพื่อโยกตัวหลบ หรือกด 2 ครั้งติดเพื่อกลิ้งหลบ [S13]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธหลัก: D-Pad Right — ชักขวาน Leviathan [S14]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธรอง: D-Pad Left — ชักดาบโซ่ Blades of Chaos [S15]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธที่สาม: D-Pad Down — ชักหอก Draupnir Spear [S16]
God of War Ragnarök / PlayStation / PS5 — เปลี่ยนชนิดลูกธนู: D-Pad Up — สลับลูกธนูของคู่หู [S17]
God of War Ragnarök / PlayStation / PS5 — หยุดเกม: Options — หยุดเกมและเปิดเมนูหลัก [S18]
God of War Ragnarök / PlayStation / PS5 — แผนที่: Touch Pad — เปิดแผนที่โลก [S19]
ปุ่มชุดนี้มาจากแหล่งรอง ยังไม่ได้ตรวจยืนยันกับเวอร์ชันเกมและการตั้งค่าปุ่มของเครื่องที่ศูนย์ใช้อยู่จริง
หมายเหตุ: เกมมีระบบการกดปุ่มผสม โดยใช้ L1 (Block) และ L2 (Aim) เป็นปุ่ม Modifier เพื่อเปลี่ยน Action ของปุ่มอื่นๆ
```

**Source IDs ที่เลือก:** C05:controls_ps5_god_of_war_ragnar_k:binding_0:0, C05:controls_ps5_god_of_war_ragnar_k:binding_0:1, C05:controls_ps5_god_of_war_ragnar_k:binding_0:2, C05:controls_ps5_god_of_war_ragnar_k:binding_1:3, C05:controls_ps5_god_of_war_ragnar_k:binding_1:4, C05:controls_ps5_god_of_war_ragnar_k:binding_1:5, C05:controls_ps5_god_of_war_ragnar_k:binding_2:6, C05:controls_ps5_god_of_war_ragnar_k:binding_2:7, C05:controls_ps5_god_of_war_ragnar_k:binding_2:8, C05:controls_ps5_god_of_war_ragnar_k:binding_3:9, C05:controls_ps5_god_of_war_ragnar_k:binding_3:10, C05:controls_ps5_god_of_war_ragnar_k:binding_3:11, C05:controls_ps5_god_of_war_ragnar_k:binding_4:12, C05:controls_ps5_god_of_war_ragnar_k:binding_4:13, C05:controls_ps5_god_of_war_ragnar_k:binding_4:14, C05:controls_ps5_god_of_war_ragnar_k:binding_5:15, C05:controls_ps5_god_of_war_ragnar_k:binding_5:16, C05:controls_ps5_god_of_war_ragnar_k:binding_5:17, C05:controls_ps5_god_of_war_ragnar_k:binding_6:18, C05:controls_ps5_god_of_war_ragnar_k:binding_6:19, C05:controls_ps5_god_of_war_ragnar_k:binding_6:20, C05:controls_ps5_god_of_war_ragnar_k:binding_7:21, C05:controls_ps5_god_of_war_ragnar_k:binding_7:22, C05:controls_ps5_god_of_war_ragnar_k:binding_7:23, C05:controls_ps5_god_of_war_ragnar_k:binding_8:24, C05:controls_ps5_god_of_war_ragnar_k:binding_8:25, C05:controls_ps5_god_of_war_ragnar_k:binding_8:26, C05:controls_ps5_god_of_war_ragnar_k:binding_9:27, C05:controls_ps5_god_of_war_ragnar_k:binding_9:28, C05:controls_ps5_god_of_war_ragnar_k:binding_9:29, C05:controls_ps5_god_of_war_ragnar_k:binding_10:30, C05:controls_ps5_god_of_war_ragnar_k:binding_10:31, C05:controls_ps5_god_of_war_ragnar_k:binding_10:32, C05:controls_ps5_god_of_war_ragnar_k:binding_11:33, C05:controls_ps5_god_of_war_ragnar_k:binding_11:34, C05:controls_ps5_god_of_war_ragnar_k:binding_11:35, C05:controls_ps5_god_of_war_ragnar_k:binding_12:36, C05:controls_ps5_god_of_war_ragnar_k:binding_12:37, C05:controls_ps5_god_of_war_ragnar_k:binding_12:38, C05:controls_ps5_god_of_war_ragnar_k:binding_13:39, C05:controls_ps5_god_of_war_ragnar_k:binding_13:40, C05:controls_ps5_god_of_war_ragnar_k:binding_13:41, C05:controls_ps5_god_of_war_ragnar_k:binding_14:42, C05:controls_ps5_god_of_war_ragnar_k:binding_14:43, C05:controls_ps5_god_of_war_ragnar_k:binding_14:44, C05:controls_ps5_god_of_war_ragnar_k:binding_15:45, C05:controls_ps5_god_of_war_ragnar_k:binding_15:46, C05:controls_ps5_god_of_war_ragnar_k:binding_15:47, C05:controls_ps5_god_of_war_ragnar_k:binding_16:48, C05:controls_ps5_god_of_war_ragnar_k:binding_16:49, C05:controls_ps5_god_of_war_ragnar_k:binding_16:50, C05:controls_ps5_god_of_war_ragnar_k:binding_17:51, C05:controls_ps5_god_of_war_ragnar_k:binding_17:52, C05:controls_ps5_god_of_war_ragnar_k:binding_17:53, C05:controls_ps5_god_of_war_ragnar_k:binding_18:54, C05:controls_ps5_god_of_war_ragnar_k:binding_18:55, C05:controls_ps5_god_of_war_ragnar_k:binding_18:56, controls_ps5_god_of_war_ragnar_k

**เส้นทางเดิม:** pipeline:source_operation_control_lookup; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 16. f10707b2

กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า วันอังคารศูนย์เปิดกี่โมง

**วิเคราะห์:** วันอังคารเวลาเล่น09–12,13–16 แยกจาก dashboard open09–16

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
วันอังคาร: เปิดให้เล่น 09:00-12:00 และ 13:00-16:00

รายละเอียดจากตาราง:
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
อังคาร — ตารางให้บริการเล่น: เปิดให้บริการเล่นตามตาราง 09:00–12:00, 13:00–16:00 [S1]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_1:service_periods:0, migrated_schedule_1

**เส้นทางเดิม:** pipeline:structured_schedule; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 17. 00301c15

กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว

**วิเคราะห์:** คืน query profile จากข้อมูลเดิมให้เข้าถึงนโยบายระงับสิทธิ์ชั่วคราวพร้อมเงื่อนไข

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
แบนชั่วคราว: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S1]
```

**Source IDs ที่เลือก:** C10:migrated_faq_rule_penalty_temp_suspension:owner_policy:0, migrated_faq_rule_penalty_temp_suspension

**เส้นทางเดิม:** pipeline:protected_temporary_suspension; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 18. 0d05eaf6

How much does it cost for an adult to play VR for one hour?

**วิเคราะห์:** adult VR60 นาทีต้องเลือก rate60 ไม่ใช้30นาทีคูณโดยไม่มี declared arithmetic

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Service prices (recorded package rates):

VR — 60 minutes/package (1-5 people)
Requested duration: 60 minutes (1 hours); 1 session(s).
• General adults: 1,050 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB for 60 minutes [S1]
```

**Source IDs ที่เลือก:** C06:migrated_rate_vr_60_1_5_general_adult:amount:0, C06:migrated_rate_vr_60_1_5_general_adult:amount:1, C06:migrated_rate_vr_60_1_5_general_adult:amount:2, C06:migrated_rate_vr_60_1_5_general_adult:amount:3, C06:migrated_rate_vr_60_1_5_general_adult:amount:4, C06:migrated_rate_vr_60_1_5_general_adult:amount:5, migrated_rate_vr_60_1_5_general_adult

**เส้นทางเดิม:** pipeline:structured_service_fee_conversation; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 19. 0f5e0fd0

กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม

**วิเคราะห์:** R03ตีคำถามมีเมาส์ไหมเป็น list และเตือนความครบเกินจำเป็น; R05แก้เป็น detail ของอุปกรณ์ที่ผูก source ได้ ไม่ยืนยันเครื่องว่างจริง

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
มีอุปกรณ์ที่ยืนยันได้ดังนี้ครับ
•    Gaming Mouse อยู่ใน PC Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Gaming Mouse — การใช้งาน: เมาส์สำหรับเล่นเกมบน Gaming PC
ใช้งานกับ PC ที่จองไว้ และควรแจ้งเจ้าหน้าที่หากคลิกไม่ติด เซนเซอร์รวน หรือพบความเสียหาย
ควบคุมเกม PC โดยเฉพาะเกม FPS/MOBA [S1]
```

**Source IDs ที่เลือก:** C03:equipment_gaming_mouse:usage:0, equipment_gaming_mouse

**เส้นทางเดิม:** pipeline:equipment_availability_fast_path; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 20. 104194c2

หำลังจะลงแข่ง VALORANT อยากรู้เรื่องบทลงโทษ

**วิเคราะห์:** teacherอ่านเพียงบางโทษ; ใหม่อ่าน source section family ครบ5ประเภทพร้อมขอบเขตรายการแข่ง

**ผลใหม่ที่แสดง:** candidate05_final_checks / R04 targeted CLI

**คำตอบเดิมจริง**

```text
คำตอบ: ประเภทบทลงโทษในเกม

รายละเอียดที่เกี่ยวข้อง:
•    5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)
•    3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม [S1]
PSU Phuket VALORANT 2026 Tournament — 1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ [S2]
PSU Phuket VALORANT 2026 Tournament — 2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้ [S3]
PSU Phuket VALORANT 2026 Tournament — 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ [S4]
PSU Phuket VALORANT 2026 Tournament — 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น [S5]
PSU Phuket VALORANT 2026 Tournament — 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing) [S6]
```

**Source IDs ที่เลือก:** C13:competition_competition_rules_valorant_psu_phuket_2026_section_010:rule_clause:0, C13:competition_competition_rules_valorant_psu_phuket_2026_section_011:rule_clause:1, C13:competition_competition_rules_valorant_psu_phuket_2026_section_011:rule_clause:2, C13:competition_competition_rules_valorant_psu_phuket_2026_section_012:rule_clause:3, C13:competition_competition_rules_valorant_psu_phuket_2026_section_012:rule_clause:4, C13:competition_competition_rules_valorant_psu_phuket_2026_section_013:rule_clause:5, C13:competition_competition_rules_valorant_psu_phuket_2026_section_013:rule_clause:6, C13:competition_competition_rules_valorant_psu_phuket_2026_section_014:rule_clause:7, C13:competition_competition_rules_valorant_psu_phuket_2026_section_014:rule_clause:8, C13:competition_competition_rules_valorant_psu_phuket_2026_section_015:rule_clause:9, C13:competition_competition_rules_valorant_psu_phuket_2026_section_015:rule_clause:10, competition_competition_rules_valorant_psu_phuket_2026_section_010, competition_competition_rules_valorant_psu_phuket_2026_section_011, competition_competition_rules_valorant_psu_phuket_2026_section_012, competition_competition_rules_valorant_psu_phuket_2026_section_013, competition_competition_rules_valorant_psu_phuket_2026_section_014, competition_competition_rules_valorant_psu_phuket_2026_section_015

**เส้นทางเดิม:** pipeline:competition_source_rag; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate05_final_checks/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 21. 11f9129c

รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องพบปัญหา เครื่อง

**วิเคราะห์:** คืน profile คำถามพบปัญหาเครื่องให้เลือกแจ้งเจ้าหน้าที่จาก native policy

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
หากพบปัญหาการใช้งานหรือเครื่องมีปัญหา โปรดแจ้งเจ้าหน้าที่ทันที
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
หากพบปัญหาการใช้งาน พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ ควรแจ้งเจ้าหน้าที่ทันที [S1]
```

**Source IDs ที่เลือก:** C10:migrated_faq_rule_report_problem:owner_policy:0, migrated_faq_rule_report_problem

**เส้นทางเดิม:** pipeline:rules_fast_path; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 22. 1f7c4f9a

ขอสอบถามหน่อยครับ New Super Mario Bros. U Deluxe เล่นได้ที่โซนไหน

**วิเคราะห์:** เกม→โซน Nintendo จาก offering; ไม่เดาจากชื่อแพลตฟอร์ม

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ได้ครับ New Super Mario Bros. U Deluxe เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons)
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
New Super Mario Bros. U Deluxe — โซนที่ยืนยันว่ามีเกมนี้: Nintendo Switch Zone [S1]
```

**Source IDs ที่เลือก:** C04:game_detail_new_super_mario_bros:zone:0, C04:game_detail_new_super_mario_bros:zone:1, C04:game_detail_new_super_mario_bros:zone:2, C04:game_detail_new_super_mario_bros:zone:3, C04:game_detail_new_super_mario_bros:zone:4, C04:game_detail_new_super_mario_bros:zone:5, C04:game_detail_new_super_mario_bros:zone:6, C04:game_detail_new_super_mario_bros:zone:7, C04:game_detail_new_super_mario_bros:zone:8, C04:game_detail_new_super_mario_bros:zone:9, C04:game_detail_new_super_mario_bros:zone:10, game_detail_new_super_mario_bros

**เส้นทางเดิม:** pipeline:structured_service_game_availability; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 23. 2204b0a8

ขอข้อมูลเรื่องวันศุกร์ maintenance

**วิเคราะห์:** ศุกร์ maintenance13–16 ใช้ source calendar facet ตรง

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_4:maintenance_periods:0, migrated_schedule_4

**เส้นทางเดิม:** pipeline:source_operation_schedule_query; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 24. 2c110689

ขอสอบถามหน่อยครับ ขอข้อมูลที่ยืนยันได้หน่อยครับ: pc2 available ตอน 3pm ไหม

**วิเคราะห์:** R03 binding effective ถูกเทียบกับ semantic date21ก่อนbindingcreated23จน false mapping gap; R04แยก binding/freshness clock เป็น wall clock และเก็บ booking date แยก; ผล live ต่างเวลาห้ามเทียบเป็น accuracy

**ผลใหม่ที่แสดง:** candidate05_final_checks / R04 targeted CLI

**คำตอบเดิมจริง**

```text
วันที่ตรวจสอบ: 2026-10-21 (เวลาไทย)
PC #02 (1 Person) ถูกจองในช่วง 15:00-16:00 น. (เวลาไทย) ครับ
อัปเดต: 2026-10-23 16:14:00
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
วันที่ตรวจสอบ: 2026-10-21 (เวลาไทย)
PC #02 (1 Person) ถูกจองในช่วง 15:00-16:00 น. (เวลาไทย) ครับ
อัปเดต: 2026-10-23 17:35:17
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**Source IDs ที่เลือก:** ไม่มี selected claim; ดูเหตุผล bounded response ใน JSON

**เส้นทางเดิม:** pipeline:live_booking_status_fast_path; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate05_final_checks/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 25. 2ee7827c

What position does Ms. Kamlawan Nuansai hold

**วิเคราะห์:** ชื่ออังกฤษกับ role ผูก native profile ได้; source-version difference และ recorded role ไม่ยืนยันปัจจุบันทุกกรณี

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
I could not verify a member record for Ms. Kamlawan Nuansai. Please provide the exact name from the official member directory; I cannot infer an official identity from an unverified English spelling.
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
According to the recorded source profile:
นางสาวกมลวรรณ นวลสาย — role: Committee member [S1]
```

**Source IDs ที่เลือก:** C02:member_18a751d710b9b30c:role:0, member_18a751d710b9b30c

**เส้นทางเดิม:** pipeline:member_person_not_found_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 26. 3020765f

ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ

**วิเคราะห์:** ใช้ canonical center address เก็บอาคาร5ชั้น1ไม่ตกจาก generic FAQ

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
PSU Esports Studio - Phuket — ที่อยู่: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
```

**Source IDs ที่เลือก:** C01:center_psu_phuket:address:0, center_psu_phuket

**เส้นทางเดิม:** pipeline:user_service_facts; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 27. 36c23990

กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ

**วิเคราะห์:** booking procedure มีหลาย source variants; ตอบข้อความที่มีแต่ยัง wordy/partial ไม่อ้างว่ามี authority reconciliation สมบูรณ์แล้ว

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
พบข้อความขั้นตอนการจองหลายฉบับ ด้านล่างคงข้อความแต่ละฉบับไว้ ยังไม่ได้รวมเป็นนโยบายฉบับเดียว
วิธีจอง: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S1]
ขั้นตอนการจอง: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S2]
```

**Source IDs ที่เลือก:** C08:migrated_faq_rule_booking_steps:owner_policy:0, C08:migrated_faq_curated_booking_steps:owner_policy:1, migrated_faq_rule_booking_steps, migrated_faq_curated_booking_steps

**เส้นทางเดิม:** pipeline:structured_reservation_fact; **เส้นทางใหม่:** pipeline:common_partial_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 28. 3a769b08

กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า VALORANT คือเกมอะไร

**วิเคราะห์:** เลือก game summary ไม่ใช่บริการ/controls

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ
แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5
วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

**Source IDs ที่เลือก:** C04:game_detail_valorant:summary:0, game_detail_valorant

**เส้นทางเดิม:** pipeline:structured_game_detail; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 29. 3cc3c5c3

What does the Shift + Q / W / E / R button do in League of Legends on PC

**วิเคราะห์:** R03 single-letter parser เลือก R ท้าย Shift+Q/W/E/R; R04เลือก whole recorded compound ก่อน single key ยืนยันผ่าน API

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
League of Legends controls:
- Shift + Q / W / E / R: Quick cast abilities
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://dignitas.gg/articles/blogs/Unknown/8721/improving-inputs-effective-keybinds-for-lol
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.
Note: Riot support confirms hotkeys can be reset/managed, but the detailed default notes here rely on a secondary esports guide. Verify against the local League client before marking complete.
```

**Source IDs ที่เลือก:** C05:controls_pc_league_of_legends:binding_2:0, C05:controls_pc_league_of_legends:binding_2:1, C05:controls_pc_league_of_legends:binding_2:2, controls_pc_league_of_legends

**เส้นทางเดิม:** pipeline:structured_game_controls_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 30. 3df1eea3

Please answer from verified studio information: Which zone has the Gaming Chair

**วิเคราะห์:** อุปกรณ์→location PC Zone จาก current native record

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Verified equipment record: Gaming Chair is listed in PC Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Gaming Chair — location: PC Zone [S1]
```

**Source IDs ที่เลือก:** C03:equipment_gaming_chair:location:0, equipment_gaming_chair

**เส้นทางเดิม:** pipeline:structured_equipment_item_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 31. 4b0fb4a4

I am preparing for a AOV match. What is the policy for competition equipment and devices

**วิเคราะห์:** explicit AOV competition context ต้องอ่านอุปกรณ์การแข่งขันพร้อมข้อห้าม/เงื่อนไขจาก event เดียว

**ผลใหม่ที่แสดง:** candidate05_final_checks / R04 targeted CLI

**คำตอบเดิมจริง**

```text
Answer: 5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Blueket Games 2025 Men's Team — 5. Competition kits and equipment: 5. Competition kits and equipment
5.1. Personal mobile phones and internet access, and/or university-provided internet
5.2. Power adapters and personal charging devices
5.3. Tablets or iPads, as well as any other equipment other than a mobile phone (Mobile Phone), are not permitted for use during competition. If detected, the team will be immediately disqualified [S1]
```

**Source IDs ที่เลือก:** C13:competition_competition_rules_rov_blueket_2025_men_section_010:rule_clause:0, competition_competition_rules_rov_blueket_2025_men_section_010

**เส้นทางเดิม:** pipeline:structured_competition_rules_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate05_final_checks/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 32. 546c4490

How much does Beat Saber cost

**วิเคราะห์:** Beat Saber→VR rates แสดง audience/duration options ไม่เดาราคาหนึ่งเดียวเมื่อโจทย์ไม่ระบุ

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
The question does not specify the duration, so both verified packages are shown.
VR - 30 minutes (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 190 THB
- General adults: 525 THB
VR - 1 hour (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 375 THB
- General adults: 1,050 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 30 minutes [S1]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB per person for 30 minutes [S2]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S3]
VR Station 1 ชั่วโมง / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — per-person price for the rate duration: 375 THB per person for 60 minutes [S5]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S6]
```

**Source IDs ที่เลือก:** C06:migrated_rate_vr_30_1_5_psu_student_staff:amount:0, C06:migrated_rate_vr_30_1_5_psu_student_staff:amount:1, C06:migrated_rate_vr_30_1_5_psu_student_staff:amount:2, C06:migrated_rate_vr_30_1_5_psu_student_staff:amount:3, C06:migrated_rate_vr_30_1_5_psu_student_staff:amount:4, C06:migrated_rate_vr_30_1_5_psu_student_staff:amount:5, C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:amount:6, C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:amount:7, C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:amount:8, C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:amount:9, C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:amount:10, C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:amount:11, C06:migrated_rate_vr_30_1_5_general_adult:amount:12, C06:migrated_rate_vr_30_1_5_general_adult:amount:13, C06:migrated_rate_vr_30_1_5_general_adult:amount:14, C06:migrated_rate_vr_30_1_5_general_adult:amount:15, C06:migrated_rate_vr_30_1_5_general_adult:amount:16, C06:migrated_rate_vr_30_1_5_general_adult:amount:17, C06:migrated_rate_vr_60_1_5_psu_student_staff:amount:18, C06:migrated_rate_vr_60_1_5_psu_student_staff:amount:19, C06:migrated_rate_vr_60_1_5_psu_student_staff:amount:20, C06:migrated_rate_vr_60_1_5_psu_student_staff:amount:21, C06:migrated_rate_vr_60_1_5_psu_student_staff:amount:22, C06:migrated_rate_vr_60_1_5_psu_student_staff:amount:23, C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount:24, C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount:25, C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount:26, C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount:27, C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount:28, C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount:29, C06:migrated_rate_vr_60_1_5_general_adult:amount:30, C06:migrated_rate_vr_60_1_5_general_adult:amount:31, C06:migrated_rate_vr_60_1_5_general_adult:amount:32, C06:migrated_rate_vr_60_1_5_general_adult:amount:33, C06:migrated_rate_vr_60_1_5_general_adult:amount:34, C06:migrated_rate_vr_60_1_5_general_adult:amount:35, migrated_rate_vr_30_1_5_psu_student_staff, migrated_rate_vr_30_1_5_psu_alumni_general_student, migrated_rate_vr_30_1_5_general_adult, migrated_rate_vr_60_1_5_psu_student_staff, migrated_rate_vr_60_1_5_psu_alumni_general_student, migrated_rate_vr_60_1_5_general_adult

**เส้นทางเดิม:** pipeline:structured_service_fee_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 33. 5b2d0e13

Can I play Beat Saber in the VR Zone? Please answer briefly

**วิเคราะห์:** presence ในโซนที่ระบุอ่าน offering ตรง ไม่ใช่ live vacancy

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Beat Saber is available on: VR Station 30 minutes, VR Station 1 hour. Studio zone(s): VR Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Beat Saber — confirmed studio zones offering this game: VR Zone [S1]
```

**Source IDs ที่เลือก:** C04:game_detail_beat_saber:zone:0, C04:game_detail_beat_saber:zone:1, C04:game_detail_beat_saber:zone:2, C04:game_detail_beat_saber:zone:3, C04:game_detail_beat_saber:zone:4, C04:game_detail_beat_saber:zone:5, C04:game_detail_beat_saber:zone:6, C04:game_detail_beat_saber:zone:7, C04:game_detail_beat_saber:zone:8, C04:game_detail_beat_saber:zone:9, C04:game_detail_beat_saber:zone:10, game_detail_beat_saber

**เส้นทางเดิม:** pipeline:structured_game_availability_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 34. 69812416

ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ตอนนี้ศูนย์เปิดมั้ย

**วิเคราะห์:** เปิดตอนนี้เป็น recorded play calendar ไม่ใช่ live machine occupancy; runtimeจริงใช้วัน23 ส่วน CLI reference21 จึงไม่เทียบคำตอบ literalข้ามclock

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
ตอนนี้ยังเล่นไม่ได้ครับ รอบเปิดถัดไปของวันนี้คือ Afternoon 13:00-16:00
เวลาระบบ: 12:00 น. วันที่ 21/10/2026 (วันพุธ) ตามเวลาไทย

ตารางประจำที่ใช้ตรวจ:
•    วันจันทร์: 09:00-12:00 Maintenance*, 13:00-16:00 เปิดให้บริการ
•    วันอังคาร-พฤหัสบดี: 09:00-12:00 และ 13:00-16:00 เปิดให้บริการ
•    วันศุกร์: 09:00-12:00 เปิดให้บริการ, 13:00-16:00 Maintenance
•    วันหยุด/วันปิดพิเศษของศูนย์จะดูจากไฟล์ปิดบริการก่อนตารางประจำ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
ศุกร์ — ตารางให้บริการเล่น: วันที่ 2026-10-23 อยู่นอกช่วงให้บริการเล่นที่บันทึกไว้ [S1]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_4:service_periods:0, migrated_schedule_4

**เส้นทางเดิม:** pipeline:current_service_slot_fast_path; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 35. 6d26c7fe

Can I cancel my booking? Please use verified information

**วิเคราะห์:** cancellation policy ตามเวลาแจ้งล่วงหน้า ไม่เพิ่มrefund/rescheduleเอง

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Cancellations must be made at least 1 hour in advance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Cancel reservation: Cancellation of reservations must be made at least 1 hour in advance. [S1]
```

**Source IDs ที่เลือก:** C08:migrated_faq_curated_cancel_1_hour:owner_policy:0, migrated_faq_curated_cancel_1_hour

**เส้นทางเดิม:** pipeline:rule_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 36. 6f6cb1e0

ขอสอบถามหน่อยครับ Gaming Keyboard อยู่โซนไหน

**วิเคราะห์:** keyboard→location source

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Gaming Keyboard: คีย์บอร์ดสำหรับควบคุมเกมและพิมพ์บน Gaming PC
อยู่ที่: PC Zone
ใช้สำหรับ:
•    ควบคุมเกม PC
•    พิมพ์ข้อมูล
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

**Source IDs ที่เลือก:** C03:equipment_gaming_keyboard:location:0, equipment_gaming_keyboard

**เส้นทางเดิม:** pipeline:structured_equipment_item; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 37. 790d4406

กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันจันทร์เช้าเปิดหรือปิด

**วิเคราะห์:** จันทร์เช้า maintenance09–12 ไม่อนุมานจาก dashboard open12–16 ว่ารอบเล่นเริ่ม12

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
วันจันทร์: เปิดให้เล่นช่วง 13:00-16:00 ส่วน 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
จันทร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 09:00–12:00 เนื่องจากบำรุงรักษาตามตาราง [S1]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_0:service_periods:0, migrated_schedule_0

**เส้นทางเดิม:** pipeline:structured_schedule; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 38. 83ff647f

Do I need to check in before playing VALORANT?

**วิเคราะห์:** teacherสับสน checkin เล่นVALORANT กับ checkinการแข่งขัน; ใหม่เลือก studio checkin action ก่อนgame context

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Answer: Teams must arrive at the venue at least 30 minutes before the scheduled match time.

Details:
• No more than 6 players are allowed in the match preparation area.
• The team captain is allowed to bring documents, which must be submitted to the referee before the match.
• Personnel: During Match Prep, no more than 6 players may be present.
• Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.
• Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Check-in in advance: Users must check in before the scheduled round starts. They may check in up to 30 minutes early, and must check in prior to the round's start time. [S1]
Check-in in advance: Check-in is available up to 30 minutes before the reserved time slot, and users must check in before the slot begins. [S2]
```

**Source IDs ที่เลือก:** C08:migrated_faq_curated_checkin_30_minutes:owner_policy:0, C08:migrated_faq_rule_checkin_advance:owner_policy:1, migrated_faq_curated_checkin_30_minutes, migrated_faq_rule_checkin_advance

**เส้นทางเดิม:** pipeline:structured_competition_rules_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 39. 88b3a23b

Could you please help me with this: I am planning a visit and nee to know: What GPU model is inside the PCs

**วิเคราะห์:** native GPU sourceใหม่RTX5060; teacherไม่มีคำยืนยันเดียวกัน จึงไม่ใช่ causal gainจากFlowล้วน

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
The published equipment record does not verify the GPU model inside the studio PCs.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Gaming PC Model MSI MAG Infinite S3 14th — specifications: GPU: NVIDIA GeForce RTX 5060 8GB [S1]
```

**Source IDs ที่เลือก:** C03:equipment_gaming_pc:specifications:0, equipment_gaming_pc

**เส้นทางเดิม:** pipeline:equipment_spec_unverified_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 40. 8acac2d3

What does the R2 button do in God of War Ragnarök on PlayStation / PS5

**วิเคราะห์:** R2ตรงแพลตฟอร์มและmodifier L1; เก็บคำเตือนsecondary source/installed preset

**ผลใหม่ที่แสดง:** candidate05_final_checks / R04 targeted CLI

**คำตอบเดิมจริง**

```text
God of War Ragnarok controls:
- R2: Heavy Attack / Heavy Runic Attack (While blocking)
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/14
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
God of War Ragnarök / PlayStation / PS5 — Heavy Attack / Heavy Runic Attack (While blocking): R2 — Heavy attack or perform Heavy Rune move with L1 held [S1]
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.
Note: The game supports button combinations, using L1 (Block) and L2 (Aim) as Modifier buttons that change the Action of other buttons.
```

**Source IDs ที่เลือก:** C05:controls_ps5_god_of_war_ragnar_k:binding_8:0, C05:controls_ps5_god_of_war_ragnar_k:binding_8:1, C05:controls_ps5_god_of_war_ragnar_k:binding_8:2, controls_ps5_god_of_war_ragnar_k

**เส้นทางเดิม:** pipeline:structured_game_controls_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate05_final_checks/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 41. 96ef8f71

Could you please help me with this: Do you have Hades II

**วิเคราะห์:** HadesIIไม่มี sourceยืนยัน ไม่ควรแทนเกมใกล้ชื่อหรือสรุปไม่มีบริการถาวร

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
I could not find Hades II in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
No confirmed source is available for the requested detail.
```

**Source IDs ที่เลือก:** ไม่มี selected claim; ดูเหตุผล bounded response ใน JSON

**เส้นทางเดิม:** pipeline:games_unknown_target_en; **เส้นทางใหม่:** pipeline:common_unconfirmed

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 42. 981fa8d4

ขอข้อมูลเรื่องอยู่ที่หน

**วิเคราะห์:** fragmentที่อยู่แบบไม่มี referent อื่นใช้ center address; unknown named subject มี guard ไม่ตอบที่อยู่ศูนย์แทน

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
PSU Esports Studio - Phuket — ที่อยู่: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
```

**Source IDs ที่เลือก:** C01:center_psu_phuket:address:0, center_psu_phuket

**เส้นทางเดิม:** pipeline:candidate_margin_clarification; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 43. 9be5826b

Counter-Strike 2 map pool ในกติกาคืออะไร

**วิเคราะห์:** R03 map poolถูกตีC03; R04ให้event-ruleก่อนequipment และอ่านheading+numberedchild7maps ไม่รับheadingล้วนเป็นคำตอบครบ

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
คำตอบ: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
PSU Phuket CS2 2026 Tournament — 3. แผนที่ในการแข่งขัน [S1]
PSU Phuket CS2 2026 Tournament — 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN [S2]
```

**Source IDs ที่เลือก:** C13:competition_competition_rules_cs2_psu_phuket_2026_section_028:rule_clause:0, C13:competition_competition_rules_cs2_psu_phuket_2026_section_029:rule_clause:1, C13:competition_competition_rules_cs2_psu_phuket_2026_section_029:rule_clause:2, competition_competition_rules_cs2_psu_phuket_2026_section_028, competition_competition_rules_cs2_psu_phuket_2026_section_029

**เส้นทางเดิม:** pipeline:competition_rule_detail_source; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 44. 9db7acd1

What does the X button do in The Legend of Zelda: Breath of the Wild on Nintendo Switch

**วิเคราะห์:** รองรับ X buttonและbutton X โดยเลือกbindingจริง ไม่ไปgamepresence

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
The Legend of Zelda: Breath of the Wild controls:
- X: Jump / Dodge (While locked)
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/31
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.
```

**Source IDs ที่เลือก:** C05:controls_nintendo_the_legend_of_zelda_breath_of_the_wild:binding_6:0, C05:controls_nintendo_the_legend_of_zelda_breath_of_the_wild:binding_6:1, controls_nintendo_the_legend_of_zelda_breath_of_the_wild

**เส้นทางเดิม:** pipeline:structured_game_controls_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 45. a1c90b6e

Which studio zone has The Last of Us Part I / Part II

**วิเคราะห์:** PartI/PartIIแยกเป้าหมาย; PartIIฐานยังไม่มีofferingedgeที่เท่ากับRemastered จึงคงpartial ไม่รวมeditionเอง

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
The Last of Us Part I / Part II is listed in: PlayStation 5 Zone.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
The Last of Us Part I — confirmed studio zones offering this game: PlayStation 5 Zone [S1]
Zone relations still unconfirmed for: The Last of Us Part II
```

**Source IDs ที่เลือก:** C04:migrated_game_the_last_of_us_part_i:zone:0, C04:migrated_game_the_last_of_us_part_i:zone:1, C04:migrated_game_the_last_of_us_part_i:zone:2, C04:migrated_game_the_last_of_us_part_i:zone:3, C04:migrated_game_the_last_of_us_part_i:zone:4, C04:migrated_game_the_last_of_us_part_i:zone:5, C04:migrated_game_the_last_of_us_part_i:zone:6, C04:migrated_game_the_last_of_us_part_i:zone:7, C04:migrated_game_the_last_of_us_part_i:zone:8, migrated_game_the_last_of_us_part_i

**เส้นทางเดิม:** pipeline:structured_game_zone_en; **เส้นทางใหม่:** pipeline:common_partial_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 46. a87e6d58

Could you please help me with this: How much does Cockpit cost

**วิเคราะห์:** Cockpit ratesทุกaudienceตามsource เมื่อไม่ระบุผู้ใช้ ไม่เลือกแพ็กเกจเหมาแทน

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Service prices (recorded package rates):

Cockpit — 60 minutes/package (1 person)
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 65 THB/package
• General adults: 200 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

**Source IDs ที่เลือก:** C06:migrated_rate_cockpit_60_1_1_psu_student_staff:amount:0, C06:migrated_rate_cockpit_60_1_1_psu_student_staff:amount:1, C06:migrated_rate_cockpit_60_1_1_psu_student_staff:amount:2, C06:migrated_rate_cockpit_60_1_1_psu_student_staff:amount:3, C06:migrated_rate_cockpit_60_1_1_psu_student_staff:amount:4, C06:migrated_rate_cockpit_60_1_1_psu_student_staff:amount:5, C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount:6, C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount:7, C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount:8, C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount:9, C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount:10, C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount:11, C06:migrated_rate_cockpit_60_1_1_general_adult:amount:12, C06:migrated_rate_cockpit_60_1_1_general_adult:amount:13, C06:migrated_rate_cockpit_60_1_1_general_adult:amount:14, C06:migrated_rate_cockpit_60_1_1_general_adult:amount:15, C06:migrated_rate_cockpit_60_1_1_general_adult:amount:16, C06:migrated_rate_cockpit_60_1_1_general_adult:amount:17, migrated_rate_cockpit_60_1_1_psu_student_staff, migrated_rate_cockpit_60_1_1_psu_alumni_general_student, migrated_rate_cockpit_60_1_1_general_adult

**เส้นทางเดิม:** pipeline:structured_service_fee_conversation; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 47. aefe9911

ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ครับ

**วิเคราะห์:** fragmentเครื่องดื่มพื้นที่อ่านconsumption policyไม่ใช่bring permission

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
อาหารและเครื่องดื่ม: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

**Source IDs ที่เลือก:** C10:migrated_faq_curated_rule_food_drinks:owner_policy:0, migrated_faq_curated_rule_food_drinks

**เส้นทางเดิม:** pipeline:protected_food_consumption; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 48. b32fb6ba

รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ศุกร์บ่ายเปิดไหม

**วิเคราะห์:** ศุกร์บ่ายmaintenance13–16 ไม่ใช้rawopen_periodsที่ขัดกันตอบ

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
วันศุกร์: เปิดให้เล่นช่วง 09:00-12:00 ส่วน 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
ศุกร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 13:00–16:00 เนื่องจากบำรุงรักษาตามตาราง [S1]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_4:service_periods:0, migrated_schedule_4

**เส้นทางเดิม:** pipeline:structured_schedule; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 49. c43bbed1

ขอสอบถามหน่อยครับ บุคคลทั่วไป เล่น PC 1 ชั่วโมง เสียกี่บาท

**วิเคราะห์:** PC70บาท/60นาทีสำหรับGeneralAdult พร้อมsourceconfirmationและรายการPCที่มีrateเท่ากัน

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
ระยะเวลาที่ถาม 60 นาที (1 ชั่วโมง) คิดเป็น 1 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที [S1]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที [S2]
```

**Source IDs ที่เลือก:** C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:0, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:1, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:2, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:3, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:4, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:5, C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount:6, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:7, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:8, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:9, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:10, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:11, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:12, C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount:13, rate_recovered_pc_availability_pc_01_02_general_adult, rate_recovered_pc_availability_pc_03_10_general_adult

**เส้นทางเดิม:** pipeline:structured_service_fee_conversation; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 50. c8d9c78f

Could you please help me with this: Is it open on Sundays

**วิเคราะห์:** Sunday regular play closed ตามตาราง ไม่ใช่ยืนยันspecialevent/liveทุกกรณี

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Sunday: no regular service period is listed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Sunday — regular play-service timetable: Closed for play under the regular timetable. [S1]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_6:service_periods:0, migrated_schedule_6

**เส้นทางเดิม:** pipeline:structured_schedule_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 51. da13326d

ขอข้อมูลเรื่องนินเทนโด overcooked

**วิเคราะห์:** R03ตอบNintendo catalogueกว้างเกินโจทย์; alias overcookedชนOvercooked!กับOvercooked2 แก้R05ถามeditionจากชื่อในsource ไม่เลือกแทน

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
Overcooked มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องข้อมูลเกม ขอเลือกเกมก่อน:
•    Overcooked! (Nintendo Switch Zone)
•    Overcooked! 2 (Nintendo Switch Zone)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
หมายถึงเกมรุ่นใดครับ: Overcooked 2 / Overcooked!?
```

**Source IDs ที่เลือก:** ไม่มี selected claim; ดูเหตุผล bounded response ใน JSON

**เส้นทางเดิม:** pipeline:ambiguity_clarification; **เส้นทางใหม่:** pipeline:common_clarification

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 52. df43bd38

Which studio zone has Little Nightmares II

**วิเคราะห์:** LittleNightmaresII→NintendoZoneจากoffering; controlsPS5sourceไม่ได้เป็นหลักฐานว่ามีPS5serviceติดตั้งเกมนี้

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Little Nightmares II is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Little Nightmares II — confirmed studio zones offering this game: Nintendo Switch Zone [S1]
```

**Source IDs ที่เลือก:** C04:game_detail_little_nightmares_2:zone:0, C04:game_detail_little_nightmares_2:zone:1, C04:game_detail_little_nightmares_2:zone:2, C04:game_detail_little_nightmares_2:zone:3, C04:game_detail_little_nightmares_2:zone:4, C04:game_detail_little_nightmares_2:zone:5, C04:game_detail_little_nightmares_2:zone:6, C04:game_detail_little_nightmares_2:zone:7, C04:game_detail_little_nightmares_2:zone:8, C04:game_detail_little_nightmares_2:zone:9, C04:game_detail_little_nightmares_2:zone:10, game_detail_little_nightmares_2

**เส้นทางเดิม:** pipeline:structured_game_availability_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 53. e7a3582e

ช่วยอธิบายให้เข้าใจง่ายหน่อยว่า ขอข้อมูลเรื่องของหาย อุปกรณ์ เปียก

**วิเคราะห์:** คืนprofileข้อความของหาย/อุปกรณ์เปียก รักษาเงื่อนไขความรับผิดตามsource

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
กรณีทรัพย์สินส่วนตัวสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี ส่วนกรณีทำอุปกรณ์เสียหายหรือเปียก ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย [S1]
```

**Source IDs ที่เลือก:** C10:migrated_faq_rule_mixed_lost_and_damage:owner_policy:0, migrated_faq_rule_mixed_lost_and_damage

**เส้นทางเดิม:** pipeline:protected_studio_rule_direct; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 54. e8694671

Who holds te role of ประธาน

**วิเคราะห์:** inverse role→peopleจากnativepublicprofile ไม่สลับชื่อกับหน้าที่

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- นายษุภากรณ์ จิราจินดากุล: Chairperson (ประธาน)
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
According to the recorded source profile:
นายษุภากรณ์ จิราจินดากุล — role: Chair [S1]
```

**Source IDs ที่เลือก:** C02:member_1d884f11f3890dea:role:0, member_1d884f11f3890dea

**เส้นทางเดิม:** pipeline:structured_members_source_th; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 55. eafe23b9

ปุ่มของ New Super Mario Bros. U Deluxe มีอะไรบ้าง

**วิเคราะห์:** sourceมีเพียงpartialofficial ไม่ใช่fullbuttonlayout; R04เปลี่ยนterminalเป็นpartial แม้ส่งครบrowsที่มี

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
New Super Mario Bros. U Deluxe มีข้อมูลปุ่มควบคุมดังนี้:
Nintendo Switch
•    One Joy-Con: ควบคุมตัวละครด้วย Joy-Con เดี่ยว - หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน
•    Simple controls: วิ่ง กระโดด และเหยียบศัตรู - หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม
แหล่งข้อมูล: https://www.nintendo.com/sg/switch/adal/index.html
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
แหล่งข้อมูลระบุวิธีควบคุมเพียงบางส่วน ยังไม่มีผังปุ่มครบชุดที่ยืนยันได้
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
New Super Mario Bros. U Deluxe / Nintendo Switch — วิ่ง กระโดด และเหยียบศัตรู: Simple controls — หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม [S2]
หมายเหตุ: หน้าอย่างเป็นทางการของ Nintendo ยืนยันการควบคุมที่เรียบง่ายและการใช้ Joy-Con หนึ่งข้าง แต่ไม่ได้ให้ผังปุ่มครบทุกปุ่มในหน้าสาธารณะ
```

**Source IDs ที่เลือก:** C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_0:0, C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_0:1, C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_0:2, C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_1:3, C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_1:4, C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_1:5, controls_nintendo_new_super_mario_bros_u_deluxe

**เส้นทางเดิม:** pipeline:source_operation_control_lookup; **เส้นทางใหม่:** pipeline:common_partial_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 56. f683a42c

On which device can Animal Crossing: New Horizons be played

**วิเคราะห์:** whichdevicecanplay→gameofferedservices ไม่ใช่การบอกhardwarecompatibilityทั่วไป

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Animal Crossing: New Horizons is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

**Source IDs ที่เลือก:** C04:game_detail_animal_crossing:studio_services:0, C04:game_detail_animal_crossing:studio_services:1, game_detail_animal_crossing

**เส้นทางเดิม:** pipeline:structured_game_availability_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 57. 42582c1e

ขอสอบถามหน่อยครับ Nintendo Switch OLED คืออะไร

**วิเคราะห์:** definitionอุปกรณ์OLED→usage ไม่ใช่nameechoหรือข้อมูลเกมแทน

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
Nintendo Switch OLED: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จำนวน: 1 Unit
อยู่ที่: Nintendo Switch Zone
ใช้สำหรับ:
•    เล่น Mario Kart 8 Deluxe
•    เล่น Overcooked 2
•    เล่น Super Smash Bros Ultimate
•    เล่น Nintendo Switch Sports
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Nintendo Switch OLED — การใช้งาน: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ
เล่น Mario Kart 8 Deluxe
เล่น Overcooked 2
เล่น Super Smash Bros Ultimate
เล่น Nintendo Switch Sports [S1]
```

**Source IDs ที่เลือก:** C03:equipment_nintendo_switch_oled:usage:0, equipment_nintendo_switch_oled

**เส้นทางเดิม:** pipeline:structured_equipment_item; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 58. c7ef53bc

PSU Staff เล่น PS5 2 ชั่วโมง เสียกี่บาท

**วิเคราะห์:** PSUStaffPS5120นาทีตามrate0บาท/คน รักษาaudienceไม่ใช้GeneralAdult

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
ระยะเวลาที่ถาม 120 นาที (2 ชั่วโมง) คิดเป็น 2 session (แพ็กเกจ)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ × 2 = 0 บาท
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาท สำหรับ 120 นาที [S1]
```

**Source IDs ที่เลือก:** C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount:0, C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount:1, C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount:2, C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount:3, C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount:4, C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount:5, migrated_rate_playstation_5_60_1_2_psu_student_staff

**เส้นทางเดิม:** pipeline:structured_service_fee_conversation; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 59. 8711c0d5

วันศุกร์ช่วงบ่ายปิดใช่ไหม ขอรายละเอียดแบบสั้น ๆ

**วิเคราะห์:** ศุกร์บ่ายตอบปิดช่วงเล่นเพราะmaintenance13–16แบบscopeชัด

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
วันศุกร์ Afternoon เล่นไม่ได้/ปิด/ไม่เปิดให้จองเล่น เพราะ 13:00-16:00 เป็น Maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
ศุกร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 13:00–16:00 เนื่องจากบำรุงรักษาตามตาราง [S1]
```

**Source IDs ที่เลือก:** C11:migrated_schedule_4:service_periods:0, migrated_schedule_4

**เส้นทางเดิม:** pipeline:structured_schedule; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 60. 5d18afc2

How do you use the controller in Little Nightmares II

**วิเคราะห์:** genericcontrollerusage→recordedbindinglistพร้อมplatform/sourcequalification ไม่สรุปinstalledmappingใหม่

**ผลใหม่ที่แสดง:** revision05_system / actual latest HTTP API / real clock

**คำตอบเดิมจริง**

```text
Little Nightmares II controls:
- L (Left Stick): Move
- R (Right Stick): Camera
- Cross: Jump / Throw / Attack
- Square: Sprint
- Circle: Flashlight / Remote
- Triangle: Call
- L1 / L2: Crouch / Slide
- R1 / R2: Grab
- Options: Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/304
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
Little Nightmares II / PlayStation / PS5 — Move: L (Left Stick) — Move and navigate the character [S1]
Little Nightmares II / PlayStation / PS5 — Camera: R (Right Stick) — Pan the camera to view surroundings and control flashlight direction [S2]
Little Nightmares II / PlayStation / PS5 — Jump / Throw / Attack: Cross — Use for jumping, throwing items, or swinging weapons to attack [S3]
Little Nightmares II / PlayStation / PS5 — Sprint: Square — Press to sprint, increasing movement speed or fleeing speed [S4]
Little Nightmares II / PlayStation / PS5 — Flashlight / Remote: Circle — Use to toggle flashlight and press TV remote button [S5]
Little Nightmares II / PlayStation / PS5 — Call: Triangle — Call out Six or use to grab hands [S6]
Little Nightmares II / PlayStation / PS5 — Crouch / Slide: L1 / L2 — Hold to crouch walk, or tap while running to slide through narrow gaps [S7]
Little Nightmares II / PlayStation / PS5 — Grab: R1 / R2 — Hold to pick up items, climb stairs, drag objects, or grab Six's hand [S8]
Little Nightmares II / PlayStation / PS5 — Pause: Options — Pause the game briefly and return to the main menu [S9]
These controls come from a secondary source and have not been verified against the studio installed game version and button preset.
```

**Source IDs ที่เลือก:** C05:controls_ps5_little_nightmares_ii:binding_0:0, C05:controls_ps5_little_nightmares_ii:binding_0:1, C05:controls_ps5_little_nightmares_ii:binding_1:2, C05:controls_ps5_little_nightmares_ii:binding_1:3, C05:controls_ps5_little_nightmares_ii:binding_2:4, C05:controls_ps5_little_nightmares_ii:binding_2:5, C05:controls_ps5_little_nightmares_ii:binding_3:6, C05:controls_ps5_little_nightmares_ii:binding_3:7, C05:controls_ps5_little_nightmares_ii:binding_4:8, C05:controls_ps5_little_nightmares_ii:binding_4:9, C05:controls_ps5_little_nightmares_ii:binding_5:10, C05:controls_ps5_little_nightmares_ii:binding_5:11, C05:controls_ps5_little_nightmares_ii:binding_6:12, C05:controls_ps5_little_nightmares_ii:binding_6:13, C05:controls_ps5_little_nightmares_ii:binding_7:14, C05:controls_ps5_little_nightmares_ii:binding_7:15, C05:controls_ps5_little_nightmares_ii:binding_8:16, C05:controls_ps5_little_nightmares_ii:binding_8:17, controls_ps5_little_nightmares_ii

**เส้นทางเดิม:** pipeline:structured_game_controls_en; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/live_api_1792759173596188200/LATEST_API_PROBES.json>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)

## 61. dcddcfd2

ขอถามเกี่ยวกับศูนย์หน่อยครับ: อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า

**วิเคราะห์:** consumptionเฉพาะพื้นที่กำหนด ไม่ทำให้bringpermissionกลายเป็นห้ามนำเข้า

**ผลใหม่ที่แสดง:** candidate04_final / R03 selected61 CLI

**คำตอบเดิมจริง**

```text
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบใหม่ล่าสุดที่มีหลักฐาน**

```text
อาหารและเครื่องดื่ม: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

**Source IDs ที่เลือก:** C10:migrated_faq_curated_rule_food_drinks:owner_policy:0, migrated_faq_curated_rule_food_drinks

**เส้นทางเดิม:** pipeline:protected_food_consumption; **เส้นทางใหม่:** pipeline:common_answer

[หลักฐานผลใหม่](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/candidate04_final/RESULTS.jsonl>) · [ผลเดิมและtrace](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/teacher02/RESULTS.jsonl>) · [source refs / contracts / trace ฉบับเต็ม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r124_legacy_guided_parity_20261023/CASE_COMPARISON.json>)
