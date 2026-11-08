# แผนลงมือและตารางครอบคลุม R94

สถานะ: implementation specification · ยังไม่ติดตั้งตามแผนนี้ · ไม่รัน chatbot tests ในรอบจัดทำเอกสาร

## 1. สถานะเริ่มต้นที่ต้องยอมรับก่อน

- R78 มีโค้ด common หลังติดตั้ง R92; ผล R93 มาจาก frozen copy ของชุดนั้น ไม่ใช่ Flow R91 ที่ทำเสร็จทุกช่วง
- ของที่มีแล้ว: store/schema/evidence/revision lifecycle, domain readers/bridges หลายชนิด และส่วน R92 เช่น pinned provider, shared owner preview, readiness, task profiles สี่กลุ่ม
- ของที่ยังไม่ครบ: normalization ก่อนทุก branch, TaskPlan/semantic acceptance ทุกหมวด, qualifiers/dependency coverage, กลุ่มราคา/ระยะเวลา, generic explain/compare/procedure และการยืนยันพฤติกรรมบน published deployment/portable ล่าสุด
- `มีโมดูล` ไม่เท่ากับ `ผ่านคำถามทั้งหมวด`; `ข้อมูลพร้อม` ไม่เท่ากับ `เข้าใจคำถามทุกสำนวน`; `ติดตั้ง R78` ไม่เท่ากับ `ทุก package อัปเดต`

## 2. แหล่งโค้ดที่จะนำมาใช้และวิธีเชื่อม

Paths ในตารางอ้าง `r78_web_session_check_20261016/system/` โดยย่อ `common/` แทน `app/knowledge/common/` ไม่ใช่ไฟล์ใหม่ที่สร้างในงานออกแบบนี้

| กลุ่มโค้ด | สิ่งที่รักษา/นำมาใช้ | สิ่งที่ต้องเปลี่ยน |
|---|---|---|
| `app/pipeline/engine.py`, `migrated_chat.py` | scope, entry/session integration, provider injection | ย้าย normalization ก่อน common early return; entry เดียวรับ TaskPlan flow; ส่งทุกผลผ่าน finalizer |
| `common/query_contract.py`, `entity_search.py`, `schema_language.py`, `name_candidates.py`, `task_interpretation.py` | names/schema meaning/recovery ที่มีข้อจำกัดปลอดภัย | shared normalized input/spans; task recovery ไม่ถูกข้ามเพราะ exact name; แยก discourse/conditions |
| `common/task_registry.py`, catalog/schema files | readiness/kinds/fields | แยก data readiness registry จาก runtime task/acceptance registry ให้ชัด; ไม่เปลี่ยนชื่อ registry แล้วอ้างว่าครบ |
| `common/planner.py`, `read_contract.py` | JSON/schema/allowed fields/trace | เพิ่ม TaskPlan proposal/acceptance ก่อน EvidencePlan; ไม่คง field-only gate เป็นผู้ตัดสิน paraphrase ทั้งหมด |
| `common/query_scope.py`, `relations.py`, `discovery.py`, `intent_index.py`, `semantic_profile.py` | compatible names/relations/topic retrieval | task-compatible candidate recall; ไม่ล็อก entity ผิดก่อน semantic plan; บันทึก rejection reason |
| `common/answer.py` | orchestration/projection/readers ที่ใช้ได้ | ค่อยแยก executors ออกจากการตีความและ early returns; delegation ตาม capability |
| `common/billing.py`, `audience_scope.py`, `budget.py`, `price_comparison.py` | typed arithmetic/units/group checks ที่ยืนยันแล้ว | รับ service/audience/duration/quantity/date ที่ตรวจแล้ว; แยก parsing errors จาก validity |
| `common/legacy_bridge.py`, `legacy_intent_bridge.py`, `equipment_bridge.py`, `competition_bridge.py` | pure intent helpers, rental/equipment/clause behavior | audit dependency; อ่าน common evidence เท่านั้น; adapters ห้ามตัดสิน/ส่งคำตอบนอก finalizer |
| `common/control_rows.py`, `game_presence.py`, `faq_topics.py`, `unconfirmed_request.py` | controls/catalog/policy distinctions | เติม task granularity และ proposition/qualifier coverage |
| `common/open_day.py` และ configured live booking integration | compact date answer, source calendar, live read-only contract | plan ชี้ static vs live ตั้งแต่ต้น; scope/precedence/freshness/physical pool validation |
| `common/dialogue.py`, `followup_scope.py`, `qualified_reply.py`, `composition.py` | delivered context/role-aware follow-up/partial clauses | NeedGraph/pending-choice state; dependent tasks ไม่ถูกแยกจนความหมายหาย |
| `common/snapshot_provider.py`, `store.py`, `authority.py`, `evidence.py`, `provenance.py` | coherent revisions/source/authority | คง contract ร่วมทุก executor; audit caches/ref invalidation ไม่เปิด facts fallback |
| `common/translation.py`, `semantics.py`, render paths | labels/localization metadata | task-specific English output + polarity/numeric invariants; ชื่อเฉพาะไม่ตีเป็น translation failure อัตโนมัติ |
| `common/owner_server.py`, `ui/owner.js`, templates | editor/save/review/publish/preview | capability readiness ที่เข้าใจง่าย, published validation และ deploy identity ชัดเจน |

