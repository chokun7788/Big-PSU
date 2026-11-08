# วิเคราะห์ตัวอย่างจากผลสุ่ม R93 — อ่านผลที่บันทึก ไม่ส่งคำถามซ้ำ

ตัวอย่างต่อไปนี้แยกสิ่งที่ trace ยืนยันได้ออกจากข้อที่ต้องตรวจความหมาย/ต้นฉบับเพิ่ม ไม่จัดทุก literal failure เป็นคำตอบผิดทางธุรกิจ และไม่ยกเลิกผลคะแนนเดิม

## C01 — คำเกริ่นทำให้ game task ที่มีชื่อชัดยังถูกปฏิเสธ

Request key: `3fb0c97f8a90c09d5180bc3475cdc2f3bf0d00dbfff6ce484c7412ce8dc6f999`

**คำถาม**

I am planning a visit and would like to know: What kind of game is Animal Crossing: New Horizons

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
I cannot confirm an answer for the full situation you described. Please add details or split the question into separate parts.
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

ผู้ใช้ถามแนวเกม/ภาพรวม Animal Crossing ไม่ได้ขอเปลี่ยนหัวข้อ การจับชื่อเกมได้แต่ไม่ตอบสาระเป็นช่องว่างในการตอบที่ต้องแก้ถ้า source summary/genre พร้อม

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

task_interpretation._framing รับเฉพาะ framing บางรูป ขณะที่ entity_search.query_variants มีการตัด planning-a-visit อยู่ในอีกเส้นทางหนึ่ง การ normalize ที่ใช้เฉพาะ selector ไม่ได้ช่วยทุก named-target path; คำ and ในคำเกริ่นยังชนตัวตรวจ multi-task ได้

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [
    "unresolved_clause_veto"
  ],
  "mode": "pipeline:migrated_clarification",
  "method": "bounded_llm_schema_fields",
  "record_ids": [
    "game_detail_animal_crossing"
  ],
  "fields": [
    "genre"
  ],
  "unresolved": [
    "i am planning a visit"
  ],
  "text_failures": [
    "missing all alternatives: ['Animal Crossing: New Horizons']",
    "missing all alternatives: ['Animal Crossing: New Horizons']"
  ]
}
```

**แนวแก้ต่อไป**

ทำ normalization ของ discourse ร่วมก่อน task selection โดยเก็บ spans/raw input ไม่ลบ qualifiers/negation/ตัวเลข และแยก conversational and จาก substantive task coordination

## C02 — คำถามผู้ดำเนินการศูนย์เลือกข้อมูลไม่สำเร็จ

Request key: `be1521b7d8bc5e7b10cc06a9d58202ef9b644a04998e3aad2a3836b84ca941b3`

**คำถาม**

Could you please help me with this: Who operates PSU Esports Studio? Please use verified information

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

ควรเลือก operator/FAQ ผู้ดำเนินการที่ตรงกับศูนย์จากข้อมูลกลาง การขอ verified information เป็นข้อกำหนดหลักฐาน ไม่ใช่เหตุให้ถามชื่อเกมแทน

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

ผลนี้ไม่มี usable final query plan และตอบว่า match ข้อมูลไม่ได้ ต้องไล่ named_scope และ candidate/guard ของคำถาม who/operator; ไม่สรุปว่าไม่มีข้อเท็จจริงเพียงเพราะตัวเลือกสุดท้ายว่าง

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [],
  "mode": "pipeline:migrated_clarification",
  "method": null,
  "record_ids": null,
  "fields": null,
  "unresolved": null,
  "text_failures": [
    "missing required: College of Computing",
    "missing required: College of Computing",
    "missing required: College of Computing"
  ]
}
```

**แนวแก้ต่อไป**

เพิ่ม task profile ของ center/operator/directory ที่อ่าน fields/relations จาก snapshot ร่วมกับ wrapper normalization ไม่เพิ่ม alias เต็มประโยคต่อ record

## C03 — กฎพื้นที่รับประทานกับสิทธิ์นำอาหารมาเป็นคนละขอบเขต

Request key: `9116184773c3768f551aee8d13f5a2eac5a18acf182db91e4c2b261a627400c3`

