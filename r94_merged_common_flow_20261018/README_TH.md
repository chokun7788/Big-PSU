# Flow กลางฉบับรวม R94

รวม Flow กลางเดิมตาม R90 กับ Flow ใหม่ R91 ใช้สิ่งที่ทำแล้วใน R92 และข้อผิดพลาดจากผล R93 เป็นหลักฐานปรับแบบ

**สถานะ: ออกแบบรวมและตรวจทานแล้ว ยังไม่ติดตั้งตามแผนนี้ ไม่รัน chatbot tests ใหม่ และไม่แก้ข้อมูล/approval/log เดิม**

## อ่านเอกสารตามนี้

1. [Flow รวมฉบับหลัก](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r94_merged_common_flow_20261018/01_MERGED_COMMON_FLOW_TH.md) — เปรียบเทียบส่วนที่เก็บ/เปลี่ยน แผนภาพ full flow, interfaces, runtime steps, domain subflows และ owner workflow
2. [แผนลงมือและ coverage](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r94_merged_common_flow_20261018/02_IMPLEMENTATION_AND_COVERAGE_TH.md) — source modules, rollout/retirement ของ branch เดิม, S0–S7, mapping ปัญหา 37 ข้อและ kinds 24 หมวด พร้อมเกณฑ์เสร็จ
3. [การทบทวนแบบสามรอบ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r94_merged_common_flow_20261018/03_DESIGN_REVIEW_TH.md) — ช่องโหว่ที่พบ วิธีปรับ และ counterexamples ที่ต้องตรวจเมื่อพัฒนา

## ข้อสรุปของแบบรวม

- ใช้ TaskPlan/NeedGraph ของแนวใหม่เป็นแกนร่วมก่อนเลือก fields
- รักษา schema/store/evidence/revisions และ typed domain readers ที่มีอยู่ โดยต่อผ่าน interfaces เดียวกัน
- แก้คำเกริ่น/คำผิด/context ก่อนแยก branch ไม่ให้ exact name ข้ามการเข้าใจงาน
- Semantic acceptance ไม่กลับไปติด lexical gate เดิม และไม่เปิดรับทุก JSON ของ LLM
- เพิ่ม/แก้ records ผ่านข้อมูลกลาง ไม่เพิ่ม handler ชื่อเกม/คำตอบรายรายการ
- ราคา policy calendar และ live ยังยืนยันตาม source/validity ของแต่ละ need
- ระบุสถานะเป็นราย capability พร้อมหลักฐาน ไม่ใช้ targeted pass แทนการแก้ทั้ง Flow

## ไฟล์ตรวจสอบ

`BASELINE_MANIFEST.json` ตรึง hashes ของ app/data และแหล่งวิเคราะห์ที่อ้างอิงก่อนจัดเอกสาร ส่วน `DOCUMENT_QA.json` และ `PRESERVATION_CHECK.json` บันทึกการตรวจเอกสาร/ไฟล์หลังเสร็จเมื่อสร้างแล้ว ทั้งหมดเป็น artifact เพิ่มใน R94

การตรวจโครงเอกสารไม่ใช่ผลทดสอบ chatbot ไม่มีคะแนน accuracy ใหม่และไม่มีคำรับรองว่า production-ready เพิ่มจากงานรอบนี้
