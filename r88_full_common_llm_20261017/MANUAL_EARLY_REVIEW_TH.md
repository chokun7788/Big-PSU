# ตรวจคำตอบจริงช่วงต้นของ R88

**ยังเป็นผลบางส่วน ไม่ใช่รายงานคะแนนทั้งชุด** อ่านตัวอย่างจาก FAILURE_EVIDENCE_EARLY01.sqlite ซึ่งรวบรวมผล 1,911 requests ณ เวลาที่อ่าน ส่วน ANALYSIS_EARLY01.json เป็น snapshot ก่อนหน้านั้น 233 requests จึงไม่ใช้ตัวเลขสอง snapshot เป็นฐานเดียวกัน รายงาน FINAL จะตรวจ coverage ใหม่เมื่อครบทั้งหมด

ข้อมูล โค้ดแชท และ oracle ไม่ถูกแก้ระหว่างรัน การตรวจนี้อ่านคำตอบเดิมที่เก็บไว้ ไม่ถามซ้ำเพื่อเลือกผลที่ดีกว่ามาแทน

## 1. Timeout จริง ต้องแยกจากข้อผิดพลาดข้อมูล

คำถาม: `เอาอาหารเข้าได้ไหม`

- ไม่มีคำตอบที่ส่งสำเร็จ ตัว evaluator บันทึก `TimeoutError('request watchdog 28 seconds')`
- เกณฑ์คาดว่าเนื้อหามีอาหาร เครื่องดื่ม และพื้นที่ที่กำหนด แต่ครั้งนี้ไม่มี output ให้ตรวจ
- นี่เป็น execution/watchdog failure จริงของรอบตรวจ ไม่ใช่หลักฐานว่าข้อมูลอาหารถูกย้ายมาไม่ครบ
- การที่ watchdog หมดเวลาเพียงอย่างเดียวยังไม่ยืนยันว่าต้นเหตุคือ LLM เพราะไม่มีผล/trace สุดท้ายจากคำขอนี้ ต้องดูเวลา การโหลด และ call logs ที่เกี่ยวข้องต่อ
- ไม่ขยาย timeout หรือแก้เนื้อหาเพื่อทำให้ผลรอบที่กำลังรันผ่านย้อนหลัง

## 2. เลือก entity ถูกอุปกรณ์ แต่ task ยังผิดประเด็น และมี model timeout ร่วมด้วย

คำถาม: `A question about the studio: Can an external visitor use the VR headset?`

คำตอบจริง:

> The requested topic is unclear. Which part of VR Zone do you need: Service / platform / Play time per session / Booking occupancy?

- method=`exact`; selected IDs เป็น `zone_vr`, `availability_vr_30`, `availability_vr_60`
- คำถามถามสิทธิ์ของบุคคลภายนอก แต่แผนไปผูกกับรายการ VR/เวลาเล่น แล้วถามว่าจะอ่าน field ไหน
- มี `TimeoutError` ของ HTTP ไปโมเดลในคำขอนี้ด้วย จึงยังไม่ควรสรุปว่าปัญหามาจาก entity matcher อย่างเดียว หรือโมเดลอย่างเดียว
- คำตอบที่ควรได้ต้องเป็นเงื่อนไขสิทธิ์ใช้บริการจากนโยบายปัจจุบัน หากไม่มีหลักฐานตรงให้บอกส่วนที่ยังยืนยันไม่ได้ ไม่ถามเรื่องระยะเวลา/occupancy แทนโดยไม่รักษาเจตนาเดิม
- แนวตรวจหลังครบชุด: task/permission coverage, candidate policy scope, ประโยคขึ้นต้นที่ทำให้ grammar bridge ไม่รับ และ model timeout/fallback ต้องดูร่วมกัน

## 3. Literal ไม่ตรง ไม่เท่ากับแปลความหมายผิดทันที

คำถาม: `Hello, could you help? What conduct and etiquette do Tekken 8 tournament players follow?`

คำตอบเลือกเล่ม TEKKEN 8 และหัวข้อ Etiquette in Competition ถูกตำแหน่ง มีข้อความเรื่องห้ามล้อเลียน/ดูหมิ่น พฤติกรรมที่ไม่เหมาะสม ความเคารพกรรมการ และบทลงโทษจาก source ที่อ่าน

เกณฑ์คาดประโยคขึ้นต้น `Unsportsmanlike behavior, such as mocking, taunting, or rude words ...` แต่คำตอบจากข้อมูลกลางใช้ `No conduct shall be exhibited that shows lack of respect ...` จึงขึ้น `missing_complete_clause` แม้มีเนื้อหาที่เกี่ยวข้องอย่างชัดเจน

- เป็นหลักฐานว่าตัวตรวจประโยคแบบ exact/literal กับคำแปลใน source กลางไม่ใช่ถ้อยคำฉบับเดียวกัน
- ยังต้องอ่านเงื่อนไข/บทลงโทษทั้งหมดเทียบกันก่อนรับรองว่าความหมายเท่ากันครบ ไม่เปลี่ยนชื่อเป็น “แปลถูกโดยมนุษย์” เพียงเพราะ topic ตรง
- ไม่ควรแก้ข้อมูลกลางให้ใช้ถ้อยคำเก่าเพียงเพื่อทำให้ literal ผ่าน หรือเรียกทุก missing clause ว่าไม่มีข้อมูลในระบบ

