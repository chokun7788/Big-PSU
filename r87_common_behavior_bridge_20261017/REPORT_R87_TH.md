# R87 ผลเชื่อม Flow เดิมเข้ากับข้อมูลกลาง

## สถานะส่งมอบ

ติดตั้งในแชททดสอบ R78 ที่ http://127.0.0.1:8115/ แล้ว ตรวจ API จริงหลัง restart และตรวจ loaded source fingerprint เปิด LLM และยืนยันการสร้างข้อความจากโมเดลจริงก่อนเริ่ม ข้อมูลยังเป็น migration draft 602 รายการ ไม่ได้สร้าง owner approval หรือเผยแพร่ production

## 1. ผลตรวจที่แยกตามความหมาย

| ชุด | ผ่าน | สิ่งที่พิสูจน์ |
|---|---:|---|
| ก่อนแก้ R84: คำถามเป้าหมายเดิม | 36/51 | ผลเก็บเดิม เปิด LLM ไม่รันก่อนแก้ซ้ำ |
| หลังแก้: 51 เทิร์นเดียวกัน/เกณฑ์เดิม | 51/51 | ตรวจผลเว็บรอบล่าสุดด้วยเกณฑ์ V1 ที่เก็บไว้ |
| Candidate: เกณฑ์เข้มขึ้น + เพิ่มเคสกติกา | 55/55 | โมเดลจริงเปิด; ตรวจเนื้อหา ขอบเขต และหลายเทิร์น |
| เว็บที่ติดตั้งจริง: เกณฑ์เข้มขึ้น | 55/55 | HTTP จริง ผ่าน session และ common_read_state |
| ฐานทดลองราคา/ข้อมูลใหม่ | 19/19 | เพิ่ม แก้ ถอนข้อมูล และขอบเขต tuple; ควบคุม transport |
| ฐานทดลองกติกา | 7/7 | เปลี่ยน source เพิ่มข้อใหม่ ถอนข้อ และ block legacy loader |
| Qualified replies | 41/41 | regression ที่เกี่ยวข้องกับ ownership/context; ควบคุม transport |
| Rejection/replacement | 34/34 | ปฏิเสธ เปลี่ยนคำถาม และ context; ควบคุม transport |

36→51 เป็นผลใน 51 เทิร์นเดิมตามเกณฑ์เดิม ไม่ใช่ accuracy ของผู้ใช้ทุกคน เกณฑ์กติกาเดิมอ่อนเกิน จึงมีการอ่านคำตอบและแก้ oracle เพิ่ม รายงานผล 55/55 แยกต่างหาก ไม่รวมจำนวนจากชุดซ้ำให้เป็นคะแนนใหญ่ และไม่อ้างว่า full test ผ่าน

### ภาษาและโมเดล

| ภาษา | เว็บผ่าน | มัธยฐาน HTTP (วินาที) |
|---|---:|---:|
| th | 30/30 | 0.467 |
| en | 25/25 | 0.407 |

Preflight generation จริง: True; selector calls ที่ query_plan นับ: 4; proposal calls: 3; model transport/selection failures ที่ตัวตรวจพบ: 0

เปิด LLM ไม่ได้บังคับให้ทุกคำถามเรียกโมเดล คำถามที่มี task contract ชัดอ่าน source ตรงได้ ส่วนที่กำกวมยังใช้ตัวเลือกของโมเดลพร้อมตรวจแผนและขอความชัดเจนตามเดิม ตัวเลขนี้ไม่ใช่จำนวน HTTP ทุกชนิด และเวลาชุดเล็กหลังเตรียมโมเดลไม่ใช่ load benchmark

## 2. สิ่งที่แก้และเหตุผล

### 2.1 ตีความเดิม แต่อ่านข้อเท็จจริงจากข้อมูลกลาง

legacy_intent_bridge ใช้ compiler/priority/category/pattern จาก trusted routing configuration เดิม เฉพาะกรณีครอบคลุมสาระคำถามและ map ไป intent_key ปัจจุบันได้รายการเดียว ไม่อ่าน answer ของ RuleMatcher และไม่ compile owner aliases เป็น regex เอง เมื่อเลือก task แล้วรักษาทั้ง record และ field=answer จนจบ แก้กรณีต้องจองล่วงหน้ากี่ชั่วโมงที่เคยถูกเปลี่ยนเป็น walk-in/ถาม field อีก

### 2.2 ราคาเหมาจ่ายและการถามต่อ

