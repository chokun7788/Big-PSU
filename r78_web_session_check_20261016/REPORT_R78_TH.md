# รายงาน R78 — ผลทำงานตาม 3 ลำดับ

## สถานะสำคัญ

| ลำดับที่อนุญาต | ผลจริง |
|---|---|
| เปิด R77 และตรวจโมเดลจริง | ทดลองแล้ว ยังยืนยันการเปิดเว็บ/เรียกโมเดลไม่ได้: WinError 10013; ขอสิทธิ์ผ่านระบบแล้ว network=null |
| ทดลองบทสนทนาไทย/อังกฤษพร้อมดู log | ทำผ่าน HTTP handler/session store จริงภายใน process กับฐานจริง เปิด LLM ไม่มี model mock; ยังไม่ใช่ browser/TCP |
| แก้สาเหตุและตรวจซ้ำ | แก้ใน R78 แยกจาก R77; บทสนทนารอบสุดท้าย 38/38 และ regression ที่เกี่ยวข้องผ่าน |

ไม่ได้ติดป้ายว่างานตรวจเว็บจริงเสร็จ เพราะการเชื่อมต่อยังไม่ผ่าน การตรวจภายในช่วยพบและแก้บั๊กที่พิสูจน์ได้ระหว่างที่ส่วนนี้ติดข้อจำกัด

## 1. โมเดลและการเปิดเว็บ

MODEL_PREFLIGHT.json บันทึกการเรียก http://127.0.0.1:11434/api/tags ล้มด้วย URLError / WinError 10013 จึงไม่มีหลักฐาน transport สำเร็จหรือ generation สำเร็จ

R77_STARTUP_STATUS.json และ R77_STARTUP.log บันทึกว่า launcher ไม่ผ่าน health ที่ 127.0.0.1:8113 เพราะ socket permissions เช่นกัน ตรวจ process ที่ launcher สร้างหลังจบแล้วไม่พบว่ากำลังรัน stdout/stderr ไม่มีข้อมูลยืนยันสาเหตุเพิ่มเติม จึงไม่วินิจฉัยว่า Ollama เสีย โมเดลไม่มี หรือ server bind ล้มโดยเดา

ได้เรียกขอสิทธิ์ network ผ่านระบบ ผล network=null ไม่ได้รับสิทธิ์เพิ่ม ไม่ใช้ browser/ช่องทางอื่นเลี่ยงข้อจำกัด ไม่เปิดพอร์ตโมเดลออกภายนอกหรือปิดระบบป้องกันเครื่อง

MODEL_HEALTH ของ baseline02/repair01/repair02 และ regression แสดง actual model attempts ล้มด้วย error เดียวกันและไม่มี success บางคำตอบทำงานได้จากเส้นทาง deterministic/source จึงไม่ใช้การตั้ง LLM ON เป็นหลักฐานว่าโมเดลตอบถูก

## 2. ปัญหาที่พบและแก้

### A. Follow-up เปลี่ยนอุปกรณ์ หลุดจาก profile

ตัวอย่าง:

- Can I bring my own input peripheral? → Yes, but it is my own keyboard. → **And my mouse?**
- ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม → ใช่ แต่เป็นเมาส์ของผม → **คีย์บอร์ดด้วยได้ไหม**

ก่อนแก้: EN ใช้ method typed_common_state:pending_fields อ่าน source ถูกแต่ coverage ยังเหลือ my mouse เป็น unresolved_query_clause จึงถูก validation ปฏิเสธ TH fuzzy match ไป FAQ เบอร์โทร ทำให้ขอรายละเอียดคนละหัวข้อ

ควรตอบ: source เดิมระบุไม่อนุญาตคีย์บอร์ด/เมาส์ส่วนตัวในการใช้บริการทั่วไป จึงตอบกฎนี้ได้เมื่อคำถามต่อยังตรง subject/ownership/context โดยไม่ต้องให้ผู้ใช้พิมพ์ประโยคเต็มใหม่

แก้: เก็บ profile_read_scope เป็น ID+fingerprint ใน state ที่ server ส่ง แล้วตรวจ follow-up ที่มีชื่อ subject ด้วย scope_plan เดิม หากเปลี่ยนเจ้าของ/เพิ่ม wireless ที่ยังไม่ครอบคลุม จะไม่ยืนยันกฎเดิมแทน

### B. ถามเกม/รายการแข่งแล้วไม่ใช้คำตอบเลือกของผู้ใช้

ก่อนแก้: ใช่ แต่ใช้ตอนแข่ง → บอทถามเกม/รายการ → VALORANT → กลับไปอธิบาย summary ของเกม

ควรตอบ: ค้นกติกาอุปกรณ์ของรายการ VALORANT ตามความต้องการเดิม ไม่ตอบคำห้ามอุปกรณ์ส่วนตัวของการใช้บริการทั่วไป

