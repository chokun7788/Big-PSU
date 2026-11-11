# แผนวงรอบแก้ปัญหาจาก log

อ่าน [รายงานผล log](../r135_log_analysis_20261112/REPORT_TH.md) และ [งานวิจัยที่คัดเลือก](../r135_log_analysis_20261112/RESEARCH_FOLLOWUP_TH.md) ก่อนเลือกงาน ถ้างานนั้นมีผลผ่านแล้วและไม่มี change อย่าทดสอบเดิมซ้ำ

รอบ01: แก้ false duration notice ของ same-audience service alternatives ตาม LOOP01_REPORT_TH.md ผลแต่ละรอบอยู่ใน LOOP01_MANIFEST.json ไม่ใช่คะแนน semantic accuracy หรือผลรอบรวมใหม่

Flow: raw request + pinned snapshot/time → bounded spelling/need spans → source-bound entity/service/platform/audience → typed reads/calculation → independently check every delivered line → request coverage/partial state → final text + provenance + logs

หลักฐาน duration ของหลายบริการต้องครบทุก alternative ที่ส่ง หากมีหนึ่งบรรทัดผิดหรือไม่ยืนยันต้องไม่เอา proof ของบรรทัดอื่นมากลบ ไม่บวกราคา alternatives เป็นยอดซื้อ และไม่เปลี่ยน authority/currentness caveat

งานต่อ:

1. ตรวจ actual failure ของ audience typo ที่ทำให้ส่งหลายกลุ่มรวมราคา PSU0บาท แยกการถามยืนยันจากการแสดงราคาทุกกลุ่ม
2. ตรวจ denied/timeout/schema/store taxonomy และ cooldown recovery จาก receipts; parent มี half-open/kind isolation อยู่แล้ว ห้ามอ้างว่ายังไม่มีโดยไม่อ่านและทดสอบ ห้ามปิด health guard หรือ reset/หยุด protected model
3. แก้ completion/output reconciliation สำหรับกรณีตอบแล้วบอกว่า need เดิมยังไม่ตอบ โดยตรวจ actual parent ล่าสุดก่อน
4. owner/editor HTTP lifecycle, attachments/source scope และ sparse categories ตามแผนเดิม

ทุกกลุ่ม: เก็บ before → แก้สาเหตุร่วมหนึ่งชุด → positive/negative/affected regression หนึ่งรอบ → ตรวจคำตอบจริง claims/receipts/terminal state → เก็บ log/limitations → เลือกกลุ่มถัดไป แนวทางเดิมล้มสองครั้งให้เปลี่ยน/ถอน/พัก

รอบรวมใหม่ต้องมี substantive integration change และใช้ worker1/manifestเดิม ไม่ฝึก weights จาก holdout ไม่ rerun/regrade R132 ไม่ติดตั้ง production ก่อน gates/backupWAL เก็บ raw/DB/logs บน D เท่านั้น

ผู้ใช้ให้ทำต่อจนสั่งหยุด การรายงานทุก6ชั่วโมงต้องอ้างเฉพาะงานและ process ที่เกิดจริง ไม่อ้างว่าได้ทำต่อเนื่องระหว่างรอบ
