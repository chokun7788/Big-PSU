# R68 — ตรวจข้อมูลตกหล่นรอบใหม่ และเติม Format กลาง

วันที่ 16 ตุลาคม 2026 — ผลสุดท้ายอยู่ที่ **candidate06.sqlite** และ **DELIVERY_final/candidate.sqlite**

## 1. สรุปสิ่งที่ทำจริง

ตรวจต่อจาก R67 596 รายการ เพิ่มเป็น **602 รายการ** โดย append revision ของ 187 รายการเดิม/ใหม่ในรอบนำเข้าหลัก และมี revision เพิ่มสำหรับสเปก แหล่งอ้างอิง และชื่อแสดงภายหลัง มี field mappings รวม **293 ช่อง** และย้ายชื่อเรียกเกมที่ยังไม่อยู่ในฐานอีก **749 ชื่อ** ไม่ใช่การเพิ่ม 749 เกม ไม่ใช่การสร้าง alias สำหรับคำถามใหม่ 749 ประโยค

แก้ schema/catalog/templates/presentation/query reader ให้ช่องที่เติมอ่านได้จริง จำนวนเกม offered ยัง **42 เกม** และ game-service links **70 รายการ** เหมือน R67 ไม่มีการสร้างเครื่อง/บริการจอง/ราคา/สิทธิ์ออนไลน์ใหม่

**ยังไม่เปลี่ยนเว็บแชทเดิมหรือโปรเจกต์ใน Downloads**: ขอกลุ่มสิทธิ์เขียน app และ data/knowledge/migration_r68_20261016 ผ่าน request_permissions แล้ว ระบบคืน file_system=null จึงไม่พยายามเขียนผ่านวิธีอื่น ข้อมูลนี้ยังเป็นร่าง มี active release ว่างและ approvals 0 ทุก 602 รายการยังติด publication gates เดิม

## 2. ทำไมรอบก่อนดูเหมือนครบ แต่ยังมีข้อมูลตกหล่น

### 2.1 เทียบกับไฟล์ที่ถูกตัดข้อความมาแล้ว

R67 เทียบ our_games_scraped_details.jsonl ซึ่งเก็บคำบรรยายสั้น แต่ data/sources/our_games_raw.jsonl ยังมีข้อความต่อท้าย ตัวอย่าง Animal Crossing ข้อความท้ายเรื่องฤดูกาล/เซอร์ไพรส์ตลอดปีไม่อยู่ในฉบับสั้น รอบนี้พบ **23 จาก 31 รายการ** ที่ข้อความภาษาต้นทางสั้นกว่าไฟล์ดิบ เติมครบแล้ว ส่วนอีก 8 รายการตรงอยู่แล้ว

ตัวตรวจแรกที่เลือกไทยก่อนอังกฤษจะรายงานความต่าง 24 รายการ เพราะสองคำบรรยายต้นฉบับเป็นอังกฤษ จึงแก้ auditor ให้เทียบ locale ของต้นทางก่อนนับ ผลสุดท้าย **31/31 ตรงข้อความฉบับดิบในภาษาต้นทาง** ไม่ตัด ellipsis เพิ่มเอง

ไทย/อังกฤษของฉบับเต็มมีครบ แต่ข้อความอีกภาษาที่เพิ่มเป็น agent translation ยังไม่ได้ owner approve หรือประเมินอิสระทุกประโยค คง source และ revision สั้นเดิมไว้

### 2.2 ชื่อเรียกเกมอยู่ในพจนานุกรมเก่า แต่ไม่อยู่ใน common aliases

พบรายการที่ยังไม่อยู่ 755 ชื่อ ย้าย 749 ชื่อหลังตรวจตัวตนตรงกับเกมเพียงหนึ่งรายการ เว้น 6 ชื่อ ได้แก่ CSGO, CS:GO 2, csgo2, WZ, ลีก, รีสี่ ด้วยเหตุผลต่างกันเรื่อง release เก่าหรือสั้นเกินไป ไม่เปลี่ยนการสะกดใหม่ทุกแบบให้เป็นชื่อจริงอัตโนมัติ

