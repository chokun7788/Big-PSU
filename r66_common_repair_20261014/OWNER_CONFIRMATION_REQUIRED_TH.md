# คำถามเจ้าของที่ต้องตอบจาก facts เท่านั้น

ไม่ต้องยืนยันซ้ำ: 12:00–13:00 ไม่เปิดจอง; VR 30 นาทีใช้ช่องเต็มชั่วโมง; สถานะสดเดิมและอังกฤษที่ผู้ใช้ยืนยันแล้ว การทดสอบ R66 แยกจากคำยืนยันเหล่านี้

1. ตารางราคา PS5/Switch/Cockpit/VR มี source ระบุถึง 31 มี.ค. 2026: หลังจากนั้นใช้อัตราใด เริ่มมีผลวันและเวลาใด? ส่งประกาศ/ตารางล่าสุดได้เลย ไม่ยืดอายุภาพเดิมเอง
2. ราคา PC เดิม 0/25/70 บาทต่อ 60 นาทีมีใน local update 27 ก.ค. 2026 อยู่แล้ว: ยังไม่ระบุวันเริ่ม/สิ้นสุดในหลักฐานเดิม ต้องระบุช่วงมีผลก่อน publish ไม่ต้องให้ตัวเลขใหม่เพียงเพราะ migration ตกหล่น
3. เวลาที่เปิดพื้นที่กับเวลาที่เปิดจอง: แหล่งที่บอกถึง 18:00 หมายถึงพื้นที่ยังเข้าได้หลัง slot เล่นสุดท้าย 16:00 หรือไม่? ช่วง booking ที่ยืนยันแล้วคง 09–12/13–16 และวัน Maintenance ตาม source เดิม
4. แพ็กเกจครึ่งวัน/เต็มวันตาม Excel ครอบคลุมนาฬิกาใด และอัตรามีผลตั้งแต่วันใด? ถ้าไม่มีต้นฉบับระบุ ห้ามแปลงเป็น 4/8 ชั่วโมงหรือคิดสัดส่วนเอง
5. “จองผิดวันและจ่ายแล้วเปลี่ยนวันได้” ต่างจาก “ขอเลื่อนแทนคืนเงินไม่ได้” ในเงื่อนไขใด? แยก context ข้อ 45/46 เดิม ไม่สรุปเป็นอนุญาต/ห้ามเลื่อนทั้งหมด
6. เฉพาะนโยบายที่ยังไม่มีหลักฐาน: อายุขั้นต่ำ/ผู้ปกครอง, บัญชีเกมให้ยืม, ติดตั้งเกม/mods, การชดเชยเมื่อเครื่องเสีย, การมาสาย/ต่อเวลา และเงื่อนไขสตรีม/บันทึกภาพ ขอข้อความอนุมัติแต่ละเรื่อง ไม่คัดลอกนโยบายร้านอื่น
7. ถ้าต้องการชื่อบุคลากรเป็นอักษรอังกฤษ ให้ชื่อสะกดทางการ ปัจจุบันคงชื่อไทยไว้ในคำตอบอังกฤษเมื่อไม่มี source อังกฤษ ไม่ให้โมเดลตั้งชื่อหรือเลื่อนตำแหน่งวิชาการเอง
8. Walk-in ที่ต้องจองผ่านระบบ ใช้บริการทันทีหลังจองได้หรือยังต้องจองก่อนอย่างน้อย 1 ชั่วโมงตาม published-policy text? owner FAQ ยืนยันเฉพาะต้องจอง ไม่ยืนยันการยกเว้นเวลา ต้องแยก source context ก่อนรวมคำตอบหรือ publish

source ที่มีการยืนยันเดิมแล้วเก็บ lineage ไว้ ไม่สร้างคำอนุมัติใหม่แทนเจ้าของ publication gate ที่ยังไม่ผ่านแสดงราย record ใน RELEASE_AUDIT ล่าสุด

## ช่องที่ publication gate ยังบล็อก แยกหมวด

ตารางนี้เป็น backlog ของ migration/แหล่งข้อมูล ไม่ได้แปลว่าต้องถามเจ้าของทุกแถว: ถ้ามีหลักฐานเดิมอยู่แล้วให้ใช้หลักฐานนั้นก่อน ห้ามให้เจ้าของกรอกซ้ำเพื่อกลบข้อบกพร่องของ importer

