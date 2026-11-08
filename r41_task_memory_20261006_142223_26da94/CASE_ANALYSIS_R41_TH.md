# วิเคราะห์บทสนทนาต่อเคส r41.3

คะแนนผ่านหมายถึงเกณฑ์ task/content/scope ที่กำหนด ไม่รับรอง owner facts ทุกข้อ

## บทสนทนาหลักใหม่

### th-all-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: ทั้งหมด

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มควบคุมทั้งหมดอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: all_controls_for_selected_targets

Child statuses: []

### th-resume-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: ราคา PC ของบุคคลภายนอก

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 3: กลับไปเรื่องปุ่มเมื่อกี้

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: []

### th-resume-price

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true, "retained_external_groups": true}

#### รอบ 1: ราคา PC ของบุคคลภายนอก

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: กฎการแข่งขัน CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `กติกาการแข่งขัน Counter-Strike 2`; outcome: `answered_complete`

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 3: กลับไปเรื่องราคาเมื่อกี้

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-resume-rules

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: กฎการแข่งขัน CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `กติกาการแข่งขัน Counter-Strike 2`; outcome: `answered_complete`

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 2: ราคา PC ของบุคคลภายนอก

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 3: กลับไปกฎการแข่งขันเมื่อกี้

mode: `pipeline:competition_rule_overview_source`; resolved: `กติกาการแข่งขัน Counter-Strike 2`; outcome: `answered_complete`

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: []

### th-resume-catalog

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: PC มีเกมอะไรบ้าง

mode: `pipeline:structured_service_game_availability`; resolved: `PC มีเกมอะไรบ้าง`; outcome: `answered_complete`

PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: กฎการแข่งขัน CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `กติกาการแข่งขัน Counter-Strike 2`; outcome: `answered_complete`

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 3: กลับไปเรื่องรายชื่อเกม

mode: `pipeline:structured_service_game_availability`; resolved: `PC มีเกมอะไรบ้าง`; outcome: `answered_complete`

PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: []

### th-new-target-after-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: ขอราคา PS5

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PlayStation 5`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-ambiguous-ordinal-catalog

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: มีเกมอะไรให้เล่นบ้าง

mode: `pipeline:structured_games_catalog`; resolved: `มีเกมอะไรให้เล่นบ้าง`; outcome: `answered_complete`

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

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: อันแรก

mode: `pipeline:dialogue_state_clarification`; resolved: `อันแรก`; outcome: `needs_clarification`

หมายถึงเกมหรือโซนใดครับ กรุณาพิมพ์ชื่อ เพราะรายการที่แสดงมีตัวเลือกหลายระดับ

เหตุผลการผูกบริบท: ordinal_catalog_axis_ambiguous

Child statuses: []

### th-no-context-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: ทั้งหมด

mode: `pipeline:conversation_scope_clarification`; resolved: `ทั้งหมด`; outcome: `needs_clarification`

ต้องการดูทั้งหมดของเรื่องหรือบริการใดครับ?

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-no-context-resume

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: กลับไปเรื่องปุ่มเมื่อกี้

mode: `pipeline:dialogue_state_clarification`; resolved: `กลับไปเรื่องปุ่มเมื่อกี้`; outcome: `needs_clarification`

ยังระบุคำถามก่อนหน้าที่ได้รับคำตอบแล้วของเรื่องนี้ไม่ได้ครับ กรุณาระบุเกมหรืออุปกรณ์และเรื่องที่ต้องการทราบ

เหตุผลการผูกบริบท: no_acknowledged_archived_task

Child statuses: []

### th-partial-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT กับ มายคราฟต์

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_partial`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง
ยังไม่พบข้อมูลปุ่มควบคุมที่ยืนยันสำหรับเกมที่คุณระบุในฐานข้อมูลของศูนย์ครับ กรุณาตรวจชื่อเต็มและภาคของเกมอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

### th-complete-multi-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT กับ Beat Saber

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; Beat Saber มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Beat Saber มีปุ่มควบคุมอะไรบ้าง
Beat Saber ปุ่มที่ตรงกับคำถาม:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "games", "pipeline:structured_game_controls"]]

### th-all-after-compound

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง และ PC ราคาเท่าไหร่

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มอะไรบ้าง และ PC ราคาเท่าไหร่`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: PC ราคาเท่าไหร่
ราคา PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท
•    General Adult / บุคคลทั่วไป: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "service_fee", "pipeline:deterministic_calculator_fast"]]

#### รอบ 2: ทั้งหมด

mode: `pipeline:dialogue_state_clarification`; resolved: `ทั้งหมด`; outcome: `needs_clarification`

คำว่า “ทั้งหมด” หมายถึงเรื่องหรือตัวเลือกใดครับ เช่น ปุ่มควบคุม ราคา รายชื่อเกม หรือโซน

เหตุผลการผูกบริบท: all_has_multiple_operations

Child statuses: []

### en-all-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What are the controls for VALORANT?

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: all of them

mode: `pipeline:structured_game_controls_en`; resolved: `What are all the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: all_controls_for_selected_targets

Child statuses: []

### en-resume-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What are the controls for VALORANT?

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: PC prices for external users

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 3: back to the controls

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: []

### en-resume-price

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true, "retained_external_groups": true}

#### รอบ 1: PC prices for external users

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: Competition rules for CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `Competition rules for Counter-Strike 2`; outcome: `answered_complete`

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 3: back to the prices

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-resume-rules

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: Competition rules for CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `Competition rules for Counter-Strike 2`; outcome: `answered_complete`

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 2: PC prices for external users

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 3: back to the competition rules

mode: `pipeline:competition_rule_overview_source`; resolved: `Competition rules for Counter-Strike 2`; outcome: `answered_complete`

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: []

### en-resume-catalog

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What games are available in PC?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games are available in PC?`; outcome: `answered_complete`

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: Competition rules for CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `Competition rules for Counter-Strike 2`; outcome: `answered_complete`

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 3: back to the game list

mode: `pipeline:structured_games_catalog_en`; resolved: `What games are available in PC?`; outcome: `answered_complete`

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: []

### en-new-target-after-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What are the controls for VALORANT?

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: Show PS5 prices

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PlayStation 5`; outcome: `answered_complete`

Service prices (recorded package rates):

PlayStation 5 — 60 minutes/package (1-2 people)
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 50 THB/package
• General adults: 150 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-ambiguous-ordinal-catalog

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: the first one

mode: `pipeline:dialogue_state_clarification`; resolved: `the first one`; outcome: `needs_clarification`

Which game or zone do you mean? Please provide its name; the displayed list contains more than one level of choices.

เหตุผลการผูกบริบท: ordinal_catalog_axis_ambiguous

Child statuses: []

### en-no-context-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: all of them

mode: `pipeline:conversation_scope_clarification`; resolved: `all of them`; outcome: `needs_clarification`

All of which topic or service would you like to see?

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-no-context-resume

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: back to the controls

mode: `pipeline:dialogue_state_clarification`; resolved: `back to the controls`; outcome: `needs_clarification`

I cannot identify a previously delivered request for that topic. Please specify the game or device and what you want to know.

เหตุผลการผูกบริบท: no_acknowledged_archived_task

Child statuses: []

### en-partial-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and Minecraft

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for minecraft?`; outcome: `answered_partial`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for minecraft?
I do not have verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

### en-complete-multi-controls

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and Beat Saber

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Beat Saber?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### en-all-after-compound

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What are the controls for VALORANT and what are PC prices?

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT and what are PC prices?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: what are PC prices
PC - 1 hour (1 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 25 THB
- General adults: 70 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "service_fee", "pipeline:structured_service_fee_en"]]

#### รอบ 2: all of them

mode: `pipeline:dialogue_state_clarification`; resolved: `all of them`; outcome: `needs_clarification`

Which topic or selection does "all" refer to: controls, prices, game lists, or zones?

เหตุผลการผูกบริบท: all_has_multiple_operations

Child statuses: []

### explicit-all-zones

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What games are available in PC?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games are available in PC?`; outcome: `answered_complete`

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: all zones

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: explicit_all_catalog_zones

Child statuses: []

## คำถามเพิ่มเติมและขอบบริบท

### th-partial-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT กับ มายคราฟต์

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_partial`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง
ยังไม่พบข้อมูลปุ่มควบคุมที่ยืนยันสำหรับเกมที่คุณระบุในฐานข้อมูลของศูนย์ครับ กรุณาตรวจชื่อเต็มและภาคของเกมอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

#### รอบ 3: ทั้งหมด

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_partial`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง
ยังไม่พบข้อมูลปุ่มควบคุมที่ยืนยันสำหรับเกมที่คุณระบุในฐานข้อมูลของศูนย์ครับ กรุณาตรวจชื่อเต็มและภาคของเกมอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: all_preserves_unresolved_children

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

### th-multi-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT กับ Beat Saber

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; Beat Saber มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Beat Saber มีปุ่มควบคุมอะไรบ้าง
Beat Saber ปุ่มที่ตรงกับคำถาม:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "games", "pipeline:structured_game_controls"]]

