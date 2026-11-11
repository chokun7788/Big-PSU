# Flow ทำงานปัจจุบัน

รุ่นทดลองนี้ยังไม่ปิดการตรวจรับR135ครบ48/76ข้อ ฐานทำงานล่าสุดคือ `system/data/knowledge/verified_sources.sqlite` เก็บ `common.sqlite` เดิมไว้ ห้ามคัดลอกฐานเก่าทับฐานใหม่

1. ตรึงraw question,บริบท,เวลาและsnapshot
2. แยกสิ่งที่ถามและผูกเป้าหมายกับrecordจริง
   ก่อนตีความใช้bounded intent-edit channelจากhelpersเก่า ป้องกันชื่อ/ตัวเลข/เงื่อนไข เก็บrawและedit receipts ถ้าคำแนะนำหลายความหมายถามกลับ และKEEPเมื่อโครงงานเดิมกับฉบับแก้เหมือนกัน ดูTYPO_RECOVERY_TH.md
3. ใช้typed readerหรือcompatibilityที่ประกาศไว้ร่วมกับsource/receipt verifier ไม่ใช้fallbackเพื่อเลี่ยงการปฏิเสธหลักฐาน
4. ตรวจservice/platform/audienceสำหรับราคา และsource-attested center relationสำหรับpolicyที่ประกาศขอบเขตไว้
5. ตอบส่วนที่ผ่านก่อน ไม่ใช้คำถามเดิมเป็นหัวข้อคำตอบFAQ;เก็บส่วนที่ยังขาดและเหตุผลตรงกรณี
6. ใส่public citationเฉพาะexact text+record+sourcepinsที่ตรวจแล้ว คงinternalreceiptsแต่ซ่อนpublicmarkersที่ไม่มีหลักฐานเว็บ
7. การแก้/ถอนข้อมูลต้องอ่านrevisionใหม่และไม่ใช้webcitationเก่ารับรองข้อความที่เปลี่ยน
8. ตรวจpositive/negative/affected regressionตามสาเหตุร่วม เก็บผลก่อนแก้ เปลี่ยนแนวทางเมื่อวิธีเดิมล้มซ้ำ ไม่วนunchanged

หลักฐานรอบข้อมูลเว็บอยู่ `VERIFIED_SOURCE_FLOW_TH.md` ผลรวม200ที่ตรึงไว้และข้อจำกัดอยู่ `../r135_verified_eval200_20261111/evaluation/REPORT_TH.md`

previewล่าสุด8141ใช้working codeหลังแก้เฉพาะจุดเพิ่ม ส่วน8140เป็นfrozen measured trial ผล196/255literalไม่รวมpost-eval patches ต้องไม่อ้างคะแนนใหม่โดยรวมผลเฉพาะจุดเข้าไป

ลำดับต่อไป:จัดกลุ่ม36unavailableจากtraceจริง โดยแยก15store/snapshot codeจาก21model transport codeก่อนสรุปสาเหตุ ตรวจowner/editor HTTP lifecycleและsource scopesที่ยังขาด ภาพ/เอกสารแนบที่เว็บเข้าไม่ได้ยังไม่รับรอง ไม่deployproductionก่อนgates/backupWAL

อัปเดตการแยกสาเหตุ:15caseที่ติดรหัสstoreเดิมทั้งหมดมาจากr101_model_unavailable ไม่มีstore_error_type โดย13มีcontext-kind cooldown denialและ2มีtimeout ดูUNAVAILABLE_ATTRIBUTION_TH.md แพตช์reason labelsผ่านreplay20checks แต่ยังไม่แก้admission/timeoutและยังไม่โหลดแพตช์นี้เข้าpreviewเดิม
