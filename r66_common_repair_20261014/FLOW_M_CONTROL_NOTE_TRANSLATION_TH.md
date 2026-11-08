# ลูป M — เติม English control notes จาก source เดิม

## ทบทวน 1: ขอบเขตข้อมูล

390 rows / 36 records ใน CONTROL_NOTE_OMISSIONS.json ต้องแปลเฉพาะคอลัมน์ note ไทยซึ่ง EN ว่าง รักษา game/platform/button/action เดิม ไม่แก้ mechanics จากความรู้ภายนอก ไม่เปลี่ยนนโยบาย ไม่ทำ source ที่ไม่ทราบ gesture ให้กลายเป็น gesture ที่ทราบ

## ทบทวน 2: ขั้นตอนและผลที่ตรวจได้

หลัง final18 รันครบจึงเริ่ม local model แบบ serialized เพื่อไม่แย่งกับแขน ON บันทึกทุก transport/schema/validation failure และคำแปลที่รับ ตรวจ literal digits/URLs/negations/exceptions ต่อ note แล้วตรวจ output เป็นภาษาอังกฤษจริง แยก machine draft จาก semantic review; เตรียม proposals แยกไฟล์ก่อนแตะ DB

อ่านคำแปลที่มี risk: ตัวเลข/คำห้าม/gesture/context และคำเฉพาะ เทียบไทย ห้ามเลือกหรือบิดคำแปลให้ตรง gold เพียงเพื่อเพิ่มคะแนน หากแปลไม่ได้คง fallback ไทยพร้อม pending ซึ่งลูป L รองรับแล้ว

## ทบทวน 3: revision, preservation และยืนยันใหม่

การเติม note ไม่ใช่การอนุมัติภาษาอังกฤษ บันทึก derived source และ revision ใหม่ โดยเก็บ original sources/revisions ทุกแถว ปรับ preservation audit ให้รายงานการเปลี่ยน EN อย่างเจาะจงจาก manifest ที่ตรวจ hash/old/new ตรงกัน ไม่ยกเว้นทั้งภาษา

หลัง apply หยุดแก้ข้อมูลแล้วเปิด final19 common OFF/ON บน snapshot ใหม่ ทดสอบทั้งข้อมูลที่แปลแล้วและ fallback สำหรับข้อมูลเดิมที่ยังมี note ว่าง; final18 ยังเก็บเป็นผลก่อนเติม EN notes ห้ามอ้างว่า final18 ทดสอบข้อมูลรอบ M แล้ว
