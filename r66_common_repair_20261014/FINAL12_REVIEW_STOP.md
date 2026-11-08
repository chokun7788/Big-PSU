# final12 หยุดเพื่อแก้ procedure scope

ชุด targeted OFF ผ่านรวม scoped topics เดิม 10 tests แต่การอ่าน schema ทบทวนพบว่า procedure.preconditions เป็น typed conditions เช่นเดียวกับ policy.conditions_all ตัว scoped search เดิมเช็กแค่ known จึงอาจเสนอขั้นตอนของบริการอื่นหากหัวข้อเหมือนกัน

หยุดเฉพาะ owned matrix_off child PID 31648 (parent 12348) หลังตรวจ command line; parent บันทึก interrupted_or_failed ตามจริง ไม่มีการแก้ raw log/status ให้ดู complete ไม่อ้าง final12 เป็นผลครบ OFF/ON และไม่เขียน app ระหว่าง matrix ที่ยังทำงาน

แก้ให้ procedure และ policy ใช้ scope predicate เดียวกัน เพิ่ม positive สองบริการคำตอบคนละแบบและ negative precondition mismatch รวม scoped tests ใหม่ 11 tests ก่อนรันรอบใหม่ที่มี manifest/snapshots ใหม่
