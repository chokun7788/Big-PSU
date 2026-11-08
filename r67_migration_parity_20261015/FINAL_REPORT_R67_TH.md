# R67 — ผลตรวจและย้ายข้อมูลเดิมเข้า Format กลาง

จัดทำวันที่ 16 ตุลาคม 2026 (ประเทศไทย) เริ่มงานในโฟลเดอร์ชื่อ 20261015

## สถานะใช้งาน

โค้ดและฐานร่างอยู่ใน workspace นี้ ข้อมูล 596 รายการ ยังไม่มี active release หรือ approval ใหม่ **ยังไม่ได้นำเข้าโปรเจกต์จริง** ระบบไม่ให้สิทธิ์เขียนโฟลเดอร์ Downloads และไม่ให้สิทธิ์เชื่อม socket ของ Ollama หลังขอผ่าน request_permissions แล้ว ไม่ใช่ความผิดของโมเดลที่พิสูจน์ได้

เปิดทดลองได้ด้วย [Open-R67-Drafts.cmd](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/Open-R67-Drafts.cmd) ซึ่งใช้ Python ที่มีอยู่ใน r58 และพอร์ต 8099 ตัว launcher ผ่านการตรวจ syntax แต่ยังไม่ได้เปิด HTTP จริงจากรอบนี้ เพราะ socket ถูกจำกัด หน้าทดลองเรียก reader ตัวเดียวกับ common chat และติดป้าย DRAFT PREVIEW ข้อมูลนี้ยังไม่ถูกใช้ในเว็บแชทเดิมที่เปิดค้าง

## สิ่งที่ตกหล่นและย้ายเพิ่ม

- ตรวจ canonical 270 รายการทุกช่องข้อความ TH/EN ไม่ใช้จำนวน record แทนความครบของข้อมูล
- เติมสังกัดบุคลากร 12 รายการ วาระ 5 รายการ หมายเหตุบริการ 8 รายการ สรุปชุดปุ่ม 38 รายการ ชื่อหัวเอกสารการแข่งขัน 4 รายการ ลำดับข้อความ 104 หัวข้อ และจัดหมวดกฎจาก source ที่จับคู่ได้โดยไม่บังคับหมวดที่ไม่ทราบ
- เปลี่ยนปุ่มเก่าจากข้อความใน limitations เป็น bindings ที่อ่านได้แยกปุ่ม/action/notes/section/order 427 แถว โดยไม่เดา gesture/context
- พบแหล่งก่อน canonical ที่ย้ายไม่ครบ: กู้คำบรรยายเกม 31 รายการ และปุ่ม eFootball/Overcooked! 2/THE FINALS อีก 21 แถว รวมผังปุ่มทั้ง 43 กลุ่ม / 448 แถว + 43 สรุป = 491 รายการต้นทาง
- Delta Force และ Pokémon Champions มีเพียงข้อมูลว่ายังไม่มีผังปุ่มที่ตรวจได้ ไม่สร้างปุ่มขึ้นเอง
- รักษาหมายเหตุความน่าเชื่อถือ/เวอร์ชันชุดปุ่มเดิม พร้อมแปลให้ไทย/อังกฤษ 31 คำบรรยายและ 21 คำอธิบายปุ่มที่กู้เพิ่มมีภาษาอังกฤษแล้ว การแปลครั้งนี้ตรวจโดย agent จากต้นฉบับ ไม่ใช่ owner approval หรือการตรวจแพตช์เกมจริง
- เพิ่ม source listing profiles 3 รายการสำหรับชื่อ edition/รายการรวมตามต้นฉบับ ไม่มีการสร้าง game_service/เครื่อง/การติดตั้งเพิ่ม จำนวนเกมที่ offered ตาม source เดิมยัง 42 เกม แม้จำนวน profile รวมเป็น 51
- เก็บหัวข้อ intent เดิมของ FAQ 73 รายการเป็นข้อมูล เพื่อเลือกหัวข้อร่วมกันโดยไม่เพิ่ม alias รายประโยค
- คืนกฎทั่วไปภาษาอังกฤษฉบับเต็มจากไฟล์เดิม พร้อมแปลไทยตรงกัน และเก็บ source variants เรื่องความรับผิดชอบค่าเสียหายที่ไทย/อังกฤษระบุเงื่อนไขไม่เท่ากัน

## ตรวจความครบและการรักษาต้นฉบับ

