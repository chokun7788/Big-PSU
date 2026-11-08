# R120 ทดลองให้ Flow เดิมสอน Flow กลาง

## เป้าหมาย

ทดลองถ่ายทอดวิธีตีความและจัดการคำถามจาก Legacy R64 มายัง Common R119 โดยให้ระบบกลางอ่านข้อมูลปัจจุบันจาก native ต่อไป ตรวจทั้งข้อที่เคยผิดและคำถามอีกชุดที่ไม่ใช้สอน

รอบนี้เป็น **การถ่ายทอดพฤติกรรมด้วยตัวอย่าง แผน และกติกาที่ตรวจสอบได้** มี retrieval ของตัวอย่างสำหรับ prompt และปรับจุดเชื่อมของ reader ไม่ใช่การ train/fine-tune น้ำหนัก Typhoon และจะไม่รายงานว่ามีการเปลี่ยนน้ำหนักโมเดล

งานต้นฉบับ [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) ศึกษาการถ่ายทอดจาก teacher ไปยัง student ผ่านการฝึกโมเดล ส่วน [Distilling Step-by-Step](https://aclanthology.org/2023.findings-acl.507/) ใช้ supervision เพิ่มเติมจาก teacher เพื่อสอนโมเดลขนาดเล็ก รอบนี้นำแนวคิดการถ่ายทอดกระบวนการมาประยุกต์กับ Flow ไม่ได้ทำซ้ำการฝึกหรืออ้างผล benchmark ของ paper

## สิ่งที่จะเรียนจาก teacher

1. คำถามต้องการงานอะไร เช่น ราคา วิธีจอง ตำแหน่ง ปุ่ม หรือบทลงโทษ
2. แยกชื่อเกม/อุปกรณ์ที่เป็นเป้าหมายออกจากบริบทประกอบ
3. รักษาเวลา กลุ่มผู้ใช้ จำนวนคน การปฏิเสธ และฉบับการแข่งขัน
4. ใช้ calculator/structured reader/rule lookup ที่เหมาะสม
5. ตอบส่วนที่ถามก่อน แล้วตามด้วยเงื่อนไขและขอบเขตที่ยังไม่ทราบ

เก็บ route, entities, mode, trace, request plan, source hits และคำตอบที่ระบบเดิมส่งจริง วิธีที่อธิบายในรายงานจะอิงข้อมูลเหล่านี้และโค้ด ไม่อ้างว่ามองเห็นความคิดภายในของโมเดล

## สิ่งที่จะไม่ถือว่าเป็นความจริงจาก teacher โดยอัตโนมัติ

- ราคาหรือหน่วยราคาเก่าที่ต่างจาก owner confirmation ปัจจุบัน
- คำตอบเรื่องไม่พบข้อมูลในอดีต ซึ่งอาจไม่จริงแล้วหลังเพิ่มข้อมูล
- การตอบ edition/สถานะสด/สิทธิ์อนุญาตเกินกว่าหลักฐาน
- การผ่าน route/keyword ใน grader ซึ่งไม่รับรอง semantic correctness

raw teacher answers เก็บไว้เป็นหลักฐานทดลอง ตัวอย่างใน prompt ของ student จะมีเพียงคำถามและแผนจัดการ ไม่ใส่คำตอบธุรกิจ ราคา โทษ หรือข้ออนุญาตจาก Legacy ลงไปเป็น facts

## ขั้นตอน

1. คัดคำถามเดิมที่มี saved teacher trace เหมาะสม แยก teaching 64 ข้อ / evaluation 27 ข้อ ใน 9 หมวด และแยก development 48 ข้อเดิมออกจาก teaching
2. จัดกลุ่มด้วย source case IDs และ origin IDs เพื่อกัน corpus/typo variants ของกรณีเดียวกันข้าม split ทั้งนี้ semantic near-duplicates ที่ใช้ IDs คนละชุดอาจยังเหลือ จึงไม่เรียกชุดนี้ว่า real-user holdout หรือ Full accuracy
3. รัน Legacy จริงแบบ LLM ON บน teaching 64 ข้อใน snapshot แยก เก็บผลและ observable traces
4. ตรวจ teacher labels แล้วถ่ายเป็นตัวอย่างแผนและบทเรียนที่ไม่พก business answers เข้า runtime
5. วัด baseline R119 บน evaluation 27 ข้อก่อนแก้ code ด้วย model/digest/clock/ข้อมูลชุดเดียวกัน
6. เสริม student: ตัวอย่างที่เกี่ยวข้องใน prompt, ตรวจ requested operation, รักษาบริบท/slots, เชื่อม topic กับ native reader และตรวจ completeness ของคำตอบกว้าง
7. ตรวจ source contracts แล้วรัน evaluation 27 ข้อและ regression 48 ข้อเดิมบน student
8. รายงานก่อน/หลัง แยก semantic review, literal checks, protocol, validity, transport และ latency รวมกรณีที่ student แย่ลงด้วย

### ขอบเขตการคัดชุดทดลอง

ทั้ง teaching และ evaluation คัดจาก saved Legacy ที่มีคำตอบ validation ผ่าน confidence อย่างน้อย .85 และไม่มี positive literal check ที่ตกในผลเดิม จึงเป็นการทดลองกู้ความสามารถในกลุ่มที่ Legacy เคยผ่านเกณฑ์ ไม่ใช่การสุ่มตัวแทน Full ทั้งหมด การผ่านเงื่อนไขนี้ยังไม่รับรอง semantic correctness ของครู หลังอ่าน evaluation และนำข้อผิดพลาดมาปรับ revision02/03 ชุด 27 ข้อนั้นเป็น development ที่นำกลับมาใช้ ไม่ใช่ holdout ใหม่

## เงื่อนไขตัดสินผล

- ไม่มี teaching/evaluation key หรือ source-case-family ซ้ำกันตามกฎที่ระบุใน SPLIT_MANIFEST.json
- Runtime student ไม่เรียก Legacy เพื่อยืมคำตอบ และไม่อ่านไฟล์ grader/expected answer
- ข้อมูล native, approvals, withdrawals และ sources ของ R119 เหมือนเดิม
- วิธีหรือค่าที่ teacher ตอบผิดไม่ถูกยกระดับเป็น owner-approved
- คำถามเดิมที่ตอบผิดต้องตรวจคำตอบจริง ไม่ใช้ positive keyword score ที่เต็มอยู่แล้วเป็นหลักฐานว่าปรับดีขึ้น
- ชุดเล็กนี้ใช้ตัดสินความเหมาะสมของแนวทาง และไม่ใช้ประกาศว่าดีกว่า Legacy ทั้งระบบ
