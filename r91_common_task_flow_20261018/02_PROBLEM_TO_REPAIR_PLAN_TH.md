# วิเคราะห์ปัญหาและแผนแก้รายข้อ P01–P37

วันที่ 18 ตุลาคม 2026 — เป็นแผน ยังไม่ใช่รายการแก้เสร็จและไม่รันเทสใหม่ในรอบนี้

อ่านคู่กับ [Flow หลัก](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/01_PROPOSED_COMMON_FLOW_TH.md>); หลักฐานต้นทางคือ [R90 problem catalog](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/PROBLEM_CATALOG_REVIEWED.json>) และ [R90 casebook](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/05_CASEBOOK_TH.md>).

## วิธีอ่านหลักฐาน

C ในบันทึกเดิมหมายถึงมีหลักฐานจาก code/log/ผลที่บันทึก; R หมายถึงความเสี่ยงหรือขอบเขตที่ยังต้องพิสูจน์ ไม่ใช่ทุกข้อเป็น failure ที่นับแล้ว แต่ละ count ด้านล่างใช้หน่วยตามต้นทาง ห้ามบวก audit events/grades/requests/fields เป็นจำนวนคำถามผิดทั้งหมด

## ลำดับการแก้

| ลำดับ | ปัญหาที่เกี่ยว | เหตุผล |
|---|---|---|
| 1 | P01–P07, P12, P18, P36 | shared interpretation เป็นฐานให้หลายหมวดกลับมาตอบได้ |
| 2 | P08–P11, P14, P19, P22 | ความครบของคำตอบ ราคา เงื่อนไขและกติกามีผลต่อการใช้งานจริง |
| 3 | P13, P15–P16, P20–P21, P27, P33 | projection/time/language และ readiness รายงาน |
| 4 | P26, P37 และ P27 | owner workflow และ published path ต้องใช้ semantics เดียว |
| ประกอบทุกช่วง | P23–P25, P28–P32, P34–P35, P17 | แยก measurement/runtime/data risks และเตรียมส่งมอบ |

ลำดับนี้ไม่หมายถึงเลื่อนงานป้องกันข้อเท็จจริงผิดไปทีหลัง: validity, qualifier และ source-authority gates ต้องคงอยู่ตั้งแต่เริ่ม ไม่มีการผ่อน guard ระหว่างรอพัฒนา

## P01 — เปลี่ยน data format พร้อมเปลี่ยนเส้นทาง interpreter โดยไม่ย้าย behavioral contract ครบ

**ตำแหน่ง:** engine entry → migrated dispatcher  
**หลักฐาน/ข้อจำกัด:** C: ยืนยันลำดับจากโค้ด; ผลกระทบทั้งระบบต้องแยกรายกรณี  
**ตัวเลขที่รายงานไว้:** ทั้ง20,554requestsเข้าprofileใหม่; ไม่ใช่จำนวนคำตอบผิด20,554

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

Engineใหม่ return migrated_answer ก่อน legacy request focus, cue preflight, typed fee/compound และ _answer_single ที่มีpreprocess/handlers จึงไม่เกิดความสามารถเดิมจากการมีข้อมูลเท่านั้น R87นำกลับบางส่วนแต่ยังไม่ใช่ parityทั้งต้นไม้

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R87finalbridgesรวม202requests: intent16, rental5, equipment166, overview13, protest2; ชุดย่อย55/55ไม่ได้พิสูจน์ว่ากลุ่มอื่นผ่านด้วย

### พฤติกรรมที่ควรได้

แยกการตีความงานออกจากfacts provider ให้task contractเดิมที่ยังถูกต้องส่งต่อไปcurrent common recordsได้ โดยรักษาowner source/validityใหม่

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **A→B**

ทำ inventory ของ early returns และ legacy handlers; แต่ละ handler ระบุ task contract แล้วแยก interpreter ออกจาก source loader ก่อนต่อเข้า common dispatcher

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำadapterชั้นtask/operation/slots/qualifiers ไม่เรียกlegacy answer loader; map old output contractsไปschema/joinsปัจจุบัน; เลือกdomainที่มีช่องว่างจริงก่อน

### ข้อผิดพลาดใหม่ที่ต้องกัน

การเรียก legacy answer ตรงทำให้ข้อมูลเก่าทับสิ่งที่เจ้าของแก้

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ใช้คำถามเดิม/ใหม่คู่กันแล้วตรวจentity, operation, fields, qualifiers, output coverageและ source revision รวมnegative/ambiguous cases ไม่ใช้scoreรวมอย่างเดียว

### ทำเองได้แค่ไหน

ทำโค้ด/การวิเคราะห์เองได้; ไม่ต้องให้เจ้าของออกนโยบายใหม่

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/pipeline/engine.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/engine.py>) — answer
- [common / app/pipeline/migrated_chat.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py>) — answer

## P02 — การฟื้นคำผิดของ task cue ไม่ได้ถูกเรียกเหมือนเดิม

**ตำแหน่ง:** raw input → task normalization  
**หลักฐาน/ข้อจำกัด:** C: มีคู่คำถาม+traceและตำแหน่งโค้ด  
**ตัวเลขที่รายงานไว้:** known-name+no-fields1,979requestsเป็นอาการที่เกี่ยวข้อง ไม่ใช่ทั้งหมดเกิดจากtypo

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

เดิมมีkeyboard-neighbor/transposition/multi-error/cue/game variants ส่วนcommon normalizeกับschema-language recoveryคนละช่วงและคนละเงื่อนไข ชื่อเกมที่exactได้ทำให้ไม่ต้องfuzzyชื่อ แต่คำกริยาหรือชนิดคำถามยังผิดอยู่

### หลักฐานตัวอย่างจากผลที่เก็บไว้

Zelda “คือกมอะๆร”: entityตรง, operationNone, requested_fieldsว่าง, unresolved clauseยังอยู่ ข้อมูลsummary/genre/how_to_play/official_descriptionในฐานกลางknownแล้ว

### พฤติกรรมที่ควรได้

ฟื้นความหมายของoperationโดยรักษาrawและedit trace ไม่แก้ชื่อเครื่อง ตัวเลข edition/วันที่/negationแบบเดา

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B**

รวม recovery เป็น candidate generator เดียวสำหรับชื่อและ task cue แยกกัน พร้อม raw spans/protected tokens; ใช้กับ typed และ LLM paths

กรอบวิธีแก้จากการวิเคราะห์เดิม: แชร์pure recovery/task cue helpersของเดิมก่อนsemantic field selection พร้อมcandidate/margin/anchor protection ไม่เพิ่มaliasประโยคทีละข้อ

### ข้อผิดพลาดใหม่ที่ต้องกัน

fuzzy correction เปลี่ยน valid word เช่น pay เป็น play หรือ PC11 เป็น PC1

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ตรวจdouble/delete/transpose/neighbor/multiple editsในtaskและentityแยกกัน มีhard-negativeชื่อคล้าย/PC1กับPC11/CS2กับVALORANT

### ทำเองได้แค่ไหน

ทำเองได้ในขอบเขตข้อความและfactsเดิม

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [legacy / app/pipeline/preprocess.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/preprocess.py>) — preprocess_input
- [common / app/knowledge/common/query_contract.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_contract.py>) — normalize
- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — named

## P03 — Exact entity ถูกเข้าใจผิดว่าเข้าใจคำถามแล้ว

**ตำแหน่ง:** entity match → operation/field selection  
**หลักฐาน/ข้อจำกัด:** C: ยืนยันจากaggregateและtrace  
**ตัวเลขที่รายงานไว้:** exact10,179; exactแต่ไม่มีrequested fields1,979; selected entityไม่มีfieldsรวม3,747

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

exactแปลว่าพบชื่อ/alias ไม่ได้บอกว่าuserขอoverview, price, controls, permissionหรือstatus ตัวกลางยังอาจเหลือgenericfield menuแม้subjectแน่นอนแล้ว

### หลักฐานตัวอย่างจากผลที่เก็บไว้

Zeldaได้recordถูกแต่ถามชื่อเกมอย่างเป็นทางการ; SF-006ได้PCscopeแต่คำว่าอุปกรณ์ยังไม่ลงrender contract

### พฤติกรรมที่ควรได้

ระบุobjectและtaskคนละslot แล้วตรวจว่ามีคำตอบสำหรับtaskที่ถาม ไม่เสนอmenuภายในเพียงเพราะรู้kind

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→C**

แยก entity_resolution_result จาก task_resolution_result; การพบ entity ห้ามตั้ง operation/default fields โดยไม่มี task support

กรอบวิธีแก้จากการวิเคราะห์เดิม: เพิ่มtyped request contractที่มีoperation/needs/constraints/unknown slotsก่อนเลือกfield; field menuควรเกิดเมื่อuserยังไม่ระบุเจตนาจริงเท่านั้น

### ข้อผิดพลาดใหม่ที่ต้องกัน

เลือกเมนู field หรือราคาทั้งที่ถามวิธีเล่น

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ชุดexact-name+clean task, exact-name+typo task, unnamed task, multi-target และshort followup ต้องเลือกทางต่างกันถูก

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — named
- [common / app/knowledge/common/query_scope.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py>) — primary_ids

## P04 — Regex/priority ของเดิมไม่ได้กลายเป็นความหมายของaliasesโดยอัตโนมัติ

**ตำแหน่ง:** trusted patterns → current FAQ  
**หลักฐาน/ข้อจำกัด:** C: source+R86audit; จำนวนผลเสียเฉพาะยังไม่แยก  
**ตัวเลขที่รายงานไว้:** legacy intent final16requests; routing stageพบ23events

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

legacy matchercompilepatternและpriority ขณะที่common namedescapealiasเป็นliteral R87bridgeรับเฉพาะwhole-query coverageและunique currentintent รวมทั้งexcludeหลายoperation จึงมีขอบเขตต่างจากrouterเก่ามาก

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R86พบregex-looking aliases61FAQ/308entriesในsnapshotที่auditไว้ ไม่ใช้ตัวเลขนั้นอ้างว่าทั้ง308กำลังตอบผิด R87FAQadvance timeแก้ได้ แต่ยังไม่ใช่ทุกparaphrase

### พฤติกรรมที่ควรได้

routing configurationใช้เพื่อระบุtask ส่วนanswerอ่านจากcommon intent_key/sourceปัจจุบันเสมอ

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **A→B**

สำรวจ regex/priority เดิมทีละ capability; แปลงผลเป็น TaskPlan และให้ alias ของ owner เป็น literal entity name ต่อไป

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำintent compiler/adaptorที่ประกาศcoverageและexclusionsชัด รองรับคำสุภาพ/กรอบคำถามแบบsemantic ไม่compileทุกowner aliasเป็นregex

### ข้อผิดพลาดใหม่ที่ต้องกัน

เจ้าของต้องเขียน regex หรือ alias รายคำถามเพื่อเพิ่ม record

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

เปลี่ยนanswerในDB/ถอนrecordแล้วrouterต้องไม่คืนanswerเก่า; patternชนกัน/หลายintentต้องถามเพิ่มอย่างจำเพาะ

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [legacy / app/rules/matcher.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/rules/matcher.py>) — RuleMatcher
- [common / app/knowledge/common/legacy_intent_bridge.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/legacy_intent_bridge.py>) — select