rental_bridge ใช้ pure _selection/_periods/_asks ของเดิม แต่โซน กลุ่ม ราคา ที่นั่ง อุปกรณ์ และหลักฐานมาจาก snapshot กลาง เก็บ request_contract เป็น tuple ต่อ clause ไม่เก็บราคาใน history จึงถาม PC/ภายนอก/เต็มวัน → ครึ่งวัน → ภายใน ได้ และคำถามผสม PC/ภายนอก/เต็มวัน + VR/ภายใน/ครึ่งวันไม่จับเงื่อนไขข้ามฝั่ง

ไม่ใช้ load_zone_rental_data/build_zone_rental_answer เป็นแหล่งคำตอบ ทดสอบแก้ราคาและโซนสมมุติ Aurora โดย block loader เก่าแล้ว ยังอ่านค่า revision ใหม่ได้ ถอนรายการแล้วไม่คืนค่าจาก history เงื่อนไข unknown รุ่น PS6, เหมา 5 ชั่วโมง, ชุดปรับเอง, รายชั่วโมง และขั้นตอนจองแบบเหมายังไม่ถูกเดาเป็นนโยบาย

### 2.3 รายการอุปกรณ์

equipment_bridge อ่านอุปกรณ์ผ่าน relations/source grouping ของโซนที่ถาม แก้ Nintendo Switch ที่เคยเลือก service root ซึ่งไม่มี resource FK ไม่สร้างความสัมพันธ์เดา OLED/TV86/Sofa และจำนวนมาจาก source ปัจจุบัน

### 2.4 ข้อมูลใหม่แทนหัวข้อที่เคยไม่มี

ก่อน specific-unconfirmed ตรวจ source-backed record ปัจจุบันที่ประกาศ intent_key/query_profile ว่าครอบคลุมคำถามหรือไม่ Fixture เพิ่มขั้นตอนแก้ยอดชำระเงิน → ยืนยันหัวข้อ → อ่าน V1 → แก้เป็น V2 → ถอนแล้วกลับเป็น unconfirmed ได้ ไม่แก้ข้อมูลศูนย์จริง และไม่ได้เอาวิธีแก้สลิปมาใช้กับการยืนยันตัวตน/ยอดเงิน

### 2.5 สรุปกติกาและข้อประท้วง

competition_bridge ใช้ pure clause/facet/detail predicates ของเดิม อ่านเฉพาะ competition_rule ปัจจุบันของ parent เล่มเดียว ไม่เรียก legacy overview/detail builders หรือ load_curated_rows สรุปเลือกข้อเต็มไม่เกิน 6 facet บอกว่าเป็นบางข้อ ไม่หั่นกลางเงื่อนไข ไม่เลือกบรรทัด “Occurrence 1: warning” ที่ขาดเหตุแห่งโทษ และแนบ dependency ถ้ามี ถ้าขอทั้งหมดจะกลับไปอ่านครบตาม source order

ข้อประท้วงเลือก proposition ที่ตรงคำถาม จึงมีครบว่า 15 นาทีหลังจบแมตช์ และกัปตันหรือโค้ชเท่านั้น โดยไม่แถมทั้งหมวดภาษา/อำนาจตัดสิน หากถามภาษาเพิ่มต้องตอบด้วย ไม่ตัดคำถามเหลือข้อประท้วงเพียงอย่างเดียว

English objection/protest เป็นถ้อยคำคนละแบบใน source กลาง จึงใช้ vocabulary สำหรับเลือก clause ร่วมกับ predicate เดิม ไม่ฝังตัวเลขหรือคำตอบลงโค้ด Fixture เปลี่ยน 15→23 เฉพาะฐานทดลอง แล้วตอบ 23 ทั้งไทย/อังกฤษได้ รวมทั้งเพิ่มข้ออุปกรณ์ใหม่และถอนข้อกติกาได้โดยไม่แก้ routing

## 3. สิ่งที่พบระหว่าง loop และการแก้ตัวทดสอบ

