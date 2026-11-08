# ผลตรวจทานเอกสารก่อนส่ง

งานนี้ตรวจเอกสารและหลักฐานที่มีอยู่ ไม่มีการส่งคำถามใหม่เข้าบอท ไม่มี model generation และไม่มีการรัน full/targeted chatbot test

## รอบที่ 1 — ตรงกับโค้ดที่มีจริงหรือไม่

- แยก legacy R64 snapshot ออกจาก common R88/R87 และจากโฟลเดอร์ Downloads ต้นฉบับ
- ตรวจ early return ของ common: ตัวตอบเดิมด้านล่างยังอยู่ใน source แต่ไม่ได้หมายความว่า profile ใหม่เดินผ่านทั้งหมด
- แยกภาพรวม branch families ออกจากลำดับ return จริง เพิ่มตาราง retrieval ที่ระบุว่า general fallback อาจจบก่อน final curated/vector
- ตรวจ owner preview, published CommonStore และ migration draft reader ว่าเป็นคนละเส้นทาง
- พบ reference ของ draft catalog ชี้ชื่อ resolve_date ซึ่งไม่มีใน open_day.py จึงเก็บ draft เดิมไว้และสร้าง PROBLEM_CATALOG_REVIEWED.json ที่ชี้ function answer จริง เอกสารฉบับส่งใช้รุ่นตรวจทาน

## รอบที่ 2 — ไม่กล่าวเกินผลทดสอบหรือไม่

- ใช้คะแนน positive จากตัวตรวจเดียวกัน 94.41%/72.10% ไม่ใช้คนละ denominator ของรายงานเก่า
- แยก strict protocol, literal content, meaning/source correctness และ owner review
- แยก request/grade/call/audit event โดยเฉพาะ schema-pass แต่ rejected 2,494 เป็น audit events
- แยก runtime exceptions เดิม 2,692 NameError + 2 timeout จากใหม่ 2 watchdog และ 36 model transport timeout calls
- ไม่เปรียบ engine sessions ใหม่ 23/24 กับ HTTP sessions เดิม 22/24 เหมือนเป็นการทดลองเดียวกัน
- ตัวอย่างราคาเดิมมี expiry caveat จริง จึงระบุใน casebook และไม่กล่าวว่าเดิมอ้างเป็นราคาปัจจุบันโดยไม่มีคำเตือน
- R88 controlled booking unavailable ไม่ถูกใช้เป็นหลักฐานว่า WordPress จริงเสีย
- 116 missing localization metadata ไม่ถูกแปลงเป็น 116 records ไม่มีค่าอังกฤษ; 11 known section values และ 32 Thai-character flags แยกไว้
- Unknown optional fields ไม่ถูกนับเป็นข้อเท็จจริงที่ย้ายตกหล่นทั้งหมด และไม่ถามเจ้าของซ้ำเรื่องที่ผู้ใช้ยืนยันแล้ว

## รอบที่ 3 — อ่าน ใช้ และตรวจย้อนกลับได้หรือไม่

- ทำ README พร้อมลำดับอ่านและคำศัพท์ ให้ใช้สอง Full Flows แยกกันได้
- เพิ่ม casebook 12 กรณี พร้อมคำตอบเดิม/ใหม่และ trace ที่เก็บไว้แล้ว; 10 กลุ่มตัวอย่างมี raw subset ส่วน legacy NameError และ controlled booking ใช้ aggregate/source evidence
- เพิ่มบัญชีข้อมูลกับคำถามเจ้าของแบบ conditional ไม่โยนงานตีความโค้ดให้เจ้าของ
- ตรวจลิงก์ไฟล์/เลขบรรทัด จุดอ้างอิงโค้ด fences, จำนวน 37 sections และดัชนี failed requests ครบตามหลักฐาน
- เพิ่มช่องว่างไทย–อังกฤษใน prose โดยคง quoted raw answers, JSON, code spans และ link destinations
- ตรวจ hashes source ของทั้งสอง snapshots ไม่เปลี่ยน; ตรวจ installed R78 เทียบ R88 และ hash ฐานกลางที่บันทึกไว้

## สิ่งที่ผลตรวจนี้ไม่รับรอง

- ไม่ใช่การแก้ runtime หรือรับรองว่าทุกคำถาม 20,554 ข้อได้รับ human semantic review แล้ว
- ไม่ใช่การอนุมัติเผยแพร่ข้อมูล draft หรือรับรองแพ็กเกจ portable หลังแก้ล่าสุด
- ไม่ตัดสินคำแปลต่างสำนวนว่าถูกครบทุกเงื่อนไขจาก literal mismatch อย่างเดียว
- กลุ่มปัญหาอัตโนมัติยังเป็นสมมติฐาน; ตัวอย่างที่พิสูจน์สาเหตุแล้วไม่ใช้แทน root cause ของทุกข้อในกลุ่ม
- ข้อเสนอ target flow ในเอกสาร 04 ยังไม่ได้ติดตั้ง ต้องแยกผลทดสอบใหม่ในอนาคตจากหลักฐานเดิมชุดนี้

ผลตรวจเชิงเครื่องอ่านและ manifest เอกสารอยู่ใน DELIVERY_QA.json
