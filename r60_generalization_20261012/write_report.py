from pathlib import Path
import json,collections
B=Path(__file__).resolve().parent
def rows(name):return [json.loads(x) for x in (B/name/'RESULTS.jsonl').read_text(encoding='utf-8').splitlines()]
def selected(r):return (r.get('decision') or {}).get('query_plan',{}).get('requested_fields',[])
def write(name,text):
 with (B/name).open('x',encoding='utf-8') as f:f.write(text)
final=rows('context3072_verified');reserved=rows('reserved_regression')
extras=collections.Counter(k for r in final for k in r.get('quality',{}).get('extra_fields',[]))
exact=sum(r['quality']['exact_required_fields'] for r in final)
report='''# ผล r60 — สำนวนใหม่และความครบของคำตอบตาม format กลาง

วันที่ 2026-10-12 (วันที่ตาม client); ใช้โมเดล local `scb10x/typhoon2.5-qwen3-4b` ที่มีอยู่ในเครื่อง ไม่ดาวน์โหลดหรือฝึกโมเดลใหม่

## ผลที่วัดได้จริง

| เส้นทาง / ชุด | ผล | ความหมาย |
|---|---:|---|
| ก่อนแก้, deterministic, development | 17/100 | อ่านชื่อรายการได้ แต่การเลือกเนื้อหาตามสำนวนใหม่อ่อน |
| ก่อนแก้, actual LLM, development | 79/100 | เชื่อมโมเดลได้ยังตอบไม่ครบ/ผิดช่อง |
| หลัง descriptions / gate / history รอบแรก | 87/100 | คำอธิบายอย่างเดียวไม่พอ |
| หลังแยก clause | 93/100 | ยังมี schema-valid แต่เลือกความหมายผิด |
| หลัง guard | 98/100 | มีส่วนที่สองตกหล่น |
| รอบถัดไป | 99/100 | มี false partial: เนื้อหาครบ แต่ why clause ถูกทำเป็น [] |
| หลัง typed coverage repair และใช้ context 3072 | 100/100 | ไทย 50/50 อังกฤษ 50/50; เป็น development ที่เห็นแล้ว |
| reserved ที่ freeze ก่อนเปิดผล ครั้งแรก | 43/48 | ไทย 22/24 อังกฤษ 21/24; synthetic ที่ agent แต่งเอง |
| reserved หลังแก้ | 48/48 | เป็น regression หลังเห็นปัญหาแล้ว |
| หลังแก้ แต่ปิด LLM, development | 18/100 | ยังไม่รองรับสำนวนใหม่กว้างเท่าเส้นทางเปิด LLM |
| actual pipeline + actual LLM | 12/12 | 6 หมวด × ไทย/อังกฤษ; มีแหล่งข้อมูล/เนื้อหาตาม fixture |
| actual authenticated owner preview HTTP + actual LLM | 12/12 | หลังแก้หน้าทดลองให้ใช้ planner; epoch ไม่เปลี่ยน |
| game → fields ของรายการลูกที่อ้าง game_id | 16/16 | catalog-driven projection; ไม่ได้ทดสอบ graph ทั้งหมด |
| related r59 regression | 5,056/5,056 | ไทย 2,528 อังกฤษ 2,528; seen synthetic, ไม่ใช่ชุดผู้ใช้จริง |
| owner/common unit ก่อนแก้ endpoint ล่าสุด | 81 tests ผ่าน | มี base tests ถูก discover ซ้ำ ไม่ใช่ 81 ความสามารถอิสระ |
| guards รุ่นสุดท้าย | 21 tests ผ่าน | r60 13 + r59 8; รวมการปิด LLM / default / clause overflow |
| owner save/approve/publish/preview guard หลังแก้ | 1 test ผ่าน | ใช้ฐานข้อมูลชั่วคราว; auth/origin/draft guard ยังอยู่ |

ไม่รวมคะแนนเหล่านี้เป็น accuracy เดียว เพราะหน่วยวัด/เส้นทาง/การเห็นข้อมูลต่างกัน ไม่ใช่ latency หรือ concurrent benchmark ไม่ได้ทดสอบ WordPress รอบนี้

## สิ่งที่แก้

1. แยกคำถามภาพรวมจริงออกจากการมีคำว่า “ข้อมูล/information” อยู่ในประโยค ทำให้คำถาม expiry ยังเข้าตัวตีความได้
2. เพิ่มคำอธิบายความหมายของ attribute ไทย/อังกฤษใน `schema_descriptions.json` ซึ่งเป็น metadata นักพัฒนา แยกจากข้อมูลเจ้าของและ gold
3. ให้โมเดลเลือก field ต่อ clause ในคำขอเดียว บังคับ enum/type/IDs จำนวน clause ไม่ให้ตอบ facts/SQL หรือเลือก record ใหม่
4. ทบทวนเมื่อ lexical match อาจเป็นแค่คำหัวข้อ เช่น eligibility/proof, provider/status mapping, rule text/rulebook edition, play/reserved time
5. ไม่คง field ที่เป็น weak match ไว้เพียงเพราะมันเลือกได้ก่อน; เก็บ strong needs และ rejected-task guard
6. ต่อบทสนทนาโดยสืบทอดรายการ แต่สืบทอด fields เฉพาะเมื่อข้อความเป็นตัวเลือกสั้นจริง ไม่สืบทอดทุก field เมื่อ user ถามเรื่องใหม่
7. spelling candidate จากศัพท์ schema เฉพาะ insertion/deletion ระยะ 1 และ candidate เดียว รักษาเลข/คำปฏิเสธ/คำที่เป็นคำจริง ไม่เพิ่ม alias ของคำถามทั้งประโยค
8. ตัวอ่าน game ใช้ metadata catalog เลือก fields ของรายการลูกโดย game_id พร้อม evidence เดิม
9. แยก transport / schema / semantic / content ใน trace; JSON ผิดแต่ HTTP สำเร็จไม่ทำให้ circuit มองว่าโมเดลล่ม
10. ถ้ารู้ว่าบาง clause ยังไม่ตีความ ให้ partial_answer พร้อมแจ้งส่วนที่ค้าง ไม่ validated complete; เกิน 6 clause ปฏิเสธ planner พร้อมเหตุผล ไม่ตัดข้อความเงียบ ๆ
11. context planner เปลี่ยน 4096 → 3072 ให้ตรง warmup ของแชท; วัด dev ใหม่ผ่านครบ แต่ยังไม่ได้วัดผลด้าน cold-start latency
12. owner preview เปิด planner ตาม `PSU_LOCAL_LLM_ASSIST_ENABLED` ค่าเริ่มต้นเปิด เหมือนเว็บแชท; `PSU_COMMON_PLAN_LLM=0` ยังปิดเฉพาะ planner ได้ มี deadline และ audit
13. pipeline ที่รับ `experimental_allow_llm=None` อ่าน `PSU_EXPERIMENTAL_ALLOW_LLM` ก่อน common route; explicit False ยังปิดได้เหมือนเดิม

## ข้อจำกัด

- คะแนนผ่านต้องมี expected fields/status/value leaves/evidence locator และไม่ตอบงานที่ปฏิเสธ แต่ไม่บังคับว่าห้ามมี field เสริมทุกชนิด
- คำถามใหม่ใช้ชื่อ/alias ของ fixture ที่ resolve ได้ก่อน; ยังไม่พิสูจน์ unnamed search, หลายรายการในข้อความเดียว หรือข้อความกำกวมทุกชนิด
- noise 48 เคสเป็นการเบิ้ล 2 จุดและลบ 1 จุดใน sentence รักษา entity names และตัวเลข; ไม่ใช่ 48 รูปแบบ keyboard substitution และไม่ใช่ human typo distribution
- context 2 เคสใน development เป็น previous user alias + all information; หลักฐานสนทนาหลาย turn ชุดใหญ่เป็นของ r59 ไม่ได้แต่งเติมว่าร60ทดสอบทั้งหมดใหม่
- schema-valid plan ยังเลือก field ผิดได้ ไม่ใช้ 100/100 เป็นหลักฐานว่า LLM เข้าใจทุกคำถามแล้ว
- ข้อมูลตัวอย่าง 720 รายการแยกจาก production และ opt-in demo; ฐานจริงยังมี draft ที่ไม่ได้ publish ข้อมูลใหม่ผ่าน format กลางต้อง owner review/approve/publish ก่อน
- การแปลความหมาย field โดย agent ไม่ใช่การยืนยันการแปลข้อเท็จจริงเจ้าของโดยมนุษย์
- process เว็บเดิมเก็บ Python modules รุ่นที่โหลดแล้ว ต้องปิด/เปิดใหม่เพื่อรับโค้ดนี้ ไม่ได้ restart session ของผู้ใช้ระหว่างทำงาน

รายละเอียดการเลือกผิดทุกเคส LLM และ reserved อยู่ใน [ANALYSIS_TH.md](ANALYSIS_TH.md); flow ฉบับปรับปรุงอยู่ใน [Flow.md](Flow.md)
'''
report+=f'\n## ความเกินของเนื้อหาใน development ที่ผ่าน\n\nตรง expected fields เป๊ะ {exact}/100; มี field เสริม {100-exact}/100. ตารางนี้แยก content recall จาก field precision: `{dict(extras)}`. Field เสริมจึงยังเป็นพื้นที่พัฒนา ไม่ปิดประเด็นด้วยคำว่า “ผ่านครบ”.\n'
write('RESULTS_TH.md',report)
analysis='''# วิเคราะห์สาเหตุ r60 แบบแยกชั้น พร้อมหลักฐานก่อน/หลัง

## 1. ทำไมข้อมูลมีครบแล้วยังตอบผิด

การมีข้อเท็จจริงกับการเลือกข้อเท็จจริงเป็นคนละขั้น: resolve record → interpret needs → select related records → render values → validate coverage. เมื่อรายการถูกแต่เลือก `eligibility` แทน `required_proofs` ระบบอ่านข้อความที่มีอยู่จริงได้อย่างซื่อสัตย์ แต่ไม่ตอบสิ่งที่ user ต้องการ ยิ่ง validator ตรวจเฉพาะ field ที่ระบบเลือกเอง มันอาจผ่านทั้งที่ need ที่ตกหล่นไม่เคยกลายเป็น obligation เลย

รอบนี้ gold แยกจาก runtime: ตัวประเมินกำหนด expected fields เองก่อนวัด ไม่ส่งให้ LLM/parser และใช้ raw fixture values/evidence locator ตรวจคำตอบ อย่างไรก็ดี gold ที่ agent แต่งเองยังมีข้อจำกัดด้าน human agreement ไม่ใช่ “คำตอบจริงทุกสถานการณ์”

## 2. จัดลำดับสาเหตุและวิธีแก้

### P0A — Planner ไม่ถูกเรียก ทั้งที่ต้องตีความเพิ่ม

**หลักฐาน:** คำถาม `รหัสสถานะถูกแปลว่าอะไร แล้วข้อมูลหมดอายุเมื่อไหร่` ก่อนแก้ selected=[] และ clarification; reserved contact/schedule ไทย/อังกฤษมี audits=[] ทั้งที่มี need ที่สองตกหล่น. owner_server `/api/preview` ส่ง CommonAnswerer โดยไม่มี planner; engine common route ใช้ bool(None)=False ก่อนอ่าน environment default

**สาเหตุ:** broad information gate กว้างเกิน, resolver เจอหนึ่ง field จึงคิดว่าครบ, entry point มี setting ไม่ตรงกัน. นี่ไม่ใช่โมเดลสร้างคำตอบผิด เพราะหลายเคสไม่ได้ส่งคำถามไปหาโมเดลเลย

**แก้:** overview_request ต้องเป็นภาพรวมจริง; resolution_uncertain ตรวจการเปรียบเทียบ/คำถามหลายส่วน/weak nouns; owner preview ใช้ setting เดียวกับเว็บแชท + audit; engine ใช้ default เมื่อ None. explicit disable คงอยู่. เปิด LLM ไม่รับรองว่าเลือก field ถูก ต้องมีชั้นถัดไป

### P0B — Semantic collision: คำตรง แต่หมายถึงคนละ attribute

**หลักฐาน:** verify eligibility→eligibility (ต้อง proof); provider status codes→provider (ต้อง mapping+freshness); rule edition→text (ต้อง rulebook_release); FAQ response→question (ต้อง answer)

**สาเหตุ:** topic word กับ requested property ใช้คำร่วมกัน; description อังกฤษเดิมมาจาก key ที่แยก underscore จึงไม่อธิบายความต่าง; constraint ให้ field อยู่ใน schema ไม่บังคับความหมาย. ไม่ได้มี retrieval fact ผิดในเคสเหล่านี้

**แก้:** descriptions ความหมาย/ขอบเขตชัดเจน, review weak interpretations, strong needs ไม่ใช่ทุก lexical match, intent terms/concept conjunctions ใน metadata เฉพาะ kind. reserved ยังพลาด FAQ response เพราะ modelเลือก question แม้ JSONถูก ต่อมาจึงเติมความหมาย response/reply→answer ใน schema metadata. เป็นการแก้ attribute reuse ไม่เพิ่ม fixture-name branch

### P0C — ตอบส่วนเดียวในคำถามหลายส่วน

**หลักฐาน:** session_minutesไม่มี occupancy_minutes; facility accessibilityไม่มีlocation; live mappingไม่มีfreshness; closure reasonไม่มีstate. ข้อมูลทุกส่วนอยู่ใน release เดียวกัน

**สาเหตุ:** flattened field array ไม่บอกความรับผิดชอบต่อคำถามแต่ละส่วน; detector เดิมไม่ split แล้ว; selection ที่มีแค่หนึ่งข้อถูกมองว่าพอ

**แก้:** semantic_clauses + JSON per clause IDs enum + ต้องมีครบทุก ID + union fields และ obligations. เพิ่ม แล้ว/then และ modifier ellipsis. ยังไม่ใช่ syntactic parser: conjunction ในชื่อ/วลีอาจ split เกิน, >6 clause เป็น documented limit; [] ต้องแจ้ง partial ถ้าตีความไม่ได้

### P1A — False partial แม้รวม facts ครบ

**หลักฐาน:** dev_final closure EN noisy เลือกstate,reasonครบ แต่ why clause=[] เนื้อหาคำตอบมีทั้งสอง จึง response_partial_answer และ fail

**สาเหตุ:** modelใส่reasonในclause0 แล้วปล่อยclause1ว่าง; coverage guard ที่มอง allocationอย่างเดียวจึงสร้าง false alarm

**แก้:** typed clause need ที่ชัดเจน ถ้า fieldนั้นเลือกอยู่แล้วในunion ให้ repair coverage พร้อม trace clause_coverage_repairs ไม่ลบ unknown clause ทิ้งทุกกรณี. กฎนี้ไม่สามารถพิสูจน์ความหมาย clause ที่ไม่รู้ได้

### P1B — ไม่รู้ task ที่ถูกปฏิเสธ / ต่อบทสนทนาผิด

**หลักฐาน:** “ไม่เอาราคา ขอเวลาเล่นอย่างเดียว” selected session+amount; “So what should I bring to prove I qualify?” หลังข้อมูล audience คืนno_common_answer

**สาเหตุ:** bag-of-cues เก็บคำราคาโดยไม่สนใจ negation; followup trigger จำกัด; inheritfieldsจากคำถามภาพรวมเดิมอาจพาทั้งหมดกลับมา

**แก้:** focus_request เฉพาะ rejected named task + affirmative alternative ไม่ rewrite “ไม่ได้เป็นนักศึกษา/not a student”; inherited record context กับ inherited requested fields แยกกัน; bare selectorจึงสืบทอดfields คำถามใหม่เลือกneedsใหม่. ใส่ test explicit new entity priority ของr59ร่วมด้วย

### P1C — พิมพ์ผิดหลายส่วนและภาษาอังกฤษไม่ใช่ key

**หลักฐาน:** whic edition/rullebook, อย่างน้อ, ลงให้เลล่น/รอบี้ ทำให้lexicalfieldsตก; descriptionเพียงอย่างเดียวจากรอบแรกยังfail13

**แก้:** คง original input + suggested_spelling จาก lexicon schema เฉพาะ one-edit insertion/deletion candidateเดียว; private valid-English dictionary / protected words / digitsคงไว้; THnoiseอาศัยdescriptions+clauseLLM ไม่มีการอ้างว่าทำ Thai spellchecker สมบูรณ์

**ขอบเขต:** ไม่แก้same-length substitution/transpositionในhelperนี้ ป้องกันเปลี่ยนคำจริงโดยเดา; ไม่มีkeyboard-weighted probability, embedding rerankingหรือtrainednoisy-channel. งานก่อนหน้ารองรับบางแนวแยกอยู่แล้ว ไม่รวมคะแนนร60เพื่ออ้างว่าไทยทุกtypoผ่าน

### P1D — ความสัมพันธ์ระหว่างหมวดยังไม่มี projection

**หลักฐาน:** game parentถามoffered/version/installed_resource_ids/บัญชี/ข้อจำกัดของservice; เดิม readerรู้เฉพาะfieldลูกบางกลุ่ม

**แก้:** catalog-driven unique childfield projection + game_id joins; ทวน16/16พร้อมevidence. ไม่เปลี่ยนdata/FKsหรือให้LLMสร้างjoinอิสระ. fieldร่วมเช่นgame_versionยังใช้scopeheuristic; policy_idแสดงชื่อpolicy ไม่ขยายทุกเนื้อหากฎ เป็นงานต่อ

### P2 — การวัดและเครื่องมือทำให้เข้าใจผลผิด

**หลักฐาน:** unitคำสั่งหนึ่งใช้ชื่อmoduleผิด จึงFAILED(errors=1) แม้r60ทั้ง13methodผ่าน; เก็บlogนั้นไว้ แล้วแก้ชื่อเป็นtest_common_query_contract_r59รัน21ผ่าน. relatedregressionก่อนแก้เกิด20failgame_modeจากphraseเดียว across20profiles แม้harnessรายงานregressions=0เพราะมันเทียบbaselineรุ่นเก่ากว่าr59

**แก้:** รายงาน5056 actualpass/failตรงๆ เทียบr59ที่เคยผ่านครบ; repairmodifierellipsisแล้ว5056/5056. ไม่ลบfailedrun/เรียกทุกผลว่า100%. schema rejectionแยกtransportfailure และสุขภาพโมเดล

## 3. ความหมายคะแนนและ confidence

confidenceในanswerเป็นheuristic ไม่ได้calibrateกับhumanlabels; confidence_calibrated=Falseในartifact. semantic_status=typed_clause_scope คือknown typed cuesครบในช่วงนั้น; schema_only_unverified_intentแปลว่าenumถูกแต่ยังไม่มีหลักฐานรับรองintent. transport_ok=Trueหมายถึงได้HTTPresponse ไม่ได้แปลว่าเลือกfield/ตอบถูก. schema_accepted=Trueไม่รับรองsource/evidence/needทั้งหมด

ผลdevelopmentผ่านต้องครบexpectedfields/status/content/evidenceและไม่ตอบforbiddenfields แต่fieldextrasไม่ได้ทำให้failทุกกรณี จึงรายงานprecisionแยก. คำถามreservedrental “What kit is covered by the rental price?” goldกำหนดทั้งincludedkitและamount ทั้งที่priceอาจไม่ใช่สิ่งที่ขอชัดเจน เป็นgoldambiguityที่ต้องทวนในรอบhumanblind ห้ามบังคับproductionให้นำราคาออกทุกครั้งเพียงเพื่อคะแนน

## 4. ใช้งานจริงและรายการยังต้องทำ

1. **สูงสุด:** semantic validation ยังไม่รู้needที่โมเดลตีความผิดแต่ไม่เว้นclause. แก้ต่อด้วยschema meaning/exclusion/examplesแยกkindและgoldใหม่ก่อนทดสอบ; เปรียบเทียบexactfieldprecision ไม่ใช้ข้อเท็จจริงเป็นaliases. ไม่เพิ่มjudgeLLMอัตโนมัติจนกว่าจะวัดquality/latency/budget
2. ชื่อไม่ครบ/ไม่ระบุrecordหลายเป้าหมาย: รอบนี้ยังnamedrecord; ต้องมีentityretrievalrankingและclarificationbeforefactsพร้อมfuzzyadversarialcases ไม่เหมาว่าเพิ่มdescriptionแล้วจบ
3. กระบวนการpublish/withdrawกับlegacyfallback: ต้องทดสอบว่าcommonmissของrecordที่เคยpublishไม่กลับไปตอบfactsเก่าในlegacyindex อันนี้ยังไม่ได้พิสูจน์ในr60
4. graphdetails: expandpolicycontentwhenasked, resource→service→rateที่unique, multi-platformscope, sharedgame_versionsemantics; มีFKguardsแล้วแต่readprojectionยังไม่ครบทุกเส้น
5. renderer: humanlabels/enums/scopesและemptyzone_idsที่อาจหมายถึงallzones; อย่าแสดงblankจนผู้ใช้ตีความว่าไม่มี; ต้องอิงcatalogก่อนแก้
6. LLMoff/unavailable/busy: dev18/100ในสำนวนนี้; ต้องแจ้งunknownneeds/clarifyอย่างเฉพาะเมื่อfactsไม่ครบ หรือยืนยันfieldผ่านUI ไม่fallbackตอบที่ผิดเพียงเพื่อให้มีคำตอบ. plannerdeadline4sec/admission/circuitยังคงอยู่ ไม่ได้ทำconcurrencybenchmarkใหม่
7. modelsemanticmeaningมี122keysรวม155catalogslots คำที่ใช้ซ้ำแต่meaningต่างkindอาจต้องkind-specificoverride. metadataไม่ใช่เจ้าของfacttranslation; nativeTH/ENhumanreviewยังคนละงาน
8. actualownerrecordsยังdraft/ยังไม่publish — ต้องยืนยันข้อเท็จจริงโดยเจ้าของก่อนpublish; รอบนี้แก้logic/ทดสอบsynthetic ไม่อนุมัติหรือกรอกนโยบายแทน

## 5. งานวิจัยที่ใช้ประกอบจากr59

ดู [Research.md ของ r59](../r59_schema_repair_20261012/Research.md) พร้อมวิธีค้น/ข้อจำกัด ไม่มีการค้นเพิ่มหรืออ้างว่าฝึกโมเดลในร60

- [D3ST](https://arxiv.org/abs/2201.08904): ประยุกต์schema descriptionsและfieldselection; ไม่ได้reproduce model/training
- [SGD-X](https://ojs.aaai.org/index.php/AAAI/article/view/21341): เป็นเหตุผลให้แยกสำนวนใหม่กับcanonicalและfreeze reserved
- [PICARD](https://aclanthology.org/2021.emnlp-main.779/): แนวทางtypedconstraint; ระบบนี้ใช้JSONschema+postvalidator ไม่ใช่PICARDdecoder
- [CheckList](https://aclanthology.org/2020.acl-main.442/): behavioraltests/negation/invarianceและgroupfailure; ไม่เอาaggregateเดียวปิดปัญหา
- noisy-channel/Thai keyboard papersในresearchเดิม: ชี้ว่าความน่าจะเป็นcandidate+contextสำคัญ; r60ใช้เพียงconservativecandidateproposal ไม่อ้างimplementationprobabilisticทั้งชุด

## 6. หลักฐานรายเคส

ด้านล่างแสดงinputจริง/gold/selected/response/error/auditจากlog ไม่แปลว่าgoldทุกข้อผ่านhumanreview การเลือกผิดเป็นการอ่านlogร่วมกับcode ไม่ได้อ้างว่ามีhiddenchain-of-thoughtของโมเดล
'''
for phase,newname in [('baseline_llm','context3072_verified'),('reserved_first','reserved_regression')]:
 after={r['id']:r for r in rows(newname)}
 analysis+=f'\n### ชุด {phase}\n'
 for old in rows(phase):
  if old['passed']:continue
  new=after[old['id']];p=(old.get('decision') or {}).get('query_plan',{})
  analysis+=f"\n#### {old['id']}\n\nคำถาม: {old['question']}\n\nต้องมี: `{old['expected_fields']}`\n\nเลือกก่อน: `{selected(old)}`; ผล: `{old['reasons']}`\n\nคำตอบก่อน:\n\n```text\n{old.get('answer','')}\n```\n\nคำตอบหลัง:\n\n```text\n{new.get('answer','')}\n```\n\nเลือกหลัง: `{selected(new)}`; ผ่าน={new['passed']}; fieldเสริม=`{new.get('quality',{}).get('extra_fields',[])}`\n\nTraceก่อน:\n\n```json\n{json.dumps({'plan':p,'planner_audits':old.get('planner_audits',[])},ensure_ascii=False,indent=2)}\n```\n"