## 4. ชื่อ Zone ใน oracle กับชื่อบริการในคำตอบ

คำถาม: `Please answer from verified studio information: Which studio zone has The Legend of Zelda: Breath of the Wild`

คำตอบจริงแสดงเกมที่ถาม พร้อมรายการ `Nintendo Switch (1-2 Persons)` และ `Nintendo Switch (1-4 Persons)` และระบุว่าเป็นข้อมูลเกมที่ให้บริการ ไม่ใช่สถานะจองสด

- method=`declared_game_installation_scope`
- selected IDs เป็นเกม Zelda และบริการ Nintendo ทั้งสองแบบ
- oracle ต้องเห็นข้อความ `Nintendo Switch Zone` จึงไม่ผ่านแม้คำตอบระบุ Nintendo Switch ทั้งสองบริการ
- ต้องแยก “เลือกแพลตฟอร์มผิด” ออกจาก “ตอบชื่อบริการแทน label ของ Zone ที่ผู้ใช้ถาม” กรณีนี้มีหลักฐานเรื่องชื่อ/การนำเสนอที่ไม่ตรง ไม่ใช่หลักฐานว่าไปตอบ PS5/PC ผิดเครื่อง
- แนวปรับหลังตรวจทั้งชุด: render label ของระดับที่ผู้ใช้ถาม โดยอาศัย relation ที่มีหลักฐาน หากไม่มี relation ยืนยัน ห้ามสร้าง FK หรืออ้าง Zone เพิ่มเอง

## 5. Validity guard ที่ทำงานตามข้อมูล ไม่ใช่ต้องฝืนคืนราคาที่หมดอายุ

คำถาม: `General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท`

คำตอบจริงแจ้งว่าอัตราที่บันทึกมีผลตั้งแต่ `2026-02-01` ถึงก่อน `2026-04-01` จึงยืนยันราคาปัจจุบันไม่ได้ และแสดงสถานะของบริการ VR ที่เกี่ยวข้อง

- reference clock ของชุดตรวจคือ 16 ต.ค. 2026 ซึ่งอยู่หลัง effective_until ที่คำตอบระบุ
- oracle เก่ายังคาดคำว่า “บาท/ฟรี” จึงไม่ผ่าน literal แม้ระบบกำลังป้องกันการอ้างราคาที่หมดอายุ
- เรื่องนี้ต้องแยกจากการเลือก VR 30/60 นาทีและคำถามระยะเวลา 3 ชั่วโมงที่อาจยังมี ambiguity อีกส่วนหนึ่ง
- ไม่ต่ออายุราคาเอง ไม่ลบ validity และไม่หาร/คูณจากราคาเก่ามายืนยันเป็นราคาปัจจุบันเพื่อให้คะแนนผ่าน

## 6. คำถามผสมและข้อความขาดท้าย

คำถาม: `How much does it cost for a general visiror to play Cockpit for 30 minutes and how do I boo`

คำตอบจริง:

> I cannot confirm an answer for the full situation you described. Please add details or split the question into separate parts.

- ผู้ตรวจเห็นเจตนาถามราคาและขั้นตอนจอง แต่มี typo `visiror` และคำท้ายขาด `boo`
- คำตอบนี้ยังไม่ให้สาระของส่วนที่อาจมีหลักฐาน ต้องอ่าน rejected_candidate / unresolved_query_clause และขอบเขต field ก่อนตัดสินว่าควรตอบบางส่วนแล้วถามเฉพาะที่ขาด หรือจำเป็นต้องถามใหม่ทั้งหมด
- ราคามี validity ของตัวเอง จึงไม่ควรแก้ปัญหาการถามต่อด้วยการฝืนยืนยันจำนวนเงินเก่า
- ยังไม่สรุปว่าการขอความชัดเจนทุกกรณีเป็นความผิด เพราะบางโจทย์กำกวมจริง ต้องแยก false clarification จากการถามเพิ่มที่จำเป็น

## สิ่งที่ต้องอ่านเมื่อครบชุด

1. Execution/watchdog และ model HTTP failures แยกกัน พร้อมอัตรา schema/binding ที่ผ่าน
2. False clarification / task coverage โดยเฉพาะ permission, ราคา+วิธีจอง และข้อความขึ้นต้นหลากหลาย
3. Clause completeness กับความต่างของคำแปล ไม่ใช้ exact phrase เป็นตัวแทนความถูกต้องทางความหมายทั้งหมด
4. การตอบระดับ Zone/Service/Resource ให้ตรงกับระดับที่ถาม
5. Oracle/source validity และข้อมูลที่ยังไม่มีนโยบายปัจจุบันยืนยัน
6. Session 12 ชุด / 24 เทิร์น และ input-guard 500 เคสที่ตัว supervisor จะตรวจต่อหลังคำถามหลัก

หลักฐานอัตโนมัติที่อ่านได้ตอนนี้: DEEP_FAILURE_ANALYSIS_TH_EARLY01.md, DEEP_ANALYSIS_EARLY01.json และ FAILURE_EVIDENCE_EARLY01.sqlite

เมื่อครบ supervisor จะสร้าง REPORT_FINAL_TH.md, ANALYSIS_FINAL.json, DEEP_FAILURE_ANALYSIS_TH.md และ FULL_TEST_COMPLETE.json เฉพาะเมื่อผ่านการตรวจ coverage ไม่ใช้ผลช่วงต้นแทนผลสุดท้าย
