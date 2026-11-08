# R120 ผลทดลองให้ Flow เดิมสอน Flow กลาง

## สรุป

**วิธีนี้ช่วยได้บางส่วน แต่ตัวอย่างสอนอย่างเดียวไม่แก้ข้อผิดพลาดทุกชั้น** รอบนี้ถ่ายทอดวิธีตีความ แผนเลือกเครื่องมือ และโครงสร้างคำตอบ โดยแก้ compiler/reader/operator ที่พบปัญหาร่วมด้วย ไม่มีการ train/fine-tune น้ำหนัก Typhoon และยังไม่ได้ติดตั้งทับ R78/production

ครูคือ Legacy R64 และนักเรียนเริ่มจาก Common R119 ใช้คำถามเดิมทั้งหมด: teacher 64 ข้อ → ตัวอย่างแผนที่ตรวจแล้ว 60 ข้อ, คัดออก 4 ข้อ; ชุดเปรียบเทียบ 27 ข้อและ development 48 ข้อ ไม่ใช่ Full Test

## ผลก่อนและหลัง

**ตารางนี้เป็น positive literal-content checks ไม่ใช่เปอร์เซ็นต์ความถูกต้องของคำตอบทั้งระบบ** คำถามเดียวมีหลาย grades จากหลาย corpus; 27 คำถามมีเพียง 17 คำถามที่มี positive checks รวม 51 grades และ 48 คำถามมีเพียง 18 คำถามที่มี positive checks รวม 62 grades ข้อที่ไม่มี positive checks ยังตรวจคำตอบประกอบในรายงานรายข้อ

| ชุด | ก่อน R119 | R120 รอบแรก | R120 revision03 |
|---|---:|---:|---:|
| ชุดแยกไว้ 27 ข้อ | 39/51 (76.5%) | 49/51 (96.1%) | 49/51 (96.1%) |
| Development 48 ข้อ | 62/62 (100.0%) | 58/62 (93.5%) | 62/62 (100.0%) |

ทั้ง teaching และชุด 27 ข้อคัดจาก saved Legacy ที่ validation/confidence ผ่านและไม่มี positive literal fail จึงมี selection bias ไปยังกรณีที่ Legacy เคยผ่านเกณฑ์ ไม่ใช่ตัวแทนสุ่มของ Full ทั้งหมด การผ่านเกณฑ์นี้ยังไม่รับรอง semantic correctness ของครู

รอบแรกแยกครอบครัว case IDs/origin IDs ไม่ให้ข้าม teaching/evaluation/development และตรึง code ก่อนอ่านคำตอบรายข้อของ evaluation หลังพบปัญหา ได้นำ 27 ข้อนั้นมาวิเคราะห์และแก้ revision02/03 ดังนั้น **คะแนน revision03 เป็นผลพัฒนาบนคำถามที่เคยดูแล้ว ไม่ใช่ holdout ใหม่** แม้ก่อนแก้ก็อาจมี semantic near-duplicates ที่คนละ IDs; ไม่ใช้ตัวเลขนี้ทำนาย Full accuracy

### แยกภาษา — ชุดเปรียบเทียบ 27 ข้อ

| ภาษา | คำถาม | R119 | R120 revision03 |
|---|---:|---:|---:|
| th | 15 | 28/34 (82.4%) | 33/34 (97.1%) |
| en | 11 | 9/15 (60.0%) | 14/15 (93.3%) |
| auto | 1 | 2/2 (100.0%) | 2/2 (100.0%) |

### แยกภาษา — Development 48 ข้อ

| ภาษา | คำถาม | R119 | R120 revision03 |
|---|---:|---:|---:|
| th | 24 | 25/25 (100.0%) | 25/25 (100.0%) |
| en | 22 | 36/36 (100.0%) | 36/36 (100.0%) |
| auto | 2 | 1/1 (100.0%) | 1/1 (100.0%) |

## ครูสอนอะไรจริง

