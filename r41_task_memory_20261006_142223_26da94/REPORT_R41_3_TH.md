# รายงาน r41.3 — request memory และคำตอบหลายเรื่อง

## สรุป

แก้ source จริง 4 ไฟล์ เพิ่ม module 2 ไฟล์ และ test 1 ไฟล์ เก็บก่อนแก้/raw/candidate เก่าแยกไว้ ไม่ commit หรือ reset งานเดิม รุ่นเว็บที่ตรวจ: http://127.0.0.1:8093/ — `2026.10.06-task-memory-r41.3`

## สิ่งที่แก้แล้ว

1. กลับไปเรื่องราคา/ปุ่ม/กฎ/รายชื่อเกม หลังเปลี่ยนหัวข้อ โดยรักษาเกม/โซน/กลุ่มบุคคลภายนอก
2. ทั้งหมด/all of them หลังเลือกเกม แสดง controls ของเกมที่เลือก; หลาย operation ถาม scope
3. อันแรก/อันที่สอง/first/second ใช้ลำดับ family choices ที่แสดงจริง; catalog หลายระดับไม่เดาแกน
4. Minecraft controls ภาษาไทยไม่ถูกเติม VALORANT จากคำถามเก่า และ all รอบถัดไปไม่หวนกลับผิดเกม
5. หลาย targets ไม่จำเหลือเกมสุดท้าย; missing child ไม่ถูกตัดเมื่อ all/resume
6. แยก answered/partial/clarification/missing/unavailable/rejected ใน API/log/decision artifact; timeout เก็บ executed/pending แต่ไม่กล่าวว่า output ครบ

## ผลอัตโนมัติ

| ชุด | ผ่าน/ทั้งหมด | Requests | หลักฐาน |
|---|---:|---:|---|
| บทสนทนาหลักใหม่ | 25/25 | 54 | [final_r41_3_targeted_20261006_145120_402dfc_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/final_r41_3_targeted_20261006_145120_402dfc_summary.json) |
| คำถามเพิ่มเติมและขอบบริบท | 18/18 | 54 | [final_r41_3_variations_20261006_145205_141cca_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/final_r41_3_variations_20261006_145205_141cca_summary.json) |
| เคส r40 หลัก | 31/31 | 43 | [final_r41_3_regression_targeted_20261006_145217_7fd72a_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/final_r41_3_regression_targeted_20261006_145217_7fd72a_summary.json) |
| สำนวน r40 | 12/12 | 19 | [final_r41_3_regression_transfer_20261006_145224_41ab64_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/final_r41_3_regression_transfer_20261006_145224_41ab64_summary.json) |
| ขอบเขตและข้อจำกัด | 8/8 | 15 | [final_r41_3_regression_boundary_20261006_145228_f8d7f2_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/final_r41_3_regression_boundary_20261006_145228_f8d7f2_summary.json) |
| คำถามผสมราคา/ปุ่ม | 4/4 | 4 | [final_r41_3_regression_mixed_20261006_145231_9bc4fd_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/final_r41_3_regression_mixed_20261006_145231_9bc4fd_summary.json) |
| สองรอบ ราคา/กฎ/หัวข้อ | 36/36 | 72 | [adjacent_http_20261006_145233_0585a7_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/adjacent_http_20261006_145233_0585a7_summary.json) |

รวม **134/134 conversations**, **261 HTTP requests**. Unit ที่เกี่ยวข้อง **95/95 test methods**. ไม่รัน full corpus สองหมื่นกว่าเคส

ผล baseline HTTP ด้วยเกณฑ์เดียวกัน: **10/25**; มี failure เพราะคำตอบ/บริบท **11** และเพราะ metadata coverage ใหม่ยังไม่มี **4**. จึงไม่เรียกทุก failure ว่าตอบผิด

