# คำถามบริการและคำตอบจริง r54 — ฉบับภาษาไทย

ชุดหลัก156คำถาม ไทย92/อังกฤษ64 ผ่านAPIที่เว็บใช้จริง ข้อวิเคราะห์เป็นการตรวจโดยagentจากsource/trace ไม่ใช่ownerยืนยันนโยบายใหม่ รายละเอียดดิบอยู่responses*.jsonและextra_responses.json

## c001: ที่นี่เป็นร้านเกมทั่วไปหรือของมหาวิทยาลัย

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 2.97 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

PSU Esports Studio - Phuket เป็นศูนย์ของมหาวิทยาลัยสงขลานครินทร์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c002: Is this a university facility or a regular gaming cafe?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 2.70 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

PSU Esports Studio - Phuket is a university facility of Prince of Songkla University.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c003: ต้องเป็นสมาชิกก่อนเล่นไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 1.03 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c004: Do I need membership to use the studio?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 1.32 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Membership is not required to use the studio.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c005: ไปนั่งดูเพื่อนเล่นเฉยๆได้ไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 1.15 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

สามารถมานั่งดูเพื่อนเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c006: Can I sit and watch my friend play?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 2.09 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

You may sit and watch your friends play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c007: เดินเข้าไปเล่นเลยได้ไหม ต้องจองไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 1.04 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c008: Can I walk in without booking?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.83 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Walk-in visitors must still book through the reservation system before using the service.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c009: ศูนย์อยู่ตึกไหน ชั้นอะไร

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.74 วินาที
- ผล: PASS_FORMAT
- วิเคราะห์: คำตอบตรงข้อมูลเจ้าของ ต่างแค่ช่องว่างก่อนคำว่า “ครับ” เป็นตัวตรวจแจ้งเตือนเกินจริง ไม่ใช่ข้อมูลผิด

### คำตอบจริง

ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c010: Which building and floor is the studio in?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.73 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

The studio is in Building 5, Floor 1, Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c011: ขอลิงก์แผนที่ศูนย์หน่อย

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.73 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ลิงก์แผนที่ศูนย์: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c012: Can I have the studio map link?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.54 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Studio map: https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c013: มีที่จอดรถยนต์กับมอเตอร์ไซค์ไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.60 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c014: Is there parking for cars and motorcycles?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.82 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Parking for cars and motorcycles is available in front of Building 5.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c015: หาศูนย์ไม่เจอ ติดต่อใครได้

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.54 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ติดต่อผ่านเพจศูนย์อีสปอร์ตได้ครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c016: Who can I contact if I cannot find the studio?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.61 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Contact the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c017: มากันสี่คนควรเลือกเครื่องไหน

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.56 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

มากัน 4 คน แนะนำ Nintendo Switch ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c018: What should a group of four choose?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:english_no_answer
- เวลา: 1.06 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: มีคำตอบ Nintendo Switch สำหรับกลุ่ม 4 คนอยู่แล้ว แต่การจับจำนวนคนและคำถามเลือกบริการไม่ครอบคลุม group of four / 4 ppl / เล่นอันไหนดี

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for this question.

## c019: จองชื่อเราแต่ให้เพื่อนที่ไม่มีชื่อเล่นแทนได้ไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:request_timeout_no_answer
- เวลา: 19.12 วินาที
- ผล: FAIL_TIMEOUT
- วิเคราะห์: คำตอบผู้เล่นต้องมีชื่อในรายการจองมีในข้อมูล แต่คำถามนี้กลับ timeout ไม่มี trace รายขั้นครบพอระบุว่าติดขั้นไหน ห้ามสรุปว่าเป็น GPU อย่างเดียว

### คำตอบจริง

ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง
ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ

## c020: Can a friend who is not named in my booking play instead?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.62 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

The player must be the person who booked or be named in the booking. Someone not listed cannot use the booking instead.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c021: ตอนมาถึงต้องแสดงบัตรอะไร

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.57 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

เมื่อมาถึงให้แสดงบัตรประชาชน บัตรนักศึกษา บัตรนักเรียน หรือ Passport อย่างใดอย่างหนึ่งครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c022: What ID should I show when I arrive?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.54 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c023: จองผิดเครื่องต้องแก้ยังไง

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.54 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c024: How do I change a booking for the wrong machine?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.80 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

If you booked the wrong machine, cancel through the email and make a new booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c025: เปลี่ยนเวลาจองทำยังไง

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.59 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

หากต้องการเปลี่ยนเวลาจอง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c026: How can I change my booking time?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.60 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

To change the booking time, cancel through the email and make a new booking.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c027: เอาคีย์บอร์ดหรือเมาส์ตัวเองมาใช้ได้ไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.81 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c028: Can I bring my own keyboard or mouse?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.59 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c029: แนบสลิปผิดรูปต้องทำยังไง

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.58 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: https://www.facebook.com/psuesportsphuket

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c030: What should I do if I uploaded the wrong payment slip?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.55 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: https://www.facebook.com/psuesportsphuket

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c031: จองหลายเครื่องโอนครั้งเดียวได้ไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.92 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c032: Can I make one bank transfer for several machines?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.88 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

You may make one bank transfer for multiple machines, but you must add a note when booking so the studio can verify it.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c033: มาถึงก่อนเพื่อนเช็กอินแทนทั้งกลุ่มได้ไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.89 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

เช็กอินแทนทั้งกลุ่มไม่ได้ ศูนย์ตรวจเป็นรายคน แต่คนที่มาก่อนสามารถเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c034: Can I check in for my whole group before my friends arrive?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.59 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

You cannot check in for the whole group. Each person is checked individually, but those who arrive first may play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c035: มีที่นั่งพักรอเพื่อนไหม

- หมวด/ภาษา: policy / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 2.19 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

มีที่นั่งพักตรงโซนกลางห้องครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c036: Is there seating where I can rest while waiting for friends?

- หมวด/ภาษา: policy / en
- เส้นทาง: pipeline:games_unknown_target_en
- เวลา: 2.14 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: ถามที่นั่งพัก/รอ แต่ไม่เข้าข้อมูล rest_seating; อังกฤษเข้าเส้นทางชื่อเกม ส่วนไทยถามกลับแบบกว้าง ควรตอบจุดพักกลางห้อง

### คำตอบจริง

I could not find seating where I can rest while waiting for friends in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

## c037: ต้องสมัคสมาชิกก่อนไหม

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.57 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c038: do i need a memebrship first

- หมวด/ภาษา: policy_variant / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.60 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Membership is not required to use the studio.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c039: แค่มาดูเพื่อนได้ปะ ไม่เล่น

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.55 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

สามารถมานั่งดูเพื่อนเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c040: can i just watch my freind

