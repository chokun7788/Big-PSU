# Flow แก้จากผลคำถามบริการจริง r54

## ขอบเขต

ใช้ผล156คำถาม+2paginationrequests ของr53.3 เป็นหลัก เลิกจัดบทความ500คำเป็นpriorityหลัก บริการยาวให้วัดครบหัวข้อ/แพ็กเกจ/กฎตามsource ไม่ใช้จำนวนคำแทนcoverage

## ลำดับลงมือจากหลักฐาน

1. Snapshot source+owner hashes ขอระบบอนุญาตเขียนROOTก่อนแก้ source เก็บไฟล์และlogเดิม สร้างcandidateใหม่ไม่เขียนทับr53.3
2. P0 time/entity: แยกclock/date/amount/durationจากstation number ก่อนแยกหมายเลขเครื่อง ใช้colon/โมง/unit guardทั้งexactและfuzzy ไม่เติมaliasเฉพาะVR9; tests PC1 vs PC10 vs PC10:00, VR09:00, VR#1เวลา09:00 ไทย–อังกฤษ
3. P0 policy: parseคำถามเป็น operation+subject และfieldที่ขอ ส่งwrong-slip/group-checkinเข้าข้อมูลเจ้าของก่อนretrieval generic booking; negative tests จองผิดเครื่องกับสลิปผิดต้องใช้คนละขั้นตอน
4. P0 typed filters: customer group/number words/duration/people ต้องคงจากraw inputสู่plan ตรวจrequired slotcoverageก่อนเรียกanswered_complete; ห้ามconfidenceสูงพร้อมslotสำคัญหาย
5. P1 multi-clause: สร้างtasksเป็นชุดพร้อมrequested_fields, targets+timeรายclause ไม่ให้early-returnของราคา/location/liveทำอีกคำถามหาย; missing fieldต้องตอบunknownเฉพาะส่วนนั้น
6. P1 dialogue: เก็บdomain/operation/target/filter/coveragecursorจากคำตอบที่acknowledged “ทั้งหมด/ต่อ”เป็นactอ้างงานเดิมเมื่อมีscopeพอ ไม่ทำtopic_shiftเพราะคำกฎในfollowup; paginationต้องพิสูจน์returned union=expected56 ไม่มีซ้ำจนจบ
7. P1 domain paraphrases: จับความสัมพันธ์จำนวนคนกับการเลือกบริการ และpermission/price/location/controls/specแยกกัน ทดสอบคำใหม่ที่ไม่ใช้พัฒนาและคำหมวดใกล้เคียง อย่าเพิ่มaliasประโยคหนึ่งต่อหนึ่งเป็นคำตอบหลัก
8. P1 budget: operation affordability ที่รับbudget,group,service,package duration/capacity คำนวณinteger sessionsและเงินเหลือจากsource ไม่แต่งfractional pricing; groupขาดถามยืนยัน ไม่บังคับAdult
9. P2 evidence/rendering: source contaminationแก้ในcurated layerพร้อมprovenance ส่วนmappingที่ยังไม่ตรวจเครื่องจริงคงflag; maintenanceใช้schedule; parking/spectator permissionต้องแยกfee status
10. ตรวจtime-out traceให้เก็บขั้นตอนล่าสุดก่อนfallback ไม่อ้างทุกtimeoutเป็นโมเดล/GPU; ทดสอบ latencyหลังความถูกต้อง ไม่เพิ่มmodel concurrencyจากชุดsequentialนี้

## Loop และเกณฑ์รับ

baselineเคสผิด→unitของoperation/slotที่ถูกและผิด→mockedfixture→candidateใหม่→เว็บเคสผิด+เคสใกล้เคียงที่เดิมถูก→วิเคราะห์trace/false positives→แก้ซ้ำเฉพาะหลักฐาน→รายงานผลแยกตามชั้น

- ไม่ให้transport_completed=correctness
- PASS_TARGET_ONLY≠full-rule coverage
- SAFE_UNCONFIRMED≠bugที่ต้องให้โมเดลเดา
- LIVE_UNVERIFIED≠สถานะจริงผิดหรือผ่าน ต้องมีoracle/timestampตรงกัน
- คำตอบเปลี่ยนรูปแบบช่องว่างไม่ควรfail ถ้าความหมาย/เลข/หน่วย/sourceตรง
- finalcandidateเทียบsource hashes, ownerdata38ไฟล์ต้องตรงก่อนแก้ และเก็บtestoutputsใหม่ทุกloop

Flowนี้วางจากผลทดสอบ ยังไม่ได้เรียกแต่ละfixว่าทำแล้ว รายการsource/current policyที่ownerยังไม่ยืนยันแยกในRESULTS_ANALYSIS_TH.md