#### รอบ 3: ทั้งหมดเลยครับ

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมทั้งหมดอะไรบ้าง; Beat Saber มีปุ่มควบคุมทั้งหมดอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมทั้งหมดอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Beat Saber มีปุ่มควบคุมทั้งหมดอะไรบ้าง
Beat Saber มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Head/body movement: หลบและจัดตำแหน่งร่างกาย - เป็นข้อมูลวิธีเล่นระดับภาพรวมจากแหล่งทางการ ไม่ใช่ผังคีย์ละเอียดรายปุ่ม
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: all_controls_for_selected_targets

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "games", "pipeline:structured_game_controls"]]

### th-multi-resume

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT กับ Beat Saber

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; Beat Saber มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Beat Saber มีปุ่มควบคุมอะไรบ้าง
Beat Saber ปุ่มที่ตรงกับคำถาม:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "games", "pipeline:structured_game_controls"]]

#### รอบ 3: ราคา PC ของบุคคลภายนอก

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 4: กลับไปเรื่องปุ่มเดิม

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; Beat Saber มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Beat Saber มีปุ่มควบคุมอะไรบ้าง
Beat Saber ปุ่มที่ตรงกับคำถาม:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "games", "pipeline:structured_game_controls"]]

### th-family-second

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: Call of Duty มีปุ่มอะไรบ้าง

mode: `pipeline:ambiguity_clarification`; resolved: `Call of Duty มีปุ่มอะไรบ้าง`; outcome: `needs_clarification`

Call of Duty มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องปุ่ม/วิธีควบคุม ขอเลือกเกมก่อน:
•    Call of Duty: Modern Warfare III (PlayStation 5 Zone)
•    Call of Duty: Warzone (PC Zone)

พิมพ์ต่อได้ เช่น `Call of Duty: Modern Warfare III ปุ่มอะไร` หรือ `Call of Duty: Warzone ปุ่มอะไร`

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: อันที่สอง

mode: `pipeline:structured_game_controls`; resolved: `Call of Duty: Warzone มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

Call of Duty: Warzone มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    Cross: กระโดด / ปีนป่าย - กระโดด หรือปีนข้ามสิ่งกีดขวาง
•    Circle: ย่อตัว / หมอบ / สไลด์ - กดเปลี่ยนท่าทาง หรือกดขณะวิ่งเพื่อสไลด์เข่า
•    Square: โต้ตอบ / รีโหลด - เก็บของ เปิดกล่อง ฟาร์มไอเทม หรือรีโหลดกระสุน
•    Triangle: สลับอาวุธ - สลับเปลี่ยนปืน
•    D-Pad: คำสั่งเฉพาะโหมด - คำสั่งเสริมตามโหมดการเล่น เช่น ปิง หรือ คิลสตรีค
•    Touch Pad: ตารางคะแนน / แผนที่ - เปิดตารางคะแนนและแผนที่ยุทธวิธี
•    Options: เมนูหลัก - เปิดเมนูตั้งค่าและหยุดเกม
•    L1: ใช้อุปกรณ์ยุทธวิธี - ใช้งานระเบิดควัน แฟลช หรืออุปกรณ์สายสนับสนุน
•    R1: ใช้อุปกรณ์ทำลายล้าง - ใช้งานระเบิดทำลายล้างต่าง ๆ
•    L2: เล็งปืน (ADS) - ยกปืนเล็งศูนย์
•    R2: ยิง - ลั่นไกปืน
•    L3: วิ่ง / กลั้นหายใจ - กดวิ่ง หรือกลั้นหายใจขณะเล็งกล้องสโคป
•    R3: โจมตีประชิด - โจมตีด้วยพานท้ายปืน
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameaccess.info/call-of-duty-warzone-battle-royale-mode-controls/

เหตุผลการผูกบริบท: explicit_ordinal_of_offered_family_options

Child statuses: []

### th-typo-then-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: Valoant มีปุ่มอะไรบ้าง

mode: `pipeline:structured_game_controls`; resolved: `Valoant มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: ทุกอัน

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มควบคุมทั้งหมดอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: all_controls_for_selected_targets

Child statuses: []

### th-catalog-multi-resume

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: มีเกมอะไรให้เล่นบ้าง

mode: `pipeline:structured_games_catalog`; resolved: `มีเกมอะไรให้เล่นบ้าง`; outcome: `answered_complete`

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

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: PC กับ PS5

mode: `pipeline:multi_question_splitter`; resolved: `PC มีเกมอะไรบ้าง; PlayStation 5 มีเกมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: PC มีเกมอะไรบ้าง
PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

คำถามที่ 2: PlayStation 5 มีเกมอะไรบ้าง
PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้

PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
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
หมายเหตุ: PlayStation 5 #01 และ #02 ใช้รายการเกมเดียวกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: selected_multiple_catalog_services

Child statuses: [["task-1", "answered", "games", "pipeline:structured_service_game_availability"], ["task-2", "answered", "games", "pipeline:structured_service_game_availability"]]

#### รอบ 3: กฎการแข่งขัน CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `กติกาการแข่งขัน Counter-Strike 2`; outcome: `answered_complete`

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 4: กลับไปรายชื่อเกมเมื่อกี้

mode: `pipeline:multi_question_splitter`; resolved: `PC มีเกมอะไรบ้าง; PlayStation 5 มีเกมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: PC มีเกมอะไรบ้าง
PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

คำถามที่ 2: PlayStation 5 มีเกมอะไรบ้าง
PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้

PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
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
หมายเหตุ: PlayStation 5 #01 และ #02 ใช้รายการเกมเดียวกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: [["task-1", "answered", "games", "pipeline:structured_service_game_availability"], ["task-2", "answered", "games", "pipeline:structured_service_game_availability"]]

### th-unknown-cannot-revert

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: Minecraft มีปุ่มอะไรบ้าง

mode: `pipeline:game_controls_target_unconfirmed`; resolved: `Minecraft มีปุ่มอะไรบ้าง`; outcome: `no_answer`

ยังไม่พบข้อมูลปุ่มควบคุมที่ยืนยันสำหรับเกมที่คุณระบุในฐานข้อมูลของศูนย์ครับ กรุณาตรวจชื่อเต็มและภาคของเกมอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: explicit_unsupported_game_preserved

Child statuses: []

#### รอบ 3: ทั้งหมด

mode: `pipeline:dialogue_state_clarification`; resolved: `ทั้งหมด`; outcome: `needs_clarification`

ต้องการปุ่มควบคุมทั้งหมดของเกมใดครับ

เหตุผลการผูกบริบท: all_controls_without_game

Child statuses: []

### th-unresolved-return-filter

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: ราคา PC ของบุคคลภายนอก

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: กฎการแข่งขัน CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `กติกาการแข่งขัน Counter-Strike 2`; outcome: `answered_complete`

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 3: กลับไปเรื่องราคาของพรุ่งนี้

mode: `pipeline:dialogue_state_clarification`; resolved: `กลับไปเรื่องราคาของพรุ่งนี้`; outcome: `needs_clarification`

คำว่า “ทั้งหมด” หมายถึงเรื่องหรือตัวเลือกใดครับ เช่น ปุ่มควบคุม ราคา รายชื่อเกม หรือโซน

เหตุผลการผูกบริบท: resume_contains_unresolved_new_conditions

Child statuses: []

### th-explicit-return-new-target

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: ราคา PC ของบุคคลภายนอก

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 3: กลับไปดูปุ่ม Beat Saber

mode: `pipeline:structured_game_controls`; resolved: `กลับไปดูปุ่ม Beat Saber`; outcome: `answered_complete`

Beat Saber ปุ่มที่ตรงกับคำถาม:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

### en-partial-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and Minecraft

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for minecraft?`; outcome: `answered_partial`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for minecraft?
I do not have verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

#### รอบ 3: all of them

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for minecraft?`; outcome: `answered_partial`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for minecraft?
I do not have verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: all_preserves_unresolved_children

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

### en-multi-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and Beat Saber

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Beat Saber?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

#### รอบ 3: all of them please

mode: `pipeline:multi_question_splitter`; resolved: `What are all the controls for VALORANT?; What are all the controls for Beat Saber?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are all the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are all the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: all_controls_for_selected_targets

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### en-multi-resume

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "compound": true, "outcome": true, "task_ids_complete": true, "child_statuses": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and Beat Saber

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Beat Saber?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

#### รอบ 3: PC prices for external users

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 4: return to the controls

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Beat Saber?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### en-family-second

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: Call of Duty controls

mode: `pipeline:game_family_clarification_en`; resolved: `Call of Duty controls`; outcome: `needs_clarification`

Which game do you mean: Call of Duty: Modern Warfare III, Call of Duty: Warzone? Please name the exact title so I can check its controls.

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: the second one

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for Call of Duty: Warzone?`; outcome: `answered_complete`

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

เหตุผลการผูกบริบท: explicit_ordinal_of_offered_family_options

Child statuses: []

### en-typo-then-all

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: Valoant controls

mode: `pipeline:structured_game_controls_en`; resolved: `Valoant controls`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: everything

mode: `pipeline:structured_game_controls_en`; resolved: `What are all the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: all_controls_for_selected_targets

Child statuses: []

### en-catalog-multi-resume

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PC and PS5

mode: `pipeline:multi_question_splitter`; resolved: `What games are available in PC?; What games are available in PlayStation 5?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PC?
There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in PlayStation 5?
There are currently 17 verified games in PlayStation 5 Zone.