ตารางนี้เป็น functional change map ชื่อโมดูลใหม่จะกำหนดเมื่อ refactor จริง โดยรักษา public API และลดวง dependencies ไม่ได้อ้างว่าไฟล์ที่ระบุทำงานได้ถูกทุกกรณีแล้ว

## 3. วิธีเปลี่ยนทางเดินโดยไม่สร้าง Flow สองชุดซ้อนกัน

1. ตรึง baseline/app/data/config/model identity พร้อมสำรองไฟล์ก่อนแก้ในโฟลเดอร์รอบใหม่
2. สร้าง interfaces/normalizer/finalizer กลางใน candidate ก่อน แล้วทำ adapters ให้ typed executors ที่มีอยู่รับ interfaces เหล่านี้
3. สลับเป็นราย capability เช่น game overview → equipment explanation → policy/procedure ไม่ใช้ feature flag แยกตามชื่อคำถามหรือเฉลย
4. สำหรับ capability ที่ย้ายแล้ว ใช้ TaskPlan path เป็นผู้ตัดสินเพียงทางเดียว ไม่เรียก reader เดิมรอบสองหลัง guard ปฏิเสธ
5. Capability ที่ยังไม่ย้าย ใช้ common branch ปัจจุบันผ่าน explicit compatibility adapter ซึ่งรายงาน `interpretation_path=compat` ตามจริง ไม่มีคำรับรองว่ามี TaskPlan แล้ว
6. ถ้า compat กับ candidate ให้ผลต่างกัน ให้เก็บ paired diagnostic ในสภาพแวดล้อมทดสอบ ไม่ส่งสองคำตอบให้ผู้ใช้และไม่ตัดสินด้วยความยาว/คะแนนคล้าย/คำตอบที่ไม่ว่าง
7. ตัด old routing/lexical gate สำหรับ capability นั้นเมื่อ replacement ผ่านเกณฑ์และมี rollback ของ app/config ตามรุ่น อ้าง old gate ต่อหลัง TaskPlan ผ่านไม่ได้ เพราะจะสร้างปัญหาเดิมซ้ำ
8. ตรวจ integrated API/owner/published surfaces แล้วจึงเตรียม package; ไม่แอบเปลี่ยน production authority หรือ approval ระหว่าง rollout

Rollback โค้ดต้องพิจารณา compatibility กับ schema/data revisions ไม่ย้อนทับฐานข้อมูลหรือประวัติของเจ้าของเพื่อให้โค้ดเก่าอ่านได้ หากมี schema migration ต้องออกแบบ forward/backward behavior ก่อนทำ

## 4. ลำดับทำงานและนิยามคำว่าเสร็จ

