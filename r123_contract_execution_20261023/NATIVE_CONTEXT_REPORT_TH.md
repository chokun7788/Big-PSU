# ผลพัฒนา R123: native calendar/live และบริบทคำถาม — revision05

## 1. สรุปผลจริง

พัฒนาต่อจาก foundation revision03 ใน candidate สำเนาใหม่ `revision05_system` แล้ว ส่วนที่ทำในรอบนี้คือปิดช่องทางที่ native calendar/live ข้ามบันทึก execution contract, รักษาแผนทั้งคำถามเมื่อมีหลายหมวด, แยกที่มาของ current input กับข้อความประกอบจาก history และแก้การอ้างอิงวันที่สำหรับสถานะสด

**ยังไม่ใช่ R123 ครบทั้งสถาปัตยกรรม และยังไม่ใช่ผลวัด accuracy ใหม่** ไม่ได้ฝึกโมเดลเพิ่ม ไม่ได้รัน Full Test ไม่ได้ติดตั้งทับ R78 หรือแก้ production data/approvals

อ่าน Flow ที่ปรับจริง: [FLOW_NATIVE_CONTEXT_TH.md](FLOW_NATIVE_CONTEXT_TH.md)

## 2. ปัญหาจากโค้ดที่พบและสิ่งที่แก้

| จุดเดิม | สาเหตุ | การเปลี่ยนใน candidate | ขอบเขตที่ยังเหลือ |
|---|---|---|---|
| แค่มี history ก็ข้าม R123 compiled executor | guard ใช้ `category is not None or history` ทั้งที่ legacy method ไม่อ่าน history | ประวัติทั่วไปไม่บังคับใช้ compatibility; ยังส่งต่อให้ native dialogue ที่เป็นเจ้าของการเติมช่อง | ไม่ได้ทำ history binder ครบทุกเจตนา |
| calendar/live special path ไม่มี compiled plan/ledger แบบใหม่ | public integration เรียก native adapters โดยตรง | compile ก่อน dispatch และแนบ native source/observation receipts | native predicate/text entailment ยังไม่ตรวจอิสระครบ |
| compound ตัดเป็น child แล้วที่มาของ shared target หาย | ส่งเพียง task.quote กับ child proposal | เก็บ parent plan ทั้งคำถาม สร้าง child query จาก local material และ explicit bindings ที่ compiler อนุญาต | shared-prefix ทุกรูปแบบยังไม่ครบ |
| native path อาจข้าม ambiguity/unsupported gate | ตรวจ source ภายหลังการ dispatch | ตรวจ compiled scope/capability ก่อนส่ง task เข้า special adapter | บาง operation ยังไม่รองรับและต้องแจ้งตรง ๆ |
| child ledger อาจใช้ t1 ซ้ำใน parent | child ทุกตัวมี namespace ของตนเอง | parent need ledger ใช้ t1/t2 ตามแผนทั้งคำถาม พร้อมเก็บ child contract เดิม | native child scheduling ยังตามลำดับ |
| วันที่ live ไม่ตรงกับเวลาอ้างอิงทดสอบ | resolver ใช้วันจริงของเครื่องเสมอ | เพิ่ม optional reference_date; native live reader ส่งวันจาก request clock ใน Asia/Bangkok | observation จริงยังต้องผ่าน freshness contract เดิม |
| missing binding ถูกมองคล้าย transport ล้ม | fallback ใช้ unavailable และ explicit category compatibility | เก็บ compiled plan และ terminal missing_source พร้อมบอกว่ายังไม่ได้อ่าน provider | ต้องมี binding ที่เจ้าของยืนยันก่อนใช้สถานะสดจริง |
| raw input กับข้อความ resume เสี่ยงปะปนใน audit | query ถูกประกอบก่อนเข้า Engine | แยก raw/normalized/derived provenance และที่มาของ pending query/current reply | Unicode round-trip mapping และ semantic shared scope ยังไม่ครบ |
| retry อาจเหลือ receipts ใน nested contract | native/dispatcher ล้างเฉพาะข้อมูลบางระดับ | invalidate top-level และ child delivery receipts รวม coverage/claim packets | เป็นการป้องกันส่งหลักฐานเก่า ไม่ใช่ distributed transaction กับ provider |

