# งานที่ต้องทำต่อจนกว่าจะครบ

ผู้ใช้สั่งทำ Flow ใหญ่ให้ครบ และ Full Test เฉพาะ Flow ใหม่ LLM ON ไม่มีการลดขอบเขตเป็นตัวอย่างไม่กี่เคส

## สถานะที่ยืนยันได้

- R129 runtime แยกจาก R128, ตรวจสัญญา task/shared context/provenance/result/gateway เพิ่มแล้ว
- ชุดสอน review ครบ 289, แก้ 53, quarantine 8
- รอบใช้จริง training_v2: 154 train / 17 validation / 110 retained test; ฝึกเสร็จจริง 60 optimizer steps, frozen base unchanged
- รอบฝึก root/train01 ไม่รับเพราะ original family ข้าม split เก็บ NOT_ACCEPTED_SPLIT_REVIEW.json ไว้
- พิสูจน์ profile base/retained/new จริงแล้ว backend 12921, manifest MODEL_IDENTITY_BEFORE.json
- Pilot three_arm01 ไม่รับหลัง 2 ข้อ เพราะตัววัดข้าม fallback เมื่อ JSON ไม่ผ่าน ไม่ใช้เป็นคะแนนเปรียบเทียบ
- three_arm02 เป็นรอบที่ใช้จริง แก้ตัววัดใน compare_planners_v2.py ไม่แก้ frozen system นำ raw transport 2 ข้อมาใช้ซ้ำโดยไม่ generate ใหม่
- Controller continue_execution.py ปัจจุบันดู STATUS.json และ SUPERVISOR_PROCESS.json; error log เก่ารุ่นแรกไม่ใช่สถานะ process ใหม่
- เมื่อ 330 ผลครบ comparator รอ PLANNER_ADJUDICATION.json ทุกกรณี ไม่ต้องขอ approval ผู้ใช้ งานนี้เป็นการ review ของ agent

## ข้อพบใหม่ที่ต้องแก้ก่อน Full Test

อ่าน REQUIRED_PRE_FULL_FIXES.json ก่อน ห้ามปล่อย R129 Full Test โดยอัตโนมัติเพียงเพราะ JSON/คะแนน planner ดีขึ้น

Owner50 ข้อ 12 (มากันสองคน) และข้อ 13 (แนะนำเครื่องเมื่อมาสี่คน) อยู่ในเอกสาร intake แต่คำแนะนำไม่ได้เป็น record ที่อ่านได้ใน active snapshot ปัจจุบัน การไม่มี game_mode ไม่ได้แปลว่าไม่มีคำแนะนำที่ตอบได้เลย

ต้อง audit ทั้ง 50 รายการโดยเทียบ SOURCE_OWNER_50, PREFILL_PAYLOAD, R109 SOURCE_STATE และ current active records แยกคำยืนยัน/คำแนะนำ/คำตอบมีเงื่อนไข/คำสั่งให้ค้นต่อ/ส่วนยังไม่ทราบ ห้ามยกคำแนะนำสองคนเป็นการยืนยัน split-screen/co-op/players_max หรือเดารุ่น Naruto/SF6 ที่ไม่ได้ระบุ

ทำใน r130_owner_context_completion_20261025 โดย copy frozen R129 system เป็น candidate ใหม่ ไม่แก้ R129 ที่กำลังวัดหรือข้อมูล/approvals เดิม หลังแก้ source/executor ที่จำเป็น ให้ replay raw planner outputs ที่เก็บไว้บน engine/data ของ candidate ใหม่เหมือนกันครบสามแขน (ไม่ต้อง generate planner ใหม่ถ้า messages/schema/weights/precision/decoding เหมือนเดิม) นับ planner call ที่ replay ว่าใช้งบแล้ว 1 ครั้ง; fallback base ที่จำเป็นยังต้องเก็บ actual calls ตามจริง

P7 ของ R129 ยังเดินต่อได้เพื่อเก็บ raw output ทั้ง 330 และรักษาการทดลองเดิม แต่ไม่เขียน PLANNER_ADJUDICATION ให้ controller เริ่ม full ของ R129 ก่อนจัดการข้อพบนี้ เลือก Flow ใหม่ที่ครบกว่าเป็นตัวที่ Full Test จริง 20,554 keys / 55,811 grades แล้ววิเคราะห์ทุกกลุ่มตามคำสั่งเดิม

## รายงานคะแนน

- Saved original legacy R64 ครบ 20,554 keys / 55,811 grades, strict 42,601; ไม่รัน baseline ใหม่
- SAVED_LEGACY_REFERENCE.json และ SAVED_LEGACY_ROWS.jsonl.gz รีดจาก saved responses เท่านั้น
- รายงาน R64 เดิมแบ่งภาษาตาม effective locale อย่าเทียบตรงกับ requested locale; มี rebucket requested ไว้แล้ว
- reconcile_saved_scores.py เตรียมไว้สำหรับอ่าน full ผลใหม่ภายหลัง เปรียบเทียบ fixed literal eligibility จาก frozen inputs พร้อม unassessed แยก ไม่ตัด execution failures ออกจากตัวหารจนคะแนนดูดี
- Strict, literal clause mismatch, validity/source gaps, protocol, model transport และ semantic content failure ต้องแยกกัน ไม่เหมารวม keyword fail เป็น semantic ผิด
- Candidate ยังไม่แทน R78; real live provider unavailable ใน workload เป็น fixture ไม่ใช่สถานะจริง

ยังไม่ประกาศว่าทำครบหรือให้เปอร์เซ็นต์เสร็จจากการมีโมดูล ต้องปิด original P0–P8 / R00–R12 / C01–C14 พร้อมหลักฐานและข้อจำกัดจริง
