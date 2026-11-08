# ตรวจทาน Flow รวม R94 สามรอบ

การตรวจนี้เป็นการทบทวนสถาปัตยกรรมและ cross-check กับเอกสาร/โค้ด/ผลเดิม ไม่ใช่การส่งคำถามเข้า chatbot ไม่ใช่ independent human review และไม่ใช่ผลพิสูจน์ว่า runtime ใหม่ผ่านแล้ว

## รอบ 1 — การผสมสอง Flow จะเกิดการตีความซ้ำหรือไม่

| จุดบกพร่องของแบบรวมอย่างง่าย | ผลเสีย | สิ่งที่ปรับใน R94 |
|---|---|---|
| เรียก common เดิมก่อน ถ้าตอบไม่ได้ค่อยเรียกแผนใหม่ | คำตอบเดิมที่ผิดแต่ไม่ว่างอาจหยุดก่อนถึง interpreter ใหม่ | TaskPlan ใหม่เป็นผู้ตัดสิน capability ที่ย้ายแล้ว ส่วนเดิมเป็น typed executor |
| วาง TaskPlan ใหม่แล้วกลับเข้า lexical guard เดิมทุกครั้ง | paraphrase ยังถูกปฏิเสธเหมือนเดิม | semantic acceptance contract และกำหนดปลด gate เดิมเป็นราย capability |
| ใส่ wrapper recovery เฉพาะ entity_search | named path ยังตก Animal Crossing/Sofa เช่นเดิม | normalized input/spans ร่วมก่อน routing ทุกทาง |
| ใช้ตัวอ่านเดิมโดยไม่ตรวจ dependencies | อาจอ่าน facts เก่าทับ common ที่เจ้าของแก้ | audit adapter; facts อ่าน provider กลางเท่านั้น |
| ให้ fast paths return คำตอบออกเอง | ข้าม need/authority/completeness checks | ผล fast path ต้องเข้า shared finalizer |

ผลทบทวน: เอกสาร 01 M02/M04/M05/M07 และเอกสาร 02 ขั้น rollout ระบุ seam/ownership/retirement ของ branch ชัดขึ้น การใช้จุดเด่นเดิมคือรักษาความสามารถอ่าน/คำนวณ/เลือกข้อ ไม่รักษาทุก early return

## รอบ 2 — แผนใหม่อาจตอบผิดอย่างมั่นใจหรือไม่

| ความเสี่ยง | ตัวอย่าง | สิ่งที่ปรับ |
|---|---|---|
| จัดคำที่มีสาระเป็นคำเกริ่น | เฉพาะบุคคลภายนอก / หลัง First Blood | raw span map + discourse vs qualifiers + protected values |
| ผ่อน guard เพื่อรับ JSON ให้มากขึ้น | known game แต่ LLM ขอทุก field | task-specific semantic acceptance; evidence/field ownership ไม่ใช่แค่ schema |
| คิดว่า bindings ตรวจความหมายครบ | quote ถูกแต่ task เป็นคนละเรื่อง | ระบุข้อจำกัดของ span checks; negatives/held-out; uncertainty ถามตรงประเด็น |
| พบ source ใกล้เคียงแล้วถือว่าอนุญาต | กินในพื้นที่กำหนด → เอาอาหารส่วนตัวเข้าได้ทุกกรณี | action/ownership/conditions เป็นส่วนของ task contract |
| เลือกราคาให้ผ่านแต่ไม่รู้กลุ่ม/สูตร | VR90 ต่างมหาวิทยาลัย | slot correctness + calculation provenance + validity แยกกัน |
| แยก needs จนเงื่อนไขข้ามส่วนหาย | งบจำกัดกับเวลาที่เล่นได้ | NeedGraph: dependent computation ต้องครบก่อนตอบยอด/ระยะเวลา |
| ตี wording mismatch ว่าต้นฉบับผิด | RoV new game vs restart | proposition/translation review แยก raw exact-clause score |

ผลทบทวน: เปลี่ยนจาก “LLM เลือกแล้วตรวจ fields” เป็น “เลือกงานพร้อมเงื่อนไข แล้วหา evidence ที่พอ” การยืนยัน facts ยังจำกัดด้วย source authority/currentness ไม่ให้การแปล/โมเดลสร้างนโยบายเอง

