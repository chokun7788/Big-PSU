# R121 — ฝึก LoRA ให้ตีโจทย์ก่อนตอบ และแก้การเชื่อม Flow

## สถานะ

**ทำการฝึกจริงและตรวจการเชื่อม candidate เสร็จแล้ว** candidate ล่าสุดอยู่ใน `revision04_system` ใช้ adapter เดียวกับการวัดก่อน/หลังฝึก ยังไม่ติดตั้งทับ R78 หรือ server เดิม และยังไม่ถือว่าพร้อม production

## 1. สิ่งที่ทำจริง

- Typhoon2.5 Qwen3 4B แบบ QLoRA/NF4; LoRA rank 8 ที่ q/k/v/o projections รวม 5,898,240 พารามิเตอร์ที่ฝึก
- ฝึกจากคำถามเดิม 244 ข้อ, validation 15, ชุดวัดแยก 30; ไม่เพิ่มคำถามใหม่
- ครบ 3 epochs, 732 micro steps, 93 optimizer steps; ทุกตัวอย่างถูกใช้หนึ่งครั้งต่อ epoch
- ตรวจยืนยัน adapter เปลี่ยนจริง และ base parameter hash ไม่เปลี่ยน
- เลือก epoch 3 ด้วย validation loss ต่ำสุดประมาณ 0.0462; peak allocated GPU memory 4,221,578,752 bytes
- target เป็นแผนตีความคำถาม ไม่ใช่คำตอบ ราคา เวลา หรือกฎธุรกิจ ข้อเท็จจริงยังอ่านจากข้อมูลกลาง

หลักฐาน: [train02/OPTIMIZATION_PROOF.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/train02/OPTIMIZATION_PROOF.json) · [TRAINING_VERIFICATION.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/TRAINING_VERIFICATION.json) · [FINAL_VERIFICATION.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/FINAL_VERIFICATION.json)

## 2. ผลของน้ำหนักในชุดแยก 30 ข้อ

ใช้ HF NF4 base เดียวกัน, prompt/decoding เดียวกัน ก่อน/หลัง adapter ไม่มีการเปลี่ยน Flow ระหว่างสองแขน และไม่ใช่การเทียบตรงกับ Ollama GGUF ของ R120

| ตัววัด | ก่อนฝึก | หลังฝึก |
|---|---:|---:|
| focus | 14/30 | 20/30 |
| domain | 12/30 | 22/30 |
| domain + facet | 5/30 | 19/30 |
| task signature และ contract | 2/30 | 17/30 |
| source-quoted contract | 5/30 | 29/30 |
| จำนวนงาน | 26/30 | 30/30 |

**domain เพิ่มจาก 40.0% เป็น 73.3% แต่ไม่ใช่ accuracy ของคำตอบทั้งระบบ** การผ่าน contract ดีขึ้นส่วนหนึ่งเป็นการเรียนรูปแบบ/vocabulary ส่วน typed-constraint recall กลับลดจาก 6/27 เป็น 4/27 จึงยังไม่รับรองว่าผูกเงื่อนไขครบ

| locale | จำนวน | focus ก่อน → หลัง | domain ก่อน → หลัง | task signature ก่อน → หลัง |
|---|---:|---:|---:|---:|
| auto | 7 | 4 → 4 | 6 → 6 | 2 → 5 |
| en | 17 | 7 → 11 | 6 → 11 | 0 → 7 |
| th | 6 | 3 → 5 | 0 → 5 | 0 → 5 |

`auto` คือ requested locale ไม่ได้แปลว่าข้อความทั้งหมดเป็นภาษาใดภาษาเดียว ชุดวัดมีขนาดเล็กและ labels จัดทำโดย agent ไม่ใช่เจ้าของยืนยันทุก field มี 13 domains ในชุดวัด แต่ rental/news ไม่มี fresh test รอบนี้

ผลและคำตอบรายข้อครบ: [PLANNER_PER_REQUEST_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/PLANNER_PER_REQUEST_TH.md) · [PLANNER_COMPARISON.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/PLANNER_COMPARISON.json)

## 3. ผล API ก่อน/หลัง adapter

ใช้ candidate/source เดียวกัน 8 คำถามต่อแขน การตีโจทย์หลังฝึกเร็วและเป็น schema มากขึ้น แต่ยังมี reader และ intent errors จึงตรวจและแก้ Flow ต่อ

| ตัววัด | base | trained |
|---|---:|---:|
| HTTP 200 | 8 | 8 |
| model events ที่ schema ผ่าน | 2 | 8 |
| positive literal checks ผ่าน | 0 | 0 |
| strict grades ผ่าน | 0 | 1 |
| median เวลาต่อคำถาม (วินาที) | 52.0 | 22.6955 |