1. แยก requested operation จากบริบท: ถามราคา Beat Saber ให้ใช้ game→service→rate ไม่ตอบรายการเกม
2. ใช้ structured tools สำหรับคำนวณ ปุ่มเกม ตาราง และนโยบาย ไม่บังคับให้ LLM เขียนข้อเท็จจริงจากความจำ
3. เก็บชื่อเกม/รายการและเงื่อนไขทั้งประโยคก่อนอ่าน clause
4. คำถามกว้างต้องอ่าน source family/รายการครบตาม scope หรือบอก partial
5. ตอบ fact ที่ถามก่อน ลดชื่อ field ภายในและข้อความ heading ซ้ำ โดยคงเงื่อนไขและ source citations

ข้อมูลใน prompt มีเพียงคำถามกับ task plan ที่ผ่านการตรวจ ไม่มีราคา โทษ หรือข้ออนุญาตจากคำตอบ teacher teacher รันแบบอนุญาต LLM แต่หลายข้อจบใน structured fast paths จึงไม่อ้างว่าเป็นการกลั่นคำตอบโมเดล 64 ครั้ง และใช้เฉพาะ trace ที่ระบบเปิดเผย ไม่อ้างความคิดภายในของโมเดล

## ทำไมไม่คัดลอกทุกคำตอบครู

ครูยังมีกรณี route ผิดและคำถามหลายงานที่แปลงเป็น task เดียวไม่ได้ อีกทั้ง Legacy และ native มีข้อมูลคนละรุ่น เช่น หน่วยราคา/owner reaffirmation ปัจจุบัน การสอนตัวเลขเก่าจะสร้างความผิดพลาดใหม่ จึงคัดออก/แก้ mapping ตาม [TEACHER_MAPPING_REVIEW.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/TEACHER_MAPPING_REVIEW.json) และอ่าน native ปัจจุบันเมื่อจะตอบทุกครั้ง

## สาเหตุที่ยืนยันและสิ่งที่แก้

| ชั้นที่ผิด | หลักฐาน | สิ่งที่เปลี่ยน |
|---|---|---|
| Projection | temporary_suspension มีอยู่ใน native แต่ไม่ได้เป็น C10 fact | ใช้ declared topic/route category เชื่อม FAQ เข้าตัวอ่าน |
| Requested operation | Beat Saber cost ไป catalogue; multi-zone ไป detail | source-backed price frame และ set predicate ก่อนอ่านข้อมูล |
| Context | AOV อยู่ในประโยคเตรียมแข่งแต่ quote เหลือคำถาม equipment | รักษาบริบททั้ง single need และเชื่อม heading ใน event เดียว |
| Clause coverage | Rollback/Map Forfeit ถูกจัด facet ต่างกลุ่ม | อ่าน parent และ numbered siblings ตาม source_order |
| Language slots | one hour ทำให้แสดงทั้ง 30/60 นาที | แปลงหน่วยภาษาเป็น 60 นาทีโดยไม่แก้ business rate |
| Inverse lookup | role อยู่หลังคำอธิบายยาวจึงไม่ตรงทั้ง string | จับ source role suffix และยังตรวจ public scope |
| Source action | กฎรับประทานถูกใช้ตอบนำอาหารเข้า | คืนข้อความ scope limit และสถานะ partial |
| Presentation | internal policy identifiers, session_ceil, label/value ซ้ำ | ตอบ fact ก่อนพร้อม citations; calculation rules ยังอยู่ใน audit |

รายละเอียด Flow และจุดจำกัด: [FLOW_DISTILLATION_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/FLOW_DISTILLATION_TH.md); หลักฐาน source: [REGRESSION_SOURCE_EVIDENCE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/REGRESSION_SOURCE_EVIDENCE.json) และ [STUDENT_CONTRACT_CASES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/STUDENT_CONTRACT_CASES.json)

## ตัวอย่างก่อนและหลังจาก API จริง

### `546c4490` — How much does Beat Saber cost

**ก่อน:**
confirmed answer: VR Station games include Beat Saber and Horizon Call of the Mountain. [S1]

