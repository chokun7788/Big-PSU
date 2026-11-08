# รายงานผลพัฒนาและทดสอบ r50

2026-10-09 เวลาไทย · version 2026.10.09-flow-r50.2 · เว็บ candidate http://127.0.0.1:8091/

## สรุปงานที่ทำ

- วาง Flow, ตรวจ 10 มิติ, แก้ routing/facet/typo/followup และเพิ่มความจำ SQLite ข้าม restart
- ตรวจ source trace เริ่ม 15/22 ผ่าน หลังแก้ 22/22; HTTP ชุดใหม่ 22/22 (11TH/11EN), regression r49 110/110 และ r48 136/136 รวม 268/268 scenario ไม่ใช่ 268 request เพราะบาง scenario หลาย turn
- Unit ล่าสุด persistence12, dialogue10, taxonomy2, sourcefacet10, domainresume18: 52/52 tests; r42 เคยผิด1เรื่อง member groups แล้วแก้
- รีสตาร์ต server จริง 10 session ตามลำดับ + fresh-session isolation1: 11/11; HTTP followups พร้อมกัน4: 4/4 หลังแก้ oracle ให้ตรง public contract
- Data/นโยบายเจ้าของไม่เปลี่ยน; source audit: 9 existing files เปลี่ยน +2ใหม่, อีก 381 ไฟล์ใน snapshot ไม่เปลี่ยน; source/release 217/217 ตรงกัน
- โฟลเดอร์ส่งต่อสองแบบมี full app/web/data ตรง release: {'01_Download_Models': 640, '02_With_Models': 640}; bundledPythonผ่าน; withmodelsน้ำหนัก2ไฟล์ SHA256ผ่าน ไม่มี state/logsส่วนตัว

## แยกประเภทหลักฐาน

| เรื่อง | ผู้ใช้ยืนยัน | อัตโนมัติรอบนี้ | ยังไม่รับรอง |
|---|---|---|---|
| สถานะจองจริง | ผู้ใช้เช็คแล้วถูกต้อง | ไม่ยิง burst WordPress | throughput/status ทุกสภาวะเครือข่ายภายใต้โหลด |
| อังกฤษ | ผู้ใช้แจ้งผ่าน | focused/regression TH/EN ในส่วนแก้ | ไม่แก้ approval metadata ของทุกเอกสารย้อนหลัง |
| Dialogue correctness | ยังไม่มี human approve ทุก input | required content + mode/target/session/locale/timeout | ทุกสำนวนที่ไม่เคยทดสอบ |
| Restart | — | unit12, actual HTTP11, separate parallel4 | ทุก domain/cross browser/cross folder |
| Package | — | source/data equality, Python, model hash | fresh recipient machine cold startup ทั้ง2แบบ |

## ทำไมเคยตอบผิด

1. สมาชิกทีม CS2/VALORANT: route เดิมเริ่ม competition ถูก แต่ service_fact_scope_guard ที่ทำงานถัดมาจับคำสมาชิกและคืน clarification ก่อนอ่าน rule clause; จึงมีข้อมูลก็ไม่ได้ใช้ แก้ guard delegation เมื่อ game+team count ชัด
2. Team size VS timeout: สำนวนไทยเวลานอกไม่อยู่ taxonomy matching ขณะที่อังกฤษได้; เพิ่ม facet cue ของ tactical timeout ไม่ใช้ team keyword เป็น team_size เสมอ
3. Source gap VALORANT: ความไม่ครบของ source ที่นำเข้า ยังไม่มีจำนวนตัวจริง/สำรอง; แก้ให้ระบุ missing ชัด ไม่เอาตัวเลขผู้เข้า Match Prep มาเป็น roster
4. Member groups: guard เพิ่มแล้วพบ regression `How many member groups are there?` ถูกตอบไม่ต้องสมัครสมาชิก; เพิ่ม delegation ให้ directory count ไม่ใช่ membership admission
5. สำนวนผิดสองจุด/คำสุภาพ: ตัวจับ lexical noun/followup ไม่ครอบคลุมคำที่มี anchor ชัด; ขยาย canonical recovery และ suffix handling แบบ bounded ไม่เปลี่ยนเลขหรือวันเวลา
6. Return marker: ก่อนนี้ task memory ไม่รู้ว่าขอกลับ service topic เก่าชัดเจน; เพิ่ม lookup เฉพาะ acknowledged server turn ไม่ย้อนเรื่องเอง
7. Location: parking answer ถูกใช้กับ Bangkok; เพิ่ม guard เฉพาะการระบุสถานที่อื่นที่รู้จัก ผลผ่านมิได้หมายถึงแก้ place entity ทุกเมืองแล้ว
8. Restart: state อยู่ memory จึงหายเมื่อ parent processเปลี่ยน; SQLite snapshotแก้ persistence แต่ยังต้อง session/TTL/pathเดียว

