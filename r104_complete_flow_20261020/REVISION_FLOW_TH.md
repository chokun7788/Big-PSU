# Flow กลาง R103: แก้จากผลรวม R102 ก่อนทดสอบรุ่นใหม่

## ขอบเขต

พัฒนาบนสำเนา R102 ที่แยกจาก R78 และ R101 เก็บผลรอบแรกและ source manifest เดิมไว้ครบ ไม่แก้ฐานข้อมูลจริง ไม่สร้าง approvals จริง และไม่เผยแพร่แทนเจ้าของ

## หลักฐานรอบแรก

R102 รันครบ 19 lanes ภายในประมาณ 19.6 นาที แต่มี lane ที่หยุดก่อนครบ checks จึงไม่เท่ากับผ่านทั้งระบบ Acceptance 37 สถานการณ์ × 3 ภาษา × 4 รูปคำถาม = 444 variants ผ่าน 265 (59.68%) รายละเอียดทุกเคสผิดอยู่ใน `analysis_batch01/FAILURES_TH.md` และ JSON ที่เก็บคำตอบ/decision artifact ไว้ ไม่รวมจำนวน assertions กับคำถามเป็นคะแนนเดียว

### ปัญหาและการแก้เป็นชุด

| จุด | หลักฐาน/ความเสี่ยง | การแก้ R103 |
|---|---|---|
| คำขึ้นต้น/ลงท้าย | ขอถามหน่อย, Could you help…, ตอบสั้น ๆ เปลี่ยนเส้นทาง | interpretation surface รักษาชื่อเจ้าของข้อมูลและ raw input, ตัดเฉพาะกรอบคำถามที่ทราบความหมาย |
| typo ในคำถาม | ราาคา, prcie, Waht ทำให้เหลือเพียงคำถามย่อยหนึ่งส่วน | ใช้ concrete error channel และ schema lexicon ก่อนแตก needs ไม่แก้ชื่อ/ตัวเลข/คำปฏิเสธ |
| หลายคำถาม | ราคาและวิธีจอง, สองเกม, สองบริการคนละเวลา | แยก needs ก่อนอ่านข้อมูลและ execute task ของแต่ละส่วน เก็บ service/duration ต่อ need และแชร์เฉพาะ audience ที่มีหลักฐานในประโยค |
| aggregate | conflict/privacy ของหนึ่ง need อาจลบอีก need ที่ถูก | certify ราย need ก่อน aggregate; parent ใช้ผลที่ตรวจแล้ว และรวม claim packets ของลูก |
| รายการเกม | catalog อ่านชื่อแต่ไม่มี offering receipts จึงถูกปฏิเสธ | enumerate game_service ที่ offered=true พร้อม game title/service FK/offered และ scope receipt ไม่มี top K |
| กติกา | vocabulary เก่าหากฎเกมใหม่ไม่เจอ และเลือก rule IDs แล้ว bridge อาจเปลี่ยน scope | source rule reader ตามเกม/รายการ/หัวข้อจากข้อมูล ปิด dependency closure ภายในรายการเดียว; incomplete clause ไม่อ้างว่า complete |
| ตอบต่อด้วยชื่อ | ROV กลายเป็นภาพรวมเกม | pending game/event selection เก็บ original task/query แล้วเติม entity ที่เลือก ไม่มี answer facts ใน history |
| ราคาและคำปฏิเสธ | ไม่ใช่บุคลากรแต่กลับมีราคาบุคลากร | actor exclusions มี record IDs ชัดก่อนอ่าน rate; ไม่อนุมานว่าผู้ใช้มีสิทธิ์กลุ่มอื่น |
| supersession | metadata บอกใช้แทนของเก่าแต่ calculator อาจใช้ตัวเลขเก่า | บล็อกตัวเลขที่ถูก supersede จนมี typed replacement; ไม่แก้ approved record อย่างเงียบ ๆ |
| currency projection | minor units อาจแสดงเป็นบาทโดยไม่หาร 100 | renderer แสดง current_rate integer ด้วย /100 พร้อมหน่วยและ source pointer |
| สถานะผล | attach เขียนทับ broken_relation/conflict/declared set | รักษา terminal receipt ที่ตรวจแล้ว แยก missing source/invalid relation/conflict |
| วันเปิด | wrapper ทำให้ open-day reader ไม่เข้า | canonical framing + schedule dispatch ก่อน fallback; bookable ไม่เท่ากับ physical open |
| วันที่ในชื่อ FAQ | strip_names อาจลบวันที่ผู้ใช้ถาม | ป้องกันเฉพาะชื่อ entity ไม่ลบข้อความ FAQ/policy ที่เป็นคำถาม |
| live | static facility FAQ อาจถูกยืนยันว่า live available | confirmed live ต้องมี live_booking observation; ไม่มีให้ unavailable ไม่ใช้ static presence เป็น vacancy |
| ราคาอุปกรณ์รุ่น | ไม่มี graph model→resource→service→rate | เพิ่ม declared FK path และ task kinds ไม่สร้างราคาซื้อฮาร์ดแวร์ |
| owner mapping | ผู้กรอกต้องคิด ID/หน่วยเอง และ diff ไม่แสดง mapping | auto claim ID, เลือก canonical units, ใส่ mapping ใน before/after review |

