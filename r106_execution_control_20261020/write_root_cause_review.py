"""Assemble an evidence-linked Thai review of the completed, saved run."""
import collections,json,re
from pathlib import Path
B=Path(__file__).resolve().parent.parent;R=B/'r106_complete_flow_20261020';O=R/'full_analysis'
def load(n):return json.loads((O/n).read_text('utf8'))
scores=load('SCORES.json')['by_locale'];counts=load('REVIEW_STREAM_COUNTS.json');methods=load('REVIEW_FAILURE_METHODS.json');extra=load('REVIEW_ADDITIONAL_COUNTS.json');delta=load('REVIEW_GRADER_AND_DELTA_DETAILS.json');comp=load('REVIEW_R95_COMPARISON.json')['by_locale_same_grade_identities'];verify=load('INDEPENDENT_POSTRUN_VERIFICATION.json');samples=load('REVIEW_GROUP_SAMPLES.json');raw=load('REVIEW_SELECTED_RAW_AND_SOURCES.json');source=load('REVIEW_SOURCE_EVIDENCE.json')
def link(label,p):return '['+label+']('+p.resolve().as_posix()+')'
lines=[]
def add(s=''):lines.extend(s.strip('\n').splitlines());lines.append('')
add('''# R106 Full Test — วิเคราะห์สาเหตุแบบตรวจหลักฐานย้อนหลัง

วันที่ทบทวน: 20 ตุลาคม 2026 (Asia/Bangkok)

## 1. ข้อสรุปที่ใช้ตัดสินใจได้

Full workload รันครบแล้ว แต่ยังไม่ควรประกาศว่า candidate พร้อมส่ง production หรือดีกว่า R95 โดยรวม คะแนน strict แทบไม่เปลี่ยน และ positive literal-content checks ลดลงทั้งไทย อังกฤษ และ auto เทียบคำถามและ grade identity เดียวกันของ R95 ที่บันทึกไว้

สาเหตุไม่ได้มีเพียง “LLM ตอบผิด” หรือ “ข้อมูลหาย”:

1. เกณฑ์เก่าคาด route/intent/mode และ source ID ของระบบเดิม ขณะที่ common ตอบผ่าน category `knowledge` จึงตก strict จำนวนมากแม้มีข้อความตอบที่เกี่ยวข้อง
2. ข้อมูลข้อความย้ายมาแล้วหลายส่วน แต่ metadata ที่ Flow ใหม่บังคับใช้ยังไม่พร้อม โดยเฉพาะ `completeness`, วันมีผลราคา, `public_scope` และความหมาย open/bookable/maintenance
3. Flow ยังมี compatibility branches ที่เลือก/แสดงข้อความได้ แต่ coverage contract ยังเป็น `scope_unverified`; การมี source hit จึงยังไม่ยืนยันว่าตอบ proposition ของผู้ใช้ครบ
4. พบปัญหาจริงด้านการเลือกประเด็น การตอบหลายส่วน และภาษาอังกฤษปนไทย มีตัวอย่างยืนยันจาก raw answer และ source อยู่ในรายงานนี้
5. พบ timeout ของ model HTTP และ watchdog ระดับ request แยกต่างหากจากความถูกต้องของเนื้อหา

รายงานนี้อ่านผลที่บันทึกไว้ ไม่มีการถามแชทซ้ำ ไม่มี baseline rerun ไม่มีแก้ frozen system, real data, approvals, input หรือ original logs เพื่อให้คะแนนดีขึ้น

**ขอบเขตการยืนยัน:** อ่านและจัดกลุ่มทุก failure row แบบ streaming แล้วตรวจตัวอย่างพร้อม source/code ของแต่ละกลุ่มหลัก การจัดกลุ่มครบไม่เท่ากับตัดสิน semantic ทุกคำตอบครบ ไม่สร้างตัวเลข “actual semantic accuracy” จาก keyword grader กรณีที่ยังไม่ได้ตรวจ proposition เทียบ source รายข้อยังระบุเป็น `review_pending`
''')
add('## 2. ตรวจความครบและความคงเดิมอย่างอิสระ')
add(f'''- อ่าน raw results จริง {verify['requests']:,} แถว / {verify['unique_keys']:,} unique keys / {verify['grades']:,} grades
- ไม่มี key ขาด เกิน หรือซ้ำ และ Counter ของ `(file,row,variant,id)` ต่อ request ตรงกับ input ทุก key จึงตรวจลึกกว่าการเทียบจำนวน grades รวมอย่างเดียว
- ตรวจ hash source {verify['source_files_verified']:,} ไฟล์ และ frozen inputs {verify['frozen_input_files_verified']} ไฟล์: ไม่มีการเปลี่ยน
- hash ของ FULL_JOBS ตรง FULL_INPUT ที่ supervisor เก็บก่อนเริ่ม
- model digest ก่อนและหลังตรงกัน: `b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05`
- model identity verification เป็นการยืนยันรุ่นที่ใช้ ไม่ใช่การยืนยัน semantic answer correctness ทุก request
- 18 requests จบด้วย watchdog failure แต่ยังมี execution-failure grades ครบตาม input จึงกล่าวได้ว่า coverage ครบ ไม่ใช่กล่าวว่าทุก request ได้คำตอบสำเร็จ
''')
add(link('หลักฐานการตรวจซ้ำ',O/'INDEPENDENT_POSTRUN_VERIFICATION.json')+' · '+link('Completion marker',R/'FULL_TEST_COMPLETE.json')+' · '+link('Coverage เดิม',O/'COVERAGE.json'))
add('''## 3. คะแนนแยกภาษา และการเทียบ R95 ที่บันทึกไว้

Strict = ผ่านทุกข้อใน grader ของ grade นั้น รวม protocol/outcome/text/evidence/performance ตามเกณฑ์เดิม

Positive literal-content checks = grade มี positive text assertion และไม่ตก partition content/evidence/validation/grader ตามตัวแยกเดิม ไม่ใช่การอ่าน semantic โดยมนุษย์ และไม่ได้เป็นจำนวนคำถามอิสระ
''')
add('''| ภาษา | Requests | Strict R95 → R106 | Positive literal R95 → R106 (grade เดียวกัน) | Model HTTP สำเร็จ/สังเกตได้ |
|---|---:|---|---|---|''')
for loc in ['th','en','auto']:
 v=comp[loc];s=scores[loc]
 add(f"| {loc} | {s['requests']:,} | {v['r95_strict']:,}/{v['shared_grades']:,} ({100*v['r95_strict']/v['shared_grades']:.2f}%) → {v['r106_strict']:,}/{v['shared_grades']:,} ({100*v['r106_strict']/v['shared_grades']:.2f}%) | {v['r95_positive']:,}/{v['shared_positive']:,} ({100*v['r95_positive']/v['shared_positive']:.2f}%) → {v['r106_positive']:,}/{v['shared_positive']:,} ({100*v['r106_positive']/v['shared_positive']:.2f}%) | {s['model_transport_success']:,}/{s['model_calls']:,} |")
