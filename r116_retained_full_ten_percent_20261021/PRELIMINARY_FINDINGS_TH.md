# ข้อสังเกตระหว่าง R116 — ยังไม่ใช่ผลครบชุด

เอกสารนี้บันทึกสิ่งที่ตรวจพบระหว่างรันเท่านั้น คะแนนสุดท้ายต้องรอ 2,108 keys / 5,643 grades และ integrity checks ครบใน full01/TEST_COMPLETE.json ไม่แก้ candidate จากข้อค้นพบเหล่านี้ระหว่าง benchmark

## 1. ถามโซน แต่จบที่ชื่อบริการ

ตัวอย่าง: `Please answer from verified studio information: Which studio zone has TEKKEN 8`

คำตอบ: `TEKKEN 8 — studio services offering this game: PC #01-#02; PlayStation 5 #01-#02 [S1]`

ฐานมีเส้นทางจริง game_detail_tekken_8 → migrated_link_availability_pc_01_02_game_detail_tekken_8 → availability_pc_01_02 → resource_pc_01 → zone_pc (PC Zone) รวมถึงเส้นทางของ PS5

นี่เป็นหลักฐานว่าโซนมีใน relation graph แต่ projection ที่ส่งออกเป็น studio_services ไม่ได้ลงไปถึง zone ที่ถาม จึงแยกจากข้อมูลหาย และยังไม่เรียกว่าให้ข้อมูลผิดโซน เพราะคำตอบไม่ได้อ้างชื่อโซนผิด

สิ่งที่ควรแก้ภายหลัง: task/facet สำหรับ location-of-game ควรอ่าน game_service → service/resource → zone และแสดงโซน พร้อม source ของ relation ไม่ใช้ชื่อบริการแทน field ของสถานที่

## 2. FAQ compatibility reader ยังแสดง metadata ภายใน

ตัวอย่าง: `May I record video inside the studio`

ส่วนคำตอบเงื่อนไขถ่ายภาพในเกมอ้าง owner source ได้ แต่มี topic C10 และ scope_note ที่เป็น JSON r114_fact/source_record_id แสดงเป็น bullet พร้อม citation เพิ่ม

ปัญหาเป็นการเลือก field/การนำเสนอ ไม่ได้หมายความว่า source ถูกแต่ง ข้อมูลควบคุมการอ่านและ provenance ควรอยู่ใน debug/owner view ไม่ใช่คำตอบทั่วไป เกณฑ์ literal เก่าอาจยังผ่านบางส่วนแม้ UX นี้ยังผิด

สิ่งที่ควรแก้ภายหลัง: field visibility/response projection ต้องมีขอบเขตสำหรับผู้ใช้ และ all_fields จาก LLM ต้องไม่เปิด metadata ของเครื่องมือโดยอัตโนมัติ

## 3. บุคลากรมี role แต่ inverse lookup ถูก public_scope กันไว้

ตัวอย่าง: `ใครมีตำแหน่งนักศึกษาสหกิจ Game and 3D Developer`

Common people directory เลือก member_c0944fdade08a06c ได้แล้ว แต่ public_scope ของ record ยัง unknown จึงถูก complete_flow.certify กันไว้และตอบไม่ยืนยัน ขณะที่ display_name/role/team มี field และ evidence_refs จริง

`complete_flow.py` มี guard person_public_scope_not_confirmed; ทาง domain_flow ที่ตอบชื่อ/หน้าที่ตรง ๆ ใช้ flow contract อีกเส้นทาง จำเป็นต้องตรวจความสม่ำเสมอของ delivery guards ทั้งสองเส้นทาง และแยกสิทธิ์ของ owner preview กับข้อมูลที่เผยแพร่จริง ไม่แก้ public_scope หรือ approve แทนเจ้าของเพื่อเพิ่มคะแนน

จึงไม่ใช่หลักฐานว่าชื่อหรือหน้าที่ไม่ได้ย้ายมา แต่เป็นปัญหาขอบเขตข้อมูล/เส้นทางอ่านที่ต้องทำให้ชัดเจน

## 4. ถามราคา 2 ชั่วโมง แต่ตอบให้ระบุรายการ/เวลาอีก

ตัวอย่าง: `ขอสอบถามหน่อยยครับ บุคคลทั่วไป เล่น PS5 2 ชั่วโมง เสียกี่บาท`

reason code เป็น duration_arithmetic_not_declared แต่ข้อความที่ส่งกลับขอรายละเอียดรายการ/เวลา ทั้งที่มีในคำถามแล้ว ต้องแยก missing billing arithmetic rule ออกจาก missing service/time slot

source ยืนยัน rate และต่อคน ไม่ได้ยืนยันการปัดเศษ/ส่วนลด/การต่อระยะเวลาทุกแบบ จึงไม่ควรคัดลอกสมมติฐานคำนวณเก่ามาเป็นนโยบายใหม่โดยไม่ตรวจ source

