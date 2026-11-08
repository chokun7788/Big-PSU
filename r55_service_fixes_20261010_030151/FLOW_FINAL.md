# Flow ฉบับปรับปรุง r55: คำถามบริการ เกม ราคา การจอง และประวัติสนทนา

## 1. เป้าหมายและแหล่งที่เชื่อถือได้

แก้จากคำถามร้านเกมจริงใน r54 และผลผิดที่พบในแต่ละรอบของ r55 ใช้ข้อมูลเจ้าของ 18 claims ใน user_service_facts_20261008.json, ตารางราคา/เช่าเหมาเดิม, catalog เกม, rulebooks และ API จองที่ผ่านเงื่อนไขสด ไม่แก้ตัวเลขหรือข้อยกเว้นของศูนย์เพื่อให้คำตอบผ่าน test

ขอบเขตรอบนี้คือการเลือกข้อมูลและรักษาสิ่งที่ผู้ใช้ถาม ไม่มีการเปลี่ยนจำนวน worker หรือความสามารถ GPU; งานพร้อมกันของโมเดลยังใช้ระบบ queue เดิม

## 2. ขั้นตอนก่อนแก้และก่อนเปิด candidate

1. อ่าน handoff และผล r54 ตรวจโปรเจกต์จริงก่อนแก้
2. ขอสิทธิ์เขียน ROOT ผ่านระบบ สำรอง source 324 ไฟล์และ hash
3. เก็บ candidate, stdout/stderr, raw responses และผล test เป็นชื่อใหม่ทุกครั้ง
4. หลังแก้ ตรวจ owner hashes 38 ไฟล์ และ source ของ app ใน candidate เทียบ ROOT
5. หาก Git ใช้ไม่ได้ ให้เก็บ diff จาก snapshot ห้าม reset หรือ clean เพื่อทำให้ checkout ดูสะอาด

## 3. รับข้อความและประวัติ

รับ question + locale + session ID + turn ID + last_seen_response_id

- Normalize Unicode/ช่องว่างตามระบบเดิม; typo recovery ที่เพิ่มต้องมี subject ช่วย เช่น สลิปผิด ไม่เปลี่ยนเลขเครื่อง เวลา วัน ราคา หรือคำปฏิเสธ
- เก็บ original_question และ resolved_question แยกกัน
- ใช้ประวัติ session เดียวที่เข้าเงื่อนไข context และ ACK เท่านั้น; timeout/ข้อความที่ใช้เป็น context ไม่ได้ต้องไม่สร้าง target
- คำถามใหม่ที่ระบุเกมหรือ operation ชัดเจนชนะหัวข้อก่อนหน้า
- คำตอบสั้น PC/ทั้งหมด/กลุ่มผู้ใช้/PC2 ใช้งานเดิมเมื่อมี pending slot หรือ scope ที่ยืนยันได้ ไม่เลือกจากตัวอย่างเกมหลายชื่อที่บอทเขียนเอง

## 4. ตรวจคำถามหลายส่วนก่อน handler ที่ตอบทันที

แยก clause ตาม grammar และ operation ที่เห็นจริง จำกัด adapter ใหม่ 2–3 ส่วน; หากแยกไม่ได้ส่งให้ระบบเดิม

แต่ละส่วนเก็บ subject/target/customer group/duration/people/date/time ของตัวเอง เช่น

| คำถาม | สิ่งที่ต้องตอบ |
|---|---|
| PC มีเกมอะไร แล้วบุคคลทั่วไปสองชั่วโมงกี่บาท | เกม PC และราคา PC กลุ่มที่ระบุ 120 นาที |
| วันนี้ PC1 10โมง และ PC2 11โมงว่างไหม | PC1 10:00 และ PC2 11:00 วันที่เดียวกัน |
| ชำระเงินยังไง แล้วจ่ายเงินสดได้ไหม | วิธีโอนจาก source และ cash policy ที่ยังไม่ยืนยัน |

ห้าม price plan ฝั่ง server เขียนคำถามหลายส่วนให้เหลือเรื่องราคาเรื่องเดียว ก่อน pipeline ได้รับข้อความ

## 5. แยก entity และหน่วย

- หมายเลขเครื่องต้องไม่มี colon/หน่วยเวลา/หน่วยเงิน/จำนวนคนตามหลัง; PC1 ต่างจาก PC10 และ PC 10:00
- แยก ISO date ก่อนอ่านช่วงเวลา; ห้ามอ่าน 9:00-9:30 เป็น 00:00-09:00
- แปลงคำระยะเวลาไทย/อังกฤษเฉพาะข้างหน่วย เช่น สองชั่วโมง/two hours = 120 นาที
- จำนวนคนใช้กรอง package capacity เช่น Nintendo 4 คน ไม่ใช้ราคา package 1–2 คน
- VR ช่วงระบุ 09:00–09:30 ตรวจการครองรอบ 09:00–10:00 ตามที่ผู้ใช้ยืนยัน; นาทีต่อแพ็กเกจสำหรับคิดเงินยังเป็นค่าจากตารางราคา

## 6. เลือกข้อมูลตาม operation