| หมวด | Gate | จำนวน record | ตัวอย่างรหัส |
|---|---|---:|---|
| audience | eligibility: required before publication | 5 | `audience_external_org`, `audience_internal_org`, `audience_psu_student_staff` |
| center | timezone: required before publication | 1 | `center_psu_phuket` |
| closure | zone_ids: required before publication | 3 | `schedule_closure_2026-07-28`, `schedule_closure_2026-07-29`, `schedule_closure_2026-07-30` |
| competition | Time-sensitive content requires confirmed validity | 4 | `competition_competition_rules_cs2_psu_phuket_2026`, `competition_competition_rules_tekken8_psu_esports`, `competition_competition_rules_valorant_psu_phuket_2026` |
| competition | coverage: required before publication | 4 | `competition_competition_rules_cs2_psu_phuket_2026`, `competition_competition_rules_tekken8_psu_esports`, `competition_competition_rules_valorant_psu_phuket_2026` |
| competition_rule | Time-sensitive content requires confirmed validity | 104 | `competition_competition_rules_cs2_psu_phuket_2026_section_001`, `competition_competition_rules_cs2_psu_phuket_2026_section_002`, `competition_competition_rules_cs2_psu_phuket_2026_section_003` |
| competition_rule | completeness: required before publication | 104 | `competition_competition_rules_cs2_psu_phuket_2026_section_001`, `competition_competition_rules_cs2_psu_phuket_2026_section_002`, `competition_competition_rules_cs2_psu_phuket_2026_section_003` |
| competition_rule | facet: required before publication | 104 | `competition_competition_rules_cs2_psu_phuket_2026_section_001`, `competition_competition_rules_cs2_psu_phuket_2026_section_002`, `competition_competition_rules_cs2_psu_phuket_2026_section_003` |
| control_set | bindings: required before publication | 38 | `controls_nintendo_animal_crossing_new_horizons`, `controls_nintendo_luigi_s_mansion_3`, `controls_nintendo_mario_kart_8_deluxe` |
| control_set | input_device: required before publication | 38 | `controls_nintendo_animal_crossing_new_horizons`, `controls_nintendo_luigi_s_mansion_3`, `controls_nintendo_mario_kart_8_deluxe` |
| control_set | preset: required before publication | 38 | `controls_nintendo_animal_crossing_new_horizons`, `controls_nintendo_luigi_s_mansion_3`, `controls_nintendo_mario_kart_8_deluxe` |
| equipment_model | device_type: required before publication | 16 | `equipment_driving_force_shifter`, `equipment_gaming_chair`, `equipment_gaming_headset` |
| person | public_scope: required before publication | 25 | `member_0629f0033d3d9b24`, `member_17d23bd43ffdcfb0`, `member_18a751d710b9b30c` |
| policy | conditions_all: required before publication | 1 | `policy_personal_keyboard_mouse` |
| rate | Time-sensitive content requires confirmed validity | 6 | `rate_recovered_pc_availability_pc_01_02_psu_student_staff`, `rate_recovered_pc_availability_pc_01_02_general_student`, `rate_recovered_pc_availability_pc_01_02_general_adult` |
| rate | calculation_rule: required before publication | 18 | `migrated_rate_nintendo_switch_60_1_2_psu_student_staff`, `migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student`, `migrated_rate_nintendo_switch_60_1_2_general_adult` |
| rate | unit: required before publication | 18 | `migrated_rate_nintendo_switch_60_1_2_psu_student_staff`, `migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student`, `migrated_rate_nintendo_switch_60_1_2_general_adult` |
| rental_package | Time-sensitive content requires confirmed validity | 24 | `rental_pc_external_full_day`, `rental_all_zones_external_full_day`, `rental_all_zones_external_half_day` |
| resource | operational_status: required before publication | 14 | `resource_cockpit_01`, `resource_cockpit_02`, `resource_pc_01` |
| schedule | Time-sensitive content requires confirmed validity | 7 | `migrated_schedule_0`, `migrated_schedule_1`, `migrated_schedule_2` |
| schedule | open_periods: required before publication | 5 | `migrated_schedule_0`, `migrated_schedule_1`, `migrated_schedule_2` |
| schedule | open_periods: unresolved conflict | 5 | `migrated_schedule_0`, `migrated_schedule_1`, `migrated_schedule_2` |
| schedule | zone_ids: required before publication | 7 | `migrated_schedule_0`, `migrated_schedule_1`, `migrated_schedule_2` |
| service | occupancy_minutes: required before publication | 8 | `availability_nintendo_1_2`, `availability_nintendo_1_4`, `availability_vr_30` |
| service | resource_ids: required before publication | 4 | `availability_nintendo_1_2`, `availability_nintendo_1_4`, `availability_vr_30` |
