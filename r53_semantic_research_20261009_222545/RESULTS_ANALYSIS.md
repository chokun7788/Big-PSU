# ผลการค้นและแก้ r53 — 2026-10-09

## สถานะ

ลงมือแก้ source และเปิด candidate r53.3 ที่ http://127.0.0.1:8093/ ไฟล์แพ็กเกจที่แจกคนอื่นก่อนหน้านี้ยังไม่ได้ sync เป็น r53 ใช้ candidate ของรอบนี้ทดลองได้ รายงานนี้ไม่รับรองว่าความรู้ทั่วไปหรือคำแปลทุกสำนวนถูกต้องทั้งหมด

## งานที่แก้และสาเหตุ

| ปัญหา | เหตุผลที่เคยเลือกตอบผิด | สิ่งที่แก้ |
|---|---|---|
| Translate ประโยค booking ถูกตอบกฎจอง | routing ตีความคำใน source เป็นคำถามศูนย์ก่อนระบุ translation task | route งานแปลที่มี source/target ชัดก่อน protected intent และใช้ปลายทางตามคำสั่ง |
| Wait 15 minutes ไป no_answer | การคัด general request ผ่าน guard เดิมไม่ครอบคลุม source แปล | ตรวจ task syntax ก่อน guard หมวดบริการ |
| network กลายเป็น internet | model เลือกคำใกล้เคียงและตัวตรวจเดิมดูรูปแบบอย่างเดียว | terminology/scope constraints พร้อม feedback |
| เลข/หน่วย/PC เปลี่ยน | ยังไม่มี source-output constraints | เปรียบเทียบตัวเลข หน่วย entities และ negation ที่ตรวจได้; ไม่รับ PC10 แทน PC1 |
| 15 กลายเป็นประมาณ 15 | รูปแบบและตัวเลขยังผ่าน แต่ระดับความแน่นอนเปลี่ยน | ตรวจ numeric approximation และบอกวิธีแก้ด้วยภาษาตรงไปตรงมา |
| คำเทคนิคขาดข้อยกเว้น | ไม่มี reference facts/ตรวจ contradiction ตามหมวด | context facts แยกจาก owner policy: ping, HTTP/TLS, TCP, RAM/SSD |
| meta Note/QUESTION กับคำถามกลับเกิน | prompt ชี้การคงศัพท์จน model บรรยาย prompt | ปรับ prompt และตรวจ instruction commentary/clarifying tail; literal Note ในคำแปลยังอนุญาต |
| งานคัดลอกมี note เกิน/คำชวนมีแต่คำทักทาย | provenance และ format validation ไม่รู้ชนิดงาน | ไม่เติม note ลงข้อความแปล/งานเขียนสั้น; แยก metadata; ตรวจ content sentence ของคำชวน |
| ทุก failure ถูกเข้าใจว่าโมเดลล่ม | mode legacy มี unavailable แม้ model done | เพิ่ม provider attempted/done และ failure_reason output_meaning_unverified; mode เดิมยังเก็บเพื่อ compatibility |

ไฟล์เปลี่ยน: app/pipeline/experimental_fallback.py, engine.py, query_signals.py เพิ่ม semantic_quality.py, tests/test_semantic_quality_r53.py และ data/general_evidence/technical_facts_20261009.json

## ผลแยกตามชั้น

- Fixtures bad/good เดิม: ก่อนแก้ 10/21 → หลังแก้ 21/21 → ตรวจสุดท้าย 21/21 นี่คือความถูกต้องตัวตรวจบนเคสที่กำหนด ไม่ใช่ accuracy ของผู้ใช้ทุกคำถาม
- Unit/pipeline/provider/jobs/conversation ที่เกี่ยวข้อง: source สุดท้ายผ่าน 49/49 methods (targeted_unit_r53_3.txt); รอบก่อน 48/48 และเพิ่มหนึ่ง test อธิบาย feedback ในรอบสุดท้าย
- เว็บ baseline 6 เคส: transport 6/6, model answer 3/6; baseline เลือก subset จึงไม่เอาไปเทียบเปอร์เซ็นต์กับ 14 เคสโดยตรง
- เว็บ r53.1 14 เคส: transport 14/14, model answer 11/14; checker เดิมไม่มี error ใน 11 คำตอบ แต่ตรวจอ่านพบ addition “ประมาณ” ใน Wait 15 minutes จึงไม่นับ 11/11 เป็น semantic accurate
- เว็บ r53.2 11 เคส: transport 11/11, model answer 8/9 งาน LLM + 2/2 deterministic controls; คำแปล exact 15 ถูกปฏิเสธหลัง repair ยังเติมประมาณ เก็บ failure ไม่ยอมปล่อยเป็นคำแปลถูกต้อง
- เว็บ r53.3 5 เคสที่แก้เฉพาะ: transport/model 5/5, 0.54–1.46 วินาที; exact15/exact30/about15/คำสั่งไทย/exact PC10+negation ผ่านการอ่านตาม constraints
- ราคา PC บุคคลทั่วไปยังตอบ 70 บาท/60 นาทีจาก owner source; identification ภาษาอังกฤษยังตอบ national ID/student/school/passport จากคำตอบผู้ใช้

