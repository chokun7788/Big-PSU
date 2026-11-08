# Coverage ก่อนเริ่ม implementation R102

สถานะทุกแถวคือ **planned — ยังไม่รันใน R102** เอกสารนี้ไม่ได้เปลี่ยน executed flags ของ R97 และไม่ถือผล R101 เดิมเป็น exact acceptance ของ R102

## 1. R97 exact scenarios ทั้ง 37 ข้อ

| ID | คำถามต้นฉบับ | Preconditions ที่ runner ต้องสร้าง | Expected invariant | ขั้นที่เกี่ยวข้อง / จุดต้องปิด |
|---|---|---|---|---|
| C01 | ขอราคาบุคคลภายนอกทั้งหมด | Published offered-service scope and rates have explicit evidence | price table uses service set and preserves audience | S05/S07/S08/S13 — ทั้ง service set และ audience; สมาชิกไม่มีราคาต้องไม่หาย |
| C02 | PC | Pending price/service slot and previously stated audience exist | fills service slot; preserves price intent and audience | S03/S05/S08 — PC เติม service พร้อมราคา/audience เดิม |
| C03 | ทั้งหมด | Pending task has a delivered candidate scope | selects full declared scope without inventing a new task | S03/S07 — ทั้งหมดใช้ displayed scope เดิมและอ่าน release ใหม่ |
| C04 | Please tell me: Can I get a refund | Source policy matches the action and actor | wrapper does not cause blanket rejection of supported policy | S04/S06/S10 — wrapper ไม่ปิด policy ที่ source รองรับ; actor/action ตรง |
| C05 | ตอนเย็นเปิดถึงกี่โมง | Schedule has explicit day-specific closing periods | uses temporal meaning; shows day differences or asks only material day slot | S05/S08/S13 — เวลาเย็น/วันต่างกันคง closing periods ไม่ตอบ now แทน |
| C06 | VALORANT ใช้ผู้เล่นกี่คน | Linked game_mode has count facts | reads mode relation; does not require unrelated optional fields | S07/S08/S10 — reverse game_mode FK และ required claims เฉพาะจำนวนผู้เล่น |
| C07 | ROV ถ้าเกมหลุดทำยังไง | General-play and competition contexts give materially different actions; no prior context | asks which context, not a generic topic menu | S05/S12 — ถาม context เมื่อทั่วไปกับแข่งขันให้ผลต่างจริง |
| C08 | ROV | Pending competition disconnect topic exists | inherits rule topic and resolves the selected game | S03/S05/S08 — เลือก ROV แล้วรักษา disconnect topic และ event qualifiers |
| C09 | กฎ CS2 | CS2 requested; only VALORANT rule is in first candidates | does not answer another game; tries declared CS2 scope or reports exact gap | S06/S09/S10 — CS2 ห้ามถูกแทนด้วย VALORANT แม้ retrieval สูงกว่า |
| C10 | ขอเกมทั้งหมด | Declared complete offering set is larger than retrieval top K | enumerates full offering set or labels pagination | S07/S08/S14 — complete offering set ใหญ่กว่า top-K และมี scope receipt |
| C11 | มีเกมใน PS5 กับ Switch อะไรบ้าง | Same game is offered in both scopes | deduplicates or groups by requested offering scope explicitly | S05/S07/S13 — multi-platform scope และ dedup ตามเกมหรือ offering ที่ถาม |
| C12 | ราคาและวิธีจอง PC | Current rate unavailable; booking procedure supported | does not calculate price; answers independent booking need | S11/S12/S15 — ราคาไม่พร้อมยังตอบ booking independent need |
| C13 | มี 100 บาทเล่นได้นานแค่ไหน | No current eligible rate or billing rule | no derived play time from missing or expired rate | S10/S11 — งบ derive ไม่ได้หากราคา/สูตรไม่พร้อม |
| C14 | PC 2 ชั่วโมง กับ VR 30 นาทีสำหรับบุคคลภายนอก | Eligible rate facts exist for requested tuples | does not create unintended audience/service/duration cross product | S05/S06/S11 — PC2h/VR30m/audience ไม่คูณไขว้ |
| C15 | เหมาเต็มวันราคาเท่าไร | Published rental package exists; no hourly-to-day conversion policy | reads package; does not infer rental price by multiplying hourly rate | S05/S08/S11 — rental package ไม่ derive จาก hourly |
| C16 | วันนี้เปิดไหม | Opening predicate is explicitly confirmed for request local date | date plus confirmed opening status in concise answer | S08/S10/S13 — วันไทยและ physical opening มี evidence; ตอบสั้นตรง |
| C17 | วันนี้เปิดไหม | Only empty bookable periods are known; physical opening unknown | does not infer physical closure from empty booking slots | S10/S12 — empty bookable ไม่ยืนยัน physical closed |
| C18 | ตอนบ่ายสามมีเครื่องไหนว่างบ้าง | Fresh read-only provider observation with known mapping exists | lists verified free resources within requested scope | S07/S08/S10 — free set ตรง15:00/freshness/mapping ไม่ใช่ available_now |
| C19 | PC ว่างไหมแล้วจองยังไง | Live provider unavailable; static booking procedure supported | reports live limitation and answers independent procedure | S08/S12/S15 — live unavailable ยังตอบ booking procedure |
| C20 | เกม A กับเกม B คือเกมอะไร | Both games have source-backed summaries | two subject-bound overview needs even though operation is the same | S05/S06/S15 — same task สองเกมคงสอง subject-bound needs |
| C21 | ก่อนกับหลัง First Blood ต่างกันยังไง | Relevant rule clauses with different conditions and dependencies exist | preserves both conditions and required exceptions | S07/S08/S10/S14 — before/after FirstBlood พร้อม linked exceptions ครบ |
| C22 | ไม่ใช่บุคลากร PSU ใช้ราคาไหน | Audience information and eligibility rules exist | negation is preserved; does not pick PSU staff rate by substring | S05/S06/S10 — not PSU staff ไม่เลือก staff rate เพราะ substring |
| C23 | ราคานี้ใช่ไหม | FAQ and structured rate disagree without resolved claim authority | reports or resolves conflict only with applicable source-backed policy | S07/S10/S12 — FAQ-rate claim mapping/overlapping applicability/authority/conflict |
| C24 | ราคา PC | Same service selected previously; rate has new published revision | re-reads amount from new release without asking service again | S03/S08/S16 — published new price revision reread โดยไม่ถาม service ซ้ำ |
| C25 | ราคา PC | Selected service or rate was withdrawn after previous answer | does not resurrect value from history, alias or cache | S03/S08/S16 — withdrawal ไม่ resurrect history/cache |
| C26 | PC | Unrelated contact record changed epoch; service task unchanged | revalidates dependencies and preserves valid task slots | S03/S16 — unrelated epoch change ไม่ทิ้ง valid task slots |
| C27 | มีอุปกรณ์ไหม | Explicit complete inventory is empty | may assert empty within that exact scope | S07/S10 — known complete empty inventory จึงตอบไม่มีใน scope นั้น |
| C28 | มีอุปกรณ์ไหม | Inventory completeness and members unknown | does not assert that no equipment exists | S07/S12 — unknown inventory ไม่แปลเป็นไม่มี |
| C29 | เกม A เล่นที่ไหน | Game supported_platforms exists but studio offering relation does not | does not equate supported platform with installed studio offering | S07/S10 — platform supported ไม่เท่ากับ offering/installed ที่ศูนย์ |
| C30 | Explain the booking exception in English | Source permission and exception are supported; translation mode permitted | critical decision, amounts and exception remain unchanged | S13/S14 — ภาษาอังกฤษคง decision/exception/critical quantities |
| C31 | ขอข้อมูลกติกา | Model returns body that is not valid plan JSON | temporary/plan failure is not reported as absence of source facts | S06/S12/S17 — invalid model body แยกจาก source missing |
| C32 | ขอราคาและกติกา | Shared budget exhausted while waiting for model | no recursive budget reset; finalizer reserve preserved | S01/S11/S15 — queue/model/children ใช้งบเดียว finalizer reserve ไม่ reset |
| C33 | เกมใหม่เล่นยังไง | New game uses supported kind with valid how_to_play source | data-only addition works without new name-specific regex | S04/S08/S16 — เกมชื่อใหม่จาก owner form ตอบ how_to_play ไม่เพิ่ม regex |
| C34 | ขอสูตรโปรโมชั่นแบบใหม่ | New record describes an unsupported billing operator | does not execute a model-invented business formula | S06/S11/S12 — unsupported operator ไม่ให้โมเดล invent formula |
| C35 | เกม A เล่นได้กี่คน | game_mode references a missing game or invalid platform | reports broken relation rather than guessing count | S07/S10/S12 — broken FK/invalid platform ไม่เดาผู้เล่น |
| C36 | ไม่ใช่ ขอวิธีจอง | Pending service-price clarification exists | replaces task explicitly instead of answering abandoned price intent | S03/S05 — explicit reset price→booking ไม่ตอบ abandoned task |
| C37 | ศูนย์อยู่ที่ไหน แล้วราคาเท่าไร | Address supported; price has a material unresolved service/audience scope | reads and answers address while asking only necessary price slot | S07/S12/S15 — ตอบที่อยู่แล้วถามเฉพาะ material price slot |