ตรวจ resolution ของทุกชื่อที่เพิ่ม **749/749** และทดสอบชื่อเกมคนละภาค/แพลตฟอร์มมือถือ 19 กรณี ไม่พบ match เพิ่มจากข้อมูลชุดนี้เทียบก่อนเติม นี่เป็นหลักฐานในขอบเขตชุดตรวจ ไม่รับรองว่าไม่มีชื่อกำกวมอื่นในทุกคำถาม

### 2.3 มีข้อมูลอยู่ในข้อความรวม แต่ช่องเฉพาะยังว่าง

Gaming PC มี CPU/RAM/GPU อยู่ใน usage แต่ specifications เดิมแสดงเพียง zone/quantity จึงเพิ่มค่าที่คัดตรงได้ 3 ค่า: Intel Core i5-14400, DDR5 32GB, NVIDIA GeForce RTX 5060 8GB โดยรักษา usage และ specifications เดิม ไม่อ้างว่าไปตรวจเครื่องจริงใหม่

### 2.4 ใช้ field ที่มีความหมายใกล้กันแทนกัน

- ข้อมูล game.zones ของศูนย์ไม่ควรถูกกรอกเป็น supported_platforms ซึ่งหมายถึงแพลตฟอร์มที่เกมรองรับทั่วไป จึงเพิ่ม venue_zone_ids ให้ **36 เกม** จากโซนที่มีอยู่จริง ไม่สร้าง game-service links เพิ่ม
- วันที่ตรวจรายการเครื่อง/เกมเดิมไม่ใช่การตรวจสถานะว่างสด เพิ่ม inventory_verified_on และ inventory_basis ให้ **8 บริการ** ตามวันที่ 2026-07-30 ใน source ไม่ใช้วันที่ย้ายข้อมูลเป็นวันที่ตรวจจริง
- ชื่อหัวข้อ overview chunk ไม่ใช่ชื่อเอกสารทั้งฉบับ แก้ source_title **4 เอกสาร** จาก metadata เอกสาร และเติม division ประเภททีมชายของ RoV เฉพาะรายการที่ระบุจริง

## 3. รายการที่เติม/จัดโครงสร้าง

| กลุ่ม | สิ่งที่ทำ | ขอบเขตที่รักษา |
|---|---|---|
| คำบรรยายเกม | ขยายฉบับเต็ม 23 รายการ; capture timestamp และ scope note 31 รายการ | ไม่ใช่เวอร์ชันปัจจุบัน/DLC/จำนวนคนที่ร้านรองรับ |
| เกมกับโซน | venue_zone_ids 36 เกม | ไม่แทน supported_platforms หรือการติดตั้งปัจจุบัน |
| ชื่อเรียกเกม | 749 ชื่อพร้อม source/locator; เว้น 6 | ไม่รวมคนละภาคหรือคำกำกวมโดยเดา |
| รายการบริการ | วันที่/หลักฐาน 8 บริการ รวม 16 ช่อง | ไม่ใช่สถานะจองสด |
| อุปกรณ์ | device_type 16 รายการ และสเปก PC 3 ค่า | ไม่สร้าง serial unit/จับคู่เครื่องจริง |
| เอกสารการแข่งขัน | source_title 4, division 1 | ไม่เติมวันที่จัดแข่งหรือประกาศฉบับใหม่ |
| หมวดกฎ | facet 104 ข้อจาก canonical classifier ของข้อความเดียวกัน | เป็น metadata ค้นหา ไม่ถือว่าตรวจความครบ/ข้อยกเว้นแล้ว |
| ศูนย์ | description จากคำตอบมหาวิทยาลัย และ timezone จากค่าที่โปรแกรมกำหนด | ไม่เปลี่ยนตารางเวลา |
| สิ่งอำนวยความสะดวก | facility ที่จอดรถและที่นั่งพัก 2 รายการ | ไม่เติมจำนวนที่นั่ง/ที่จอด/สิทธิ์ผู้พิการ |
| ติดต่อ | Facebook 1 รายการเป็น channel/value/purpose/name | ไม่สมมุติเวลาตอบกลับ/เบอร์/อีเมล |
| ขั้นตอน | จองผิดเครื่อง, เปลี่ยนเวลา, แนบสลิปผิด 3 รายการ | แยกขั้นตอนตามคำตอบเดิม ไม่เพิ่มเงื่อนไขคืนเงิน |
| เชื่อมข้อมูลเดิม | related_ids ของ FAQ ที่เป็น claim เดียวกัน 6 รายการ | เก็บคำตอบ FAQ เดิมครบ |
| แหล่งอ้างอิง | คืน URL HTTPS ให้ 153 ช่องใน 66 รายการ | สร้าง source ใหม่ ไม่แก้ immutable source เดิม ไม่ใช้ URL แทน approval |

