# R111 — ลำดับพัฒนาและเกณฑ์รับ Flow ตามหมวด

สถานะ: แผนงาน ยังไม่ได้แก้โค้ดใช้งานหรือรัน customer/full test ในรอบนี้

## 1. เลือกฐานพัฒนาอย่างไร

ใช้ candidate เดียวต่อจาก R106 เพื่อรักษา owner lifecycle, typed schema, snapshot และงาน game detail ที่ดีขึ้น พร้อมนำพฤติกรรม R95/Legacy กลับมาเป็น adapter เฉพาะจุดที่มีหลักฐานว่าตอบตรงกว่า ไม่ fork ระบบหลายตัวแล้วสลับคำตอบตามคะแนนรายหมวด

ฐานข้อมูลตอบเพียงชุดกลางที่เลือก revision ชัดเจน Legacy เป็นแหล่งอ้างอิงพฤติกรรม/การแยกภาษาและโจทย์ ไม่เป็น fallback source ของค่าราคา เกม หรือกฎจริง

## 2. ลำดับทำงาน

### ขั้น 0 — ตรึงข้อเท็จจริงและข้อคาดหวัง

1. แยก source snapshot จาก runtime snapshot และ reference time ของ workload
2. สร้าง intake mapping ของ R108/R109: source answer → record/field/predicate → known/unknown/conflict → เวอร์ชันที่ใช้ตอบ
3. จัดเคสเก่าเป็น expected ยังตรง / เจ้าของแก้ข้อมูลใหม่ / oracle ผูก protocol / คำถามกำกวม / ขาดหลักฐานจริง
4. เก็บคู่คำถาม–คำตอบ Legacy/R95/R106 เป็น retained evidence โดยไม่รัน baseline ใหม่

**เสร็จเมื่อ:** ทุกค่าที่จะเปลี่ยนมี source และรู้ว่าต้องไปฟิลด์ใด; ไม่ถือว่า JSON รับเข้าคือ runtime ใช้แล้ว

### ขั้น 1 — นำข้อมูลที่เจ้าของยืนยันเข้าชุด candidate ให้ถูกช่อง

| ชุดข้อมูล | สิ่งที่ต้องลง | ระวัง |
|---|---|---|
| ราคาเดิมที่ยืนยันล่าสุด | current confirmation ผูก amount references และเวลาที่ตอบ | ไม่แก้วันมีผลย้อนหลัง/รับรองทุกวันอนาคต |
| ราคาเหมา 24 rows | duration 180/420 นาที + periods + source ของแต่ละ field | เหมาเต็มวันรวมเที่ยงไม่เปลี่ยน hourly slots |
| คำตอบบริการทั่วไป | policy/procedure ตาม action และเงื่อนไข | Steam ไม่ตอบ console; capture เกมไม่ตอบการถ่ายคน |
| PS5 จอย | controllers_per_console=2 กับ resource/service scope | ไม่ใช้แทนจำนวนผู้เล่นทุกเกม |
| ผู้เล่นต่างกลุ่ม | audience ต่อผู้เล่น + billing unit ของรายชั่วโมง | ไม่คูณราคาเหมาห้องต่อคน |
| ชื่อ/ตำแหน่ง | public field scope ตามคำยืนยัน group_people | ไม่ขยายสิทธิ์ข้อมูลส่วนตัว |
| กติกา 4 เล่ม | event identity + clauses + dependency + owner corrections | ไม่ mark complete ทั้งเล่ม; Tekken unit deferred |
| เปลี่ยน/ยกเลิก/ชำระ | เงื่อนไขราย action และ source priority | ไม่กลับคำปฏิเสธหรือทิ้งหนึ่งชั่วโมง/สลิปเดิม |

**เสร็จเมื่อ:** อ่าน candidate ผ่าน read API พบค่าที่คาดและ source ตรง; readiness ราย task ไม่บล็อกเพราะ optional field ที่ไม่เกี่ยวข้อง

