# R123 — ลำดับพัฒนา Distillation และเกณฑ์วัดผล

สถานะ: **แผนงาน ยังไม่มีการรันขั้นพัฒนาหรือฝึกในเอกสารนี้**  
เอกสารหลัก: [FLOW_MAIN_TH.md](FLOW_MAIN_TH.md) · [DATA_CONTRACTS_TH.md](DATA_CONTRACTS_TH.md)

## 1. ขอบเขตและหลักฐานฐานตั้งต้น

- Source อ้างอิง: R122 revision04 แยกจาก production R78
- Adapter อ้างอิง: R121 checkpoint ที่ผ่านการฝึก 93 optimizer steps
- R121 raw model pilot: 30 ข้อ; domain ตรงป้าย 12→22 ข้อ; source-quote contract 5→29 ข้อ ไม่ใช่ end-to-end accuracy
- R122: API paired 8 ข้อต่อแขนบน revision02, probes 2 ข้อบน revision03 และ 1 ข้อบน revision04 ไม่ใช่ชุดวัดครบของ revision04
- Draft labels ของ R122 ไม่ใช่ gold ที่ review ครบ และไม่ใช่น้ำหนักที่ฝึกใหม่แล้ว

ห้ามใช้ตัวเลขฐานเหล่านี้เป็นคะแนน R123 และห้ามสรุปว่า R123 ดีกว่าก่อนมีผลวัด

## 2. ลำดับงานที่ต้องทำ

### P0 — Freeze contracts และ capability coverage ทั้ง 14 หมวด

Deliverables:

1. schema ของ RequestContext/PlannerProposal/CompiledTask/SharedBinding/ExecutorResult/Receipt/ObligationLedger
2. operation vocabulary และ adapters จากชื่อเดิมของ R122
3. capability matrix ของ C01–C14 ระบุ supported/planned/unsupported ตามโค้ดที่มีจริง
4. รายการ fields และความสัมพันธ์ข้อมูลที่แต่ละ operation ต้องใช้
5. error taxonomy และ public API mapping version

ผ่านเมื่อ contracts ระบุ semantics ของ compare/list/count/calendar/policy/live ได้ครบ และไม่มี operation ที่ประกาศ supported โดยไม่มี executor การทำ matrix ครบไม่เท่ากับ implement ครบ ต้องมีสถานะราย operation

### P1 — สร้าง task graph, slot ownership และ verifier ก่อนต่อโมเดลใหม่

ใช้แผนที่ตรวจแล้วและ saved model proposals จากคำถามเดิมตรวจการส่งต่อระหว่างชั้น โดยไม่ต้องเรียก LLM เพื่อทดสอบทุกข้อ

ประเด็นที่ต้องครอบคลุม:

- local/shared/history slots และการ override
- ตัวเลขในชื่อเกม/เครื่อง เทียบกับจำนวนคน/ระยะเวลา
- comparison option เทียบกับ total duration/session period
- independent booking task ยัง execute ได้เมื่อ price task ขาด source
- ambiguity ไม่ถูกลบเมื่อเปลี่ยน domain สำเร็จ
- unsupported operation ไม่ถูกลดเป็น detail อัตโนมัติ
- budget exhausted, missing source และ provider offline เป็นคนละสาเหตุ

ผ่านเมื่อ source-level assertions ของกรณีที่ freeze ไว้ผ่านครบ และความผิดทุกชนิดมี reason ที่ตรงกัน ตัวเลข assertions ไม่ใช้เป็น accuracy

### P2 — ต่อ executors เดิมเข้ากับ contracts ใหม่ให้ครบหมวด