## 3. Flow ที่นำมาใช้

รับและเก็บ input → native delivered-state binder เมื่อเป็นการเติมช่อง → planner proposal → context guard → compile task/slot/binding/obligation → capability/scope gate → typed/native reader → source/observation verification → รวมราย task → snapshot delivery check → ส่งคำตอบพร้อมสถานะและ provenance

Engine ปกติยังอ่าน typed ทุก task ก่อน bounded selector ตาม foundation ส่วน compound ที่ใช้ native calendar/live ยังคง child execution ตามลำดับ ใช้ snapshot/cache/budget เดียวกัน จึงระบุ `typed_reads_before_fallback=false` ในเส้นทางนี้ ไม่อ้างว่า scheduler เหมือนกันทั้งระบบแล้ว

## 4. ผลตรวจ

| การตรวจ | ผล | สิ่งที่ตัวเลขนี้บอก |
|---|---|---|
| Foundation regression gates | **35/35 ผ่าน** | compile, task isolation, source/numeric/option guards และ typed-first ของ Engine ปกติ |
| Native/context gates | **27/27 ผ่าน** | request clock, source pointers, stale/wrong-date observations, provenance, history boundary, cache และ retry invalidation |
| Native packaging unit gates | **5/5 ผ่าน** | contract/receipts ส่งผ่าน package ได้ ไม่ใช่ HTTP benchmark |
| Annotations เดิม | **289 แถว compile ได้** | โครงสร้างผ่าน ไม่ใช่ semantic-review ครบ |
| Saved proposals เดิม | **40 observations / 32 unique question keys** | replay ด้วยข้อมูลเดิมและไม่เรียกโมเดล |
| Native adapter outputs | **12 observations / 7 question keys** | มีการใช้คำถามเดิมซ้ำภายใต้ fixture ต่างกัน ไม่ใช่ 12 คำถามใหม่ |
| เทียบกับ R123 revision03 บน saved proposals 40 ชุด | **คำตอบ/สถานะ/claims เปลี่ยน 0 ชุด** | ไม่พบ regression ในชุด replay นี้ ไม่ใช่การพิสูจน์ว่าแม่นขึ้น |
| Model inference ใหม่ / optimizer steps ใหม่ | **0 / 0** | ยังไม่ได้วัด planner ใหม่หรือฝึกต่อ |

ไม่รวมจำนวน gates เป็นเปอร์เซ็นต์ความถูกต้องของแชท และไม่ถือว่า source-pointer pass เท่ากับคำตอบถูกเชิงความหมาย

### กรณีสำคัญที่ตรวจ

- คำถามเดิมเรื่อง pc2 เวลา 3pm: ข้อมูลจริงยังไม่มี binding จึงไม่อ่าน provider และไม่ยืนยัน occupancy
- คำถามเดิมเดียวกันบน binding/observation จำลองในหน่วยความจำ: native reader ทำงานได้ เมื่อข้อมูลสด วันถูก และ mapping ถูก
- เมื่อ observation เก่าเกิน TTL: ไม่ยกระดับเป็น supported
- เมื่อ observation เป็นคนละวัน: ไม่ยกระดับเป็น supported
- เมื่อบังคับ freshness_checked=true แต่ timestamp เก่า: bridge ปฏิเสธ
- อ่าน scope เดิมสองครั้งใน request context เดียว: ใช้ provider snapshot ร่วมกัน อ่าน provider ครั้งเดียว
- คำถาม “วันนี้เปิดไหม” หลัง normalization: ทดสอบ native calendar dispatch โดยใช้ข้อมูลจริงจากสำเนา ไม่อ้างช่วงจองเป็นการเปิดเข้าศูนย์
- คำถามเดิม “How to book VR and what days are available”: มี parent plan สอง task; booking ยังตอบส่วนที่มีหลักฐานได้แม้ schedule ยังไม่ยืนยัน
- ประวัติ assistant ที่เป็น prose และไม่มี delivered state: ไม่ถูกนำมาเป็น facts/state
- ช่วงข้อความของ resumed query: มีป้าย derived source แยกจาก current raw
- snapshot retry: ล้าง receipts ทั้ง parent และ nested child contracts