add('''เทียบ R95 ที่ retained ไว้ครบ 20,554 shared keys และ 55,811 shared grade identities: strict ดีขึ้น 27 grades ถอยลง 38 grades สุทธิ -11; positive checks บน intersection ดีขึ้น 1,778 ถอยลง 2,814 สุทธิ -1,036

**ไม่ใช่ causal effect ของ Flow ล้วน ๆ:** migration source data/metadata ของ R95 กับ R106 ต่างรุ่นกันด้วย ผลนี้จึงบอกพฤติกรรมของ candidate ทั้งชุด ณ เวลาทดสอบ ไม่สามารถยกส่วนต่างทั้งหมดให้ algorithm ใหม่ หรือสรุปว่าข้อมูลเดิมหายทั้งหมดได้

R95 ในตารางนี้คือ saved common R95 baseline ไม่ใช่การรัน legacy ใหม่ และไม่ใช่การเทียบ production R78 สด
''')
add(link('Comparison ราย grade',O/'REVIEW_R95_COMPARISON.json')+' · '+link('Strict deltas เดิม',O/'VS_R95_STRICT_CHANGES.json'))
add('''### 3.1 ข้อจำกัดของ metric ที่ต้องเปิดเผย

- watchdog failure 18 requests ส่ง grades เป็น `pipeline_exception` รวม 49 grades และตั้ง `positive_text_contract=false` ทั้งหมด ในจำนวนนี้ input เดิมมี positive assertion 18 grades (ไทย 16 อังกฤษ 1 auto 1) จึงไม่รวมใน positive denominator เดิม หากนับ execution failure เหล่านี้เป็นไม่ผ่านด้วย denominator จะเป็นไทย 13,142 อังกฤษ 9,466 auto 2,301 โดย numerator เดิมไม่เพิ่ม
- ตัวแยก failure partition ใน `run_common.py` ใช้การพบ substring `latency` หรือ `timeout` ก่อนแยก content ทำให้ `missing all alternatives: ['latency', ...]` และ `missing_complete_clause: ... Timeout ...` ถูกนับ performance ทั้งที่เป็น text mismatch
- พบการจัด bucket เช่นนี้ 72 failure events: missing alternatives 66 และ missing complete clause 6; 66 grades ในกลุ่ม alternatives ถูกนับ positive-pass เดิมเพราะไม่มี content/evidence/validation/grader failure อื่น (ไทย 38 auto 28) จึงไม่ควรยก positive metric เดิมเป็นความถูกต้อง semantic หรือแก้ทับคะแนนย้อนหลังเงียบ ๆ
- `wrong_category` ของ composition grader ถูกอยู่ content ทั้งที่เป็น protocol ทำให้ positive check บางกรณีถูก penalize ด้าน protocol ด้วย ต้องแก้ taxonomy ใน evaluator รุ่นถัดไปพร้อม version ใหม่
- native quality gate, source ID mismatch, heading/first-line mismatch และ substring ในประโยคปฏิเสธล้วนต้องอ่านคำตอบจริงก่อนตัดสิน
''')
add(link('รายละเอียด taxonomy และ delta',O/'REVIEW_GRADER_AND_DELTA_DETAILS.json'))
add('## 4. ภาพรวมกลุ่มความผิดพลาด — ห้ามรวมเป็น actual content failures')
add(f"Raw requests ที่มี grade ไม่ผ่านอย่างน้อยหนึ่งข้อ = {counts['stats']['failed_requests']:,}; ในนี้ {counts['stats']['protocol_only_requests']:,} requests มีเฉพาะ protocol partition และ {counts['stats']['positive_failure_requests']:,} requests มี positive grade ที่ตกตัวกรอง content/evidence/validation/grader เดิม ตัวเลขเหล่านี้ไม่ใช่จำนวนคำตอบผิด semantic")
add('''| Partition เดิม | Distinct failed requests ที่เกี่ยวข้อง | คำอธิบาย |
|---|---:|---|''')
explain={'protocol':'ชื่อ route/intent/mode และ source namespace ที่ oracle คาด','content':'ข้อความ/keyword/clause หรือ native category check ยังต้องตรวจความหมาย','evidence':'canonical fact/rule identity หรือ rulebook target','outcome':'answer/clarification/no-answer classification ตามเกณฑ์เก่า','performance':'มีทั้ง latency จริงและข้อความที่มีคำ timeout/latency ซึ่งถูกจัด bucket ผิด','validation':'18 execution-failure requests / 49 grades ไม่ใช่ 49 คำตอบที่ validator จับ hallucination'}
for k,n in methods['distinct_requests_by_partition'].items():add(f'| {k} | {n:,} | {explain.get(k,"review_pending")} |')
add('กลุ่มทับซ้อนกันได้ ห้ามนำจำนวน requests หรือ failure events มาบวกแล้วอ้างเป็นจำนวนคำตอบผิดทั้งหมด')
add('''## 5. ปัญหาที่ตรวจยืนยันจาก source/code ได้

### 5.1 ข้อกติกามีข้อความ แต่ gate บังคับ completeness จนตอบข้อเฉพาะไม่ได้

ตัวอย่าง `6b55634a8f5ecc0fd3f2efddcf577cce3445e749cefe737d4d1c18adfd64bda5`:

> Under CS2 tournament rules, list the equiment that organizers provide.

ตอบจริง: `The clause or its required references are incomplete; this rule cannot be confirmed.`

ฐานข้อมูลมี record `competition_competition_rules_cs2_psu_phuket_2026_section_043` โดย `text.en` ระบุว่า `3. The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs.` พร้อม evidence source `r66_en_805e25f3040efc0d59084835` แต่ `completeness.status=unknown` และ `depends_on_ids.status=unknown`

`rules_reader.py` ตรวจ `value(completeness) != 'complete' and not reference_only` แล้วออก `_gap` ก่อน render ข้อความ เงื่อนไขนี้ทำให้ reference รวมบางแบบแสดงข้อที่มีได้ แต่คำถามเจาะข้อถูกปฏิเสธ ข้อความไม่ได้หายเสมอไป; coverage metadata กับ execution gate ไม่สอดคล้องกับระดับคำตอบที่ยอมให้แสดง

ยืนยันเพิ่มจาก record `_section_034` ของ CS2: มี 4 timeouts/team, 30 seconds, Freeze time; และ VALORANT `_section_006`: 2 ครั้งใน regulation, 60 วินาที และ overtime เพิ่ม 1 ไม่ทบโควตา ทั้งหมดมีข้อความ แต่ completeness ของ competition_rule ทั้ง 104 records เป็น unknown

ใน failed sink มี method `r103_rule_dependency_gap` 2,537 requests และ reason `rule_dependency_incomplete` 2,533 distinct requests (จำนวนไม่เท่ากันเพราะ aggregate/branch metadata); ไม่อ้างว่าทุก request ในกลุ่มนี้มีคำตอบสมบูรณ์อยู่จริง ต้องตรวจ relation/qualifier รายข้อ

**สิ่งที่ควรแก้:** แยก full-rulebook completeness, selected-clause integrity และ applicability; จัดสถานะ `quoted_partial_source` เมื่อข้อความข้อที่ถามมีหลักฐานครบ แต่ห้ามยกเป็นการตัดสินอนุญาต/ลงโทษถ้ายังขาด exception/dependency; ตรวจ clause boundary และ dependencies จาก snapshot โดยอัตโนมัติก่อนเสนอ review ห้ามตั้งทั้ง 104 ข้อเป็น complete โดยไม่มีหลักฐาน

### 5.2 คำถามเฉพาะเรื่องที่ไม่มี source กลับ dump กติกาคนละหัวข้อ

ตัวอย่าง `b61dd910b704abc38637c18169f715cc7c3ebbad66151158a685ff670f1f0439`:

> ถ้าผู้เล่น VALORANT พูดหยาบหรือแสดงพฤติกรรมไม่เหมาะสมจะโดนโทษอะไร

ตอบจริงเริ่มด้วยกติกา VALORANT และข้อสงวนสิทธิ์ผู้จัด จากนั้นยาวไปถึงอุปกรณ์ มาโคร โปรแกรม และ bugs; artifact ระบุ `task=unresolved`, `status=scope_unverified`, `compatibility_scope_not_migrated`, method `exact` แต่ mode เป็น `common_answer`

นี่เป็นปัญหาความเกี่ยวข้องที่ยืนยันได้: คำถามถามโทษของ conduct แต่ไม่มีคำตอบตรงประเด็นในข้อความที่ส่ง ไม่จำเป็นต้องเรียกว่าประดิษฐ์โทษขึ้นเองเพราะตัวอย่างไม่ได้ยืนยันว่ามีการแต่งโทษใหม่ ส่วน oracle ระบุ active source gap ต้องเทียบ source clause ปัจจุบันก่อนสรุปว่าทั้ง 84 failure events ของชนิดนี้ผิดเหมือนกัน

**สิ่งที่ควรแก้:** ทุก fallback ต้องผ่าน relevance/coverage ของ proposition เดียวกับ typed path; ถ้าไม่มี conduct clause ให้ตอบว่าข้อมูลโทษส่วนนี้ยังไม่มี และไม่แทนด้วย overview ทั้งเล่ม การขอ “กติกาทั้งหมด” ต้องเป็น explicit user intent แยกจากการถามรายละเอียดข้อเดียว

### 5.3 สนามคำถามหลายส่วนยังตกหล่นหรือไม่ระบุ unknown เป็นรายส่วน

ตัวอย่าง `3e332262f02c76f494c20c8adda6c4d07dad078a4fb19b09710f256c0baf321f`:

> Under CS2 tournament rules, are scripts allowed and what is the registration fee?

ตอบจริงเพียง `The selected source does not directly confirm the requested detail.` ไม่มีการแยก scripts และ registration fee ทั้งที่ `_section_046` มีข้อห้าม scripts/macros อยู่ และค่าธรรมเนียมเป็นอีก source need หนึ่ง

**สิ่งที่ควรแก้:** แยก need ก่อนเลือก source, ตอบส่วนข้อความที่ยืนยันได้พร้อมข้อจำกัดของ completeness แล้วระบุเฉพาะค่าสมัครว่ายังไม่มีข้อมูล ไม่ให้ missing อีกส่วนทำให้ known ส่วนแรกหาย และไม่ให้ known ส่วนแรกสร้างภาพว่าตอบครบแล้ว เคสนี้คือ coverage/communication defect; ไม่ใช่หลักฐานว่าระบบแต่งราคาค่าสมัคร

### 5.4 Graph ของ schedule อาจบล็อกข้อมูล maintenance ที่ทราบเพราะ open_periods conflicted

ตัวอย่าง `8bda4c2959af2685ea45665765197d4d0bbe24ecb334d3b707118ca447a419b0` ถามเรื่องวันศุกร์ maintenance แต่ตอบ generic linked data invalid/unconfirmed; task=schedule, status=conflict, method=`r102_invalid_graph_dependency`

`migrated_schedule_4.maintenance_periods` เป็น known 13:00–16:00 พร้อม source `r66_8b8799fa0b0f242ce50dede11782`; bookable เป็น known 09:00–12:00 แต่ open_periods เป็น conflicted จากสองแหล่ง Raw request_plan ของตัวอย่างนี้เลือก predicate `service_schedule` แทน `maintenance_period` แล้ว graph จึงเลือก required field เป็น open_periods

ตรวจ code `read_graph.compile` แล้วมีการรองรับ maintenance_period → maintenance_periods อยู่แล้ว จึงไม่ควรอธิบายว่า graph ไม่รองรับการแยกเลย จุดผิดที่ยืนยันในตัวอย่างคือการเลือก/ส่ง predicate สูญเสียความเฉพาะของคำถามก่อนเข้า graph และผลสุดท้ายบล็อก maintenance ด้วย conflict ของ opening

**สิ่งที่ควรแก้:** สร้าง required fields ตามคำถามย่อย: maintenance ใช้ maintenance_periods, จองได้ใช้ bookable_periods, เปิดพื้นที่ใช้ open_periods โดยไม่สรุปสามความหมายแทนกัน ถ้าถาม “เปิดไหม” จริงและ open conflicted ให้คง conflict พร้อมคำอธิบายตรงประเด็น ไม่เอาเวลาที่จองได้มาอ้างว่าเปิดพื้นที่แน่นอน

### 5.5 คำตอบอังกฤษมีข้อความไทยที่ถูกเก็บอยู่ใน structured value

ตัวอย่าง `099e9aaaf0cdad44be5fdd3a45e47afecb446fff5edca84822b71286bd1f4d2f` ถามอังกฤษเรื่อง MSI Gaming PC แต่ `specifications` แสดง `recorded_source_detail` เป็นภาษาไทย และแสดง `unit: None` ในคำตอบผู้ใช้

source `equipment_gaming_pc.fields.specifications.value` เป็น list ของ key/unit/value ซึ่งมี raw Thai detail; ไม่ใช่ bilingual value ต่อ entry แม้ usage มี en อยู่แล้ว renderer จึงพ่น source ไทยออกมาตรง ๆ อีกตัวอย่าง It Takes Two ใช้ button label `Cross (กากบาท)` ในอังกฤษ

23 failure events ของ English Thai prose flag ไม่เท่ากับ 23 semantic translation errors: ชื่อบุคคลไทย ชื่อปุ่มสองภาษา และย่อหน้าไทยเต็มมีนัยต่างกัน ต้องแยก แต่ย่อหน้า Thai specs เป็น localization/rendering defect ที่ยืนยันได้

**สิ่งที่ควรแก้:** รองรับ localized structured entries หรือรักษา language ของแต่ละ cell; แยก stable technical keys เช่น CPU/GPU จากข้อความบรรยาย; ซ่อน null units; ห้ามใช้ข้อความไทย fallback เงียบ ๆ ว่าแปลแล้ว; translation draft ที่ไม่มี en ให้แจ้งข้อจำกัดและไม่เปลี่ยน fact

### 5.6 ยังมีการจับประโยคผิดและ fallback ไป source ที่ไม่ตอบคำถาม

ตัวอย่าง `b87fe52b3b8d3161f23c762b061b3c8b5dcb6f068ef39426dab892b98dad498d` ถามนิยาม latency แต่ตอบสรุปจองล่วงหน้าและเช็คอินจาก FAQ task=faq_content, coverage=scope_unverified

ผู้ใช้จำกัดขอบเขตไว้เรื่องศูนย์/ร้านเกมแล้ว จึงไม่ต้องทำให้ตอบนิยามทั่วไปทั้งหมดตาม oracle เก่า แต่เมื่อคำถามไม่อยู่ใน data scope ต้องปฏิเสธ/ถามเพิ่มอย่างตรงประเด็น การเอาขั้นตอนจองมาตอบเป็น relevance bug จริง

อีกกลุ่มคือ typo ของ role/ปุ่ม/คำถามสั้นที่จบ `no_accepted_interpretation` กลุ่มนี้มี 2,103 distinct failed requests แต่รวมทั้งคำกำกวมจริง คำผิด และ out-of-domain จึงยังไม่จัดทั้งหมดเป็น parser defect

**สิ่งที่ควรแก้:** task/subject/qualifier/span validation ก่อนอ่าน source; ใช้ domain-aware typo recovery โดยรักษาชื่อเกมและตัวเลข; semantic planner เสนอแผนได้แต่ต้องตรวจว่าพยาน source ตอบ predicate ของผู้ใช้จริง; ไม่ให้คำว่า “สรุปเป็น 2 ข้อ” เลือก FAQ ที่ชื่อเกี่ยวกับสรุปแทนหัวข้อหลัก
''')
add('''## 6. กลุ่มที่ตก test แต่ยังไม่ใช่หลักฐานว่าตอบข้อเท็จจริงผิด

### 6.1 ราคาเก่าหมดช่วงมีผล และ price basis ยังไม่ครบ

ตัวอย่างนักศึกษา PSU เล่น Nintendo Switch: คำตอบปฏิเสธยืนยัน current rate โดยอ้างช่วง 1 ก.พ. ถึงก่อน 1 เม.ย. 2026 ฐาน `migrated_rate_*` มีช่วงดังกล่าวจริง และ runner ใช้เวลาอ้างอิง 16 ต.ค. 2026 เมื่อ job ไม่มี reference_date

VR PSU Student and Staff 60 นาทีมี amount_minor=0 แต่ `unit` กับ `calculation_rule` unknown จึงไม่ควรขยายเป็นราคาหลายชั่วโมง/หลายคนตามใจ แม้ oracle อยากได้ “0 บาท” ส่วน recovered PC มี session_ceil และ per_session จาก source แต่ validity unknown

reason source_not_effective พบ 1,238 distinct failed requests; เป็นสัญญาณ data applicability ไม่ใช่ 1,238 hallucinations ยังมี UX/parser risk แยก เช่นคำถามระบุ PSU Student แล้วคำตอบ exact branch ยังพ่นหลาย audience ที่หมดอายุ แทนจำกัดให้กลุ่มที่ถาม

**แนวแก้:** owner workflow ระบุ effective dates, pricing unit, audience/service relation และ rounding rule; แสดง historical quote พร้อมวันที่ได้เฉพาะเมื่อผู้ใช้ถามประวัติ; ห้ามขยายวันหมดอายุเองเพื่อให้ keyword test ผ่าน

### 6.2 บุคลากรมีชื่อ/ตำแหน่ง แต่ public_scope ยังไม่ยืนยัน

ตัวอย่าง “ใครเป็นประธาน” (`7dc03c3b0e66f7715b048135bee92796f7043e0cb9f126d22a2f0fddafbbdd9b`) ตอบยังยืนยันขอบเขตเปิดเผยไม่ได้ source ของ `member_1d884f11f3890dea` มีชื่อและ role ประธาน แต่ public_scope unknown จึงตรงกับ guard ใหม่ ไม่ใช่ชื่อหายจาก DB

reason person_public_scope_not_confirmed พบ 222 distinct failed requests; positive regressions จำนวนมากเป็น unsupported status (1,323 grades ใน comparison) มีผลจาก gate นี้ แต่ยังไม่ควรเหมา unsupported ทุกข้อเป็นบุคลากรจนกว่าจะ join ราย grade

**แนวแก้:** แยก public directory role/title จาก contact details ที่ต้องมี scope; owner ต้องมีช่องเลือก scope และ provenance ชัดเจน การนำชื่อจากข้อมูลเดิมมาได้ไม่ได้แปลว่าได้อนุมัติเผยแพร่ข้อมูลทุกช่องแล้ว

### 6.3 Unknown relation, inventory scope และ qualifiers

- `r104_required_relation_missing` 218 distinct failed requests: ต้องตรวจว่าข้อมูลใหม่ยังไม่เชื่อม game_service/control_set หรือ resolver หา relation ไม่เจอ ไม่ตัดสินว่าแต่ละรายการไม่มีบริการจริง
- `r103_inventory_scope_unknown` 39: การมี equipment model ไม่ยืนยันจำนวน physical units หรือจำนวนที่ว่าง
- `r101_qualifier_source_gap` 47: เงื่อนไขเช่นพร้อมกัน แพลตฟอร์ม ช่วงเวลา บัญชีของศูนย์ ไม่ได้ตามมาจากชื่อเกมอย่างเดียว
- `explicit_pending_selection` 825: หลายอัตราต้องถาม audience/service เพิ่มได้ แต่ควรเก็บ state และถามเฉพาะ slot ที่จำเป็น ไม่เริ่มถามหัวข้อใหม่เมื่อตอบชื่อสั้น ๆ
- กลุ่มทั้งหมดต้องแยก data missing กับ relation resolver defect ด้วย source snapshot ห้ามเติมคำตอบจากความรู้ทั่วไปของ LLM

### 6.4 หลักฐานแบบ ID mismatch และ wrong-game flag

Old canonical IDs เช่น `competition_rules_cs2_psu_phuket_2026_s43_c01` เปลี่ยนเป็น common section ID `competition_competition_rules_cs2_psu_phuket_2026_section_043`; field hits อาจมี suffix field/label อีกด้วย การเทียบ ID ตรงตัวโดยไม่มี provenance crosswalk จึงแพ้ได้ทั้งที่เนื้อหา/เกมตรงกัน

R27 grader ตั้ง wrong_game_evidence เมื่อ `not hits` ด้วย ตัวอย่าง refusal ไม่มี hits จึงได้ flag นี้ ไม่ใช่มีหลักฐานว่าเอากติกาเกมอื่นมาปนจริง ต้องเปิด hit_count/source ของแต่ละ request ก่อนนับ wrong-game contamination

**แนวแก้:** canonical evidence identity crosswalk จาก origin hash+locator+common record field พร้อมตรวจ game/event boundary; semantic entailment ของข้อความแยกจาก source identity; ไม่เปลี่ยน evaluator ให้ยอมทุก common ID โดยไม่ตรวจ source

### 6.5 Keyword, first-line และ negation false positives

- “เอาอาหารเข้าได้ไหม” ตอบอนุญาตเฉพาะพื้นที่กำหนดพร้อม source แต่มี native quality gate failure และ route mismatch ตัวอย่างนี้ให้สาระตรงคำถาม; native failure ไม่เพียงพอที่จะเรียกคำตอบผิด
- “คนนอกเข้าไปเล่นได้ทุกเกมเลยไหม” ตอบ “ยังยืนยันไม่ได้ว่าบุคคลภายนอกเล่นได้ทุกเกมครับ...” แต่ substring forbidden `เล่นได้ทุกเกมครับ` ยังอยู่ภายใต้ประโยคปฏิเสธ และ must_contain เว้นวลีไม่ตรง จึง fail ทั้งที่ปฏิเสธการยืนยันจริง
- first_line_off_topic มี 702 events แต่ในหลายตัวอย่างคำตอบเป็น refusal จาก completeness gate จึงไม่ใช่เพียงหัวเรื่องสลับลำดับ; ส่วนคำตอบถูกแต่มีหัวข้อก่อนก็ต้องแยกเป็น presentation mismatch
- complete-clause exact match อาจไม่ยอมรับคำแปลต่างถ้อยคำ/เลขข้อ/grammar ซึ่งต้องเทียบ proposition, quantity, condition และ exception ห้ามนับทั้งหมดว่าผิด semantic

**แนวแก้:** คง literal metrics เพื่อเทียบย้อนหลัง แต่เพิ่ม proposition-based checks และ negation-aware adjudication เป็นอีก layer; เก็บกรณี undecided ไว้ ไม่ใช้ LLM judge ตัวเดียวสร้าง pass ทั้งหมด
''')
add('''## 7. Transport, deadline และเวลา — แยกจาก correctness

- Model HTTP ที่ observe ได้ 4,307 attempts, 4,292 transport successes, 15 timeouts (`TimeoutError: timed out`) ไม่แปลว่ามีเพียง 15 semantic failures และ successes ไม่ยืนยันว่า planner ตีความถูก
- Watchdog 18 requests หยุดรอที่ 28 วินาทีและ restart worker: 11 ไทย, 6 อังกฤษ, 1 auto; 49 grades ถูกนับ execution_failure ไม่มีคำตอบให้ตรวจ semantic
- Killed worker อาจยังส่ง observation ของ in-flight model call กลับมาไม่ทัน จึงไม่ควรใช้ observed 4,307 เป็นหลักฐานว่ารวม network attempts ทุกตัวที่เริ่มแล้วอย่างสมบูรณ์
- มี latency_ceiling failure จริง 28 grades จาก 11 requests แยกจากข้อความที่มีคำ timeout/latency ซึ่งถูก misbucket
- LLM ON คือเปิดให้ router ใช้ LLM เมื่อจำเป็น deterministic source reads/calculators ไม่ต้องเรียกโมเดลทุกคำถาม การใช้ request count เป็นจำนวน generation จึงผิด

**แนวแก้:** propagate absolute deadline เดียว, bounded admission/queue wait ที่รู้เวลาคงเหลือ, timeout reason แบบแยก queue/model/parser/store, เก็บ call event ที่ parent ก่อนเริ่มและหลังเสร็จเพื่อไม่สูญหายเมื่อตัด worker, ไม่ retry อัตโนมัติข้ามงบเวลา request; ไม่เพิ่ม concurrency โดยไม่ดู VRAM/latency

## 8. ทำไม targeted gates ผ่าน แต่ full workload ยังได้ผลแบบนี้

R105 เคยตรวจ integrated 19 lanes แล้ว; R106 เปลี่ยน runtime 5 ไฟล์และรันเฉพาะกลุ่มที่ได้รับผลก่อน Full Test: model readiness 1/1, updated contracts 25/25, retained contracts 59/59, retained V2 17/17, task matrix 248/248 และ acceptance 444/444

หน่วยของแต่ละ lane ต่างกัน ห้ามบวกเป็นความแม่นยำเดียว และ 444/444 คือ 37 scenarios หลายภาษา/variant ของ acceptance ไม่ได้แทน 20,554 request keys

Synthetic owner fixtures ให้ completeness/relations/validity ชัดเจนเพื่อพิสูจน์กลไก; real migrated DB มี 602 heads, approvals 0, releases 0, unknown/conflicted metadata จำนวนมาก จึงผ่านกลไกเพิ่มข้อมูลใน fixture ได้พร้อมกับใช้งาน migration จริงแล้วถูก gate บล็อก ความต่างนี้เป็นช่องว่าง test representativeness และ data readiness ที่ต้องแก้ก่อนส่งจริง

Compatibility task parsers ยังอยู่ รายงานเหตุ compatibility_scope_not_migrated ใน failed sink 1,853 distinct requests การออกคำตอบผ่าน branch เหล่านี้ไม่ได้รับ semantic verification ครบแล้ว แม้จะมี typed claim receipt ของบาง field

ดู `LINEAGE.json` สำหรับ inherited lanes และ changed files ไม่อ้างว่า R106 rerun ทั้ง 19 lanes ใหม่ทั้งหมด

## 9. Workload ยังมีคำถามนอกเป้าหมายและสัญญาทดสอบเก่า

พบ `general_llm` 275 requests ที่ oracle เดิมต้องการให้ตอบความรู้ทั่วไปทั้งหมด; mode ผลลัพธ์กระจายเป็น migrated clarification 165, common_answer 70, common_clarification 37, studio_scope_no_answer 2 และ common_unavailable 1

ผู้ใช้กำหนดแล้วว่าไม่ต้องตอบทุกเรื่องนอกข้อมูลศูนย์/ร้านเกม จึงไม่ควรแก้ระบบให้ตอบทุกนิยามทั่วไปเพื่อไล่คะแนนชุดนี้ บางคำถามเทคนิคอาจอยู่ในหมวดเกมได้ถ้ามี source ที่เจ้าของใส่ แต่ไม่ได้แปลว่าอนุญาต general-knowledge fallback ไม่มีหลักฐาน

70 common_answer ไม่ใช่หลักฐานว่าตอบนอกโดเมนถูกทั้งหมด ตัวอย่าง latency ที่ตอบเรื่องจองเป็นความผิดด้าน relevance จริง ดังนั้นต้องแยก old oracle mismatch จาก unsafe irrelevant substitution

คะแนนรวมเดิมยังเก็บไว้โดยไม่ลบเคสย้อนหลัง รอบหน้าควร freeze domain-scoped acceptance ใหม่พร้อมรายงาน out-of-scope abstention อีกตาราง และเก็บ strict legacy comparison ต่างหาก
''')
add('## 10. Delta R95 → R106 บอกอะไรได้และยังบอกอะไรไม่ได้')
add('''| ทิศทาง / สถานะ need ของผล R106 | Positive grade changes |
|---|---:|''')
for k,n in delta['positive_change_grade_statuses'].items():add(f'| {k} | {n:,} |')
add('''สถานะเหล่านี้เป็นเหตุใน artifact ของ request ที่มี grade เปลี่ยน ไม่ได้พิสูจน์ causal cause ของแต่ละ grade โดยลำพัง ตัวอย่าง Resident Evil Village ถามราคาพิมพ์ผิด: R95 ถามว่าอยากรู้เรื่องเกม/วิธีเล่น/ปุ่มอะไร ส่วน R106 ถาม audience สำหรับราคา ตัวใหม่เข้า intent ราคาดีกว่าแต่ไม่มีชื่อเกมในคำตอบจึงตก literal ที่เดิมผ่านได้ด้วยการ echo ชื่อเกม นี่แสดงว่าทั้ง “คะแนนถอย” และ “คะแนนเพิ่ม” ต้องอ่านคำตอบคู่ source ก่อนสรุปคุณภาพ

พร้อมกันนั้นมี regressions ที่ source gate ทำให้ข้อมูลที่ต้องการไม่ออกจริง เช่นบุคลากรและตารางเวลา และมีการปรับ interpretation ที่ตอบข้อความเพิ่มได้จริง สรุปที่ถูกต้องคือ candidate มีทั้งข้อดีและข้อเสีย; aggregate literal-content ยังลดลงและยังไม่พร้อมอ้างว่าดีกว่าทุกหมวด
''')
add('''## 11. ลำดับแก้ที่เสนอหลังจบรอบนี้ (ยังไม่ได้แก้ frozen R106)

| ลำดับ | สิ่งที่ต้องทำ | หลักฐานก่อนยอมรับ | ส่วนที่ทำเองได้ / ต้องรอเจ้าของ |
|---|---|---|---|
| P0 | Predicate dependency isolation สำหรับ schedule/people/rules | เปลี่ยน field ที่ไม่เกี่ยวข้องไม่ทำให้ known answer ของ predicate หลักหาย; source gap ที่เกี่ยวจริงยังถูกบล็อก | โค้ดและ source audit ทำเองได้; open semantics จริง/permission ต้องมีเจ้าของยืนยัน |
| P0 | ปิด overview fallback สำหรับ specific unanswered proposition | คำถาม conduct ไม่มี clause ต้องไม่คืน equipment/bugs ทั้งเล่ม; multi-need known/unknown แยกครบ | ทำเองได้จาก source scope |
| P0 | Clause integrity/readiness migration | ตรวจ segmentation, matching language, references, full exception chain จาก snapshot พร้อมรายงาน unexplained cases | ทำ source audit อัตโนมัติได้; ข้อกำหนดใหม่/เอกสารไม่ครบห้ามสร้างแทน |
| P0 | ดึงราคาให้ถูก audience/date/unit ก่อนคำนวณ | historical/current แยกชัด; ตัวเลข/ceil/capacity มาจาก source | relation/code ทำเองได้; วันที่และกฎราคาที่ยังไม่มีต้องเจ้าของ |
| P1 | Owner readiness dashboard ทุกหมวด | draft save บอก field ที่ขาดเฉพาะความสามารถ ไม่แค่ schema valid; preview ใช้ snapshot เดียวกับ chat | ทำเองได้ |
| P1 | English structured localization | nested list ไม่หลุด Thai prose/null unit; tech labels ชื่อเฉพาะคงเดิม; source version tracked | renderer/validation ทำเองได้; owner translation review ยังต้องมีหากนโยบายกำหนด |
| P1 | ราย need และ follow-up state | user ตอบชื่อ/ทั้งหมดแล้วสืบ subject+task+audience เดิม; selection หมดอายุต้องถามใหม่เฉพาะ slot | ทำเองได้จาก contract |
| P1 | Deadline/transport diagnostics | request budget ไม่ถูกใช้ซ้ำในทุก branch; observation ไม่หายเมื่อ kill worker | ทำเองได้ |
| P1 | Version evaluator ใหม่ | protocol/content/evidence/format/transport แยก; semantic undecided ไม่ถูกนับ pass; retain old metrics คู่กัน | ทำเองได้; semantic gold ที่เป็นกฎเจ้าของต้อง review |
| P2 | ชุด owner lifecycle บนสำเนาข้อมูลจริง | add/edit/supersede ถอนค่าเก่าแล้ว chat เห็นใหม่ครบภาษาพร้อม provenance; ไม่เปลี่ยน production | ทำเองได้บนสำเนา |

ไม่ต้องรัน Full Test ซ้ำเพื่อทำรายงานนี้ การแก้รอบต่อไปควรทำใน candidate ใหม่ รักษา R106 เป็น frozen evidence; หลังแก้ค่อย freeze แล้วทดสอบตามขอบเขตที่ได้รับอนุญาต ไม่วน full โดยอัตโนมัติจาก heartbeat

## 12. ข้อจำกัดการใช้งานจริงและการติดตั้ง

- Candidate R106 **ยังไม่ได้ติดตั้งทับ R78**; common DB เป็น migration preview มี draft heads ไม่ใช่ published owner release ที่เสร็จแล้ว
- ไม่มีการ autoapprove real records หรือแก้ validity dates เพื่อให้ test ผ่าน; production readiness ยังต้องแก้ ownership/release readiness ตามข้อเท็จจริง
- live provider ใน Full Test ถูกตั้ง controlled unavailable โดยเจตนา ไม่มี actual booking oracle และไม่สร้างการจอง จึงไม่ได้ยืนยันสถานะเครื่อง/รอบจริง
- real live provider lane แยกเคยได้ dashboard_unavailable; simulated live ที่ผ่านทดสอบตรรกะเท่านั้น ไม่ใช่หลักฐานว่าการเชื่อมต่อจริงปัจจุบันพร้อม
- รายงานนี้ไม่สรุปว่า LLM ปิด ไม่สรุปว่าผู้ใช้พร้อมกันทั้งหมดจะเร็วเท่ากัน และไม่ใช้ transport success แทน answer accuracy
''')
add('## 13. หลักฐานที่ตรวจย้อนหลังได้')
for label,p in [('รายงานผลอัตโนมัติ',O/'FINAL_REPORT_TH.md'),('Independent integrity verification',O/'INDEPENDENT_POSTRUN_VERIFICATION.json'),('ทุก failed request พร้อมคำตอบเต็ม',O/'ALL_FAILURES.jsonl.gz'),('ตัวอย่าง raw พร้อม hit และ source records',O/'REVIEW_SELECTED_RAW_AND_SOURCES.json'),('Source snapshots/records ที่ใช้ตรวจสาเหตุ',O/'REVIEW_SOURCE_EVIDENCE.json'),('Inventory ทุก failure pattern และ eval file',O/'REVIEW_STREAM_COUNTS.json'),('Failure methods / reason counts',O/'REVIEW_FAILURE_METHODS.json'),('Comparison R95 บน grade เดียวกัน',O/'REVIEW_R95_COMPARISON.json'),('Taxonomy errors และตัวอย่าง before/after',O/'REVIEW_GRADER_AND_DELTA_DETAILS.json'),('Lineage R105 → R106',B/'r106_execution_control_20261020/LINEAGE.json'),('Final grouped gate',R/'final_gate/REPORT_TH.md')]:add('- '+link(label,p))
add('''Code anchors ที่ใช้วิเคราะห์ (เป็น source R106 แช่แข็ง):

- `system/app/knowledge/common/rules_reader.py`: completeness gate และ `_gap`
- `system/app/knowledge/common/complete_flow.py`: execute/evaluate graph, people guard, final coverage
- `system/app/knowledge/common/claim_coverage.py`: compatibility_scope_not_migrated และ predicate receipts
- `system/app/knowledge/common/result_contract.py`: status/reason mapping
- `system/app/knowledge/common/answer.py`: compatibility/exact/semantic plan branches
- `run_common.py`: request clock, controlled live unavailable, partitions และ watchdog
- `reference_grader.py`: native graders และ positive_text_contract detection
- `system/tools/run_competition_contract_r27.py`: first-line และ wrong_game_evidence check
- `system/tools/run_competition_composition_r28.py`: wrong_category, clauses และ unknown fee check

## 14. บัญชีทุก failure pattern ที่พบ พร้อมตัวอย่างและสถานะทบทวน

จำนวนด้านล่างเป็น failure events ต่อ grade ไม่ใช่จำนวน unique requests และหนึ่ง grade เกิดได้หลาย events “ยืนยันสาเหตุของตัวอย่าง” ไม่ขยายไปเป็นคำตัดสิน semantic ของทั้งกลุ่ม ส่วนที่ไม่มี source adjudication รายตัวคง `review_pending` ไว้
''')
confirmed={'r103_rule_dependency_gap','r102_invalid_graph_dependency','r101_model_unavailable'}
for i,(label,n) in enumerate(counts['failure_patterns'],1):
 xs=samples.get(label,[]);x=xs[0] if xs else None
 add(f'### 14.{i} `{label}` — {n:,} events')
 if label.startswith('protocol'):note='Protocol mismatch; ต้องเทียบเนื้อหา/source ต่างหาก ไม่จัดเป็น actual content failure จากชื่อนี้'
 elif label.startswith('performance') and 'latency_ceiling' not in label:note='พบ taxonomy misbucket เพราะคำ timeout/latency ใน failure string; ให้ตีความเป็น text assertion และตรวจ semantic ต่อ'
 elif label=='validation | pipeline_exception':note='Execution/watchdog failure; ไม่มีคำตอบให้ตัดสิน semantic'
 elif label=='MODEL_TRANSPORT_FAILURE':note='Model HTTP transport; ไม่ใช่ semantic verdict'
 elif 'wrong_game' in label:note='Evidence identity/absence ต้องตรวจ hits; empty hits ถูก grader ตั้ง wrong-game ได้ ไม่ยืนยันเกมปนจาก flag อย่างเดียว'
 elif 'legacy_english_thai' in label:note='Localization flag; ยืนยัน raw Thai specs รั่วในตัวอย่างหลัก แต่ชื่อเฉพาะ/ปุ่มสองภาษาต้องแยก review'
 else:note='review_pending ในระดับทุก semantic case ของกลุ่ม; สาเหตุของตัวอย่างหลักที่ตรวจแล้วดูหัวข้อ 5–6'
 add('สถานะ: '+note)
 if x:
  add('Key: `'+x['key']+'`\n\nคำถาม: '+x['question'])
  ans=(x.get('answer') or '(ไม่มีคำตอบ: execution failure)');add('คำตอบจริง (ตัดเฉพาะในรายงานให้อ่านง่าย; ฉบับเต็มใน raw):\n\n```text\n'+ans[:950]+('\n…' if len(ans)>950 else '')+'\n```')
  qp=x.get('query_plan') or {};add('method=`'+str(qp.get('method'))+'`; record_ids=`'+', '.join(qp.get('record_ids') or [])+'`')
  add('Need status: '+json.dumps([{'task':v.get('task'),'status':v.get('status'),'reasons':v.get('reason_codes')} for v in x.get('need_results') or []],ensure_ascii=False))
