# ผลทดสอบเคสเพิ่มเติม r45.2 — 7 ตุลาคม 2026

## ผลสุดท้าย

- ชุดใหม่ 40 เคสก่อนแก้ผ่าน 15/40; พบ 25 เคสผิดหรือข้อมูลเกิน scope ที่ขอ
- หลังแก้ ชุดใหม่ 40 เคสผ่านทั้งหมด ร่วมกับเคสเดิม 103 และเคสต่อเนื่อง/ขอบเขตเพิ่ม 5 รวม **148/148 เคส HTTP, 191 requests**
- Unit ที่เกี่ยวข้อง **128/128 methods**: r45 scope 17, r44 workbook 19, dialogue/resume/schedule/booking fixtures เดิม 92
- Code/data parity source ↔ release **155/155 ไฟล์**; workbook ต้นฉบับและสำเนา unchanged; ราคาทั้งหมดและเครื่องคิดค่าบริการรายชั่วโมงเดิม unchanged
- แก้ production code เพียง `app/pipeline/zone_rental.py`; เพิ่ม `tests/test_rental_scope_r45.py`; ไม่ reset/stash/commit งานเดิมและไม่ลบ log
- เว็บที่ใช้: http://127.0.0.1:8091/ รุ่น `2026.10.07-rental-scope-r45.2`
- ชุด local ล่าสุด: `C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r45_rental_cases_20261007_110336_e4eaa3\release_r45_2\PSU_Esports_Chatbot_Local` เปิด `Open-PSU-Esports-Background.cmd`; ไม่ได้ rebuild ชุดแจกพร้อม/ไม่มีโมเดลในรอบนี้

## เคสที่ครอบคลุม

ภาษาไทย/อังกฤษ, ประโยคยาว/สั้น, ชื่ออุปกรณ์พิมพ์เบิ้ล/ขาด เช่น cockpitt/cockpik/nintndo/playstaton, คำลงท้าย, ชื่อสินค้าเลขผิด PS55, Xbox ที่ไม่มีราคา, ครึ่งวัน/เต็มวัน, หน่วยงานภายใน/ภายนอก, ไม่เอา/ยกเว้น/not/excluding, เปลี่ยนกลุ่มหรือช่วงในคำถามต่อ, รวมอะไรบ้างแล้วกลับมาถามราคา, จองยังไง, เปลี่ยนเรื่องเกม/กฎ/เวลาเปิด, กลับไปเรื่องราคาเหมา, compound ต่างกลุ่ม/ต่างช่วง/โซนเดียวคนละเงื่อนไข, เลือก child ต่อจาก compound, ขยายทั้งหมด, ยกเลิกถามราคา

## สาเหตุและวิธีแก้

| หมวดที่ผิดในชุดใหม่ | จำนวน | สาเหตุ | การแก้ |
|---|---:|---|---|
| Grammar/คำขยาย | 1 | สำหรับ/แบบถูกมองเป็นชื่อสินค้า unknown | แยกคำโครงสร้างออกจาก noun ที่ขอ |
| ปฏิเสธกลุ่ม | 2 | เจอ internal แล้วเลือก internal แม้มี excluding/ไม่เอา | อ่าน polarity ก่อนเลือกค่า ไม่ใช้ positive substring อย่างเดียว |
| ปฏิเสธช่วง | 2 | half/full รวมกันแม้ขอ not half | ตัดช่วงที่ถูกปฏิเสธ หากปฏิเสธทุกช่วงให้ clarification |
| ทั้งหมดพร้อมยกเว้นใน followup | 2 | หลุดไป hourly หรือ reset groups/periods | ขยาย targets และคงตัวกรองที่รับแล้ว |
| Unknown menu/PS55 | 4 | ไม่รับคำตอบชื่ออย่างเดียว หรือ match PS5 เป็น prefix ของ PS55 | แยก noun choice จาก new topic; รักษาเลขสินค้า ไม่ fuzzy แก้เลข |
| Field แล้วกลับถามราคา | 2 | Generic price ไม่มี target จึงออกจาก rental | คง typed scope และเปลี่ยน requested field กลับเป็น rates |
| All Zones ตัดโซน | 2 | ยังคงใช้ราคา full package ทั้งที่ขอ modified bundle | แจ้ง custom_package missing ไม่คำนวณหรือใช้ 12,000 แทนแพ็กเกจที่ตัดโซน |
| Explicit followup | 2 | แล้ว/And rental price ถูกถือเป็นคำถามใหม่ reset scope | ยอม inherit เฉพาะ contextual link ที่ชัดเจน |
| Booking followup | 2 | จองยังไง/How do I book it ไม่คง rental domain | ตอบตรงว่าขั้นตอน rental ไม่มีใน workbook ไม่ยก play booking cap 3 sessions มาแทน |
| Compound conditions | 6 | เก็บ targets/groups/periods เป็นรายการรวม ทำ Cartesian product จนตอบเงื่อนไขที่ไม่ได้ถาม | เพิ่ม scoped_requests ต่อ clause และ render เฉพาะ target/group/period triples ที่สังกัด child นั้น |

