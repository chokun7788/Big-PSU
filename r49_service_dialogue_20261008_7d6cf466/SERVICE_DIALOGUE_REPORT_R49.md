# รายงานขยายเคสบริการและบทสนทนา r49

วันที่ 2026-10-09, เวลาไทย — runtime สุดท้าย `2026.10.09-service-dialogue-r49.2`

## สรุปผลที่ทดสอบจริง

ชุดใหม่ 110/110 เคส, เว็บปกติที่ debug=False 28/28 เคส, ชุดเดิมที่เกี่ยวข้อง 136/136 เคส ผ่านตามเงื่อนไขแต่ละชุด ไม่มี full test 20k ในรอบนี้ ตัวเลขสามชุดไม่ใช่เคสอิสระทั้งหมด: ชุด debug=False เป็นส่วนหนึ่งของชุดใหม่

| ชุด | รุ่น / วิธี | ผ่าน / เคส | คำขอ | หลักฐาน |
|---|---|---:|---:|---|
| ก่อนแก้ | Source, ปิด LLM/semantic | 37/102 | 122 | [R49_BASELINE_SOURCE_20261008_220522_4ad425_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_BASELINE_SOURCE_20261008_220522_4ad425_summary.json>) |
| แก้รอบแรก | Source, ปิด LLM/semantic | 100/102 | 122 | [R49_FIXED_SOURCE_V1_20261009_153531_1283dc_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_FIXED_SOURCE_V1_20261009_153531_1283dc_summary.json>) |
| แก้ตัวจับคำ | Source, ปิด LLM/semantic | 102/102 | 122 | [R49_FIXED_SOURCE_V2_20261009_154101_6ceee3_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_FIXED_SOURCE_V2_20261009_154101_6ceee3_summary.json>) |
| ตรวจขอบเขตเพิ่มเติม | Source, ปิด LLM/semantic | 12/12 | 24 | [R49_FOCUS_SOURCE_FINAL_20261009_154816_f951ed_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_FOCUS_SOURCE_FINAL_20261009_154816_f951ed_summary.json>) |
| เว็บ debug เปิด รุ่น r49.1 | HTTP API จริง | 110/110 | 142 | [R49_NEW_WEB_FINAL_20261009_155459_04ed37_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_NEW_WEB_FINAL_20261009_155459_04ed37_summary.json>) |
| เว็บ debug ปิด รุ่น r49.1 (พบข้อผิดพลาด) | HTTP API จริง | 6/28 | 60 | [R49_NODEBUG_WEB_FINAL_20261009_155632_557e5a_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_NODEBUG_WEB_FINAL_20261009_155632_557e5a_summary.json>) |
| เว็บ debug ปิด รุ่น r49.2 | HTTP API จริง | 28/28 | 60 | [R49_NODEBUG_WEB_R49_2_20261009_155907_57cd88_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_NODEBUG_WEB_R49_2_20261009_155907_57cd88_summary.json>) |
| ชุดเดิม r48 บนเว็บ r49.2 | HTTP API จริง | 136/136 | 136 | [R49_R48_REGRESSION_WEB_FINAL_20261009_160427_42e314_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_R48_REGRESSION_WEB_FINAL_20261009_160427_42e314_summary.json>) |
| ชุดใหม่บนเว็บ r49.2 | HTTP API จริง | 110/110 | 142 | [R49_NEW_WEB_R49_2_20261009_160728_8f9477_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\R49_NEW_WEB_R49_2_20261009_160728_8f9477_summary.json>) |

คำว่า “ผ่าน” รวมถึงตอบว่าไม่มีข้อมูลที่ยืนยันและขอรายละเอียดเมื่อควรทำ ไม่ได้หมายความว่าศูนย์ยืนยันทุกนโยบายแล้ว

## Coverage และ oracle

