# Flow r44: นำเข้าราคาเช่าเหมาจากไฟล์ผู้ใช้

1. อ่านทุก sheet/cell/formula/merged header; เก็บต้นฉบับและ SHA256; 1 sheet ไม่มีสูตร/ภาพ
2. แมป 6 โซน × 2 หน่วยงาน × 2 ระยะ = 24 อัตรา พร้อมที่นั่ง/อุปกรณ์และ cell provenance
3. แยก zone rental for organizations จากราคาเล่นต่อเครื่อง/ชั่วโมงของบุคคล; ไม่ทับ hourly fee data หรือแปลงนักศึกษาเป็นหน่วยงานภายใน
4. รักษา period ครึ่งวัน/เต็มวันตามไฟล์ ไม่กำหนด 3/4/6/8 ชั่วโมงเอง ไม่สร้างวันเริ่มใช้หรือส่วนลด/รวมค่าเจ้าหน้าที่
5. เพิ่ม source registry + structured answer ที่อ่านไฟล์ normalized; ข้อมูลใหม่มี precedence เฉพาะราคาเช่าเหมา ไม่ใช้ no-answer เหมาทั้งวันเก่าปฏิเสธราคาที่มีแล้ว
6. รองรับ TH/EN และ short follow-up ที่ส่งถึงผู้ใช้แล้ว เก็บ target/group/period ใน typed rental plan; explicit hourly/topic shift ต้องออกจาก rental
7. คำถาม booking/current availability/day definition/overtime inclusion บอกข้อที่ไฟล์ไม่มีอย่างตรงประเด็น ไม่ใช้กฎ 3 sessions ของการเล่นทั่วไปกำหนดการเช่าเหมา
8. ทดสอบ 24 cell values + capacity/equipment + broad/specific/สองรอบ + typo/paraphrase ที่เกี่ยวข้อง + negative hourly/live queries; เปรียบเทียบ output จริง
9. Freeze local candidate ใหม่ ไม่ทับรุ่นเก่า; start/readiness/HTTP source parity + dataset/source workbook hashes
10. วิเคราะห์ failures แก้เฉพาะหลักฐาน สรุปคำถามเจ้าของที่ยังขาด และเก็บ raw/failed log ทุกครั้ง

## คำถามข้อมูลที่ไม่อยู่ในไฟล์

- ครึ่งวัน/เต็มวันนับกี่ชั่วโมงและใช้ช่วงเวลาใด? การเช่าเหมาจัดช่วง Maintenance/นอกเวลาปกติได้อย่างไร?
- อัตรานี้เริ่มใช้/หมดอายุเมื่อไร?
- ค่าตอบแทนเจ้าหน้าที่นอกเวลารวมในค่าเช่าหรือคิดแยก ใครจ่ายและคิดเท่าไร?
- การเช่าเหมาจองผ่านช่องทางใด และบุคคลทั่วไป/นักศึกษาใช้ราคาใดเมื่อไม่ได้เป็นหน่วยงาน?
