# R122 — ผลพัฒนาการเข้าใจบริบทและตัวอ่านข้อมูล

## สรุปสถานะ

ทำ candidate ล่าสุด `revision04_system` แล้ว ใช้ LoRA ที่ฝึกจริงใน R121 จำนวน 93 optimizer steps ไม่มีการฝึกน้ำหนักรอบใหม่ใน R122 และยังไม่ได้ติดตั้งทับ R78/production

แก้การปนเงื่อนไขระหว่างคำถามย่อย การผูกคำอ้างอิง การถามกลับเมื่อยังตีความไม่ได้ ตารางให้บริการทั้งสัปดาห์ และชื่อโปรไฟล์โมเดลของ fallback พร้อมเสริม service→game ellipsis จากความสัมพันธ์ต้นทาง

ทดสอบ API ครบ 16 คำตอบสำหรับคู่ base/trained บน revision02 เพิ่ม 2 คำตอบบน revision03 และตรวจแก้ VR อีก 1 คำตอบบน revision04 รวม 19 คำตอบที่วัดจบ คำถามทั้งหมดมาจากชุดเดิม ไม่มี Full Test ไม่มีการรัน Flow เดิมใหม่ และไม่มีเปอร์เซ็นต์ semantic accuracy รวมที่ยืนยันได้จากงานนี้

## 1. ผลการเทียบแบบตั้งค่าเดียวกัน

| ตัววัด | Base | Trained context adapter |
|---|---:|---:|
| HTTP 200 / คำถาม | 8/8 | 8/8 |
| Strict benchmark เดิม | 0/15 | 0/15 |
| Positive literal checks | 0/5 | 4/5 |
| Median API latency | 50.297 วินาที | 23.680 วินาที |

Positive literal checks มีอยู่เพียง 2 จาก 8 คำถาม: Nintendo 4 checks และ CS2 1 check ดังนั้น 4/5 ไม่ใช่ 80% ของคำถามทั้งหมด และไม่ใช่คะแนนความถูกต้องรวม

### แยก locale

| Locale | คำถามต่อแขน | Strict base → trained | Positive literal base → trained |
|---|---:|---:|---:|
| th | 3 | 0/8 → 0/8 | 0/4 → 4/4 |
| en | 5 | 0/7 → 0/7 | 0/1 → 0/1 |
| auto | 0 | ไม่มีในชุด API นี้ | ไม่มี |

8 ข้อนี้เคยใช้วิเคราะห์และพัฒนาแล้ว จึงเป็น development comparison ไม่ใช่ fresh holdout ผลจาก R121 raw model 30 ข้อเป็นการวัดอีกแบบและคนละชั้นของระบบ ต้องไม่เอามารวม denominator กัน

## 2. วิเคราะห์รายกรณีจากคำตอบจริง

