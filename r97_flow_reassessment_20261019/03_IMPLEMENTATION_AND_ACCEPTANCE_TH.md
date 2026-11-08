# แผนลงมือและเกณฑ์ตรวจรับ Flow V2

สถานะ: แผน implementation ไม่มีการรัน chatbot tests หรือเปลี่ยน production ในรอบนี้

## 1. หลักการลงมือ

ทำเป็น vertical slice ที่ผ่านเส้นทางรับคำถาม→plan→read→verify→render→state สำหรับหมวดหนึ่งให้ครบ ไม่ทำเพียงติด task IDs ให้ทุกหมวดแล้วเรียกว่ารองรับแล้ว

ใช้ source-backed fixtures และ cases จากผลเก่า ไม่ใช้คำตอบ Legacy เป็น source authority อัตโนมัติ ไม่แก้ GT เก่าหรือ approvals ให้คะแนนผ่าน

## 2. Work packages ตาม dependency

| WP | งานและจุดโค้ด | ต้องมีมาก่อน | สิ่งที่ส่งตรวจ |
|---|---|---|---|
| W0 | freeze R95/R96, source/date/profile และ failure cases | ไม่มี | manifest + raw baseline; ไม่มีการทับ logs |
| W1 | shared RequestPlan/NeedResult และ adapters ของ task_flow, answer, composition | W0 | plan version เดียว, origin ของ slots, per-need trace |
| W2 | candidate discovery + pure Legacy interpretation | W1 | ไม่มี facts import เก่า; game/event/service IDs มาจาก common |
| W3 | broad/all + pending slots ใน followup_scope และ dispatcher | W1/W2 | “ทั้งหมด”, “PC”, “อันที่สอง”, reset topic, revision re-read |
| W4 | required/optional/any-of read graph และ relation executors | W1/W2 | field receipts, unmet dependencies, no wrong-subject joins |
| W5 | ราคา/งบ/เหมาจ่าย + schedule/closure + policy/procedure | W3/W4 | tuples/units/validity, predicates แยก และ targeted questions |
| W6 | competition/controls/multi-subject และ live mixed needs | W4/W5 | ข้อกฎพ่วงครบ, game mode/editionถูก, live shared observation |
| W7 | bounded LLM planner + language renderer | W2/W4; ทำประกอบแต่ละ slice ได้ | paraphrase paths เข้าถึง executor เดียวกัน ไม่ถูก regex gate เดิม veto ซ้ำ |
| W8 | publish/index/cache/state integration และ task readiness | W3–W7 | เพิ่ม/แก้/ถอนข้อมูลใช้ได้จริง และไม่คืน facts เก่า |
| W9 | focused/holdout/regression review | ทุก slice ที่จะเปิดใช้ | metric แยกกลุ่ม + first-result logs + regression explanations |

W7 ไม่จำเป็นต้องรอจนย้ายทุกหมวด หาก slice หนึ่งต้องใช้ semantic interpretation ให้ใช้ใน slice นั้นผ่าน validator ร่วม แต่ห้ามนับ capability หมวดอื่นว่าทำเสร็จด้วย

## 3. Migration matrix ที่ต้องกรอกตอน implementation

แต่ละ task family ต้องมีสถานะ **ยังไม่เริ่ม / interpreter พร้อม / read พร้อม / render พร้อม / lifecycle พร้อม / focused verified** แยกกัน

| Family | Kinds ที่เกี่ยวข้อง | เส้นทางที่ต้องส่งผ่านแผนร่วม |
|---|---|---|
| center/public info | center, contact, facility, person | operator/location/directory/public scope |
| offerings/inventory | zone, equipment_model, resource, service, game_service | list/specs/location/capacity/offered/installed |
| games/gameplay | game, game_mode, control_set | overview/how-to/players/controls/version |
| fees/rental/budget | audience, rate, rental_package, service | audience/duration tuples + allowed formula |
| schedule | schedule, closure | date/weekday/period/global-or-zone applicability |
| policy/procedure | policy, procedure, faq | action/actor/condition/exception/dependencies |
| competition | competition, competition_rule | game/event/edition/division/topic/clauses |
| news | news | current event/registration/source validity |
| live | live_binding, resource, service | status mapping/observed_at/freshness/provider scope |

ครอบคลุม kinds ทั้ง 24 ไม่เท่ากับทุก task ผ่าน และ task family ที่มีหลายงานต้องลง coverage ของงานย่อยด้วย

## 4. ประเด็นที่ต้องเลิกใช้หรือเปลี่ยนบทบาท

