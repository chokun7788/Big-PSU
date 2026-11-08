# ผลแก้และวิเคราะห์ r56.7 · 10 ต.ค. 2026

## ผลที่ยืนยันอัตโนมัติในขอบเขตทดสอบ

- Source unit/fixtures: 110 tests, failures 0, errors 0 ใน10 modules รวม calendar/VR/maintenance/closure/API faults/queue/conversation
- เว็บบริการ: 156 requests บน r56.7, fail 0; content contracts 145 ข้อ + live transport/format 11 ข้อที่ไม่ได้ตรวจ independent truth ในรอบนี้
- เว็บสำนวนใหม่/context: 38 requests, fail 0 ตาม mandatory text/negative checks; ไม่ใช่ทุกข้อความใหม่ในอนาคต
- Oracle wrong-answer mutations 11/11 rejected; frontend protocol mock checks4ผ่าน; ไม่ใช่ human/browser visual QA ทุกหน้าจอ
- Full rulebooks: 28 requests บน r56.5, 8 game/locale section-ID checks ผ่าน; codeกฎ/source hashesตรงรุ่น7 (รุ่น6–7แก้creativeเท่านั้น) CS2 56/56, RoV12/12, Tekken7/7, VALORANT25/25 ทุกภาษา
- RoV coverage12/12 เป็น recorded-section coverage; outcome answered_partial เพราะต้นฉบับข้อ6.1.5/6.1.5.1ยังขาด ไม่ใช่ครบกฎจริงทั้งหมด คำแปล fragment ของ agent มี label และ SHA match ก่อนใช้
- Portable WithModels: actual launch พร้อม bundled Python/Ollama บนพอร์ต8096 และคำถาม smoke 3 ข้อ, fail 0; ไม่ใช่ clean machine certification

## ทำไมเคยตอบผิด และแก้ตรงไหน

1. **ข้อความหลายหัวข้อถูกดักตอบข้อเดียว**: typed plan/server adapter ตอบ policy ก่อน compound; แก้ delegation และแยก clauses2–6, source child binding ไม่ให้ราคาขาดเงื่อนไข
2. **คำปฏิเสธกิน target ข้างหลัง**: regexข้าม not a student ไปยังPC; ผูกคำปฏิเสธกับชื่อบริการทันที และแยกคำขอใหม่เมื่อปฏิเสธงานก่อนหน้าโดยชัดเจน
3. **ที่จอดรถถูกมองเป็นจอ**: keywordจอไม่มีขอบเขต; แก้จอ(?!ด) จึงตอบ address+parkingครบ
4. **รูปประโยคจริงไม่เข้าคิวบริการ**: “คนเล่นไม่มีชื่อในรายการ”/forgot logout word order; เพิ่ม cues ที่อธิบาย action+subject จริง ไม่เติม policy
5. **APIหลายlookupอาจเห็นคนละ snapshot**: ใช้ request-local snapshot/date/transport ร่วมกันในคำตอบเดียว แต่คำถามถัดไป refresh ไม่ใช่ cacheสถานะเก่า
6. **RoV ENขาด section**: validatorถูกที่ไม่เรียก untranslated fragmentว่า complete; เพิ่มเฉพาะแปลข้อความที่อ่านได้แบบ hashbound + sourcegap warning ต้นฉบับไม่ถูกแก้
7. **คิวทำให้เข้าใจผิดว่าโมเดลช้าเท่าทั้งjob**: ก่อนนี้ไม่แยก elapsed/dispatch; ตอนนี้มี timingfields/UI label และเก็บ trace, lastdispatchไม่ใช่ cumulative GPUtime
8. **เขียนคำเชิญENตอบเกม42เกม**: English inventoryguardมาก่อน creationintent; named taskเลือก general creation ก่อน incidentalgamewords แต่ actualstudiofactrequestยัง grounded
9. **80คำใช้ cap25คำ**: wordprofileจับขั้นต่ำ100; ลดเฉพาะ explicitwordrequestถึง30และปรับboundedtokenbudget
10. **ระหว่างถูกเป็นว่าง/เติมวันเวลาเอง**: factualregexไม่มีboundary, promptไม่ชัดและ longcreationrejectไม่ได้repair; จำกัดregex เพิ่มpromptและrepairครั้งเดียวภายใต้deadline เก็บrejectguardเดิม

## โหลดพร้อมกันบนเครื่องนี้

| ชุด/พร้อมกัน | median วินาที | max วินาที | ผลไม่ผ่านเกณฑ์ |
|---|---:|---:|---:|
| fast/1 | 0.23 | 0.23 | 0 |
| fast/2 | 0.37 | 0.47 | 0 |
| fast/4 | 0.83 | 1.01 | 0 |
| fast/8 | 1.31 | 1.95 | 0 |
| llm/1 | 5.11 | 5.11 | 0 |
| llm/2 | 6.20 | 7.87 | 1 |
| llm/4 | 9.48 | 15.36 | 1 |
| llm/6 | 12.78 | 20.20 | 1 |
| mixed/8 | 2.18 | 10.62 | 1 |

finite warm batches ไม่ใช่ sustained maximum capacity; nสูงสุดแต่ละชุดมีsampleเท่าจำนวนn จึงไม่ใช้ p95 เป็น production SLO งานLLMยังใช้sharedlimit1 ต้องรอคิว ส่วนfastใช้workersได้โดยไม่รอGPUทั้งหมด

