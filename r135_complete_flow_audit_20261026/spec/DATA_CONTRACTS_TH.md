# R123 — สัญญาข้อมูลระหว่าง planner, binder, executor และ verifier

สถานะ: **ข้อกำหนดออกแบบ ยังไม่ใช่ schema ที่ runtime ใช้งานแล้ว**  
อ่านคู่กับ [Flow หลัก](FLOW_MAIN_TH.md)

## 1. หลักการร่วม

1. แยกข้อเสนอของโมเดลออกจากข้อมูลที่ resolve/verify แล้ว
2. เก็บ raw question และ snapshot เดิมตลอด request
3. ชื่อ entity ที่ฝึกในป้ายสอนเป็นข้อความจากคำถาม; IDs จริง resolve จาก index ปัจจุบัน
4. ทุก slot มี source และ scope ไม่คัดลอกทุก slot ไปทุก task
5. ทุกคำตอบมี obligation และ receipts ที่โยงกลับ source ได้
6. ทุก failure มีรหัสสาเหตุ ไม่ใช้ unavailable หรือ partial ตัวเดียวแทนทุกปัญหา

## 2. RequestContext

| Field | ความหมายและข้อกำหนด |
|---|---|
| request_id | identity ของคำขอ |
| raw_question | ข้อความผู้ใช้เดิม ไม่เขียนทับ |
| normalized_question | ข้อความที่ normalize เพื่อประมวลผล |
| span_map | แปลง offsets ระหว่าง normalized/raw; อ้าง raw text ย้อนกลับได้ |
| locale | requested/effective locale แยกกัน |
| reference_time | timestamp ที่ pin พร้อม timezone Asia/Bangkok |
| snapshot | release/epoch/source revisions ที่ใช้ทั้งคำขอ |
| trusted_context | คำระบุของผู้ใช้ก่อนหน้าและ refs ที่อนุญาต พร้อม session/turn IDs |
| budget | เวลา/model-call budget พร้อม events; ไม่เป็น business fact |
| model_profile | requested/resolved model, adapter, digest และ backend identity |

คำว่า today/ตอนนี้ resolve จาก reference_time พร้อมบอกที่มา หากเปลี่ยน snapshot ระหว่าง request ต้องมีนโยบาย retry/แจ้งผลที่ชัดเจน ห้ามรวม claims จากคนละ snapshot เงียบ ๆ

## 3. PlannerProposal

planner ส่งเฉพาะส่วนที่ตรวจจากภาษาได้:

- `focus`: ภาพรวม ไม่ใช่ตัวตัดสิน executor เพียงตัวเดียว
- `spans`: ข้อความหรือ offsets ของ task/entity/slot ใน raw question
- `tasks`: งานจริงที่ผู้ใช้ต้องการ ไม่รวมคำขอให้ตอบสั้นเป็นอีก factual task
- `entities`: mentions และชนิดที่เสนอ ยังไม่ใช่ source facts
- `slots`: role/value proposal พร้อม source span และ scope
- `context_edges`: shared target/slot หรือ override ที่เสนอ
- `ambiguities`: สิ่งที่ยังตีความต่างกันได้และผลที่ต่างต่อคำตอบ

ไม่รับ business values ที่โมเดลจำมาสร้างเอง ไม่รับ source ID ที่ไม่มีใน snapshot ไม่ใช้ self-reported confidence เป็นเกณฑ์ผ่าน และไม่ให้โมเดลส่ง SQL/โค้ดที่ backend นำไปรันทันที

## 4. Task และ vocabulary ของ operation

| กลุ่ม | ตัวอย่าง operation ที่ต้องมีสัญญาแยก |
|---|---|
| Detail | field_lookup, relation_lookup, action_lookup |
| Set | list, count, group_list, group_count |
| Financial | unit_rate, calculate_total, compare_rates, compare_durations |
| Procedure/policy | procedure_lookup, permission_lookup, condition_lookup |
| Calendar | weekday_timetable, dated_service_state, weekly_timetable, maintenance_lookup |
| Live | resource_availability |
| Competition | rule_clause_lookup, rule_dependency_lookup |
| Unresolved | clarification_required, unsupported |

