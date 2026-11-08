# ลูป E — แก้ช่องว่างที่ยังมี source อยู่หลัง final11

## หลักฐานที่ต้องใช้ก่อนแก้

`AUDIT_final11/ALL_FAILED_GRADES.json`: แยกคำแปล/ถ้อยคำที่เทียบไม่ตรง อัตราหมดอายุ และปัญหาการอ่านข้อมูลจริง ไม่เปลี่ยน gold เพื่อให้ผ่าน

1. ที่ตั้ง: center.address unknown แต่เจ้าของเคยให้ที่อยู่ครบและมี FAQ location เดิม ต้องกู้ source/pointer มาเป็นร่าง ไม่ให้โมเดลตั้งที่อยู่
2. policy/ค่าปรับ: ชื่ออุปกรณ์ต้องเป็น scope ไม่ใช่ตัวบังคับให้เลือกเฉพาะ service fields ค้น policy/FAQ topic ที่มีหลักฐานตรงเรื่องและใช้ source priority เดิม ไม่เปลี่ยนตัวเลข/เงื่อนไข
3. FAQ ที่เลือกด้วยชื่อ/หัวข้อได้แล้ว: ถ้าผู้ใช้ขอเนื้อหา ไม่ควรถามว่าอยากได้ field ไหน; metadata ที่ไม่รู้ไม่เพิ่มเอง; explicit metadata request ยังต้องรายงานขาด
4. คำถามจอง: แยก “ต้องจองไหม/ไม่จองได้ไหม” จาก “จองขั้นตอนอย่างไร” โดยอ่าน FAQ ที่ตรง operation จากข้อมูลเดิม
5. อุปกรณ์: family label ที่มีในชื่อ เช่นส่วนก่อนคำว่า รุ่น แยกจาก model suffix ได้ โดยไม่เพิ่มชื่อรุ่น/นโยบายเอง
6. แพลตฟอร์มราคา: ใช้ equivalence เดียวกับ control presets เช่น PS5 กับ PlayStation 5 และคง PS4 แยก ไม่ให้ราคาหายเพราะรูปแบบข้อความ
7. เกมรายเครื่อง: ตรวจ service/resource/game relation และ source เดิมก่อน หาก source ไม่ยืนยัน negative ให้ตอบเฉพาะที่ยืนยันและระบุช่องว่าง ไม่ใช้ absence เป็น not-installed โดยเดา

## ตรวจทานรอบ 1 — ป้องกัน scope เปลี่ยนเป็น facts

การค้น topic policy ไม่ให้ชื่อบริการบังคับโทษทุกเกม; source ต้องระบุเงื่อนไขความเสียหายเอง; กติกาแข่งและกฎการใช้ศูนย์แยก ไม่ใช้ penalty ธรรมดาทับเกม

## ตรวจทานรอบ 2 — FAQ default ต้องไม่กลบ explicit detail

default answer ใช้เมื่อจับ FAQ ได้ชัดและไม่ได้ถาม field อื่น ไม่ใช้เมื่อ target fuzzy เสี่ยง หรือมีหลาย FAQ ไม่ตรงกัน การถาม scope/เงื่อนไขที่ไม่รู้ยัง partial/clarify

## ตรวจทานรอบ 3 — กู้ source ไม่ใช่แก้ owner policy

เก็บ DB ก่อนแก้และ append revisions มี original evidence refs; unknown address กู้ข้อความเดิม; unknown validity คง unknown; game/resource negative ที่ไม่มีหลักฐานยังไม่ยืนยัน; rerun common OFF/ON และ source-based regressions ไม่รัน legacy
