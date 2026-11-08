# ผลลงมือและทดสอบ Flow V2 — R98

วันที่ 19 ตุลาคม 2026 · candidate แยกจากระบบใช้งานจริง · ไม่มี full test R98 ในรอบนี้

## 1. สรุปที่ตรวจยืนยันได้

- ลงโค้ดชั้น RequestPlan/NeedResult ร่วมใน common candidate พร้อมการรวมคำตอบหลายเรื่องและการรักษา pending selection
- แก้ “ทั้งหมด/PC” หลังถามกลับ โดยเก็บกลุ่มผู้ใช้และระยะเวลา แล้วอ่านข้อมูลปัจจุบันใหม่
- แก้การถามสองเกมภาษาอังกฤษ, อ่านจำนวนผู้เล่นผ่าน game-mode relation, แยก live unavailable จากขั้นตอนจอง และถามบริบทเกมหลุดก่อนดึงกติกา
- แก้การเลือก booking procedure ผิดแทนตารางวันและเวลาที่จองได้
- มีการทดสอบ owner เพิ่ม/แก้/ถอนข้อมูลในฐานทดลอง โดยไม่มีการเพิ่ม facts หรือ approvals จำลองลงฐานจริง
- **R98 ยังไม่ใช่การย้ายทุก task ของ R97 ครบ และยังไม่ได้ติดตั้งทับ R78**

อ่านขั้นตอนพร้อมสถานะ W0–W9 ที่ [IMPLEMENTED_FLOW_TH.md](IMPLEMENTED_FLOW_TH.md)

## 2. ผลทดสอบแต่ละชุด

| ชุด | ผล | ความหมายและข้อจำกัด |
|---|---:|---|
| Customer probes ปิด LLM รอบสุดท้าย | 23/23 ผ่าน | ตรวจ scope, source, pending selection, exception และคำตอบหลายส่วนตามเงื่อนไขที่เขียนไว้ |
| Customer probes เปิด LLM รอบสุดท้าย | 23/23 ผ่าน | เปิด LLM จริง; มี model HTTP attempts 2 ครั้งและ response opened 2 ครั้ง; อีกหลายข้อใช้ deterministic readers |
| Existing task/owner/snapshot contracts | 65/65 ผ่าน | รวมความหมายคำถามใกล้เคียง, qualifiers, readiness, preview parity, snapshot race และ mixed question |
| Owner lifecycle | 13/13 ผ่าน | เพิ่ม/แก้/เผยแพร่/ถอน game, FAQ, equipment ใน SQLite แยก |
| Existing rental/source fixture | 19/19 ผ่าน | ราคาเหมา, audience/period tuple, เปลี่ยนราคา, วันมีผล, ถอนข้อมูล, FAQ ใหม่; transport ถูกจำลองว่าไม่พร้อม |
| Existing competition fixture | 7/7 ผ่าน | เปลี่ยน/เพิ่ม/ถอนข้อกฎ ไทยและอังกฤษ;ไม่ใช่ model inference benchmark |
| New V2 source contracts | 17/17 ผ่าน | ราคา all, rate ที่ไม่มี, audience/duration, mode join, เลือกบริบทแข่ง, multi-subject, mixed live |
| Saved-corpus subset เปิด LLM | 91/91 requests จบ, 162 grades | ใช้คำถามเดิมที่เลือกตาม domain/locale;ไม่ใช่สุ่มตัวแทนทั้ง corpus |

65+13+19+7+17 = **121 contract checks** เป็นจำนวน assertions รวม ไม่ใช่ 121 คำถามลูกค้าอิสระ และบางข้อเป็น schema/readiness tests จึงห้ามนำไปเรียกว่า accuracy 100% ของทุกหมวด

ผล 23/23 เป็น focused development contracts ไม่ใช่ holdout ที่ยังไม่ใช้พัฒนา เงื่อนไขบางข้อเช็กโครงสร้าง receipts ด้วย จึงไม่เท่ากับคะแนน semantic จากผู้ประเมินอิสระ

หลักฐาน:

- [Customer probe checks](CUSTOMER_PROBE_ANALYSIS.json)
- [LLM ON requests ทั้ง 23 ข้อและคำตอบเต็ม](final_on02/ANSWERS.jsonl)
- [LLM OFF requests ทั้ง 23 ข้อและคำตอบเต็ม](final_off02/ANSWERS.jsonl)
- [Existing contracts](verification/contracts02/SUMMARY.json)
- [Owner lifecycle](verification/owner01/SUMMARY.json)
- [Rental fixture](verification/existing02/SUMMARY.json)
- [Competition fixture](verification/competition01/SUMMARY.json)
- [V2 fixture](verification/v2_04/SUMMARY.json)