## P05 — Candidate recall และ independent-topic anchor ปิดทางก่อน LLM เห็น source

**ตำแหน่ง:** entity_search retrieval → pre-inference guard  
**หลักฐาน/ข้อจำกัด:** C: policyในโค้ด; H: ไม่ใช่ทุก no_candidate เป็นfalse negative  
**ตัวเลขที่รายงานไว้:** global diagnostic audit no_candidate1,403 / no_independent_topic_anchor1,733; เป็นeventsจากตัววิเคราะห์เดิม ไม่ใช่requestไม่ซ้ำ

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

boundedtrigram, excerptbudget, allowed kinds, numbered/broad/live gatesและtitle/topic overlapช่วยกันมั่วแต่ทำให้unseen wordingบางคำไม่ถึงโมเดล การมีคำตอบอยู่ท้ายfieldหรืออีกrelatedrecordไม่ได้รับประกันว่าจะได้candidate

### หลักฐานตัวอย่างจากผลที่เก็บไว้

entity_searchจำกัด8candidatesและtask backstop4, threshold.16; topic_alignmentระบุเองว่าไม่ใช่entailment/calibrated score

### พฤติกรรมที่ควรได้

เพิ่มrecallจากschema/task/relationsโดยยังรักษาquoted subjectและanti-confusion constraints ไม่ส่งทุกfactsให้LLMแล้วเชื่อทั้งหมด

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→I**

ทำ candidate-stage trace รวม source ที่ควรเจอแต่ไม่ผ่าน kind/topic/recall gate; ออกแบบค้นชื่อ+topic+semantic proposals ตาม task

กรอบวิธีแก้จากการวิเคราะห์เดิม: วัดcandidate recallจากsource IDsที่รู้ผล แยกsource absent, retrieval miss, preguard rejection, model selection errorเป็นคนละเหตุ; รองรับtopic metadataที่ownerไม่ต้องเขียนregex

### ข้อผิดพลาดใหม่ที่ต้องกัน

เพิ่ม top-k จน noise สูง หรือส่งข้อมูลทั้งหมดให้ LLM โดยไม่ล็อกขอบเขต

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ใช้held-out paraphrase, tail facts, similar-policy negatives และnew recordsที่ไม่เพิ่มชื่อในcode; เก็บretrieved/rejected IDsพร้อมreason

### ทำเองได้แค่ไหน

ทำเองได้จากfactsที่มี; factsใหม่ที่ยังไม่มีไม่ควรสร้าง

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/entity_search.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py>) — candidates
- [common / app/knowledge/common/entity_search.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py>) — topic_alignment

## P06 — LLM schema ผ่าน แต่ semantic guard ปฏิเสธเพราะ lexical intent ยังไม่รู้จัก

**ตำแหน่ง:** planner checked_plan → semantic_guard  
**หลักฐาน/ข้อจำกัด:** C: มีauditและcodeชัด; ไม่ใช่พิสูจน์ว่าทุกแผนที่rejectควรถูกรับ  
**ตัวเลขที่รายงานไว้:** schemaผ่าน2,623events; finalรับ129; rejected_unverified_intent2,494events

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

schemaตรวจว่าชื่อfield/shapeถูก แต่semantic_guardยังต้องมีstrong typed needs ถ้าparaphrase/typoไม่อยู่ในgrammarก็reject ถึงโมเดลจะเสนอsummaryหรือgenreมาแล้ว ในทางกลับกันบางแผนโมเดลก็กว้างเกินจริงจึงไม่ควรรับทั้งก้อน

### หลักฐานตัวอย่างจากผลที่เก็บไว้

Zelda transport/schemaTrue แต่finalFalse reasonrejected_unverified_intent; Fridaymaintenanceถามpolicyแต่โมเดลเสนอquestionและถูกปฏิเสธ

### พฤติกรรมที่ควรได้

รับแผนที่ผูกแต่ละclauseกับoperation/fieldที่มีความหมายได้จริง และตัดเฉพาะextra fields; คงguardต่อunsupported facts/unknown target

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→C**

แยก guard เป็น shape, task binding, qualifier preservation และ evidence checks; รองรับ whole-task contracts ก่อน; semantic proposals ที่กว้างกว่านั้นต้องมี acceptance policy แยก

กรอบวิธีแก้จากการวิเคราะห์เดิม: ปรับrequest semantic bindingและsharedcue normalization; แยกunknown wordingจากunrelated task ไม่ใช้การปิดsemantic_guardเป็นวิธีแก้

### ข้อผิดพลาดใหม่ที่ต้องกัน

ปิด guard ทั้งหมด หรือใช้ regex เดิมเพียงตัวเดียวตัดสิน LLM paraphrase

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ต้องมีpositive paraphraseที่เคยrejectและnegative JSONถูกแต่intentผิด วัดschema acceptance/semantic acceptance/answer contentแยกกัน

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/planner.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py>) — semantic_guard
- [common / app/knowledge/common/planner.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py>) — _plan_fields_batch

## P07 — LLM เลือก field กว้างหรือผิดหน้าที่ แม้ JSON ถูกต้อง

**ตำแหน่ง:** schema prompt → field proposal  
**หลักฐาน/ข้อจำกัด:** C: ตัวอย่างauditจริง; H: สัดส่วนmodel semantic errorsยังไม่ตีตราทุกcall  
**ตัวเลขที่รายงานไว้:** ดูproposalรายcall ไม่เท่ากับ4,206schema accepted auditเป็นคำตอบถูก

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

promptอนุญาตfieldหลายชนิดของselectedkindและchildren โมเดลอาจเลือกmetadata/publisher/edition/venueทั้งหมดแทนgameoverview หรือเลือกFAQ.questionแทนanswer รูปแบบถูกแต่taskยังผิด

### หลักฐานตัวอย่างจากผลที่เก็บไว้

Zeldaเสนอ12fieldsรวมpublisher_url/age_rating/profile_roleที่ไม่ได้ขอ; ResidentEvilVillage “ราคเท่าไหร่”เสนอ[]

### พฤติกรรมที่ควรได้

เลือกminimal sufficient fieldsต่อclauseให้ครอบคลุมสิ่งที่ถามและqualifier ไม่เพิ่มall_fieldsเพราะไม่แน่ใจ

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **C**

กำหนด primary/optional/forbidden fields ต่อ task: game overview=summary/genre, how-to=how_to_play, FAQ content=answer; โมเดลเสนอเฉพาะ task-compatible fields

กรอบวิธีแก้จากการวิเคราะห์เดิม: ให้task-to-field profilesที่ใช้ร่วมทุกrecordและตัวตรวจunrequested fields; metadataช่วยอธิบายความหมายfield ไม่ใส่factsที่โมเดลไม่จำเป็นต้องgenerate

### ข้อผิดพลาดใหม่ที่ต้องกัน

profile broad เกินไปจนตอบ publisher/edition/ชื่อคำถามแทนสาระ

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

assert must-answer needsและmust-not-answer extra fields ทั้งtemplatequestionsและคำถามใหม่ ไม่วัดแค่JSON/schema

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/planner.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py>) — _plan_fields_batch
- [common / app/knowledge/common/query_contract.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_contract.py>) — resolve_fields

## P08 — คำถามผสมมีส่วนขาด แล้วคำตอบที่มีหลักฐานถูกทิ้งทั้งก้อน

**ตำแหน่ง:** clauses → partial coverage → outer migrated guard  
**หลักฐาน/ข้อจำกัด:** C: rejected_candidateและcomposition paths; H: ไม่ใช่700กรณีควรตอบทุกส่วน  
**ตัวเลขที่รายงานไว้:** rejected_candidateถูกเปลี่ยนเป็นsafe response700requests; compound final262requests

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

บางpathcomposeเป็นpartialได้ แต่บางpathมีunresolved_query_clauseจนvalidationไม่ผ่าน แล้วmigrated dispatcherเปลี่ยนทั้งคำตอบเป็นขอแยกถาม ผู้ใช้จึงไม่ได้ส่วนที่ตอบได้

### หลักฐานตัวอย่างจากผลที่เก็บไว้

Cockpit30minutes+“howdoIboo” มีknown price needsแต่bookingclauseขาด และมีvalidityอีกชั้น ต้องแยกเหตุไม่ใช่อ้างtypoอย่างเดียว

### พฤติกรรมที่ควรได้

ถ้าส่วนใดตอบได้อย่างอิสระตามsource ให้ตอบพร้อมขอบเขต แล้วถามเฉพาะส่วนที่ยังไม่ทราบ; ถ้าdependencyทำให้ตอบส่วนแรกไม่ได้ต้องอธิบายdependency

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→E**

ทำ Need ledger และ dependency graph; คืนผลต่อ clause; รวมเฉพาะ independent answered needs และอธิบาย unresolved needs

กรอบวิธีแก้จากการวิเคราะห์เดิม: กำหนดper-clause status/obligationsและatomicityตามความสัมพันธ์ ไม่ล้างทุกส่วนหรือแสร้งว่าครบด้วยการตอบclauseเดียว

### ข้อผิดพลาดใหม่ที่ต้องกัน

partial answer ถูกเรียกว่าครบ หรือ dependent calculation ถูกตอบทั้งที่ input ขาด

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

mixedknown/unknown, negative correction, shared subjectต่างperiod/audience และconditional dependency ต้องไม่สลับslot

### ทำเองได้แค่ไหน

ทำเองได้ภายใต้factsเดิม

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/composition.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/composition.py>) — compose
- [common / app/pipeline/migrated_chat.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py>) — answer

## P09 — ระดับ Zone/Service/Resource และ relation projection ยังไม่ตรงกับคำถามบางแบบ

**ตำแหน่ง:** primary IDs → relations → labels  
**หลักฐาน/ข้อจำกัด:** C: traceตัวอย่าง; H: ไม่ใช่ทุกliteralชื่อzoneไม่ตรงคือplatformผิด  
**ตัวเลขที่รายงานไว้:** source-selection/coverage/wordingกลุ่มหลัก516requests; เป็นกลุ่มผสม

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

ระบบอาจเลือกserviceที่สัมพันธ์กับเกมถูกแต่renderเป็นบริการ1-2/1-4Persons แทนzoneที่ถาม หรือrootมีrelationอุปกรณ์แต่requestedfieldsไม่ยอมprojectionไปequipment_model

### หลักฐานตัวอย่างจากผลที่เก็บไว้

ZeldaถามwhichzoneตอบNintendoสองบริการแต่ไม่พูดNintendoSwitchZone; SF-006relation_edgesพบอุปกรณ์PCแล้วแต่ยังveto

### พฤติกรรมที่ควรได้

คืนข้อมูลตามระดับที่ถามและมีsource relationshipรองรับ ไม่สร้างzone membership/FKเองเพื่อให้มีlabelตามoracle

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **C→H**

ระบุ root kind/output granularity ใน EvidencePlan; เชื่อม resource→equipment, game→service→resource→zone ด้วย explicit refs; audit inferred joins