1. Candidate 1 49/51: PS5 ไม่ผูก source label PlayStation 5 และ equipment list เลือก root ผิด แก้คำย่อจากหมายเลขรุ่นใน label และใช้ named zone ที่มีจริง
2. Candidate 2 50/51 ตามเกณฑ์แรก แต่ oracle เลข 1 ยอมรับ [S1] จึงเปลี่ยนเป็นต้องมี “1 ชั่วโมง/1 hour” จริง เก็บผลเดิมไว้
3. Candidate 3 50/51: เลือก booking_advance_time ถูกแล้ว แต่ขั้น field/FAQ ด้านหลังเปลี่ยน task แก้การส่ง contract ให้ครบจน render; Candidate 4 51/51
4. เว็บครั้งแรก 51/51 แต่ manual source inspection พบ RoV สรุปยาว 2,729 ตัวอักษร และ CS2 ประท้วงยาว 1,417 ตัวอักษร เพราะตรวจเพียง domain/มี keyword จึงเพิ่ม oracle ความหลากหลายหัวข้อ ขอบเขต และข้อห้าม dump หัวข้ออื่น
5. competition_1 และ _2 ยังไม่รับ summary เพราะไม่ได้ใช้ derived acronym RoV; แก้ให้ใช้ derived_names เดียวกับตัวกลาง แก้ full-rules oracle ให้ตรวจ selected source IDs จริง ไม่ใช้ parent projection เป็นจำนวนข้อ
6. Fixture competition ครั้งแรกใช้ facet/source_order ผิด schema เป็น setup error; ไม่ลด validator ครั้งที่สองพบ English generic equipment ไม่ตรงศัพท์ predicate เก่า จึงใช้ singleton facet ที่ owner ระบุร่วมกับ clause predicate เพื่อรับ source ใหม่ โดยยังไม่ฝังคำตอบ
7. competition_fixture_release 7/7 และ Candidate release 55/55; ติดตั้งสองระยะ เก็บ before_stage2/CHANGESET_2.patch แล้วตรวจเว็บจริงใหม่ด้วย fingerprint ล่าสุด

## 4. ตัวอย่างผลเว็บจริง

### เหมา PC เต็มวันหน่วยงานภายนอกราคาเท่าไหร่

**เหมา PC Zone เต็มวัน หน่วยงานภายนอก**
ราคาแพ็กเกจ: 4,000.00 THB [S1]

ข้อมูลต้นฉบับยังไม่ระบุวันมีผลของราคาเหมา กรุณายืนยันกับศูนย์ก่อนใช้บริการ

### แล้วครึ่งวันล่ะ

**PC Zone หน่วยงานภายนอก half_day**
ราคาแพ็กเกจ: 2,000.00 THB [S1]

ข้อมูลต้นฉบับยังไม่ระบุวันมีผลของราคาเหมา กรุณายืนยันกับศูนย์ก่อนใช้บริการ

### ภายใน

**PC Zone หน่วยงานภายใน half_day**
ราคาแพ็กเกจ: 1,000.00 THB [S1]

ข้อมูลต้นฉบับยังไม่ระบุวันมีผลของราคาเหมา กรุณายืนยันกับศูนย์ก่อนใช้บริการ

### กติกา CS2 เรื่องการประท้วงและข้อพิพาท ว่าอย่างไร

ข้อกติกาตามประเด็นที่ถาม — PSU Phuket CS2 2026 Tournament



**ข้อพิพาท**
• 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น [S1]

### CS2 competition rules: who can submit a protest and when?

Requested rulebook clause — PSU Phuket CS2 2026 Tournament



**Disputes**
• 2. Objections must be submitted within 15 minutes after the match ends, by only the team captain or coach. [S1]

### ROV สรุปกติกาสั้นๆ

สรุปกติกาบางประเด็นจากเอกสารที่มี — Blueket Games 2025 ประเภททีมชาย



**รูปแบบการแข่งขัน**
• เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3 [S1]

**คุณสมบัติและการลงทะเบียน**
• เวลา 8.00-8.30 ลงทะเบียน [S2]

**อุปกรณ์การแข่งขัน**
• 5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที [S3]

**การหยุดเกมและเวลานอก**
• 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ [S4]

**ข้อห้ามและพฤติกรรม**
• 4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น [S5]

**บทลงโทษ**
• 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที [S6]



เป็นสรุปบางข้อ ถ้าต้องการครบทุกข้อ ให้ถามกติกาทั้งหมด หรือระบุหัวข้อที่ต้องการรายละเอียด

### Give me a brief overview of RoV competition rules

Selected rulebook clauses — Blueket Games 2025 Men's Team



**Competition format**
• 8.40-10.00 Round of 5 teams: Single Elimination BO3 [S1]

**Eligibility and registration**
• 8.00-8.30 Registration [S2]

**Competition equipment**
• 5.3. Tablets or iPads, as well as any other equipment other than a mobile phone (Mobile Phone), are not permitted for use during competition. If detected, the team will be immediately disqualified [S3]

**Pauses and timeouts**
• 4.3.1. If a competitor disconnects, temporarily pause the game. Each team may pause 5 times, no more than 1 minute each. Beyond that time, the other team may immediately press Resume and continue normally. [S4]