| กลุ่มงาน | หมวด | สิ่งที่ต้องส่งมอบ |
|---|---|---|
| รายละเอียดและความสัมพันธ์ | C01–C05 | bound entity, field/relation scope, set/count proof, control subset handling |
| ตัวเลขและแพ็กเกจ | C06–C07 | unit/billing semantics, option coverage, arithmetic receipts, audience alignment |
| ขั้นตอนและนโยบาย | C08–C10 | action/condition matching, authority/variants/conflict, dedup ที่ไม่ทำเงื่อนไขหาย |
| เวลาและข้อมูลจริง | C11–C12 | dated/weekly distinction, timezone, closure precedence, freshness และ provider states |
| กติกาและประกาศ | C13–C14 | event edition/dependencies, validity, source publication/scope |

ใช้ตัวอ่าน typed ที่มีอยู่เมื่อทำงานถูก แล้วเพิ่มส่วนที่ขาดตาม contract ไม่เขียนราคา เวลาเปิด หรือ expected answer ของข้อสอบลงใน router

การทยอย implement เป็นกลุ่มช่วย review โค้ด แต่การประกาศพร้อมต้องอิง capability matrix ทั้งหมด ไม่ใช้ผลสามหมวดแรกแทนทุกหมวด และไม่ต้องรัน Full Test ใหม่ทุกครั้งที่จบ module

### P3 — แก้ data/compiler/authority ที่จำเป็น

1. ตรวจ source relations, units, validity และ aliases ที่ executors ต้องใช้
2. สร้างรายงาน gap แยก record missing / relation missing / applicability missing / conflict
3. ตรวจประวัติ owner-supplied answers และข้อที่ยังไม่มีคำตอบ โดยรักษา approvals/status เดิม
4. แยก duplicate จาก competing policy versions ด้วย scope/conditions/effective period
5. ตรวจการเพิ่ม record ใน schema ที่รองรับแล้ว index/reader เห็นข้อมูลใหม่โดยไม่ฝึกโมเดล

ข้อมูลที่ยังไม่ยืนยันต้องคง unknown/conflicted และถูกตอบด้วยสถานะที่ตรงจริง ไม่เติมเพื่อให้คะแนนผ่าน

### P4 — ตรวจชุดสอนทั้งชุดและสร้าง teacher plan labels

ใช้คำถามเดิมและ traces ที่เก็บไว้ก่อน โดยไม่รัน Flow เดิมซ้ำในงานวางแผนนี้ ขั้นเตรียมจริงต้องระบุว่า source ของครูกับ source ปัจจุบันต่างกันหรือไม่

รายการตรวจ annotation:

- แยก task ครบตาม factual needs และไม่แยก style requests เป็นงาน
- intent/operation/facet ตรงความหมาย ไม่เพียงตรงชื่อหมวด
- entity และ slots อ้าง raw spans ได้
- ระบุ local/shared scope ถูก ไม่มี `constraints(whole_question)` แจกทุก task
- duration comparison มีทุก option และไม่กลายเป็นคำขอซื้อเวลารวม
- shared prefix และ anaphora มี provenance; ambiguous จริงถูกเก็บไว้
- จุดที่ teacher ตอบผิด/อ้าง source เก่า/ยังตัดสินไม่ได้ถูก quarantine
- ไม่ใส่ราคา/สิทธิ์/ตารางของศูนย์เป็น factual targets ของ planner

Review labels เดิม 244 train / 15 validation / 30 test ในฐานะ corpus ที่มีประวัติ ไม่ถือว่าชุดเก่าทั้งหมดเป็น gold หรือ fresh holdout อีกต่อไปเมื่อถูกเปิดดูและใช้แก้ระบบแล้ว

Teacher supervision ควรเป็น plan และ decision codes สั้นที่ตรวจได้ พร้อม source refs สำหรับการ adjudicate ไม่บังคับให้โมเดลสร้างคำอธิบายยาวหรือถือคำอธิบายของครูเป็นหลักฐานความถูกต้อง

### P5 — Freeze การแบ่งข้อมูลและ metric ก่อนฝึก

