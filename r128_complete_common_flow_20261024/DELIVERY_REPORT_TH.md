# R128 — ผลพัฒนาและตรวจรับ

## สถานะส่งมอบ

ทำ implementation ครบ 14 กลุ่มสาเหตุที่ตรวจใน R127 และตรวจข้อต่อ C01–C14 แล้ว แชท candidate ใช้ source กลางของตัวเองและ live provider จริง หน้า owner เพิ่ม/แก้ข้อมูลผูก SQLite เดียวกัน การเพิ่ม/แก้/ถอนข้อมูลทดสอบตรวจในฐานแยก

คำว่า “ครบ” เป็นขอบเขตรายการพัฒนานี้ ไม่ใช่ความถูกต้องภาษาธรรมชาติ 100% หรือ Full Test 20,554 requests รอบใหม่ ผลรวมนี้ไม่มีคะแนน accuracy ทั้งระบบ

## ผลรอบโค้ดเดียวกัน

| ชุด | จำนวน HTTP requests | มัธยฐาน | HTTP errors |
|---|---:|---:|---:|
| คำถามเดิม R126/R127 | 34 | 0.432 วินาที | 0 |
| บทสนทนาเดิม 8 ชุด | 19 turns | 0.462 วินาที | 0 |
| บทสนทนาเพิ่มเรื่องจำนวนคน/เหมา/live/เปลี่ยนเรื่อง | 9 turns | 0.437 วินาที | 0 |
| คำถาม retained อีกชุด | 61 | 0.482 วินาที | 0 |

รวม 123 HTTP requests; มีคำถามข้อความซ้ำระหว่างชุด ไม่เรียกทั้งหมดว่า unique questions ชุดนี้เลือกเพื่อตรวจปัญหา ไม่ใช่ตัวอย่างสุ่มของ Full Test

คำถามเดี่ยวชุดเดียวกัน R125 ที่เก็บไว้มีมัธยฐาน 20.703 วินาที ส่วน R128 0.432 วินาที ลดประมาณ 97.9% ในตัวอย่างนี้ Legacy ที่เก็บไว้ 0.684 วินาที เปรียบเทียบระบบทั้งชุดและคนละเวลา ไม่ใช่ causal effect ของ Flow ล้วน ๆ: backend protocol, cache/warmup และ profile แตกต่างกัน และ live ปัจจุบันไม่ใช่ ground truth ของวันเก่า

R128 single p95 = 2.025 วินาที; max = 3.432 วินาที รวม cold first request จึงไม่อ้างว่าทุกคำถามตอบต่ำกว่า 1 วินาที

รอบนี้เปิดสิทธิ์ใช้ LLM แต่ไม่บังคับเรียกทุกข้อ TIMINGS ของ API ตรวจพบ model HTTP attempts 0 ครั้ง และ model transport failures 0 ครั้ง การที่โจทย์ในชุดนี้อ่านแบบ native ได้มากไม่ได้พิสูจน์ว่าโมเดลเข้าใจสำนวนใหม่ทั้งหมด คุณภาพโมเดลกับการเชื่อมต่อโมเดลเป็นคนละเรื่อง; actual model identity/input/token tests แยกไว้ใน MODEL_VERIFICATION.json

## สิ่งที่แก้ครบตาม R127

