# สรุป r47: แก้เคสมีข้อมูลแต่ตอบไม่ได้ และเพิ่มเกณฑ์ตรวจเนื้อหา

## ทำเสร็จ
- Where is the venue?/studio/centre และสำนวนสถานที่อังกฤษตอบจากที่อยู่ที่มีอยู่แล้ว
- ศูนย์อยู่ที่ไหน/ขอที่อยู่ศูนย์/ที่ตั้ง PSU Esports Studio ตอบข้อมูลเดิมได้
- คำถาม Xbox studio in Bangkok ไม่ได้ถูกแทนด้วยที่อยู่ PSU; ถามยืนยันชื่อสถานที่
- อุปกรณ์ เกม สมาชิก และสถานที่แข่งขันมีขอบเขตของตัวเอง; คำถามเดินทางให้ที่อยู่และแจ้งว่าข้อมูลเส้นทางไม่มี
- เพิ่มเกณฑ์เนื้อหาให้เคสเก่าที่เคยตรวจเพียงไม่ตอบราคาเหมา

## ผล
- ก่อนแก้ HTTP ชุดแรก **16/23**
- ชุดเฉพาะสุดท้าย **25/25** ผ่าน source และ HTTP
- รวมไทย/อังกฤษที่เกี่ยวข้อง **206/206** ผ่าน HTTP **268 requests** ด้วย Local LLM เปิดใช้งาน
- Unit tests สุดท้าย **50/50** ผ่าน 4 ไฟล์
- Source/release **164/164** hashes ตรง; Git diff --check exit 0
- คำถามที่อยู่ HTTP median 0.6489s; max 3.4082s ไม่รวมการ render หน้าเว็บ

## เปลี่ยนไฟล์ใด
แก้ app/pipeline/bilingual_english.py, app/pipeline/question_frame.py, app/pipeline/closed_query_improvements.py และเพิ่ม tests/test_studio_location_r47.py
ข้อมูล data/rules และ data/curated ทุกไฟล์ใน snapshot ไม่เปลี่ยน; address/translation ใช้ record เดิม ไม่มีการเพิ่มนโยบายหรือสถานที่โดยเดา
เก็บ before snapshot, ทุก run/raw/trace, diff และ Git status แยกไฟล์; ไม่ reset/stash/commit หรือทับ log เดิม

## ยังเหลือ
- คำถามยกเลิกยังต้องปรับข้อความตอบรับและการปิดบริบท (งานถัดไปข้อ 2); เคสนี้ยังผ่านเฉพาะเกณฑ์ไม่ส่งราคาเดิมซ้ำ
- ไม่ได้ยืนยันสถานะจองสดจากข้อมูลจริง ไม่ได้รัน full 20k และไม่ได้ปรับแพ็กแจกทั้งสองแบบ
- ชั่วโมง/วิธีจอง/วันที่มีผล/ค่าเจ้าหน้าที่เช่าเหมายังรอหลักฐานเจ้าของ
- นำคำแปลที่อยู่เดิมมาใช้ ไม่อ้างว่าได้รับ human approval ใหม่; ผลผ่านเป็นชุดคำถามจำกัด ไม่ใช่ทุกสำนวน

## ใช้งาน
http://127.0.0.1:8091/ — รุ่น **2026.10.07-answer-content-r47.1**
release local: C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r47_answer_content_20261007_91dd6684\release_r47_1\PSU_Esports_Chatbot_Local
ชุดนี้อ้าง runtime Python/Ollama เดิมบนเครื่อง ไม่ใช่แพ็ก portable ที่แจกคนอื่นได้ทันที

## หลักฐาน
FLOW_R47_CONTENT.md, CASE_ANALYSIS_R47_TH.md, FINAL_AUTOMATED_GATES_R47.json, FINAL_HEALTH_R47.json, SOURCE_AND_RELEASE_AUDIT_R47.json, SOURCE_CHANGE_R47.diff และ raw/summary R47_* ทุก run
