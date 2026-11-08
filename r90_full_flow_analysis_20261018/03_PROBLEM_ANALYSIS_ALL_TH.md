# วิเคราะห์ปัญหาทั้งหมดที่พบ — Legacy R64 เทียบ Common R88

## 0. คำว่า “ทั้งหมด” และระดับหลักฐาน

ครอบคลุมโครงสร้างโค้ดทั้งสอง snapshot, ผล 20,554request/55,811 grades ต่อแขน ON, ประเภทเหตุไม่ผ่านทุกชนิดที่ logs เก็บไว้, state/translation/data/source/transport/publication และข้อจำกัดของตัวตรวจ ไม่ได้อ้างว่าอ่านเจตนาถูกด้วยมนุษย์ครบทุกคำถามหรือรู้ rootcause ทุกกรณีจาก keywordfailure เพียงอย่างเดียว

- **C — Confirmed:** ยืนยันเส้นทาง/ค่า/trace หรือ source โดยตรง
- **H — Hypothesis:** เป็นคำอธิบายที่ต้องตรวจรายกรณี ไม่เอาจำนวนกลุ่มอัตโนมัติมาเท่ากับจำนวน semanticbugs
- **D — Designed/controlled:** guard/fixture/unknown ที่อาจเป็นผลที่ถูกต้อง ไม่ใช่ต้องทำให้ตอบเพื่อผ่าน
- **R — Risk/unverified:** โครงสร้างต่างหรือขอบเขตที่ยังไม่ได้ตรวจจริง ไม่อ้างว่าเป็น failure ที่เกิดแล้วทุกกรณี

งานนี้อ่านโค้ดและผลเดิมเท่านั้น ไม่รัน chatbot/LLM ใหม่ ไม่แก้ ownerfacts,productioncode,approvals หรือ logs เดิม

## 1. สรุปตัวเลขที่เทียบได้

| ตัวชี้วัด | Legacy ON R64 | Common ON R88 | ความหมาย |
|---|---:|---:|---|
| Requests / Grades |20,554 /55,811|20,554 /55,811|ชุดโจทย์และ key ตรงกัน|
| Strict ทุกเกณฑ์เดิม |42,601/55,811 =76.33%|5,033/55,811 =9.02%|รวม route/intent/mode/status เดิม ไม่ใช่เนื้อหาล้วน|
| Positive literal ตัวตรวจเดียวกัน |23,517/24,909 =94.41%|17,960/24,909 =72.10%|ข้อความ/ข้อกฎที่ต้องปรากฏ ไม่ใช่ semanticaccuracy ทั้งคำตอบ|
| คำถามที่ผ่าน positive ทุกแถวของตัวเอง |8,160/8,907 =91.61%|5,962/8,907 =66.94%|อีกส่วนของ 20,554 ไม่มี positivecontract ชนิดนี้ ไม่อ้างว่าถูกครบ|
| Execution exceptions |2,694|2|คนละ runtime/deadline; แยกความเสถียรจากเนื้อหา|

Positive paired: ทั้งคู่ผ่าน 17,596 / เดิมผ่านใหม่ไม่ผ่าน 5,921 / ใหม่ผ่านเดิมไม่ผ่าน 364 / ทั้งคู่ไม่ผ่าน 1,028 grades ความต่างไม่ใช่แค่ route แต่จำนวน literalfail ก็ยังรวมคำแปลคนละสำนวนและ guard ราคาหมดอายุด้วย

ตาม locale ในคำขอที่คง cohort เดียวกัน: ไทยเดิม 95.47%→ใหม่ 73.61%; อังกฤษ 96.00%→70.79%; auto81.83%→68.88% ไม่ใช้ effective-language ต่างรุ่นสลับ denominator ไปมา

**ข้อสรุปที่รับผิดชอบได้:** ความสามารถตีความ/เลือกข้อมูล/ประกอบคำตอบของใหม่ยังมีช่องว่างจากของเดิมจริง แต่ schema กลางไม่ได้เป็นสาเหตุเพียงตัวเดียว และไม่ควรเอาคำตอบราคาที่หมดอายุหรือข้อมูลที่ยังไม่ยืนยันกลับมาตอบเพื่อทำคะแนน

## 2. ปัญหากระจุกที่ขั้นใด

| หลักฐานจาก R88 | จำนวน | สิ่งที่บอก/สิ่งที่ยังไม่บอก |
|---|---:|---|
| exactentitymethod |10,179 requests|เจอชื่อ ไม่ได้แปลว่ารู้ task|
| exactentity แต่ไม่มี requestedfields |1,979 requests|ช่องว่างชื่อ→operation/field; ไม่ใช่ typo ทุกข้อ|
| มี selectedIDs แต่ไม่มี fields |3,747 requests|อาจเป็น clarification/list/metadata; ต้องดู task ก่อนตีว่า error|
| semantic_review_needed |2,289 requests|เคสที่ grammar ไม่พอ ไม่ใช่ทุกข้อผิด|
| schema ผ่านแต่ semanticguardrejectunverified |2,494audit events|เหตุหลักหนึ่งที่ LLM ตอบ JSON ถูกแต่ไม่ได้ใช้แผน; ไม่ใช่ 2,494uniqueusers|
| field-planner final accepted |129audit events|finalmethodbounded_llm_schema_fields พบ 62 requests เนื่องจาก call ย่อย/outerpath|
| clarification |6,090 requests|รวมการถามเพิ่มที่จำเป็นกับ falseclarification ต้องแยก|
| rejectedcandidate→saferesponse |700 requests|validation ทำงาน แต่ผู้ใช้อาจไม่ได้ส่วนที่ตอบได้|
| ModelHTTPtransporttimeout |36 calls|ไม่ใช่คำอธิบายของ contentfail ทั้งหมด|
| fixedconfidence.8 |10,969 requests|ค่าคงที่ ไม่ใช่ความถูกต้อง 80%|

Counts ของ finalplan,recursiveaudits,HTTPcalls,gradeevents และ uniquequestions เป็นคนละหน่วย ไม่บวกข้ามกันเพื่อสร้างจำนวนปัญหาที่มากกว่า requests

## 3. กลุ่มอัตโนมัติที่ครอบคลุมทุก raw-failed request

กลุ่มหลักจาก DEEP_ANALYSIS มี 18,824 requests ที่ไม่ผ่านอย่างน้อยหนึ่งเกณฑ์ แต่ละ request ได้กลุ่มหลักเพียงหนึ่งกลุ่มตาม priority ของตัวจัดหมวด ไม่ใช่ยืนยันว่าเหตุอื่นไม่มี ดูรายละเอียดทุก grade ใน FAILURE_EVIDENCE.sqlite และดัชนีท้ายชุดนี้

| กลุ่มหลัก | Requests |
|---|---:|
| protocol_only_no_literal_failure | 10,606 |
| clarification_or_topic_confirmation | 4,467 |
| competition_clause_scope_or_wording | 330 |
| protocol_outcome_or_lineage_needs_review | 1,776 |
| native_grader_failure_needs_content_review | 455 |
| execution_or_watchdog | 2 |
| source_validity_guard_vs_historical_oracle | 500 |
| model_transport_failure | 31 |
| source_selection_field_coverage_or_wording | 516 |
| price_scope_validity_or_wording | 107 |
| controlled_booking_unavailable | 18 |
| control_projection_or_wording | 9 |
| product_scope_guard_vs_historical_oracle | 4 |
| specific_unconfirmed_policy_vs_expected_answer | 2 |
| retry_or_data_model_guard | 1 |

**ห้ามตีความ** 10,606protocol-only เป็น semanticcorrect10,606 ข้อ เพราะบางข้อไม่มี positivecontract และห้ามเรียก 4,467clarification ว่า 4,467falseclarifications โดยยังไม่อ่าน source/needs

## 4. รายการปัญหาและแนวแก้รายประเภท


### P01 — เปลี่ยน data format พร้อมเปลี่ยนเส้นทาง interpreter โดยไม่ย้าย behavioral contract ครบ

**ลำดับ/สถานะหลักฐาน:** P1; C: ยืนยันลำดับจากโค้ด; ผลกระทบทั้งระบบต้องแยกรายกรณี

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** ทั้ง 20,554 requests เข้า profile ใหม่; ไม่ใช่จำนวนคำตอบผิด 20,554

**จุดใน Flow:** engine entry → migrated dispatcher

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

Engine ใหม่ return migrated_answer ก่อน legacy request focus, cue preflight, typed fee/compound และ _answer_single ที่มี preprocess/handlers จึงไม่เกิดความสามารถเดิมจากการมีข้อมูลเท่านั้น R87 นำกลับบางส่วนแต่ยังไม่ใช่ parity ทั้งต้นไม้

**หลักฐานที่พบ**

R87finalbridges รวม 202 requests: intent16, rental5, equipment166, overview13, protest2; ชุดย่อย 55/55 ไม่ได้พิสูจน์ว่ากลุ่มอื่นผ่านด้วย

**สิ่งที่ควรตอบหรือควรทำแทน**

แยกการตีความงานออกจาก facts provider ให้ task contract เดิมที่ยังถูกต้องส่งต่อไป current common records ได้ โดยรักษา owner source/validity ใหม่

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ adapter ชั้น task/operation/slots/qualifiers ไม่เรียก legacy answer loader; map old output contracts ไป schema/joins ปัจจุบัน; เลือก domain ที่มีช่องว่างจริงก่อน

**วิธีตรวจหลังแก้**

ใช้คำถามเดิม/ใหม่คู่กันแล้วตรวจ entity, operation, fields, qualifiers, output coverage และ source revision รวม negative/ambiguous cases ไม่ใช้ score รวมอย่างเดียว

**ต้องใช้มนุษย์หรือไม่**

ทำโค้ด/การวิเคราะห์เองได้; ไม่ต้องให้เจ้าของออกนโยบายใหม่

**Source code:**

- [app/pipeline/engine.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/engine.py:840)
- [app/pipeline/migrated_chat.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py:13)

### P02 — การฟื้นคำผิดของ task cue ไม่ได้ถูกเรียกเหมือนเดิม

**ลำดับ/สถานะหลักฐาน:** P1; C: มีคู่คำถาม+trace และตำแหน่งโค้ด

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** known-name+no-fields1,979 requests เป็นอาการที่เกี่ยวข้อง ไม่ใช่ทั้งหมดเกิดจาก typo

**จุดใน Flow:** raw input → task normalization

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

เดิมมี keyboard-neighbor/transposition/multi-error/cue/game variants ส่วน common normalize กับ schema-language recovery คนละช่วงและคนละเงื่อนไข ชื่อเกมที่ exact ได้ทำให้ไม่ต้อง fuzzy ชื่อ แต่คำกริยาหรือชนิดคำถามยังผิดอยู่

**หลักฐานที่พบ**

Zelda “คือกมอะๆร”: entity ตรง, operationNone, requested_fields ว่าง, unresolved clause ยังอยู่ ข้อมูล summary/genre/how_to_play/official_description ในฐานกลาง known แล้ว