ใช้ retained question pool ที่มีอยู่ เลือกตาม category/locale/operation/ความซับซ้อน แยก family และ normalized core ระหว่าง train/validation/holdout รวมทั้งคำถามที่เป็น paraphrase ต่างภาษาเมื่อรู้ว่ามาจาก family เดียวกัน

กลุ่มที่ต้องมี coverage:

1. single need ที่ตอบตรงได้
2. multi need คนละหมวด
3. shared entity และ shared audience/date
4. negation และ condition/exception
5. comparison/list/count
6. ambiguity และ missing source ที่ควรถามกลับ/งดตอบ
7. source conflict/validity/provider unavailable
8. event edition และ rule dependencies

จำนวนตัวอย่างให้ขึ้นกับ corpus ที่มีและ coverage ที่ตรวจได้ ไม่ประกาศว่าจำนวนหนึ่งเพียงพอทุกหมวดโดยไม่มีข้อมูล ถ้าบางกลุ่มมีตัวอย่างน้อยให้รายงานว่าแปลผลกลุ่มนั้นไม่ได้

Holdout ที่เห็นผลและนำมาใช้แก้ระบบแล้วต้องเลื่อนเป็น development set พร้อมบันทึก ไม่แก้คำตอบอ้างอิงระหว่างรันเพื่อทำให้ผลดูดี ถ้าพบ gold ผิดให้เก็บ adjudication และรายงานทั้ง reference version เดิม/ใหม่จาก saved responses

### P6 — ฝึก planner ใหม่อย่างมีเหตุผล

เริ่มจาก base/model family และ LoRA configuration ที่เคยรันได้ก่อน เพื่อแยกผลของข้อมูลสอนและ contracts ที่แก้ ไม่เปลี่ยนขนาดโมเดล จำนวน calls และทุก hyperparameter พร้อมกัน

ฝึก targets ของ task graph/slots/shared refs/clarification และ operation selection วัด validation แยกตามชนิด ไม่ให้ JSON ที่สร้างสั้นลงหรือ slots ว่างทำให้ดูเหมือนดีขึ้นโดยไม่รักษาบริบท

เงื่อนไขก่อนฝึก:

- examples ที่ใช้ optimize ผ่าน annotation review ที่กำหนด
- production/native data และชุดผลเดิมถูก freeze
- schema/prompt ที่ใช้ฝึกและที่ backend ใช้ infer version ตรงกัน
- checkpoint/optimizer steps/gradients/parameter hashes และ environment บันทึกได้
- ไม่ใช้ test loss หรือคำตอบ holdout เลือกแก้ป้ายหรือเพิ่ม epochs

LoRA เป็นวิธีอัปเดตน้ำหนักแบบจำกัด ไม่ใช่หลักฐานว่าถ่ายทอด Flow ครบ การเพิ่ม epochs ไม่รับรองว่าจะเรียนเงื่อนไขที่ป้ายยังผิดหรือแทบไม่มีตัวอย่าง

### P7 — วัดสามแขนบน engine เดียวกัน

| แขน | Engine/data | Planner |
|---|---|---|
| A | candidate contracts/executors รุ่นเดียวกัน | base ไม่มี context adapter |
| B | รุ่นเดียวกับ A | adapter R121 ปัจจุบัน |
| C | รุ่นเดียวกับ A | adapter ที่ฝึกจาก labels ที่ตรวจใหม่ |

คุม source snapshot, question keys, locale, reference clock, prompt/schema, decoding, budgets, model precision/base revision และ live-provider fixture ให้ตรงกัน รักษา adapter stage ของ selector/generic calls ให้ตรงทุกแขน และบันทึก actual model identity ทุก call

ต้องตรวจ prompt/chat template ที่ backend ใช้จริงด้วย โดยเฉพาะ transport ที่ประกอบ context messages ใหม่ภายใน Accepted wire versions และ compatibility adapters ต้องใช้เกณฑ์เดียวกันทุกแขน และแยกสิ่งที่โมเดลทำนายออกจากสิ่งที่ compiler เติม R121 adapter เดิมยังไม่ได้เรียน R123 output protocol จึงต้องรายงาน protocol adaptation failures โดยไม่อธิบายทั้งหมดว่าเข้าใจบริบทผิด

