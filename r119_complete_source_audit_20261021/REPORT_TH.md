# R119 ผลตรวจการย้ายข้อมูลเดิมเข้าสู่ Format กลาง

## ผลสรุป

ตรวจชุดต้นฉบับที่พบครบแล้ว และย้ายส่วนที่ตกหล่นพร้อมต่อตัวอ่านใน candidate R119 revision03 ข้อผิดพลาดเดิมหลายส่วนเกิดจากการแปลงข้อมูล/ความสัมพันธ์/ชื่อเรียกไม่ครบ และมีข้อมูลอยู่ใน native แล้วแต่ตัวอ่านไม่ใช้ ไม่ใช่เจ้าของยังไม่ได้ให้ข้อมูลทุกกรณี

**ยังไม่รับรองว่า Flow ตอบถูกทั้งหมด** ผลทดสอบคำถามเดิมดีขึ้น แต่ยังพบปัญหาเก็บบริบท เลือกหมวด และรวมกติกาบางกรณี รายงานนี้แยกความครบของข้อมูลออกจากคุณภาพคำตอบ ไม่ขอให้เจ้าของกรอกข้อมูลเดิมซ้ำเพื่อแก้ปัญหาที่ตัวอ่านหรือการตีเจตนา

candidate ยังไม่ได้ติดตั้งทับ R78/ระบบที่ใช้อยู่ ไม่ได้เปลี่ยน production data, approvals, releases, withdrawals หรือ log/result เดิม

## 1 ขอบเขตที่บังคับตรวจ

| รายการ | ผลตรวจ |
|---|---:|
| ไฟล์ข้อมูลใน candidate ที่มีคำตัดสินทุกไฟล์ | 502 |
| ไฟล์ต้นฉบับที่เก็บใน source registry และตรวจคืน byte ตรง | 488 |
| อีก 14 ไฟล์ | workload/intent 11 และ native runtime 3; คงไฟล์ไว้ แต่ไม่เป็น answer authority |
| canonical records | 270 |
| ค่าปลายทางของ JSON ที่ตรวจตาม pointer | 11,693 |
| active canonical roots / guard templates | 249 / 21 |
| เอกสาร/ไฟล์ประกอบ structured rows ที่ parse เพิ่ม | 229 ไฟล์ / 12,524 rows |
| โมดูล literal constants ที่ทำบัญชีแยก | 251 |
| actual Legacy checkout ที่เทียบแบบอ่านอย่างเดียว | 1,115 ไฟล์ |
| Word กติกาต้นฉบับ | 4 เอกสาร / 373/373 ย่อหน้าตรงกับ native rule text |
| Excel ราคาเหมา | 52 เซลล์มีค่า จาก 25,740 cell elements; ราคา 24/24 แถวตรงทั้ง workbook → curated → native |
| native records / fields / evidence refs | 806 / 6,428 / 4,454 |
| source snapshots ตรวจ hash | 3,001 |
| schema, source hash, pointer และ FK errors ที่เพิ่ม | 0 |
| source/operator/alias contracts | 743/743 |
| การเทียบค่าที่แปลงเป็น typed fields | 1,875 checks: 1,870 literal ตรง และ 5 รูปแบบ/ข้อความขยายที่ตรวจแยก |

จำนวนเซลล์ Excel ส่วนใหญ่เป็นเซลล์เปล่าที่มี formatting จึงไม่ใช้ 25,740 เป็นจำนวนข้อเท็จจริงทางธุรกิจ ส่วน Word ตรวจข้อความ body/table paragraphs ไม่ได้อ้างว่าตรวจ layout ของเอกสารใหม่

## 2 สิ่งที่เพิ่มและซ่อม

เพิ่ม native revisions แบบ append-only 310 ครั้ง กระทบ active roots ไม่ซ้ำ 291 รายการ; ฐานยังมี active roots 806 รายการเท่าเดิม ไม่สร้างเกมหรือเครื่องใหม่เพื่อกลบข้อมูลที่ไม่ทราบ

