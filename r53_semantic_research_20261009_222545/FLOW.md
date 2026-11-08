# Flow แก้ความหมายคำแปลและคุณภาพคำตอบ r53

## หลักฐานตั้งต้น

ต่อจาก r52: network แปลแคบเป็น internet, ping ถูกอธิบายคล้าย bandwidth test, HTTP/TLS ไม่ระบุขอบเขตรุ่น, คำชวนสองประโยคมีหนึ่งประโยคเป็นคำทักทาย, meta-instruction/คำถามกลับเกิน และ provenance note ปะปนกับข้อความที่โมเดลสร้าง

## แนวทางจากงานวิจัย

- xCOMET/MQM: แยก error span/ชนิด/severity เช่น mistranslation, omission, addition; นำมาทำ constrained checks ที่อธิบายเหตุผล ไม่ใช้คะแนนรวมรับรองภาษาไทยทั้งหมด
- FActScore: แยก atomic claims กับ evidence; ในงานนี้เริ่มจาก fact cards หมวดที่พบความผิดจริง ไม่อ้างว่าใช้ FActScore model เต็มระบบ
- CoVe และ survey self-correction: verification ต้องมีเงื่อนไข/evidence ที่ตรวจได้ แก้หนึ่งครั้งตามเวลาที่เหลือ ไม่สั่งโมเดลเดียวรับรองตัวเองทุกประโยค
- Thai segmentation: คง word-count unknown จนเลือก/ทดสอบ tokenizer/version ได้ ไม่ใช้การนับ space หรือ character เป็น 500 คำ

## Loop 1 — เก็บ baseline และข้อกำหนด

1. snapshot/hash source, tests และ owner data ก่อนแก้ เก็บ log เดิม
2. ชุด bad/good คู่กัน: network/internet, ตัวเลข, หน่วย, negation, PC1/PC2, literal Note, meta tail, invitation, ping, HTTP, RAM
3. แยก expected rejection จาก provider success; good paraphrases ต้องไม่ถูกปฏิเสธเพราะต่างตัวสะกด

## Loop 2 — แก้ความหมายและ output

raw request → ระบุ translation source/target → constraints ตัวเลข/หน่วย/ชื่ออุปกรณ์/คำปฏิเสธ/terminology → generate → ตรวจ error reasons → bounded repair ถ้ามีเวลา → final output

1. คำสั่งแปลต้องไม่ถูก profile จำนวนคำ/ประโยคดึงไปเป็นงานเขียน ไม่ตัดข้อความยาวเหลือวลี
2. แยกภาษาปลายทางจากภาษา UI ไม่บังคับคำแปลเป็นภาษาของหน้าเว็บ
3. เปลี่ยน prompt ไม่ให้บรรยายคำสั่ง/คัดคำว่า QUESTION/ANSWER และไม่ถามกลับท้ายคำตอบที่มีข้อมูลพอแล้ว
4. งานชวนสองประโยคต้องไม่ใช้ประโยคทักทายเปล่าเป็นส่วนเนื้อหาหนึ่งประโยค
5. ไม่เติม provenance note ลงในข้อความแปล/งานเขียนที่ต้องคัดลอกใช้; บันทึกชนิดงาน/การตรวจใน metadata
6. สำหรับคำตอบความรู้ทั่วไป แสดง provenance แบบ exact marker แยกจาก Note ของโมเดล ไม่ให้ Note ใด ๆ ปิดคำเตือนที่จำเป็น

## Loop 3 — หลักฐานของ factual answers

1. เพิ่ม general evidence file ใหม่ แยกจากนโยบายเจ้าของ: ping/HTTP/TCP/RAM/SSD ใช้ Microsoft/RFC/manufacturer ที่อ่านจริง
2. เลือก evidence เฉพาะ concept ที่ถาม ไม่ใช้กับ translation/creative หรือจอง/ราคา/กฎศูนย์
3. prompt ให้ใช้ขอบเขตและข้อยกเว้นจาก evidence ไม่แต่งรายละเอียดเกิน
4. ตรวจ known contradictory claims; ระบุ supported context ≠ ทุกประโยค verified ไม่ใช้ source URL เป็นเครื่องหมาย accuracy 100%
5. ไม่เปิด web fetch ในทุกคำถามหรือเพิ่ม evaluator โมเดลหนักบน GPU เดิมโดยไม่มี benchmark

## Loop 4 — ทดสอบจริงและตรวจทาน

1. pure fixtures → mocked pipeline/provider → เว็บจริงด้วยหลายสำนวนไทย/อังกฤษ ไม่ full 20k
2. เก็บ raw draft/rejected reason/repair outcome/provider_done/เวลาแต่ละคำขอ
3. ตรวจ semantic oracle รายเคส แยก shape, answer delivered, meaning constraints, claim support
4. ถ้าพบ false rejection ปรับข้อกำหนดจากหลักฐานและรันชุดเฉพาะซ้ำ
5. ตรวจ owner-data hash ไม่เปลี่ยน พร้อม source/candidate parity เก็บ report + revised flow

## ข้อจำกัดตั้งแต่ก่อนทำ

