# วิเคราะห์คำตอบและเกณฑ์เนื้อหา r47

## ผลก่อน/หลัง

ชุด HTTP ก่อนแก้ 16/23; หลังแก้ชุดเฉพาะ 25/25 และชุดรวม HTTP 206/206 (268 requests). Unit tests 50/50. ผลนี้ไม่ใช่ความแม่นยำของทุกคำถามที่เป็นไปได้

## สาเหตุจาก trace

### 1. อังกฤษมีคำตอบ แต่รูปประโยคไม่ตรงตัวรับคำถาม

Where is the venue? ไม่มี location/address และไม่ได้ใช้ studio/PSU Esports ที่ legacy regex กำหนด RuleMatcher ไม่พบผล และ English path ห้ามตกไปตอบไทย จึงคืน english_no_answer. r46 นับเคสนี้ผ่านเพราะเช็คเพียงว่า mode ไม่ใช่ราคาเหมา ไม่ได้เช็คว่าคำตอบมีที่อยู่จริง

แก้: ตีความคำถามสถานที่ของศูนย์แล้วใช้ bilingual contact_location rule เดิม ส่ง source ID curated_contact_location และ URL เดิม เกณฑ์ใหม่บังคับ category contact + เนื้อหาที่อยู่ตรง record + URL + ไม่ใช่ no_answer

### 2. ภาษาไทยหาเจอข้อมูล แต่ frame บังคับประเภทคำตอบผิด

ศูนย์อยู่ที่ไหน: route contact/contact_lookup → Local LLM contact/detail confidence 0.9 → question_frame equipment/equipment_lookup confidence 0.92 เพราะ looks_like_equipment_query มีคำว่าอยู่ที่ไหนโดยไม่ต้องมีชื่ออุปกรณ์ → decision_candidates เลือก structured.equipment score 0.789 → category_rule_base พบ rule_contact_location → validation ปฏิเสธ answer_contract_type_mismatch expected equipment,list actual fact,summary และ answer_contract_source_domain_mismatch expected equipment actual contact → curated retrieval ก็ถูกปฏิเสธด้วยกรอบเดิม → no_answer แม้มีข้อมูลจริง

แก้: รักษา frame หมวด contact ก่อน generic equipment-location cue และใช้ resolver ที่ผูกคำถามที่ตั้งภาษาไทยกับ curated fact เดิมก่อน late ambiguity gate สำหรับขอที่อยู่ศูนย์/ที่ตั้ง PSU Esports Studio

### 3. ชื่อสถานที่อื่นถูกแทนด้วยที่อยู่ PSU

Where is the Xbox studio in Bangkok? เดิม matched regex where is ... studio ซึ่งอนุญาตคำใดก็ได้ระหว่าง is กับ studio จึงตอบที่อยู่ PSU ทั้งที่ subject ไม่ตรง แก้ตรวจ noun/คำที่ยังไม่ resolve และถามยืนยัน ไม่ใช้ที่อยู่ PSU เป็นคำตอบของสถานที่นั้น

### 4. จุดที่พบขณะพัฒนาและข้อผิดพลาดของเทส

- Resolver ไทยรอบแรกใช้ row.id เป็น key แต่ canonical projection มี id curated_contact_location::th::text และ content_id curated_contact_location ทำให้หา record ไม่เจอ แก้ใช้ content_id ตามตัวระบุหลัก ตรวจ unit และ HTTP ซ้ำ

- เกณฑ์ catalog_source รอบแรกกำหนด URL our-games ให้ทั้งไทยและอังกฤษ แต่คำตอบไทยเป็นรายการเกมแยกเลขเครื่องจาก service_game_availability ซึ่งอ้าง esports.computing.psu.ac.th/ จริง แก้ oracle ให้ตรงแหล่งข้อมูลต้นฉบับของแต่ละชุด โดยไม่แก้คำตอบที่ถูกอยู่แล้ว

## การอ่านคะแนน

Confidence ของ routing/intent/frame เป็นคะแนนของแต่ละขั้น ไม่ได้ยืนยันว่ามีเนื้อหาที่ตอบคำถามได้ Candidate score 0.789 เป็นคะแนนการเลือก capability ไม่ใช่ความถูกต้องของที่อยู่ ส่วน English location handler 0.98 เป็นค่าที่กำหนดในโค้ด การผ่านจึงต้องใช้เกณฑ์เนื้อหาและแหล่งข้อมูลร่วมด้วย

