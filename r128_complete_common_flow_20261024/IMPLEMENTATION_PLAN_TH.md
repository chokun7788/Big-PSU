# R128 — ทำ Flow ให้ครบตามรายการที่ตรวจพบ

## เกณฑ์เสร็จ

แต่ละรายการต้องมี implementation ที่อยู่ในเส้นทางจริง และหลักฐานการตรวจรับ แยก implemented / verified / unavailable-source ไม่ใช้จำนวนโมดูลหรือ HTTP200 เป็นหลักฐานว่าถูกทั้งหมด

1. Context resolver กลางก่อนทุก domain; state ที่ส่งแล้วและ provenance
2. Active task slots + patch/replace/topic shift/ordinal/pending clarification
3. Canonical entity type / game-definition precedence
4. Coordinated multiple targets และแยก longest alias เฉพาะช่วงที่ทับกัน
5. Explicit target/action/constraint obligations ก่อนส่งคำตอบ
6. Canonical policy binding + source-declared aliases/profiles
7. Canonical operation ส่งเข้า reader ไม่ให้เดา raw query ซ้ำอย่างเดียว
8. Action/button retrieval ก่อน bounded selector และตรวจ relevance
9. Group financial AST / audience overlap / rate equivalence / validity
10. Complete clause family enumeration และ source/event scope
11. Date resolver ไทย/อังกฤษ/เลขคำ/relative weekday + live scoped requests
12. Procedure canonicalization โดยไม่ทิ้งเงื่อนไขหรือสรุป conflict เอง
13. Renderer แยกหมวด + citation descriptors สำหรับ draft/private evidence
14. Model input/context transport contract + bounded outputs/cache และ latency evidence

## ลำดับ

- ทำ shared contracts/context/data projection และ reader/renderer ครบก่อนประเมินภาพรวม
- ตรวจ invariants ที่ interface และ C01-C14 รวม missing/conflicting/withdrawn/invalid/live-unavailable
- รันคำถามเดิม R127 และบทสนทนาเดิมทั้งชุดกับ candidate จริง เก็บ trace/response
- ตรวจ source-add behavior ด้วยฐานทดสอบแยก ไม่แก้ real data/approvals
- แก้ regression ที่พบแล้วตรวจซ้ำเฉพาะกลุ่มที่ได้รับผล จบด้วยชุดตรวจรับรวม
- ส่งมอบ flow, implementation matrix, ผลเทียบเดิม และรายการ source gap ที่ระบบถามกลับอย่างถูกต้อง

Source R125 / original legacy / logs เดิมคงเป็นหลักฐานอ้างอิง Candidate ใช้ common data ที่คัดลอกมาและอ่านจากนั้นเท่านั้น ไม่มี fallback คำตอบธุรกิจจาก legacy
