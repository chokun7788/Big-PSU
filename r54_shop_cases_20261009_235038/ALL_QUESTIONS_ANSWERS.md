# คำถามและคำตอบจริงของชุดบริการ r54

156 คำถาม + ตรวจ CS2 pagination เพิ่ม เก็บคำตอบทั้งหมดและlogเดิม คำอธิบายผลในanalysis.json/case_index.csv เป็นการอ่านวิเคราะห์ของagent ไม่ใช่การยืนยันนโยบายใหม่จากเจ้าของ คำอธิบายเชิงเทคนิคในตารางใช้ศัพท์อังกฤษ/จีนบางส่วน

## c001: ที่นี่เป็นร้านเกมทั่วไปหรือของมหาวิทยาลัย

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 2.97s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

PSU Esports Studio - Phuket เป็นศูนย์ของมหาวิทยาลัยสงขลานครินทร์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c002: Is this a university facility or a regular gaming cafe?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 2.70s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

PSU Esports Studio - Phuket is a university facility of Prince of Songkla University.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c003: ต้องเป็นสมาชิกก่อนเล่นไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 1.03s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c004: Do I need membership to use the studio?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 1.32s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Membership is not required to use the studio.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c005: ไปนั่งดูเพื่อนเล่นเฉยๆได้ไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 1.15s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

สามารถมานั่งดูเพื่อนเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c006: Can I sit and watch my friend play?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 2.09s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

You may sit and watch your friends play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c007: เดินเข้าไปเล่นเลยได้ไหม ต้องจองไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 1.04s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c008: Can I walk in without booking?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.83s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Walk-in visitors must still book through the reservation system before using the service.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c009: ศูนย์อยู่ตึกไหน ชั้นอะไร

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.74s
- ผล: PASS_FORMAT
- วิเคราะห์: 答案与owner source一致，只因83120后空格导致原始exact-match报警；忽略空白后通过。

### คำตอบจริง

ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c010: Which building and floor is the studio in?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.73s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

The studio is in Building 5, Floor 1, Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c011: ขอลิงก์แผนที่ศูนย์หน่อย

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.73s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ลิงก์แผนที่ศูนย์: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c012: Can I have the studio map link?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.54s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Studio map: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c013: มีที่จอดรถยนต์กับมอเตอร์ไซค์ไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.60s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c014: Is there parking for cars and motorcycles?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.82s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c015: หาศูนย์ไม่เจอ ติดต่อใครได้

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.54s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ติดต่อผ่านเพจศูนย์อีสปอร์ตได้ครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c016: Who can I contact if I cannot find the studio?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.61s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Contact the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c017: มากันสี่คนควรเลือกเครื่องไหน

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.56s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

มากัน 4 คน แนะนำ Nintendo Switch ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c018: What should a group of four choose?

- หมวด/ภาษา: policy / en
- mode: pipeline:english_no_answer
- เวลา: 1.06s
- ผล: FAIL_INTENT
- วิเคราะห์: 四人选择问题未匹配four_people；pattern只含four people/four of us和有限中文动作词，漏group of four/4 ppl/玩哪个等表达。应按owner回答Nintendo Switch。

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for this question.

## c019: จองชื่อเราแต่ให้เพื่อนที่ไม่มีชื่อเล่นแทนได้ไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:request_timeout_no_answer
- เวลา: 19.12s
- ผล: FAIL_TIMEOUT
- วิเคราะห์: 未在deadline内回答。owner已给出named-player policy，实际只返回timeout；response无完整stage trace，不能确认是哪次模型调用耗时。

### คำตอบจริง

ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง
ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ

## c020: Can a friend who is not named in my booking play instead?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.62s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

The player must be the person who booked or be named in the booking. Someone not listed cannot use the booking instead.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c021: ตอนมาถึงต้องแสดงบัตรอะไร

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.57s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

เมื่อมาถึงให้แสดงบัตรประชาชน บัตรนักศึกษา บัตรนักเรียน หรือ Passport อย่างใดอย่างหนึ่งครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c022: What ID should I show when I arrive?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.54s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c023: จองผิดเครื่องต้องแก้ยังไง

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.54s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c024: How do I change a booking for the wrong machine?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.80s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

If you booked the wrong machine, cancel through the email and make a new booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c025: เปลี่ยนเวลาจองทำยังไง

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.59s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

หากต้องการเปลี่ยนเวลาจอง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c026: How can I change my booking time?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.60s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

To change the booking time, cancel through the email and make a new booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c027: เอาคีย์บอร์ดหรือเมาส์ตัวเองมาใช้ได้ไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.81s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c028: Can I bring my own keyboard or mouse?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.59s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c029: แนบสลิปผิดรูปต้องทำยังไง

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.58s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c030: What should I do if I uploaded the wrong payment slip?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.55s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c031: จองหลายเครื่องโอนครั้งเดียวได้ไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.92s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c032: Can I make one bank transfer for several machines?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.88s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

You may make one bank transfer for multiple machines, but you must add a note when booking so the studio can verify it.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c033: มาถึงก่อนเพื่อนเช็กอินแทนทั้งกลุ่มได้ไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 0.89s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

เช็กอินแทนทั้งกลุ่มไม่ได้ ศูนย์ตรวจเป็นรายคน แต่คนที่มาก่อนสามารถเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c034: Can I check in for my whole group before my friends arrive?

- หมวด/ภาษา: policy / en
- mode: pipeline:user_service_facts
- เวลา: 0.59s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

You cannot check in for the whole group. Each person is checked individually, but those who arrive first may play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c035: มีที่นั่งพักรอเพื่อนไหม

- หมวด/ภาษา: policy / th
- mode: pipeline:user_service_facts
- เวลา: 2.19s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

มีที่นั่งพักตรงโซนกลางห้องครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c036: Is there seating where I can rest while waiting for friends?

- หมวด/ภาษา: policy / en
- mode: pipeline:games_unknown_target_en
- เวลา: 2.14s
- ผล: FAIL_INTENT
- วิเคราะห์: 休息座位有owner source，却未匹配rest_seating；英文被当游戏标题，中文返回泛化澄清。应回答中央休息区；不能据此确认特定booking等候点。

### คำตอบจริง

I could not find seating where I can rest while waiting for friends in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

## c037: ต้องสมัคสมาชิกก่อนไหม

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.57s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c038: do i need a memebrship first

- หมวด/ภาษา: policy_variant / en
- mode: pipeline:user_service_facts
- เวลา: 0.60s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Membership is not required to use the studio.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c039: แค่มาดูเพื่อนได้ปะ ไม่เล่น

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.55s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

สามารถมานั่งดูเพื่อนเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c040: can i just watch my freind

- หมวด/ภาษา: policy_variant / en
- mode: pipeline:user_service_facts
- เวลา: 0.40s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

You may sit and watch your friends play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c041: ไม่ได้จองมา เดินเข้าได้ปะ

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.54s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c042: can i walkin and play straight away

- หมวด/ภาษา: policy_variant / en
- mode: pipeline:user_service_facts
- เวลา: 0.57s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Walk-in visitors must still book through the reservation system before using the service.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c043: อยู่ตึกไร ชั้นไหนอ่ะ

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.56s
- ผล: PASS_FORMAT
- วิเคราะห์: 答案与owner source一致，只因83120后空格导致原始exact-match报警；忽略空白后通过。

### คำตอบจริง

ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c044: มอไซจอดไหน มีที่จอดปะ

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.57s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c045: มา4คน เล่นอันไหนดี

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:general_rag_miss_llm_unavailable
- เวลา: 18.02s
- ผล: FAIL_INTENT
- วิเคราะห์: 四人选择问题未匹配four_people；pattern只含four people/four of us和有限中文动作词，漏group of four/4 ppl/玩哪个等表达。应按owner回答Nintendo Switch。

### คำตอบจริง

การสร้างคำตอบใช้เวลาเกินเวลาที่ระบบกำหนดครับ กรุณาลองคำถามที่สั้นลง

## c046: we are 4 ppl what can we play

