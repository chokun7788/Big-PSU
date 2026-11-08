# R78 — ตรวจโมเดล บทสนทนา และซ่อมจาก log

เริ่มงานจากคำขอให้ทำทั้ง 3 ลำดับ วันที่ 16 ตุลาคม 2026 และตรวจต่อหลังเที่ยงคืนวันที่ 17 ตุลาคม 2026 เวลาไทย เก็บชื่อโฟลเดอร์เดิมของรอบไว้

## 1. ลำดับทำงานและผล

1. ขอสิทธิ์เชื่อมต่อผ่านระบบ → ผล network=null ไม่ได้รับสิทธิ์เพิ่ม
2. ตรวจ local model /api/tags → URLError/WinError 10013 ไม่ได้รายชื่อโมเดลหรือผล generation
3. ทดลอง launcher R77 แบบไม่เปิด browser → health ที่พอร์ต 8113 ถูกปฏิเสธด้วย error เดียวกัน; ตรวจภายหลังไม่พบ process ที่ launcher สร้างกำลังรัน ห้ามสรุปว่าผู้ใช้เปิดเว็บได้/ไม่ได้จากข้อมูลนี้ และห้ามอ้างว่า bind ล้มโดยไม่มี log ยืนยัน
4. ตรวจ actual HTTP handler/session store ภายใน process กับ common DB จริง เปิด LLM และไม่มี model mock → เก็บทุก request/response/state/trace ในโฟลเดอร์รอบใหม่
5. แยก protocol mismatch ของตัวตรวจออกจาก content failures → ทบทวน saved baseline โดยไม่ส่ง request ซ้ำ
6. คัดลอก system+DB จาก R77 เป็น R78 แล้วแก้โค้ดเฉพาะสาเหตุที่พิสูจน์ได้
7. ทดสอบบทสนทนาเดิม + variants ไทย/อังกฤษ → ตรวจ source projection, unknown, negation, validity และ state
8. ตรวจ regression ที่เกี่ยวข้อง, ข้อมูลเดิม/ไฟล์เดิม, syntax และเอกสาร แล้วสรุปส่วนที่ยังขาด

ไม่มีการใช้ browser/ช่องทางอื่นเพื่อข้ามการเชื่อมต่อที่ไม่ได้รับสิทธิ์ ไม่มีการรัน legacy/OFF/full ชุดใหญ่

## 2. ปัญหาคำถามต่อสั้น

### ก่อนแก้

หลังตอบกฎอุปกรณ์ส่วนตัวแล้ว `And my mouse?` อ่าน source ได้แต่ contract ยังถือ my mouse เป็น unresolved clause จึงถูก validation ปฏิเสธ ส่วน `คีย์บอร์ดด้วยได้ไหม` fuzzy match หลุดไป FAQ เบอร์โทร

### Flow ใหม่

1. รับเฉพาะ latest delivered assistant state ที่ server เชื่อถือ
2. คำตอบจาก declared query_profile เก็บ profile_read_scope = record_id + fingerprint ของ kind/profile ไม่มีข้อความคำตอบเก่า
3. ต้องมี follow-up framing ที่รองรับ เช่น And/What about/แล้ว หรือ ด้วยได้ไหม/ล่ะ
4. ต้องมีชื่อ subject ที่มีอยู่ใน metadata คำถามใหม่เต็ม ๆ ไม่ถูกบังคับเข้า flow นี้
5. ตรวจ fingerprint/withdraw/current scope
6. เรียก scope_plan ร่วมกับ R77 ตรวจ ownership/context/subject และข้อความเงื่อนไขที่เหลือ
7. ตรง source เดียว → DEFAULT_FIELDS จาก revision ปัจจุบัน; หลาย/ไม่ตรง/มีเงื่อนไขที่ยังไม่รู้ → clarification/unconfirmed

`And my wireless mouse?` ยังไม่ยืนยัน เพราะ wireless ไม่ถูกตัดทิ้ง ส่วน `And when?` ไม่มี subject จึงไป flow เลือก field เดิมตามปกติ

## 3. ปัญหาถามเกมหลังคำถามแข่งขัน

### ก่อนแก้

R77 ถามว่าใช้แข่งเกม/รายการไหน แต่ไม่ได้เก็บความต้องการเดิมแบบ typed เมื่อผู้ใช้ตอบ VALORANT จึงกลับไปอธิบายตัวเกม

### Flow ใหม่