## รอบ 3 — ใช้กับเจ้าของ/production และวัดผลได้จริงหรือไม่

| ช่องว่าง | ผลเสีย | สิ่งที่ปรับ |
|---|---|---|
| readiness มี 24 kinds แล้วนับว่า NLU เสร็จ | รายงานความพร้อมเกิน implementation | task coverage, compatibility path และ evidence artifact แยกจาก data readiness |
| owner preview อ่าน draft แต่ public อ่านคนละสิทธิ์ | เห็นตอบได้ใน preview แล้วคิดว่าเผยแพร่แล้ว | provider identity/authority ชัด, same core semantics, deployment gate |
| เปลี่ยนข้อมูลแต่ state/cache/translation เก่า | ตอบราคา/กฎฉบับเดิม | revision dependencies, cache keys, pending revalidation, translation lineage |
| “ทั้งหมด” แสดงเพียง top-k | ผู้ใช้คิดว่าครบทั้งที่ขาด | cardinality/coverage และ continuation ที่ผูก release |
| products VR30/VR60 ถูกนับเป็นสองเครื่อง | x/y availability ผิด | physical pool mapping และแยก session/occupancy |
| หนึ่ง static snapshot ถูกเข้าใจว่ารวม live พร้อมกันทั้งหมด | สถานะคนละเวลาถูกอ้างเป็น atomic live truth | live observed time/freshness แยก static epoch; partial visibility แจ้งตามจริง |
| ทุก need เรียก LLM/HTTP เอง | latency และ queue โต | request budget/admission, batched plans, shared typed execution; performance metrics แยก |
| สรุปจาก targeted checks ว่าเสร็จทั้ง Flow | เกิดคำอธิบายคลาดเคลื่อนแบบ R92 | S0–S7 completion evidence, held-out/new records/multi-turn และ runtime/package identity |
| rollback app โดยทับ DB ไปด้วย | สูญเสียข้อมูลที่เจ้าของเพิ่ม | app/config rollback แยก data compatibility; preserve revisions/logs |

ผลทบทวน: เพิ่ม implementation/coverage matrix และ rollout exit criteria แผนรวมจึงตรวจได้ว่า “ทำถึงช่วงไหน” แต่ยังต้องลงมือและพิสูจน์ตามช่วง ไม่เรียกแผนนี้ว่า production-ready runtime

## Counterexamples ที่ตรวจแบบด้วยการไล่เหตุผล

ตารางนี้เป็น expected behavior ที่ต้องนำไปใช้ตรวจเมื่อพัฒนา ไม่ใช่รายการทดสอบที่รันแล้ว