การค้นเป็น targeted primary-source fallback เพราะ skill helper ขาด config; ไม่มี saturation/citation-rank/PRISMA claim ไม่ติดตั้ง xCOMET และไม่เรียก bounded checks ว่า learned entailment ภาษาไทยทั่วไปยังต้องมี evaluation set และ tokenizer ที่ชัดเจน


## ตรวจทานหลังลงมือจริง — Flow ฉบับใช้ต่อ

### ลำดับที่ปรับหลังพบปัญหา

raw input → detect explicit translation boundary ก่อน routing หมวดศูนย์ → แยก source กับ target language → profile budget → scoped evidence เฉพาะ factual request → generate → require provider done → shape check → meaning constraints → ถ้าพลาดและมี budget ส่งชื่อ error พร้อมคำอธิบายให้แก้เพียงครั้งเดียว → ตรวจซ้ำ → answer หรือ failure_reason ที่ระบุสาเหตุ → format provenance ตามชนิดงาน → job completed

job completed คือระบบส่งผลแล้ว อาจส่ง refusal/timeout ไม่ใช่คำตอบสำเร็จ; model done คือข้อความจาก provider จบ ไม่ใช่คำตอบถูกต้อง; semantic checks pass คือผ่านเฉพาะข้อกำหนดที่มี ไม่ใช่ทุก claim verified

### การทบทวนและผล 4 รอบ

1. Baseline: fixtures10/21 และเว็บ6เคส พบ source booking ถูกตีความเป็นนโยบายจอง รวมทั้ง no_answer ของ Wait15 เพิ่ม routing ก่อน protected intent ใน Flow
2. Implement r53.1: fixtures21/21; เว็บ14เคสมี11modelanswers; ตรวจอ่านพบ “ประมาณ” ที่ checker ยังไม่จับ และพบงานยาวไม่ครบ แยก semantic addition จาก timeout/coverage
3. Review r53.2: เพิ่ม target-first syntax, entity boundary PC1≠PC10, numeric certainty; unit48/48 และเว็บ11เคส ราคา/เอกสารยังผ่าน แต่ exact15ถูก reject หลัง repair พบชื่อรหัส error อย่างเดียวไม่ชี้วิธีแก้ชัดพอ
4. Refine r53.3: เพิ่ม feedback อธิบาย numeric certainty และ constraints อื่น; เว็บ5เคส exact15/exact30/about15/Thai command/PC10+negation ผ่าน; เพิ่ม unit แยก exact vs approximate ทั้งดี/ผิด ไม่ลด coverage criteria ของ500คำ

### งานลำดับถัดไปที่ทำเองได้

1. เส้นทาง long-job: กำหนด answer-length/deadline ตาม throughput ที่วัดจริง ใช้ queue/job polling และ explicit time limit ของงานยาว ทดสอบเฉพาะ100/300/500คำ ไทย–อังกฤษ ไม่เอาคำตอบสั้นแทนคำขอยาวแล้วบอกผ่าน
2. Expand meaning evaluation: held-out source/good/bad pairs ใส่ multiple negations, omission, numeric words, modifiers, bilingual identifiers กำหนด expected meaning ก่อนดู model answer แยก precision/coverage/false reject
3. Learnable evaluator feasibility: benchmark NLI/xCOMET offline แยก GPU generation วัดขนาด/เวลาและความน่าเชื่อถือไทย ใช้ abstain เมื่อ evaluator ไม่ชัด ไม่ใช่เพิ่มการเรียกโมเดลเองทุก request
4. Thai tokenizer: เลือก version/licence/dependency วัดหน่วยคำกับไทยผสมอังกฤษ เก็บ unknown ไว้จนวัดจริงได้
5. Clear provenance in UI: แสดง task/provider/verification status แยกจาก answer ที่ copy ได้; อย่าใช้ true accuracy badge จาก constraints_pass
6. Concurrent semantic test: เริ่ม2/4users แยก jobs capacity/admission wait/first token/answer quality และ session isolation ไม่เพิ่ม model parallelism จน memory/latency รองรับ

### เกณฑ์หยุดและคำถามเจ้าของ

รอบนี้หยุดเมื่อข้อผิดที่ยืนยันและอยู่ใน scope มี guard/repair พร้อมเทสเฉพาะและรายงานสิ่งค้าง งานยาว/semantic general ไม่ถือว่าปิดครบ ไม่มีคำถามนโยบายใหม่ที่ต้องเดาเพื่อทำ r53 ถ้าจะเปลี่ยนเงื่อนไขราคา/จองให้นอก source ต้องให้เจ้าของยืนยันตามรายการเดิม ห้ามใช้ general evidence ไปแทนนโยบายศูนย์

### เอกสารประกอบ

- papers/report.md: source links, selected papers, limits และ research→code mapping
- RESULTS_ANALYSIS.md: เหตุผลที่ยังตอบไม่ได้/ขอบเขตที่ไม่ได้แก้
- QUESTIONS_ANSWERS_ANALYSIS.md: คำถาม/คำตอบจริง/trace reasons/repair draft
- targeted_unit_r53_3.txt และ PRESERVATION_AUDIT.json: final verification / owner-data hashes / candidate parity

ผล gate สุดท้าย: unit/pipeline/jobs/conversation 49/49 methods ผ่าน, owner-data 38/38 hashes ไม่เปลี่ยน และ candidate r53.3 ตรงกับ source ในทุกไฟล์ที่ตรวจ