- หมวด/ภาษา: policy_variant / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.40 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

You may sit and watch your friends play.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c041: ไม่ได้จองมา เดินเข้าได้ปะ

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.54 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c042: can i walkin and play straight away

- หมวด/ภาษา: policy_variant / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.57 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Walk-in visitors must still book through the reservation system before using the service.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c043: อยู่ตึกไร ชั้นไหนอ่ะ

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.56 วินาที
- ผล: PASS_FORMAT
- วิเคราะห์: คำตอบตรงข้อมูลเจ้าของ ต่างแค่ช่องว่างก่อนคำว่า “ครับ” เป็นตัวตรวจแจ้งเตือนเกินจริง ไม่ใช่ข้อมูลผิด

### คำตอบจริง

ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c044: มอไซจอดไหน มีที่จอดปะ

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.57 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c045: มา4คน เล่นอันไหนดี

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:general_rag_miss_llm_unavailable
- เวลา: 18.02 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: มีคำตอบ Nintendo Switch สำหรับกลุ่ม 4 คนอยู่แล้ว แต่การจับจำนวนคนและคำถามเลือกบริการไม่ครอบคลุม group of four / 4 ppl / เล่นอันไหนดี

### คำตอบจริง

การสร้างคำตอบใช้เวลาเกินเวลาที่ระบบกำหนดครับ กรุณาลองคำถามที่สั้นลง

## c046: we are 4 ppl what can we play

- หมวด/ภาษา: policy_variant / en
- เส้นทาง: pipeline:english_no_answer
- เวลา: 1.13 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: มีคำตอบ Nintendo Switch สำหรับกลุ่ม 4 คนอยู่แล้ว แต่การจับจำนวนคนและคำถามเลือกบริการไม่ครอบคลุม group of four / 4 ppl / เล่นอันไหนดี

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for this question.

## c047: เพื่อนไม่มีชื่อในจอง เล่นแทนได้มะ

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:semantic_rag_dynamic
- เวลา: 6.23 วินาที
- ผล: PASS_EQUIVALENT
- วิเคราะห์: คำตอบห้ามโอนสิทธิ์ตรงกับกรณีที่คำถามระบุว่าเพื่อนไม่มีชื่อในจอง ไม่ใช้ผลนี้สรุปว่าคนมีชื่อในกลุ่มก็เล่นไม่ได้

### คำตอบจริง

ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c048: ไปถึงต้องเอาบัตรไรไปมั่ง

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:candidate_margin_clarification
- เวลา: 8.21 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: คำถามบัตรเช็กอินมีข้อมูล แต่ภาษาพูด/สะกด documents ผิดไม่ตรงตัวจับเจตนา ควรบอกบัตรประชาชน/นักศึกษา/นักเรียน/passport ตาม source

### คำตอบจริง

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

## c049: which documnts do i bring for checkin

- หมวด/ภาษา: policy_variant / en
- เส้นทาง: pipeline:english_no_answer
- เวลา: 1.11 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: คำถามบัตรเช็กอินมีข้อมูล แต่ภาษาพูด/สะกด documents ผิดไม่ตรงตัวจับเจตนา ควรบอกบัตรประชาชน/นักศึกษา/นักเรียน/passport ตาม source

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for reservation.

## c050: จองผืดเครื่อง เปลี่ยนไง

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.57 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c051: อยากเปลี่ยนรอบที่จอง ต้องทำไง

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:rag_direct_curated
- เวลา: 2.11 วินาที
- ผล: SOURCE_REVIEW
- วิเคราะห์: ตอบยกเลิกผ่านอีเมลแล้วจองใหม่จากกฎเดิม พร้อมเงื่อนไขอย่างน้อย 1 ชั่วโมงและใช้สลิปเดิม คำตอบล่าสุดเจ้าของไม่ได้กล่าวถึงเงื่อนไขเหล่านี้ ต้องประสานเวอร์ชัน ไม่เรียกว่า LLM แต่ง

### คำตอบจริง

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c052: เอาเม้าส์ตัวเองไปเสียบได้ปะ

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.58 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c053: can i use my own keybaord

- หมวด/ภาษา: policy_variant / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.55 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Personal keyboards and mice are not allowed for general studio use.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c054: อัพสลิปผืด ส่งใหม่ทางไหน

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:rag_direct_curated
- เวลา: 1.87 วินาที
- ผล: FAIL_WRONG_POLICY
- วิเคราะห์: ควรส่งสลิปที่ถูกต้องทางเพจศูนย์ตามคำตอบเจ้าของ แต่ retrieval เลือกกฎยกเลิกจอง/จองใหม่ เป็นขั้นตอนคนละเรื่อง

### คำตอบจริง

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c055: จอง3เครื่อง จ่ายรวมทีเดียวได้ปะ

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.30 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c056: เพื่อนยังมาไม่ถึง เช็คอินให้ทั้งแก๊งได้ไหม

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:protected_checkin_required
- เวลา: 0.80 วินาที
- ผล: FAIL_WRONG_POLICY
- วิเคราะห์: ควรตอบว่าเช็กอินแทนกลุ่มไม่ได้ ตรวจรายคน และคนมาก่อนเล่นได้ แต่กลับตอบขั้นตอนเช็กอินทั่วไป

### คำตอบจริง

ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c057: มีตรงให้นั่งรอมั้ย

- หมวด/ภาษา: policy_variant / th
- เส้นทาง: pipeline:candidate_margin_clarification
- เวลา: 1.38 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: ถามที่นั่งพัก/รอ แต่ไม่เข้าข้อมูล rest_seating; อังกฤษเข้าเส้นทางชื่อเกม ส่วนไทยถามกลับแบบกว้าง ควรตอบจุดพักกลางห้อง

### คำตอบจริง

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

## c058: ราคา PC บุคคลทั่วไป

- หมวด/ภาษา: price_budget / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.30 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c059: PC prices for general adults

- หมวด/ภาษา: price_budget / en
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.30 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

Service prices (recorded package rates):

PC — 60 minutes/package (1 person)
• General adults: 70 THB/package
PC rates use the local update dated 2026-07-27.
Source: local://service_fee/pc_price_update_20260727

## c060: เป็นบุคคลทั่วไป เล่น PC 2 ชั่วโมงเท่าไหร่

- หมวด/ภาษา: price_budget / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.29 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
ระยะเวลาที่ถาม 120 นาที (2 ชั่วโมง) คิดเป็น 2 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ × 2 = 140 บาท
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c061: General adult PC for two hours, how much?

