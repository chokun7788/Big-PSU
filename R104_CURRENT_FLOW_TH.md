# Flow ที่กำลังพัฒนาและทดสอบ

รุ่นปัจจุบันของงานนี้คือ **R104** ใน `r104_complete_flow_20261020` แยกจากระบบ production และรุ่นก่อนหน้า

- แผน Flow และรายการแก้: [REVISION_FLOW_TH.md](r104_complete_flow_20261020/REVISION_FLOW_TH.md)
- วิธีเปิด/เพิ่ม/แก้ข้อมูล: [OWNER_START_TH.md](r104_complete_flow_20261020/OWNER_START_TH.md)
- ข้อมูลจริงที่ยังไม่พร้อม: [REAL_DATA_READINESS_TH.md](r104_complete_flow_20261020/REAL_DATA_READINESS_TH.md)
- สถานะการรัน: [STATUS.json](r104_execution_control_20261020/STATUS.json)
- ผลตรวจรวมก่อน Full Test: `r104_complete_flow_20261020/analysis_integrated03/REPORT_TH.md` เมื่อวิเคราะห์เสร็จ
- ผล Full Test: `r104_complete_flow_20261020/full_analysis/FINAL_REPORT_TH.md` เมื่อรันครบและวิเคราะห์เสร็จ

## ลำดับการรันที่ตั้งไว้

1. ตรวจรวมทุก lane จาก source ที่ freeze แล้ว
2. ถ้า safety/regression gates ยังไม่ผ่าน ให้เก็บผลและหยุดก่อน Full Test เพื่อแก้เป็นชุด
3. เมื่อผ่าน gates จึงรัน **common-only + LLM ON** 20,554 request keys / 55,811 grades
4. ตรวจ key coverage, grade coverage, source/config unchanged แล้วสร้างรายงาน

ผลระหว่างทาง:

- R102 acceptance: 265/444
- R103 acceptance: 399/444 แต่ยังมี regression gates ไม่ผ่าน จึงไม่ปล่อย Full Test ต่อ
- R104: กำลังตรวจรวม ให้ดูสถานะจริงจาก STATUS.json

คะแนนข้างต้นเป็น automated acceptance variants ไม่ใช่ความแม่นยำของคำถามผู้ใช้ทั้งหมด มีการแก้ oracle C07 ที่เดิมบังคับถามเงื่อนไขซึ่งต้นทางไม่ได้ระบุ รายงานแยกเคสนี้ในการเปรียบเทียบ

R78/R101/source data/approvals/logs เดิมคงไว้ ไม่ได้ติดตั้ง candidate แทน production และยังไม่ได้อ้างว่า Full Test เสร็จ
