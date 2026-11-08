# R118 revision03 — ผลการเสริมความเข้าใจ ตัวอ่าน และการตรวจคำตอบ

## สรุป

พัฒนาจาก R117 revision04 และตรวจซ้ำด้วยคำถามเดิม 48 keys ผ่าน HTTP API จริง เปิด LLM โดยไม่มี category hints/expected answers ส่งเข้าแชท มีการแก้จากการอ่านคำตอบรายข้อเพิ่มเติมหลัง revision01 จึงมี 96 HTTP attempts รวมสองรุ่น แต่มีคำถามไม่ซ้ำเพียง 48 ข้อ ไม่ใช่ Full ใหม่ และไม่ใช่ชุดสุ่มเพื่อประมาณความถูกต้องทั้งระบบ

รุ่น HTTP ล่าสุดที่ทดสอบครบคือ revision02 หลังตรวจพบ metadata topic ยังหลุดในคำตอบ จึงมี revision03 เพิ่ม topic ในรายการช่องภายในที่ไม่แสดงต่อผู้ใช้เพียงจุดเดียว ตรวจด้วยการ replay แผนเดิมผ่าน renderer จริง (ไม่เรียก LLM/HTTP ใหม่) และเก็บ source code ของ revision02 ไว้ครบ การเทียบคะแนนในตารางยังติดป้าย revision02 ตรงตามรุ่นที่รัน

### คะแนนบนคำถามเดียวกัน

| รุ่น | Positive literal/clause | ข้อที่ผ่าน positive ทุกแถว | Strict compatibility |
|---|---:|---:|---:|
| Legacy R64 saved | 62/62 (100.00%) | 18/18 (100.00%) | 133/164 (81.10%) |
| R115 saved | 25/62 (40.32%) | 7/18 (38.89%) | 0/164 (0.00%) |
| R117 revision03 saved | 40/62 (64.52%) | 12/18 (66.67%) | 0/164 (0.00%) |
| R118 revision01 | 53/62 (85.48%) | 15/18 (83.33%) | 0/164 (0.00%) |
| R118 revision02 | 49/62 (79.03%) | 14/18 (77.78%) | 0/164 (0.00%) |

R117 ที่มีผลครบ 48 keys เปรียบเทียบในตารางคือ revision03; R118 สร้างจาก revision04 ซึ่งมีการตรวจเฉพาะ 8 keys ใน R117 รอบสุดท้าย จึงไม่ติดป้ายผล R117 revision03 ว่าเป็นคะแนน revision04

**คะแนน literal ไม่ใช่ semantic accuracy** รวมถึงกรณี Part I/Part II ที่ผ่าน keyword ได้จากส่วนที่ตอบ Part I แต่ยังตอบ Part II ไม่ครบ ต้องดูสถานะ partial และส่วนที่ขาดด้วย Strict ยังเทียบ route/mode/contract รุ่นเก่า จึงห้ามแปล strict 0 ว่าคำตอบเนื้อหาผิดทั้งหมด

คะแนน revision01 53/62 ลดเป็น revision02 49/62 จากคำถามศุกร์บ่ายเปิดไหม 4 grades: รุ่นแรกใส่หัวข้อทวนคำถามที่มีคำว่า “เปิด” จึงผ่าน keyword ทั้งที่ข้อความจริงยังตอบว่าไม่มีข้อมูลยืนยัน รุ่นหลังตัด general-style task ออกจึงไม่ทวนคำถามและไม่ผ่านคำเหล่านั้น ไม่ใช่หลักฐานว่าเนื้อหาที่เคยยืนยันถูกหายไป และไม่เพิ่มคำ keyword กลับเพื่อเอาคะแนน ตารางวันศุกร์มี open_periods=conflicted จริง แต่ข้อความ no-confirmation ยังอธิบายเหตุผลนี้ไม่ดีพอ เป็นจุดที่ต้องเสริมต่อ ดู CASEBOOK_TH.md

Legacy R64 ใช้ source data และกฎราคาคนละรุ่นกับ candidate จึงไม่ใช่ causal comparison ของ Flow ล้วน ๆ ไม่มีการรัน baseline ใหม่

### แยกภาษา

| ภาษา | Legacy R64 | R115 | R117 revision03 | R118 revision02 |
|---|---:|---:|---:|---:|
| th | 25/25 (100.00%) | 8/25 (32.00%) | 21/25 (84.00%) | 17/25 (68.00%) |
| en | 36/36 (100.00%) | 16/36 (44.44%) | 18/36 (50.00%) | 31/36 (86.11%) |
| auto | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) |

