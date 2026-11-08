# ผลแก้การรอโมเดลเลือกข้อมูล — R81

## สรุป

แก้บนแชท R78 พอร์ต 8115 เดิม โดยคง LLM ON และการแก้คำตอบเปิด–ปิด R80 ไว้ครบ ลดการเรียกโมเดลในกรณีที่ต้องถามยืนยันหัวข้ออยู่แล้ว เพิ่มข้อมูลวัดเวลา และแยก timeout จากปัญหาเชื่อมต่อ

ชุดตรวจที่เกี่ยวข้องผ่าน **115/115 ข้อตรวจ** ไม่ใช่ 115 คำถามไม่ซ้ำ และไม่ใช่คะแนนความแม่นยำของ LLM จริง ตัวช่วยตรวจ HTTP จาก Windows พร้อมใช้ แต่ยังไม่ได้เก็บผลจริงหลังเปลี่ยนโค้ด เพราะเครื่องมือในแชทถูกปฏิเสธ loopback ด้วย WinError 10013

## 1. หลักฐานเดิมและเหตุที่ผล “ผ่าน” ไม่ได้แปลว่าหายทุกปัญหา

ผลผู้ใช้รอบ `r79_connection_diagnostics_20261017/user_results/20261017T064224Z-0f14c1`:

| ส่วน | ผลจริง | สิ่งที่พิสูจน์ได้ |
|---|---|---|
| Ollama รายชื่อโมเดล | HTTP 200 | ติดต่อบริการและอ่านรายการได้ |
| ขอคำว่า READY | HTTP 200, done=true, READY, 6.953 วินาที | โมเดลสร้างข้อความได้ในคำขอนี้ |
| เวลาโหลดในคำขอ READY | 6.657 วินาที | คำขอ READY นี้เสียเวลาส่วนใหญ่ในการโหลด |
| คำถาม input peripheral | HTTP 200 ประมาณ 7.154 วินาที | เว็บตอบกลับได้ แต่ selector เกิด TimeoutError |
| คำตอบของคำถามแรก | ถามว่าหมายถึงคีย์บอร์ด/เมาส์ใช่ไหม | เป็น fallback ยืนยันหัวข้อ ไม่ใช่หลักฐานว่าโมเดลเลือกหัวข้อถูก |
| ข้อความยืนยันและถามต่อ | ตอบข้อห้ามจากข้อมูลต้นทางได้ | บทสนทนาตัวอย่างอ่านข้อมูลต่อได้ ไม่ได้พิสูจน์ทุกคำถาม |

READY และ selector เป็นคนละคำขอ ความยาว prompt/รูปแบบผลลัพธ์ต่างกัน จึงยังยืนยันไม่ได้ว่า timeout ของ selector เกิดจากโหลดโมเดล RAM GPU หรือคิวส่วนใด ไม่เอาเวลา READY ไปใช้เป็นเวลาตอบปกติของแชท

## 2. สาเหตุใน Flow ที่ยืนยันจากโค้ด

เดิม unnamed question → หา candidate → ล็อกโมเดล/รอคิว → ให้โมเดลคืน indices + semantic binding → หากเป็น declared profile ยังต้องถามยืนยันหัวข้อ → ผู้ใช้ยืนยัน → อ่านข้อมูลจริง

กรณี query profile ที่ต้องยืนยัน จึงมีค่าใช้จ่ายในการเรียกโมเดลก่อนหน้าคำตอบยืนยัน ทั้งที่การผ่าน binding ก็ยังไม่อนุญาตให้ตอบข้อเท็จจริงตรง ๆ อยู่ดี เหตุผลที่ยังต้องยืนยันคือข้อความอ้างอิงตรงกับคำถามไม่ได้พิสูจน์ว่าความหมายเท่ากัน เช่น proof of identity ไม่ใช่ proof of payment

## 3. สิ่งที่แก้

### 3.1 ข้ามเฉพาะงานโมเดลที่ไม่จำเป็น

เพิ่ม `prefer_profile_confirmation` เฉพาะ CommonAnswerer ของคำถามที่ยังไม่ระบุรายการ หาก candidate **ทุกตัว** เป็น declared profile และเข้าเงื่อนไข task/context/ownership จะไปถามยืนยันทันที ไม่แตะ model lock/admission/HTTP

ยังไม่ถือว่าระบบพิสูจน์ความหมายแล้ว ไม่ใส่ transport_ok/schema_accepted เป็นผลสำเร็จปลอม ไม่ตอบเนื้อหานโยบายจากการคาดเดา การเลือกหัวข้อ/ตอบใช่ยังตรวจ state/fingerprint/revision/เงื่อนไขเดิม

ตัวเลือกปกติที่ปะปนกับ profile, profile ที่ไม่เข้าเงื่อนไข, scoped lookup และการเรียก selector ปกติยังใช้โมเดลตามเดิม ไม่ได้ปิด LLM ทั้งระบบ