ตัวอย่างก่อนแก้ PC เต็มวันภายนอก + VR ครึ่งวันภายใน ถูกตอบทั้งสองกลุ่ม/ทั้งสองช่วงของทั้งสองโซน หลังแก้คืนเฉพาะ `pc:external:full_day=4000` และ `vr:internal:half_day=1500`

## Regression ที่พบระหว่างแก้

1. รวม source cases 143 รอบแรกผ่าน 142/143: “both groups” ถูกจัดเป็น unknown noun หลังเพิ่มเมนูสินค้าไม่รู้จัก แก้ gating ให้คำสั่ง scope/selection ที่รู้จักมาก่อน unknown selection และเพิ่ม unit
2. เว็บ candidate .1 ผ่าน 147/148: “Competition rules for CS2” หลังคำถามราคาแบบหลายเงื่อนไขถูกคิดเป็น menu selection และเขียนทับ memory เรื่องราคา ทำให้ resume พก unknown ผิดกลับมา แก้ใช้ domain guard เดิมสำหรับ rules/games/controls/schedule ก่อน noun selection เพิ่ม unit และเพิ่ม check ว่า intermediate turn ไป competition_rules จริง
3. เว็บ candidate .2 ผ่าน 148/148 เก็บ candidate .1 พร้อม raw/failed logs ไว้ ไม่แก้ frozen release เดิม

## คะแนนและการตรวจคำตอบ

เส้นทาง rental ใช้คะแนนคงที่ .99 แปลว่า direct source route ไม่ใช่ความน่าจะเป็นว่าเข้าใจ intent ถูก 99% บั๊กก่อนแก้เกิดก่อน render จากการตี scope ผิด แม้ข้อมูลและ source hit ถูก จึงต้องตรวจ expected rate IDs/values, missing fields, intermediate topic, rendered values และ validation แยกจากคะแนน/HTTP success

ตัวเลข oracle อิง XML cells B3:E8 ของ workbook เดิมที่อ่านใน r44; unit r44 เปิด archived workbook โดยตรงและเทียบ 24 cells; ทดสอบยังแยก seating capacity จากจำนวนเครื่อง ไม่กำหนด seats เป็นผู้เล่นพร้อมกัน

เวลาคำตอบ rental ที่วัดในเว็บรอบสุดท้าย 181 requests: median 0.043 s, max 0.2937 s; เป็น HTTP timing ไม่รวมวาดหน้าเว็บ ไม่ใช่เวลา WordPress fetch และไม่รับรองเวลาคำถาม LLM/general

## สิ่งที่ยังไม่ได้ยืนยัน

- จำนวนชั่วโมง/ช่วงเวลาของ half/full day, effective dates, ช่องทาง/มัดจำ/ยกเลิกการเช่าเหมา, ค่าเจ้าหน้าที่รวมไหม/ใครจ่าย, สิทธิ์บุคคลที่ไม่ได้จองนามหน่วยงาน, ราคา modified bundles/ส่วนลด/ต่อเครื่อง/รายชั่วโมง ยังต้องข้อมูลจากศูนย์
- รอบนี้ไม่ใช้ตารางราคาไปยืนยัน live availability ของ WordPress; booking fixture methods ผ่านไม่ได้เท่ากับตรวจสถานะจองจริงกับเจ้าของ
- “Where is the venue?” ยังเป็น english_no_answer; ในชุดเดิมเป็น negative test ไม่ให้ตอบราคา จึงไม่ถือว่าตอบคำถามสถานที่ถูกแล้ว
- 148 เคสเป็น focused regression ไม่ใช่ full 20k suite หรือการรับรองคำพิมพ์ผิดและ compound ทุกรูปแบบ; schema scoped requests จำกัด 6 children
- การยกเลิกถามราคาไป `ambiguity_clarification` ในเคสที่ลอง เป็น negative gate ว่าไม่ resend ราคา ไม่ถือว่าทดสอบข้อความยืนยันยกเลิกที่สวยงามครบแล้ว

## หลักฐาน

- `R45_FINAL_WEB_V2_20261007_112428_444855_summary.json` และ JSONL raw ที่อ้างใน summary
- `CASE_ANALYSIS_R45_ALL_TH.md` มีคำถาม/expected/chosen plan/คำตอบก่อนและหลังทั้ง 40 เคส
- `FINAL_AUTOMATED_GATES_R45_2.json`, `FINAL_HEALTH_R45_2.json`, `SOURCE_AUDIT_R45_2_FINAL.json`, `SOURCE_CHANGE_R45_2_FINAL.diff`
- source/unit logs ทุก attempt; backup `before/`; `FLOW_R45_FINAL.md`
