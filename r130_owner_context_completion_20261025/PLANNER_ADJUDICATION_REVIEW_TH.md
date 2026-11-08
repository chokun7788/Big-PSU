# การตรวจเลือกน้ำหนักหลัง R130 replayครบ330

ข้อสรุป: **ไม่รับน้ำหนักnewสำหรับFull Testรอบนี้ ใช้retainedตามfallbackที่กำหนดไว้** เพราะพบcritical reservation/payment regressionและตอบgenreแทนcompetition format แม้raw wire/obligation ratioดีขึ้น

## ขอบเขตหลักฐาน

- 110keysเหมือนกันทั้ง3แขน รวม330แถว ตรวจactual profile/messages/schema/adapter/precision provenance ไม่มีcontext inferenceใหม่
- source/inputของR130คงเดิม; แตกต่างจากข้อมูลR95/R64 จึงไม่ใช่causal Flow comparisonกับlegacy
- newผ่านwire90/110, operation+field56/110, mean slotF1ประมาณ0.131 แต่base/retainedwire0เกิดserialization/version mismatch ไม่ใช่คำตอบถูก0% อ่าน RAW_PROTOCOL_REVIEW_TH.md
- mean typed obligation ratioเพิ่ม0.2409→0.3955 แต่denominatorมาจากproposal อาจตกgold needs จึงใช้ratioอย่างเดียวเลือกไม่ได้
- เปรียบคำตอบ/statusครบ110pairs:79เหมือนกัน และ31เปลี่ยน อ่าน31กรณีเปลี่ยนด้านล่างพร้อมsource bundle; sameไม่เท่ากับcorrect
- retainedเป็นR121plannerweightsบนengine/dataใหม่ ไม่ใช่FlowlegacyR64 การเลือกนี้ไม่รับรองคุณภาพretainedหรือบอกว่าแก้ทุกหมวดครบ

## กรณีเปลี่ยนทั้งหมด31กรณี

### 1. eca9a6816e9e5627bedd41f819355b4c325185fefbeac56ae5174b6489e2ab83

ขอสอบถามหน่อยครับ ช่วง Maintenance จองได้ไหม

**กลุ่ม:** predicate_incomplete_gain

อ่านmaintenance periodsได้เพิ่ม แต่ไม่ตอบcan-book predicate จึงไม่ให้เครดิตว่าfulfilledทั้งคำถาม

**Retained:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**New:** `answer`

**จันทร์**
**ช่วงบำรุงรักษา**: 09:00–12:00 [S1]
**อังคาร**
**ช่วงบำรุงรักษา**: ไม่มี / None [S2]
**พุธ**
**ช่วงบำรุงรักษา**: ไม่มี / None [S3]
**พฤหัสบดี**
**ช่วงบำรุงรักษา**: ไม่มี / None [S4]
**ศุกร์**
**ช่วงบำรุงรักษา**: 13:00–16:00 [S5]
**เสาร์**
**ช่วงบำรุงรักษา**: ไม่มี / None [S6]
**อาทิตย์**
**ช่วงบำรุงรักษา**: ไม่มี / None [S7]

**Source records:** `migrated_schedule_0`, `migrated_schedule_1`, `migrated_schedule_2`, `migrated_schedule_3`, `migrated_schedule_4`, `migrated_schedule_5`, `migrated_schedule_6`

### 2. 703523faaabe601a65578894f204ea56f4c7d676501fa35c8e5b6b3ab13441cd

Please tell me: What time is the afternoon session

**กลุ่ม:** shared_failure_wording_only

ทั้งคู่ไม่ตอบเวลารอบบ่าย ไม่ใช่ข้อมูลขาดที่พิสูจน์แล้ว

**Retained:** `missing_source`

No confirmed source is available for the requested detail.

**New:** `missing_source`

The requested game, machine or topic is not identified. Please specify the target.

**Source records:** 

### 3. 87aa69e37cd5b550f86d95d41525033d6510a1fb1e0ca3adcdbfc65483bbcd1c