### 3.2 แยกเวลาและความผิดพลาด

เพิ่มใน audit ของ entity_selection:

- `timing_ms`: retrieval, model_work_wait, admission_wait, http_wait_and_read, total
- `model_request`: เพดาน/timeout ที่เหลือจริง ขนาด payload, num_ctx, num_predict
- `model_metrics`: load/prompt_eval/eval/total จาก Ollama เมื่อมี response โดยแปลง nanoseconds เป็น milliseconds และเก็บ token counts
- `availability_failure`: timeout, transport, schema, busy, model_gate หรือ deadline ตามหลักฐาน

ฟิลด์ที่โมเดลไม่ส่งกลับยังเป็น “ไม่มีข้อมูล” ไม่เติมศูนย์ ไม่ใช้ความเร็วหรือ HTTP 200 มาอ้างว่าคำตอบถูก semantic rejection ยังคงแยกจาก schema failure

### 3.3 ตรวจ budget หลังรอคิว

ตรวจเวลาที่เหลืออีกครั้งก่อนส่ง HTTP ถ้าหมดเวลาแล้วไม่เรียกด้วย timeout=0 และคืน gate/lock เสมอ คง cap HTTP 6 วินาที num_ctx 3072 และ num_predict 70/420 ตามเส้นทางเดิม ไม่เพิ่มเพดานเพื่อกลบปัญหา

### 3.4 ข้อความตอบกลับเมื่อหมดเวลา

กรณีไม่มีหัวข้อ fallback ที่เหมาะสมและเกิด timeout จะบอกว่าโมเดลใช้เวลาเกินกำหนด ให้ระบุหัวข้อหรือลองอีกครั้ง แยกจาก “เชื่อมต่อโมเดลไม่ได้” ทั้งไทยและอังกฤษ

## 4. ภาษาไทยที่ยังมีข้อจำกัด

คำถาม `ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม` ดึง candidate 8 รายการ ได้แก่ profile คีย์บอร์ด/เมาส์ นโยบายไฟ/ปลั๊ก นโยบายอุปกรณ์ และข้อมูลเกมหลายตัว ชุดนี้มีทั้ง profile และรายการทั่วไป จึงไม่เข้า shortcut

คะแนน candidate ตัวอย่าง .4893, .4945 เป็นคะแนนการทับซ้อนอักษรแบบถ่วงน้ำหนัก ไม่ใช่โอกาสที่คำตอบถูก หรือ confidence ที่ผ่านการสอบเทียบ การดึงข้อมูลเกมเข้ามาไม่แปลว่าเกมนั้นตอบคำถามได้

payload ของกรณีไทยที่ทดสอบประมาณ **19,796 bytes** และใช้โปรโตคอล profile ที่มีเพดานสร้างผล 420 tokens ซึ่งมากกว่าการคืน indices ธรรมดา แต่ bytes ไม่เท่ากับ tokens และยังไม่มี token count จริงของ selector ที่ timeout จึงไม่อ้างว่า context ล้นแน่นอน

คำถามไทย `แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง` มี candidate 6 รายการปะปนเช่นกัน ยังต้องดูเวลาจริงและผลของ model selector ต่อ การตัดรายการจากเพียงคะแนนอักษรอย่างเดียวอาจทำให้ข้อมูลที่ควรตอบหลุด จึงยังไม่ลด candidate โดยเดา

## 5. ผลทดสอบอัตโนมัติ

| ชุด | ผล | วิธี/ขอบเขต |
|---|---:|---|
| selector + timeout + budget + คืนคิว | 22/22 | controlled model transport/envelope, ข้อมูลจริงอ่านอย่างเดียว |
| ยืนยันพร้อมเงื่อนไขเพิ่ม | 41/41 | isolated source fixtures, dispatcher และ handler ในหน่วยความจำ |
| ปฏิเสธ/เปลี่ยนเรื่อง/ถามต่อ | 34/34 | isolated source fixtures, dispatcher และ handler ในหน่วยความจำ |
| วันนี้/พรุ่งนี้/วันเฉพาะ/วันปิด/ข้ามเที่ยงคืนไทย | 18/18 | frozen clock, ข้อมูลจริง, คงผล R80 |
| รวมชุดที่เกี่ยวข้อง | **115/115** | ไม่ใช่ full test หรือการวัดความแม่นยำโมเดลจริง |
| ตัวช่วย HTTP/identity/fingerprint/LLM ON | 14/14 | offline contract QA ไม่เรียก network |
| ตัวช่วย restart | parse errors 0 | ตรวจไวยากรณ์ PowerShell ยังไม่รันหยุด/เปิดบริการจากเครื่องมือ |

Baseline แบบควบคุม 2/2 ยืนยันว่าก่อนแก้ คำถาม input peripheral เรียกโมเดลก่อน fallback; ไม่ใช้เวลา mock เทียบเป็น speedup จริง

