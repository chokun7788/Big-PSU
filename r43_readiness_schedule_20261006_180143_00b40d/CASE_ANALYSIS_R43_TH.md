# วิเคราะห์ปัญหา r43 จากหลักฐานจริง

## 1. ข้อมูลเวลาอยู่ครบ แต่ generic English ตอบไม่ครบ

Baseline `_answer_schedule` ใช้ branch weekday=None ซึ่งตอบเพียง Monday-Friday และให้เลือกวัน คำตอบไม่เข้าถึง renderer ของ slot รายวัน ข้อมูลไม่ได้ขาดและไม่มีเหตุให้ผู้ใช้ระบุวันเพิ่มเมื่อเขาขอตารางทั้งหมด แก้เป็นสรุป 7 วันจาก regular_service_slots พร้อม maintenance/lunch/closure guards

## 2. ระบุ “every day” แล้วกลับถาม scope

HTTP r43.2 เคส `Please list opening hours for every day.` ให้ `All of which topic or service would you like to see?` mode conversation_scope_clarification, confidence ของ guard ไม่ใช่คะแนนว่าข้อมูลปฏิทินผิด request_plan มี act=ambiguous, tasks=[], missing=scope และ metadata context_domain=service_fee ไม่มี source hits

สาเหตุ: price conversation planner มี ALL regex ที่ตรง every แต่ OTHER_TASK รับ open ไม่รับ opening/hour schedule เมื่อ price=False จึงเข้าสาขา all_selected ไม่มีบริบทก่อนเข้าตัวตอบ schedule ทำให้ไม่ได้อ่านข้อมูลเวลาเลย ควรตอบตารางประจำทุกวันพร้อมช่วงเปิด/maintenance ไม่ใช่ถามว่าทั้งหมดเรื่องอะไร

แก้ด้วย explicit schedule operation signals ก่อนใช้ all/every เพื่อเลือกราคา ไม่เพิ่ม alias ของทั้งประโยค และไม่ใช้คำ hours เดี่ยวเพื่อเปลี่ยนหมวด เพราะ 2 hours อาจเป็น duration ของราคา ทดสอบทั้งถามเดี่ยว ถามหลังราคา และ all services 2 hours เพื่อไม่แก้เคสหนึ่งแล้วทำอีกเคสเสีย

## 3. เปิดเว็บจาก health ผ่าน แต่ยังไม่พิสูจน์ตอบได้

ตัวเปิดเก่าตรวจ service/version/installation เท่านั้น จึง reuse instance ที่ warmup/preflight/worker/Python ไม่เหมาะสมได้ เพิ่ม guards และ POST ผ่าน worker จริง Fixture HTTP500, HTTP200 timeout, คำตอบจำนวนชั่วโมงผิด, validation false, wrong installation/Python, warmup/preflight fail และ worker ตาย ต้องไม่เปิด browser หรือ reuse แบบ ready

Readiness เป็น snapshot ของ source oracle ข้อเดียว พิสูจน์จริงว่าคำขอนี้ตอบถูก แต่ยังไม่ใช่ความถูกต้องของทุกคำถาม/current booking/LLM จึงคงงาน content/load/recovery แยกไว้

## 4. Windows PowerShell 5.1 กับ Python command quoting

โค้ด Python สำหรับตรวจ identity ใช้ double quoted literals ภายใน -c ซึ่ง PowerShell 5.1 native argument forwarding ทำเครื่องหมาย quote หาย ทั้งที่รันผ่าน PowerShell 7 ได้ เปลี่ยนเป็น single quoted Python literals แล้วทดสอบผ่าน powershell.exe จริง Path ที่มีช่องว่างไม่ถูกแยก และ explicit path ถูกส่งผ่านสามตัวเปิด

## 5. แยก environment/harness ออกจากบั๊กตอบคำถาม

Fixture รอบแรกสร้าง temp ใต้ AppContainer temp แล้วเขียนไฟล์ไม่ได้ เป็นปัญหาสิทธิ์ harness แก้ให้ใช้ test output root ที่เขียนได้ ไม่ใช่ chatbot ตอบผิด การเปิด sandbox r43.1 ผ่าน readiness แต่หลัง tool จบเชื่อม HTTP ไม่ได้ จึงเปิด r43.2/3 ผ่านระบบ permission แล้วตรวจซ้ำหลัง tool จบเพื่อยืนยัน process อยู่จริง

