# วิธีพิสูจน์ว่า Flow ที่เสนอช่วยจริง และการตรวจทานแผน 3 รอบ

สถานะ: แผนทดสอบและ design review เท่านั้น ยังไม่ได้รันข้อใดในแผนนี้กับ chatbot

## 1. คำว่า “คะแนนดีกว่า” ต้องมีสองแกน

### แกน A — เกณฑ์เดิมเพื่อรักษาความเทียบกันได้

- ใช้ keys/grades/ตัวตรวจเดิม และรายงานผลดิบเดิมโดยไม่แก้ GT ย้อนหลัง
- แสดง strict/protocol กับ positive text-clause แยกกัน
- แยก request-level all-needs จากจำนวน grades เพราะหนึ่งคำถามอยู่หลายไฟล์ GT ได้
- ห้ามอ้างว่าเพิ่มจาก 74.59% เป็นเลขใหม่เมื่อเปลี่ยน denominator หรือเกณฑ์ไปแล้ว
- เป้าหมาย 94.41% ของ Legacy เป็น reference ไม่ใช่ผลที่รับประกัน ไม่กดให้ผ่านด้วยคำสำคัญหรืออนุญาตราคาเก่า

### แกน B — ความถูกต้องของธุรกิจ ณ source/date ที่ตรงกัน

- ตรึง source snapshot, effective time, availability fixture, locale และ business scope
- label คำถามแต่ละส่วนว่า answerable, missing, ambiguous, not_current, conflicting หรือ live-unavailable
- ประเมิน facts/conditions/units/negation/completeness จาก source เดียวกัน
- ถ้าต้องแก้ oracle ให้ทำ version ใหม่แยก มีเหตุผลและ diff ไม่ทับข้อมูลเก่า
- ถ้าไม่มีคำตอบ Legacy บน source/date/เกณฑ์ใหม่นี้ จะอ้างว่า “ชนะ Legacy บนเกณฑ์ใหม่นี้” ไม่ได้

ผลทั้งสองแกนต้องรายงานคู่กัน ไม่เลือกเฉพาะแกนที่ทำให้รุ่นใหม่ดูดี

## 2. Diagnostic experiments เพื่อแยกคอขวด

ทดลองใน sandbox/candidate ใหม่เท่านั้น ห้ามให้ oracle plan รั่วเข้า runtime จริง ไม่มีการรันในงาน R96 นี้

| ทดลอง | ป้อนอะไรเพิ่ม | ส่วนที่ตรึง | ถ้าดีขึ้นบอกอะไร |
|---|---|---|---|
| A0 | คำถามจริง | baseline R95 | ฐานเทียบ |
| A1 | task/slots ที่ตรวจจาก source แล้ว | reader/executor/renderer | ติดการตีความคำถามหรือ qualifier |
| A2 | task เหมือน A1 + candidate IDs ที่ถูก | executor/renderer | ติด candidate retrieval/linking |
| A3 | task+IDs+relation path/field projection ที่ถูก | source/renderer | ติด read graph/schema mapping |
| A4 | evidence packet ที่ครบและตรวจแล้ว | renderer/output guards | ติดการใช้ evidence หรือ blanket rejection |
| A5 | typed claim set ที่ถูก | final rendering/delivery | ติดภาษา/รูปแบบ/state commit |

แผน gold ต้องอ้าง source ไม่ใช่ถือว่าคำตอบ Legacy ทุกอันถูก กรณีข้อมูลไม่พอจริงคงสถานะไม่พอทุกแขน ห้ามใส่ค่าที่ไม่มีใน source เพื่อทำให้ตอบได้

ทดลองนี้เป็น counterfactual diagnostic ภายใน pipeline ไม่ใช่หลักฐานสาเหตุเชิงสถิติที่ควบคุมทุกปัจจัย เพียงช่วยจัดตำแหน่งที่ควรแก้ก่อน

## 3. ประเมินเป็นชั้น

