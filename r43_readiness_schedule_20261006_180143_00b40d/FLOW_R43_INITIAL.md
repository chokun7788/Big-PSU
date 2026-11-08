# Flow r43: เปิดระบบแล้วตอบได้จริง + ตารางอังกฤษครบ

1. สำรองไฟล์และ hash ก่อนแก้ เก็บสถานะ Git; ไม่ทับ log/release เดิม
2. เลือก Python ครั้งเดียว: explicit path → bundled runtime → manifest local binding → PATH/fallback; ตรวจรุ่น/64-bit แล้วส่ง path เดิมตลอด launcher chain
3. ตรวจเว็บเก่า: version + installation + Python identity + warmup + LLM preflight + workers + POST คำถามจริงที่มี oracle ใน source
4. HTTP 200/health ok ไม่ใช่หลักฐานตอบถูก ต้องตอบจำนวนชั่วโมง/ข้อความที่ถูกและไม่ใช่ timeout/no-answer
5. เว็บเดิมที่ผิด identity/ไม่พร้อมต้องรายงานเหตุผล ไม่หยุด process ของผู้ใช้หรือสร้างอีก instance โดยเงียบ
6. Startup ใหม่เก็บ stdout/stderr และ readiness result แยก run ID; เปิด browser หลัง gates ผ่าน
7. ตารางอังกฤษแบบกว้าง render ทุกวันจาก regular_service_slots; ระบุพักกลางวัน maintenance และเงื่อนไข special closure ไม่อ้างความว่างสด
8. Fixture launcher failure/reuse + คำถามตารางหลายรูปแบบ + date/maintenance guards + regressions บริบทเดิมที่เกี่ยวข้อง
9. สร้าง release local ใหม่ immutable; ทดสอบ HTTP จริง และเปิด launcher ซ้ำตรวจ reuse
10. บันทึกผล/ข้อผิดพลาด/ข้อจำกัดและอัปเดต backlog; แยก automated pass จากข้อมูลที่ต้องเจ้าของยืนยัน

## สิ่งที่ไม่ได้รับการพิสูจน์ใน gates นี้

MemoryError มีหลักฐานทรัพยากรระบบตึงและ interpreter ต่างกัน แต่ยังสรุปไม่ได้ว่า Python รุ่นใดเป็นสาเหตุเดียว; readiness ไม่รับรองโหลดพร้อมกันหรือความถูกต้องทุกคำถาม การจองสดยังต้อง oracle จริง และ portable clean-machine ยังต้องเครื่องทดสอบ