add('## 15. Cohort inventory ตามหมวดใน input เดิม')
add('หมวดด้านล่างใช้ `group/domain/suite/file` ที่ fixture ประกาศ ไม่ใช่รายการ category ที่ production รองรับครบแล้ว Positive expected ในตารางนี้รวม execution failures ที่ input มี positive assertion ด้วย เพื่อไม่ซ่อน request ที่ล้ม จำนวนเป็น grades และมีหลาย grades ต่อหนึ่งคำถาม')
add('''| Cohort | Grades | Strict pass | Positive pass / expected |
|---|---:|---:|---:|''')
for k,v in sorted(extra['cohorts'].items(),key=lambda kv:-kv[1]['grades']):
 add(f"| {str(k).replace('|','/')} | {v['grades']:,} | {v['strict_pass']:,} | {v['positive_pass_including_execution_failures']:,}/{v['positive_expected']:,} |")
add('## ข้อสรุปสุดท้าย')
add('Coverage และ integrity ผ่าน แต่คุณภาพคำตอบยังมีทั้ง data readiness gaps, overly broad dependency gates, unresolved compatibility coverage, relevance/composition defects และ localization defects ต้องแก้ตาม predicate/source contract พร้อม owner workflow ก่อนอ้างพร้อม production การลด route mismatch อย่างเดียวทำคะแนน strict ดีขึ้นได้โดยไม่ทำคำตอบดีขึ้น จึงต้องเก็บ metric แยกและยืนยันด้วยหลักฐานของเนื้อหาที่ผู้ใช้ถามจริง')
report=re.sub(r'(?m)^(\|[^\n]*)\n\n+(?=\|)',r'\1\n','\n'.join(lines))
(O/'ROOT_CAUSE_REVIEW_TH.md').write_text(report,'utf8')
print(json.dumps({'report':str(O/'ROOT_CAUSE_REVIEW_TH.md'),'lines':len(lines),'bytes':(O/'ROOT_CAUSE_REVIEW_TH.md').stat().st_size,'patterns':len(counts['failure_patterns'])},ensure_ascii=False))