**หลัง revision03:**
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 30 minutes [S1]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB per person for 30 minutes [S2]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S3]
VR Station 1 ชั่วโมง / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — per-person price for the rate duration: 375 THB per person for 60 minutes [S5]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S6]

จากตอบรายการเกมเป็นข้อมูลค่าบริการที่ให้เล่นเกมนั้นได้ ผ่าน native game→service→rate; คำถามไม่ระบุกลุ่ม/ระยะเวลา จึงแสดงแยกอัตรา ไม่ใช่ราคาเดียว

### `00301c15` — กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว

**ก่อน:**
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**หลัง revision03:**
แบนชั่วคราว: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S1]

FAQ temporary suspension มีอยู่ใน native ก่อนเริ่ม แต่ intent/topic ไม่เข้า compiler; เพิ่ม declared topic mapping แล้ว source เดิมตอบได้

### `0d05eaf6` — How much does it cost for an adult to play VR for one hour?

**ก่อน:**
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S1]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S2]

**หลัง revision03:**
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB for 60 minutes [S1]

one hour ต้องกลายเป็น 60 นาที ไม่ควรออกทั้งอัตรา 30 และ 60 นาที; ใช้ current owner rates ไม่คัดลอกเงินเก่าของ teacher

### `104194c2` — หำลังจะลงแข่ง VALORANT อยากรู้เรื่องบทลงโทษ

**ก่อน:**
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — บทลงโทษ: เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact) [S1]

**หลัง revision03:**
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม [S1]
PSU Phuket VALORANT 2026 Tournament — 1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ [S2]
PSU Phuket VALORANT 2026 Tournament — 2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้ [S3]
PSU Phuket VALORANT 2026 Tournament — 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ [S4]
PSU Phuket VALORANT 2026 Tournament — 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น [S5]
PSU Phuket VALORANT 2026 Tournament — 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing) [S6]

facet เดิมของ Round Rollback/Map Forfeit ต่างกลุ่ม ทำให้เลือก penalty facet แล้วตก; อ่าน parent + numbered source siblings เพื่อรวม 5 types ตาม source

### `4b0fb4a4` — I am preparing for a AOV match. What is the policy for competition equipment and devices

**ก่อน:**
Please specify the tournament or rulebook edition so I can match the rule you are asking about.

**หลัง revision03:**
Blueket Games 2025 Men's Team — 5. Competition kits and equipment: 5. Competition kits and equipment
5.1. Personal mobile phones and internet access, and/or university-provided internet
5.2. Power adapters and personal charging devices
5.3. Tablets or iPads, as well as any other equipment other than a mobile phone (Mobile Phone), are not permitted for use during competition. If detected, the team will be immediately disqualified [S1]

รักษา AOV จากทั้งประโยคแล้วจับ heading competition equipment ใน RoV Blueket 2025 source; ยังคงขอบเขตรายการ/ปี ไม่ยืนยันทุกการแข่งขันปัจจุบัน

### `1806def7` — เกมไหนเล่นได้หลายโซน

**ก่อน:**
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
Gran Turismo 7 — โซนที่ยืนยันว่ามีเกมนี้: Cockpit Zone; PlayStation 5 Zone [S1]
Resident Evil 4 — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S2]
Resident Evil Village — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S3]
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S4]

**หลัง revision03:**
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
Gran Turismo 7 — โซนที่ยืนยันว่ามีเกมนี้: Cockpit Zone; PlayStation 5 Zone [S1]
Resident Evil 4 — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S2]
Resident Evil Village — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S3]
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S4]

initial student เปลี่ยน list predicate เป็น detail ทำให้ lost source set; revision02 เพิ่ม explicit multi-zone set frame จาก native relations

### `18fc2648` — Who is the PSU student in the Web & AI Developer internship role

**ก่อน:**
No confirmed source is available for the requested detail.

**หลัง revision03:**
According to the recorded source profile:
นายสุพศิน อะนะฝรั่ง — role: Cooperative education student: Web & AI Developer [S1]