- หมวด/ภาษา: price_budget / en
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.33 วินาที
- ผล: FAIL_FILTERS
- วิเคราะห์: request_plan ทำกลุ่ม general adult และ two hours หาย: customer_scope=unspecified, duration_minutes=null ควรคำนวณ PC 70×2=140 บาทตามอัตราบันทึก

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
- เส้นทาง: pipeline:deterministic_calculator_fast
- เวลา: 3.73 วินาที
- ผล: FAIL_BUDGET
- วิเคราะห์: ไม่มีการตีความงบประมาณเป็นงานคำนวณความสามารถซื้อแพ็กเกจ: บางเคสตอบราคาหนึ่งชั่วโมง บางเคสตอบรายชื่อเกมหรือจำกัดจอง 3 รอบ PC บุคคลทั่วไปงบ100ตามอัตราบันทึกควรเล่นได้1รอบ60นาทีและเหลือ30บาท

### คำตอบจริง

ราคา PC 1 ชั่วโมง สำหรับ General Adult / บุคคลทั่วไป: 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

## c063: I am a general adult with 100 baht. What can I play?

- หมวด/ภาษา: price_budget / en
- เส้นทาง: pipeline:structured_games_catalog_en
- เวลา: 1.89 วินาที
- ผล: FAIL_BUDGET
- วิเคราะห์: ไม่มีการตีความงบประมาณเป็นงานคำนวณความสามารถซื้อแพ็กเกจ: บางเคสตอบราคาหนึ่งชั่วโมง บางเคสตอบรายชื่อเกมหรือจำกัดจอง 3 รอบ PC บุคคลทั่วไปงบ100ตามอัตราบันทึกควรเล่นได้1รอบ60นาทีและเหลือ30บาท

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
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.30 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: Nintendo 3–4 คนตอบ 280 บาท/60 นาทีตามอัตราที่บันทึก พร้อมแจ้งวันสิ้นสุดตารางเดิม ไม่ใช่การยืนยันการต่ออายุราคาปัจจุบัน

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

Nintendo Switch — 60 นาที/แพ็กเกจ (3-4 คน)
ระยะเวลาที่ถาม 60 นาที (1 ชั่วโมง) คิดเป็น 1 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 280 บาท/แพ็กเกจ
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

## c065: ขอตารางราคาทุกบริการบุคคลภายนอก

- หมวด/ภาษา: price_budget / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.31 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.31 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.30 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.28 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.35 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.37 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.30 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: ตอบอย่างเหมาะสมว่าไม่มีชั่วโมงครึ่งวัน/เต็มวันในไฟล์ หรือไม่มีราคาอุปกรณ์ PS55 โดยไม่เดาเป็น PS5

### คำตอบจริง

ราคาเช่าเหมาโซนสำหรับหน่วยงาน

ไฟล์ไม่ได้ระบุว่าครึ่งวัน/เต็มวันนับกี่ชั่วโมงหรือเริ่ม–สิ้นสุดกี่โมง ต้องยืนยันช่วงเวลาเช่าเหมาจากศูนย์ครับ

แหล่งข้อมูล: ไฟล์ค่าบริการครึ่งวันและเต็มวันที่ผู้ใช้ส่งให้
local://service_fee/zone_rental_fees_20261006

## c072: Can I rent PS55 for a full day?

- หมวด/ภาษา: rental / en
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.36 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: ตอบอย่างเหมาะสมว่าไม่มีชั่วโมงครึ่งวัน/เต็มวันในไฟล์ หรือไม่มีราคาอุปกรณ์ PS55 โดยไม่เดาเป็น PS5

### คำตอบจริง

Zone rental fees for organizations

No rental rate is recorded for these requested targets: ps55

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c073: PC มีเกมอะไรบ้าง ขอทั้งหมด

- หมวด/ภาษา: games / th
- เส้นทาง: pipeline:structured_service_game_availability
- เวลา: 0.81 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:structured_games_catalog_en
- เวลา: 0.55 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:game_target_ambiguous
- เวลา: 0.54 วินาที
- ผล: FAIL_CATALOG
- วิเคราะห์: คำถามรายการเกมของ Nintendo/Cockpit ถูกตีความผิดหรือ no_answer ทั้งที่มี catalog ตามโซน

### คำตอบจริง

ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน
กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

## c076: What games can I play on Nintendo Switch?

- หมวด/ภาษา: games / en
- เส้นทาง: pipeline:structured_games_catalog_en
- เวลา: 0.56 วินาที
- ผล: PASS_CATALOG
- วิเคราะห์: ตอบรายการเกมตามโซนที่เลือกจากข้อมูล ไม่ใช่ยืนยันเวอร์ชันเกม/สถานะติดตั้งปัจจุบันทุกเครื่อง

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
- เส้นทาง: pipeline:structured_service_game_availability
- เวลา: 0.58 วินาที
- ผล: PASS_CATALOG
- วิเคราะห์: ตอบรายการเกมตามโซนที่เลือกจากข้อมูล ไม่ใช่ยืนยันเวอร์ชันเกม/สถานะติดตั้งปัจจุบันทุกเครื่อง

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
- เส้นทาง: pipeline:no_answer
- เวลา: 13.04 วินาที
- ผล: FAIL_CATALOG
- วิเคราะห์: คำถามรายการเกมของ Nintendo/Cockpit ถูกตีความผิดหรือ no_answer ทั้งที่มี catalog ตามโซน

### คำตอบจริง

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

## c079: VR มีเกมอะไรบ้าง

- หมวด/ภาษา: games / th
- เส้นทาง: pipeline:structured_service_game_availability
- เวลา: 0.60 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:hybrid_guarded_rerank
- เวลา: 6.16 วินาที
- ผล: FAIL_AGGREGATE
- วิเคราะห์: ถามจำนวนเกมทั้งหมด แต่ดึงคำอธิบายเกม Naruto รายเกมมาทั้งย่อหน้า ควร aggregate catalog และระบุว่าตัดเกมซ้ำข้ามโซนหรือไม่

### คำตอบจริง

Naruto X Boruto Ultimate Ninja Storm Connections: สัมผัสกับเนื้อเรื่องของ Naruto และ Sasuke อย่างเต็มรูปแบบเป็นครั้งแรกในการเฉลิมฉลองครบรอบ 20 ปีการเปิดตัวอนิเมะ Naruto ที่ครอบคลุมไปทั้งหมดนี้ NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS ปล่อยให้คุณได้สัมผัสกับพลังของ Ninjutsu อย่างที่ไม่เคยมีมาก่อน โดยมีนักสู้ที่สามารถเล่นได้จำนวนมากกว่า 130 ตัว เชี่ยวชาญกลไกการต่อสู้ที่อัพเดตในโหมดการต่อสู้ออฟไลน์และออนไลน์ที่น่าตื่นเต้นจำนวนมากมาย...
อยู่ในรายการเกมหน้า Our Games ส่วน: PlayStation 5
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games, https://esports.phuket.psu.ac.th/home

