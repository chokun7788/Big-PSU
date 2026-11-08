# ไล่คำตอบจริงทีละขั้น: เหตุใดจึงตอบแบบนี้

อ่านควบคู่กับ [บัญชีปัญหา 37 ประเภท](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/03_PROBLEM_ANALYSIS_ALL_TH.md) ตัวอย่างต่อไปนี้คัดจากผลที่บันทึกไว้แล้ว ไม่ได้ส่งคำถามทดสอบใหม่ คำตอบเดิมเป็นพฤติกรรมเปรียบเทียบ ไม่ใช่ gold truth โดยอัตโนมัติ

แต่ละตัวอย่างแยก **เจตนาที่ตีความจากคำถาม → แผนที่ระบบเลือกจริง → field/source → guard → output → เกณฑ์ที่ให้ไม่ผ่าน → วิธีแก้** รายละเอียด raw ทุก field เก็บใน [CASE_EVIDENCE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/CASE_EVIDENCE.json) จึงตรวจย้อนโดย key ได้

## K01 — ชื่อเกมถูก แต่คำถามว่าเป็นเกมอะไรพิมพ์ผิด

**Request key:** `e3547941eff33374ff75551fbf0f886c8570b64d0714e4bc9746040e864268f6`

**เจตนา/สิ่งที่ต้องรักษา:** เข้าใจว่าถาม “Zelda เป็นเกมอะไร” แม้คำว่า “เกมอะไร” พิมพ์ผิด ไม่ได้ถามชื่อทางการซ้ำ

### Input และคำตอบจริง

**คำถาม**
```text
The Legend of Zelda: Breath of the Wild คือกมอะๆร
```

**คำตอบเดิม R64 ON**
```text
The Legend of Zelda: Breath of The Wild: The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ
แนวเกม: เกม Open-world Adventure
วิธีเล่นโดยสรุป: สำรวจแผนที่ เก็บอาวุธ/อาหาร แก้ shrine ต่อสู้ และเลือกเส้นทางการผจญภัยเองได้มาก
เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```

**คำตอบกลาง R88 ON**
```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ The Legend of Zelda: Breath of the Wild เช่น ชื่อเกมอย่างเป็นทางการ?
```

### เส้นทางตัดสินที่พบจริง

1. จับชื่อเกมตรงด้วย method `exact` และเลือก `game_detail_zelda_breath_of_the_wild` ถูกแล้ว
2. ส่วนที่เหลือ `คือกมอะๆร` ไม่ผ่านตัวระบุ task จึงไม่มี operation และไม่มี requested fields
3. ตัวค้นหัวข้อใน scope ไม่มี candidate ส่วนตัววางแผน LLM เสนอ field ถึง 12 ช่อง ตั้งแต่ title จนถึง source listing/zone IDs
4. JSON และ schema ผ่าน แต่ semantic guard ยังไม่ยอมรับว่ารู้เจตนาของคำผิดนี้ จึงปฏิเสธแผนด้วย `rejected_unverified_intent`
5. ทางออกจึงเป็นคำถามกลับเรื่องชื่อเกม ทั้งที่ชื่อถูกเลือกอยู่แล้ว และไม่อ่าน summary ที่มีอยู่

### เหตุและหลักฐานประกอบ

ฐานกลางมี summary, genre, how_to_play และ official_description เป็น known พร้อม evidence pointers อยู่แล้ว ดู DATA_INVENTORY.json/example_records จึงยืนยันได้ว่าเคสนี้ไม่ใช่ย้ายเนื้อหาเกมไม่มา สาเหตุประกอบกันคือ task recovery ไม่พอ + model เสนอเกินโจทย์ + guard ต้องการหลักฐานเจตนาที่ชั้นก่อนหน้ายังให้ไม่ได้

### ควรตอบ/ควรแก้อย่างไร

ควรตอบสรุปจาก summary ว่าเป็นเกมผจญภัยโลกเปิดที่สำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ได้ แล้วเสริมแนวเกมเมื่อเหมาะสม ไม่จำเป็นต้องคืนทุก field ที่โมเดลเสนอ แก้ที่การกู้ task cue และ contract ของ game overview โดยคงการป้องกันชื่อเกม/ตัวเลข/field ที่ไม่ได้ถาม

### อ่านคะแนนอย่างไร

