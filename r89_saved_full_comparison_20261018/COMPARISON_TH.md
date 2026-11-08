# เปรียบเทียบผลที่บันทึกไว้: Format เดิม R64 กับ Format กลาง R88

ใช้เฉพาะแขน LLM ON ของทั้งสองรอบ อ่านคำตอบเดิมและผลล่าสุดเทียบโจทย์/ตัวตรวจเดียวกัน ไม่รัน pipeline หรือโมเดลใหม่ ไม่แก้ oracle ข้อมูล โค้ด หรือ logs เดิม

## ผลรวมคำถามและเกณฑ์เดียวกัน

| ตัวชี้วัด | เดิม R64 / LLM ON | ใหม่ R88 / LLM ON |
|---|---:|---:|
| ผ่านเกณฑ์เดิมทั้งหมด รวม route/mode/status | 42,601/55,811 (76.33%) | 5,033/55,811 (9.02%) |
| ผ่านเกณฑ์ข้อความที่ต้องปรากฏ (ตัวตรวจเดียวกัน) | 23,517/24,909 (94.41%) | 17,960/24,909 (72.10%) |
| ระดับคำถาม: ผ่านเกณฑ์ข้อความเชิงบวกทุกแถวที่ผูกไว้ | 8,160/8,907 (91.61%) | 5,962/8,907 (66.94%) |

เกณฑ์ strict ถูกออกแบบตาม flow เดิม จึงไม่ใช่เนื้อหาล้วน ส่วน positive literal ตรวจข้อความ/ข้อกฎตรงตามที่กำหนด ไม่ใช่ความถูกต้องเชิงความหมายทุกประโยค ข้อไม่มีเกณฑ์เชิงบวกไม่ถูกนำไปอ้างว่าตอบครบ

## คู่เกณฑ์ข้อความเดียวกัน

- ทั้งคู่ผ่าน: 17,596
- เดิมผ่าน ใหม่ไม่ผ่าน: 5,921
- ใหม่ผ่าน เดิมไม่ผ่าน: 364
- ทั้งคู่ไม่ผ่าน: 1,028

## แยกตามภาษาในคำขอ (cohort คงที่ทั้งสองฝั่ง)

| ภาษา requested | Requests | เดิมผ่าน positive literal | ใหม่ผ่าน positive literal |
|---|---:|---:|---:|
| auto | 2,475 | 1,883/2,301 (81.83%) | 1,585/2,301 (68.88%) |
| en | 10,235 | 9,087/9,466 (96.00%) | 6,701/9,466 (70.79%) |
| th | 7,844 | 12,547/13,142 (95.47%) | 9,674/13,142 (73.61%) |

auto แยกไว้ ไม่เปลี่ยนกลุ่มตามภาษาที่บอตแต่ละรุ่นตอบกลับ จึงต่างจากตาราง effective locale ในรายงานเก่า

## ข้อสรุปที่หลักฐานรองรับ

Format กลางปัจจุบันยังตามผลเดิมไม่ทันในเกณฑ์ข้อความชุดนี้ ความต่างไม่ใช่เฉพาะชื่อ route เพราะยังมีช่องว่างใน positive literal อย่างไรก็ดี ช่องว่างนี้รวมการแปลคนละถ้อยคำ การตอบ label ต่างระดับ และการไม่ยืนยันราคาที่หมดอายุ จึงไม่ใช่จำนวนข้อผิดสาระจริงทั้งหมด

ยังสรุปไม่ได้ว่า schema กลางทำให้แย่ลงด้วยตัวมันเอง: engine/router/relations/field selection/projection และวันที่/validity เปลี่ยนด้วย ต้องแก้ task coverage และตรวจ source/oracle เป็นรายกลุ่ม ไม่ปิด validity guard หรือเติมนโยบายเพื่อไล่คะแนน

คะแนน R64 content-only 96% ในรายงานเก่าใช้ตัวตรวจคนละนิยามกับ positive literal 72.10% ของ R88 จึงไม่ใช้คู่นั้นเป็นตารางเทียบตรง ตัวเลขในรายงานนี้อ่านคำตอบเก่าผ่าน R88 literal เดียวกันแล้ว

## ตัวอย่างที่ผลต่างกัน

### เดิมผ่าน / ใหม่ไม่ผ่าน

#### ปุ่มยิงกดอะไร

หมวด: game_controls; key: `2df6cad064b00dd2b0042ae9f8033e3b8de253cb687893a152ff4e6f607cf654`

**คำตอบเดิม**

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