## c081: กฏตอนเเข่ง cs2 มีอะไรมั่ง

- หมวด/ภาษา: competition / th
- เส้นทาง: pipeline:competition_rule_overview_source
- เวลา: 0.87 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:competition_rule_overview_source
- เวลา: 1.08 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:competition_rule_overview_source
- เวลา: 0.59 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:competition_rule_overview_source
- เวลา: 0.88 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:competition_rule_full_sections_source
- เวลา: 0.59 วินาที
- ผล: PARTIAL_PAGE
- วิเคราะห์: ตอบเอกสาร CS2 เพียง8/56ส่วนและบอกชัดว่าเป็นบางส่วน การมีชื่อเกมถูกต้องยังไม่ผ่านข้อกำหนด “ทั้งหมด”; การถามต่อทดสอบเพิ่มแล้วหลุดบริบท

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
- เส้นทาง: pipeline:competition_rule_full_sections_source
- เวลา: 0.59 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:competition_rule_overview_source
- เวลา: 0.82 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:competition_rule_detail_no_answer
- เวลา: 0.29 วินาที
- ผล: SAFE_EDITION
- วิเคราะห์: เอกสารมีปี2026 จึงไม่ใช้ยืนยันกติกาปี2030 เป็นการปฏิเสธที่เหมาะสม

### คำตอบจริง

เอกสารกติกาที่มีระบุปี 2026 จึงยังยืนยันกติกาฉบับปี 2030 ที่ถามไม่ได้ ต้องขอเอกสารฉบับปีนั้นจากผู้จัดก่อนครับ

## c089: ตอนนี้ PC ว่างไหม

- หมวด/ภาษา: live_booking / th
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.88 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เข้าเส้นทาง WordPress สด มีวันเวลาและแหล่งข้อมูล แต่รอบนี้ไม่ได้เทียบแต่ละ slot กับ oracle ที่เวลาเดียวกัน ไม่เรียกว่าความถูกต้องของสถานะจริงผ่าน

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
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.91 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เข้าเส้นทาง WordPress สด มีวันเวลาและแหล่งข้อมูล แต่รอบนี้ไม่ได้เทียบแต่ละ slot กับ oracle ที่เวลาเดียวกัน ไม่เรียกว่าความถูกต้องของสถานะจริงผ่าน

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
โซน Cockpit: ว่าง 0/2 รายการ ช่วง 23:53 น. เพราะศูนย์ปิดให้บริการ
•    Cockpit #1 (1 Person): ปิดให้บริการ
•    Cockpit #2 (1 Person): ปิดให้บริการ
อัปเดต: 2026-10-09 23:53:02
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c091: วันนี้ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง

- หมวด/ภาษา: live_booking / th
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.60 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เข้าเส้นทาง WordPress สด มีวันเวลาและแหล่งข้อมูล แต่รอบนี้ไม่ได้เทียบแต่ละ slot กับ oracle ที่เวลาเดียวกัน ไม่เรียกว่าความถูกต้องของสถานะจริงผ่าน

### คำตอบจริง

วันที่ 2026-10-09 ช่วง 15:00-16:00 น. (เวลาไทย): ศูนย์ไม่เปิดให้บริการ จึงไม่มีอุปกรณ์ที่เปิดให้จองในช่วงนี้ครับ
อัปเดต: 2026-10-09 23:53:03
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c092: Which equipment is free today at 3 pm?

- หมวด/ภาษา: live_booking / en
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.65 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เข้าเส้นทาง WordPress สด มีวันเวลาและแหล่งข้อมูล แต่รอบนี้ไม่ได้เทียบแต่ละ slot กับ oracle ที่เวลาเดียวกัน ไม่เรียกว่าความถูกต้องของสถานะจริงผ่าน

### คำตอบจริง

At 2026-10-09, 15:00-16:00 (Asia/Bangkok), the studio is closed; no equipment is bookable then.
Updated: 2026-10-09 23:53:05
Source: https://esports.computing.psu.ac.th/reservation

## c093: Is PC1 free today at 10 am?

- หมวด/ภาษา: live_booking / en
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.64 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เข้าเส้นทาง WordPress สด มีวันเวลาและแหล่งข้อมูล แต่รอบนี้ไม่ได้เทียบแต่ละ slot กับ oracle ที่เวลาเดียวกัน ไม่เรียกว่าความถูกต้องของสถานะจริงผ่าน

### คำตอบจริง

Date: 2026-10-09 (Asia/Bangkok)
PC #01 (1 Person) had no booking during 10:00-11:00 (Asia/Bangkok).
Updated: 2026-10-09 23:53:06
Source: https://esports.computing.psu.ac.th/reservation

## c094: วันนี้ VR 9:00-9:30 ว่างไหม

- หมวด/ภาษา: live_booking / th
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.66 วินาที
- ผล: FAIL_TIME_ENTITY
- วิเคราะห์: ตัวจับหมายเลขเครื่องอ่าน VR 9:00 เป็น VR #9 เพราะ regex ของชื่อที่สะกดถูกไม่มีข้อห้ามตัวเลขติด colon เช่นที่ fallback ชื่อพิมพ์ผิดมีอยู่แล้ว

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
ไม่พบ โซน VR เครื่อง #9 ใน Booking Dashboard ครับ
อัปเดต: 2026-10-09 23:53:08
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c095: เครื่องค้างระหว่างเล่น คืนเวลาให้ไหม

- หมวด/ภาษา: policy_boundary / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.82 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกกฎเดิมที่บันทึกกับประเด็นที่เจ้าของยังไม่ยืนยัน เช่นคืนเวลา ติดตั้งเกม เด็ก มาสาย สตรีม การเลื่อนวันและเวลาอัปเดต ถือเป็นตอบ unknown อย่างเหมาะสม

### คำตอบจริง

กฎการจองที่บันทึกไว้เดิม: โดยทั่วไปไม่มีการคืนเงิน ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ
https://esports.computing.psu.ac.th/

ยังไม่ได้ยืนยันวิธีคิดหรือชดเชยเวลาที่เสียไปเมื่อเครื่องค้างหรือดับครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c096: Can I install a game that is not in your list?

- หมวด/ภาษา: policy_boundary / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.87 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกกฎเดิมที่บันทึกกับประเด็นที่เจ้าของยังไม่ยืนยัน เช่นคืนเวลา ติดตั้งเกม เด็ก มาสาย สตรีม การเลื่อนวันและเวลาอัปเดต ถือเป็นตอบ unknown อย่างเหมาะสม

### คำตอบจริง

Permission to request additional games or install games, programs, or mods yourself has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c097: เอา Steam ตัวเองล็อกอินได้ไหม