**คำถาม**

Can I bring my own food into the studio?

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
**Relevant information**
• Confirmed information: Food and drinks are allowed only in designated areas. [S1]

English translation is machine generated and has not been reviewed by the owner.
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

คำตอบที่ให้บอก designated consumption areas ส่วนตัวตรวจคาดถ้อยคำ you may bring จึงไม่ผ่าน แต่คำตอบและ oracle ต้องตรวจว่าต้นฉบับยืนยันการนำอาหารส่วนตัวเข้ามาจริงหรือไม่

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

มี source-backed answer เรื่อง food/drinks consumption แต่คำว่า own/bring เพิ่ม action/ownership ที่อาจไม่ครอบคลุม การมีหลักฐานเรื่องพื้นที่ไม่ยืนยัน permission ทุกกรณี

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [],
  "mode": "pipeline:common_answer",
  "method": "common_faq_topic",
  "record_ids": [
    "migrated_faq_rule_en_food_drink_natural"
  ],
  "fields": [
    "answer"
  ],
  "unresolved": [],
  "text_failures": [
    "missing required: you may bring"
  ]
}
```

**แนวแก้ต่อไป**

รักษา action/object/ownership ใน TaskPlan; ถ้ามี policy ตรงให้อ้าง ถ้าไม่มีให้บอกเฉพาะส่วนที่ยืนยันไม่ได้ ไม่เพิ่ม you may bring เพื่อคะแนน

## C04 — คำถามเข้าชมฟรียังเลือก unsupported-policy outcome ไม่ตรง

Request key: `36f7672ac3904e8cdadc6ace14e9ec2488545025657fbbac0b215c063c2cd461`

**คำถาม**

Can visitors enter just to look around for free?

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

ถ้าไม่มีนโยบายยืนยันค่าเข้าชม ควรบอกว่า free visit ยังยืนยันไม่ได้พร้อมช่องทางถามเจ้าหน้าที่ ไม่ควรเอาค่าเล่นหรือสิทธิ์ผู้ใช้มาอนุมาน

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

final no-match message กว้างกว่าประเด็นค่าเข้าชมฟรีที่ผู้ใช้ถาม ตัวตรวจคาด specific unconfirmed statement; เป็นทั้ง gap ด้าน task coverage และความเฉพาะเจาะจงของคำตอบ

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [],
  "mode": "pipeline:migrated_clarification",
  "method": null,
  "record_ids": null,
  "fields": null,
  "unresolved": null,
  "text_failures": [
    "missing required: does not confirm whether a visit just to look around is free"
  ]
}
```

**แนวแก้ต่อไป**

เพิ่ม need visit_only_fee ที่แยกจาก service price และไม่สร้างค่า 0 จากการไม่มี rate

## C05 — RoV restart ก่อน/หลัง First Blood: ตรวจ proposition และคำแปล

Request key: `0a92ddcf09f0c0a768db1c7814a94e8d0fab855bf2960bd9b98190c4d65cb5aa`

**คำถาม**

Under RoV tournamment rules, contrast restart requests before and after First Blood.

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
Competition rules: Arena of Valor (RoV) — Blueket Games 2025 Men's Team

**4. Competition Rules and Regulations**
• Rule topic: 4. Competition Rules and Regulations [S1]
• Rule details: 4. Competition regulations and rules
4.1. Basic rules
4.1.1. Character names or language that are rude or mock others are prohibited.
4.1.2. In the first game, the team at the top of the bracket takes the blue side. In subsequent games, the loser of the previous game chooses the side.
4.1.3. The referee announces the room number, and both teams must enter that room.
* The blue team is at the top.
* The red team is at the bottom.
4.1.4. If a side delays the start by more than 15 minutes beyond the scheduled time, it immediately loses the competition.
4.2. Competition rules
4.2.1. Every competitor must have at least 18 heroes to enter the competition 5v5 mode (formerly Tournament Mode).
4.2.2. Global Ban/Pick is used for hero bans and picks.
4.2.3. Runes and enhancements may be configured as desired.
4.2.4. All heroes may be selected during the competition.
4.2.5. Skins other than Default are prohibited.
4.2.6. Repeating a hero selection in the competition, or any other action causing a system problem, is prohibited in all cases.
4.3. Disconnect and Rematch
4.3.1. If a competitor disconnects, temporarily pause the game. Each team may pause 5 times, no more than 1 minute each. Beyond that time, the
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

