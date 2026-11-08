# R87 เชื่อมพฤติกรรมเดิมให้อ่าน Format กลาง

## ขอบเขต

ใช้ interpreter/grammar/การแบ่งเงื่อนไขและ routing configuration ที่มีเดิม ข้อเท็จจริงต้องอ่านจาก common snapshot ปัจจุบันเท่านั้น ไม่คืน fallback ไป facts ใน JSON เก่า ไม่แก้ราคา นโยบาย approvals/release หรือ log เดิม ไม่รัน full test

## Flow และการตรวจทานก่อนทำ

1. สำรองโค้ดปัจจุบันและ hash ฐานข้อมูล ใช้ candidate overlay ก่อนติดตั้ง
2. Rental bridge ใช้ grammar helpers ของเดิม (_selection/_periods/_asks และสัญญาณภาษา) แต่สร้างรายการโซน/กลุ่ม/แพ็กเกจจาก DB กลาง ไม่ใช้ TARGETS หรือราคาในไฟล์เก่า
3. แผนงานกลางเก็บ requests ที่ผูก zones/audiences/periods เป็น tuple ต่อ clause พร้อม asks และ trusted server state ไม่เก็บตัวเลขราคาใน state
4. อ่านและ render ทุกครั้งจาก revision/source ปัจจุบัน พร้อม validity และ unknown ห้ามแปลงที่นั่งเป็นจำนวนผู้เล่น ห้ามหารราคาเหมาวันเป็นรายชั่วโมง
5. ใช้ RuleMatcher compiler/priority/category เดิมเป็นการตีความ โดยเอาเฉพาะ routing config แล้ว map intent_key → record ปัจจุบัน ไม่ใช้คำตอบเก่าจาก rules และไม่ compile owner aliases ทั้งหมดเป็น regex
6. หัวข้อที่เคย unknown ต้องตรวจ source-backed records ที่เพิ่มใหม่ก่อนปิด semantic lookup
7. กฎแข่งขันและปุ่มยังใช้ reader/facet/projection ที่เชื่อมไว้แล้ว ตรวจคำถามคู่เดิมและแหล่งข้อมูลย่อย ไม่สลับไป renderer ที่อ่าน facts เก่า
8. ตรวจ data-only updates/new zone/withdrawal ในฐานทดลองแยก ทุกค่าทดลองไม่ใช่นโยบายศูนย์
9. ตรวจเส้นทางจริงเมื่อ LLM ON และผ่านเว็บหลังติดตั้ง เปรียบเทียบชุดเดียวกันก่อน/หลัง แยก transport จาก answer correctness

## ทบทวน 3 รอบ

1. Source separation: ห้ามเรียก load_zone_rental_data/build_zone_rental_answer และห้ามอ่าน answer ของ RuleMatcher มาแสดง ตรวจด้วย fixture ที่แก้ราคาและ block legacy fact loaders
2. State contract: การถามต่อเปลี่ยนแค่ slot ที่ผู้ใช้ระบุ รักษา tuple ต่อ clause, reset เมื่อเปลี่ยนเรื่อง/ยกเลิก และอ่านราคาฉบับใหม่ไม่เก็บ facts ใน history
3. Growth: สร้างโซนชื่อใหม่ในฐานทดลองโดยไม่แก้รายการในโค้ด ต้องถามราคา/อุปกรณ์ได้ และ unknown gate ต้องไม่ปิดทางข้อมูลใหม่

เก็บผลทุก attempt และปรับตามข้อผิดพลาดจริงก่อนติดตั้ง ไม่มีการอ้างว่าชุดเฉพาะจุดเท่ากับ full parity ของทุกคำถาม

## ปรับจากการทดสอบจริง

- Candidate 1 49/51: คำย่อ PS5 ยังไม่ผูกกับ label PlayStation 5 และรายการอุปกรณ์ Nintendo ยังใช้ service ที่ไม่มี resource FK
- เติมคำย่อจากหมายเลขใน source label ไม่เขียนราคาหรือเพิ่มรุ่นที่ไม่มีใน source และใช้ named zone ที่คำถามระบุจริงอ่านอุปกรณ์ตาม source grouping
- Candidate 2 50/51 ตามเกณฑ์แรก แต่ตรวจพบ oracle เลข 1 อ่อนเกิน เพราะ [S1] ก็ทำให้ผ่านได้ จึงแก้เกณฑ์ให้ต้องมี 1 ชั่วโมง/1 hour จริง ผลเก่าเก็บครบ
- Candidate 3 50/51: intent เดิมเลือกถูกแล้ว แต่ field/FAQ stages ด้านหลังยังเปลี่ยนงานหรือไม่ยอมอ่าน answer จึงคง contract ที่ครอบคลุมคำถามผ่านไปจนจบ ไม่ใช้เฉพาะชื่อ record
- Candidate 4 51/51 พร้อม actual model generation/selector ส่วน update/withdraw/new-zone checks อยู่ในฐานทดลองและควบคุม model transport แยกกัน
- ตรวจเพิ่มเติมใน fixture: สืบ tuple เดียวจากคำถามผสม, ปฏิเสธ PS6 ที่ไม่มี, เวลาเหมา 5 ชั่วโมงที่ไม่มีราคา, ยกเลิก context, ยกเว้น VR และ validity unknown ต้องไม่ถูกแสดงเป็น fully confirmed current price