initial student ส่งทั้ง directory แทนตำแหน่งที่ถาม ต้องจับ role suffix จาก source และใช้ public-scope gate ต่อไป

### `d7158a36` — Can I bring food into the studio? Please answer briefly

**ก่อน:**
The following sources confirm consumption rules inside the studio. They do not separately confirm permission to bring the item into the studio.

**Relevant information**
• Confirmed information: Permitted to consume food and beverages only in designated areas [S1]

**Relevant information**
• Confirmed information: Food and drinks are allowed only in designated areas. [S2]

English translation is machine generated and has not been reviewed by the owner.

**หลัง revision03:**
The following source confirms consumption in designated areas. It does not separately confirm permission to bring food or drinks into the studio.
Food and drinks are allowed only in designated areas. [S1]

แหล่งที่เลือกยืนยันการรับประทานในพื้นที่กำหนด ไม่ได้ยืนยันสิทธิ์นำเข้าแยกต่างหาก ต้องแสดง scope limit แม้ผ่าน literal food/designated keywords

### `42582c1e` — ขอสอบถามหน่อยครับ Nintendo Switch OLED คืออะไร

**ก่อน:**
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**หลัง revision03:**
Nintendo Switch OLED — การใช้งาน: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ
เล่น Mario Kart 8 Deluxe
เล่น Overcooked 2
เล่น Super Smash Bros Ultimate
เล่น Nintendo Switch Sports [S1]

คำถามนิยามอุปกรณ์ต้องใช้ usage/description การคืนชื่อเดิมอย่างเดียวไม่อธิบายอุปกรณ์; แยกผล cold request/model transport ออกจากการเลือก facet

## ข้อที่ยังไม่ควรเรียกว่าถูกครบ