เป็น content regression ที่มีข้อมูลรองรับ ไม่ใช่ protocol mismatch อย่างเดียว ส่วนการเปิดรับทุก field ของโมเดลจะสร้างปัญหาใหม่ จึงไม่ใช่แนวแก้ที่เหมาะสม

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route:knowledge expected:['games']`
- `status:clarification expected:answer_available`
- `missing all alternatives: ['The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ']`

แผนสุดท้ายที่เปิดให้อ่านได้:

```json
{
  "method": "exact",
  "record_ids": [
    "game_detail_zelda_breath_of_the_wild"
  ],
  "operation": null,
  "requested_fields": [],
  "unresolved_clauses": [
    "คือกมอะๆร"
  ],
  "semantic_review_needed": true,
  "semantic_plan_accepted": false
}
```

Planner audit ต่อ call (ไม่ใช่คะแนนความถูกต้องของคำตอบ):

| รอบ | Transport | Schema | Final plan | Semantic/Error |
|---|---|---|---|---|
| 1 | True | True | False | rejected_unverified_intent |

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 67; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K02 — ถาม PC แล้วตอบสั้น ๆ ว่าอุปกรณ์: state มาถึง แต่ task ยังถูกปฏิเสธ

**หลักฐาน:** SESSION_TURNS.jsonl, session SF-006 ของ R88 เป็น engine session fixture; ไม่อ้างว่าเป็นบทสนทนา HTTP ของผู้ใช้จริง

### Turn 1

**ผู้ใช้**
```text
PC มีอะไรบ้าง
```

**คำตอบที่ส่งจริง**
```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ PC Zone เช่น บริการ / แพลตฟอร์ม เช่น PC หรือ PS5 / เวลาเล่นต่อรอบ / เวลาที่กันช่องจอง?
```

### Turn 2

**ผู้ใช้**
```text
อุปกรณ์
```

**คำตอบที่ส่งจริง**
```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### สิ่งที่ trace ยืนยัน

1. Turn แรก `PC มีอะไรบ้าง` จับ PC scope ได้ และส่ง clarification พร้อม common state ที่มี zone/service IDs กลับไป
2. Turn สอง `อุปกรณ์` ไม่ได้เริ่มจากศูนย์: rejected candidate ใช้ method `typed_common_state`, platform=PC, operation=equipment และ requested fields specifications/usage
3. read contract มี equipment_model fields แล้ว และ relation_edges พบ PC/monitor/mouse/keyboard/headset/gaming chair ที่ผูกกับบริการ PC
4. แต่ `อุปกรณ์` ยังเหลือใน unresolved clauses จึงไม่ผ่าน `unresolved_query_clause` และ dispatcher เปลี่ยนเป็น safe generic clarification
5. equipment bridge รับ grammar ของรายการอุปกรณ์แบบประโยคเต็มบางรูป แต่ bare follow-up ยังไม่ถูกผูกเป็น task เดียวกันสำเร็จ

**ข้อสรุป:** เคสนี้ไม่ใช่ประวัติไม่ถูกส่งและไม่ใช่ไม่รู้จักอุปกรณ์ทั้งหมด รากปัญหาอยู่การรับ short task/context กับการตัดสิน coverage/guard หลังได้ scope แล้ว

**ควรทำแทน:** pending request ต้องระบุ task และ allowed selection slots ไว้ เมื่อผู้ใช้เลือก “อุปกรณ์” ให้ใช้ scope PC ที่ส่งจริง แล้วอ่าน related equipment ที่มีหลักฐาน ถ้าขาดเฉพาะเครื่องหรือระดับรายละเอียดค่อยถามเฉพาะส่วนนั้น ไม่ทิ้ง task กลับเป็นคำถามทั่วไป

**ข้อจำกัด:** session นี้ไม่ได้วัดการรับหลายผู้ใช้พร้อมกัน และผล 23/24 ของ suite ไม่ได้แปลว่าทุก turn มี positive fact assertion

## K03 — ถามสิทธิ์คนนอกใช้ VR กลับได้เมนูเวลาเล่น

**Request key:** `eed9942c1154f47b25b1348687772419742fe9b3824eecec167f1a1a3bb58cb5`

**เจตนา/สิ่งที่ต้องรักษา:** ถามว่าบุคคลภายนอกเข้าใช้ VR ได้หรือไม่ เป็น eligibility/policy ไม่ใช่เวลาเล่นหรือช่องจองว่าง

### Input และคำตอบจริง

**คำถาม**
```text
A question about the studio: Can an external visitor use the VR headset?
```

**คำตอบเดิม R64 ON**
```text
Yes. Public visitors can book and use a VR station. Fees depend on the service and user group. Book through the reservation system and present a national ID card at check-in.
Source: https://esports.computing.psu.ac.th/
```

**คำตอบกลาง R88 ON**
```text
The requested topic is unclear. Which part of VR Zone do you need: Service / platform / Play time per session / Booking occupancy?
```