- ชุดใหม่ภาษา: {'th': 55, 'en': 55}; ประเภท: {'paraphrase': 28, 'typo': 28, 'compound': 10, 'followup': 24, 'scope': 18, 'ambiguity': 2}
- 14 หัวข้อบริการ มีวลีทั่วไปและ typo ทั้งไทย/อังกฤษ เช่น membrship, walkk, keyboarrd, คีย์บอด, โอนครังเดียว
- compound ตรวจครบทุก claim ที่คาดไว้และ missing fields ไม่ดูเพียง HTTP 200
- คำถาม 2–3 รอบ: motorcycles, map link, passport, own mouse/controller, note, slip channel, waiting point, date, ambiguous free และการเปลี่ยนไปถามรายชื่อเกม
- scope ตรวจว่าไม่ใช้ user_service_facts กับ Steam/team/ปุ่มยิง/กติกาแข่ง จุดนี้ไม่ได้ประเมินความครบถ้วนของคำตอบกติกาแข่งหรือ Steam
- แหล่ง oracle คือคำตอบผู้ใช้/claim IDs เดิมและ missing fields ไม่ใช้โมเดลตัดสินเองจากความคล้ายของประโยค ชื่อและข้อความภาษาอังกฤษแปลโดยระบบ ยังไม่มีการตรวจภาษาอังกฤษโดยเจ้าของเพิ่ม
- debug=False ตรวจข้อความที่จำเป็น, missing ที่ชัด, outcome ไม่ประกาศ complete เมื่อข้อมูลไม่ครบ, ไม่มี trace หลุด, ไม่ลากที่จอดรถกลับมาหลังเปลี่ยนเรื่อง
- ผลทั้งหมดเป็น automated checks ไม่มีหลักฐานใหม่จากการใช้บริการจริง ไม่มีการยืนยันสถานะจองสดในรอบนี้

## ทำไม baseline ถึงผิด

baseline ผ่าน 37/102 ไม่ควรแปลว่าอีก 65 คำตอบเป็นข้อเท็จจริงผิดทั้งหมด: 51 เคสไม่ผ่านข้อความที่ต้องมี และบางเคสเนื้อหาถูกแต่ไม่ผ่าน trace/context/scope contract เงื่อนไขที่ตกซ้ำซ้อนกันได้: `{'required_content': 51, 'claims_traced': 52, 'english_no_thai': 1, 'missing_fields': 12, 'context_used': 18, 'separate_scope': 3}`

1. **คำและวลีไม่เข้าตัวจับ claim** — ข้อมูลมีอยู่ แต่ nonmembers, turn up, incorrect transfer receipt image หรือ motorcycle parking ไม่ตรงคำที่ handler รู้จัก จึงตกไป handler รายชื่อบุคลากร/ตารางเวลา/คำตอบไม่พบข้อมูล แก้ด้วยแนวคิดและ anchor ที่สัมพันธ์กับบริการ
2. **สะกดผิดทำให้ไม่เห็น noun หลัก** — อังกฤษใช้ token และ OSA หนึ่ง edit; ไทยไม่มีช่องว่างคั่นทุกคำและมีเครื่องหมายรวม จึงเทียบ span พร้อม diacritic fold กรณีโอนครังเดียวต้องเลือกระยะที่ใกล้ก่อนความยาว เพื่อไม่กินตัว น ของ “โอน”
3. **คำถามสั้นหายเงื่อนไขเดิม** — “แล้วเมาส์ล่ะ” ไม่มี own/personal, “ส่งที่ไหน” ไม่มี slip; เดิม reroute เป็นคำถามใหม่ แก้โดยบันทึก typed service state จากคำตอบที่ ACK แล้วและขยายเฉพาะ slot ที่สัมพันธ์กัน
4. **ขอบเขตข้อมูลรั่ว** — สมาชิกศูนย์ใช้ตอบสมาชิก Steam/team; นโยบายห้ามเมาส์ส่วนตัวมีโอกาสใช้ตอบปุ่มเมาส์ในเกม ต้องแยก service/account/game-control/tournament ก่อนเลือก claim
5. **ข้อมูลว่างแต่ขยายจากส่วนใกล้เคียง** — ดูเพื่อนได้ไม่เท่ากับฟรี มีที่จอดไม่เท่ากับฟรี ห้าม keyboard/mouse ไม่ยืนยันว่าห้าม controller แก้โดยแสดง missing field โดยตรงและไม่สร้างนโยบาย
6. **เส้นทางเว็บ debug=False ไม่ส่ง state** — รุ่น r49.1 ใช้ query_debug.trace ซึ่งมี preprocessing เท่านั้น จึงไม่เห็น user_service_facts การทดสอบ store แยกส่วนผ่านเพราะส่ง full trace ให้เอง แต่ HTTP ปิด debug ผ่านเพียง 6/28 รุ่น r49.2 ใช้ result.trace ภายในจึงผ่าน 28/28