- หมวด/ภาษา: policy_variant / en
- mode: pipeline:english_no_answer
- เวลา: 1.13s
- ผล: FAIL_INTENT
- วิเคราะห์: 四人选择问题未匹配four_people；pattern只含four people/four of us和有限中文动作词，漏group of four/4 ppl/玩哪个等表达。应按owner回答Nintendo Switch。

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for this question.

## c047: เพื่อนไม่มีชื่อในจอง เล่นแทนได้มะ

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:semantic_rag_dynamic
- เวลา: 6.23s
- ผล: PASS_EQUIVALENT
- วิเคราะห์: 提问限定无名朋友代玩，答不可转让与该上下文的owner禁止条件一致；未评价其他有名队友的情况。

### คำตอบจริง

ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c048: ไปถึงต้องเอาบัตรไรไปมั่ง

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:candidate_margin_clarification
- เวลา: 8.21s
- ผล: FAIL_INTENT
- วิเคราะห์: 证件问题有source，口语/拼错documents未进checkin_documents，而进入clarification/no_answer。

### คำตอบจริง

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

## c049: which documnts do i bring for checkin

- หมวด/ภาษา: policy_variant / en
- mode: pipeline:english_no_answer
- เวลา: 1.11s
- ผล: FAIL_INTENT
- วิเคราะห์: 证件问题有source，口语/拼错documents未进checkin_documents，而进入clarification/no_answer。

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for reservation.

## c050: จองผืดเครื่อง เปลี่ยนไง

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.57s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c051: อยากเปลี่ยนรอบที่จอง ต้องทำไง

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:rag_direct_curated
- เวลา: 2.11s
- ผล: SOURCE_REVIEW
- วิเคราะห์: 旧rule source提供取消重订和至少1小时前、原slip；latest owner回答仅确认取消重订。答案主步骤相符，但source条件版本需协调，不能称为凭空编造。

### คำตอบจริง

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c052: เอาเม้าส์ตัวเองไปเสียบได้ปะ

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.58s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c053: can i use my own keybaord

- หมวด/ภาษา: policy_variant / en
- mode: pipeline:user_service_facts
- เวลา: 0.55s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c054: อัพสลิปผืด ส่งใหม่ทางไหน

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:rag_direct_curated
- เวลา: 1.87s
- ผล: FAIL_WRONG_POLICY
- วิเคราะห์: 错误slip应发Facebook page；却返回取消booking再重订旧rule。

### คำตอบจริง

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c055: จอง3เครื่อง จ่ายรวมทีเดียวได้ปะ

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:user_service_facts
- เวลา: 0.30s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c056: เพื่อนยังมาไม่ถึง เช็คอินให้ทั้งแก๊งได้ไหม

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:protected_checkin_required
- เวลา: 0.80s
- ผล: FAIL_WRONG_POLICY
- วิเคราะห์: 代全组checkin应回答逐人检查/先到者可玩；却答一般checkin时间及证件。

### คำตอบจริง

ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c057: มีตรงให้นั่งรอมั้ย

- หมวด/ภาษา: policy_variant / th
- mode: pipeline:candidate_margin_clarification
- เวลา: 1.38s
- ผล: FAIL_INTENT
- วิเคราะห์: 休息座位有owner source，却未匹配rest_seating；英文被当游戏标题，中文返回泛化澄清。应回答中央休息区；不能据此确认特定booking等候点。

### คำตอบจริง

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

## c058: ราคา PC บุคคลทั่วไป

- หมวด/ภาษา: price_budget / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.30s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c059: PC prices for general adults

- หมวด/ภาษา: price_budget / en
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.30s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Service prices (recorded package rates):

PC — 60 minutes/package (1 person)
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

## c060: เป็นบุคคลทั่วไป เล่น PC 2 ชั่วโมงเท่าไหร่

- หมวด/ภาษา: price_budget / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.29s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
ระยะเวลาที่ถาม 120 นาที (2 ชั่วโมง) คิดเป็น 2 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ × 2 = 140 บาท
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c061: General adult PC for two hours, how much?

- หมวด/ภาษา: price_budget / en
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.33s
- ผล: FAIL_FILTERS
- วิเคราะห์: request_plan把General adult及two hours丢失，customer_scope=unspecified、duration_minutes=null，回答全部人群每小时价格。应70×2=140 THB。

### คำตอบจริง

Service prices (recorded package rates):

PC — 60 minutes/package (1 person)
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

## c062: มี 100 บาท เป็นบุคคลทั่วไป เล่น PC ได้กี่ชั่วโมง

- หมวด/ภาษา: price_budget / th
- mode: pipeline:deterministic_calculator_fast
- เวลา: 3.73s
- ผล: FAIL_BUDGET
- วิเคราะห์: 没有budget allocation路径。中文只报70/小时，英文What can I play触发games catalog，未按100baht筛选/算可负担session。PC General Adult100baht应1个60分钟package，余30baht（按记录价）。

### คำตอบจริง

ราคา PC 1 ชั่วโมง สำหรับ General Adult / บุคคลทั่วไป: 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

## c063: I am a general adult with 100 baht. What can I play?

- หมวด/ภาษา: price_budget / en
- mode: pipeline:structured_games_catalog_en
- เวลา: 1.89s
- ผล: FAIL_BUDGET
- วิเคราะห์: 没有budget allocation路径。中文只报70/小时，英文What can I play触发games catalog，未按100baht筛选/算可负担session。PC General Adult100baht应1个60分钟package，余30baht（按记录价）。

### คำตอบจริง

There are currently 42 verified games available.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 games)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 games)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 game)
•    Gran Turismo 7

VR Zone (4 games)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

## c064: มา4คนเล่น Nintendo 1 ชั่วโมง บุคคลทั่วไปเท่าไหร่

- หมวด/ภาษา: price_budget / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.30s
- ผล: PASS_RECORDED
- วิเคราะห์: Nintendo3-4people generaladult记录价280/60min，正确标明原表到2026-03-31；本测试不确认现价续期。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
ระยะเวลาที่ถาม 60 นาที (1 ชั่วโมง) คิดเป็น 1 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

## c065: ขอตารางราคาทุกบริการบุคคลภายนอก