กรอบวิธีแก้จากการวิเคราะห์เดิม: มีtask-specific projectionplanและsemantic roleของroot/child แสดงzone+serviceรายละเอียดเมื่อมีหลักฐาน; ห้ามใช้name similarityแทนrelation

### ข้อผิดพลาดใหม่ที่ต้องกัน

เลือก relation ถูกแต่แสดงระดับผิด หรือ deduplicate จนทำเครื่องจริงหาย

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

zone↔service↔resource↔equipment↔game-service tests รวมno-FK/withdrawn/multi-platformและlabel equivalence

### ทำเองได้แค่ไหน

ทำเองได้ถ้ามีrelation/source grouping; mappingที่ไม่มีต้องยืนยันแหล่ง

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/query_scope.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py>) — primary_ids
- [common / app/knowledge/common/relations.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/relations.py>) — related_attributes

## P10 — การผูกกลุ่มราคา หน่วยเวลา และบริการยังต้องแยกจากการงดตอบเพราะราคาเก่า

**ตำแหน่ง:** price needs → audience/rates → billing  
**หลักฐาน/ข้อจำกัด:** C: sourceและplans; H:107diagnosticsไม่ใช่107ราคาคิดผิดที่ยืนยันแล้ว  
**ตัวเลขที่รายงานไว้:** price_scope_validity_or_wording107requests; regular rate18มีknownexpiry/6unknownvalidity

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

คำถามอาจมีVR30เป็นชื่อpackageและ3ชั่วโมงเป็นเวลาที่เล่น ต้องไม่เลือกเลขแรกเป็นเวลาสุดท้ายเสมอ กลุ่มภายนอกทั่วไป/GeneralStudent/PSUต่างกัน การรู้gameไม่พอคำนวณราคาโดยไม่รู้service

### หลักฐานตัวอย่างจากผลที่เก็บไว้

ตัวอย่างGeneralStudent VR30นาที3ชั่วโมง: เดิมตอบ30นาที190บาทจากsourceเก่า ใหม่งดราคาปัจจุบันเพราะexpiry; ผลนี้ไม่ยืนยันduration parserของฝั่งใดว่าถูกทุกเงื่อนไข

### พฤติกรรมที่ควรได้

แยกservice package duration, requested play duration, reserved occupancy และaudience แสดงunknownเฉพาะที่มีผลต่อจำนวนเงิน

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **D**

แยก duration role ออกจาก package label, audience scope, player quantity และ billing unit; ตรวจ validity ก่อน calculation

กรอบวิธีแก้จากการวิเคราะห์เดิม: ใช้billing contractระบุหน่วย/rounding/minimum explicit และsource revision; หากcontradictory durationให้ถามเจาะจง ไม่คูณเองจากราคาเก่าที่หมดอายุ

### ข้อผิดพลาดใหม่ที่ต้องกัน

VR30 ในชื่อกับเล่น 3 ชั่วโมงถูกจับเป็นเลขเดียวกัน หรือเติม audience โดยเดา

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

boundary30/60minutes,3h,หลายservice,ต่างกลุ่ม,expired/unknown validity พร้อมexpected priceที่มีsourceและreference date

### ทำเองได้แค่ไหน

parserทำเองได้; ราคาปัจจุบัน/วันที่มีผลที่ไม่มีหลักฐานต้องเจ้าของ

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/billing.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/billing.py>)
- [common / app/knowledge/common/audience_scope.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/audience_scope.py>)
- [common / app/knowledge/common/price_comparison.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/price_comparison.py>)

## P11 — ราคาเหมาอ่านได้แล้ว แต่ไม่ใช่ทุกเงื่อนไขการเช่ามีนโยบายให้ตอบ

**ตำแหน่ง:** rental interpretation → current package + followup  
**หลักฐาน/ข้อจำกัด:** C: bridge/fixtureและinventory; D: unknownที่ถูกต้อง  
**ตัวเลขที่รายงานไว้:** 24packages validityunknown; rentalbridgefinal5requestsในcorpusนี้

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

คำว่าครึ่งวัน/เต็มวันในsourceไม่ได้ให้ชั่วโมงหรือเงื่อนไขmulti-day/hourly/custompackageเสมอ การเหมาexcludeVRบางรูปแบบไม่เท่ากับมีแพ็กเกจใหม่ที่เอาราคามาลบกันได้

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R87fixtureแก้ราคา/เพิ่มAurora/ถอนpackageได้และรักษาPCexternalfull→half→internal แต่ไม่ได้ยืนยันevery rental paraphrase/ownerbookingterms

### พฤติกรรมที่ควรได้

ตอบราคาที่บันทึกและscopeที่ตรง ชี้ว่าไม่มีข้อมูลชั่วโมง/การยกเลิก/มัดจำถ้าไม่มีsource ไม่คำนวณส่วนลดเอง

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **D→H**

ให้ rental task ใช้ dynamic current package catalog; terms/duration/validity แยก readiness ต่อ need; ไม่คำนวณแพ็กเกจ custom ที่ source ไม่อนุญาต

กรอบวิธีแก้จากการวิเคราะห์เดิม: คงtuplecontractและdynamiccatalog เพิ่มgeneral paraphrasecoverageตามtask; ระบุunknown validity/termsเป็นdata readinessแยกจากcode

### ข้อผิดพลาดใหม่ที่ต้องกัน

ตอบแพ็กเกจ 5 ชั่วโมงจากราคาเต็มวันหรือหัก VR ออกเอง

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

compoundtuples,customduration,PS6unknown,cancelstate,all-exceptและrevisionupdate/withdrawในisolatedfixtures

### ทำเองได้แค่ไหน

โค้ด/stateทำเอง; เงื่อนไขใหม่/จำนวนชั่วโมง/วันมีผลต้องมีsourceเจ้าของ

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/rental_bridge.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/rental_bridge.py>) — answer

## P12 — ข้อมูลเกมมีอยู่แล้ว แต่ overview/description operation ยังไม่ครอบคลุมรูปประโยค

**ตำแหน่ง:** game target → overview needs  
**หลักฐาน/ข้อจำกัด:** C: known field+traceครบ  
**ตัวเลขที่รายงานไว้:** ตัวอย่างZelda; ไม่ได้สรุปว่า51gamesผิดทุกเกม

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

known genre/summary/how_to_play/official_descriptionไม่ได้ช่วยถ้าoperationNoneหรือdefaultmenuมองว่าuserขอtitle field ตัวใหม่บางเกมตอบได้ในcleanwording แต่ไม่ยืนยันว่าtask recoveryครอบคลุมทุกเกม

### หลักฐานตัวอย่างจากผลที่เก็บไว้

DATA_INVENTORYบันทึกknownfieldsของZeldaและR89มีคำตอบเก่าที่อธิบายได้กับคำถามtypoเดียวกัน

### พฤติกรรมที่ควรได้

เมื่อถามเกมอะไรควรใช้summary/genreที่มีsource ส่วนofficialdescriptionยาวให้ตามระดับรายละเอียดที่ขอ ไม่เผยage/publisherเพียงเพราะfieldมี

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **C**

ย้าย task resolution ก่อน game→service projection และให้ overview/how-to ใช้ทุก game ID จาก snapshot; จำกัด required fields ตาม task

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำgame-overview contractที่ไม่ผูกชื่อเกม ใส่requestfocusและlength/scopeprojectionจากtask ไม่เพิ่มaliasทุกชื่อ+ทุกประโยค

### ข้อผิดพลาดใหม่ที่ต้องกัน

เพิ่มเฉพาะชื่อ Zelda หรือบังคับต้องมีวิธีเล่นก่อนตอบแนวเกมได้

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

เปลี่ยนชื่อเกม/เพิ่มเกมใหม่/ไทยอังกฤษ/คำขาดเบิ้ลและaskingallvsbrief พร้อมassertsubstantivegenre/actiondescription

### ทำเองได้แค่ไหน

ทำเองได้จากsourceเดิม

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/query_scope.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py>) — primary_ids
- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — answer

## P13 — ปุ่มและวิธีเล่น: action/mode mapping กับ completeness ไม่ใช่แค่ชื่อปุ่มปรากฏ

**ตำแหน่ง:** control request → set/action bindings  
**หลักฐาน/ข้อจำกัด:** C: schema/projectionและบางdiagnostics; H:ต้องอ่านcontentรายข้อ  
**ตัวเลขที่รายงานไว้:** 43controlsets;9requestsอยู่กลุ่มหลักcontrol_projection_or_wording

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

ชื่อเกมกับplatformอาจตรงแต่mode/actionไม่ตรง การแสดงปุ่มบางส่วนไม่ใช่ครบทุกปุ่ม sourceบางชุดไม่เคยตรวจphysical mapping ต้องไม่เพิ่มคำยืนยันเอง

### หลักฐานตัวอย่างจากผลที่เก็บไว้

MarioKartLivebindingsectionมีthแต่ไม่มีen11จุด; R87MarioPartybuttoncaseผ่านแต่ไม่ครอบคลุมทั้ง43sets

### พฤติกรรมที่ควรได้

ตอบactionที่ถามพร้อมbinding/เงื่อนไขของโหมด ถ้าขอทั้งหมดให้ครบscopeที่sourceมีและระบุpartialsource/mappingreview

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **E**

กำหนด control action vocabulary, platform/preset/mode resolution, requested/all coverage และ source verification flags

กรอบวิธีแก้จากการวิเคราะห์เดิม: มาตรฐานcontrolaction/mode/sourceclauseและcoveragecounter; รักษาunknowncontroller/missingmodeไม่สร้างmappingใหม่

### ข้อผิดพลาดใหม่ที่ต้องกัน

มีคำว่า jump ในคำตอบแต่เป็นปุ่มคนละแพลตฟอร์มหรือ source ยังไม่รับรอง

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

singleaction/allbuttons/multi-mode/unknownplatform/partialset/Englishsectionและquestiontypos

### ทำเองได้แค่ไหน

โค้ดและแปลจากsourceทำเอง; physicalmappingที่ไม่ยืนยันไม่รับรองแทนผู้ตรวจ

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/control_rows.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/control_rows.py>)
- [common / app/knowledge/common/query_scope.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py>) — control_projection

## P14 — กติกาแข่งขัน: เล่มถูกไม่ได้แปลว่าเลือก proposition/ข้อยกเว้นครบ

**ตำแหน่ง:** competition target → facet → clause projection  
**หลักฐาน/ข้อจำกัด:** C: source/clausesและdiagnostics; H:330ไม่ใช่จำนวนsemanticผิดทั้งหมด  
**ตัวเลขที่รายงานไว้:** 330requestsในกลุ่มหลัก; English301/Thai29ตามdiagnostic

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

ขอบเขตปี/edition, facetและpropositionต่างกัน มีทางเลือกliteral source/topicที่ยังตอบส่วนใหญ่เกินหรือขาดconditions/penaltiesได้ R87overview/protestbridgeเป็นเพียงบางงาน

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R88summarybridge13/protest2requests; TekkenetiquetteบางcaseขาดexactEnglishclauseทั้งที่sourceใช้คำแปลอีกสำนวน ต้องอ่านทั้งความหมายและcompletenessก่อนลงว่าเลือกผิด