ตัวอย่างคำถาม/คำตอบก่อนและหลังทั้งหมด: [FAILURE_DETAILS_R50.md](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\FAILURE_DETAILS_R50.md>)

## วิธีวัดโหลด

ส่ง POST /api/chat บนเครื่องนี้ผ่าน loopback; barrierเริ่มพร้อมกัน; session/turnแยก; debugfalse; ไม่ retry; เก็บ first attempt เท่านั้น Fast3 waves/ระดับ Mixed2 waves/ระดับ เริ่ม1คนแล้วเพิ่ม RuntimeเปิดlocalLLM+semanticRAGจริง แต่หลายคำถามตอบstructuredตรงได้

- Fast = service facts 6รูปแบบ ไทย/อังกฤษ
- Mixed = CS2ยิง, VALORANTเมาส์แข่ง, PC gamesEN, personalkeyboardEN ไม่ใช่ worst-case LLMทั้งหมด
- worker1, activecap16, queuewait3s, answerdeadline20s, recycle250completed requests ตาม launcherจริง
- p50คือมัธยฐานเวลาแต่ละ request; p95 nearest-rank; จำนวนตัวอย่างน้อย บางระดับ p95จึงเท่าค่าสูงสุด ตารางlatencyเฉพาะคำตอบที่ถูกต้อง ไม่รวม503ที่ตอบเร็วกว่าจนทำให้เวลาดูดี
- RAMก่อนรอบfinal83% เหลือประมาณ2.69GB; หลังประมาณ85% เหลือ2.40GB; ขนาด/โหลดงานอื่นบนเครื่องมีผล

### Baseline r49.2

| ประเภท | คนส่งพร้อมกัน | ถูกต้อง/คำขอ | p50 (s) | p95 (s) | สูงสุด (s) | HTTP 503 | PID เปลี่ยน | ผ่านเกณฑ์ |
|---|---:|---:|---:|---:|---:|---:|---|---|
| fast | 1 | 3/3 | 0.31 | 0.33 | 0.33 | 0 | ไม่ | ผ่าน |
| fast | 2 | 6/6 | 0.46 | 0.80 | 0.80 | 0 | ไม่ | ผ่าน |
| fast | 4 | 12/12 | 0.77 | 1.12 | 1.12 | 0 | ไม่ | ผ่าน |
| fast | 8 | 24/24 | 1.21 | 1.77 | 1.85 | 0 | ไม่ | ผ่าน |
| fast | 12 | 36/36 | 1.90 | 3.04 | 3.26 | 0 | ไม่ | ผ่าน |
| fast | 16 | 47/48 | 2.41 | 3.74 | 3.97 | 1 | ไม่ | ไม่ผ่าน |
| fast | 24 | 53/72 | 2.53 | 3.91 | 4.10 | 19 | ไม่ | ไม่ผ่าน |
| mixed | 1 | 2/2 | 0.77 | 0.88 | 0.88 | 0 | ไม่ | ผ่าน |
| mixed | 2 | 4/4 | 1.01 | 1.38 | 1.38 | 0 | ไม่ | ผ่าน |
| mixed | 4 | 8/8 | 1.05 | 2.26 | 2.26 | 0 | ไม่ | ผ่าน |
| mixed | 6 | 12/12 | 1.95 | 3.23 | 3.23 | 0 | ไม่ | ผ่าน |
| mixed | 8 | 13/16 | 2.49 | 18.47 | 18.47 | 3 | ใช่ | ไม่ผ่าน |
| mixed | 12 | 14/24 | 2.88 | 4.48 | 4.48 | 10 | ไม่ | ไม่ผ่าน |