### เส้นทางตัดสินที่พบจริง

1. พบ VR Zone และบริการ VR 30/60 นาที แต่ยังไม่มี requested fields
2. ตัวค้นหัวข้อย่อยกลับได้ candidate เรื่องสลิปผิดและเปลี่ยนเวลา ไม่ใช่ eligibility; selector เลือกว่าง จึงไม่ได้ใช้ข้อเท็จจริงจากสองหัวข้อนั้น
3. field planner รอบถัดมามี transport TimeoutError ประมาณ 8 วินาที
4. ทางออกสุดท้ายเป็นเมนู field ของ VR เช่น Service/platform/Play time/Booking occupancy

### เหตุและหลักฐานประกอบ

มีทั้ง candidate recall/task mismatch และ transport timeout ใน request เดียว จึงไม่ควรอธิบายว่าเกิดจาก timeout อย่างเดียว หรือกล่าวว่า LLM ไม่ได้ถูกเรียกเลย คำตอบเดิมกล่าวถึงสิทธิ์บุคคลภายนอก แต่ต้องตรวจ source ของ policy ปัจจุบันก่อนนำรายละเอียดบัตร/ขั้นตอนทุกข้อกลับมาใช้

### ควรตอบ/ควรแก้อย่างไร

เลือก policy การเข้าใช้ของกลุ่มบุคคลภายนอกก่อน หาก source ยืนยันให้ตอบสิทธิ์นั้นโดยตรง หากไม่มี source ให้ระบุว่าเงื่อนไขการเข้าใช้ส่วนไหนยังยืนยันไม่ได้ การขอให้เลือกเวลาเล่นไม่ช่วยตอบคำถามนี้

### อ่านคะแนนอย่างไร

ตัวตรวจบางแถวมีแต่ route/outcome ไม่มี positive content assertion แม้ผ่านแถวนั้นก็ไม่ได้ยืนยันว่าตอบ eligibility ถูก

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification']`

แผนสุดท้ายที่เปิดให้อ่านได้:

```json
{
  "method": "exact",
  "record_ids": [
    "zone_vr",
    "availability_vr_30",
    "availability_vr_60"
  ],
  "operation": null,
  "requested_fields": [],
  "unresolved_clauses": [
    "a question about the studio: can an external visitor use the headset"
  ],
  "semantic_review_needed": true,
  "semantic_plan_accepted": false
}
```

Planner audit ต่อ call (ไม่ใช่คะแนนความถูกต้องของคำตอบ):

| รอบ | Transport | Schema | Final plan | Semantic/Error |
|---|---|---|---|---|
| 1 | False | False | None | TimeoutError |

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 101; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K04 — ถามนโยบาย Maintenance แต่แผนเลือกช่องคำถาม

**Request key:** `0f863c96fa66427e13a97dfc9cee137ef81ab4fb72879dd12509054269c858de`

**เจตนา/สิ่งที่ต้องรักษา:** ถามนโยบายช่วง Maintenance วันศุกร์ ซึ่งควรได้เนื้อหานโยบายของหัวข้อนั้น

### Input และคำตอบจริง

**คำถาม**
```text
What is the studio policy for friday maintenance
```

**คำตอบเดิม R64 ON**
```text
Regular booking/service periods (not live station availability):
- Monday: open 13:00-16:00; maintenance 09:00-12:00
- Tuesday-Thursday: open 09:00-12:00, 13:00-16:00
- Friday: open 09:00-12:00; maintenance 13:00-16:00
- Weekend (Saturday-Sunday): no regular service or booking period is listed.
Special closures override this weekly schedule. A bookable period does not confirm that a station is free.
Source: https://esports.computing.psu.ac.th/reservation
```

**คำตอบกลาง R88 ON**
```text
The requested topic is unclear. Which part of Friday — maintenance do you need: question / Confirmed information / topic?
```

### เส้นทางตัดสินที่พบจริง

1. จับ FAQ `migrated_faq_rule_schedule_friday_maintenance` ด้วย bounded_fuzzy และระบุ operation=policy
2. field selection ยังว่างและข้อความทั้งประโยคอยู่ใน unresolved clauses
3. LLM เลือก field `question` แทน `answer`; schema ยอมรับว่าเป็นชื่อ field ที่มีจริง
4. semantic guard ปฏิเสธ intent ที่ยังไม่ยืนยัน จึงถามกลับให้เลือก question/Confirmed information/topic

### เหตุและหลักฐานประกอบ