### พฤติกรรมที่ควรได้

ให้ครบทุกpropositionที่ถามและqualifier รวมdependencies ไม่เปลี่ยนเกมเอง; ถ้าไม่มีrulebookของเกมนั้นให้บอกขอบเขต

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **E**

จัด ordered rule clauses, dependencies, exceptions และ per-proposition obligations; all/overview/detail แยก renderer

กรอบวิธีแก้จากการวิเคราะห์เดิม: ใช้target-locked clausecontracts/relation graph, distinguishsummary/all/detail และsemanticequivalence checkที่ไม่ลบตัวเลข/negation/conditions

### ข้อผิดพลาดใหม่ที่ต้องกัน

summary ซ่อนข้อยกเว้น หรือเอากฎปีอื่นมาเติมส่วนที่ขาด

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

4rulebooks หลายfacet/compoundtopic,unknownedition,summaryvsall,consequence/exception,TH/ENparaphraseและtypo

### ทำเองได้แค่ไหน

โค้ด/การเลือกข้อทำเอง; เอกสารขัดกัน/รายการใหม่ที่ไม่มีsourceต้องผู้จัด

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/query_scope.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/query_scope.py>) — rule_selection
- [common / app/knowledge/common/competition_bridge.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/competition_bridge.py>) — answer

## P15 — Open / bookable / Maintenance ยังมีความขัดแย้งใน metadata ที่ต้องแยกความหมาย

**ตำแหน่ง:** schedule facts → day status / booking windows  
**หลักฐาน/ข้อจำกัด:** C:5fieldsconflicted; มีownerconfirmationเดิมบางส่วนแล้ว  
**ตัวเลขที่รายงานไว้:** schedule7records; open_periodsconflicted5

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

migrationเก็บความต่างระหว่างdashboardกับchatcalendarเป็นconflict ห้ามเอาช่วงจองไม่ได้ไปสรุปข้อเท็จจริงอื่นที่ยังไม่ทราบ และห้ามลืมข้อมูลที่ผู้ใช้ยืนยันแล้ว

### หลักฐานตัวอย่างจากผลที่เก็บไว้

5conflict notesระบุopen/bookable/พักเที่ยง/Maintenance; ผู้ใช้ยืนยัน12–13ไม่มีให้จองและVR30กันชั่วโมงเต็มแล้ว

### พฤติกรรมที่ควรได้

การตอบวันที่เปิดใช้service/bookableตามsourceที่ยืนยัน แยกวันMaintenance/เวลาเข้าพื้นที่/occupancy ไม่ตอบweekdaydebugแทนวันนี้วันที่...เปิด/ปิด

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **F→H**

แยก semantic field open/bookable/maintenance พร้อมนำ user confirmation เดิมไปผูก provenance ตามขอบเขต; ส่ง conflict เฉพาะ need ที่ยังคลุมเครือ

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำseparate typed fieldsกับauthority mapping ใช้confirmationเดิมแก้ได้เท่าที่รองรับ ไม่ขอให้ยืนยันซ้ำเรื่องจอง12–13; คำถาม physical access ที่ยังไม่มีคำตอบค่อยถามเฉพาะประเด็น

### ข้อผิดพลาดใหม่ที่ต้องกัน

ตีความจองไม่ได้ว่าเข้าอาคารไม่ได้ หรือถามผู้ใช้ยืนยันเที่ยงซ้ำ

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ก่อน/ตรง/หลังขอบเวลา,bookablegap,Maintenance,TH/ENday/dateและavailabilityต้องไม่ขัดกัน

### ทำเองได้แค่ไหน

ทำmapping/ตรรกะเองได้; หากต้องระบุสิ่งอื่นนอกbookabilityที่ยืนยันแล้วต้องsourceเพิ่ม

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/open_day.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/open_day.py>) — answer
- [common / app/calendar/service_calendar.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/calendar/service_calendar.py>)
- [common / app/knowledge/common/registry.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py>) — validate

## P16 — วันปิดพิเศษ วันหยุด และวันที่อ้างอิงต้องมี precedence ที่สม่ำเสมอ

**ตำแหน่ง:** relative date → calendar/closure precedence  
**หลักฐาน/ข้อจำกัด:** C: date/closurecode; H:aggregateไม่ชี้ว่าทุกclosureผิด  
**ตัวเลขที่รายงานไว้:** closure3knownvalidity; bulkใช้reference16ต.ค.2026

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

วันนี้/พรุ่งนี้/weekdayกับclosure rangeไม่ควรยึดweekday FAQแทนวันที่จริง จุดเริ่ม/สิ้นสุดแบบexclusiveกับtimezoneมีผลต่อstatus

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R88มีcalendar/date methodsแยกจากcompactopenstatus; fullbulkไม่ใช้วันที่18ต.ค.ที่อ่านรายงานเป็นreferenceทุกข้อ

### พฤติกรรมที่ควรได้

ตอบวันที่ไทยและสถานะตามวันที่ถาม/closureที่ครอบ ไม่ใช้สถานะวันนี้ไปตอบวันอื่นและไม่อ้างliveoccupancyจากcalendar

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **F**

ทำ time context เดียวและ calendar precedence ต่อ zone/date พร้อม intervals ชัด; ordinary weekday FAQ ไม่ override closure

กรอบวิธีแก้จากการวิเคราะห์เดิม: รวมcalendardecisioncontractพร้อมsource precedence/affectedzones และtimebound ไม่ให้FAQทั่วไปoverrideข้อยกเว้นที่มีผล

### ข้อผิดพลาดใหม่ที่ต้องกัน

วันนี้อ้างวันของ host แทนเวลาไทย หรือปิดโซนเดียวแล้วตอบปิดทุกโซน

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

closurestart/end,all-day/partialday,crossdate,unknownspecialholiday,ไทย/อังกฤษ และknownreferencecases

### ทำเองได้แค่ไหน

ตรรกะทำเอง; วันปิดใหม่ที่ไม่มีsourceห้ามเดา

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/open_day.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/open_day.py>) — answer
- [common / app/calendar/service_calendar.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/calendar/service_calendar.py>)

## P17 — สถานะจองถูกจำลอง unavailable ในชุดใหญ่ จึงห้ามตีความว่า live จริงล่มหรือจองผิด

**ตำแหน่ง:** common defer → live adapter → controlled fixture  
**หลักฐาน/ข้อจำกัด:** D:ควบคุมโดยharness ไม่ใช่regressionoccupancy  
**ตัวเลขที่รายงานไว้:** live_unavailable1,074requests;18อยู่กลุ่มdiagnosticหลักนี้หลังจัดpriority

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

bulkตั้งget_live_booking_statusให้unavailableเพื่อไม่ให้เวลาทดสอบเปลี่ยนtruth การที่oracleอยากได้slotแต่ระบบตอบunavailableเป็นผลจากเงื่อนไขทดสอบนี้

### หลักฐานตัวอย่างจากผลที่เก็บไว้

RUN_SCOPE/runnerกำหนดfixture_offline; ผู้ใช้ยืนยันสถานะจริงถูกต้องมาก่อนแล้ว ไม่เปิดประเด็นเก็บtruthลูกค้าจริงใหม่ในรายงานนี้

### พฤติกรรมที่ควรได้

แยกAPIreachable/schema validกับfree/booked correctness และเขียนevaluationconditionชัด ไม่อ้างfailure1074คือWordPressจริงเสีย

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **F→I**

แยก controlled unavailable fixture กับ live provider ที่ผู้ใช้ยืนยันแล้วในรายงาน; runtime ให้ unknown/unavailable distinct

กรอบวิธีแก้จากการวิเคราะห์เดิม: ใช้known-result staticbookingfixturesในการตรวจlogic และsourcevalidatedlivegroundtruthเฉพาะเมื่อพร้อม/ได้รับคำขอแยก

### ข้อผิดพลาดใหม่ที่ต้องกัน

ไปแก้ WordPress จากความล้มเหลวใน mock หรือ API200 ถูกนับเป็น free-correct

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

day/time/resource ranges,VR30fullhour,free-onlyallinventory,TH/EN และupstream unavailableแต่ไม่ใช้oldoccupancyแทนlive

### ทำเองได้แค่ไหน

fixtureทำเอง; ไม่ต้องให้เจ้าของยืนยันliveที่ยืนยันแล้วซ้ำ

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/booking/live_status.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/booking/live_status.py>) — get_live_booking_status
- [common / app/booking/wordpress_status.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/booking/wordpress_status.py>) — fetch_wordpress_status

## P18 — ประวัติมาถึงแล้ว แต่ short follow-up ยังไม่กลายเป็น task ที่ตอบได้

**ตำแหน่ง:** trusted history → state scope → follow-up operation  
**หลักฐาน/ข้อจำกัด:** C: SF-006 traceพิสูจน์scopeและrelationsถูกส่งมา  
**ตัวเลขที่รายงานไว้:** sessions12/24turns; literalผ่าน23; positivecontract12turns

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

servercommonปิดlegacyrequest_planโดยตั้งใจแต่เก็บcommon_read_state SF006typed_common_stateมีPCservicesและrelationedges6อุปกรณ์ แต่คำว่าอุปกรณ์ไม่ผ่านfield/coverageguard ทำให้ไม่มีสาระตอบ

### หลักฐานตัวอย่างจากผลที่เก็บไว้

PCมีอะไรบ้าง→อุปกรณ์: stateไม่ได้หาย แต่requestedfieldsเลือกspecifications/usageและunresolved_query_clauseจึงouterveto

### พฤติกรรมที่ควรได้

รับshortreplyในบริบทที่แยกambiguityได้แล้ว แล้วทำequipment-listprojectionของscopeเดิม ไม่ถามเกม/ราคาใหม่หรือทิ้งtargetโดยไม่มีเหตุ

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→C→G**

ทำ pending need/selection state ที่มี scope และ delivered turn; short replies สร้าง TaskPlan แบบเดียวกับ full question แล้วอ่าน revision ใหม่

กรอบวิธีแก้จากการวิเคราะห์เดิม: ผูกofferedneed/pendingselectionกับcanonicaloperation ตรวจdeliveredstate/revision และปรับshortoperationcontractให้ตรงกับfullquestion

### ข้อผิดพลาดใหม่ที่ต้องกัน

สรุปว่า history หายทั้งที่ guard ปฏิเสธ หรือ carry stale facts

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

2–5turns เลือกชื่ออย่างเดียว/all/another/negative/cancel/changeaudience และไม่inheritเมื่อเปลี่ยนเรื่อง; HTTPและengineต้องรายงานแยก

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/web_api/server.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/web_api/server.py>) — do_POST
- [common / app/knowledge/common/dialogue.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/dialogue.py>) — resolve_state
- [common / app/knowledge/common/equipment_bridge.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/equipment_bridge.py>) — answer

## P19 — Qualification และ unknown policy ต้องไม่ถูกแทนด้วยคำตอบใกล้เคียง

**ตำแหน่ง:** profile/task ownership → confirmed or unknown source  
**หลักฐาน/ข้อจำกัด:** C: code+fixture; D:การบอกunknownบางข้อถูกต้อง  
**ตัวเลขที่รายงานไว้:** specific_unconfirmed_request12methods;2requestsในกลุ่มหลักนี้

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

