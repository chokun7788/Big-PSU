# R134 — แก้ต่อและใส่ใช้งานแล้ว

ตัวเปิดแชทเดิมและ `Open-Current-Chat.cmd` ใช้R134ที่ http://127.0.0.1:8115/ แล้ว ตัวแก้ข้อมูลพอร์ต8116ใช้ฐานเดียวกัน ตรวจprocess, runtimeversion, loaded-source fingerprint และตัวเปิดจริงผ่าน `INSTALLATION_VERIFIED.json`

พบจากการเทียบคำตอบจริงว่า **resolution** ใน **dispute resolution** ถูกตีเป็นความละเอียดจอ จึงตอบกฎBrightness/Resolution/Crosshairแทนข้อพิพาท และทำให้คำถามตั้งค่าTekkenแสดงหัวข้อDisputeResolutionเกินขอบเขต

แก้การแยกความหมายทั้งฝั่งคำถามและฝั่งข้อความหลักฐานในtopic matcher: ข้อพิพาทไปอ่านกฎการตัดสิน/ประท้วง ส่วนคำถามความละเอียดจอและมาโครยังรักษาทั้งสองประเด็น ไม่ใส่ค่ากฎหรือrecord IDsธุรกิจในruntime

ตรวจแล้ว:

- การแยกความหมาย7checks, core54checksและfollowup9checksผ่าน โดยไม่เรียกโมเดล
- APIบนรุ่นติดตั้งจริง3คำถามที่ได้รับผลกระทบ อ่านsourceตรงชุดที่ตรวจไว้ทั้งหมด ไม่เรียกโมเดล
- CS2ข้อพิพาทอ่านsection006/057/058; Tekkenตั้งค่าอ่าน003/004และไม่เอา008ข้อพิพาทมาตอบ; CS2ตั้งค่า+มาโครอ่าน045/046ครบ
- ย้ายข้อมูลจากR133ที่ผู้ใช้ใช้งานจริงด้วยSQLitebackupรวมcommittedWAL เก็บฐานข้อมูล/approvals/ประวัติแชทและlogs ไม่เอาฐานทดสอบตรึงไว้ไปทับข้อมูลใช้งาน ตรวจdigestทุกtableของknowledge/approvalsตรงก่อนและหลังเปิดรุ่นใหม่ มีbundleและตัวเปิดรุ่นก่อนสำหรับย้อนกลับ

โมเดลยังเป็นTyphoon2.5Qwen3-4B HFNF4BF16 ใช้weightsR121retainedสำหรับcontextplanner ส่วนselector/genericใช้base ไม่promoteweightsใหม่ที่เคยถอยในcriticalreview ตัวบังคับJSONที่เตรียมไว้ยังไม่เปิดจริง จึงไม่อ้างผลจากมัน

ชุดทดสอบ10%เดิม2111คำถาม/5584grade identitiesยังรันบนfrozenR132 ส่วนR133/R134เป็นfollowupที่แยกผลไว้ การเทียบsource replayใช้rawเดิมเฉพาะคำขอที่ตรวจตรงกัน ไม่มีbaselineinference/regradeใหม่ กรณีwire/transport/health stateเทียบไม่ได้คงunassessed และไม่ใช้เวลาreplayอ้างเวลาinference

ยังต้องรอcoverageทั้งหมด ตรวจchangedanswers/source regressionsและทำroot-cause/คะแนนรวมแยกภาษา ขอบเขต76requirements/14หมวดคงอยู่ ยังไม่ประกาศFlowครบ100%หรือsemanticaccuracyจากchecksเหล่านี้ ข้อจำกัดauthority/version/translation/source gapsและtail latencyยังต้องรายงานตามผลจริง

หลักฐาน: `RESOLUTION_VERIFICATION_LATEST.json`, `LATEST_CORE_VERIFICATION.json`, `FOLLOWUP_VERIFICATION_LATEST.json`, `INSTALLATION_RECEIPT.json`, `INSTALLATION_VERIFIED.json`, `PREPARED_UPGRADE.json`, `REQUIREMENTS_TRACEABILITY.json`
