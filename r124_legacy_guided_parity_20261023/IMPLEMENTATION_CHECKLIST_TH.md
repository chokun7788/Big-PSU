# รายการติดตาม A01–F05 จาก inventory ก่อนหน้า

ทุกแถวมีการจัดการหรือขอบเขตที่ชัดเจน ข้อจำกัดจาก source และข้อจำกัดของการพิสูจน์ semantic ไม่ได้ถูกแปลงเป็นข้อเท็จจริงเพื่อให้สถานะดูครบ และไม่ถือว่าต้องให้เจ้าของกรอกข้อมูลเดิมใหม่ทั้งหมด

คำว่าใช้ได้ในตารางหมายถึง implementation/หลักฐานตามขอบเขตที่ระบุ ไม่ใช่ 100% accuracy ของทุก operator หรือทุกบทสนทนา การเปลี่ยนเป็น graph wire ใหม่/ฝึก weights ใหม่ไม่ได้เป็นเงื่อนไขจำเป็นของการซ่อม binding/projection/reader ในรอบนี้ และไม่มีการอ้างว่าได้ฝึกใหม่

| ID | รายการเดิม | การจัดการใน R124 / ขอบเขตหลักฐาน |
|---|---|---|
| A01 | live_binding records | เชื่อมแล้ว: 18 draft bindings จาก catalogue จริง |
| A02 | internal service → external resource key | เชื่อมแล้ว: internal service/resource → external ID พร้อม source snapshot |
| A03 | physical pool ของบริการที่ใช้เครื่องร่วมกัน | ใช้การเลือกผลิตภัณฑ์ตามรอบ/เวลาแบบเดิม; ไม่บวก binding เป็นจำนวนเครื่อง และไม่สร้าง physical equivalence ที่ source ไม่ยืนยัน |
| A04 | status mapping ที่ตรง payload จริง | ใช้ status mapping พร้อม available count; unknown ไม่เป็น free |
| A05 | TTL/timezone/วันที่มีผลของ binding | ตรวจ timezone, TTL และ effective mapping ด้วย observation wall clock แยก semantic booking date |
| A06 | profile เชื่อม live จริง | เปิด profile WordPress จริงบน candidate API ไม่ใช่ unavailable fixture |
| A07 | provider health/schema/identity ปัจจุบัน | ตรวจ catalogue/status จริงและ health แล้ว; เป็นหลักฐาน ณ เวลา probe ไม่ใช่ uptime guarantee |
| A08 | calendar ของ Dashboard กับ common snapshot | แยก recorded play slots จาก conflicted physical opening; ไม่แก้ raw conflicted fields |
| A09 | จำนวนเครื่องว่าง/ความจุ/ช่วงเวลาต่อเนื่อง | ใช้ renderer/contiguous-slot/count/list selectors เดิม และมี fault gates |
| A10 | การแยก failure ของ API กับไม่มี binding | แยก missing binding/configuration, payload/freshness และ transport; ไม่รวมเป็น model/content failure |
| B01 | ความขัดแย้ง physical opening hours | อธิบายตัวเลขขัดแย้งครบ 5 วันและแยก predicate แล้ว |
| B02 | โซนที่ตารางเวลาใช้บังคับ | คง unknown scope; ใช้ตารางบริการเล่นที่บันทึกไว้ ไม่ขยายเป็นเวลาเข้าทุกพื้นที่ |
| B03 | ช่วงมีผลของตาราง | คงข้อจำกัด effective period ไม่ประกาศว่าเป็นตารางใหม่ทุกปี |
| B04 | ขอบเขตวันปิดพิเศษ | ใช้ recorded closure/calendar semantics เดิม; ไม่อ้าง physical scope ที่ไม่มีหลักฐานเพิ่ม |
| B05 | ปิดพิเศษแล้วจัดการ booking อย่างไร | ใช้ source-backed FAQ/policy ที่มี; ไม่สร้างนโยบายจัดการ booking จากการมี closure record |
| B06 | หน่วยราคาที่ตรงกับ rate | คง owner per-person confirmation ที่ผูก value hash; unit unknown ไม่ทำให้อัตราทั้งแถวหาย |
| B07 | วันมีผล/คำยืนยันราคา | แยก as-of confirmation กับ effective interval และตรวจปี/วันที่ใน calculator |
| B08 | เงื่อนไขราคาเหมา | คงราคาเหมา 24 แถว; terms ที่ไม่ยืนยันไม่ถูกเดาจากราคา |
| B09 | Service → physical resource | live ใช้ catalogue mapping จริง; physical members ที่ไม่ระบุไม่ถูกแต่งเพิ่ม |
| B10 | Game → เครื่องที่ติดตั้ง | อ่าน offering/zone graph ได้; exact installed station ต้องมี edge ของมันเอง |
| B11 | โหมดและจำนวนผู้เล่นพร้อมกัน | ใช้ FAQ เจ้าของสำหรับคำถามที่ตรงครบข้อ; ไม่อนุมาน max players ของทุก mode จากจำนวนจอย |
| B12 | แพลตฟอร์มที่เกมรองรับ | แยก studio offering platform จากทุก platform ที่ตัวเกมรองรับ |
| B13 | รายละเอียดเกมที่เหลือ | ตรวจทุก record ว่ามี projection หรือเป็น relation/stub/metadata; FAQ known-answer projection gap เป็น 0 |
| B14 | เกมเวอร์ชัน/edition/อายุผู้เล่น | คง edition/version/age uncertainty; ไม่ย้ายชื่อใกล้กันมาเป็นเกมเดียวโดยไม่มีหลักฐาน |
| B15 | เอกสาร check-in/กำหนดเวลาใน procedure | เอกสาร check-in และ deadline อ่านจาก FAQ เดิม/เจ้าของได้ ไม่ต้องกรอกซ้ำเพราะ typed field บางช่อง unknown |
| B16 | ข่าว/กิจกรรมเป็น typed records | ข่าวต้องมี source/date ที่ใช้ได้; exact FAQ ไม่รับคำถาม latest/upcoming เป็นข้อมูลคงที่ |
| B17 | นโยบายหลายฉบับและข้อมูลบุคลากร | เก็บ variants/conflict และ source profile period; ไม่สร้าง approvals แทนเจ้าของ |
| B18 | Completeness และ English ของ clauses | รวม clause เฉพาะ full body/event ตรงกัน รักษา English และ dependencies |
| C01 | ระบุ factual needs ครบทั้งคำถาม | ใช้ whole-question context/validated task plan + exact FAQ ทั้งข้อ; ไม่อ้างว่ามี perfect semantic need detector |
| C02 | Shared-prefix audience/date/condition | คง shared/local slot compiler และ source-span gates; ไม่คัดลอกปริมาณข้าม task เอง |
| C03 | Pronoun/anaphora/“อันเดิม/เครื่องนั้น” | ใช้ unique referent ที่ตรวจได้; หลาย antecedents ต้องถามกลับ |
| C04 | History binding ทุกหมวด | คง trusted delivered-state adapters; ตรวจ source edit/withdraw และ cache epoch ไม่ใช่รับประกันทุก dialogue scenario |
| C05 | Negation/conditions/exceptions | ใช้ protected intents เดิมแยก bring/consume และ studio/tournament context |
| C06 | ตัวเลขในชื่อกับจำนวนจริง | แก้ PS5 #01 normalization; ป้องกัน edition/จำนวนและ button substring; compound chord มาก่อน single key |
| C07 | Duration roles | คง duration/session/compare operator และ rounding ตาม current rate source |
| C08 | Alias/typo และหลาย entity | ใช้ source aliases/query profiles และ explicit event rules ก่อน equipment definition; ไม่สอน teacher error |
| C09 | Planner wire ใหม่ตาม R123 | คง R121 validated wire แล้ว compile เป็น IR; เปลี่ยน runtime/source wiring โดยไม่อ้างว่าฝึก graph-wire model ใหม่ |
| C10 | Raw/normalized Unicode alignment | คง provenance/quote/span gates และตรวจ 289 annotations compile; ไม่อ้าง Unicode equivalence ครบทุกการแปลง |
| C11 | ถามกลับเฉพาะช่องที่ขาด | แยก missing input/source, conflict, unsupported operation และ provider failure ใน ledger |
| D01 | Operation coverage ทุกหมวด | registry ระบุ operation/facet ที่ทำได้จริง รวม recorded calendar-state; ไม่เปิดทุก operator ให้ผ่านโดยปริยาย |
| D02 | Set/list/count/group completeness | ตรวจ complete recorded control set และ partial_official แยกกัน; partial list ไม่เท่ากับ factual error |
| D03 | Global typed-first ของ native compounds | แก้ native calendar/live compounds ให้ typed reads ของทุก child มาก่อน deferred evidence selection |
| D04 | Dependency graph และ partial success | ทดสอบ budget 0 แล้วยังเก็บ calendar/booking ที่ตอบได้ ไม่ให้ task แรกทำผลอื่นหาย |
| D05 | Arithmetic ครบตาม billing semantics | ใช้ Decimal/current unit/duration/audience rules; ไม่ฝังราคาใน model/router |
| D06 | Rule dependency/complete clause | ใช้ event-specific clauses, section families, declared dependencies; ไม่หยิบ keyword hit เดียวตอบหมวดเต็ม |
| D07 | Authority/supersession/dedup | source refs/current snapshot/variants/conflict guards; ไม่ประกาศว่ามี global authority theorem solver |
| D08 | Semantic answer completeness verifier | ตรวจค่า ตัวเลข identity และ planned obligations; ยังไม่ใช่ semantic entailment oracle ทุกประโยค |
| D09 | ภาษา/ความกระชับ/first answer | ตอบ fact ก่อน เก็บเงื่อนไขและ verification notes; ยังมี wording/variant repetition ที่ไม่ใช่ content failure |
| D10 | Calendar capabilities เต็มชุดเดิม | ต่อ shared native calendar adapter และ recorded play slots; การมี helper ไม่ใช่คะแนน parity เดือน/ปีทุกคำถาม |
| D11 | Reason codes ไปถึง API/UI/log/metric | เก็บ reason codes/source/transport แยกถึง API logs และรายงานรายข้อ |
| E01 | Semantic review labels ทุกแถว | review teacher contrasts ที่พบจริง; 289 compile gates ไม่ถูกเรียกว่า reviewed gold ทั้งหมด |
| E02 | Teacher plans ที่แก้ scope แล้ว | เก็บ wrong-topic/task-omission/source-version teacher cases แยก ไม่คัดลอกเป็นคำตอบฝึก |
| E03 | ฝึก adapter สำหรับ wire/graph ใหม่ | ใช้ R121 adapter ที่มีอยู่กับ native compiler/legacy frames; ไม่มี training ใหม่ใน R124 และไม่อ้างว่าฝึกแล้ว |
| E04 | Family split ที่ยังไม่ปนการพัฒนา | 61 retained keys เป็น development set ใช้แก้ระบบแล้ว ไม่ถือเป็น fresh holdout |
| E05 | เปรียบเทียบ base/current/new แบบคุมตัวแปร | รัน legacy/common จริงและเปิดเผย model/data/clock/provider differences ไม่อ้าง causal Flow-only effect |
| E06 | วัด semantics แยก strict/literal | แยก protocol/literal/source/content/transport; ไม่มีการเปลี่ยน gate count เป็น % accuracy ทั้งระบบ |
| E07 | Latency/budget/actual model calls | เก็บ actual generation calls, profile/provenance, traced latency และ real API probe latencyแยกกัน |
| F01 | Schema/editor/source refs | คง schema/editor/source references และ draft/approval boundaries เดิม |
| F02 | Data compiler/capability readiness ตรง runtime ใหม่ | compile readiness และ capability registry ตรงตัว executor ที่เปิด; ขอบเขต semantic verification ระบุชัด |
| F03 | Add/update → index refresh → reader ใช้ข้อมูลใหม่ | มี exact whole-question stable FAQ path และทดสอบ source change/epoch ให้ข้อมูลใหม่เปลี่ยนคำตอบได้ |
| F04 | การแก้/ถอนข้อมูลและ conversation scope เก่า | withdrawn known intent ไม่ย้อนตอบ legacy constant; test cache/source withdrawal เป็น memory fixture |
| F05 | Deployment จริงและ end-to-end readiness | เปิด candidate live API จริง แยกจาก R78; ไม่ติดตั้งทับ production หรือสร้าง approvals |
