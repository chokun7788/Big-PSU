# ทะเบียนสาเหตุข้อ 2 — อ่านฉบับนี้ก่อนตารางรายคำถาม

เอกสารนี้แยกต้นเหตุ อาการ ผลกระทบ และวิธีตรวจรับ ใช้ผล R130 เดิมครบ 20,554 คำถาม / 55,811 เกณฑ์ ไม่มีการแก้ Flow ระหว่างการทดสอบย่อยบนี้

ก่อนเริ่มทดสอบได้ตรวจ source/trace รายกรณี 72 คำถามและเขียนรายงานหลักแล้ว จากนั้นตรวจเพิ่มระหว่างรอผล รวมเป็น **167 unique request keys ที่ตรวจ source รายกรณีหรือทดลองเส้นทางโค้ดเฉพาะในหน่วยความจำ** ยืนยันตัวอย่างผิดขอบเขต/ตอบขาด/ตอบผิดเรื่อง 117 keys ตัวเลขนี้เป็นตัวอย่างที่ยืนยันได้ ไม่ใช่จำนวนผิดทั้งหมดหรือเปอร์เซ็นต์ความถูกต้องของชุด Full

อีก 20,387 keys ยังไม่ได้ตัดสินความหมายรายข้อ ตารางกลไกครอบคลุมทุก key แต่การพบกลไกผิดไม่เท่ากับคำตอบสุดท้ายผิดเสมอไป