| ช่วง | งานและขอบเขต | ของที่ส่งมอบ | เกณฑ์ออกจากช่วง |
|---|---|---|---|
| S0 | baseline + behavioral inventory ทุก capability + instrumentation | manifests, compatibility map, need/plan contracts, trace schema | บอกได้ว่า task ใดไป path ไหน; preserved sources/logs/data; ไม่อ้าง as-built ปน target |
| S1 | shared normalization/context/task candidates ไทย/อังกฤษ | NormalizedQuery, discourse/protected-span handling, pending-state contract | exact name + noisy task, typo preface, wrapper, short reply และ hard negatives ใช้แกนเดียว; ไม่เปลี่ยนเลข/negation |
| S2 | TaskPlan acceptance + NeedGraph + resolver/finalizer | accepted/uncertain plans, per-need outcomes, compatibility adapters | schema-valid wrong plan ถูกปฏิเสธ; paraphrase ที่รองรับไม่ถูก old regex veto; uncertainty ถามตรงช่อง |
| S3 | game/equipment/catalog/center/contact/directory/tasks ที่ไม่ซับซ้อน | task-to-field/ref projections และ task renderers | new records ใน kinds เดิมตอบได้โดยไม่แก้ชื่อในโค้ด; explain/list/how-to/controls/installed/live ไม่สลับกัน |
| S4 | price/rental/budget/audience/duration + policy/procedure | typed slot/qualifier models, current-price calculations, action-specific policies | parsing correctness แยก expiry; ไม่มีการเดา rate/billing; compound ตอบ independent facts ได้; unsupported policy ตอบตรงเรื่อง |
| S5 | competition/compare/dependencies + schedule/live/cardinality | proposition selection, date precedence, live state model, all/list continuation | rulebook/edition ถูก; exceptions ครบ; unknown ไม่เป็น free; opening ไม่ผูก occupancy; physical pool ไม่ซ้ำ |
| S6 | owner lifecycle/localization/published behavior/cache | create/edit/publish/withdraw parity evidence และ release readiness | owner เพิ่ม/แก้รายการแล้วคำถามอ่าน revision ถูก; stale refs/translation ถูกแยก; draft ไม่รั่ว public |
| S7 | integrated verification + evaluator review + package | content/semantic/protocol/transport reports, build/runtime/data manifests | ผ่าน capability gates, no critical contradictions, package ตรง build, แจ้ง unknowns และข้อจำกัดที่ยังเหลือ |

Validity/authority, observability, safety negatives, translation และ preservation เป็น gates ทุกช่วง ไม่รอ S6/S7; ตารางจัดลำดับงานหลักเท่านั้น

S3–S5 ไม่ถือว่าเสร็จเมื่อแก้ได้เพียงหนึ่งเกมหรือหนึ่งประโยค ต้องมี coverage ต่อ task family + wordings + constraints + unseen records และต้องบันทึกขอบเขตที่ยัง compat อยู่ การผ่าน flow unit checks ไม่แทน semantic answer checks

ไม่กำหนดเวลาเสร็จหรือคะแนนเป้าหมายใหม่โดยไม่มีการวัด ข้อมูลปัจจุบันที่ยังไม่มีเอกสารทำให้ current-price capability ยังตอบยอดจริงไม่ได้ แม้ implementation ส่วนอื่นเสร็จแล้ว

## 5. ปัญหาเดิม P01–P37 ต้องไม่หายจากแผน