**คำตอบใหม่**

ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing all alternatives: ['ยังไม่แน่ใจ', 'ยังไม่พบ', 'ขอ', 'ไม่มี']"
  ]
}
```

#### The Legend of Zelda: Breath of the Wild คือกมอะๆร

หมวด: game_detail; key: `e3547941eff33374ff75551fbf0f886c8570b64d0714e4bc9746040e864268f6`

**คำตอบเดิม**

The Legend of Zelda: Breath of The Wild: The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ
แนวเกม: เกม Open-world Adventure
วิธีเล่นโดยสรุป: สำรวจแผนที่ เก็บอาวุธ/อาหาร แก้ shrine ต่อสู้ และเลือกเส้นทางการผจญภัยเองได้มาก
เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

**คำตอบใหม่**

ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ The Legend of Zelda: Breath of the Wild เช่น ชื่อเกมอย่างเป็นทางการ?

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing all alternatives: ['The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ']"
  ]
}
```

#### เอาอาหารเข้าได้ไหม

หมวด: rules; key: `b0b908e3789f04a2084a19d2b8c00c722d72f1e606a56da60dbe80fb380f15e3`

**คำตอบเดิม**

นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

**คำตอบใหม่**



**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
  ]
}
```

#### General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท

หมวด: service_fee; key: `f3ae278c43764dbda15c79671b61aafde8de0a50342a5abd5f1daf94becd847f`

**คำตอบเดิม**

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

VR — 30 นาที/แพ็กเกจ (1-5 คน)
ระยะเวลาที่ถาม 30 นาที (0.5 ชั่วโมง) คิดเป็น 1 session (แพ็กเกจ)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

**คำตอบใหม่**

**ค่าบริการ — VR Station 30 นาที / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 1 ชั่วโมง / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

ราคาปัจจุบันยังยืนยันไม่ได้จากอัตราที่หมดอายุแล้ว

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ]
}
```

#### Under CS2 tournamment rules, what exception applies to social media access?

หมวด: unclassified; key: `eb0a7ba6e14542bba455e0b05664f61d676be44d6ecd0444e756eed8817954a7`

**คำตอบเดิม**

Answer: 5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

**คำตอบใหม่**

Competition rules: Counter-Strike 2 — PSU Phuket CS2 2026 Tournament

**5. No social media or communication websites other than the programs provided by the organizers shall be accessed on any competition computer.**
• Rule topic: 5. No social media or communication websites other than the programs provided by the organizers shall be accessed on any competition computer. [S1]
• Rule details: 5. No social media or communication websites other than the programs provided by the organizers shall be accessed on any competition computer. [S2]

English translation is machine generated and has not been reviewed by the owner.

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing_complete_clause:5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers."
  ]
}
```

#### Under VALORANT tournamment ruls, how many players may be in match preparation and how many regulation Tactical Timeouts are allowed with what duration?

หมวด: composite; key: `74cdfb76eb55e64fd08d7609ac14e36d667a4fd94e260568ef1495cbb5cebfb5`

**คำตอบเดิม**

Answer: Personnel: During Match Prep, no more than 6 players may be present.

Details:
• 2 requests per map during regulation (first 24 rounds), 60 seconds each.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026

**คำตอบใหม่**

Competition rules: VALORANT — PSU Phuket VALORANT 2026 Tournament

**Game pauses are divided into 3 main types for different reasons.**
• Rule topic: Game pauses are divided into 3 main types for different reasons. [S1]
• Rule details: Game pauses are divided into 3 main types for different reasons. [S2]

**1. Tactical Timeout**
• Rule topic: 1. Tactical Timeout [S3]
• Rule details: 1. Tactical Timeout
* 2 requests per map during regulation (the first 24 rounds), 60 seconds each.
* In Overtime, each team receives 1 additional request. Unused regulation requests do not carry over. [S4]

**2. Technical Pause**
• Rule topic: 2. Technical Pause [S5]
• Rule details: 2. Technical Pause
* Used when there is equipment malfunction, disconnection issues, or software problems.
* Players are prohibited from communicating with each other (either verbally or in writing) unless authorized. [S6]

**3. Player Emergency Pause (Emergency Stop)**
• Rule topic: 3. Player Emergency Pause (Emergency Stop) [S7]
• Rule details: 3. Player Emergency Pause
* 1 request per map.
* Total time must not exceed 10 minutes per match. If exceeded, that player may lose eligibility to continue and must be replaced by a substitute.
Bug rules
Bugs are unintended game errors. They are classified to determine the procedure:
* Play Through Bug: a bug with no significant effect on fairness. Players must continue and cannot request a Challenge.
* Major Bug: a bug with a major effect on gameplay or game mechanics and no immediate workaround. The team may request a Challenge for review.
* Game Breaking Bug: a bug that destroys the fairness of the round so its winner cannot be determined.
* Round Rollback:
* If a bug occurs before any damage is dealt, officials may roll back the round.
* After damage has been dealt, there is no rollback except through the Challenge procedure.
* For a Game Breaking Bug, officials will immediately roll back to the start of that round.
Exploit Adjudication [S8]

**There are three main types of pauses, each for different purposes**
• Rule topic: There are three main types of pauses, each for different purposes [S9]
• Rule details: There are three main types of pauses, each for different purposes [S10]

**1. Tactical Timeout**
• Rule topic: 1. Tactical Timeout [S11]
• Rule details: 1. Tactical Timeout
* Each team may request up to 2 timeouts per map during regulation (first 24 rounds), each lasting 60 seconds.
* During Overtime, each team receives 1 additional timeout. Timeouts from regulation do not carry over. [S12]

**2. Technical Pause**
• Rule topic: 2. Technical Pause [S13]
• Rule details: 2. Technical Pause
* Used in cases of hardware malfunction, disconnection, or software issues.
* Players may not communicate (voice or text) unless permitted by officials. [S14]

**3. Player Emergency Pause**
• Rule topic: 3. Player Emergency Pause [S15]
• Rule details: 3. Player Emergency Pause
* Each team may request 1 pause per map.
* Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute
Bug Regulations [S16]

English translation is machine generated and has not been reviewed by the owner.

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing_complete_clause:Personnel: During Match Prep, no more than 6 players may be present.",
    "missing_complete_clause:2 requests per map during regulation (first 24 rounds), 60 seconds each."
  ]
}
```