เคสนี้แสดงว่า schema ถูกไม่เท่ากับเลือกสาระถูก และการรู้ชื่อ FAQ ไม่เท่ากับอ่านคำตอบ FAQ การตอบเดิมคืนทั้งสัปดาห์ซึ่งกว้างกว่าสิ่งที่ถาม ไม่ควรคัดลอกผลเดิมทั้งก้อนเป็นเป้าหมายใหม่

### ควรตอบ/ควรแก้อย่างไร

อ่าน answer ของ FAQ ที่ตรงวัน/นโยบาย หากต้องกล่าวช่วงเวลาให้ใช้ schedule ปัจจุบันที่ไม่ขัดแย้งกัน จำกัดคำตอบที่วันศุกร์ และแยก Maintenance ออกจากช่องจองหรือการเปิดให้เข้าอาคาร

### อ่านคะแนนอย่างไร

grades ในตัวอย่างนี้ส่วนใหญ่ตรวจ route/outcome; trace ระบุปัญหา field ได้ละเอียดกว่าคะแนนเพียงอย่างเดียว

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route:knowledge expected:['reservation']`
- `status:clarification expected:answer_available`
- `route:knowledge expected:['reservation', 'schedule']`

แผนสุดท้ายที่เปิดให้อ่านได้:

```json
{
  "method": "bounded_fuzzy",
  "record_ids": [
    "migrated_faq_rule_schedule_friday_maintenance"
  ],
  "operation": "policy",
  "requested_fields": [],
  "unresolved_clauses": [
    "what is the studio policy for friday maintenance"
  ],
  "semantic_review_needed": true,
  "semantic_plan_accepted": false
}
```

Planner audit ต่อ call (ไม่ใช่คะแนนความถูกต้องของคำตอบ):

| รอบ | Transport | Schema | Final plan | Semantic/Error |
|---|---|---|---|---|
| 1 | True | True | False | rejected_unverified_intent |

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 14; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K05 — คำถามผสมราคาและวิธีจองที่พิมพ์ขาด

**Request key:** `adabcf3a2ca3d695a117988e02e1a5d00467f9748ec8580c159142c2058ab6f4`

**เจตนา/สิ่งที่ต้องรักษา:** มีสองงาน: ราคาบุคคลทั่วไปเล่น Cockpit 30 นาที และวิธีจองที่พิมพ์ขาดท้าย

### Input และคำตอบจริง

**คำถาม**
```text
How much does it cost for a general visiror to play Cockpit for 30 minutes and how do I boo
```

**คำตอบเดิม R64 ON**
```text
Service prices (recorded package rates):

Cockpit — 60 minutes/package (1 person)
Requested duration: 30 minutes (0.5 hours); 1 session(s).
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 65 THB/package
• General adults: 200 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**คำตอบกลาง R88 ON**
```text
I cannot confirm an answer for the full situation you described. Please add details or split the question into separate parts.
```

### เส้นทางตัดสินที่พบจริง

1. field planner เสนอข้อมูล service/inventory หลายช่อง ซึ่งไม่ตอบราคาและวิธีจองตรง ๆ
2. semantic guard ลบ field เกินโจทย์ และรักษา strong needs `amount_minor`/`duration_minutes` ไว้ได้
3. แผนได้รับการรับแบบ `typed_partial_scope` แต่ clause `how do i boo` ยังไม่ชัด
4. outer validation/dispatcher คืนคำขอให้แยกคำถามทั้งก้อน แทนการแสดงสถานะของแต่ละงาน

### เหตุและหลักฐานประกอบ

การมี final_plan_accepted=True ไม่รับรองว่าจะมี output ที่ใช้ได้ เพราะ outer path ยัง veto ได้ ส่วนคำว่า visiror และ boo คือคนละจุดของความผิดในประโยค ราคาก็มีประเด็น validity ร่วมอยู่ด้วย คำตอบเดิมให้แพ็กเกจ 60 นาทีและเตือนตารางหมดอายุ ไม่ได้ตอบวิธีจองครบ

### ควรตอบ/ควรแก้อย่างไร

แยกสถานะต่อ need: ราคาเป็น current/historical/unknown ตาม source และวิธีจองเป็น answered/clarify เฉพาะข้อความท้ายที่ยังไม่ชัด หาก intent จองกู้ได้อย่างมั่นคงให้อ่าน procedure ปัจจุบัน ห้ามแปลง 30 นาทีเป็นราคาเฉลี่ยเอง

### อ่านคะแนนอย่างไร