| ปัญหา | งานซ่อมในแผนรวม | ช่วงหลัก / หลักฐานเสร็จที่ต้องเก็บ |
|---|---|---|
| P01 | คืน behavioral contracts ก่อน common early return โดยแยก facts | S0–S2: routing/capability map และ trace |
| P02 | task typo recovery ร่วมกับ entity recovery แบบแยกหน้าที่ | S1: edits/protected spans/meaningful task evidence |
| P03 | entity exact ไม่เท่ากับ task understood | S2–S3: independently recorded task acceptance |
| P04 | แยก pure intent helpers จาก regex/loader dependencies | S0–S2: dependency audit; no per-record handler |
| P05 | task-compatible candidate recall โดยไม่เสีย independent topic | S2–S3: candidate/rejection logs + source-recall cases |
| P06 | semantic acceptance ไม่ขึ้นกับ lexical cue เดิมอย่างเดียว | S2: accepted paraphrases + rejected wrong plans |
| P07 | จำกัด LLM task/fields/roles และตรวจ meaningful coverage | S2: schema/semantic decisions แยก |
| P08 | independent partial answer และ dependent task graph | S2/S4/S5: covered/missing needs แสดงตรงจริง |
| P09 | zone/service/resource/equipment output granularity | S3/S5: relation path/identity/cardinality evidence |
| P10 | service/audience/duration/units/billing แยก validity | S4: slot plan + calculation trace |
| P11 | rental จาก package; conditions unknown ไม่แต่ง | S4: package inputs/terms/missing facts |
| P12 | overview/how-to ทุก records ใน task ที่รองรับ | S3: clean/noisy/held-out/new-record evidence |
| P13 | controls action/input/preset/platform และ source completeness | S3: binding/limitations/missing-action checks |
| P14 | rule propositions/dependencies/edition/compare | S5: source clause coverage + semantic translation review |
| P15 | open/bookable/maintenance แยกความหมาย | S5: status source และ conflicting fields แยก |
| P16 | local date/closure scope/precedence | S5: time boundary/override/conflict evidence |
| P17 | controlled live-unavailable ไม่เท่ากับ live ผิด | S0/S5/S7: fixture/live results คนละรายงาน |
| P18 | short follow-up เติม pending task ไม่เริ่มหัวข้อใหม่ | S1/S2: multi-turn delivered-state evidence |
| P19 | qualifier/action-specific policies + precise unknown | S4: neighboring policy negatives |
| P20 | English understanding/source/render/review แยก | ทุกช่วง/S6: invariants/localization lineage |
| P21 | task renderer แทน internal field menu/dump | S3–S5: answer body/diagnostics separation |
| P22 | validation ไม่ใช้ confidence หรือ keyword ผ่านแทน meaning | S2/S7: acceptance reason + per-need correctness |
| P23 | transport/body/JSON/semantic/final correctness คนละ metric | S0/S7: model audit และ content reports |
| P24 | ไม่ดึง legacy retrieve_curated ที่มี ownership_blocked bug มาทั้งก้อน | S0/S2: audited pure helpers, no legacy loader fallback |
| P25 | expired/historical/current แยกตามเวลาที่ถาม | S4/S7: validity-aware outcome ไม่เปลี่ยน source dates |
| P26 | migration draft ไม่ใช่ published/owner approval | S0/S6: provider/release/publication identity |
| P27 | data-only onboarding ใน kinds/tasks เดิม | S3–S6: unseen records, create/edit/withdraw lifecycle |
| P28 | protocol route/mode/source IDs ไม่ใช่ content score | S7: separate raw strict table |
| P29 | keyword อ่อน/exact clause แข็งต้อง review แยก | S7: raw results retained + semantic labels/case notes |
| P30 | targeted pass ไม่แทน distribution | ทุกช่วง/S7: development/held-out/sample/full scopes ชัด |
| P31 | retained rejected plans และ phase timing | S0 เป็นต้นไป: trace completeness |
| P32 | shared deadline/model admission/queue/capacity | S0/S2/S7: no uncontrolled fan-out; latency/queue audits |
| P33 | unknown/conflicted เฉพาะ field ไม่ถือว่าข้อมูลทั้งหมดหาย | S2/S6: readiness/result reasons ต่อ need |
| P34 | archive comparison ไม่ใช่ schema-only experiment | S7: matched cohort/reference clock/build/data report |
| P35 | installed R78 กับ portable เป็นคนละ artifact | S7: package build/data/model manifest และ launcher identity |
| P36 | input layout/repeat guard ไม่ใช่ NLU ทั้งประโยค | S1: guard correction candidates ผ่าน task checks |
| P37 | preview/public core semantics ร่วม, authority/capabilities ต่างชัด | S6: same task result under equivalent provider, public envelope checked |

R93 findings ไม่ใช่ 37 ปัญหาใหม่อีกชุด: wrapper/typo-preface → P02/P06/P36, generic no-match → P03/P05/P19, fee slots+expiry → P10/P25, RoV wording → P14/P29, จอง keyword pass → P22/P29, little generalization → P27/P30

## 6. Schema ทั้ง 24 kinds ต้องมีงานที่ใช้จริง

ชนิดข้อมูลไม่เท่ากับจำนวน task families ตารางต่อไปนี้เป็น runtime coverage target ไม่ใช่สถานะผ่านแล้วของทั้งหมวด Field names อ้าง catalog ปัจจุบัน; source/validity/lifecycle เป็น metadata ของ record/evidence ประกอบทุกชนิด