ใครเป็นผู้จัดกา

**กลุ่ม:** shared_failure_wording_only

คำสะกดผู้จัดกาถูกตีความไม่สำเร็จทั้งคู่

**Retained:** `missing_source`

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**New:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**Source records:** 

### 4. fe55f25aaebb1da6334206ac51f14ddbe94f9f67fe187a21cdfabd862779dbb9

ขอสอบถามหน่อยครับ ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ

**กลุ่ม:** source_backed_gain

newอ่านroleที่ถามจากmember_832e24bbcd11737eได้ โดยมีsource profile qualifier

**Retained:** `missing_source`

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**New:** `answer`

ตามโปรไฟล์ต้นทางที่บันทึกไว้
**ผศ.ดร.ณัฐพงศ์ ทองเทพ**
**หน้าที่และตำแหน่ง**: ผู้ช่วยอธิการบดีฝ่ายวิชาการ [S1]

**Source records:** `member_832e24bbcd11737e`

### 5. 2a729438da53f233061c6c765da72d9b1735bccabf9f95d04f3096c03e7d0856

What is PSU Esports Studio - Phuket? I need the official answer

**กลุ่ม:** known_source_refusal_regression

retainedอธิบายศูนย์จากFAQที่มีอยู่ได้ แต่newเสียentity binding

**Retained:** `answer`

PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. [S1]

**New:** `missing_source`

The requested game, machine or topic is not identified. Please specify the target.

**Source records:** `migrated_faq_rule_overview_identity`

### 6. 2fe50255e1804a59bbcac8aacf797072089fe2b4d5d3150a412ffe78b89bc3ab

PC ช้กาดจอรุ่นอะไร

**กลุ่ม:** source_backed_gain_with_rendering_gap

newแสดงGPUตามspecificationsได้ แต่ปะปนtechnical keys/ข้อมูลไม่จำเป็น ต้องแยกformattingจากvalue

**Retained:** `unavailable`

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

**New:** `answer`

**Gaming PC รุ่น MSI MAG Infinite S3 14th**
**สเปก**: zone; PC Zone; quantity; 10 Units; recorded_source_detail; สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB; CPU; Intel Core i5-14400; RAM; DDR5 32GB; GPU; NVIDIA GeForce RTX 5060 8GB [S1]

**Source records:** `equipment_gaming_pc`

### 7. b12fff150defd77ca13250799e79b8432b1182c72cfc3689d226445a86dff6dc

Could you explain: Please retrieve the official TEKKEN 8 rulebook evidence for the compettition format. please.

**กลุ่ม:** old_heading_not_complete_answer

retainedแสดงชื่อ/หัวข้อrulebook ไม่ใช่เนื้อหาcompetition formatครบ จึงไม่ใช้answer statusเป็นหลักฐานว่าตอบถูกครบ; newunsupportedก็ตอบไม่ได้

**Retained:** `answer`

**PSU Esports ปะทะมันส์ สนั่นจอ**
Competition rules and format for the Tekken 8 event at PSU Esports: Intense clashes, electrifying screens [S1]

**New:** `missing_source`

The reader does not support the requested operation, so this part cannot be confirmed.

**Source records:** `competition_competition_rules_tekken8_psu_esports_section_001`

### 8. ad28947d610ba429ff05e73c28cf5c3a6b1bbfc7afa9df226af42dffc29a9ed7

ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 เลือกด่านยังไง

**กลุ่ม:** shared_failure_different_layer

Tekkenเลือกด่าน: unavailableเทียบunsupported_operation ยังไม่มีเนื้อหาคำตอบทั้งคู่

**Retained:** `unavailable`

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

**New:** `missing_source`

ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้

**Source records:** 

### 9. 6fd7a9ebca01251de0ca430355a909af4f13f1019252c66c197f4079669ff79f

พื้นที่ PSU Esports Studio - Phuket - All Zones / ภายใน / เต็มวัน นั่งได้กี่คน

**กลุ่ม:** known_source_refusal_regression

