# ลูป H — แก้ validation regressions จาก final13

## หลักฐานและสาเหตุ

AUDIT_final13: 7 requests ต่อ flag ถูก validation ปฏิเสธ รากเหตุสองกลุ่มคือ policy priority ถูกวางก่อน competition context และ FAQ ที่จับชื่อได้ตอบ answer แล้ว แต่ generic question tails ยังถูกนับเป็น unresolved intent

RESIDUAL_READER หลังเปิด LLM ยังพบคำถามที่ตั้งถูกเลือก FAQ ติดต่อ เพราะ semantic candidate ทำงานก่อน typed center.address discovery ทั้งที่มี source ที่อยู่ครบ

## Flow และทบทวน 3 รอบ

### รอบ 1 — อย่าลด validation เพื่อให้ผ่าน

ย้าย policy priority หลัง competition resolution รักษาข้อมูลกฎและ facets เดิม; เลือก center.address ก่อน model เมื่อคำถามสถานที่ระบุศูนย์ชัดและไม่ได้ถามติดต่อ; source ยังต้องผ่าน validity/withdrawal และ field authority

### รอบ 2 — FAQ ต้องแยก topic กับ boilerplate

Default FAQ answer รับได้เมื่อ tail หลัง exact alias เหลือเพียงรูปประโยคคำถาม/คำสุภาพ ไม่ยอมรับเนื้อหาใหม่ที่ขอเพิ่ม เช่น scope หรือ compensation; cancellation ต้องเลือก cancel/edit source จริง แทน booking steps ที่ชื่อสั้นชนกัน และคงเงื่อนไขของต้นฉบับในข้อความ

### รอบ 3 — positive/negative และ model-on

เพิ่มเคส match policy ต้องได้กติกา, ที่อยู่เปิด/ปิด LLM, ยกเลิก/ของหาย/เบอร์แบบพิมพ์ต่างกัน รวม negative ที่ FAQ ถูกถามเนื้อหาเพิ่มแล้วต้องยังไม่รับเป็นครบ; ไม่ rewrite grader เดิม ไม่ตัด validation errors จาก denominator; rerun common OFF/ON กับ snapshot ใหม่

ระหว่างอ่าน source พบคำแปลคำถามเจ้าของผิดตามบริบท: เครื่อง→flight และศูนย์→zero ต้องแก้เฉพาะ generated English เป็น draft revision โดยเก็บ Thai/evidence เดิม ตรวจคำถามเจ้าของที่มีอยู่ทั้งหมดแล้ว แยก agent review จากเจ้าของอนุมัติ