Load7 เหลือ 4 คำตอบไม่ผ่านเกณฑ์; รายละเอียด/provider/draft/repair อยู่ load_final7_failures_extracted.json: EN invitation3ครั้งความยาวต่ำกว่า64คำหลังrepair1ครั้ง, THdialogue1ครั้งวนซ้ำจนtokenlimit. เป็นผลซ้ำของคำถามบางแบบ ไม่ใช่4uniquebugs. Modeเดิม general_rag_miss_llm_unavailable ยังเป็นชื่อlegacy; llm_failure_reason/rejected_reasonแสดงoutputquality. ไม่ใช่ automatic transport outage ผลLLMไม่รับรองความลื่นของภาษาไทยหรือwordcountภาษาไทยตรง80ทุกคำ

งานเขียนทั่วไปยังมีข้อจำกัด จึงไม่ปิดT34/T35ทั้งหมด; คำตอบที่rejectไม่ได้ถูกปล่อยให้ผู้ใช้เป็นข้อมูลศูนย์ที่ยืนยันแล้ว

## การตีความผลแต่ละรอบ

- baseline38มี15fail (รวมoracle3ข้อ); targeted1เหลือ4 (oracle3+namedplayer1); targeted2/3ผ่านหลังแก้ตามsource
- v1contractaudit8failส่วนใหญ่oracle; v2เหลือ2tracebindingcompoundที่คำตอบเดิมถูกอยู่แล้ว จึงแก้evidenceไม่แต่งราคาหรืออ้างผลเดิมผิด
- load6fail4: providerstopไม่ได้truncation/timeoutหลัก แต่inventedtoday/tonightและroutefalsepositive; loop7แก้prompt/repair/regex ไม่ลดvalidationเพื่อเพิ่มคะแนน
- HTTPconnectionrefusedครั้งแรกหลังrestartเกิดก่อนserverlisten; ไม่ใช่failedanswercontract การรันหลังhealthreadyมีไฟล์web_final7
- Portable startupแรกผ่านแต่พบworker override; StopแรกfailเพราะcurrentcultureThaiแปลISOyear2026เป็น1483. แก้helperInvariantCulture+RoundtripKindโดยไม่ผ่อนPID/path/timechecks. ตัวหยุดจริงผ่านหลังแก้ และเปิดซ้ำใช้worker2; เก็บlauncherก่อนแก้+hash+testผลไว้ ไม่แก้R50

## เก็บรักษาและแจกใช้งาน

Snapshot484ไฟล์, changedexisting12, addedrelevant5, originalsourceที่หาย0, owner38ไฟล์hashไม่เปลี่ยน; candidate/app/webและแต่ละแพ็กเกจruntimeData495ไฟล์ไม่มีhashmismatch
ไฟล์sourceเดิมที่แก้มีcopyก่อนแก้+diff; originallogsไม่ได้hashทั้งหมดแต่ไม่มีการตั้งใจdelete/truncate; ผลแต่ละรอบและpackagesR50ไม่ถูกแทนที่ Gitmetadataเดิมbrokenจึงใช้snapshotdiff ไม่claimgitclean

แพ็กเกจใหม่: C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_R56_20261010
01_Download_Modelsประมาณ3.02GB โหลดweightsอีก3.65GBครั้งแรก;02_With_Modelsประมาณ6.68GBมีweights (decimalGB) ขนาดเทียบตอนbuildก่อนnewsmokelogs
ไฟล์modelcheck/hashpassของWithModelsแยกจากready=falsemissing2ของDownloadModelsที่ตั้งใจไม่มีweights; เว็บจองยังต้องinternet

เอกสารต่อ: FLOW_FINAL.md, REMAINING_AFTER_R56.md, PRESERVATION_AND_PACKAGE_AUDIT_7.json, source_changes_7.patch, SUMMARY.json

## ตรวจท้ายรอบ

- Candidate runtime data495ไฟล์ตรงกับโปรเจกต์จริง ดู CANDIDATE_RUNTIME_DATA_AUDIT_7.json
- ตัวเปิด/หยุดทั้ง2แพ็กเกจhashตรงกัน, worker2 และ LLM admission1 ตรวจใน PACKAGE_RUNTIME_AUDIT_7.json
- Portable healthหลังแก้: warmupok, workers2alive/ready; smokeคำตอบ3ข้อผ่าน แล้วStopของแพ็กเกจหยุดได้จริง เก็บmodel_check7.jsonและpackage_process_identity_tests.json
- ประวัติ/stateที่เกิดจากsmokeของแพ็กเกจใหม่ถูกย้ายเก็บใน portable7c_runtime_evidence หลังหยุดแล้ว จึงไม่ติดไปกับชุดแจก ไม่มีการลบlogเดิมของโปรเจกต์หรือR50
- RAMload96%ในportable smokeเป็นการเปิดหลายสำเนาพร้อมกันบนเครื่องพัฒนา ไม่ใช้เป็นRAMขั้นต่ำหรือcapacityของruntimeเดี่ยว
- Activeเว็บ8093ยังเป็นr56.7 workers2ready, LLMactive0/waiting0; portable8096ใช้เฉพาะsmokeและหยุดแล้ว
