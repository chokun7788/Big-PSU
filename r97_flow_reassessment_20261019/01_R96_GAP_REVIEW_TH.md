# R97 — ทบทวนจุดบกพร่องของ Flow R96

วันที่: 19 ตุลาคม 2026 เวลาไทย

สถานะ: วิเคราะห์เอกสารและโค้ดที่มีอยู่ พัฒนา design ต่อจาก R96 ยังไม่เปลี่ยน runtime หรือรันทดสอบ chatbot

## 1. ข้อสรุปจากการทบทวน

R96 มีทิศทางที่เหมาะสม แต่ยังเป็นรายการหลักการมากกว่าสัญญาการทำงานที่ตัดสินได้ทุกทางแยก หากเริ่มลงโค้ดตามนั้นทันที มีโอกาสเพิ่ม planner อีกตัวแล้วคำถามส่วนใหญ่ยังถูกเส้นทางเดิมปิดกั้นเหมือน R95

R97 จึงเพิ่มลำดับ candidate discovery ก่อน semantic planning, แผนงานร่วมที่มี version, ผลการอ่านเป็นราย need, หลักฐานความครบของรายการ, และแผนเปลี่ยน ownership ของ early returns ที่ตรวจได้

คะแนนฐานยังใช้ R95 เดิม 18,579/24,909 = 74.59% และ Legacy R64 23,517/24,909 = 94.41% ไม่มีคะแนนรุ่นใหม่เกิดขึ้นในงานนี้

## 2. จุดที่ดีอยู่แล้วและควรใช้ต่อ

- การรักษา facts กลางเป็นแหล่งคำตอบ และนำเฉพาะ logic ตีความของ Legacy มาใช้
- การตรวจ schema, source pointers, source authority และ validity ที่ registry ทำอยู่แล้ว
- PinnedSnapshotView ที่ทำให้ส่วนประกอบคำถามอ่าน snapshot เดียว
- budget/deadline ร่วมและ finalizer reserve ที่มีใน request_deadline
- การตรวจการอ้างถึง record ที่ถอน/เปลี่ยน routing fingerprint ใน follow-up
- การแยก validity, protocol, transport และ content ในผลประเมิน

R97 ไม่ถือว่าส่วนเหล่านี้ไม่มีอยู่ แต่กำหนดให้ใช้ร่วมกันอย่างครบเส้นทางและเพิ่มข้อกำหนดเฉพาะที่ยังคลุมเครือ

## 3. ตารางข้อบกพร่องและการแก้ใน R97

ชนิดหลักฐาน: **DOC** = ช่องว่างของแผน, **CODE** = พฤติกรรมที่อ่านพบในโค้ด, **LOG** = มีตัวอย่างใน log, **RISK** = ความเสี่ยงที่ยังไม่พิสูจน์ว่าผิดจริงใน runtime