Git ใน sandbox อ่าน parent repository root ไม่ได้ เก็บ output fatal เดิมไว้ ใช้ read-only escalation แล้วตรวจ diff พบ blank EOF ในคู่มือที่เพิ่ม แก้เฉพาะ newline ก่อน freeze r43.3; Git status/diff-check สุดท้าย exit0

หน่วยความจำจริงระหว่างร43ใช้สูง 94–96% จึงเพิ่ม available physical/commit snapshot ใน health ไม่อ้างว่า Python 3.13 เป็นสาเหตุเดียว หรือ pin 3.12 แล้ว MemoryError ถูกแก้ถาวร

## ตัวอย่างคำตอบจริงของเคสที่แก้และเคสกัน regression

### en-week-0

คำถาม: What are the studio opening hours?

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-week-1

คำถาม: When is the studio open?

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-week-2

คำถาม: What is your opening timetable?

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-week-3

คำถาม: Please list opening hours for every day.

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-week-4

คำถาม: What is the service schedule?

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-week-5

คำถาม: What days are available?

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-week-6

คำถาม: What are the opening times?

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-week-7

คำถาม: Give me the complete opening schedule.

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-monday-Monday

คำถาม: Monday opening hours

Mode: pipeline:structured_schedule_en

Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-friday-Friday

คำถาม: Friday opening hours

Mode: pipeline:structured_schedule_en

Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-weekend-Saturday

คำถาม: Saturday opening hours

Mode: pipeline:structured_schedule_en

Saturday: no regular service period is listed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-weekend-Sunday

คำถาม: Sunday opening hours

Mode: pipeline:structured_schedule_en

Sunday: no regular service period is listed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-maintenance-Monday

คำถาม: Monday morning opening hours

Mode: pipeline:structured_schedule_en

Monday morning, 09:00-12:00, is a maintenance period and is not a regular play session.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-maintenance-Friday

คำถาม: Friday afternoon opening hours

Mode: pipeline:structured_schedule_en

Friday afternoon, 13:00-16:00, is a maintenance period and is not a regular play session.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-regular-date

คำถาม: What are the opening hours on 2026-10-05?

Mode: pipeline:structured_schedule_en

Monday, 05/10/2026: 09:00-12:00 is a maintenance period for equipment inspection and cleaning; play and booking are unavailable; 13:00-16:00 is open for play and booking.
System reference date: today is Tuesday, 06/10/2026 (Asia/Bangkok).
Thai calendar for this date:
No Thai public holiday or recorded calendar festival was found for this date.
Regular schedule details:
Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-all-week-after-price

คำถาม: PC prices for external users → Please list opening hours for every day.

Mode: pipeline:structured_schedule_en

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en-price-duration-after-price

คำถาม: PC prices for external users → all services 2 hours

Mode: pipeline:structured_service_fee_conversation

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
Requested duration: 120 minutes (2 hours); 2 session(s).
• PSU alumni / students from other institutions: 25 THB/package × 2 = 50 THB
• General adults: 70 THB/package × 2 = 140 THB

PlayStation 5 — 60 minutes/package (1-2 people)
Requested duration: 120 minutes (2 hours); 2 session(s).
• PSU alumni / students from other institutions: 50 THB/package × 2 = 100 THB
• General adults: 150 THB/package × 2 = 300 THB

Nintendo Switch — 60 minutes/package (1-2 people)
Requested duration: 120 minutes (2 hours); 2 session(s).
• PSU alumni / students from other institutions: 50 THB/package × 2 = 100 THB
• General adults: 140 THB/package × 2 = 280 THB

Nintendo Switch — 60 minutes/package (3-4 people)
Requested duration: 120 minutes (2 hours); 2 session(s).
• PSU alumni / students from other institutions: 100 THB/package × 2 = 200 THB
• General adults: 280 THB/package × 2 = 560 THB

Cockpit — 60 minutes/package (1 person)
Requested duration: 120 minutes (2 hours); 2 session(s).
• PSU alumni / students from other institutions: 65 THB/package × 2 = 130 THB
• General adults: 200 THB/package × 2 = 400 THB

VR — 60 minutes/package (1-5 people)
Requested duration: 120 minutes (2 hours); 2 session(s).
• PSU alumni / students from other institutions: 375 THB/package × 2 = 750 THB
• General adults: 1,050 THB/package × 2 = 2,100 THB
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
PC rates use the local update dated 2026-07-27.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
Source: local://service_fee/pc_price_update_20260727