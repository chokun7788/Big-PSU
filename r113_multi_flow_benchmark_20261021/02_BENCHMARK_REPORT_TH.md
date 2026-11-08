# R113 — ผลเปรียบเทียบ 3 Flow ต่อหมวด

## 1. สิ่งที่ทำจริง

- ออกแบบ 140 Flow = 14 หมวด × 10 ทางเลือก พร้อมคะแนนความเป็นไปได้ทางวิศวกรรม และคัด 42 configurations ก่อนรันผล
- พัฒนาตัวรัน 3 families: lexical scoped retrieval / typed subject–facet contracts / typed + bounded local-model evidence selection พร้อม source provider ร่วม. แต่ละหมวดมี configuration/ขอบเขตข้อมูลของตนเอง ไม่ใช่การติดตั้ง 42 full chatbot engines
- คำตอบใช้ experimental compiled read model จาก common 602 records และ owner overlays R108/R109 รวม 1,268 facts. เป็น candidate projection สำหรับทดลอง ไม่ใช่ import ลง schema common ที่เปิดใช้งานจริง
- ชุดหลักมี 100 คำถามต่อหมวด ใช้ชุดเดียวกันทั้งสาม Flow = 1,400 คำถาม / 4,200 executions ครบ ไม่มี key คู่ Flow–คำถามซ้ำหรือขาด
- ใช้ local model scb10x/typhoon2.5-qwen3-4b:latest เมื่อ hybrid ตีความแบบ typed ไม่ลงตัว ตรวจ digest ก่อน–หลัง ไม่บังคับเรียกโมเดลเมื่ออ่านตรงได้
- ไม่แก้ production R78, frozen R106, approvals หรือ logs เก่า; ผลพร้อมติดตามใน main_natural/TEST_COMPLETE.json

## 2. คะแนนนี้หมายถึงอะไร

คะแนนออกแบบในไฟล์ 01 เป็น heuristic สำหรับเลือกแนวทางล่วงหน้า โดยใช้ค่าประเมินร่วมตาม family และลำดับไอเดีย ไม่ได้มีผู้เชี่ยวชาญให้คะแนนอิสระทั้ง 140 แบบ จึงใช้เป็นสมมติฐานออกแบบเท่านั้น คะแนนที่ใช้เปรียบเทียบการตอบจริงคือตารางผล 4,200 executions ด้านล่าง

ผ่านหนึ่งข้อเมื่อ source claim IDs ที่ตอบครบและไม่เกินขอบเขต ค่า/จำนวนที่ตรวจตรง evidence refs ตรง และ answer state ตรงกับ oracle ที่ตรึงจาก source ก่อนรัน. ตรวจโดยเครื่องจาก task/source contracts ไม่ใช่มนุษย์ตรวจความหมายคำตอบอิสระทั้งหมด

โจทย์เป็น source-grounded natural paraphrases สำหรับการพัฒนา มี 60 single-need / 20 multi-need / 20 missing-or-unconfirmed ต่อหมวด บางข้อทดสอบ source claim เดียวกันด้วยสำนวนต่างกัน จึงไม่ใช่ 100 facts หรือ 100 semantic situations ที่เป็นอิสระต่อหมวด และยังไม่ใช่ representative holdout จากคำถามลูกค้าจริง

แต่ละ adapter ได้รับหมวดที่เลือกไว้แล้ว จึงวัดคุณภาพตัวอ่านในหมวด ไม่วัดการเลือก 14 หมวดอัตโนมัติของ chatbot ทั้งระบบ. ไม่เอาคะแนนนี้ไปเทียบ 94.41% Legacy หรือผล full R106 ตรง ๆ

## 3. ผลหลักรายหมวด

| หมวด | ค้นข้อความ | Typed contract | Hybrid + LLM เมื่อจำเป็น | คะแนนสูงสุด | Flow คะแนนสูงสุด |
|---|---:|---:|---:|---:|---|
| C01 ข้อมูลศูนย์ สถานที่ และช่องทางติดต่อ | 77% (C01-F01) | 60% (C01-F02) | 82% (C01-F08) | 82% | C01-F08 |
| C02 บุคลากรและหน้าที่ | 43% (C02-F01) | 79% (C02-F04) | 74% (C02-F09) | 79% | C02-F04 |
| C03 อุปกรณ์ เครื่อง และความจุ | 64% (C03-F01) | 61% (C03-F05) | 78% (C03-F10) | 78% | C03-F10 |
| C04 เกมที่มี ข้อมูลเกม และรูปแบบเล่น | 41% (C04-F01) | 44% (C04-F05) | 68% (C04-F10) | 68% | C04-F10 |
| C05 ปุ่มควบคุมและการใช้อินพุต | 80% (C05-F01) | 100% (C05-F04) | 80% (C05-F08) | 100% | C05-F04 |
| C06 ราคาใช้บริการรายคนและการคำนวณ | 79% (C06-F01) | 75% (C06-F04) | 78% (C06-F10) | 79% | C06-F01 |
| C07 เช่าเหมาโซน ห้อง และกิจกรรมส่วนตัว | 52% (C07-F01) | 32% (C07-F04) | 72% (C07-F09) | 72% | C07-F09 |
| C08 การจอง การมาถึง และการเปลี่ยนรายการ | 69% (C08-F01) | 7% (C08-F06) | 74% (C08-F10) | 74% | C08-F10 |
| C09 การชำระเงิน สลิป เอกสาร และเงินคืน | 68% (C09-F01) | 8% (C09-F04) | 72% (C09-F09) | 72% | C09-F09 |
| C10 สิทธิ์ใช้บริการ กฎศูนย์ และปัญหาระหว่างใช้ | 94% (C10-F02) | 0% (C10-F05) | 75% (C10-F10) | 94% | C10-F02 |
| C11 ตารางเปิด ช่วงจอง และวันปิดพิเศษ | 81% (C11-F01) | 46% (C11-F04) | 79% (C11-F09) | 81% | C11-F01 |
| C12 สถานะเครื่องหรือรายการจองจากระบบสด | 94% (C12-F01) | 0% (C12-F04) | 75% (C12-F10) | 94% | C12-F01 |
| C13 รายการแข่งขันและข้อกติกา | 32% (C13-F02) | 80% (C13-F05) | 90% (C13-F10) | 90% | C13-F10 |
| C14 ข่าว กิจกรรม ประกาศ และโปรโมชัน | 55% (C14-F01) | 0% (C14-F04) | 73% (C14-F09) | 73% | C14-F09 |