| ส่วนที่แก้ | จำนวน/ลักษณะ | เหตุผล |
|---|---|---|
| ต้นฉบับ canonical เต็มรายการ | legacy_context 249 roots | ไล่ตรวจค่าเดิมและ locale/provenance ได้ครบ; ไม่เอา raw context ไปแสดงเป็นคำตอบ |
| โซนที่ต้นฉบับระบุโดยตรง | 51 ช่องใน game/service; มี 53 field writes เพราะบางเกมรวมหลายแหล่ง | แก้ข้อผิดพลาดที่บังคับมี resource ก่อนจึงตอบโซนได้ |
| รูปแบบคำถามเดิม | legacy_search 73 roots | ใช้ช่วยเมื่อ typed reader ยังจับคำถามไม่ได้; ไม่แย่งตอบก่อนช่องตรง |
| ขอบเขตโปรไฟล์สาธารณะที่บันทึกไว้ | 25 คน | ย้ายสถานะเผยแพร่ของต้นฉบับ ไม่สร้าง approval หรือยืนยันตำแหน่งปัจจุบันแทนเจ้าของ |
| ค้นจากตำแหน่ง | role_aliases 22 คน | role → person ใช้คำเรียกเดิมได้ |
| สังกัด/ช่วงเวลาบุคลากร | เปิด reader ให้ค่าที่มีอยู่แล้ว 12/5 คน | ไม่อ้างว่าสร้างข้อมูลใหม่; เก็บคำแปลที่ใหม่กว่า |
| กฎคำนวณราคา | calculation_rule เติม 18 จาก 24 rates | คัดลอกกฎปัดรอบเฉพาะ service/group/amount/duration ที่ตรงต้นฉบับ |
| ตารางให้เล่น | service_slots/service_closed ครบ 7 วัน | แยกจากเวลาเปิดอาคารและสถานะจองจริง |
| คำบรรยายเกมต้นทางฉบับเต็ม | projection 31 เกม | ค่ามีใน native แล้ว ต่อ reader พร้อมวันที่บันทึกและ source scope |
| ช่วงผู้ใช้บริการ | projection 8 บริการ | ไม่แปลงเป็นจำนวนเล่นพร้อมกันโดยไม่มีหลักฐาน |
| aliases ที่เติมรวม | 311 รายการ = เดิม 183 + code aliases 128 | ชุดหลังมีอุปกรณ์ 91, โซน 24, เกม 13; ไม่ย้ายข้อความคำตอบลัดมาทับ business facts |
| alias ที่ชนกับ entity อื่น | 12 รายการไม่เติม | ไม่เลือก entity เดียวจากคำเรียกกำกวม |

17 กรณีคงค่า native ที่ใหม่กว่าไว้ เป็นข้อมูลบุคลากรที่มีค่าเดิมภาษาไทยพร้อมคำแปล/ข้อมูลเพิ่ม ไม่ใช่ 17 ข้อมูลที่ย้ายตกหล่น ดู RETAINED_VARIANTS_AND_LIMITS.json และ TYPED_VARIANT_DECISIONS.json

## 3 ผล API บนคำถามเดียวกัน

ใช้ 48 keys เดิมจากชุด Full ที่เคยเทส ไม่สร้างคำถามเพิ่มและไม่รัน Legacy baseline ใหม่ มี 164 grades แต่มีเพียง 62 positive literal/clause checks ใน 18 คำถาม จึงห้ามแปล 62/62 ว่าถูก 100% ของคำถามทั้งระบบ

ทดสอบ R119 สามรอบเพื่อแก้ปัญหาที่พบระหว่างตรวจ รวม 144 HTTP attempts แต่มีเพียง 48 คำถามไม่ซ้ำ รอบล่าสุดคือ revision03 แบบ LLM ON ไม่มีการส่ง category hint/expected answer เข้าแชท