| ลำดับ | ปัญหา | สิ่งที่ใช้จริง | หลักฐานตรวจรับ |
|---|---|---|---|
| 1 | history เกมไม่ถึง reader | resolver ก่อนทุกเส้นทาง | เกม → โซน → R2 ผ่าน HTTP session จริง |
| 2 | active slots หลุด | ผูกบริการ กลุ่ม เวลา จำนวนคน ช่วงเหมา และ live window | 70 → 140 → PS5 300; กลุ่มรวม 280 → 420 → PS5 900 |
| 3 | เกมคืออะไรเข้าอุปกรณ์ | game entity definition precedence | Beat Saber/Tekken เป็นคำอธิบายเกม |
| 4 | PC ถูกชื่อ PS5 ที่ยาวกว่าตัด | ตัด longest alias เฉพาะช่วงทับกัน | รายการ PC + PS5 อยู่ครบ |
| 5 | ตรวจ subset แล้วอ้างครบ | explicit-target/action obligations | fault injection ลบ PC แต่เหลือ PS5 refs ถูกต้องต้องตรวจไม่ผ่าน |
| 6 | FAQ เปลี่ยนสำนวนไม่เจอ | canonical source policy frames | นั่งดูเพื่อน/นำขวดน้ำ/เมาส์ส่วนตัว |
| 7 | intent ถูกแต่ reader เดาใหม่ผิด | canonical_operation ถึง policy reader | ขั้นตอนเริ่มเข้าเล่น/จอง/ยกเลิก |
| 8 | heavy attack เลือก L2 | source action ก่อน bounded selector | ตีแรง → R2 และ full controls table |
| 9 | กลุ่ม/alias/จำนวนคนคิดผิด | non-overlap alias + per-audience counts + ตรวจหน่วย/อัตราเทียบเท่า | mixed billing และ short Thai alias negative checks |
| 10 | บทลงโทษตอบไม่ครบ | source clause family + scoped dependencies | VALORANT ทั้ง 5 ประเภท; CS2 settings clause เต็ม |
| 11 | เดือนอังกฤษ/เลขคำ/วันหน้า | deterministic date resolver + pending month + แยก clock range | October 26 / อีกสามวัน / วันจันทร์หน้า / วันพร้อม time range |
| 12 | ขั้นตอนซ้ำ | canonical equivalent procedure โดยรักษา source IDs | ขั้นตอนจองหนึ่งชุด 6 ข้อ; ต่างเงื่อนไขยังเป็น partial |
| 13 | คำตอบอ่านยาก/แหล่ง draft หาย | renderer ตามหมวดและ source descriptors | รายการเกม ตารางปุ่ม ราคาแยกกลุ่ม ขั้นตอนเลขลำดับ |
| 14 | โมเดลผิด input/budget และช้า | resolved input hash, bounded tokens/timeout, interpretation cache | actual model identity/token/input/cache checks และ TIMINGS.jsonl |

## ตรวจ interface และ source behavior

- foundation: all_passed=true, 35 checks — [VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/verification_1792827767465238000/VERIFICATION.json>)
- live: all_passed=true, 19 checks — [VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/live_verification_1792827155145517600/VERIFICATION.json>)
- source: all_passed=true, 19 checks — [VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/source_guard_verification_1792827155510257300/VERIFICATION.json>)
- extended: all_passed=true, 42 checks — [RESULTS.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/extended_1792827108760679800/RESULTS.json>)
- model: all_passed=true, 7 checks — [MODEL_VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/MODEL_VERIFICATION.json>)
- owner: all_passed=true, 4 checks — [OWNER_VERIFICATION.json](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/OWNER_VERIFICATION.json>)

Foundation รวม replay annotations เดิม 289 รายการ, planner output เดิม 30 และ API proposal 10 โดยไม่เรียกโมเดลใหม่ Live fixtures 15 กรณีตรวจข้อมูลสด/เก่า/อนาคต/wrong-date/provider ล้ม/status mapping หาย/unknown resource และช่วงต่อเนื่อง Fixtures ไม่ใช่สถานะจองจริง

ตรวจ model base revision และ adapter SHA เดิม, num_predict=1 ถูกเคารพ, effective input hash ตรง, และ repeated interpretation ไม่ generate เพิ่ม ไม่มีการฝึกน้ำหนักใหม่ครั้งนี้

ตรวจ owner API แบบ authenticated read-only: registry 24 kinds, list heads 848 รายการ, ฐานตรงกับแชท และ hash DB ก่อน–หลังไม่เปลี่ยน ฐานที่แชทอ่านมี 824 active records และ 24 withdrawn records ไม่ใช่ข้อมูลหายจากการคัดลอก

## ข้อมูลและขอบเขตที่ยังต้องระวัง

