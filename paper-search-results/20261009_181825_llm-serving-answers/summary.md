# สรุปงานวิจัย

ค้นและตรวจแหล่งต้นฉบับ 19 งาน เทียบกับผลวัด r51 และอ่านโค้ดที่เกี่ยวข้อง พบว่าต้องแก้ทั้งการเข้าใจคำถาม การตรวจคำตอบ ความครบของ output และคิว

สิ่งที่ทำได้ก่อน:

1. แก้ price/scope guards และใช้ AnswerPlan เดียวทั้งระบบ คำ rate ปัจจุบันถูกนับเป็นทั้งราคาและ usage; each ถูกใช้เป็น scope บริการแม้หมายถึงกล่อง/protocol
2. คง metadata เมื่อ timeout แยก model unavailable / source missing / contract failed
3. สร้างคิวงานมีขอบเขต พร้อม job ID และ fairness ใช้ model broker ร่วมทุก process/ทุก LLM call
4. จัด token budget ตาม task/ภาษา/ความยาว ตรวจเนื้อหาที่ต้องมี ไม่เรียกข้อความสองประโยคว่าทำคำขอ 500 คำครบ
5. แสดง progress และรักษา validated final; ทดลอง parallel 1 เทียบ 2 บน runtime แยกหลัง P0 ผ่าน

งานอย่าง Orca/PagedAttention/Sarathi ต้องมี inference engine รองรับ ส่วน DistServe ต้องหลาย GPU ไม่มีงานใดรับรองว่าเพิ่ม worker แล้ว RTX4050 6GB จะตอบทุกงานพร้อมกันโดยไม่ช้าลง

อ่านรายละเอียดใน [report.md](report.md) และวิธีดำเนินการใน [FLOW_IMPLEMENTATION.md](FLOW_IMPLEMENTATION.md) มี reading ledger, exports และ search log ประกอบ

ข้อจำกัด: Setup ของ paper-search-pro ยังขาด OpenAlex API key/NCBI email จึงหยุด helper workflow แล้วค้น web จากแหล่งต้นฉบับแทน นี่เป็น targeted review ไม่ใช่ Standard หรือ systematic search ที่เสร็จครบ ไม่อ้าง coverage หรือ citation counts

รอบนี้สร้างเอกสารวิจัยและแผน ไม่เปลี่ยนโค้ด/นโยบายหรือ log เดิม และไม่รันทดสอบโหลดใหม่