- หมวด/ภาษา: policy_boundary / th
- เส้นทาง: pipeline:candidate_margin_clarification
- เวลา: 7.99 วินาที
- ผล: FAIL_UNHELPFUL_CLARIFICATION
- วิเคราะห์: เรื่องใช้บัญชี Steam ส่วนตัวไม่มีข้อมูลยืนยัน ควรบอกข้อที่ยังไม่ทราบโดยตรง แทนถามกลับหมวดเกม/ราคา/อุปกรณ์กว้าง ๆ

### คำตอบจริง

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

## c098: If I arrive 15 minutes late, can I still play?

- หมวด/ภาษา: policy_boundary / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.56 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกกฎเดิมที่บันทึกกับประเด็นที่เจ้าของยังไม่ยืนยัน เช่นคืนเวลา ติดตั้งเกม เด็ก มาสาย สตรีม การเลื่อนวันและเวลาอัปเดต ถือเป็นตอบ unknown อย่างเหมาะสม

### คำตอบจริง

Recorded booking rule: If users fail to check in before the reserved time slot begins, the booking will be automatically cancelled with no refund.
https://esports.computing.psu.ac.th/



No separate grace period or exception for arriving 15 minutes late has been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c099: เด็กอายุ10ขวบเล่นได้ไหม ต้องมีผู้ปกครองไหม

- หมวด/ภาษา: policy_boundary / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.33 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกกฎเดิมที่บันทึกกับประเด็นที่เจ้าของยังไม่ยืนยัน เช่นคืนเวลา ติดตั้งเกม เด็ก มาสาย สตรีม การเลื่อนวันและเวลาอัปเดต ถือเป็นตอบ unknown อย่างเหมาะสม

### คำตอบจริง

ยังไม่ได้ยืนยันข้อกำหนดอายุและการมีผู้ปกครองสำหรับเด็กครับ การเปิดให้บุคคลทั่วไปใช้บริการยังใช้ยืนยันข้อนี้ไม่ได้

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c100: May I stream from a studio computer?

- หมวด/ภาษา: policy_boundary / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.28 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกกฎเดิมที่บันทึกกับประเด็นที่เจ้าของยังไม่ยืนยัน เช่นคืนเวลา ติดตั้งเกม เด็ก มาสาย สตรีม การเลื่อนวันและเวลาอัปเดต ถือเป็นตอบ unknown อย่างเหมาะสม

### คำตอบจริง

Permission to stream from the studio machines has not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c101: จ่ายแล้วจองผิดวัน เปลี่ยนวันกับขอเลื่อนแทนคืนเงินได้ไหม

- หมวด/ภาษา: policy_boundary / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.39 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกกฎเดิมที่บันทึกกับประเด็นที่เจ้าของยังไม่ยืนยัน เช่นคืนเวลา ติดตั้งเกม เด็ก มาสาย สตรีม การเลื่อนวันและเวลาอัปเดต ถือเป็นตอบ unknown อย่างเหมาะสม

### คำตอบจริง

ข้อมูลที่ให้มาระบุว่าจองผิดวันและจ่ายแล้วเปลี่ยนวันได้ แต่ระบุอีกข้อว่าเลื่อนวันแทนคืนเงินไม่ได้ จึงยังต้องยืนยันขอบเขตข้อยกเว้นและช่องทางดำเนินการครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c102: เกมต้องอัปเดตตอนมาถึง เวลานับยังไง

- หมวด/ภาษา: policy_boundary / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.82 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกกฎเดิมที่บันทึกกับประเด็นที่เจ้าของยังไม่ยืนยัน เช่นคืนเวลา ติดตั้งเกม เด็ก มาสาย สตรีม การเลื่อนวันและเวลาอัปเดต ถือเป็นตอบ unknown อย่างเหมาะสม

### คำตอบจริง

ยังไม่ได้ยืนยันว่าช่วงอัปเดตเกมคิดเวลาใช้บริการอย่างไรครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c103: ราคาของบุคคลภายนอก

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:protected_price_missing_service
- เวลา: 0.42 วินาที
- ผล: PASS_CLARIFICATION
- วิเคราะห์: คำถามแรกขาดบริการสำหรับราคา หรือขาดชื่อเกมสำหรับกฎ การถามยืนยันเป็นขั้นตอนที่ถูกต้อง

### คำตอบจริง

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

## c104: PC

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.29 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:protected_price_missing_service
- เวลา: 0.38 วินาที
- ผล: PASS_CLARIFICATION
- วิเคราะห์: คำถามแรกขาดบริการสำหรับราคา หรือขาดชื่อเกมสำหรับกฎ การถามยืนยันเป็นขั้นตอนที่ถูกต้อง

### คำตอบจริง

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

## c106: ทั้งหมด

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.33 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:protected_price_missing_service
- เวลา: 0.31 วินาที
- ผล: PASS_CLARIFICATION
- วิเคราะห์: คำถามแรกขาดบริการสำหรับราคา หรือขาดชื่อเกมสำหรับกฎ การถามยืนยันเป็นขั้นตอนที่ถูกต้อง

### คำตอบจริง

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

## c108: PC

- หมวด/ภาษา: dialogue / en
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.30 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:protected_price_missing_service
- เวลา: 0.29 วินาที
- ผล: PASS_CLARIFICATION
- วิเคราะห์: คำถามแรกขาดบริการสำหรับราคา หรือขาดชื่อเกมสำหรับกฎ การถามยืนยันเป็นขั้นตอนที่ถูกต้อง

### คำตอบจริง

Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.

## c110: all of them

- หมวด/ภาษา: dialogue / en
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.28 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:structured_service_game_availability
- เวลา: 0.56 วินาที
- ผล: PASS_CATALOG
- วิเคราะห์: ตอบรายการเกมตามโซนที่เลือกจากข้อมูล ไม่ใช่ยืนยันเวอร์ชันเกม/สถานะติดตั้งปัจจุบันทุกเครื่อง

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
- เส้นทาง: pipeline:dialogue_state_clarification
- เวลา: 0.30 วินาที
- ผล: FAIL_CONTEXT
- วิเคราะห์: ส่ง last_seen_response_id แล้ว แต่ resolver ยังตัดสิน all_catalog_axis_ambiguous; ควรคง scope PC + รายการเกมจากคำถามก่อนหน้า

### คำตอบจริง

คำว่า “ทั้งหมด” หมายถึงเรื่องหรือตัวเลือกใดครับ เช่น ปุ่มควบคุม ราคา รายชื่อเกม หรือโซน

## c113: ขอกฎการแข่งขัน

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:competition_target_clarification
- เวลา: 0.54 วินาที
- ผล: PASS_CLARIFICATION
- วิเคราะห์: คำถามแรกขาดบริการสำหรับราคา หรือขาดชื่อเกมสำหรับกฎ การถามยืนยันเป็นขั้นตอนที่ถูกต้อง