### ข้อสังเกตจากการพัฒนา tests

เก็บ failed runs เดิมไว้ ไม่เขียนทับ:

1. native verification รอบแรกสร้างข้อเสนอทดสอบไม่ครบ root fields ของ wire R121 (`focus/context_quotes`) จึงถูก parser ปฏิเสธ แก้ที่ harness โดยใช้ label เดิมทั้ง envelope
2. รอบถัดมาคาดว่าจะมี live binding ในฐานข้อมูลจริง แต่ตรวจพบว่าไม่มี และ calendar unit call ข้าม normalization ที่ public pipeline ทำตามปกติ จึงแยก fixture ในหน่วยความจำกับการตรวจข้อมูลจริง และปรับ harness ให้ผ่าน normalization ตามเส้นทางจริง
3. ระหว่าง review เพิ่ม guard contract สำหรับ missing binding และแก้ parent task IDs ใน revision05 โดยเก็บ revision04 และผลเดิมไว้

ข้อผิดพลาดของ harness ข้างต้นไม่ถูกนับเป็น semantic failures ของโมเดล และผลที่ผ่านภายหลังไม่ได้ลบหลักฐานรอบที่ไม่ผ่าน

## 5. เรื่องข้อมูลที่ต้องแยกจากปัญหา Flow

### 5.1 สถานะเครื่องว่างยังยืนยันจริงไม่ได้

ฐานข้อมูล candidate นี้มี **live_binding=0** ดังนั้นแม้ native bridge ทำงาน การถามว่าง/ไม่ว่างยังต้องตอบว่าไม่มีการเชื่อมที่ยืนยันได้ การใส่ binding ต้องทราบ service/resource/provider key/physical pool/status mapping/timezone/freshness policy ที่ถูกต้องจากระบบจริง ไม่ควรเดาแล้วใส่เพื่อให้คะแนนผ่าน

binding ที่ใช้ verification เป็นข้อมูลจำลองใน memory เท่านั้น ไม่เขียนลง DB ไม่เปลี่ยน approvals และไม่ใช่ผลสถานะเครื่องจริง

### 5.2 เวลาเปิดกับช่วงจองไม่เหมือนกัน

source ที่มีเพียงตาราง bookable/maintenance หรือขอบเขตโซน/ช่วงมีผลยังไม่ชัด ไม่ควรถูกสรุปว่าเปิดเข้าอาคารได้วันนี้ การตอบไม่ยืนยันในกรณีนี้อาจเป็นข้อจำกัดของ source/predicate ไม่ใช่เพียง classifier เลือกหมวดผิด

### 5.3 Distillation ยังไม่แก้ source/authority โดยอัตโนมัติ

การฝึก planner เพิ่มจาก labels ที่ยัง review ไม่ครบสามารถสอน scope ผิดให้โมเดลได้ รอบนี้จึงแก้ทาง execute/provenance ก่อน ข้อมูลธุรกิจยังอ่านจากฐานกลางปัจจุบัน ไม่ฝังราคา/นโยบายลงน้ำหนักเพื่อชดเชย binding ที่ขาด

## 6. ความครบถ้วนและข้อจำกัดปัจจุบัน