## 3. เทียบ R95 ด้วยคำถามเดียวกันจากผลที่เก็บไว้

เลือก 91 request keys ก่อนเห็นผล R98 โดยใช้ domain/locale และลำดับ hash คงที่ มี 162 grades รวม และมี positive text contracts 72 grades ใช้ checker เดิม ไม่แก้ expected answer หรือ GT เก่า

| มิติ | R95 retained | R98 หลังแก้รอบสุดท้าย |
|---|---:|---:|
| Requests ที่เทียบตรง key | 91 | 91 |
| Positive literal/clause ผ่าน | 55/72 (76.39%) | **61/72 (84.72%)** |
| ไทย | 23/29 (79.31%) | 25/29 (86.21%) |
| อังกฤษ | 16/26 (61.54%) | 20/26 (76.92%) |
| auto | 16/17 (94.12%) | 16/17 (94.12%) |
| Strict รวม protocol/outcome/text | 19/162 | 19/162 |
| Protocol failure reasons | 150 | 150 |
| Outcome failure reasons | 29 | 21 |
| Content failure reasons รวมทั้ง positive/negative contracts | 19 | 13 |
| Exceptions / empty answers | 0 / 0 | 0 / 0 |

ดีขึ้น **6 positive grades จาก 3 requests** หรือ **8.33 จุดเปอร์เซ็นต์เฉพาะ subset นี้** ไม่พบ positive literal regression ใน 91 ข้อนี้

Strict ไม่เพิ่ม เพราะยังมี protocol expectations เดิม เช่น route/intent/mode ที่ไม่ได้เปลี่ยนตาม candidate แม้ข้อความดีขึ้น ต้องตรวจ contract ให้ตรง interface ที่จะส่งจริง ไม่ใช้การตัด protocol ออกเป็นเหตุผลว่าทุกข้อถูกแล้ว

จำนวน reasons ไม่ใช่จำนวน requests และหนึ่ง grade อาจมีหลาย reasons จึงบวกทุกแถวเพื่อหา “จำนวนคำตอบผิด” ไม่ได้

**ห้ามสรุปว่า full-system accuracy เพิ่มจาก 74.59% เป็น 84.72%** เพราะคนละชุดคำถาม ชุดนี้เลือกมาพัฒนาและตรวจขอบเคียงเท่านั้น ยังต้องมี untouched holdout/full test ในขั้นถัดไป

หลักฐาน: [Comparison พร้อมคำถามที่ดีขึ้น](subset02/COMPARISON.json), [Selection manifest](FOCUSED_SELECTION.json), [Run coverage](subset02/RUN_FINISHED.json)

## 4. Loop ที่เกิดขึ้นจริง

### รอบ A — ก่อนแก้

บันทึก baseline จาก copy R95 แบบปิด LLM ไว้ที่ `baseline01` พบคำถาม refund ที่มีคำเกริ่นตกไป clarification, คำถามหลายเรื่องหายไปบางส่วน, EN สองเกมตอบไม่ได้ และคำตอบ PC/ทั้งหมดไม่รักษา price task ตามที่ต้องการ

baseline focused contracts ผ่าน 6/20 แต่ตัวเลขนี้รวมข้อกำหนด receipts/plan ใหม่ด้วย จึงไม่ใช่หลักฐานว่ามี 14 คำตอบที่เนื้อหาผิดทั้งหมด

### รอบ B — ลงชั้นแผนร่วมและ domain slices

ทำ request-plan aggregation, price scope, relations และ context clarification จากนั้นทดสอบ source lifecycle พบข้อผิดพลาดที่เกิดจากโค้ดใหม่จริง:

1. ตัวดักราคาทั่วไปแย่ง `price again` จาก rental pending contract ทำให้ถามเลือก service ใหม่ ทั้งที่ก่อนหน้ารู้ PC/full-day/external แล้ว
2. ตัวดักราคาทั่วไปแย่ง `game overview and price` จน overview ของเกมหายไป

แก้ด้วยการให้ rental parser resolve contract ก่อน และแยก task coordination ที่ชัดเจนก่อน price selector ไม่เพิ่มราคาหรือชื่อเกมลงโค้ด

รันซ้ำแล้ว existing rental 19/19 และ task contracts 65/65 ผ่าน

### รอบ C — ทดสอบชุดข้างเคียง 91 requests

รอบแรก positive text score ยัง 55/72 เท่า retained R95 พบ 3 คำถามที่ควรตอบ schedule แต่ไปตอบ booking procedure:

- “อยากทราบวันและเวลาที่ศูนย์ให้บริการสำหรับการจอง”
- “Can I book Monday morning, or only the afternoon?” พร้อมคำเกริ่น
- “On which days can I book morning and afternoon slots?” พร้อมคำเกริ่น

