# ข้อผิดพลาดของตัวตรวจที่เก็บแยกจากแอป

1. baseline01: KeyError records ก่อนส่ง request เพราะ CommonStore.snapshot ไม่คืนโครงสร้างที่ตัวตรวจคาด แก้ setup แล้วรัน baseline02 โฟลเดอร์เดิมไม่ถูกใช้ซ้ำ
2. baseline02: ตัวตรวจมอง response.hits ทั้งที่ public API ใช้ sources และ common plan/projection จึงมี false failures 4 ข้อ เก็บ raw 20/29 และ regrade saved responses เป็น 24/29 ใน BASELINE_ORACLE_REVIEW.json ไม่ส่ง requests ใหม่หรือแก้ log เดิม
3. SCOPE_GUARDS.json: ตัวตรวจเรียก price_selection ด้วย raw snapshot names แต่ caller จริงส่ง derived_names(scoped_names(...)) จึงเกิด false failure PC ปรับ setup ให้เหมือน caller และเก็บ SCOPE_GUARDS_REVIEWED.json 14/14 โดยไม่แก้ production logic ในการทบทวนนี้

ข้อผิดจริง 5 turn ใน baseline คือ follow-up อุปกรณ์ EN/TH, เลือกเกมหลังถามแข่งขัน, คำถามราคากว้าง และทั้งหมดที่ต่อจากคำถามราคานั้น แก้ใน system สำเนา R78 เท่านั้น