PlayStation 5 Zone (17 games)
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
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: selected_multiple_catalog_services

Child statuses: [["task-1", "answered", "games", "pipeline:structured_games_catalog_en"], ["task-2", "answered", "games", "pipeline:structured_games_catalog_en"]]

#### รอบ 3: Competition rules for CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `Competition rules for Counter-Strike 2`; outcome: `answered_complete`

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 4: back to the game list

mode: `pipeline:multi_question_splitter`; resolved: `What games are available in PC?; What games are available in PlayStation 5?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PC?
There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in PlayStation 5?
There are currently 17 verified games in PlayStation 5 Zone.

PlayStation 5 Zone (17 games)
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
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: explicitly_resumed_archived_task

Child statuses: [["task-1", "answered", "games", "pipeline:structured_games_catalog_en"], ["task-2", "answered", "games", "pipeline:structured_games_catalog_en"]]

### en-unknown-cannot-revert

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT controls

mode: `pipeline:structured_game_controls_en`; resolved: `VALORANT controls`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: Minecraft controls

mode: `pipeline:game_controls_target_unconfirmed`; resolved: `Minecraft controls`; outcome: `no_answer`

I could not find verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: explicit_unsupported_game_preserved

Child statuses: []

#### รอบ 3: all of them

mode: `pipeline:dialogue_state_clarification`; resolved: `all of them`; outcome: `needs_clarification`

Which game do you want all the controls for?

เหตุผลการผูกบริบท: all_controls_without_game

Child statuses: []

### en-unresolved-return-filter

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: PC prices for external users

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: Competition rules for CS2

mode: `pipeline:competition_rule_overview_source`; resolved: `Competition rules for Counter-Strike 2`; outcome: `answered_complete`

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: canonicalized_explicit_generic_competition_rules

Child statuses: []

#### รอบ 3: back to the prices for tomorrow

mode: `pipeline:dialogue_state_clarification`; resolved: `back to the prices for tomorrow`; outcome: `needs_clarification`

Which topic or selection does "all" refer to: controls, prices, game lists, or zones?

เหตุผลการผูกบริบท: resume_contains_unresolved_new_conditions

Child statuses: []

### en-explicit-return-new-target

ผล: ผ่าน

เกณฑ์: {"transport": true, "required_content": true, "forbidden_content": true, "operation": true}

#### รอบ 1: VALORANT controls

mode: `pipeline:structured_game_controls_en`; resolved: `VALORANT controls`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: PC prices for external users

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 3: back to controls for Beat Saber

mode: `pipeline:structured_game_controls_en`; resolved: `back to controls for Beat Saber`; outcome: `answered_complete`

Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

## เคส r40 หลัก

### clarify-th-0

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### clarify-th-1

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: ขอดูปุ่มทั้งหมด

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มทั้งหมด`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### clarify-th-2

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: ช่วยบอกปุ่มเกมหน่อยครับ

mode: `pipeline:game_control_missing_game_context`; resolved: `ช่วยบอกปุ่มเกมหน่อยครับ`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### clarify-th-3

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: เกมมีปุ่มอะไรบ้าง

mode: `pipeline:game_control_missing_game_context`; resolved: `เกมมีปุ่มอะไรบ้าง`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### clarify-th-4

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: ปุ่มควบคุมต้องกดยังไง

mode: `pipeline:game_control_missing_game_context`; resolved: `ปุ่มควบคุมต้องกดยังไง`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### clarify-th-5

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: อยากรู้วิธีบังคับเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `อยากรู้วิธีบังคับเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: not_followup

Child statuses: []

### clarify-en-0

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### clarify-en-1

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: Can I see the game controls?

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Can I see the game controls?`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### clarify-en-2

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: What buttons can I use?

mode: `pipeline:game_control_missing_game_context_en`; resolved: `What buttons can I use?`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### clarify-en-3

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: Tell me the keyboard controls please

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Tell me the keyboard controls please`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### clarify-en-4

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: How do I control the game?

mode: `pipeline:game_control_missing_game_context_en`; resolved: `How do I control the game?`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### clarify-en-5

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: List all game buttons

mode: `pipeline:game_control_missing_game_context_en`; resolved: `List all game buttons`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### clarify-en-6

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: I need the controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `I need the controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### multi-controls-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT กับ Mario Kart 8 Deluxe

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; Mario Kart 8 Deluxe มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Mario Kart 8 Deluxe มีปุ่มควบคุมอะไรบ้าง
Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม:
Nintendo Switch
•    L (Left Stick): เลี้ยว / ควบคุมทิศทาง - บังคับพวงมาลัยรถให้เลี้ยวไปทางซ้ายหรือขวา
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/57

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "games", "pipeline:structured_game_controls"]]

### multi-controls-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and Mario Kart 8 Deluxe

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Mario Kart 8 Deluxe?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Mario Kart 8 Deluxe?
Mario Kart 8 Deluxe controls:
- L (Left Stick): Steer
- A: Accelerate
- B: Brake
- X: Look Backward
- ZL: Use Item / Horn
- ZR: Drift
- + (Plus): Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/57

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### multi-controls-typo-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: Valoant and Beat Saber please

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Beat Saber?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### multi-catalog-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "all_selected_zones": true, "no_unselected_zones": true, "catalog_operation": true}

#### รอบ 1: มีเกมอะไรให้เล่นบ้าง

mode: `pipeline:structured_games_catalog`; resolved: `มีเกมอะไรให้เล่นบ้าง`; outcome: `answered_complete`

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

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: PC กับ PS5

mode: `pipeline:multi_question_splitter`; resolved: `PC มีเกมอะไรบ้าง; PlayStation 5 มีเกมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: PC มีเกมอะไรบ้าง
PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

คำถามที่ 2: PlayStation 5 มีเกมอะไรบ้าง
PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้

PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
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
หมายเหตุ: PlayStation 5 #01 และ #02 ใช้รายการเกมเดียวกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: selected_multiple_catalog_services

Child statuses: [["task-1", "answered", "games", "pipeline:structured_service_game_availability"], ["task-2", "answered", "games", "pipeline:structured_service_game_availability"]]

### multi-catalog-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "all_selected_zones": true, "no_unselected_zones": true, "catalog_operation": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PC and PS5

mode: `pipeline:multi_question_splitter`; resolved: `What games are available in PC?; What games are available in PlayStation 5?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PC?
There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in PlayStation 5?
There are currently 17 verified games in PlayStation 5 Zone.

PlayStation 5 Zone (17 games)
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
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: selected_multiple_catalog_services

Child statuses: [["task-1", "answered", "games", "pipeline:structured_games_catalog_en"], ["task-2", "answered", "games", "pipeline:structured_games_catalog_en"]]

### multi-catalog-typo-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "all_selected_zones": true, "no_unselected_zones": true, "catalog_operation": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PC and cockpik please