ไม่ใช่ตัวอย่างที่เดิมตอบครบแต่ใหม่ไม่ครบเพียงฝ่ายเดียว ต้องตรวจ completeness ทั้งสองคำตอบ และตัวตรวจในแถวนี้ไม่มี positive text assertion

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route:knowledge expected:['equipment', 'games', 'multi_question', 'reservation']`
- `status:clarification expected:answer_available`

Planner audit ต่อ call (ไม่ใช่คะแนนความถูกต้องของคำตอบ):

| รอบ | Transport | Schema | Final plan | Semantic/Error |
|---|---|---|---|---|
| 1 | True | True | True | typed_partial_scope |

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 5; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K06 — กติกา Tekken อังกฤษ: เนื้อหากับสำนวนตัวตรวจ

**Request key:** `ed920c5962389f0a735cda26e46615e40a01037708c074b3858de0cc02e3ce19`

**เจตนา/สิ่งที่ต้องรักษา:** ถามพฤติกรรมและมารยาทผู้เล่น Tekken 8 ต้องตอบกฎเกมนี้พร้อมเงื่อนไขและโทษที่เกี่ยวข้อง

### Input และคำตอบจริง

**คำถาม**
```text
Hello, could you help? What conduct and etiquette do Tekken 8 tournament players follow?
```

**คำตอบเดิม R64 ON**
```text
(ไม่มีคำตอบที่ส่งกลับในผลที่เก็บไว้)
```

**คำตอบกลาง R88 ON**
```text
Competition rules: TEKKEN 8 — PSU Esports ปะทะมันส์ สนั่นจอ

**Etiquette in Competition**
• Rule topic: Etiquette in Competition [S1]
• Rule details: Sportsmanship
* No conduct shall be exhibited that shows lack of respect toward athletes, such as mockery, disparagement, or any unsuitable verbal or physical behavior toward others. Any violation will result in an immediate loss with no exceptions.
* Competitors must show respect to referees and other competitors. No conduct showing disrespect or lack of courtesy shall be tolerated under any circumstances. Any violation will result in an immediate loss with no exceptions. [S2]

English translation is machine generated and has not been reviewed by the owner.
```

### เส้นทางตัดสินที่พบจริง

ระบบเลือกกติกา Tekken 8 และส่งเนื้อหาเกี่ยวกับการไม่เคารพคู่แข่ง การเยาะเย้ย/ดูหมิ่น และการเคารพกรรมการ แต่ตัวตรวจคาดวลีอังกฤษอีกสำนวนหนึ่ง เช่น “Unsportsmanlike behavior, such as mocking, taunting...”

### เหตุและหลักฐานประกอบ

การไม่พบวลีที่กำหนดไม่พอจะตัดสินว่าตอบผิดเกมหรือไม่มีสาระนั้น อย่างไรก็ตามยังต้องเทียบทุก proposition และข้อยกเว้น/โทษตาม source ไม่ให้คำว่า etiquette เพียงคำเดียวทำให้ถือว่าครบทั้งคำตอบ

### ควรตอบ/ควรแก้อย่างไร

รักษา game/edition lock และสรุป conduct/etiquette จาก clause ที่ตรงจริง ตรวจทั้งความหมายของข้อห้าม ผู้บังคับใช้ และผลของการละเมิด ประเมินแบบ fact/condition coverage ควบคู่กับ literal โดยไม่แก้ oracle เพื่อรับทุกข้อความ

### อ่านคะแนนอย่างไร

เป็นกลุ่ม clause scope หรือ wording ที่ต้องตรวจตาม source; ยังไม่ประกาศว่า semantic pass สมบูรณ์หรือ English ได้รับ owner review จากตัวอย่างเดียว

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route_mismatch`
- `missing_complete_clause:Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.`
- `missing_complete_clause:Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception.`
- `first_line_off_topic`

แผนสุดท้ายที่เปิดให้อ่านได้:

```json
{
  "method": "exact",
  "record_ids": [
    "competition_competition_rules_tekken8_psu_esports"
  ],
  "operation": "rules",
  "requested_fields": [
    "text"
  ],
  "unresolved_clauses": [],
  "semantic_review_needed": false,
  "semantic_plan_accepted": false
}
```

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 6; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K07 — ถามโซนของเกม กลับได้รายการบริการ

**Request key:** `98db8777d79361985fa4635a167d2f2e0d063c5676110287b61664cc4a997d44`

**เจตนา/สิ่งที่ต้องรักษา:** ถามระดับโซนของเกม ไม่ใช่รายการแพ็กเกจหรือสถานะจองสด

### Input และคำตอบจริง

**คำถาม**
```text
Please answer from verified studio information: Which studio zone has The Legend of Zelda: Breath of the Wild
```