รอบ variation แรก 11/16 ตามเกณฑ์ที่บันทึกไว้: 2 เคส catalog ตอบสองโซนจริงแต่ grader ไม่รับ multi mode, 2 เคส family ordinal ยังไม่เข้าใจและเฉลยเดิมระบุ second title ผิดลำดับ, 1 เคส Thai unknown target inherit old game. เก็บ raw เดิมและแก้ oracle แยก ไม่แก้คะแนนย้อนหลังในไฟล์เดิม

ตอนขยาย guard พบ regression ของ bare unknown selections จึงจำกัด guard เฉพาะ controls question ที่สมบูรณ์และรัน regression ใหม่ ไม่ยกระดับ guard ให้ครอบทุกคำถามโดยไม่มีหลักฐาน

## ความเร็วและรันไทม์

ชุดนี้ p50 0.104s / p95 0.736s / max 14.588s. เป็นเวลาที่เครื่องนี้กับคำถามชุดนี้หลัง warmup ไม่ใช่ SLA ทุกคำถาม

Health ยืนยัน local LLM + semantic RAG เปิด และ preflight/warmup ผ่าน ไม่ได้แปลว่าทุกเคสเรียกโมเดลหรือพิสูจน์ทุกคำตอบถูกตามนโยบายจริง

## การรักษาข้อมูล

ตรวจ hash ไฟล์หลัก 5 ไฟล์ไม่เปลี่ยน: calendar เจ้าของ, service policy, competition chunks, review queue, calculator rates. Source app/web ตรง candidate **140 ไฟล์**. มี [source diff](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/SOURCE_CHANGE_R41.diff) เทียบ backup รอบนี้ ไม่ใช้ git diff ทั้งหมดแทนงานรอบนี้

รุ่น r40.3/r41.1/r41.2/log เดิมยังอยู่ ปิดเฉพาะ baseline/r41.1 ที่ผมเปิดในรอบนี้เพื่อเปลี่ยนไป candidate ใหม่; รุ่นอื่นที่คุณเปิดไว้ไม่ได้ปิด. พบรุ่นแจกเดิมที่พอร์ต 8092 จึงรุ่นใหม่เลือก 8093

## ข้อจำกัดที่ยังเหลือ

- Memory เก็บ requested tasks ≤8 operations/session, TTL 30 นาทีโดยค่าเริ่มต้น, ไม่อยู่หลัง server restart. ครอบคลุม explicit return grammar ที่ตรวจ; ไม่รับรองทุก paraphrase/ทุกหมวด
- Bare all ของ catalog ยังถามว่าหมายถึงโซนหรือเกมเมื่อไม่ชัด; ถ้าบอก all zones จึงแสดงทุกโซน
- Generic task status เป็น execution coverage; completeness ของเนื้อหาต้องใช้ domain oracle เพิ่ม โดยกฎละเอียดมี clause coverage แยก
- Fixture/mock tests พิสูจน์ state/timeout contract; ยังไม่พิสูจน์ real booking occupancy และ owner policy
- Current prices, pause conflicts, truncated rules และ source gaps ต้องรอหลักฐานมนุษย์ ไม่ใช้คะแนน tests ตัดสิน
- ชุดทดลองใหม่นี้ใช้ Python/Ollama/models ที่มีในเครื่อง ไม่ได้อัปเดตชุดแจก WithModels/DownloadModels และไม่ยืนยันเครื่องสะอาด

## ไฟล์ใช้งาน/ตรวจต่อ

- [Flow ฉบับสมบูรณ์](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/FLOW_R41_FINAL.md)
- [หลักฐานผ่านอัตโนมัติ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/FINAL_AUTOMATED_GATES_R41.json)
- [หลักฐานต่อบทสนทนา](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/CASE_ANALYSIS_R41_TH.md)
- [ตัวเปิด candidate ที่ตรวจบนเครื่องนี้](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r41_task_memory_20261006_142223_26da94/release_r41_3/PSU_Esports_Chatbot_Local/Open-PSU-Esports-Background.cmd)