**สิ่งที่ควรตอบหรือควรทำแทน**

ฟื้นความหมายของ operation โดยรักษา raw และ edit trace ไม่แก้ชื่อเครื่อง ตัวเลข edition/วันที่/negation แบบเดา

**แนวแก้ที่รักษาข้อมูลจริง**

แชร์ pure recovery/task cue helpers ของเดิมก่อน semantic field selection พร้อม candidate/margin/anchor protection ไม่เพิ่ม alias ประโยคทีละข้อ

**วิธีตรวจหลังแก้**

ตรวจ double/delete/transpose/neighbor/multiple edits ใน task และ entity แยกกัน มี hard-negative ชื่อคล้าย/PC1 กับ PC11/CS2 กับ VALORANT

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้ในขอบเขตข้อความและ facts เดิม

**Source code:**

- [app/pipeline/preprocess.py :: preprocess_input](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/preprocess.py:120)
- [app/knowledge/common/query_contract.py :: normalize](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_contract.py:13)
- [app/knowledge/common/answer.py :: named](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:90)

### P03 — Exact entity ถูกเข้าใจผิดว่าเข้าใจคำถามแล้ว

**ลำดับ/สถานะหลักฐาน:** P1; C: ยืนยันจาก aggregate และ trace

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** exact10,179; exact แต่ไม่มี requested fields1,979; selected entity ไม่มี fields รวม 3,747

**จุดใน Flow:** entity match → operation/field selection

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

exact แปลว่าพบชื่อ/alias ไม่ได้บอกว่า user ขอ overview, price, controls, permission หรือ status ตัวกลางยังอาจเหลือ genericfield menu แม้ subject แน่นอนแล้ว

**หลักฐานที่พบ**

Zelda ได้ record ถูกแต่ถามชื่อเกมอย่างเป็นทางการ; SF-006 ได้ PCscope แต่คำว่าอุปกรณ์ยังไม่ลง render contract

**สิ่งที่ควรตอบหรือควรทำแทน**

ระบุ object และ task คนละ slot แล้วตรวจว่ามีคำตอบสำหรับ task ที่ถาม ไม่เสนอ menu ภายในเพียงเพราะรู้ kind

**แนวแก้ที่รักษาข้อมูลจริง**

เพิ่ม typed request contract ที่มี operation/needs/constraints/unknown slots ก่อนเลือก field; field menu ควรเกิดเมื่อ user ยังไม่ระบุเจตนาจริงเท่านั้น

**วิธีตรวจหลังแก้**

ชุด exact-name+clean task, exact-name+typo task, unnamed task, multi-target และ short followup ต้องเลือกทางต่างกันถูก

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/answer.py :: named](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:90)
- [app/knowledge/common/query_scope.py :: primary_ids](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py:33)

### P04 — Regex/priority ของเดิมไม่ได้กลายเป็นความหมายของ aliases โดยอัตโนมัติ

**ลำดับ/สถานะหลักฐาน:** P1; C: source+R86audit; จำนวนผลเสียเฉพาะยังไม่แยก

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** legacy intent final16 requests; routing stage พบ 23 events

**จุดใน Flow:** trusted patterns → current FAQ

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

legacy matchercompilepattern และ priority ขณะที่ common namedescapealias เป็น literal R87bridge รับเฉพาะ whole-query coverage และ unique currentintent รวมทั้ง exclude หลาย operation จึงมีขอบเขตต่างจาก router เก่ามาก

**หลักฐานที่พบ**

R86 พบ regex-looking aliases61FAQ/308entries ใน snapshot ที่ audit ไว้ ไม่ใช้ตัวเลขนั้นอ้างว่าทั้ง 308 กำลังตอบผิด R87FAQadvance time แก้ได้ แต่ยังไม่ใช่ทุก paraphrase

**สิ่งที่ควรตอบหรือควรทำแทน**

routing configuration ใช้เพื่อระบุ task ส่วน answer อ่านจาก common intent_key/source ปัจจุบันเสมอ

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ intent compiler/adaptor ที่ประกาศ coverage และ exclusions ชัด รองรับคำสุภาพ/กรอบคำถามแบบ semantic ไม่ compile ทุก owner alias เป็น regex

**วิธีตรวจหลังแก้**

เปลี่ยน answer ใน DB/ถอน record แล้ว router ต้องไม่คืน answer เก่า; pattern ชนกัน/หลาย intent ต้องถามเพิ่มอย่างจำเพาะ

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/rules/matcher.py :: RuleMatcher](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/rules/matcher.py:14)
- [app/knowledge/common/legacy_intent_bridge.py :: select](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/legacy_intent_bridge.py:24)

### P05 — Candidate recall และ independent-topic anchor ปิดทางก่อน LLM เห็น source

**ลำดับ/สถานะหลักฐาน:** P1; C: policy ในโค้ด; H: ไม่ใช่ทุก no_candidate เป็น false negative

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** global diagnostic audit no_candidate1,403 / no_independent_topic_anchor1,733; เป็น events จากตัววิเคราะห์เดิม ไม่ใช่ request ไม่ซ้ำ

**จุดใน Flow:** entity_search retrieval → pre-inference guard

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

boundedtrigram, excerptbudget, allowed kinds, numbered/broad/live gates และ title/topic overlap ช่วยกันมั่วแต่ทำให้ unseen wording บางคำไม่ถึงโมเดล การมีคำตอบอยู่ท้าย field หรืออีก relatedrecord ไม่ได้รับประกันว่าจะได้ candidate

**หลักฐานที่พบ**

entity_search จำกัด 8candidates และ task backstop4, threshold.16; topic_alignment ระบุเองว่าไม่ใช่ entailment/calibrated score

**สิ่งที่ควรตอบหรือควรทำแทน**

เพิ่ม recall จาก schema/task/relations โดยยังรักษา quoted subject และ anti-confusion constraints ไม่ส่งทุก facts ให้ LLM แล้วเชื่อทั้งหมด

**แนวแก้ที่รักษาข้อมูลจริง**

วัด candidate recall จาก source IDs ที่รู้ผล แยก source absent, retrieval miss, preguard rejection, model selection error เป็นคนละเหตุ; รองรับ topic metadata ที่ owner ไม่ต้องเขียน regex

**วิธีตรวจหลังแก้**

ใช้ held-out paraphrase, tail facts, similar-policy negatives และ new records ที่ไม่เพิ่มชื่อใน code; เก็บ retrieved/rejected IDs พร้อม reason

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้จาก facts ที่มี; facts ใหม่ที่ยังไม่มีไม่ควรสร้าง

**Source code:**

- [app/knowledge/common/entity_search.py :: candidates](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py:57)
- [app/knowledge/common/entity_search.py :: topic_alignment](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py:42)

### P06 — LLM schema ผ่าน แต่ semantic guard ปฏิเสธเพราะ lexical intent ยังไม่รู้จัก

**ลำดับ/สถานะหลักฐาน:** P1; C: มี audit และ code ชัด; ไม่ใช่พิสูจน์ว่าทุกแผนที่ reject ควรถูกรับ

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** schema ผ่าน 2,623 events; final รับ 129; rejected_unverified_intent2,494 events

**จุดใน Flow:** planner checked_plan → semantic_guard

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

schema ตรวจว่าชื่อ field/shape ถูก แต่ semantic_guard ยังต้องมี strong typed needs ถ้า paraphrase/typo ไม่อยู่ใน grammar ก็ reject ถึงโมเดลจะเสนอ summary หรือ genre มาแล้ว ในทางกลับกันบางแผนโมเดลก็กว้างเกินจริงจึงไม่ควรรับทั้งก้อน

**หลักฐานที่พบ**

Zelda transport/schemaTrue แต่ finalFalse reasonrejected_unverified_intent; Fridaymaintenance ถาม policy แต่โมเดลเสนอ question และถูกปฏิเสธ

**สิ่งที่ควรตอบหรือควรทำแทน**

รับแผนที่ผูกแต่ละ clause กับ operation/field ที่มีความหมายได้จริง และตัดเฉพาะ extra fields; คง guard ต่อ unsupported facts/unknown target

**แนวแก้ที่รักษาข้อมูลจริง**

ปรับ request semantic binding และ sharedcue normalization; แยก unknown wording จาก unrelated task ไม่ใช้การปิด semantic_guard เป็นวิธีแก้

**วิธีตรวจหลังแก้**

ต้องมี positive paraphrase ที่เคย reject และ negative JSON ถูกแต่ intent ผิด วัด schema acceptance/semantic acceptance/answer content แยกกัน

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/planner.py :: semantic_guard](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py:54)
- [app/knowledge/common/planner.py :: _plan_fields_batch](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py:100)

### P07 — LLM เลือก field กว้างหรือผิดหน้าที่ แม้ JSON ถูกต้อง

**ลำดับ/สถานะหลักฐาน:** P1; C: ตัวอย่าง audit จริง; H: สัดส่วน model semantic errors ยังไม่ตีตราทุก call

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** ดู proposal ราย call ไม่เท่ากับ 4,206schema accepted audit เป็นคำตอบถูก

**จุดใน Flow:** schema prompt → field proposal

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

prompt อนุญาต field หลายชนิดของ selectedkind และ children โมเดลอาจเลือก metadata/publisher/edition/venue ทั้งหมดแทน gameoverview หรือเลือก FAQ.question แทน answer รูปแบบถูกแต่ task ยังผิด

**หลักฐานที่พบ**

Zelda เสนอ 12 fields รวม publisher_url/age_rating/profile_role ที่ไม่ได้ขอ; ResidentEvilVillage “ราคเท่าไหร่”เสนอ[]

**สิ่งที่ควรตอบหรือควรทำแทน**

เลือก minimal sufficient fields ต่อ clause ให้ครอบคลุมสิ่งที่ถามและ qualifier ไม่เพิ่ม all_fields เพราะไม่แน่ใจ

**แนวแก้ที่รักษาข้อมูลจริง**

ให้ task-to-field profiles ที่ใช้ร่วมทุก record และตัวตรวจ unrequested fields; metadata ช่วยอธิบายความหมาย field ไม่ใส่ facts ที่โมเดลไม่จำเป็นต้อง generate

**วิธีตรวจหลังแก้**

assert must-answer needs และ must-not-answer extra fields ทั้ง templatequestions และคำถามใหม่ ไม่วัดแค่ JSON/schema

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/planner.py :: _plan_fields_batch](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py:100)
- [app/knowledge/common/query_contract.py :: resolve_fields](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_contract.py:239)

### P08 — คำถามผสมมีส่วนขาด แล้วคำตอบที่มีหลักฐานถูกทิ้งทั้งก้อน

**ลำดับ/สถานะหลักฐาน:** P1; C: rejected_candidate และ composition paths; H: ไม่ใช่ 700 กรณีควรตอบทุกส่วน

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** rejected_candidate ถูกเปลี่ยนเป็น safe response700 requests; compound final262 requests

