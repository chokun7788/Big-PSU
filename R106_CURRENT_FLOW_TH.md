# รุ่นล่าสุด R106 — ตรวจ Flow และรัน Full Test

- [แผนและเหตุผลการแก้สุดท้าย](r106_complete_flow_20261020/FINAL_REVIEW_TH.md)
- [Flow ฉบับละเอียด](r106_complete_flow_20261020/REVISION_FLOW_TH.md)
- [วิธีเปิด/เพิ่ม/แก้ข้อมูล](r106_complete_flow_20261020/OWNER_START_TH.md)
- [สถานะจริงล่าสุด](r106_execution_control_20261020/STATUS.json)
- [ผลตรวจรอบสุดท้าย](r106_complete_flow_20261020/final_gate/REPORT_TH.md) เมื่อรันครบ
- Full Test report: `r106_complete_flow_20261020/full_analysis/FINAL_REPORT_TH.md` เมื่อรันครบและวิเคราะห์เสร็จ

R105 ตรวจรวม 19 lanes เป็นฐาน R106 แยก source ใหม่และตรวจสาขาที่แก้ซ้ำ พร้อม source/input/model freeze ก่อน Full Test common-only LLM ON 20,554 unique request keys / 55,811 grades ไม่ใช้ผล partial อ้างว่าครบ และไม่รวมหน่วย checks ต่างชนิดเป็น accuracy เดียว

R78/R101 และข้อมูลจริง/approvals/logs เดิมไม่เปลี่ยน Candidate ยังไม่ได้ติดตั้งแทน production ชื่อ launcher และ build protocol บางส่วนคง R102 เพื่อ compatibility แต่ใช้ system ภายในโฟลเดอร์ R106 นี้จริง