**คำตอบเดิม R64 ON**
```text
The Legend of Zelda: Breath of the Wild is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

**คำตอบกลาง R88 ON**
```text
Confirmed game records: The Legend of Zelda: Breath of the Wild

• Confirmed source scope: Nintendo Switch (1-2 Persons) [S1][S2][S3]

• Confirmed source scope: Nintendo Switch (1-4 Persons) [S4][S5][S6]

This confirms game offerings/installations, not live booking availability.
```

### เส้นทางตัดสินที่พบจริง

เลือก game presence และบริการ Nintendo Switch แบบ 1–2/1–4 คนถูกกลุ่มแล้ว แต่ renderer แสดงเฉพาะ confirmed source scope ของบริการ ไม่แสดงชื่อ Nintendo Switch Zone ที่โจทย์คาด

### เหตุและหลักฐานประกอบ

ไม่ได้เปลี่ยนเกมไป PS5 และยังกันความเข้าใจผิดเรื่อง live availability แต่ระดับคำตอบ service กับ zone ต่างกัน ต้องตรวจ relation หรือ source listing ก่อน map เป็นชื่อโซน ไม่สร้าง FK จากชื่อที่คล้ายกันโดยเดา

### ควรตอบ/ควรแก้อย่างไร

ตอบชื่อโซนจาก relation/source ที่ยืนยัน แล้วค่อยเสริมชื่อบริการถ้าจำเป็น แยก installed/offered ออกจาก available-now

### อ่านคะแนนอย่างไร

มีทั้ง literal label mismatch และ projection ระดับคำตอบ จึงไม่ควรจัดเป็น model translation failure เพียงอย่างเดียว

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route:knowledge expected:['games']`
- `missing all alternatives: ['Nintendo Switch Zone']`

แผนสุดท้ายที่เปิดให้อ่านได้:

```json
{
  "method": "declared_game_installation_scope",
  "record_ids": [
    "game_detail_zelda_breath_of_the_wild",
    "availability_nintendo_1_2",
    "availability_nintendo_1_4"
  ],
  "operation": "game_presence",
  "requested_fields": [],
  "unresolved_clauses": null,
  "semantic_review_needed": null,
  "semantic_plan_accepted": null
}
```

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 105; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K08 — ราคาที่หมดอายุ: ไม่ตอบตัวเลขปัจจุบันอาจเป็นการป้องกันที่ถูกต้อง

**Request key:** `f3ae278c43764dbda15c79671b61aafde8de0a50342a5abd5f1daf94becd847f`

**เจตนา/สิ่งที่ต้องรักษา:** ถามค่าบริการ VR ของ General Student แต่มีทั้ง 30 นาทีและ 3 ชั่วโมง ต้องรักษาบทบาทของแต่ละระยะเวลา

### Input และคำตอบจริง

**คำถาม**
```text
General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท
```

**คำตอบเดิม R64 ON**
```text
ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

VR — 30 นาที/แพ็กเกจ (1-5 คน)
ระยะเวลาที่ถาม 30 นาที (0.5 ชั่วโมง) คิดเป็น 1 session (แพ็กเกจ)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

**คำตอบกลาง R88 ON**
```text
**ค่าบริการ — VR Station 30 นาที / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

**ค่าบริการ — VR Station 1 ชั่วโมง / PSU Alumni and General Student**
ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้ (ช่วงมีผลที่บันทึก: 2026-02-01T00:00:00+07:00 ถึงก่อน 2026-04-01T00:00:00+07:00)

ราคาปัจจุบันยังยืนยันไม่ได้จากอัตราที่หมดอายุแล้ว
```

### เส้นทางตัดสินที่พบจริง

1. ระบุกลุ่มศิษย์เก่า/นักศึกษาทั่วไปและเลือก rates ของ VR ได้
2. เวลาอ้างอิงของ full run อยู่เดือนตุลาคม แต่ rates ที่เกี่ยวข้องระบุ valid ตั้งแต่ 1 ก.พ. ถึงก่อน 1 เม.ย. 2026
3. ระบบไม่แสดงตัวเลขเป็นราคาปัจจุบัน และอธิบายช่วงมีผลที่บันทึก
4. oracle ที่มองหาคำว่า บาท/ฟรี จึงให้ literal fail แม้การงดรับรองราคาปัจจุบันมีเหตุผล

### เหตุและหลักฐานประกอบ

คำตอบเดิมระบุชัดว่าตัวเลขเป็น recorded rates และเตือนวันหมดอายุเช่นกัน จึงห้ามเขียนว่าเดิมอ้างราคาเก่าเป็นราคาปัจจุบันโดยไม่มีคำเตือน ส่วน duration 30 นาที/3 ชั่วโมงก็ไม่ได้แปลว่า parser เดิมเลือกถูกเสมอเพียงเพราะพบคำว่าบาท

### ควรตอบ/ควรแก้อย่างไร

คง validity guard ถ้าต้องการราคาปัจจุบันให้ขอ source รุ่นใหม่หรือการยืนยันต่ออายุที่ระบุช่วงเวลาให้ชัด ถ้าผู้ใช้ถามราคาอดีตจึงตอบ recorded rate พร้อมวันที่ อย่าต่ออายุหรือคำนวณ duration ที่ยังคลุมเครือเอง

### อ่านคะแนนอย่างไร

เป็น protective behavior ปน evaluator mismatch และความเสี่ยงเรื่อง duration ไม่ควรปิด guard เพื่อเพิ่มคะแนน; VR กันเต็มชั่วโมงเป็น occupancy อีกชั้น ไม่เปลี่ยนราคาของแพ็กเกจ

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route:knowledge expected:['service_fee']`
- `missing all alternatives: ['บาท', 'บาท', 'ฟรี']`