| ID | หลักฐาน | ช่องว่าง | ผลที่อาจเกิด | ข้อกำหนดเพิ่ม |
|---|---|---|---|---|
| G01 | DOC | planner ต้องเลือก ID แต่ขั้นค้น candidate อยู่หลัง planner | ไม่มี ID ให้เลือก หรือยึด entity ผิดตั้งแต่ต้น | discovery รอบแรกตาม task families ก่อน planner; grounding รอบถัดไปตาม typed plan |
| G02 | CODE/LOG | plan ใหม่และ common plan ยังตัดสินงานแยกกัน | qualifier หายหรือถูกตรวจซ้ำแบบคนละความหมาย | RequestPlan version เดียวก่อนเรียก domain executor |
| G03 | CODE | composition.parts ปฏิเสธ live และชุดที่มี rules; ต้องมีหลาย operation | คำถามกติกาหลายส่วน/ราคา PC กับ VR อาจไม่เข้า multi-need | ย้าย decomposition ไปก่อน gate เหล่านี้; แยก need แม้ task เดียวแต่คนละ subject |
| G04 | DOC | required/optional/any-of ยังไม่มีนิยามตัดสินที่ชัด | รวมทุก field เป็น required หรือเลือก branch ที่ดูง่ายแต่ตอบไม่ตรง | เลือก read branch ที่ครอบคลุม claims และ qualifiers; optional ไม่เพิ่มสิ่งที่ผู้ใช้ไม่ได้ถาม |
| G05 | CODE/DOC | ledger ปัจจุบันเริ่มจาก requested_fields | บันทึกครบ fields ทั้งที่ตก need ของผู้ใช้ | need IDs มาจากคำถาม ก่อนเลือก fields; source projection ผูกกลับ need ID |
| G06 | DOC | “ทั้งหมด” ยังไม่มีหลักฐานสมาชิกครบ | อ่านแค่ top-K แล้วอ้างว่า list ครบ | ใช้ exhaustive set query บน scope snapshot; นับ returned/unknown/filtered และ continuation |
| G07 | DOC/RISK | common มี FAQ กับ structured facts ที่อาจซ้ำกัน | แก้ rate แล้ว FAQ เก่ายังบอกราคาเดิม | topic/claim ownership และ supersession ที่มี source รองรับ; ไม่มีเจ้าของชัดให้ conflict |
| G08 | DOC | “อ่านข้อมูลกลาง” ถูกใช้แทนข้อพิสูจน์ความหมาย | source pointer ถูกแต่ตอบคนละคำถาม | evidence receipt ระบุ subject, predicate, qualifiers, time, source value |
| G09 | DOC | confidence/ranking ไม่มีความหมาย operational | ใช้ .9 เป็นความน่าจะถูกโดยไม่มี calibration | จัดการด้วยเหตุผลและ hard constraints; probabilistic threshold ใช้ได้หลัง calibration เท่านั้น |
| G10 | DOC | ทุกการเปลี่ยน epoch อาจทำให้ทิ้ง state | เปลี่ยนข้อมูลที่ไม่เกี่ยวข้องแล้วต้องถามใหม่ | re-read facts เสมอ; preserve intent/slots เมื่อ dependency และ scope ยังเทียบกันได้ |
| G11 | DOC | “ข้อมูลไม่มี” กับ known empty กับไม่เกี่ยวข้องไม่แยก | ไม่มีรายการถูกตีความว่าห้าม/ปิด/ไม่มีเครื่อง | closed-world inference ต้องมี completeness/negative evidence |
| G12 | DOC | regular schedule กับ physical access/bookability/live อยู่ใกล้กัน | ไม่มี slot กลายเป็นศูนย์ปิด | predicate คนละชนิดและห้าม derive ข้ามโดยไม่มี policy |
| G13 | DOC | เพิ่มหลาย sources เข้า common ยังไม่อธิบาย conflict ต่อ field | แหล่ง owner ยืนยันบาง field ถูกขยายไปทุก field | authority ระดับ claim/field, ขอบเขตและช่วงมีผลต้องตรง |
| G14 | DOC | partial answers ยังไม่มี dependency rule ที่ใช้ตัดสิน | สรุปงบจากราคาที่ไม่พร้อม หรือปฏิเสธวิธีจองไปด้วย | supported need ต้องไม่มี unmet hard dependency; answer independent parts ได้ |
| G15 | CODE/DOC | fixed one-call policy อาจชน slot/state/planner retry หลายชั้น | queue รอซ้ำและหมดเวลาตอนจัดคำตอบ | ใช้งบเดิมและ attempt ledger เดียวทุก branch; corrective read ไม่เพิ่มงบโมเดล |
| G16 | DOC | readiness ของ 24 kinds ถูกอ่านเป็นตอบได้ทุกคำถาม | owner คิดว่าใส่ครบแล้วทุก capability พร้อม | แสดง readiness ตาม task/field/relation/language ไม่ใช่ kind ผ่านอย่างเดียว |
| G17 | DOC | ไม่มีตัวชี้ว่าอะไรถูกแทนจริงหลังลงโค้ด | เพิ่มด้านหน้า 4 tasks แล้วอ้าง flow เปลี่ยนครบ | migration matrix ของ ingress/plan/read/render พร้อม branch retirement receipts |
| G18 | DOC | ภาษา/หน่วย/เงื่อนไขอาจเปลี่ยนระหว่าง render | คำแปลสวยแต่ permission/exception เปลี่ยน | สร้างคำตอบจาก claim packet เดียว ตรวจ critical slots หลัง localization |

G07/G10/G13 เป็นการปิดช่องว่างแผนและตรวจความเสี่ยง ไม่ได้ยืนยันว่า runtime เกิดความผิดทุกกรณีดังกล่าวแล้ว

## 4. ตัวอย่างที่แผนใหม่ต้องอธิบายได้

### 4.1 “ขอราคาบุคคลภายนอกทั้งหมด”

คำว่า “ทั้งหมด” กำหนด service set; audience ถูกระบุแล้ว ถ้าขอราคาตามตาราง ให้ list packages/durations ที่มีหลักฐาน ไม่บังคับถามเครื่องหรือระยะเวลาซ้ำ หากถามยอดรวมสำหรับช่วงเล่นหนึ่งช่วง จึงต้อง resolve duration/quantity ที่เปลี่ยนยอด

