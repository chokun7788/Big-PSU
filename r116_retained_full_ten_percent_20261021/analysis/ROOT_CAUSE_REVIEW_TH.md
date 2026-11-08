# R116 — สรุปวิเคราะห์หลังทดสอบครบชุด

อ่านร่วมกับ [รายงานคะแนนและ coverage 104 กลุ่ม](REPORT_TH.md) และ [คำถาม/คำตอบ/เกณฑ์ทุกกรณีไม่ผ่าน](CASEBOOK_TH.md) เอกสารนี้ไม่รันคำถามเพิ่มและไม่เปลี่ยนคะแนนเดิม

## 1. สิ่งที่ทดสอบจริง

- สุ่มจาก Full เดิมที่เคยรันกับ Legacy: หมวดละ ceil(10%) ครบ 104 กลุ่ม รวม 2,108 unique requests / 5,643 grades ไม่ใช้คำถามใหม่มาแทน
- ทดสอบ R115 frozen ผ่าน HTTP API จริง เปิด LLM และให้ Flow เลือกเองว่าจะเรียกโมเดลหรือใช้ typed reader ไม่ส่งชื่อหมวดหรือ expected เข้า API
- ใช้ผล Legacy LLM ON ที่บันทึกไว้ของ keys เดียวกัน ไม่รัน baseline ใหม่ จึงมี source/runtime/วันที่ต่างรุ่น ไม่อ้างว่าความต่างเกิดจาก Flow อย่างเดียว
- จบครบและ hash/model verification ผ่าน ไม่มี capture mismatch, grader exception, empty API answer หรือ chat timed_out; HTTP 200 ไม่เท่ากับตอบเนื้อหาถูก

## 2. ผลที่ตอบคำถามว่าใกล้เคียงของเดิมหรือยัง

**บนชุดนี้ยังไม่ใกล้เคียง:** positive literal/clause grades เดิม 2,370/2,517 = 94.16%; ใหม่ 1,709/2,517 = 67.90% ลด 26.26 จุดเปอร์เซ็นต์ การที่รอบก่อนผ่าน source identity/value/state 96.46% บนคำถามรายหมวด ไม่รับรองการตีความโจทย์ Full ที่หลากหลาย

มี 921 จาก 2,108 requests ที่มี positive literal contracts; อีก 1,187 requests ไม่ได้อยู่ใน denominator นี้ ไม่ใช่ว่าถูกละทิ้งจากการรันหรือถือว่าตอบไม่ได้ทั้งหมด

- ผ่าน positive ทุกแถวของคำขอ: เดิม 842/921 = 91.42%; ใหม่ 562/921 = 61.02%
- ในระดับ request: 296 ข้อจากเดิมผ่านทุก positive มาไม่ผ่านบางแถว; 16 ข้อดีขึ้นจนผ่านทุก positive; ไม่ใช่จำนวน semantic regressions ที่มนุษย์ตัดสินครบแล้ว
- Strict เดิม 76.22% / ใหม่ 3.24% มีชื่อ mode/route/status/evidence/เวลาเป็น contract เดิมรวมอยู่ด้วย จึงไม่ใช้ 3.24% เรียกความถูกต้องของเนื้อหา

## 3. หมวดหลักจากชื่อหมวดเดิม

ตารางนี้เป็นกลุ่มเดิมที่มี positive grades มาก ไม่รวม/เปลี่ยนชื่อหมวดเพื่อให้คะแนนดีขึ้น ตารางครบทั้ง 104 กลุ่มอยู่รายงานหลัก กลุ่มเล็กไม่ควรนำเปอร์เซ็นต์ไปสรุป generalization

| หมวด | คำขอที่รัน | Positive grades | เดิม | ใหม่ |
|---|---:|---:|---:|---:|
| game_controls | 177 | 555 | 99.10% | 85.95% |
| games_catalog_availability | 143 | 292 | 97.26% | 78.42% |
| game_detail | 114 | 289 | 97.92% | 61.94% |
| equipment | 105 | 233 | 98.28% | 83.69% |
| service_fee | 153 | 223 | 99.55% | 52.47% |
| members_overview_contact | 65 | 127 | 99.21% | 65.35% |
| reservation_policy | 117 | 122 | 95.90% | 73.77% |
| schedule_calendar | 87 | 122 | 93.44% | 36.07% |
| compound_context_boundary | 65 | 107 | 52.34% | 52.34% |
| studio_rules_penalties | 87 | 85 | 100.00% | 85.88% |
| unclassified | 273 | 46 | 93.48% | 10.87% |
| games | 92 | 40 | 100.00% | 95.00% |
| general_llm | 28 | 28 | 10.71% | 25.00% |
| booking_days_hours | 10 | 20 | 100.00% | 40.00% |
| competition_rules | 128 | 20 | 20.00% | 70.00% |
| damage_responsibility | 10 | 20 | 90.00% | 40.00% |
| food_consumption | 10 | 20 | 100.00% | 80.00% |
| weekday_live_slots | 10 | 20 | 100.00% | 0.00% |