หลักฐาน: [R50_LOAD_BASELINE_20261009_163513_cbea3c_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\R50_LOAD_BASELINE_20261009_163513_cbea3c_summary.json>)

### Final r50.2 — ทั้ง fast และ mixed ต่อเนื่อง

| ประเภท | คนส่งพร้อมกัน | ถูกต้อง/คำขอ | p50 (s) | p95 (s) | สูงสุด (s) | HTTP 503 | PID เปลี่ยน | ผ่านเกณฑ์ |
|---|---:|---:|---:|---:|---:|---:|---|---|
| fast | 1 | 3/3 | 0.43 | 0.44 | 0.44 | 0 | ไม่ | ผ่าน |
| fast | 2 | 6/6 | 0.58 | 0.84 | 0.84 | 0 | ไม่ | ผ่าน |
| fast | 4 | 12/12 | 0.76 | 1.20 | 1.20 | 0 | ไม่ | ผ่าน |
| fast | 8 | 24/24 | 1.39 | 2.17 | 2.23 | 0 | ไม่ | ผ่าน |
| fast | 12 | 36/36 | 1.97 | 2.98 | 3.07 | 0 | ไม่ | ผ่าน |
| fast | 16 | 48/48 | 2.50 | 3.77 | 3.88 | 0 | ไม่ | ผ่าน |
| fast | 24 | 48/72 | 2.52 | 3.70 | 3.83 | 24 | ไม่ | ไม่ผ่าน |
| fast | 32 | 48/96 | 2.76 | 3.91 | 4.27 | 48 | ไม่ | ไม่ผ่าน |
| mixed | 1 | 2/2 | 4.17 | 5.46 | 5.46 | 0 | ไม่ | ผ่าน |
| mixed | 2 | 4/4 | 1.09 | 1.51 | 1.51 | 0 | ไม่ | ผ่าน |
| mixed | 4 | 8/8 | 1.53 | 2.24 | 2.24 | 0 | ไม่ | ผ่าน |
| mixed | 6 | 12/12 | 2.23 | 3.70 | 3.70 | 0 | ไม่ | ผ่าน |
| mixed | 8 | 11/16 | 2.90 | 4.37 | 4.37 | 5 | ใช่ | ไม่ผ่าน |
| mixed | 12 | 7/24 | 4.08 | 16.51 | 16.51 | 17 | ไม่ | ไม่ผ่าน |

หลักฐาน: [R50_LOAD_FINAL_20261009_171512_1eb447_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\R50_LOAD_FINAL_20261009_171512_1eb447_summary.json>)

mixed8มี PIDเปลี่ยน25756→35632; performance eventระบุ planned worker_recycle warming/promoted และ launcher threshold250 จึงไม่สรุปว่าเป็น crashหรือข้อจำกัดจำนวนคนอย่างเดียว mixed12ต่อจากworkerใหม่ยังมี503และtail16.51s แต่ต้องรายงานสภาพหลัง recycleด้วย

### ยืนยัน Mixed แยกจากรอบเปลี่ยน worker

| ประเภท | คนส่งพร้อมกัน | ถูกต้อง/คำขอ | p50 (s) | p95 (s) | สูงสุด (s) | HTTP 503 | PID เปลี่ยน | ผ่านเกณฑ์ |
|---|---:|---:|---:|---:|---:|---:|---|---|
| mixed | 1 | 2/2 | 0.79 | 0.81 | 0.81 | 0 | ไม่ | ผ่าน |
| mixed | 2 | 4/4 | 0.95 | 1.40 | 1.40 | 0 | ไม่ | ผ่าน |
| mixed | 4 | 8/8 | 1.14 | 1.96 | 1.96 | 0 | ไม่ | ผ่าน |
| mixed | 6 | 12/12 | 1.99 | 3.24 | 3.24 | 0 | ไม่ | ผ่าน |
| mixed | 8 | 15/16 | 2.00 | 3.83 | 3.83 | 1 | ไม่ | ไม่ผ่าน |
| mixed | 12 | 19/24 | 2.48 | 5.10 | 5.10 | 5 | ไม่ | ไม่ผ่าน |