**จุดใน Flow:** clauses → partial coverage → outer migrated guard

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

บาง pathcompose เป็น partial ได้ แต่บาง path มี unresolved_query_clause จน validation ไม่ผ่าน แล้ว migrated dispatcher เปลี่ยนทั้งคำตอบเป็นขอแยกถาม ผู้ใช้จึงไม่ได้ส่วนที่ตอบได้

**หลักฐานที่พบ**

Cockpit30minutes+“howdoIboo” มี known price needs แต่ bookingclause ขาด และมี validity อีกชั้น ต้องแยกเหตุไม่ใช่อ้าง typo อย่างเดียว

**สิ่งที่ควรตอบหรือควรทำแทน**

ถ้าส่วนใดตอบได้อย่างอิสระตาม source ให้ตอบพร้อมขอบเขต แล้วถามเฉพาะส่วนที่ยังไม่ทราบ; ถ้า dependency ทำให้ตอบส่วนแรกไม่ได้ต้องอธิบาย dependency

**แนวแก้ที่รักษาข้อมูลจริง**

กำหนด per-clause status/obligations และ atomicity ตามความสัมพันธ์ ไม่ล้างทุกส่วนหรือแสร้งว่าครบด้วยการตอบ clause เดียว

**วิธีตรวจหลังแก้**

mixedknown/unknown, negative correction, shared subject ต่าง period/audience และ conditional dependency ต้องไม่สลับ slot

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้ภายใต้ facts เดิม

**Source code:**

- [app/knowledge/common/composition.py :: compose](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/composition.py:16)
- [app/pipeline/migrated_chat.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py:13)

### P09 — ระดับ Zone/Service/Resource และ relation projection ยังไม่ตรงกับคำถามบางแบบ

**ลำดับ/สถานะหลักฐาน:** P1; C: trace ตัวอย่าง; H: ไม่ใช่ทุก literal ชื่อ zone ไม่ตรงคือ platform ผิด

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** source-selection/coverage/wording กลุ่มหลัก 516 requests; เป็นกลุ่มผสม

**จุดใน Flow:** primary IDs → relations → labels

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

ระบบอาจเลือก service ที่สัมพันธ์กับเกมถูกแต่ render เป็นบริการ 1-2/1-4Persons แทน zone ที่ถาม หรือ root มี relation อุปกรณ์แต่ requestedfields ไม่ยอม projection ไป equipment_model

**หลักฐานที่พบ**

Zelda ถาม whichzone ตอบ Nintendo สองบริการแต่ไม่พูด NintendoSwitchZone; SF-006relation_edges พบอุปกรณ์ PC แล้วแต่ยัง veto

**สิ่งที่ควรตอบหรือควรทำแทน**

คืนข้อมูลตามระดับที่ถามและมี source relationship รองรับ ไม่สร้าง zone membership/FK เองเพื่อให้มี label ตาม oracle

**แนวแก้ที่รักษาข้อมูลจริง**

มี task-specific projectionplan และ semantic role ของ root/child แสดง zone+service รายละเอียดเมื่อมีหลักฐาน; ห้ามใช้ name similarity แทน relation

**วิธีตรวจหลังแก้**

zone↔service↔resource↔equipment↔game-service tests รวม no-FK/withdrawn/multi-platform และ label equivalence

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้ถ้ามี relation/source grouping; mapping ที่ไม่มีต้องยืนยันแหล่ง

**Source code:**

- [app/knowledge/common/query_scope.py :: primary_ids](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py:33)
- [app/knowledge/common/relations.py :: related_attributes](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/relations.py:5)

### P10 — การผูกกลุ่มราคา หน่วยเวลา และบริการยังต้องแยกจากการงดตอบเพราะราคาเก่า

**ลำดับ/สถานะหลักฐาน:** P1; C: source และ plans; H:107diagnostics ไม่ใช่ 107 ราคาคิดผิดที่ยืนยันแล้ว

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** price_scope_validity_or_wording107 requests; regular rate18 มี knownexpiry/6unknownvalidity

**จุดใน Flow:** price needs → audience/rates → billing

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

คำถามอาจมี VR30 เป็นชื่อ package และ 3 ชั่วโมงเป็นเวลาที่เล่น ต้องไม่เลือกเลขแรกเป็นเวลาสุดท้ายเสมอ กลุ่มภายนอกทั่วไป/GeneralStudent/PSU ต่างกัน การรู้ game ไม่พอคำนวณราคาโดยไม่รู้ service

**หลักฐานที่พบ**

ตัวอย่าง GeneralStudent VR30 นาที 3 ชั่วโมง: เดิมตอบ 30 นาที 190 บาทจาก source เก่า ใหม่งดราคาปัจจุบันเพราะ expiry; ผลนี้ไม่ยืนยัน duration parser ของฝั่งใดว่าถูกทุกเงื่อนไข

**สิ่งที่ควรตอบหรือควรทำแทน**

แยก service package duration, requested play duration, reserved occupancy และ audience แสดง unknown เฉพาะที่มีผลต่อจำนวนเงิน

**แนวแก้ที่รักษาข้อมูลจริง**

ใช้ billing contract ระบุหน่วย/rounding/minimum explicit และ source revision; หาก contradictory duration ให้ถามเจาะจง ไม่คูณเองจากราคาเก่าที่หมดอายุ

**วิธีตรวจหลังแก้**

boundary30/60minutes,3h,หลาย service,ต่างกลุ่ม,expired/unknown validity พร้อม expected price ที่มี source และ reference date

**ต้องใช้มนุษย์หรือไม่**

parser ทำเองได้; ราคาปัจจุบัน/วันที่มีผลที่ไม่มีหลักฐานต้องเจ้าของ

**Source code:**

- [app/knowledge/common/billing.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/billing.py:1)
- [app/knowledge/common/audience_scope.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/audience_scope.py:1)
- [app/knowledge/common/price_comparison.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/price_comparison.py:1)

### P11 — ราคาเหมาอ่านได้แล้ว แต่ไม่ใช่ทุกเงื่อนไขการเช่ามีนโยบายให้ตอบ

**ลำดับ/สถานะหลักฐาน:** P1/ข้อมูล; C: bridge/fixture และ inventory; D: unknown ที่ถูกต้อง

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 24packages validity unknown; rentalbridgefinal5 requests ใน corpus นี้

**จุดใน Flow:** rental interpretation → current package + followup

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

คำว่าครึ่งวัน/เต็มวันใน source ไม่ได้ให้ชั่วโมงหรือเงื่อนไข multi-day/hourly/custompackage เสมอ การเหมา excludeVR บางรูปแบบไม่เท่ากับมีแพ็กเกจใหม่ที่เอาราคามาลบกันได้

**หลักฐานที่พบ**

R87fixture แก้ราคา/เพิ่ม Aurora/ถอน package ได้และรักษา PCexternalfull→half→internal แต่ไม่ได้ยืนยัน every rental paraphrase/ownerbookingterms

**สิ่งที่ควรตอบหรือควรทำแทน**

ตอบราคาที่บันทึกและ scope ที่ตรง ชี้ว่าไม่มีข้อมูลชั่วโมง/การยกเลิก/มัดจำถ้าไม่มี source ไม่คำนวณส่วนลดเอง

**แนวแก้ที่รักษาข้อมูลจริง**

คง tuplecontract และ dynamiccatalog เพิ่ม general paraphrasecoverage ตาม task; ระบุ unknown validity/terms เป็น data readiness แยกจาก code

**วิธีตรวจหลังแก้**

compoundtuples,customduration,PS6unknown,cancelstate,all-except และ revisionupdate/withdraw ใน isolatedfixtures

**ต้องใช้มนุษย์หรือไม่**

โค้ด/state ทำเอง; เงื่อนไขใหม่/จำนวนชั่วโมง/วันมีผลต้องมี source เจ้าของ

**Source code:**

- [app/knowledge/common/rental_bridge.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/rental_bridge.py:109)

### P12 — ข้อมูลเกมมีอยู่แล้ว แต่ overview/description operation ยังไม่ครอบคลุมรูปประโยค

**ลำดับ/สถานะหลักฐาน:** P1; C: known field+trace ครบ

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** ตัวอย่าง Zelda; ไม่ได้สรุปว่า 51games ผิดทุกเกม

**จุดใน Flow:** game target → overview needs

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

known genre/summary/how_to_play/official_description ไม่ได้ช่วยถ้า operationNone หรือ defaultmenu มองว่า user ขอ title field ตัวใหม่บางเกมตอบได้ใน cleanwording แต่ไม่ยืนยันว่า task recovery ครอบคลุมทุกเกม

**หลักฐานที่พบ**

DATA_INVENTORY บันทึก knownfields ของ Zelda และ R89 มีคำตอบเก่าที่อธิบายได้กับคำถาม typo เดียวกัน

**สิ่งที่ควรตอบหรือควรทำแทน**

เมื่อถามเกมอะไรควรใช้ summary/genre ที่มี source ส่วน officialdescription ยาวให้ตามระดับรายละเอียดที่ขอ ไม่เผย age/publisher เพียงเพราะ field มี

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ game-overview contract ที่ไม่ผูกชื่อเกม ใส่ requestfocus และ length/scopeprojection จาก task ไม่เพิ่ม alias ทุกชื่อ+ทุกประโยค

**วิธีตรวจหลังแก้**

เปลี่ยนชื่อเกม/เพิ่มเกมใหม่/ไทยอังกฤษ/คำขาดเบิ้ลและ askingallvsbrief พร้อม assertsubstantivegenre/actiondescription

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้จาก source เดิม

**Source code:**

- [app/knowledge/common/query_scope.py :: primary_ids](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py:33)
- [app/knowledge/common/answer.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:200)

### P13 — ปุ่มและวิธีเล่น: action/mode mapping กับ completeness ไม่ใช่แค่ชื่อปุ่มปรากฏ

**ลำดับ/สถานะหลักฐาน:** P1; C: schema/projection และบาง diagnostics; H:ต้องอ่าน content รายข้อ

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 43controlsets;9 requests อยู่กลุ่มหลัก control_projection_or_wording

**จุดใน Flow:** control request → set/action bindings

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

ชื่อเกมกับ platform อาจตรงแต่ mode/action ไม่ตรง การแสดงปุ่มบางส่วนไม่ใช่ครบทุกปุ่ม source บางชุดไม่เคยตรวจ physical mapping ต้องไม่เพิ่มคำยืนยันเอง

**หลักฐานที่พบ**

MarioKartLivebindingsection มี th แต่ไม่มี en11 จุด; R87MarioPartybuttoncase ผ่านแต่ไม่ครอบคลุมทั้ง 43sets

**สิ่งที่ควรตอบหรือควรทำแทน**

ตอบ action ที่ถามพร้อม binding/เงื่อนไขของโหมด ถ้าขอทั้งหมดให้ครบ scope ที่ source มีและระบุ partialsource/mappingreview