## เกณฑ์เดิมที่เพิ่มความเข้ม

- en-venue-location: ต้องตอบที่อยู่จริงและอ้าง record
- en-venue-hours: ต้องมีช่วงเปิด/พัก/maintenance ตามวัน
- การเปลี่ยนจากเหมาเป็น PC รายชั่วโมง: ต้องมี 25/70 และ source local update ที่มีหลักฐาน
- เปลี่ยนเป็น PC games: ต้องมีรายชื่อ PC และไม่แทรกโซนอื่น พร้อม URL ของแหล่งรายการจริง
- เปลี่ยนเป็น CS2 rules: ต้องมีเนื้อหา format/team จาก rulebook CS2 ไม่ใช่แค่หลุดจากราคาเหมา

## ขอบเขตที่ยังไม่ใช่ผลยืนยัน

คำถามยกเลิก th-cancel-rental-prices ยังเป็น ambiguity_clarification; เกณฑ์เดิมตรวจเฉพาะไม่ส่งราคาเหมาเดิมซ้ำ ยังไม่ได้แก้ข้อความรับทราบการยกเลิก. ข้อมูลขั้นตอน/ชั่วโมงเช่าเหมาที่ไม่มีใน workbook ยังคงขาด. ไม่มีการยืนยันข้อมูลจองสดกับ oracle จริงหรือทดสอบ UI render. ที่อยู่ภาษาอังกฤษนำจาก record เดิม ไม่ได้อ้างว่าผ่านมนุษย์ตรวจเพิ่มในรอบนี้

## ทุกเคสเฉพาะที่ตรวจ

### en-location-1

คำถาม: Where is the venue?

ก่อนแก้: pipeline:english_no_answer; failed checks: category, source_bound_address, source_url, not_no_answer

I could not find verified PSU Esports Studio - Phuket information for this question.

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-2

คำถาม: Where is the studio located?

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-3

คำถาม: Where is PSU Esports Studio - Phuket?

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-4

คำถาม: What is the venue address?

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-5

คำถาม: What is the address of the studio?

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-6

คำถาม: Can you tell me the studio location?

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-7

คำถาม: Where can I find the studio?

ก่อนแก้: pipeline:english_no_answer; failed checks: category, source_bound_address, source_url, not_no_answer

I could not find verified PSU Esports Studio - Phuket information for this question.

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-8

คำถาม: I need the venue address

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-9

คำถาม: How do I get to the venue?

ก่อนแก้: pipeline:english_no_answer; failed checks: category, source_bound_address, source_url, not_no_answer

I could not find verified PSU Esports Studio - Phuket information for this question.

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120. This is the recorded address; travel directions are not provided in the studio records.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-10

คำถาม: Could you please share the address of PSU Esports Studio - Phuket?

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-11

คำถาม: Studio address

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-12

คำถาม: Where is the centre?

ก่อนแก้: pipeline:english_no_answer; failed checks: category, source_bound_address, source_url, not_no_answer

I could not find verified PSU Esports Studio - Phuket information for this question.

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-after-rental

คำถาม: PC rental full day external organizations → Where is the venue?

ก่อนแก้: pipeline:english_no_answer; failed checks: category, source_bound_address, source_url, not_no_answer

I could not find verified PSU Esports Studio - Phuket information for this question.

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### en-location-after-rules

คำถาม: Competition rules for CS2 → Where is the studio?

ก่อนแก้: pipeline:rule_en; failed checks: 

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:structured_studio_location_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true, "source_record_id": true}`

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### th-location

คำถาม: ศูนย์อยู่ที่ไหน

ก่อนแก้: pipeline:no_answer; failed checks: source_bound_address, source_url, not_no_answer

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

หลังแก้: pipeline:structured_studio_location_th; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true}`

PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us

### th-location-address

คำถาม: ขอที่อยู่ศูนย์

ก่อนแก้: pipeline:candidate_margin_clarification; failed checks: category, source_bound_address, source_url

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

หลังแก้: pipeline:structured_studio_location_th; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true}`

PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us

### th-location-explicit

คำถาม: ที่ตั้ง PSU Esports Studio อยู่ที่ไหน

ก่อนแก้: pipeline:game_target_unknown; failed checks: category, source_bound_address, source_url

ยังไม่พบชื่อเกมที่ตรงกับข้อมูลที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
กรุณาตรวจสอบชื่อเกมหรือพิมพ์ชื่อเกมที่ต้องการถามอีกครั้ง

หลังแก้: pipeline:structured_studio_location_th; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "category": true, "source_bound_address": true, "source_url": true, "not_no_answer": true}`

PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us

### en-equipment-location

คำถาม: Where is the 65-inch TV located?

ก่อนแก้: pipeline:structured_equipment_item_en; failed checks: 

Verified equipment record: TV 65-inch is listed in Cockpit Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

หลังแก้: pipeline:structured_equipment_item_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true, "category": true}`

Verified equipment record: TV 65-inch is listed in Cockpit Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### en-game-location

คำถาม: Can I play Beat Saber in the VR Zone?

ก่อนแก้: pipeline:structured_game_availability_en; failed checks: 

Beat Saber is available on: VR Station 30 minutes, VR Station 1 hour. Studio zone(s): VR Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

หลังแก้: pipeline:structured_game_availability_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true, "category": true}`

Beat Saber is available on: VR Station 30 minutes, VR Station 1 hour. Studio zone(s): VR Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-competition-location

คำถาม: Where is the RoV competition venue?

ก่อนแก้: pipeline:structured_competition_rules_en; failed checks: 

Answer: 2.1. PSU Esports Studio - Phuket (Building 5, Floor 1)

Details:
• 1.1. Offline competition on 11 September 2025 (B.E. 2568).
• 08:00-08:30: registration
• 08:30-08:40: bracket allocation
• 3.2. Each round played as Best of 3 (BO3)

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men

หลังแก้: pipeline:structured_competition_rules_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true, "category": true}`

Answer: 2.1. PSU Esports Studio - Phuket (Building 5, Floor 1)

Details:
• 1.1. Offline competition on 11 September 2025 (B.E. 2568).
• 08:00-08:30: registration
• 08:30-08:40: bracket allocation
• 3.2. Each round played as Best of 3 (BO3)

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men

### en-fire-button-location

คำถาม: Where is the fire button in Counter-Strike 2?

ก่อนแก้: pipeline:structured_game_controls_en; failed checks: 

Counter-Strike 2 controls:
- W / A / S / D: Move
- Left Shift: Walk
- Left Ctrl: Duck
- Spacebar: Jump
- E: Use
- Left Mouse Button: Fire
- Right Mouse Button: Secondary Fire
- R: Reload
- Q: Last Weapon Used
- G: Drop Weapon
- B: Buy Menu
- 1 / 2 / 3: Select weapons
- 4: Cycle Grenades
- Tab: Scoreboard
- Y / U: Chat
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.holy.gg/en/post/counter-strike-2-keyboard-mouse-controls-pc

หลังแก้: pipeline:structured_game_controls_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true, "category": true}`

Counter-Strike 2 controls:
- W / A / S / D: Move
- Left Shift: Walk
- Left Ctrl: Duck
- Spacebar: Jump
- E: Use
- Left Mouse Button: Fire
- Right Mouse Button: Secondary Fire
- R: Reload
- Q: Last Weapon Used
- G: Drop Weapon
- B: Buy Menu
- 1 / 2 / 3: Select weapons
- 4: Cycle Grenades
- Tab: Scoreboard
- Y / U: Chat
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.holy.gg/en/post/counter-strike-2-keyboard-mouse-controls-pc

### en-studio-hours

คำถาม: What are the venue opening hours?

ก่อนแก้: pipeline:structured_schedule_en; failed checks: 

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

หลังแก้: pipeline:structured_schedule_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true, "category": true}`

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

### en-pc-price-shift

คำถาม: PC rental full day external organizations → PC hourly price for external users

ก่อนแก้: pipeline:structured_service_fee_conversation; failed checks: 

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

หลังแก้: pipeline:structured_service_fee_conversation; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true, "category": true}`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

### en-pc-games-shift

คำถาม: PC rental full day external organizations → PC games

ก่อนแก้: pipeline:structured_games_catalog_en; failed checks: 

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

หลังแก้: pipeline:structured_games_catalog_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true, "category": true}`

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### en-unknown-venue

คำถาม: Where is the Xbox studio in Bangkok?

ก่อนแก้: pipeline:rule_en; failed checks: forbidden_content

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

หลังแก้: pipeline:studio_location_target_clarification_en; checks: `{"transport": true, "no_timeout": true, "english_no_thai": true, "required_content": true, "forbidden_content": true}`

Do you mean PSU Esports Studio - Phuket? I only have its recorded studio address; please specify the venue you mean.