ต้องครอบคลุมสองเงื่อนไขครบ ได้แก่ช่วงก่อน First Blood/ไม่เกินเวลาที่กฎกำหนด และช่วงหลัง First Blood/เกินเวลา รวมข้อยกเว้นและสิ่งที่ต้องคงเดิมก่อน restart

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

เลือก rule text ได้ แต่ complete-clause checker ระบุ missing clauses จากถ้อยคำที่คาด การไม่ตรงประโยคทั้งข้ออาจเป็น translation mismatch หรือขาด proposition จริง ต้องเทียบ source clauses/answer เต็ม ไม่สรุปว่าผิดทุกสาระจาก marker นี้อย่างเดียว

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [],
  "mode": "pipeline:common_answer",
  "method": "exact",
  "record_ids": [
    "competition_competition_rules_rov_blueket_2025_men"
  ],
  "fields": [
    "text"
  ],
  "unresolved": [],
  "text_failures": [
    "missing_complete_clause:4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game.",
    "missing_complete_clause:4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate."
  ]
}
```

**แนวแก้ต่อไป**

ทำ per-proposition coverage: condition/time/actor/permission/exception; รักษา literal result เดิม และเพิ่ม equivalence review แยก ไม่ตัดข้อยกเว้นหรือใช้เล่มคนละรายการ

## C06 — โจทย์ general LLM เดิมอยู่นอกขอบเขตบริการที่ผู้ใช้กำหนด

Request key: `4fc4b7f5244fb329778281ae4f59e5ac58daa61cdf58d9d2e278ba2077842f50`

**คำถาม**

API คืออะไร ตอบแบบเด็กปีหนึ่งเข้าใจได้

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

ผู้ใช้กำหนดให้บอตเน้นร้านเกม/ข้อมูลศูนย์ ไม่ต้องตอบความรู้ทั่วไปทุกเรื่อง คำถาม API ที่ไม่โยงบริการเป็นข้อที่ควรตรวจ scope ของ oracle ก่อนใช้เป็น production content failure

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

corpus เก็บคำถามจาก benchmark ความรู้ทั่วไปเดิมไว้ด้วย จึงคงคะแนนดิบที่ไม่ผ่าน แต่ไม่ตีความว่าระบบต้องเปิด general generation กลับมาเพื่อให้ผ่าน

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [],
  "mode": "pipeline:migrated_clarification",
  "method": null,
  "record_ids": null,
  "fields": null,
  "unresolved": null,
  "text_failures": [
    "missing all alternatives: ['API', 'เชื่อมต่อ']"
  ]
}
```

**แนวแก้ต่อไป**

แยก studio-service evaluation กับ retained legacy-general cohort ในรายงานรอบต่อไป โดยเก็บผลเดิม ไม่แก้ scope เพื่อไล่คะแนน

## C07 — การอธิบายอุปกรณ์ยังไม่ทั่วไปเท่าภาพรวมเกม

Request key: `0f48637863a8fde61bf099c53d3ae8b666b43e0f3382cf9e153f47a41c5d26f5`

**คำถาม**

จอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

ต้องหาว่าหมายถึง Sofa รายการใด แล้วอธิบาย device type/usage/specifications ที่มีหลักฐาน ส่วนคำเกริ่นพิมพ์ผิดไม่ควรเปลี่ยน subject เป็นจอโดยไม่มีหลักฐาน

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

