# R64 Full test: format เดิมและ format กลาง (ไทย/อังกฤษ)
อัปเดต: 2026-10-14T19:34:19.193068+07:00
สถานะ: **ครบทั้งสี่แขนทดสอบ**

## ขอบเขตและวิธีทดสอบ

- 20,554 คำขอไม่ซ้ำ จากชุดเดิมทั้งหมดที่ inventory อ่านได้; 55,811 เกณฑ์ตรวจต่อ format ต่อแขนทดสอบ รวม clean/noisy และชุดที่ใช้คำถามซ้ำกันแต่มีเกณฑ์ต่างกัน
- แยก LLM ปิด และ LLM/embedding เปิด; รูปแบบคำถามไทย/อังกฤษตาม corpus เดิม ไม่มีการลดเกณฑ์เพื่อให้ผ่าน
- format เดิมใช้ backup ฐานจริง; format กลางใช้ R63 draft ผ่าน view อ่านอย่างเดียว (582 รายการ) ไม่มีการ approve/publish และไม่ได้สลับระบบผู้ใช้
- Booking ในการกวาด corpus จำลอง API ไม่พร้อมใช้งาน; การว่าง/ถูกจองตรวจผ่าน fixture ของชุด native เท่านั้น ไม่มีการเก็บ ground truth จากการจองลูกค้าจริงเพิ่ม
- common matcher ใน evaluator ใช้ upper bounds ของ SequenceMatcher, caching และ multiset upper bound ที่ไม่เปลี่ยน candidate ที่ถึง threshold .88; ตรวจ equivalence 186 query/600 pair แล้ว ผลเวลาจากแขนนี้ใช้รับรอง production latency ไม่ได้
- model enabled เป็นการอนุญาตให้เรียกโมเดล ไม่ได้แปลว่าทุกคำถามเรียก LLM หรือทุกการเรียกสำเร็จ; ต้องอ่าน trace ของแต่ละเคส

## Coverage ที่รันได้จริง

| แขนทดสอบ | คำขอที่มีผล / 20,554 | เกณฑ์ผ่าน / เกณฑ์ที่รัน | ครบหรือยัง |
|---|---:|---:|---|
| legacy_offline | 20,554 / 20,554 | 42,410 / 55,811 | ครบ |
| common_offline | 20,554 / 20,554 | 16,998 / 55,811 | ครบ |
| legacy_llm | 20,554 / 20,554 | 42,601 / 55,811 | ครบ |
| common_llm | 20,554 / 20,554 | 12,517 / 55,811 | ครบ |

คะแนนแต่ละแขนด้านบนยังเทียบเปอร์เซ็นต์ข้าม format โดยตรงไม่ได้ถ้ารันคนละจำนวน/คนละ subset ให้ใช้ paired comparison ของคำถามเดียวกันด้านล่าง และแยก protocol จากเนื้อหา

## เปรียบเทียบเฉพาะคำถามเดียวกัน

| แขน | คำขอคู่ | เกณฑ์คู่ | ผ่านทั้งคู่ | เดิมผ่านอย่างเดียว | กลางผ่านอย่างเดียว | ไม่ผ่านทั้งคู่ |
|---|---:|---:|---:|---:|---:|---:|
| offline | 20,554 | 55,811 | 16,927 | 25,483 | 71 | 13,330 |
| llm | 20,554 | 55,811 | 12,394 | 30,207 | 123 | 13,087 |

อ่านผลภาษาไทย/อังกฤษแยกได้ใน `ANALYSIS_LATEST.json` และ `PAIRED_COMPARISON.json` (by_language) ตัวเลข failure bucket เป็นเหตุการณ์หลายสาเหตุต่อเคส ไม่ใช่จำนวนคำถามที่ผิดไม่ซ้ำ

## Native tests ที่จบแล้ว

| รูปแบบ | test functions | failure events | error events |
|---|---:|---:|---:|
| legacy | 899 | 23 | 46 |
| common | 899 | 246 | 9 |

- ไม่คำนวณ passed = 899 - events เพราะ unittest subtest ทำให้หนึ่ง function มีหลายเหตุการณ์ผิดได้
- Legacy missing-reference-fixture errors 4 ข้อได้รับการ copy fixture เดิมเข้าพื้นที่ทดสอบแล้ว rerun 4/4 ผ่าน; ผลก่อนแก้ environment ยังเก็บไว้
- PowerShell Booking Dashboard probe 6/6 ผ่าน
- Smoke Python 85 ไฟล์ต่อ format: legacy ผ่าน 41/84 ที่รันใน wrapper; common ผ่าน 33/84; อีกไฟล์คือ concurrent bilingual API ที่รันผ่าน HTTP แล้วแต่ยังไม่ผ่าน
- Guard 500 เคสต่อรูปแบบ: layout500/500, repeat471/500, historical block-policy500/500; launcher ปัจจุบัน repeat ใช้ warn_and_continue ต้องแยกจากต้นแบบ block

## HTTP และบทสนทนา

- รอบแรกใช้ session ID สั้นกว่าที่ API อนุญาต จึงได้ session ใหม่ทุกครั้ง: ตัวเลข 17/24 และ15/24 รอบนั้น **ไม่ใช่ผลความจำบทสนทนาที่ถูกต้อง**
- รอบ protocol_fixed ที่ถูก sandbox ปฏิเสธ socket10013 คือปัญหาสภาพแวดล้อม ไม่ใช่คำตอบของ chatbot
- รอบ protocol_network ส่ง ID ที่ถูกต้องและ last_seen_response_id เหมือน frontend: legacy22/24; common13/24 เทิร์น (ตรวจ SUMMARY/RESULTS ของรอบนี้เป็นหลัก)
- concurrent smoke 10 คำขอมี client timeout15s ในระหว่างรันชุดใหญ่พร้อมกัน ผลนี้ไม่ใช้สรุปความจุ production หรือเวลาเมื่อเครื่องว่าง และไม่ใช่ข้อพิสูจน์การรั่วภาษา