สลิปผิด≠ยืนยันตัวตนผิด≠ยอดเงินผิด นำอุปกรณ์ส่วนตัวใช้≠ให้ศูนย์เตรียมอุปกรณ์ การคล้ายคำไม่ให้ย้ายอำนาจsourceหรือทิ้งnegation

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R87fixtureเพิ่มpolicyยอดเงินแล้วอ่านV1/V2/withdrawได้ แต่productionsnapshotยังไม่ใช่การอนุมัตินโยบายใหม่นั้น

### พฤติกรรมที่ควรได้

ถ้าfactsเฉพาะไม่มีให้บอกว่าไม่ยืนยันเรื่องนั้น ถ้ามีsourceใหม่แล้วต้องไม่ติดoldunknowngate

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→E**

เก็บ action/object/ownership/context/polarity/exception เป็น typed constraints และตรวจ source applicability ก่อนตอบ

กรอบวิธีแก้จากการวิเคราะห์เดิม: ใช้typed task/subject/ownership/context/qualifier bindingsและcurrent-source-checkก่อนunconfirmed; yesยืนยันหัวข้อไม่ใช่อนุมัติfacts

### ข้อผิดพลาดใหม่ที่ต้องกัน

คำตอบใกล้เคียงด้านการชำระเงินถูกใช้กับอีกนโยบายหนึ่ง

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

slip/identity/amount/personal/competitionเงื่อนไขใกล้กัน newpolicyrevisionและwithdrawalไม่คืนค่าจากhistory

### ทำเองได้แค่ไหน

โค้ดทำเอง; นโยบายที่ยังไม่มีต้องownerหรือsourceจริง ไม่ใช้fixturesเป็นpolicyศูนย์

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/qualified_reply.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/qualified_reply.py>)
- [common / app/knowledge/common/unconfirmed_request.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/unconfirmed_request.py>)
- [common / app/knowledge/common/legacy_intent_bridge.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/legacy_intent_bridge.py>) — source_for_need

## P20 — ภาษาอังกฤษ: metadata, ค่าที่ขาด, proper names และคำแปลต้องแยกกัน

**ตำแหน่ง:** localized source values → English rendering  
**หลักฐาน/ข้อจำกัด:** C:scanknownvaluesและflags; H:Thai-characterflagไม่เท่ากับแปลผิด  
**ตัวเลขที่รายงานไว้:** agent_translated486records;metadata missing116;knownlocalizedobjectsไม่มีen11;Thai-in-en32objects;Englishanswerflag512requests

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

116คือrecord-levelstatus ไม่ใช่จำนวนrecordที่ไม่มีEnglishทั้งหมด 11actualmissingอยู่bindingsectionMarioKartLiveบางส่วน Thaiชื่อรายการ/หน่วยอาจติดflagแม้ไม่ใช่ประโยคที่ต้องแปล ส่วนclausetranslationอีกสำนวนทำให้literalfailได้

### หลักฐานตัวอย่างจากผลที่เก็บไว้

DATA_INVENTORYเก็บทุกmissingpathและen_thai_paths; Tekkenetiquetteมีsemanticใกล้เคียงแต่ถ้อยคำไม่ตรงoracle

### พฤติกรรมที่ควรได้

อ่านEnglishsourceที่ผูกrevisionและรักษาตัวเลข เงื่อนไข negation ปุ่ม/ชื่อเฉพาะ ถ้ายังไม่ครบให้บอกpartial/translationpendingตามขอบเขต

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **H**

ตรวจ localized fields จริงทีละ field; เติมเฉพาะที่มีต้นฉบับ; แยก proper names/prose; translation revision/hash ตามต้นฉบับ

กรอบวิธีแก้จากการวิเคราะห์เดิม: เติมเฉพาะ11ค่าที่มีต้นฉบับ, review32flagsเป็นชื่อเฉพาะหรือprose, ทำclauseequivalence checksแต่ไม่ทิ้งliteralcriteriaเดิม และไม่เปลี่ยนagenttranslatedเป็นowner-reviewedจากคะแนน

### ข้อผิดพลาดใหม่ที่ต้องกัน

แก้ภาษาเพื่อผ่าน literal แต่เปลี่ยนตัวเลข/negation หรือประกาศ owner-reviewed เอง

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

TH↔ENsamefact parity, amounts/dates/negation, controlbuttonidentity, names/mixedlanguageและmissinglocalizednestedobjects

### ทำเองได้แค่ไหน

แปลและตรวจตัวเลขทำเอง; factual/translationreviewโดยownerไม่อ้างว่าเกิดแล้ว

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — text
- [common / app/knowledge/common/translation.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/translation.py>)
- [common / app/knowledge/common/registry.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py>) — validate

## P21 — Output ยังเผยชื่อ field ภายในหรือ label ที่ไม่ช่วยตอบคำถาม

**ตำแหน่ง:** projection → human-readable answer  
**หลักฐาน/ข้อจำกัด:** C:คำตอบจริง; H:ต้องแยกUIdebugกับbody  
**ตัวเลขที่รายงานไว้:** ตัวอย่างVR Service/platform/playtime/bookingoccupancy และZeldaถามtitle

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

schemafieldใช้สร้างform/LLMplanได้ แต่ไม่ใช่รายการตัวเลือกที่ผู้ใช้ต้องรู้จักเมื่อtaskชัด citationtitleถูกเปลี่ยนเป็นdraftgenericก็ช่วยprovenanceระดับmodeแต่ไม่ได้อธิบายsourceหัวข้อจริงทั้งหมด

### หลักฐานตัวอย่างจากผลที่เก็บไว้

VRpermissioncaseตอบmenufieldแทนสิทธิ์เข้าใช้;Zeldaเกมอะไรตอบ“ชื่อเกมอย่างเป็นทางการ?”

### พฤติกรรมที่ควรได้

ตอบข้อเท็จจริงที่ถามด้วยภาษาผู้ใช้ หากต้องถามเพิ่มให้ถามslotที่มีผลต่อคำตอบ ไม่ถามfieldtechnical

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **C→G**

task renderer แยกจาก schema form labels; debug/source pointers อยู่ trace ส่วนผู้ใช้เห็นคำตอบตาม need และชื่อแหล่งอ่านได้

กรอบวิธีแก้จากการวิเคราะห์เดิม: แยกpresentationcontractจากcatalog/schema ใช้domaincaptionและscope/partial explanation พร้อมแหล่งอ้างอิงที่ติดตามได้; debugอยู่ส่วนdebug

### ข้อผิดพลาดใหม่ที่ต้องกัน

ผู้ใช้ถามเปิดไหมแต่เห็น weekday/open_periods/unknown ดิบทั้ง record

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ถามกว้าง/เฉพาะ/all/brief ทั้งสองภาษา ต้องไม่มีopaqueID/fieldtechnicalในmainanswerเว้นแต่userขอdebug

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/rendering.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/rendering.py>)
- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — title

## P22 — Validation/score ดูดีไม่ได้รับรองว่าเข้าใจเจตนาถูก

**ตำแหน่ง:** finish validation → confidence/status interpretation  
**หลักฐาน/ข้อจำกัด:** C:โค้ดและcounts  
**ตัวเลขที่รายงานไว้:** confidence.8พบ10,969requests;uncalibratedflag15,892requests

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

common finishให้.8คงที่สำหรับanswer/list ส่วนschema/evidenceตรวจfieldที่เลือก ไม่ตรวจว่าควรเลือกfieldนั้นตั้งแต่แรก FinalsafeclarificationอาจvalidTrueหลังvetoคำตอบที่ผิด

### หลักฐานตัวอย่างจากผลที่เก็บไว้

fieldplanner schemaTrueแต่finalFalseได้; old_build_resultหลังvetoกลับvalidTrueพร้อมwarnings; migrationtrace1.0คือเลือกprofileไม่ใช่factual100%

### พฤติกรรมที่ควรได้

แยกexecution validity, schema validity, source support, intent/task coverage, semantic correctnessและapproval status

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→I**

สร้าง per-need statuses/coverage และแยก evidence-valid จาก task-correct; ยกเลิกการใช้ fixed confidence เป็นคะแนนความถูกต้อง

กรอบวิธีแก้จากการวิเคราะห์เดิม: เพิ่มper-need coverage/unansweredneeds/counterevidence output contract ไม่เอาdefaultconfidenceไปปรับranking/โชว์เปอร์เซ็นต์ความถูกต้อง

### ข้อผิดพลาดใหม่ที่ต้องกัน

safe clarification schema-valid ถูกนับเหมือนตอบครบ

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

wrongfieldbutknownsource,correctfieldbutexpired,correctcitationwronggame,safeclarification,unverifiedtranslationต้องให้สถานะแยก

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — finish
- [legacy / app/pipeline/engine.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/engine.py>) — _build_result

## P23 — Model transport, JSON/schema, binding และคำตอบต้องวัดแยก

**ตำแหน่ง:** model admission → HTTP → body/parse → semantics  
**หลักฐาน/ข้อจำกัด:** C:calllogsและaudit  
**ตัวเลขที่รายงานไว้:** 4,412HTTPattempts;4,376transportobservations;36TimeoutErrors;31requestsถูกจัดprimarytransportfailure

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

LLMONเป็นสิทธิ์ให้เรียก ไม่ใช่ทุกคำถามต้องเรียก HTTPobserverบันทึกสำเร็จเมื่อurlopenคืนresponse ไม่ใช่รับรองbody/schema/answerทั้งก้อน แต่plannerมีbody/parse/semantic auditแยก

### หลักฐานตัวอย่างจากผลที่เก็บไว้

จำนวนschemaacceptedaudits4,206ไม่เท่ากับ4,206คำตอบถูก; จำนวนcallกับrequestsต่างกันเพราะrequestอาจมีหลายcall

### พฤติกรรมที่ควรได้

ตรวจservedmodel+จริงgenerationpreflightแล้วเก็บphasefailureรายcall อธิบายfallbackโดยไม่สลับOFFเงียบๆ

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **I เริ่ม trace ตั้งแต่ A**

บันทึก attempt/connect/body/parse/schema/semantic/final stages; timeout อยู่ phase ไหนต้องเห็นจาก trace ไม่อาศัย HTTP status อย่างเดียว

กรอบวิธีแก้จากการวิเคราะห์เดิม: root-causeตามtransport/read/schema/binding/semanticsและdeadline ไม่เพิ่มaliasหรือแก้factsเพื่อรักษาคะแนนเมื่อติดต่อโมเดลไม่ได้

### ข้อผิดพลาดใหม่ที่ต้องกัน

เพิ่ม alias เพื่อแก้ transport error หรืออ้าง model success จาก headers

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

available/refused/permission/timeout/malformedJSON/schemawrong/bindingwrong/semanticwrongต้องแยกและpreserverawresult

### ทำเองได้แค่ไหน