### 4.1 ก่อน RequestPlan

- greeting/scope guards ใช้ได้เมื่อไม่กลบคำถามธุรกิจที่แนบมาในประโยคเดียว
- static common/live/rental/price shortcuts ต้องคืนผลที่ผูก need IDs ไม่แอบ return ทั้งคำขอเมื่อยังมีงานอื่น
- live/rules gates ของ composition ต้องย้ายความรับผิดชอบไป task decomposition และ per-domain executor

### 4.2 หลัง RequestPlan

- ไม่ให้ reader ตีความ task ใหม่แบบเงียบ ๆ เมื่อเลือก fields ไม่ได้
- ไม่ใช้ flat requested_fields เป็นรายการ user needs โดยตรง
- ไม่เอา unknown meaningful spans ออกเพื่อให้ plan ผ่าน แต่ข้อความประกอบการพูดที่มีหลักฐานว่าไม่เปลี่ยนเจตนาไม่ควรทำให้ล้มทั้งคำตอบ
- compatibility adapter เก็บได้สำหรับ logic ที่เหมาะสม แต่ต้องรักษา plan/qualifiers/receipts เหมือน executor อื่น

## 5. Walkthrough ที่ใช้ตรวจ design

**เป็นการไล่ลำดับในเอกสาร ไม่ใช่คำตอบที่ chatbot รุ่นใหม่ให้แล้ว** ทุก expected result ผูกกับเงื่อนไขว่าข้อมูลมีจริงหรือไม่มีตาม fixture

### T01 — ราคาภายนอกทั้งหมด → PC

1. ถ้าคำถามแรกต้องการตารางทั้งหมด ให้ resolve service set + audience แล้วตอบตารางที่มีหลักฐาน ไม่ถาม PC ตั้งแต่ต้น
2. ถ้าผู้ใช้เริ่มคำถามราคากว้างและระบบจำเป็นต้องถาม service จริง เก็บ pending=service + audience เดิม
3. ผู้ใช้ตอบ PC → เปลี่ยน subject selection เป็น PC โดยคง price task
4. read current rate; หากหมดอายุให้ not_current และอย่าใส่ราคาเก่าเป็น current

### T02 — ราคาและวิธีจอง แต่ราคาปัจจุบันไม่มี

need ราคาเป็น not_current/missing_source; need ขั้นตอนจอง supported ตาม source ของ procedure ตอบสองสถานะแยก ไม่ให้ workflow ราคาไม่พร้อมทำให้ขั้นตอนจองหาย

### T03 — เกมหลุดตอนแข่ง → เลือกเกม

เก็บ topic=disconnect และ context=competition เมื่อถามเกม ผู้ใช้ตอบ ROV → ค้นการแข่งขันของ ROV และ clauses ที่เกี่ยวข้อง หากไม่มี edition ที่ระบุและหลาย edition ต่างกันให้ถามเฉพาะ edition; ห้ามตอบ VALORANT แทน

### T04 — จำนวนผู้เล่น

เกมที่มี game_mode relation ให้ตาม relation; โหมดเดียวและมี min/max พอตอบให้ตอบโดยไม่ต้องมี studio_supported หากถาม “ที่ศูนย์เล่นพร้อมกันได้ไหม” ต้องตรวจทั้ง game mode และ offered/resource constraints

### T05 — วันนี้เปิดไหม

เวลา request ไทย → วัน local → schedule + closure ที่ครอบคลุม zone → opening predicate → คำตอบสั้น หากมีเพียง bookability ให้ระบุข้อจำกัดแทนการสรุป opening

### T06 — ประโยคหลายตัวเลข

“PC 2 ชั่วโมง กับ VR 30 นาทีของบุคคลภายนอก” เก็บสอง tuples แยก ห้ามตีความ VR 2 ชั่วโมงหรือ PC 30 นาทีโดยการคูณรายการ slots กัน

### T07 — เปลี่ยน facts ระหว่างสนทนา

เลือก PC ไว้แล้ว owner แก้ราคา → request ใหม่ re-read จาก release ใหม่ รักษา service intent ได้ หาก record ถูกถอนให้แจ้งและเสนอเฉพาะตัวเลือกปัจจุบัน ไม่คืนค่าจาก history/cache

### T08 — ทุกอย่างที่ค้นเจอมีชื่อคล้ายแต่ผิด scope

คำถามกฎ CS2 ค้นเจอ VALORANT คะแนนสูง → hard subject constraint ปฏิเสธ candidate แล้วค้น CS2 path ที่อนุญาตได้หนึ่งรอบ หากยังไม่มีให้ missing_source/unsupported ที่ตรงเรื่อง ห้ามย้ายเกมเพื่อให้มีคำตอบ

