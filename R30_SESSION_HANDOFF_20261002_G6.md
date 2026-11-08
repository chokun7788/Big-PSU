# ส่งต่อหลังพัฒนา r30 G6 — 2 ตุลาคม 2026

## สถานะใช้งาน

- เว็บ: http://127.0.0.1:8090/ รุ่น `2026.10.02-full-improvement-r30-G6`
- Launcher ของงานนี้ PID 41092; ตรวจ command line/พอร์ต/ต้นไม้ process ใหม่ก่อนหยุดเสมอ เพราะ PID เปลี่ยนหรือถูกใช้ซ้ำได้
- บันทึกเริ่ม: `web_chat_runs/r30_ready_8090_a517ce050d.json`
- เว็บทดสอบ 8091 หยุดแล้ว; เก็บแพ็กเกจและ logs ทุกชุดไว้
- แพ็กเกจล่าสุด: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261002_full_improvement_r30_G6\PSU_Esports_Chatbot_Local`
- หลังปิดเครื่อง เปิด `Open-PSU-Esports-Chatbot.cmd` ในแพ็กเกจล่าสุดนี้

## ไฟล์หลัก

- โปรเจกต์: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data`
- Flow: `docs/130_full_improvement_r30_flow_20261002.md` revision 4
- รายงาน: `reports/r30_full_improvement_20261002_020311_6374c0/FINAL_RESULTS_TH.md`
- หลักฐานทั้งหมดอยู่โฟลเดอร์รายงานเดียวกัน; รายการและข้อจำกัดในรายงาน/Flow

## ผลที่ตรวจจริง

- G6 รันใหม่ครบ 20,327 unique inputs / 55,583 grades; coverage/provenance audit แยกแก้คำอธิบาย template ใน raw summary โดยไม่แก้ raw
- API จริง 8091: 903/903; หลังสลับ 8090: 53/53; live path/guard 44/44
- WordPress สดสำเร็จ 8/8 ครั้ง fetch 813–2313 ms; ยังไม่มี booked/free oracle จริงตามคำขอพักเก็บข้อมูล
- Unit 424/425: failure เดิม frozen EN metadata 6 แถวไม่ตรง builder; ไม่มี errors/skips
- Smoke 71/85; เก็บ 14 failure logs และรายละเอียด ไม่เหมารวมเป็นเกณฑ์เก่าทั้งหมด
- Guard action 500/500 แต่ exact flags 471/500; repeat FN27/FP2 ไม่ใช่ answer accuracy
- Paired V2 clean 1740/2000, noisy 1640/2000; clean-pass/noisy-fail 117 คู่
- Extra competition 970 requests / 981 grades; human review 120 ไม่มี oracle คน ไม่ใช่ความแม่นยำ
- Protected data/booking 584 ไฟล์คงเดิม, original snapshots 248 ตรวจตรง, original tests/Gold ไม่ถูกแก้; ไม่มี reset/stash/log deletion

## เริ่มต่อจากไหน

1. P1 source-backed matcher failures: สำนวน `สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน` และ bare `timeout` ร่วม `freeze time` ยังผิดจริง; อ่าน `CONFIRMED_REMAINING_G6_CASES.json` กับ `REMAINING_G6_PRIORITY_AND_FLOW_TH.md` ก่อนแก้
2. Content/proposition ledger ทั่วไปและ noisy regressions 117 คู่; แยก raw target/action/condition/negation/quantity/time และตรวจคำตอบครบ ไม่เพิ่ม whole-question aliases เป็นหลัก
3. ทบทวน Gold/heading/mode/source ID รายข้อโดยทำ overlay ใหม่ ห้ามแก้ frozen เพื่อให้ผ่าน
4. Source gaps/conflicts ต้องถามผู้จัดตามรายการใน Flow; ห้ามแต่งนโยบาย/edition/ราคาหรือวันจัดใหม่
5. Load queue/503 ต้องตรวจแยกจาก idle 10/10 และ WordPress transport; ไม่ลด global thresholds หรือเพิ่ม workers โดยไม่วัด

ยังไม่ได้แก้ข้อ P1 สองข้อใหม่ดังกล่าวใน G6; อย่าอ้างว่า Flow ทุกส่วนหรือทุกคำถามถูกแล้ว สิทธิ์เขียนโปรเจกต์เคยอนุมัติในรอบนี้ แต่รอบใหม่ถ้าสิทธิ์ไม่พอให้ขอผ่านระบบก่อนแก้ ไม่ spawn subagents เว้นแต่ผู้ใช้หรือ instructions ที่ใช้จริงระบุ