สิ่งที่ควรแก้ภายหลัง: คืนอัตราต่อรอบที่ยืนยันได้ พร้อมระบุเงื่อนไข/กฎคำนวณที่ยังขาด ให้ partial response ที่มีประโยชน์ และตรวจว่าจะนำเลขคณิตหรือกฎเดิมมาใช้ได้ภายใต้หลักฐานใด ไม่ถามซ้ำช่องที่ผู้ใช้บอกแล้ว

## 5. Model transport สำเร็จ แต่ plan ใช้ไม่ได้

ตัวอย่างคำถามจำนวน sessions ต่อ booking มี reason model_invalid_choice และตอบ unavailable ต้องอ่าน MODEL_EVENTS.raw_content/invalid_items คู่กับ candidate scope

การได้รับ HTTP response จาก Ollama ไม่รับรองว่า indices/plan/schema/ความหมายถูกต้อง การปฏิเสธ plan ที่อยู่นอก pool เป็น guard ที่จำเป็น แต่ผลยังเป็นคำถามที่ตอบไม่สำเร็จ สาเหตุ candidate selection/protocol ต้องแยกจากความถูกต้องของ policy

## 6. ถามปุ่มทั้งหมด แต่ top-K ให้โมเดลไม่ครบทุกรายการ

ตัวอย่าง: `What are all the buttons in Call of Duty: Warzone`

native มี 13 binding facts ของ controls_ps5_call_of_duty_warzone แต่คำตอบจาก domain reader คืน 8 facts ขาด binding_1, binding_4, binding_7, binding_8, binding_11 แม้ทุกปุ่มที่พูดจะอ้าง source ที่มีจริง

`Engine.scoped_candidates` จำกัด 8 candidates เป็นขอบเขตสำหรับ semantic selection เมื่อใช้กับ list-all task จึงไม่สามารถให้โมเดลเลือก facts ที่ไม่ได้ส่งเข้า pool ได้ นี่เป็นคนละปัญหากับ source migration หาย และเกณฑ์ literal ที่เช็กคำเพียงบางปุ่มอาจไม่จับความไม่ครบ

สิ่งที่ควรแก้ภายหลัง: จำแนก set/list task จาก single action lookup สำหรับการขอทั้งหมดให้อ่าน member set ใน game/platform scope ครบโดย deterministic relation reader หรือแบ่งอ่านพร้อมตรวจ union/count ส่วน LLM ใช้ระบุ intent/target ไม่จำกัดจำนวน source members ที่ควรคืน

source completeness diagnostic นี้ไม่แก้ expected เดิมและไม่ปรับคะแนน strict/literal เก็บเป็นแกนตรวจเพิ่มใน PER_REQUEST_REVIEW และ COMPARISON

## 7. Inverse relation query ไม่คืนแม้ confirmed subset และ baseline ก็ไม่ได้เป็น semantic gold ทุกข้อ

ตัวอย่าง: `เกมไหนเล่นได้หลายโซน` — key 1806def707336a05166ef9b2589b66cb0450c840866d7ea5f6b920dccd0823f8

R115 ตอบว่าข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรง แต่ native relation graph มีอย่างน้อย game_detail_tekken_8 ผ่าน resource links ไปถึง zone_pc และ zone_ps5 จึงมี confirmed subset ที่สามารถแสดงแบบมีขอบเขตได้

Legacy ที่เก็บไว้ตอบแค็ตตาล็อกเกมทั้งหมด 42 เกมแยกโซน ซึ่งช่วยให้อนุมานบางคู่ได้ แต่ไม่ได้กรองเฉพาะเกมหลายโซนตามคำถาม ดังนั้นการที่ literal oracle เดิมให้ผ่านไม่ได้แปลว่าคำตอบเก่าตรงทุก predicate แล้ว

การไล่เฉพาะ graph ผ่าน resource ของ native ยังไม่ครอบคลุมทุกสิ่งที่ legacy จัดเป็นหลายโซน เช่น VR; ต้องตรวจ completeness ของ relation edges เพิ่มด้วย ห้ามถือ edge ที่หายเป็นหลักฐานว่าไม่ offered และห้ามประกาศว่าทั้งปัญหาเป็น Flow ล้วนหรือข้อมูลล้วน

สิ่งที่ควรแก้ภายหลัง: แยก inverse/group/filter task จาก forward lookup เช่น เกม→บริการ กับ บริการ→เกม และเกมที่มีจำนวนโซนมากกว่าหนึ่ง คืน confirmed subset พร้อม completeness/source scope ที่ยืนยันได้ก่อน ไม่ถามหาชื่อเกมในคำถามที่ตั้งใจให้ระบบค้นเป็นชุด

## วิธีใช้รายงาน

อ่าน raw ก่อน/หลังกับ source evidence ไม่เรียก literal fail ทั้งหมดว่า actual content failure และไม่ใช้ source refs ที่ถูกต้องมาแทนการพิสูจน์ว่าตอบตรงคำถาม บาง oracle มาจาก source/วันที่เก่าและคลังคำถาม candidate จึงต้องแยก source-version gap ออกด้วย
