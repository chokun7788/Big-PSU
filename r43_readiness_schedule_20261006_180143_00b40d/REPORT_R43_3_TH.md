# ผลงาน r43.3 — 6 ตุลาคม 2026 (Asia/Bangkok)

## แก้แล้ว

- ตัวเปิดเลือก Python หนึ่งตัวและส่ง path เดิมผ่านทุกขั้นตอน ทดสอบกับ Windows PowerShell 5.1 จริง แก้ native quoting ที่ทำให้ตรวจ Python ล้มเหลว
- ก่อนเปิดเว็บ/reuse ตรวจ package+Python+warmup+LLM preflight+worker แล้ว POST คำถามจริงพร้อม content oracle; HTTP200/health ok อย่างเดียวไม่ผ่าน
- health เพิ่ม Python version/bitness/PID/fingerprint และ available physical/commit memory; launcher เก็บ readiness diagnostic แยก run ID
- คำถามอังกฤษเวลาเปิดแบบกว้างตอบครบ 7 วัน ช่วงเปิด/maintenance พักเที่ยง และข้อยกเว้นจาก calendar เดิม
- แก้ `Please list opening hours for every day.` ที่ price planner แย่งคำว่า every จนถาม scope ทั้งที่ระบุเรื่องแล้ว พร้อมกัน regression สำหรับ `all services 2 hours`
- คู่มือ local ตรงการรันเบื้องหลังและการตรวจพร้อม ไม่ต้องคงหน้าต่างคำสั่งของตัวเปิดปกติ; เครื่องยังต้องเปิดอยู่

## ผลตรวจอัตโนมัติ

- Source/fixture 159/159 test methods ใน 10 ไฟล์ รอบสุดท้ายหลังแก้ source
- HTTP 72/72 scenarios / 131 requests บน r43.3 จริง โดยตรวจเนื้อหา/operation/scope ของเคสที่เกี่ยวข้อง ไม่รัน full20k
- เปิด launcher ซ้ำจริงผ่าน: server PID เดิม, worker PID เดิม, ไม่มี stdout log ของ launcher ใหม่ และ POST readiness ใหม่ผ่าน
- app/web parity 140/140, launcher/document parity 5/5, knowledge parity 22/22, owner/data/rates hash เดิม 5/5
- 7 ไฟล์เดิมเปลี่ยนเฉพาะ scope งาน + 3 ไฟล์ใหม่; backup 312 hashes, ไม่มีไฟล์ก่อนรอบหาย; Git status/diff-check ที่อ่านผ่านระบบ permission exit0

| ชุด HTTP | ผ่าน | Requests | หลักฐาน |
|---|---|---|---|
| final_r43_3_domain_resume | 16/16 | 44 | [final_r43_3_domain_resume_20261006_182141_217257_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/final_r43_3_domain_resume_20261006_182141_217257_summary.json) |
| final_r43_3_policy | 14/14 | 14 | [final_r43_3_policy_20261006_182232_0ce366_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/final_r43_3_policy_20261006_182232_0ce366_summary.json) |
| final_r43_3_schedule | 17/17 | 19 | [final_r43_3_schedule_20261006_182133_5a2a7d_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/final_r43_3_schedule_20261006_182133_5a2a7d_summary.json) |
| final_r43_3_task_memory | 25/25 | 54 | [final_r43_3_task_memory_20261006_182212_8cd3fc_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/final_r43_3_task_memory_20261006_182212_8cd3fc_summary.json) |

Latency คำขอในชุดนี้: median 0.287s / P95 1.230s / max 12.052s ไม่ใช่ SLA หลายผู้ใช้

## ข้อผิดพลาดที่พบและเก็บไว้

Baseline ตารางอังกฤษไม่ครบ; fixture เจอ PowerShell 5.1 quoting และ sandbox temp permissions; r43.2 HTTP ตาราง 14/15 เพราะ every day ถูก price plan; ทุก raw/summary/failed log และ release r43.1/r43.2 ยังอยู่ ไม่มีการทับเพื่อให้ผลดูผ่าน ดู CASE_ANALYSIS_R43_TH.md

## ยังไม่ได้ยืนยัน

เครื่องใช้หน่วยความจำสูงช่วงตรวจ 94–96% ยังไม่ได้พิสูจน์ root cause เดียวของ MemoryError หรือกู้ได้ทุกภาวะโหลด worker warmup บาง exception ยังถูก catch แล้วตั้ง ready; actual probe static หนึ่งข้อไม่รับรองทุก LLM/RAG path คงไว้เป็น P0 ต่อ

สถานะจองจริง/current prices/conflicting or incomplete rules/official English names ยังต้องหลักฐานเจ้าของ; fixture และ API connected ไม่เป็นความจริงการจองในปัจจุบัน ชุดแจก WithModels/DownloadModels และเครื่องสะอาดยังไม่ยืนยัน local manifest นี้ใช้ path Python ของเครื่องนี้

## ใช้งานรุ่นที่ตรวจ

- เว็บ [เปิด r43.3](http://127.0.0.1:8090/) — version `2026.10.06-readiness-schedule-r43.3`
- [ตัวเปิดเบื้องหลัง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/release_r43_3/PSU_Esports_Chatbot_Local/Open-PSU-Esports-Background.cmd)
- [Flow ฉบับสมบูรณ์](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/FLOW_R43_FINAL.md)
- [วิเคราะห์สาเหตุและคำตอบจริง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/CASE_ANALYSIS_R43_TH.md)
- [รายการที่เหลือทั้งหมด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/REMAINING_ISSUES_R43_TH.md)
- [Gates](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/FINAL_AUTOMATED_GATES_R43.json) และ [Source audit](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r43_readiness_schedule_20261006_180143_00b40d/SOURCE_AUDIT_R43_FINAL.json)