### วิธีเลือกเมื่อคะแนนเท่ากัน

รายงานทุก Flow ที่คะแนนสูงสุดร่วมกัน ไม่อ้างว่าตัวใดชนะด้าน accuracy เมื่อเท่ากัน. Candidate configuration เสนอเลือกตัวที่ตอบเกินขอบเขตน้อยกว่า แล้วจึงพึ่งโมเดลน้อยกว่า. เวลาในชุดนี้มี batch amortization ไม่ใช้เป็น production latency

## 4. ผลละเอียดและจุดที่ยังพลาด

### C01 ข้อมูลศูนย์ สถานที่ และช่องทางติดต่อ

คะแนนสูงสุด 82% — C01-F08; เสนอสำหรับประกอบ candidate: C01-F08

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 23 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C01-F01 | 48/60 | 16/20 | 13/20 | 0 | {"missing_requested_source_claims": 16, "unrequested_or_wrong_scope_claims": 19, "answer_state_mismatch": 7} |
| C01-F02 | 47/60 | 13/20 | 0/20 | 0 | {"missing_requested_source_claims": 20, "answer_state_mismatch": 40} |
| C01-F08 | 58/60 | 17/20 | 7/20 | 40 | {"missing_requested_source_claims": 4, "answer_state_mismatch": 17, "model_protocol_or_transport_unavailable": 6, "unrequested_or_wrong_scope_claims": 11} |

ตัวอย่าง C01-F01 / C01-Q007: ถามจากข้อมูลที่ศูนย์ให้ไว้ งาน PSU Esports Studio - Phuket คือกิจกรรมอะไร

> PSU Esports Studio - Phuket — ชั้น: 1 [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C01:center_psu_phuket:description"], "unrequested_claims": ["C01:center_psu_phuket:floor"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C01-F02 / C01-Q006: รบกวนเช็กให้หน่อย อยากหา ที่นั่งพัก ต้องไปบริเวณใด

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C01:facility_rest_seating:location"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C01-F08 / C01-Q029: ขอรายละเอียดของงาน PSU Esports Studio - Phuket

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C01:center_psu_phuket:description"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C02 บุคลากรและหน้าที่

คะแนนสูงสุด 79% — C02-F04; เสนอสำหรับประกอบ candidate: C02-F04

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 81 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C02-F01 | 36/60 | 7/20 | 0/20 | 0 | {"missing_requested_source_claims": 37, "unrequested_or_wrong_scope_claims": 49, "answer_state_mismatch": 20} |
| C02-F04 | 47/60 | 12/20 | 20/20 | 0 | {"missing_requested_source_claims": 21, "answer_state_mismatch": 21} |
| C02-F09 | 53/60 | 19/20 | 2/20 | 41 | {"unrequested_or_wrong_scope_claims": 9, "missing_requested_source_claims": 1, "answer_state_mismatch": 18, "model_protocol_or_transport_unavailable": 17} |

ตัวอย่าง C02-F01 / C02-Q004: อยากรู้ว่า นางสาวกมลวรรณ นวลสาย ทำหน้าที่อะไร

> นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C02:member_18a751d710b9b30c:role"], "unrequested_claims": ["C02:member_18a751d710b9b30c:display_name"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C02-F04 / C02-Q006: รบกวนเช็กให้หน่อย ใครดูแลงานอะไรในกรณีของ ผศ.ดร.นิวัติ แก้วประดับ

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C02:member_ce4590ddc09c0f4e:role"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C02-F09 / C02-Q006: รบกวนเช็กให้หน่อย ใครดูแลงานอะไรในกรณีของ ผศ.ดร.นิวัติ แก้วประดับ

> ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S1]
> ผศ.ดร.นิวัติ แก้วประดับ — ทีม: Members [S2]
> ผศ.ดร.นิวัติ แก้วประดับ — หน้าที่และตำแหน่ง: อธิการบดี [S3]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C02:member_ce4590ddc09c0f4e:display_name", "C02:member_ce4590ddc09c0f4e:team"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 1, "expected_claims": 1, "returned_claims": 3, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C03 อุปกรณ์ เครื่อง และความจุ

