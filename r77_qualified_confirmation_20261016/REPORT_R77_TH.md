# รายงาน R77 — คำยืนยันพร้อมเงื่อนไข

## สถานะสรุป

ลงมือแก้และตรวจ targeted common-format/LLM ON แล้วในสำเนา R77 แยกจาก R76 ไม่ได้รัน legacy/OFF/full ชุดใหญ่ และไม่ได้แทนเว็บที่เปิดอยู่โดยอัตโนมัติ

แก้กรณีหลังบอทเสนอหัวข้อ ผู้ใช้ตอบ `ใช่ แต่…`/`Yes, but…` ให้ตรวจ subject/ownership/context และเงื่อนไขที่เหลือก่อนอ่าน source คงข้อมูลจริง 602 heads เดิมทั้งหมด ไม่มีการสร้าง owner approval หรือเผยแพร่ release ใหม่

## 1. สาเหตุที่พบ

### 1.1 คำยืนยันที่มีเงื่อนไขไม่มีเส้นทางเฉพาะ

R76 มี bare yes และ rejection+replacement แต่ข้อความ yes-but ไม่ตรงสองแบบนี้ จึงหลุดกลับไปตีความเป็นคำถามเดี่ยว ขณะที่ qualifier อย่าง `เป็นของศูนย์` ต้องพึ่งหัวข้อที่บอทกำลังถามอยู่

ผล baseline 8 qualification contracts ไม่ผ่านทั้งหมด หลายเคสกลับเป็น retry เพราะโมเดลเชื่อมต่อไม่ได้ และบางเคส clarification ไม่ตรงหัวข้อ เช่น TH ของศูนย์ไปถามหัวข้อเบอร์โทร คะแนนนี้ไม่เท่ากับตอบนโยบายผิดทุกเคส และเป็นผลภายใต้ controlled model-unavailable environment

### 1.2 การยืนยันหัวข้อไม่พอจะยืนยัน scope

หัวข้ออุปกรณ์ส่วนตัวไม่ได้เป็นหลักฐานเรื่องของศูนย์หรือเรื่องการแข่งขัน การนำ source เดิมมาใช้เพราะมีคำว่าใช่เสี่ยงขยายกฎเกินข้อมูล ต้องแยกค่าที่เปลี่ยนและค้น source ที่เข้าเงื่อนไขครบ

### 1.3 คำปฏิเสธและคำขยายหายระหว่างวิเคราะห์ได้

การดูคำว่า mine หรือ tournament โดยไม่อ่าน not ให้ครบทำให้กลับขั้วความหมาย การลบ prefix `my wireless` ทั้งหมดทำให้ wireless หาย จึงแก้ matcher ให้ลบเฉพาะ grammar/ownership ที่รู้ ไม่ใช้รายชื่อคุณสมบัติใหม่เป็นคำที่ข้ามได้

### 1.4 ข้อมูลบางเงื่อนไขยังไม่มีจริง

อายุ/ผู้ปกครอง ผ่อนชำระ เงินเกิน/ขาด และเวลาตรวจจ่ายยังไม่มีนโยบายยืนยันตามงานก่อนหน้า การตอบ unknown สำหรับเรื่องเหล่านี้ไม่ใช่ content failure เช่นเดียวกับ qualifier ที่ไม่มี source ใน scope ที่ขอ ไม่เพิ่ม policy เพื่อให้ผ่าน test

## 2. สิ่งที่เปลี่ยนในโค้ด

| ไฟล์ | การเปลี่ยน |
|---|---|
| system/app/knowledge/common/qualified_reply.py | parser สำหรับ qualified acknowledgement, positive/negative scope, subject จาก metadata, uncovered text และ compatible source |
| system/app/knowledge/common/profile_confirmation.py | ประมวลผล qualification ก่อน bare confirmation |
| system/app/knowledge/common/answer.py | เลือก source ที่ตรง scope หรือ clarification/unconfirmed, คง barrier และ audit; ใช้ DEFAULT_FIELDS เดิม |
| system/app/pipeline/migrated_chat.py | คำถามใหม่หลัง yes-but ใช้ dispatcher ปกติพร้อมตัด context เก่า |