แต่ละแขนมี 15 grades แต่ positive literal assertions เพียง 5 grades ครอบคลุม 2 คำถาม ไม่ใช่หลักฐานว่าอีก 6 คำถามตอบถูก/ผิดตามสัดส่วนเดียวกัน strict grades มี protocol/source-ID/first-line/performance requirements ของ Legacy จึงไม่ใช้แทน semantic accuracy

ตัวอย่าง CS2: คำตอบหลังฝึกยืนยันจาก source ว่าปรับ brightness/resolution/crosshair ได้เฉพาะในเกมและหน้าจอ แต่ literal checker ต้องการทั้ง clause ที่ใช้คำว่า “computer monitor” ส่วน source แปลใช้ “computer screen”; first line ยังมีคำเตือน translation และ source IDs เป็นของ native records จึงเกิด clause/first-line/source-ID mismatch แยกจากเนื้อหาหลัก

รายละเอียด: [API_PER_REQUEST_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/API_PER_REQUEST_TH.md) · [API_COMPARISON.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/API_COMPARISON.json)

**ข้อจำกัดของ API comparison:** พบ fallback model transport errors 3 ครั้งในฝั่ง base จึงไม่ใช้ผล API สรุปว่า adapter ทำให้คำตอบดีขึ้นเพียงปัจจัยเดียว ดูรายละเอียดและ config ที่แก้ในข้อ 10

## 4. แก้ Flow จากข้อผิดพลาดที่ตรวจพบ

1. ผูก target/quote ที่ต่างเพียงตัวพิมพ์กลับต้นฉบับเฉพาะเมื่อพบตำแหน่งเดียว แล้วตรวจ contract เดิมต่อ ทำให้แผน Nintendo ไม่ถูกทิ้งไป fallback เป็นรายชื่อเกม
2. ตรวจคำถามหลายงานทีละงาน ให้คำขอปุ่มเกมมาก่อนคำขึ้นต้นทั่วไป “What are” และตัด target ที่รั่วจากงานอื่นเมื่อไม่มีคำสืบทอดยืนยัน
3. แยกสิทธิ์บุคคลภายนอกออกจากเอกสารที่ต้องแสดง โดยอ่านคนละ policy จาก source ปัจจุบัน
4. ผูกคำถามว่าเกมต้องจองอะไรเข้าความสัมพันธ์ game → studio_services ไม่ไหลไป rental packages
5. เพิ่มการรับรู้คำถามเรื่องกินอาหารโดยตรง และกั้นคำถามนำเข้า/ข้อความที่ปฏิเสธว่าถามเรื่องกิน
6. เมื่อ source มี 12 control entries แต่ถาม 8 ปุ่ม ให้ระบุความต่างและสถานะ partial ไม่เลือก subset เอง

การแก้เหล่านี้เป็น source/intent guards และ reader corrections ไม่ใช่ผลจากการฝึกน้ำหนักเพิ่ม ไม่แก้ค่าในฐานข้อมูลหรือยัดคำตอบของคำถามไว้ในโค้ด

Flow ฉบับละเอียด: [FLOW_V4_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/FLOW_V4_TH.md) · candidate: [โฟลเดอร์โค้ด revision04](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/revision04_system)

## 5. ผลตรวจหลังแก้ Flow — development/regression เท่านั้น

| รอบ | จำนวนคำถาม | positive literal checks | ขอบเขต |
|---|---:|---:|---|
| revision02 | 14 | 14/17 | 8 เคสปัญหา + 6 known training regressions |
| revision03 | 4 | 4/4 | 4 เส้นทางที่แก้ลำดับ/target scope |
| revision04 | 3 | 2/2 | 3 เคส count / consumption / bring-vs-consume |

ทั้งสามรอบ HTTP 200 ครบและ frozen source ไม่เปลี่ยน แต่ positive assertions ครอบคลุมเพียงบางคำถาม ผลหลังแก้จากปัญหาที่เห็นแล้ว **ไม่ใช่ fresh held-out accuracy** และ revision04 ยังไม่ได้รันทั้ง 14 ข้อในรุ่นเดียวกัน ห้ามรวมผลต่าง revision แล้วอ้างว่า Full ผ่าน

คำตอบ/แผน/source repair/reason code ทุกข้อ: [DEVELOPMENT_PER_REQUEST_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/DEVELOPMENT_PER_REQUEST_TH.md) · [DEVELOPMENT_COMPARISON.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/DEVELOPMENT_COMPARISON.json)

## 6. แยกเคสสำคัญตามหลักฐานล่าสุดที่ตรวจ

