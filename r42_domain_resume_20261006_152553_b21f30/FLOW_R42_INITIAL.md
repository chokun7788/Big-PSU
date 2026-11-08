# รายการที่เหลือและ Flow r42

## ลำดับงาน

| ลำดับ | ปัญหา | ทำเองได้ / ต้องมีข้อมูล | งานรอบนี้ |
|---|---|---|---|
| 1 | Resume หมวดเวลา การจอง สมาชิก และรายละเอียดเกมยังไม่ครบ | ทำเองได้จาก source/fixtures | เพิ่ม task schema/selector + TH/EN |
| 2 | Compound หลายงาน operation เดียวถูก archive เหลือข้อแรกหรือ resume ไม่ได้ | ทำเองได้ | typed replay เก็บทุก child; จำกัดขอบเขต |
| 3 | Complete turn ซ้ำอาจ append history ซ้ำหรือแทน response เดิม | ทำเองได้; ต้อง reproduce | idempotence + cache/log identity |
| 4 | Execution complete ไม่รับรองเนื้อหาครบ/ถูกทุก fact | ทำเองได้จาก source oracle; current policy ต้องเจ้าของ | เปรียบเทียบ resumed answer/operation/scope และ future content gates |
| 5 | Typo/paraphrase holdout ยังไม่ครบ | ทำเองได้ | เพิ่มสำนวน return และ negative conditions ที่สัมพันธ์กับรอบนี้ |
| 6 | ชุดแจก WithModels/DownloadModels และเครื่องสะอาด | ทำเองได้ด้าน build; portability ต้อง environment จริง | candidate local ใหม่; ยังไม่อ้าง clean machine |
| 7 | Concurrent load/latency/recovery | ทำเองได้แบบ fixture/controlled runtime | double-completion/state tests; ไม่ full load benchmark |
| 8 | Current price/pause conflict/truncated rules/live occupancy | ต้องข้อมูลต้นฉบับ/เจ้าของ | รักษาไฟล์และแยกจาก automatic gates |

## ขั้นตอน

1. Backup + hash + Git status; baseline source และเว็บ r41.3 เท่าที่เกี่ยวข้อง
2. เก็บ query ที่ผู้ใช้ต้องการในแต่ละ operation ไม่เก็บคำตอบเก่าเพื่อใช้เป็น fact
3. Resume เฉพาะ archived acknowledged task; อ้างถึง booking กว้างที่มีทั้งสถานะสด/วิธีจองต้อง clarification
4. ชื่อใหม่/ตัวเลข/วันเวลาใหม่/negation ต้องรักษาไว้หรือถามเฉพาะเงื่อนไขที่ยังรวมไม่ได้
5. Compound เดียวกันใช้ requests array แบบมีชนิด เพื่อไม่ split target labels ตาม comma หรือทิ้ง unknown child
6. ทดสอบ duplicate completion และ stale revision ก่อนแก้; เขียนครั้งแรกเป็น authoritative response ของ turn
7. Trace/API ใช้ actual domain และ outcome; ยืนยัน caller ได้รับ cached response ID เดิมเมื่อ replay
8. Fixture สถานะสดต้องเปลี่ยนจากว่างเป็นถูกจองระหว่าง resume แล้วตรวจว่า fetch ใหม่; API connected ไม่เป็น occupancy oracle
9. Source targeted + regressions เดิมที่เกี่ยวข้อง → candidate unique + source parity → HTTP เปิด LLM/RAG
10. เก็บแต่ละรอบ / วิเคราะห์ failed cases / แก้จน gates ที่ตั้งไว้ผ่าน / review รายงานและ remaining backlog

## Review guards

- Memory ≤8 operations/session และ TTL เดิม ไม่เพิ่ม persistent personal memory
- Bare all หลายมิติยังถาม scope; ไม่ตี catalog ทุกโซนว่าผู้ใช้เลือกทุกเกม
- Relative today/now ใน booking ถูก resolve ใหม่ตอน execute; explicit timestamp ใน query เดิมคงไว้
- หมวดสมาชิก/บุคคลมี metadata จาก source ไม่อ้างชื่ออังกฤษที่เจ้าของยังไม่ยืนยัน
- ไม่เปลี่ยน owner schedule/rates/rules; ไม่เก็บข้อมูลจองจริงในรอบนี้
- ไม่รัน full corpus 20k; pass เป็น targeted evidence ไม่ใช่พิสูจน์ backlog 66 ข้อหมด