### คำตอบจริง

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

## c114: CS2

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:competition_rule_overview_source
- เวลา: 0.60 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:competition_target_clarification_en
- เวลา: 0.57 วินาที
- ผล: PASS_CLARIFICATION
- วิเคราะห์: คำถามแรกขาดบริการสำหรับราคา หรือขาดชื่อเกมสำหรับกฎ การถามยืนยันเป็นขั้นตอนที่ถูกต้อง

### คำตอบจริง

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

## c116: Tekken 8

- หมวด/ภาษา: dialogue / en
- เส้นทาง: pipeline:competition_rule_overview_source
- เวลา: 0.55 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.34 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: ตอบราคา PC รายแพ็กเกจ70 หรือเหมาโซนภายนอกเต็มวัน4000จาก source ตรง scope

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.57 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: คำถามต่อรองรับกี่คนคงบริบทเหมา PC และตอบ43ที่นั่ง/10เครื่องตามตาราง ต้องแยกที่นั่งจากจำนวนเครื่องหรือผู้เล่นพร้อมกัน

### คำตอบจริง

Zone rental fees for organizations

**PC Zone**
• Seating capacity: 43 seats; equipment: 10 PC units

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c119: PC full-day rental price for external organizations

- หมวด/ภาษา: dialogue / en
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.34 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: ตอบราคา PC รายแพ็กเกจ70 หรือเหมาโซนภายนอกเต็มวัน4000จาก source ตรง scope

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
- เส้นทาง: pipeline:zone_rental_fee
- เวลา: 0.32 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: คงบริบทเหมา PC แต่ไฟล์ราคาเหมาไม่มีขั้นตอนจอง จึงบอกว่ายังไม่ยืนยัน ไม่หยิบการจองเล่นทั่วไปมาทดแทน

### คำตอบจริง

Zone rental fees for organizations

The workbook lists rental fees but does not specify the rental booking procedure. Please confirm it with the studio.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

## c121: ราคา PC บุคคลทั่วไป

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.30 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: ตอบราคา PC รายแพ็กเกจ70 หรือเหมาโซนภายนอกเต็มวัน4000จาก source ตรง scope

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c122: แล้ว VR ล่ะ

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.31 วินาที
- ผล: PASS_BOUNDED
- วิเคราะห์: ผ่านข้อกำหนด source/keyword ที่กำหนดไว้ในเคสนี้ ไม่ใช่การรับรองทุกข้อกล่าวอ้างหรือสถานะปัจจุบันทั้งหมด

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
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.36 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: ตอบราคา PC รายแพ็กเกจ70 หรือเหมาโซนภายนอกเต็มวัน4000จาก source ตรง scope

### คำตอบจริง

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

## c124: กฎแข่ง ROV ล่ะ

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:competition_source_rag
- เวลา: 1.88 วินาที
- ผล: PASS_TARGET_ONLY
- วิเคราะห์: เปลี่ยนจากราคา PC มาถาม ROV ได้ source/game ถูก แต่แสดงกฎเพียงหนึ่งข้อ ผลนี้ผ่านเฉพาะการเปลี่ยนหมวด ไม่รับรองสรุปครอบคลุมทั้งหมด

### คำตอบจริง

คำตอบ: 4. ระเบียบและกติกาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
•    4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

## c125: วันนี้ PC1 ตอน10โมงว่างไหม

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.62 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เข้าเส้นทาง WordPress สด มีวันเวลาและแหล่งข้อมูล แต่รอบนี้ไม่ได้เทียบแต่ละ slot กับ oracle ที่เวลาเดียวกัน ไม่เรียกว่าความถูกต้องของสถานะจริงผ่าน

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
PC #01 (1 Person) ไม่มีรายการจองในช่วง 10:00-11:00 น. (เวลาไทย) ครับ
อัปเดต: 2026-10-09 23:53:32
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c126: แล้ว PC2 ล่ะ

- หมวด/ภาษา: dialogue / th
- เส้นทาง: pipeline:candidate_margin_clarification
- เวลา: 1.09 วินาที
- ผล: FAIL_CONTEXT
- วิเคราะห์: “แล้ว PC2 ล่ะ” ไม่มีการสืบทอดเจตนาว่าง/วันที่/10โมงใน trace: no_matching_context_resolution จึงถามกลับกว้าง

### คำตอบจริง

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

## c127: เปิดกี่โมง ปิดกี่โมง

- หมวด/ภาษา: hours / th
- เส้นทาง: pipeline:structured_schedule
- เวลา: 0.53 วินาที
- ผล: PASS_SCHEDULE
- วิเคราะห์: ตอบตามตารางบริการที่บันทึกไว้ แยก maintenance กับช่วงเปิด ไม่ใช่การยืนยันวันปิดพิเศษหรืออุปกรณ์สด

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
- เส้นทาง: pipeline:chatbot_identity_en
- เวลา: 0.33 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: ถาม opening hours แต่ถูกเส้นทาง chatbot_identity_en ตอบการแนะนำตัว เป็นการเลือกเจตนาผิด

### คำตอบจริง

I am PSU Esports Assistant, the chatbot for PSU Esports Studio - Phuket. I can help with verified information about games, equipment, booking, opening hours, service fees, rules, competitions, and studio contacts.

## c129: วัน Maintenance ใช้บริการได้ไหม

- หมวด/ภาษา: hours / th
- เส้นทาง: pipeline:general_llm_after_rag_miss
- เวลา: 15.45 วินาที
- ผล: GROUNDING_GAP
- วิเคราะห์: เรื่อง maintenance ของศูนย์กลับตอบด้วยความรู้ทั่วไปของ LLM และไม่มี source ตารางที่มีอยู่ ต้องใช้ตารางช่วงบริการ ไม่ตีความว่า maintenance ทั้งวัน

### คำตอบจริง

ไม่สามารถใช้งานได้ในช่วงเวลาบำรุงรักษาครับ
หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

## c130: Is the studio open on maintenance days?

- หมวด/ภาษา: hours / en
- เส้นทาง: pipeline:structured_schedule_en
- เวลา: 0.54 วินาที
- ผล: PASS_SCHEDULE
- วิเคราะห์: ตอบตามตารางบริการที่บันทึกไว้ แยก maintenance กับช่วงเปิด ไม่ใช่การยืนยันวันปิดพิเศษหรืออุปกรณ์สด

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
- เส้นทาง: pipeline:structured_schedule
- เวลา: 0.92 วินาที
- ผล: FAIL_COVERAGE
- วิเคราะห์: ถามวันอาทิตย์ แต่ตอบตารางจันทร์–ศุกร์โดยไม่บอกผลของวันอาทิตย์ตรง ๆ

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
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.30 วินาที
- ผล: FAIL_COVERAGE
- วิเคราะห์: ถามที่ตั้งกับเวลาเปิด แต่ตอบเพียงที่ตั้ง ต้องวัด coverage แยกทุกคำถามย่อย