## 4. ปัญหาที่ตรวจยืนยันจาก output/source/code

### 4.1 Reader สำหรับถามทั้งหมดถูกจำกัดเหมือน lookup

Warzone ถามปุ่มทั้งหมด มี source bindings 13 แต่คืน 8; God of War Ragnarök มี 19 แต่คืน 8 เส้นทาง domain_flow/engine.py scoped_candidates จำกัด rank limit=8 ก่อนส่งให้โมเดล เลือก facts ที่อยู่นอก pool ไม่ได้ ตัวตรวจ source-set พบ 6 requests ลักษณะนี้

**แก้ภายหลัง:** แยก list-all กับ single-action lookup; เมื่อ scope game/platform ชัด ให้ enumerate สมาชิกทั้งหมดพร้อมตรวจ set/count ไม่ใช้ top-K retrieval เป็นขอบเขตความครบของคำตอบ

### 4.2 Relation projection จบที่บริการแทนโซน และยังขาด inverse/group operators

ตัวอย่าง Which studio zone has TEKKEN 8 คืน PC #01-#02 และ PlayStation 5 #01-#02 แต่ native graph ไปถึง PC Zone และ PlayStation 5 Zone ได้ ตัวตรวจพบ 17 requests ที่ถามโซนและคืน service โดยไม่ระบุชื่อ zone ที่เชื่อมอยู่ เป็นการตรวจ projection gap ไม่ได้กล่าวว่าทุกคำตอบอ้างสถานที่ผิด

คำถาม เกมไหนเล่นได้หลายโซน ตอบ unconfirmed ทั้งที่ graph ยืนยัน TEKKEN 8 ได้อย่างน้อยหนึ่งเกม; Legacy ก็คืน catalog ทั้งหมดโดยไม่กรองเฉพาะหลายโซน จึงไม่ใช่ semantic gold ที่สมบูรณ์เช่นกัน Graph ของบางบริการยังเชื่อม resource/zone ไม่ครบ ต้องตรวจ relation migration เพิ่ม ไม่ถือ missing edge ว่าไม่ offered

**แก้ภายหลัง:** เพิ่ม forward/inverse traversal, distinct/group/filter และ projection ตาม predicate ที่ถาม พร้อมประกาศ completeness ของ graph คืน confirmed subset เมื่อยืนยันได้ ไม่ถามหาชื่อเกมเมื่อผู้ใช้ต้องการค้นรายชื่อเกม

### 4.3 มีอัตราราคา แต่กฎเลขคณิตยังไม่ประกาศและถามซ้ำข้อมูลที่มีแล้ว

ขอสอบถามหน่อยยครับ บุคคลทั่วไป เล่น PS5 2 ชั่วโมง เสียกี่บาท → ขอรายการและช่วงเวลาเพิ่ม ทั้งที่โจทย์ระบุแล้ว reason duration_arithmetic_not_declared แสดงว่าขาดกฎคำนวณ ไม่ใช่ขาดชื่อบริการ/ระยะเวลา

reason นี้พบ 49 requests ไม่ถือว่าทั้งหมดควรคูณตรง ๆ เพราะ billing unit/การปัดเศษ/ระยะรอบต้องมีหลักฐาน

**แก้ภายหลัง:** แยก known rate / known slots / missing calculation rule; คืน unit rate ที่ยืนยันได้และบอกกฎที่ยังขาดอย่างตรงจุด ไม่สร้าง prorating หรือนโยบายใหม่เพื่อให้ตรง expected เก่า

### 4.4 Compatibility fallback ยังเลือกข้อมูลไม่ตรงจุดและแสดง metadata

API คืออะไร ได้คำอธิบายศูนย์และ Esports; Can a tourist use the studio equipment? ได้กฎศูนย์ทั่วไป ทั้งที่ไม่ตอบสิทธิ์นักท่องเที่ยว แม้แต่ละข้อความมี source จริงก็ยังไม่ตอบ predicate ของโจทย์

compatibility_scope_not_migrated อยู่ใน need_results ของ 99 requests เป็นร่องรอย contract ที่ยังไม่ถูกยกระดับ ไม่ใช่จำนวนคำตอบผิดทั้งหมด ส่วนข้อความ JSON r114_fact/source_record_id แสดงใน answer พบ 34 requests เช่นคำถามถ่ายวิดีโอ

**แก้ภายหลัง:** evidence relevance/answerability gate ก่อน render; ใส่ field visibility allowlist เพื่อซ่อน topic/scope_note ทางเทคนิคจาก customer response; ถ้ามีเพียงข้อมูลข้างเคียงให้บอกขอบเขต ไม่ใช้หัวข้อ confirmed มาแทนคำตอบตรงจุด