analysis+='\n## 7. ตาราง development ทั้ง100 — ความครบกับความเกิน\n\n| ID | ผ่าน | ต้องมี | เลือกจริง | fieldเสริม |\n|---|---|---|---|---|\n'
for r in final:analysis+=f"| {r['id']} | {r['passed']} | {', '.join(r['expected_fields'])} | {', '.join(selected(r))} | {', '.join(r['quality']['extra_fields'])} |\n"
write('ANALYSIS_TH.md',analysis)
flow='''

## Runtime flow ฉบับหลังแก้

### A. จากเจ้าของกรอกข้อมูลถึงคำตอบ

1. ฟอร์มรับtypedvalues/status/evidence → draft immutable revision; previewไม่publishdraftเอง
2. เจ้าของreviewfacts/การแปลที่ใช้ → approve exact revisionhash → publishrelease transaction
3. runtimeอ่านsnapshot releaseที่validated และ epoch; demoต้อง opt-inแยกจากproduction
4. คำถามรับ locale/history/config/deadline; common reader resolveexplicitrecordก่อนcontext และรักษาข้อความดิบ
5. stripselectedentitynamesเฉพาะการหาneeds; focusเฉพาะrejectedtaskที่ยืนยันรูปแบบได้; newquestionไม่inheritfieldsเดิม
6. resolvefieldsจากcatalog+schema metadata; scopekindsชัดเจน; broad=trueเฉพาะallจริง; overviewเฉพาะภาพรวมจริง
7. หากlexicalcomplete/reliableใช้fastpath; หากmissing/weak/multineedต้องreview และLLMenabled ให้ส่งschema meaning+clauses+enumโดยไม่ส่งgold
8. spellcandidateจากschemaใช้suggestionพร้อมoriginaltext ไม่มีsame-lengthrewriteโดยเดา; ไม่มีrewriteเลข/คำปฏิเสธ
9. >6clause→explicitplannerdecline;<=6clause→oneLLMcall;deadline4sec+modeladmission+healthgateเดิม
10. validateHTTP/outputsize/JSON/IDs/enum/types; outputerrorไม่ปะปนtransporterror; allfieldsถูกconstraintจากrequest
11. preserveclearneeds/removeweakmatchเมื่อมีvalidreview; tracksemanticsunverified; typedcoverageallocationrepairเฉพาะneedที่มีfieldแล้ว
12. selectrelatedrecordsโดยFK/catalogscope; ไม่ให้LLMสร้างSQL/เปลี่ยนfacts; ถ้ามีpresetหลายตัวถามเลือกก่อน
13. renderexactpublishedvalues,statusandlocator; unsupported/unknownต้องยังระบุ; unresolvedclauses→partialพร้อมบอกส่วนค้าง
14. verifyselectedobligations/evidence/epochอีกครั้งก่อนส่ง; ถ้าreleaseเปลี่ยนต้องไม่ส่งstalefacts; confidenceเป็นheuristic
15. ส่งanswer+decisionartifact+planner_audits; evaluatorนอกruntimeตรวจexpectedneedsที่เลือกไว้ก่อนวัด

### B. Loopพัฒนาที่ทำจริงรอบนี้

| รอบ | พบอะไร | เปลี่ยนอะไร | หลักฐาน |
|---|---|---|---|
| baseline | deterministic17,LLM79 | freeze100/48และสำรอง | BEFORE,manifest,rawlogs |
| 1 | schemaอังกฤษเป็นkey/overviewgate/history | descriptions+gate+focus | 87/100 |
| 2 | flattenedplanตกneed | per-clauseJSON+descriptionsTH | 93/100 |
| 3 | wrongweakcue/falsewholeoverview | strongneeds,wholeoverview,semanticreview | 98/100 |
| 4 | แล้วclauseไม่ตรวจ | splitแล้ว+FAQscope | 99/100 |
| 5 | whyallocationfalsepartial | typedcoverage repair | 100/100 |
| 6 | reserved5failure | conceptmetadata+comparativegate | first43/48→regression48/48 |
| 7 | relatedoldpatternfail20 | sharedmodifierobject | 5056/5056 |
| 8 | context4096vswarmup3072,ownerpreviewnoplan,Nonefalse | contextalignment+entrysettings+audit | dev100,actualpipeline12,previewHTTP12,guards21+1 |

ตารางนี้เป็นรอบที่มีการเปลี่ยนและวัดจริง ไม่เรียกการอ่านเอกสารซ้ำว่าexperimentใหม่ ไม่เพิ่มผลของชุดที่ยังไม่ได้ทดสอบ

### C. Flowรอบถัดไปตามความเสี่ยง

1. ทำmeaning/exclusionแยกkindเมื่อkeyซ้ำ; freezeชุดใหม่ก่อนเห็นผล; goldต้องแยกexplicitneed vs optionalcontextและทวนhumanambiguityภายหลัง
2. เพิ่มqueryentityvariants/unnamed/multitargetพร้อมhardnegatives; isolateddemoพร้อมepoch/withdrawal; เลือกrecordผิดต้องclarifyก่อนfacts
3. เพิ่มlegacyfallbackafterwithdraw/publishregression; ป้องกันข้อมูลownerใหม่ถูกข้อมูลเก่าตอบทับ
4. เพิ่มtypedrelationshipneedสำหรับlinkedpolicy/rateที่ชัดเจน; ambiguityถามเลือก; ตรวจrenderallzonesจากcatalog
5. วัดcoverage+fieldprecision+partialqualityพร้อมtimeouts/busy/unavailable; ทดสอบพ่วงendpointจริงไม่ใช่readerอย่างเดียว
6. ค่อยทำblindhumancheckของfacts/policy/translationหลังautomatedlogicคงที่; userเคยยืนยันlivebookingถูกแยกจากfixtureของcommonรอบนี้

### D. วิธีใช้และการนำเข้า

- เว็บแชท `PSU_LOCAL_LLM_ASSIST_ENABLED` ค่าเริ่มต้นเปิด; owner previewใช้ค่าเดียวกันหลังr60
- directpipeline `experimental_allow_llm=None` อ่าน `PSU_EXPERIMENTAL_ALLOW_LLM`; explicitTrue/Falseoverrideได้
- `PSU_COMMON_PLAN_LLM=0`ปิดเฉพาะcommonplanner; ปิดแล้วสำนวนใหม่ชุดนี้ผ่าน18/100 จึงต้องไม่แสดงว่าเป็นโหมดความสามารถเท่ากัน
- เปิดOllama/modelที่แพ็กมีตามlauncherเดิม; ไม่แก้launcherหรือดาวน์โหลดmodelในรอบนี้; หากmodelcold/busyไม่รับรองlatency
- การอัปเดตโค้ดไม่reloadprocessเดิมอัตโนมัติ: เปิดใหม่จากlauncherหลังปิดprocessของชุดนั้นอย่างปกติ
- สำรอง/ตรวจhashก่อนcopyเฉพาะlogic+test+metadata+docs; ห้ามcopyDEMO.sqliteลงproduction/h้ามpublishdraftแทนเจ้าของ
'''
with (B/'Flow.md').open('a',encoding='utf-8') as f:f.write(flow)
print('Reports written; full failure examples retained')