สาเหตุคือ booking cue ทำให้ FAQ ขั้นตอนจองชนะ ทั้งที่ requested predicate คือ weekday/time period

เพิ่ม timetable interpretation ก่อน booking reader โดยยังห้ามนำ regular timetable ไปใช้เป็น live slot answer และไม่ override วันที่เฉพาะ จากนั้นรัน 91 keys เดิมอีกครั้ง → positive score 61/72 โดยเก็บผลรอบแรกไว้

## 5. ปัญหาที่ยังเห็นใน 91 requests รอบสุดท้าย

มี 10 requests ที่ยังมี content/keyword failures รวม 13 failure reasons ตาม checker ต้องแยกดังนี้:

| คำถาม/กรณี | สิ่งที่เกิดขึ้น | วิเคราะห์และงานที่ยังเหลือ |
|---|---|---|
| ขอข้อมูลที่ไม่ได้อยู่ในเว็บ | ตอบว่าจับคู่ข้อมูลไม่ได้และขอหัวข้อเพิ่ม | ข้อความไม่ตรง alternatives ของ GT;ไม่ใช่ hallucination แต่ควรบอกขอบเขตข้อมูลให้ชัดกว่า generic clarification |
| unknown game Example Quest | generic clarification ไม่สะท้อนชื่อที่ถาม | entity mention ของเกมที่ไม่อยู่ใน catalog ไม่ถูกเก็บเป็น unresolved target;ควรถาม/แจ้งเฉพาะชื่อนั้น |
| Call of Duty เล่นได้ที่ไหน | generic clarification | มีหลายชื่อ/edition แต่ยังไม่ให้ตัวเลือกเฉพาะ;ต้องทำ ambiguity candidate choice |
| คนนอกเล่นได้ทุกเกมไหม | generic clarification | เป็น universal eligibility/offerings claim ที่ยังพิสูจน์ไม่ได้;ควรบอกข้อจำกัดตรงประเด็นแทนให้ระบุอุปกรณ์ลอย ๆ |
| server กับ client ต่างกันอย่างไร | fallback | อาจเป็นข้อมูล technical explainer ในขอบเขตเดิม ต้องตรวจว่ามี source/owner scope ที่ตั้งใจรองรับหรือไม่;ไม่เพิ่มความรู้ทั่วไปเพื่อไล่คะแนนโดยอัตโนมัติ |
| Super Mario Odyssey อยู่โซนไหน | ตอบ Nintendo Switch services แบบ 1–2 / 1–4 Persons | source relation ตรงตระกูล Switch แต่ GT ต้องการคำว่า Nintendo Switch Zone;ควรอ่าน zone label ผ่าน relation ให้ตรงระดับที่ถาม ไม่ถือว่าเนื้อหาผิดทั้งหมดเพียงเพราะ keyword ไม่ตรง |
| visitors use VR without booking | ตอบว่าต้องจองผ่านระบบก่อน | ใจความเรื่องต้องจองมี source แล้ว แต่ GT ต้องการประโยค No แบบตรงตัวและ one hour;ต้องตรวจ clause scope ของ GT ไม่เติม duration ที่ผู้ใช้ไม่ได้ถามเพื่อให้ผ่าน |
| food/noise/damage policy | ตอบ summary แต่ไม่มี 100–500 THB ที่ checker รอ | เป็น candidate missing-clause/dependency issue;ต้องไล่ source ว่าค่าปรับนี้ผูกข้อใดก่อนดึงมารวม ห้ามเติมจำนวนเงินโดยไม่มี scope ยืนยัน |
| คนทั่วไปจอง PC ราคาเท่าไร | แจ้งวันมีผลยังไม่ยืนยันและแสดงหลายกลุ่ม | มีทั้งปัญหา validity ของ source และ audience narrowing ที่ยังไม่แม่น;checker รอคำว่า บาท การไม่แสดงราคาปัจจุบันที่ไม่มีวันมีผลไม่ได้แปลว่า retrieval ไม่มีตัวเลข |
| bring alcohol into gaming area | generic qualified-scope clarification | source ยืนยันห้าม consume alcohol แต่ bring กับ consume เป็นคนละ action;ควรตอบส่วนที่ยืนยันและบอกข้อจำกัดเรื่องการนำเข้า แทน clarification ลอย ๆ และไม่อนุมานข้อห้ามการนำเข้าจากข้อห้ามดื่ม |

อ่านคำตอบเต็มและ failures ทั้งหมดที่ [CONTENT_REVIEW.json](subset02/CONTENT_REVIEW.json) ข้างต้นเป็นการวิเคราะห์จาก saved output/source ที่อ่าน ไม่ใช่ human adjudication หรือ oracle ที่ยืนยันทุก clause แล้ว