ผลเว็บทั้งหมด 36 requests คือ 6 baseline +14 r53.1 +11 r53.2 +5 r53.3 ไม่ใช่ 36 คำถามไม่ซ้ำและไม่ได้เป็น load test

## วิเคราะห์สิ่งที่ยังผิดหรือไม่ยืนยัน

### P1 — งานยาวภายใต้ deadline

คำถาม RAM/SSD ไทยประมาณ 500 คำได้ stream บางส่วน 1,222 characters แต่ไม่ done ภายใน 15 วินาที ระบบจึงไม่ปล่อยข้อความตัดกลางคำตอบ คำถาม DNS/TCP/TLS/HTTP อังกฤษ stream done ได้ 370 คำ ไม่ถึง minimum coverage ของคำขอ500 จึง reject ตาม requested_length_coverage_missing นี่คือสองเหตุผลต่างกัน: timeout กับ output coverage ต้องแก้ architecture long-job/deadline หรือ progressive delivery และวัด throughput ก่อน ไม่ลดเกณฑ์เพื่อให้ผลดูผ่าน ไม่ได้แก้ในรอบนี้

### P1 — การตรวจความหมายยังมีขอบเขต

negation เป็น presence check ยังแยกหลาย clause / not only / scope ไม่ได้; numbers ไม่รองรับคำเขียนเป็นตัวอักษรทุกแบบ; terminology มีเพียง concept/units ที่ระบุ; omission ของรายละเอียดอื่นยังหลุดได้ การมี keyword หรือ source URL ไม่รับรองความถูกต้องทุก claim ตัวตรวจ ping/HTTP/RAM เป็น pattern ตามข้อผิดจริง มีโอกาสทั้ง false positive และ false negative ต้องมี held-out paraphrase/contradiction set ก่อนใช้เป็นคะแนน accuracy

### P2 — source extraction และคำขอหลายงาน

รองรับ source-first และ target-first ที่มีภาษา/ขอบเขตชัด ไม่ครอบคลุมข้อความกำกวม/ไม่มี source; การแปลพร้อมถามราคาต่อในคำขอเดียวอาจมี ambiguity ยังไม่ได้ออกแบบ compositional task parser ไม่ควรอ้างว่ารองรับทุกสำนวน

### P2 — ภาษาไทยและรูปแบบคัดลอก

Thai word count ยังไม่มี tokenizer ที่ยืนยัน จึงห้ามนับ space/character แล้วอ้าง 500 คำ ภาษาไทยคำตอบ RAM สั้นบางสำนวนยังไม่ลื่น (“RAM ... สูญหาย”) ต้องปรับความชัดว่า “ข้อมูลใน RAM” แทนกล่าวตัวอุปกรณ์หาย การตัด note ใน task สำหรับ copy อยู่ใน metadata ผู้ใช้ควรเห็น provenance จาก UI แยก answer text ในงานถัดไป

### P2 — runtime และผลทดลอง

network translation อังกฤษหนึ่งครั้ง timeout ก่อน first token 15.6s; rerun r53.2 ได้คำตอบประมาณ1.44s จึงยังยืนยันสาเหตุระดับ GPU/queueไม่ได้จาก traceนี้ ไม่ตั้งชื่อว่าเป็น hallucination การทดสอบส่วนใหญ่ sequential ยังไม่วัดคุณภาพ r53 ภายใต้ concurrent workload

## การรักษาข้อมูล

snapshot before และ hashes อยู่แยกจาก source เดิม ตรวจ owner curated/rules/booking_dashboard ว่าไม่เปลี่ยนใน PRESERVATION_AUDIT.json ตรวจ source กับ candidate r53.3 ตรงกัน Git status ใช้ไม่ได้ตั้งแต่ก่อนแก้เพราะ metadata ชี้ checkout path เก่า จึงไม่อ้างว่า working tree clean ไม่ได้ reset Git ไม่ลบ log หรือแพ็กเกจเดิม

## Paper และ Flow

อ่าน 8 งานที่คัดจาก ACL/arXiv รายงานข้อจำกัดและ mapping อยู่ papers/report.md ใช้หลักการจากงานวิจัยร่วม constraints/context โดยไม่ได้ติดตั้ง xCOMET, FActScore หรือ CoVe เต็มระบบ Flow สมบูรณ์พร้อมการตรวจทานอยู่ FLOW.md ผลรายคำถามและเหตุผล trace อยู่ QUESTIONS_ANSWERS_ANALYSIS.md