ทำเองได้ในสภาพเครื่อง; ไม่สรุปnetwork permissionเป็นpolicyข้อมูลผิด

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/pipeline/llm_health.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/llm_health.py>)
- [common / app/knowledge/common/planner.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py>) — _plan_fields_batch
- [common / app/knowledge/common/entity_search.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py>) — select

## P24 — Bug ฝั่งเดิม: ownership_blocked ไม่อยู่ใน scope ของ retrieve_curated

**ตำแหน่ง:** legacy curated retrieval trace construction  
**หลักฐาน/ข้อจำกัด:** C:exception2692และตำแหน่งcode  
**ตัวเลขที่รายงานไว้:** legacyONNameError2,692requests + harness timeout2 = exceptions2,694

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

ใช้ownership_blockedที่returnของretrieve_curated แต่assignmentที่พบอยู่ในretrieve_competition_fact_cardsคนละfunction จึงล้มเมื่อเข้าbranchนั้น ไม่ใช่LLMไม่รู้คำตอบ

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R65resultsexceptionและR90exceptiontypesตรวจตรงกัน; strictscoreสูงของเดิมไม่ลบล้างbugนี้

### พฤติกรรมที่ควรได้

ทุกbranchต้องมีownershipauditที่ถูกscopeและจริงตามguardไม่ใช่ใส่ตัวแปรว่างเพื่อซ่อนข้อผิดพลาด

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **A**

ตรวจ dependency ของ helper ที่นำจาก legacy; ไม่ย้าย retrieve_curated ทั้งก้อน; บันทึก bug scope เดิมไว้ต่างหาก

กรอบวิธีแก้จากการวิเคราะห์เดิม: หากนำlegacyhelperกลับมา ใช้pureinterpretationที่จำเป็น ไม่คัดลอกretrievalทั้งชุด; แก้auditflowพร้อมtestownerblocked/unmanaged/nohitsbranchในงานซ่อมภายหลัง

### ข้อผิดพลาดใหม่ที่ต้องกัน

copy code เดิมทั้ง subtree แล้วพา NameError กลับเข้าระบบใหม่

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

branchcoverageทั้งมี/ไม่มีownershipblock,sourceconflict,emptyhitsและlexicalfallback; ไม่rerunlegacyใหญ่เพื่อไล่คะแนนในงานเอกสารนี้

### ทำเองได้แค่ไหน

ทำเองได้ แต่รอบนี้ยังไม่แก้โค้ดเก่าหรือโค้ดใช้งาน

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [legacy / app/pipeline/retrieval.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/retrieval.py>) — retrieve_curated
- [legacy / app/pipeline/retrieval.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/retrieval.py>) — retrieve_competition_fact_cards

## P25 — ข้อมูลหมดอายุ: คะแนนเดิมดีขึ้นได้จากการตอบค่าที่ระบบใหม่ไม่ควรยืนยัน

**ตำแหน่ง:** source validity → answer status → historical expected  
**หลักฐาน/ข้อจำกัด:** C:18ratesexpiryชัด; D:refusalcurrentpriceอาจถูกต้อง  
**ตัวเลขที่รายงานไว้:** not_current1,113requests;500อยู่primaryvaliditydiagnostic

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

referenceOct2026อยู่หลังexpiryก่อน1Apr2026 oracleบางข้อยังคาดบาท/ฟรีหรือราคาเดิม การเทียบcorrectnessต้องดูวันมีผลและหน่วย ไม่ใช้การมีตัวเลขเป็นproof

### หลักฐานตัวอย่างจากผลที่เก็บไว้

VRGeneralStudentcaseใหม่ระบุendtimestampตรงsource เดิมคืน190จากตารางเก่าตามคำถามที่มีdurationซ้อน

### พฤติกรรมที่ควรได้

ห้ามใช้ราคาเก่าเป็นcurrentโดยไม่มีหลักฐาน หากuserถามราคาประวัติในช่วงที่มีผลจึงตอบแบบhistoricalscopeได้

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **D→H→I**

ทำ outcome not_current พร้อม source date และ data request ที่เฉพาะเจาะจง; evaluator แยก historical/current

กรอบวิธีแก้จากการวิเคราะห์เดิม: แยกhistoricalvscurrentoracleและvaliditygroundtruth เก็บเกณฑ์เก่าเป็นcompatibilityresult ไม่ลบenddate/ย้ายclockเพื่อให้ผ่าน

### ข้อผิดพลาดใหม่ที่ต้องกัน

ลบ end date หรือเลื่อน clock ให้เกณฑ์เก่าผ่าน

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ก่อน/ตรง/หลังexpiry;no-current-rate;historicalpriceexplicit;unknownvalidityและpackageaudienceunits

### ทำเองได้แค่ไหน

logic/analysisทำเอง; ราคาปัจจุบันหรือวันมีผลใหม่ต้องsourceที่ยืนยัน

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — active
- [common / app/knowledge/common/billing.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/billing.py>)

## P26 — Draft preview ไม่ใช่ production authority หรือ owner approval

**ตำแหน่ง:** owner save/preview → approve/publish → runtime reader  
**หลักฐาน/ข้อจำกัด:** C:store/previewprofile/metadata  
**ตัวเลขที่รายงานไว้:** 602heads;581validityunknown;5conflictedfields;R88ไม่มีapproval/publicationใหม่

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

MigratedViewอ่านlatestdraftheadsและตั้งproduction_publication_verifiedFalse ขณะที่normalstoreอ่านactivepublishedrelease การเห็นข้อมูลใหม่ในpreviewจึงไม่เท่ากับปล่อยใช้จริงได้ด้วยapprovalเดิม

### หลักฐานตัวอย่างจากผลที่เก็บไว้

time-sensitive publishต้องknownvalidityและtrustreview; forecastallunknown581ไม่ใช่581recordsต้องownerกรอกทุกอย่าง เพราะบางkindไม่ต้องtime-sensitiveและfieldsoptional

### พฤติกรรมที่ควรได้

แยกmodeให้ชัดและเลือกcutovercontractที่รักษาreview/revision/publish semantics ไม่ปล่อยdraftหรือfixtureเป็นownerpolicy

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **G→H**

SnapshotProvider ต้องระบุ publication mode; approval ผูก revision/hash; form แสดง draft/published ให้ตรง runtime

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำreadinessreportตามrequired/publish_coreต่อkind sourceauthority/translationhash/relations ไม่ผ่อนvalidatorเพื่อผ่านbatch

### ข้อผิดพลาดใหม่ที่ต้องกัน

preview ผ่านแล้ว agent เปลี่ยน approval หรือสลับใช้ draft ใน production

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

draftnotvisibleinpublished,revisioneditinvalidatesapproval,withdraw/rollback,currentepochandsourcepointertestsโดยไม่แก้ownerfacts

### ทำเองได้แค่ไหน

โค้ดและreadinessทำเอง; factualapproval/policyconfirmationจริงไม่ทำแทนเจ้าของ

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/migrated_view.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/migrated_view.py>) — snapshot
- [common / app/knowledge/common/store.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/store.py>) — approve
- [common / app/knowledge/common/store.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/store.py>) — publish

## P27 — Data-only extensibility ยังจำกัดด้วย vocabulary, relation และ runtime contract

**ตำแหน่ง:** owner new record → discover → plan → render  
**หลักฐาน/ข้อจำกัด:** C:สัญญาในโค้ด; R:ไม่อ้างว่าnewrecordทุกประเภทถูกทดสอบแล้ว  
**ตัวเลขที่รายงานไว้:** fixtureR87growth19checks+rule7checksไม่ใช่ทุกkind/paraphrase

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

เพิ่มrecordในschemaเดียวกันอาจไม่ต้องแก้code แต่ถ้าoperation/fieldmeaning/relationships/newgameeditionไม่เข้าresolverหรือadapterก็ยังตอบไม่ได้ ข้อมูลอย่างเดียวไม่สอนtaskgrammarใหม่โดยอัตโนมัติ

### หลักฐานตัวอย่างจากผลที่เก็บไว้

newAurorapackageราคา/อุปกรณ์ในfixtureผ่าน แต่ไม่ทดสอบliveproductmappingใหม่หรือallpropositionsของทุกหมวด

### พฤติกรรมที่ควรได้

เพิ่มข้อมูลชนิดที่รองรับแล้วต้องเข้าสู่candidate/schema/rendererตามregistryเดียวกัน โดยไม่แก้aliasต่อคำถามหรือใช้sourcefixtureแทนจริง

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→H**

Task registry ต่อชนิดข้อมูล + per-task readiness + automatically rebuilt name/text/relation indexes; new kind ต้องมี versioned contract

กรอบวิธีแก้จากการวิเคราะห์เดิม: taskregistry/schema-description/profilemetadataและrelation-awareprojectionร่วมกันสำหรับknownkinds; schemaใหม่จริงต้องมีversion/migration/rendererdecisionชัด

### ข้อผิดพลาดใหม่ที่ต้องกัน

schema รับ record ใหม่แต่ renderer/dispatcher ไม่มีทางอ่าน หรือทำ per-ID aliases

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

newrecord-only,update/withdraw,newname,heldoutquestionsทุกหมวดและemptyrelatedsource ต้องตรวจdiscoverability+answercoverageไม่ใช่saveได้อย่างเดียว

### ทำเองได้แค่ไหน

โค้ดทำเอง; เนื้อหานโยบายใหม่ต้องsource

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/registry.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py>)
- [common / app/knowledge/common/entity_search.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/entity_search.py>)
- [common / app/knowledge/common/relations.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/relations.py>)

## P28 — คะแนน strict ถูกผูก route/mode/source IDs เดิม

**ตำแหน่ง:** result protocol → historical grader  
**หลักฐาน/ข้อจำกัด:** C:countsและsame-checkerpairedresults  
**ตัวเลขที่รายงานไว้:** 31,649gradesprotocol-only;10,606requestsอยู่primaryprotocol-onlynoliteralfailure

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

commonใช้knowledge/common_read/common_answerและtypedrecordIDs ต่างจากservice_fee/rules/competition modesเดิม แม้bodyบางข้อผ่านliteralก็strictfail บางข้อไม่มีpositivecontractจึงยังบอกไม่ได้ว่าตอบครบ

### หลักฐานตัวอย่างจากผลที่เก็บไว้

legacystrict76.33%กับnew9.02%; samepositivecheckerต่างกัน94.41%กับ72.10% แสดงว่าปัญหาไม่ได้มีแค่protocolแต่ก็ห้ามเรียกstrict9%ว่าaccuracy9%

### พฤติกรรมที่ควรได้

รายงานcompatibility, positivecontent, taskoutcome, source lineageและhumanreviewแยก ไม่เปลี่ยนexpectedให้เข้ากับoutputใหม่เพียงเพื่อคะแนน

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **I**

evaluator adapter แปลง outcomes/source lineage เป็น contract กลาง พร้อมเก็บ strict legacy score เดิมในรายงานต่างหาก

กรอบวิธีแก้จากการวิเคราะห์เดิม: สร้างadapterของevaluatorที่อ่านtypedoutcome/source lineageโดยเก็บstrictlegacycriterionไว้ และทบทวนความหมายของcategory/statusเฉพาะที่อ้างได้

### ข้อผิดพลาดใหม่ที่ต้องกัน