| Operation | ตัวทำงาน | ข้อจำกัดที่ต้องแสดง |
|---|---|---|
| Policy/ข้อมูลบริการ | owner claims ก่อน semantic retrieval | ไม่มีคำยืนยันของ field ที่ถามต้องตอบ unknown |
| ราคา | typed plan และ fee calculator เดิม | กลุ่ม/บริการขาดให้ถามเฉพาะ slot; แสดง validity ของราคา |
| งบประมาณ | integer packages = floor(budget/unit fee) | แสดงเงินเหลือ, capacity, eligibility; ราคา 0 ไม่หมายถึงเวลาไม่จำกัด |
| เกมทั้งหมด/เกมในโซน/จำนวนเกม | catalog เดิม | deduplicate ชื่อข้ามโซน; ไม่เปลี่ยน install permission เป็น list เกม |
| เวลาปกติ | calendar/schedule adapter เดิม | ไม่ใช่ข้อมูลเครื่องว่าง; วันปิดพิเศษชนะตารางปกติ |
| สถานะจอง | booking API + date/freshness/source guards | unavailable/stale/wrong date ไม่ใช่ว่าง |
| กฎภาพรวม | explicit game + broad request parser | ปี/หัวข้อเฉพาะต้องไม่ถูกล้างทิ้ง; ภาพรวมไม่ใช่กฎครบทุกข้อ |
| กฎครบทุกข้อ/ต่อหน้า | rulebook coverage + ACK cursor | returned union = expected IDs, ไม่มีซ้ำ |
| ปุ่มควบคุม | control catalog resolver + structured handler เดิม | ไม่เดา family/version/ปุ่มที่ไม่มี และคงคำเตือนแหล่งรอง |
| สเปก PC | local hardware facts เดิม | Home inventory ไม่ได้ยืนยันองค์ประกอบภายในเครื่อง |

ค่าความมั่นใจ .98/.9 เป็นคะแนน routing ตาม heuristic ไม่ใช่ความน่าจะเป็นว่าคำตอบถูก 98%/90%

## 7. ข้อกำหนดก่อนเรียกว่า complete

ตรวจ target, operation, units, negation, จำนวนส่วนที่ผู้ใช้ถาม และ evidence ก่อนปิดงาน

- ถ้าขอทั้งหมด ต้องบอก scope: เกมทั้งโซน / ทุกบริการ / กฎทั้งเอกสาร
- ภาพรวมกฎต้องตอบหลายหัวข้อตาม source ไม่เลือก clause เดียวแล้วเรียกว่าครบ
- ในคำถามหลายส่วนต้องตอบทุกส่วน; unknown ของ cash ไม่ทำให้วิธีโอนหาย
- English ใช้ข้อเท็จจริง/เงื่อนไขเดียวกับไทย ตัวเลข/ราคา/วัน/IDs ต้องตรง ไม่ถือว่าคนอนุมัติคำแปลแล้วเพียงเพราะ test ผ่าน
- แก้คำปนภาษาอาหรับในแถว Tekken ที่รู้ provenance เฉพาะข้อความแสดงผล; เก็บ raw source เดิม

## 8. สถานะและ diagnostics

แยก transport_complete, checked_content, safe_unconfirmed, live_without_oracle, review_pending

timeout ต้องคืน partial_progress ราย request: ขั้นตอนล่าสุดและ events ที่ส่งแล้ว; cause_confirmed=false จนกว่าจะมีหลักฐานสาเหตุ ไม่เรียกขั้นตอนล่าสุดว่าเป็น root cause ทันที

performance cache จำกัด 64 requests และ 16 events/request ไม่เก็บข้อความถามตอบไว้ใน cache นี้

## 9. Loop ที่ใช้จริง

baseline → unit ของ parser/slot และ negative controls → fixture ที่รู้ผล → candidate ใหม่ → HTTP jobs + session ACK → อ่าน answer/trace → ตรวจ omission → แก้เงื่อนไขที่ยืนยันได้ → test ส่วนที่เกี่ยวข้องอีกครั้ง

ตรวจทาน 10 จุด: เลขเครื่อง/เวลา, policy subject, กลุ่มราคา, จำนวนคน, affordability, หลาย clause, scope เกม, rule cursor, language/source, timeout diagnostics; เพิ่มรอบหลังอ่านคำตอบพบ broad RoV ถูกตอบเป็น clause เดียว และ adapter ปุ่มใช้ session alias list คนละชุดกับ catalog

อย่าถือว่า test ที่ตรวจแค่ชื่อเกมพิสูจน์ความครบ ต้องเพิ่ม oracle โดยเก็บผลเก่าไว้ ตัวอย่าง c124 เพิ่ม broad_rules_need_overview หลังพบ omission แม้เกณฑ์เดิมผ่าน

## 10. Release gates และผลรอบนี้

อ่าน RESULTS_ANALYSIS_TH.md และ SUMMARY.json สำหรับตัวเลขจริงตาม candidate ไม่รวมผลคนละรุ่นเป็น accuracy ของรุ่นเดียว

unit/fixture ผ่านไม่แทนสถานะจริงทุกช่องทุกวัน; เจ้าของเคยแจ้งว่าตรวจสถานะจริงแล้วถูกต้อง แต่ fixture รอบนี้เป็นหลักฐานแยกต่างหาก

## 11. ข้อจำกัดที่ยังต้องติดตาม

ไม่รับประกัน typo ใหม่ทุกแบบหรือ compound เกิน 3 ส่วน และยังไม่มี load test หลายคนของ r55; อายุข้อมูลราคา กฎ ปุ่ม และนโยบายที่ไม่มีข้อมูลต้องให้เจ้าของยืนยัน รายละเอียดคำถามเฉพาะอยู่ในรายงานท้ายรอบ