#### Before visiting, I need to know: What hours are PS5 stations available to book?

หมวด: booking_days_hours; key: `23a6cd8aeb774ef243196cb0e9bd0b2e24f6f920cf111e4f62d4540a341a5e4c`

**คำตอบเดิม**

Regular booking/service periods (not live station availability):
- Monday: open 13:00-16:00; maintenance 09:00-12:00
- Tuesday-Thursday: open 09:00-12:00, 13:00-16:00
- Friday: open 09:00-12:00; maintenance 13:00-16:00
- Weekend (Saturday-Sunday): no regular service or booking period is listed.
Special closures override this weekly schedule. A bookable period does not confirm that a station is free.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

**คำตอบใหม่**

I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing all alternatives: ['09:00', '13:00', '9:00', '1 pm']"
  ]
}
```

#### Coud you check the studio information for me? Can I smoke inside the studio

หมวด: studio_rules_penalties; key: `696174c28005a30d83ea6b75bc61391a753d9a7712b9d7bfc1e88b3aaab5236e`

**คำตอบเดิม**

Smoking and alcoholic drinks are prohibited inside the studio.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

**คำตอบใหม่**

I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [],
  "new": [
    "missing required: prohibited"
  ]
}
```

### ใหม่ผ่าน / เดิมไม่ผ่าน

#### จองแล้วไม่สามารถยกเลิกได้ใช่ไหม ขอรายละเอียดแบบสั้น ๆ

หมวด: reservation_policy; key: `4dc69c73e386a0c78ae08185b7670353a2c754dd39f4f4bc8f322b9630fea34b`

**คำตอบเดิม**



**คำตอบใหม่**

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง [S1]

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing all alternatives: ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก']"
  ],
  "new": []
}
```

#### What are the controls for Super Smash Bros. Ultimate on Nintendo Switch

หมวด: game_controls; key: `c91e481310986020be37b130bc9f784a249946c5fc5d79d00f51f4e0f7cc678a`

**คำตอบเดิม**

Super Smash Bros Ultimate controls:
- L (Left Stick): Move
- R (Right Stick): Smash Attack
- A: Attack
- B: Special
- X / Y: Jump
- ZL / ZR: Shield
- L / R: Grab
- D-Pad (Up, Down, Left, Right): Taunt
- + (Plus): Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/46

**คำตอบใหม่**

Game: Super Smash Bros Ultimate

**Super Smash Bros. Ultimate**
• Controls: L (Left Stick) | Move | Use walk, run, or crouch, as well as determine the direction of various attacks
R (Right Stick) | Smash Attack | The right analog stick is used to launch Smash Attacks in a rapid direction determined by pushing it
A | Attack | Basic attacks (Jab/Tilt/Aerial) depend on the direction of the left analog stick
B | Special | Character special moves can be changed based on the direction of the left analog stick
X / Y | Jump | Use jump; you can press it simultaneously with an attack button to perform an Aerial Attack
ZL / ZR | Shield | Raise a shield to block attacks; combine it with the left stick to dodge-roll.
L / R | Grab | Grab an opponent to throw them; this is effective against opponents who are shielding.
D-Pad (Up, Down, Left, Right) | Taunt | Display taunt poses in the direction pressed (Up Taunt, Down Taunt, Side Taunt).
+ (Plus) | Pause | Pause the game temporarily. [S1]
• Platform: Nintendo Switch [S2]
• Control information status: Secondary source; the venue control layout is not yet verified [S3]

English translation is machine generated and has not been reviewed by the owner.

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing all alternatives: ['Super Smash Bros. Ultimate', 'Nintendo Switch']"
  ],
  "new": []
}
```