## 6. ข้อมูลที่ยังขาดจริง

### 6.1 จำนวนผู้เล่นเกมเดิม

snapshot ที่คัดลอกมาไม่มี `game_mode` records ดังนั้น VALORANT ใช้ผู้เล่นกี่คนจึงยังไม่ควรตอบเป็นตัวเลขโดยเดา ใน fixture ที่เพิ่ม mode พร้อม min/max แล้ว ระบบอ่านผ่าน relation ได้ทั้งไทยและอังกฤษโดยไม่แก้ชื่อเกมในโค้ด

### 6.2 ราคาปัจจุบัน

บาง rates มีช่วงมีผลสิ้นสุดแล้ว และบาง PC rates ยังมี validity=unknown ปัญหานี้แก้ด้วยการยืนยัน/เผยแพร่ owner data ที่มีวันมีผลถูกต้อง ไม่ใช่ยืดวันในฐานเดิมให้คะแนนผ่าน

ราคาเหมาจ่ายยังอยู่ใน common source และ existing rental fixture ตรวจการแก้/ถอน/เปลี่ยนช่วงราคาแล้วผ่าน ไม่มีการลบข้อมูลเหมาออก

### 6.3 สิทธิ์คำว่า external visitors

audiences มีชื่อกลุ่ม แต่ eligibility/proofs ของข้อมูลที่ย้ายมายังไม่ครบ จึงไม่ควรเลือก General Adult แทนผู้ถามทุกคน ต้องให้ owner กำหนด alias และเกณฑ์สิทธิ์ที่ชัดเจน

## 7. Model transport และเวลา

- รอบ 23 คำถาม LLM ON: มี HTTP generate 2 attempts, response opened 2 ครั้ง ส่วน deterministic tasks ไม่ต้องเรียก model ทุกข้อ
- รอบ 91 คำถามสุดท้าย: 43 model HTTP attempts, response opened 43 ครั้ง ไม่มี request exception/empty answer
- response opened คือ transport ส่งกลับได้ ไม่เท่ากับ planner ตีความถูกหรือคำตอบมีหลักฐานครบ
- median wall time ใน probe รอบสุดท้ายประมาณ 0.65 วินาทีเมื่อเปิด LLM และ 0.63 วินาทีเมื่อปิด;ค่าสูงสุดประมาณ 6.41 และ 3.76 วินาทีตามลำดับ
- ชุด 91 ใช้ 2 worker และ admission limit 1;มี probe ที่รันร่วมช่วงหนึ่ง จึงใช้ตัวเลขเวลาเป็น development observation เท่านั้น ไม่ใช่ benchmark concurrent production capacity
- Live booking ถูกกำหนดให้ unavailable ใน tests;ไม่มีการยืนยันความถูกต้องของที่นั่งว่างจริง
- reference clock ใน real-data probes/corpus คือ 16 ตุลาคม 2026 เวลาไทยตาม baseline;คำตอบ “วันนี้” ใน logs ไม่ใช่วันทำรายงาน

## 8. Integrity และการส่งมอบ

ตรวจ [INTEGRITY.json](INTEGRITY.json):

- R95 source 1,075 ไฟล์ unchanged
- candidate common database unchanged
- final probe source manifests ก่อนและหลังตรงกัน
- candidate แก้ไฟล์เดิม 7 ไฟล์ เพิ่ม modules 5 ไฟล์
- ไม่ติดตั้งทับ R78 ไม่แก้ production data/approvals และไม่ทับ logs ของรอบก่อน

ไฟล์ทดสอบและเครื่องมือวิเคราะห์อยู่ในโฟลเดอร์นี้ทั้งหมด แต่ **โฟลเดอร์ R98 นี้เป็น implementation candidate ไม่ใช่ portable production package ที่ส่ง owner ใช้ได้ทันที**

## 9. ข้อสรุปและลำดับต่อไป

Flow slices ที่ทำช่วยแก้ปัญหาที่เจาะจงได้จริง และชุด 91 ข้อมี positive text gain โดยไม่พบ literal regression ในชุดนั้น แต่ยังมี compatibility routing, ambiguity และ source scope gaps ตามที่ระบุไว้

งานลำดับต่อไปควรเป็น shared semantic interpretation + targeted ambiguity + policy dependency/entailment และ global model budget โดยใช้ source-backed holdout เพิ่มก่อนพิจารณา full test/ติดตั้ง ไม่ควรกลับไปสะสม canned answers ทีละชื่อเกมหรือแก้ GT เพื่อทำคะแนนให้สูงขึ้น