| ID | จุดแรก/ต้นเหตุ | หลักฐานและจำนวนที่แยกตรวจได้ | ผลต่อผู้ใช้ | การแก้ที่ควรตรวจรับ |
|---|---|---|---|---|
| D01 | Entity binding ใช้ alias ไทยเป็น substring และเลือก span ยาวก่อนตรวจชนิด | GPU 13 keys และจอง→จอภาพ 10 keys; ทดลองแก้เฉพาะ pool ในหน่วยความจำแล้วอ่าน GPU ได้ทุกข้อ | บอกไม่มี GPU ทั้งที่มี หรือถามสิทธิ์จองแล้วตอบวิธีใช้จอ | รักษาขอบเขตคำ ชนิด entity และ predicate; pool ที่ไม่ว่างแต่ผิดชนิดต้องไม่กีดกันตัวเลือกถูก |
| D02 | ชื่ออุปกรณ์กลบการกระทำที่ถาม | Damage→inventory 10 keys; public→person อีกเคสที่ตรวจยืนยัน | ถามชดเชยกลับได้รายการอุปกรณ์ ถามบุคคลทั่วไปกลับได้รายชื่อคน | ตรวจ actor/action/target ก่อนเลือก reader และไม่ใช้ entity match ปิด need |
| D03 | Native policy fallback / การแตกประเด็นทำ event scope หาย | ตรวจครบ 36 keys: 29 มีเนื้อหา/ขอบเขต/ประเด็นตกจริง; 4 ข้อ No เรื่องติดตั้งตรงสาระแต่ evidence ผิด scope; 3 ข้อยังต้อง review เงื่อนไขสิทธิ์ | กฎศูนย์ทั่วไปไปตอบในบริบทแข่งขัน; ดูสตรีมถูกแปลเป็นถ่ายทอด; อาหารเฉพาะรายการหาย | ให้ event/edition กำกับทุก need ที่เกี่ยวข้อง; แยก watching/broadcasting และการติดตั้ง/การใช้ macro |
| D04 | Verifier ใช้ text ต่างจาก heading เป็นตัวแทน substantive rule | ตรวจครบ 13 keys ของ source CS2 sections033/045/046/058 | มีสาระเรื่องหยุดเทคนิค ตั้งค่า macro และประท้วง แต่ตัดคำตอบทิ้ง | ประโยคกติกาเต็มต้องผ่านแม้ใช้เป็นหัวข้อด้วย ตรวจ predicate+condition ไม่ใช้การเทียบข้อความหัวข้ออย่างเดียว |
| D05 | Reader เลือก document title และ ledger ยอมรับว่า complete | ตรวจคำถาม Tekken format ครบ 29 keys ที่ได้ title-only; source002 มี FT2/R3/60S | ตอบชื่อเอกสารแทนรูปแบบแข่งขัน แต่บางเกณฑ์พบเพียง route mismatch | ต้องส่งสาระรูปแบบที่ source ยืนยัน พร้อมตรวจ clause hierarchy/dependencies และ coverage |
| D06 | Resolve คำอ้างกลับแล้ว แต่ยังคง ambiguity เก่า | 2 keys ที่ it ผูก Tekken/control record แล้ว | ถามชื่อเกมซ้ำ ส่วน controls ไม่ถูกตอบ | หลัง binding สำเร็จ reconcile ambiguity แล้วส่ง target ถึง executor; คงเฉพาะ platform ambiguity ที่ยังจำเป็น |
| D07 | Need coverage ตรวจเฉพาะแผนที่สร้าง ไม่ตรวจกลับคำถาม | พบทั้ง settings+macro, macro+install, equipment+responsibility และ prep+food | ประเด็นแรกหรือหลังหายแม้ receipt ของส่วนที่อ่านผ่าน | สร้าง need ledger ก่อนอ่านและตรวจกลับทุก predicate/condition ของคำถามต้นฉบับ |
| D08 | ตัวเลขเป็นคำอ่านไม่ถูกเก็บเป็นข้อจำกัด | seven buttons ของ Gran Turismo: ตอบ14 entriesโดยไม่อธิบาย subset7; Flow เดิมก็มีปัญหานี้ | คำตอบดูครบเพราะลิสต์ยาว แต่ไม่ตรงจำนวน/ชุดที่ถาม | แยกเลขในชื่อเกมกับ requested count และแสดง unknown subset ตาม source |
| D09 | Service scope ถูกแทนด้วยบริการใกล้เคียง | offsite notebook ถูกตอบราคาเหมาโซน หรือถามว่าจะเหมาโซนใด | ชี้ไปบริการที่ผู้ใช้ไม่ได้ถาม | ต้องผูก item/service/location ก่อนใช้ package; ไม่มีข้อมูล offsite ให้บอกตรงเรื่อง |
| D10 | ราคา/authority/validity ยังมีส่วนที่ตัดสินไม่ได้ | Nintendo30นาที ขนาดกลุ่ม กลุ่มผู้ใช้ effective interval; source conflict/equivalence 320 task occurrencesในรายงานกลไก | ตัวเลขหลายชุดไม่มี label หรือเตือน conflict เกินจำเป็น | ตรวจ billing rule/actor/condition/version และ validity ราย source; ไม่เรียกราคาผิดก่อนมีหลักฐาน |
| D11 | Admission ปฏิเสธก่อนส่ง HTTP | 8,890 requests พบ denial; 3,971 มี metadata ว่า concurrency busy; 8,857 ไม่ยิง HTTP เลย บางข้อยังตอบด้วย typed reader ได้ | โมเดลยังทำงานอยู่ แต่คำถามถูกตอบ retry หรือ fallback | แยก busy/cooldown/budget/transport และกำหนด queue/deadline กับ reserved/attempted/spent ให้ชัด |
| D12 | รุ่น wire/schema ไม่เข้ากับ parser และ backend ไม่ constrain format | เมื่อรวม compatibility path พบ schema-rejection237 requests; unique parser events196 context +64 selector | เสียเวลาสร้างผลแล้วใช้ต่อไม่ได้ หรือ fallback | Prompt/version/parser ต้องตรงทุก stage; ตรวจ selector input echo; ผ่าน JSON ยังไม่ผ่าน semantic |
| D13 | เกณฑ์ประเมินปะปน protocol กับสาระ | route/intent/mode mismatch19,221requests; แต่ title-only เป็นตัวอย่างที่ strict พบแค่ route ทั้งที่สาระไม่ครบ | มองคะแนนต่ำเป็นข้อมูลผิดทั้งหมด หรือมอง literal ผ่านว่าเข้าใจครบ | เก็บ strict/literal เดิม แยก semantic/source review และ unknown โดยไม่แก้ baseline grades |
| D14 | ข้อมูลไม่ยืนยันจริงกับ reader หาไม่เจอถูกรวมเป็น label เดียว | GPU/กติกามีแล้ว; game_mode/เวอร์ชันติดตั้ง/ข่าวปัจจุบันยังมี source gaps | ขอข้อมูลซ้ำในสิ่งที่มี หรืออนุมานสิ่งที่ยังไม่ทราบ | ทำทะเบียน known/unknown/conflicted/not-current/reader-gap แยก source authority และ publication |
| D15 | Renderer และ unnecessary model calls | เริ่มด้วยชื่อเอกสารหรือบันทึกแก้ข้อมูล; building/floor41sใน API readiness แม้ source มี | อ่านยากและรอนาน | เปิดด้วยคำตอบตาม operation; labelเงื่อนไข; อ่าน local fields เมื่อ scope ชัด และตรวจ tail latency |

