# R121 ฝึกโมเดลให้ตีความบริบทก่อนเลือกตัวอ่านข้อมูล

## เป้าหมาย

ฝึก adapter ของ Typhoon ให้แยก **ผู้ใช้ต้องการอะไร → บริบทและเงื่อนไขที่เกี่ยวข้อง → งานที่ต้องทำ → หมวดและ field ที่ต้องอ่าน** ลดการเลือกหมวดตามชื่อเกมหรืออุปกรณ์เพียงอย่างเดียว

คำถามสิทธิ์ใช้ PS5 ต้องเป็น eligibility, คำถามว่าจองอะไรเพื่อเล่นเกมต้องเป็น game/service availability, ขั้นตอนการจองจึงเป็น reservation, บริบทเตรียมแข่งต้องคงชื่อเกม/ฉบับ/เงื่อนไขก่อนอ่าน competition rules คำขอให้ตอบสั้นเป็นรูปแบบคำตอบ ไม่ใช่งานเพิ่ม

## สิ่งที่ฝึกจริง

- ใช้ QLoRA/NF4 กับ checkpoint `typhoon-ai/typhoon2.5-qwen3-4b` revision `ce0a7416fe82d4404b2b4a253ce3ac095ab1252c`
- ฝึกเฉพาะ LoRA ใน q/k/v/o projections, rank 8; โมเดลหลัก frozen
- Loss เป็น causal cross entropy เฉพาะ completion ไม่มี loss บน system prompt/คำถาม
- ฝึก 3 epochs, micro batch 1, gradient accumulation 8, learning rate เริ่ม .00015 มี warmup/cosine decay
- เลือก checkpoint ด้วย mean validation completion loss ไม่ใช้ test accuracy เลือก checkpoint
- เก็บ initial/final adapter hashes, base parameter hashes, gradient norm, loss, จำนวน optimization steps และ VRAM เป็นหลักฐานการฝึกจริง
- ข้อมูลเป้าหมายเป็น JSON แผน ไม่มีคำตอบธุรกิจ ราคา โทษ หรือข้ออนุญาตให้โมเดลท่องจำ

## โครงสร้างแผน

`focus` ระบุจุดประสงค์ก่อน → `context_quotes` ยกเงื่อนไขสำคัญจากคำถาม → `tasks` ระบุ quote/domain/operation/facet/target/constraints/ambiguous

ทุก quote/target/constraint ต้องอ้าง substring ที่มีอยู่ในคำถามจริง `source_record_id` เป็นค่าว่าง ให้ runtime จับคู่กับข้อมูลปัจจุบันภายหลัง เหตุผลที่ให้ดูจากภายนอกเป็นการจัดประเภทงานและยกข้อความต้นทาง ไม่มีการร้องขอหรืออ้างความคิดภายในของโมเดล

## ชุดข้อมูล

ใช้คำถามที่มีอยู่แล้วทั้งหมด: train 244, validation 15, test 30

- นำ task plans ที่ตรวจแล้วจาก R120 มาเป็นส่วนหนึ่งของชุดสอน
- แก้ label ของกรณีที่ R120 ผิดหรือถอยหลัง โดยดูเจตนาของคำถาม ไม่ใช้คำตอบผิดมาสอน
- เพิ่มคำถามเดิมที่เป็นคู่ต่างบริบท เช่น อุปกรณ์/สิทธิ์เข้าใช้, นำเข้า/บริโภค, ราคา/จอง, กติกา/วิธีเล่น
- เพิ่มคำถามหลายงานเดิมเพื่อสอนการแยกงานพร้อมคง shared context
- ใช้คำถาม development เดิมของ R113 สำหรับ rental/payment/news เพื่อเพิ่มหมวดที่พบไม่มากใน retained Full; news มีคำถาม fixture เดิม ใช้สอน intent เท่านั้น ไม่ย้ายกิจกรรมจำลองเป็นข้อเท็จจริง
- ชุดสอนครอบคลุม 14 หมวด native และ general แต่ test ใหม่ในรอบนี้ไม่ครอบคลุม rental/news จึงไม่อ้างความแม่นยำของสองหมวดนี้
- แยกด้วย source case/origin family และตรวจ normalized core ไม่ข้าม train/held-out; semantic near-duplicates ที่คนละ identifiers อาจยังมี
- Labels เป็น annotations ที่ agent ตรวจจากคำถามร่วมกับ span extraction และ schema checks ไม่ใช่ owner approval หรือ independent human evaluation
- ไม่สร้างคำถามใหม่ ไม่แก้ production/native records/approvals/withdrawals หรือผลทดสอบต้นฉบับ

## การเปรียบเทียบ

วัด **HF base NF4 ก่อนฝึก** กับ **HF base checkpoint เดียวกัน + adapter หลังฝึก** ด้วย prompt, decoding และชุด test เดียวกัน เพื่อแยกผลของน้ำหนัก adapter จากการเปลี่ยน Flow

ไม่ได้อ้างว่า HF checkpoint นี้ตรง byte-for-byte กับ GGUF ของ Ollama ใน R120 และไม่เอาคะแนน planner มาเทียบตรงกับ positive literal-content checks ของ R120

ตัวชี้วัด: JSON validity, source-quote contract, focus, domain, operation/facet, จำนวน tasks, constraint precision/recall แยกจากความถูกต้องของคำตอบที่อ่านจากฐานข้อมูล

เมื่อได้ adapter แล้วจึงตรวจการใช้งานใน candidate Flow และ reader เดิมอีกครั้ง การที่ planner เลือกหมวดถูกไม่ได้รับรองว่า reader จะหา facts ครบ

## ทรัพยากรและการแยกงาน

เครื่องตรวจพบ RTX 4050 Laptop 6 GB ใช้ isolated CUDA Python environment และ base model ที่ `D:/CodexTraining/psu-r121-20261022` เพื่อรักษาพื้นที่ไดรฟ์ C โค้ด/ชุดข้อมูล/ผลอยู่ในโฟลเดอร์ R121 นี้

Runtime: Python 3.12, PyTorch 2.7.1+cu128, Transformers 4.56.2, PEFT 0.17.1, bitsandbytes 0.48.1, Accelerate 1.10.1 ผล CUDA NF4 forward/backward อยู่ใน `CUDA_PREFLIGHT.json` ไม่เปลี่ยน Python ที่ระบบเดิมใช้อยู่

## เงื่อนไขก่อนนำไปใช้จริง

1. ต้องมี optimizer updates จริงและ adapter weights เปลี่ยน โดย base weights ไม่เปลี่ยน
2. ต้องตรวจผลนอกชุดสอนและกรณีที่แย่ลงด้วย ไม่ใช้ training loss เป็น accuracy
3. quote/condition/public scope/validity/source guards ต้องยังทำงาน
4. ต้องแยก model transport, source gaps และ reader failures จาก intent errors
5. การทดสอบรอบนี้เป็น pilot ไม่ใช่ Full Test และยังไม่ติดตั้งทับ R78

## เอกสารอ้างอิงของเครื่องมือ

- [HF PEFT: quantization and LoRA](https://huggingface.co/docs/peft/v0.17.0/en/developer_guides/quantization)
- [HF Transformers: Qwen3](https://huggingface.co/docs/transformers/v4.56.2/model_doc/qwen3)
- [bitsandbytes installation and Windows/CUDA support](https://huggingface.co/docs/bitsandbytes/main/en/installation)
- [Official Typhoon model card](https://huggingface.co/typhoon-ai/typhoon2.5-qwen3-4b)
