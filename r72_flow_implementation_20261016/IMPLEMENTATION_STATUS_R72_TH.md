# สถานะ R72 เทียบ Flow R71

รายการนี้แยกสิ่งที่ทำแล้วออกจากงานที่ยังไม่ครบ ไม่ใช้คะแนนชุดเจาะจงแทนการตรวจทั้งระบบ

| งานเดิม | ผลในรอบนี้ | ยังเหลือ |
|---|---|---|
| S00 เก็บต้นทาง | สำเนา R72, manifest, DB/seed hash เท่าเดิม, source code/data ไม่เปลี่ยน | ไม่มีงานย้าย production ในรอบนี้ |
| S01 แยกชนิดปัญหา | แยก content/safety/oracle/model และเก็บแต่ละรอบ | ยังไม่จัดหมวดทุก 10,277 คำถามใหม่ |
| S02 LLM | ON; มี actual selector attempt และ error จริง | socket ไม่ได้สิทธิ์ ต้องตรวจ generation/schema/selection สำเร็จ |
| S03 trace | เพิ่ม request needs/named scope/unresolved scope และ coverage ต่อ role | universal tracing ของทุกเส้นทางเก่ายังไม่ได้รับรอง |
| S04 metadata | ใช้ intent_key เดิมโดยไม่ผูกกับ record ID | แบบกรอก/semantic metadata ครอบคลุมทุกหัวข้อใหม่ |
| S05 identity | 1 คู่ 3 fields พร้อม hash/withdraw guard | คู่ซ้ำอื่นและ conflict ทุกหมวดยังต้อง audit |
| S06 needs | method/deadline/quota/studio rules, negative/exception, compound | paraphrase/qualifier ที่นอก grammar ยังไม่ครบ |
| S07 retrieval | ไม่ตัด prefix ก่อน index, relevant windows ภายใต้ prompt budget, คง guard | ความแม่น selector กับโมเดลจริงและ ambiguous headings |
| S08 planner | คง schema/semantic guard เดิม | ยังไม่ปรับครบข้อจำกัด model paraphrase ใหม่ |
| S09 เวลา/ราคา | วันหยุดไม่ระบุวันขอวันที่; ไม่แก้ validity/นโยบาย | temporal/conflict comprehensive review ยังไม่ครบ |
| S10 coverage | หลาย roles และ missing source แสดงชัด; explicit mixed topic composition | pagination และ coverage กฎทุก clause ยังไม่ครบ |
| S11 ภาษา | retry/unavailable ตาม locale, หน่วยบริการอังกฤษ | translation audit ทุก record/ชื่อเฉพาะ และ status ทุก template |
| S12 บริบท | follow-up วิธี/เวลาไทยอังกฤษ, domain switch; update fixture epoch/revision | browser session/release operation จริง |
| S13 ทดสอบ | Target 43, Risk 18, Holdout 12, API46, Update8, Fixture8, สำรวจ7; ON/common เท่านั้น | replay model-dependent เมื่อเชื่อมโมเดลได้; ไม่รัน full/legacy/OFF |
| S14 ส่งมอบ | launcher/README สำเนา R72 พอร์ต8103/editor8104 และทางกลับ R69 | ยังเป็น draft; portable production package และ release gate ยังไม่เสร็จ |

ผลและเหตุผลละเอียด: `REPORT_R72_TH.md` ส่วนคำถามที่ยังตอบไม่ได้และสิ่งที่ต้องให้เจ้าของยืนยันอยู่ในรายงานนั้นด้วย