| กรณี | Base รอบนี้ | Trained รอบนี้ | ข้อสรุปจาก source |
|---|---|---|---|
| CS2 ปรับ Brightness/Resolution/Crosshair | งดตอบเพราะหา clause ไม่ครบ | ดึง clause ของ CS2 2026 ได้ | แหล่งข้อมูลมีจริง ปัญหา base อยู่ที่แผน/เส้นทางอ่าน ไม่ใช่ไม่มี clause |
| Nintendo Zone มีอะไรให้ใช้ | ตอบรายชื่อเกม | ตอบ OLED, TV 86 นิ้ว, จอย และตัวอย่างเกม | เลือก equipment usage ตรงเจตนาขึ้น |
| Tekken 8 ปุ่ม + ราคา PC | ตอบเฉพาะราคา | ตอบ controls และราคา แยกสองงาน | source มี 12 control entries แต่ไม่ระบุชุด 8 ปุ่มที่ถาม จึงต้อง partial/ถามกลับ ไม่อ้างว่าตอบชุด 8 ปุ่มครบ |
| ไม่ใช่นักศึกษา PSU เข้าได้ไหม | ตอบ owner policy ได้ | ตอบ owner policy ได้ | ทั่วไปเข้าได้ตามข้อมูล draft; ไม่ขยายเป็นสิทธิ์ลงแข่ง |
| ถือขวดน้ำเข้า ไม่ได้ถามเรื่องกิน | ยังไม่ยืนยัน | ยังไม่ยืนยัน | source การบริโภคไม่ใช่หลักฐานสิทธิ์นำเข้าแยกต่างหาก |
| FF16 ต้องจองอะไร | PS5 #01–#02 | PS5 #01–#02 | ใช้ relation เกม→บริการที่มีอยู่ |
| จอง Cockpit และเปิดวันไหน | ตอบเฉพาะตาราง | ตอบขั้นตอนจองและตาราง 7 วัน | ตารางมีจริง; applicability ต่อ resource และช่วงมีผลยังไม่ยืนยัน จึงไม่ใช่คำตอบเปิดจริงแบบไร้เงื่อนไข |
| ผู้ใช้ภายนอกต้องแสดง ID อะไร | ดึง documents ได้ | ดึง documents ได้ | มี owner policy และ legacy document policy ซ้ำ ควรรวมให้อ่านง่ายขึ้น |

คำว่า source ในตารางหมายถึงฐานข้อมูล migration/evaluation draft ที่ frozen ไว้ ไม่ใช่การยืนยันว่าเจ้าของเผยแพร่หรืออนุมัติใช้งานจริงแล้ว

## 3. ทำไม strict ยังเป็นศูนย์

1. Protocol: route ภายนอกของ format กลางเป็น `knowledge` แต่ evaluator เดิมคาด `equipment`, `multi_question`, `rules` ฯลฯ จึงผิด route แม้เนื้อหาบางข้อรองรับจาก source

2. Complete-clause/keyword: CS2 evaluator ต้องการประโยคลงท้าย `computer monitor` ขณะที่ source ที่ดึงมี `computer screen` และข้อความไทยที่ความหมายสอดคล้อง ต้อง review ความหมายแยก ห้ามนับเป็นคำตอบผิดทั้งหมดจาก literal fail อย่างเดียว

3. First-line: ประโยคแรก CS2 เป็นคำชี้แจงการแปล ก่อนเริ่มตอบ clause ทำให้ first_line_off_topic ซึ่งเป็นปัญหาการจัดคำตอบที่ยังแก้ได้

4. Evidence identity: wrong_game_source ของ CS2 ต้องอ่านกับหลักฐานจริง โดย hit มี `common_game_id=game_detail_cs2`, game=Counter-Strike 2 และ rulebook=competition_rules_cs2_psu_phuket_2026 จึงยังไม่มีหลักฐานว่าไปดึงกติกาคนละเกม เพียงเพราะ checker อ้าง source ID เดิมไม่ตรง

5. Performance: trained ยังมี latency_ceiling 10 occurrences ใน 15 grades; base มี 15 occurrences ตัวเลขเป็น occurrences ต่อ grade จึงซ้ำคำถามได้ และความเร็วดีขึ้นไม่ได้หมายความว่าผ่าน SLA แล้ว

## 4. Model transport แยกจากคุณภาพคำตอบ

รอบเทียบ revision02 เรียก backend จริง 21 ครั้ง สำเร็จ 21 ครั้ง: context 16, evidence selection 4 และ generic base inference 1 ไม่มี transport error ในรอบนี้ โปรไฟล์ที่ caller ขอและ adapter_active ถูกตรวจจาก log จริง

รอบ probe revision03 เรียก backend 3 ครั้ง สำเร็จ 3 ครั้ง รายละเอียด stage และ raw output เก็บใน inference03/REQUESTS.jsonl

รอบแก้ revision04 เรียก backend 1 ครั้ง สำเร็จทั้งหมด รวมรอบที่วัดครบทั้งสามชุด 25 backend calls ไม่มี transport failure

