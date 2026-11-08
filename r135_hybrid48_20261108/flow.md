# R135 รุ่นทดลองแบบผสม — Flow และวิธีตรวจรับ

## เป้าหมายและขอบเขต

ใช้แกน R135 กับ reader algorithm ของ R134 ใน snapshot/budget/renderer/verifier เดียวกัน เพื่อให้ทดลองตอบและปรับข้อมูลได้ โดยยังไม่อ้างว่าปิด requirement ครบ 48 หรือ 76 ข้อ

ชุด 48 หมายถึง `requirement_specific_review_ids` ใน STATUS เดิม ไม่ใช่48แถวแรก: FLOW-04–07, FLOW-09–21, C01–14, CONTRACT-02–15 และ PHASE-07–09 ส่วนพึ่งพาจากอีก28ข้อยังต้องรักษา ดู REQUIREMENT_MAP.json สำหรับข้อความเดิมครบ76ข้อ ไม่แก้สถานะตรวจรับเดิมให้เสร็จเอง

## การประกอบและเส้นทาง

1. สำเนา R135/system จากต้นทาง พร้อม SQLite online backup รวม committed WAL; ไม่คัดลอก token/log/session จริง
2. BASELINE_MANIFEST.json เก็บไฟล์ตั้งต้นและ hash; การแก้เกิดเฉพาะโฟลเดอร์นี้
3. hybrid_routes.json ระบุ category/operation/field ก่อนอ่าน: r135, r134_compat หรือ withhold สำหรับรายการที่ไม่ลงทะเบียน
4. R134 compatibility คือ plan algorithm ที่ดึงจากไฟล์ R134 จริง แต่ใช้ current R135 helpers/index; ไม่อ้างว่าเหมือนรัน R134 ทั้งระบบ
5. เริ่มเส้นทาง R134 เฉพาะ C03/detail/device_type พร้อมผลตรวจ source positive/edit/withdraw/wrong-entity; ความสามารถอื่นใช้ R135 และต้องผ่าน runtime receipts เช่นเดิม
6. ไม่ลอง reader อีกตัวหลัง fatal/source mismatch/conflict/expiry ไม่เพิ่ม model call/snapshot แยก
7. Native calendar/live/source-special paths คงสัญญาตรวจเดิม และบันทึกว่าเป็น native path; route metadata ที่ไม่ปรากฏไม่ใช่หลักฐานว่ารัน R134

## Flow ของคำถาม

รับ raw question → pin snapshot/เวลาไทย/runtime identity → วิเคราะห์ needs → ผูก entity/local slot/shared context → สร้าง obligations → เลือก reader → deterministic read → limited shared model budget → verify source/target/units/coverage → terminal state → ตอบคำตอบหลักก่อนเงื่อนไข/ส่วนเสริม → final request coverage check → automatic log

- แยก price+booking/address+booking เป็นคนละ need; เป้าหมายและจำนวนคนต้องมีเจ้าของ
- ถ้าข้อมูลจำเป็นกำกวมให้ถามเฉพาะช่องที่ขาด ไม่เลือกชื่อใกล้กันเอง
- ถ้าตอบบางส่วนได้ให้รักษาส่วนนั้นและแจ้งส่วนที่ยืนยันไม่ได้
- provider/model failure แยกจาก missing_source และ HTTP success แยกจากความถูกต้อง
- ไม่ผูก FAQ operator เข้าศูนย์ด้วย regex อย่างเดียว กรณีไม่มี target/authority binding คง unknown
- ราคา/ยอดรวมตรวจ source amount, currency, duration rule, audience/person count และ rendered total; independent bounded check ไม่เรียก financial.billing/unit_calculation
- ตัวตรวจ independent รองรับ explicit numeric quantities ตามชุดทดสอบ ภาษา/รูปแบบที่ไม่รองรับยังไม่เป็น semantic proof
- total request ที่ไม่มี verified computations ต้องมี notice; ordinary unit price ไม่ถูกบังคับให้มี headcount
- ตาราง play-service, building hours, booking windows และ live availability เป็นข้อมูลคนละชนิด

## Flow เพิ่ม แก้ ถอนข้อมูล