**จำนวนแต่ละแถวซ้อนทับกันได้ ห้ามบวกเป็นจำนวนคำถามผิดทั้งหมด** เช่น macro+settings อยู่ได้ทั้ง D04 และ D07 และ admission failure อาจถูกกู้ด้วย typed path จึงไม่ใช่ semantic failure ทุก key

## สิ่งที่แตกต่างจากการจัดกลุ่มอาการครั้งก่อน

1. มี case ledger ทุก key พร้อมคำถาม คำตอบ แผน source ที่ส่งออก grade identities และ observed issues
2. เคสที่ตรวจรายกรณีมี first failing stage, root-cause confidence, source revision/locator, ผลของ Flow เดิมที่บันทึกไว้ และประเด็นที่ยังไม่ตัดสิน
3. มีการทดลองเชิงสาเหตุเฉพาะ process วินิจฉัย เช่นเปลี่ยน binding pool อย่างเดียว โดยไม่แตะ runtime ที่กำลังวัด
4. แยก cohort ที่เพียง trace คล้ายกันจาก cohort ที่อ่าน source ทุก key แล้ว ตัวอย่างกลุ่มแข่งขัน36ข้อถูกแยกอีกครั้ง ไม่ติดป้ายว่าผิดเนื้อหาทั้งหมด
5. ใช้ saved legacy trace จริงเมื่อมี และบอก exception/ไม่มีคำตอบเมื่อไม่มี ไม่สมมติว่า Flow เดิมถูกทุกกรณี

## Coverage ของชุดทดสอบ 10%

เลือกจาก FULL_JOBS เดิม โดยปัดขึ้น10%ทุก original stratum และเติมหมวดตาม input ให้ครบ C01–C14 ได้2,111 unique keys/5,584 grades คำถามหลายหมวดมี membershipsซ้อนทับ จึงไม่บวกจำนวนหมวดเป็นจำนวน unique keys

C07 มีเพียง6คำถามใน Full เดิมและเลือก1 ส่วนใหญ่เป็นคำถาม offsite จึงไม่ใช้ผลนี้ยืนยันคุณภาพราคาเหมา onsite ทุกชนิด C14 ไม่มี real news records ให้ source gap แยกจาก runtime failure การมี sample ครบหมวดไม่เท่ากับ capability ทุก operation ถูกทดสอบครบ

รอบนี้ไม่มี runtime fixes และไม่ฝึกโมเดลใหม่ ผลต่างจาก saved R130 จึงใช้ตรวจการเกิดซ้ำ/คิว/เส้นทาง fallback ไม่ใช้ประกาศว่าปรับคุณภาพดีขึ้น ผลครบแล้ว2111keys/5584grades คำตอบเหมือนsavedR130ทุกข้อ; strictต่าง9grade identitiesเฉพาะlatency ดูSAMPLE10_FINAL_REPORT_TH.md และSTRICT_ONLY_CHANGES_REVIEW.json

## อ่านหลักฐาน

- รายงานก่อนเริ่มทดสอบ: ITEM02_DETAILED_DIAGNOSIS_TH.md / DIAGNOSIS_PRETEST_COMPLETE.json
- รายกรณี: INDIVIDUAL_SOURCE_REVIEW.json / POST_GATE_GPU_CAUSAL_REFINEMENT.json / POST_GATE_RELATED_SOURCE_REVIEW.json / POST_GATE_TOURNAMENT_SCOPE_REVIEW.json
- โค้ดและ source: DETERMINISTIC_CAUSAL_PROBES.json / SOURCE_CAUSAL_EVIDENCE.json
- ทุกคำถาม: CASE_DIAGNOSTICS_REVIEWED.jsonl.gz; การวินิจฉัยเพิ่มอยู่ใน sidecars ด้านบน
- กลไกทั้งหมด: ISSUE_COUNTS.json / ADMISSION_AND_PROTOCOL_FORENSICS.json
- ข้อมูลที่ยังไม่ทราบ: SOURCE_GAP_DIAGNOSIS_TABLE.json
- ชุดที่เลือกและเงื่อนไข: SAMPLE_ALLOCATION.json / SELECTION_FREEZE.json / RUN_FREEZE.json

ยังไม่ประกาศ semantic accuracy และยังไม่ปิดคุณภาพทั้ง76requirements Candidateยังไม่ติดตั้งทับR78