ก่อนหน้านี้ R121 API มี base fallback 3 ครั้งเรียกชื่อ default ที่ backend ทดลองไม่รองรับ รอบนี้กำหนด model environment ทั้งห้าตัวแล้ว จึงแก้สาเหตุด้านการตั้งค่าได้ อย่างไรก็ตาม HTTP 200 และ schema ผ่านไม่ใช่หลักฐานว่าคำตอบถูก semantic

Context adapter ใช้เฉพาะ context stage ของ trained arm; selector และ generic inference ใช้ base weights ทั้งสองแขน รุ่น base HF NF4 นี้ไม่ใช่ไฟล์น้ำหนักแบบเดียวกับ Ollama GGUF ของ Flow เดิม จึงไม่อ้างผลนี้ว่าเทียบกับ Flow เดิมโดยตรง

## 5. การเสริม revision03 หลังการเทียบ

จับ implicit ellipsis แบบจำกัด: task แรกมีชื่อบริการเดียว task ถัดมาถาม game catalog โดยไม่มีชื่อใหม่ และมี source relation บริการ→เกม จึงสืบทอดเฉพาะชื่อบริการเป็น target พร้อม audit โดยไม่สืบทอด duration/audience/price ของอีก task

ตรวจ 11 จุดจาก saved plans, 6 regression questions และ 5 เงื่อนไขจาก 2 compound questions กับ revision03 แล้ว ทั้งหมดผ่าน แต่ตัวเลขเหล่านี้เป็น gates เฉพาะจุด ไม่ใช่จำนวนคำตอบที่ถูกทั่วไป

### คำตอบ probe ผ่าน API จริง

#### What is the price of Cockpit and what games are available

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]

Cockpit #01-#02 — all offered games: Gran Turismo 7 [S4]

HTTP 200; 45.594 วินาที; key `207177ab21da22e4f9091d6d06eeb0f4dfc52bc12b03ecc9615cc69c68e65121`

#### How is VR for 30 minutes different from VR for 1 hour, and how do I book it?

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / PSU Student and Staff — minutes per session: 30 [S1]
VR Station 30 นาที / General Adult — minutes per session: 30 [S2]
VR Station 30 นาที / PSU Alumni and General Student — minutes per session: 30 [S3]
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB for 30 minutes [S4]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB for 30 minutes [S5]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB for 30 minutes [S6]

The checking service is unavailable; this detail cannot be confirmed.

HTTP 200; 33.953 วินาที; key `831a618e86ca1735d5b64a3241c951ef3ca5dc5b7ada0bb6d7cdeceac7c824df`

### แก้ต่อเป็น revision04 จากผล VR ที่ยังผิด

VR_SOURCE_REVIEW.json ยืนยันว่ามีทั้ง rates 30 และ 60 นาที และมีข้อความขั้นตอนจอง 3 records ซึ่งเป็น 2 ข้อความไม่ซ้ำ จึงไม่ใช่ข้อมูลหาย ผล revision03 ส่งแผน compare มาถูกแล้ว แต่ reader/selector เลือกเพียง 30 นาที และ task จองลงท้าย reason request_model_budget_exhausted ไม่ใช่ model transport ล้ม

revision04 อ่านอัตราของแต่ละระยะเวลาที่ระบุจาก source แยกกัน ไม่รวมยอดทางเลือกเข้าด้วยกัน และนำเสนอขั้นตอนจองหลายฉบับแยกกันในสถานะ partial แทนการใช้โมเดลเลือกฉบับใดฉบับหนึ่งโดยไม่มี authority rule เพิ่ม

ตรวจ source-level เพิ่ม 6 จุด: พบ 30/60 ครบ, มี booking claims, ไม่ temporary failure, ไม่เรียกโมเดลเพิ่มจาก saved plan, ไม่รวมยอดทางเลือก, และเปิดเผยหลายฉบับของ procedure ผลผ่านทั้งหมด