### คำตอบจริง

The studio is in Building 5, Floor 1, Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c133: จองเครื่องยังไง ขอขั้นตอนทั้งหมด

- หมวด/ภาษา: booking_process / th
- เส้นทาง: pipeline:conversation_scope_clarification
- เวลา: 0.18 วินาที
- ผล: FAIL_OVERCLARIFICATION
- วิเคราะห์: คำถามขั้นตอนจองมีขอบเขตแล้ว แต่ guard คำว่า “ทั้งหมด” กลับขอให้ระบุเรื่องอีกครั้ง

### คำตอบจริง

ต้องการดูทั้งหมดของเรื่องหรือบริการใดครับ?

## c134: How do I book a PC? Give all the steps.

- หมวด/ภาษา: booking_process / en
- เส้นทาง: pipeline:rule_en
- เวลา: 0.32 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: ตอบขั้นตอนจอง6ขั้นและอ้าง source ของการจอง

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
- เส้นทาง: pipeline:protected_payment_method
- เวลา: 0.36 วินาที
- ผล: FAIL_COVERAGE
- วิเคราะห์: ตอบวิธีโอนเงิน แต่ไม่ได้ตอบว่าเรื่องจ่ายเงินสดมี/ไม่มีข้อมูลยืนยัน ต้องไม่อนุมานว่าระบุการโอนแล้วจึงรับรองข้อห้ามเงินสด

### คำตอบจริง

ชำระเงินโดยโอนผ่าน Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## c136: Can I pay cash when I arrive?

- หมวด/ภาษา: payment / en
- เส้นทาง: pipeline:english_no_answer
- เวลา: 6.35 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: ยังไม่มีข้อมูลยืนยันว่ารับเงินสดหรือไม่ no_answer ไม่แต่งข้อห้าม แต่สามารถตอบวิธีโอนที่มีและบอกว่าเงินสดยังไม่ยืนยันให้มีประโยชน์กว่าเดิม

### คำตอบจริง

I could not find verified PSU Esports Studio - Phuket information for this question.

## c137: มี 100 บาท เล่น PC ได้กี่รอบ บุคคลทั่วไป

- หมวด/ภาษา: budget / th
- เส้นทาง: pipeline:deterministic_calculator_fast
- เวลา: 0.56 วินาที
- ผล: FAIL_BUDGET
- วิเคราะห์: ไม่มีการตีความงบประมาณเป็นงานคำนวณความสามารถซื้อแพ็กเกจ: บางเคสตอบราคาหนึ่งชั่วโมง บางเคสตอบรายชื่อเกมหรือจำกัดจอง 3 รอบ PC บุคคลทั่วไปงบ100ตามอัตราบันทึกควรเล่นได้1รอบ60นาทีและเหลือ30บาท

### คำตอบจริง

ราคา PC 1 ชั่วโมง สำหรับ General Adult / บุคคลทั่วไป: 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

## c138: I have 100 THB and want to play PC as a general adult. How many sessions can I afford?

- หมวด/ภาษา: budget / en
- เส้นทาง: pipeline:rule_en
- เวลา: 0.55 วินาที
- ผล: FAIL_WRONG_POLICY
- วิเคราะห์: ไม่มีการตีความงบประมาณเป็นงานคำนวณความสามารถซื้อแพ็กเกจ: บางเคสตอบราคาหนึ่งชั่วโมง บางเคสตอบรายชื่อเกมหรือจำกัดจอง 3 รอบ PC บุคคลทั่วไปงบ100ตามอัตราบันทึกควรเล่นได้1รอบ60นาทีและเหลือ30บาท

### คำตอบจริง

One booking can include a maximum of 3 sessions.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

## c139: ปุ่มยิงกับรีโหลดใน CS2 คืออะไร

- หมวด/ภาษา: controls / th
- เส้นทาง: pipeline:structured_game_controls
- เวลา: 0.99 วินาที
- ผล: DEVICE_VERIFY_PENDING
- วิเคราะห์: ตอบ mapping จากคู่มือแหล่งรองและแสดงข้อจำกัดแล้ว ยังไม่ได้ยืนยันปุ่มตามเครื่อง/เกมจริงของศูนย์

### คำตอบจริง

Counter-Strike 2 ปุ่มที่ตรงกับคำถาม:
PC
•    Left Mouse Button: ยิง - ยิงอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.holy.gg/en/post/counter-strike-2-keyboard-mouse-controls-pc

## c140: How do I shoot and reload in CS2?

- หมวด/ภาษา: controls / en
- เส้นทาง: pipeline:structured_game_availability_en
- เวลา: 0.39 วินาที
- ผล: FAIL_INTENT
- วิเคราะห์: ถามปุ่มยิงและรีโหลด CS2 แต่ไปตอบว่าเกมมีที่โซนใด เป็นหมวด availability แทน controls

### คำตอบจริง

Counter-Strike 2 is available on: PC #01-#02, PC #03-#10. Studio zone(s): PC Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

## c141: ขอปุ่มควบคุม Tekken 8 ทั้งหมด

- หมวด/ภาษา: controls / th
- เส้นทาง: pipeline:structured_game_controls
- เวลา: 0.93 วินาที
- ผล: SOURCE_QUALITY_ISSUE
- วิเคราะห์: ข้อมูลปุ่ม Tekken ภาษาไทยมีคำอาหรับ “بشكل” ปะปน ต้นตออยู่ใน data/curated/game_control_facts.jsonl แถว394 ไม่ใช่ LLM ใหม่สร้างในรอบนี้

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
- เส้นทาง: pipeline:structured_game_controls_en
- เวลา: 0.40 วินาที
- ผล: DEVICE_VERIFY_PENDING
- วิเคราะห์: ตอบ mapping จากคู่มือแหล่งรองและแสดงข้อจำกัดแล้ว ยังไม่ได้ยืนยันปุ่มตามเครื่อง/เกมจริงของศูนย์

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
- เส้นทาง: pipeline:structured_equipment_item
- เวลา: 0.31 วินาที
- ผล: PASS_RECORDED
- วิเคราะห์: ตอบ CPU/RAM/GPU ตามสเปกในไฟล์ การทดสอบนี้ไม่ใช่ตรวจฮาร์ดแวร์จริง

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
- เส้นทาง: pipeline:structured_equipment_catalog_en
- เวลา: 0.36 วินาที
- ผล: FAIL_COVERAGE
- วิเคราะห์: ภาษาอังกฤษถาม specifications แต่ตอบ inventory ของอุปกรณ์ ไม่ได้ตอบ CPU/RAM/GPU ที่มีในข้อมูล

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
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.18 วินาที
- ผล: FAIL_COVERAGE
- วิเคราะห์: ถามสมาชิก/ที่จอดรถ/บัตร ตอบเพียงสองหัวข้อแรก ข้อมูลบัตรมีแต่รูปคำไม่เข้า matcher