### ขั้น 2 — แก้สัญญา Need/AnswerPacket และลำดับ dispatch

1. คง infrastructure เดิม ไม่เพิ่ม global orchestrator ทับอีกชุด
2. เลือก subject + predicate + qualifiers ก่อนให้ตัวอ่านตอบ และห้าม adapter เปลี่ยนงานเงียบ ๆ
3. แยก result status: interpretation miss ไม่ใช่ source gap ไม่ใช่ provider failure
4. ตัวอ่านที่ไม่ครอบคลุม predicate ต้องคืน not_applicable/mismatch ไม่ใช่คำตอบทั่วไป non-None
5. allow corrective interpretation แบบจำกัดหนึ่งครั้งเมื่อผิด task หรือ evidence ไม่ตรง ทั้งที่ยังมี candidate ที่ตรง ห้ามวนหลาย adapter/LLM ไม่จำกัด
6. ทำ required-claims ต่อ predicate และตรวจ hard dependencies ต่อ need; ข้อมูลขาดของคนละ need ไม่ทำลายส่วนที่ตอบได้

**เสร็จเมื่อ:** trace บอกได้ว่าทุก need เข้าตัวอ่านใด มี claim ใดตอบ และสาเหตุที่ตอบไม่ได้อยู่ที่ชั้นใด

### ขั้น 3 — แก้แต่ละหมวดให้ครบก่อน full test

ลำดับความสำคัญจากขนาดช่องว่างและผลกระทบ:

1. ราคา/เหมา + การเชื่อม owner confirmation
2. ตารางเปิด/จอง/maintenance และ public directory ที่ถูก gate
3. booking policy/procedure และคำถามเงื่อนไข/ปฏิเสธ
4. equipment count/location/list; game catalog และ player-filter
5. controls และกติกาเฉพาะ clause/dependency
6. การประกอบหลาย needs, followup และภาษาในทุกหมวด

ไม่ใช้คะแนนของหมวดหนึ่งมาปิดงานทั้งระบบ แต่ละ adapter ต้องทำ input/read/output และ data-only update path ครบ

### ขั้น 4 — วนทบทวนแผน/โค้ดโดยยังไม่กวาด customer corpus

- รอบขอบเขต: คำถามแต่ละแบบไปถูก predicate หรือไม่ รวมคำคล้ายข้ามหมวด
- รอบ source/gate: required vs optional, scope, validity, authority, withdraw และ clause dependencies
- รอบประกอบคำตอบ: multi-need, unit, negation, ภาษา, pagination และ state หลัง owner เปลี่ยนข้อมูล

ระหว่างพัฒนาตรวจ static/schema/mapping และ pure calculation invariants ตามส่วนที่เปลี่ยน ไม่ใช้การรัน 91 คำถามซ้ำหลายรอบแล้วตีความเป็นความแม่นยำเต็มระบบ

### ขั้น 5 — Full Test หลัง implementation และข้อมูลพร้อมทั้งชุด

เฉพาะ common Flow ใหม่ + LLM ON ตามขอบเขตที่ผู้ใช้เคยเลือก ตรึง code/data/evaluator/model/reference time ก่อนรอบจริง เก็บ raw answer, needs, source revision, selected fields, rejection reason และ model transport

แยกผลเป็นสองชุดเกณฑ์ที่มี provenance ชัด:

1. **Historical compatibility:** ใช้คำถาม/expected เดิมที่ยังใช้ได้และผล baseline ที่เก็บไว้; protocol ต่างจากเนื้อหาแยกกัน
2. **Current-owner correctness:** ข้อที่ owner เปลี่ยนหรือเติมใช้ expected ใหม่พร้อม source answer ID/date และแสดงว่าต่างจาก GT เดิมตรงไหน ห้ามเปลี่ยน expected เพียงเพื่อรับคำตอบที่ตัวใหม่พลาด

