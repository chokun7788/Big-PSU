# ผูกเจตนา → ชนิดข้อมูล → บริการ/แพลตฟอร์ม → ต้นทาง

เริ่มใช้ใน candidate สำหรับ C06/amount: หลังตีความงานราคาแล้ว verifier ตรวจว่า claim อ้าง fact ในหมวด C06 และ record ชนิด rate จริง จากนั้นตาม service_id และ audience_id ไปยัง records ชนิด service/audience และตรวจ platform ของบริการกับ platform ที่สังเกตได้จากข้อความ task พร้อมตรวจ evidence_refs ของความสัมพันธ์ทั้งสอง

บันทึกเส้นทางที่ตรวจใน ledger `intent_source_chain`: rate ID, service ID, audience ID, platform ที่ถาม/ที่มีในต้นทาง, revision และ source refs ตัวตรวจ arithmetic, snapshot/currentness และ authority เดิมยังทำหน้าที่ของตนต่อ การมีเส้นทางนี้ไม่รับรองว่าเจตนาภาษาธรรมชาติหรือข้อมูลปัจจุบันถูกต้องทั้งหมด

หลักฐาน: `intent_source_chain_1794291454274764800` ผ่าน 5 direct checks รวม PC ปกติ, platform ผิด, service หาย, locator ความสัมพันธ์หาย และการไม่บังคับ C05 ให้เป็นราคา; currency regression `price_currency_1794291461815106900` ผ่าน12 และ natural source-only PC เดี่ยว/ผสม `pc_assessment_1794291466588699900` ใช้ตรวจการส่งคำตอบต่อ

ขอบเขตที่ยังเปิด: ชื่อบริการซ้อน/กำกวม, คำถามหลาย platform, คำปฏิเสธและทางเลือก, source owner edit/withdraw ผ่าน bridge MigratedView/HTTP, หมวดอื่นนอก C06 และ model interpretation ตัวอ่าน platform ใช้ helper เดิม จึงไม่ใช่ implementation อิสระด้านความหมายทั้งชุด ยังไม่ติดตั้ง ไม่รัน 5% และไม่แก้ DB ต้นทาง