ผลชุดนี้ใช้แยกประโยชน์ของ planner training ภายใต้ engine ใหม่ หากจะอ้างผลของ engine ใหม่เทียบ R122 ต้องมีอีกการทดลองที่ตรึง planner/data/clock แล้วเปลี่ยน engine เพียงตัวแปรเดียว หรือระบุ confound ให้ครบ

ไม่ใช้คะแนนของ NF4 base เป็นการเทียบตรงกับ Flow เดิมที่ใช้ Ollama GGUF คนละ representation และไม่ใช้ saved baseline ที่ data คนละรุ่นอ้าง causal gain ของ Flow ล้วน ๆ

### P8 — ตรวจ readiness และพิจารณาการวัดขนาดใหญ่

สรุป coverage matrix และปัญหาที่ยังเหลือของทุกหมวดก่อนการวัดขนาดใหญ่ จัดผลตาม request และ grade พร้อม frozen manifests และ source/model unchanged proof

Full Test เป็นการทดลองถัดจากงานออกแบบและ implementation นี้ แผนนี้ไม่ได้เริ่ม Full Test หรือรัน baseline เดิมใหม่ จำนวน/ชุดคำถาม/รุ่นและ profile ที่จะวัดต้องระบุชัดเมื่อเข้าสู่ขั้นนั้น และแยกการแจ้งจบจากการอ้างว่าคำตอบถูกทั้งหมด

## 3. Metric ที่ต้องใช้

### 3.1 Planner metrics

- task boundary/count ที่ตรง annotation
- domain/operation/field ที่ถูกตามความหมาย
- entity binding accuracy
- slot extraction และ role/scope accuracy ต่อ task
- shared-context edge correctness และ override correctness
- coverage ของ factual needs/conditions
- clarification precision และการถามกลับเกินจำเป็น
- structural/schema validity แยกรายงาน ไม่ถือเป็น semantic accuracy

### 3.2 Executor/verifier metrics

- requested options/set members ถูก execute ครบ
- source/entity/event/audience/time alignment
- arithmetic/unit correctness และ proof coverage
- source conflict/validity/provider handling ที่ถูกสถานะ
- งานอิสระถูกทิ้งเพราะ task ก่อนหน้าหรือ budget กี่ครั้ง
- unsupported operation ที่ถูกบอกตรง เทียบกับแปลงเป็น detail แบบผิดความหมาย

### 3.3 End-to-end answer metrics

- source-supported factual claims
- ตอบครบทุก need/option ตาม operation
- ไม่มี unsupported facts/permissions/conditions เพิ่ม
- correct abstention/clarification และ unnecessary refusal
- citations/claim IDs ตรงหลักฐาน
- first-line relevance และความซ้ำ/ข้อมูลนอกประเด็น
- latency แยก cold/warm, median/p95, timeout และ actual model-call count

`complete_supported_answer` นับระดับ request เมื่อทุก factual need มีคำตอบที่ถูก scope หรือมีการจัดการ ambiguity/source gap ที่ adjudicate ว่าเหมาะสม ต้องรายงานกลุ่ม answerable และ unanswerable แยกกันเพื่อไม่ให้ระบบที่ปฏิเสธทุกข้อได้คะแนนดี

กรณีตัดสิน semantic อัตโนมัติไม่ได้ต้องเก็บเป็น review_required ไม่บังคับแปลงเป็น correct/incorrect จาก keyword เพียงอย่างเดียว และไม่ใช้โมเดลตัวเดียวกับผู้ตอบเป็นผู้ตัดสินเพียงแหล่งเดียว

### 3.4 Legacy benchmark