| kind | งานที่ต้องตอบ | data path ที่สำคัญ |
|---|---|---|
| center | operator/overview/address/map/building/floor | operator, description, address/building/floor/map_url/timezone |
| contact | ติดต่อเรื่องใด/ช่องทาง/เวลาตอบ | purpose, channel/value, office_hours |
| facility | ที่จอดรถ/ที่นั่งพัก/เงื่อนไขเข้าถึง | location, usage_conditions, accessibility |
| zone | หมวดพื้นที่/ทรัพยากรในโซน/ตำแหน่ง | name/location, reverse resource/service/package refs |
| equipment_model | explain/specs/usage/list via resource | device_type, specifications/units, usage |
| resource | เครื่องใด/ความจุ/อุปกรณ์/สถานะกายภาพ | zone_id, equipment_model_ids, capacity_persons, physical_pool_key, operational_status |
| service | บริการ/รอบ/ผู้เล่น/เครื่องที่ใช้ | resource_ids, session_minutes, occupancy_minutes, platform/capacity, booking_product_key |
| game | overview/genre/how-to/description | title/edition, summary/genre/how_to_play, supported_platforms, scope/source listing |
| game_service | ศูนย์มีเกมนี้ให้เล่นที่ไหน/ติดตั้งที่เครื่องใด | game_id/service_id, offered/installed_resource_ids, account_policy_id |
| game_mode | เล่นด้วยกันกี่คน/โหมดใด | players_min/max, platform, network_requirement, studio_supported |
| control_set | action/button/input/preset/version | bindings, game_id/platform/input_device/preset, limitations/source_coverage |
| audience | ใครใช้ได้/หลักฐาน/เลือกกลุ่มราคา | eligibility, required_proofs, linked rates/packages |
| rate | quote/table/compare/budget | service_id/audience_id, amount_minor/currency/unit/duration_minutes, calculation_rule |
| rental_package | ราคาเหมา/รวมอะไร/เงื่อนไข | zone_ids/audience_id, period_label/duration_minutes, amount_minor, equipment_included/terms |
| schedule | วันเปิด/จอง/maintenance | timezone/weekday/zone_ids, open/bookable/maintenance periods |
| closure | วันปิดพิเศษ/เวลา override | local_date/zone_ids/state, periods/reason/resolution_policy_id |
| policy | permission/prohibition/exception/consequence | subject/decision/conditions_all/exceptions/consequence/procedure_id |
| procedure | ขั้นตอน/เอกสาร/กำหนดเวลา/ผล | preconditions/steps/required_documents/deadline_minutes/outcome |
| competition | รายการ/เกม/edition/division/coverage | game_id/event_name/division/rulebook_release/supersedes_id |
| competition_rule | whole book/facet/proposition/compare | competition_id/section_number/text/facets/depends_on_ids/completeness/source_order |
| news | ข่าว/กิจกรรม/กำหนดการ/สมัคร | title/body, event_start/end/audience_ids/contact_id/registration_url |
| person | บุคลากร/หน้าที่/ทีม/ช่องทางสาธารณะ | display_name/role/team/affiliation/period/public_scope/public_contact_id |
| faq | คำตอบตามหัวข้อ/ขอบเขต/related facts | question/answer, related_ids/topic/scope_note/query_profile |
| live_binding | สถานะสดตาม mapping | service_id/provider/external_resource_key/physical_pool_key/status_mapping/timezone/freshness_policy |

ถ้า kind ยังไม่มี records จริง ใช้ synthetic isolated fixture ภายหลังเพื่อพิสูจน์ flow ได้ แต่ห้ามเรียกว่าศูนย์มีบริการนั้นจริง การมี unknown optional fields ไม่จำเป็นต้องถามเจ้าของทุกช่อง ใช้ readiness ตาม task

## 7. Verification ที่จะใช้เมื่อพัฒนา — งานรอบนี้ยังไม่รัน

### 7.1 สิ่งที่ต้องวัดแยก