| เคส | ผลที่ตรวจได้ | ประเภท/สิ่งที่ยังเหลือ |
|---|---|---|
| Nintendo Zone มีอะไรให้ใช้ | revision02 ตอบอุปกรณ์/การใช้งานและผ่าน literal 4/4 | เดิมเป็น quote binding จากตัวพิมพ์ แล้ว fallback ผิดหมวด ไม่ใช่ข้อมูลไม่ครบ |
| คนนอก PSU ใช้ได้ไหม | revision02 อ่าน r114_q037_owner_policy ได้ | ข้อมูลมีอยู่เดิม แต่ขาดการจับ paraphrase ของ eligibility |
| เล่น FINAL FANTASY XVI ต้องจองอะไร | revision02 กลับมาตอบ PlayStation 5 #01-#02 จาก relation | trained-only เคยถอยไป rental; guard แก้การเลือก action |
| เอกสารของ external visitor | revision03 ตอบเอกสารเช็คอินจาก source | เดิมตอบเพียงสิทธิ์เข้าใช้; corrected purpose ไม่ใช่เพิ่มข้อมูล |
| 8 ปุ่ม Tekken + ราคา PC | revision04 แยก C05/C06 ได้ ตอบราคา และแจ้งว่ามี 12 control entries แต่ไม่รู้ subset 8 | ยังเป็น partial ของ subset ที่ขอ ไม่อ้างว่าตอบครบ 8 ปุ่มแล้ว |
| อาหารต้องกินในพื้นที่กำหนด | revision04 ตอบ policy และผ่าน literal 2/2 | reader เดิมหา source ไม่ถึงทั้งที่มีข้อมูล |
| ถือขวดน้ำเข้า แต่ไม่ได้ถามกิน | revision04 ยังไม่ยืนยันสิทธิ์นำเข้า | source ยืนยัน consumption ไม่พอให้สรุป permission นำเข้า คงขอบเขตนี้ไว้ |
| จอง Cockpit และเปิดวันไหน | revision02 ตอบขั้นตอนจอง แต่ส่วนวันเปิดยังขาด | C11 reader/entity/context handoff ยังไม่ครบ ไม่ควรบอกว่าข้อมูล calendar หายทั้งหมด |
| CS2 ปรับตั้งค่า | เนื้อหาหลักรองรับ source ของรายการ 2026 แต่ literal clause/first line/source ID ยัง fail | แยก semantic support, localization และ protocol mismatch |

ตารางนี้เป็น agent review ของตัวอย่างที่ระบุ ไม่ใช่การนับ semantic accuracy แบบอิสระหรือแบบครบทุกคำถาม หลักฐาน source: [CONTEXT_SOURCE_REVIEW.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/CONTEXT_SOURCE_REVIEW.json) · [CALENDAR_SOURCE_EVIDENCE.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/CALENDAR_SOURCE_EVIDENCE.json)

## 7. สิ่งที่ยังไม่ครบและควรแก้ต่อ

- ชุดสอนยังมี whole-question constraints รั่วข้าม task ต้องแก้ annotation ใน revision ใหม่ ไม่แก้หลักฐาน/คะแนนรอบนี้ย้อนหลัง
- typed slots และ ambiguity ยังอ่อน: เวลา ปฏิเสธ เงื่อนไข, pronoun ที่ไม่มี antecedent และระยะเวลาที่ตีความได้หลายแบบ
- raw model ยังสับสน live availability กับ regular bookable timetable ต้องทดสอบ authority และการถามข้อมูลวัน/บริการที่ขาดแยก
- calendar หลายงาน/วันเปิดทั้งสัปดาห์ยังมี reader gap และ source applicability ต้องยืนยัน
- subset/cardinality ยังต้อง source ที่แยกกลุ่มปุ่มได้ชัด ไม่แก้ด้วยการตัดให้เหลือจำนวนที่ขอตามใจ
- HF NF4 ในเครื่องนี้ยังช้า: raw planner median ประมาณ 52.89 → 21.16 วินาที; API trained medianประมาณ 22.70 วินาที จึงยังไม่ผ่านเกณฑ์ความเร็วเดิมหลาย grades
- ต้องวัด fresh retained families หลังตรึง Flow/ชุดสอนใหม่ ก่อนตัดสินใช้แทนระบบเดิม ไม่ใช้คะแนน development แทน Full

วิเคราะห์สาเหตุและข้อบกพร่อง annotation อย่างละเอียด: [ROOT_CAUSE_REVIEW_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/ROOT_CAUSE_REVIEW_TH.md)

## 8. การรักษาข้อมูลและเหตุขัดข้องที่เก็บไว้