- ตรวจ original lineage 1,933 ช่อง: ทุก source hash และ source pointer ตรงเดิม ส่วนที่แปล/ขยายจาก source แยกบัญชี ไม่เรียกว่า byte-identical ทุกช่อง
- canonical localized nonempty leaves 3,487 จุด: 3,442 ตรงข้อความในช่องอ่านโดยตรง, 3 เป็น revision ที่มีหลักฐานและต้องอ่านคู่ source/ประวัติ, 42 เป็น refusal/language configuration ที่เก็บไว้ ไม่เผยแพร่เป็นข้อเท็จจริงของศูนย์ ไม่มี missing_readable_field ในขอบเขตนี้
- ตัวเลข direct-field coverage ไม่ใช่คะแนนความถูกต้อง 100% ก่อนแก้ปุ่มบางส่วนอ่านผ่าน adapter ได้อยู่แล้ว จึงไม่ตีความ 2,615 จุดก่อนแก้ว่าเป็นคำตอบที่หายทั้งหมด
- raw-row/FK/source/revision checks 2,840/2,840 ผ่าน เก็บ original revisions 1,140 และ original sources 1,144 ทุกชุด unchanged
- source inputs ที่ snapshot 1402 ไฟล์ ตรวจโปรเจกต์จริงอีกครั้ง: เปลี่ยน 0 ไฟล์
- จัดเตรียมโค้ดเปลี่ยน 47 ไฟล์ สำรองไฟล์เดิมไว้ใน DELIVERY_final06/before ไม่มี conflict กับฐาน R66 ในโปรเจกต์ ณ ตอนตรวจ
- candidate.sqlite ที่เตรียมส่งเทียบทุกตารางกับฐานที่ทดสอบแล้วตรงกัน ไฟล์ SQLite backup อาจมี hash ทั้งไฟล์ต่างกันเพราะ header จึงเก็บทั้ง file hash และ logical table hashes ไม่อ้างว่า byte-identical

## สิ่งที่แก้ในตัวอ่านและหน้าเจ้าของ

1. ชื่อ Counter-Strike 2 เคยทำให้เลข 2 ถูกใช้เลือกปุ่ม 2 แม้ถามปุ่มทั้งหมด แก้ให้ projection ใช้คำถามหลังแยก entity
2. ข้อมูลที่ตอบได้เพียงบางขอบเขต เช่น อาหารภายนอก แสดง source ที่มีและบอกส่วนที่ยังไม่ยืนยัน ไม่ปัดตกเป็น validation error และไม่สร้างสิทธิ์นำอาหารใหม่
3. DraftView ของหน้าเจ้าของขาด connect/sources ทำให้ FAQ และกฎบางคำถามล้ม เพิ่ม read-only evidence access และแก้ป้ายข้อมูลจริงร่างที่เคยถูกมองเป็น synthetic demo
4. FAQ heading ที่มาจากคำค้น เช่น Afternoon — Close ไม่ถูกนำมาแสดงเป็นหัวข้อยืนยันสถานะ ใช้หัวข้อกลางและแสดงคำตอบจาก source
5. เปลี่ยนรหัส coverage ภายในเป็นคำอธิบายไทย/อังกฤษ และไม่แสดง metadata ค้นหา/ลำดับในคำตอบ “ทั้งหมด” โดยอัตโนมัติ เก็บข้อมูลครบในแบบฟอร์ม/trace
6. สืบ field เดิมเมื่อผู้ใช้เปลี่ยน entity แบบสั้นและ entity ใหม่รองรับ field นั้น เช่น PC notes → PS5 ไม่ต้องเขียน handler ใหม่ให้แต่ละช่องข้อมูล

## ผลทดสอบและข้อจำกัด

- Source-focused behavior: 210/210 เมื่อปิด LLM และ 210/210 เมื่อเปิด flag ON ทั้งสองภาษารวมอยู่ในชุดนี้ **ไม่มี model call** เพราะเป็นคำถามที่ reader ตีความได้ จึงไม่ใช่หลักฐานว่า LLM inference/transport ผ่าน
- Owner draft preview function และ backward compatibility 7/7 รวม payload เก่า 588 รายการ ตรวจผ่านก่อน patch เฉพาะ history ขั้นสุดท้าย ไม่มี actual HTTP/socket test ในรอบนี้
- Follow-up 6 บทสนทนา / 12 เทิร์นหลัง patch history ดู FOLLOWUPS_final06.json แยกจากตัวทดสอบเดิมที่ oracle อ่อน/ตั้งสมมติฐานกลุ่มผู้ใช้ผิด
- ชุดเดิม common OFF: 223 คำถาม / 503 grades เปรียบ R66 final20 ที่เก็บไว้กับ R67 final05; ไม่รัน legacy หรือ full 20,554 ซ้ำ ตัวเลขดูหัวข้อถัดไป
- การเปลี่ยนสุดท้ายหลัง final05 อยู่ใน resolve_state เมื่อมี previous_state เท่านั้น ตรวจ targeted followups เพิ่ม ผล 210 และ 223 เป็นรอบก่อน patch history นี้ ไม่อ้างว่าเป็น full rerun ของ final06