package_2มีroom_seats50และretainedตอบได้ newกลับentity_not_bound; ไม่ใช่live capacity

**Retained:** `answer`

**PSU Esports Studio - Phuket - All Zones / ภายใน / เต็มวัน**
**ที่นั่งห้อง**: 50 [S1]

**New:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**Source records:** `package_2`

### 10. 1e0acdf434f61a5ed8f9e71e6ffda2be603a0823784a84e31d34b59dd4edb453

Could you please help me with this: Could you check this using verified information: How can I contact the studio

**กลุ่ม:** known_source_refusal_regression

contact_studio_facebookมีURLตรงคำถาม แต่newไม่ส่งfieldที่ขอ

**Retained:** `answer`

Studio Facebook page — contact information: https://www.facebook.com/psuesportsphuket [S1]

**New:** `missing_source`

Related records exist, but the requested detail is not established.

**Source records:** `contact_studio_facebook`

### 11. a603ab1aed328e10dbf5ac72b6a752be2fb77658ea0365896a1776cd04806370

How to book Cockpit and what days is it open?

**กลุ่ม:** source_backed_multi_need_gain

newเก็บทั้งขั้นตอนจองCockpitและตารางบริการ ในขณะที่retainedตกbooking need; ยังpartialและไม่เท่ากับlive slot

**Retained:** `partial`

Recorded regular play-service timetable, not live machine availability or building access hours. Special closures override this timetable.
**Monday**
**regular play-service timetable**: 09:00–12:00 maintenance; 13:00–16:00 open for play [S1]
**Tuesday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S2]
**Wednesday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S3]
**Thursday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S4]
**Friday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 maintenance [S5]
**Saturday**
**regular play-service timetable**: Closed for play under the regular timetable [S6]
**Sunday**
**regular play-service timetable**: Closed for play under the regular timetable [S7]

**New:** `partial`

**How to book Cockpit**

Booking steps
1. select the desired service
2. choose the date and time
3. enter customer information
4. verify the details
5. pay by transferring funds to a bank account,
6. attach the transfer slip.
[S1]

**what days is it open**

Recorded regular play-service timetable, not live machine availability or building access hours. Special closures override this timetable.
**Monday**
**regular play-service timetable**: 09:00–12:00 maintenance; 13:00–16:00 open for play [S2]
**Tuesday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S3]
**Wednesday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S4]
**Thursday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 open for play [S5]
**Friday**
**regular play-service timetable**: 09:00–12:00 open for play; 13:00–16:00 maintenance [S6]
**Saturday**
**regular play-service timetable**: Closed for play under the regular timetable [S7]
**Sunday**
**regular play-service timetable**: Closed for play under the regular timetable [S8]

**Source records:** `migrated_faq_curated_booking_steps`, `migrated_schedule_0`, `migrated_schedule_1`, `migrated_schedule_2`, `migrated_schedule_3`, `migrated_schedule_4`, `migrated_schedule_5`, `migrated_schedule_6`

### 12. 9c658222c039416e29c42c6e68afcf719cf98cf0b06e9bccf1f8fc6401c60d3c

Could uou please help me with this: What information do I need to book? Please answer brefly

**กลุ่ม:** shared_failure_wording_only

ข้อมูลที่ต้องใช้จองไม่สำเร็จทั้งคู่ แม้newเข้าwireได้ ไม่ถือเป็นsemantic gain

**Retained:** `missing_source`

No confirmed source is available for the requested detail.

**New:** `missing_source`

The requested game, machine or topic is not identified. Please specify the target.

**Source records:** 

### 13. 90a565b2ff823f91fec2e54b32d819555f60b3be8028c0ce983178330f1ca956

Could you please help me with this: Can I walk in

**กลุ่ม:** critical_reservation_regression

walk-inต้องจองผ่านระบบมีsourceชัด retainedตอบได้ newกลับmissing_source

**Retained:** `answer`

Can I just walk in and use the service, or do I need to book beforehand?: Walk-in visitors must still book through the reservation system before using the service. [S1]