| ชั้น | ตัวชี้วัด | สิ่งที่ยังสรุปไม่ได้จากตัวเลขนี้ |
|---|---|---|
| Input | protected-span preservation, recovery task invariance | normalize ได้ไม่ได้แปลว่าคำถามถูกตีความ |
| Plan | task accuracy, slot/qualifier binding, all-needs extraction | task ถูกไม่ได้แปลว่า source มีข้อมูล |
| Retrieval | evidence/claim recall at K, candidate kind accuracy | ชื่อถูกไม่ได้แปลว่า clause ครบ |
| Read | relation path correctness, required-claim availability | fields ครบไม่ได้แปลว่า current |
| Evidence | sufficient/insufficient/conflicting/current classification | sufficiency classifier ก็ผิดได้ |
| Execute | numeric/unit/date/audience/rule-condition exactness | ได้ตัวเลขถูกยังอาจตอบไม่ครบคำถาม |
| Answer | supported-claim precision, requested-need recall, contradiction | semantic similarity อย่างเดียวตรวจข้อยกเว้นไม่พอ |
| Interaction | unnecessary clarification rate, missing-fact guessing, state carryover | ถามกลับน้อยลงอาจเกิดจากเดามากขึ้น |
| Reliability | transport/body/schema/semantic/delivery success แยก | HTTP เปิดได้ไม่เท่ากับตอบถูก |
| Performance | wait/model/processing time, p50/p95/p99, queue admission | batch completion time ไม่ใช่ multiuser SLA |

สูตรหลัก:

- **Requested-need coverage** = needs ที่ตอบหรือระบุสถานะขาดอย่างถูกต้อง / needs ที่ผู้ใช้ถามจริง
- **Answerable fulfillment** = needs ที่มีหลักฐานพอและได้รับคำตอบถูก / answerable needs
- **False abstention** = answerable needs ที่ถูกปฏิเสธ / answerable needs
- **Unsupported assertion** = claims ที่ยืนยันโดยไม่มีหลักฐานเพียงพอ / asserted claims
- **Condition preservation** = เงื่อนไขจำเป็นที่คงความหมายครบ / เงื่อนไขจำเป็นจาก source และคำถาม

ต้องไม่ใช้ coverage เพียงค่าเดียว เพราะระบบที่บอก unknown ทุกเรื่องอาจดูเหมือนครอบคลุม ต้องรายงาน fulfillment และ unsupported assertions คู่กัน

## 4. การตรวจคำตอบโดยไม่ overfit กับเฉลย

1. structured facts ตรวจตามค่า/หน่วย/ชนิด/วันที่/ID และ qualifier
2. rule/policy ตรวจ required propositions + applicability + exceptions + prohibitions
3. free prose ใช้ความหมายร่วมกับ source support เป็นตัวช่วย ไม่บังคับแปลตามประโยคอ้างอิงทุกคำ
4. proper nouns ใช้ canonical aliases ไม่ถือชื่อไทยเป็นการแปลผิดอัตโนมัติ
5. แยก contradictions ออกจาก neutral/no-support; ห้ามให้ทั้งสองถูกกลบเป็น similarity ต่ำค่าเดียว
6. อย่าให้ Typhoon 4B ที่เลือกข้อมูลเป็นผู้ตัดสินความถูกต้องของตัวเองเพียงคนเดียว
7. หากใช้ semantic judge ต้องตรึงรุ่น/prompt ตรวจด้วย positive/negative controls และเก็บ disagreement เป็น uncertain
8. เรื่องธุรกิจที่ไม่มีหลักฐานให้อยู่ owner-data queue อย่าให้ auto judge แต่งนโยบายเพื่อปิด issue

อาศัยแนวคิด RAGChecker และ Semantic Answer Similarity แต่ยังต้องสร้าง control set ไทย/อังกฤษของเรา เพราะบทความเหล่านั้นไม่รับรองตัวตรวจบนชุดนี้

## 5. ชุด focused evaluation ที่เสนอ

จำนวนจริงต้องสร้างและตรึง manifest ก่อนปรับโค้ด ไม่ใช่รันสุ่มเพิ่มจนได้คะแนนที่พอใจ

### 5.1 Minimum functionality