หลักฐาน: [R50_LOAD_MIXED_CONFIRM_20261009_172446_883e79_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\R50_LOAD_MIXED_CONFIRM_20261009_172446_883e79_summary.json>)

ทุกระดับนี้ PIDคงเดิม ไม่มี timeout/content mismatch; 503เป็น worker_queue_busy ไม่มีการretry ที่8คนได้15/16 ที่12ได้19/24 จึงยืนยันว่าคิวจำกัดก่อ rejectionได้แม้ไม่มี recycle จำนวน8ไม่ใช่ผ่านครบ

### สรุปจำนวนและเวลา

- Fast: สูงสุดที่ทดสอบผ่านทั้งหมด16คน (48/48), p50ประมาณ2.50s/p95 3.77s; baseline16เคย47/48จึงควรเผื่อที่12คน
- Mixed: สูงสุดที่ผ่านครบทั้งรอบหลักและรอบแยก6คน, p50ประมาณ2s และp95ประมาณ3.2–3.7s; 1–4คนรอบยืนยัน p95ประมาณ0.8–2.0s
- ยังไม่ได้ทดสอบ7คนหรือ17–23คน จึงเป็น highest tested passing level ไม่ใช่ exact maximum
- “คนพร้อมกัน” หมายถึงส่งคำถามในจังหวะเดียวกัน จำนวนคนเปิดแท็บค้างอาจมากกว่าได้ ผลนี้ไม่ใช่จำนวนผู้ใช้บริการตลอดวัน
- ถ้าต้องให้เลขเริ่มต้นสำหรับ workloadผสมนี้ ใช้4–6คำขอพร้อมกันและติดตาม503/queue; เพิ่มโหลดต้องวัด sustained/LLM-heavy/livebookingแยก
- ภาระเกินคิวเกิด503แบบให้ลองใหม่ ข้อมูลที่ตอบสำเร็จไม่พบเนื้อหาผิดตามoracle แต่ไม่ได้แปลว่าคำขอที่ถูกปฏิเสธให้บริการสำเร็จ

### ยอดคำขอและข้อผิดพลาดดิบ

- R50_LOAD_BASELINE: 234/267 ถูกต้องทุกระดับรวม overload; errors [{"profile": "fast", "http": "503", "timing": "worker_queue_busy", "error": "server_busy", "count": 2}, {"profile": "fast", "http": "503", "timing": "", "error": "server_busy", "count": 18}, {"profile": "mixed", "http": "503", "timing": "worker_queue_busy", "error": "server_busy", "count": 13}]
- R50_LOAD_FINAL: 269/363 ถูกต้องทุกระดับรวม overload; errors [{"profile": "fast", "http": "503", "timing": "", "error": "server_busy", "count": 72}, {"profile": "mixed", "http": "503", "timing": "worker_queue_busy", "error": "server_busy", "count": 22}]
- R50_LOAD_MIXED_CONFIRM: 60/66 ถูกต้องทุกระดับรวม overload; errors [{"profile": "mixed", "http": "503", "timing": "worker_queue_busy", "error": "server_busy", "count": 6}]

รวมรายละเอียดรายระดับ/ข้อผิดพลาด: [LOAD_ANALYSIS_R50.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\LOAD_ANALYSIS_R50.json>) ไม่มีการเอาเฉพาะคำขอสำเร็จมาคิด accuracyรวม

## การทดสอบที่พลาดและเหตุผลที่ไม่ลบทิ้ง