### T09 — บาง need ยังคลุมเครือแต่อีก need ตอบได้

“ศูนย์อยู่ที่ไหน แล้วราคาเท่าไร” เมื่อที่อยู่มี source ชัด แต่ราคาต้องเลือก scope → อ่านและตอบที่อยู่ พร้อมถามเฉพาะตัวแปรราคาที่มีผล ไม่ให้ ambiguity ของราคาไปหยุด need ที่อยู่

## 6. Acceptance scenarios

มีทะเบียน scenario ใน `FLOW_SPEC.json` สำหรับผูกกับ fixtures และ assertions ตอน implementation แต่ละกรณีระบุ precondition และ expected invariants ไม่มีค่าราคาหรือนโยบายจริงที่แต่งขึ้น

กลุ่มที่ต้องมี:

- broad/all, semantic paraphrase, multi-turn, relation reads
- price tuples, rental distinction, validity boundaries
- rules/event edition/exception, same-task multi-subject
- mixed static/live, opening/bookability distinction
- broken relations, conflicts, known-empty/unknown
- owner new/edit/withdraw, data-only updates และ source authority
- bilingual critical slots, transport/body/schema/semantic distinction

การตรวจ spec ว่ากรณีครบ/IDs ถูก/กราฟเดินถึง terminal ไม่ใช่การทดสอบว่าระบบตอบ scenarios เหล่านี้ได้จริง

## 7. วิธีวัดการเปลี่ยน Flow จริง

ในแต่ละ request เก็บ:

- original entry path และ interpreter ที่เสนอแผน
- selected plan version + need IDs + slots ที่มี origin
- executor/read branch ของทุก need
- rejected plan พร้อมเหตุผลเฉพาะ
- receipts ของ claims และ proof ของ set/list
- final per-need status และสิ่งที่ถูกส่งจริง

เปรียบเทียบก่อน/หลังด้วย failure attribution เช่น `found_evidence_but_rejected`, `missing_relation_read`, `unnecessary_user_slot`, `wrong_subject`, `incomplete_set`, `actual_not_current`, `wording_only_or_uncertain`

ลดสัดส่วน compatibility ไม่ใช่เป้าหมายด้วยตัวเอง สิ่งที่ต้องเปลี่ยนคือคำถามที่ข้อมูลพอถูกนำไปตอบ และเงื่อนไขสำคัญไม่หาย

## 8. เกณฑ์ก่อนเสนอเปลี่ยนรุ่นใช้งาน

1. source-backed critical fixtures ไม่มี unsupported price/permission/rule/live claims
2. false abstention ลดและ all-needs fulfillment เพิ่มบน source/date/fixture เดียวกัน
3. raw old checker results ยังเก็บแยก ไม่เปลี่ยนคำจำกัดความคะแนนเพื่ออ้างชนะ Legacy
4. new/edit/withdraw และ named entities ที่ไม่มีใน legacy aliases ผ่านตาม capability ที่เปิดใช้
5. no unreviewed factual fallback และ no invented business defaults
6. regression ทุก critical case มีคำอธิบายและแผนแก้ ไม่กลบด้วยคะแนนเฉลี่ยรวม
7. เวลาและ model admission วัดจาก workload ที่กำหนดจริง ไม่อ้างจากการตรวจเอกสาร

การเปิดใช้ production หรือ full test เป็นขั้นถัดไปหลัง implementation และการตรวจรับที่เกี่ยวข้อง งานรอบนี้ยังอยู่ที่การวิเคราะห์และพัฒนา Flow

## 9. สิ่งที่ทำเองได้และสิ่งที่ยังต้องมีหลักฐาน

ทำเองได้: refactor plan adapters, typed read graph, targeted state, list completeness, imports/source assertions, index/revision consistency และชุด focused fixtures ที่อิง facts เดิม

ต้องมี source เพิ่มหากยังไม่มี: ราคาที่มีผลปัจจุบัน, วิธีตัดสินนโยบายที่ขัดกัน, ความหมาย physical opening ที่ไม่ได้ระบุในตารางจอง, และข้อมูลเกม/กติกาที่ต้นฉบับไม่กล่าวถึง

ข้อมูลที่ผู้ใช้ยืนยันไว้แล้วต้องใช้ต่อ ไม่ขอซ้ำ และไม่เติม facts ด้วยโมเดลเพื่อให้ Flow ดูสมบูรณ์
