# การตรวจตอนส่งมอบ r59

วันที่ 2026-10-12

- ตรวจไฟล์ logic/test 4 ไฟล์ตรงกันทั้งโปรเจกต์จริง, candidate และ ready_package
- รัน unit guards จากโปรเจกต์จริงหลังติดตั้ง ผ่าน 8/8; บันทึกอยู่ใน project_installed_unit.log
- รัน guard ไทย “ระหว่าง/ว่าง” ผ่าน 8/8 tests ใน unit_thai_guard.log ซึ่งมี assertions เพิ่มโดยไม่เพิ่มจำนวน test methods
- ก่อน/หลัง DB logical hashes ตรงกัน 4 ฐาน: production project, production package, DEMO 720, DEMO 240
- สำเนา source ก่อนแก้ตรง hash เดิมทุกไฟล์ที่สำรอง
- Git status entries ที่มีตั้งแต่ก่อนแก้ยังอยู่ครบ; ไม่ใช้ reset/clean/commit และไม่ได้ลบงานที่ยังไม่บันทึก
- ข้อมูลกลางจริงยัง 41 heads, 41 revisions, 0 releases ทั้งโปรเจกต์และแพ็กเกจ ไม่ publish หรือแก้ facts แทนเจ้าของ
- เอกสาร 4 ฉบับถูกเพิ่มในโฟลเดอร์ docs/common_content_r59_20261012 ใหม่ของทั้งสามชุด ไม่ทับ docs r58
- โปรแกรมที่เปิดอยู่ไม่ได้ restart ในรอบนี้ จึงยังต้องเปิดโปรเซสใหม่ก่อนใช้ source รุ่นล่าสุด

FINAL_VERIFICATION.json เป็น receipt หลักสำหรับ hashes/counts/path; FINAL_SOURCE_DIFF.patch เป็น diff โค้ดล่าสุด เอกสารนี้เพิ่มภายหลัง receipt และไม่เปลี่ยนโค้ดหรือฐานข้อมูล
