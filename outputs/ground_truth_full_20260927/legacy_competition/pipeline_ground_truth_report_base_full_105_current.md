# Pipeline Ground Truth Evaluation

วันที่: 2026-09-27

## Summary

- Total: 105
- PASS: 47
- FAIL: 58
- ERROR: 0
- Pass rate: 44.76%
- Average latency: 0.6927s
- P95 latency: 1.1597s
- Keyword fail: 58
- Source fail: 21
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:structured_reservation_fact`: 11
- `pipeline:no_answer`: 9
- `pipeline:structured_service_game_availability`: 6
- `pipeline:structured_schedule`: 6
- `pipeline:studio_rules_overview_fast_path`: 6
- `pipeline:rule_en`: 5
- `pipeline:structured_equipment_item`: 5
- `pipeline:structured_equipment_catalog`: 4
- `pipeline:rag_direct_curated`: 4
- `pipeline:rules_fast_path`: 4
- `pipeline:structured_members_role_lookup`: 4
- `pipeline:structured_members_group_list`: 3
- `pipeline:candidate_margin_clarification`: 3
- `pipeline:category_rule_fast_path`: 3
- `pipeline:hybrid_guarded_rerank`: 3
- `pipeline:structured_game_detail`: 3
- `pipeline:protected_checkin_required`: 2
- `pipeline:protected_food_consumption`: 2
- `pipeline:protected_studio_rule_direct`: 2
- `pipeline:protected_damage_responsibility`: 2
- `pipeline:protected_alcohol_rule`: 2
- `pipeline:competition_target_clarification`: 2
- `pipeline:competition_facet_not_covered_no_answer`: 2
- `pipeline:ambiguity_clarification`: 2
- `pipeline:overview_fast_path`: 1
- `pipeline:structured_service_capacity`: 1
- `pipeline:protected_payment_deadline`: 1
- `pipeline:booking_fast_path`: 1
- `pipeline:checkin_fast_path`: 1
- `pipeline:protected_payment_method`: 1
- `pipeline:schedule_fast_path`: 1
- `pipeline:protected_temporary_suspension`: 1
- `pipeline:structured_schedule_en`: 1
- `pipeline:guard_no_answer`: 1

## Route Category Distribution

- `reservation`: 24
- `rules`: 17
- `games`: 11
- `overview`: 9
- `equipment`: 9
- `schedule`: 8
- `penalty`: 7
- `clarification`: 5
- `knowledge`: 4
- `competition_rules`: 4
- `contact`: 3
- `general`: 2
- `events_news`: 1
- `no_answer`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| overview_001 | overview | `knowledge` | ศูนย์พัฒนาการเรียนรู้; ภูเก็ต | PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต แหล่งข้อมูล: https://esports.phuket.psu.ac.... |
| overview_002 | overview | `overview` | มหาวิทยาลัยสงขลานครินทร์; วิทยาลัยการคอมพิวเตอร์; home | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •... |
| overview_004 | overview | `overview` | นักเล่นเกม; ผู้สนใจ; home | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •... |
| equipment_005 | equipment | `games` | TV 86; 1 Units; home | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| equipment_006 | equipment | `equipment` | OLED model; Neon Red Neon Blue | Nintendo Switch OLED: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว จำนวน: 1 Unit อยู่ที่: Nintendo Switch Zone ใช้สำหรับ: • เล่น Mario Kart 8 Deluxe • เล่น Overcooked 2 • เล่น Super Smash... |
| equipment_008 | equipment | `equipment` | PlayStation VR; Sony PlayStation VR2 | อุปกรณ์ใน PlayStation 5 Zone: PlayStation 5 Zone / VR Zone • PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home |
| games_001 | games | `rules` | Gran Turismo 7; Mario Kart 8 Deluxe; Tekken 8; Beat Saber; home | กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| games_003 | games | `games` | Marvel’s Spider-Man 2 | ได้ครับ Marvel's Spider-Man 2 เล่นได้ที่ PlayStation 5 Zone - PlayStation 5 #01-#02 แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| games_008 | games | `games` | Gran Turismo 7 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| services_002 | services | `equipment` | 60 min; Reservation | Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: • เล่น VALORANT • เล่น Counter-Strike 2 • เล่น PUBG: BATTLEGR... |
| services_003 | services | `general` | 1 Hour; 60 min; 30 Mins; 30 min; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| reservation_004 | reservation | `schedule` | การจองจะถูกยกเลิก | เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:0... |
| reservation_005 | reservation | `reservation` | ยกเลิกการจอง | เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| reservation_006 | reservation | `reservation` | ยกเลิกการจองผ่านทางอีเมล | การยกเลิกหรือแก้ไขการจองควรทำล่วงหน้าอย่างน้อย 1 ชั่วโมง หากกดจองแล้วจะแก้ข้อมูลเดิมไม่ได้ ต้องยกเลิกแล้วจองใหม่ตามเงื่อนไข แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| reservation_008 | reservation | `reservation` | ข้อมูลไม่ถูกต้อง; ไม่ปฏิบัติตามกฎ | ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| checkin_002 | reservation | `reservation` | ต้องเช็คอินก่อน; เวลาเริ่มต้น | ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| checkin_003 | reservation | `schedule` | ระบบจะยกเลิกการจองทันที; ไม่มีการคืนเงิน | เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open • วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:0... |
| checkin_004 | reservation | `reservation` | บัตรประจำตัวนักศึกษา; บัตรประจำตัวบุคลากร | ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| cancel_002 | reservation | `reservation` | ไม่มีการคืนเงิน; ยกเว้น; ศูนย์เป็นฝ่ายผิดพลาด | การยกเลิกหรือแก้ไขการจองควรทำล่วงหน้าอย่างน้อย 1 ชั่วโมง หากกดจองแล้วจะแก้ข้อมูลเดิมไม่ได้ ต้องยกเลิกแล้วจองใหม่ตามเงื่อนไข แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| cancel_003 | reservation | `clarification` | อุปกรณ์ขัดข้อง; เหตุสุดวิสัย; ศูนย์ต้องปิดให้บริการ; Reservation | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| cancel_004 | reservation | `general` | สามารถเปลี่ยนแปลงเวลา; แจ้งล่วงหน้า; อย่างน้อย 1 ชั่วโมง; Reservation | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| payment_001 | reservation | `reservation` | โอนเข้าบัญชีธนาคาร | ชำระเงินโดยโอนผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| payment_004 | reservation | `reservation` | Siam Commercial Bank | ชำระเงินโดยโอนผ่านธนาคารไทยพาณิชย์ ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| howto_001 | reservation | `reservation` | เลือกวันและเวลา; กรอกข้อมูล | ขั้นตอนจองโดยสรุป: • เลือกบริการหรือโซนที่ต้องการใช้ • เลือกวันและรอบเวลาที่ต้องการ • กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ • ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง • หลั... |
| howto_002 | reservation | `reservation` | Student ID; Staff ID; National ID; ชื่อ; อีเมล; เบอร์โทรศัพท์ | การยกเลิกหรือแก้ไขการจองควรทำล่วงหน้าอย่างน้อย 1 ชั่วโมง หากกดจองแล้วจะแก้ข้อมูลเดิมไม่ได้ ต้องยกเลิกแล้วจองใหม่ตามเงื่อนไข แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| schedule_003 | reservation | `schedule` | Monday | วันจันทร์ Morning เล่นไม่ได้/ปิด/ไม่เปิดให้จองเล่น เพราะ 09:00-12:00 เป็น Maintenance* รายละเอียดจากตาราง: • วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open แหล่งข้อมูล: https://esports.computi... |
| rules_002 | rules | `reservation` | ฝากสัมภาระก่อนเข้าใช้บริการ | ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| rules_003 | rules | `rules` | นำอุปกรณ์; มาคืน | อุปกรณ์และแผ่นเกมที่เบิกไปใช้งานต้องคืนหลังจากใช้งานเสร็จ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| rules_004 | rules | `rules` | ห้ามทิ้งขยะ; บริเวณที่ไม่ได้กำหนด | กติกาการใช้บริการในศูนย์โดยสรุปครับ • ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย • รับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด • คืนอุปกรณ์และแผ่นเกมหลังใช้งานเสร็จ • งดส่งเสียงดังเกินควร และ... |
| rules_009 | rules | `penalty` | ราคากลาง | ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต... |
| rules_010 | rules | `rules` | ห้ามเคลื่อนย้าย | ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| rules_011 | rules | `rules` | ห้ามนำอุปกรณ์อิเล็กทรอนิกส์ส่วนตัว | ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| rules_014 | rules | `rules` | ห้ามพกอาวุธ; ของมีคม | กติกาการใช้บริการในศูนย์โดยสรุปครับ • ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย • รับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด • คืนอุปกรณ์และแผ่นเกมหลังใช้งานเสร็จ • งดส่งเสียงดังเกินควร และ... |
| rules_015 | rules | `rules` | ห้ามเล่นการพนัน | กติกาการใช้บริการในศูนย์โดยสรุปครับ • ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย • รับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด • คืนอุปกรณ์และแผ่นเกมหลังใช้งานเสร็จ • งดส่งเสียงดังเกินควร และ... |
| penalty_001 | penalty | `rules` | คำเตือน; ระงับสิทธิ์; ชั่วคราว; ถาวร | กติกาการใช้บริการในศูนย์โดยสรุปครับ • ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย • รับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด • คืนอุปกรณ์และแผ่นเกมหลังใช้งานเสร็จ • งดส่งเสียงดังเกินควร และ... |
| penalty_003 | penalty | `penalty` | ละเมิดกฎอย่างร้ายแรง; ละเมิดซ้ำ; ทำลายทรัพย์สิน | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ |
| penalty_004 | penalty | `penalty` | ยื่นคำร้อง; 7 วัน | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ |
| penalty_005 | penalty | `rules` | บันทึกในประวัติการใช้บริการ | กติกาการใช้บริการในศูนย์โดยสรุปครับ • ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย • รับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด • คืนอุปกรณ์และแผ่นเกมหลังใช้งานเสร็จ • งดส่งเสียงดังเกินควร และ... |
| contact_001 | contact | `contact` | มหาวิทยาลัยสงขลานครินทร์; วิทยาเขตภูเก็ต; 80 หมู่ 1; Contact | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ |
| contact_003 | contact | `reservation` | facebook.com/psuesportsphuket; Contact | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| contact_004 | contact | `reservation` | 7627 6004; 7627 6045 | ตอนจองต้องกรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล, เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี จากนั้นชำระเงินโดยโอนเข้าบัญชีธนาคารและแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| knowledge_002 | knowledge | `clarification` | 19 ตุลาคม; 1972; มหาวิทยาลัยสแตนฟอร์ด; Spacewar; Knowledge | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| knowledge_003 | knowledge | `competition_rules` | MOBA; FPS; Battle Royale; Fighting Games; Knowledge | ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT |
| knowledge_006 | knowledge | `games` | ทักษะชีวิต; ความสนุก; Knowledge | Overcooked! 2: Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย แนวเกม: เกม Co-op ทำอาหาร วิธีเล่นโดยสรุป: ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีม... |
| knowledge_007 | knowledge | `games` | ไหวพริบ; การตัดสินใจ; Knowledge | Mario Kart 8 Deluxe: Mario Kart 8 Deluxe คือเกมแข่งรถสไตล์ปาร์ตี้ที่ใช้ตัวละคร Nintendo ขับรถแข่งกันในสนามหลากหลายแบบ แนวเกม: เกมแข่งรถ Party Racing วิธีเล่นโดยสรุป: เลือกตัวละครและรถ ขับเข้าเส้นชัย ใช้ไอเทมช่วยโจมตี/ป้อ... |
| knowledge_008 | knowledge | `games` | บริหารจักระ; การตัดสินใจ; Knowledge | NARUTO X BORUTO Ultimate Ninja Storm Connections: NARUTO X BORUTO Ultimate Ninja Storm Connections คือเกมต่อสู้ที่ใช้ตัวละครจากจักรวาล Naruto/Boruto แนวเกม: เกมต่อสู้จากอนิเมะ วิธีเล่นโดยสรุป: เลือกตัวละคร ใช้คอมโบ สกิลน... |
| news_001 | events_news | `competition_rules` | PSU Phuket CS 2 2026 Tournament; News | ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT |
| news_002 | events_news | `competition_rules` | 21 กุมภาพันธ์ 2569; VALORANT; News | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| news_003 | events_news | `competition_rules` | 4 คน; Tekken 8; News | ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน |
| news_004 | events_news | `events_news` | 11 คน; Game-based Learning; News | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด events_news ตอนนี้ครับ |
| news_005 | events_news | `clarification` | ม.3; โรงเรียนท้ายเหมืองวิทยา; News | คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: เวลาเปิด-ปิด, สมาชิกทีม |
| about_005 | about_us | `overview` | Nintendo Switch; PlayStation 5; Gallery | สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •... |
| english_003 | reservation | `schedule` | 30 minutes | Regular service hours are Monday-Friday. Monday morning and Friday afternoon are maintenance periods. Please specify a day for the exact play window. Source: https://esports.computing.psu.ac.th/ (original source in Thai) |
| english_004 | reservation | `reservation` | automatically cancelled | Payment must be made immediately after booking. If payment is not made within 10 minutes, the booking will be cancelled, and the user must make a new booking to use the service. Source: https://esports.computing.psu.ac.t... |
| no_answer_001 | no_answer | `equipment` | ไม่พบข้อมูล | อุปกรณ์ใน PC Zone: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units) • Gaming Monitor (10 Units) • Gaming Keyboard • Gaming Mouse • Gaming Headset • Gaming Chair (10 Units) แหล่งข้อมูล: https://esports.phuket.... |
| no_answer_003 | no_answer | `rules` | ไม่พบข้อมูล | ยังยืนยันไม่ได้ว่าโต๊ะเล่นเกมเป็นพื้นที่รับประทานที่กำหนดครับ อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| no_answer_004 | no_answer | `clarification` | ไม่พบข้อมูล | ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา? |
| no_answer_005 | no_answer | `clarification` | ไม่พบข้อมูล | ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่` |

## Files

- Results JSONL: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\outputs\ground_truth_full_20260927\legacy_competition\pipeline_ground_truth_results_base_full_105_current.jsonl`