รายละเอียดทุก mapping: MIGRATION_LINEAGE_final.json; ชื่อเรียกทุกชื่อ: ALIAS_LINEAGE.json; source citation changes: SOURCE_CITATION_REPAIRS.json

## 4. ตรวจ source families อื่น ไม่เอาข้อมูลทดสอบมาปน

- สำรวจโครงสร้างไฟล์ธุรกิจระดับบน 38 JSON/JSONL files ใน curated/rules/sources/calendar/competition_rules พร้อมแฟ้ม canonical และ snapshot inputs **1,402 ไฟล์** ตรวจ hash กับโปรเจกต์จริงอีกครั้ง เปลี่ยน 0 ไฟล์
- คำตอบ user_service_facts มี **18 claims / 36 localized answers** และ service_policy_answers อีก **8 รูปแบบ / 16 localized answers** อยู่ใน common แล้วครบข้อความทั้งสองภาษา จึงไม่สร้าง FAQ ซ้ำเพียงเพราะบางเส้นทางยังเลือกตอบผิด
- ราคาเหมา 24 packages, rates 24, schedules 7, closures 3 และ personnel 25 ยังอยู่ครบ ช่องที่ไม่ทราบยังไม่ถูกกรอกค่าปริยาย
- controls แบบ curated ยัง **43 ชุด / 448 binding rows** ไม่มีการแก้ปุ่มจากการเดา; ตรวจ raw JSON ต้นทาง 43 เอกสาร / 437 rows เพิ่มด้วย การจับ platform label แบบเคร่งพบ 64 ไม่ตรง ก่อนตรวจ source-file/row identity ซ้ำ พบ 60 เป็นแถวเดิมภายใต้ label PlayStation/PS5 ของ curated เหลือ 4 แถวในเอกสารรวม Overcooked ที่คำอธิบาย/ปุ่มไม่ตรงชุดปัจจุบัน เก็บใน RAW_CONTROL_VARIANT_REVIEW.json ไม่ทับ bindings ปัจจุบัน
- competition chunks/curated **104 ข้อ** มีอยู่แล้ว ไม่พบเหตุให้เพิ่มคำตอบสรุป 166 fact cards เป็นกฎใหม่อัตโนมัติ เพราะหลักฐานใน canonical projections ระบุ **129 document_level_only, 28 candidate_review_required, 9 declared_chunk_reference_pending_text_check** ไม่ใช่ 166 verified missing facts
- metadata ของเอกสารการแข่งขันชี้ TXT ภายนอก 4 ไฟล์ แต่ path นั้นไม่พบแล้วในเครื่องรอบนี้ จึงยืนยันความตรงของ 104 chunks กับข้อมูลที่เก็บในโปรเจกต์ได้ ไม่ยืนยันว่าเท่ากับทุกบรรทัดของ TXT ต้นฉบับที่หายไป
- approved_localizations.jsonl มี **0 รายการ** ไม่ได้มีคำแปล owner-approved ตกหล่นจากไฟล์นี้; translation review drafts ไม่ถูกเลื่อนสถานะเป็น approved
- human_review มี **2,521 แถว** โดย human_decision ไม่ได้กรอกทุกแถว ไม่ใช้ AI answers หรือ auto PASS ในแฟ้มนี้เป็น business facts/คำยืนยันจากมนุษย์
- knowledge_inbox มี schema กับ placeholder example ยังไม่ใช่ข้อมูลใหม่ที่เผยแพร่ ไม่เอาตัวอย่างเข้า production knowledge
- general_evidence มีข้อมูลเทคนิคทั่วไป 4 cards (ping/HTTP/TCP/memory) แยกจาก studio policy และผู้ใช้เคยกำหนดขอบเขตเน้นร้านเกม จึงไม่เพิ่มเป็นนโยบาย/ข้อเท็จจริงของศูนย์
- วันหยุด 2026/2027 ไม่ถูกใช้สร้าง closure ของศูนย์อัตโนมัติ; training messages, regex/routing, eval/ground-truth และ vector/projections เป็นไฟล์ทำงานของระบบ ไม่ใช่ข้อมูลใหม่จากเจ้าของ