**แนวแก้ที่รักษาข้อมูลจริง**

มาตรฐาน controlaction/mode/sourceclause และ coveragecounter; รักษา unknowncontroller/missingmode ไม่สร้าง mapping ใหม่

**วิธีตรวจหลังแก้**

singleaction/allbuttons/multi-mode/unknownplatform/partialset/Englishsection และ questiontypos

**ต้องใช้มนุษย์หรือไม่**

โค้ดและแปลจาก source ทำเอง; physicalmapping ที่ไม่ยืนยันไม่รับรองแทนผู้ตรวจ

**Source code:**

- [app/knowledge/common/control_rows.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/control_rows.py:1)
- [app/knowledge/common/query_scope.py :: control_projection](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py:240)

### P14 — กติกาแข่งขัน: เล่มถูกไม่ได้แปลว่าเลือก proposition/ข้อยกเว้นครบ

**ลำดับ/สถานะหลักฐาน:** P1; C: source/clauses และ diagnostics; H:330 ไม่ใช่จำนวน semantic ผิดทั้งหมด

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 330 requests ในกลุ่มหลัก; English301/Thai29 ตาม diagnostic

**จุดใน Flow:** competition target → facet → clause projection

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

ขอบเขตปี/edition, facet และ proposition ต่างกัน มีทางเลือก literal source/topic ที่ยังตอบส่วนใหญ่เกินหรือขาด conditions/penalties ได้ R87overview/protestbridge เป็นเพียงบางงาน

**หลักฐานที่พบ**

R88summarybridge13/protest2 requests; Tekkenetiquette บาง case ขาด exactEnglishclause ทั้งที่ source ใช้คำแปลอีกสำนวน ต้องอ่านทั้งความหมายและ completeness ก่อนลงว่าเลือกผิด

**สิ่งที่ควรตอบหรือควรทำแทน**

ให้ครบทุก proposition ที่ถามและ qualifier รวม dependencies ไม่เปลี่ยนเกมเอง; ถ้าไม่มี rulebook ของเกมนั้นให้บอกขอบเขต

**แนวแก้ที่รักษาข้อมูลจริง**

ใช้ target-locked clausecontracts/relation graph, distinguishsummary/all/detail และ semanticequivalence check ที่ไม่ลบตัวเลข/negation/conditions

**วิธีตรวจหลังแก้**

4rulebooks หลาย facet/compoundtopic,unknownedition,summaryvsall,consequence/exception,TH/ENparaphrase และ typo

**ต้องใช้มนุษย์หรือไม่**

โค้ด/การเลือกข้อทำเอง; เอกสารขัดกัน/รายการใหม่ที่ไม่มี source ต้องผู้จัด

**Source code:**

- [app/knowledge/common/query_scope.py :: rule_selection](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py:289)
- [app/knowledge/common/competition_bridge.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/competition_bridge.py:10)

### P15 — Open / bookable / Maintenance ยังมีความขัดแย้งใน metadata ที่ต้องแยกความหมาย

**ลำดับ/สถานะหลักฐาน:** P1/ข้อมูล; C:5fieldsconflicted; มี ownerconfirmation เดิมบางส่วนแล้ว

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** schedule7 records; open_periodsconflicted5

**จุดใน Flow:** schedule facts → day status / booking windows

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

migration เก็บความต่างระหว่าง dashboard กับ chatcalendar เป็น conflict ห้ามเอาช่วงจองไม่ได้ไปสรุปข้อเท็จจริงอื่นที่ยังไม่ทราบ และห้ามลืมข้อมูลที่ผู้ใช้ยืนยันแล้ว

**หลักฐานที่พบ**

5conflict notes ระบุ open/bookable/พักเที่ยง/Maintenance; ผู้ใช้ยืนยัน 12–13 ไม่มีให้จองและ VR30 กันชั่วโมงเต็มแล้ว

**สิ่งที่ควรตอบหรือควรทำแทน**

การตอบวันที่เปิดใช้ service/bookable ตาม source ที่ยืนยัน แยกวัน Maintenance/เวลาเข้าพื้นที่/occupancy ไม่ตอบ weekdaydebug แทนวันนี้วันที่...เปิด/ปิด

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ separate typed fields กับ authority mapping ใช้ confirmation เดิมแก้ได้เท่าที่รองรับ ไม่ขอให้ยืนยันซ้ำเรื่องจอง 12–13; คำถาม physical access ที่ยังไม่มีคำตอบค่อยถามเฉพาะประเด็น

**วิธีตรวจหลังแก้**

ก่อน/ตรง/หลังขอบเวลา,bookablegap,Maintenance,TH/ENday/date และ availability ต้องไม่ขัดกัน

**ต้องใช้มนุษย์หรือไม่**

ทำ mapping/ตรรกะเองได้; หากต้องระบุสิ่งอื่นนอก bookability ที่ยืนยันแล้วต้อง source เพิ่ม

**Source code:**

- [app/knowledge/common/open_day.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/open_day.py:35)
- [app/calendar/service_calendar.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/calendar/service_calendar.py:1)
- [app/knowledge/common/registry.py :: validate](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py:62)

### P16 — วันปิดพิเศษ วันหยุด และวันที่อ้างอิงต้องมี precedence ที่สม่ำเสมอ

**ลำดับ/สถานะหลักฐาน:** P1; C: date/closurecode; H:aggregate ไม่ชี้ว่าทุก closure ผิด

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** closure3knownvalidity; bulk ใช้ reference16 ต.ค.2026

**จุดใน Flow:** relative date → calendar/closure precedence

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

วันนี้/พรุ่งนี้/weekday กับ closure range ไม่ควรยึด weekday FAQ แทนวันที่จริง จุดเริ่ม/สิ้นสุดแบบ exclusive กับ timezone มีผลต่อ status

**หลักฐานที่พบ**

R88 มี calendar/date methods แยกจาก compactopenstatus; fullbulk ไม่ใช้วันที่ 18 ต.ค.ที่อ่านรายงานเป็น reference ทุกข้อ

**สิ่งที่ควรตอบหรือควรทำแทน**

ตอบวันที่ไทยและสถานะตามวันที่ถาม/closure ที่ครอบ ไม่ใช้สถานะวันนี้ไปตอบวันอื่นและไม่อ้าง liveoccupancy จาก calendar

**แนวแก้ที่รักษาข้อมูลจริง**

รวม calendardecisioncontract พร้อม source precedence/affectedzones และ timebound ไม่ให้ FAQ ทั่วไป override ข้อยกเว้นที่มีผล

**วิธีตรวจหลังแก้**

closurestart/end,all-day/partialday,crossdate,unknownspecialholiday,ไทย/อังกฤษ และ knownreferencecases

**ต้องใช้มนุษย์หรือไม่**

ตรรกะทำเอง; วันปิดใหม่ที่ไม่มี source ห้ามเดา

**Source code:**

- [app/knowledge/common/open_day.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/open_day.py:35)
- [app/calendar/service_calendar.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/calendar/service_calendar.py:1)

### P17 — สถานะจองถูกจำลอง unavailable ในชุดใหญ่ จึงห้ามตีความว่า live จริงล่มหรือจองผิด

**ลำดับ/สถานะหลักฐาน:** เงื่อนไขทดสอบ; D:ควบคุมโดย harness ไม่ใช่ regressionoccupancy

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** live_unavailable1,074 requests;18 อยู่กลุ่ม diagnostic หลักนี้หลังจัด priority

**จุดใน Flow:** common defer → live adapter → controlled fixture

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

bulk ตั้ง get_live_booking_status ให้ unavailable เพื่อไม่ให้เวลาทดสอบเปลี่ยน truth การที่ oracle อยากได้ slot แต่ระบบตอบ unavailable เป็นผลจากเงื่อนไขทดสอบนี้

**หลักฐานที่พบ**

RUN_SCOPE/runner กำหนด fixture_offline; ผู้ใช้ยืนยันสถานะจริงถูกต้องมาก่อนแล้ว ไม่เปิดประเด็นเก็บ truth ลูกค้าจริงใหม่ในรายงานนี้

**สิ่งที่ควรตอบหรือควรทำแทน**

แยก APIreachable/schema valid กับ free/booked correctness และเขียน evaluationcondition ชัด ไม่อ้าง failure1074 คือ WordPress จริงเสีย

**แนวแก้ที่รักษาข้อมูลจริง**

ใช้ known-result staticbookingfixtures ในการตรวจ logic และ sourcevalidatedlivegroundtruth เฉพาะเมื่อพร้อม/ได้รับคำขอแยก

**วิธีตรวจหลังแก้**

day/time/resource ranges,VR30fullhour,free-onlyallinventory,TH/EN และ upstream unavailable แต่ไม่ใช้ oldoccupancy แทน live

**ต้องใช้มนุษย์หรือไม่**

fixture ทำเอง; ไม่ต้องให้เจ้าของยืนยัน live ที่ยืนยันแล้วซ้ำ

**Source code:**

- [app/booking/live_status.py :: get_live_booking_status](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/booking/live_status.py:286)
- [app/booking/wordpress_status.py :: fetch_wordpress_status](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/booking/wordpress_status.py:44)

### P18 — ประวัติมาถึงแล้ว แต่ short follow-up ยังไม่กลายเป็น task ที่ตอบได้

**ลำดับ/สถานะหลักฐาน:** P1; C: SF-006 trace พิสูจน์ scope และ relations ถูกส่งมา

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** sessions12/24turns; literal ผ่าน 23; positive contract 12turns

**จุดใน Flow:** trusted history → state scope → follow-up operation

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

servercommon ปิด legacyrequest_plan โดยตั้งใจแต่เก็บ common_read_state SF006typed_common_state มี PCservices และ relationedges6 อุปกรณ์ แต่คำว่าอุปกรณ์ไม่ผ่าน field/coverageguard ทำให้ไม่มีสาระตอบ

**หลักฐานที่พบ**

PC มีอะไรบ้าง→อุปกรณ์: state ไม่ได้หาย แต่ requestedfields เลือก specifications/usage และ unresolved_query_clause จึง outerveto

**สิ่งที่ควรตอบหรือควรทำแทน**

รับ shortreply ในบริบทที่แยก ambiguity ได้แล้ว แล้วทำ equipment-listprojection ของ scope เดิม ไม่ถามเกม/ราคาใหม่หรือทิ้ง target โดยไม่มีเหตุ

**แนวแก้ที่รักษาข้อมูลจริง**

ผูก offeredneed/pendingselection กับ canonicaloperation ตรวจ deliveredstate/revision และปรับ shortoperationcontract ให้ตรงกับ fullquestion

**วิธีตรวจหลังแก้**

2–5turns เลือกชื่ออย่างเดียว/all/another/negative/cancel/changeaudience และไม่ inherit เมื่อเปลี่ยนเรื่อง; HTTP และ engine ต้องรายงานแยก

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/web_api/server.py :: do_POST](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/web_api/server.py:477)
- [app/knowledge/common/dialogue.py :: resolve_state](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/dialogue.py:34)
- [app/knowledge/common/equipment_bridge.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/equipment_bridge.py:6)