ถ้าราคาหมดอายุ ระบุรายแถว/กลุ่มว่า current rate ไม่พร้อม ยังอาจตอบชื่อบริการและขั้นตอนจองที่มีหลักฐานได้ ไม่แก้ effective_until เพื่อให้ผ่านคะแนน

### 4.2 “PC” หลังระบบถามว่าจะดูเครื่องอะไร

ใช้ pending_task=price และ audience จากคำผู้ใช้เดิม เปลี่ยน subject เป็น service PC อ่านราคาใหม่ตาม snapshot/time ปัจจุบัน ห้ามเริ่ม entity-only question แล้วถามว่าต้องการปุ่ม ราคา หรือจองอีกครั้ง

### 4.3 “ROV ถ้าเกมหลุดทำยังไง”

operation อาจเป็นปัญหาระหว่างเล่นทั่วไปหรือกติกาแข่ง ต้องใช้บริบทที่มีอยู่ก่อน ถ้าบริบทระบุการแข่งขัน ให้ค้น competition/rule clauses; ถ้าไม่ระบุและคำตอบสองบริบทต่างกันจริง ให้ถามเฉพาะบริบทนั้น ไม่เลือก game.how_to_play หรือ procedure.steps จากคำว่า “ทำยังไง” เพียงอย่างเดียว

### 4.4 “วันนี้เปิดไหม”

ตีความเป็นสถานะเปิดบริการของวันที่ใน Asia/Bangkok ตรวจขอบเขตว่าข้อมูลที่มีเป็น physical opening หรือ bookability ถ้าหลักฐานยืนยันได้ จัดคำตอบสั้น วันที่ + เปิด/ปิด ถ้ามีเพียงข้อมูลจอง ห้ามยืนยันการเปิดเข้าศูนย์จากการไม่มี slot

### 4.5 “ตอนเย็นเปิดถึงกี่โมง”

“ตอนเย็น” เป็น temporal constraint ไม่ใช่ filler หากมีตารางที่ยืนยันช่วงปิดปลายวัน ให้ตอบเวลาสิ้นสุดพร้อมขอบเขตวัน หากตารางแต่ละวันต่างกันและไม่มีวันที่ ให้ตอบแยกวันหรือถามวันตาม scope ที่เหมาะสม ไม่ใช้ unresolved span เป็นเหตุให้ทิ้งตารางที่อ่านได้ทั้งหมด

## 5. ผลของการทบทวนต่อลำดับงาน

1. ทำ RequestPlan/NeedResult และ mapping ของเส้นทางที่มีอยู่ก่อนเพิ่ม semantic planner ใหม่
2. แก้ broad/all และ follow-up เพราะเป็นปัญหาตรงตามการใช้งานจริงของผู้ใช้
3. แก้ relation execution และ aggregation ที่ทำให้ข้อมูลที่มีไม่ถูกใช้
4. ย้าย price/rental/calendar/policy/rules เข้าสัญญาร่วมทีละ vertical slice
5. เพิ่ม LLM proposal เมื่อความหมายยังแก้ไม่ได้ โดยไม่ใช้ whole-sentence regex เดิม veto ทุก paraphrase อีกชั้น
6. ประเมิน quality และ regression แยกตาม source sufficiency; ยังไม่อ้างว่าคะแนนขึ้นจนมีการทดลองจริง

## 6. เอกสารอ้างอิงภายใน

- [Flow R96](../r96_paper_informed_flow_20261019/02_PROPOSED_FLOW_TH.md)
- [งานวิจัยเดิมและข้อจำกัด](../r96_paper_informed_flow_20261019/01_RESEARCH_AND_DIAGNOSIS_TH.md)
- [task flow R95](../r95_merged_flow_implementation_20261018/system/app/knowledge/common/task_flow.py)
- [composition ปัจจุบัน](../r95_merged_flow_implementation_20261018/system/app/knowledge/common/composition.py)
- [need ledger ปัจจุบัน](../r95_merged_flow_implementation_20261018/system/app/knowledge/common/need_ledger.py)
- [source/schema validation](../r95_merged_flow_implementation_20261018/system/app/knowledge/common/registry.py)
- [snapshot provider](../r95_merged_flow_implementation_20261018/system/app/knowledge/common/snapshot_provider.py)
- [shared deadline](../r95_merged_flow_implementation_20261018/system/app/pipeline/request_deadline.py)