ไม่รัน Legacy/R95 ใหม่เพื่อทำคะแนนรอบนี้ เทียบ retained keys ที่ overlap และเปิดเผยว่า data versions ต่างกัน จึงไม่ใช่ causal algorithm experiment

หน่วยโทษ Pause Tekken ที่เจ้าของให้ข้ามต้อง map ไปยัง keys/grades ที่เกี่ยวข้องก่อนตรึง workload และเก็บ exclusion ledger. ตัวเลข executed + excluded + blocked ต้อง reconcile กับ inventory เดิม ห้ามบอกครบ 20,554 ที่รันจริงหากมีข้อถูกตัด และไม่ตัดกติกา Tekken ทุกหัวข้อ

## 3. จุดในโค้ดที่ควรแก้และของที่ควรคงไว้

| จุด | เปลี่ยนอะไร | คงอะไรไว้ |
|---|---|---|
| intent_contracts.py / request_plan.py | จับ predicate เฉพาะ และ needs/qualifiers ที่ไม่หาย | IDs จาก snapshot, protected names, slot provenance |
| complete_flow.py | precedence ต่อ capability และ correction เฉพาะสาเหตุ | context, budget, snapshot เดียว, audit stages |
| read_graph.py / task_contracts.py | required sets ตาม predicate และ partial per member | typed refs, authority, withdrawn checks, hard dependencies |
| claim_coverage.py / result_contract.py | ตรวจ claim ตรง need ไม่เพียงแปะ predicate บน pointer | หลักฐาน field/revision และการแยก unknown |
| catalog_reader.py / set_reader.py | explicit-empty scope, exhaustive filtering, dedup/paging | read offering joins และ enumeration receipts |
| financial_scope.py / financial/rental readers | table quote vs total, owner-confirmation applicability, tuple calculator | deterministic math, units/audiences แยก และ current common-only facts |
| open_day.py / calendar / live readers | day/time/bookable/maintenance/occupancy predicates แยก | zone-scoped closure, Bangkok time, provider freshness |
| rules_reader.py / competition_bridge.py | clause readiness, proposition selection, bounded dependency closure | event identity, source text และ qualifier completeness |
| source_rows.py / domain renderers | direct answer layouts + nested localization | source hits/obligations และ stable IDs |
| owner readiness / publish preview | แสดงตอบได้อะไรเป็นราย capability; import mapping | revision และวงจรเผยแพร่เดิม ไม่เขียน production อัตโนมัติ |

ต้องตรวจ path ของ price reader/calculator ที่ถูก dispatch จริงก่อนแก้ ไม่สร้าง calculator ใหม่ซ้ำกับตัวเก่าเพียงเพราะชื่อไฟล์ต่างกัน; Legacy code ที่จะ reuse ต้องแยก parser ออกจาก loader ของ legacy data และพิสูจน์ read path ว่าอ่าน common เท่านั้น

## 4. Acceptance ที่ต้องออกแบบไว้ก่อน ไม่ใช่ผลผ่านแล้ว