owner draft → schema/relations validation → approvals ตามเดิม → revision/epoch ใหม่ → snapshot ใหม่ → คำตอบอ่านฉบับใหม่

ทดสอบ add/edit/withdraw ในฐานสำเนาเท่านั้น ตรวจทั้งข้อความ claims/receipts/caches เมื่อแก้ข้อมูล confirmation เดิมอาจใช้ต่อไม่ได้ ห้ามยกระดับ draft เป็น published อัตโนมัติ การรันทดลองใช้ DraftSnapshotView/preview จึงไม่พิสูจน์ authority หรือ production approval

## วงรอบ audit → แก้ → ตรวจ → re-audit

กลุ่ม A: intent/entity/compound/direct-answer; กลุ่ม B: price/booking/calendar/live; กลุ่ม C: source lifecycle/compatibility; กลุ่ม D: all14 categories/list/count/compare

แต่ละกลุ่ม: เก็บ failure เดิม → ระบุ root cause และ affected dependencies → แก้หนึ่งชุด → positive+negative+affected regressionหนึ่งรอบ → อ่านคำตอบ+claims+receipts+terminal stateจริง → รวมถ้าผ่าน

แนวทางเดิมล้มสองรอบต้องเปลี่ยนวิธี ถอน หรือพัก capability; ไม่วน unchanged และไม่เพิ่มแต่ negative tests ชุดfocusedที่ยอมรับ missing_source ได้เป็นเพียง bounded controls ไม่ใช่ proof ว่าหมวดนั้นตอบได้ครบ

FOCUSED_BATCH.json เก็บทุก exit code/stdout/stderr รวม harness failures แยกจาก behavior failures ไม่ลบความล้มเหลวเก่าและไม่เขียนทับผลรอบเดิม

## Gate และรอบ 5%

ก่อนรัน: focused critical checks ผ่าน, positive ยังส่งคำตอบได้, เพิ่ม/แก้/ถอนผ่าน, forced wrong entity/forged total/output ถูกปฏิเสธ, partial มี notice, API smoke ใช้ build/profile/DB ที่ถูกต้อง, UI ระบุรุ่นทดลอง

รัน manifestเดิม1056ข้อใน evaluation/SELECTED_5_PERCENT_v2.jsonl หนึ่งรอบหลังรวมแก้ ตรึง code/config/source manifest ก่อนวัด ไม่แก้ runtime ระหว่างวัด ไม่เริ่มซ้อนและไม่ retry เงียบ ไม่ rerun/regrade R132

คะแนน literal รายงาน matched/not_matched/unassessed พร้อมตัวหาร เกณฑ์ที่ไม่ตรวจแยกไว้ เทียบ saved R134 ตาม key เดียวกันแบบ observational เนื่องจาก source/time/backendต่างกัน ไม่เรียกว่า semantic accuracy และ C07มีเพียง1ตัวอย่าง ใช้ controlled tests เสริมแยกคะแนน

หลังรอบรวมจัด failures เป็นกลุ่ม source/harness/model/implementation แล้วแก้เฉพาะสาเหตุร่วม ก่อนรัน5%ใหม่ต้องมีการเปลี่ยนที่กระทบระบบจริง

## การใช้และส่งมอบ

ใช้ bundled Python 3.12.14 ที่ระบุใน manifest ไม่ติดตั้งแพ็กเกจเพิ่ม ไม่ใช้subagents ไม่หยุดprotected model รุ่น R135เต็มเก็บไว้และพักการแก้ระหว่างรุ่นผสม

แชตและ editor รุ่นทดลองมีฐานข้อมูลและ logs ของตนเอง ใช้ portว่างที่กำหนด ไม่หยุด process ที่ครอบครอง port คนอื่น การติดตั้งแทนของจริงต้องผ่าน gatesเดิม/backupรวมWALและrollback; รอบนี้เป็น isolated trial

รายงานทุก6ชม: สิ่งที่เปลี่ยนจริง หลักฐานใหม่ blockers next action และสถานะ eval ไม่อ้างทำงานต่อเนื่องระหว่างรอบ ไม่สร้างcompletionเปอร์เซ็นต์เอง