mode: `pipeline:multi_question_splitter`; resolved: `What games are available in PC?; What games are available in Cockpit?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PC?
There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in Cockpit?
There are currently 1 verified games in Cockpit Zone.

Cockpit Zone (1 game)
•    Gran Turismo 7
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: selected_multiple_catalog_services

Child statuses: [["task-1", "answered", "games", "pipeline:structured_games_catalog_en"], ["task-2", "answered", "games", "pipeline:structured_games_catalog_en"]]

### roman-edition-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "not_other_edition": true, "not_missing_target": true, "not_catalog": true, "source_status": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: TEKKEN IX

mode: `pipeline:game_edition_unconfirmed`; resolved: `What are the controls for tekken ix?`; outcome: `no_answer`

I do not have verified information for tekken ix in the recorded studio catalog. Please confirm the game title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: unrecognized_missing_control_game

Child statuses: []

### roman-edition-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "not_other_edition": true, "not_missing_target": true, "not_catalog": true, "source_status": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: TEKKEN IX

mode: `pipeline:game_edition_unconfirmed`; resolved: `tekken ix มีปุ่มควบคุมอะไรบ้าง`; outcome: `no_answer`

ยังไม่พบข้อมูลยืนยันของ tekken ix ในรายการเกมของศูนย์ครับ กรุณายืนยันชื่อเกมและภาคที่ต้องการอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: unrecognized_missing_control_game

Child statuses: []

### new-operation-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "new_operation": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: What is VALORANT?

mode: `pipeline:structured_game_detail_en`; resolved: `What is VALORANT?`; outcome: `answered_complete`

Verified English information:
VALORANT
Genre: Tactical 5v5 team-based FPS
Overview: VALORANT is a tactical shooter game where players select agents with unique skills and play as either attackers or defenders in each round.
How to play: Attackers must plant the Spike; defenders must defend the area or defuse the Spike. Play emphasizes aiming, communication, ability use and teamwork.
Available at: PC Zone
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

### new-operation-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "new_operation": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT คืออะไร

mode: `pipeline:structured_game_detail`; resolved: `VALORANT คืออะไร`; outcome: `answered_complete`

VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ
แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5
วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

### unknown-latin-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "no_substitute": true, "received_name": true, "keeps_operation": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: Minecraft

mode: `pipeline:game_controls_target_unconfirmed`; resolved: `What are the controls for minecraft?`; outcome: `no_answer`

I could not find verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: unrecognized_missing_control_game

Child statuses: []

### unknown-thai-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "no_substitute": true, "received_name": true, "keeps_operation": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: มายคราฟต์

mode: `pipeline:game_controls_target_unconfirmed`; resolved: `มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง`; outcome: `no_answer`

ยังไม่พบข้อมูลปุ่มควบคุมที่ยืนยันสำหรับเกมที่คุณระบุในฐานข้อมูลของศูนย์ครับ กรุณาตรวจชื่อเต็มและภาคของเกมอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: unrecognized_missing_control_game

Child statuses: []

### known-controls-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: What are the controls for VALORANT?

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

### known-controls-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

### hardware-not-game-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "not_generic_controls": true}

#### รอบ 1: What controller model does the PS5 zone use?

mode: `pipeline:equipment_spec_unverified_en`; resolved: `What controller model does the PS5 zone use?`; outcome: `no_answer`

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### booking-button-not-controls-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "not_generic_controls": true, "booking_not_game": true}

#### รอบ 1: Where is the booking button?

mode: `pipeline:booking_navigation`; resolved: `Where is the booking button?`; outcome: `answered_complete`

Open the studio booking page using the link below. I cannot confirm the current button position on that page.
Booking page: https://esports.computing.psu.ac.th/reservation

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### equipment-damage-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "not_generic_controls": true}

#### รอบ 1: คีย์บอร์ดพังต้องทำยังไง

mode: `pipeline:penalty_fast_path`; resolved: `คีย์บอร์ดพังต้องทำยังไง`; outcome: `answered_complete`

ต้องรับผิดชอบค่าปรับ/ค่าซ่อมครับ หากทำเมาส์หรืออุปกรณ์ของศูนย์เสียหาย โดยข้อมูลกฎที่มีระบุว่า ความเสียหายเล็กน้อยคิด 100-500 บาท และความเสียหายปานกลางคิด 500-2,000 บาทหรือตามราคาซ่อมจริง หากเสียหายร้ายแรงอาจต้องชดเชยเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### explicit-reject-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "not_generic_controls": true, "price_selected_pc": true}

#### รอบ 1: ไม่เอาปุ่ม ขอราคาของ PC

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

## สำนวน r40

### fresh-clarify-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: Could you show me all the controls please?

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Could you show me all the controls please?`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

### fresh-clarify-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: ช่วยแสดงปุ่มของเกมให้หน่อยค่ะ

mode: `pipeline:game_control_missing_game_context`; resolved: `ช่วยแสดงปุ่มของเกมให้หน่อยค่ะ`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### fresh-mixed-clarify

ผล: ผ่าน

เกณฑ์: {"http_success": true, "asks_game": true, "no_catalog": true}

#### รอบ 1: ขอดู controls ทั้งหมดหน่อย

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดู controls ทั้งหมดหน่อย`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

### fresh-three-controls-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: วาโล, Beat Saber และ Mario Kart 8 Deluxe

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; Beat Saber มีปุ่มควบคุมอะไรบ้าง; Mario Kart 8 Deluxe มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Beat Saber มีปุ่มควบคุมอะไรบ้าง
Beat Saber ปุ่มที่ตรงกับคำถาม:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

คำถามที่ 3: Mario Kart 8 Deluxe มีปุ่มควบคุมอะไรบ้าง
Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม:
Nintendo Switch
•    L (Left Stick): เลี้ยว / ควบคุมทิศทาง - บังคับพวงมาลัยรถให้เลี้ยวไปทางซ้ายหรือขวา
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/57

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "games", "pipeline:structured_game_controls"], ["task-3", "answered", "games", "pipeline:structured_game_controls"]]

### fresh-repeat-selection-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT, VALORANT and Beat Saber

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Beat Saber?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### fresh-three-zones-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "all_selected_zones": true, "no_unselected_zones": true, "catalog_operation": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PS5 / Nintendo Switch / VR

mode: `pipeline:multi_question_splitter`; resolved: `What games are available in PlayStation 5?; What games are available in Nintendo Switch?; What games are available in VR?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PlayStation 5?
There are currently 17 verified games in PlayStation 5 Zone.

PlayStation 5 Zone (17 games)
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
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in Nintendo Switch?
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

Question 3: What games are available in VR?
There are currently 4 verified games in VR Zone.

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: selected_multiple_catalog_services

Child statuses: [["task-1", "answered", "games", "pipeline:structured_games_catalog_en"], ["task-2", "answered", "games", "pipeline:structured_games_catalog_en"], ["task-3", "answered", "games", "pipeline:structured_games_catalog_en"]]

### fresh-partial-controls-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "known_target_answered": true, "partial_explicit": true, "not_substituted_edition": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and Minecraft

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for minecraft?`; outcome: `answered_partial`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for minecraft?
I do not have verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

### fresh-partial-controls-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "known_target_answered": true, "partial_explicit": true, "not_substituted_edition": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT กับ มายคราฟต์

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง; มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_partial`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: มายคราฟต์ มีปุ่มควบคุมอะไรบ้าง
ยังไม่พบข้อมูลปุ่มควบคุมที่ยืนยันสำหรับเกมที่คุณระบุในฐานข้อมูลของศูนย์ครับ กรุณาตรวจชื่อเต็มและภาคของเกมอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "missing", "games", "pipeline:game_controls_target_unconfirmed"]]

### fresh-edition-in-multi

ผล: ผ่าน