แก้: pending_competition_scope เก็บ scope เดิมพร้อม fingerprint เลือกเกม/รายการด้วย metadata ปัจจุบัน แล้วอ่าน competition_rule ผ่าน dispatcher เดิม ผลตัวอย่างอ่านส่วนอุปกรณ์ที่นำมาเองได้ ข้อห้ามมาโคร/ติดตั้งโปรแกรม และเงื่อนไขเจ้าหน้าที่จากต้นฉบับ ไม่มีการแต่งกฎใหม่

### C. ราคาที่ไม่มีชื่อบริการไม่มี pending ที่ใช้ต่อได้

ก่อนแก้: ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก → ไม่ตรงข้อมูล → ทั้งหมด → ไม่ตรงข้อมูล รอบ PC ถัดไปค้นได้แต่ไม่ได้เกิดจาก flow เลือกที่ครบถ้วน

แก้: สร้าง price_scope_request จาก FK rate.service_id; ตอบชื่อบริการหรือทั้งหมด/all ได้ และ PC ถัดไปยังอ่าน field ราคา กลุ่มผู้ใช้แสดงแยก ไม่แปลงบุคคลภายนอกเป็น General Adult โดยเดา

### D. รายการทั้งหมดตกหล่นเพราะกรองอัตราหมดอายุเร็วเกินไป

ใน repair01 เมนูราคาเหลือ PC เพราะอัตราอีก 18 รายการมี validity ที่บันทึก 2026-02-01 ถึงก่อน 2026-04-01 ซึ่งผ่านช่วงนั้นแล้ว ณ เวลาทดสอบ ทั้ง 18 คือ Nintendo 6, PS5 3, Cockpit 3, VR 6 ตามกลุ่มผู้ใช้ ส่วน PC 6 รายการมี validity unknown

แก้รายการเลือกให้มองเห็นครบ 8 service options และ 24 rate records แต่ renderer ยังป้องกันอัตราที่ไม่ current: แสดงบริการ/กลุ่ม/ช่วงวันที่และแจ้งยังยืนยันราคาปัจจุบันไม่ได้ ไม่แสดงจำนวนเงินเก่าเป็นราคาปัจจุบัน ส่วน PC ยังคงคำอธิบายว่าต้นฉบับไม่ระบุช่วงมีผล

ไม่ได้แก้วันหมดอายุหรือยืดอัตราเอง ไม่สามารถรับรองราคาปัจจุบันทั้ง 24 รายการจากข้อมูลชุดนี้ได้

## 3. คะแนน การทบทวน oracle และผลแต่ละรอบ

| ชุด | ผล | ข้อสรุป |
|---|---|---|
| baseline01 | หยุดก่อนส่ง request | ตัวตรวจคาดโครงสร้าง CommonStore.snapshot ผิด; เป็น setup error ไม่ใช่ chatbot error |
| baseline02 raw | 20/29 | รวม false failures จากตัวตรวจอ้างช่อง hits ซึ่งเป็นชื่อภายใน ไม่ใช่ public API |
| baseline02 reviewed | 24/29 | แก้การอ่าน query_plan/response_projection จาก saved response; protocol mismatch 4 ข้อ และ content failures จริง 5 ข้อ |
| repair01 | 28/29 | follow-up/profile/competition/price pending ดีขึ้น; all ยังไม่ครบเพราะ effective filter |
| repair02 | 38/38 | 29 turn เดิมผ่าน 29/29 และเพิ่ม EN price, EN competition, wireless follow-up รวมอีก 9 turn |
| qualification_regression01 | 41/41 | qualified reply/state/update/withdraw เดิมผ่าน; controlled model-unavailable suite |
| regression01 | 43/43 | source contracts ผ่าน dispatcher; real model attempts ยัง transport failure |
| scope01 | 50/50 | scope/unknown/source guard เดิมผ่าน |
| SCOPE_GUARDS raw/reviewed | 13/14 → 14/14 | ตัวตรวจ PC ใช้ raw names ต่างจาก derived names ของ caller; แก้ setup ให้ตรง ไม่แก้โค้ดแอปเพื่อผ่านข้อทดสอบนี้ |

ห้ามรวมชุดที่มีเคสซ้ำเป็น unique requests หรือ global accuracy 38/38 เป็นสัญญาที่ตั้งไว้สำหรับบทสนทนาจำนวนเล็กน้อย มีทั้งคำตอบจริง การถามเพิ่ม และ unknown ไม่ใช่ผล full test หรือผลตัดสินทุกคำในคำตอบ

baseline02/TURNS.jsonl, raw summaries, repair01 และ guard raw ยังเก็บอยู่ทุกไฟล์ การ regrade ไม่ส่ง request ใหม่ และไม่เขียนทับ log เดิม ดู BASELINE_ORACLE_REVIEW.json

ตัวรับ HTTP และ session persistence ถูกเรียกจริง แต่ request/response ใช้ bytes ใน memory ไม่มี TCP/browser จริง การวัด seconds_internal_only จึงเป็นเวลาเฉพาะทางเดินภายในขณะโมเดลล้มและอาจมีการตรวจอื่นรันพร้อมกัน ใช้เป็น latency ของผู้ใช้หรือจำนวนผู้ใช้สูงสุดไม่ได้

