# ขอบเขต wire v3 สำหรับรอบบริการเล่น

`graph_protocol_v3.py` ประกาศ `r135-plan-v3` แยกจาก `r129-plan-v2` โดยเพิ่ม focus/facet `service_periods` สำหรับรอบบริการเล่นที่มีชื่อ เช่น รอบบ่าย การอ่าน `service_slots` ไม่ใช้แทนช่วงเปิดจอง `bookable_periods` เวลาเปิดพื้นที่ `open_periods` หรือสถานะเครื่องว่างแบบสด

V3 มี prompt/schema/parser ของตนเอง ตรวจ version ที่ระบุจริง ไม่รับ v2 โดยปริยาย ใช้ shape adapter เดิมตรวจ task IDs/ทิศทาง shared edges/ข้อความอ้างจากคำถาม โดยไม่แปลง semantic facet ไปเป็น bookable_periods การใช้ vocabulary เพิ่มทำผ่านพารามิเตอร์ที่ระบุชัดของ context validator; ค่าปริยายและข้อความ/schema ของ v2 ไม่เปลี่ยน

คำถามเดิม191 `Please tell me: What time is the afternoon session` สามารถเสนอ `schedule/list/service_periods` ใน v3 แล้วผ่าน compiled executor ไปอ่านแหล่งข้อมูลจริงเจ็ดวันได้ วันศุกร์มีรอบบ่ายเป็น maintenance จึงไม่เท่ากับช่วงเปิดจองของวันศุกร์ ตัวเลขและสถานะมาจาก source หลังประมวลผล ไม่อยู่ใน label ของ planner

ยังไม่มีหลักฐานว่าโมเดลใดสร้างหรือเรียนรู้ v3 และยังไม่เลือก v3 ใน gateway ที่ใช้งานอยู่ Consumer ฝึกรองรับ wire version ที่ระบุชัดใน runtime contract พร้อม hash ของ prompt/schema/implementation แต่ทุก cohort จริงยัง NOT_READY ไม่มีการเริ่ม optimizer เดิม row191 ใน round010 และ cohort v2 ยัง quarantined อยู่

`prepare_protocol_v3_admission.py` สร้าง cohort v3 แยก: ป้าย204ข้อใช้ semantic review เดิมได้หลัง replay การเปลี่ยน version เท่านั้น โดย pin ตัวอย่าง/review ต้นฉบับและตรวจว่า facet, quote, entity, slot, history, family และ provenance ไม่เปลี่ยน ส่วน191มี individual v3 adjudication ใหม่เป็น schedule/list/service_periods พร้อมเหตุผลทั้งเจ็ดข้อและ source revisions เดิม ไม่ใช้ migration ยกเลิก quarantine อัตโนมัติ อีก84ข้อยัง unreviewed และบล็อก READY

V3 cohort ที่แก้การแบ่งข้อมูลแล้วมี132train/73development ไม่มี fresh holdout เทียบสมาชิก281ข้อกับไฟล์ train/validation/test เดิมจริง ไม่ใช้ split tag ใน proposal ต้นทาง เมื่อเริ่มทำพบว่า proposal round011 มี train tags ค้าง จึงเก็บ cohort แรกที่ผิดไว้เป็นหลักฐาน (ไม่มี READY/optimization) และแก้ builder/gate ให้ใช้ final saved-file membership ห้ามย้าย old validation/test ไป train ผ่าน migration หรือ manual readmission

`verify_protocol_v3_admission.py` ตรวจ29 controls: ยอมรับ review เดิมเฉพาะ version-only proof, ปฏิเสธการเปลี่ยน facet/operation/slot/quote/input/family/provenance, wrong hashes/versions/splits, การปลอม accepted แทน quarantine และการปะปน v3 กับ runtime v2 ตรวจ consumer จริงว่า84 unreviewed หยุดก่อน import model frameworks ป้าย205ข้อที่ตรวจแล้วจึงไม่ถูกนับเป็น semantic review ใหม่204ครั้งเพียงเพราะเปลี่ยน protocol

การวัดสามแขนต้อง freeze accepted versions/parser/prompt/schema/compiler เหมือนกันทุกแขน ถ้าฝึกพร้อมเปลี่ยน protocol ต้องระบุผลร่วมของ protocol adaptation กับ supervision และแยก structural failure จาก semantic failure ผล v2/raw R132 ที่เก็บไว้ไม่ใช่การวัด v3 และห้ามสร้าง raw หรือ teacher provenance ทดแทน

G115 ยังเปิด: ต้องตรวจอีก84ข้อและ context transforms ที่เหลือ ตรวจ semantic family/eight strata/freeze metrics แล้วจึง actual optimization/model provenance/evaluation อีกทั้ง mapping ประกาศปิด/เปลี่ยนเวลาไปยังรอบบริการยังไม่ครบ งานทั้ง76ข้อ/14หมวดและ final installation/re-audit ยังไม่จบ