| กลุ่ม | คำถาม/การเปลี่ยน | ผลที่ต้องได้ |
|---|---|---|
| อุปกรณ์ | OLED อยู่โซนไหน รวมภาษาอังกฤษพิมพ์ผิด | ที่ตั้งอุปกรณ์ ไม่ใช่เกม |
| อุปกรณ์ | มีจอย PS5 กี่อันต่อเครื่อง | 2 จอย พร้อม source owner |
| ความจุ | PS5 เล่นพร้อมกันกี่คน vs ห้อง PS5 นั่งกี่คน | ใช้คนละหน่วย/แหล่ง ไม่เอา 37 ที่นั่งมาเป็น players |
| catalog | ขอทุกเกมเฉพาะ PC / ไม่เอา VR | enumerate ตาม filter ครบ ไม่ top-K |
| catalog | โซนที่รู้จักแต่ไม่มี offering links | ระบุไม่มีข้อมูล scope นี้ ไม่คืนเกมทุกโซน |
| เกมใหม่ | เพิ่มเกมชื่อใหม่ไม่เคยอยู่ใน code มี summary และ offering | list/overview/ที่ให้บริการตอบได้ โดยไม่แก้ Python |
| controls | ถาม action เดียวภาค/แพลตฟอร์มชัด | binding เดียวตรง preset; ไม่ใช้ภาคอื่น |
| ราคา | ขอดูราคาทุกกลุ่ม vs คำนวณของฉัน | ตารางไม่ถาม audience ซ้ำ; calculation ถามเฉพาะ slot จำเป็น |
| ราคา | สองคน PSU+ภายนอก | แยก rate ตามคน ไม่คูณกลุ่มเดียว |
| เหมา | ครึ่งวัน/เต็มวันของโซนเดียว | 3/7 ชั่วโมง; full รวมเที่ยง; ไม่ extrapolate hourly |
| เปลี่ยนราคา | owner เปลี่ยนค่าใน candidate | คำตอบใหม่ใช้ revision ใหม่; ค่าประวัติเดิมไม่ถูกทับ |
| ยกเลิก | จองแล้วไม่สามารถยกเลิกใช่ไหม | รักษาคำปฏิเสธ ตอบเงื่อนไขยกเลิกก่อน 1 ชั่วโมงตาม source |
| เครื่องเสีย | update vs เกมเปิดไม่ได้จากเหตุอื่น | ใช้ข้อยกเว้นคนละบริบทตามเจ้าของ |
| ตาราง | วันนี้เปิดไหม / ตอนนี้เปิดไหม / มี slot ไหม | ไม่สลับ day opening, current opening และ occupancy |
| provider | TCP/HTTP unavailable | บอกตรวจสดไม่ได้ ไม่ตอบว่าง/เต็ม |
| กติกา | CS2 ผู้จัดให้อุปกรณ์อะไร | ข้อที่ครบตอบได้ ไม่โดน whole-book unknown ปิดทั้งหมด |
| กติกา | Tekken Pause ได้ไหม / หน่วยโทษ | permission ตาม owner; unit unknown/deferred ไม่แต่ง |
| บุคลากร | ขอชื่อ/ตำแหน่งที่ยืนยันแล้ว | แสดง field ที่ยืนยัน; ข้อมูลส่วนตัวที่ไม่ยืนยันไม่ออก |
| หลายเรื่อง | จอย+เกมสองคน+ราคา | 3 needs ไม่ทิ้งส่วนใด หรือบอก missing slot เฉพาะส่วน |
| followup | แล้ว VR ล่ะ / เปลี่ยนเป็นคนนอก | เปลี่ยนเฉพาะ slot ที่กล่าว; คงบริบทที่ส่งจริง |
| ถอนข้อมูล | owner ถอนเกม/บริการ | ไม่หลงใช้ตัวเลือกหรือ cache เก่า |
| ภาษา | English specs/rules/ราคา | nested labels เป็นอังกฤษ ตัวเลข/เงื่อนไขเดิมครบ |

ใช้ทั้งเคสที่คาดว่าตอบได้และคู่ใกล้กันที่ควรตอบต่างกัน พร้อมข้อมูลใหม่/เปลี่ยน/ถอน ห้ามวัดเฉพาะ happy paths ของรายการที่มีอยู่ก่อน

## 5. เกณฑ์ความสำเร็จที่ใช้ตัดสินงาน