- คำถามข้อมูลศูนย์/ติดต่อ/สถานที่/บุคลากร ที่มี source
- เกมคืออะไร/เล่นยังไง/อยู่โซนไหน/กี่คน/บัญชี/controls โดยชื่อและ relation ใหม่
- hourly fee/rental/budget/เปรียบเทียบหลายกลุ่มและหลายระยะเวลา
- วันนี้เปิดไหม/วันศุกร์บ่าย/วันปิดพิเศษ/ตารางจองประจำ/slot สด
- permission/procedure ที่มีทั้งเงื่อนไขและข้อยกเว้น
- กติกาแยกเกม/event/edition/topic และข้อกฎที่ต้องอ่านพ่วง
- current/historical/future-effective/conflict/missing information

### 5.2 Invariance — เปลี่ยนรูปประโยคแต่สาระคงเดิม

- เพิ่ม/ซ้อน “ขอสอบถาม”, “Please tell me”, “ก่อนจะไปใช้บริการ”
- คำซ้ำ คำหาย การสลับตัวอักษร รวมไทย-อังกฤษ โดยไม่แตะเลขรุ่น/เวลา/negation
- สลับลำดับประโยคหลาย need โดยไม่ทำให้ subject เปลี่ยน
- เปลี่ยนชื่อรายการเป็น record ใหม่ชนิดเดียวกัน โดย relation เดิมถูกต้อง
- ปรับ style คำอธิบาย schema โดยความหมายคงเดิม

### 5.3 Directional/contrast — สาระเปลี่ยนต้องตอบเปลี่ยน

- บุคคลภายนอก → นักศึกษา PSU
- วันศุกร์เช้า → วันศุกร์บ่าย; วันนี้ → วันปิดพิเศษ
- game edition/platform/mode/event คนละชุด
- “นำอาหารเข้า” → “รับประทานตรงเครื่อง” → “นำของตัวเองเข้า” ไม่รวมเป็นสิทธิเดียวกัน
- “เกมมีไหม” → “เครื่องที่เล่นเกมนั้นว่างตอนนี้ไหม”
- “กฎก่อน First Blood” → “หลัง First Blood”
- จำนวนผู้เล่นในเกม → จำนวนที่นั่ง → จำนวนผู้เล่นลงทะเบียนแข่ง
- สลิปผิดรูป → ยอดเงินผิด → ชื่อผู้เล่นผิด ต้องไม่ยืมคำตอบคนละนโยบาย

### 5.4 Multi-turn ที่ต้องพิสูจน์

| ลำดับบทสนทนา | สิ่งที่คาดหวังเชิงโครงสร้าง |
|---|---|
| ขอราคาบุคคลภายนอก → ถามเครื่อง → PC | ราคา + audience เดิม โดยอ่าน current rate ใหม่ |
| ขอราคาทั้งหมด → ทั้งหมด | list services ใน scope เดิม ไม่ generic no-answer |
| ขอกติกาเกมหลุด → ถามเกม → ROV | rule topic เดิม + game ใหม่ ไม่ game catalog |
| ถามราคา PC → เปลี่ยนเป็น VR | เปลี่ยน service; ถ้ากลุ่มเดิมยังใช้ได้ให้รักษา ไม่ใช้ราคาเก่า |
| ถูกถามวัน → พรุ่งนี้ | resolve date จาก reference time และ timezone เดียว |
| ถามรายละเอียด → อันที่สอง | อ้างตัวเลือกที่ส่งจริง ไม่อ้างรายการภายในที่ไม่ได้แสดง |
| ถูกถามเครื่อง → ไม่ใช่ อยากรู้วิธีจอง | reset pending price slot ไป procedure |
| มี state เก่า → owner ถอนรายการ | ไม่ใช้ facts เก่าหรือ resurrect withdrawn record |

### 5.5 New/edit/withdraw โดย data only

ทุก kind ทั้ง 24 ต้องมี fixture ขั้นต่ำสร้างใหม่/แก้ field ที่ใช้ตอบ/ถอน พร้อมความสัมพันธ์ตามจริง เฉพาะ task ที่มี capability อยู่แล้ว