## ทบทวนหลังอ่านคำตอบจริงและปรับรอบที่สอง

1. เว็บครั้งแรก 51/51 ตาม oracle เดิม แต่เมื่ออ่านเนื้อหาจริงพบว่า RoV “สรุปสั้นๆ” ยาว 2,729 ตัวอักษร และ CS2 ประท้วงยาว 1,417 ตัวอักษร เพราะ oracle ตรวจเพียง domain/มีคำที่ต้องการ ไม่ตรวจการครอบคลุมหลายหัวข้อและเนื้อหาที่เกินประเด็น คะแนนเดิมจึงไม่ใช่การรับรองคุณภาพสรุป
2. เพิ่ม competition_bridge ใช้ substantive_lines/clause_supports_facet และ detail concept predicates ของเดิม แต่ไม่เรียก build_competition_overview/lookup_competition_detail/load_curated_rows ที่อ่านข้อมูลเก่า เลือกจาก competition_rule ของ parent ปัจจุบันเพียงเล่มเดียว
3. สรุปเลือกข้อเต็มจากไม่เกิน 6 facet พร้อมบอกว่าเป็นบางข้อ ไม่หั่นข้อความกลางเงื่อนไข ไม่เลือก “Occurrence 1: warning” ที่ไม่มีเหตุให้ลงโทษ แสดง dependency rows ถ้ามี; ถ้าผู้ใช้ขอทั้งหมดไม่จำกัดด้วย summary
4. รายละเอียดประท้วงเลือก proposition ของ source จริง เก็บเส้นตาย/เงื่อนไขหลังจบแมตช์/ผู้มีสิทธิ์ยื่นครบ ถ้าถามภาษา/อำนาจ/หลายประเด็นไม่ตัดเหลือ proposition เดียว
5. รอบ competition_1 และ _2 พบ derived RoV acronym ไม่ถูกตัดออกจาก residue จึงยังไม่รับ summary; ใช้ derived_names เดียวกับตัวกลางแทนการเพิ่ม alias ต่อคำถาม นอกจากนี้แก้ oracle ของ “ครบทุกข้อ” ให้ตรวจ selected source sections จริง ไม่ใช่ response_projection ที่มีเฉพาะ parent
6. Fixture competition ครั้งแรกหยุดเพราะตัวอย่างใช้ค่า facet/source_order ผิด schema (ไม่ได้แก้ validator); ครั้งที่สองพบ English generic equipment ไม่เข้า predicate เก่า ใช้ explicit singleton facet ของข้อมูลกลางร่วมกับ predicate จึงรองรับ source ใหม่ทั้งสองภาษาโดยไม่ใส่เนื้อหาคำตอบลงโค้ด
7. ชุด candidate_release เปิดโมเดลจริง 55/55; fixture_release ราคา/ข้อมูลใหม่ 19/19 และ competition_fixture_release 7/7 แยกจากความถูกต้องของโมเดล เปลี่ยนเส้นตาย 15→23 ในฐานทดลองเท่านั้น พร้อม block legacy competition loader และทดสอบเพิ่ม/ถอนข้อกติกา

ทบทวนความเสี่ยงรอบสุดท้าย: จำกัด bridge เฉพาะงานที่ตีความครบ; ถ้ามี proposition ที่เหลือให้ตัวกลางจัดการ, metadata/source pointer/withdrawal ยังมาจาก snapshot ปัจจุบัน, ห้ามอ้างว่าครบทุกแพตเทิร์นเดิมหรือทุกภาษา, ติดตั้งสองระยะพร้อม before_stage2/CHANGESET_2.patch และตรวจ API ของเว็บที่โหลด fingerprint ล่าสุด ชุดใหญ่ยังไม่รัน