ไม่มี ID ของ keyboard/slip หรือชื่อหัวข้อ fixture ใน production router ชื่อ subject มาจาก query_profile; ภาษา ownership/context เป็น grammar แบบมีขอบเขต จึงยังไม่ใช่ตัวเข้าใจภาษาทั่วไป

## 3. ผลทดสอบและความหมายของคะแนน

| ชุด | ผล | วัดอะไร | ไม่ได้ยืนยันอะไร |
|---|---|---|---|
| baseline01 บน R76 | qualification 0/8; รวม helper checks 2/10 | แสดงช่องว่างเดิมด้วย 8 เคสเดียวกัน | ไม่ใช่ accuracy ทั้งระบบ/จำนวน false facts |
| qualified01 บน R77 | 34/34 | qualifier, fixture, state, handler | โมเดลจริง/ทุกสำนวน |
| qualified02 บน R77 | 41/41 | เพิ่ม negation contrasts และ wireless/gaming; รวม 8 เคส baseline ผ่าน 8/8 | ไม่ใช่ 41 คำตอบนโยบายจริงทั้งหมด |
| regression01 | 43/43 | source content contracts ผ่าน dispatcher เดิม | ไม่ใช่คะแนนสร้างคำตอบด้วยโมเดลจริง |
| scope01 | 50/50 | แยกขอบเขต/unknown/ไม่ใช้ source ผิดเรื่อง | ไม่ได้เพิ่มนโยบายของเจ้าของ |
| rephrase_regression01 | 34/34 | no/ไม่ใช่+ถามใหม่, follow-up, update/withdraw, handler | browser/TCP/WordPress สด |

ชุดต่าง ๆ มีบางสถานการณ์ซ้ำกัน จึงไม่รวมเป็นจำนวน unique requests หรือ global accuracy ทุกกรณีตั้ง LLM ON แต่ deterministic path และ fixture fallback สามารถตอบได้เมื่อโมเดลไม่พร้อม

### เคสสำคัญที่ตรวจแล้ว

- ของศูนย์ TH/EN: ไม่คืนคำห้ามอุปกรณ์ส่วนตัวแทน
- ของส่วนตัว TH/EN: อ่าน source เดิมที่ห้ามใช้ ไม่สร้างกฎใหม่
- ใช้แข่ง TH/EN: ถ้าไม่มี source scope แข่ง ให้ถามเกม/รายการ; fixture ที่เพิ่ม scope แข่งอ่าน COMP_SCOPE เท่านั้น
- ไม่ใช่ของผม แต่เป็นของศูนย์: อ่าน scope ใหม่; ไม่ใช่ของผมล้วน ๆ ยังไม่สรุปว่าเป็นของศูนย์
- ไม่ได้ใช้แข่ง แต่เล่นทั่วไป: อ่าน context=studio ไม่กลับเป็นการแข่งขัน
- mine and studio's: clarification เพราะขัดกัน
- my wireless keyboard / my gaming keyboard: คงคำขยายและไม่ยืนยันเกินข้อมูล
- yes-but ตามด้วยคำถามชำระ: อ่าน source ชำระเงินใหม่; And when? ใช้บริบทใหม่
- อายุ 12/ผ่อน: unconfirmed topic ที่ตรงเรื่อง ไม่ตอบกฎอุปกรณ์แทน
- yes หลัง unresolved ไม่คืนกฎเก่าที่เพิ่งไม่ครอบคลุม
- เพิ่ม subject ใหม่ cobaltpad/แผงฟ้าข้อมูลแยก: อ่าน metadata โดยไม่เพิ่ม alias หรือ record ID ใน router
- เปลี่ยนคำตอบ STUDIO_V1 → STUDIO_V2: อ่านค่าล่าสุด; withdraw แล้วไม่คืน V2; เปลี่ยน scope ของ pending ตอบ expired
- overlapping profiles: clarification ไม่เลือกด้วยคะแนนค้น

### แยก model transport

qualified01/02 และ rephrase_regression01 จำลอง model-unavailable อย่างชัดเจนเพื่อทดสอบเส้นทางควบคุม ไม่ใช่การอนุมานจริง

regression01 และ scope01 ไม่ได้จำลอง model transport: MODEL_HEALTH บันทึก actual attempts ที่ล้มด้วย URLError / WinError 10013 และ successes=0 ทั้ง common_query_plan/common_entity_select ที่มีการเรียก ส่วน state kind=model ที่ status=ok แต่ successes=0/last_checked_at=0 หมายถึงยังไม่มีหลักฐานสำเร็จ ไม่ถือว่าเชื่อมโมเดลผ่าน