เปลี่ยนเกณฑ์แล้วประกาศคะแนนดีขึ้นเหมือนใช้เกณฑ์เดิม

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

bodyเดียวกันrouteใหม่ต้องcontentเท่าเดิมแต่strictต่างได้; wrongprice/wronggameต้องยังfailแม้routeถูก

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — finish
- [legacy / app/pipeline/engine.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/engine.py>) — _build_result

## P29 — Literal checker มีทั้ง false mismatch และเงื่อนไขที่อ่อนเกินกว่าจะยืนยันคำตอบถูก

**ตำแหน่ง:** expected contract → pass/fail interpretation  
**หลักฐาน/ข้อจำกัด:** C:ตัวอย่างคำตอบคู่; H:ยังไม่คำนวณsemanticaccuracyแท้  
**ตัวเลขที่รายงานไว้:** positive24,909grades; noadditional literal23,714grades

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

คำแปลคนละสำนวน/ชื่อserviceแทนzoneอาจfailแม้relatedfactsถูก ขณะเดียวกันแค่มีคำหรือmarkerบางคำอาจpassทั้งที่scopeยังไม่ครบ ตัวตรวจwordingไม่ใช่semanticjudgeที่รับรองfacts

### หลักฐานตัวอย่างจากผลที่เก็บไว้

ปุ่มยิงกดอะไร:ทั้งคู่ขอชื่อเกม แต่ใหม่ไม่มีหนึ่งในmarker“ยังไม่แน่ใจ/ขอ/ไม่มี”ตามoracleจึงfail; TekkenEnglishclausesอีกสำนวนเช่นกัน

### พฤติกรรมที่ควรได้

เกณฑ์ควรตรวจentity/requiredpropositions/qualifiers/numbers/negation/citations/out-of-scopeextrasพร้อมsource ไม่ยึดstringอย่างเดียวหรือให้LLMjudgeแทนtruth

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **I**

ใช้ needs/required propositions/forbidden claims/numbers/qualifiers/citations; semantic judge เป็นหลักฐานเสริมพร้อม uncertainty

กรอบวิธีแก้จากการวิเคราะห์เดิม: เก็บrawliteralscoreเดิม เพิ่มstructuredneed/sourcecontractและsemanticreviewชั้นต่างหากพร้อมuncertainty ไม่เลื่อนคะแนนใหม่มาแทนเดิมเงียบๆ

### ข้อผิดพลาดใหม่ที่ต้องกัน

LLM judge ให้ผ่านเพราะคำตอบฟังดี หรือ literal keywords ให้ผ่านผิด task

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

meaning-preservingparaphraseต้องแยกจากmeaning-changingnumber/negation/edition และคำตอบยาวที่มีkeywordแต่wrongtaskต้องไม่ถือครบ

### ทำเองได้แค่ไหน

ทำตัวตรวจและanalysisเอง; semanticreview/factualapprovalยังไม่อ้างว่ามนุษย์ทำครบแล้ว

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / tools/eval_contract_v2.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/tools/eval_contract_v2.py>)
- [common / tools/run_competition_contract_r27.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/tools/run_competition_contract_r27.py>)

## P30 — ชุดเฉพาะจุดผ่าน ไม่ได้แทน distribution ของ full corpus

**ตำแหน่ง:** regression selection → coverage claim  
**หลักฐาน/ข้อจำกัด:** C:ชุดคำถาม/จำนวนbridgesและfullscores  
**ตัวเลขที่รายงานไว้:** R87web55/55; R88positive17,960/24,909; ไม่ใช่ตัวชี้วัดชุดเดียวกัน

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

ชุด55เน้นปัญหาที่เพิ่งแก้และกรณีที่รู้ผล Fullมีwrapper,typo,operation,domainและoracleหลากหลายกว่า ความสำเร็จในfixedcasesไม่แปลว่าระบบgeneralizeทุกหมวด

### หลักฐานตัวอย่างจากผลที่เก็บไว้

bridgeprotest2/summary13/rental5finalmethodในfull ขณะที่หลายพันคำถามยังไปexact/ordinaryreader/clarification paths

### พฤติกรรมที่ควรได้

ระบุcoverage matrixตามtask/language/style/needs/sourcekind และใช้heldoutcasesที่ไม่เลือกจากข้อที่รู้ว่าผ่าน

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **I**

ออกแบบ task×language×style×context×data-status matrix และ held-out records/wording; targeted ไม่แทน full

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำtargetedrepair→nearneighbors→heldoutstratified→fullภายหลังตามคำสั่ง ไม่เพิ่มaliasเฉพาะข้อสอบหรือรันซ้ำจนเลือกanswerที่ผ่าน

### ข้อผิดพลาดใหม่ที่ต้องกัน

เลือกเฉพาะโจทย์ที่เพิ่งแก้แล้วประกาศ production ready

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

ตรวจschema/intent/source/equivalenceและstrongnegativeพร้อมpairedbeforeafterจากผลเดิม ไม่อ้าง55/55เป็นproductionaccuracy

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/legacy_intent_bridge.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/legacy_intent_bridge.py>)
- [common / app/knowledge/common/competition_bridge.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/competition_bridge.py>)

## P31 — Root cause บางข้อระบุไม่ได้จาก final answer อย่างเดียว ต้องรักษา rejected plan และ phase timing

**ตำแหน่ง:** trace/audit/progress → diagnosis  
**หลักฐาน/ข้อจำกัด:** C:loggingpaths/timeoutcases; R:instrumentation gapsบางช่วง  
**ตัวเลขที่รายงานไว้:** watchdog2requestsไม่มีfinalworkerresult; no_common_method4,691ไม่เท่ากับalllosthistory

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

outervetoอาจทำให้top-levelplanหายแต่ยังมีrejected_candidate; watchdogอาจไม่มีmodelcallที่กำลังค้างมาถึงparent จึงไม่ควรนับmodel_calls[]ว่าไม่ได้พยายามเรียก; composite/recursiveplansทำให้นับauditซ้ำได้

### หลักฐานตัวอย่างจากผลที่เก็บไว้

SF006traceยืนยันPCscope+relations; foodwatchdog28sไม่มีbodyจึงยังไม่ชี้ว่าsourceขาดหรือโมเดลเป็นต้นเหตุ

### พฤติกรรมที่ควรได้

เก็บstageenter/exit, queuewait,selected/rejectedcandidate, perclauseneeds, source/revision, request/call IDs และfinaldelivery โดยไม่นำข้อมูลองค์กรที่ไม่จำเป็นมารั่วในchat

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **A→I**

ใช้ correlation IDs ต่อ request/task/model call/source; เก็บ selected/rejected plans, reason codes, phase enter/exit และ outcome

กรอบวิธีแก้จากการวิเคราะห์เดิม: เพิ่มstructuredphaseobservabilityที่ไม่แก้decision และanalysisให้นับcall/request/grade/auditeventแยก

### ข้อผิดพลาดใหม่ที่ต้องกัน

นับ audit events เป็น unique requests หรือไม่มี final trace แล้วเดาสาเหตุ

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

inducedparserfailure/modeltimeout/workerrestart/cancellationต้องเก็บphaseเดิมครบและไม่retryคำตอบแล้วทับผลครั้งแรก

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/pipeline/migrated_chat.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py>) — answer
- [common / app/web_api/pipeline_supervisor.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/web_api/pipeline_supervisor.py>)
- [common / app/knowledge/common/planner.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/planner.py>) — _plan_fields_batch

## P32 — Latency และ concurrency มี queue หลายชั้น ไม่ใช่เปิด LLM แล้วตอบพร้อมกันได้ทุกคำขอ

**ตำแหน่ง:** web admission → worker → model gate → HTTP  
**หลักฐาน/ข้อจำกัด:** C:config/admission/elapsed; R:ไม่ใช่loadcapacityรับรอง  
**ตัวเลขที่รายงานไว้:** R88worker2/modelslot1; bulk8,833.08sรวมgrading; watchdog28s/global18s

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

typed/CPUงานบางส่วนขนานได้ แต่โมเดลถูกจำกัด1slotเพื่อทรัพยากรเครื่อง queuewaitกินdeadlineก่อนgeneration ทำให้requestที่รออาจไม่มีbudgetพอ FieldplannereventZeldaรอ5.85sแล้วทำงาน3.46s

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R64ใช้evalmatchingoptimizationsต่างจากruntime; R88coreคำถามเดี่ยว+batchworkersไม่ใช่การวัดเวลาผู้ใช้หนึ่งคนหรือจำนวนuserproduction

### พฤติกรรมที่ควรได้

รายงานqueue/service/totalและp95/p99ตามcohortจริง ไม่ใช้HTTPelapsedของobserverที่หยุดที่headersแทนเวลารวมทุกphase

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B→I**

ลด model calls ที่ไม่จำเป็นด้วย typed tasks และ cache plans ตาม schema/version; จัด global budget/queue deadline; วัดหลัง correctness นิ่ง

กรอบวิธีแก้จากการวิเคราะห์เดิม: ลดLLMที่ถูกเรียกแต่โดนsemanticrejectซ้ำ, cacheเฉพาะแผนที่invalidateตามschema/source, typedtaskfastpaths และadmission/deadlinecontract; ไม่เพิ่มthreadsไม่จำกัดบนGPUเดิม

### ข้อผิดพลาดใหม่ที่ต้องกัน

เพิ่ม threads ไม่จำกัดหรือ cache คำตอบราคานานข้าม release

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

หลังcorrectnessคงที่ค่อยวัดsingle/concurrentmixโดยแยกwarm/coldและtimeout/gate/content ไม่ใช้fullbatchเป็นSLA

### ทำเองได้แค่ไหน

ทำโค้ด/การวัดเองได้; ไม่ปรับทรัพยากรระบบหรือซื้อบริการโดยอนุมาน

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/pipeline/model_admission.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/model_admission.py>)
- [common / app/pipeline/request_deadline.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/request_deadline.py>)
- [common / app/pipeline/llm_health.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/llm_health.py>)

## P33 — Unknown/conflicted fields ไม่ใช่หลักฐานว่าข้อมูลหายทั้งหมด และบางข้อไม่ต้องถามคนใหม่

**ตำแหน่ง:** source readiness → task applicability  
**หลักฐาน/ข้อจำกัด:** C:inventoryและsourceconflictpaths  
**ตัวเลขที่รายงานไว้:** known2,951/unknown1,431/conflicted5fields; 5conflictsเป็นopen_periods

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

optionalmetadataว่างกับข้อเท็จจริงrequiredที่ขาดมีผลต่างกัน recordมีfieldunknownไม่ได้แปลว่าตอบอะไรไม่ได้; ข้อมูลที่ผู้ใช้ยืนยันในsessionแล้วควรใช้เป็นหลักฐานเดิม ไม่ถามซ้ำเพราะmigrationnoteยังเก่า

### หลักฐานตัวอย่างจากผลที่เก็บไว้

5scheduleconflictsnoteค้างเรื่องopen/bookable;12–13bookabilityและVRoccupancyมีhumanconfirmationเดิมอยู่แล้ว

### พฤติกรรมที่ควรได้