## Flow runtime ตั้งแต่ต้นถึงจบ

1. รับ raw question/locale/history จากช่องทางที่ระบุ delivery status ได้เท่านั้น
2. Pin snapshot: release/epoch/reference clock/ภาษา ให้ทุก need ใช้ข้อมูลรุ่นเดียวกัน
3. สร้าง interpretation surface โดยป้องกันชื่อ entity แล้วคืนชื่อเดิม เก็บการเปลี่ยนใน trace
4. อ่าน pending selection จาก state ที่ server ส่งแล้ว; task ใหม่ชัดเจนต้องรีเซ็ต scope เดิม
5. แยก independent needs, เก็บ source span, IDs, actor, duration, negation, predicate
6. ค้นจาก names/schema/declared relations; ห้ามใช้ retrieved top K เป็นคำว่า “ทั้งหมด”
7. ถ้ายังตีความไม่พอจึงใช้ LLM เสนอ plan ภายใต้หนึ่ง budget ร่วม ห้าม model เสนอ facts/SQL/formula
8. Validate plan spans/IDs/kinds และ confident task locks; live ไม่เปลี่ยนเป็น FAQ
9. Compile read graph จาก task + subject + declared FK paths
10. ตรวจ evidence pointer, authority, effective dates, public scope, withdrawn records และ relation validity
11. เลือก executor ตามชนิด: graph read, source rule closure, catalog set, price calculator, calendar, mapped claim, live adapter
12. ข้อขัดแย้งต้องมี explicit scoped authority จึงใช้แทนกันได้ ไม่มี default ว่าใหม่กว่าเชื่อกว่า
13. ตรวจ prerequisites และ dependency closure ของแต่ละ need แยกกัน
14. Source gap ตอบว่าขาดอะไร; missing user slot ถามเฉพาะตัวเลือก; transport failure ระบุ unavailable ไม่อ้างว่าไม่มีข้อมูล
15. Render จาก field values/complete source clauses พร้อม conditions/exceptions และ citations ไม่หั่นเงื่อนไขเพียงให้สั้น
16. Certify delivered claims เทียบ required graph และ source receipts; ไม่เอา field completeness แทน semantic correctness
17. Aggregate child answers โดยรักษาคำตอบส่วนที่สำเร็จและเหตุขัดข้องรายส่วน
18. ตรวจ snapshot ปิดท้าย หากข้อมูลเปลี่ยนใช้ corrective read budget ร่วม มิฉะนั้นให้ retry ไม่คืน facts เก่า
19. บันทึก server_written logs/audit/model transport; ไม่ถือว่า client เห็นข้อความแล้ว

## การทบทวนแผนสามรอบ

1. เทียบกับ failure ทั้ง 37 scenarios: จัด symptom → interpretation/state/read/evidence/render/evaluation ไม่รวมเป็นสาเหตุเดียว
2. ตรวจ interaction: supersession+calculator, private person+address, conflict+booking, live+static FAQ, named date+calendar เพิ่ม guard ที่ขอบเขตใช้ร่วม
3. ตรวจการวัดผล: แยก malformed fixture, เปรียบเทียบ requested display fields กับ graph prerequisites, แยก source unknown/transport failure จาก content failure ไม่ปรับคะแนนเพียงให้ผ่าน

