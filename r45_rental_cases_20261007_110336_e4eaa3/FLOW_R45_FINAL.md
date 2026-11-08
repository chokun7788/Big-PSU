# Flow r45 หลังทดสอบและแก้ scope ราคาเหมา

1. เก็บก่อนแก้และ expected rate IDs จาก original workbook cell extraction → new 40 cases ครอบคลุมคำปฏิเสธ/บริบท/compound → รันจริง เก็บ trace/output ตก 25 เคส
2. อ่านฟิลเตอร์ด้วย polarity ก่อน positive matching; ไม่ fuzzy เลขสินค้า; unknown product ไม่ default เป็นทุกโซน
3. หลัง ACK ใน session เดียว: แยก short selection, generic price followup, requested field, contextual explicit link, new domain; OTHER_TASK/SCHEDULE_TASK guard มาก่อน unknown noun selection
4. เก็บ scope ต่อ child ใน scoped_requests: target/group/period ไม่ผสมข้าม child; unspecified field แสดง source options ตามแผน ไม่ map individual เป็น internal/free
5. Validate child schema/ขอบเขต/subset/type → สร้าง allowed triples → อ่าน rates จาก source table → render เฉพาะ triples พร้อม source provenance
6. Modified All Zones package ไม่มี source tariff → custom_package missing; ปฏิเสธช่วงทุกแบบ → scope clarification; booking method ไม่มี → missing ไม่เอา play policy มาตัดสิน rental
7. Field followup คง child scopes; เลือก PC จาก compound คง PC's groups/periods; all rental rates ขยาย catalog; explicit resume ใช้ acknowledged archive ไม่เอา facts ตัวอย่างคำตอบมาสร้าง target
8. Source regression 142/143 พบ both groups false unknown → แก้ + unit; actual HTTP .1 147/148 พบ noun-style rules topic ถูกกินเป็น choice → แก้ domain guard + intermediate operation oracle
9. Freeze .2 ใหม่และยืนยันรุ่น/Python/warmup/readiness → HTTP final 148/148, unit methods 128/128, source-release parity 155/155, ราคากับ workbook hash เดิม
10. วิเคราะห์เป็น .md ทุกเคสใหม่; เก็บผลผิด/ก่อนแก้/release .1/logs ทั้งหมด; ไม่รัน full 20k; owner missing policies และ negative tests ไม่ถูกนับเป็น human approval หรือการยืนยัน live booking