- `eca9a681` ขอสอบถามหน่อยครับ ช่วง Maintenance จองได้ไหม: รู้ว่าเป็น bookable/maintenance แต่ยังไม่ผูก source สำหรับคำถามที่ไม่ระบุวัน ควรตอบจากกฎ maintenance เมื่อมีขอบเขตยืนยัน หรือถามวันที่
- `5d18afc2` How do you use the controller in Little Nightmares II: คำถามการใช้ controller กว้าง reader เลือกเพียงบาง bindings ไม่ควรเรียกว่ารายการปุ่มครบ ต้องตรวจ scope/การสรุปกับ source ทั้งชุด
- `8711c0d5` วันศุกร์ช่วงบ่ายปิดใช่ไหม ขอรายละเอียดแบบสั้น ๆ: คำขอให้ตอบสั้นถูกแยกเป็น factual task และตอบซ้ำสามช่วง การมี schema ถูกต้องไม่ได้รับรองว่าจำนวน needs ถูกต้อง
- `d01ecd03` ถ้าไม่มีรหัส PSU ใช้เครื่อง PS5 ได้หรือเปล่า: ไม่มี PSU ID เป็นเรื่องสิทธิ์เข้าใช้ แต่ได้จำนวนจอย PS5 ไม่ตอบคำถาม แม้ข้อมูลอุปกรณ์ที่ส่งจะเป็นจริง
- `4930d252` กติกา VALORANT ใช้สกิลนอกขอบแผนที่เพื่อหาข้อมูลได้ไหม: ถามข้ออนุญาตตามกติกา แต่ไหลไปวิธีเล่นเกม เป็น confirmed wrong requested operation ไม่ใช่ขาด keyword อย่างเดียว
- `50d3e66b` General Adult เล่น VR 30 นาที 1 ชั่วโมง เสียกี่บาท: คำถามมีทั้ง 30 นาทีและ 1 ชั่วโมง ไม่มีตัวเชื่อมที่ชัด การเลือกเพียง 60 นาทีไม่พิสูจน์ว่าครบ ควรถามว่าจะเทียบสองอัตราหรือคำนวณระยะใด
- `9c658222` Could uou please help me with this: What information do I need to book? Please answer brefly: รู้หมวด reservation แล้วแต่ยังหาเงื่อนไขข้อมูลที่ต้องกรอกไม่ได้ การสอนหมวดไม่ทดแทน procedure facet/aliases
- `0234e46d` Could you please help me with this: How many people can play PlayStation 5 #01-#02: ต้องแยกจำนวนคนเล่นพร้อมกันต่อเครื่องจาก participant range ของบริการ รอบแรกมี model transport failure; revision03 ยังตีเป็น games/players_max และเลือกไม่เจอ source แทนที่จะอ่าน equipment/service capacity จึงยังเป็นปัญหา intent/reader คนละส่วนกับ transport
- `7551e61a` ช่วยดูหน่อย กฎตอนแข่ง วาโล มีไรบ้าง ครับ: ถามกฎการแข่งขันกว้าง แต่ได้เฉพาะบทลงโทษบางข้อ ไม่ใช่ full rulebook; ตัวแก้ penalty family ไม่ครอบคลุม generic rules request นี้
- `3020765f` ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ: profile FAQ สั้นอาจให้ที่อยู่ถูกแต่ขาดอาคาร 5 ชั้น 1 ที่ baseline structured address มี ต้องจัดลำดับ source ที่ตอบ location ครบกว่า
- `9efbf2ac` Please answer from verified studio information: May I record video inside the studio: คำตอบเจ้าของเรื่อง capture ภายในเกมไม่ครอบคลุมการถ่ายวิดีโอพื้นที่จริง การไม่ยืนยันจึงไม่ใช่ความผิดเพราะ teacher ตอบได้
- `a1c90b6e` Which studio zone has The Last of Us Part I / Part II: Part II กับ Part II Remastered ต้องมีความสัมพันธ์ source ยืนยันก่อน การตอบ Part I และบอกส่วน Part II ยังไม่ทราบเป็น partial ที่รักษาขอบเขต
- `eafe23b9` ปุ่มของ New Super Mario Bros. U Deluxe มีอะไรบ้าง: source Nintendo ที่มีเป็นคำอธิบายการควบคุมกว้าง ไม่มี mapping ปุ่มละเอียดทั้งหมด จึงยังห้ามเรียกว่าปุ่มรายปุ่มครบ
- `96ef8f71` Could you please help me with this: Do you have Hades II: Hades II ยังได้ unconfirmed ต้องตรวจ source record/edition/reader เพิ่ม ไม่สรุปจาก missing_source เพียงอย่างเดียวว่าข้อมูลยังไม่ย้าย

มีบันทึกผลครบ 75 keys รวม 1 key ที่ HTTP ไม่กลับและแยกผล retry ไว้ อ่านคำตอบที่กลับและ receipt/fact IDs ได้ที่ [PER_REQUEST_COMPARISON_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/PER_REQUEST_COMPARISON_TH.md); ข้อสังเกตรายข้ออยู่ใน [SEMANTIC_REVIEW_NOTES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/SEMANTIC_REVIEW_NOTES.json) รายงานนี้ไม่แปลง “ไม่พบ defect ในการอ่านรอบนี้” เป็นคำรับรอง semantic correctness ทั้งประโยค

## Strict/protocol, content, validity และ model transport

- Strict checker เดิมผ่าน 0/81 และ 0/164 ทั้งก่อนและหลัง เพราะยังคาด legacy mode/route/protocol หลายข้อ ไม่ใช่หลักฐานว่าคำตอบทุกข้อผิดเนื้อหา ต้องแยก expected outcome/performance/evidence IDs และ content/format ต่อไป
- Positive literal checks ยังพลาดการประเมินคำตอบครบ/ตรงเจตนา เช่น food bring vs consumption และ directory ที่ยาวแต่ไม่กรองตำแหน่ง จึงตรวจคำตอบและ source ประกอบ
- Validity/scope: owner rates reaffirmed ณ 2026-10-20 ไม่ได้สร้าง effective interval ใหม่, กติกา AOV ที่อ่านเป็น Blueket 2025, ตารางให้บริการไม่ใช่ live occupancy และไม่ยืนยันอาคารเปิดทุกส่วน
- Live provider ใน workload ถูกควบคุม unavailable; ผลนั้นไม่บอกสถานะจริงของเครื่อง
- HTTP 200, validation_ok หรือ model identity verified ไม่รับรอง intent/content accuracy; model call ล้มอาจทำให้คำตอบ unavailable แม้ API ตอบสำเร็จ