## 2. Task graph ทั้ง 32 งาน

Required alternatives ด้านล่างคัดจาก registry documentation ของ R101 เพื่อเป็นฐาน ไม่ได้ประกาศว่า R102 implementation ผ่านแล้ว ทุก task ต้องมี reader/render/status และอย่างน้อย source-backed positive กับ relevant missing/invalid path ผูก case IDs ก่อน freeze

| Task | Kinds | Required alternatives ฐาน R101 | R102 acceptance ที่ต้องมี |
|---|---|---|---|---|
| `game_overview` | game | summary | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `game_how_to_play` | game | how_to_play | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `game_platforms` | game | supported_platforms | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `game_at_studio` | game | offered + service_id | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `game_players` | game, game_mode | players_min + players_max | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `game_controls` | game, control_set | bindings OR limitations | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `game_account` | game, game_service | decision + conditions_all + details | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `game_version` | game, game_service, control_set | game_version | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; game/mode/platform/edition ไม่ปน; offering ไม่เท่ากับ installed |
| `equipment_explain` | equipment_model | name + device_type | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `equipment_specs` | equipment_model, resource, service | specifications | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `equipment_location` | equipment_model | zone_id OR specifications | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `equipment_list` | zone, service, resource | name | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `resource_capacity` | resource, service | capacity_min + capacity_max OR capacity_persons | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `service_duration` | service | session_minutes | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `center_operator` | center | operator | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `center_location` | center | address OR building + floor OR map_url | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `center_overview` | center | name + description | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `contact` | contact | channel + value | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `facility` | facility | name + location | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `people` | person | display_name + role + public_scope | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `audience` | audience | name + eligibility + required_proofs | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `price` | zone, service, resource, audience, rate | amount_minor + currency + unit + duration_minutes + calculation_rule | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; currentness/unit/audience/operator และ conflict |
| `rental` | rental_package, zone, audience | amount_minor + currency + duration_minutes + terms | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; currentness/unit/audience/operator และ conflict |
| `policy` | policy, faq | decision + conditions_all + exceptions + details OR answer | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; action/actor/conditions/dependent clauses ไม่ตกหล่น |
| `procedure` | procedure, faq | steps + preconditions OR answer | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; action/actor/conditions/dependent clauses ไม่ตกหล่น |
| `faq_content` | faq | answer | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; action/actor/conditions/dependent clauses ไม่ตกหล่น |
| `competition_rules` | competition, competition_rule | text + completeness | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; action/actor/conditions/dependent clauses ไม่ตกหล่น |
| `competition_metadata` | competition | event_name + rulebook_release | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `schedule` | schedule, closure | open_periods | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; physical-open/bookable/closing/maintenance แยกและ timezone/date scope |
| `news` | news | title + body | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |
| `live_status` | live_binding, service, resource, zone | service_id + provider + external_resource_key + status_mapping + freshness_policy + freshness_max_age_seconds | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่; target window/provider/mapping/freshness/partial static needs |
| `schema_attributes` | center, contact, facility, zone, equipment_model, resource, service, game, game_service, game_mode, control_set, audience, rate, rental_package, schedule, closure, policy, procedure, competition, competition_rule, news, person, faq, live_binding | ตาม explicit attributes ที่ผู้ใช้เลือก | เพิ่มข้อมูลใหม่ใน kind ที่รองรับ → ถามเฉพาะงานนี้ → ตรวจ receipts/qualifiers → แก้/ถอนแล้วอ่านใหม่ |