- Source V1ผิด7/22; r42ผิด1/18 เก็บbefore/after traceและผลเก่า
- Persistence testแรกใช้ sandbox Temp ที่SQLiteเข้าถึง/cleanupไม่ได้ เปลี่ยนfixtureไปartifactdirและเก็บfixture ไม่ลบไฟล์เดิม; unitล่าสุด12ผ่าน
- Restartครั้งแรกยิง10followupsพร้อมกัน harnessหยุดที่503 ไม่ได้เก็บHTTPครบ; retrospectiveอ่าน committed/pendingของ10sessionจากDBเก็บแยก ไม่อ้างว่าผ่าน10พร้อมกัน
- Restartครั้งถัดไปใช้seedใหม่/realPIDchangeและrecoveryตามลำดับ11/11เพื่อแยกfunctionalจากload
- Parallel context oracleแรก0/4เพราะrequiredebug-onlyfieldขณะdebugfalse; คำตอบ/networkเดิมทั้ง4ถูก ตรวจresolved_question+content+session แล้ว4/4 เก็บทั้งสองรายงาน
- Sharebuildแรกlongpath/hardlink permissionไม่สำเร็จ เก็บpartialfolderในartifactแต่ไม่ใช้ส่งต่อ; shortpathใหม่สร้างและตรวจครบ

## ส่งต่อและเปิดใช้งาน

โฟลเดอร์ใหม่: [PSU_Esports_Share_R50_20261009_66d96bb7](<C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_R50_20261009_66d96bb7>)

- [มีโมเดล เปิด Start-Chatbot.cmd](<C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_R50_20261009_66d96bb7\02_With_Models\Start-Chatbot.cmd>)
- [แบบดาวน์โหลดโมเดล เปิด Start-Chatbot.cmd](<C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_R50_20261009_66d96bb7\01_Download_Models\Start-Chatbot.cmd>)
- ต้องย้ายทั้งโฟลเดอร์ variant ไม่ย้ายเฉพาะcmd; อ่านREADMEรุ่นr50ที่ใส่ใหม่
- บนเครื่องนี้ immutablebinary/modelใช้hardlinkเพื่อประหยัดพื้นที่จริง แต่เมื่อคัดลอกไปเครื่องอื่น/ZIPเป็นfullbytesตามขนาดlogical ไม่ได้ลดไฟล์โมเดล
- ไม่ทับชุดเก่า ไม่มีZIPใหม่ในรอบนี้; package checksไม่เท่ากับcoldlaunchทั้งสองแบบบนเครื่องใหม่
- private conversation DB/logs ของการทดสอบอยู่เฉพาะartifactcandidate ไม่รวมในโฟลเดอร์ส่งต่อ

## สิ่งที่ยังต้องทำ/ถามอย่างเจาะจง

1. หากต้องการตอบ VALORANT roster: “รายการ PSU Phuket VALORANT 2026 ให้มีตัวจริงกี่คน สำรองกี่คน และโค้ชรวมอยู่ในจำนวนใด? ขอ clause/เอกสารของรายการนี้” ไม่จำเป็นต้องให้เจ้าของตอบ CS2 5คนซ้ำเพราะsourceมีแล้ว
2. Service fieldsที่ยังไม่ยืนยัน: ค่าจอดรถฟรีหรือคิดเท่าไร, อนุญาตจอยส่วนตัวหรือไม่, และรายการunknownเดิม ต้องตอบว่าไม่ทราบต่อไป
3. งานทำเองได้ต่อ: sustained load/LLM-heavy, stage latencyprofiling, recyclewarmup contention, coldrecipient test, unseen typo/return markers negativecases; จัดลำดับตามfailureจริง
4. ไม่ควรเพิ่มworkerโดยเดา: เครื่องมีRAMแรงกดดันและmodelเดียว ต้องวัดผลจริงหลังการปรับทีละค่า

Flowฉบับสุดท้าย: [FLOW_FINAL_R50.md](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\FLOW_FINAL_R50.md>) · Review10มิติ: [REVIEW_LOG_R50.md](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\REVIEW_LOG_R50.md>) · Audit: [SOURCE_RELEASE_AUDIT_R50.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r50_flow_load_20261009_66d96bb7\SOURCE_RELEASE_AUDIT_R50.json>)