คง strict grader เดิมไว้รายงาน route/protocol/source-ID/literal/performance failures แยกจาก semantic answer metrics หากมี API mapping ใหม่ต้อง version และอธิบายว่าเปลี่ยน interface อะไร ไม่แก้ grader เดิมเพื่อซ่อน failure

## 4. เกณฑ์ตัดสินว่าจะใช้ adapter ใหม่หรือไม่

Freeze ก่อนเห็นผล:

1. Critical source/unit/scope/contracts assertions ในชุดที่ประกาศต้องผ่านครบ
2. แยก semantic score ตามหมวด/locale/operation และรายงานตัวหาร/จำนวนตัวอย่างเสมอ
3. Adapter ใหม่ต้องแสดงประโยชน์ด้าน task/slot/shared-context และคำตอบปลายทางบนคำถามที่กันไว้ ไม่ผ่านจาก JSON อย่างเดียว
4. ตรวจ regressions สำคัญ เช่น ราคา/กลุ่มผู้ใช้/เงื่อนไข/การอ้างสิทธิ์ผิด แม้ค่าเฉลี่ยรวมดีขึ้น
5. รายงาน paired improvements/regressions และ uncertainty ของผลเมื่อจำนวนตัวอย่างน้อย
6. เป้าหมาย latency และ tolerance ต้องกำหนดก่อนรันตามการใช้งานจริง ไม่ปรับเพดานหลังรู้ผล
7. ถ้าใหม่ไม่ดีกว่าหรือดีขึ้นไม่ชัด ให้เก็บ adapter ปัจจุบันและแก้สาเหตุ ไม่ติดตั้งใหม่เพราะฝึกสำเร็จอย่างเดียว

ไม่ระบุล่วงหน้าว่าจะได้ 90/95/99% เพราะผล R121/R122 ยังไม่รองรับการคาดการณ์นั้น

## 5. แผนที่ module สำหรับ implementation

เริ่มจาก copy candidate ใน workspace ใหม่และทำ manifest ก่อนแก้ ไฟล์ชื่อใหม่ด้านล่างเป็น **ชื่อเสนอ ยังไม่ได้สร้าง implementation**

| งาน | จุดต่อจาก R122 | สิ่งที่จะสร้าง/ปรับ |
|---|---|---|
| Plan schema | domain_flow/understanding.py, context_contract.py | versioned plan contracts และ compatibility adapter |
| Context binding | context_guard.py, meaning_review.py | context_bindings.py พร้อม slot ownership/shared edges |
| Capability | readers.py, meaning_reader.py | capability_registry.py และ executor dispatch |
| Task scheduling | engine.py | task graph compiler/scheduler และ per-obligation execution |
| Model calls | model.py และ native fallback callers | ModelGateway/profile/budget ledger ชุดเดียว |
| Evidence/completeness | engine.finish_plan และ precision.py | receipt validation และ obligation verifier |
| Business reads | financial.py, service_calendar.py, policy/rule readers | operator-specific results ตาม contracts |
| Data | migrated snapshot/projection/index | compiler diagnostics และ atomic index revision |
| Response | engine._render_one และ public mapping | renderer ตาม operation และ versioned status mapping |
| Training/eval | R121/R122 scripts และ retained question pool | ชุดงานใหม่แบบ freeze; ไม่เขียนทับไฟล์เดิม |

เส้นทางอ้างอิงเหล่านี้อยู่ใต้ `r122_context_scope_calendar_20261022/revision04_system/app/knowledge/common/domain_flow/` ยกเว้น fallback callers/training scripts ที่อยู่คนละ module ต้องสำรวจ dependency ก่อนย้าย

## 6. ความเสี่ยงและวิธีป้องกันในการพัฒนา