- **Parity:** หมวดที่ Legacy ทำได้ดีต้องลดช่องว่างบนคำถาม/ground truth ที่เทียบกันได้ โดยไม่ทำให้หมวดที่ R106 ดีขึ้นถอยลง เปอร์เซ็นต์ Legacy เป็น baseline ประวัติ ไม่เป็นตัวตรวจ truth ของข้อมูลที่ owner เปลี่ยนแล้ว
- **Answer precision:** ตรวจข้ออ้างและหลักฐานตรงจริง รวมตัวเลข หน่วย เงื่อนไข และคำปฏิเสธ ไม่ใช้แค่มี keyword
- **Answerability:** คำถามที่มี source พอต้องไม่ปฏิเสธเพราะ optional metadata; คำถามที่ไม่มี source ต้องไม่ตอบเดา
- **Completeness:** ทุก need และสมาชิกของชุด all มีผลที่อธิบายได้; ตอบบางส่วนระบุบางส่วน
- **Data-only usability:** เพิ่ม/แก้/ถอนข้อมูลในชนิดที่รองรับแล้วใช้ได้ในแชทโดยไม่แก้ code/aliases ตามชื่อรายการ
- **Infrastructure:** model transport/latency แยกจากความถูกต้อง และ controlled-live workload ไม่ใช่ผลสถานะจองจริง

เป้าหมายออกแบบคือเข้าใกล้ระดับ Legacy ในหมวดที่ Legacy ทำได้ดี และรักษาส่วนที่ common ทำได้ดีกว่า ตัวเลขเช่น 90–95% เป็นได้เพียงเป้าหมายรับงานหลังนิยามชุดตรวจและความหมายให้ชัด **ยังไม่ใช่ผลคาดการณ์หรือคำรับรองว่าจะได้เท่านั้น**

## 6. ความเสี่ยงของแผนและวิธีควบคุม

1. **เปลี่ยนแค่ router แต่ required gate เดิมยังขวาง:** ต้องทำ input/read/output contract ครบในขั้นเดียว ไม่ติดป้าย adapter แล้วจบ
2. **แก้ gate ด้วยการปิดตรวจทุกอย่าง:** ใช้ required claims ต่อ predicate ไม่ข้าม authority, conflict, withdrawal หรือ dependency ที่มีผลจริง
3. **ใช้ Legacy fallback แล้ว facts เก่าปน:** แยก pure language/calculator จาก data loaders และตรวจ source revision ทุก claim
4. **overfit ชุด 91:** หยุดใช้ชุดพัฒนาซ้ำเป็นเปอร์เซ็นต์รับรอง; ใช้ neighbor cases และ full frozen run หลังทำครบ
5. **owner add ข้อมูลแต่ runtime ไม่ refresh:** ตรวจ revision/epoch/provider และ preview/chat path เดียวกัน
6. **แก้ privacy แรงไปหรือปิดทั้งชุด:** field-level public scope ตามเจ้าของ ไม่ขยายคำยืนยันไป field อื่น
7. **ราคา confirmation กลายเป็นปลอม effective dates:** แยกหลักฐานยืนยันล่าสุดกับช่วงมีผลทางธุรกิจ และแสดงข้อจำกัดคำถามอดีต/อนาคต
8. **คำตอบยาวขึ้นจนดูเหมือนครบ:** renderer ตอบตรง predicate และตรวจ need coverage แทนการใส่ทุก field
9. **เพิ่ม LLM หลายจุดจนช้า:** budget เดียว, index ต่อ snapshot, one bounded planning attempt, deterministic math/reads

## 7. สิ่งที่พร้อมและสิ่งที่ยังไม่ทำในรอบนี้

พร้อม: ผลวิเคราะห์รายหมวด, ตัวอย่าง raw failures, code anchors, แผน ingestion/dispatch/adapters/renderer และแผนตรวจครบทุกหมวดหลัก

ยังไม่ทำ: สร้าง runtime candidate ใหม่, import คำตอบเข้า common database, แก้ engine, ติดตั้งทับ R78, เปลี่ยน frozen R106, รัน LLM หรือ Full Test. เอกสารนี้ไม่ใช้คำว่า implementation เสร็จจากการเขียนแผน
