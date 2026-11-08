# รายงานพัฒนาและตรวจผล — Conversation Reliability r38.3

วันที่ 5 ตุลาคม 2026 / Asia Bangkok

## สรุป

แก้กลไกที่ทำให้ “PC” และ “ทั้งหมด” หลุดจากคำถามราคาที่บอทถามค้าง เพิ่มการตอบตามกลุ่มผู้ใช้และขอบเขตที่ขอ รองรับคำเลือกบริการหลายสำนวนไทย/อังกฤษ ทำกติกาฉบับเต็มเป็นส่วนพร้อมการต่อหน้า และแก้คำถามทั่วไปที่ถูกถามกลับเรื่องศูนย์

ทดสอบกับ source จริง โมเดลจริง เว็บ และแพ็กเกจใหม่ โดยเก็บผลที่ล้มเหลวไว้ก่อนแก้ ไม่ทับ release หรือ log เดิม ไม่มีการเปลี่ยนอัตรา นโยบาย เวลาเปิดปิด หรือข้อมูลที่เจ้าของกรอก

**เว็บชุดที่แก้:** [เปิด r38.3](http://127.0.0.1:8096/) — ชุดเดิมที่ 8090–8092 ยังอยู่ตามเดิม ตัวเปิดใหม่ตรวจ version และ installation เพื่อไม่เปิดผิดชุด

**ไม่ได้สรุปว่าทั้งระบบไม่มีข้อผิดพลาดแล้ว:** รายการที่ยังขาดหลักฐานแยกไว้ในข้อ 7 และ [Flow ที่ปรับตามผลจริง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/conversation_reliability_implementation_20261005/FLOW_IMPLEMENTED_R38.md)

## 1. ทำไมคำตอบเดิมผิด และแก้ตรงไหน

| หมวด | สาเหตุที่ตรวจพบ | วิธีแก้ | ผล/ข้อจำกัด |
|---|---|---|---|
| คำตอบต่อ PC | resolver ไม่ได้เติมบริการลง price task เดิม แล้วข้อความสั้นถูก route ใหม่ | typed request plan และ pending service; parent เก็บ task ก่อนส่ง worker | หลังถามราคาบุคคลภายนอก → PC ได้ 25/70 บาทตาม source แยกกลุ่ม |
| คำตอบต่อ ทั้งหมด | ขอบเขตคำถามเดิมหาย และ fuzzy อาจอ่าน all phrase เป็นชื่อบริการ | all scope ก่อน fuzzy; expected package IDs ตาม task | ทุกบริการภายนอก 7 แพ็กเกจ × 2 กลุ่ม = 14 rows ตาม snapshot ที่ตรวจ |
| ตัวเลือกถูกเข้าใจเป็นการเลือก | อ่านชื่ออุปกรณ์จากรายการในคำตอบผู้ช่วย | selected targets ใช้หลักฐานจากผู้ใช้และ metadata ที่ตรวจ schema | ไม่ default PS5 จากตัวเลือกของบอท |
| ราคาเกินกลุ่ม | วน catalog ทุกกลุ่มแม้ถาม external/Adult | customer group filter และตรวจ negation ก่อนคำด้านบวก | external ไม่มี PSU ฟรี; Adult/Student เลือกเฉพาะกลุ่มที่ถาม |
| เวลา/จำนวนคนหลายบริการ | ตัวแปรรวมอาจปนกัน | per-target duration/capacity; ไม่คูณต่อหัวเอง | PC 2 ชั่วโมง/VR 30 นาทีตรวจแยก; จำนวนคนไม่ตรงแพ็กเกจแจ้งจุดที่ต้องระบุ |
| คำถามหลายงาน | pending ราคาเหลือ task เดียว | เก็บราคา + วิธีจอง; outcome ราย task | TH/EN ตอบสองส่วน; แหล่งของส่วนหนึ่งขาดยังแสดงราคาที่มี |
| กติกา ขอทั้งหมด/ต่อ | ยึด raw question หรือ summary แทนเนื้อหาที่แสดง และ ack ถูกอ่านช้า | rule manifest/hash/full-section ledger; รับ ack ก่อนอ่าน history | หน้าใหม่ไม่ซ้ำส่วนที่รับรองการแสดงแล้วในเคสตรวจ |
| เนื้อหากติกาบางบรรทัดหาย | filter จากภาษา/ความยาวทำให้แผนที่และข้อความสั้นที่มีความหมายตก | หน่วยเนื้อหาตามต้นฉบับ รวมตาราง/บทลงโทษ | manifest ครบหน่วยที่กำหนด; RoV EN มี gap ที่ต้องรายงาน |
| ไก่กับไข่ถูกถามเกม/ราคา | unknown/general ถูกกันด้วย candidate margin | complete general route และออกจาก pending price | TH/EN ใช้ general model ได้; ไม่รับรองความถูกต้องของคำถามทั่วไปทุกเรื่อง |
| General EN มีเนื้อหาแล้วแต่ rejected | provider จบที่ token limit และยังมีท้ายประโยคไม่จบ | รับได้เฉพาะ prefix ประโยคสมบูรณ์ตาม concise contract | ไม่รับ fragment; ไม่ใช้วิธีนี้ตัดรายการหรือกติกาฉบับเต็ม |
| เปิดชุดแก้แต่ยังเจอคำตอบเดิม | ตัวเปิดใช้บอทชื่อเดียวกันที่ 8090 โดยไม่ตรวจ release/root | health installation ID + version และเลือกพอร์ตว่าง | ชุดสุดท้ายเปิด 8096; reuse instance เดิมผ่าน |

### คะแนนไม่ได้แปลว่าคำตอบถูก 98%

คำตอบราคาใหม่แสดง route confidence 0.98 เป็นค่าของเส้นทาง deterministic ที่พบเงื่อนไขชัด ไม่ใช่ผลประเมินความถูกต้องของราคา และไม่ใช่ความน่าจะเป็นจากโมเดล ต้องตรวจ target/group/coverage/source แยกกัน

การเลือกบริการด้วยโมเดลให้ผล JSON และบันทึก provenance หลังผ่าน schema ไม่อนุญาตให้โมเดลสร้างตัวเลขราคาเอง คะแนนของคำถามในภาพเก่าที่ไม่มี trace ของคำขอนั้นยังยืนยันย้อนหลังไม่ได้ จึงไม่สร้างคะแนนใหม่มาอ้างเป็นคะแนนเดิม

## 2. โค้ดและสถานะข้อมูล

แก้ source ใน `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data` หลังได้รับสิทธิ์ผ่านระบบแล้ว สถานะก่อนเริ่มไม่มี Git changes ในส่วนที่ตรวจ ไม่มี reset/commit/ลบไฟล์เดิม

เพิ่มโมดูล:

- [conversation_plan.py](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/app/session/conversation_plan.py): งานราคา ช่องที่ขาด บริการ กลุ่ม scope และเงื่อนไขราย target
- [conversation_store.py](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/app/session/conversation_store.py): parent session, revision, retry และ delivery
- [conversation_fee.py](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/app/pipeline/conversation_fee.py): render ราคาและ completeness/temporal metadata
- [dialogue_choice.py](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/app/pipeline/dialogue_choice.py): bounded model สำหรับเลือกบริการ
- [conversation_rules.py](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/app/pipeline/conversation_rules.py): full sections, manifest, hash และ coverage ledger
- [test_conversation_flow_r38.py](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/tests/test_conversation_flow_r38.py): ชุด functional ที่รันจาก repository ได้

ปรับ resolver, pipeline, API/supervisor, decision metadata, frontend retry/ack, general answer contract, log output location และ launcher/builder รวม 15 ไฟล์เดิม มีไฟล์ใหม่ 6 ไฟล์ รายละเอียดและ hash ใน `after_manifest.json`; สำเนาก่อนแก้ใน `before/` และ `before_manifest.json`

ราคายังอ่านข้อมูลเดิม ตารางศูนย์/เจ้าของและไฟล์กติกา/ภาษาอังกฤษเดิมไม่ได้แก้ในรอบนี้ ผลทดสอบและ debug logs อยู่โฟลเดอร์ใหม่ ช่วงต้นมี performance logs สองไฟล์ใหม่ในตำแหน่ง source เดิมก่อนเพิ่ม override; เป็นชื่อ run ใหม่ ไม่ทับ log เก่า

## 3. วงรอบทดสอบ → วิเคราะห์ → แก้

| รอบ | พบ | แก้และตรวจซ้ำ |
|---|---|---|
| Functional แรก | all phrase ผิดบริการ, รูปคำตอบ PC/หน่วยไม่ตรง smoke เก่า, group/negation และหลาย task ต้องรักษา | จัดลำดับ all/filter, duration/capacity, outcome ราย task; 21 methods ผ่าน |
| เว็บ source 8093 | ผ่าน 25/28 checks; ต่อกติกา TH/EN ไม่ได้ และ general EN ไม่ผ่าน token contract | แก้ rendered metadata anchor/ack ordering และ complete sentence contract |
| เว็บ source 8094 | 28/28 checks จาก 32 requests ผ่าน | โมเดลจริงเลือก “the desktop station please” เป็น PC; ต่อหน้า/negative group/general TH/EN ผ่าน |
| แพ็กเกจ r38.2 8095 | 30/30 checks จาก 36 requests ผ่าน รวม Auto/retry | พบความเสี่ยง launcher เปิดชุดเก่า จึงแก้ identity check เพิ่ม |
| แพ็กเกจสุดท้าย r38.3 8096 | 8/8 release checks จาก 12 requests ผ่าน | เริ่ม background ได้, ไม่ reuse r37 ที่ 8090, เปิดซ้ำ reuse r38.3 เดิม; ตรวจเว็บและ ZIP |

จำนวน checks กับ requests ต่างกัน: หนึ่ง check อาจใช้หลาย turn และ request conflict ที่คาดไว้เป็นผลผ่านเมื่อได้ HTTP 409 ตามสัญญา ไม่ได้นับจำนวน HTTP 200 เป็น accuracy

## 4. ผลทดสอบที่ยืนยันอัตโนมัติ

### 4.1 ชุดใหม่

21 test methods ผ่าน มีหลาย subcases และ recorded outputs 75 รายการในชุดที่เก็บ: 47 pipeline answers และ 28 หน้ากติกา นี่เป็นชุดตรวจแบบมี expected values ไม่ใช่ 75 คำถามสุ่มอิสระ

ครอบคลุมคำเลือกบริการหลายสำนวน, all, group filters, negation/correction, per-target duration, capacity, topic shifts, legacy metadata, schema rejection, task partial result, temporal expiry, revision/TTL/session isolation, model schema/deadline และกติกา full/summary/release change/uncertain delivery

Manifest กติกาที่ตรวจ: CS2 56 หน่วย, RoV 12, Tekken 8 จำนวน 7, VALORANT 25 หน่วย ตัวเลขคือหน่วยเนื้อหาที่ระบบจัด ไม่ใช่จำนวนมาตราอย่างเป็นทางการ RoV อังกฤษตอบได้ 11 หน่วยและแจ้งหนึ่ง gap

ชุดที่ย้ายเข้ repository รันได้จริงอีกครั้ง 21/21 (ไฟล์ `portable_tests_final.log`) ไม่เพิ่มจำนวนเป็น 42 เคสใหม่

### 4.2 Regression ที่เลือก

| ชุด | ผล |
|---|---:|
| competition session context r35 | 18/18 |
| competition reliability r31 | 16/16 |
| competition recorded year r32 | 5/5 |
| r30 closed query boundaries | 10/10 |
| r30 competition and ingress | 7/7 |
| P0 calendar/booking reconciliation | 11/11 |
| live booking typo fixture | 3/3 |
| **รวม unittest เดิมที่เลือก** | **70/70** |
| booking/price regression smoke | 4 checks ผ่าน |
| PC service fee smoke | 5 checks ผ่านหลังปรับ format/หน่วย |

ไม่ได้รัน Ground Truth/noise corpus ทั้งหมดของโปรเจกต์ใหม่ในรอบนี้ ข้อสรุปจำกัดตามชุดข้างบน

### 4.3 Smoke ที่ยังไม่ผ่าน: เปรียบเทียบ baseline แล้ว

1. `smoke_test_decision_artifact`: คาดว่า “ROV คือเกมอะไร” ต้องผ่าน repair และมี `repair_attempted=True`; เส้นทางปัจจุบันตอบตรงโดยไม่ repair การคาด flag นี้ล้มเหมือน source ก่อนแก้ (`baseline_decision.log`) ไม่ควรเพิ่ม repair ปลอมเพียงให้ test ผ่าน
2. `smoke_test_availability_policy_regressions`: คาดว่าชื่อ Call of Duty กว้าง ๆ จะไปเลือกบริการ แต่ข้อมูลมีหลาย edition และระบบถาม edition ก่อน ล้มเหมือน baseline (`baseline_availability.log`) ต้องทบทวน expected behavior ก่อนแก้ oracle

คงไฟล์ tests/oracles เดิมไว้ รายงาน fail ทั้งสอง ไม่กล่าวว่าทุก test ของโปรเจกต์ผ่าน

ระหว่างเก็บหลักฐาน final มีหนึ่งคำสั่งเรียก PC smoke ผิดตำแหน่ง `tools/` จึงไม่พบไฟล์ เก็บ error ไว้ใน `pc_service_fee_final.log` แล้วรันจาก `tests/` ถูกต้อง ผลอยู่ `pc_service_fee_final_correct_path.log` ไม่จัด error การเรียกไฟล์นี้เป็นคำตอบ chatbot ผิด

### 4.4 เว็บ โมเดล และตัวเปิด

- `http_summary_8095_213224.json`: 30/30 checks, 36 requests, raw requests/responses เก็บใน JSONL
- `final_package_summary_221253.json`: 8/8 checks, 12 requests บน r38.3
- `launcher_verification_r38_3.json`: version/root identity ตรงชุดใหม่ และ started_at ไม่เปลี่ยนเมื่อเปิดซ้ำ; r37.2 ที่ 8090 ยังเดิม
- source 8094 ใช้ worker recycle ขณะทดสอบ; บริบทคำตอบต่อยังอยู่ใน parent แต่ไม่ได้บังคับ crash/hang จริงทุกจังหวะ
- เวลาบนเครื่องนี้เมื่อโมเดลพร้อม: price follow-up โดยมากประมาณ 0.02–0.19 วินาที; คำเลือกบริการผ่านโมเดลที่ตรวจประมาณ 0.39 วินาที; general ในรอบ r38.2 ประมาณ 2.27–2.60 วินาที รอบ cold ก่อนหน้าบางคำถามใช้ 4–5 วินาที ไม่ใช่ SLA
- health/API ผ่านเป็นหลักฐานระบบพร้อมและสัญญาการส่งผ่านเท่านั้น สถานะว่าง/ถูกจองถูกต้องรอบนี้ยืนยันจาก fixtures ที่ระบุข้างบน ยังไม่ได้เทียบ WordPress จริงกับข้อมูลเจ้าหน้าที่

ภาพผลจริง:

![เว็บ r38.3 ตอบราคา PC ตามบริบทบุคคลภายนอก](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/conversation_reliability_implementation_20261005/WEB_R38_3_VERIFIED.png)

## 5. เก็บหลักฐานและแพ็กเกจ

- [โฟลเดอร์ r38.3](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/conversation_reliability_implementation_20261005/release_r38_3/PSU_Esports_Chatbot_Local)
- [ตัวเปิดเบื้องหลัง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/conversation_reliability_implementation_20261005/release_r38_3/PSU_Esports_Chatbot_Local/Open-PSU-Esports-Background.cmd)
- [ZIP r38.3](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/conversation_reliability_implementation_20261005/PSU_Esports_Chatbot_r38_3.zip)
- [ผลตรวจ ZIP](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/conversation_reliability_implementation_20261005/archive_verification.json)

ZIP ขนาด 7,298,673 bytes ประมาณ 6.96 MiB มี 661 entries; CRC ผ่าน เทียบ hash app/web ที่เปลี่ยน 17 ไฟล์กับ source ผ่าน ไม่มี logs/test results/cache หรือโมเดลใน ZIP

SHA256: `ed570d35e9ee9cb1b301e420462f3a15e5bf9565e751cf75ca992de03c6c917d`

โฟลเดอร์ที่ทดสอบมี log ของรอบทดสอบอยู่เพื่อรักษาหลักฐาน ส่วน ZIP ตัด log เหล่านั้นออก ชุด Ready/WithModels เดิมไม่ได้ปรับรุ่น หากยังเปิดโฟลเดอร์เดิมจะยังใช้ r37

## 6. วิธีลองใช้

เครื่องนี้เปิด [เว็บ 8096](http://127.0.0.1:8096/) ได้ทันที เพราะเริ่ม r38.3 ไว้แล้ว หลังหยุด/เปิดเครื่องใหม่ ให้เปิด `Open-PSU-Esports-Background.cmd` ในโฟลเดอร์ r38.3 ตัวเปิดค้นหาชุดนี้ก่อนเลือกพอร์ตว่าง ไม่จำเป็นว่าพอร์ตครั้งถัดไปจะเป็น 8096

ลองตามลำดับ:

1. “ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก” → “PC” → “แล้ว VR ล่ะ”
2. เริ่มแชทใหม่ → คำถามแรกเดิม → “ทั้งหมด” หรือ “ทุกเครื่องเลย”
3. “กติกาการแข่งขัน CS2” → “ขอรายละเอียดทั้งหมด” → “ต่อ”
4. ภาษาอังกฤษ: “Service prices for external users” → “the desktop station please” หรือ “all of them”
5. “ไก่กับไข่อะไรเกิดก่อนกัน” ควรตอบคำถามทั่วไป ไม่ถามเลือกหมวดของศูนย์

แพ็กเกจนี้ใช้ Python/Ollama/โมเดลที่มีในเครื่องอยู่แล้ว **ไม่ใช่ชุด bundled models สำหรับส่งให้เครื่องใหม่เปิดได้ทันที** เครื่องอื่นต้องติดตั้ง dependencies ตาม README/Setup-Local-Models ก่อน ไม่มีการดาวน์โหลดโมเดลใหม่ในรอบนี้

หยุดเว็บทดสอบที่ผมเปิดไว้ 8093–8095 แล้ว คง r38.3 สำหรับลองใช้และไม่หยุดชุดเดิมของผู้ใช้ 8090–8092

## 7. สิ่งที่ยังต้องยืนยันหรือพัฒนาต่อ

### 7.1 คำถามเฉพาะที่ต้องถามเจ้าของ/ผู้จัด

1. **ราคา:** อัตราในภาพที่มีช่วงสิ้นสุด 31 มีนาคม 2026 ยังใช้หลังวันนั้นหรือไม่? ถ้าใช้/เปลี่ยน ขออัตราแต่ละบริการและกลุ่มผู้ใช้ พร้อมวันเริ่ม/สิ้นสุดที่ประกาศจริง ราคา PC ที่ปรับ 27 กรกฎาคม 2026 ยังใช้ปัจจุบันหรือไม่?
2. **RoV:** ขอประโยคเต็มของเนื้อหาบทลงโทษใน `competition_rules_rov_blueket_2025_men_s08_c01` โดยเฉพาะข้อความที่จบ “…ออกจาก” และบรรทัด 6.1.5 ที่ไม่สมบูรณ์ เพื่อแปลอังกฤษโดยไม่เดาเงื่อนไขลงโทษ
3. **Tekken:** เมื่อข้อความเรื่อง pause/หยุดเกมในกติกาต้นฉบับขัดกัน กรณีใดอนุญาต pause และกรณีใดได้รับบทลงโทษ? ให้ผู้จัดชี้ข้อที่ใช้จริงและ exception ก่อนแก้ source

### 7.2 สิ่งที่ทำต่อเองได้โดยไม่รอเจ้าของ

1. ทดสอบ fault ที่ขาดอย่างเจาะจง: worker hang/crash, input rejected, task timeout จริง, network ตัดระหว่างส่ง และข้ามเที่ยงคืน ไม่รัน suite เดิมซ้ำเพื่อเพิ่มยอด
2. เพิ่มชุดคำถามใหม่ที่ยังไม่ใช้พัฒนา โดยเน้นคำถามทั่วไปที่มีคำว่า PC/VR, scope สองมิติ และ typo หลายตำแหน่ง
3. ทบทวน smoke expectations สองรายการโดยคง baseline evidence แล้วปรับ oracle เมื่อกำหนดพฤติกรรมที่ถูกต้องชัด
4. ขยาย typed plan/coverage ไปยังหลายหมวดและการเปรียบเทียบ live snapshots ระบบรอบนี้ไม่ได้แทน planner ทุกหมวด
5. ออกแบบ persistence หากต้องคงบริบทข้าม restart/เครื่อง ความจำปัจจุบัน TTL 30 นาทีอยู่ใน parent process
6. เมื่อมีข้อมูลจองจริงที่รู้ผล จับคู่ช่วงเวลา/อุปกรณ์กับ output และ trace เพื่อวัด status accuracy แยกจาก API connectivity

ยังไม่มี human/owner review ยืนยันคำตอบทุกหมวดหรือทุกภาษา ความสำเร็จอัตโนมัติยืนยันเฉพาะ assertions และ source versions ที่เก็บในรอบนี้