คืน safe clarification แทนสาระที่ถาม แสดงว่าการมี equipment-list contract ยังไม่ครอบคลุม equipment-explanation; ต้องอ่าน rejected plan เพื่อยืนยันว่าเสียที่ names, task หรือ coverage ไม่เดาจากคำตอบล้วน

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [
    "semantic_unverified_intent",
    "unresolved_clause_veto"
  ],
  "mode": "pipeline:migrated_clarification",
  "method": "exact",
  "record_ids": [
    "equipment_sofa_2_seats"
  ],
  "fields": [
    "specifications",
    "usage"
  ],
  "unresolved": [
    "จอสอบถามหน่อยครับ คืออุปกรณ์อะไร"
  ],
  "text_failures": [
    "missing all alternatives: ['Sofa 2 seats']"
  ]
}
```

**แนวแก้ต่อไป**

เพิ่ม reusable explain-entity task ต่อ schema kind และตรวจ mixed-target ambiguity พร้อม recovery ที่ไม่จับคำในคำเกริ่นเป็นอุปกรณ์

## C08 — รายชื่อภาษาไทยในคำตอบอังกฤษกับเกณฑ์ English localization

Request key: `c9b51b6fa71dfb3329f066ff0cd0bbcb6c870fe5ee248477d9ad8ff62401b63b`

**คำถาม**

Who are the studio members? Could you check this for me?

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
**นายชนะชัย สิริพันธ์วราภรณ์**
• Name: นายชนะชัย สิริพันธ์วราภรณ์ [S1]
• Group: Members [S2]
• Role: Manager [S3]

**นายณัฐวัฒน์ นิธิคุณานนต์**
• Name: นายณัฐวัฒน์ นิธิคุณานนต์ [S4]
• Group: Members [S5]
• Role: Computer technical officer [S6]

**รศ.ดร.อซีส นันทอมรพงศ์**
• Name: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
• Group: Members [S8]
• Role: Dean [S9]

**รศ.ดร.พันธ์ ทองชุมนุม**
• Name: รศ.ดร.พันธ์ ทองชุมนุม [S10]
• Group: Members [S11]
• Role: Vice president [S12]

**ผศ.ดร.ณัฐพงศ์ ทองเทพ**
• Name: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S13]
• Group: Members [S14]
• Role: Assistant to the president for academic affairs [S15]

**นายพฤทธิ์ เกษตรสมบูรณ์**
• Name: นายพฤทธิ์ เกษตรสมบูรณ์ [S16]
• Group: Members [S17]
• Role: Computer technical officer [S18]

**ผศ.ดร.นิวัติ แก้วประดับ**
• Name: ผศ.ดร.นิวัติ แก้วประดับ [S19]
• Group: Members [S20]
• Role: President [S21]

English translation is machine generated and has not been reviewed by the owner.
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

รายชื่อเฉพาะอาจคงอักษรไทยได้ตามข้อมูลต้นฉบับ ขณะที่ role/team ที่เป็น prose ควรเป็นอังกฤษ ต้องแยกชื่อเฉพาะออกจากการแปลสาระไม่ครบ

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

มีรายชื่อและ roles ในคำตอบ แต่ตัวตรวจคาด marker English localization การขาด marker ไม่พิสูจน์ว่าคน/หน้าที่ผิด และไม่ควรแต่งชื่อโรมันใหม่โดยไม่มีต้นฉบับ

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [
    "english_thai_prose_flag_requires_review"
  ],
  "mode": "pipeline:common_answer",
  "method": "common_people_directory",
  "record_ids": [
    "member_17d23bd43ffdcfb0",
    "member_2035485e1198bd6d",
    "member_453ecaf47e840388",
    "member_4e005eeca4b538a1",
    "member_832e24bbcd11737e",
    "member_930bf12e4f38f6ff",
    "member_ce4590ddc09c0f4e"
  ],
  "fields": [
    "display_name",
    "team",
    "role"
  ],
  "unresolved": [],
  "text_failures": [
    "missing required: English localization"
  ]
}
```

**แนวแก้ต่อไป**

ตรวจ actual localized values และ translation status แยกจาก proper-name flags; ประเมินสาระ/ขอบเขตสาธารณะของ directory และ wording caveat คนละเงื่อนไข

## C09 — คำถามกว้างที่ตอบ clarification แล้วแต่ไม่ตรง wording oracle

Request key: `8a85ca899d99c94f28df724dce206223b5af6bd471628a6c95131d418e51eb05`

**คำถาม**

มีอะไรบ้าง

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

