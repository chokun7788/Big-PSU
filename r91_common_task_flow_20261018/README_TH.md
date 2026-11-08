# แผนปรับ Flow กลางให้รักษาความสามารถเดิมและเพิ่มข้อมูลได้จริง

จัดทำ 18 ตุลาคม 2026 (เวลาไทย) ตามคำขอให้วิเคราะห์และวางแผนก่อน ยังไม่เริ่มเทสเพิ่มหรือติดตั้ง candidate

## เริ่มอ่าน

1. [Flow กลางฉบับเสนอใหม่ — หลักฐานเปรียบเทียบ, Full Flow 3 แบบ, runtime 12 ขั้น, owner workflow, ลำดับพัฒนา](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/01_PROPOSED_COMMON_FLOW_TH.md>)
2. [วิเคราะห์และแผนแก้ครบ P01–P37 — สาเหตุ หลักฐาน พฤติกรรมที่ควรได้ ความเสี่ยง และเกณฑ์ตรวจภายหลัง](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/02_PROBLEM_TO_REPAIR_PLAN_TH.md>)
3. [Format กลางครบ 24 หมวด — fields ปัจจุบัน งานที่ควรตอบได้ และ readiness](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/03_OWNER_SCHEMA_TASK_MAP_TH.md>)
4. [การตรวจทานแผน 3 รอบ — ข้อบกพร่องที่พบและสิ่งที่ปรับ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r91_common_task_flow_20261018/04_PLAN_REVIEW_TH.md>)
 
## ข้อสรุป

ข้อมูลกลางไม่ได้แย่ลงเพราะเป็น format กลางอย่างเดียว ตัวใหม่เปลี่ยน interpreter/guards/projection พร้อมย้ายข้อมูล ทำให้ความสามารถเดิมบางส่วนไม่ถูกเรียก แผนจึงนำการตีความเดิมที่ใช้ซ้ำได้มาออก TaskPlan แล้วอ่าน facts จากข้อมูลกลางปัจจุบันผ่าน Need ledger/evidence contracts โดยไม่ fallback ราคาหรือนโยบายจากไฟล์เก่า

## หลักฐานที่ใช้อ้างอิง

- [Flow เดิม as built](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/01_FULL_FLOW_LEGACY_TH.md>)
- [Flow กลาง as built](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/02_FULL_FLOW_COMMON_TH.md>)
- [ผลเปรียบเทียบเกณฑ์เดียวกัน R89](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json>)
- [รายละเอียดปัญหา R90](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/03_PROBLEM_ANALYSIS_ALL_TH.md>)
- [ตัวอย่างคำถามและ trace R90](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/05_CASEBOOK_TH.md>)
- [Data inventory](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r90_full_flow_analysis_20261018/DATA_INVENTORY.json>)
- [Catalog ที่อ่านจริง](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r78_web_session_check_20261016/system/app/knowledge/common/catalog.json>)
- [Engine early return](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r78_web_session_check_20261016/system/app/pipeline/engine.py>) — บรรทัด 881–885
- [Common answer/projection](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r78_web_session_check_20261016/system/app/knowledge/common/answer.py>) — บรรทัด 315 เป็นต้นไป
- [Owner preview/save](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r78_web_session_check_20261016/system/app/knowledge/common/owner_server.py>) — บรรทัด 17 และ 52
- [Approve/snapshot/publish](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r78_web_session_check_20261016/system/app/knowledge/common/store.py>) — บรรทัด 132, 142 และ 167

## ขอบเขต candidate ที่เก็บไว้ก่อนคำสั่งล่าสุด

โฟลเดอร์ candidate/ และ verification/ เป็นงานเตรียมและหลักฐานก่อนผู้ใช้ขอให้เน้นแผน ไม่ใช่ระบบติดตั้งล่าสุดและไม่ใช่หลักฐานว่าแผนทั้งฉบับเสร็จแล้ว ไม่เปลี่ยนหรือทำผลเดิมให้หายไป รายงานฉบับนี้ใช้ผลเก่า R89/R90 เพื่อเปรียบเทียบและใช้โค้ดปัจจุบันเพื่อยืนยัน call paths

ข้อเท็จจริงที่ผู้ใช้ยืนยันแล้ว เช่น สถานะสดถูกต้อง ช่วงเที่ยงไม่เปิดจอง และ VR30 กินช่องชั่วโมงเต็ม ให้รักษาตามขอบเขตนั้น ไม่ขอยืนยันซ้ำหรือขยายเป็นนโยบายอื่น