**Restrictions and conduct**
• 4.1.1. Character names or language that are rude or mock others are prohibited. [S5]

**Penalties**
• 6.1.2.1. Penalty: Immediate game loss and disqualification of the offending team from the competition upon detection of misconduct. [S6]



These are selected clauses. Ask for all rules or name a topic for details.

### ต้องจองล่วงหน้ากี่ชั่วโมง

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง [S1]

### Nintendo Switch Zone มีอุปกรณ์อะไรบ้าง

อุปกรณ์ตามโซนที่ถาม
• Nintendo Switch OLED — 1 Unit [S1] [S2]
• Sofa 2 seats — 2 Sets [S3] [S4]
• TV 86 นิ้ว — 1 Unit [S5] [S6]

## 5. รายการคำถามที่ตรวจผ่าน API จริง

| ภาษา | คำถาม | ผล |
|---|---|---|
| en | I attached incorrect proof of identity. How do I fix it? | ผ่าน |
| th | ส่งหลักฐานยืนยันตัวตนผิด ต้องแก้ยังไง | ผ่าน |
| en | I uploaded the wrong passport document. How do I correct it? | ผ่าน |
| th | แนบรูปบัตรนักศึกษาผิด ต้องแก้ยังไง | ผ่าน |
| en | The payment amount was incorrect. How do I fix it? | ผ่าน |
| en | The amount I paid was wrong. How can I correct it? | ผ่าน |
| th | ยอดเงินที่โอนผิด ต้องแก้ยังไง | ผ่าน |
| th | ผมชำระจำนวนเงินผิด ต้องแก้ยังไง | ผ่าน |
| en | I attached incorrect proof of payment. How do I fix it? | ผ่าน |
| en | yes | ผ่าน |
| th | แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง | ผ่าน |
| th | ใช่ | ผ่าน |
| th | ผมอัปโหลดรูปหลักฐานโอนเงินผิด ต้องแก้ยังไง | ผ่าน |
| th | ใช่ครับ | ผ่าน |
| en | I uploded the wrong payment attachement. How can I correct it? | ผ่าน |
| en | yes | ผ่าน |
| en | Can I bring my own input peripheral? | ผ่าน |
| en | keyboard | ผ่าน |
| th | ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม | ผ่าน |
| th | ใช่ แต่เป็นเมาส์ของผม | ผ่าน |
| th | เหมา PC เต็มวัน หน่วยงานภายนอกราคาเท่าไหร่ | ผ่าน |
| en | Full-day PC zone rental for an external organization price | ผ่าน |
| th | เหมา VR ครึ่งวัน หน่วยงานภายในราคาเท่าไหร่ | ผ่าน |
| en | How much is half-day PS5 zone rental for an internal organization? | ผ่าน |
| th | เหมาทุกโซนเต็มวันหน่วยงานภายนอกราคาเท่าไหร่ | ผ่าน |
| en | Full-day all zones rental for external organizations price | ผ่าน |
| th | เหมา PC เต็มวันหน่วยงานภายนอกราคาเท่าไหร่ | ผ่าน |
| th | แล้วครึ่งวันล่ะ | ผ่าน |
| th | ภายใน | ผ่าน |
| en | Full-day PC zone rental for an external organization price | ผ่าน |
| en | What about half-day? | ผ่าน |
| en | internal | ผ่าน |
| th | เหมา PC เต็มวันหน่วยงานภายนอก และ VR ครึ่งวันหน่วยงานภายในราคาเท่าไหร่ | ผ่าน |
| en | PC full-day rental for external organizations and VR half-day rental for internal units price | ผ่าน |
| th | เหมา PC ครึ่งวันหน่วยงานภายนอกราคาเท่าไหร่ | ผ่าน |
| th | มีอุปกรณ์อะไรให้บ้าง | ผ่าน |
| th | แล้วจองยังไง | ผ่าน |
| en | PC half-day rental for external organizations price | ผ่าน |
| en | What equipment is included? | ผ่าน |
| en | How do I book it? | ผ่าน |
| en | How many hours is a half-day PC zone rental for internal units? | ผ่าน |
| th | เหมา PC รายชั่วโมงเท่าไหร่ | ผ่าน |
| th | เหมา PS6 เต็มวันราคาเท่าไหร่ | ผ่าน |
| en | Rent the whole studio except VR for a full day | ผ่าน |
| th | ต้องจองล่วงหน้ากี่ชั่วโมง | ผ่าน |
| en | How far in advance must I reserve? | ผ่าน |
| th | ROV สรุปกติกาสั้นๆ | ผ่าน |
| th | กติกา CS2 เรื่องการประท้วงและข้อพิพาท ว่าอย่างไร | ผ่าน |
| en | Give me a brief overview of RoV competition rules | ผ่าน |
| en | CS2 competition rules: who can submit a protest and when? | ผ่าน |
| th | กติกา CS2 ต้องประท้วงภายในกี่นาที แล้วใช้ภาษาอะไร | ผ่าน |
| th | ขอกติกา ROV ทั้งหมดทุกข้อ | ผ่าน |
| th | Mario Party Superstars ปุ่มเล่นบอร์ดและมินิเกมด้วยปุ่มกดอะไร | ผ่าน |
| th | Animal Crossing: New Horizons คือเกมอะไร | ผ่าน |
| th | Nintendo Switch Zone มีอุปกรณ์อะไรบ้าง | ผ่าน |