ผล API จริงหลังแก้:

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Comparison of recorded durations and rates only. Each line is an alternative, not a combined total.
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB for 30 minutes [S1]
VR Station 30 นาที / PSU Student and Staff — minutes per session: 30 [S2]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB for 30 minutes [S3]
VR Station 30 นาที / PSU Alumni and General Student — minutes per session: 30 [S4]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB for 30 minutes [S5]
VR Station 30 นาที / General Adult — minutes per session: 30 [S6]
VR Station 1 ชั่วโมง / PSU Student and Staff — per-person price for the rate duration: 0 THB for 60 minutes [S7]
VR Station 1 ชั่วโมง / PSU Student and Staff — minutes per session: 60 [S8]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — per-person price for the rate duration: 375 THB for 60 minutes [S9]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — minutes per session: 60 [S10]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB for 60 minutes [S11]
VR Station 1 ชั่วโมง / General Adult — minutes per session: 60 [S12]

Multiple recorded versions of the booking steps follow. They are retained separately rather than merged into a single policy.
How to book: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S13]
Booking steps: The booking procedure is: select the desired service, choose the date and time, enter customer information, verify the details, pay by transferring funds to a bank account, and attach the transfer slip. [S14]

HTTP 200; 47.453 วินาที; ผลก่อนแก้เก็บใน ellipsis01 ผลหลังแก้เก็บใน comparison01

## 6. สิ่งที่แก้และสิ่งที่ยังเหลือ

### แก้แล้วใน candidate

- ตรวจ local constraints ต่อ task และบันทึกสิ่งที่ถูกเอาออก
- ผูกชื่อจาก it/its/เครื่องนั้น ด้วยชื่อที่อ้างจากคำถามและ source index
- รองรับ PC/VR ซึ่งเป็นชื่อย่อสองตัวอักษร
- ถามกลับเมื่อ pronoun ไม่มีสิ่งอ้างอิง หรือระยะเวลาสองค่ายังไม่แยกบทบาท
- รักษาคำถามเปรียบเทียบระยะเวลาและข้อความกำกับรูปแบบ เพื่อไม่สร้างความกำกวมเกินจำเป็น
- อ่าน recorded play-service timetable ทั้ง 7 วัน
- แยก regular timetable ออกจาก live availability
- ตั้งค่า caller/fallback ให้ใช้โปรไฟล์ถูกแขน
- เสริมบริการ→เกมในคำถามที่ละชื่อบริการตามเงื่อนไขที่รองรับ

### ยังเหลือ

- Shared prefix, audience, เงื่อนไขซ้อน และหลาย entity ในหลายประโยคยังไม่ใช่ semantic parser ที่ครอบคลุมทุกแบบ
- แหล่งข้อมูลที่ยืนยันสิทธิ์ถือเครื่องดื่มเข้าแยกจากสิทธิ์บริโภคยังขาด
- ชุดย่อย 8 ปุ่มและจำนวน control entries ต้องระบุความหมายให้ชัด
- ตารางยังขาด applicability ต่อ resource และ effective interval ที่ยืนยัน จึงต้องรักษาคำชี้แจง partial
- Comparison reader ใหม่จำกัดที่ duration_minutes และระยะเวลาชัดเจน ไม่ครอบคลุมจำนวนคน/รอบร่วมใน comparison; การเขียนระยะเวลาเป็นคำและคำเปรียบเทียบรูปอื่นยังต้องตรวจ normalization ต่อ
- รูปแบบ first line, คำตอบซ้ำจากหลาย source และ taxonomy ของ public API ยังควรพัฒนาต่อ
- ความเร็วบน GPU 6GB ยังไม่ผ่านเกณฑ์เดิมหลายข้อ
- Native compatibility typed parsers/fallback ยังอยู่ และยังไม่มีการวัด Full ของ candidate นี้