## การแก้ตัวทดสอบที่ต้องเปิดเผย

- new_contracts หยุดหลัง 13 assertions เพราะ conditions_all ใส่ bilingual prose แต่ schema กำหนด list ของ field/operator/value: แก้เฉพาะ synthetic fixture เป็น typed condition มี FIXTURE_CODE
- published test ใช้ profile common-r101-published จึงไม่ตรงรุ่นปัจจุบัน: ใช้ profile รุ่น candidate
- C07 ต้นทางมี complete disconnect clause และไม่มีเงื่อนไขแบ่ง phase: การบังคับให้ถาม phase เป็น oracle ที่เพิ่มเงื่อนไขเอง จึงเปลี่ยนตรวจว่าตอบ clause พร้อม exception ได้ ไม่เพิ่ม phase ลง production
- task matrix เดิมเลือก audience เป็นตัวอย่าง price โดยไม่ระบุ service แล้วคาดหวังคำตอบราคา: เปลี่ยนเลือก service + actor
- matrix แยก graph prerequisites จาก displayed fields ตามคำถาม เช่นถาม release ตรวจ rulebook_release ส่วน event_name ยังคงถูกตรวจใน graph ไม่บังคับให้พิมพ์ทุกช่องเสมอ

คะแนน R102 เดิมไม่แก้ย้อนหลัง การเปรียบเทียบต้องแสดงทั้ง common-oracle subset และ cases ที่ oracle เปลี่ยน

## ขั้นทดสอบ

1. Static AST/schema/import/JS syntax; ไม่เรียกแชทเพื่อไล่เคสทีละข้อ
2. Freeze R103 source/config/model/input hashes
3. Integrated batch ครบทุก lane ตามรุ่นนี้ และบันทึกทุก failure/exception
4. Full common-only LLM ON workload เดิม 20,554 unique request keys / 55,811 grades ตามคำขอผู้ใช้ล่าสุด เก็บ coverage manifest และ source unchanged แยกจริง; ไม่รัน legacy
5. วิเคราะห์จากผลที่จบครบ; strict/protocol/content/evidence/validity/model transport ต้องแยก ไม่อ้าง strict failure ทั้งหมดเป็นตอบผิดจริง
6. ส่วนที่ทดสอบด้วย synthetic provider ไม่ใช่การยืนยัน occupancy จริง; provider integration ที่ติดต่อไม่ได้รายงาน blocked โดยเฉพาะ

## ข้อจำกัดที่ยังต้องวัด

การรับข้อมูลครบ schema ไม่รับรองทุก paraphrase หรือความหมาย prose อัตโนมัติ ตัวอ่าน typed compatibility ยังมีอยู่ ข้อมูลที่ไม่ระบุวันมีผล/สิทธิ์การใช้เกม/การเผยแพร่จริงต้องคง unknown จนมีหลักฐาน ไม่สร้าง approval แทนเจ้าของเพื่อให้คะแนนดีขึ้น


## รอบแก้ R104 หลัง R103 integrated02

R103 acceptance 399/444 (89.86%) แต่ชุดตรวจเดิมพบ regressions จึงยังไม่ปล่อย Full Test ต่อแบบเงียบ ๆ เก็บ source/logs ของ R103 ไว้แล้ว แก้ root causes: รักษาตัวพิมพ์ชื่อ unknown, typo recovery จำกัดเฉพาะ transposition/duplicate, franchise selection ก่อน catalog, ไม่ใช้หัวข้อ rule แทนชื่อเกม, แยก price+booking เมื่อแชร์ subject ท้ายประโยค, อ่านกฎก่อน/หลังพร้อม dependency, ใช้ mature scoped clause bridge ก่อน heading fallback, missing relation ตอบ source gap ที่ valid, รักษา explicit version/procedure task ไม่ถูกคำในชื่อบัง และไม่แสดง FK IDs ในคำตอบ

R104 ไม่เปลี่ยน oracle C07 เพิ่มเติมและไม่ปรับราคา/ช่วงมีผล/approval จริง ใช้ integrated03 ตรวจครบทุก lane ก่อน Full Test common-only LLM ON ตาม workload เดิม 20,554 keys / 55,811 grades
