# ผลการประกอบ R135 รุ่นทดลองแบบผสม

แชตทดลอง: http://127.0.0.1:8125/ — editor 8126 ใช้ฐานสำเนาของตนเอง
เซิร์ฟเวอร์ประเมิน: 8127 — ฐานข้อมูล snapshot แยกจาก editor

- เอกสาร flow.md และ REQUIREMENT_MAP.json เก็บการใช้ชุด48 historical IDs และส่วนพึ่งพาจากข้อที่เหลือ โดยไม่ปิดข้อกำหนดเดิมเอง
- ลงทะเบียนเส้นทาง104 category/operation/field; R134 ใช้เฉพาะ C03/detail/device_type ผ่าน shared R135 helpers/index/renderer/verifier ไม่อ้างว่าเป็นR134ทั้งระบบ
- เพิ่ม bounded independent calculation checks, direct output-total tamper checks, missing-total notice และ source-specific person bounds ที่ไม่จับบริการต่างกันด้วย platform เดียว
- ผ่าน controlled lifecycle/forgery และ actual owner/chat HTTP add→edit→withdraw ของ synthetic record แยก ไม่มีการยืนยัน authority ของธุรกิจ
- เก็บ failed attempts และ harness amendments ครบ ตัวทดสอบเก่าบางส่วนตั้งเป้ากว้างกว่าพฤติกรรมที่guardตั้งใจอนุญาต ไม่ได้นำการปรับ assertion มาอ้างเป็นproduction fix
- แยก30คำถามที่ literal ต่างจากR134 เป็นsource/runtime/clarification/formatting/content triage ยังไม่ให้semantic score
- known limits: operator FAQ ยังไม่มีcenter/authority binding; mechanical subtype definitionยังระงับ; range labelsยังไม่พิสูจน์group allocation; all14 bounded lanesไม่ใช่การรับรองทุกoperation
- รันทดสอบ5%จากmanifestเดิม1056คำถามหนึ่งรอบ ผล literal/transport/unassessedแยกจากsemantic correctness

เปิด RESULTS_VIEW.html เพื่อดูผลโดยไม่ต้องเปิด JSON โดยตรง หลัง evaluation/PROGRESS.json running=false ให้ตรวจผลดิบ จำนวนแถว scores และข้อผิดพลาดก่อนสรุป รุ่นนี้ยังไม่แทนตัวใช้งานจริง และR135เต็มยังเก็บไว้