## 5. ข้อผิดพลาดการเลือกตอบที่แก้ระหว่างทดสอบ

| อาการจริง | ทำไมเกิด | แก้ |
|---|---|---|
| ถาม source_title ของ CS2/VALORANT แล้วตอบไม่พบข้อกฎ | operation rules บังคับเปลี่ยน requested_fields เป็น text แม้ field ที่ขอตรงกับ competition schema | ให้ช่องเอกสารที่ระบุชัดมีสิทธิ์อ่านก่อน clause routing |
| Change a wrongly booked machine steps ไม่ตอบ | booked ถูก live guard จับเป็น occupancy | ตัดเฉพาะ participle ที่บอกว่าจองผิด; ถ้ามี Is PC1 booked at 15:00? อีกส่วนยังส่ง live |
| timezone อังกฤษได้ที่อยู่แทน | FAQ alias location แย่งตัวตนศูนย์ | ให้ explicit center attribute เลือกศูนย์เมื่อ schema/บริบทชัด |
| timezone ไทย OFF ผ่าน แต่ ON ไม่ตอบค่าที่มี | entity LLM selector อยู่ก่อน typed fallback | เลือก singleton center ด้วย field ชัดเจนก่อน semantic entity selection |
| Parking location/Rest seating location เรียก model ทั้งที่มี field | FAQ alias location ถูก strip ทิ้งพร้อม entity names | ไม่นับ bare attribute word เป็น FAQ entity เมื่อมี typed entity ที่ระบุแยกอยู่ |
| ขั้นตอนมีหัวข้อ change_time/ลิงก์ดิบ | category ไม่มีชื่อแสดงภาษาไทย/อังกฤษ | เพิ่ม optional name ใน procedure/contact และกรอกจาก claim เดียวกัน |

เก็บผลเดิม TEST_off01, TEST_final_on และ log ทั้งหมดไว้ ชุด ON ระหว่างทางเคยมี transport failures จาก socket/Ollama ที่ถูกจำกัด จึงไม่กล่าวว่าเป็นความผิดของเนื้อหาหรือเป็น inference ที่ผ่านแล้ว

## 6. ผลตรวจสุดท้าย

| ชุด | OFF | ON flag |
|---|---:|---:|
| ข้อมูลที่เติมใหม่ ไทย/อังกฤษ | 206/206 | 206/206 |
| รักษาพฤติกรรม common เดิมที่เกี่ยวข้อง | 210/210 | 210/210 |

- ตรวจ source/schema/FK/lineage/old revisions/old sources/ข้อมูลที่ต้องคงเดิม/alias/live guard **8634/8634** ผ่าน ตัวเลขนี้เป็น technical assertions ไม่ใช่จำนวนคำถามจากคน
- Owner draft preview function/backward compatibility **7/7** และ follow-ups **6/6 บทสนทนา / 12 เทิร์น**
- ชุด OFF/ON สุดท้ายไม่มี model_audits: การเปิด flag ไม่ได้บังคับให้ทุกคำถามเรียกโมเดล ชุดนี้อ่านข้อมูลได้โดยตรง จึง **ยังไม่ยืนยัน actual LLM transport/inference**
- ไม่รัน legacy หรือ full test 20,554 ซ้ำ ไม่ใช้ผล targeted นี้แทนคะแนน benchmark 503 grades ที่ยังมีปัญหาจาก R67
- การตรวจคำบรรยายตรงครบต้นทางและมีอีกภาษาครบ ไม่เท่ากับพิสูจน์ข้อมูลเกมต้นฉบับถูกทุกประโยค ตัวอย่าง RE4 “สองปี” และ New Super Mario “3 คน*” ติด scope note เฉพาะไว้แล้ว ไม่เลื่อนเป็นข้อเท็จจริงเรื่องจำนวนคนที่ศูนย์อนุญาต
- UI JavaScript และ PowerShell launcher ผ่านการตรวจ syntax; owner preview ตรวจเป็นฟังก์ชัน ยังไม่เปิด HTTP/socket จริงในรอบนี้

