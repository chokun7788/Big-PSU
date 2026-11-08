# R83 — แก้ selector และทดสอบเฉพาะส่วน

## สถานะ

ติดตั้งใน R78 เดิม พอร์ต 8115 แล้ว LLM ยังเปิดอยู่ เทสใหญ่/full corpus ยังไม่ได้รัน และจะรอคำสั่งใหม่ของผู้ใช้

## สิ่งที่เปลี่ยน

1. ย้าย independent-topic guard เดิมมาคัด candidate ก่อนเรียกโมเดล ไม่ตัดแหล่งจากคะแนนต่ำอย่างเดียว ตัวอย่างคำถามไทยเดิมลดจาก 8 เหลือ 3 รายการ
2. เฉพาะขั้นที่ยังต้องถามยืนยัน: ให้ LLM เสนอ topic indices แบบสั้น ไม่ให้สร้าง quote/binding ที่ยังไม่จำเป็น ไม่สร้างคำตอบข้อเท็จจริงจากการเสนอหัวข้อ
3. กรณีโมเดลเลือก profile หรือเลือก profile ปนรายการทั่วไป จะถามยืนยันหัวข้อด้วย state/fingerprint เดิมก่อนอ่าน source revision ปัจจุบัน
4. คง strict quote/binding validator เดิมสำหรับผู้เรียกที่ยังต้องใช้ ไม่ยอมรับคำที่ไม่มีใน input และคง HTTP cap 6 วินาที/context 3072; ลด output cap ของ topic proposal จาก 420 เหลือ 70 tokens
5. หาก named FAQ ตอบไม่ครอบคลุมและ validation ปฏิเสธด้วย unresolved_query_clause ให้กู้กลับไปถามยืนยัน declared topic ที่เข้าเงื่อนไข โดยเก็บ rejected candidate ไว้และไม่แสดง facts ที่ถูกปฏิเสธ

## เหตุของสองปัญหาเดิม

- ไทย: candidate ที่ไม่ผ่านเงื่อนไขรับเดิมยังถูกส่งเข้า prompt และต้องสร้าง binding ยาว ก่อนถามผู้ใช้ยืนยันอยู่ดี ทำให้คำขอเดิมรอ Ollama ถึง deadline
- อังกฤษ: model เลือก source ขั้นตอนสลิปถูก แต่คัด task_span ไม่ผ่าน exact-input และใส่ subject span “slip” ซึ่งไม่มีในคำถาม การคืน JSON ได้จึงไม่ได้แปลว่า binding ใช้ได้
- การแก้ลดงานโมเดลในขั้นเสนอหัวข้อ คงการตรวจ source และการยืนยัน ไม่เพิ่ม alias ของคำถามตัวอย่าง และไม่เปลี่ยนนโยบาย

## การทดสอบและ loop

| ชุด | ผล | วิธี |
|---|---:|---|
| selector/protocol/recovery guards | 31/31 | controlled outputs, strict validator และ trusted state |
| ยืนยันพร้อมเงื่อนไขเพิ่มเติม | 41/41 | fixtures แยก ตรวจขอบเขต/ownership/competition/revision |
| ปฏิเสธแล้วเปลี่ยนเรื่อง/ถามต่อ | 34/34 | fixtures แยกและ handler ในหน่วยความจำ |
| candidate กับ LLM จริง รอบสุดท้าย | 24/24 ข้อความ | real dispatcher, candidate overlay, ไม่ใช่ TCP ของเว็บ |
| ติดตั้งแล้วผ่านเว็บจริง | 24/24 ข้อความ | session จริงแยก, HTTP /api/chat, LLM ON |

ชุดตรวจภายใน 106 ข้อไม่ใช่ 106 คำถามไม่ซ้ำ ไม่รวมเป็นคะแนนความแม่นยำของ LLM; เว็บจริงแยกไทย 10/10 อังกฤษ 14/14

### รอบที่พบปัญหาและเก็บไว้

- live_candidate_1: Ollama ไม่เปิดรับการเชื่อมต่อ 10061 ยังไม่ส่งคำถาม
- live_candidate_2: เปิด Ollama เบื้องหลังได้ แต่ GPU discovery ใช้ประมาณ 45.8 วินาที เกินเวลา readiness 30 วินาทีของตัวรัน ปรับเฉพาะเวลาเตรียมบริการเป็น 90 วินาที ไม่เปลี่ยนเวลาตอบคำถาม
- live_candidate_3: 12 เทิร์นแรกผ่าน จากนั้น harness สมมุติว่า state ต้องเป็น dict แล้วหยุดเมื่อได้ None แก้ harness ให้เก็บผลกรณีไม่มี state เป็น failure แทน crash
- live_candidate_4: 22/24 ผ่าน พบ alias “โอนเงิน” ดึง FAQ เลขบัญชีแทนคำถามรูปหลักฐานผิด ทำให้ validation ปฏิเสธ และตอบ “ใช่” ต่อไม่ได้
- live_candidate_5: หลังเพิ่ม rejected-coverage recovery ผ่าน 24/24 พร้อม selector proposal จริง 7 ครั้ง ไม่มี timeout/binding failure ในชุดนั้น
- หลังติดตั้ง ตรวจเว็บจริง 24/24 ผ่าน selector proposal จริง 7/7 ครั้ง ไม่มี timeout/binding failure ในเส้นทางที่ทดสอบ