1. ฐานจริงยังไม่มี game_mode records ที่ยืนยันจำนวนผู้เล่นแยกเกม/โหมด จึงตอบรายชื่อเกมเล่นพร้อมกัน 4 คนจากความจุบริการไม่ได้ ตัวอ่านรองรับแล้วและพิสูจน์ด้วย record ที่ save ในฐานทดสอบ แต่ไม่ใส่ข้อเท็จจริงเกมที่เดาเองลงฐานจริง
2. บาง control_set เป็นแหล่งรองหรือ partial official ยังไม่ตรวจ preset/เวอร์ชันเครื่องศูนย์ครบ จึงไม่ลบคำเตือนเพื่อให้ดูเหมือนสมบูรณ์
3. ชื่อเกมคนละ edition เช่น The Last of Us Part II กับ Part II Remastered ไม่ถือว่าเป็น record เดียวกันโดยอัตโนมัติ ความสัมพันธ์บริการที่ยังไม่มีต้องยืนยันก่อน
4. นโยบายบาง intent มีข้อความหลายฉบับ เช่นเอกสารเช็กอิน ไม่มี superseding authority ที่ครบ จึงแสดง partial พร้อมแหล่งแต่ละฉบับ บางคู่เป็นข้อความใกล้เคียงกันมาก การแสดง conflict จึงยังค่อนข้างอนุรักษ์นิยม
5. ราคาอ้างการยืนยันของเจ้าของ ณ 20 ต.ค. 2569 แต่ไม่สร้าง effective interval ใหม่เอง และไม่รับรองปีอนาคตที่ไม่อยู่ในหลักฐาน
6. ตารางช่วงเล่นที่ยืนยันใช้แทน open_periods ที่ขัดแย้ง แต่ไม่เท่ากับเวลาเข้าอาคาร และไม่พิสูจน์เครื่องว่างจริง
7. C14 อ่านประกาศ/FAQ ที่มีได้ แต่ไม่ได้เพิ่ม feed ข่าวล่าสุดทั้งหมดมาเอง
8. นโยบาย capture ในเกมไม่อนุญาตให้สรุปสิทธิ์ถ่ายสถานที่/บุคคล รุ่นนี้คืน source scope พร้อม partial แทนคำตอบสิทธิ์แบบเหมารวม
9. ยังมี compatibility typed adapters และ bounded model interpretation ไม่ได้เปลี่ยนทุกอย่างเป็น IR architecture ใหม่ทั้งหมด ตัว artifact จึงยังคง flag full_r123_architecture_implemented=false ตามความจริง
10. สำนวนใหม่/เจตนาที่นอกชุดตรวจยังพลาดได้ การเพิ่ม content ไม่ทำให้ operation ธุรกิจชนิดใหม่ถูกสร้างขึ้นเองทุกแบบ

ทั้งหมดข้างต้นแยกจาก bug ที่แก้แล้ว ไม่ใช้ความขาด source เป็นข้ออ้างให้ reader ตอบผิด และไม่ใช้ citation ผ่านเป็นคะแนนความเข้าใจ

## การคงหลักฐานเดิม

- R125 source freeze: 1145 files unchanged
- Legacy original: 1505 files unchanged
- Prior protected parent: 1144 files unchanged
- candidate common.sqlite ตรง byte/hash กับ R125, approval changes = 0
- รอบตรวจรับสุดท้าย application/UI 426 files unchanged ขณะทดสอบ
- candidate ยังไม่ติดตั้งทับ R78; เปลี่ยนเฉพาะ local preview เมื่อเปิดใช้ R128

## ไฟล์ส่งมอบ

- [สาเหตุที่พบระหว่างพัฒนาและการแก้ข้อต่อ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/DEVELOPMENT_REVIEW_TH.md>)
- [Flow ทั้งระบบและวิธีเพิ่มข้อมูล](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/FULL_FLOW_TH.md>)
- [คำตอบจริงเต็มทุก turn](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/ALL_RESPONSES_TH.md>)
- [ผลตรวจแบบ machine-readable](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/EVIDENCE.json>)
- [เริ่มแชท R128](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/Start-R128.cmd>)
- [เปิดหน้าเพิ่ม/แก้ข้อมูล](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/Open-Owner-Content.cmd>)

เปิดแชทที่ http://127.0.0.1:12422/ หลัง activation สำเร็จใน ACTIVATION.json หากหน้าเดิมยังค้างให้ refresh ใหม่ ชุดนี้เป็น draft preview สำหรับตรวจและพัฒนาต่อ การส่งมอบ published production ยังต้องผ่าน review/publish ของเนื้อหาจริงตามระบบเดิม

## ตรวจหน้าจอหลังเปิดใช้

ตรวจหน้าเว็บจริงว่าเป็น R128 ตารางปุ่มเป็นตาราง HTML และแถบหลักฐานรักษาเลขอ้างอิง `[S1–S19]` โดยไม่เผย path ภายใน ตรวจ activation เพิ่ม 11 ข้อผ่านแล้ว (อยู่นอกจำนวน 123 requests ของชุดหลัก)

![ตัวอย่างหน้าแชท R128](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r128_complete_common_flow_20261024/UI_R128.png>)