## คะแนนชุดเดิมไม่ได้ดีขึ้นทั้งหมด

R66 → R67: strict 133/503 → **123/503**; ไทย 90/324 → 90/324; อังกฤษ 43/179 → 33/179 มี 1 repair และ 11 regressions ตามเกณฑ์เดิม ต้องเก็บตัวเลขนี้ไว้คู่ผล targeted tests

11 regressions เกิดจาก 4 unique questions: เวลา afternoon, นำอาหาร, เครื่องดื่ม, อาหารภายนอก โดยส่วนใหญ่เพิ่ม route:knowledge ต่างจาก route เดิม; อาหารภายนอกมี literal “พื้นที่ที่ศูนย์กำหนด” ต่างจาก “พื้นที่ที่กำหนด” อีกเกณฑ์หนึ่ง คำตอบใหม่ยังระบุข้อจำกัดเรื่องอาหารภายนอกตาม source จึงไม่ได้แก้ wording/source ให้ตรง gold เพียงเพื่อผ่านคะแนน

ยังมี content-contract failed grades 31, source-alignment 39, presentation 30 และ protocol-only 294 กลุ่มซ้อนกันได้ ห้ามนับเป็นจำนวนคำถามผิดจริงทั้งหมดหรืออ้างว่าที่เหลือถูกหมด เก็บคำถาม คำตอบจริง และเหตุผลครบใน ALL_FAILED_GRADES_final05.md

ชุดนี้ไม่มี exception หรือ validation rejection; mean 0.434 s, p50 0.209 s, p95 1.152 s, max 16.917 s เป็น serial sample บนเครื่องนี้ ไม่ใช่ concurrency/SLA และไม่รับรอง production ที่ยังไม่ได้ restart/deploy

## สิ่งที่ยังต้องทำก่อนใช้แทนฐานจริง

- สิทธิ์เขียนโปรเจกต์และเครือข่าย: request_permissions คืน grant ว่างทั้งสองรายการ จึงยังไม่ deploy และยังทดสอบ actual local LLM/HTTP ไม่ได้ ไม่ใช้ช่องทางอื่นหลบข้อจำกัด
- อ่าน residual content/source contracts ต่อเป็นรายข้อ และปรับ behavioral coverage ของคำถามใหม่/คำถามหลายเจตนา ไม่ใช้ 210 source-focused cases แทนการพิสูจน์ทุก paraphrase
- Publication ยัง blocked 596 รายการ แยก metadata ที่เติมจาก source ได้ออกจาก facts ที่ยังไม่ทราบ ไม่เปิด draft override ใน production
- วันมีผลของราคา PC และตารางหลัง 31 มีนาคม, ระยะเวลาราคาเหมา, เวลาเปิดพื้นที่ และความต่างนโยบายเดิมยังต้องใช้หลักฐาน/คำยืนยันเฉพาะ อ่าน OWNER_CONFIRMATION_REQUIRED_R67_TH.md
- ไม่อ้างว่า preset/version/gameplay/current installation ยืนยันแล้วเพราะผังปุ่มย้ายครบ ไม่ใช้ source listing แทนสถานะจองสด ผู้ใช้ยืนยันสถานะจองจริงเดิมแล้ว ไม่ถาม lunch/VR occupancy ซ้ำ

## ไฟล์หลัก

- [คู่มือ Format ทุกหมวด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/FORMAT_SPEC_R67_TH.md)
- [Flow และทบทวนแผน](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/FLOW_R67_TH.md)
- [ผลเทียบ R66/R67](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/PAIRED_R66_R67.json)
- [รายการเกณฑ์ที่ยังไม่ผ่านทั้งหมด](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/ALL_FAILED_GRADES_final05.md)
- [แผนนำเข้าและหลักฐานรักษาไฟล์เดิม](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/DELIVERY_final06/PLAN.json)
- [ฐานร่างที่เตรียมส่ง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r67_migration_parity_20261015/DELIVERY_final06/candidate.sqlite)