#### กติกกา CS2 ใช้มาโครได้ไหม แล้วติดตั้งโปรแกรมเองได้ไหม

หมวด: composite; key: `b0b03f821fff8f80612be632facffaf4256f06f1aa8aaf68dcd73705c78f419a`

**คำตอบเดิม**

ยังไม่ได้ยืนยันว่าให้ขอลงเกมเพิ่มหรือติดตั้งเกม โปรแกรม หรือ mod เองได้หรือไม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

**คำตอบใหม่**

กติกา Counter-Strike 2 — PSU Phuket CS2 2026 Tournament

**5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง**
• หัวข้อกติกา: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง [S1]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง [S2]

**3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด**
• หัวข้อกติกา: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด [S4]

**4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้**
• หัวข้อกติกา: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ [S5]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ [S6]

**8. ตารางบทลงโทษ (Penalties)**
• หัวข้อกติกา: 8. ตารางบทลงโทษ (Penalties) [S7]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: 8. ตารางบทลงโทษ (Penalties)
การละเมิด
บทลงโทษ
การด่าทอ/ใช้ความรุนแรงทางวาจา
ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
การโกงทุกรูปแบบ
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
ดูสตรีมระหว่างแข่ง
ปรับแพ้ในแมตช์นั้น
หยุดเกมโดยไม่ได้รับอนุญาต
ปรับแพ้ในรอบนั้น
การใช้บัค
ปรับแพ้ในรอบหรือแมตช์นั้น
พฤติกรรมผิดจริยธรรม
ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
เพิกเฉยต่อคำตัดสินของเจ้าหน้าที่
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์
การพิมพ์แชทในเกมที่ไม่เหมาะสม
ปรับแพ้ในรอบหรือแมตช์นั้น
การหมิ่นศาสนา [S8]

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด",
    "missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้"
  ],
  "new": []
}
```

#### TEKKEN 8 ขอ restart ได้ไหม

หมวด: competition_rules; key: `9eaffae05a2711ade39af491da7440ab0fef989358726319e9e264bc5c1441cc`

**คำตอบเดิม**



**คำตอบใหม่**

กติกา TEKKEN 8 — PSU Esports ปะทะมันส์ สนั่นจอ

ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing all alternatives: ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']"
  ],
  "new": []
}
```

#### กติกกา VALORANT ใช้ Snap Tap หรือ SOCD ได้ไหม

หมวด: unclassified; key: `58c55ec14b93d55c0ad4d118c93d786218fdf9c76a653164c3d9d898728368f1`

**คำตอบเดิม**



**คำตอบใหม่**

กติกา VALORANT — PSU Phuket VALORANT 2026 Tournament

**ภาพรวมเอกสาร**
• หัวข้อกติกา: ภาพรวมเอกสาร [S1]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: กฎระเบียบและรูปแบบการแข่งขัน VALORANT
รายการ PSU Phuket VALORANT 2026 Tournament
Update: 17/02/2026
English below
อุปกรณ์และอุปกรณ์ต่อพ่วง
ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม
* อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)
* อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้
* เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
* ข้อห้ามสำคัญ
* ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
* ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
* ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ [S2]

**พื้นที่การแข่งขันและกฎระเบียบ**
• หัวข้อกติกา: พื้นที่การแข่งขันและกฎระเบียบ [S3]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: พื้นที่การแข่งขันและกฎระเบียบ
* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
กระบวนการแข่งขัน [S4]

**ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า**
• หัวข้อกติกา: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า [S5]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
--------------------------------------------------------------------------------------
English
Equipment and Peripherals
In LAN competitions, players must strictly comply with equipment regulations to ensure fair play.
* Allowed personal equipment
* Players may bring and use their own keyboard (wired/wireless), mouse (wired/wireless), mouse bungee, mouse pad, In-ear earphones (wired), headset (wired).
* Equipment provided by the organizer
* The organizer will provide PCs, monitors, headsets with microphones, desks, and chairs.
* Keyboard technology
* The use of Snap Tap, SOCD, or equivalent technologies is permitted, unless otherwise instructed by officials.
* Key Prohibitions
* The use of macros (configured via software or hardware) is strictly prohibited.
* Players may not install any software on the provided competition computers.
* Access to any social media or communication websites on the competition computers is strictly prohibited, except for the programs provided by the organizers. [S6]

**Competition Area and Regulations**
• หัวข้อกติกา: Competition Area and Regulations [S7]
• ข้อความกติกาเต็ม รวมเงื่อนไขท้ายข้อ: Competition Area and Regulations
* Personnel during Match Preparation
* No more than 6 players are allowed in the match preparation area.
* Electronic devices
* Mobile phones, tablets, and smartwatches are strictly prohibited in the competition area until the match has concluded.
* Documents and notes
* Players may not bring notes or documents into the competition area.
* The team captain is allowed to bring documents, which must be submitted to the referee before the match.
* Food and beverages
* Only drinking water in a sealed container and chewing gum are permitted.
Match Procedure [S8]

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing_complete_clause:เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น"
  ],
  "new": []
}
```

#### แปลคำ่า reservation เป็ยภาษาไทย ขอ 1 ย่อหน้า

หมวด: compound_context_boundary; key: `1e608d2965a45e9d55c127ece29f773e7ce99ae8f559fc3f625675e3b2b5077f`

**คำตอบเดิม**

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

**คำตอบใหม่**

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S1]

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing all alternatives: ['จอง']"
  ],
  "new": []
}
```

#### Could you please help me wit this: Where is the stidio

หมวด: members_overview_contact; key: `4246cd501977881363d19e13ef92151a707cadaaa66fbad79eb5adf7f52b77fd`

**คำตอบเดิม**

Do you mean PSU Esports Studio - Phuket? I only have its recorded studio address; please specify the venue you mean.

**คำตอบใหม่**

**PSU Esports Studio - Phuket**
• address: Building 5, 1st floor, Prince of Songkla University, Phuket Campus, 80 Moo 1 Wichit Songkhram Road, Kathu, Phuket 83120. [S1]

English translation is machine generated and has not been reviewed by the owner.

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing required: Phuket Campus"
  ],
  "new": []
}
```

#### ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: Mario Party Superstars เล่นยังไง

หมวด: game_detail; key: `3d920c78713325d5eea3b2d00f895381dbdf0ec23dc4a571c2955239e3e16adb`

**คำตอบเดิม**

Mario Party Superstars มีข้อมูลปุ่มควบคุมดังนี้:
Nintendo Switch
•    Button controls: เล่นบอร์ดและมินิเกมด้วยปุ่ม - แหล่งทางการยืนยันว่า 100 มินิเกมรองรับ button controls และเล่นได้ด้วย Joy-Con หรือ Nintendo Switch Pro Controller
•    Single Joy-Con / Joy-Con grip / Pro Controller: รูปแบบคอนโทรลเลอร์ที่รองรับ - สามารถเล่นด้วย Joy-Con เดี่ยว, Joy-Con grip, Nintendo Switch Pro Controller หรือ Nintendo Switch Lite ตามข้อมูล Play Nintendo
แหล่งข้อมูล: https://play.nintendo.com/news-tips/game-releases/mario-party-superstars-game-announcement/

**คำตอบใหม่**

ข้อมูลเกม: Mario Party Superstars

**Mario Party Superstars**
• วิธีเล่นเบื้องต้นและเป้าหมายของเกม: ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน [S1]

**เหตุที่ตัวตรวจไม่ผ่าน**

```json
{
  "old": [
    "missing all alternatives: ['ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน']"
  ],
  "new": []
}
```

## หลักฐาน

- SAME_CHECKER_COMPARISON.json: counts ทุกกลุ่มและตัวอย่างพร้อม expected/decision
- PER_REQUEST_COMPARISON.jsonl.gz: ผลทุก request key ที่เทียบ
- ต้นทางเดิม: r65_detailed_failure_analysis_20261014/evidence.sqlite (read-only)
- ต้นทางใหม่: r88_full_common_llm_20261017/full01/RESULTS_*.jsonl.gz
- ทั้งสองฝั่ง 20,554 requests / 55,811 grades; ไม่มีผลตกหล่นหรือรัน chatbot ซ้ำ