| ความเสี่ยงที่สัมพันธ์กับปัญหาที่พบ | วิธีตรวจ/จัดการ |
|---|---|
| schema สวยแต่ความหมายผิด | วัด operation/slot scope และคำตอบจริงแยกจาก JSON validity |
| ป้ายครูผิดถูกเรียนซ้ำ | review/quarantine, source-version alignment, ไม่เชื่อ teacher score อย่างเดียว |
| planner สร้าง slots ว่างเป็นทางลัด | ดู slot-role coverage และแผนที่ยังรักษาบริบทใน quote แยกกัน |
| relation ที่เกี่ยวข้องแต่ใช้ผิด scope | receipt ต้องยืนยัน target/action/condition ไม่ใช่เพียงมีชื่อใกล้กัน |
| context guard ลบ shared slots ที่ถูก | เก็บ local/shared refs และตรวจ overrides แทน substring-only deletion |
| กฎ pronoun ทำให้ style phrase ถูกถามกลับ | regression จากคำถามเดิม เช่น “ตอบเฉพาะประเด็นนั้น” |
| compare อ่านตัวเลือกแรกแล้วหยุด | obligation ต่อ option และห้ามใช้ first duration เป็น global filter |
| model budget ทำงานหลังหาย | typed reads ทั้งหมดก่อน fallback, status budget แยก transport |
| source variants ถูกผสมเป็นนโยบายใหม่ | explicit authority/conditions; ถ้า resolve ไม่ได้ให้คง variants/conflict |
| เพิ่มข้อมูลแล้วต้องฝึกทุกครั้ง | data-update acceptance ภายใต้ schema/capability เดิม |
| ชุดทดสอบที่แก้ซ้ำดูดีเกินจริง | กัน family/holdout และย้ายชุดที่ใช้แก้แล้วเป็น dev |
| คะแนนจากคนละ revision ถูกเล่ารวม | ทุก artifact ระบุ code/data/model/question manifest |

## 7. หลักฐานที่ต้องส่งเมื่อ implement เสร็จ

1. capability matrix ที่เป็นสถานะจริงของทุก operation
2. plan/slot/shared-edge review report
3. source/data/approval preservation proof
4. training dataset split/freeze และ optimization proof ถ้ามีการฝึก
5. results ของสามแขนบน engine เดียวกัน พร้อม actual model provenance
6. per-request analysis และ source evidence ของ failures/regressions
7. strict benchmark และ semantic answer results แยกกัน
8. candidate readiness report พร้อม unsupported/gaps ที่ยังเหลือ

## 8. ที่มาของแนวทางและขอบเขตการอ้าง

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531): แนวคิดถ่ายทอดพฤติกรรมครูสู่โมเดลที่นำไปใช้ได้ง่ายกว่า ไม่ใช่การย้ายโค้ดทั้งหมดของ Flow
- [Distilling Step-by-Step](https://arxiv.org/abs/2305.02301): แสดงประโยชน์ของ supervision เพิ่มเติมในงานที่ทดลอง; การเลือกใช้ structured plans สั้น ๆ เป็นข้อเสนอสำหรับระบบนี้ ไม่ใช่ผลที่ paper พิสูจน์ให้แชทบอตนี้แล้ว
- [PICARD](https://aclanthology.org/2021.emnlp-main.779/): ตัวอย่าง constrained decoding ลด output ที่ผิดไวยากรณ์ ไม่รับรอง semantic correctness ทุกกรณี
- [DAgger / Ross et al.](https://proceedings.mlr.press/v15/ross11a.html): แนวคิดเก็บกรณีที่ learner พบจริงมาแก้ supervision; การนำมาใช้เป็น failure-review loop ที่นี่เป็นการประยุกต์ ไม่อ้าง theoretical guarantee ของงานต้นฉบับกับแชทบอตนี้

หลักฐานเฉพาะระบบที่ใช้วางแผนอยู่ใน R121/PLANNER_COMPARISON.json, R122/ANALYSIS_FINAL.json, R122/VR_SOURCE_REVIEW.json และ saved API/model logs ไม่มีการทดลองใหม่เพื่อสร้างตัวเลขในเอกสารแผนนี้