นี่เป็น vocabulary ที่ต้องตกลงและ version ก่อน implement ไม่ให้แต่ละ module ตั้งชื่อ operator ที่หมายถึงคนละอย่าง ค่าเดิม เช่น `compare` ของ R122 ต้องผ่าน adapter ไป operation ใหม่ที่ executor รองรับจริง

Task มีอย่างน้อย:

- task_id และ source span refs
- proposed domain และ operation
- requested field/relation
- target mention refs และ bound entity refs หลัง resolve
- local slot refs / shared binding refs แยกกัน
- answer obligations
- semantic dependencies และ execution dependencies แยกกัน
- ambiguities/missing slots
- capability selection และเหตุผลหลัง compiler ตรวจแล้ว

## 5. Slot: มีทั้งบทบาทและเจ้าของ

| Slot/role | จุดที่ต้องตรวจ |
|---|---|
| service/platform/resource | PC platform ไม่เท่ากับ PC เครื่องเฉพาะ และเครื่องหมายเลขไม่ใช่จำนวนคน |
| audience | positive/negative mentions; ไม่เป็นนักศึกษา PSU ไม่แปลว่าเป็น General Adult อัตโนมัติ |
| persons | จำนวนคนรวม/ต่อกลุ่ม/ต่อ audience ต้องแยก |
| duration | requested total, session length, comparison option ต้องแยก |
| sessions | จำนวนรอบไม่เท่ากับจำนวนเครื่อง |
| date/time | requested date/time/range, reference_time และ timezone มีที่มา |
| event | game, tournament, edition/year แยกชัด |
| condition/exception | เงื่อนไขใช้กับ action/task ใด มี scope |
| negation | ปฏิเสธ entity, action หรือ topic ใด ไม่กระจายทั้งประโยคแบบเหมารวม |
| requested set/subset | all/8 buttons/multiple zones ใช้กับชุดอะไรและหน่วยนับอะไร |

Slot provenance มี `origin=current_user|trusted_history`, span/turn refs, raw value, normalized value/unit และวิธี normalize หากเกิด ambiguity ให้เก็บ candidate interpretations แทนการเลือกค่าหนึ่งแบบไม่มีหลักฐาน

## 6. SharedBinding

SharedBinding เป็น edge ที่บอกว่า task ใดใช้ entity/slot ร่วมกัน พร้อม:

- binding ID
- source task/span หรือ trusted turn
- target task IDs
- entity/slot ที่ส่งต่อ
- basis: explicit_anaphor / shared_prefix / source_related_ellipsis
- supporting entity/relation refs
- override exclusions
- validation outcome และ ambiguity ที่เหลือ

ตัวอย่างการตัดสิน:

| สถานการณ์ | ผล |
|---|---|
| ราคา Cockpit แล้วถามเกม ไม่มีชื่อใหม่ มี service→game relation | ส่งชื่อบริการไป task เกม พร้อม shared edge |
| ปุ่ม Tekken แล้วถามราคา PC | เก็บคนละ target; ห้ามส่ง PC เข้า task ปุ่ม |
| prefix กลุ่มผู้ใช้ใช้กับสองราคา และงานหลังเปลี่ยนเป็นอีกกลุ่ม | ส่งกลุ่มเดิมเฉพาะงานที่ไม่ถูก override |
| “มัน” มีสอง antecedents ที่เป็นไปได้ | missing_input เฉพาะงานที่ได้รับผล |
| “ตอบเฉพาะประเด็นนั้น” | style constraint ไม่ใช่ shared entity |

## 7. ตัวอย่างแผนเชิงโครงสร้างจากคำถาม VR เดิม

JSON นี้แสดง payload เป้าหมาย ไม่ใช่ผลโมเดลจริง และ IDs เช่น e_vr เป็น request-local refs การ implement ต้องเติม offsets จากข้อความจริงและ resolve native IDs จาก snapshot