แผนสุดท้ายที่เปิดให้อ่านได้:

```json
{
  "method": "exact",
  "record_ids": [
    "availability_vr_30",
    "availability_vr_60",
    "audience_psu_alumni_general_student"
  ],
  "operation": "price",
  "requested_fields": [
    "amount_minor"
  ],
  "unresolved_clauses": [],
  "semantic_review_needed": false,
  "semantic_plan_accepted": false
}
```

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 81; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K09 — อาหาร: หยุดที่ watchdog ก่อนมีคำตอบ

**Request key:** `b0b908e3789f04a2084a19d2b8c00c722d72f1e606a56da60dbe80fb380f15e3`

**เจตนา/สิ่งที่ต้องรักษา:** คำถามนโยบายอาหารทั่วไป ต้องได้คำตอบจาก source หรือระบุสิ่งที่ไม่ทราบ

### Input และคำตอบจริง

**คำถาม**
```text
เอาอาหารเข้าได้ไหม
```

**คำตอบเดิม R64 ON**
```text
นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

**คำตอบกลาง R88 ON**
```text
(ไม่มีคำตอบที่ส่งกลับในผลที่เก็บไว้)
```

**Exception:** `TimeoutError('request watchdog 28 seconds')`

### เส้นทางตัดสินที่พบจริง

parent harness หยุด request ด้วย `TimeoutError('request watchdog 28 seconds')` ก่อนมี result สุดท้าย เกณฑ์หลายแถวของ key เดียวจึง fail เป็น pipeline_exception ทั้งหมด

### เหตุและหลักฐานประกอบ

นี่เป็น execution failure ที่ยืนยันได้ ไม่ใช่หลักฐานว่าไม่มีนโยบายอาหารหรือเลือกคำตอบผิด เพราะไม่มี final query plan ให้ไล่ต่อ การไม่มี observed model calls ใน row นี้ก็ไม่รับรองว่า subprocess ไม่เคยเริ่ม model request

### ควรตอบ/ควรแก้อย่างไร

แยกเวลารอคิว การค้น การวางแผน และการ render ให้ชัด พร้อมบันทึก checkpoint ก่อนถูก kill ถ้าตอบ policy จาก source ได้ไม่ควรต้องรอ LLM หลายชั้น นโยบายรับประทานเฉพาะพื้นที่กำหนดห้ามขยายเป็นรายละเอียดอาหารภายนอกทุกเงื่อนไขโดยไม่มี source

### อ่านคะแนนอย่างไร

ไม่อ้างวิเคราะห์ exact hanging function สำเร็จจาก exception อย่างเดียว และไม่ถือ failed grade หลายแถวเป็นหลายคำถามที่ timeout

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `pipeline_exception`

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 70; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K10 — ปุ่มยิง: ถามเพิ่มเหมือนกัน แต่ไม่ตรงคำที่ตัวตรวจบังคับ

**Request key:** `2df6cad064b00dd2b0042ae9f8033e3b8de253cb687893a152ff4e6f607cf654`

**เจตนา/สิ่งที่ต้องรักษา:** ผู้ใช้ไม่ได้ระบุเกม จึงควรถามชื่อเกมสำหรับปุ่มยิง ไม่เดาปุ่มของเกมอื่น

### Input และคำตอบจริง

**คำถาม**
```text
ปุ่มยิงกดอะไร
```

**คำตอบเดิม R64 ON**
```text
ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`
```