### P19 — Qualification และ unknown policy ต้องไม่ถูกแทนด้วยคำตอบใกล้เคียง

**ลำดับ/สถานะหลักฐาน:** P1/ข้อมูล; C: code+fixture; D:การบอก unknown บางข้อถูกต้อง

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** specific_unconfirmed_request12methods;2 requests ในกลุ่มหลักนี้

**จุดใน Flow:** profile/task ownership → confirmed or unknown source

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

สลิปผิด≠ยืนยันตัวตนผิด≠ยอดเงินผิด นำอุปกรณ์ส่วนตัวใช้≠ให้ศูนย์เตรียมอุปกรณ์ การคล้ายคำไม่ให้ย้ายอำนาจ source หรือทิ้ง negation

**หลักฐานที่พบ**

R87fixture เพิ่ม policy ยอดเงินแล้วอ่าน V1/V2/withdraw ได้ แต่ productionsnapshot ยังไม่ใช่การอนุมัตินโยบายใหม่นั้น

**สิ่งที่ควรตอบหรือควรทำแทน**

ถ้า facts เฉพาะไม่มีให้บอกว่าไม่ยืนยันเรื่องนั้น ถ้ามี source ใหม่แล้วต้องไม่ติด oldunknowngate

**แนวแก้ที่รักษาข้อมูลจริง**

ใช้ typed task/subject/ownership/context/qualifier bindings และ current-source-check ก่อน unconfirmed; yes ยืนยันหัวข้อไม่ใช่อนุมัติ facts

**วิธีตรวจหลังแก้**

slip/identity/amount/personal/competition เงื่อนไขใกล้กัน newpolicyrevision และ withdrawal ไม่คืนค่าจาก history

**ต้องใช้มนุษย์หรือไม่**

โค้ดทำเอง; นโยบายที่ยังไม่มีต้อง owner หรือ source จริง ไม่ใช้ fixtures เป็น policy ศูนย์

**Source code:**

- [app/knowledge/common/qualified_reply.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/qualified_reply.py:1)
- [app/knowledge/common/unconfirmed_request.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/unconfirmed_request.py:1)
- [app/knowledge/common/legacy_intent_bridge.py :: source_for_need](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/legacy_intent_bridge.py:48)

### P20 — ภาษาอังกฤษ: metadata, ค่าที่ขาด, proper names และคำแปลต้องแยกกัน

**ลำดับ/สถานะหลักฐาน:** P1/ข้อมูล; C:scanknownvalues และ flags; H:Thai-characterflag ไม่เท่ากับแปลผิด

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** agent_translated486 records;metadata missing116;knownlocalizedobjects ไม่มี en11;Thai-in-en32 objects;Englishanswerflag512 requests

**จุดใน Flow:** localized source values → English rendering

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

116 คือ record-levelstatus ไม่ใช่จำนวน record ที่ไม่มี English ทั้งหมด 11actualmissing อยู่ bindingsectionMarioKartLive บางส่วน Thai ชื่อรายการ/หน่วยอาจติด flag แม้ไม่ใช่ประโยคที่ต้องแปล ส่วน clausetranslation อีกสำนวนทำให้ literalfail ได้

**หลักฐานที่พบ**

DATA_INVENTORY เก็บทุก missingpath และ en_thai_paths; Tekkenetiquette มี semantic ใกล้เคียงแต่ถ้อยคำไม่ตรง oracle

**สิ่งที่ควรตอบหรือควรทำแทน**

อ่าน Englishsource ที่ผูก revision และรักษาตัวเลข เงื่อนไข negation ปุ่ม/ชื่อเฉพาะ ถ้ายังไม่ครบให้บอก partial/translationpending ตามขอบเขต

**แนวแก้ที่รักษาข้อมูลจริง**

เติมเฉพาะ 11 ค่าที่มีต้นฉบับ, review32flags เป็นชื่อเฉพาะหรือ prose, ทำ clauseequivalence checks แต่ไม่ทิ้ง literalcriteria เดิม และไม่เปลี่ยน agenttranslated เป็น owner-reviewed จากคะแนน

**วิธีตรวจหลังแก้**

TH↔ENsamefact parity, amounts/dates/negation, controlbuttonidentity, names/mixedlanguage และ missinglocalizednestedobjects

**ต้องใช้มนุษย์หรือไม่**

แปลและตรวจตัวเลขทำเอง; factual/translationreview โดย owner ไม่อ้างว่าเกิดแล้ว

**Source code:**

- [app/knowledge/common/answer.py :: text](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:50)
- [app/knowledge/common/translation.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/translation.py:1)
- [app/knowledge/common/registry.py :: validate](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py:62)

### P21 — Output ยังเผยชื่อ field ภายในหรือ label ที่ไม่ช่วยตอบคำถาม

**ลำดับ/สถานะหลักฐาน:** P2; C:คำตอบจริง; H:ต้องแยก UIdebug กับ body

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** ตัวอย่าง VR Service/platform/playtime/bookingoccupancy และ Zelda ถาม title

**จุดใน Flow:** projection → human-readable answer

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

schemafield ใช้สร้าง form/LLMplan ได้ แต่ไม่ใช่รายการตัวเลือกที่ผู้ใช้ต้องรู้จักเมื่อ task ชัด citationtitle ถูกเปลี่ยนเป็น draftgeneric ก็ช่วย provenance ระดับ mode แต่ไม่ได้อธิบาย source หัวข้อจริงทั้งหมด

**หลักฐานที่พบ**

VRpermissioncase ตอบ menufield แทนสิทธิ์เข้าใช้;Zelda เกมอะไรตอบ“ชื่อเกมอย่างเป็นทางการ?”

**สิ่งที่ควรตอบหรือควรทำแทน**

ตอบข้อเท็จจริงที่ถามด้วยภาษาผู้ใช้ หากต้องถามเพิ่มให้ถาม slot ที่มีผลต่อคำตอบ ไม่ถาม fieldtechnical

**แนวแก้ที่รักษาข้อมูลจริง**

แยก presentationcontract จาก catalog/schema ใช้ domaincaption และ scope/partial explanation พร้อมแหล่งอ้างอิงที่ติดตามได้; debug อยู่ส่วน debug

**วิธีตรวจหลังแก้**

ถามกว้าง/เฉพาะ/all/brief ทั้งสองภาษา ต้องไม่มี opaqueID/fieldtechnical ใน mainanswer เว้นแต่ user ขอ debug

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/rendering.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/rendering.py:1)
- [app/knowledge/common/answer.py :: title](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:61)

### P22 — Validation/score ดูดีไม่ได้รับรองว่าเข้าใจเจตนาถูก

**ลำดับ/สถานะหลักฐาน:** P1 ด้านการวัด; C:โค้ดและ counts

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** confidence.8 พบ 10,969 requests;uncalibratedflag15,892 requests

**จุดใน Flow:** finish validation → confidence/status interpretation

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

common finish ให้.8 คงที่สำหรับ answer/list ส่วน schema/evidence ตรวจ field ที่เลือก ไม่ตรวจว่าควรเลือก field นั้นตั้งแต่แรก Finalsafeclarification อาจ validTrue หลัง veto คำตอบที่ผิด

**หลักฐานที่พบ**

fieldplanner schemaTrue แต่ finalFalse ได้; old_build_result หลัง veto กลับ validTrue พร้อม warnings; migrationtrace1.0 คือเลือก profile ไม่ใช่ factual100%

**สิ่งที่ควรตอบหรือควรทำแทน**

แยก execution validity, schema validity, source support, intent/task coverage, semantic correctness และ approval status

**แนวแก้ที่รักษาข้อมูลจริง**

เพิ่ม per-need coverage/unansweredneeds/counterevidence output contract ไม่เอา defaultconfidence ไปปรับ ranking/โชว์เปอร์เซ็นต์ความถูกต้อง

**วิธีตรวจหลังแก้**

wrongfieldbutknownsource,correctfieldbutexpired,correctcitationwronggame,safeclarification,unverifiedtranslation ต้องให้สถานะแยก

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/answer.py :: finish](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:964)
- [app/pipeline/engine.py :: _build_result](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/engine.py:4499)

### P23 — Model transport, JSON/schema, binding และคำตอบต้องวัดแยก

**ลำดับ/สถานะหลักฐาน:** P0 เฉพาะล่ม/P1 คุณภาพ; C:calllogs และ audit

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 4,412HTTPattempts;4,376transportobservations;36TimeoutErrors;31 requests ถูกจัด primarytransportfailure

**จุดใน Flow:** model admission → HTTP → body/parse → semantics

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

LLMON เป็นสิทธิ์ให้เรียก ไม่ใช่ทุกคำถามต้องเรียก HTTPobserver บันทึกสำเร็จเมื่อ urlopen คืน response ไม่ใช่รับรอง body/schema/answer ทั้งก้อน แต่ planner มี body/parse/semantic audit แยก

**หลักฐานที่พบ**

จำนวน schemaacceptedaudits4,206 ไม่เท่ากับ 4,206 คำตอบถูก; จำนวน call กับ requests ต่างกันเพราะ request อาจมีหลาย call

**สิ่งที่ควรตอบหรือควรทำแทน**

ตรวจ servedmodel+จริง generationpreflight แล้วเก็บ phasefailure ราย call อธิบาย fallback โดยไม่สลับ OFF เงียบๆ

**แนวแก้ที่รักษาข้อมูลจริง**

root-cause ตาม transport/read/schema/binding/semantics และ deadline ไม่เพิ่ม alias หรือแก้ facts เพื่อรักษาคะแนนเมื่อติดต่อโมเดลไม่ได้

**วิธีตรวจหลังแก้**

available/refused/permission/timeout/malformedJSON/schemawrong/bindingwrong/semanticwrong ต้องแยกและ preserverawresult

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้ในสภาพเครื่อง; ไม่สรุป network permission เป็น policy ข้อมูลผิด

**Source code:**

- [app/pipeline/llm_health.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/llm_health.py:1)
- [app/knowledge/common/planner.py :: _plan_fields_batch](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py:100)
- [app/knowledge/common/entity_search.py :: select](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py:89)

### P24 — Bug ฝั่งเดิม: ownership_blocked ไม่อยู่ใน scope ของ retrieve_curated

**ลำดับ/สถานะหลักฐาน:** P0 ใน legacy snapshot; C:exception2692 และตำแหน่ง code

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** legacyONNameError2,692 requests + harness timeout2 = exceptions2,694

**จุดใน Flow:** legacy curated retrieval trace construction

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

ใช้ ownership_blocked ที่ return ของ retrieve_curated แต่ assignment ที่พบอยู่ใน retrieve_competition_fact_cards คนละ function จึงล้มเมื่อเข้า branch นั้น ไม่ใช่ LLM ไม่รู้คำตอบ

