# งานต่อหลัง R77

## 1. Subject definition และ typed constraints — ทำเองต่อได้ด้วยข้อมูลตัวอย่างแยก

ปัญหาเด่น: format มีชื่อ subject แต่ยังไม่มีนิยาม/ความต่าง/ขอบเขตเชิงความหมาย และมี profile จริงแค่ 2 records การปรับคำว่า yes-but จึงยังไม่ทำให้ทุกหมวดตอบ paraphrase ใหม่ได้ทันที

แนวทาง:

1. ออกแบบ optional subject_id/definition TH/EN, inclusion/exclusion และ reference ไปข้อมูลจริง แยก source-backed facts ออกจากคำอธิบายเพื่อค้น
2. ออกแบบ constraint แบบ typed สำหรับ ownership, context, audience, device/property, เงื่อนไขหลายข้อ และ scope เฉพาะ เช่น studio-only; ไม่ใช้ any แทนข้อจำกัดที่ยังไม่มีชนิดรองรับ
3. ทำ form ที่คนกรอกเห็นตัวอย่าง/ข้อผิดพลาดเข้าใจง่าย และ validate ความเข้ากันของ source กับ scope
4. ทดสอบตัวอย่างใหม่ที่ router ไม่รู้ชื่อ พร้อมคำใกล้เคียงที่ความหมายต่าง, update/withdraw, conflict, missing language, unknown conditions
5. เพิ่ม metadata ให้ข้อมูลจริงเฉพาะที่หลักฐานรองรับ เก็บ revision เดิม ไม่เติมนโยบายเพื่อให้ test ผ่าน

เกณฑ์ผ่าน: เพิ่มข้อมูลชนิดที่รองรับแล้วต้องใช้คำถามหลายแบบได้โดยไม่เพิ่ม record ID/alias ประโยคทุกแบบในโค้ด; negative contrasts ไม่อ่าน source คนละเรื่อง; ช่องที่ไม่รู้ยัง unknown

## 2. โมเดลจริง — ต้องมีการเชื่อมต่อที่อนุญาตก่อน

actual attempts รอบนี้ติด WinError 10013 และไม่มี success ไม่สามารถใช้ fixture ให้คะแนนความหมายของโมเดลจริงแทนได้ เมื่อเชื่อมได้จึงตรวจ model transport → schema validity → subject/constraint equivalence → source answer correctness แยกกัน และวัด latency จริง

การเชื่อมโมเดลสำเร็จไม่ได้เท่ากับตอบถูก; การตอบ unknown ตรงนโยบายที่ไม่มีข้อมูลไม่ใช่ hallucination

## 3. Dialogue repair นอก pending profile — ทำเองได้

ขยายด้วย typed state ไป name ambiguity/price/entity menu, คำตอบสั้นที่พิมพ์ผิด, that's not what I meant/จริง ๆ หมายถึง, qualified fragment และหลายหัวข้อ ห้ามอนุมานชนิดเมนู/นโยบายจาก assistant prose ตรวจการเปลี่ยนหัวข้อและ barrier ทุกครั้ง

## 4. Coverage และ retrieval scale — ทำเองได้

สำรวจข้อมูลจริงที่ยังไม่มี query_profile/role mapping โดยอิงหลักฐาน เพิ่มเฉพาะหมวดที่ schema รองรับ ทดสอบ sample หลายขนาดในฐานแยก วัด candidate recall/omitted IDs/menu pagination/latency ก่อนปรับ top-k และ prompt budget

## 5. Source consistency และข้อมูลเจ้าของ

ทำเองได้: audit duplicate/translation/validity/relationships/conditions, ทำรายการข้อขัดแย้งพร้อม source และข้อความที่ควรตอบ

ต้องเจ้าของเฉพาะนโยบายที่ยังขาดหรือขัดกันจริง: เงินเกิน/ขาด ผ่อน ระยะตรวจจ่าย อายุ/ผู้ปกครอง ดู OWNER_QUESTIONS_R73_TH.md ใน r73_scope_completion_20261016 ไม่เดาคำตอบจากขั้นตอนแก้สลิป

ไม่ต้องถามเรื่องที่ผู้ใช้ยืนยันแล้วซ้ำ: สถานะจองจริง ภาษาอังกฤษที่เคยตรวจ เวลา 12:00–13:00 ไม่ให้จอง และ VR 30 นาทีนับว่ากินเต็มชั่วโมง

## 6. ส่งใช้งาน

ก่อนจัดแพ็กเกจ production ให้ตรวจ real model/browser/TCP/state หลัง restart และ publish/update/rollback ของข้อมูลจริง สำเนา R77 ยังใช้ draft preview และ runtime R69 การเปิดชุดก่อนหน้าไม่ได้รับ code R77 อัตโนมัติ

การวัดหลายผู้ใช้ควรทำหลังเชื่อมโมเดลจริงได้ แยก source-only/semantic/field planner/live, เวลารอคิว/สร้างคำตอบ/รวม และค่อยเพิ่มจำนวนคน ไม่ใช้เวลาของ controlled fixtures เป็นความเร็วเครื่องจริง