1. เมื่อ qualifier มี context=competition แต่ไม่มี profile ตรง เก็บ pending_competition_scope: version, origin record_id/fingerprint, ownership/context/subjects
2. คำตอบถัดไปต้องตรงชื่อ/alias ของเกมหรือรายการที่มีข้อมูลจริง ไม่ใช้ fuzzy guess ใน flow นี้
3. ตรวจ game_id → competition จากข้อมูลปัจจุบัน
4. สร้างคำค้นกติกาด้วยชื่อเกมที่ผู้ใช้พิมพ์ + subject/ownership ที่เก็บไว้ แล้วส่งเข้า dispatcher กติกาปกติ โดยไม่ส่ง assistant prose เป็น facts
5. อ่าน source competition_rule และเก็บ audit method=qualified_competition_game_selection
6. ถ้า scope เปลี่ยนให้ expired; ถ้าเป็นคำถามใหม่ เช่นวิธีชำระ ให้ใช้ dispatcher ปกติ

ไม่ได้สร้างนโยบาย personal keyboard ใหม่สำหรับการแข่งขัน กฎที่ตอบใน VALORANT มาจาก section อุปกรณ์ของกติกาเดิม ซึ่งระบุอุปกรณ์ที่นำมาเองได้และข้อห้ามอื่น ไม่ใช้คำห้ามของการใช้บริการทั่วไปแทน

## 4. ปัญหาราคา → ทั้งหมด → PC

### ก่อนแก้

คำถามราคาที่ไม่มีชื่อบริการไม่สร้าง typed pending สำหรับถามต่อ `ทั้งหมด` จึงไม่มีขอบเขตให้สืบทอด ต่อมาแม้ PC อาจค้นราคาได้ แต่บริบทคำถามแรกหาย

### Flow ใหม่

1. ถามราคาที่ไม่ระบุ service/resource/zone/game/rate → สร้าง price_scope_request
2. สร้างตัวเลือกจาก rate.service_id จริง ไม่เขียนชื่ออุปกรณ์/ราคาใน router
3. เก็บ audience เฉพาะที่ resolver ยืนยันตรงข้อมูล; คำว่าบุคคลภายนอก/visitors ไม่ถูกบังคับให้เท่ากับ General Adult
4. รับชื่อบริการ/zone/resource แบบตรง หรือ ทั้งหมด/all
5. ทั้งหมดครอบคลุมทุก service ที่มีอัตราบันทึก แม้ rate หมดช่วงมีผลแล้ว ใช้ renderer เดิมระบุ not_current พร้อมช่วงวันที่ และไม่แสดงราคาเก่าเป็นราคาปัจจุบัน
6. เก็บ requested_fields=amount_minor เพื่อให้ PC รอบถัดไปยังเป็นการถามราคา
7. ถ้ายังไม่ระบุกลุ่ม แสดงแยกแต่ละกลุ่ม ไม่เลือกกลุ่มให้เอง

ระหว่างรอบแรกพบการเลือกเฉพาะ rate ที่ effective ทำให้เมนูเหลือ PC จึงเปลี่ยนการสร้างรายการเป็นทุกอัตราที่บันทึก และให้ validity guard เดิมตัดสินการตอบแต่ละรายการ

## 5. การทบทวน Flow ระหว่างทำ

| รอบ | สิ่งที่พบ | สิ่งที่ทำ |
|---|---|---|
| baseline | ข้อผิดจริง 5/29; protocol mismatch 4 ข้อในคะแนน raw | เก็บ raw, regrade saved responses, ระบุสาเหตุแยกกัน |
| repair01 | ประวัติ subject/competition ดีขึ้น; ทั้งหมดตกหล่นบริการที่ rate หมดอายุ | แก้รายการให้ครบ พร้อมรักษา validity guard |
| repair02 | 38/38 ในขอบเขตที่ตรวจ | ตรวจเนื้อหาตัวอย่างจริง พบคำตอบกติกา/ราคายังยาว จดเป็น quality limitation |
| state guard review | raw names ต่างจาก derived names ที่ caller ใช้ ทำให้ guard test PC false failure | แก้ setup ตัวตรวจให้ตรง caller; เก็บผลเดิม 13/14 และผลทบทวน 14/14 |

## 6. เกณฑ์ส่งต่อรอบนี้

- source DB และ R77 system เดิมไม่เปลี่ยน
- โมเดลจริงและเว็บ TCP ยังถือไม่ยืนยัน ไม่ใช้คะแนนภายในแทน
- ผล targeted ผ่านทุกข้อที่รายงาน แต่ไม่อ้างว่า format กลางครอบคลุมทุกหมวดหรือทุกสำนวนแล้ว
- ไม่เปลี่ยนวันที่มีผล ราคา นโยบาย หรือสถานะ approvals เพื่อให้คะแนนผ่าน