**หลักฐานที่พบ**

R65resultsexception และ R90exceptiontypes ตรวจตรงกัน; strictscore สูงของเดิมไม่ลบล้าง bug นี้

**สิ่งที่ควรตอบหรือควรทำแทน**

ทุก branch ต้องมี ownershipaudit ที่ถูก scope และจริงตาม guard ไม่ใช่ใส่ตัวแปรว่างเพื่อซ่อนข้อผิดพลาด

**แนวแก้ที่รักษาข้อมูลจริง**

หากนำ legacyhelper กลับมา ใช้ pureinterpretation ที่จำเป็น ไม่คัดลอก retrieval ทั้งชุด; แก้ auditflow พร้อม testownerblocked/unmanaged/nohitsbranch ในงานซ่อมภายหลัง

**วิธีตรวจหลังแก้**

branchcoverage ทั้งมี/ไม่มี ownershipblock,sourceconflict,emptyhits และ lexicalfallback; ไม่ rerunlegacy ใหญ่เพื่อไล่คะแนนในงานเอกสารนี้

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้ แต่รอบนี้ยังไม่แก้โค้ดเก่าหรือโค้ดใช้งาน

**Source code:**

- [app/pipeline/retrieval.py :: retrieve_curated](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/retrieval.py:696)
- [app/pipeline/retrieval.py :: retrieve_competition_fact_cards](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/retrieval.py:601)

### P25 — ข้อมูลหมดอายุ: คะแนนเดิมดีขึ้นได้จากการตอบค่าที่ระบบใหม่ไม่ควรยืนยัน

**ลำดับ/สถานะหลักฐาน:** ข้อมูล/Oracle; C:18ratesexpiry ชัด; D:refusalcurrentprice อาจถูกต้อง

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** not_current1,113 requests;500 อยู่ primaryvaliditydiagnostic

**จุดใน Flow:** source validity → answer status → historical expected

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

referenceOct2026 อยู่หลัง expiry ก่อน 1Apr2026 oracle บางข้อยังคาดบาท/ฟรีหรือราคาเดิม การเทียบ correctness ต้องดูวันมีผลและหน่วย ไม่ใช้การมีตัวเลขเป็น proof

**หลักฐานที่พบ**

VRGeneralStudentcase ใหม่ระบุ endtimestamp ตรง source เดิมคืน 190 จากตารางเก่าตามคำถามที่มี duration ซ้อน

**สิ่งที่ควรตอบหรือควรทำแทน**

ห้ามใช้ราคาเก่าเป็น current โดยไม่มีหลักฐาน หาก user ถามราคาประวัติในช่วงที่มีผลจึงตอบแบบ historicalscope ได้

**แนวแก้ที่รักษาข้อมูลจริง**

แยก historicalvscurrentoracle และ validitygroundtruth เก็บเกณฑ์เก่าเป็น compatibilityresult ไม่ลบ enddate/ย้าย clock เพื่อให้ผ่าน

**วิธีตรวจหลังแก้**

ก่อน/ตรง/หลัง expiry;no-current-rate;historicalpriceexplicit;unknownvalidity และ packageaudienceunits

**ต้องใช้มนุษย์หรือไม่**

logic/analysis ทำเอง; ราคาปัจจุบันหรือวันมีผลใหม่ต้อง source ที่ยืนยัน

**Source code:**

- [app/knowledge/common/answer.py :: active](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:75)
- [app/knowledge/common/billing.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/billing.py:1)

### P26 — Draft preview ไม่ใช่ production authority หรือ owner approval

**ลำดับ/สถานะหลักฐาน:** P0 ก่อน cutover; C:store/previewprofile/metadata

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 602heads;581validity unknown;5conflictedfields;R88 ไม่มี approval/publication ใหม่

**จุดใน Flow:** owner save/preview → approve/publish → runtime reader

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

MigratedView อ่าน latestdraftheads และตั้ง production_publication_verifiedFalse ขณะที่ normalstore อ่าน activepublishedrelease การเห็นข้อมูลใหม่ใน preview จึงไม่เท่ากับปล่อยใช้จริงได้ด้วย approval เดิม

**หลักฐานที่พบ**

time-sensitive publish ต้อง knownvalidity และ trustreview; forecastallunknown581 ไม่ใช่ 581 records ต้อง owner กรอกทุกอย่าง เพราะบาง kind ไม่ต้อง time-sensitive และ fieldsoptional

**สิ่งที่ควรตอบหรือควรทำแทน**

แยก mode ให้ชัดและเลือก cutovercontract ที่รักษา review/revision/publish semantics ไม่ปล่อย draft หรือ fixture เป็น ownerpolicy

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ readinessreport ตาม required/publish_core ต่อ kind sourceauthority/translationhash/relations ไม่ผ่อน validator เพื่อผ่าน batch

**วิธีตรวจหลังแก้**

draftnotvisibleinpublished,revisioneditinvalidatesapproval,withdraw/rollback,currentepochandsource pointertests โดยไม่แก้ ownerfacts

**ต้องใช้มนุษย์หรือไม่**

โค้ดและ readiness ทำเอง; factualapproval/policyconfirmation จริงไม่ทำแทนเจ้าของ

**Source code:**

- [app/knowledge/common/migrated_view.py :: snapshot](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/migrated_view.py:25)
- [app/knowledge/common/store.py :: approve](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/store.py:132)
- [app/knowledge/common/store.py :: publish](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/store.py:167)

### P27 — Data-only extensibility ยังจำกัดด้วย vocabulary, relation และ runtime contract

**ลำดับ/สถานะหลักฐาน:** P1; C:สัญญาในโค้ด; R:ไม่อ้างว่า newrecord ทุกประเภทถูกทดสอบแล้ว

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** fixtureR87growth19 checks+rule7 checks ไม่ใช่ทุก kind/paraphrase

**จุดใน Flow:** owner new record → discover → plan → render

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

เพิ่ม record ใน schema เดียวกันอาจไม่ต้องแก้ code แต่ถ้า operation/fieldmeaning/relationships/newgameedition ไม่เข้า resolver หรือ adapter ก็ยังตอบไม่ได้ ข้อมูลอย่างเดียวไม่สอน taskgrammar ใหม่โดยอัตโนมัติ

**หลักฐานที่พบ**

newAurorapackage ราคา/อุปกรณ์ใน fixture ผ่าน แต่ไม่ทดสอบ liveproductmapping ใหม่หรือ allpropositions ของทุกหมวด

**สิ่งที่ควรตอบหรือควรทำแทน**

เพิ่มข้อมูลชนิดที่รองรับแล้วต้องเข้าสู่ candidate/schema/renderer ตาม registry เดียวกัน โดยไม่แก้ alias ต่อคำถามหรือใช้ sourcefixture แทนจริง

**แนวแก้ที่รักษาข้อมูลจริง**

taskregistry/schema-description/profilemetadata และ relation-awareprojection ร่วมกันสำหรับ knownkinds; schema ใหม่จริงต้องมี version/migration/rendererdecision ชัด

**วิธีตรวจหลังแก้**

newrecord-only,update/withdraw,newname,heldoutquestions ทุกหมวดและ emptyrelatedsource ต้องตรวจ discoverability+answercoverage ไม่ใช่ save ได้อย่างเดียว

**ต้องใช้มนุษย์หรือไม่**

โค้ดทำเอง; เนื้อหานโยบายใหม่ต้อง source

**Source code:**

- [app/knowledge/common/registry.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py:1)
- [app/knowledge/common/entity_search.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py:1)
- [app/knowledge/common/relations.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/relations.py:1)

### P28 — คะแนน strict ถูกผูก route/mode/source IDs เดิม

**ลำดับ/สถานะหลักฐาน:** Compatibility; C:counts และ same-checkerpairedresults

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 31,649gradesprotocol-only;10,606 requests อยู่ primaryprotocol-onlynoliteralfailure

**จุดใน Flow:** result protocol → historical grader

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

common ใช้ knowledge/common_read/common_answer และ typedrecordIDs ต่างจาก service_fee/rules/competition modes เดิม แม้ body บางข้อผ่าน literal ก็ strictfail บางข้อไม่มี positivecontract จึงยังบอกไม่ได้ว่าตอบครบ

**หลักฐานที่พบ**

legacystrict76.33%กับ new9.02%; samepositivechecker ต่างกัน 94.41%กับ 72.10% แสดงว่าปัญหาไม่ได้มีแค่ protocol แต่ก็ห้ามเรียก strict9%ว่า accuracy9%

**สิ่งที่ควรตอบหรือควรทำแทน**

รายงาน compatibility, positivecontent, taskoutcome, source lineage และ humanreview แยก ไม่เปลี่ยน expected ให้เข้ากับ output ใหม่เพียงเพื่อคะแนน

**แนวแก้ที่รักษาข้อมูลจริง**

สร้าง adapter ของ evaluator ที่อ่าน typedoutcome/source lineage โดยเก็บ strictlegacycriterion ไว้ และทบทวนความหมายของ category/status เฉพาะที่อ้างได้

**วิธีตรวจหลังแก้**

body เดียวกัน route ใหม่ต้อง content เท่าเดิมแต่ strict ต่างได้; wrongprice/wronggame ต้องยัง fail แม้ route ถูก

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/answer.py :: finish](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:964)
- [app/pipeline/engine.py :: _build_result](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/engine.py:4499)

### P29 — Literal checker มีทั้ง false mismatch และเงื่อนไขที่อ่อนเกินกว่าจะยืนยันคำตอบถูก

**ลำดับ/สถานะหลักฐาน:** P1 ด้านการวัด; C:ตัวอย่างคำตอบคู่; H:ยังไม่คำนวณ semanticaccuracy แท้

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** positive24,909 grades; noadditional literal 23,714 grades

**จุดใน Flow:** expected contract → pass/fail interpretation

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

คำแปลคนละสำนวน/ชื่อ service แทน zone อาจ fail แม้ relatedfacts ถูก ขณะเดียวกันแค่มีคำหรือ marker บางคำอาจ pass ทั้งที่ scope ยังไม่ครบ ตัวตรวจ wording ไม่ใช่ semanticjudge ที่รับรอง facts

**หลักฐานที่พบ**

ปุ่มยิงกดอะไร:ทั้งคู่ขอชื่อเกม แต่ใหม่ไม่มีหนึ่งใน marker“ยังไม่แน่ใจ/ขอ/ไม่มี”ตาม oracle จึง fail; TekkenEnglishclauses อีกสำนวนเช่นกัน

**สิ่งที่ควรตอบหรือควรทำแทน**

เกณฑ์ควรตรวจ entity/requiredpropositions/qualifiers/numbers/negation/citations/out-of-scopeextras พร้อม source ไม่ยึด string อย่างเดียวหรือให้ LLMjudge แทน truth

**แนวแก้ที่รักษาข้อมูลจริง**