## 7. ข้อมูลสอน

annotation_draft03 เก็บคำถามเดิม 244 train / 15 validation / 30 test พบ label แตกต่าง 11 ข้อจาก 289 ข้อ เป็น draft ของ task scope ที่ต้อง review semantic เพิ่ม ไม่ได้นำไป optimize น้ำหนัก ไม่ได้แทนที่ gold เก่า และไม่ได้เปลี่ยนคะแนน R121 ย้อนหลัง

## 8. การเก็บหลักฐานและข้อจำกัดการเปรียบเทียบ

- คู่ API 16 คำตอบใช้ revision02 ที่ frozen; probe 2 คำตอบใช้ revision03 ที่ frozen แยกกัน ไม่เอามาปนว่า 18 คำตอบรัน source รุ่นเดียวกัน
- R121 saved API ที่แสดงใน API_PER_REQUEST_TH.md เป็น initial system รอบ api02 ก่อน guard revisions รุ่นหลัง และมี config confound ที่ระบุไว้ จึงใช้ดูกรณี ไม่ใช่ causal comparison ของ revision04→R122
- Runtime label ใน paired harness คงชื่อ R121-context-lora เดิม แต่ source path/hash ของ R122 ถูกตรวจโดย RUN_FREEZE; manual launcher ใช้ชื่อ R122 revision03 แล้ว
- รันแรกใน execution01 ถูกยกเลิกเมื่อพบ pronoun guard กว้างเกินไป เก็บ partial results, CANCEL_REASON และ logs ไว้ ไม่เอามานับเป็นรอบครบ
- รักษาฐานข้อมูลจริง approvals logs เดิม น้ำหนักและชุดฝึกเดิม รวมถึงไฟล์ source ที่ป้องกันไว้

```json
{
  "parent_source_files_unchanged": 1135,
  "original_protected_files_unchanged": 1138,
  "current_frozen_files_unchanged": 1145,
  "training_frozen_files_unchanged": 13,
  "same_adapter_verified": true,
  "same_model_revision_verified": true,
  "all_runtime_model_variables_verified": true,
  "production_installed": false,
  "latest_candidate": "R122 revision04",
  "latest_candidate_frozen_files_unchanged": 1145,
  "latest_database_sha256": "029119eaa24e53b4110c6c8cc7f650674f68e03ee605929cea8f23857a6429d3",
  "probe_adapter_identity_verified": true
}
```

## 9. ไฟล์สำหรับตรวจต่อ

- FLOW_R122_TH.md: Flow และขอบเขตของแต่ละ guard
- API_PER_REQUEST_TH.md: คู่คำตอบ base/trained และ R121 saved รายข้อ
- ANSWER_SOURCE_EVIDENCE.json: คำตอบ, source IDs, snapshot hash และ decision artifacts
- API_COMPARISON.json: คะแนนแยก strict/literal/locale/transport
- OFFLINE_CONTEXT_VERIFICATION03.json, CONTEXT_REGRESSION_VERIFICATION03.json, ELLIPSIS_VERIFICATION.json: จุดตรวจ source/context
- api02 และ ellipsis01: actual API captures กับ RUN_FREEZE
- inference02 และ inference03: backend requests/raw outputs/provenance
- annotation_draft03/REVIEW_REQUIRED.json: diff ป้ายสอนที่ต้อง review

ขั้นถัดไปควรขยาย shared context/normalization ของ comparison ตรวจ authority ของ procedure variants และทำ contract mapping ของ public API โดยคงเกณฑ์ benchmark เดิมแยกไว้ จากนั้นค่อยขยายการวัดด้วยคำถามเดิมที่มีอยู่ ยังไม่ควรอ้างว่าทุกหมวดพร้อม production หรือเริ่ม Full Test โดยไม่มีการพิจารณาผลรอบนี้