## สิ่งที่แก้และตรวจยืนยันจาก source

1. R2 ของ God of War Ragnarök อ่าน Heavy Attack/Heavy Runic Attack จากคอลัมน์ R2 ไม่เลือก R3 Lock-On
2. ยกเลิกจองผูกหัวข้อ customer cancellation ได้ เก็บเงื่อนไขอย่างน้อย 1 ชั่วโมงจาก source แยกจาก studio cancellation/penalty/refund
3. ค้น role→person ได้ แต่ไม่คืนชื่อเมื่อ public_scope ไม่ยืนยัน ข้อความระบุว่าพบ source แล้วแทนการบอกเหมือนไม่มีข้อมูล
4. Part I / Part II แยกเป็นสองชื่อ ชื่อไม่ระบุ Remastered จะไม่ใช้ฉบับ Remastered แทน ตอบ Part I และบอกขาด Part II
5. เช็กอินก่อนเล่นเกมต้องอ่านขั้นตอน C08 ไม่ตอบ service catalogue ของเกม
6. map pool ในกติกา CS2 ต้องอ่าน clause ของการแข่งขัน ไม่ตอบคำอธิบายเกม เพิ่ม bilingual topic bridge โดยไม่ฝังรายชื่อแผนที่ในโค้ด
7. วิธีจองต้องอ่าน booking_steps ที่มี source ไม่ติด entity_not_bound เพราะคำถามใช้ถ้อยคำทั่วไป
8. รุ่น GPU ใน PCs ผูกจากชนิดอุปกรณ์ pc และช่อง specifications.GPU คืนค่าที่บันทึกไว้โดยไม่สร้างสเปกใหม่
9. คำเกริ่นที่เป็น general task ว่าง เช่น กำลังวางแผนไปใช้บริการ/รบกวนเช็กข้อมูล ไม่ถูกแยกเป็นคำถามธุรกิจเพิ่ม โดยไม่ตัด factual clause/constraints
10. FAQ ไม่แสดง topic/intent_key/scope_note/คำถามตั้งต้นเป็นคำตอบลูกค้า แต่คงสถานะและหลักฐานใน audit; topic ตรวจยืนยันด้วย renderer replay หลัง HTTP revision02
11. คง explicit facets ของ typed reader และตรวจตัวตน/หลักฐานหลังเลือก; all controls ยังได้ครบ scoped source set
12. เก็บสมาชิก catalog เป็น game IDs ไม่ซ้ำสำหรับ operator list/count/group; รอบ HTTP นี้ยังไม่ได้วัดคุณภาพ natural-language count เป็นเปอร์เซ็นต์

## สิ่งที่ยังขาดและความผิดที่คะแนนไม่บอกทั้งหมด

อ่านรายงาน `02_SOURCE_GAPS_TH.md` ประกอบ: snapshot มี person 25 รายที่ public_scope unknown, rate 18 จาก 24 รายยังไม่มี calculation_rule ยืนยัน และเกมที่มีบริการยืนยัน 19 จาก 42 เกมยังไม่มีเส้นทางถึงโซนที่ยืนยันได้

- Nintendo/VR บางบริการไม่ทราบ resource_ids จึงตอบบริการที่มีเกมได้ แต่ยืนยันโซนไม่ได้ ไม่เติม relation จากความคล้ายของชื่อ
- การคำนวณระยะเวลาที่ไม่ได้ประกาศสูตรยังให้ unit rate พร้อมข้อจำกัด ไม่อ้างยอดรวม; ถ้า interpreter พลาด audience อาจยังแสดงหลายกลุ่ม ต้องเสริม alias/slot completeness โดยยึด source
- ชื่อบุคคลภาษาอังกฤษที่ source มีเพียงภาษาไทยยังจับไม่ได้บางราย และ public_scope ก็ยังต้องยืนยันแยกกัน
- คำเรียกอุปกรณ์ภาษาไทย/พิมพ์ผิดบางแบบยังจับเป้าหมายไม่ได้ แม้มีอุปกรณ์อยู่ใน source
- คำถามกว้างเรื่องบทลงโทษอาจเลือกได้เพียง clause บางส่วน ต้อง review parent/child scope และความครบถ้วน ไม่ถือว่าทุกย่อหน้าถูกครอบคลุมแล้ว
- คำถามราคาเกมที่ต้องไปผ่านหลายบริการ/หลาย duration อาจยังถาม slot ไม่เฉพาะเจาะจงพอ
- physical video recording กับ in-game capture เป็นคนละ predicate; source แบบหนึ่งไม่อนุญาตให้อ้างสิทธิ์อีกแบบ
- schedule มี open_periods ขัดแย้ง; ไม่อนุมานเปิด/ปิดจาก bookable/maintenance และไม่ใช้ provider ที่ตั้ง unavailable ใน test เป็นสถานะจริง
- compare/recommendation หลายเงื่อนไขและ paraphrase ที่ยังไม่ผูก target ไม่ได้ถือว่าแก้ครบ