Clock อ้างอิงของชุดนี้ตรึงตาม R118 ที่ 2026-10-21T12:00:00+07:00 จึงไม่ใช่การตรวจว่าเวลาที่กำลังอ่านรายงานศูนย์เปิดจริงหรือไม่

| รุ่น | Positive literal/clause | ข้อผ่าน positive ทุกแถว | Strict compatibility |
|---|---:|---:|---:|
| Legacy_R64_saved | 62/62 (100.00%) | 18/18 (100.00%) | 133/164 (81.10%) |
| R115_saved | 25/62 (40.32%) | 7/18 (38.89%) | 0/164 (0.00%) |
| R118_revision02_saved | 49/62 (79.03%) | 14/18 (77.78%) | 0/164 (0.00%) |
| R119_revision01 | 62/62 (100.00%) | 18/18 (100.00%) | 0/164 (0.00%) |
| R119_revision02 | 62/62 (100.00%) | 18/18 (100.00%) | 0/164 (0.00%) |
| R119_revision03 | 62/62 (100.00%) | 18/18 (100.00%) | 0/164 (0.00%) |

### แยกภาษา

| ภาษา | Legacy saved | R118 revision02 saved | R119 revision03 |
|---|---:|---:|---:|
| th | 25/25 (100.00%) | 17/25 (68.00%) | 25/25 (100.00%) |
| en | 36/36 (100.00%) | 31/36 (86.11%) | 36/36 (100.00%) |
| auto | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) |

Strict ยังมี route/mode/contract รุ่น Legacy รวมอยู่ด้วย ทุก grade ของ candidate ยังมี protocol mismatch จึงไม่ใช้ strict 0 เป็นหลักฐานว่าคำตอบเนื้อหาผิดทุกข้อ และไม่แก้ grader ให้เข้าข้าง candidate ส่วน positive เป็น literal checks ไม่ได้ตรวจความครบของคำตอบทุกมิติ

Legacy R64 กับ candidate ใช้ข้อมูลต่างรุ่น โดยเฉพาะข้อยืนยันเจ้าของ/หน่วยราคา/แปลภาษา จึงไม่ใช่ causal effect ของ Flow เพียงอย่างเดียว

### Transport และความถูกต้อง

- API ล่าสุด HTTP 200 ครบ 48/48; capture mismatch 0; ไม่มีคำตอบว่างหรือ API timeout ตาม flag ของ API
- Model transport: {'attempts': 55, 'transport_to_headers_ok': 55, 'transport_failures': 0}; เป็นสถานะการเชื่อมต่อถึง response headers ไม่ใช่ semantic score
- เวลา median 2.60 วินาที; สูงสุด 31.89 วินาที
- ตรวจ model name และ digest ต้น/ท้ายรอบ: scb10x/typhoon2.5-qwen3-4b:latest
- การสร้าง JSON/schema ผ่าน การตีเจตนาถูก การเลือกข้อมูลครบ และการตอบถูก เป็นคนละเกณฑ์กัน
- live provider ใน workload ถูกตั้ง unavailable เพื่อเทียบสถานการณ์เดิม ไม่ใช่ผลยืนยันว่าเครื่องจริงว่าง/ไม่ว่าง

## 4 เคสที่ยืนยันว่าดีขึ้นจากข้อมูลที่เติม

- Mario และ Little Nightmares II: อ่าน Nintendo Switch Zone จาก direct source relation ได้
- ประธาน: ค้นชื่อจากตำแหน่งได้ภายใต้ published-profile scope
- Kamlawan Nuansai: จับกับชื่อเรียกที่มีแหล่งเดิมและคนเดียว ไม่สร้างชื่อบุคคลใหม่
- ศุกร์บ่าย/จันทร์เช้า: ตอบไม่เปิดให้เล่นเพราะบำรุงรักษาตามตารางที่บันทึกไว้
- PS5 2 ชั่วโมง: ใช้กฎปัดรอบที่ถ่ายจาก calculator เดิม พร้อมหน่วย/ข้อยืนยันราคาล่าสุด
- Gaming Chair: revision02 เปลี่ยนกลับมาอ่าน location: PC Zone โดยตรง
- เมาส์ภาษาไทย: เติม aliases จากโค้ดเดิม และมี source contract ตรวจว่าคำถามพิมพ์ผิดเดิมเข้าถึง Gaming Mouse ได้; ดูผล HTTP revision03 รายข้อประกอบ