**New:** `missing_source`

The requested game, machine or topic is not identified. Please specify the target.

**Source records:** `migrated_owner_claim_walk_in`

### 14. 1d252f4fee66dd473f373f0d0147ca4ed325bc0a1c05a796d2c071c614b923c3

รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องข้อมูลผิด หลังจอง

**กลุ่ม:** critical_reservation_regression_with_scope_limit

retainedอ่านกฎแก้ข้อมูลทั่วไปได้ newไม่ตอบ; ยังต้องแยกข้อยกเว้นเบอร์โทรผิด ไม่ถือข้อความทั่วไปว่าครบทุกscenario

**Retained:** `answer`

แก้ไขการจอง: เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม [S1]

**New:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**Source records:** `migrated_faq_rule_edit_booking`

### 15. 96f755fd0f43b27fc5299d4357dcddc318809e699e062c341e8fbcb25f17198a

ช่วยอ้างอิงข้อมูลที่ยืนยันได้: ทำจอยเกมพังต้องรับผิดชอบยังไง

**กลุ่ม:** wrong_domain_clarification

ทำจอยพังเป็นนโยบายบริการทั่วไป แต่newขอรายการแข่งขัน ไม่ใช่missing eventที่ผู้ใช้ต้องใส่

**Retained:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**New:** `missing_input`

กรุณาระบุรายการแข่งขันหรือฉบับกติกาที่ต้องการ เพื่อให้จับคู่กติกาที่ถามได้ตรงครับ

**Source records:** 

### 16. a635e4bd14ac41d41a2ad4e14bec6b72a4b7f8e3fa9c7add6747de323541aaff

ช่วยอ้างอิงข้อมูลที่ยืนยันได้: ใครรับผิดชอบค่าเสียหายเมื่อผู้ใช้ทำเก้าอี้พัง

**กลุ่ม:** shared_failure_different_layer

ความรับผิดชอบเก้าอี้พังไม่ตอบทั้งคู่ ต้องแยกการไม่รองรับoperationจากไม่มีข้อมูล

**Retained:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**New:** `missing_source`

ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้

**Source records:** 

### 17. b7317ee13433178c93f9dff62e62c2f310708a11788897173d5412e796a603fb

ใครมีสิทธิ์เข้าใช้บริการ

**กลุ่ม:** shared_failure_wording_only

สิทธิ์เข้าใช้บริการไม่ตอบทั้งคู่ ไม่อ้างว่าข้อมูลeligibilityไม่มี

**Retained:** `missing_source`

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**New:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**Source records:** 

### 18. 737ff3d31b174cda802050dc5c2d732fe5166938d56d7d69da6eef37131b703c

ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม

**กลุ่ม:** shared_failure_different_layer

Switchตก/ค่าปรับไม่สำเร็จทั้งคู่ ไม่สร้างค่าปรับเป็นตัวเลข

**Retained:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**New:** `missing_source`

ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้

**Source records:** 

### 19. 05a5f2936ac3bb678c0d07355485024155fdec4b7ca38fd9b39126e8b1042421

Could you please help me with this: How long do I have to pay after booking? Please answer briefly

**กลุ่ม:** source_backed_payment_gain

newอ่านpayment deadline10นาทีจากFAQที่มีอยู่ได้ ไม่ใช่ผลยืนยันรายการจ่ายเงินจริง

**Retained:** `missing_source`

The requested game, machine or topic is not identified. Please specify the target.

**New:** `answer`

Payment must be made immediately after booking. If payment is not made within 10 minutes, the booking is cancelled and a new booking is required. [S1]

**Source records:** `migrated_faq_rule_en_payment_deadline_natural`

### 20. a5cb9450a1fe2c15e2ce0815499137d929bc7867aaeeb5370590496a3a1d3d60

ขอใบเสร็จ ใบเสนอราคาหรือใบกำกับภาษีได้ไหม

**กลุ่ม:** critical_payment_regression