เมื่อไม่มีประวัติ/subject ควรถามเลือกหัวข้อของศูนย์พร้อมตัวอย่างที่เข้าใจง่าย การตอบ clarification จึงไม่ใช่ failure ด้าน facts โดยอัตโนมัติ

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

ตัวตรวจต้องการข้อความตัวอย่างเฉพาะ เช่น คำถามนี้ยังกว้างเกินไป และ มีเกมอะไรบ้าง คำตอบปัจจุบันขอชื่อเกม/อุปกรณ์/หัวข้อด้วยอีกสำนวนจึง fail literal

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [],
  "mode": "pipeline:migrated_clarification",
  "method": null,
  "record_ids": null,
  "fields": null,
  "unresolved": null,
  "text_failures": [
    "missing required: คำถามนี้ยังกว้างเกินไป",
    "missing required: มีเกมอะไรบ้าง",
    "missing required: มีอุปกรณ์อะไรบ้าง"
  ]
}
```

**แนวแก้ต่อไป**

ปรับ clarification UX ให้เสนอ task options ตามขอบเขต และตรวจ semantic outcome แยกจาก required string โดยยังเก็บ literal score เดิม

## C10 — ราคา VR: แยก validity จากกลุ่มผู้ใช้และระยะเวลา

Request key: `fb96a0a428d59004f6f4e9f7e1ff4ed65d36af199c8a8fbb31eb532113f7d42e`

**คำถาม**

นักศึกษาต่างมหาลัย เล่น VR 1 ชั่วโมง 30 นาที เสียกี่บาท

**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**

```text
**ค่าบริการ — VR Station 30 นาที / General Adult**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 30 นาที / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 30 นาที / PSU Student and Staff**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 1 ชั่วโมง / General Adult**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 1 ชั่วโมง / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 1 ชั่วโมง / PSU Student and Staff**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+
```

**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**

ถ้าราคาใน source หมดอายุ ณ reference clock ต้องไม่ยืนยันยอดปัจจุบัน แต่ยังต้องระบุให้ถูกว่ากำลังตรวจกลุ่มและระยะเวลาใด

**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**

ผลแสดงหลาย rate ที่หมดอายุก่อน 1 เม.ย. 2026 และไม่มี marker บาท/ฟรีที่ oracle ต้องการ เป็นเหตุด้าน temporal data/oracle ส่วนหนึ่ง แต่ไม่ได้รับรองว่า audience/duration bindings ถูกแล้ว ต้องตรวจแยก

**สัญญาณและแผนที่เลือกจริง**

```json
{
  "signals": [
    "not_current_needs_validity_review"
  ],
  "mode": "pipeline:common_not_current",
  "method": "exact",
  "record_ids": [
    "availability_vr_30",
    "availability_vr_60"
  ],
  "fields": [
    "amount_minor"
  ],
  "unresolved": [],
  "text_failures": [
    "missing all alternatives: ['บาท', 'บาท', 'ฟรี']"
  ]
}
```

**แนวแก้ต่อไป**

คง validity guard และขอ source ราคาปัจจุบันตามงานข้อมูล; ตรวจ typed audience/session/duration contracts ด้วย isolated current fixtures โดยไม่เอาราคาเก่ามาคูณให้ผ่าน

## ลำดับที่ควรแก้ต่อจากหลักฐานชุดนี้

1. Discourse/wrapper normalization ที่ใช้ร่วมทุก named/unnamed path โดยเก็บ protected constraints
2. ขยาย explain/overview/eligibility task contracts ไปอุปกรณ์ ศูนย์ และ policy พร้อม per-need outcomes
3. Semantic binding/guard ของ paraphrases และ qualifiers โดยไม่เปิดรับทุก JSON จาก LLM
4. Proposition coverage ของ rules และการแยก exact-clause mismatch จากการขาดเงื่อนไขจริง
5. จัด data readiness/validity/translation ตาม field ที่บล็อกงานจริง และทบทวน oracle scopes/markers อย่างโปร่งใส

รอบนี้เป็นการทดสอบและวิเคราะห์ ไม่เปลี่ยน production code/data ระหว่างวัดผล แผนแก้ข้างต้นยังไม่ใช่สิ่งที่แก้เสร็จแล้ว