- หมวด/ภาษา: price_budget / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.31s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (1-2 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 140 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ

Cockpit — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 65 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 200 บาท/แพ็กเกจ

VR — 30 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 525 บาท/แพ็กเกจ

VR — 60 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 1,050 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c066: All service prices for external users

- หมวด/ภาษา: price_budget / en
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.31s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package

PlayStation 5 — 60 minutes/package (1-2 people)
• PSU alumni / students from other institutions: 50 THB/package
• General adults: 150 THB/package

Nintendo Switch — 60 minutes/package (1-2 people)
• PSU alumni / students from other institutions: 50 THB/package
• General adults: 140 THB/package

Nintendo Switch — 60 minutes/package (3-4 people)
• PSU alumni / students from other institutions: 100 THB/package
• General adults: 280 THB/package

Cockpit — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 65 THB/package
• General adults: 200 THB/package

VR — 30 minutes/package (1-5 people)
• PSU alumni / students from other institutions: 190 THB/package
• General adults: 525 THB/package

VR — 60 minutes/package (1-5 people)
• PSU alumni / students from other institutions: 375 THB/package
• General adults: 1,050 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
PC rates use the local update dated 2026-07-27.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
Source: local://service_fee/pc_price_update_20260727

## c067: หน่วยงานภายนอกเหมา PC เต็มวันราคาเท่าไหร่

- หมวด/ภาษา: rental / th
- mode: pipeline:zone_rental_fee
- เวลา: 0.30s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาเช่าเหมาโซนสำหรับหน่วยงาน

**PC Zone**
•    หน่วยงานภายนอก: เต็มวัน 4,000 บาท
•    รองรับ: 43 ที่นั่ง; อุปกรณ์: PC 10 เครื่อง

อัตรานี้เป็นราคาเช่าเหมาโซนของหน่วยงาน ไม่ใช่ราคาต่อผู้เล่น/เครื่อง ไฟล์ไม่ได้ระบุจำนวนชั่วโมงของช่วงเช่าหรือวันที่มีผลของอัตรา

แหล่งข้อมูล: ไฟล์ค่าบริการครึ่งวันและเต็มวันที่ผู้ใช้ส่งให้
local://service_fee/zone_rental_fees_20261006

## c068: PC whole-day rental price for external organizations

- หมวด/ภาษา: rental / en
- mode: pipeline:zone_rental_fee
- เวลา: 0.28s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c069: หน่วยงานภายนอกเหมาทุกโซน ครึ่งวันกับเต็มวันราคาเท่าไหร่

- หมวด/ภาษา: rental / th
- mode: pipeline:zone_rental_fee
- เวลา: 0.35s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาเช่าเหมาโซนสำหรับหน่วยงาน

**All Zones**
•    หน่วยงานภายนอก: ครึ่งวัน 6,000 บาท / เต็มวัน 12,000 บาท
•    รองรับ: 50 ที่นั่ง; อุปกรณ์: อุปกรณ์เกมทั้งหมด

อัตรานี้เป็นราคาเช่าเหมาโซนของหน่วยงาน ไม่ใช่ราคาต่อผู้เล่น/เครื่อง ไฟล์ไม่ได้ระบุจำนวนชั่วโมงของช่วงเช่าหรือวันที่มีผลของอัตรา
ค่าตอบแทนของเจ้าหน้าที่ทำงานนอกเวลาเบิกตามระเบียบมหาวิทยาลัย

แหล่งข้อมูล: ไฟล์ค่าบริการครึ่งวันและเต็มวันที่ผู้ใช้ส่งให้
local://service_fee/zone_rental_fees_20261006

## c070: Compare PC full-day rental external organizations with VR half-day internal organizations

- หมวด/ภาษา: rental / en
- mode: pipeline:zone_rental_fee
- เวลา: 0.37s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Zone rental fees for organizations

**VR Zone**
• Internal organizations: half day 1,500 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c071: เหมาครึ่งวันคือกี่ชั่วโมง

- หมวด/ภาษา: rental / th
- mode: pipeline:zone_rental_fee
- เวลา: 0.30s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 正确不猜缺失的rental hours或不存在的PS55费率。

### คำตอบจริง

ราคาเช่าเหมาโซนสำหรับหน่วยงาน

ไฟล์ไม่ได้ระบุว่าครึ่งวัน/เต็มวันนับกี่ชั่วโมงหรือเริ่ม–สิ้นสุดกี่โมง ต้องยืนยันช่วงเวลาเช่าเหมาจากศูนย์ครับ

แหล่งข้อมูล: ไฟล์ค่าบริการครึ่งวันและเต็มวันที่ผู้ใช้ส่งให้
local://service_fee/zone_rental_fees_20261006

## c072: Can I rent PS55 for a full day?

- หมวด/ภาษา: rental / en
- mode: pipeline:zone_rental_fee
- เวลา: 0.36s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 正确不猜缺失的rental hours或不存在的PS55费率。

### คำตอบจริง

Zone rental fees for organizations

No rental rate is recorded for these requested targets: ps55

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c073: PC มีเกมอะไรบ้าง ขอทั้งหมด

- หมวด/ภาษา: games / th
- mode: pipeline:structured_service_game_availability
- เวลา: 0.81s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c074: What games are available on PC? List all of them.

- หมวด/ภาษา: games / en
- mode: pipeline:structured_games_catalog_en
- เวลา: 0.55s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

## c075: Nintendo มีเกมไรมั่ง

- หมวด/ภาษา: games / th
- mode: pipeline:game_target_ambiguous
- เวลา: 0.54s
- ผล: FAIL_CATALOG
- วิเคราะห์: Nintendo/Cockpit游戏列表请求被当成未知游戏/没有答案；已存在按zone的catalog。

### คำตอบจริง

ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน
กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

## c076: What games can I play on Nintendo Switch?

- หมวด/ภาษา: games / en
- mode: pipeline:structured_games_catalog_en
- เวลา: 0.56s
- ผล: PASS_CATALOG
- วิเคราะห์: 命中正确zone游戏列表；不代表现场每台都安装/已更新。

### คำตอบจริง

There are currently 17 verified games in Nintendo Switch Zone.

Nintendo Switch Zone (17 games)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

## c077: PS5 มีเกมไรบ้าง

- หมวด/ภาษา: games / th
- mode: pipeline:structured_service_game_availability
- เวลา: 0.58s
- ผล: PASS_CATALOG
- วิเคราะห์: 命中正确zone游戏列表；不代表现场每台都安装/已更新。

### คำตอบจริง

PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้

PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection
หมายเหตุ: PlayStation 5 #01 และ #02 ใช้รายการเกมเดียวกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c078: Cockpit เล่นเกมอะไร

- หมวด/ภาษา: games / th
- mode: pipeline:no_answer
- เวลา: 13.04s
- ผล: FAIL_CATALOG
- วิเคราะห์: Nintendo/Cockpit游戏列表请求被当成未知游戏/没有答案；已存在按zone的catalog。

### คำตอบจริง

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

## c079: VR มีเกมอะไรบ้าง

- หมวด/ภาษา: games / th
- mode: pipeline:structured_service_game_availability
- เวลา: 0.60s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

VR Station มีเกมที่ยืนยันได้ดังนี้ (รอบ 30 นาทีและ 1 ชั่วโมงใช้รายการเกมเดียวกัน)

VR Station 30 นาที (30 นาที, 1-5 คน)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
หมายเหตุ: VR Station แบบ 30 นาทีและ 1 ชั่วโมงใช้รายการเกมเดียวกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c080: ที่ศูนย์มีเกมให้เล่นทั้งหมดกี่เกม

- หมวด/ภาษา: games / th
- mode: pipeline:hybrid_guarded_rerank
- เวลา: 6.16s
- ผล: FAIL_AGGREGATE
- วิเคราะห์: ถามจำนวน游戏总数却检索到Naruto单条描述。应该从游戏catalog按去重口径计算并说明zone重复。

### คำตอบจริง

Naruto X Boruto Ultimate Ninja Storm Connections: สัมผัสกับเนื้อเรื่องของ Naruto และ Sasuke อย่างเต็มรูปแบบเป็นครั้งแรกในการเฉลิมฉลองครบรอบ 20 ปีการเปิดตัวอนิเมะ Naruto ที่ครอบคลุมไปทั้งหมดนี้ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ปล่อยให้คุณได้สัมผัสกับพลังของ Ninjutsu อย่างที่ไม่เคยมีมาก่อน โดยมีนักสู้ที่สามารถเล่นได้จำนวนมากกว่า 130 ตัว เชี่ยวชาญกลไกการต่อสู้ที่อัพเดตในโหมดการต่อสู้ออฟไลน์และออนไลน์ที่น่าตื่นเต้นจำนวนมากมาย...
อยู่ในรายการเกมหน้า Our Games ส่วน: PlayStation 5
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games, https://esports.phuket.psu.ac.th/home

## c081: กฏตอนเเข่ง cs2 มีอะไรมั่ง

- หมวด/ภาษา: competition / th
- mode: pipeline:competition_rule_overview_source
- เวลา: 0.87s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

## c082: กฏตอนเเข่ง rov มีอะไรมั่ง

- หมวด/ภาษา: competition / th
- mode: pipeline:competition_rule_overview_source
- เวลา: 1.08s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

สรุปกติกา Arena of Valor (RoV) บางประเด็นจากเอกสารที่มี:
รายการ: Blueket Games 2025 ประเภททีมชาย

**รูปแบบการแข่งขัน**
•    เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
•    เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3

**คุณสมบัติและการลงทะเบียน**
•    6.1.3.ห้ามทีมผู้เข้าแข่งขันทุกทีมอนุญาตให้บุคคลอื่นที่ไม่ได้อยู่ในรายชื่อผู้เข้าแข่งขันในทีมของตนตามที่ได้ลงทะเบียนไว้เข้าแข่งขันโดยเด็ดขาด หากพบว่ามีชื่อผู้เข้าแข่งขันไม่ตรงตามที่ลงทะเบียนไว้ ให้ทำการบันทึกภาพหลักฐานและยุติการแข่งขันในทันที แต่หากมีการแข่งขันจนจบเกม จะถือว่าทั้งสองทีมยินยอมให้เกิดการแข่งขันขึ้น ทางทีมงานจะไม่รับฟังข้อโต้แย้งใด ๆ ทั้งสิ้น

**อุปกรณ์การแข่งขัน**
•    5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที

**การหยุดเกมและเวลานอก**
•    4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ
•    4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
•    4.5.6.1. ผู้เข้าแข่งขันอาจหยุดพักเกมการแข่งขันได้ภายหลังจากเกิดเหตุการณ์ใดเหตุการณ์หนึ่งดังต่อไปนี้ โดยผู้เข้าแข่งขันดังกล่าวจะต้องส่งสัญญาณให้ผู้ตัดสินทราบโดยทันทีภายหลังจากการหยุดเกมและชี้แจงเหตุผลแห่งการหยุดเกมดังกล่าว

**บทลงโทษ**
•    4.6.3.1. ครั้งที่ 1: ตักเตือน

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

## c083: กฏตอนเเข่ง tekken 8 มีอะไรมั่ง

- หมวด/ภาษา: competition / th
- mode: pipeline:competition_rule_overview_source
- เวลา: 0.59s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

สรุปกติกา Tekken 8 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Esports ปะทะมันส์ สนั่นจอ

**รูปแบบการแข่งขัน**
•    แข่งขันแบบ เดี่ยว (1v1)
•    FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน

**การตั้งค่าแมตช์**
•    จำนวนรอบต่อเกม (Round): 3
•    เวลาแข่งขันต่อรอบ (Timer): 60 วินาที

**การหยุดเกมและเวลานอก**
•    เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
•    หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที
•    การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน

**ข้อห้ามและพฤติกรรม**
•    ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
•    ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น

เอกสารมีทั้งข้อห้ามหยุดเกมและข้อยกเว้นกรณีฉุกเฉิน/ผู้เล่นเห็นพ้อง ต้องให้ผู้จัดยืนยันขอบเขตและบทลงโทษที่ใช้ครับ

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

## c084: กฏตอนแข่งวาโลมีอะไรมั่ง

- หมวด/ภาษา: competition / th
- mode: pipeline:competition_rule_overview_source
- เวลา: 0.88s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

สรุปกติกา VALORANT บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket VALORANT 2026 Tournament

**อุปกรณ์การแข่งขัน**
•    ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม
•    เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น

**ก่อนแข่งและหน้างาน**
•    จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
•    อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**

**1. เวลานอกทางยุทธวิธี (Tactical Timeout)**
•    ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
•    เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

**2. การหยุดเกมทางเทคนิค (Technical Pause)**
•    ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์
•    ห้ามผู้เล่นสื่อสารกัน (ทั้งเสียงและข้อความ) เว้นแต่ได้รับอนุญาต

**3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)**
•    ขอได้ 1 ครั้งต่อแผนที่
•    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน

**บทลงโทษ**
•    3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026

## c085: ขอกฎการแข่งขัน CS2 ทั้งหมดทุกหัวข้อ

- หมวด/ภาษา: competition / th
- mode: pipeline:competition_rule_full_sections_source
- เวลา: 0.59s
- ผล: PARTIAL_PAGE
- วิเคราะห์: CS2 full rules返回8/56部分，明确标记partial；target命中并不代表all coverage通过。后续分页另测失败。

### คำตอบจริง

กติกา Counter-Strike 2: รายละเอียดจากเอกสารที่บันทึกไว้ (แสดงแล้ว 8/56 ส่วน)

•    ข้อมูลทั่วไป (General Information)

•    ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

•    เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

•    ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

•    การจับฉลากและตารางเวลา

•    การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

•    การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

•    ข้อจำกัด

ยังเหลือ 48 ส่วน พิมพ์ “ต่อ” เพื่อดูหน้าถัดไปครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

## c086: All documented competition rules for Tekken 8

- หมวด/ภาษา: competition / en
- mode: pipeline:competition_rule_full_sections_source
- เวลา: 0.59s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Tekken 8: detailed sections from the recorded rulebook (7/7 sections covered).

Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S rule (60 seconds per round) * If tied at 1-1, a deciding game will be played

Characters and Setup * Any character can be selected (except DLC characters) * No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.) * Only standard skins are permitted * Assist buttons or special assist systems are allowed * No use of bugs or glitches that provide an advantage * Once the game starts, no game pausing for any reason is permitted * Any intentional game pause will result in a penalty of losing one round immediately

Game settings
* Rounds per game (Round): 3
* Time per round (Timer): 60 seconds
* Advantage: No advantage
* Stage: Random

Competition etiquette
* Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.
* Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception.

Agreements and conduct
* Competitors must accept and follow the rules, regulations, and referees' decisions unconditionally.
* Organizers may change competition rules at any time without prior notice.
* Referees' decisions are final.
* Referees may reconsider decisions as appropriate to ensure fairness.

Game Pause * Players must not leave the game before the competition ends unless authorized by the referees. * If a player leaves the game without authorization, they will be forfeited immediately. * The game may be paused only when all players agree and there is a valid reason, such as equipment malfunction or an emergency. * Pausing the game without necessity will result in the same penalty as leaving the game prematurely.

Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice.
All readable recorded sections have been covered; this does not confirm rules for a new event.
The source has conflicting pause conditions; the organizer must confirm their application.
Source: local://competition_rules/competition_rules_tekken8_psu_esports

## c087: What are the ROV tournament rules?

- หมวด/ภาษา: competition / en
- mode: pipeline:competition_rule_overview_source
- เวลา: 0.82s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Selected Arena of Valor (RoV) competition rules from the recorded rulebook:
Tournament: Arena of Valor (RoV) / 2025


**Competition format**
•    08:40-10:00: round of 5 teams, Single Elimination BO3
•    10:00-11:30: semifinal match 1, Single Elimination BO3

**Competition equipment**
•    5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.

**Pauses and timeouts**
•    4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.
•    4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.
•    4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
•    4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.

**Penalties**
•    6.2.4.1. Penalty: If staff verify such violations or receive complaints from others, staff will impose penalties on offending competitors by disqualifying them from the competition.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_rov_blueket_2025_men

## c088: กฎแข่ง CS2 ปี 2030

- หมวด/ภาษา: competition / th
- mode: pipeline:competition_rule_detail_no_answer
- เวลา: 0.29s
- ผล: SAFE_EDITION
- วิเคราะห์: 正确拒绝拿2026文档确认2030规则。

### คำตอบจริง

เอกสารกติกาที่มีระบุปี 2026 จึงยังยืนยันกติกาฉบับปี 2030 ที่ถามไม่ได้ ต้องขอเอกสารฉบับปีนั้นจากผู้จัดก่อนครับ

## c089: ตอนนี้ PC ว่างไหม

- หมวด/ภาษา: live_booking / th
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.88s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: WordPress live path有timestamp并返回closed/history状态，但未用同一timestamp外部ground truth逐slot比对；不等同availability accuracy确认。

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
โซน PC: ว่าง 0/10 รายการ ช่วง 23:53 น. เพราะศูนย์ปิดให้บริการ
•    PC #01 (1 Person): ปิดให้บริการ
•    PC #02 (1 Person): ปิดให้บริการ
•    PC #03 (1 Person): ปิดให้บริการ
•    PC #04 (1 Person): ปิดให้บริการ
•    PC #05 (1 Person): ปิดให้บริการ
•    PC #06 (1 Person): ปิดให้บริการ
•    PC #07 (1 Person): ปิดให้บริการ
•    PC #08 (1 Person): ปิดให้บริการ
•    PC #09 (1 Person): ปิดให้บริการ
•    PC #10 (1 Person): ปิดให้บริการ
อัปเดต: 2026-10-09 23:53:00
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c090: cockpik ว่างไหม