- Task correctness: subject/operation/slots/audience/conditions/negation ถูกหรือไม่
- Retrieval/evidence: source ที่ควรมีถูกส่งถึง executor หรือถูกตัดที่ใด
- Answer correctness/completeness: ตอบตรงทุก need ที่มีหลักฐาน ไม่มีข้อยืนยันเกิน
- Business validity: current/historical/expired/conflicted แยกตามเวลาที่ใช้
- Translation: meaning/invariants/proper names/review state แยกกัน
- Dialogue: pending slot/ทั้งหมด/เปลี่ยนเรื่อง/ปฏิเสธ/แก้ตัวเลือก/withdrawn refs
- Protocol: route/mode/source identifiers ตาม contract ที่ตั้งใจ ไม่ใช้แทน semantic score
- Transport/performance: queued/admitted/HTTP/body/JSON/deadline และ end-to-end latency แยก

### 7.2 ลำดับตรวจที่พอพิสูจน์ implementation

1. Contract checks เฉพาะ interfaces/protected constraints ที่มีความเสี่ยงจริง
2. Paired targeted cases จาก R93 + paraphrases ไทย/อังกฤษและ negatives โดยเก็บ first-run outputs
3. Held-out wordings/entities ที่ไม่ใช้ปรับ grammar/threshold
4. Isolated new records ทุก kind ที่รองรับ พร้อม edits/relations/publish/withdraw/English source revision ไม่มี production approvals ถูกแก้
5. Multi-turn เช่น external price → PC/all, PC details → equipment, rulebook → facet; ไม่ใช้ single-turn sample รับรอง history
6. Integrated engine/API/owner/published path และ controlled live fixtures แยก liveจริง
7. ขนาดใหญ่เฉพาะ common + LLM ON ตามคำขอ/ขอบเขตที่อนุญาตภายหลัง ไม่รัน legacy ซ้ำเพื่อรองรับแผนนี้

Raw GT failures ต้องคงไว้ เพิ่ม review labels ว่า actual wrong fact, incomplete, wrong task, valid abstention, lexical-only mismatch, out-of-scope หรือ unknown cause แยก ไม่แก้เฉลย/เพิ่มคำผ่านเพื่อทำคะแนนสวย

### 7.3 เมื่อไรจึงบอกว่าช่วงหนึ่งเสร็จ

มี code diff + runtime/build identity + evidence artifact + known limitations ที่ชี้ capability ได้ ต้องผ่าน critical negatives ที่เกี่ยว ไม่อ้าง “ครบทุกหมวด” จาก four profiles หรือ readiness 24 kinds

ถ้ายังมีข้อผิดพลาดต้องระบุ root-cause stage และข้อเท็จจริงที่ยืนยันได้ แก้จุดที่ทำเองได้ต่อ ส่วนราคาหรือเงื่อนไขที่ไม่มีหลักฐานเก็บเป็น missing fact พร้อมคำถามเจ้าของที่เฉพาะเจาะจง ไม่ปิดทั้งโครงการด้วยคำถามกว้าง

## 8. เรื่องที่ทำเองได้กับเรื่องที่ยังต้องมีหลักฐานเพิ่ม

ทำเองได้: refactor normalization/task/adapter/ledger/renderer, analyze logs, translation draft/invariant checks, task-based readiness, cache/revision handling, evaluator review และ isolated fixtures

ต้องมีเอกสารหรือการตัดสินใจเฉพาะเรื่อง: current tariff หลัง expiry, duration/billing/package terms ที่ไม่ระบุ, policy conflicts ที่แหล่งยืนยันขัดกัน และการอนุมัติเผยแพร่จริง ไม่ส่งคำถามเจ้าของซ้ำในเรื่องที่ผู้ใช้ยืนยันแล้ว เช่น 12–13 ไม่เปิดจอง, VR30 ใช้ช่องเต็มชั่วโมง, สถานะจองจริงที่ตรวจแล้ว และการยอมรับภาษาอังกฤษเดิมตามขอบเขตนั้น

ตัวอย่างคำถามที่จำเป็นเมื่อไม่พบหลักฐานในไฟล์: “อัตราชุดนี้สิ้นสุดก่อน 1 เม.ย. 2026 ใช้ตารางใดต่อและเริ่มวันไหน” หรือ “แพ็กเกจนี้ระบุเต็มวันแต่ไม่ระบุชั่วโมง รวมกี่ชั่วโมงและต่อเนื่องหรือเลือกเป็นรอบ” ถ้าหาหลักฐานที่ตรงเจอเองให้ใช้หลักฐานนั้น ไม่ถามซ้ำ