| รอบ | Model events | Events transport failed | Wire attempts failed | Schema rejected events |
|---|---:|---:|---:|---:|
| baseline01 | 34 | 0 | 0/34 | 5 |
| student01 | 35 | 1 | 1/35 | 5 |
| regression01 | 53 | 0 | 0/53 | 5 |
| student02 | 35 | 1 | 1/35 | 5 |
| student03 | 34 | 0 | 0/34 | 5 |
| regression03 | 53 | 0 | 1/55 | 5 |
| transport_retry01 | 2 | 1 | 1/2 | 0 |

### HTTP timeout ที่ต้องอ่านแยกจากคะแนน

regression03 รันครบ 48 keys / 164 grades แต่ HTTP สำเร็จ 47/48 และมีคำตอบว่าง 1 ข้อ คือ `f683a42c` Animal Crossing เกิด `TimeoutError:timed out` ที่ client ใช้เวลาที่บันทึก 79.188 วินาที ค่า API timed_out เป็น 0 เพราะไม่มี response body กลับมา ไม่ได้หมายความว่าไม่มี timeout สาเหตุชั้นในยังไม่ยืนยัน จึงไม่เหมารวมว่าเป็น model transport หรือ content failure

ข้อนี้ไม่มี positive literal check จึงทำให้ 62/62 ยังผ่านได้แม้คำขอล้ม เก็บผลเดิมไว้แล้ว retry เฉพาะ key นี้หนึ่งครั้ง ใช้ candidate/frozen data เดียวกันแยก folder ไม่แทนที่คะแนนเดิม

ผล retry: HTTP 200; error=None; คำตอบจริง:

The checking service is unavailable; this detail cannot be confirmed.

แม้ retry จะได้ HTTP 200 แต่ trace ระบุ evidence selector `model_transport_failure` และ wire TimeoutError 3.781 วินาที จึงยังไม่ได้คำตอบเนื้อหาที่ยืนยันได้ ไม่ถือว่า retry แก้ข้อนี้สำเร็จ และแยกจาก live-provider fixture ที่ใช้กับคำถามสถานะสด

[transport_retry01/RESULTS.jsonl](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/transport_retry01/RESULTS.jsonl) / [transport_retry01/TEST_COMPLETE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/transport_retry01/TEST_COMPLETE.json)

ดู error types/affected request keys ใน [ANALYSIS_FINAL.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/ANALYSIS_FINAL.json) และ MODEL_TRANSPORT/MODEL_EVENTS ของแต่ละรอบ request แรกมี cold initialization ร่วมกับ deadline จึงไม่สรุปว่า latency ต่างกันเกิดจาก distillation เพียงอย่างเดียว

## ขอบเขตการทดลองและการตรวจความคงเดิม

