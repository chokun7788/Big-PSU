# รุ่นปัจจุบัน R105

- Flow และเหตุผลการแก้: [REVISION_FLOW_TH.md](r105_complete_flow_20261020/REVISION_FLOW_TH.md)
- คู่มือเจ้าของข้อมูล: [OWNER_START_TH.md](r105_complete_flow_20261020/OWNER_START_TH.md)
- สถานะการทดสอบ: [STATUS.json](r105_execution_control_20261020/STATUS.json)
- ผลตรวจรวม: `r105_complete_flow_20261020/analysis_integrated04/REPORT_TH.md` เมื่อรันครบ
- ผลทดสอบใหญ่: `r105_complete_flow_20261020/full_analysis/FINAL_REPORT_TH.md` เมื่อรันครบและวิเคราะห์เสร็จ

R102/R103/R104 เก็บ source และผลทดสอบไว้ทุกชุด R105 แก้บนสำเนาแยก ไม่ติดตั้งทับ R78 ไม่เปลี่ยนฐานข้อมูลจริงหรือ approvals

ก่อนทดสอบใหญ่จะตรวจ source/model/config/input freeze และ regression gates จากนั้นรันเฉพาะ common Flow ใหม่ + LLM ON 20,554 unique request keys / 55,811 grades ตัวเลข attempted/completed/strict/content/model transport รายงานแยกกัน

สถานะขณะสร้างหน้านี้: integrated04 กำลังทำงาน Full Test ยังไม่เริ่ม ให้ใช้ STATUS.json เป็นสถานะปัจจุบัน ห้ามถือว่าจบจากหน้านี้