## 5 สิ่งที่ยังไม่จบที่ระดับคุณภาพคำตอบ

ข้อมูลครบในขอบเขตที่ตรวจไม่ได้แปลว่า reader/การตีเจตนาสมบูรณ์ทั้งหมด โดยเฉพาะราคาเกม การทิ้งบริบท AOV การรักษา duration ภาษาอังกฤษ และการรวมบทลงโทษหลาย clause ต้องอ่านผลล่าสุดและสาเหตุใน ROOT_CAUSE_REVIEW_TH.md

ไม่ควรขอให้เจ้าของตอบว่า Gaming Mouse มีหรือไม่ หรือส่งเอกสารกติกาใหม่ เพื่อแก้ปัญหาที่ระบบมีข้อมูลอยู่แล้วแต่เลือก/อ่านผิด ส่วนสิ่งที่ต้นฉบับไม่ยืนยันจริง เช่น physical video recording, unqualified game edition และ live occupancy ต้องคงขอบเขตไว้

## 6 หลักฐานและไฟล์อ่านต่อ

- [Flow และ mapping แบบละเอียด](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/FLOW_AND_MAPPING_TH.md>)
- [วิเคราะห์ปัญหาที่ยังพบและแนวทางแก้](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/ROOT_CAUSE_REVIEW_TH.md>)
- [canonical ทั้ง 270 รายการ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/ALL_RECORDS_CHECKLIST_TH.md>)
- [ไฟล์ข้อมูลทั้ง 502 ไฟล์](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/ALL_FILES_CHECKLIST_TH.md>)
- [คำถาม คำตอบ แผน และหลักฐานทุกข้อ](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/http03/analysis/CASEBOOK_TH.md>)
- [ผลตรวจข้อมูลและอ้างอิง](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/FULL_AUDIT_GATE.json>)
- [เทียบ Word ต้นฉบับทุกย่อหน้า](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/PRIMARY_DOCX_AUDIT.json>)
- [เทียบราคาเหมา workbook กับ native](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/RENTAL_WORKBOOK_PRICE_AUDIT.json>)
- [aliases ในโค้ดเดิมที่ย้าย/ไม่ย้ายพร้อมเหตุผล](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/CODE_ALIAS_MIGRATION.json>)
- [ตรวจ revisions/sources/approvals/withdrawals เดิม](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r119_complete_source_audit_20261021/PRESERVED_STATE_GATE.json>)

## 7 ข้อสรุปเรื่องความครบ

ครบในความหมายว่าไฟล์/record/ค่าต้นฉบับที่อยู่ในขอบเขตตรวจมีบัญชีครบ เก็บต้นฉบับได้ตรง ย้ายค่าธุรกิจที่แปลงได้อย่างมีหลักฐาน และเปิดตัวอ่านส่วนที่ระบุในรายงานแล้ว ไม่มีข้อผิดพลาดด้าน schema/evidence เพิ่ม ไม่ใช่คำรับรองว่าทุกข้อความจาก cache เป็น business authority หรือทุกคำถามเข้า Flow ถูก 100%

21 guard templates, 12 aliases ที่ชน entity อื่น, ข้อความ cache ที่ไม่มีหลักฐานธุรกิจอิสระ และ Minecraft ที่ไม่มี native business entity ไม่ถูกนำมาแต่งเป็นรายการบริการใหม่ ต้นฉบับเหล่านี้ยังคงอยู่และมีเหตุผลกำกับครบ
