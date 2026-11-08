# Research → implementation r53

## ขอบเขตและวิธีค้น

ใช้ paper-search-pro วางกลุ่มคำค้น แต่ helper หยุดตามคำสั่ง Setup เพราะยังไม่มี OpenAlex key และ NCBI email ใช้ web search/open ไปยัง ACL Anthology และ arXiv โดยตรงเป็น targeted fallback เมื่อ 2026-10-09 รายการคำค้นและสิ่งที่ข้ามอยู่ใน ../query_plan.json ไม่มีการอ้าง saturation, PRISMA completeness หรือ journal rank การค้นนี้คัด 8 งานเพื่อแก้ปัญหาที่เห็น ไม่ใช่ systematic review รายงาน HTML เป็น static fallback ไม่ใช่ Shadcn renderer ของ skill

อ่าน abstract/metadata ทุกงาน และอ่าน PDF methods/evaluation ของ xCOMET, limitations ของ FActScore และ CoVe เพิ่ม ไม่ได้อ้างว่าอ่านเนื้อหาทุกหน้าของทุกงาน ไม่มีการนำผลภาษาอื่นมายืนยัน accuracy ภาษาไทยของระบบเรา

## งานที่เลือกและการนำมาใช้

### 1. [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://aclanthology.org/2023.emnlp-main.741/) — 2023 / EMNLP

- หลักฐาน: แยกคำตอบเป็นข้อกล่าวอ้างและตรวจหลักฐานประกอบ; การตอบน้อยหรือไม่ตอบอาจทำ precision ดูดี จึงต้องรายงาน coverage และ abstention ด้วย
- ใช้ในโปรเจกต์: นำหลักการ evidence scope และแยก answer delivered มาใช้; ยังไม่ได้ทำ atomic extraction/evaluator เต็มระบบ

### 2. [xCOMET: Transparent Machine Translation Evaluation through Fine-grained Error Detection](https://aclanthology.org/2024.tacl-1.54/) — 2024 / TACL

- หลักฐาน: ให้คะแนนและตำแหน่งข้อผิดพลาดพร้อม severity; WMT22/23 evaluation ที่อ่านไม่ใช่คู่ไทย–อังกฤษ โมเดล XL/XXL มีขนาด 3.5B/10.7B
- ใช้ในโปรเจกต์: ยืมวิธีจัดหมวด accuracy/addition/coverage/factuality ไม่ได้ติดตั้งหรืออ้างคะแนน xCOMET

### 3. [Guiding Large Language Models to Post-Edit Machine Translation with Error Annotations](https://aclanthology.org/2024.findings-naacl.265/) — 2024 / Findings NAACL

- หลักฐาน: external MQM feedback ใช้ชี้การแก้คำแปล; ผล fine-grained prompting ไม่ชัดเท่า fine-tuning ในงานนี้; tested zh-en/en-de/en-ru
- ใช้ในโปรเจกต์: ส่งเหตุผลที่ตรวจได้และคำอธิบายวิธีแก้กลับเพียงหนึ่งครั้งภายใต้งบเวลา ไม่ย้ายผลทดลองมาอ้างเป็นภาษาไทย

### 4. [Chain-of-Verification Reduces Hallucination in Large Language Models](https://arxiv.org/abs/2309.11495) — 2023 / arXiv preprint

- หลักฐาน: ร่าง→คำถามตรวจสอบ→ตอบตรวจอย่างอิสระ→แก้ร่าง; งานยังมี hallucination และใช้การคำนวณเพิ่ม
- ใช้ในโปรเจกต์: นำแนวคิดตรวจเงื่อนไขก่อนปล่อยมาใช้ร่วม external facts; ไม่ได้ติดตั้ง CoVe สี่ขั้นเต็มทุกคำขอ

### 5. [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://aclanthology.org/2024.tacl-1.78/) — 2024 / TACL

- หลักฐาน: survey แยกเงื่อนไขและคุณภาพ feedback; reliable external feedback เป็นเงื่อนไขสำคัญ ไม่ควรถือการสั่งโมเดลตรวจตนเองว่าเชื่อถือได้เสมอ
- ใช้ในโปรเจกต์: ใช้ deterministic constraints และ reference cards แทนการขอโมเดลรับรองตนเองโดยไม่มีหลักฐาน

### 6. [Can LLMs Detect Intrinsic Hallucinations in Paraphrasing and Machine Translation?](https://aclanthology.org/2025.gem-1.13/) — 2025 / GEM workshop

- หลักฐาน: ประเมิน hallucination ใน translation/paraphrase; detector ผลต่างตาม model และ NLI มีผลเทียบได้ในงานที่ศึกษา
- ใช้ในโปรเจกต์: NLI/learned evaluator เป็นทางเลือกต่อไป ต้องทดสอบไทยและ false positive ก่อนเพิ่ม runtime; ยังไม่ได้ติดตั้ง

### 7. [Syllable-based Neural Thai Word Segmentation](https://aclanthology.org/2020.coling-main.407/) — 2020 / COLING

- หลักฐาน: ไทยมีปัญหาขอบเขตคำ; งานเสนอ syllable-based segmentation ไม่ใช่การนับช่องว่าง
- ใช้ในโปรเจกต์: คง Thai word-count unverified; ขั้นถัดไปเลือก tokenizer/version และทดสอบข้อความผสมไทย–อังกฤษก่อนใช้รับรอง 500 คำ

### 8. [FactCorrector: A Graph-Inspired Approach to Long-Form Factuality Correction of Large Language Models](https://arxiv.org/abs/2601.11232) — 2026 / arXiv preprint

- หลักฐาน: ใช้ structured factual feedback; VELI5 สร้าง errors ที่มี corrections เพื่อประเมินการแก้
- ใช้ในโปรเจกต์: นำแนวคิด bad/good paired fixtures มาใช้ ไม่ได้ติดตั้ง graph pipeline หรืออ้างผล benchmark ว่าจะเกิดบนเครื่องนี้

## ข้อสรุปที่ใช้ตัดสินใจ

1. ข้อผิดพลาด routing ต้องแก้ก่อนประเมินคำแปล: quotation ของ booking/PC เป็นข้อมูลของงานแปล การเพิ่ม evaluator ไม่ช่วยถ้าระบบไม่ได้แปลตั้งแต่แรก
2. Output ผ่านจำนวนบรรทัด/stream done ยังไม่พอ ต้องรักษาตัวเลข หน่วย คำปฏิเสธ ชื่อเครื่อง และระดับความแน่นอน
3. คำตอบเทคนิคต้องมี facts และ version qualifier จากแหล่งต้นทาง การแนบ URL อย่างเดียวไม่ได้พิสูจน์ทุกประโยค
4. Repair ต้องระบุความผิดและเงื่อนไขแก้ให้เข้าใจได้ มี budget และตรวจผลซ้ำ ไม่ใช้ retry ไม่จำกัด
5. ค่าผ่าน fixtures คือคุณภาพตัวตรวจบนเคสที่ออกแบบ ค่าตอบสำเร็จคือผล runtime และ accuracy ต้องตรวจความหมายแยกจากสองค่านี้

## สิ่งที่ยังต้องทำต่อจากรอบนี้

negation หลาย clause, omission ที่ไม่ใช่เลขหรือศัพท์ในชุด, qualifiers ที่เกินรูปแบบตัวตรวจ และ semantic entailment ภาษาไทยทั่วไปยังตรวจไม่ครบ ต้องเพิ่ม evaluation set ที่แยก held-out กับตัวอย่างพัฒนา ก่อนพิจารณา learned evaluator ไม่มีการปรับ model หรือ fine-tuning ในรอบนี้