### Positive literal ที่ยังไม่ผ่าน

| คำถาม | Failed grades | การจำแนกหลังดู source |
|---|---:|---|
| ขอสอบถามหน่อยครับ New Super Mario Bros. U Deluxe เล่นได้ที่โซนไหน | 4 | source_relation_gap |
| รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ศุกร์บ่ายเปิดไหม | 4 | calendar_source_conflict_and_generic_unconfirmed_response |
| Which studio zone has Little Nightmares II | 4 | source_relation_gap |
| Who holds te role of ประธาน | 1 | public_scope_unconfirmed |

กลุ่มข้างบนไม่ได้ถูกนับทั้งหมดเป็น actual content failure: สองคำถามขาดความสัมพันธ์โซนใน source อีกคำถามถูก public-scope guard และคำถามวันศุกร์มีเวลาเปิดขัดแย้งพร้อมปัญหาข้อความตอบกว้างเกินไป ส่วนการตอบครบความหมายของคำถามอื่นยังต้องอ่าน casebook ไม่ใช่สรุปจาก keyword pass

## การตรวจและข้อจำกัดการทดลอง

- Contract checks: 72/72 (แยกเป็น operator/source guards และสัญญา R117 เดิม)
- HTTP 48/48; validation_ok 48/48; capture mismatch 0
- Model transport: {'attempts': 58, 'successful_transport': 57, 'failed_transport': 1}; median latency 3.25s
- ตรวจรุ่นและ digest ของ scb10x/typhoon2.5-qwen3-4b:latest ก่อน–หลัง; transport/schema/ความถูกต้องเป็นคนละชั้น
- candidate source และ inputs ไม่เปลี่ยนระหว่างรัน; R117/ผลเก่าที่ป้องกันไว้ไม่เปลี่ยน; schema และข้อมูลทุกแถวใน DB ทั้ง 15 ตารางเท่ากับ R117 revision04 โดยตรวจ read-only ส่วน byte hash ของ SQLite file ต่างกันหลัง SQLite backup จึงไม่อ้างว่าไฟล์เหมือนกันทุก byte ดู DATABASE_EQUIVALENCE.json
- revision01/02 เก็บ source code ที่รันไว้ใน http01/FROZEN_SYSTEM และ http02/FROZEN_SYSTEM พร้อม ARCHIVED_CODE_VERIFIED.json; system เป็น revision03 ซึ่งเปลี่ยนการซ่อน topic เพียงจุดเดียว ดู RENDER_REGRESSION.json
- เปิด LLM หมายถึง Flow เลือกใช้ตามงาน ไม่ได้หมายถึง LLM สร้างคำตอบทุกคำถาม
- baseline เป็น saved results; 48 keys นี้เคยใช้พัฒนาแล้ว ไม่ใช่ holdout หรือหลักฐานว่าคะแนน Full เท่ากัน

## เอกสารและหลักฐาน

- [แผน Flow และการทบทวน](01_FLOW_AND_REVIEW_TH.md)
- [ช่องว่างของ source](02_SOURCE_GAPS_TH.md)
- [ทุกคำตอบและก่อน–หลัง](CASEBOOK_TH.md)
- [ตัวเลขผลวิเคราะห์](ANALYSIS_FINAL.json)
- [source contracts](PRECISION_CONTRACTS.json)
- [R117 contracts](CONTRACT_CHECKS.json)
- [HTTP latest completion](http02/TEST_COMPLETE.json)
- [HTTP latest raw](http02/RESULTS.jsonl)
- [การตรวจ renderer รุ่นสุดท้าย](RENDER_REGRESSION.json)
- [ความเท่ากันของข้อมูล SQLite](DATABASE_EQUIVALENCE.json)
- [ไฟล์โค้ดที่แก้](IMPLEMENTED_FILES.json)

Candidate R118 ยังไม่ติดตั้งทับ R78 และไม่ใช่การประกาศว่าแก้ครบทุกหมวดแล้ว