ราคาและกฎให้เพิ่ม boundary dates และ revision race; relational kinds ต้องมี broken-reference negative case; live_binding ใช้ fixture ที่รู้ผล ไม่แตะรายการจองจริง

## 6. ป้องกัน leakage จากการแก้ซ้ำ

- corpus เดิมถูกอ่านหลายรอบแล้ว ใช้เป็น regression set ไม่เรียกว่า unseen holdout
- แบ่ง dev/validation/holdout ตาม task family, source fact และ template family ไม่สุ่มแยก typo ของคำถามเดียวกันคนละฝั่ง
- ทดสอบชื่อ/records ใหม่ที่ไม่มีใน examples และ legacy aliases
- แยก model-generated questions จาก owner-confirmed propositions; คำถามที่โมเดลสร้างไม่ใช่ความจริงอ้างอิง
- ตั้ง seed/hash และ manifest ก่อนรัน; เก็บ first-result ไม่ retry เฉพาะที่ผิดเพื่อแทนคะแนนเดิม
- เก็บจำนวนคำถาม unique และจำนวนเกณฑ์ซ้ำจากหลาย GT files ให้เห็น
- ถ้ารายงานช่วงความไม่แน่นอน ให้ resample ตามกลุ่มคำถาม/ข้อเท็จจริงที่เกี่ยวข้อง ไม่ถือว่า grades ซ้ำเป็นตัวอย่างอิสระ

## 7. ลำดับทดลองเมื่อได้รับงาน implementation

1. เก็บ R95 เป็น baseline frozen และสร้าง candidate ถัดไปแยก
2. ทำ source-backed triage ของกลุ่ม representative โดยเก็บ unresolved ที่ยังยืนยันไม่ได้
3. รัน diagnostic A1–A5 กับกลุ่มเกี่ยวข้อง เพื่อเลือกตำแหน่งแก้
4. ทำ P1/P2 ก่อน แล้ว focused regression + counterexamples
5. เพิ่ม relation/domain executors ทีละหมวดและ data-only fixtures
6. เพิ่ม bounded LLM planner เฉพาะเมื่อ deterministic coverage ยังขาด
7. ใช้ heldout ที่ตรึงไว้ประเมินแพ็กเกจรวม พร้อม ablation legacy-interpreter/common-only/semantic-assist
8. full test ใหม่เป็นขั้นแยกตามคำขอ และเก็บ raw failures ทุกครั้ง
9. ยังไม่เปลี่ยน production จน review ตัวอย่างที่ regress และ safety-critical business claims

ไม่มีการรัน full test หรือ focused chatbot test ในงานค้น paper รอบนี้

## 8. Acceptance gates ที่เสนอ

เป็นเงื่อนไขทางวิศวกรรมที่ต้องตรวจจริง ไม่ใช่ตัวเลขจากบทความหรือผลที่เกิดขึ้นแล้ว

- ต้องไม่มี regression ที่ยังไม่อธิบายได้ใน cases ราคา/หน่วย/นโยบาย/ข้อยกเว้น/live ที่ source รองรับชัด
- actual unsupported assertions ใน critical fixtures ต้องเป็นศูนย์; ศูนย์บน fixture ไม่รับรองศูนย์ในโลกจริง
- false abstention ต้องลดจาก baseline บน answerable set เดียวกัน โดย unsupported assertions ไม่เพิ่ม
- answerable fulfillment ต้องดีขึ้นแยกไทย/อังกฤษ และไม่อาศัยเปลี่ยนกรอบคำถามให้แคบลง
- owner lifecycle fixtures และ scope boundaries ต้องผ่าน; ไม่ใช้ facts เก่าเมื่อแก้หรือถอน
- หากอ้างเทียบเท่า/เหนือ Legacy ต้องเทียบตาม source/date/เกณฑ์ที่เข้ากัน พร้อมแสดง raw historical score เดิมแยก
- เวลา p95/model busy ต้องไม่แย่ลงอย่างมีนัยต่อการใช้งาน; กำหนด SLA และ workload ก่อนทดสอบ ไม่อนุมานจาก batch 4 workers

## 9. ตรวจทานแผนสามรอบ