## 4. ขอบเขตและไฟล์ที่แก้

สำเนา R78: system/app/knowledge/common/answer.py, dialogue.py, followup_scope.py (ใหม่), system/app/pipeline/migrated_chat.py

ใช้ metadata เดิม ไม่เพิ่ม aliases ของประโยคหรือ record ID จริงใน router ผล source DB, snapshots, revisions, audit, approvals เหมือน R77; ไม่มี fixtures ในฐานของเว็บ ข้อมูลตัวอย่าง qualification regression อยู่ verification แยกตามรอบ

DELIVERY_QA_FINAL.json: source R77 1,426 ไฟล์ตาม manifest ไม่เปลี่ยน; logical tables เท่ากัน; heads=602; approvals=0; common releases=0; source/copy SHA256 เดียวกัน:

`4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d`

R77 runtime มีเฉพาะ log/ข้อมูล process ใหม่จากการลองเปิดที่ได้รับอนุญาต ไม่ทับ log เก่าหรือเปลี่ยน R77 system ใหม่

## 5. สิ่งที่ยังเหลือ

### ทำเองต่อได้

1. ย่อการแสดงผลโดยคงเนื้อหาที่จำเป็น: ตัวอย่างกติกา VALORANT ยังมี source sections TH/EN ซ้ำและส่วนอุปกรณ์อิเล็กทรอนิกส์ที่กว้างกว่าคีย์บอร์ด/เมาส์ TH 3,625 ตัวอักษร EN 3,792; ตัวอย่างราคาทั้งหมด TH 6,649 EN 6,995 ตัวอักษร เพราะแจ้ง validity ซ้ำตาม rate/group ทุกบรรทัด ยังไม่ใช่ content failure ในสัญญาปัจจุบัน แต่ usability ยังควรปรับ
2. เพิ่ม definition/typed constraints และ profile coverage ตาม NEXT_STEPS_R77_TH.md ปัจจุบัน profile known จริงยัง 2 records การเพิ่มข้อมูลใหม่ทุกหมวดจึงยังไม่รับรองทุกสำนวน
3. ขยายการเลือกเกมหลังถามแข่งขันที่เป็น typo/หลายตัวเลือก และ qualification หลังเมนูชนิดอื่น การซ่อมรอบนี้รับ exact names/aliases ของข้อมูลจริงเพื่อไม่เดาหัวข้อ
4. ตรวจ contradiction และ source consistency ของวันที่ราคา โดยย้อน provenance ก่อนขอเจ้าของ หากหลักฐานต้นทางยืนยันวันที่ใหม่จึงย้ายข้อมูลผ่าน revision ได้

### ยังยืนยันไม่ได้ในรอบนี้

- real model transport/generation/semantic equivalence/latency และ browser/TCP หลัง restart เนื่องจากข้อจำกัดการเชื่อมต่อที่ตรวจพบ
- WordPress สดและ concurrent load ไม่มีการตรวจใหม่ในรอบนี้ ไม่ลบผลยืนยัน live booking เดิมของผู้ใช้
- R78 ยัง draft preview ใช้ runtime R69 ไม่ใช่ portable release และไม่แทนเว็บเดิมอัตโนมัติ

### ข้อมูลที่อาจต้องเจ้าของตัดสินใจหลังตรวจ provenance

- อัตรา Nintendo/PS5/Cockpit/VR ทั้ง 18 แถวที่สิ้นสุดก่อน 1 เม.ย. 2026 ยังใช้ต่อหรือไม่? ถ้าใช้/เปลี่ยน ขอวันที่เริ่มใช้และสิ้นสุด พร้อมราคาต่อ service/กลุ่มผู้ใช้ที่เปลี่ยน
- อัตรา PC 6 แถวที่ไม่มีช่วงมีผล ใช้ตั้งแต่เมื่อไรและยังเป็นราคาปัจจุบันหรือไม่?
- คำว่า “บุคคลภายนอก” ในการแจ้งราคา ต้องแยกนักเรียน/ศิษย์เก่ากับบุคคลทั่วไปตาม 3 audience records เดิมอย่างไร? ระหว่างยังไม่ยืนยัน ระบบแสดงแต่ละกลุ่มแยกกัน

ไม่เปิดถามเรื่องที่ผู้ใช้ยืนยันแล้ว เช่น noon booking, VR occupancy และผลตรวจ live booking/อังกฤษเดิมซ้ำ

## 6. เปิดชุดแก้

อ่าน README_R78_TH.md โฟลเดอร์นี้มี Open-New-Chat.cmd สำหรับพอร์ต 8115 และ editor 8116 ยังไม่ได้อ้างว่าเปิดสองพอร์ตนี้ผ่านแล้ว เพราะข้อจำกัดเดิม การเปิดเว็บก่อนหน้าจะไม่ได้รับ R78 อัตโนมัติ