### 4.5 Schedule ยังติด source conflict และบาง paraphrase ไปคนละเส้นทาง

ถาม วันอังคารศูนย์เปิดกี่โมง บางข้อไป migrated_schedule_1.open_periods ซึ่ง status=conflicted; bookable_periods ของ record เดียวกัน known เป็น 09:00–12:00 และ 13:00–16:00 จึงไม่ควรแก้ conflict เองหรือเรียกช่วงจองว่าเวลาที่อนุญาตเข้าอาคารทันที

artifact ของตัวอย่างนี้ระบุ closing_time ทั้งที่ผู้ใช้ถามเวลาเปิด; ถาม Maintenance คือช่วงไหน บาง paraphrase กลับไม่มี accepted interpretation ทั้งที่มี FAQ และ maintenance periods อยู่ ต้องแก้ทั้ง task binding และการตอบ partial จากส่วนที่รู้ได้

**แก้ภายหลัง:** แยก opening, closing, bookable, maintenance, current live ชัดเจน; มี supported parser สำหรับการถามช่วง/รายวัน คืนเฉพาะ bookable hours เมื่อ physical opening ยัง conflict พร้อมแจ้งขอบเขต ไม่ทับ source status เพื่อคะแนน

### 4.6 บุคลากร: ข้อมูลมี แต่สิทธิ์การแสดงยังไม่ยืนยัน

inverse role lookup มี person_public_scope_not_confirmed 17 requests ตัวอย่าง role นักศึกษาสหกิจ Game and 3D Developer เลือก person record ได้แล้ว แต่ public_scope unknown ถูก complete_flow.certify กันไว้

**แก้ภายหลัง:** ทำ delivery/public-scope contract ให้สอดคล้องทุก reader รวม direct และ inverse; ให้เจ้าของยืนยัน scope ผ่านงานเผยแพร่จริง ไม่ approve หรือเปิดสิทธิ์อัตโนมัติเพียงเพื่อทำคะแนน

## 5. กลุ่มที่ต้องแยกจาก actual content failures

- Protocol mismatch 5,372 grade events: route/mode contract เก่า; event counts ซ้อนกลุ่มอื่นได้ ห้ามรวมเป็นจำนวนคำถามผิด
- Content_or_format 841 grade events: รวม literal/first-line/complete-clause; ยังต้อง review ความหมาย/source version ไม่ใช่ 841 semantic failures ที่ยืนยันแล้ว
- Source gaps/conflicted/unknown/live unavailable: แยกสิ่งที่ไม่มีจริงจาก facts ที่มีแต่ reader ไม่คืน; booking provider รอบนี้ถูกควบคุม unavailable ไม่ใช่ผลยืนยัน occupancy จริง
- Model transport 1,056 attempts: HTTP success 1,055; TimeoutError 1; selector schema ผ่าน 776/778 แม้ transport ผ่าน 778/778 การสร้าง plan ผิดจึงไม่เท่ากับระบบโมเดลติดต่อไม่ได้
- API ไม่มี timed_out response แต่ backend model call เคย timeout ได้: เป็นคนละชั้น อย่าใช้ HTTP200 มาลบ transport error ที่บันทึกไว้
- Typed claim packets ที่อ่านตรวจไม่พบ ref นอก native reference snapshot ไม่รับรอง claim relevance, publication approval หรือความครบทุก predicate

## 6. ลำดับแก้จากหลักฐานรอบนี้ — ยังไม่ได้แก้ candidate ใน benchmark

1. แก้ contract ของ query operators และ delivery ก่อน: list-all, inverse/group/filter, zone projection, partial answer และ field visibility
2. ปรับ intent/slot binding ให้ทน paraphrase/คำสุภาพ/สะกดผิด โดยเก็บที่มาของ slots และไม่ถามซ้ำช่องที่มีแล้ว
3. ทำ reader สำหรับราคาและ calendar แยก operator จาก source state; กฎคำนวณที่ขาดต้องยืนยันก่อน ไม่เติมสมมติฐาน
4. ปิดช่อง fallback ที่คืน fact จริงแต่ไม่ตอบโจทย์ พร้อมจัด public-scope guard ให้สม่ำเสมอทุกทาง
5. เมื่อแก้แล้วใช้คำถาม sample เดิมเป็น regression suite และติดป้ายว่าเป็น development corpus; ถ้าจะอ้างผล generalization ต้องมีชุดประเมินแยกต่างหากในภายหลัง

รอบนี้ทำตามคำขอทดสอบ sample เท่านั้น ไม่เริ่มแก้ production หรือรัน Full/คำถามเพิ่มโดยอัตโนมัติ หลักฐานก่อน/หลังทุก key อยู่ PER_REQUEST_REVIEW.jsonl และ raw RESULTS.jsonl