**คำตอบกลาง R88 ON**
```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

### เส้นทางตัดสินที่พบจริง

เดิมขอชื่อเกมโดยตรง ส่วนกลางขอเกม/อุปกรณ์/หัวข้อเพิ่มแบบกว้าง ทั้งคู่ยังไม่ดึงปุ่มเกมอื่นมาตอบ แต่ oracle ต้องการหนึ่งในวลี ยังไม่แน่ใจ/ยังไม่พบ/ขอ/ไม่มี ซึ่งคำตอบกลางไม่ได้ใช้ตามรูปที่ตรวจ

### เหตุและหลักฐานประกอบ

การไม่มี marker ทำให้ literal fail ได้แม้หลักการถามเพิ่มมีเหตุผล ขณะเดียวกันคำขอให้เลือกอุปกรณ์หรือหัวข้อยังไม่เจาะจงเท่าเดิม จึงมี UX ที่ปรับได้จริง

### ควรตอบ/ควรแก้อย่างไร

ถามสั้น ๆ ว่า “หมายถึงปุ่มยิงของเกมไหนครับ?” และเก็บ pending task=controls/action=shoot ไว้ พอผู้ใช้ตอบแค่ชื่อเกมให้ resolve task เดิมและ platform ตาม source ถ้าจำเป็น

### อ่านคะแนนอย่างไร

แยก “ควรถามเพิ่ม” ออกจาก “ตัวตรวจบังคับถ้อยคำ” ไม่บังคับตอบปุ่มเพื่อให้ผ่าน answer_available และไม่อ้างว่า clarification ทุกข้อเป็น bug

เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):

- `route:knowledge expected:['clarification', 'games', 'no_answer']`
- `status:clarification expected:answer_available`
- `missing all alternatives: ['ยังไม่แน่ใจ', 'ยังไม่พบ', 'ขอ', 'ไม่มี']`

**ตำแหน่ง raw:** `RESULTS_0.jsonl.gz`, logical JSONL line 47; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts

## K11 — เดิมมี runtime bug จริง: ownership_blocked

Legacy ON มี execution exceptions 2,694 requests โดย 2,692 เป็น NameError ของ `ownership_blocked` และอีก 2 เป็น harness_timeout_30s จุดใช้ตัวแปรอยู่ใน `retrieve_curated` แต่ assignment ที่พบอยู่ในอีก function (`retrieve_competition_fact_cards`) จึงไม่อยู่ใน local scope เดียวกัน

เป็นหลักฐานว่าไม่ควรยก retrieval เดิมมาทั้งชุด การนำ behavior กลับมาควรแยก pure task interpreter ออกจาก facts provider และไม่ดึง bug/facts เก่ากลับมาด้วย จำนวนนี้เป็น requests ไม่ใช่ grade events

## K12 — สถานะจอง: ผลชุดนี้ไม่ได้เป็นการพิสูจน์ว่า API สดผิด

R88 ตั้ง booking=controlled_unavailable ใน corpus หลัก จึงตั้งใจไม่อ้างสถานะเครื่องสดจาก WordPress การตอบว่าไม่สามารถยืนยันสถานะใน fixture นี้ต้องแยกจาก transport จริงและ occupancy correctness

ผู้ใช้เคยตรวจสถานะจริงแล้วว่าถูกต้อง ข้อนี้คงไว้เป็นข้อมูลยืนยันจากผู้ใช้ ชุดทดสอบอัตโนมัติรอบนี้ไม่ได้ยกระดับเป็นการตรวจ live ground truth ใหม่ และไม่ได้หักล้างการยืนยันเดิม

การแยกชั้นที่ถูกต้องคือ **เชื่อม endpoint ได้ → response parse ได้ → target/timezone ถูก → ช่วงเวลาทับกันตาม policy ถูก → ตรง known-result fixture/สถานะจริง** แต่ละชั้นต้องมีหลักฐานของตัวเอง

## วิธีใช้ตัวอย่างเพื่อแก้โดยไม่ overfit

1. กำหนด task/field/condition ที่ต้องตอบจาก source ก่อนเพิ่มคำถามกลายรูป
2. แก้ component ที่ทำความหมายหาย ไม่เพิ่ม alias ของคำถามเต็มทีละบรรทัด
3. คง hard negatives เช่น คนละเกม ตัวเลขเครื่องต่างกัน นโยบายชำระเงินคนละเงื่อนไข
4. ตรวจ partial answer/unknown/conflict/expiry ให้เป็นสถานะที่ถูกต้อง ไม่บังคับทุกข้อเป็น answer_available
5. แยกผลหลังแก้จากผลเก่าที่เก็บในชุดนี้ ไม่แก้ log เดิมเพื่อให้ดูเหมือนเคยผ่าน