ไม่ได้เกิดจากคะแนน retrieval เพียงอย่างเดียว หลายเคสหลุดก่อนถึงการค้นหรือเปลี่ยน operation เลย [รายละเอียดทุกเคสที่เคยพลาด](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r49_service_dialogue_20261008_7d6cf466/FAILED_CASE_ANALYSIS_R49.md>) เก็บ mode/trace/normalized query คำตอบเดิม และคำตอบหลังแก้ เพื่อแยกสาเหตุระดับ route/context/oracle

## ตัวอย่างผลจริงหลังแก้

### th-follow-parking-moto

1. มีที่จอดรถไหม
2. แล้วมอเตอร์ไซค์ล่ะ

คำตอบสุดท้ายจริง:

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-own-controller

1. เอาคีย์บอร์ดส่วนตัวมาได้ไหม
2. แล้วจอยล่ะ

คำตอบสุดท้ายจริง:

```text
ข้อมูลที่ยืนยันห้ามเฉพาะคีย์บอร์ดและเมาส์ส่วนตัว ยังไม่ได้ยืนยันสิทธิ์นำจอยส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-follow-transfer-note

1. จองหลายเครื่องโอนครั้งเดียวได้ไหม
2. ต้องเขียนอะไรใน note

คำตอบสุดท้ายจริง:

```text
จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

ยืนยันว่าต้องเขียน Note ตอนจองเพื่อให้ศูนย์ตรวจสอบ แต่ยังไม่ได้กำหนดข้อความหรือรูปแบบ Note ที่ต้องเขียนครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-select-parking-fee

1. มีที่จอดรถไหม และนั่งดูเพื่อนได้ไหม
2. ฟรีไหม
3. ที่จอดรถ

คำตอบสุดท้ายจริง:

```text
มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

ยังไม่ได้ระบุค่าจอดรถ จึงยืนยันว่าจอดฟรีไม่ได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-watch-free

1. นั่งดูเพื่อนได้ไหม
2. ฟรีไหม

คำตอบสุดท้ายจริง:

```text
สามารถมานั่งดูเพื่อนเล่นได้ครับ

ยังไม่ได้ระบุค่าเข้าชมหรือยืนยันว่าเข้าดูเพื่อนฟรีครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### th-topic-reset

1. มีที่จอดรถไหม
2. PC มีเกมอะไรบ้าง
3. แล้วมอเตอร์ไซค์ล่ะ

คำตอบสุดท้ายจริง:

```text
ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?
```


## Unit checks ที่เกี่ยวข้อง

Unit logs นี้เป็น gate ระหว่างพัฒนา ก่อนแก้การส่ง trace ฉบับเต็มใน server รอบสุดท้าย จึงไม่ใช้เป็นหลักฐานว่าเส้นทางเว็บปกติผ่านเอง หลักฐานสุดท้ายของส่วนนี้คือ HTTP debug=False 28/28 และ HTTP ชุดใหม่/ชุดเดิมบน runtime r49.2 ด้านบน

ปรับ assertion เก่าเพียงกรณีจอยส่วนตัว จาก handler ต้องไม่รับคำถาม เป็น handler ต้องระบุ `personal_controller_permission` ว่ายังไม่ยืนยัน ไม่มีการเปลี่ยนคำตอบนโยบายให้จอยได้รับอนุญาตหรือถูกห้าม และไม่ได้แก้ oracle ของเคสที่พลาดเพื่อให้ผลผ่าน

- test_service_fact_dialogue_r49: Ran 10 tests in 2.039s  OK — [test_service_fact_dialogue_r49_220db1.txt](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\test_service_fact_dialogue_r49_220db1.txt>)
- test_user_service_facts_r48: Ran 9 tests in 0.219s  OK — [test_user_service_facts_r48_b4a027.txt](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\test_user_service_facts_r48_b4a027.txt>)
- test_task_memory_r41: Ran 23 tests in 7.830s  OK — [test_task_memory_r41_218ff1.txt](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\test_task_memory_r41_218ff1.txt>)
- test_two_turn_choices_r39: Ran 16 tests in 9.889s  OK — [test_two_turn_choices_r39_4c0706.txt](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\test_two_turn_choices_r39_4c0706.txt>)

## เวลาในการตอบบนเครื่องนี้

รวมคำขอจริงจาก 3 ชุดสุดท้าย 338 requests: median 0.367s, p95 0.777s, max 14.157s นี่คือการส่งตามลำดับไปยังเครื่อง/โมเดลที่เปิดอยู่ จึงไม่ใช่ benchmark รองรับหลายคนพร้อมกันหรือ WordPress live booking และรวมกรณีขอรายละเอียด/ไม่พบคำตอบด้วย