คะแนนสูงสุด 78% — C03-F10; เสนอสำหรับประกอบ candidate: C03-F10

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 81 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C03-F01 | 51/60 | 13/20 | 0/20 | 0 | {"missing_requested_source_claims": 16, "unrequested_or_wrong_scope_claims": 33, "answer_state_mismatch": 20} |
| C03-F05 | 35/60 | 6/20 | 20/20 | 0 | {"missing_requested_source_claims": 39, "answer_state_mismatch": 39} |
| C03-F10 | 55/60 | 17/20 | 6/20 | 59 | {"unrequested_or_wrong_scope_claims": 8, "missing_requested_source_claims": 4, "answer_state_mismatch": 17, "model_protocol_or_transport_unavailable": 14} |

ตัวอย่าง C03-F01 / C03-Q002: ขอสอบถามหน่อยครับ อยากดูรายละเอียดฮาร์ดแวร์ Sony PlayStation VR2

> Sony PlayStation VR2 — ที่ตั้ง: VR Zone [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C03:equipment_sony_playstation_vr2:specifications"], "unrequested_claims": ["C03:equipment_sony_playstation_vr2:location"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C03-F05 / C03-Q002: ขอสอบถามหน่อยครับ อยากดูรายละเอียดฮาร์ดแวร์ Sony PlayStation VR2

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C03:equipment_sony_playstation_vr2:specifications"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C03-F10 / C03-Q002: ขอสอบถามหน่อยครับ อยากดูรายละเอียดฮาร์ดแวร์ Sony PlayStation VR2

> Sony PlayStation VR2 — ชนิดอุปกรณ์: vr [S1]
> Sony PlayStation VR2 — สเปก: key: zone; unit: None; value: VR Zone; key: quantity; unit: None; value: 1 Unit [S2]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C03:equipment_sony_playstation_vr2:device_type"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 1, "expected_claims": 1, "returned_claims": 2, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C04 เกมที่มี ข้อมูลเกม และรูปแบบเล่น

คะแนนสูงสุด 68% — C04-F10; เสนอสำหรับประกอบ candidate: C04-F10

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 81 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C04-F01 | 35/60 | 6/20 | 0/20 | 0 | {"missing_requested_source_claims": 39, "unrequested_or_wrong_scope_claims": 55, "answer_state_mismatch": 20} |
| C04-F05 | 24/60 | 0/20 | 20/20 | 0 | {"missing_requested_source_claims": 56, "answer_state_mismatch": 56} |
| C04-F10 | 55/60 | 7/20 | 6/20 | 76 | {"missing_requested_source_claims": 16, "unrequested_or_wrong_scope_claims": 14, "answer_state_mismatch": 21, "model_protocol_or_transport_unavailable": 12} |

ตัวอย่าง C04-F01 / C04-Q002: ขอสอบถามหน่อยครับ Super Mario Odyssey มีให้เล่นที่ไหนในศูนย์

> Super Mario Odyssey — แนวเกม: เกม Platformer 3D [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C04:game_detail_super_mario_odyssey:studio_services"], "unrequested_claims": ["C04:game_detail_super_mario_odyssey:genre"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C04-F05 / C04-Q001: Hogwarts Legacy จัดเป็นเกมประเภทใด

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C04:game_detail_hogwarts_legacy:genre"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C04-F10 / C04-Q006: รบกวนเช็กให้หน่อย เล่าเกี่ยวกับเกม Monster Hunter Rise ให้ฟังที

> Monster Hunter Rise — แนวเกม: เกม Action RPG ล่ามอนสเตอร์ [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C04:game_detail_monster_hunter_rise:summary"], "unrequested_claims": ["C04:game_detail_monster_hunter_rise:genre"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C05 ปุ่มควบคุมและการใช้อินพุต

คะแนนสูงสุด 100% — C05-F04; เสนอสำหรับประกอบ candidate: C05-F04

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 81 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C05-F01 | 60/60 | 20/20 | 0/20 | 0 | {"unrequested_or_wrong_scope_claims": 20, "answer_state_mismatch": 20} |
| C05-F04 | 60/60 | 20/20 | 20/20 | 0 | {} |
| C05-F08 | 60/60 | 20/20 | 0/20 | 20 | {"answer_state_mismatch": 20, "model_protocol_or_transport_unavailable": 20} |

ตัวอย่าง C05-F01 / C05-Q081: รบกวนเช็กให้หน่อย ใน Animal Crossing: New Horizons / Nintendo Switch กดปุ่มใดเพื่อสร้างด่านใหม่อัตโนมัติ

> Animal Crossing: New Horizons / Nintendo Switch — หยิบไอเทม: Y — หยิบไอเทมที่อยู่บนพื้น [S1]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C05:controls_nintendo_animal_crossing_new_horizons:binding_5"], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "missing_source", "actual_status": "answer", "matched_claims": 0, "expected_claims": 0, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C05-F08 / C05-Q081: รบกวนเช็กให้หน่อย ใน Animal Crossing: New Horizons / Nintendo Switch กดปุ่มใดเพื่อสร้างด่านใหม่อัตโนมัติ

> ระบบตีความไม่พร้อมใช้งาน จึงยังยืนยันส่วนนี้ไม่ได้

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "missing_source", "actual_status": "unavailable", "matched_claims": 0, "expected_claims": 0, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C06 ราคาใช้บริการรายคนและการคำนวณ

คะแนนสูงสุด 79% — C06-F01; เสนอสำหรับประกอบ candidate: C06-F01

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 72 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C06-F01 | 59/60 | 20/20 | 0/20 | 0 | {"missing_requested_source_claims": 1, "unrequested_or_wrong_scope_claims": 21, "answer_state_mismatch": 20} |
| C06-F04 | 57/60 | 18/20 | 0/20 | 0 | {"missing_requested_source_claims": 5, "answer_state_mismatch": 25, "unrequested_or_wrong_scope_claims": 13} |
| C06-F10 | 60/60 | 18/20 | 0/20 | 12 | {"unrequested_or_wrong_scope_claims": 13, "answer_state_mismatch": 22, "missing_requested_source_claims": 2, "model_protocol_or_transport_unavailable": 9} |

ตัวอย่าง C06-F01 / C06-Q034: รบกวนเช็กให้หน่อย คิดค่าบริการรายชั่วโมงเป็นต่อคนหรือต่อเครื่อง

> VR Station 1 ชั่วโมง / General Adult — ค่าบริการต่อคนต่อรอบ: 1050 บาทต่อคนต่อรอบ [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C06:Q049:owner_policy"], "unrequested_claims": ["C06:migrated_rate_vr_60_1_5_general_adult:amount"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C06-F04 / C06-Q019: กำลังวางแผนไปใช้บริการ เลยขอถามว่า ราคาที่แจ้งรวมภาษีหรือยัง

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C06:Q050:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C06-F10 / C06-Q082: ถามจากข้อมูลที่ศูนย์ให้ไว้ ราคา Nintendo Switch (1-2 Persons) / PSU Student and Staff ในปี 2028 จะเท่าไร

> Nintendo Switch (1-2 Persons) / PSU Student and Staff — ค่าบริการต่อคนต่อรอบ: 0 บาทต่อคนต่อรอบ [S1]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C06:migrated_rate_nintendo_switch_60_1_2_psu_student_staff:amount"], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "not_current", "actual_status": "answer", "matched_claims": 0, "expected_claims": 0, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C07 เช่าเหมาโซน ห้อง และกิจกรรมส่วนตัว

คะแนนสูงสุด 72% — C07-F09; เสนอสำหรับประกอบ candidate: C07-F09

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 81 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C07-F01 | 38/60 | 14/20 | 0/20 | 0 | {"missing_requested_source_claims": 28, "unrequested_or_wrong_scope_claims": 47, "answer_state_mismatch": 21} |
| C07-F04 | 18/60 | 0/20 | 14/20 | 0 | {"missing_requested_source_claims": 62, "answer_state_mismatch": 68, "unrequested_or_wrong_scope_claims": 6} |
| C07-F09 | 54/60 | 16/20 | 2/20 | 76 | {"unrequested_or_wrong_scope_claims": 18, "answer_state_mismatch": 19, "missing_requested_source_claims": 7, "model_protocol_or_transport_unavailable": 6} |

ตัวอย่าง C07-F01 / C07-Q003: ช่วยตอบสั้น ๆ ว่า ถ้าเช่า PSU Esports Studio - Phuket - VR Zone / ภายนอก / ครึ่งวัน ต้องจ่ายกี่บาท

> PSU Esports Studio - Phuket - VR Zone / ภายนอก / ครึ่งวัน — ที่นั่งห้อง: 34 [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C07:package_9:amount_thb"], "unrequested_claims": ["C07:package_9:room_seats"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C07-F04 / C07-Q001: ห้อง PSU Esports Studio - Phuket - VR Zone / ภายนอก / เต็มวัน มีที่นั่งกี่ที่

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C07:package_8:room_seats"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C07-F09 / C07-Q083: ถามจากข้อมูลที่ศูนย์ให้ไว้ ถ้าเหมา PSU Esports Studio - Phuket - All Zones / ภายนอก / เต็มวัน เกินเวลาจะปรับกี่บาทต่อนาที

> PSU Esports Studio - Phuket - All Zones / ภายนอก / เต็มวัน — ระยะเวลาเป็นนาที: 420 [S1]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C07:package_0:duration_minutes"], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "missing_source", "actual_status": "answer", "matched_claims": 0, "expected_claims": 0, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C08 การจอง การมาถึง และการเปลี่ยนรายการ

คะแนนสูงสุด 74% — C08-F10; เสนอสำหรับประกอบ candidate: C08-F10

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 19 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C08-F01 | 43/60 | 13/20 | 13/20 | 0 | {"missing_requested_source_claims": 24, "answer_state_mismatch": 22, "unrequested_or_wrong_scope_claims": 15} |
| C08-F06 | 0/60 | 0/20 | 7/20 | 0 | {"missing_requested_source_claims": 80, "answer_state_mismatch": 93} |
| C08-F10 | 60/60 | 10/20 | 4/20 | 100 | {"missing_requested_source_claims": 10, "answer_state_mismatch": 19, "model_protocol_or_transport_unavailable": 12, "unrequested_or_wrong_scope_claims": 8} |

ตัวอย่าง C08-F01 / C08-Q003: ช่วยตอบสั้น ๆ ว่า ถ้าศูนย์ปิดหลังจากจองแล้วทางศูนย์จะแจ้งอย่างไร

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C08:Q010:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C08-F06 / C08-Q001: กำลังเล่นอยู่แล้วอยากต่อเวลา ต้องทำยังไง

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C08:Q003:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C08-F10 / C08-Q061: How do I correct a wrong name on my booking? and also How can I extend my play session while I am already playing?

> extend session — conditions and procedure: You may book the next session through the normal process if it is available and within service hours. [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C08:Q011:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 1, "expected_claims": 2, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C09 การชำระเงิน สลิป เอกสาร และเงินคืน

คะแนนสูงสุด 72% — C09-F09; เสนอสำหรับประกอบ candidate: C09-F09

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 15 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C09-F01 | 42/60 | 12/20 | 14/20 | 0 | {"missing_requested_source_claims": 26, "answer_state_mismatch": 28, "unrequested_or_wrong_scope_claims": 11} |
| C09-F04 | 2/60 | 0/20 | 6/20 | 0 | {"missing_requested_source_claims": 78, "answer_state_mismatch": 92} |
| C09-F09 | 58/60 | 14/20 | 0/20 | 98 | {"unrequested_or_wrong_scope_claims": 3, "missing_requested_source_claims": 6, "answer_state_mismatch": 20, "model_protocol_or_transport_unavailable": 20} |

ตัวอย่าง C09-F01 / C09-Q003: ช่วยตอบสั้น ๆ ว่า สามารถแบ่งจ่ายหรือวางมัดจำก่อนใช้บริการได้ไหม

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C09:Q016:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C09-F04 / C09-Q001: ขอใบเสร็จ ใบเสนอราคาหรือใบกำกับภาษีได้ไหม

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C09:Q018:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C09-F09 / C09-Q002: ขอสอบถามหน่อยครับ ยอดที่โอนขาดไป ต้องส่งหลักฐานเพิ่มอย่างไร

> โอนเพิ่มเมื่อยอดขาด — เงื่อนไขและวิธีปฏิบัติ: ติดต่อเพจ Facebook พร้อมสลิปและหลักฐานการจอง [S1]
> เงินโอนเกิน — เงื่อนไขและวิธีปฏิบัติ: ติดต่อเพจ Facebook พร้อมสลิปและหลักฐานการจอง; คำตอบก่อนหน้าระบุเก็บใช้ session อนาคต ไม่คืนเงิน [S2]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C09:Q014:owner_policy"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 1, "expected_claims": 1, "returned_claims": 2, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C10 สิทธิ์ใช้บริการ กฎศูนย์ และปัญหาระหว่างใช้

คะแนนสูงสุด 94% — C10-F02; เสนอสำหรับประกอบ candidate: C10-F02

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 27 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C10-F02 | 56/60 | 18/20 | 20/20 | 0 | {"missing_requested_source_claims": 6, "answer_state_mismatch": 6} |
| C10-F05 | 0/60 | 0/20 | 0/20 | 0 | {"missing_requested_source_claims": 80, "answer_state_mismatch": 100} |
| C10-F10 | 58/60 | 16/20 | 1/20 | 100 | {"missing_requested_source_claims": 5, "unrequested_or_wrong_scope_claims": 14, "answer_state_mismatch": 19, "model_protocol_or_transport_unavailable": 9} |

ตัวอย่าง C10-F02 / C10-Q012: กำลังวางแผนไปใช้บริการ เลยขอถามว่า เล่นเสร็จแล้วศูนย์เก็บข้อมูลล็อกอินผู้เล่นไว้ไหม

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C10:Q022:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C10-F05 / C10-Q001: อินเทอร์เน็ตหรือระบบขัดข้องระหว่างเล่นต้องทำยังไง

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C10:Q028:owner_policy"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_input", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C10-F10 / C10-Q038: ช่วยตอบสั้น ๆ ว่า เล่นเสร็จแล้วศูนย์เก็บข้อมูลล็อกอินผู้เล่นไว้ไหม

> บัญชี Steam — เงื่อนไขและวิธีปฏิบัติ: ศูนย์มีบัญชี Steam ให้ใช้ที่ศูนย์ และใช้บัญชีส่วนตัวได้ [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C10:Q022:owner_policy"], "unrequested_claims": ["C10:Q020:owner_policy"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C11 ตารางเปิด ช่วงจอง และวันปิดพิเศษ

คะแนนสูงสุด 81% — C11-F01; เสนอสำหรับประกอบ candidate: C11-F01

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 43 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C11-F01 | 58/60 | 16/20 | 7/20 | 0 | {"missing_requested_source_claims": 6, "answer_state_mismatch": 16, "unrequested_or_wrong_scope_claims": 13} |
| C11-F04 | 32/60 | 7/20 | 7/20 | 0 | {"missing_requested_source_claims": 41, "answer_state_mismatch": 54} |
| C11-F09 | 54/60 | 20/20 | 5/20 | 61 | {"missing_requested_source_claims": 6, "answer_state_mismatch": 21, "model_protocol_or_transport_unavailable": 12, "unrequested_or_wrong_scope_claims": 9} |

ตัวอย่าง C11-F01 / C11-Q012: กำลังวางแผนไปใช้บริการ เลยขอถามว่า วันธรรมดาช่วงสี่โมงถึงหกโมงเย็นศูนย์เปิดอยู่ไหม

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C11:R108_OPEN_16_18:weekday_closing"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C11-F04 / C11-Q001: วันอังคารมีช่วงซ่อมบำรุงเมื่อไหร่

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C11:migrated_schedule_1:maintenance_periods"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C11-F09 / C11-Q001: วันอังคารมีช่วงซ่อมบำรุงเมื่อไหร่

> ระบบตีความไม่พร้อมใช้งาน จึงยังยืนยันส่วนนี้ไม่ได้

ผลตรวจ: {"passed": false, "missing_claims": ["C11:migrated_schedule_1:maintenance_periods"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "unavailable", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C12 สถานะเครื่องหรือรายการจองจากระบบสด

คะแนนสูงสุด 94% — C12-F01; เสนอสำหรับประกอบ candidate: C12-F01

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 77 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C12-F01 | 60/60 | 20/20 | 14/20 | 0 | {"unrequested_or_wrong_scope_claims": 6, "answer_state_mismatch": 6} |
| C12-F04 | 0/60 | 0/20 | 0/20 | 0 | {"missing_requested_source_claims": 80, "answer_state_mismatch": 100} |
| C12-F10 | 56/60 | 18/20 | 1/20 | 100 | {"missing_requested_source_claims": 6, "unrequested_or_wrong_scope_claims": 6, "answer_state_mismatch": 23, "model_protocol_or_transport_unavailable": 48} |

ตัวอย่าง C12-F01 / C12-Q082: ถามจากข้อมูลที่ศูนย์ให้ไว้ เครื่อง PhantomStation77 พรุ่งนี้เที่ยงว่างไหม

> PlayStation 5 #01 / 2026-10-21 12:00 — สถานะว่างสด: ข้อมูลเก่า ยืนยันสถานะไม่ได้ [S1]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C12:resource_ps5_01_3:live_status"], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "missing_source", "actual_status": "unavailable", "matched_claims": 0, "expected_claims": 0, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C12-F04 / C12-Q001: Cockpit #01 / 2026-10-21 10:00 ว่างอยู่ไหม

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C12:resource_cockpit_01_1:live_status"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C12-F10 / C12-Q002: ขอสอบถามหน่อยครับ ช่วยเช็กว่าจอง PC #05 / 2026-10-21 12:00 ได้หรือยัง

> PC #05 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C12:resource_pc_05_3:live_status"], "unrequested_claims": ["C12:resource_pc_05_0:live_status"], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "unavailable", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C13 รายการแข่งขันและข้อกติกา

คะแนนสูงสุด 90% — C13-F10; เสนอสำหรับประกอบ candidate: C13-F10

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 67 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C13-F02 | 23/60 | 9/20 | 0/20 | 0 | {"missing_requested_source_claims": 48, "unrequested_or_wrong_scope_claims": 30, "answer_state_mismatch": 20} |
| C13-F05 | 60/60 | 20/20 | 0/20 | 0 | {"answer_state_mismatch": 20} |
| C13-F10 | 60/60 | 20/20 | 10/20 | 20 | {"unrequested_or_wrong_scope_claims": 10, "answer_state_mismatch": 10} |

ตัวอย่าง C13-F02 / C13-Q002: ขอสอบถามหน่อยครับ ตามกติกา กฎระเบียบและรูปแบบการแข่งขัน VALORANT เรื่องข้อห้ามสำคัญกำหนดไว้อย่างไร

> กฎระเบียบและรูปแบบการแข่งขัน VALORANT — กฎระเบียบและรูปแบบการแข่งขัน VALORANT: รายการ PSU Phuket VALORANT 2026 Tournament [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C13:valorant_11:rule_clause", "C13:valorant_12:rule_clause", "C13:valorant_13:rule_clause"], "unrequested_claims": ["C13:valorant_2:rule_clause"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 3, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C13-F05 / C13-Q081: รบกวนเช็กให้หน่อย การแข่งขัน CS2 ปี 2028 ใช้แผนที่อะไรแน่นอน

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "missing_source", "actual_status": "missing_input", "matched_claims": 0, "expected_claims": 0, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C13-F10 / C13-Q081: รบกวนเช็กให้หน่อย การแข่งขัน CS2 ปี 2028 ใช้แผนที่อะไรแน่นอน

> กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — แผนที่ในการแข่งขัน: ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN [S1]

ผลตรวจ: {"passed": false, "missing_claims": [], "unrequested_claims": ["C13:cs2_29:rule_clause"], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "missing_source", "actual_status": "answer", "matched_claims": 0, "expected_claims": 0, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

### C14 ข่าว กิจกรรม ประกาศ และโปรโมชัน

คะแนนสูงสุด 73% — C14-F09; เสนอสำหรับประกอบ candidate: C14-F09

100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน 69 แบบ ไม่ใช่ 100 facts อิสระ

| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |
|---|---:|---:|---:|---:|---|
| C14-F01 | 36/60 | 6/20 | 13/20 | 0 | {"missing_requested_source_claims": 38, "unrequested_or_wrong_scope_claims": 37, "answer_state_mismatch": 7} |
| C14-F04 | 0/60 | 0/20 | 0/20 | 0 | {"missing_requested_source_claims": 80, "answer_state_mismatch": 100} |
| C14-F09 | 56/60 | 14/20 | 3/20 | 100 | {"missing_requested_source_claims": 9, "answer_state_mismatch": 24, "model_protocol_or_transport_unavailable": 21, "unrequested_or_wrong_scope_claims": 5} |

ตัวอย่าง C14-F01 / C14-Q007: ถามจากข้อมูลที่ศูนย์ให้ไว้ งาน กิจกรรมจำลองทดสอบ 01 ยังสมัครได้ไหม

> กิจกรรมจำลองทดสอบ 01 — วันที่จัด: 2026-10-22 [S1]

ผลตรวจ: {"passed": false, "missing_claims": ["C14:fixture_event_1:status"], "unrequested_claims": ["C14:fixture_event_1:date"], "wrong_values": [], "evidence_mismatches": [], "status_ok": true, "expected_status": "answer", "actual_status": "answer", "matched_claims": 0, "expected_claims": 1, "returned_claims": 1, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C14-F04 / C14-Q001: งาน กิจกรรมจำลองทดสอบ 06 ยังสมัครได้ไหม

> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถาม

ผลตรวจ: {"passed": false, "missing_claims": ["C14:fixture_event_6:status"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "missing_source", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

ตัวอย่าง C14-F09 / C14-Q049: ถามจากข้อมูลที่ศูนย์ให้ไว้ งาน กิจกรรมจำลองทดสอบ 06 ยังสมัครได้ไหม

> ระบบตีความไม่พร้อมใช้งาน จึงยังยืนยันส่วนนี้ไม่ได้

ผลตรวจ: {"passed": false, "missing_claims": ["C14:fixture_event_6:status"], "unrequested_claims": [], "wrong_values": [], "evidence_mismatches": [], "status_ok": false, "expected_status": "answer", "actual_status": "unavailable", "matched_claims": 0, "expected_claims": 1, "returned_claims": 0, "metric": "source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy"}

## 5. โมเดลและข้อผิดพลาดของ protocol

{
  "attempts": 308,
  "http_transport_success": 308,
  "schema_valid_batches": 248,
  "questions_sent": 903,
  "errors": {
    "ValueError": 60
  }
}

HTTP สำเร็จไม่ได้แปลว่าโมเดลส่งแผนครบหรือเลือกหลักฐานถูก. Invalid/missing per-question plans เป็น model-schema/planning failure แยกจาก transport failure; กลุ่มนั้นยังนับไม่ผ่านในคะแนน end-to-end ของ adapter ไม่ตัดออกเพื่อเพิ่มเปอร์เซ็นต์

แบบจำลองตอบหลายแผนในหนึ่ง HTTP call เพื่อประหยัดเวลา ถ้าชุด JSON ขาดแผนใด parser ปัจจุบันปฏิเสธ batch นั้นทั้งหมด ผลนี้เป็นข้อจำกัดของ implementation ที่ทดสอบ ไม่ใช่หลักฐานว่าโมเดลไม่เชื่อมต่อ. รุ่นต่อไปควรใช้จำนวน items ใน JSON schema และแยกผลที่ใช้ได้ต่อ item โดยเก็บ failed items ไว้ ไม่ต้องเลือก lexical เสมอเมื่อมี known source gap

## 6. ข้อจำกัดเฉพาะข้อมูลและหมวด

- C12 เป็น controlled provider snapshots รวม available/booked/unavailable/stale ไม่ได้เรียกหรือยืนยันสถานะจองลูกค้าจริง
- C14 ใช้ synthetic news fixtures เพราะฐานจริงไม่มี news records เพียงพอ และมีเคสถามข่าวจริงที่ต้องตอบว่าไม่มีแหล่งยืนยัน; ไม่อ้างว่ามีงานเหล่านั้นจริง
- C13 มี source excerpts ที่ยังไม่มีคำแปลอังกฤษ บันทึก flags แยก ไม่อ้างว่าคะแนน claim matching ยืนยันคุณภาพภาษาอังกฤษ
- C06 บางคำถามระยะเวลาใช้ชื่อ record ภายในแทนชื่อบริการที่ลูกค้าใช้ เพราะ projection ยังไม่มีชื่อแสดงผลครบ จึงยังไม่ใช่ชุดทดสอบภาษาลูกค้าจริงทั้งหมด
- คำถามแต่ละหมวดมี locale th 70 / en 20 / auto 10; เคส missing-source ทั้ง 20 ข้อต่อหมวดเป็นภาษาไทยทั้งหมด จึงยังไม่ได้ทดสอบ unknown handling ภาษาอังกฤษในชุดหลัก
- Required selected source claims ที่ใช้ oracle บางคำถามยังเป็น granularity ระดับ source clause/field; คำตอบที่เท่ากันทางความหมายแต่ไม่มี claim ID ตรงอาจไม่ผ่าน จึงไม่ใช้คะแนนนี้เป็น semantic accuracy โดยทั่วไป
- ตัวเลือก 140 แบบที่ไม่ถูกคัดมีเพียง design feasibility score ไม่ได้อ้างว่ารันทดสอบครบ 140 implementations
- Three shared algorithm families ถูกใช้ซ้ำตาม domain configurations ไม่ได้เขียน code engine คนละชุด 42 ชุด และยังไม่รองรับ task ย่อยทุกชนิดใน R112 อย่าง production-complete
- Source view รวม facts ที่เลือกและ owner statements ไม่ใช่การย้าย field/relations ทั้ง schema ลง chatbot runtime จึงยังต้อง integration และ data-only lifecycle checks ในระบบจริง

## 7. การรักษาขอบเขตและการรันต่อ

รอบหลักหยุดครั้งแรกจาก WinError 5 ขณะเปลี่ยนไฟล์สถานะ ไม่ใช่จากตัวอ่านตอบคำถาม มี recovery control แยกและใช้ผลที่บันทึกแล้วต่อโดยไม่ลบหรือเปลี่ยนคะแนน จากนั้นหยุด process ของ benchmark ที่ตรวจ command line แล้วที่ 2,945 ผล เพื่อตรวจคำสั่งเจ้าของก่อนเข้า C13 พบคำถามหน่วยโทษ Pause Tekken 7 ข้อที่เจ้าของเคยสั่งงด และยืนยัน C13 ยังมี 0 executions จึงแทนด้วยคำถามกติกางานอนาคตที่ไม่มี source ใน stratum เดียวกัน ก่อนรันทั้งสาม Flow ของหมวดนั้น ใช้ EFFECTIVE_QUESTIONS_1400.jsonl ร่วมกัน และเก็บ workload เดิมกับรายการเปลี่ยนใน EXCLUSION_ADDENDUM.json ไม่ถือข้อที่งดเป็นผ่าน

ตอนหยุดไม่มี model event ที่บันทึกไว้แต่ขาดผลคำตอบ อาจมี HTTP request ที่ยังไม่บันทึกผลก่อนถูกหยุด จึงไม่อ้างว่าไม่มี HTTP attempt ซ้ำเลย หลักฐานยืนยันได้คือ persisted Flow–question results ครบและไม่ซ้ำ กับคำถามในขอบเขตที่งดไม่ได้ execute ใน main run

## 8. ทำไมมีผล pilot แยก

ชุดแรกใช้คำถามที่ตรงชื่อฟิลด์เกินไป ทำให้ typed/hybrid ส่วนใหญ่ผ่าน 100% โดยไม่เรียก LLM จึงไม่ใช้เป็นข้อสรุปเลือก Flow. เก็บผล 4,200 executions เดิมใน pilot_field_contract ครบ แล้วสร้างชุดภาษาธรรมชาติหลักก่อนตรึง implementation/expected ใหม่ ไม่แก้คะแนนเก่าหรือคัดผลที่ดีที่สุดจากสองชุด. รวมการตรวจทางเทคนิค pilot และชุดหลัก 8,400 executions แต่คะแนนตารางหลักใช้ main_natural เท่านั้น

## 9. ข้อเสนอหลังเห็นผล

1. ประกอบ candidate ด้วย winner/tie recommendation รายหมวดใน WINNER_CANDIDATE_CONFIG.json เป็นข้อเสนอ ไม่สลับ production อัตโนมัติ
2. แก้ช่องว่างที่เห็นจริง: unknown qualifier, facet/subject ambiguity, multi-need coverage และ structured model output. เก็บ successful typed reads เป็นทางหลักเมื่อเหมาะสม ไม่เพิ่ม LLM ให้ทุกคำถาม
3. ตรวจด้วยคำถามอิสระจากผู้ใช้และ retained full corpus ก่อนอ้างว่าใกล้ Legacy; ถ้าต้องการคะแนนคำตอบถูกทางความหมาย ต้องเพิ่ม semantic/source review ที่อิสระจากตัวอ่าน
4. หลัง integration owner fields, dispatcher และ lifecycle พร้อม จึงทำ full common LLM ON ตามแผนเดิม โดยยังแยก fixture/transport/protocol/source gap และข้อมูลต่างรุ่น

## 10. ไฟล์ใช้งาน

- 01_DESIGNS_AND_SELECTION_TH.md / DESIGNS_140.json: แนวคิด 140 แบบและคะแนนออกแบบ
- SELECTED_42.json / flows/: configuration ที่รันได้จริง 3 แบบต่อหมวด
- flow_engine.py: เรียก CLI ด้วย --flow <id> --question <ข้อความ> --locale th หรือ en
- EFFECTIVE_QUESTIONS_1400.jsonl: workload ที่ใช้จริงร่วมกันทุก Flow; NATURAL_QUESTIONS_1400.jsonl เก็บต้นฉบับก่อน owner exclusion addendum
- main_natural/RESULTS.jsonl และ MODEL_EVENTS.jsonl: คำถาม คำตอบ claim/evidence และ model trace ทุกครั้ง
- SCORES_42.json / RANKING_BY_CATEGORY.json / ALL_FAILED_CASES.jsonl: คะแนน ลำดับ และคำตอบที่ยังไม่ผ่านทั้งหมด
- main_natural/RUN_FREEZE.json / TEST_COMPLETE.json: coverage, code/data hashes และ identity ของโมเดล

รายงานนี้เป็นผลทดลองเปรียบเทียบตัวอ่านในหมวด ไม่ใช่คำรับรองว่าระบบแชทจริงได้คะแนนดังตารางแล้ว