เป็นการ review เอกสารและ failure scenarios ไม่ใช่การทดลองสามรอบกับระบบ

### รอบ 1 — ตรวจว่าข้อมูลกลางอย่างเดียวพอหรือไม่

**ข้อบกพร่องของร่างแนวทาง:** คิดว่ามี schema descriptions แล้ว LLM จะเลือก field ตรงเอง; ย้ายเกมใหม่แต่ alias/parser ยังผูกชื่อเก่า

**ปรับแล้ว:** เพิ่ม Legacy pure interpreter interface, task descriptions + demonstrations, required claims, relation read alternatives และการตรวจ old-fact imports

**ส่วนที่ยังต้องพิสูจน์:** D3ST/SDT มีการฝึกเฉพาะในงานวิจัย ไม่มีหลักฐานว่าจะได้ผลเดียวกันด้วย prompting บน 4B ต้องใช้ heldout จริง

### รอบ 2 — ตรวจความถูกต้องของเงื่อนไขและคำตอบบางส่วน

**ข้อบกพร่องของร่างแนวทาง:** ผ่อน unresolved clauses อาจทำให้ข้อมูลทั่วไปถูกใช้ตอบเงื่อนไขเฉพาะ; ตอบบางส่วนอาจแฝงข้อสรุปจากราคาที่ไม่มี

**ปรับแล้ว:** แยก discourse จาก semantic qualifier, per-need statuses, dependency-aware partial answers, exact checks สำหรับหน่วย/negation/conditions และ counterexamples ที่เปลี่ยน qualifier

**ส่วนที่ยังต้องพิสูจน์:** free-text source ที่ขอบเขตคลุมเครือยังต้องใช้ source review หรือ uncertain queue ไม่ปิด guard ทิ้ง

### รอบ 3 — ตรวจ production updates เวลา และการพิสูจน์คะแนน

**ข้อบกพร่องของร่างแนวทาง:** index กับ snapshot อาจไม่ใช่ revision เดียว; history/cache อาจดึง facts หลังถอน; เพิ่ม retrieval/LLM calls จนแย่ด้านเวลา; เปลี่ยน evaluator แล้วอ้างชนะเดิม

**ปรับแล้ว:** pinned release/index publication, epoch-sensitive cache/state, bounded calls/deadline, lifecycle negative fixtures, แกนคะแนน A/B แยก และห้ามใช้ corpus เดิมเป็น unseen holdout

**ส่วนที่ยังต้องพิสูจน์:** actual workload SLA, Thai semantic judge calibration และราคา/นโยบายที่ไม่มี source ปัจจุบัน ไม่สามารถแก้ด้วย flow ล้วน

## 10. สิ่งที่ทำเองได้กับสิ่งที่ต้องมีข้อมูลเจ้าของ

| ทำเองได้จากหลักฐานที่มี | ต้องมี source/authority เพิ่มหากยังไม่มี |
|---|---|
| แยก log categories และ query→need trace | อัตราราคาที่หมดอายุจะต่ออายุหรือเปลี่ยนเท่าไร |
| ย้าย pure interpreter และทดสอบชื่อใหม่ | นโยบายคืนเงิน/เลื่อนวันที่ข้อมูลขัดกัน |
| แก้ field/relation execution ตาม schema ที่มี | รายละเอียดโหมด/จำนวนผู้เล่นที่ไม่มีใน source |
| targeted clarification และ trusted state | คำแปลนโยบายที่ต้องได้รับอนุมัติก่อนเผยแพร่ |
| bilingual test harness และ checker control sets | สิทธิ/กฎใหม่ที่เจ้าของยังไม่เคยให้ |
| release/index/cache consistency และ diagnostics | ข้อมูลสดเมื่อ upstream ไม่พร้อมใช้งาน |

สิ่งที่ผู้ใช้เคยยืนยันไว้แล้วให้นำหลักฐานนั้นมาใช้ ไม่ถามซ้ำ ถ้าข้อมูลมีแต่อ่านไม่เจอเป็นหน้าที่ระบบแก้ ไม่ผลักกลับให้เจ้าของกรอกใหม่ทุกครั้ง