## 3. Owner kinds ทั้ง 24 หมวด

ทุกแถวต้องมี create/edit/withdraw ใน isolated fixture, preview/published separation, correct revision receipts และ Thai/English task-specific queries ไม่ใช้ข้อมูลทดลองแทน production

| Kind / ฟอร์ม | Publish-core fields จาก schema เดิม | References ที่ต้องคง |
|---|---|---|
| center / ข้อมูลศูนย์ | name, operator, timezone | ไม่มี FK ที่ประกาศใน catalog |
| contact / ติดต่อ | channel, value, purpose | ไม่มี FK ที่ประกาศใน catalog |
| facility / สิ่งอำนวยความสะดวก | name, location | ไม่มี FK ที่ประกาศใน catalog |
| zone / โซนบริการ | name | ไม่มี FK ที่ประกาศใน catalog |
| equipment_model / รุ่นและสเปกอุปกรณ์ | name, device_type | ไม่มี FK ที่ประกาศใน catalog |
| resource / เครื่องหรือทรัพยากรจริง | name, zone_id, physical_pool_key, operational_status | zone_id→zone, equipment_model_ids→equipment_model |
| service / รายการที่เลือกในระบบจอง | name, resource_ids, platform, session_minutes, occupancy_minutes | resource_ids→resource |
| game / ข้อมูลเกม | title | venue_zone_ids→zone |
| game_service / เกมที่ศูนย์มีให้เล่นจริง | game_id, service_id, offered | game_id→game, service_id→service, installed_resource_ids→resource, account_policy_id→policy |
| game_mode / รูปแบบเล่นและเล่นกับเพื่อน | game_id, mode_name, platform | game_id→game |
| control_set / วิธีเล่นและปุ่ม | game_id, platform, input_device, preset, bindings | game_id→game |
| audience / กลุ่มผู้ใช้ | name, eligibility | ไม่มี FK ที่ประกาศใน catalog |
| rate / ราคาต่อบริการ | service_id, audience_id, amount_minor, currency, unit, duration_minutes, calculation_rule | service_id→service, audience_id→audience |
| rental_package / ราคาเหมาโซน/ห้อง | name, zone_ids, audience_id, period_label, amount_minor, currency | zone_ids→zone, audience_id→audience |
| schedule / ตารางบริการ | timezone, zone_ids, weekday, open_periods, bookable_periods | zone_ids→zone |
| closure / วันปิด/ข้อยกเว้น | local_date, zone_ids, state, reason | zone_ids→zone, resolution_policy_id→policy |
| policy / นโยบายและกฎศูนย์ | topic, subject, decision, conditions_all, details | procedure_id→procedure |
| procedure / ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา | topic, preconditions, steps | ไม่มี FK ที่ประกาศใน catalog |
| competition / รายการแข่งขันและฉบับกติกา | game_id, event_name, rulebook_release, coverage | game_id→game, supersedes_id→competition |
| competition_rule / ข้อกติกาการแข่งขัน | competition_id, section_number, facet, heading, text, completeness | competition_id→competition, depends_on_ids→competition_rule |
| news / ข่าว/กิจกรรม/ประกาศ/โปรโมชัน | title, body | audience_ids→audience, contact_id→contact |
| person / บุคลากร/ทีมที่เปิดเผยได้ | display_name, role, public_scope | public_contact_id→contact |
| faq / คำถามเสริมและเอกสารทั่วไปของศูนย์ | question, answer, topic | related_ids→* |
| live_binding / การเชื่อมสถานะสด | service_id, provider, external_resource_key, physical_pool_key, status_mapping, timezone, freshness_policy | service_id→service |

## 4. จุดที่ต้องแก้ก่อน integrated batch

1. ปิด policy/FAQ clause coverage และ source-scoped amounts; ไม่ย้ายค่าจากหัวข้ออื่นเพื่อให้ตรง keyword
2. ปิด structured/prose claim mappings และ authority-conflict safe path โดยไม่เปลี่ยน approved history
3. ปิด targeted gaps/clarification: audience, validity, universal eligibility และ source scope
4. ปิด whole-request semantic orchestration สำหรับ mixed resolved/unresolved needs และ live/unknown target locks
5. ปิด runtime tracing/output contracts และ exact fixtures/runner สำหรับทุกแถว ไม่ใส่ executed=true จากการอ่านเอกสาร
6. แยก owner facts และ real integration blockers ออกจาก implementation status

ก่อน freeze ให้ใส่ implementation paths และ fixture/case IDs จริงใน machine-readable matrix จากนั้นหนึ่ง orchestrator รันทุก lane โดย source ไม่เปลี่ยน ดู [FULL_FLOW_TH.md](FULL_FLOW_TH.md) สำหรับลำดับทั้งหมด