| กรณี | พฤติกรรมที่แบบต้องรองรับ |
|---|---|
| exact game + คำกริยาพิมพ์ผิด | entity คงเดิม ฟื้น task โดยไม่ถามชื่อเกมใหม่ |
| wrapper อังกฤษมี and + ถามงานเดียว | discourse ไม่เพิ่ม need ปลอม |
| มี PC และ VR ว่างไหม | สองเป้าหมาย ไม่ลบ and แล้วเหลือเครื่องเดียว |
| ไม่เอา VR มีอะไรเล่นได้ | exclusion คงอยู่; catalog/live แยกตามเวลาในคำถาม |
| PC11 ว่างไหม | ไม่แก้เป็น PC1 เพราะ similarity |
| pay for PC | ไม่แก้ pay เป็น play |
| ตอบ PC หลังถูกถามเลือกบริการราคา | pending fee task คง audience; เติม service |
| ทั้งหมดหลังถูกถามเลือกบริการ | ทุกบริการใน fee scope ไม่ใช่ทุก record/field |
| อุปกรณ์หลังถาม PC รายละเอียด | list ภายใต้ PC ไม่เป็นทั่วไปทั้งศูนย์ |
| ไม่ใช่ เปลี่ยนเป็น PS5 | ยกเลิกตัวเลือกเดิมก่อนใช้ PS5 |
| เปลี่ยนเรื่องจากราคาไปที่อยู่ | ไม่พา audience/duration เก่ามาตัดที่อยู่ |
| ราคา PC กับอยู่ชั้นไหน | location ตอบได้แม้ price not_current |
| งบจำกัด เล่นได้นานสุดเท่าไร | ต้องมี rate/billing/constraints ก่อนคำนวณ |
| ราคาเหมาวันโดยไม่มี duration | แจ้ง period ที่ทราบ ไม่แต่งชั่วโมง |
| ดูเพื่อนเล่นเฉย ๆ ฟรีไหม | permission to watch กับ fee เป็นคนละ need |
| แก้วันหลังจ่ายแล้ว | policy ตรงเงื่อนไขการชำระ ไม่แทนด้วย FAQ ยกเลิกทั่วไป |
| เกมมีให้เล่นไหม | game_service/offered ไม่ใช่ live free |
| เครื่องนี้ว่างตอน 15:00 ไหม | date/time + physical mapping + fresh status |
| VR30/VR60 ใช้ pool เดียว | จำนวนเครื่องไม่ซ้ำ ช่อง occupancy ตามนโยบายที่ยืนยัน |
| วันปิดพิเศษทับตารางปกติ | scope/precedence จากหลักฐาน ไม่เลือกจากไฟล์แก้ล่าสุด |
| กฎ RoV ก่อนและหลัง First Blood | สองฝั่งพร้อมเวลา/ข้อยกเว้น/สิ่งที่ต้องคงเดิม |
| กฎ CS2 แต่มี source VALORANT เท่านั้น | ไม่ยืมกฎอีกเกมมาตอบ |
| ขอทุกข้อของกฎที่ยาวเกิน UI | แบ่งส่วนและแจ้ง coverage ไม่ตัดเงียบ ๆ |
| owner แก้เกมแล้วแปลอังกฤษยังรุ่นเก่า | translation stale เฉพาะส่วนที่กระทบ พร้อม source revision |
| owner withdraw หลัง pending choice | คำตอบต่อไม่ฟื้นสิทธิ์จาก state เก่า |
| API สำเร็จแต่ status mapping ไม่ครบ | unknown/partial ไม่รายงานยืนยันว่างทั้งหมด |

## สิ่งที่แบบนี้ยังรับรองไม่ได้

1. ความถูกต้องทุก paraphrase ของโมเดล 4B: ต้อง calibrate/evaluate กับ local model และ held-out tasks ภายหลัง
2. ราคาปัจจุบันหรือ business terms ที่ source ไม่มี: refactor ไม่สร้างหลักฐานใหม่
3. เวลา/จำนวนผู้ใช้พร้อมกันที่รองรับ: ต้องวัด queue/model capacity บนเครื่องจริง ไม่สัญญาจากแผน
4. ผลจริงของ WordPress จาก mock-unavailable: ต้องแยก fixture กับ live verification ตามขอบเขตเดิม
5. คะแนนจะสูงขึ้นเท่าไร: R94 ยังไม่มี candidate runtime หรือการรันทดสอบใหม่

## หลักฐานที่ใช้กำหนดแบบ

- [Flow กลางเดิมที่ตรวจจากระบบ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/02_FULL_FLOW_COMMON_TH.md)
- [Flow ใหม่ R91](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/01_PROPOSED_COMMON_FLOW_TH.md)
- [ปัญหา P01–P37 และแผนเดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/02_PROBLEM_TO_REPAIR_PLAN_TH.md)
- [schema/task map เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/03_OWNER_SCHEMA_TASK_MAP_TH.md)
- [สิ่งที่ติดตั้งจริง R92](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r92_common_flow_implementation_20261018/IMPLEMENTATION_REPORT_TH.md)
- [สาเหตุคะแนนขยับน้อย R93](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r93_random_1000_common_on_20261018/WHY_SMALL_GAIN_REVIEW_TH.md)

ผลประเมินเอกสาร: แบบรวมรักษาจุดเด่นข้อมูล/reader ของกลางเดิมและเพิ่มการตีความ/coverage ตาม R91 โดยมีแนวทางปลดเส้นทางซ้ำชัดขึ้น ยังคงระบุว่าเป็น design-reviewed เท่านั้น ไม่ใช่ implementation-complete