ดังนั้นยังยืนยัน semantic equivalence, paraphrase robustness และ latency ของโมเดลจริงไม่ได้ ปัญหานี้เป็น transport/สิทธิ์ socket ในบริบทเครื่องมือ ไม่ใช่หลักฐานว่าคำตอบของโมเดลผิด ไม่มีการเรียกซ้ำข้ามข้อจำกัดด้วยช่องทางอื่น

### แยกการทดสอบ API

ทดสอบ HTTP ChatHandler ด้วย request/response bytes และ session state ใน memory ผ่าน ไม่ได้เปิด TCP/browser จริง และไม่ได้ดึง WordPress ใหม่ ความถูกต้องสถานะจองที่ผู้ใช้เคยยืนยันยังเป็นหลักฐานคนละส่วนกับรอบนี้

## 4. ข้อมูลและไฟล์เดิม

DELIVERY_QA_FINAL.json ยืนยัน:

- source R76 จำนวน 1,425 ไฟล์ตาม manifest ไม่เปลี่ยนแม้แต่ไฟล์เดียว
- logical tables ทุกตารางเท่ากัน รวม source snapshots, revisions, audit และ approvals
- ฐานจริงทั้งสองสำเนา SHA256 = 4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d
- cc_heads=602; cc_approvals=0; cc_releases=0
- ไฟล์ที่เปลี่ยน 4 ไฟล์ parse Python ผ่าน

fixtures อยู่ verification/<รอบ>/system/data/knowledge/common.sqlite เท่านั้น ไม่ปน system/data/knowledge/common.sqlite; marker เช่น STUDIO_V2/COMP_SCOPE/COBALT_SCOPE เป็นข้อมูลตัวอย่าง ไม่ใช่นโยบายจริง

เก็บ baseline01, qualified01, qualified02, rephrase_regression01 และ results regression01/scope01 ทั้งหมดไว้ ไม่ทับ log เดิม baseline ที่ไม่ผ่านยังคงอยู่เพื่อวิเคราะห์ย้อนหลัง

## 5. ข้อจำกัดที่ยังเหลือ

1. query_profile ปัจจุบันรองรับ 2 tasks และ known จริงเพียง 2 records ยังไม่ครอบคลุมทุก FAQ/policy/procedure
2. ไม่มี subject definitions/typed properties ที่พิสูจน์ความหมายได้ทั่วไป เช่น proof of payment vs payment identity หรือ wireless ใช้เป็นเงื่อนไขอย่างไร
3. คำตอบ qualified หลัง generic name/price/entity menu และรูป typo/สำนวนอิสระยังไม่ครอบคลุม
4. หลายหัวข้อ/หลายเงื่อนไขและข้อยกเว้นที่ซ้อนกันยังอาจต้องถามเพิ่ม การไม่เลือก source ผิดไม่ได้แปลว่าตอบได้ครบทุกคำถามแล้ว
5. ownership=any ไม่สามารถประกาศ studio-only ใน schema ตอนนี้ ต้องออกแบบเพิ่มก่อนรองรับนโยบายเฉพาะนั้น
6. โมเดลจริงและ browser/TCP หลัง restart ยังไม่ผ่านการยืนยันในรอบนี้; draft copy ยังไม่เป็น production release/portable package

## 6. เอกสารและหลักฐาน

- FLOW_R77_TH.md: flow และการตรวจปรับ 3 รอบ
- README_R77_TH.md: วิธีเปิดสำเนาทดลอง
- NEXT_STEPS_R77_TH.md: งานต่อเรียงลำดับ/ส่วนที่ทำเองได้/ส่วนที่ต้องข้อมูล
- verification/baseline01/RESULTS.json, verification/qualified01/RESULTS.json, verification/qualified02/RESULTS.json
- verification/rephrase_regression01/RESULTS.json
- results/regression01/SUMMARY.json, ANSWERS.jsonl, MODEL_HEALTH.json
- results/scope01/SUMMARY.json, ANSWERS.jsonl, MODEL_HEALTH.json
- DELIVERY_QA_FINAL.json, CHANGESET_FINAL.patch