ระหว่างตรวจพบความผิดพลาดใน test fixture และเก็บไว้ครบ: candidate_1/candidate_3 ใช้ assertion ว่าทุกกรณีห้ามเรียก HTTP ทั้งที่บางกรณีมี mixed candidates; candidate_2 มี circuit state จาก timeout จำลองข้ามเคสทำให้เคสถัดไปไม่เรียก HTTP ได้ แก้การแยก fixture กับเงื่อนไขคาดหวังโดยคง mixed-candidate model path ไว้ ผลสุดท้าย candidate_4 ผ่านทั้งหมด ไม่ลบผลรอบที่ไม่ผ่าน

## 6. ไฟล์และข้อมูลที่รักษาไว้

แก้ติดตั้งเพียง `app/knowledge/common/entity_search.py` และ `app/knowledge/common/answer.py` ใน R78 โดยเก็บก่อนแก้ใน `before/` พร้อม hash และ diff การแก้ R80 ใน answer.py ยังคงอยู่ และ open_day.py ไม่เปลี่ยน

DB SHA256 ก่อน/หลัง:

`4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d`

ไม่แก้ facts ราคา เวลาบริการ approvals/releases ไม่แก้ชุดเดิมใน Downloads ไม่ลบหรือเขียนทับ log เดิม ดูรายการไฟล์แอป/UI อื่นที่ตรวจว่าไม่เปลี่ยนและ hash ติดตั้งที่ `INSTALLATION.json` กับ `SOURCE_INVENTORY_BEFORE.json`

## 7. สิ่งที่ยังไม่ได้ยืนยัน

1. เว็บ/worker ที่กำลังรันโหลดโค้ดใหม่แล้วหรือยัง ต้อง restart และเทียบ loaded_source_sha256
2. เวลา HTTP จริงหลัง patch ทั้งไทยและอังกฤษ
3. selector ของ mixed candidates ยัง timeout หรือไม่ และเวลาไปอยู่ที่ load/prompt_eval/eval/lock ส่วนใด
4. การตอบถูกทุกหมวดหรือความพร้อม production ทั้งระบบ ชุดนี้ยังไม่ใช่หลักฐานดังกล่าว

## 8. ขั้นต่อไปที่เตรียมไว้แล้ว

เปิด **Open-R81-Restart-and-Check.cmd** หนึ่งครั้งจาก Windows โดยเปิด Ollama ทิ้งไว้ ตัวช่วยเรียก stop/start R78 เดิมที่ตรวจตัวตนก่อนหยุด จากนั้นตรวจคำถามที่เกี่ยวข้อง **14 ข้อความ** ใน session แยกกันไทย/อังกฤษ

ถ้า fingerprint/profile/LLM ON ไม่ตรงจะไม่ทดสอบต่อ ผลเก็บโฟลเดอร์ใหม่ใต้ `user_results` แยกการเกิด selector timeout/transport/schema ออกจาก content contract แม้การ fallback ทำให้คำตอบยังผ่านก็ตาม ดูวิธีใช้ `README_TH.md`

## 9. งานที่ยังควรทำหลังอ่านผลจริง

1. แก้ mixed-candidate retrieval ของไทยจากหลักฐาน log: ตรวจ independent topic support, ข้อมูลซ้ำ และ token budget ก่อนลด candidate พร้อม contrast tests ป้องกันตัดแหล่งถูกทิ้ง
2. ใช้ timings ของ selector จริงตัดสินว่าต้องลด prompt, รวมคิว/จัดบริบทโมเดล หรือจัด warm-up อย่างไร ไม่ใช้ผล READY แทนการวัด prompt จริง
3. ก่อน production ตรวจ effective dates และที่มาของข้อมูลราคาเดิม: 18 rates มีช่วง 2026-02-01 ถึงก่อน 2026-04-01 และ PC 6 rates ไม่ทราบช่วงผลบังคับใช้ ไม่ขยายวันที่ด้วยการเดา

ไม่มีคำถามนโยบายใหม่ที่ต้องให้เจ้าของตัดสินใจสำหรับ patch นี้ ส่วนราคาปัจจุบันและนโยบายที่ยังไม่มีข้อมูลยืนยันต้องให้เจ้าของให้ข้อมูลก่อนเผยแพร่เป็นข้อเท็จจริง

## 10. เอกสาร/ผลประกอบ

- `FLOW_R81_TH.md`: Flow และการตรวจทานสามรอบ
- `CHANGESET.patch`, `before/`, `candidate/`: การแก้ที่ตรวจสอบย้อนกลับได้
- `verification/candidate_4/RESULTS.json`: ผล selector สุดท้ายพร้อม audit
- `verification/qualified_1/RESULTS.json`, `verification/rephrase_1/RESULTS.json`, `verification/open_day_1/SUMMARY.json`
- `HELPER_QA.json`, `INSTALLATION.json`, `README_TH.md`
