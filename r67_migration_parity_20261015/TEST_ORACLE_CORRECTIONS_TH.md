# ตรวจความถูกต้องของตัวทดสอบเอง

เก็บ FOLLOWUPS_final05.json ไว้ทั้งหมด ไม่ทับผลเดิม

1. เคส PC notes → PS5 เดิมตรวจเพียงชื่อ PlayStation จึงปล่อยคำถามขอให้ผู้ใช้ระบุรายละเอียดผ่านได้ เป็น oracle ที่อ่อนจริง แก้ให้ต้องพบหมายเหตุของ PS5 เต็มข้อความ แล้วแก้ dialogue ให้คง field เดิมเมื่อผู้ใช้เปลี่ยน entity แบบสั้น และ field นั้นใช้กับ entity ใหม่ได้
2. เคส “บุคคลภายนอก” เดิมคาด 70 บาททันทีและเรียก CommonAnswerer โดยตรง เป็นสมมติฐานผิด: กลุ่มภายนอกยังไม่ระบุว่าเป็นนักเรียน/นักศึกษา/บุคคลทั่วไป และ protected clarification อยู่ใน pipeline ชั้นนอก ไม่ควรแก้ระบบให้เดาว่าเป็น General Adult เพื่อให้ test ผ่าน เปลี่ยนเป็นการทดสอบกลุ่มที่ระบุชัดและตามด้วยการเปลี่ยนกลุ่มโดยรักษาเวลา/บริการ
3. ผล audit raw text รอบแรกเทียบกับ JSON serialized ทำให้ newline/เครื่องหมายคำพูดที่ escape ดูเหมือนข้อมูลหาย แก้ auditor ให้ตรวจ string ที่ decode แล้ว ผลรอบแรกยังอยู่ OTHER_RAW_TEXT_AUDIT.json
4. คำแปล Mario Odyssey ใช้ three-dimensional แทนเลข 3 จึงไม่ผ่าน protected-literal guard แก้เป็น 3D ก่อนใช้ต่อ ไม่ปิด guard; revision ที่บันทึกก่อนหน้าถูกเก็บไว้ และการรันต่อข้ามค่าที่ไม่เปลี่ยน

ผล 210 คำถามเป็น source-focused behavior ไม่ใช่ full test; 223 คำถามเป็นชุดเดิมต่อโหมด OFF ไม่ใช่ legacy rerun ผลเปิด flag ON ที่ไม่เกิด model call ไม่ใช่หลักฐาน model transport/semantic inference