r114_q018ยืนยันใบเสร็จ/ใบเสนอราคา/ใบกำกับภาษีออกไม่ได้ retainedตอบครบชนิด แต่newทิ้งคำตอบหลังfield verifier

**Retained:** `answer`

ใบกำกับภาษี: ออกใบกำกับภาษีไม่ได้; คำตอบก่อนหน้าแยกระบุใบเสนอราคาและใบเสร็จออกไม่ได้เช่นกัน [S1]

**New:** `missing_source`

พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ

**Source records:** `r114_q018_owner_policy`

### 21. bf367f96c730d0bad6aac9fc5d51056cd53b64109cc86125acc9bd00ece91d02

ขอใบเสร็จ ใบเสนอราคาหรือใบกำกับภาษีได้ไหม ขอสรุปให้เข้าใจง่าย

**กลุ่ม:** critical_payment_regression

คำถามเดียวกับข้อก่อนเพิ่มstyle request; newยังทิ้งsourceที่ตอบได้ ต้องนับเป็นregressionแต่รายงานfamily exposureด้วย

**Retained:** `answer`

ใบกำกับภาษี: ออกใบกำกับภาษีไม่ได้; คำตอบก่อนหน้าแยกระบุใบเสนอราคาและใบเสร็จออกไม่ได้เช่นกัน [S1]

**New:** `missing_source`

พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ

**Source records:** `r114_q018_owner_policy`

### 22. d124ad3e74129dfb23b187ec42990ed8bd76eaad6d61d0338f5f2092518340a7

นายเป็นใคร

**กลุ่ม:** shared_general_failure

คำถามตัวตนassistantไม่ตอบทั้งคู่ ไม่ใช่ขาดข้อมูลธุรกิจ

**Retained:** `missing_source`

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**New:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**Source records:** 

### 23. d609346eaf11a47a9980fb704d0eaeeaf6c4cc41607f306ee81240bd5ecfcdc7

ช่วยอ้างอิงข้อมูลที่ยืนยันได้: คุณเปนผู้ช่วยอะไร

**กลุ่ม:** shared_general_failure

คำถามassistantมีtypoไม่ตอบทั้งคู่

**Retained:** `missing_source`

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**New:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**Source records:** 

### 24. 54f35458b485875def6e85593a04d7a4b4cb681ee06980ba7f0ef4bddd346959

เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบ bullet สั้น ๆ

**กลุ่ม:** shared_general_failure

คำขอเขียนประชาสัมพันธ์ไม่มีevent context ทั้งคู่ไม่ตอบ แต่newข้อความunsupportedต่างจากmissing entity

**Retained:** `missing_source`

ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม

**New:** `missing_source`

ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้

**Source records:** 

### 25. 95e528d34c8549076003e5e2e4b072acd38a0e13f79f34fe4df394fca8874f30

Write one polite promotional sentence for the event. Keep it under three lines.

**กลุ่ม:** shared_general_failure

คำขอประชาสัมพันธ์ภาษาอังกฤษไม่สำเร็จทั้งคู่

**Retained:** `missing_source`

The requested game, machine or topic is not identified. Please specify the target.

**New:** `missing_source`

No confirmed source is available for the requested detail.

**Source records:** 

### 26. 66e52baea0ccf04da46543d4c74b7f87cad19cc4610ba83eadda25b3e876c699

หวัดดี

**กลุ่ม:** shared_general_failure

greetingถูกตอบเป็นunsupported/missing_sourceทั้งคู่ ไม่ถือเป็นcontent accuracyที่ดี

**Retained:** `missing_source`

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**New:** `missing_source`

ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้

**Source records:** 

### 27. 3df1eea3e83aa3fb059025c57f1a6063ac223379a543d818ffc26146c42c59ae

Please answer from verified studio information: Which zone has the Gaming Chair

**กลุ่ม:** known_source_refusal_regression

equipment_gaming_chair.locationคือPC Zone แต่newจัดเป็นgame relationและไม่ตอบ

**Retained:** `answer`