| ส่วน | สถานะ |
|---|---|
| Compiled task/slot/binding/obligation foundation | ทำแล้ว |
| ปกป้อง ordinary history ไม่ให้ข้าม compiler โดยไม่จำเป็น | ทำแล้ว |
| Native calendar/live/missing-binding audit bridge | ทำแล้วใน accepted planner paths |
| Raw/normalized/derived provenance | ทำแล้ว โดยไม่อ้าง exact raw span สำหรับ synthetic query |
| Shared-prefix audience/date/เงื่อนไขซ้อนทุกแบบ | ยังไม่ครบ |
| Unicode/NFC raw-offset round-trip ทุกกรณี | ยังไม่ครบ; inherited normalizer offsets ไม่ใช่ gold alignment อัตโนมัติ |
| Typed history binder ครบทุกหมวด | ยังไม่ครบ ใช้ native delivered-state adapters ที่มีอยู่ |
| Planner wire ใหม่ตรงตาม R123 design | ยังไม่ทำ ใช้ R121 wire adapter |
| Native compound global typed-first scheduling | ยังไม่ทำ child execution ยัง sequential |
| Independent semantic entailment ของข้อความ native ทุกประโยค | ยังไม่มี pointer/registered adapter checks ไม่ใช่ universal verifier |
| Data compiler/authority/supersession/collection adapters ครบ | ยังไม่ครบ |
| Labels ที่ semantic-review ครบ / training ใหม่ / three-arm heldout test | ยังไม่ทำ |
| Production readiness / Full Test ใหม่ | ยังไม่ประกาศ |

การรับข้อมูลใหม่จากเจ้าของยังต้องผ่าน schema, source references, ขอบเขต และ operator ที่ตัวอ่านรองรับ การเก็บ record เพิ่มสำเร็จไม่ได้พิสูจน์ว่าทุกคำถามจะดึง record นั้นตอบได้ครบแล้ว

## 7. การรักษาของเดิม

ตรวจ hash ของไฟล์ที่ตรึงไว้ **8,012 ไฟล์ เปลี่ยน 0 ไฟล์** ครอบคลุมแหล่งก่อนหน้า, candidate ที่ผ่านการตรวจ, design documents, training inputs และ adapter ที่เกี่ยวข้อง

- Database SHA256: `029119eaa24e53b4110c6c8cc7f650674f68e03ee605929cea8f23857a6429d3`
- R121 adapter SHA256: `e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8`
- ไม่ติดตั้งทับ R78/production และไม่เปลี่ยน real data/approvals
- ไม่เปิด model/chat server ใหม่ในรอบนี้ ตรวจ launcher ด้วย `--check-config` เท่านั้น

## 8. หลักฐานและ entry point

- [สถานะล่าสุด](NATIVE_CONTEXT_STATUS.json)
- [Hash/source preservation](NATIVE_CONTEXT_FINAL_VERIFICATION.json)
- [Regression เทียบ revision03](NATIVE_CONTEXT_REGRESSION.json)
- [Foundation gates](verification_1792697182134450600/VERIFICATION.json)
- [Native/context gates](native_verification_1792697133991208100/VERIFICATION.json)
- [Native responses และ artifacts](native_verification_1792697133991208100/OUTPUTS.json)
- [Packaging unit gates](PACKAGE_VERIFICATION_1792697206503911600.json)
- [Manual launcher ของ revision05](launch_revision05.py)

launcher ใหม่ใช้ R121 checkpoint เดิมและ live-provider fixture unavailable เช่น workload เปรียบเทียบก่อนหน้า ไม่มีการเปิดสถานะจริงให้โดยอัตโนมัติ ส่วน launcher เดิมยังคงชี้ candidate รุ่นเดิมเพื่อรักษางานที่ผ่านมา

## 9. ลำดับถัดไป

ปิดช่องว่าง shared-prefix/typed history/offset alignment → ขยาย authority/collection/operator diagnostics → review labels ทั้งชุด → ตรึง wire/prompt/split → ฝึก planner ต่อ → เปรียบเทียบ base/current/new adapter บน engine/data เดียวกันและ family ที่ยังไม่ใช้พัฒนา → ประเมิน readiness ก่อน Full Test

ประโยชน์ที่ยืนยันได้ของรอบนี้คือ execution ตรวจสอบย้อนกลับและแยกเหตุที่ตอบไม่ได้ได้ดีขึ้น พร้อมไม่พบการเปลี่ยนคำตอบ/claims บน replay 40 ชุด ยังไม่มีหลักฐานพอจะให้เปอร์เซ็นต์ความแม่นยำใหม่
