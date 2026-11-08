# รายงาน r42.4 — สิ่งที่แก้และงานที่เหลือ

วันที่ตรวจ: 6 ตุลาคม2026 — Asia/Bangkok

## สิ่งที่แก้แล้วในรอบนี้

1. กลับหัวข้อเวลา/การจอง/สมาชิก/อุปกรณ์/รายละเอียดเกม/ติดต่อหลังเปลี่ยนเรื่อง ไทยและอังกฤษ
2. เก็บหลายchildของoperationเดียว ไม่ข้ามเกมที่ไม่มีข้อมูล; รองรับpleaseและคำถามอังกฤษสองclause
3. completed turnเขียนครั้งเดียว ไม่ซ้ำhistoryหรือแทนresponseที่ผู้ใช้เห็นแล้ว
4. รักษาคำไทยเปิดปิดที่ถูก ไม่ให้fuzzyแก้ทับ และแยกISOdateจากเวลาที่ถาม
5. แยกขั้นต่ำจอง/ยกเลิก1ชั่วโมง, max3Sessions, payment10นาที, check-in30นาที; maxdays/maxdevicesตอบsourcegap
6. สมาชิก3กลุ่มไม่ถูกตอบเป็น25คน; API/logของgenericreplayไม่ติดป้ายราคา

แก้source9ไฟล์ เพิ่มtest1ไฟล์ ไม่มีไฟล์ก่อนรอบนี้หาย; backup/diff/log/releaseเก่าคงไว้

## ผลอัตโนมัติบนเว็บจริง

| ชุด | ผ่าน/ทั้งหมด | คำขอ | หลักฐาน |
|---|---:|---:|---|
| กลับหัวข้อหลัก | 16/16 | 44 | [final_r42_4_main_after_restart_20261006_162614_97ff2e_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/final_r42_4_main_after_restart_20261006_162614_97ff2e_summary.json) |
| สำนวน/หลายข้อ/ขอบเขต | 12/12 | 38 | [final_r42_4_variations_20261006_162650_7b533f_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/final_r42_4_variations_20261006_162650_7b533f_summary.json) |
| บริบท r41 | 25/25 | 54 | [final_r42_4_r41_main_20261006_162710_e311eb_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/final_r42_4_r41_main_20261006_162710_e311eb_summary.json) |
| ขอบบริบท r41 | 18/18 | 54 | [final_r42_4_r41_variations_20261006_162726_bd29d6_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/final_r42_4_r41_variations_20261006_162726_bd29d6_summary.json) |
| สองรอบราคา/กฎ/ปุ่ม | 36/36 | 72 | [adjacent_http_20261006_162751_41194a_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/adjacent_http_20261006_162751_41194a_summary.json) |
| แยกเงื่อนไขจอง | 14/14 | 14 | [final_r42_4_policy_20261006_162826_5e5ec4_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/final_r42_4_policy_20261006_162826_5e5ec4_summary.json) |
| คำขอซ้ำ/ชนกัน | 3/3 | 7 | [final_r42_4_identity_20261006_162841_38f946_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/final_r42_4_identity_20261006_162841_38f946_summary.json) |

รวม **124/124 scenarios/conversations — 283 HTTP requests** (รวมbusy/conflictที่ตั้งใจทดสอบ ไม่ใช่ทุกrequest200) และ source **135/135 test methods** ตาม [source_regression_20261006_161336_5ba98b.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/source_regression_20261006_161336_5ba98b.json).

เกณฑ์ resume หลายหมวดตรวจoperation/scope/answerเหมือนqueryเดิม; semanticoraclesเจาะสมาชิกและbookingfields/fixtures รวมกับregressionsเดิม ไม่ใช่fact completenessทุกหมวดและไม่ใช่unseenholdout.

Baseline r41.3 regradeด้วยเกณฑ์เดียวกัน: source 6/16, HTTP 6/16. หลักฐานเดิมยังอยู่ที่ [BASELINE_REGRADED_R42.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/BASELINE_REGRADED_R42.json).

เวลาของคำขอที่ตอบ HTTP 200 ในชุดนี้: median 0.269 วินาที / P95 1.252 วินาที / สูงสุด 14.547 วินาที เป็นผลบนเครื่องนี้กับชุดที่เลือก ไม่ใช่เวลารับรองสำหรับทุกคำถามหรือหลายผู้ใช้

## ปัญหารันไทม์ที่พบระหว่างทำ

พบstartupMemoryError/LLM500และr42.4รอบแรกwarmupผ่านแต่chatHTTP500 รวมถึงhelperprocessเปิดไม่ได้หนึ่งครั้ง เก็บfailedrawทั้งหมดไว้ ไม่รวมเป็นsemanticwrong16เคส. Pythonที่ถูกเลือกตามPATHต่างกัน: startupแรกเคยใช้CodexPython3.12 แต่escalatedlauncherเลือกinstalledPython3.13; source testsใช้ReadyPython.

เริ่มใหม่ด้วยPythonเดียวกับsource testsโดยปรับPATHเฉพาะprocess; healthสุดท้ายwarmup=True / LLMpreflight=True และตรวจAPIจริงตามตาราง. นี่เป็นการกู้ระบบและทำให้interpreterแน่นอน ยังไม่พิสูจน์ว่าPythonversionเป็นสาเหตุเดียวหรือปิดmemory/rootcauseครบ.