```json
{
  "contract_version": "r123-design-v1",
  "raw_question": "How is VR for 30 minutes different from VR for 1 hour, and how do I book it?",
  "entities": [
    {"id": "e_vr", "mention": "VR", "source": "current_user", "occurrence_index": 0}
  ],
  "slots": [
    {"id": "d30", "role": "comparison_duration", "quote": "30 minutes", "value": 30, "unit": "minute", "scope": ["t1:o30"]},
    {"id": "d60", "role": "comparison_duration", "quote": "1 hour", "value": 60, "unit": "minute", "scope": ["t1:o60"]}
  ],
  "tasks": [
    {
      "id": "t1",
      "source_quote": "How is VR for 30 minutes different from VR for 1 hour",
      "domain": "service_fee",
      "operation": "compare_durations",
      "target_ref": "e_vr",
      "options": [{"id": "o30", "slot_ref": "d30"}, {"id": "o60", "slot_ref": "d60"}],
      "obligations": ["resolve_o30", "resolve_o60", "keep_audiences_and_units_aligned", "do_not_sum_alternatives"]
    },
    {
      "id": "t2",
      "source_quote": "how do I book it",
      "domain": "reservation",
      "operation": "procedure_lookup",
      "target_ref": "e_vr",
      "shared_binding_ref": "b1",
      "local_slot_refs": [],
      "obligations": ["deliver_supported_booking_steps_or_explicit_gap"]
    }
  ],
  "shared_bindings": [
    {"id": "b1", "from_entity": "e_vr", "to_task": "t2", "basis": "explicit_anaphor", "quote": "it", "inherit_slot_refs": []}
  ]
}
```

ในตัวอย่างนี้ t2 ขึ้นต่อการ resolve e_vr แต่ไม่ขึ้นต่อผลราคาใน t1 เมื่อราคาไม่มีหรือ compare ล้ม งานจองยังอ่านต่อได้ ไม่มีการเพิ่มราคา/ขั้นตอนจองไว้ใน label นี้

## 8. Capability และ ExecutorResult

Capability registry ต้องประกาศ operation/field/slot combinations ที่รองรับ input requirements, allowed source kinds, completeness rules, external dependency, และ cost class เช่น local read หรือ live provider

ExecutorResult ต้องส่ง:

| Field | ความหมาย |
|---|---|
| task_id / operation | ตรงกับ compiled task ห้ามเปลี่ยนเองเงียบ ๆ |
| status / reason_codes | terminal state ที่ตรงสาเหตุ |
| claims | ข้อเท็จจริงหรือผลคำนวณที่มี receipts |
| resolved_obligations | รายการที่ส่งคำตอบแล้วพร้อม proof |
| unresolved_obligations | รายการที่ขาดและ reason ต่อรายการ |
| result_scope | ชุด/บริการ/ช่วงเวลา/กลุ่มที่ผลครอบคลุม |
| completeness | exact set / confirmed subset / unknown coverage พร้อมฐานการตัดสิน |
| costs | model calls, provider calls, elapsed time |
| warnings | เช่น unknown effective interval หรือ translation status ที่เกี่ยวข้อง |

การมี claims หนึ่งข้อไม่ทำให้ operation compare/list/count ถือว่าสำเร็จ ถ้าไม่ผ่าน completeness rule ของ operation นั้น

## 9. EvidenceReceipt และ CalculationReceipt

EvidenceReceipt ระบุ record ID, field/fact ID, revision, source ID/locator, snapshot, source scope และสถานะที่เผยแพร่ ทุก receipt ต้องเป็นสมาชิก snapshot ที่ pin ไว้

CalculationReceipt เพิ่ม input claim refs, normalized quantities/units, business rule ที่ยืนยัน, transformation version และผลลัพธ์ การแปลงชั่วโมงเป็นนาทีทำได้โดยกฎหน่วยมาตรฐาน แต่การปัดรอบหรือคิดต่อคน/ต่อกลุ่มต้องมีกฎธุรกิจรองรับ

Comparison เก็บผลแยกตาม option ID ถ้า source ไม่ระบุ billing basis ห้าม renderer แต่งว่าเป็นราคาต่อคนเอง ข้อมูลที่เพิ่มใหม่ต้องได้กฎเดียวกัน ไม่อาศัยชื่อ record เฉพาะใน benchmark

## 10. AuthorityResolution

Resolver ใช้เฉพาะ authority/supersession ที่มีหลักฐาน พร้อม context applicability และ effective period:

1. ตรวจว่าข้อมูลพูดถึง action/subject/เงื่อนไขเดียวกันจริงหรือไม่
2. รวม literal duplicates เมื่อทั้งเนื้อหา scope เงื่อนไขและ validity เข้ากัน ไม่รวมจากภาษาไทยเพียงช่องเดียวหากคำแปลขัดกัน
3. ใช้ supersedes/authority metadata ที่ยืนยันแล้ว ไม่ถือว่า record ใหม่กว่าหรือ owner draft ชนะอัตโนมัติ
4. ถ้าขัดกันและไม่มีเกณฑ์ตัดสิน ให้ส่ง conflict พร้อม source refs และคำถามที่เจ้าของต้องตอบ
5. ถ้าเป็นหลายข้อความขั้นตอนที่ยังไม่ได้ยืนยันเป็นฉบับเดียว ให้แสดงเป็น source variants แบบ partial โดยไม่ทำเหมือนบริการล่ม

โมเดลช่วยค้นว่าข้อความใดเกี่ยวข้องได้ แต่ห้ามเลือก authority จากความมั่นใจหรือความลื่นไหลของภาษา

## 11. ObligationLedger และ VerifierResult

แต่ละ obligation มี task/option/constraint refs, expected kind, status, delivered claim refs, evidence check และ scope check

VerifierResult แยก:

- `plan_coverage`: factual needs ถูกนำเข้าแผนครบหรือยัง
- `constraint_coverage`: เงื่อนไขที่มีผลถูกใช้ครบหรือมีข้อขัดแย้งใด
- `execution_coverage`: operation และทุก options ถูก execute ครบหรือยัง
- `evidence_support`: claim/ตัวเลข/เงื่อนไขย้อน source ได้หรือไม่
- `answer_coverage`: คำตอบที่ render ยังมีเนื้อหาครบและไม่มี unsupported addition หรือไม่

การตรวจเชิงโครงสร้างเหล่านี้เป็นหลักฐานตาม contract ไม่เท่ากับการยืนยัน semantic correctness ทั้งหมด ต้องวัดกับป้ายที่ adjudicate แล้วและ review คำตอบที่ยังตัดสินอัตโนมัติไม่ได้

## 12. Terminal states และข้อความถึงผู้ใช้

| State | ความหมาย | แนวตอบ |
|---|---|---|
| supported | ตอบตาม operation ได้ครบและมีหลักฐานใน scope | ตอบตรงคำถาม |
| partial | มีบาง obligations ที่ตอบได้ | แสดงส่วนที่ตอบได้และส่วนที่ขาด |
| missing_input | คำถามยังขาดค่าที่ทำให้คำตอบต่างกัน | ถามเฉพาะค่าที่จำเป็น |
| missing_source | input ชัดแต่ไม่มีข้อมูลรองรับ | บอกช่องว่างข้อมูล |
| conflict | source ที่เกี่ยวข้องขัดกันและ resolve ไม่ได้ | ระบุจุดขัดแย้ง ไม่เดา |
| not_current | source ใช้ไม่ได้กับช่วงที่ถาม | บอกข้อจำกัดด้านเวลา |
| provider_unavailable | แหล่งข้อมูลภายนอกที่จำเป็นตรวจไม่ได้ | บอกว่าสถานะจริงยังตรวจไม่ได้ |
| budget_exhausted | ทรัพยากรคำขอหมดก่อนส่วนที่ยังต้องทำ | ไม่กล่าวว่าโมเดล/provider ล่ม; คงส่วนที่ตอบได้ |
| unsupported_operation | ข้อมูล/คำถามอาจมีแต่ executor ยังไม่รองรับ | บอกขอบเขตที่ยังทำไม่ได้ |
| invalid_plan | แผนไม่ผ่าน schema/semantics | ใช้ bounded compatibility หรือถามกลับ |

ภายนอกอาจ map ไป status ของ public API ที่มีอยู่ แต่เก็บ internal reason codes ครบ และระบุ version ของ mapping เพื่อไม่ให้เปลี่ยนความหมาย metric โดยไม่รู้ตัว

## 13. ModelGateway และ BudgetLedger