เก็บ rawliteralscore เดิม เพิ่ม structuredneed/source contract และ semanticreview ชั้นต่างหากพร้อม uncertainty ไม่เลื่อนคะแนนใหม่มาแทนเดิมเงียบๆ

**วิธีตรวจหลังแก้**

meaning-preservingparaphrase ต้องแยกจาก meaning-changingnumber/negation/edition และคำตอบยาวที่มี keyword แต่ wrongtask ต้องไม่ถือครบ

**ต้องใช้มนุษย์หรือไม่**

ทำตัวตรวจและ analysis เอง; semanticreview/factualapproval ยังไม่อ้างว่ามนุษย์ทำครบแล้ว

**Source code:**

- [tools/eval_contract_v2.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/tools/eval_contract_v2.py:1)
- [tools/run_competition_contract_r27.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/tools/run_competition_contract_r27.py:1)

### P30 — ชุดเฉพาะจุดผ่าน ไม่ได้แทน distribution ของ full corpus

**ลำดับ/สถานะหลักฐาน:** การทดสอบ; C:ชุดคำถาม/จำนวน bridges และ fullscores

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** R87web55/55; R88positive17,960/24,909; ไม่ใช่ตัวชี้วัดชุดเดียวกัน

**จุดใน Flow:** regression selection → coverage claim

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

ชุด 55 เน้นปัญหาที่เพิ่งแก้และกรณีที่รู้ผล Full มี wrapper,typo,operation,domain และ oracle หลากหลายกว่า ความสำเร็จใน fixedcases ไม่แปลว่าระบบ generalize ทุกหมวด

**หลักฐานที่พบ**

bridgeprotest2/summary13/rental5finalmethod ใน full ขณะที่หลายพันคำถามยังไป exact/ordinaryreader/clarification paths

**สิ่งที่ควรตอบหรือควรทำแทน**

ระบุ coverage matrix ตาม task/language/style/needs/sourcekind และใช้ heldoutcases ที่ไม่เลือกจากข้อที่รู้ว่าผ่าน

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ targetedrepair→nearneighbors→heldoutstratified→full ภายหลังตามคำสั่ง ไม่เพิ่ม alias เฉพาะข้อสอบหรือรันซ้ำจนเลือก answer ที่ผ่าน

**วิธีตรวจหลังแก้**

ตรวจ schema/intent/source/equivalence และ strongnegative พร้อม pairedbeforeafter จากผลเดิม ไม่อ้าง 55/55 เป็น productionaccuracy

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/legacy_intent_bridge.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/legacy_intent_bridge.py:1)
- [app/knowledge/common/competition_bridge.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/competition_bridge.py:1)

### P31 — Root cause บางข้อระบุไม่ได้จาก final answer อย่างเดียว ต้องรักษา rejected plan และ phase timing

**ลำดับ/สถานะหลักฐาน:** P1 ด้านวินิจฉัย; C:loggingpaths/timeoutcases; R:instrumentation gaps บางช่วง

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** watchdog2 requests ไม่มี finalworkerresult; no_common_method4,691 ไม่เท่ากับ alllosthistory

**จุดใน Flow:** trace/audit/progress → diagnosis

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

outerveto อาจทำให้ top-levelplan หายแต่ยังมี rejected_candidate; watchdog อาจไม่มี modelcall ที่กำลังค้างมาถึง parent จึงไม่ควรนับ model_calls[]ว่าไม่ได้พยายามเรียก; composite/recursiveplans ทำให้นับ audit ซ้ำได้

**หลักฐานที่พบ**

SF006trace ยืนยัน PCscope+relations; foodwatchdog28s ไม่มี body จึงยังไม่ชี้ว่า source ขาดหรือโมเดลเป็นต้นเหตุ

**สิ่งที่ควรตอบหรือควรทำแทน**

เก็บ stageenter/exit, queuewait,selected/rejectedcandidate, per clauseneeds, source/revision, request/call IDs และ finaldelivery โดยไม่นำข้อมูลองค์กรที่ไม่จำเป็นมารั่วใน chat

**แนวแก้ที่รักษาข้อมูลจริง**

เพิ่ม structuredphaseobservability ที่ไม่แก้ decision และ analysis ให้นับ call/request/grade/auditevent แยก

**วิธีตรวจหลังแก้**

inducedparserfailure/modeltimeout/workerrestart/cancellation ต้องเก็บ phase เดิมครบและไม่ retry คำตอบแล้วทับผลครั้งแรก

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/pipeline/migrated_chat.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py:13)
- [app/web_api/pipeline_supervisor.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/web_api/pipeline_supervisor.py:1)
- [app/knowledge/common/planner.py :: _plan_fields_batch](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py:100)

### P32 — Latency และ concurrency มี queue หลายชั้น ไม่ใช่เปิด LLM แล้วตอบพร้อมกันได้ทุกคำขอ

**ลำดับ/สถานะหลักฐาน:** P1performance; C:config/admission/elapsed; R:ไม่ใช่ loadcapacity รับรอง

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** R88worker2/modelslot1; bulk8,833.08s รวม grading; watchdog28s/global18s

**จุดใน Flow:** web admission → worker → model gate → HTTP

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

typed/CPU งานบางส่วนขนานได้ แต่โมเดลถูกจำกัด 1slot เพื่อทรัพยากรเครื่อง queuewait กิน deadline ก่อน generation ทำให้ request ที่รออาจไม่มี budget พอ FieldplannereventZelda รอ 5.85s แล้วทำงาน 3.46s

**หลักฐานที่พบ**

R64 ใช้ evalmatchingoptimizations ต่างจาก runtime; R88core คำถามเดี่ยว+batchworkers ไม่ใช่การวัดเวลาผู้ใช้หนึ่งคนหรือจำนวน userproduction

**สิ่งที่ควรตอบหรือควรทำแทน**

รายงาน queue/service/total และ p95/p99 ตาม cohort จริง ไม่ใช้ HTTPelapsed ของ observer ที่หยุดที่ headers แทนเวลารวมทุก phase

**แนวแก้ที่รักษาข้อมูลจริง**

ลด LLM ที่ถูกเรียกแต่โดน semanticreject ซ้ำ, cache เฉพาะแผนที่ invalidate ตาม schema/source, typedtaskfastpaths และ admission/deadlinecontract; ไม่เพิ่ม threads ไม่จำกัดบน GPU เดิม

**วิธีตรวจหลังแก้**

หลัง correctness คงที่ค่อยวัด single/concurrentmix โดยแยก warm/cold และ timeout/gate/content ไม่ใช้ fullbatch เป็น SLA

**ต้องใช้มนุษย์หรือไม่**

ทำโค้ด/การวัดเองได้; ไม่ปรับทรัพยากรระบบหรือซื้อบริการโดยอนุมาน

**Source code:**

- [app/pipeline/model_admission.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/model_admission.py:1)
- [app/pipeline/request_deadline.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/request_deadline.py:1)
- [app/pipeline/llm_health.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/llm_health.py:1)

### P33 — Unknown/conflicted fields ไม่ใช่หลักฐานว่าข้อมูลหายทั้งหมด และบางข้อไม่ต้องถามคนใหม่

**ลำดับ/สถานะหลักฐาน:** ข้อมูล/การตัดสิน; C:inventory และ sourceconflictpaths

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** known2,951/unknown1,431/conflicted5 fields; 5conflicts เป็น open_periods

**จุดใน Flow:** source readiness → task applicability

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

optionalmetadata ว่างกับข้อเท็จจริง required ที่ขาดมีผลต่างกัน record มี fieldunknown ไม่ได้แปลว่าตอบอะไรไม่ได้; ข้อมูลที่ผู้ใช้ยืนยันใน session แล้วควรใช้เป็นหลักฐานเดิม ไม่ถามซ้ำเพราะ migrationnote ยังเก่า

**หลักฐานที่พบ**

5scheduleconflictsnote ค้างเรื่อง open/bookable;12–13bookability และ VRoccupancy มี humanconfirmation เดิมอยู่แล้ว

**สิ่งที่ควรตอบหรือควรทำแทน**

ทำ task-levelmissingfacts inventory ว่าอะไรบล็อกคำถามใด และถามเฉพาะข้อที่ต้องตัดสินใหม่จริง

**แนวแก้ที่รักษาข้อมูลจริง**

แยก requiredtopublish/requiredtoanswer/optional, มี provenance ของ confirmation เดิม และระบุ unknown ที่ไม่กระทบคำถามไม่ต้องถาม

**วิธีตรวจหลังแก้**

fieldoptionalunknown ต้องยังตอบ needknown ได้; requiredconflict ห้ามเลือกข้างเอง; confirmation เดิมไม่ถูกลืม

**ต้องใช้มนุษย์หรือไม่**

ทำ inventory/mapping เอง; businessfact ที่ไม่มี source จริงค่อยขอผู้รับผิดชอบ

**Source code:**

- [app/knowledge/common/registry.py :: validate](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py:62)
- [app/knowledge/common/answer.py :: effective](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py:78)

### P34 — Archive comparison ไม่ใช่ controlled experiment ของ schema อย่างเดียว

**ลำดับ/สถานะหลักฐาน:** การวัดผล; C:hash/corpus/config ของ R64/R88/R89

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 20,554keys/55,811 grades ตรงกัน; dates/engine/data revisions ต่างกัน

**จุดใน Flow:** test provenance → causal conclusion

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

samechecker ช่วยเทียบคำตอบที่เก็บไว้ แต่ old/current มี validitypolicy,source602vs ข้อมูลเดิม,interpreter,LLMbudget,caching,referenceclock และ errorpaths ต่างกัน จึงไม่ยืนยันว่า JSONschema กลางทำให้แย่ลงด้วยตัวมันเอง

**หลักฐานที่พบ**

R89 ไม่มี modelcalls/requests ใหม่และตรวจ hash ชุดโจทย์; strict และ positive คนละความหมาย; ชุด native/HTTP เก่าคนละ surface กับ enginebulk ใหม่

**สิ่งที่ควรตอบหรือควรทำแทน**

สรุปได้ว่าระบบใหม่ตามผลเดิมไม่ทันตามเกณฑ์นี้ พร้อมชี้ causalmechanism จาก code/trace เฉพาะที่มีหลักฐาน

**แนวแก้ที่รักษาข้อมูลจริง**

เมื่อแก้ให้ใช้ frozenfacts/cohort/dates/tasks เดียวกันเท่าที่ปลอดภัย แยก compatibility/history/currenttruth; ไม่ทำ baseline ใหม่ถ้าผู้ใช้ไม่ขอ

**วิธีตรวจหลังแก้**

coverage/hash/no-duplicate/gradealignment/sourceimmutability และ denominator ทุกตารางต้องตรง

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้

**Source code:**

- [app/knowledge/common/migrated_view.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/migrated_view.py:1)
- [app/pipeline/engine.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/engine.py:839)

