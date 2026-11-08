# ลูป F — ให้ข้อมูลใหม่ตอบได้เมื่อคำถามระบุอุปกรณ์เดิม

ปัญหาเชิงโครงสร้าง: หากคำถามมีชื่อเครื่อง ตัวอ่านอาจหยุดที่ service/resource แม้เรื่องที่ถามอยู่ใน policy/FAQ/procedure ใหม่ การเพิ่มคำตอบเจาะจงรายหัวข้ออย่างเดียวไม่แก้เรื่องนี้

## Flow

1. Resolve เครื่อง/เกมตามเดิม หากถาม live หรือ schema field ที่ target เป็นเจ้าของ ให้ใช้เส้นทางนั้น ไม่ใช้ FAQ หลบ unknown/withdrawal/validity
2. เมื่อ target เดิมไม่มี attribute ที่ถาม ค้นบทความที่มี scope ยืนยัน: FAQ.related_ids, policy.conditions_all ที่อ้าง ID หรือ global ที่ประกาศชัด, procedure.preconditions และชื่อ scope ที่ไม่ขัดกัน
3. ตาม declared graph ไป service/resource/zone/model; ไม่เดา FK จากชื่อคล้าย และไม่ยอมให้ scoped source ของเครื่องอื่นข้ามมา
4. ถ้ามี candidate เดียวที่ topic ตรงชัด ใช้ deterministic retrieval; ถ้าไม่ชัด เปิด LLM เลือกได้เฉพาะ candidate IDs ที่ผ่าน scope guard แล้ว
5. ตรวจ topic หลังตัดชื่อ target ออกจากคำถามด้วย เพื่อไม่ให้แค่คำว่า PC ทำให้ policy ทุกเรื่องถูกเลือก
6. อ่าน answer ของ FAQ, decision/details/conditions/exceptions ของ policy หรือ steps/preconditions/documents ของ procedure จาก source; ไม่มี facts ที่โมเดลสร้าง

## ทบทวน 1

ห้าม scalar price ไม่มี target เลือก damage FAQ; ห้าม secondary topic lookup หลบ field ที่เจ้าของระบุ unknown หรือถอนแล้ว ข้อมูลราคา/live/control/rule ใช้เส้นทางเฉพาะก่อน

## ทบทวน 2

scope ของ policy ที่ประกาศเครื่องอื่นต้องถูกกรองก่อน model แม้ชื่อ topic คล้ายกัน คำหัวข้อที่เหลือหลังตัดชื่อเครื่องต้องยังตรง source ไม่ใช้ชื่อเครื่องเป็นหลักฐานว่าเจตนาถูก

## ทบทวน 3

ทดสอบข้อมูลจำลองแยกจาก production โดยใส่ FAQ/policy ใหม่ที่เกี่ยวกับเครื่องเดิม และให้เครื่องอีกตัวมีคำตอบตรงข้าม ตรวจ OFF/ON, paraphrases, unsupported topic และหลายภาษา ไม่ถือ canonical all-details 480 ข้อเป็นหลักฐานว่าคำถามเกี่ยวกับข้อมูลใหม่ได้ทุกแบบ

## ผลตรวจ implementation ที่นำกลับมาปรับ Flow

1. Resource ที่ใช้ร่วมกันไม่ใช่หลักฐานให้ FAQ ของ service พี่น้องใช้แทนกันได้ Reverse resource→service ทำเฉพาะ resource ที่ผู้ใช้ resolve ตั้งต้น ไม่ทำหลังเดินจาก service ลง resource
2. Procedure.preconditions เป็น typed conditions เช่นเดียวกับ policy.conditions_all ต้องตรวจ service_id/resource_id/zone_id/game_id/equipment_model_id และ operator ก่อนเข้าตัวเลือก ไม่ใช่เช็กแค่ known เงื่อนไขอื่นยังแสดงให้ผู้ใช้เห็น ไม่อนุมานว่าผู้ใช้ผ่านเงื่อนไข
3. Root หมดอายุหรือ field ที่ root เป็นเจ้าของแต่ unknown ยังห้ามใช้ secondary lookup กลบช่องว่าง
4. Negative/positive ของ procedure สองบริการใช้หัวข้อเดียวกันและขั้นตอนคนละแบบ ต้องเลือกตาม root ในทั้ง OFF/ON; เก็บ final12 ที่หยุดไว้และเริ่ม manifest ใหม่หลังแก้