- ต้นฉบับ 2,727 ไฟล์ตรวจ hashes ไม่เปลี่ยน รวม source และผลเดิม; native database ทุกตารางเท่ากับ R119 ก่อนแก้ รวม approvals/withdrawals ตาม source contracts และ final run freeze
- ใช้ model scb10x/typhoon2.5-qwen3-4b:latest digest b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05 ตรวจ identity ก่อน/หลัง และ response identity ใน events
- Source/code/input freeze ของทุก completed run ผ่าน ไม่แก้ log เก่า; เก็บ revision01_system/revision02_system ก่อนแก้ และตรวจ snapshots ย้อนหลังตรงกับ freeze ใน [HISTORICAL_SNAPSHOT_VERIFICATION.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/HISTORICAL_SNAPSHOT_VERIFICATION.json)
- 77 source/code contracts ก่อน initial pilot, 5 regression contracts revision02 และ 8 final contracts revision03 เป็นการตรวจโครงสร้างข้อมูล/โค้ด ไม่ใช่จำนวนคำถามถูก; ดู [STUDENT_CONTRACTS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/STUDENT_CONTRACTS.json), [REVISION02_CONTRACTS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/REVISION02_CONTRACTS.json) และ [REVISION03_CONTRACTS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/REVISION03_CONTRACTS.json)
- ตัวอย่าง teaching ครอบคลุม 9 กลุ่ม ไม่ได้ครอบคลุมทุกหมวดของระบบ ไม่มี Full Test หรือการติดตั้ง production
- คำถาม API ใช้ session แยกตาม key และ runtime conversation database แยกแต่ละรอบ ไม่ได้ประเมินบทสนทนาต่อเนื่องหลาย turn
- ผลเป็นการรวม demonstrations + parser/reader/compiler/presentation changes ยังไม่ได้ ablation ว่าตัวอย่าง prompt เพียงอย่างเดียวเพิ่มได้เท่าไร

- Candidate ยังพยายามเรียก LLM ตีความก่อนเป็นส่วนใหญ่ ไม่ได้ย้าย gated structured fast paths ของ Legacy มาครบ จึงยังมีความเสี่ยงเรื่อง transport/deadline แม้งานที่มี exact source reader จะไม่ต้องให้โมเดลสร้างคำตอบธุรกิจ

## ข้อสรุปและแนวพัฒนาต่อ

ควรใช้แนวนี้ต่อเพื่อสอน operation/slots/เครื่องมือ/ขอบเขตคำตอบ โดยให้ current source เป็นผู้ตัดสิน facts ข้อมูลครบอย่างเดียวไม่พอ ถ้า compiler ไม่ส่ง fact เข้า reader หรือ operator เลือกคนละงาน ข้อผิดพลาดยังเกิดได้

ลำดับที่ควรทำต่อ: (1) จัดการสิทธิ์ใช้บริการและกติกาที่หลุดเป็น gameplay (2) แยก style modifier กับ factual needs (3) ทำ procedure fields และ capacity semantics ให้ตรงคำถาม (4) เพิ่ม completeness contract สำหรับ broad rulebook และ broad controls (5) จัด source precedence ของที่อยู่/FAQ และประเมินบนกลุ่มคำถามเดิมที่ยังไม่เคยใช้ปรับรอบนี้ ก่อนอ้างคะแนนทั่วไป

ถ้าจะทำ parameter distillation จริงในรอบถัดไป ควรฝึกเฉพาะแผน operation/slots และการเลือกหลักฐานจากชุดที่ตรวจแล้ว รักษาราคา/สิทธิ์/กฎที่เปลี่ยนได้ไว้ใน native ไม่สอนให้จดจำเป็นคำตอบคงที่ แนวคิดการฝึกใน [Hinton et al. 2015](https://arxiv.org/abs/1503.02531) และ [Hsieh et al. 2023](https://aclanthology.org/2023.findings-acl.507/) เป็นแรงอ้างอิง แต่การทดลองนี้ไม่ได้ทำซ้ำวิธีฝึกหรืออ้างผล benchmark จากงานเหล่านั้น

## ไฟล์สำคัญ

- [PLAN_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/PLAN_TH.md)
- [FLOW_DISTILLATION_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/FLOW_DISTILLATION_TH.md)
- [TEACHER_MAPPING_REVIEW.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/TEACHER_MAPPING_REVIEW.json)
- [PER_REQUEST_COMPARISON_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/PER_REQUEST_COMPARISON_TH.md)
- [ANALYSIS_FINAL.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/ANALYSIS_FINAL.json)
- [student03/TEST_COMPLETE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/student03/TEST_COMPLETE.json)
- [regression03/TEST_COMPLETE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r120_teacher_distillation_20261022/regression03/TEST_COMPLETE.json)