- หมวด/ภาษา: live_booking / th
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.91s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: WordPress live path有timestamp并返回closed/history状态，但未用同一timestamp外部ground truth逐slot比对；不等同availability accuracy确认。

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
โซน Cockpit: ว่าง 0/2 รายการ ช่วง 23:53 น. เพราะศูนย์ปิดให้บริการ
•    Cockpit #1 (1 Person): ปิดให้บริการ
•    Cockpit #2 (1 Person): ปิดให้บริการ
อัปเดต: 2026-10-09 23:53:02
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c091: วันนี้ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง

- หมวด/ภาษา: live_booking / th
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.60s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: WordPress live path有timestamp并返回closed/history状态，但未用同一timestamp外部ground truth逐slot比对；不等同availability accuracy确认。

### คำตอบจริง

วันที่ 2026-10-09 ช่วง 15:00-16:00 น. (เวลาไทย): ศูนย์ไม่เปิดให้บริการ จึงไม่มีอุปกรณ์ที่เปิดให้จองในช่วงนี้ครับ
อัปเดต: 2026-10-09 23:53:03
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c092: Which equipment is free today at 3 pm?

- หมวด/ภาษา: live_booking / en
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.65s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: WordPress live path有timestamp并返回closed/history状态，但未用同一timestamp外部ground truth逐slot比对；不等同availability accuracy确认。

### คำตอบจริง

At 2026-10-09, 15:00-16:00 (Asia/Bangkok), the studio is closed; no equipment is bookable then.
Updated: 2026-10-09 23:53:05
Source: https://esports.computing.psu.ac.th/reservation

## c093: Is PC1 free today at 10 am?

- หมวด/ภาษา: live_booking / en
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.64s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: WordPress live path有timestamp并返回closed/history状态，但未用同一timestamp外部ground truth逐slot比对；不等同availability accuracy确认。

### คำตอบจริง

Date: 2026-10-09 (Asia/Bangkok)
PC #01 (1 Person) had no booking during 10:00-11:00 (Asia/Bangkok).
Updated: 2026-10-09 23:53:06
Source: https://esports.computing.psu.ac.th/reservation

## c094: วันนี้ VR 9:00-9:30 ว่างไหม

- หมวด/ภาษา: live_booking / th
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.66s
- ผล: FAIL_TIME_ENTITY
- วิเคราะห์: VR紧跟9:00被_requested_resource_number的regex读成设备#9。不能把clock hour当机器编号。

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
ไม่พบ โซน VR เครื่อง #9 ใน Booking Dashboard ครับ
อัปเดต: 2026-10-09 23:53:08
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c095: เครื่องค้างระหว่างเล่น คืนเวลาให้ไหม

- หมวด/ภาษา: policy_boundary / th
- mode: pipeline:user_service_facts
- เวลา: 0.82s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。

### คำตอบจริง

กฎการจองที่บันทึกไว้เดิม: โดยทั่วไปไม่มีการคืนเงิน ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ
https://esports.computing.psu.ac.th/

ยังไม่ได้ยืนยันวิธีคิดหรือชดเชยเวลาที่เสียไปเมื่อเครื่องค้างหรือดับครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c096: Can I install a game that is not in your list?

- หมวด/ภาษา: policy_boundary / en
- mode: pipeline:user_service_facts
- เวลา: 0.87s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。

### คำตอบจริง

Permission to request additional games or install games, programs, or mods yourself has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c097: เอา Steam ตัวเองล็อกอินได้ไหม

- หมวด/ภาษา: policy_boundary / th
- mode: pipeline:candidate_margin_clarification
- เวลา: 7.99s
- ผล: FAIL_UNHELPFUL_CLARIFICATION
- วิเคราะห์: Steam个人账号使用policy尚未确认；应明确该字段未知而非泛化询问游戏/价格/设备。

### คำตอบจริง

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

## c098: If I arrive 15 minutes late, can I still play?

- หมวด/ภาษา: policy_boundary / en
- mode: pipeline:user_service_facts
- เวลา: 0.56s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。

### คำตอบจริง

Recorded booking rule: If users fail to check in before the reserved time slot begins, the booking will be automatically cancelled with no refund.
https://esports.computing.psu.ac.th/



No separate grace period or exception for arriving 15 minutes late has been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c099: เด็กอายุ10ขวบเล่นได้ไหม ต้องมีผู้ปกครองไหม

- หมวด/ภาษา: policy_boundary / th
- mode: pipeline:user_service_facts
- เวลา: 0.33s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。

### คำตอบจริง

ยังไม่ได้ยืนยันข้อกำหนดอายุและการมีผู้ปกครองสำหรับเด็กครับ การเปิดให้บุคคลทั่วไปใช้บริการยังใช้ยืนยันข้อนี้ไม่ได้

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c100: May I stream from a studio computer?

- หมวด/ภาษา: policy_boundary / en
- mode: pipeline:user_service_facts
- เวลา: 0.28s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。

### คำตอบจริง

Permission to stream from the studio machines has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c101: จ่ายแล้วจองผิดวัน เปลี่ยนวันกับขอเลื่อนแทนคืนเงินได้ไหม

- หมวด/ภาษา: policy_boundary / th
- mode: pipeline:user_service_facts
- เวลา: 0.39s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。

### คำตอบจริง

ข้อมูลที่ให้มาระบุว่าจองผิดวันและจ่ายแล้วเปลี่ยนวันได้ แต่ระบุอีกข้อว่าเลื่อนวันแทนคืนเงินไม่ได้ จึงยังต้องยืนยันขอบเขตข้อยกเว้นและช่องทางดำเนินการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c102: เกมต้องอัปเดตตอนมาถึง เวลานับยังไง

- หมวด/ภาษา: policy_boundary / th
- mode: pipeline:user_service_facts
- เวลา: 0.82s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。

### คำตอบจริง

ยังไม่ได้ยืนยันว่าช่วงอัปเดตเกมคิดเวลาใช้บริการอย่างไรครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c103: ราคาของบุคคลภายนอก

- หมวด/ภาษา: dialogue / th
- mode: pipeline:protected_price_missing_service
- เวลา: 0.42s
- ผล: PASS_CLARIFICATION
- วิเคราะห์: 初轮价格缺service或比赛规则缺game，询问缺项合理；后续相同session返回选定scope。

### คำตอบจริง

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

## c104: PC

- หมวด/ภาษา: dialogue / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.29s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c105: ต้องการราคาของบุคคลภายนอก

- หมวด/ภาษา: dialogue / th
- mode: pipeline:protected_price_missing_service
- เวลา: 0.38s
- ผล: PASS_CLARIFICATION
- วิเคราะห์: 初轮价格缺service或比赛规则缺game，询问缺项合理；后续相同session返回选定scope。

### คำตอบจริง

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

## c106: ทั้งหมด

- หมวด/ภาษา: dialogue / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.33s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:
ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ

PC — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (1-2 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 140 บาท/แพ็กเกจ

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ

Cockpit — 60 นาที/แพ็กเกจ (1 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 65 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 200 บาท/แพ็กเกจ

VR — 30 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 190 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 525 บาท/แพ็กเกจ

VR — 60 นาที/แพ็กเกจ (1-5 คน)
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 375 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 1,050 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c107: Service prices for external users

- หมวด/ภาษา: dialogue / en
- mode: pipeline:protected_price_missing_service
- เวลา: 0.31s
- ผล: PASS_CLARIFICATION
- วิเคราะห์: 初轮价格缺service或比赛规则缺game，询问缺项合理；后续相同session返回选定scope。

### คำตอบจริง

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

## c108: PC

- หมวด/ภาษา: dialogue / en
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.30s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

## c109: Service prices for external users

- หมวด/ภาษา: dialogue / en
- mode: pipeline:protected_price_missing_service
- เวลา: 0.29s
- ผล: PASS_CLARIFICATION
- วิเคราะห์: 初轮价格缺service或比赛规则缺game，询问缺项合理；后续相同session返回选定scope。

### คำตอบจริง

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

## c110: all of them

- หมวด/ภาษา: dialogue / en
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.28s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Service prices (recorded package rates):
External users have different rates depending on their eligibility; both relevant groups are shown below.

PC — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package

PlayStation 5 — 60 minutes/package (1-2 people)
• PSU alumni / students from other institutions: 50 THB/package
• General adults: 150 THB/package

Nintendo Switch — 60 minutes/package (1-2 people)
• PSU alumni / students from other institutions: 50 THB/package
• General adults: 140 THB/package

Nintendo Switch — 60 minutes/package (3-4 people)
• PSU alumni / students from other institutions: 100 THB/package
• General adults: 280 THB/package

Cockpit — 60 minutes/package (1 person)
• PSU alumni / students from other institutions: 65 THB/package
• General adults: 200 THB/package

VR — 30 minutes/package (1-5 people)
• PSU alumni / students from other institutions: 190 THB/package
• General adults: 525 THB/package

VR — 60 minutes/package (1-5 people)
• PSU alumni / students from other institutions: 375 THB/package
• General adults: 1,050 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
PC rates use the local update dated 2026-07-27.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
Source: local://service_fee/pc_price_update_20260727

## c111: PC มีเกมอะไรบ้าง

- หมวด/ภาษา: dialogue / th
- mode: pipeline:structured_service_game_availability
- เวลา: 0.56s
- ผล: PASS_CATALOG
- วิเคราะห์: 首轮PC游戏按设备组给出list。

### คำตอบจริง

PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c112: ทั้งหมด

- หมวด/ภาษา: dialogue / th
- mode: pipeline:dialogue_state_clarification
- เวลา: 0.30s
- ผล: FAIL_CONTEXT
- วิเคราะห์: last_seen_response_id已提交；resolver仍用all_catalog_axis_ambiguous询问泛化scope，而非保留PC+games list。

### คำตอบจริง

คำว่า “ทั้งหมด” หมายถึงเรื่องหรือตัวเลือกใดครับ เช่น ปุ่มควบคุม ราคา รายชื่อเกม หรือโซน

## c113: ขอกฎการแข่งขัน

- หมวด/ภาษา: dialogue / th
- mode: pipeline:competition_target_clarification
- เวลา: 0.54s
- ผล: PASS_CLARIFICATION
- วิเคราะห์: 初轮价格缺service或比赛规则缺game，询问缺项合理；后续相同session返回选定scope。

### คำตอบจริง

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

## c114: CS2

- หมวด/ภาษา: dialogue / th
- mode: pipeline:competition_rule_overview_source
- เวลา: 0.60s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

สรุปกติกา Counter-Strike 2 บางประเด็นจากเอกสารที่มี:
รายการ: PSU Phuket CS2 2026 Tournament

**รูปแบบการแข่งขัน**
•    1. รูปแบบทัวร์นาเมนต์ Single Elimination

**ผู้เล่นและองค์ประกอบทีม**
•    2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**คุณสมบัติและการลงทะเบียน**
•    2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**อุปกรณ์การแข่งขัน**
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**การตั้งค่าแมตช์**
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**ก่อนแข่งและหน้างาน**
•    2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**การหยุดเกมและเวลานอก**
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

นี่เป็นสรุปบางข้อในเอกสาร หากต้องการรายละเอียด ถามหัวข้อ เช่น อุปกรณ์ การหยุดเกม หรือบทลงโทษได้ครับ
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

## c115: I want the competition rules

- หมวด/ภาษา: dialogue / en
- mode: pipeline:competition_target_clarification_en
- เวลา: 0.57s
- ผล: PASS_CLARIFICATION
- วิเคราะห์: 初轮价格缺service或比赛规则缺game，询问缺项合理；后续相同session返回选定scope。

### คำตอบจริง

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

## c116: Tekken 8

- หมวด/ภาษา: dialogue / en
- mode: pipeline:competition_rule_overview_source
- เวลา: 0.55s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

Selected Tekken 8 competition rules from the recorded rulebook:
Tournament: Tekken 8


**Competition format**
•    Singles (1v1) format
•    FT2: Winner is the first to win two games

**Match settings**
•    Rounds per game (Round): 3
•    Time per round (Timer): 60 seconds

**Pauses and timeouts**
•    Once the game starts, no game pausing for any reason is permitted
•    Any intentional game pause will result in a penalty of losing one round immediately
•    The game may be paused only when all players agree and there is a valid reason, such as equipment malfunction or an emergency.
•    Pausing the game without necessity will result in the same penalty as leaving the game prematurely.

**Restrictions and conduct**
•    Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.
•    Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception.

**Disputes**
•    In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice.

The recorded rulebook contains both a no-pause clause and an emergency/agreement exception. Ask the organizer to confirm which conditions and penalties apply.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_tekken8_psu_esports

## c117: PC full-day rental price for external organizations

- หมวด/ภาษา: dialogue / en
- mode: pipeline:zone_rental_fee
- เวลา: 0.34s
- ผล: PASS_RECORDED
- วิเคราะห์: 按对应记录source返回PC zone rental4000或PC generaladult70。

### คำตอบจริง

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c118: How many people can it accommodate?

- หมวด/ภาษา: dialogue / en
- mode: pipeline:zone_rental_fee
- เวลา: 0.57s
- ผล: PASS_RECORDED
- วิเคราะห์: followup继承PC rental并返回43 seats/10 PC units，正确区分座位容量与设备数量。

### คำตอบจริง

Zone rental fees for organizations

**PC Zone**
• Seating capacity: 43 seats; equipment: 10 PC units

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c119: PC full-day rental price for external organizations

- หมวด/ภาษา: dialogue / en
- mode: pipeline:zone_rental_fee
- เวลา: 0.34s
- ผล: PASS_RECORDED
- วิเคราะห์: 按对应记录source返回PC zone rental4000或PC generaladult70。

### คำตอบจริง

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c120: How can I reserve it?

- หมวด/ภาษา: dialogue / en
- mode: pipeline:zone_rental_fee
- เวลา: 0.32s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: followup继承rental，但workbook没有rental booking流程，正确不借一般play booking替代。

### คำตอบจริง

Zone rental fees for organizations

The workbook lists rental fees but does not specify the rental booking procedure. Please confirm it with the studio.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c121: ราคา PC บุคคลทั่วไป

- หมวด/ภาษา: dialogue / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.30s
- ผล: PASS_RECORDED
- วิเคราะห์: 按对应记录source返回PC zone rental4000或PC generaladult70。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c122: แล้ว VR ล่ะ

- หมวด/ภาษา: dialogue / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.31s
- ผล: PASS_BOUNDED
- วิเคราะห์: 通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

VR — 30 นาที/แพ็กเกจ (1-5 คน)
•    บุคคลทั่วไป (General Adult): 525 บาท/แพ็กเกจ

VR — 60 นาที/แพ็กเกจ (1-5 คน)
•    บุคคลทั่วไป (General Adult): 1,050 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

## c123: ราคา PC บุคคลทั่วไป

- หมวด/ภาษา: dialogue / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.36s
- ผล: PASS_RECORDED
- วิเคราะห์: 按对应记录source返回PC zone rental4000或PC generaladult70。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c124: กฎแข่ง ROV ล่ะ

- หมวด/ภาษา: dialogue / th
- mode: pipeline:competition_source_rag
- เวลา: 1.88s
- ผล: PASS_TARGET_ONLY
- วิเคราะห์: 换话题至ROV后game/source正确，内容只选一条rule；仅确认topic不混PC价格，未认证overview覆盖全部。

### คำตอบจริง

คำตอบ: 4. ระเบียบและกติกาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
•    4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

## c125: วันนี้ PC1 ตอน10โมงว่างไหม

- หมวด/ภาษา: dialogue / th
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.62s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: WordPress live path有timestamp并返回closed/history状态，但未用同一timestamp外部ground truth逐slot比对；不等同availability accuracy确认。

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
PC #01 (1 Person) ไม่มีรายการจองในช่วง 10:00-11:00 น. (เวลาไทย) ครับ
อัปเดต: 2026-10-09 23:53:32
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c126: แล้ว PC2 ล่ะ

- หมวด/ภาษา: dialogue / th
- mode: pipeline:candidate_margin_clarification
- เวลา: 1.09s
- ผล: FAIL_CONTEXT
- วิเคราะห์: PC2 followup丢失前轮availability/日期/10点，no_matching_context_resolution，返回泛化clarification。

### คำตอบจริง

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

## c127: เปิดกี่โมง ปิดกี่โมง

- หมวด/ภาษา: hours / th
- mode: pipeline:structured_schedule
- เวลา: 0.53s
- ผล: PASS_SCHEDULE
- วิเคราะห์: 返回recorded timetable，未重新确认特殊关门。

### คำตอบจริง

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c128: What are your opening hours?

- หมวด/ภาษา: hours / en
- mode: pipeline:chatbot_identity_en
- เวลา: 0.33s
- ผล: FAIL_INTENT
- วิเคราะห์: opening hours被chatbot_identity_en拦截，回答自我介绍。

### คำตอบจริง

I am PSU Esports Assistant, the chatbot for PSU Esports Studio - Phuket. I can help with verified information about games, equipment, booking, opening hours, service fees, rules, competitions, and studio contacts.

## c129: วัน Maintenance ใช้บริการได้ไหม

- หมวด/ภาษา: hours / th
- mode: pipeline:general_llm_after_rag_miss
- เวลา: 15.45s
- ผล: GROUNDING_GAP
- วิเคราะห์: Maintenance属于中心schedule，却用了general LLM知识，未引用已有时段表；不能据此认定整天maintenance。

### คำตอบจริง

ไม่สามารถใช้งานได้ในช่วงเวลาบำรุงรักษาครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

## c130: Is the studio open on maintenance days?

- หมวด/ภาษา: hours / en
- mode: pipeline:structured_schedule_en
- เวลา: 0.54s
- ผล: PASS_SCHEDULE
- วิเคราะห์: recorded表列具体maintenance区间/午休/周末无常规服务，区分live。

### คำตอบจริง

Regular service timetable (Asia/Bangkok):
•    Monday: 09:00-12:00 is maintenance (no play or booking); 13:00-16:00 is open for play.
•    Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Wednesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Thursday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.
•    Friday: 09:00-12:00 is open for play; 13:00-16:00 is maintenance (no play or booking).
•    Saturday: no regular service period is listed.
•    Sunday: no regular service period is listed.
•    12:00-13:00 is the lunch break; play and booking are unavailable.
Recorded special closures override this regular timetable. A Thai public holiday alone does not automatically close the studio.
This is the regular timetable, not live device availability.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

## c131: วันอาทิตย์เปิดไหม

- หมวด/ภาษา: hours / th
- mode: pipeline:structured_schedule
- เวลา: 0.92s
- ผล: FAIL_COVERAGE
- วิเคราะห์: 问周日，仅返回周一到周五，未直接说明Sunday常规表未列服务。

### คำตอบจริง

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c132: Where is the studio and when does it open?

- หมวด/ภาษา: multi_topic / en
- mode: pipeline:user_service_facts
- เวลา: 0.30s
- ผล: FAIL_COVERAGE
- วิเคราะห์: 问where+when，只答地址，漏营业时间。

### คำตอบจริง

The studio is in Building 5, Floor 1, Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c133: จองเครื่องยังไง ขอขั้นตอนทั้งหมด

- หมวด/ภาษา: booking_process / th
- mode: pipeline:conversation_scope_clarification
- เวลา: 0.18s
- ผล: FAIL_OVERCLARIFICATION
- วิเคราะห์: booking流程完整问题被all/scope guard挡成询问全部哪个topic。

### คำตอบจริง

ต้องการดูทั้งหมดของเรื่องหรือบริการใดครับ?

## c134: How do I book a PC? Give all the steps.

- หมวด/ภาษา: booking_process / en
- mode: pipeline:rule_en
- เวลา: 0.32s
- ผล: PASS_RECORDED
- วิเคราะห์: 返回6步booking流程及reservation source。

### คำตอบจริง

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

## c135: ชำระเงินยังไง จ่ายเงินสดได้ไหม

- หมวด/ภาษา: payment / th
- mode: pipeline:protected_payment_method
- เวลา: 0.36s
- ผล: FAIL_COVERAGE
- วิเคราะห์: 回答bank transfer，却没说明cash是否有确认，第二个问题未答。

### คำตอบจริง

ชำระเงินโดยโอนผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c136: Can I pay cash when I arrive?

- หมวด/ภาษา: payment / en
- mode: pipeline:english_no_answer
- เวลา: 6.35s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: cash许可未确认；generic no_answer虽不够友好，但不能按已有转账方法推出现金绝对禁止。

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for this question.

## c137: มี 100 บาท เล่น PC ได้กี่รอบ บุคคลทั่วไป

- หมวด/ภาษา: budget / th
- mode: pipeline:deterministic_calculator_fast
- เวลา: 0.56s
- ผล: FAIL_BUDGET
- วิเคราะห์: 与c062同：只答单价不答可玩几轮。

### คำตอบจริง

ราคา PC 1 ชั่วโมง สำหรับ General Adult / บุคคลทั่วไป: 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

## c138: I have 100 THB and want to play PC as a general adult. How many sessions can I afford?

- หมวด/ภาษา: budget / en
- mode: pipeline:rule_en
- เวลา: 0.55s
- ผล: FAIL_WRONG_POLICY
- วิเคราะห์: afford几session错误选择一次booking最多3session规则，与预算可负担数无关。

### คำตอบจริง

One booking can include a maximum of 3 sessions.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

## c139: ปุ่มยิงกับรีโหลดใน CS2 คืออะไร

- หมวด/ภาษา: controls / th
- mode: pipeline:structured_game_controls
- เวลา: 0.99s
- ผล: DEVICE_VERIFY_PENDING
- วิเคราะห์: CS2shoot/reload从secondary guide回复LMB/R，明确设备设置未确认；不是现场验证通过。

### คำตอบจริง

Counter-Strike 2 ปุ่มที่ตรงกับคำถาม:
PC
•    Left Mouse Button: ยิง - ยิงอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.holy.gg/en/post/counter-strike-2-keyboard-mouse-controls-pc

## c140: How do I shoot and reload in CS2?

- หมวด/ภาษา: controls / en
- mode: pipeline:structured_game_availability_en
- เวลา: 0.39s
- ผล: FAIL_INTENT
- วิเคราะห์: CS2shoot/reload被当game availability，没回答buttons。

### คำตอบจริง

Counter-Strike 2 is available on: PC #01-#02, PC #03-#10. Studio zone(s): PC Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

## c141: ขอปุ่มควบคุม Tekken 8 ทั้งหมด

- หมวด/ภาษา: controls / th
- mode: pipeline:structured_game_controls
- เวลา: 0.93s
- ผล: SOURCE_QUALITY_ISSUE
- วิเคราะห์: Thai Tekken控制描述有Arabic بشكل，来自game_control_facts.jsonl原文并非本轮LLM生成；controls现场仍未验证。

### คำตอบจริง

TEKKEN 8 มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว
•    Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter)
•    Cross: ลูกเตะซ้าย - ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู
•    Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง
•    D-Pad Up: กระโดด - ควบคุมให้ตัวละครกระโดดขึ้นด้านบนเพื่อหลบการโจมตีล่าง หรือใช้กดร่วมกับปุ่มโจมตีกลางอากาศ
•    D-Pad Left: ถอยหลัง / บล็อก - บังคับตัวละครให้เดินถอยหลังเพื่อรักษาระยะ หรือใช้กดค้างเพื่อ "บล็อก (Guard)" การโจมตีระดับสูงและระดับกลางของศัตรู
•    D-Pad Down: ย่อตัว / ก้มหลบ - สั่งให้ตัวละครย่อตัวต่ำ ใช้ก้มหลบหมัดหรือการโจมตีระดับสูง (High) และใช้บล็อกการโจมตีระดับต่ำ (Low)
•    L (Left Stick): เคลื่อนที่ - ขยับทิศทางของตัวละคร بشكلทั่วไป หรือใช้โยกทิศทางในการเคลื่อนที่และเดินหน้าถอยหลัง
•    L1: สเปเชียลสไตล์ - กดเพื่อเปิด/ปิดโหมดช่วยเหลืออัจฉริยะ ช่วยให้กดคอมโบและท่าไม้ตายของตัวละครนั้น ๆ ได้ง่ายด้วยปุ่มเดียว
•    R1: เปิดใช้งาน Heat - ระเบิดพลัง Heat System เข้าสู่สถานะโอเวอร์ไดรฟ์เพื่อบัฟการโจมตีและเพิ่มคุณสมบัติพิเศษให้ตัวละคร
•    R1 (While in Heat): ฮีทสแมช - ปลดปล่อยท่าโจมตีเผด็จศึกอันทรงพลังปิดฉากคอมโบ โดยจะใช้เกจ Heat ที่เหลืออยู่ทั้งหมดทิ้งทันที
•    Options: หยุดเกม - หยุดเกมชั่วคราวเพื่อเข้าสู่หน้าต่างเมนู เช่น การเช็ก Move List (รายการท่า) หรือการตั้งค่าอื่น ๆ
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/83

## c142: What are the basic controls for Tekken 8?

- หมวด/ภาษา: controls / en
- mode: pipeline:structured_game_controls_en
- เวลา: 0.40s
- ผล: DEVICE_VERIFY_PENDING
- วิเคราะห์: English Tekken mappings返回已有secondary guide并注明设备未确认。

### คำตอบจริง

TEKKEN 8 controls:
- Square: Left Punch
- Triangle: Right Punch
- Cross: Left Kick
- Circle: Right Kick
- D-Pad Up: Jump
- D-Pad Left: Move Backward
- D-Pad Down: Duck
- L (Left Stick): Move
- L1: Special Style
- R1: Heat Activate
- R1 (While in Heat): Heat Smash
- Options: Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/83

## c143: คอมของศูนย์สเปคอะไร

- หมวด/ภาษา: equipment_spec / th
- mode: pipeline:structured_equipment_item
- เวลา: 0.31s
- ผล: PASS_RECORDED
- วิเคราะห์: 回答记录中的CPU/RAM/GPU；本轮未核对实际机器。

### คำตอบจริง

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

## c144: What PC specifications does the studio have?

- หมวด/ภาษา: equipment_spec / en
- mode: pipeline:structured_equipment_catalog_en
- เวลา: 0.36s
- ผล: FAIL_COVERAGE
- วิเคราะห์: 问PC specifications，却只列equipment catalog，漏已有CPU/RAM/GPU。

### คำตอบจริง

Verified equipment in PC Zone:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

## c145: ต้องเป็นสมาชิกไหม มีที่จอดรถไหม แล้วต้องเอาบัตรอะไรไป

- หมวด/ภาษา: multi_topic / th
- mode: pipeline:user_service_facts
- เวลา: 0.18s
- ผล: FAIL_COVERAGE
- วิเคราะห์: membership+parking+ID只回答前两项，漏证件。

### คำตอบจริง

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c146: Do I need membership, is there parking, and what ID should I bring?

- หมวด/ภาษา: multi_topic / en
- mode: pipeline:user_service_facts
- เวลา: 0.26s
- ผล: PASS_MULTI_POLICY
- วิเคราะห์: 英文3项都答出owner source。

### คำตอบจริง

Membership is not required to use the studio.

Parking for cars and motorcycles is available in front of Building 5.

At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c147: เอาเมาส์มาเองได้ไหม แล้วจองผิดเครื่องเปลี่ยนยังไง

- หมวด/ภาษา: multi_topic / th
- mode: pipeline:multi_question_splitter
- เวลา: 0.57s
- ผล: PASS_MULTI_POLICY
- วิเคราะห์: 中文2项正确分拆：personal mouse禁止+cancel/rebook机器。

### คำตอบจริง

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: เอาเมาส์มาเองได้ไหม
ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

คำถามที่ 2: จองผิดเครื่องเปลี่ยนยังไง
กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c148: Can I bring my own keyboard, and can someone else use my booking?

- หมวด/ภาษา: multi_topic / en
- mode: pipeline:multi_question_splitter
- เวลา: 0.22s
- ผล: PASS_MULTI_POLICY
- วิเคราะห์: 英文2项正确分拆：keyboard禁止+named-player条件。

### คำตอบจริง

This question contains several topics. Here are the answers separately:

Question 1: Can I bring my own keyboard
Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

Question 2: can someone else use my booking
The player must be the person who booked or be named in the booking. Someone not listed cannot use the booking instead.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c149: วันนี้ VR เวลา 09:00 ถึง 09:30 ว่างไหม

- หมวด/ภาษา: live_booking / th
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.09s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: 明确时间隔开设备名可进live路径。09:00-09:30原区间及morning/afternoon两条输出，应再用fixture确认effective hour占用/套餐筛选，未认证可book。

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
โซน VR: ช่วง 09:00-09:30 น. ถูกจอง 0/2 รายการ และไม่มีรายการจอง 2/2 รายการ
•    VR Station (Afternoon) (1-5 Persons) 1 Hour: ไม่มีรายการจอง
•    VR Station (Morning) (1-5 Persons) 30 Mins: ไม่มีรายการจอง
อัปเดต: 2026-10-09 23:56:13
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c150: Is VR free today from 09:00 to 09:30?

- หมวด/ภาษา: live_booking / en
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.19s
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: 与c149同，英文输出已有booking历史，未独立验证有效时间/资源filter。

### คำตอบจริง

Date: 2026-10-09 (Asia/Bangkok)
VR Zone: 0/2 resources were booked during 09:00-09:30; 2/2 had no booking.
•    VR Station (Afternoon) (1-5 Persons) 1 Hour: no booking
•    VR Station (Morning) (1-5 Persons) 30 Mins: no booking
Updated: 2026-10-09 23:56:15
Source: https://esports.computing.psu.ac.th/reservation

## c151: วันนี้ PC1 เวลา10โมง และ PC2 เวลา11โมงว่างไหม

- หมวด/ภาษา: live_booking / th
- mode: pipeline:live_booking_status_fast_path
- เวลา: 1.20s
- ผล: FAIL_MULTI_TARGET
- วิเคราะห์: PC1@10及PC2@11只回PC1@10，第二目标和时间被丢弃。

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
PC #01 (1 Person) ไม่มีรายการจองในช่วง 10:00-11:00 น. (เวลาไทย) ครับ
อัปเดต: 2026-10-09 23:56:16
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c152: PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่

- หมวด/ภาษา: multi_topic / th
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.13s
- ผล: FAIL_MULTI_FILTERS
- วิเคราะห์: games+2hours+generaladult只回price全部人群每package：漏games并丢word-number/group。

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c153: What games are on PC, and how much does two hours cost for a general adult?

- หมวด/ภาษา: multi_topic / en
- mode: pipeline:structured_service_fee_conversation
- เวลา: 0.21s
- ผล: FAIL_MULTI_FILTERS
- วิเคราะห์: English同c152。

### คำตอบจริง

Service prices (recorded package rates):

PC — 60 minutes/package (1 person)
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 25 THB/package
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

## c154: คนจองกับคนเล่นต้องเป็นคนเดียวกันไหม

- หมวด/ภาษา: player_identity / th
- mode: pipeline:user_service_facts
- เวลา: 0.38s
- ผล: PASS_OWNER
- วิเคราะห์: owner named-player policy直接正确。

### คำตอบจริง

คนเล่นต้องเป็นคนที่จองหรือมีรายชื่ออยู่ในรายการจอง ไม่สามารถให้ผู้ที่ไม่มีรายชื่อมาใช้แทนได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c155: นั่งดูเพื่อนต้องเสียเงินไหม

- หมวด/ภาษา: policy_boundary / th
- mode: pipeline:user_service_facts
- เวลา: 0.34s
- ผล: FAIL_COVERAGE
- วิเคราะห์: 问观看收费，只答允许观看。owner只确认permission，未确认费用，应说明费用未知。

### คำตอบจริง

สามารถมานั่งดูเพื่อนเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c156: Is parking free?

- หมวด/ภาษา: policy_boundary / en
- mode: pipeline:user_service_facts
- เวลา: 0.19s
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: 停车可用与免费不同，正确标明parking fees未指定。

### คำตอบจริง

Parking for cars and motorcycles is available in front of Building 5.

Parking fees have not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