## การรักษา source และข้อมูล

- app/webตรงcandidate 140/140ไฟล์
- calendarเจ้าของ/servicepolicy/competitionchunks/reviewqueue/rates hashเหมือนเดิม5/5
- ไฟล์ความรู้ curated/rules ที่เทียบต้นทางกับชุดใหม่ตรงกัน 22/22 ไฟล์
- Gitstatusและdiff-checkรอบตรวจถูกroot exit0; failedsafe.directoryครั้งแรกเก็บแยก
- [SOURCE_CHANGE_R42_4.diff](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/SOURCE_CHANGE_R42_4.diff) และ [SOURCE_AUDIT_R42_4.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/SOURCE_AUDIT_R42_4.json)

## ที่ยังเหลือ เรียงลำดับ

| ลำดับ | ยังต้องทำ | ทำเองได้ / ต้องมีข้อมูล | ขั้นถัดไป |
|---|---|---|---|
| P0-1 | การเริ่มระบบเคย MemoryError/HTTP500 และเลือก Python ตาม PATH | ตรวจและแก้เองได้ | เก็บ executable/version/resource/worker-stage ทุก launch; pin interpreter, ทดสอบ recovery; ยังไม่สรุป root cause จาก restart ผ่าน |
| P0-2 | source facts บางเรื่องขาดหรือขัดกัน | ต้องต้นฉบับ/เจ้าของ | ราคาปัจจุบัน, Tekken pause, RoV ข้อขาด, เพดานวัน/จำนวนเครื่อง; คง missing/conflict guard |
| P1-1 | content completeness ยังไม่เป็น oracle ทุกหมวด | ทำเองจาก source ที่มีได้ | แยก required facts/units/conditions แล้วตรวจ output จริง ไม่ใช้ mode/confidence หรือความเหมือนของ answer แทนความถูกต้อง |
| P1-2 | สำนวน/typo และบทสนทนายาวที่ไม่เคยใช้พัฒนา | ทำเองได้ | ชุดสำรองแยกจาก training/debug; แยก typo/short choice/topic shift/negation/time filters; ไม่เปิด full20k ในงานนี้ |
| P1-3 | วันเวลาใหม่เมื่อ return ยังต้องถามบางกรณี | ทำเองได้ | รวม filter แบบ typed ที่ไม่ทิ้งวันเวลา; bare all หลายมิติยังต้องถามเจาะจง |
| P1-4 | version/package data/translation drift | ทำเองได้ | ตรวจ manifests และ source hashes ทุก publish; ไม่ใช้พอร์ตเก่าแทน candidate |
| P2-1 | ชุดแจกสองแบบและเครื่องใหม่ | ทำเองด้าน build ได้ | rebuild WithModels/DownloadModels, pin Python/dependencies, ตรวจ extraction/launch/model absent; ยังไม่ยืนยัน clean machine |
| P2-2 | load/recovery/log lifecycle | ทำเองแบบควบคุมได้ | multiuser queues, worker recycle/crash, disk full/log retention; invariant test ไม่เป็น load SLA |

สถานะครบ 66 รายการและคำถามเจาะจงสำหรับเจ้าของ: [REMAINING_ISSUES_R42_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/REMAINING_ISSUES_R42_TH.md) รายการนี้ยังมีงานที่ไม่ได้ตรวจซ้ำและงานที่ต้องใช้ข้อมูลเพิ่มเติม

## ใช้งานรุ่นที่ตรวจ

- เว็บ: [เปิดแชท r42.4](http://127.0.0.1:8090/)
- version: `2026.10.06-domain-resume-r42.4`
- ตัวเปิดที่pinPythonสำหรับเครื่องนี้: [Open-Verified-R42.cmd](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/Open-Verified-R42.cmd)
- Flow: [FLOW_R42_FINAL.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/FLOW_R42_FINAL.md)
- วิเคราะห์: [CASE_ANALYSIS_R42_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/CASE_ANALYSIS_R42_TH.md)
- Gates: [FINAL_AUTOMATED_GATES_R42.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r42_domain_resume_20261006_152553_b21f30/FINAL_AUTOMATED_GATES_R42.json)

ชุดนี้ใช้ Python, Ollama และโมเดลที่มีในเครื่อง ยังไม่ได้สร้างชุดแจก WithModels/DownloadModels ใหม่หรือทดสอบเครื่องใหม่ สถานะจองจริงและราคาปัจจุบันยังต้องหลักฐานเจ้าของ ส่วน fixture ว่าง→ไม่ว่างตรวจว่าดึงใหม่และตอบตรงข้อมูลจำลอง

ตัวเปิดที่ระบุ Python เป็นตัวเปิดสำหรับเครื่องนี้ หากมีเว็บจากโฟลเดอร์และรุ่นเดียวกันเปิดอยู่ ตัวเปิดจะใช้เว็บนั้นต่อ การตรวจว่ารุ่นตรงกันยังไม่รับรอง Python หรือสุขภาพของคำขอจริงทุกครั้ง จึงยังต้องพัฒนาการตรวจความพร้อมและกู้ระบบตาม P0-1