- ตรวจ original protected files 1138 ไฟล์: unchanged; ทุก candidate revision ใช้ native DB hash เดียวกัน
- ข้อมูลจริง approvals withdrawals และ logs เดิมไม่ถูกแก้ ไม่ติดตั้งทับ R78 ไม่รัน Legacy baseline หรือ Full ใหม่
- train01 หยุดก่อน optimization เพราะ Windows ปฏิเสธการแทนที่ไฟล์สถานะ เก็บรอบไว้ แล้ว run02 ใช้ baseline 16 rows ที่ตรวจ hashes แล้วต่อ โดยไม่เปลี่ยนค่าฝึก
- api01 หยุดใน grader เพราะ D venv ขาด tzdata หลังเรียกโมเดลหนึ่งครั้ง เก็บ probe ไว้ แล้วใช้ bundled Python เดิมสำหรับ grader ใน api02 ไม่เปลี่ยนเกณฑ์ตรวจ
- completed API measurement มี 37 requests (รวมคำถามซ้ำเพื่อเปรียบเทียบ/ตรวจการแก้), อีก 1 aborted grader probe เก็บแยก ไม่เอามาเลือกคำตอบดีที่สุด
- หลังวัดครบหยุดเฉพาะ process ของการทดลองเพื่อคืน GPU server ของผู้ใช้ยังคงเดิม

หลักฐาน transport: [MODEL_TRANSPORT_SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/MODEL_TRANSPORT_SUMMARY.json) · การตรวจสุดท้าย: [FINAL_VERIFICATION.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/FINAL_VERIFICATION.json)

## 9. ขอบเขตการเพิ่มข้อมูลของเจ้าของ

การเพิ่ม/แก้ facts ในชนิด record และ field ที่ Flow รองรับยังอ่านจากฐานข้อมูล ไม่ต้องฝึกคำตอบใหม่ทุกครั้ง แต่การเพิ่มชนิดข้อมูล/field หรือเจตนาใหม่ที่ reader ยังไม่รองรับต้องมีการผูก schema/reader เพิ่ม การฝึกนี้ไม่ได้รับประกันว่าใส่ข้อความใดก็ได้แล้วจะตอบถูกทุกคำถาม

## ไฟล์ประกอบ

- [PLAN_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/PLAN_TH.md)
- [CONTEXT_FLOW_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/CONTEXT_FLOW_TH.md)
- [FLOW_V4_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/FLOW_V4_TH.md)
- [PLANNER_PER_REQUEST_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/PLANNER_PER_REQUEST_TH.md)
- [API_PER_REQUEST_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/API_PER_REQUEST_TH.md)
- [DEVELOPMENT_PER_REQUEST_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/DEVELOPMENT_PER_REQUEST_TH.md)
- [ROOT_CAUSE_REVIEW_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/ROOT_CAUSE_REVIEW_TH.md)

## 10. ข้อจำกัด transport ของการเปรียบเทียบ API และตัวเปิด candidate

พบ inference HTTP requests 52 ครั้ง: สำเร็จ 49 และผิดพลาด 3 ครั้ง แม้ public API จะ HTTP 200 ครบ

ทั้ง 3 errors อยู่ในฝั่ง base ของ api02 ที่เรียก `/api/generate` ด้วย model name นอกสอง experimental profiles จึงถูก backend ปฏิเสธก่อน generation ตัวเรียกเก่าบางตัวอ่าน `PSU_KNOWLEDGE_LLM_MODEL` แยกจาก `PSU_CHATBOT_OLLAMA_MODEL` สถานะ HTTP 200 ด้านหน้าไม่ได้แปลว่า model transport ภายในสำเร็จทั้งหมด

**ผล API ก่อน/หลังรอบนี้จึงมี fallback transport compatibility เป็นข้อจำกัด ห้ามใช้สรุป causal effect ของน้ำหนักต่อคำตอบทั้งหมด** ส่วน raw planner 30 ข้อไม่มี HTTP fallback นี้ จึงเป็นการเปรียบเทียบก่อน/หลัง adapter ที่ตรงกว่า

เตรียม [runtime_profile.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/runtime_profile.py) และ [launch_candidate.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/launch_candidate.py) ให้ตั้งชื่อโมเดลทุกเส้นทางรวม knowledge fallback ให้ตรง profile โดยไม่ปลอมชื่อ checkpoint อื่น `--check-config` ผ่านแล้ว แต่ยังไม่ได้รัน paired API measurement ใหม่ด้วย launcher นี้ จึงคง errors เดิมไว้ในรายงานและระบุว่าต้องวัดใหม่ก่อนใช้จริง

หากต้องเปิด candidate แยกเพื่อทดลองภายหลัง ใช้ isolated training Python เรียก `launch_candidate.py` จะเปิดที่ http://127.0.0.1:12122/ และเก็บ runtime log ใหม่ทุกครั้ง ไม่เปิด server เดิมทับ Live provider ใน launcher นี้ยังเป็น controlled-unavailable fixture ไม่ใช่การยืนยันเครื่องว่างจริง

ค่าที่ตรวจแล้ว: [LAUNCH_CONFIG_VERIFIED.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r121_context_planner_training_20261022/LAUNCH_CONFIG_VERIFIED.json)