### คำตอบจริง

ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ

มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c146: Do I need membership, is there parking, and what ID should I bring?

- หมวด/ภาษา: multi_topic / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.26 วินาที
- ผล: PASS_MULTI_POLICY
- วิเคราะห์: แยกคำถามย่อยครบและตอบจากข้อมูลเจ้าของ ทั้งภาษาไทยและอังกฤษ

### คำตอบจริง

Membership is not required to use the studio.

Parking for cars and motorcycles is available in front of Building 5.

At arrival, present a national ID card, university student card, school student card, or passport.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

## c147: เอาเมาส์มาเองได้ไหม แล้วจองผิดเครื่องเปลี่ยนยังไง

- หมวด/ภาษา: multi_topic / th
- เส้นทาง: pipeline:multi_question_splitter
- เวลา: 0.57 วินาที
- ผล: PASS_MULTI_POLICY
- วิเคราะห์: แยกคำถามย่อยครบและตอบจากข้อมูลเจ้าของ ทั้งภาษาไทยและอังกฤษ

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
- เส้นทาง: pipeline:multi_question_splitter
- เวลา: 0.22 วินาที
- ผล: PASS_MULTI_POLICY
- วิเคราะห์: แยกคำถามย่อยครบและตอบจากข้อมูลเจ้าของ ทั้งภาษาไทยและอังกฤษ

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
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.09 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เว้นคำระหว่าง VR กับเวลาแล้วเข้า live path ได้ แต่แสดงช่วง09:00–09:30และทรัพยากร morning/afternoonพร้อมกัน ต้องตรวจ fixture ของ effective hour และตัวกรองแพ็กเกจแยก ไม่รับรอง bookable จากไม่มีประวัติจอง

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
โซน VR: ช่วง 09:00-09:30 น. ถูกจอง 0/2 รายการ และไม่มีรายการจอง 2/2 รายการ
•    VR Station (Afternoon) (1-5 Persons) 1 Hour: ไม่มีรายการจอง
•    VR Station (Morning) (1-5 Persons) 30 Mins: ไม่มีรายการจอง
อัปเดต: 2026-10-09 23:56:13
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c150: Is VR free today from 09:00 to 09:30?

- หมวด/ภาษา: live_booking / en
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.19 วินาที
- ผล: LIVE_UNVERIFIED
- วิเคราะห์: เว้นคำระหว่าง VR กับเวลาแล้วเข้า live path ได้ แต่แสดงช่วง09:00–09:30และทรัพยากร morning/afternoonพร้อมกัน ต้องตรวจ fixture ของ effective hour และตัวกรองแพ็กเกจแยก ไม่รับรอง bookable จากไม่มีประวัติจอง

### คำตอบจริง

Date: 2026-10-09 (Asia/Bangkok)
VR Zone: 0/2 resources were booked during 09:00-09:30; 2/2 had no booking.
•    VR Station (Afternoon) (1-5 Persons) 1 Hour: no booking
•    VR Station (Morning) (1-5 Persons) 30 Mins: no booking
Updated: 2026-10-09 23:56:15
Source: https://esports.computing.psu.ac.th/reservation

## c151: วันนี้ PC1 เวลา10โมง และ PC2 เวลา11โมงว่างไหม

- หมวด/ภาษา: live_booking / th
- เส้นทาง: pipeline:live_booking_status_fast_path
- เวลา: 1.20 วินาที
- ผล: FAIL_MULTI_TARGET
- วิเคราะห์: ถามPC1@10โมงและPC2@11โมง แต่ตอบเฉพาะPC1 ต้องรักษาการจับคู่ target+time ทั้งสอง clause

### คำตอบจริง

วันที่ตรวจสอบ: 2026-10-09 (เวลาไทย)
PC #01 (1 Person) ไม่มีรายการจองในช่วง 10:00-11:00 น. (เวลาไทย) ครับ
อัปเดต: 2026-10-09 23:56:16
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## c152: PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่

- หมวด/ภาษา: multi_topic / th
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.13 วินาที
- ผล: FAIL_MULTI_FILTERS
- วิเคราะห์: ถามเกมกับราคา2ชั่วโมงในประโยคเดียว แต่ตอบเฉพาะราคา และทำเลขเขียนเป็นคำ/กลุ่มบุคคลทั่วไปหาย

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
- เส้นทาง: pipeline:structured_service_fee_conversation
- เวลา: 0.21 วินาที
- ผล: FAIL_MULTI_FILTERS
- วิเคราะห์: ถามเกมกับราคา2ชั่วโมงในประโยคเดียว แต่ตอบเฉพาะราคา และทำเลขเขียนเป็นคำ/กลุ่มบุคคลทั่วไปหาย

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
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.38 วินาที
- ผล: PASS_OWNER
- วิเคราะห์: ตอบเงื่อนไขผู้เล่นที่เป็นคนจองหรือมีชื่อในรายการจองตรงข้อมูลเจ้าของ

### คำตอบจริง

คนเล่นต้องเป็นคนที่จองหรือมีรายชื่ออยู่ในรายการจอง ไม่สามารถให้ผู้ที่ไม่มีรายชื่อมาใช้แทนได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c155: นั่งดูเพื่อนต้องเสียเงินไหม

- หมวด/ภาษา: policy_boundary / th
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.34 วินาที
- ผล: FAIL_COVERAGE
- วิเคราะห์: ถามค่าเข้าชม แต่ตอบเพียงอนุญาตให้ดูได้ การอนุญาตกับค่าใช้จ่ายคนละ field ต้องบอกว่าค่าดูยังไม่ยืนยัน

### คำตอบจริง

สามารถมานั่งดูเพื่อนเล่นได้ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008

## c156: Is parking free?

- หมวด/ภาษา: policy_boundary / en
- เส้นทาง: pipeline:user_service_facts
- เวลา: 0.19 วินาที
- ผล: SAFE_UNCONFIRMED
- วิเคราะห์: แยกมีที่จอดรถกับจอดฟรีอย่างถูกต้อง บอกว่าค่าจอดยังไม่มีข้อมูลยืนยัน

### คำตอบจริง

Parking for cars and motorcycles is available in front of Building 5.

Parking fees have not been specified.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008