**Gaming Chair**
**location**: PC Zone [S1]

**New:** `missing_source`

No confirmed source is available for the requested detail.

**Source records:** `equipment_gaming_chair`

### 28. 9f2a7381272db47963c34abcc12f185377b7cab91156934e453aae543111cde3

CS2 แข่งรูปแบบอะไร

**กลุ่ม:** actual_requested_predicate_failure

ถามรูปแบบการแข่งขันCS2 แต่newตอบแนวเกมTacticalFPS เป็นคนละpredicate/source kindแม้genre valueมีsourceจริง; ไม่ให้เครดิตanswer status

**Retained:** `unavailable`

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

**New:** `answer`

**Counter-Strike 2**
**แนวเกม**: เกมยิง Tactical FPS [S1]

**Source records:** `game_detail_cs2`

### 29. 51b1bf0667aee428b95b3a5c021d247359cc0e220ae22856a27bd190f4c04f78

Please retrieve the official CS2 rulebook evidence for eligibility, roster, and registration

**กลุ่ม:** shared_rule_retrieval_failure

CS2eligibility/roster/registrationไม่ตอบทั้งคู่ ต้องอ่านsource clausesเพื่อแก้ ไม่เรียกว่าno-dataจากstatus

**Retained:** `unavailable`

The checking service is unavailable; this detail cannot be confirmed.

**New:** `missing_source`

The reader does not support the requested operation, so this part cannot be confirmed.

**Source records:** 

### 30. 1e48171bc6215d3060026dcf5d0bdb6a9911a8239a468693d9594452553e7fb0

ขอสอบถามหน่อยครับ กติกา CS2 เรื่องข้อกำหนดก่อนแข่งและหน้างาน ว่าอย่างไร

**กลุ่ม:** shared_rule_retrieval_failure

ข้อกำหนดก่อนแข่ง/หน้างานไม่ตอบทั้งคู่ ต่างfailure layer

**Retained:** `unavailable`

ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

**New:** `missing_source`

ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้

**Source records:** 

### 31. ef5c0b5af4c6794d174d9a9d329fe7e2535c1fac26b3cf0fd1d69f084d64ca96

Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?

**กลุ่ม:** model_timeout_plus_domain_error

newมีTimeoutError60วินาทีที่evidence_selectionจริง และcompiledเป็นC05controlsแทนC13rule settings จึงแยกtransportจากwrong-domain ไม่เหมารวมเป็นcontent hallucination

**Retained:** `missing_source`

The requested game, machine or topic is not identified. Please specify the target.

**New:** `unavailable`

The checking service is unavailable; this detail cannot be confirmed.

**Source records:** 

## ปัญหาร่วมที่ห้ามปิดบัง

ทั้งสองแขนยังมีrule retrieval failures, timetable/eligibility/contact/paraphrase misses, duplicated policy conflictsจากข้อความต่างรูป, missing needsในคำถามหลายส่วน, greeting/general handling และselector timeout/contract failures Source-verifier fatal0ยืนยันเพียงกลไกหลักฐาน ไม่ยืนยันว่าเลือกpredicateหรือคำตอบถูกครบ

Engine replayไม่ครอบคลุมnative API pathทุกเส้นทาง จึงต้องตรวจfinal APIและFull Testจริงต่อ ไม่ใช้ข้อสันนิษฐานว่าAPIอาจตอบถูกเพื่อลบregressionในชุดนี้ ไม่ใช้Full Testเป็นproduction approval

## หลักฐาน

- ADJUDICATION_ALL_110_CASES.jsonl: gold needsและคำตอบทั้งสองแขนครบ110คู่
- ADJUDICATION_REVIEW.json:31กรณีและเหตุผลแยกกลุ่ม
- ADJUDICATION_SOURCE_EVIDENCE.json: record revision/fields/pointer values/source SHA256
- paired_replay03/RESULTS.jsonl และ RUN_FREEZE.json
- RAW_PROTOCOL_REVIEW_TH.md และ RAW_PROTOCOL_REVIEW.json

