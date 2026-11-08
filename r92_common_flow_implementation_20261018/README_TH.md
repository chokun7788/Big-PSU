# R92 — พัฒนา Flow กลางและตรวจเฉพาะจุด

ติดตั้ง application/UI changes ใน R78 แล้ว 12 files ฐานข้อมูลจริงคงเดิม ไม่ใช่ full test หรือ production publication approval

- [รายงานการพัฒนา ผลตรวจ และสิ่งที่ยังเหลือ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r92_common_flow_implementation_20261018/IMPLEMENTATION_REPORT_TH.md>)
- [หลักฐานผลตรวจ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r92_common_flow_implementation_20261018/VERIFICATION_FINAL.json>)
- [Source diff](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r92_common_flow_implementation_20261018/FINAL_CHANGESET.diff>)
- [หลักฐานรักษาไฟล์เดิม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r92_common_flow_implementation_20261018/PRESERVATION_FINAL.json>)

เว็บลองใช้: [เปิดแชท](http://127.0.0.1:8115/)

ตัวอย่าง: `The Legend of Zelda: Breath of the Wild คือกมอะๆร` / `Could you please give me a beginner-friendly introduction to Beat Saber?` / `Beat Saber game overview and price` / `PC มีอะไรบ้าง` แล้วตอบ `อุปกรณ์`

candidate/ คือ source ที่แก้; before/ และ before_revision_2/3 เก็บต้นฉบับ/ฉบับระหว่างทาง ผลทุก iteration อยู่ verification/ แยก directory ผลเก่าไม่ถูกเขียนทับ อย่าเอาฐาน ISOLATED_NOT_PRODUCTION.sqlite จาก verification ไปแทนฐานจริง