### P35 — ติดตั้ง R78 แล้ว ไม่ได้แปลว่า portable package/เครื่องอื่นมีการแก้ล่าสุดครบ

**ลำดับ/สถานะหลักฐาน:** P1 ก่อนแจก; R:ขอบเขตที่ยังไม่ได้ยืนยัน ไม่ใช่ข้อผิดพลาดที่วัดแล้วใน R88

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** R87 ติดตั้ง 6codefiles ใน R78; R88 เป็น snapshot ไม่ได้ rebuildportable

**จุดใน Flow:** package manifest → runtime config → real device

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

bridge ใหม่ใช้ legacygrammar/routingconfig เป็น dependency ถ้าเอาเฉพาะ commonfiles ไปโดยไม่มี modules/data/rules ที่ต้องใช้ อาจหา intent ไม่ได้หรือ importfail ส่วน Ollama/model/download และ transportmode ต้องตรงเครื่องปลายทาง

**หลักฐานที่พบ**

R87report ระบุไม่ rebuildpackage; R88 ตรวจ codehash กับ snapshot ไม่ใช่ทดสอบ cleanWindows/อีกเครื่อง

**สิ่งที่ควรตอบหรือควรทำแทน**

แจก package ที่มี exactbuild manifest/config/data/modeloption ชัด และ health บอก version/profile/model/knowledge source จริง

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ reproduciblepackagingdependencyinventory และ startupdiagnostics ภายหลัง ไม่เปลี่ยน productionlaunchers ในงานเอกสารนี้

**วิธีตรวจหลังแก้**

clean-copy offline/online-model variants,relativepaths,portinuse,modelmissing,sourceupdates และ same-questioncanary

**ต้องใช้มนุษย์หรือไม่**

เตรียมโค้ด/แพ็กเกจทำเองได้ภายหลัง; การติดตั้ง/เผยแพร่จริงตาม scope ที่ได้รับอนุญาต

**Source code:**

- [app/knowledge/common/build_info.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/build_info.py:1)
- [app/web_api/server.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/web_api/server.py:1)

### P36 — Input guard ตรวจ layout/repeat ได้บางชนิด แต่ไม่ได้แก้เจตนาทั้งประโยค

**ลำดับ/สถานะหลักฐาน:** P1 สำหรับ typo; C:guardmetrics และ stageorder

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** 500layoutcases ผ่าน 500;repeatdetect471/500 ไม่ใช่ accuracytypo ของทั้งบอต

**จุดใน Flow:** input quality guard → recovery → semantic task

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

guard บอกว่าข้อความอาจผิดหรือเตือนเบิ้ล แต่ common ยังต้อง parseoperation ต่างหาก ตัวเลขรุ่น/เครื่องต้องป้องกันไม่ลบซ้ำผิด เช่น PC11 ไม่ใช่ PC1; ไทยไม่มีช่องว่างและ combiningmarks ทำให้ edit ตำแหน่งเดี่ยวไม่พอในหลาย cue

**หลักฐานที่พบ**

Zeldatasktypo แม้ชื่อชัดยัง reject; displaywarning ที่พบ repeat ไม่ควรแปลว่าคำตอบเลือก intent ถูกแล้ว

**สิ่งที่ควรตอบหรือควรทำแทน**

แบ่ง detection,recovery,taskselection,answercorrectness เป็นคนละ metric และใช้ context เฉพาะที่เชื่อถือได้ช่วยจำกัด candidate

**แนวแก้ที่รักษาข้อมูลจริง**

แชร์ language-awareerrorchannels และ taskvocabulary พร้อม margin/negation/numberprotection ไม่ reduceallrepeats หรือใช้ neighbor ทุกตำแหน่งโดยไม่ดู context

**วิธีตรวจหลังแก้**

Thai/Englishmixedscript,diacritics,missing/repeatedchar,multipleworderrors,legitimateelongation,numericIDsandunknowntexts

**ต้องใช้มนุษย์หรือไม่**

ทำเองได้จาก source และรูปแบบภาษา; ไม่ใช้ case รายคำเป็น policy ใหม่

**Source code:**

- [app/core/runtime_input_quality_guard.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/core/runtime_input_quality_guard.py:1)
- [app/pipeline/preprocess.py :: preprocess_input](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/preprocess.py:120)

### P37 — Owner preview กับแชทจริงใช้ dispatcher/authority surface ต่างกัน

**ลำดับ/สถานะหลักฐาน:** P1 ก่อน cutover; C:callpaths ต่างกัน; R:ยังไม่วัด failure ทุกหมวดของ preview

**จำนวน/ขอบเขตที่เกี่ยวข้อง:** preview_answer เรียก CommonAnswerer ตรง; actualchat มี engine+migrated+serverstate/liveadapter

**จุดใน Flow:** owner form preview → production-like chat path

**เหตุที่เกิดและเหตุใดจึงตอบแบบนั้น**

preview อาจไม่มี productscope/greeting/livefallback/outercandidateveto หรือ persistentdelivery เหมือน webchat และ draftpreviewrelease มีโครงประกอบต่างจาก MigratedView บางส่วน การ preview ผ่านจึงไม่รับรองว่า fullchat ถามต่อ/เลือกข้อมูลเหมือนกัน

**หลักฐานที่พบ**

owner_server.preview_answer และ migrated_chat.answer เป็นสอง entrypoints ที่เห็นจาก source ไม่อ้างจำนวนข้อผิดโดยไม่มีการรัน

**สิ่งที่ควรตอบหรือควรทำแทน**

เลือก canonicalanswercontract เดียวกันหรือประกาศ scopepreview ให้ตรงความจริง พร้อม testconformance ระหว่าง preview/engine/HTTP

**แนวแก้ที่รักษาข้อมูลจริง**

ทำ thinadapter ใช้ snapshotprovider/dispatcher contract ร่วมกันโดยไม่แอบ publishdraft หรือเอา legacyfacts กลับมา

**วิธีตรวจหลังแก้**

newrecord/update/withdraw,sourceinvalid,qualified follow-up,livequery,unknownscope และ same-questionoutputcontract ข้าม surface

**ต้องใช้มนุษย์หรือไม่**

โค้ดและ conformance ทำเองได้; ไม่ให้ preview สร้าง ownerapproval แทนเจ้าของ

**Source code:**

- [app/knowledge/common/owner_server.py :: preview_answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/owner_server.py:17)
- [app/pipeline/migrated_chat.py :: answer](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py:13)

## 5. สิ่งที่ควรแก้ก่อนตามผลกระทบจริง

1. **Task semantic contract/recovery → field selection:** P01–P08/P12/P18 มีผลกว้างต่อคำถามที่ข้อมูลอยู่แล้วและถามเพิ่มผิดประเด็น
2. **Projection/completeness:** P09/P10/P13/P14/P21/P22 ให้ตอบเฉพาะสิ่งที่ขอพร้อม conditions/relatedfacts ครบ ไม่รับ broadplan ทุก field
3. **Observability/timeouts:** P23/P31/P32 เก็บ phasefailure ชัดและลด LLM ที่เรียกแต่ reject อย่างไม่จำเป็น ไม่ขยาย timeout เป็นวิธีแก้ความหมาย
4. **Data readiness ตามหลักฐาน:** P11/P15/P16/P20/P25/P26/P33 แก้ metadata/translation ที่ทำเองได้ แยก policy/validity ที่ต้อง owner; ไม่ถามซ้ำสิ่งที่ยืนยันแล้ว
5. **Evaluator/coverage:** P28–P30/P34 ทำคู่ strict กับ semantic/source contract ที่เข้มขึ้น เก็บข้อเก่าไว้ ไม่แก้ expected ให้รับคำตอบผิด
6. **Preview/deployment:** P27/P35/P37 เมื่อ core ถูกค่อยทำ conformance และ packagecutover; แก้ buglegacyP24 เฉพาะหากต้องใช้ branch นั้นจริง ไม่ดึง legacyfactfallback มาแทน

## 6. สิ่งที่ทำเองได้กับสิ่งที่ต้อง source เพิ่ม

ทำเองได้: shared normalization,task/fieldadapters,relation projection,qualified follow-up,LLMbinding/guard validation,source-lineage analysis,English11knownsectiontranslations,scoring/coverage/package manifest และตรวจ source ที่มีอยู่แล้ว

ต้อง source/ผู้รับผิดชอบเมื่อยังไม่มีจริง: ราคาปัจจุบันหลัง expiry,วันมีผลที่จำเป็นต่อ publication,จำนวนชั่วโมง half/full-day,เงื่อนไขมัดจำ/ยกเลิก/เหมารายชั่วโมง/หลายวัน,ความหมาย physicalopen ที่นอกเหนือ bookability ที่ยืนยัน และ rulebook/physicalcontrollerpolicy ใหม่ที่ source ไม่รองรับ

ไม่ต้องให้เจ้าของยืนยันซ้ำ:12–13 ไม่มีช่องจอง,VR30 นาทีกันชั่วโมงเต็ม,live สถานะเดิมที่ผู้ใช้ตรวจแล้วถูกต้อง ส่วน English ผ่าน automatedtest ไม่เปลี่ยนเป็น owner-reviewed เอง

## 7. ดัชนีและหลักฐานทุกกรณี

- [COMMON_FAILURE_INDEX_ALL.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/COMMON_FAILURE_INDEX_ALL.md) —18,824raw-failed requests พร้อม key/ภาษา/คำถาม/กลุ่ม/จำนวน grade ที่ไม่ผ่าน
- [LEGACY_FAILURE_INDEX_ALL.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/LEGACY_FAILURE_INDEX_ALL.md) —5,689 requests จาก legacyON ที่ไม่ผ่านอย่างน้อยหนึ่งเกณฑ์
- [ALL_FAILURE_REASON_TYPES.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/ALL_FAILURE_REASON_TYPES.md) —ใหม่ 620reasonstrings/เดิม 318reasonstrings เก็บครบ ไม่ตัดเหลือเฉพาะตัวอย่าง
- [DETAILED_METRICS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/DETAILED_METRICS.json) —stagecounts/planneraudits/data scan พร้อมหน่วยที่นับ
- [DATA_INVENTORY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/DATA_INVENTORY.json) —5conflicts/11missingENpaths/validity/readiness และ knownZeldafields
- [CODE_SYMBOLS.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/CODE_SYMBOLS.json) และ [ENGINE_SINGLE_BRANCHES.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/ENGINE_SINGLE_BRANCHES.json) —จุดอ้างอิงทุก symbol และ single-enginebranchindex
- [SOURCE_MANIFEST.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/SOURCE_MANIFEST.json) —hash ของ source ที่อ่าน; rawlogs และ knowledge เดิมไม่ถูกแก้

การตรวจรายละเอียดแต่ละคำถามให้ใช้ key ค้นใน R88 FAILURE_EVIDENCE.sqlite และ R65 evidence.sqlite ไม่ใช้ index กลุ่มอัตโนมัติเป็น rootcause ที่ยืนยันแล้วแทน trace/source