ทำtask-levelmissingfacts inventoryว่าอะไรบล็อกคำถามใด และถามเฉพาะข้อที่ต้องตัดสินใหม่จริง

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **H**

สร้าง task-level missing-fact map; optional unknown ไม่บล็อกทุกงาน; confirmation เดิมต้องมี provenance

กรอบวิธีแก้จากการวิเคราะห์เดิม: แยกrequiredtopublish/requiredtoanswer/optional, มีprovenanceของconfirmationเดิม และระบุunknownที่ไม่กระทบคำถามไม่ต้องถาม

### ข้อผิดพลาดใหม่ที่ต้องกัน

บังคับเจ้าของกรอกทุก field หรือเดาเพื่อให้ JSON ดูครบ

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

fieldoptionalunknownต้องยังตอบneedknownได้; requiredconflictห้ามเลือกข้างเอง; confirmationเดิมไม่ถูกลืม

### ทำเองได้แค่ไหน

ทำinventory/mappingเอง; businessfactที่ไม่มีsourceจริงค่อยขอผู้รับผิดชอบ

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/registry.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/registry.py>) — validate
- [common / app/knowledge/common/answer.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/answer.py>) — effective

## P34 — Archive comparison ไม่ใช่ controlled experiment ของ schema อย่างเดียว

**ตำแหน่ง:** test provenance → causal conclusion  
**หลักฐาน/ข้อจำกัด:** C:hash/corpus/configของR64/R88/R89  
**ตัวเลขที่รายงานไว้:** 20,554keys/55,811gradesตรงกัน; dates/engine/data revisionsต่างกัน

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

samecheckerช่วยเทียบคำตอบที่เก็บไว้ แต่old/currentมีvaliditypolicy,source602vsข้อมูลเดิม,interpreter,LLMbudget,caching,referenceclockและerrorpathsต่างกัน จึงไม่ยืนยันว่าJSONschemaกลางทำให้แย่ลงด้วยตัวมันเอง

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R89ไม่มีmodelcalls/requestsใหม่และตรวจhashชุดโจทย์; strictและpositiveคนละความหมาย; ชุดnative/HTTPเก่าคนละsurfaceกับenginebulkใหม่

### พฤติกรรมที่ควรได้

สรุปได้ว่าระบบใหม่ตามผลเดิมไม่ทันตามเกณฑ์นี้ พร้อมชี้causalmechanismจากcode/traceเฉพาะที่มีหลักฐาน

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **A→I**

บันทึก corpus/checker/build/data/reference-clock/LLM config/booking fixture ในทุก comparison; รายงานสาเหตุได้เท่าที่ trace รองรับ

กรอบวิธีแก้จากการวิเคราะห์เดิม: เมื่อแก้ให้ใช้frozenfacts/cohort/dates/tasksเดียวกันเท่าที่ปลอดภัย แยกcompatibility/history/currenttruth; ไม่ทำbaselineใหม่ถ้าผู้ใช้ไม่ขอ

### ข้อผิดพลาดใหม่ที่ต้องกัน

อ้าง causal effect ของ schema จาก archives ที่ตัวแปรอื่นต่างกัน

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

coverage/hash/no-duplicate/gradealignment/sourceimmutabilityและdenominatorทุกตารางต้องตรง

### ทำเองได้แค่ไหน

ทำเองได้

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/migrated_view.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/migrated_view.py>)
- [legacy / app/pipeline/engine.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/engine.py>) — answer

## P35 — ติดตั้ง R78 แล้ว ไม่ได้แปลว่า portable package/เครื่องอื่นมีการแก้ล่าสุดครบ

**ตำแหน่ง:** package manifest → runtime config → real device  
**หลักฐาน/ข้อจำกัด:** R:ขอบเขตที่ยังไม่ได้ยืนยัน ไม่ใช่ข้อผิดพลาดที่วัดแล้วในR88  
**ตัวเลขที่รายงานไว้:** R87ติดตั้ง6codefilesในR78; R88เป็นsnapshot ไม่ได้rebuildportable

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

bridgeใหม่ใช้legacygrammar/routingconfigเป็นdependency ถ้าเอาเฉพาะcommonfilesไปโดยไม่มีmodules/data/rulesที่ต้องใช้ อาจหาintentไม่ได้หรือimportfail ส่วนOllama/model/downloadและtransportmodeต้องตรงเครื่องปลายทาง

### หลักฐานตัวอย่างจากผลที่เก็บไว้

R87reportระบุไม่rebuildpackage; R88ตรวจcodehashกับsnapshot ไม่ใช่ทดสอบcleanWindows/อีกเครื่อง

### พฤติกรรมที่ควรได้

แจกpackageที่มีexactbuild manifest/config/data/modeloptionชัด และhealthบอกversion/profile/model/knowledge sourceจริง

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **I หลัง runtime พร้อม**

ทำ manifest ของ helpers/dependencies/config/data/model options; build สอง package ตาม requirement เดิมภายหลัง

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำreproduciblepackagingdependencyinventoryและstartupdiagnosticsภายหลัง ไม่เปลี่ยนproductionlaunchersในงานเอกสารนี้

### ข้อผิดพลาดใหม่ที่ต้องกัน

R78 แก้แล้วอ้างว่า portable และเครื่องอื่นอัปเดตแล้วด้วย

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

clean-copy offline/online-model variants,relativepaths,portinuse,modelmissing,sourceupdatesและsame-questioncanary

### ทำเองได้แค่ไหน

เตรียมโค้ด/แพ็กเกจทำเองได้ภายหลัง; การติดตั้ง/เผยแพร่จริงตามscopeที่ได้รับอนุญาต

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/build_info.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/build_info.py>)
- [common / app/web_api/server.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/web_api/server.py>)

## P36 — Input guard ตรวจ layout/repeat ได้บางชนิด แต่ไม่ได้แก้เจตนาทั้งประโยค

**ตำแหน่ง:** input quality guard → recovery → semantic task  
**หลักฐาน/ข้อจำกัด:** C:guardmetricsและstageorder  
**ตัวเลขที่รายงานไว้:** 500layoutcasesผ่าน500;repeatdetect471/500 ไม่ใช่accuracytypoของทั้งบอต

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

guardบอกว่าข้อความอาจผิดหรือเตือนเบิ้ล แต่commonยังต้องparseoperationต่างหาก ตัวเลขรุ่น/เครื่องต้องป้องกันไม่ลบซ้ำผิด เช่นPC11ไม่ใช่PC1; ไทยไม่มีช่องว่างและcombiningmarksทำให้editตำแหน่งเดี่ยวไม่พอในหลายcue

### หลักฐานตัวอย่างจากผลที่เก็บไว้

Zeldatasktypoแม้ชื่อชัดยังreject; displaywarningที่พบrepeatไม่ควรแปลว่าคำตอบเลือกintentถูกแล้ว

### พฤติกรรมที่ควรได้

แบ่งdetection,recovery,taskselection,answercorrectnessเป็นคนละmetric และใช้contextเฉพาะที่เชื่อถือได้ช่วยจำกัดcandidate

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **B**

แยก detection/recovery/task-selection/factual-answer outcomes; ไม่ให้ warning ตัวเบิ้ลแทนการพิสูจน์ว่าฟื้นความหมายถูก

กรอบวิธีแก้จากการวิเคราะห์เดิม: แชร์language-awareerrorchannelsและtaskvocabularyพร้อมmargin/negation/numberprotection ไม่reduceallrepeatsหรือใช้neighborทุกตำแหน่งโดยไม่ดูcontext

### ข้อผิดพลาดใหม่ที่ต้องกัน

ตัวอักษรถูกลบแบบ global ทำ edition/จำนวน/ชื่อจริงเสีย

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

Thai/Englishmixedscript,diacritics,missing/repeatedchar,multipleworderrors,legitimateelongation,numericIDsandunknowntexts

### ทำเองได้แค่ไหน

ทำเองได้จากsourceและรูปแบบภาษา; ไม่ใช้caseรายคำเป็นpolicyใหม่

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/core/runtime_input_quality_guard.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/core/runtime_input_quality_guard.py>)
- [legacy / app/pipeline/preprocess.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/system/app/pipeline/preprocess.py>) — preprocess_input

## P37 — Owner preview กับแชทจริงใช้ dispatcher/authority surface ต่างกัน

**ตำแหน่ง:** owner form preview → production-like chat path  
**หลักฐาน/ข้อจำกัด:** C:callpathsต่างกัน; R:ยังไม่วัดfailureทุกหมวดของpreview  
**ตัวเลขที่รายงานไว้:** preview_answerเรียกCommonAnswererตรง; actualchatมีengine+migrated+serverstate/liveadapter

### เพราะอะไร และทำไมมีข้อมูลแล้วยังผิด

previewอาจไม่มีproductscope/greeting/livefallback/outercandidatevetoหรือpersistentdeliveryเหมือนwebchat และdraftpreviewreleaseมีโครงประกอบต่างจากMigratedViewบางส่วน การpreviewผ่านจึงไม่รับรองว่าfullchatถามต่อ/เลือกข้อมูลเหมือนกัน

### หลักฐานตัวอย่างจากผลที่เก็บไว้

owner_server.preview_answerและmigrated_chat.answerเป็นสองentrypointsที่เห็นจากsource ไม่อ้างจำนวนข้อผิดโดยไม่มีการรัน

### พฤติกรรมที่ควรได้

เลือกcanonicalanswercontractเดียวกันหรือประกาศscopepreviewให้ตรงความจริง พร้อมtestconformanceระหว่างpreview/engine/HTTP

### แผนแก้ที่เจาะจง

ช่วงพัฒนา: **G**

owner preview กับ chat เรียก dispatcher contract เดียวกันโดยเปลี่ยน snapshot provider; มี draft capability limits ที่บอกชัด

กรอบวิธีแก้จากการวิเคราะห์เดิม: ทำthinadapterใช้snapshotprovider/dispatcher contractร่วมกันโดยไม่แอบpublishdraftหรือเอาlegacyfactsกลับมา

### ข้อผิดพลาดใหม่ที่ต้องกัน

preview เรียก CommonAnswerer ตรงแล้วอ้างว่า follow-up/live/outer validation เหมือนเว็บ

### เกณฑ์ตรวจในอนาคต — ยังไม่รันรอบนี้

newrecord/update/withdraw,sourceinvalid,qualifiedfollowup,livequery,unknownscopeและsame-questionoutputcontractข้ามsurface

### ทำเองได้แค่ไหน

โค้ดและconformanceทำเองได้; ไม่ให้previewสร้างownerapprovalแทนเจ้าของ

**สถานะตามแผนนี้:** รอ implementation/verification ตามลำดับข้างต้น; candidate ก่อนหน้าที่เกี่ยวบางข้อยังไม่ใช่หลักฐานว่า installed runtime แก้ทั้งหมวดแล้ว

### ไฟล์ที่เกี่ยวข้อง

- [common / app/knowledge/common/owner_server.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/knowledge/common/owner_server.py>) — preview_answer
- [common / app/pipeline/migrated_chat.py](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r88_full_common_llm_20261017/system/app/pipeline/migrated_chat.py>) — answer

