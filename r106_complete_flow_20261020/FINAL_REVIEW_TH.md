# R106: ปิดการทบทวนก่อน Full Test

## หลักฐานตั้งต้น

R105 integrated04 รันครบ 19 lanes จาก source ที่ freeze แล้ว โดย R97 acceptance ผ่าน **444/444** (37 scenarios × 3 locale × 4 wording forms) และตรวจหลักผ่าน: contracts 59/59, shared flow 65/65, owner 24 หมวด 154/154, semantic protocol 22/22, simulated live 10/10, publication 9/9, typed conflicts 4/4, rental 19/19, competition 7/7, retained V2 17/17, actual HTTP 9/9 ข้อมูลจริง/approval เดิมไม่เปลี่ยน

ยังไม่ใช้คำว่า accuracy 100%: ชุดคำถาม synthetic นี้ออกแบบโดยผู้พัฒนา ไม่ใช่ independent unseen users และ task matrix ยังมี 12 probes ที่ไม่ผ่าน

## กลุ่มแก้สุดท้าย

1. **Equipment explain/specs/capacity ภาษาไทย**: intent เริ่มต้นหยาบเกินไป equipment กลายเป็น list เสมอ และจำนวนคนของ resource ถูกเลือกเป็น game players แก้ infer ด้วย kind + field meaning ไม่ใส่ชื่ออุปกรณ์หรือจำนวนจริงลงโค้ด
2. **ราคาเปลี่ยนเฉพาะ actor**: ตรวจ scoped supersession หลังตัด intersection ของ service และ audience แล้ว เพื่อไม่ให้อัตราภายนอกที่ถูกแทนที่ไปบล็อกราคาบุคลากรที่ยังใช้ได้ เพิ่ม negative/positive regression จากแหล่งข้อมูลแยกกลุ่ม
3. **เพิ่ม FAQ ใหม่หลังถามบริบท**: ทาง normal play เดิมตอบ source gap ตายตัว ปรับให้อ่าน FAQ ที่ owner ประกาศ query_profile ว่า correction/context=studio/ownership=any และผูก related_ids กับเกมนั้น มีหลายแหล่งให้ถามเลือก ไม่ยืมกฎแข่งขัน ไม่อ่าน policy ของอีกเกม
4. **คำถามขอกฎจากเอกสารที่มี**: หาก text มีหลักฐานแต่ completeness metadata ยัง unknown ให้แสดงข้อความที่มีเป็น partial reference พร้อมบอกว่ายังไม่ยืนยันเอกสารครบ ไม่ทิ้งข้อมูลทั้งหมด และไม่รับรองว่าเป็นกฎครบทั้งเล่ม กรณีคำถามตัดสินใจเฉพาะที่ขาด clause/dependency ยังคงไม่ยืนยัน
5. **ขอบเขต source authority**: ตัว render source rows ตรวจว่า source อนุญาต kind นั้นก่อนแสดงค่า ไม่ให้ partial-reference path ข้าม guard ของแหล่งข้อมูล

## วิธีตรวจรอบสุดท้าย

เก็บ R105 source/results ไว้ครบ แก้บน R106 แยก ตรวจ AST/JS/schema และ freeze ใหม่ รัน grouped final gate สำหรับสาขาที่เปลี่ยน: model readiness, source/data-growth contracts, retained contracts, pending/source-growth V2, 32-task matrix, 37-scenario acceptance

ส่วน owner/publication/HTTP/live/model protocol ที่ไม่เปลี่ยน ใช้หลักฐาน R105 ระบุ lineage และ hashes ชัดเจน ไม่อ้างว่า R106 รัน 19 lanes ใหม่ทั้งหมด จากนั้น **Full Test E2E ของ R106** รัน common-only + LLM ON 20,554 unique request keys / 55,811 grades เป็นการตรวจรวมจาก pipeline จริง รวม input guard

## Oracle ที่เปิดเผย

C07 ของ R97 ต้องแยก normal play กับ competition การแก้ oracle ใน R103/R104 ตามความเข้าใจว่าเป็น phase ภายในการแข่งขันไม่ถูกต้อง R105/R106 คืน invariant เดิมและเพิ่มว่าห้ามปล่อยกฎแข่งขันก่อนทราบบริบท ผลก่อนหน้าเก็บตามจริง ไม่แก้ย้อนหลัง การเทียบรวมแยกเคสนี้ออกให้ตรวจได้

## การรายงาน

- coverage ครบต้องเทียบ request keys และ grade counts จริง
- strict protocol, outcome, keyword/clause, source evidence, validity, execution exceptions, model transport แยกกัน
- การมีข้อมูล schema ครบไม่เท่ากับ semantic correctness ทุก paraphrase
- real provider blocked แยกจาก simulated live ที่ผ่าน
- real DB ยังมี applicability ที่ไม่ยืนยันและยังไม่มี publication/approvals จริง ไม่สร้างวันมีผลหรืออนุมัติแทนเจ้าของ
- R78/R101/R102/R103/R104/R105 และ logs เดิมไม่เปลี่ยน ไม่ติดตั้ง candidate ทับ production