## 7. สิ่งที่ตั้งใจยังไม่เติม

1. วันมีผลของ PC rates/ราคาเหมา และจำนวนชั่วโมงของครึ่งวัน/เต็มวัน — source ไม่ระบุ ห้ามตั้ง 4/8 ชั่วโมง
2. เวลาเปิดพื้นที่หลังรอบจองถึง 18:00 กับ bookable ถึง 16:00 — เป็นคนละความหมาย ต้องมีนโยบายชัดก่อนรวมค่า
3. เงื่อนไขกรณีจ่ายแล้วจองผิดวันเทียบการขอเลื่อนแทนคืนเงิน — คำตอบเดิมข้อ 45/46 ต้องแยกสถานการณ์ให้ชัด ไม่เดาว่าอนุญาตทุกกรณี
4. machine/resource IDs ที่ไม่มีใน source, game version/preset/operational status ปัจจุบัน, account/DLC/online access และ accessibility ที่ไม่ได้ยืนยัน
5. completeness/dependencies ของข้อกฎ และ validity ของ rulebook — การย้ายครบ chunks หรือมี facet ไม่พิสูจน์ข้อนี้
6. raw Overcooked รวมสองภาค 4 แถวที่ไม่ตรงปัจจุบัน — ยังไม่เลือกแทนชุดเดิม
7. คำถามที่ผู้ใช้ยังไม่ได้ตอบในชุด 50 ข้อ ไม่คัดลอกคำตอบ AI จาก human_review เพื่อทำให้ดูครบ

คำถามสำหรับเจ้าของแบบเจาะจงยังอยู่ใน OWNER_CONFIRMATION_REQUIRED_R67_TH.md ไม่ถามซ้ำเรื่องสถานะจองสดที่ผู้ใช้ตรวจว่าถูกแล้ว ช่วงพัก 12:00–13:00 หรือ VR 30 นาทีที่ใช้ occupancy หนึ่งชั่วโมง

## 8. ไฟล์ส่งมอบและวิธีใช้

- FLOW_R68_TH.md: ขั้นตอนและการทบทวน 3 รอบ
- FORMAT_GUIDE_R68_TH.md: ช่องใหม่/ตัวอย่างแก้ข้อมูล/ตารางทุกหมวด
- Open-R68-Drafts.cmd: ทดลองร่างพอร์ต 8100 ใช้ runtime r58 ข้างโฟลเดอร์นี้ ยังไม่ใช่ portable package ใหม่
- DELIVERY_final/PLAN.json: แผนติดตั้ง/backup/expected hashes; ต่างจาก actual base 49 code files, เพิ่มจาก R67 14 code files, conflict 0 ณ ตอนตรวจ
- DELIVERY_final/candidate.sqlite และ migration.bundle.json: **602 draft records**, ไม่มี approvals หรือ active release
- FROZEN_CODE_MANIFEST_final.json: hash โค้ดที่ใช้ปิดงาน

ยังไม่ได้นำไฟล์ไปใส่โปรเจกต์จริงเพราะระบบไม่ได้ให้สิทธิ์เขียน Downloads หลังขอแล้ว จึงเก็บชุดที่ตรวจได้และพร้อมนำเข้าหลังได้รับสิทธิ์ไว้ทั้งหมด ไม่อ้างว่าเว็บเดิมใช้ข้อมูลนี้แล้ว
