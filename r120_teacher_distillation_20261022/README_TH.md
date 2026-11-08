# ลำดับไฟล์การทดลอง R120

อ่านผลสรุปใน `FINAL_REPORT_TH.md` เมื่อ `STATUS.json` เป็น `pilot_review_complete`

| ไฟล์/โฟลเดอร์ | ความหมาย |
|---|---|
| PLAN_TH.md | แผน ขอบเขตและข้อจำกัดของการทดลอง |
| FLOW_DISTILLATION_TH.md | Flow และสิ่งที่ถ่ายทอดจาก teacher |
| teacher01 | Legacy R64 ที่รันจริง 64 ข้อ |
| TEACHER_REVIEW.json | ตัวกรองอัตโนมัติขั้นต้น 64 ข้อ ยังไม่ใช่ผลตรวจสุดท้าย |
| TEACHER_MAPPING_REVIEW.json | ผลตรวจ mapping สุดท้าย ใช้ได้ 60 ข้อ คัดออก 4 ข้อ |
| TEACHER_LESSONS.json | ตัวอย่างแผน 60 ข้อหลังตรวจ ไม่มี teacher business answers |
| baseline01 | R119 API 27 ข้อก่อนแก้ |
| student01 / regression01 | R120 revision01 บน 27 / 48 ข้อ |
| student02 | 27 ข้อหลังแก้ regressions ไม่ใช่ holdout ใหม่ |
| student03 / regression03 | Candidate สุดท้าย 27 / 48 ข้อ รวมรูปแบบคำตอบ |
| INITIAL_SAVED_COMPARISON.json | ผล initial pilot ก่อนใช้ evaluation มาปรับ code |
| SAVED_COMPARISON.json | ผล candidate สุดท้าย ระบุ revision และสถานะ partial |
| PER_REQUEST_COMPARISON_TH.md | คำตอบก่อน/หลังและ execution/source receipts รายข้อ |
| HISTORICAL_SNAPSHOT_VERIFICATION.json | ตรวจ snapshot รุ่นก่อนตรงกับ run freeze |
| system | Candidate ปัจจุบันในโฟลเดอร์ทดลอง ยังไม่ติดตั้ง production |
| revision01_system / revision02_system | Source ของ candidate รุ่นก่อนแก้ |

ทุกชุดใช้คำถามที่มีอยู่แล้ว ไม่มีการเพิ่ม benchmark questions ไม่มีการฝึกน้ำหนักโมเดล และไม่มีการใช้คำตอบ teacher เป็น facts ของ student

สคริปต์เตรียมและรันเก็บไว้เพื่อ audit หลายสคริปต์ตั้งใจปฏิเสธเมื่อ output folder มีอยู่แล้ว อย่ารันทับ artifacts เดิม หากจะทำการทดลองใหม่ควรใช้โฟลเดอร์และ run IDs ใหม่