## ปัญหาจริงที่ยืนยันจากหลักฐานแล้ว / ลำดับแก้

### P0 — retrieval ล้มก่อนตอบ

`app/pipeline/retrieval.py` ใน retrieve_curated ใช้ `ownership_blocked` ที่ไม่ได้กำหนด ใน trace ของ return; native legacy พบ41 error events และ common7 ต้องแก้การกำหนด/ส่ง ownership audit ตาม branch จริง ตรวจกรณีไม่มี ownership block ด้วย ห้ามแค่ปิด exception เพื่อให้ตอบผ่าน

### P0 — common เลือกหัวข้อย่อยและประกอบกฎการแข่งขันยังไม่ตรงคำถาม

คำถาม dispute/penalty/match format ถูกตอบภาพรวม/ทุก section หรือถามเลือกหัวข้อเพิ่ม ทั้งที่ source มี clause ที่ต้องใช้ บางคำตอบรวม brightness ที่ไม่ได้ถาม ปัญหาอยู่ที่ entity → field/facet → related records → projection ไม่ใช่แค่ข้อมูลหาย ใช้ clause-level source contract ของเดิมเป็น oracle และ map ข้อกฎใน common ให้เลือก subset/ครบชุดที่ถาม พร้อม source IDs โดยไม่เผย field ภายในที่ไม่ช่วยผู้ใช้

### P1 — English ในข้อมูลย้ายยังไม่ครบ

ตรวจ582 headsพบ791 localized slots ไม่มีภาษาอังกฤษ ได้แก่ game144, policy1, rental_package24, resource14, faq281, competition4, competition_rule208, person75, equipment_model32, closure3, audience1, schedule4 จึงเห็น [Thai source] และข้อความไทยใน English answer นี่เป็นสถานะข้อมูล common ที่ย้าย ไม่ใช่การลบล้างผล English เดิมที่ผู้ใช้ยืนยัน แปลจาก source ที่เก็บไว้พร้อมตรวจตัวเลข เงื่อนไข ปฏิเสธ และชื่อเฉพาะ; ห้ามเติมนโยบายใหม่ระหว่างแปล

### P1 — context / selector / paraphrase ใน common

รอบ HTTP ที่ protocol ถูกแล้ว commonยัง13/24 เทิร์น เทียบเดิม22/24 ต้องตรวจ active task, pending fields, offered options และ source record identity เมื่อพิมพ์แค่ชื่อ/ราคา/ปุ่ม/จอง โดยใช้ response_id และประวัติที่ส่งตาม frontendจริง ไม่เพิ่ม alias แทนการจัดการ state

### P1 — common fuzzy matching ใช้เวลามาก

faulthandler stack จับการไล่ SequenceMatcher ทุก substring/alias นานเกิน12s ได้จริง ชุดทดสอบใช้การคำนวณเทียบเท่าเพื่อกวาด corpusให้จบ แต่ production ยังไม่ได้รับการแก้; หลัง correctness ได้แล้วควรย้าย optimization ที่พิสูจน์แล้ว พร้อม regression และวัดเวลาที่โหลดเท่ากัน

### P2 — เกณฑ์เก่าบางข้อผูกกับข้อความ/route เดิม

commonใช้ route knowledge และ common_answer จึงไม่ผ่าน category/mode เดิมแม้บางเนื้อหาถูก ต้องแสดง strict compatibility score แยกจาก content score ห้ามเปลี่ยน expected เพียงเพราะตัวใหม่ตอบอีกแบบ ตัวเลขราคา ระยะเวลา บุคคล และ source ที่ไม่ตรงยังต้องถือเป็นปัญหาเนื้อหา ตรวจ original source/เจ้าของก่อนจัดเป็น stale expectation

## สิ่งที่ยังไม่ถือว่ายืนยันแล้ว

- ชุด native/oracle ผ่านอัตโนมัติไม่ได้เท่ากับเจ้าของอนุมัติ migration ทั้งชุด; ข้อมูล draft ยังไม่ใช่ข้อมูลที่ประกาศใช้
- วันมีผล ความขัดแย้งของแหล่งข้อมูล และนโยบายที่ source เว้นว่างยังต้องอ้างหลักฐาน/เจ้าของ อย่าเติมให้ผ่าน test
- ผล LLM และ latency ต้องแยก successful model calls, backend failure, client timeout และ input guard; อย่าใช้ API200 แทนความถูกต้องของคำตอบ
- ยังไม่รับรองพร้อม production จน full coverage ครบและแก้ P0/P1 พร้อม rerunเฉพาะส่วนที่เปลี่ยนแล้ว

## ไฟล์หลักฐาน

- INVENTORY.json / JOBS.jsonl — corpus hash, alias, คำถามและ expected เดิม
- *_RESULTS.jsonl[.gz] — answer, decision, trace, grades ของแต่ละเคส (ผลเดิมทุก attempt เก็บไว้)
- ANALYSIS_LATEST.json / PAIRED_COMPARISON.json / FAILURE_SAMPLES_LATEST.json — คะแนนแยกภาษาและตัวอย่าง
- NATIVE_UNIT_ANALYSIS.json / *_test_all.py_temp_fixed.* — unit failuresและ stack
- *_http_protocol_network/RESULTS.jsonl — บทสนทนาที่ส่ง protocol ถูกต้อง
- COMMON_SOURCE_AUDIT.json — localized fields ที่ยังขาด
- PRESERVATION_CHECK.json — hash ของ source และ logical SQLite เพื่อยืนยันการรักษาข้อมูลเดิม