- ทุก caller ใช้ gateway/profile resolution ชุดเดียว บันทึก requested/resolved model และ adapter stage
- ตรวจ identity ก่อนใช้ผลและบันทึก transport/schema/semantics เป็นคนละสถานะ
- planner, selector, renderer ถ้ามี ต้องระบุ stage ชัด ค่า adapter_on ไม่อนุมานจากชื่อ profile อย่างเดียว
- อ่าน typed tasks ที่ไม่ขึ้นต่อกันก่อนตัดสิน fallback เพื่อไม่ให้งานหลัง starve
- งบเริ่มต้นอิงข้อจำกัด runtime ที่วัดอยู่ก่อน การเปลี่ยน max calls/timeout ต้องเป็นตัวแปรทดลองที่บันทึก ไม่เปลี่ยนพร้อม adapter แล้วอ้างผลจากน้ำหนักล้วน
- หมดงบไม่ส่งข้อความว่า provider unavailable และไม่วน retry ไม่จำกัด
- Freeze actual model messages/chat template/schema ที่ backend ใช้จริงด้วย ไม่ตรวจเพียง HTTP payload ด้านหน้า Transport ทดลองของ R121 เคยสร้าง context prompt ภายในจาก original_question; เมื่อต่อ contract ใหม่ต้องเปลี่ยนอย่าง versioned และตรวจว่าไม่ยังใช้ prompt/target รูปเก่าโดยไม่รู้ตัว

### Wire format เทียบกับ internal plan

PlannerProposal เป็น wire format ที่ต้อง version ส่วน compiled task graph เป็น internal representation ที่รวมผลจาก binder/normalizer ด้วย ต้องแยกว่า field ใดโมเดลส่งมาและ field ใดโค้ดสร้างหลังตรวจ

R121 checkpoint ไม่ได้ฝึกให้สร้าง R123 contracts นี้มาแล้ว การใช้ checkpoint เดิมต้องมี compatibility adapter ที่ประกาศว่าแปลงอะไรได้ และส่วนใดไม่มีหลักฐานพอให้เติม shared roles/ambiguity จึงต้องเก็บ unresolved ไม่ใส่ข้อมูลที่ compiler คาดเดาลงแล้วอ้างว่าโมเดลเรียนรู้มา

การทดลองหนึ่งรอบต้อง freeze accepted wire versions, adapter/parser, prompt, schema และ compiler เหมือนกันทุกแขน หากเปลี่ยน output protocol พร้อมการฝึก ต้องระบุว่าเป็นผลร่วมของ protocol adaptation กับ supervision และรายงาน structural failures แยกจาก semantic failures

## 14. TrainingExample และ ReviewRecord

TrainingExample มี question key, family, raw question, allowed context, contract version, plan label และ annotation provenance ไม่ใส่คำตอบราคา/เวลา/สิทธิ์เป็น target ของ planner

ReviewRecord เก็บ label source, teacher trace refs, source version ที่ใช้ตรวจ, reviewer/adjudication status, unresolved issues และเหตุผลการ quarantine ป้ายที่แก้ด้วย heuristic ยังเป็น draft จนกว่าจะ review ผ่าน

ห้ามปะปน train/dev/holdout โดยนับ paraphrase ของ core เดียวกันเป็นคนละ family และห้ามอ้างว่าชุดที่เห็นผลและใช้แก้ระบบซ้ำแล้วเป็น fresh holdout

## 15. การย้ายจาก R122

ต้องมี adapters ที่ชัดเจนระหว่าง MeaningTask/Plan เดิมกับ contracts ใหม่:

1. แปลง operation vocabulary โดยไม่สูญเสีย local/shared scope
2. เพิ่ม obligation ledger โดยรักษา source IDs/revisions เดิม
3. เปลี่ยน generic evidence selection ให้ผ่าน capability checks ก่อน
4. ย้าย model env resolution เข้า gateway เดียว
5. map terminal states ไป API เดิมอย่าง versioned และคง raw results เดิมไว้
6. Compatibility readers ต้องคืน contracts เดียวกัน มิฉะนั้นทำเครื่องหมายว่าเส้นทางนั้นยังตรวจความครบได้จำกัด

การแปลงนี้เป็นงาน implement ในขั้นต่อไป เอกสารนี้ไม่ได้ยืนยันว่า source R122 รองรับ contracts ใหม่แล้ว