## 6. ขอบเขตที่ยังต้องแยกจากผลอัตโนมัติ

- ยังไม่ใช่การรับรองทุก pattern/ทุกหมวด/ทุก paraphrase เทียบ legacy ทั้งระบบ และไม่ได้รัน full corpus, legacy corpus หรือ LLM OFF รอบใหม่
- Routing bridge รับเฉพาะ coverage ที่ตรวจได้และ unique current intent; เคสที่อยู่นอกขอบเขตยังใช้ตัวกลางหรือถามเพิ่ม ไม่บังคับให้ตอบด้วยข้อเท็จจริงเก่า
- Competition bridge รอบนี้เน้นสรุปภาพรวมและข้อประท้วงที่ระบุได้ ส่วน proposition อื่นยังใช้ common selector เดิม ไม่อ้างว่า summary follow-up “ขออีก” หลายรอบผ่านครบทุกบริบท
- ยังไม่มีข้อมูลเจ้าของเรื่องจำนวนชั่วโมงครึ่งวัน/เต็มวัน ราคาเหมารายชั่วโมง ชุดปรับเอง หลายวัน และขั้นตอน/มัดจำ/ยกเลิกแบบเหมา รวมทั้งวันมีผลของราคา ระบบแจ้ง unknown เฉพาะเรื่อง ไม่หารราคาเองหรือแปลง room seats เป็นจำนวนผู้เล่นพร้อมกัน
- การตรวจภาษาอังกฤษอัตโนมัติไม่เปลี่ยน agent_translated เป็น owner-reviewed การอนุมัติความหมาย/นโยบายยังแยกต่างหาก
- ข้อมูลกลางยังเป็น draft preview ไม่ใช่ production approval; รอบนี้ไม่ได้ rebuild โฟลเดอร์ portable ที่แจกเครื่องอื่น ต้องใส่โมดูลและ routing dependencies ที่ใช้อยู่ให้ครบเมื่อแพ็กเกจรอบถัดไป
- ไม่ตรวจ WordPress live ground truth/load หลายคนใหม่ ความถูกต้องสถานะจริงที่ผู้ใช้เคยยืนยันยังแยกจาก fixture ของรอบนี้

## 7. การรักษาไฟล์และหลักฐาน

แก้/เพิ่มโค้ด 6 ไฟล์ใน R78; ตรวจไฟล์ app/UI/routing อื่น 411 ไฟล์ไม่เปลี่ยน strict validator, compact opening และ legacy grammar/matcher source ไม่ถูกแก้

ฐานความรู้เดิม SHA256: `4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d` — ไม่แก้ราคา ข้อมูลเจ้าของ approvals หรือ releases เพื่อให้ผ่าน test โครงการ Downloads และ workbook ไม่ถูกแก้ เก็บ before/, before_stage2/, candidate/, logs และผลทุก attempt ไว้แยก

หลักฐานในโฟลเดอร์นี้:

- FLOW_R87_TH.md, BASELINE_MANIFEST.json
- INSTALLATION.json / INSTALLATION_2.json, CHANGESET.patch / CHANGESET_2.patch และ inventories ก่อนติดตั้ง
- PAIRED_COMPARISON.json: 51 เทิร์นเดียวกันจากผลที่มี ไม่รันเดิมซ้ำ
- verification/baseline_1, candidate_1..4, candidate_release
- verification/fixture_release (19/19), competition_fixture_release (7/7)
- verification/qualified_hardened และ rephrase_hardened
- ผล API ล่าสุด: C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r87_common_behavior_bridge_20261017\web_results\20261017T152207Z-eddbbc

**เทสใหญ่ยังพักไว้จนกว่าผู้ใช้สั่งใหม่**