## สิ่งที่เจ้าของยังต้องให้ข้อมูล

1. ที่จอดรถฟรีไหม ถ้ามีราคา เป็นของศูนย์หรือระบบอาคาร?
2. คนมานั่งดูเพื่อนต้องจ่ายเงินไหม มีเงื่อนไขจำนวนคนหรือพื้นที่ไหม?
3. จอยส่วนตัวอนุญาตไหม แยก PC/PS5/Switch/VR และกิจกรรมแข่งหรือบริการทั่วไปหรือไม่?
4. Note สำหรับโอนรวมต้องระบุอะไรบ้าง เช่น เลขรายการ ชื่อผู้จอง และยอดของแต่ละรายการ?
5. รอก่อนเวลาจองใช้โซนกลางได้หรือมีจุดอื่นที่กำหนด?
6. เปลี่ยนวันเมื่อจ่ายแล้วทำทางไหน และกรณี “เลื่อนแทนคืนเงินไม่ได้” ต่างจากเปลี่ยนวันผิดอย่างไร?
7. ข้อมูลเดิมที่ยังว่าง เช่น เด็ก/ผู้ปกครอง, ติดตั้งเกม, บัญชีผู้จ่าย, สตรีม/ถ่ายรูป, เวลาที่เสียจากอัปเดต/เครื่องเสีย ยังคงสถานะเดิม

## ขอบเขตและส่วนที่ยังพัฒนาได้

- ตัวแก้คำรอบนี้จำกัด noun บริการและ anchor ไม่ใช่ spell checker ทั่วภาษา; คำยาวเกิน 256 ตัวอักษรจะไม่ทำ fuzzy recovery
- ยังไม่รับประกันคำผิดหลายส่วนที่ไม่เหลือ anchor, สลับภาษาในประโยคทุกแบบ หรือคำถาม follow-up ทุกสำนวน
- ความจำใช้ latest acknowledged answer; restart server ทำให้ประวัติฝั่ง memory หาย ไม่ได้เพิ่ม persistence หรือระบบหลายเครื่องในงานนี้
- หลังเปลี่ยนหัวข้อแล้วถาม “แล้วมอเตอร์ไซค์ล่ะ” ระบบขอข้อมูล/ไม่พบคำตอบได้ เงื่อนไขผ่านคือไม่ยกคำตอบที่จอดเก่ามาปะปน ไม่ใช่สัญญาว่าจะสรุปความหมายได้ทุกกรณี
- คำถามสมาชิกทีม VALORANT และ Steam ผ่านการกัน scope; บางคำถามยังขอรายละเอียด/ไม่พบข้อมูล ไม่ถือว่ารู้จำนวนสมาชิกทีมแล้ว
- candidate ที่เปิดคือ r49.2; portable bundles รุ่นก่อนหน้ายังไม่ได้ rebuild ทั้งหมด
- เพิ่ม test case ใหม่เมื่อมีคำถามผู้ใช้จริงที่พลาด โดยคง oracle ตามข้อมูลจริงก่อนปรับ handler ไม่จำเป็นต้องขยาย alias ทุกคำผิด

## การเก็บไฟล์และตรวจรุ่น

แก้ 6 ไฟล์เดิม เพิ่ม 3 ไฟล์ code/test; ไฟล์เดิมอื่นที่ snapshot ไว้ 320 ไฟล์คง hash เดิม; curated/rules ไม่เปลี่ยน; source/package ตรงกัน 169/169 ไฟล์ ตรวจ Git diff --check exit 0

[SOURCE_AND_RELEASE_AUDIT_R49_2.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\SOURCE_AND_RELEASE_AUDIT_R49_2.json>) · [SOURCE_CHANGE_R49_2.diff](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\SOURCE_CHANGE_R49_2.diff>) · [GIT_STATUS_R49_2.txt](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\GIT_STATUS_R49_2.txt>) · [GIT_DIFF_CHECK_R49_2.txt](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\GIT_DIFF_CHECK_R49_2.txt>)

snapshot ก่อนแก้และ log แต่ละรอบเก็บแยกไว้ในโฟลเดอร์นี้ รวมถึงผลรอบที่ไม่ผ่าน ไม่มีการลบ log หรือ reset/stash Git เดิม

Flow: [SERVICE_DIALOGUE_FLOW_R49.md](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r49_service_dialogue_20261008_7d6cf466\SERVICE_DIALOGUE_FLOW_R49.md>)
