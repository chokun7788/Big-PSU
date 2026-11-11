# แยกสาเหตุสถานะไม่พร้อม — 11 พฤศจิกายน 2026

รอบนี้ตรวจกลุ่ม15คำถามที่ผล200ถูกติดรหัส `store_or_snapshot_unavailable` โดยอ่านmetadataเดิมทั้งหมดและตรวจเส้นทางจริง ไม่รัน200ซ้ำ ไม่แก้ผล/โค้ด/DBสำเนาที่วัดแล้ว

## พบสาเหตุของการติดรหัสผิด

ทั้ง15มีquery method `r101_model_unavailable` ไม่มีstore_error_typeบันทึกไว้:

- 13มี `OSError: model_admission_unavailable` พร้อมrequest-context eventยืนยันว่าhealth gateของ `r129_context_understanding` อยู่ในcooldown หลังบันทึกtimeout2ครั้ง เป็นkind_only ไม่ใช่หลักฐานว่าโมเดลทุกเส้นทางปิด และไม่ได้ส่งinference HTTPในจุดที่ถูกปฏิเสธ
- อีก2มี `TimeoutError: timed out` ที่ขั้นตีความคำถาม ไม่ใช่ข้อผิดพลาดอ่านSQLiteตามหลักฐานที่มี
- ตัวแปลง `common/result_contract.py` เดิมเหมารวมresponse unavailable/retryเป็นstore/snapshot failure จึงทำให้reason codeชวนให้เข้าใจว่าฐานข้อมูลเสีย

หลักฐานสรุป `store_unavailable_attribution_20261111/AUDIT.json` ข้อความและรายละเอียดรายคำถามเก็บlocalในDETAILS.json ไม่ใช้รหัสเดิมตัดสินสาเหตุจริง

## แก้ในworking candidate

- ให้เหตุผลตามที่บันทึกจริง:store_error_typeหรือsnapshot read failureยังเป็นstore/snapshot; r101แยกadmission unavailable/timeout/interpretation unavailable; retryเป็นsnapshot changed; เหตุไม่ทราบแหล่งไม่เรียกว่าDBเสีย
- ปรับneed-result rowsที่สร้างก่อนunderstanding eventเข้ามาให้ใช้เหตุที่มีหลักฐานภายหลัง ไม่เปลี่ยนfailureเป็นsupported ไม่เติมclaims ไม่เปลี่ยนคำตอบ
- ยังไม่ได้แก้สาเหตุที่ทำให้timeout/เข้าcooldown ไม่ปิดhealth gate ไม่เพิ่มdeadline/concurrency ไม่หยุดprotected model และไม่ได้โหลดแพตช์นี้เข้าpreview8141ที่เปิดอยู่เดิม

## ตรวจ

`unavailable_attribution_1794397917471345400/RESULT.json` ผ่าน20checks:replay15caseเดิม พร้อมexplicit store-error/snapshot/retry/unknown-provider metadata controlsและจำนวนcaseตรง รักษาสถานะtemporary_failure คำตอบและproofว่างไว้ ไม่มีmodel/HTTPใหม่

การตรวจวินิจฉัย3คำถามแบบsource-onlyและallow_llm=Falseไม่เกิดexceptionอ่านDBและได้clarification จึงไม่ใช้ผลนี้อ้างว่าปัญหาadmissionถูกแก้แล้ว ครั้งแรกใช้sys.settraceกว้างเกินไปและครั้งถัดมายังรบกวนเวลา จึงหยุดเฉพาะprocessdiagnosticของรอบนี้ตามcommandlineที่ตรวจแล้ว เปลี่ยนเป็นจับexceptionผ่านconstructorในexceptแทน ไม่หยุดappหรือmodel เก็บโฟลเดอร์attemptไว้

คะแนน196/255และ36unavailableในผลวัดเดิมคงเดิม ไม่มีคะแนนระบบใหม่จากการเปลี่ยนreason labels งานถัดไปคือตรวจงบ5วินาที/เวลาอ่านcontextและเหตุtimeoutที่ทำให้เข้าcooldownด้วยpositive controlsและruntime receiptsจริง ก่อนเลือกปรับpolicyใด ๆ