## ผลผ่านเว็บและเวลา

| ภาษา | ข้อความผ่าน | มัธยฐาน HTTP (วินาที) |
|---|---:|---:|
| th | 10/10 | 1.438 |
| en | 14/14 | 1.004 |

เวลาเป็นตัวอย่างชุดเล็กหลังเตรียมโมเดล ไม่ใช่ความเร็วที่รับประกันทุกครั้งหรือผลทดสอบความจุหลายคน

### คำถามไทยเดิมที่เคย timeout

- HTTP ทั้งคำถาม 5.193 วินาที; selector รวม 925.176 ms; HTTP รอโมเดล 779.271 ms
- payload 3757 bytes; 515 prompt tokens และ 15 output tokens
- โมเดลเสนอหัวข้อแบบ ambiguous จาก source ที่เกี่ยวข้อง ระบบจึงถามยืนยัน และตอบจาก source ได้เมื่อผู้ใช้ยืนยันว่าเป็นเมาส์ส่วนตัว
- รอบ R82 คำถามเดียวกัน timeout หลังรอโมเดลประมาณ 6.0–6.4 วินาที ครั้งนี้รอโมเดลต่ำกว่า 1 วินาที แต่ไม่ใช้เป็น controlled speedup benchmark เพราะสภาพ cache/startup และภาระเครื่องต่างกัน

## สิ่งที่ผลนี้ยังไม่ได้พิสูจน์

- 7/7 คือ model transport/JSON topic-proposal protocol ผ่าน ไม่ใช่การพิสูจน์ semantic equivalence โดยอิสระ ยังต้องยืนยันก่อนอ่าน facts
- เคส proof of identity / wrong amount ผ่านในเกณฑ์ “ไม่ยืนยันขั้นตอนสลิปให้สิ่งอื่น” แต่ยังอาจเสนอหัวข้อสลิปให้ผู้ใช้ยืนยัน ทั้งที่ไม่ใช่หัวข้อที่ดีที่สุด จึงยังมีงานปรับความเกี่ยวข้องของ clarification; ไม่อ้างว่าสองเคสนี้เข้าใจความหมายสมบูรณ์
- ตัวอย่างการยืนยันมี ?? ซ้ำจาก title เดิม และข้อความอังกฤษบางส่วนยังมีป้าย steps/preconditions แบบ schema เป็นประเด็นการนำเสนอแยกจากการแก้รอบนี้
- direct/scoped callers ที่ต้องใช้ strict binding จริงยังคงโปรโตคอลเดิม ไม่อ้างว่าทุกเส้นทางของ LLM ถูกทำให้เร็วแล้ว
- ไม่ได้ทดสอบทุกหมวดหรือเต็ม corpus และไม่อนุมัติข้อมูลเจ้าของ/ราคา/วันมีผลแทนเจ้าของ

## สิ่งที่รักษาไว้

- เปลี่ยนเฉพาะ entity_search.py, answer.py, migrated_chat.py ใน R78 มี before/ และ CHANGESET.patch
- ไฟล์แอป/UI อื่น 400 ไฟล์ไม่เปลี่ยน strict semantic validator กับ open_day.py ของ R80 ไม่เปลี่ยน
- DB SHA256: `4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d` ก่อน/หลังเท่ากัน ไม่มีการแก้ facts/ราคา/นโยบาย/approvals/releases
- raw log ทุก attempt อยู่ครบ ไม่ทับไฟล์เก่าหรือรีเซ็ต Git

## ไฟล์หลักฐาน

- FLOW_R83_TH.md: Flow และการตรวจทาน
- CANDIDATE_AUDIT.json: ผู้สมัครก่อน/หลังพร้อมเหตุผล
- verification/candidate_2/RESULTS.json, qualified_final/RESULTS.json, rephrase_1/RESULTS.json
- verification/live_candidate_5/SUMMARY.json และ TURNS.jsonl
- web_results/20261017T081212Z-751801/SUMMARY.json, TURNS.jsonl และ health/launcher/model response
- INSTALLATION.json, SOURCE_INVENTORY_BEFORE.json, DELIVERY_QA.json

## สถานะเทสใหญ่

**รอผู้ใช้สั่งเพิ่มเติมเท่านั้น ยังไม่เริ่ม full test และไม่ได้ตั้งงานให้รัน full test อัตโนมัติ**