เกณฑ์: {"http_success": true, "known_target_answered": true, "partial_explicit": true, "not_substituted_edition": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT and TEKKEN IX

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for tekken ix?`; outcome: `answered_partial`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for tekken ix?
I do not have verified information for tekken ix in the recorded studio catalog. Please confirm the game title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "missing", "games", "pipeline:game_edition_unconfirmed"]]

### fresh-accepted-roman

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: What are the controls for TEKKEN VIII?

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for TEKKEN VIII?`; outcome: `answered_complete`

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

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

### fresh-number-not-edition

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: Show me VALORANT controls for 2 people

mode: `pipeline:structured_game_controls_en`; resolved: `Show me VALORANT controls for 2 people`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

### fresh-unknown-multi-service

ผล: ผ่าน

เกณฑ์: {"http_success": true, "not_partial_silently": true, "explicit_clarification": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PC and washing machine

mode: `pipeline:games_catalog_selection_clarification`; resolved: `PC and washing machine`; outcome: `needs_clarification`

I could not match these choices to a studio zone: washing machine. Please specify all the zones you want, such as PC and VR.

เหตุผลการผูกบริบท: unresolved_multiple_catalog_services

Child statuses: []

## ขอบเขตและข้อจำกัด

### limit-five-controls

ผล: ผ่าน

เกณฑ์: {"http_success": true, "safe_limit": true, "explicit_limit": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT, Beat Saber, Mario Kart 8 Deluxe, TEKKEN 8 and Gran Turismo 7

mode: `pipeline:dialogue_selection_clarification`; resolved: `VALORANT, Beat Saber, Mario Kart 8 Deluxe, TEKKEN 8 and Gran Turismo 7`; outcome: `needs_clarification`

Please select up to 4 items per reply so I can answer every selected item. You can ask for the remaining items in another message.

เหตุผลการผูกบริบท: too_many_selected_targets

Child statuses: []

### limit-five-zones

ผล: ผ่าน

เกณฑ์: {"http_success": true, "safe_limit": true, "explicit_limit": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PC, PS5, Nintendo Switch, Cockpit and VR

mode: `pipeline:dialogue_selection_clarification`; resolved: `PC, PS5, Nintendo Switch, Cockpit and VR`; outcome: `needs_clarification`

Please select up to 4 items per reply so I can answer every selected item. You can ask for the remaining items in another message.

เหตุผลการผูกบริบท: too_many_selected_targets

Child statuses: []

### four-control-targets

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT, Beat Saber, Mario Kart 8 Deluxe and TEKKEN 8

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT?; What are the controls for Beat Saber?; What are the controls for Mario Kart 8 Deluxe?; What are the controls for TEKKEN 8?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

Question 3: What are the controls for Mario Kart 8 Deluxe?
Mario Kart 8 Deluxe controls:
- L (Left Stick): Steer
- A: Accelerate
- B: Brake
- X: Look Backward
- ZL: Use Item / Horn
- ZR: Drift
- + (Plus): Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/57

Question 4: What are the controls for TEKKEN 8?
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

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"], ["task-3", "answered", "games", "pipeline:structured_game_controls_en"], ["task-4", "answered", "games", "pipeline:structured_game_controls_en"]]

### family-select-both-controls

ผล: ผ่าน

เกณฑ์: {"http_success": true, "control_operation": true, "all_targets": true, "not_missing_target": true}

#### รอบ 1: What are the controls for Call of Duty?

mode: `pipeline:game_family_clarification_en`; resolved: `What are the controls for Call of Duty?`; outcome: `needs_clarification`

Which game do you mean: Call of Duty: Modern Warfare III, Call of Duty: Warzone? Please name the exact title so I can check its controls.

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: Call of Duty: Warzone and Call of Duty: Modern Warfare III

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for Call of Duty: Warzone?; What are the controls for Call of Duty: Modern Warfare III?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for Call of Duty: Warzone?
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

Question 2: What are the controls for Call of Duty: Modern Warfare III?
Call of Duty: Modern Warfare III controls:
- L1: Jump/Mantle
- R3: Change Stance/Slide/Dive
- Cross: Use Tactical Equipment
- Circle: Melee
- L2: Aim Down Sight
- R2: Fire Weapon
- R1: Use Lethal Equipment
- Square: Interact/Reload
- Triangle: Switch Weapon
- L3: Sprint/Tactical Sprint/Focus
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.gamepur.com/guides/best-modern-warfare-3-controller-settings-aim-assist-deadzones-button-layout

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### unknown-edition-first-child

ผล: ผ่าน

เกณฑ์: {"http_success": true, "known_target_answered": true, "partial_explicit": true, "not_substituted_edition": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: TEKKEN IX and VALORANT

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for tekken ix?; What are the controls for VALORANT?`; outcome: `answered_partial`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for tekken ix?
I do not have verified information for tekken ix in the recorded studio catalog. Please confirm the game title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

Question 2: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: selected_multiple_control_games

Child statuses: [["task-1", "missing", "games", "pipeline:game_edition_unconfirmed"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### retry-unresolved-zone

ผล: ผ่าน

เกณฑ์: {"http_success": true, "selected_zones": true, "no_extra_zone": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PC and washing machine

mode: `pipeline:games_catalog_selection_clarification`; resolved: `PC and washing machine`; outcome: `needs_clarification`

I could not match these choices to a studio zone: washing machine. Please specify all the zones you want, such as PC and VR.

เหตุผลการผูกบริบท: unresolved_multiple_catalog_services

Child statuses: []

#### รอบ 3: PC and VR

mode: `pipeline:multi_question_splitter`; resolved: `What games are available in PC?; What games are available in VR?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PC?
There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in VR?
There are currently 4 verified games in VR Zone.

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: selected_multiple_catalog_services

Child statuses: [["task-1", "answered", "games", "pipeline:structured_games_catalog_en"], ["task-2", "answered", "games", "pipeline:structured_games_catalog_en"]]

### mixed-booking-navigation-price

ผล: ผ่าน

เกณฑ์: {"http_success": true, "expected_requests": true, "no_dropped_parts": true, "child_operations": true, "no_missing_known_target": true}

#### รอบ 1: Where is the booking button and what are the PC prices?

mode: `pipeline:multi_question_splitter`; resolved: `Where is the booking button and what are the PC prices?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: Where is the booking button
Open the studio booking page using the link below. I cannot confirm the current button position on that page.
Booking page: https://esports.computing.psu.ac.th/reservation

Question 2: what are the PC prices
PC - 1 hour (1 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 25 THB
- General adults: 70 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: [["task-1", "answered", "reservation", "pipeline:booking_navigation"], ["task-2", "answered", "service_fee", "pipeline:structured_service_fee_en"]]

### mixed-booking-navigation-price-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "expected_requests": true, "no_dropped_parts": true, "child_operations": true, "no_missing_known_target": true}

#### รอบ 1: ปุ่มจองอยู่ไหนและราคาของ PC เท่าไหร่

mode: `pipeline:multi_question_splitter`; resolved: `ปุ่มจองอยู่ไหนและราคาของ PC เท่าไหร่`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: ปุ่มจองอยู่ไหน
เปิดหน้าจองของศูนย์ได้จากลิงก์ด้านล่างครับ ยังไม่มีข้อมูลยืนยันตำแหน่งปุ่มในหน้าเว็บฉบับปัจจุบัน
หน้าจอง: https://esports.computing.psu.ac.th/reservation

คำถามที่ 2: ราคาของ PC เท่าไหร่
ราคา PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท
•    General Adult / บุคคลทั่วไป: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: topic_shift

Child statuses: [["task-1", "answered", "reservation", "pipeline:booking_navigation"], ["task-2", "answered", "service_fee", "pipeline:deterministic_calculator_fast"]]

## คำถามผสมราคา/ปุ่ม

### mixed-controls-price-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "expected_requests": true, "no_dropped_parts": true, "child_operations": true, "no_missing_known_target": true}

#### รอบ 1: What are the controls for VALORANT and what are the PC prices?

mode: `pipeline:multi_question_splitter`; resolved: `What are the controls for VALORANT and what are the PC prices?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: what are the PC prices
PC - 1 hour (1 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 25 THB
- General adults: 70 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls_en"], ["task-2", "answered", "service_fee", "pipeline:structured_service_fee_en"]]

### mixed-price-controls-en

ผล: ผ่าน

เกณฑ์: {"http_success": true, "expected_requests": true, "no_dropped_parts": true, "child_operations": true, "no_missing_known_target": true}

#### รอบ 1: What are the PC prices and what are the controls for VALORANT?

mode: `pipeline:multi_question_splitter`; resolved: `What are the PC prices and what are the controls for VALORANT?`; outcome: `answered_complete`

This question contains several topics. Here are the answers separately:

Question 1: What are the PC prices
PC - 1 hour (1 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 25 THB
- General adults: 70 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

Question 2: what are the controls for VALORANT
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: [["task-1", "answered", "service_fee", "pipeline:structured_service_fee_en"], ["task-2", "answered", "games", "pipeline:structured_game_controls_en"]]

### mixed-controls-price-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "expected_requests": true, "no_dropped_parts": true, "child_operations": true, "no_missing_known_target": true}

#### รอบ 1: VALORANT มีปุ่มอะไรบ้าง และ PC ราคาเท่าไหร่

mode: `pipeline:multi_question_splitter`; resolved: `VALORANT มีปุ่มอะไรบ้าง และ PC ราคาเท่าไหร่`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: PC ราคาเท่าไหร่
ราคา PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท
•    General Adult / บุคคลทั่วไป: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: [["task-1", "answered", "games", "pipeline:structured_game_controls"], ["task-2", "answered", "service_fee", "pipeline:deterministic_calculator_fast"]]

### mixed-price-controls-th

ผล: ผ่าน

เกณฑ์: {"http_success": true, "expected_requests": true, "no_dropped_parts": true, "child_operations": true, "no_missing_known_target": true}

#### รอบ 1: PC ราคาเท่าไหร่ และ VALORANT มีปุ่มอะไรบ้าง

mode: `pipeline:multi_question_splitter`; resolved: `PC ราคาเท่าไหร่ และ VALORANT มีปุ่มอะไรบ้าง`; outcome: `answered_complete`

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: PC ราคาเท่าไหร่
ราคา PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 25 บาท
•    General Adult / บุคคลทั่วไป: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

คำถามที่ 2: VALORANT มีปุ่มอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: [["task-1", "answered", "service_fee", "pipeline:deterministic_calculator_fast"], ["task-2", "answered", "games", "pipeline:structured_game_controls"]]

## สองรอบ ราคา/กฎ/หัวข้อ

### th-price-PC

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: อยากรู้ราคาของบุคคลภายนอก

mode: `pipeline:protected_price_missing_service`; resolved: `ค่าบริการ  บุคคลภายนอก`; outcome: `needs_clarification`

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: PC

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-price-PS5

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: อยากรู้ราคาของบุคคลภายนอก

mode: `pipeline:protected_price_missing_service`; resolved: `ค่าบริการ  บุคคลภายนอก`; outcome: `needs_clarification`

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: PS5

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PlayStation 5 บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-price-Nintendo

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: อยากรู้ราคาของบุคคลภายนอก

mode: `pipeline:protected_price_missing_service`; resolved: `ค่าบริการ  บุคคลภายนอก`; outcome: `needs_clarification`

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: Nintendo

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ Nintendo Switch บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

Nintendo Switch — 60 นาที/แพ็กเกจ (1-2 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 140 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-price-Cockpit

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: อยากรู้ราคาของบุคคลภายนอก

mode: `pipeline:protected_price_missing_service`; resolved: `ค่าบริการ  บุคคลภายนอก`; outcome: `needs_clarification`

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: Cockpit

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ Cockpit บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

Cockpit — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 65 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 200 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-price-VR

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: อยากรู้ราคาของบุคคลภายนอก

mode: `pipeline:protected_price_missing_service`; resolved: `ค่าบริการ  บุคคลภายนอก`; outcome: `needs_clarification`

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: VR

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ VR บุคคลภายนอก`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

VR — 30 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 525 บาท/แพ็กเกจ

VR — 60 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 1,050 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-rules-CS2

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอรายละเอียดกติกาการแข่งขัน

mode: `pipeline:competition_target_clarification`; resolved: `ขอรายละเอียดกติกาการแข่งขัน`; outcome: `needs_clarification`

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: CS2

mode: `pipeline:competition_rule_full_sections_source`; resolved: `ขอรายละเอียดกติกาการแข่งขัน Counter-Strike 2`; outcome: `answered_partial`

กติกา Counter-Strike 2: รายละเอียดจากเอกสารที่บันทึกไว้ (แสดงแล้ว 8/56 ส่วน)

•    ข้อมูลทั่วไป (General Information)

•    ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

•    เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

•    ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

•    การจับฉลากและตารางเวลา

•    การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

•    การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

•    ข้อจำกัด

ยังเหลือ 48 ส่วน พิมพ์ “ต่อ” เพื่อดูหน้าถัดไปครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### th-rules-RoV

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอรายละเอียดกติกาการแข่งขัน

mode: `pipeline:competition_target_clarification`; resolved: `ขอรายละเอียดกติกาการแข่งขัน`; outcome: `needs_clarification`

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: RoV

mode: `pipeline:competition_rule_full_sections_source`; resolved: `ขอรายละเอียดกติกาการแข่งขัน Arena of Valor (RoV)`; outcome: `answered_partial`

กติกา Arena of Valor (RoV): รายละเอียดจากเอกสารที่บันทึกไว้ (แสดงแล้ว 5/12 ส่วน)

กติกาการแข่งขัน Blueket Games 2025
รายการอีสปอร์ต
เกม Arena of Valor (RoV)

ประเภททีมชาย

•    กำหนดการแข่งขัน
1.1. แข่งขันออฟไลน์ วันที่ 11 กันยายน 2568
· เวลา 8.00-8.30 ลงทะเบียน
· เวลา 8.30-8.40 แบ่งสายการแข่งขัน
· เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
· เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
· เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
· เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
· เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3

•    สถานที่แข่งขัน
2.1. PSU Esports Studio – Phuket (อาคาร 5 ชั้น 1)

•    รูปแบบการแข่งขัน
3.1. แข่งแบบออฟไลน์
3.2. แข่ง Best of 3 (BO3) ทุกรอบ

ยังเหลือ 7 ส่วน พิมพ์ “ต่อ” เพื่อดูหน้าถัดไปครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### th-rules-TEKKEN 8

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอรายละเอียดกติกาการแข่งขัน

mode: `pipeline:competition_target_clarification`; resolved: `ขอรายละเอียดกติกาการแข่งขัน`; outcome: `needs_clarification`

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: TEKKEN 8

mode: `pipeline:competition_rule_full_sections_source`; resolved: `ขอรายละเอียดกติกาการแข่งขัน Tekken 8`; outcome: `answered_complete`

กติกา Tekken 8: รายละเอียดจากเอกสารที่บันทึกไว้ (แสดงแล้ว 7/7 ส่วน)

กติกาการแข่งขัน
•    แข่งขันแบบ ออฟไลน์ (Offline)
•    ใช้เครื่องเกม PlayStation 5
•    แข่งขันแบบ เดี่ยว (1v1)
•    รูปแบบการแข่งขัน:
•    FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน
•    ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
•    หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน

ตัวละครและการตั้งค่า
•    สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
•    ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
•    ต้องใช้ สกินมาตรฐาน เท่านั้น
•    อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ
•    ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ
•    เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
•    หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที

การตั้งค่าเกม
•    จำนวนรอบต่อเกม (Round): 3
•    เวลาแข่งขันต่อรอบ (Timer): 60 วินาที
•    Advantage: No advantage
•    Stage: Random

มารยาทในการแข่งขัน
•    ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
•    ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น

ข้อตกลงและข้อปฏิบัติ
•    ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
•    ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
•    คำตัดสินของกรรมการถือเป็นที่สิ้นสุด
•    กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม

การหยุดเกม
•    ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ
•    หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที
•    การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน
•    หากกดหยุดเกมโดยไม่จำเป็น จะได้รับโทษเช่นเดียวกับการออกจากเกมก่อนจบ

การแก้ปัญหาข้อพิพาท
•    หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที
•    ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด
หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
แสดงครบส่วนที่อ่านได้ของเอกสารที่บันทึกไว้แล้ว ไม่ได้ยืนยันกติกาของรายการใหม่ครับ
เอกสารมีเงื่อนไขการหยุดเกมที่ขัดกัน ต้องให้ผู้จัดยืนยันการใช้เงื่อนไขครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### th-rules-VALORANT

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอรายละเอียดกติกาการแข่งขัน

mode: `pipeline:competition_target_clarification`; resolved: `ขอรายละเอียดกติกาการแข่งขัน`; outcome: `needs_clarification`

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: VALORANT

mode: `pipeline:competition_rule_full_sections_source`; resolved: `ขอรายละเอียดกติกาการแข่งขัน VALORANT`; outcome: `answered_partial`

กติกา VALORANT: รายละเอียดจากเอกสารที่บันทึกไว้ (แสดงแล้ว 8/25 ส่วน)

พื้นที่การแข่งขันและกฎระเบียบ
•    จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
•    อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
•    เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
•    อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
กระบวนการแข่งขัน

ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร
•    เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
•    ข้อจำกัดเนื้อหาใหม่
•    เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
•    แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
•    การตั้งค่าเกม (Settings)
•    ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)
•    ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน
•    การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่
•    Abyss
•    Ascent
•    Bind
•    Corrode
•    Haven
•    Lotus
•    Sunset
•    การเลือกฝั่ง
•    ใช้วิธีการโยนเหรียญ
•    การ Ban map
•    แบนจนเหลือ 3 แผนที่

กระบวนการหลังจบแมตช์
•    การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที
•    การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0
การหยุดเกม

การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน

•    เวลานอกทางยุทธวิธี (Tactical Timeout)
•    ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
•    เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

•    การหยุดเกมทางเทคนิค (Technical Pause)
•    ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์
•    ห้ามผู้เล่นสื่อสารกัน (ทั้งเสียงและข้อความ) เว้นแต่ได้รับอนุญาต

•    การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
•    ขอได้ 1 ครั้งต่อแผนที่
•    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
กฎเกี่ยวกับบั๊ก
บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำหนดแนวทางปฏิบัติ ดังนี้
•    Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
•    Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้
•    Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้
•    การย้อนรอบ (Round Rollback)
•    หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้
•    หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge
•    หากเป็น Game Breaking Bug เจ้าหน้าที่จะสั่งย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที
การใช้ช่องโหว่ (Exploit Adjudication)

การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด
•    การใช้สกิลเอเจนท์
•    ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่
•    ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
•    ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง
•    การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ
บทลงโทษ
เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact)

ยังเหลือ 17 ส่วน พิมพ์ “ต่อ” เพื่อดูหน้าถัดไปครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### th-controls-VALORANT

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: VALORANT

mode: `pipeline:structured_game_controls`; resolved: `VALORANT มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: selected_missing_control_game

Child statuses: []

### th-controls-Mario Kart 8 Deluxe

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: Mario Kart 8 Deluxe

mode: `pipeline:structured_game_controls`; resolved: `Mario Kart 8 Deluxe มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม:
Nintendo Switch
•    L (Left Stick): เลี้ยว / ควบคุมทิศทาง - บังคับพวงมาลัยรถให้เลี้ยวไปทางซ้ายหรือขวา
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/57

เหตุผลการผูกบริบท: selected_missing_control_game

Child statuses: []

### th-controls-Beat Saber

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอดูปุ่มควบคุมเกม

mode: `pipeline:game_control_missing_game_context`; resolved: `ขอดูปุ่มควบคุมเกม`; outcome: `needs_clarification`

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

เหตุผลการผูกบริบท: no_matching_context_resolution

Child statuses: []

#### รอบ 2: Beat Saber

mode: `pipeline:structured_game_controls`; resolved: `Beat Saber มีปุ่มควบคุมอะไรบ้าง`; outcome: `answered_complete`

Beat Saber ปุ่มที่ตรงกับคำถาม:
PlayStation VR2 / PS5
•    Left PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือซ้าย - ใช้การขยับคอนโทรลเลอร์ฝั่งซ้ายเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
•    Right PS VR2 Sense controller motion: ฟันบล็อกด้วยดาบมือขวา - ใช้การขยับคอนโทรลเลอร์ฝั่งขวาเพื่อฟันบล็อกตามจังหวะเพลง โดยอิงจากหลักการเล่น Beat Saber ที่ให้ผู้เล่นฟัน beat ใน VR
แหล่งข้อมูล: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_missing_control_game

Child statuses: []

### th-pc-domain-games

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: PC มีอะไรบ้าง

mode: `pipeline:ambiguity_clarification`; resolved: `PC มีอะไรบ้าง`; outcome: `needs_clarification`

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PC Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 6 เกม เช่น Call of Duty: Warzone, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS และอื่น ๆ | พิมพ์ `PC มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 6 รายการ เช่น Gaming PC รุ่น MSI MAG Infinite S3 14th, Gaming Monitor, Gaming Keyboard, Gaming Mouse, Gaming Headset และอื่น ๆ | พิมพ์ `PC มีอุปกรณ์อะไรบ้าง`
•    ราคา: PC 1 ชั่วโมง (1 คน): PSU 0 บาท, General Student 25 บาท, General Adult 70 บาท | พิมพ์ `PC ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `PC จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: เกม

mode: `pipeline:structured_service_game_availability`; resolved: `PC มีเกมอะไรบ้าง`; outcome: `answered_complete`

PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: resolved_pending_ambiguity_clarification_choice

Child statuses: []

### th-pc-domain-equipment

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: PC มีอะไรบ้าง

mode: `pipeline:ambiguity_clarification`; resolved: `PC มีอะไรบ้าง`; outcome: `needs_clarification`

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PC Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 6 เกม เช่น Call of Duty: Warzone, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS และอื่น ๆ | พิมพ์ `PC มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 6 รายการ เช่น Gaming PC รุ่น MSI MAG Infinite S3 14th, Gaming Monitor, Gaming Keyboard, Gaming Mouse, Gaming Headset และอื่น ๆ | พิมพ์ `PC มีอุปกรณ์อะไรบ้าง`
•    ราคา: PC 1 ชั่วโมง (1 คน): PSU 0 บาท, General Student 25 บาท, General Adult 70 บาท | พิมพ์ `PC ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `PC จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: อุปกรณ์

mode: `pipeline:structured_equipment_catalog`; resolved: `PC มีอุปกรณ์อะไรบ้าง`; outcome: `answered_complete`

อุปกรณ์ใน PC Zone:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units)
•    Gaming Monitor (10 Units)
•    Gaming Keyboard
•    Gaming Mouse
•    Gaming Headset
•    Gaming Chair (10 Units)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

เหตุผลการผูกบริบท: resolved_pending_ambiguity_clarification_choice

Child statuses: []

### th-pc-domain-service_fee

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: PC มีอะไรบ้าง

mode: `pipeline:ambiguity_clarification`; resolved: `PC มีอะไรบ้าง`; outcome: `needs_clarification`

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PC Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 6 เกม เช่น Call of Duty: Warzone, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS และอื่น ๆ | พิมพ์ `PC มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 6 รายการ เช่น Gaming PC รุ่น MSI MAG Infinite S3 14th, Gaming Monitor, Gaming Keyboard, Gaming Mouse, Gaming Headset และอื่น ๆ | พิมพ์ `PC มีอุปกรณ์อะไรบ้าง`
•    ราคา: PC 1 ชั่วโมง (1 คน): PSU 0 บาท, General Student 25 บาท, General Adult 70 บาท | พิมพ์ `PC ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `PC จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: ราคา

mode: `pipeline:structured_service_fee_conversation`; resolved: `ค่าบริการ PC`; outcome: `answered_complete`

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### th-pc-domain-reservation

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: PC มีอะไรบ้าง

mode: `pipeline:ambiguity_clarification`; resolved: `PC มีอะไรบ้าง`; outcome: `needs_clarification`

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PC Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 6 เกม เช่น Call of Duty: Warzone, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS และอื่น ๆ | พิมพ์ `PC มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 6 รายการ เช่น Gaming PC รุ่น MSI MAG Infinite S3 14th, Gaming Monitor, Gaming Keyboard, Gaming Mouse, Gaming Headset และอื่น ๆ | พิมพ์ `PC มีอุปกรณ์อะไรบ้าง`
•    ราคา: PC 1 ชั่วโมง (1 คน): PSU 0 บาท, General Student 25 บาท, General Adult 70 บาท | พิมพ์ `PC ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `PC จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: จอง

mode: `pipeline:structured_reservation_fact`; resolved: `PC จองยังไง`; outcome: `answered_complete`

สำหรับ PC ให้เลือกบริการ/โซน PC ในระบบจอง แล้วทำตามขั้นตอนนี้ครับ
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: resolved_pending_ambiguity_clarification_choice

Child statuses: []

### th-game-zone

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: มีเกมอะไรให้เล่นบ้าง

mode: `pipeline:structured_games_catalog`; resolved: `มีเกมอะไรให้เล่นบ้าง`; outcome: `answered_complete`

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

เหตุผลการผูกบริบท: not_followup

Child statuses: []

#### รอบ 2: PS5

mode: `pipeline:structured_service_game_availability`; resolved: `PlayStation 5 มีเกมอะไรบ้าง`; outcome: `answered_complete`

PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้

PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
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
หมายเหตุ: PlayStation 5 #01 และ #02 ใช้รายการเกมเดียวกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

เหตุผลการผูกบริบท: selected_catalog_service

Child statuses: []

### en-price-PC

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What are the service prices for external users?

mode: `pipeline:protected_price_missing_service`; resolved: `Service prices  external users`; outcome: `needs_clarification`

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: PC

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-price-PS5

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What are the service prices for external users?

mode: `pipeline:protected_price_missing_service`; resolved: `Service prices  external users`; outcome: `needs_clarification`

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: PS5

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PlayStation 5 external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PlayStation 5 — 60 minutes/package (1-2 people)
• PSU alumni / students from other institutions: 50 THB/package
• General adults: 150 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-price-Nintendo

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What are the service prices for external users?

mode: `pipeline:protected_price_missing_service`; resolved: `Service prices  external users`; outcome: `needs_clarification`

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: Nintendo

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices Nintendo Switch external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

Nintendo Switch — 60 minutes/package (1-2 people)
• PSU alumni / students from other institutions: 50 THB/package
• General adults: 140 THB/package

Nintendo Switch — 60 minutes/package (3-4 people)
• PSU alumni / students from other institutions: 100 THB/package
• General adults: 280 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-price-Cockpit

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What are the service prices for external users?

mode: `pipeline:protected_price_missing_service`; resolved: `Service prices  external users`; outcome: `needs_clarification`

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: Cockpit

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices Cockpit external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

Cockpit — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 65 THB/package
• General adults: 200 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-price-VR

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What are the service prices for external users?

mode: `pipeline:protected_price_missing_service`; resolved: `Service prices  external users`; outcome: `needs_clarification`

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

#### รอบ 2: VR

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices VR external users`; outcome: `answered_complete`

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

VR — 30 minutes/package (1-5 people)
• PSU alumni / students from other institutions: 190 THB/package
• General adults: 525 THB/package

VR — 60 minutes/package (1-5 people)
• PSU alumni / students from other institutions: 375 THB/package
• General adults: 1,050 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-rules-CS2

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: I want detailed competition rules

mode: `pipeline:competition_target_clarification_en`; resolved: `I want detailed competition rules`; outcome: `needs_clarification`

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: CS2

mode: `pipeline:competition_rule_full_sections_source`; resolved: `I want detailed competition rules Counter-Strike 2`; outcome: `answered_partial`

Counter-Strike 2: detailed sections from the recorded rulebook (8/56 sections covered).

1. General Information

Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.

The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

Drawing of lots and schedule

The competition will be held for one day at PSU Esports Studio - Phuket, Prince of Songkla University, Phuket Campus.

Communication: All participants must use the Discord server designated by the Center.

Limitations

48 sections remain. Type “continue” to see the next page.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### en-rules-RoV

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: I want detailed competition rules

mode: `pipeline:competition_target_clarification_en`; resolved: `I want detailed competition rules`; outcome: `needs_clarification`

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: RoV

mode: `pipeline:competition_rule_full_sections_source`; resolved: `I want detailed competition rules Arena of Valor (RoV)`; outcome: `answered_partial`

Arena of Valor (RoV): detailed sections from the recorded rulebook (5/12 sections covered).

Competition Rules for Blueket Games 2025 Esports Event Game: Arena of Valor (RoV)

Male Team Category

1. Competition schedule
1.1. Offline competition on 11 September 2025 (B.E. 2568).
* 08:00-08:30: registration
* 08:30-08:40: bracket allocation
* 08:40-10:00: round of 5 teams, Single Elimination BO3
* 10:00-11:30: semifinal match 1, Single Elimination BO3
* 12:30-14:00: semifinal match 2, Single Elimination BO3
* 14:00-15:30: third-place match, Single Elimination BO3
* 15:30-17:00: final, Single Elimination BO3

Competition Venue
2.1. PSU Esports Studio - Phuket (Building 5, Floor 1)

Competition Format 3.1. Offline Mode 3.2. Each round played as Best of 3 (BO3)
1 source sections lack a verified English rendering: competition_rules_rov_blueket_2025_men_s08_c01

6 sections remain. Type “continue” to see the next page.
Source: local://competition_rules/competition_rules_rov_blueket_2025_men

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### en-rules-TEKKEN 8

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: I want detailed competition rules

mode: `pipeline:competition_target_clarification_en`; resolved: `I want detailed competition rules`; outcome: `needs_clarification`

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: TEKKEN 8

mode: `pipeline:competition_rule_full_sections_source`; resolved: `I want detailed competition rules Tekken 8`; outcome: `answered_complete`

Tekken 8: detailed sections from the recorded rulebook (7/7 sections covered).

Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S rule (60 seconds per round) * If tied at 1-1, a deciding game will be played

Characters and Setup * Any character can be selected (except DLC characters) * No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.) * Only standard skins are permitted * Assist buttons or special assist systems are allowed * No use of bugs or glitches that provide an advantage * Once the game starts, no game pausing for any reason is permitted * Any intentional game pause will result in a penalty of losing one round immediately

Game settings
* Rounds per game (Round): 3
* Time per round (Timer): 60 seconds
* Advantage: No advantage
* Stage: Random

Competition etiquette
* Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.
* Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception.

Agreements and conduct
* Competitors must accept and follow the rules, regulations, and referees' decisions unconditionally.
* Organizers may change competition rules at any time without prior notice.
* Referees' decisions are final.
* Referees may reconsider decisions as appropriate to ensure fairness.

Game Pause * Players must not leave the game before the competition ends unless authorized by the referees. * If a player leaves the game without authorization, they will be forfeited immediately. * The game may be paused only when all players agree and there is a valid reason, such as equipment malfunction or an emergency. * Pausing the game without necessity will result in the same penalty as leaving the game prematurely.

Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice.
All readable recorded sections have been covered; this does not confirm rules for a new event.
The source has conflicting pause conditions; the organizer must confirm their application.
Source: local://competition_rules/competition_rules_tekken8_psu_esports

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### en-rules-VALORANT

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: I want detailed competition rules

mode: `pipeline:competition_target_clarification_en`; resolved: `I want detailed competition rules`; outcome: `needs_clarification`

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT

mode: `pipeline:competition_rule_full_sections_source`; resolved: `I want detailed competition rules VALORANT`; outcome: `answered_partial`

VALORANT: detailed sections from the recorded rulebook (8/25 sections covered).

Competition Area and Regulations
* Personnel: During Match Prep, no more than 6 players may be present.
* Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.
* Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match.
* Food and drinks: Only drinking water in sealed containers and chewing gum are permitted.
Competition Process

Pre-game procedure through agent selection
* Check-in: arrive at least 30 minutes before the scheduled match time.
* New agents may not be used for approximately 2 weeks after release in Competitive mode.
* New maps may not be used for approximately 4 weeks after release in Competitive mode.
* Turn OFF Blood and Bodies displays. Displaying FPS or Latency graphs during competition is prohibited.
* Map pool: Abyss, Ascent, Bind, Corrode, Haven, Lotus, Sunset (7 maps).
* Side selection uses a coin toss.
* Ban maps until 3 remain.

Post-match procedure
* Officials confirm and record the result immediately.
* If a forfeit is imposed, the result for that map is recorded as 13-0.
Game pauses

Game pauses are divided into three main types for different reasons.

1. Tactical Timeout
* 2 requests per map during regulation (first 24 rounds), 60 seconds each.
* In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over.

Technical Pause * Used when there are device malfunctions, disconnections, or software issues * Players must not communicate with each other (either verbally or in text) unless authorized

3. Player Emergency Pause
* One request per map is allowed.
* Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute.
Bug Rules
A bug is an in-game error that produces an unintended result. It is classified to determine the appropriate response:
* Play Through Bug: does not significantly affect fairness. The player must continue and may not request a Challenge.
* Major Bug: significantly affects gameplay or game mechanics and has no immediate remedy. The team may request a Challenge for review.
* Game Breaking Bug: destroys the fairness of that round so that the outcome cannot be determined.
Round Rollback
* If a bug occurs before either side deals damage, officials may roll back the round.
* If damage has already been dealt, no rollback is allowed unless through the Challenge process.
* For a Game Breaking Bug, officials will immediately roll back the round to its starting point.
Exploit Adjudication

Using player-caused bugs to gain an unintended advantage is an offense.
* Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping.
* Abilities must not be used outside map boundaries to obtain information or an advantage.
* Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid.
* Using teammates to jump higher than the normal jump range is prohibited.
Penalties
Officials assess penalties according to Intent and Impact.

17 sections remain. Type “continue” to see the next page.
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026

เหตุผลการผูกบริบท: resolved_latest_competition_target_reply

Child statuses: []

### en-controls-VALORANT

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: VALORANT

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for VALORANT?`; outcome: `answered_complete`

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

เหตุผลการผูกบริบท: selected_missing_control_game

Child statuses: []

### en-controls-Mario Kart 8 Deluxe

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: Mario Kart 8 Deluxe

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for Mario Kart 8 Deluxe?`; outcome: `answered_complete`

Mario Kart 8 Deluxe controls:
- L (Left Stick): Steer
- A: Accelerate
- B: Brake
- X: Look Backward
- ZL: Use Item / Horn
- ZR: Drift
- + (Plus): Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/57

เหตุผลการผูกบริบท: selected_missing_control_game

Child statuses: []

### en-controls-Beat Saber

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: Show me the game controls

mode: `pipeline:game_control_missing_game_context_en`; resolved: `Show me the game controls`; outcome: `needs_clarification`

Which game do you want controls for? Please provide the game title.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: Beat Saber

mode: `pipeline:structured_game_controls_en`; resolved: `What are the controls for Beat Saber?`; outcome: `answered_complete`

Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

เหตุผลการผูกบริบท: selected_missing_control_game

Child statuses: []

### en-pc-domain-games

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What does PC have?

mode: `pipeline:service_broad_choice_en`; resolved: `What does PC have?`; outcome: `needs_clarification`

Which topic about PC do you mean: games, equipment, prices, or booking? You can reply with just the topic.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: games

mode: `pipeline:structured_games_catalog_en`; resolved: `What games are available in PC?`; outcome: `answered_complete`

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: resolved_pending_ambiguity_clarification_choice

Child statuses: []

### en-pc-domain-equipment

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What does PC have?

mode: `pipeline:service_broad_choice_en`; resolved: `What does PC have?`; outcome: `needs_clarification`

Which topic about PC do you mean: games, equipment, prices, or booking? You can reply with just the topic.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: equipment

mode: `pipeline:structured_equipment_catalog_en`; resolved: `What equipment is in PC?`; outcome: `answered_complete`

Verified equipment in PC Zone:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

เหตุผลการผูกบริบท: resolved_pending_ambiguity_clarification_choice

Child statuses: []

### en-pc-domain-service_fee

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What does PC have?

mode: `pipeline:service_broad_choice_en`; resolved: `What does PC have?`; outcome: `needs_clarification`

Which topic about PC do you mean: games, equipment, prices, or booking? You can reply with just the topic.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: prices

mode: `pipeline:structured_service_fee_conversation`; resolved: `Service prices PC`; outcome: `answered_complete`

Service prices (recorded package rates):

PC — 60 minutes/package (1 person)
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

เหตุผลการผูกบริบท: validated_typed_request_plan

Child statuses: []

### en-pc-domain-reservation

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What does PC have?

mode: `pipeline:service_broad_choice_en`; resolved: `What does PC have?`; outcome: `needs_clarification`

Which topic about PC do you mean: games, equipment, prices, or booking? You can reply with just the topic.

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: booking

mode: `pipeline:rule_en`; resolved: `How do I book PC?`; outcome: `answered_complete`

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

เหตุผลการผูกบริบท: resolved_pending_ambiguity_clarification_choice

Child statuses: []

### en-game-zone

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: What games can I play?

mode: `pipeline:structured_games_catalog_en`; resolved: `What games can I play?`; outcome: `answered_complete`

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
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

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: english_context_preserved_without_rewrite

Child statuses: []

#### รอบ 2: PS5

mode: `pipeline:structured_games_catalog_en`; resolved: `What games are available in PlayStation 5?`; outcome: `answered_complete`

There are currently 17 verified games in PlayStation 5 Zone.

PlayStation 5 Zone (17 games)
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
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: selected_catalog_service

Child statuses: []

### th-cod-warzone

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: ขอรายละเอียดเกม Call of Duty

mode: `pipeline:structured_games_family`; resolved: `ขอรายละเอียดเกม Call of Duty`; outcome: `answered_complete`

พบเกมที่เกี่ยวข้องกับ Call of Duty ในรายการที่ยืนยันได้ครับ
•    Call of Duty: Modern Warfare III: เล่นได้ที่ PlayStation 5 Zone
•    Call of Duty: Warzone: เล่นได้ที่ PC Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: Warzone

mode: `pipeline:structured_game_detail`; resolved: `Call of Duty: Warzone คือเกมอะไร`; outcome: `answered_complete`

Call of Duty: Warzone: Call of Duty: Warzone คือเกมยิงแนว Battle Royale ที่เน้นการยิงรวดเร็ว การเก็บอุปกรณ์ และการเอาตัวรอดในแผนที่ขนาดใหญ่
แนวเกม: เกมยิง Battle Royale
วิธีเล่นโดยสรุป: ลงพื้นที่ หาอาวุธ ใช้ loadout/อุปกรณ์ช่วยทีม เคลื่อนตามวง และพยายามอยู่รอดจนจบเกม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

เหตุผลการผูกบริบท: selected_family_detail_game

Child statuses: []

### en-cod-mw3

ผล: ผ่าน

เกณฑ์: {"first_question": true, "category_and_operation": true, "content": true, "scope": true, "price_groups_and_recorded_rates": true, "http": true}

#### รอบ 1: Tell me about Call of Duty

mode: `pipeline:structured_games_family_en`; resolved: `Tell me about Call of Duty`; outcome: `needs_clarification`

The verified catalog has these Call of Duty titles:
- Call of Duty: Modern Warfare III: PlayStation 5 Zone
- Call of Duty: Warzone: PC Zone
Which title do you want details for? Reply with its name.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: question_has_explicit_game

Child statuses: []

#### รอบ 2: Modern Warfare III

mode: `pipeline:structured_game_detail_en`; resolved: `What is Call of Duty: Modern Warfare III?`; outcome: `answered_complete`

Verified English information:
Call of Duty: Modern Warfare III
Genre: FPS
Overview: Call of Duty: Modern Warfare III is a first-person shooter game emphasizing fast-paced missions and combat.
How to play: Aim, shoot, move, use equipment, and complete the game mode or mission objectives
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

เหตุผลการผูกบริบท: selected_family_detail_game

Child statuses: []

