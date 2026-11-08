# Flow งานที่เหลือและการวัดผู้ใช้พร้อมกัน r50 — ฉบับตั้งต้น

2026-10-09 Asia/Bangkok

## ข้อมูลสถานะที่ผู้ใช้ยืนยัน

- สถานะจองจริง: ผู้ใช้ตรวจแล้วว่าถูกต้อง
- ภาษาอังกฤษ: ผู้ใช้แจ้งว่าผ่านแล้ว
- เก็บการยืนยันใน USER_CONFIRMATIONS_20261009.json ไม่อ้างว่าเป็นผลทดสอบอัตโนมัติใหม่หรือแก้ approval metadata ย้อนหลัง
- การใช้พร้อมกัน: คำขอล่าสุดให้ทดลอง จึงรวมไว้ในงานรอบนี้

## งานเรียงลำดับ

### P0 ข้อมูลมี แต่ handler ไม่ตอบ

1. ใช้ log ที่พบ no-answer เริ่มสมาชิกทีม VALORANT TH/EN
2. เปิด source chunk และ approved localization จริง เช็ค game ID, facet, literal size, starter/substitute distinctions, source hash
3. จับ failure ที่ taxonomy → row facet → coverage → formatter → validator อย่าสรุปว่า retrieval score ต่ำอย่างเดียว
4. แก้ matching/facet เฉพาะที่ clause รองรับ ไม่แทน missing ด้วยข้อมูลเกมอื่น ไม่เผย draft
5. ทดสอบคำถามใหม่หลายสำนวน ตัวเลขที่คาดไว้ และ negative team pause/team penalty ไม่ใช่จำนวนคน

### P1 สำนวนคำถามต่อและคำผิด

1. ประวัติของ session เดียวจาก server และต้อง ACK; เปิด/ปิด debug ผลต้องเหมือนกัน
2. ต่อจากคำตอบบริการ เก็บ claim scope และเงื่อนไข เช่น own/personal/date/payment
3. รองรับ return marker แบบระบุเรื่องเพื่อกลับหัวข้อบริการเก่า; ถ้า ambiguous ให้เลือก ห้ามย้อนหลังเองเมื่อถามเรื่องใหม่
4. จับคำผิดโดย canonical vocabulary + anchored distance; ตัวเลข วันที่ ID และคำปฏิเสธต้องไม่เปลี่ยน
5. เพิ่ม tests ที่ไม่ได้อยู่ในชุดแก้เดิม รวม typo สองจุดและคำถามสองหรือสามรอบ
6. ดูคำตอบจริงครบทุกประเด็นพร้อมแหล่งข้อมูล unknown policy ต้องยัง unknown

### P2 ความจำหลัง restart

1. เก็บ state ในฐานข้อมูลใหม่แยกจาก transcript เดิม ใช้ SQLite transactions และ TTL ตามเวลา wall clock
2. persist เฉพาะ state ที่ server เป็นผู้สร้าง ไม่รับ history client เป็น trusted
3. คง bounded sessions/history/turns, ACK และ duplicate turn semantics
4. pending ที่ยังไม่ complete ก่อน restart ต้องไม่กลายเป็นคำตอบสำเร็จ
5. restart ของ candidate ที่ยืนยัน PID ได้เท่านั้น และทดสอบ same session/other session/expired/corrupt state
6. live booking ต้องเรียกใหม่ ห้าม replay คำตอบสถานะเก่าเป็น live หลัง restart
7. ปัญหาเขียน DB ต้องรายงานสุขภาพและใช้ memory fallback ห้ามทำเว็บล่มหรืออ้าง durable สำเร็จ

### P3 package

1. สร้าง version ใหม่ ไม่ทับชุดเก่า เก็บ manifest และ SHA-256
2. คัดเฉพาะ code/data/runtime ที่ต้องใช้ ไม่ copy log/state DB/history ทดสอบให้ผู้รับ
3. ทำสองแบบตามรูปแบบเดิม download models / with models; ไม่ duplicate weights โดยไม่จำเป็น
4. เช็ค extracted package ด้วย HTTP เห็น version ใหม่และ source equality
5. เปลี่ยนเว็บ local เป็น candidate หลัง identity checks เก็บ launcher logs แยก

### P4 concurrent users บนเครื่องนี้

1. สร้างผู้ใช้จำลองแต่ละคน session ID/turn ID ของตัวเอง ส่งคำขอด้วย barrier ให้เกิดพร้อมกันจริง
2. วัดสอง profiles: fast structured/service และ mixed RAG/control พร้อมภาษา TH/EN ไม่ bypass worker หรือบังคับปิดโมเดล
3. เริ่ม N=1,2,4,8,12,16,24,32; ทำ 3 waves ต่อระดับ fast และอย่างน้อย 2 waves ต่อระดับ mixed
4. ไม่ retry 503 อัตโนมัติแล้วนับเป็นผ่าน เก็บ first-attempt HTTP/code/error/busy/timeout/answer correctness และเวลาแต่ละคน
5. รายงาน p50/p95/max/throughput/health worker PID/restarts/RAM แยกเวลา successful answers กับเวลาที่ server ปฏิเสธ
6. เกณฑ์ใช้งานในผลรอบนี้: ทุก request ถูกต้อง ไม่มี timeout/restart/session leakage และ p95 <=20s; ระดับที่พลาดให้รายงานเป็น boundary
7. หยุดเมื่อ worker ไม่ฟื้น/timeoutหนัก/RAMใกล้หมดหรือสองระดับต่อกันเกิด failure ไม่เพิ่ม workers จนแย่ง GPU โดยเดา
8. ตรวจ independent dialogue parking vs personal mouse ด้วยคำถามต่อพร้อมกัน และ same session conflict แยกจาก multi-user
9. คำถามทดสอบยิง local API เท่านั้น ไม่ทำ burst ใส่ WordPress; ขีดจำกัด booking สดยังต้องแยกจาก profiles นี้
10. จำนวนคนส่งคำถามพร้อมกันเป็น concurrent requests ไม่ใช่จำนวนแท็บเปิดค้างหรือ public internet capacity; ผลใช้เฉพาะเครื่องและรุ่นที่บันทึก

## Loop ตรวจทาน

Review 1 evidence, 2 source/locale, 3 scope, 4 partial answer, 5 context/ACK, 6 persistent TTL, 7 failure/restart, 8 load measurement, 9 package/data preservation, 10 acceptance & remaining work

แต่ละรอบต้องบันทึกปัญหาที่พบ การเปลี่ยนแปลง และหลักฐานใหม่ เก็บฉบับตั้งต้นไว้ เมื่อจบการทดสอบจึงสร้าง FLOW_FINAL_R50.md พร้อมสถานะทำแล้ว/ยังไม่ได้ทำ ห้ามนับการอ่านซ้ำเป็นการแก้ผลทดสอบ
