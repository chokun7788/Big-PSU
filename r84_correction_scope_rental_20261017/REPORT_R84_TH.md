# ผลแก้ไข R84: ขอบเขต correction และราคาเหมา

## สรุป

ติดตั้งในแชท Format กลาง R78 ที่ http://127.0.0.1:8115/ แล้ว เปิด LLM และตรวจ fingerprint ของโค้ดที่โหลดจริงก่อนทดสอบ ไม่ได้ทดสอบ full corpus, legacy หรือ LLM OFF ฐานข้อมูลยังเป็น migration preview ไม่มีการอนุมัติหรือเผยแพร่ราคาแทนเจ้าของ

- ชุดเป้าหมายเดียวกันก่อนแก้ 15/26 → candidate 26/26 → เว็บที่ติดตั้งจริง 26/26 ข้อ เป็น 20 บทสนทนา มี 6 บทสนทนาที่ถามต่อสองรอบ
- ตรวจสอดคล้องกับ workbook: จำนวนเงิน + audience + ครึ่งวัน/เต็มวัน 24/24 รายการ ไม่ใช่การยืนยันอัตราปัจจุบันโดยเจ้าของ
- Unit/ขอบเขต/เทียบ source 70/70, qualified reply 41/41, rejection/replacement 34/34 สองชุดหลังใช้ model transport ที่ควบคุมไว้ ไม่ใช่คะแนนโมเดลจริง
- generation ของโมเดลจริงผ่าน และ selector จริงใน candidate/web ผ่าน แยกจากการตรวจเนื้อหาข้างต้น

## สิ่งที่ใส่ไว้เรื่องราคาเหมา

ใน DB มี rental_package 24 รายการ = 6 รูปแบบ × 2 ช่วงวัน × 2 กลุ่มหน่วยงาน ได้แก่ทุกโซน, PC, PS5, Nintendo Switch, Cockpit, VR เป็นราคาเหมาโซนสำหรับหน่วยงานภายใน/ภายนอก ไม่ควรแปลงเป็นราคาต่อเครื่องหรือต่อคนเอง

ไฟล์ต้นฉบับ: D:\Download New\ค่าบริการครึ่งวันและเต็มวัน PSU Esports Studio - Phuket (1).xlsx
เซลล์ราคา: ค่าบริการเช่าห้อง PSU Esports S!B3:E8
SHA256 ต้นฉบับและไฟล์ที่ติดมากับระบบตรงกัน: `bbcc850c1b348e79b9c65577ebf2a284f26fc81674c1d44de9e8e846653b8894`

| รูปแบบ | ภายนอกเต็มวัน | ภายนอกครึ่งวัน | ภายในเต็มวัน | ภายในครึ่งวัน |
|---|---:|---:|---:|---:|
| ทุกโซน | 12,000 | 6,000 | 6,000 | 3,000 |
| Cockpit | 2,000 | 1,000 | 1,000 | 500 |
| VR | 6,000 | 3,000 | 3,000 | 1,500 |
| Nintendo Switch | 2,000 | 1,000 | 1,000 | 500 |
| PS5 | 2,000 | 1,000 | 1,000 | 500 |
| PC | 4,000 | 2,000 | 2,000 | 1,000 |

หน่วย: บาทตาม workbook ประวัติ source เชื่อมกับ records ได้ใน RENTAL_AUDIT.json ไม่คำนวณส่วนลด/ราคาเหมาต่อชั่วโมงจากครึ่งวันเอง

## ทำไมยังตอบผิดทั้งที่ข้อมูลมี

### 1. จับ task ถูก แต่ subject ผิด

คำว่า wrong/incorrect/ผิด ทำให้ candidate เสนอ procedure_wrong_slip ได้ทั้งกรณีรูปสลิป ยอดเงิน และเอกสารตัวตน เมนู confirmation เดิมตรวจ task/context/ownership แต่ไม่ป้องกันวัตถุที่ขัดกัน จึงถามยืนยันหัวข้อสลิปแม้ผู้ใช้ระบุชัดว่าเป็น passport หรือ amount

แก้ด้วย correction_scope ที่แยกประเภทวัตถุชัดเจนจากภาษาของหมวด ใช้ร่วมกันที่ literal profile, retrieval/model candidates และ fallback menu โดย derive ประเภทของ source จาก query_profile.subjects ไม่ผูก record ID และไม่สร้างวิธีแก้รายการเอง

### 2. FAQ ซ้ำที่ไม่มี query_profile ยังถูกเลือกผิดได้

Candidate 1 ปิดเมนูสลิปผิดเรื่องแล้ว แต่ “แนบรูปบัตรนักศึกษาผิด” ยังถูกเลือกเป็นรายการเอกสารเช็กอิน และ “The amount I paid was wrong” ถูกตอบด้วย FAQ สลิปอีก record หนึ่งที่ไม่มี profile นี่เป็น content failure ไม่ใช่ transport failure

แก้ให้ตรวจ known-unconfirmed need ก่อน semantic selection เมื่อยังไม่มี source ที่ระบุได้ตรง ยอดเงินผิด/เอกสารตัวตนผิดจึงระบุสิ่งที่ยังไม่มีวิธีดำเนินการยืนยัน พร้อมช่องทางศูนย์ คำถามยอดเงินผิดยังถามต่อว่าโอนเกินหรือขาด ไม่ยืนยันขั้นตอนคืนเงินเอง ข้อมูลที่ตรง source ชัดเจนยังเข้าสู่เส้นทาง source ปกติก่อน

### 3. ราคาเหมาอยู่ครบ แต่ operation / audience / zone scope ผิด

- How much มี priority สูงกว่า half-day rental จึงค้นราคารายชั่วโมงที่หมดอายุ แก้ priority ให้ rental ที่ระบุชัดทำงานก่อน price ทั่วไป
- External organization ไม่ตรง External organizations ขณะที่ Internal organization ไม่ตรง Internal unit จึงอาจตอบทั้งสองกลุ่ม แก้ grammar ของหน่วยงานแล้ว map เฉพาะ audience ที่ประกาศว่าเป็น internal/external organizational actor ไม่มีการจับ visitor เป็น General Adult หรือหน่วยงานภายนอก
- ทุกโซนภาษาไทยไม่ถูกผูกกับ zone All Zones จึงคืนทุกแพ็กเกจแยกโซน แก้ให้เลือก zone รวมที่มีอยู่จริงใน source

## ผลเว็บจริงแยกภาษา

| ภาษา | ผ่าน | มัธยฐาน HTTP วินาที |
|---|---:|---:|
| th | 13/13 | 0.850 |
| en | 13/13 | 0.850 |

เวลาจากชุดเล็กหลังเตรียมโมเดล ไม่ใช่ latency guarantee หรือผล load test โมเดลเปิดอยู่ แต่คำถามที่อ่านข้อมูลตรง/known-unconfirmed ไม่จำเป็นต้องเรียกโมเดลทุกครั้ง

## เทียบทุกคำถามในชุดเดียวกัน

| ภาษา | คำถาม | ก่อน | หลัง candidate | เว็บจริง |
|---|---|---|---|---|
| en | I attached incorrect proof of identity. How do I fix it? | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| th | ส่งหลักฐานยืนยันตัวตนผิด ต้องแก้ยังไง | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| en | I uploaded the wrong passport document. How do I correct it? | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| th | แนบรูปบัตรนักศึกษาผิด ต้องแก้ยังไง | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| en | The payment amount was incorrect. How do I fix it? | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| en | The amount I paid was wrong. How can I correct it? | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| th | ยอดเงินที่โอนผิด ต้องแก้ยังไง | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| th | ผมชำระจำนวนเงินผิด ต้องแก้ยังไง | wrong_slip_menu_or_source, not_specific_unconfirmed_need | ผ่าน | ผ่าน |
| en | I attached incorrect proof of payment. How do I fix it? | ผ่าน | ผ่าน | ผ่าน |
| en | yes | ผ่าน | ผ่าน | ผ่าน |
| th | แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง | ผ่าน | ผ่าน | ผ่าน |
| th | ใช่ | ผ่าน | ผ่าน | ผ่าน |
| th | ผมอัปโหลดรูปหลักฐานโอนเงินผิด ต้องแก้ยังไง | ผ่าน | ผ่าน | ผ่าน |
| th | ใช่ครับ | ผ่าน | ผ่าน | ผ่าน |
| en | I uploded the wrong payment attachement. How can I correct it? | ผ่าน | ผ่าน | ผ่าน |
| en | yes | ผ่าน | ผ่าน | ผ่าน |
| en | Can I bring my own input peripheral? | ผ่าน | ผ่าน | ผ่าน |
| en | keyboard | ผ่าน | ผ่าน | ผ่าน |
| th | ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม | ผ่าน | ผ่าน | ผ่าน |
| th | ใช่ แต่เป็นเมาส์ของผม | ผ่าน | ผ่าน | ผ่าน |
| th | เหมา PC เต็มวัน หน่วยงานภายนอกราคาเท่าไหร่ | ผ่าน | ผ่าน | ผ่าน |
| en | Full-day PC zone rental for an external organization price | wrong_package_scope | ผ่าน | ผ่าน |
| th | เหมา VR ครึ่งวัน หน่วยงานภายในราคาเท่าไหร่ | ผ่าน | ผ่าน | ผ่าน |
| en | How much is half-day PS5 zone rental for an internal organization? | wrong_package_scope, missing_source_price | ผ่าน | ผ่าน |
| th | เหมาทุกโซนเต็มวันหน่วยงานภายนอกราคาเท่าไหร่ | wrong_package_scope | ผ่าน | ผ่าน |
| en | Full-day all zones rental for external organizations price | ผ่าน | ผ่าน | ผ่าน |

## ตัวอย่างคำตอบหลังแก้

### The amount I paid was wrong. How can I correct it?

The information I could read does not confirm how to correct an incorrect payment amount. Please contact the studio staff to confirm before proceeding.
Was the payment above or below the booking amount? I cannot yet confirm a correction or refund procedure.
Studio page: https://www.facebook.com/psuesportsphuket [S1]

### แนบรูปบัตรนักศึกษาผิด ต้องแก้ยังไง

จากข้อมูลที่อ่านได้ ยังยืนยันวิธีแก้ไขเอกสารหรือหลักฐานยืนยันตัวตนที่ผิดไม่ได้ครับ กรุณาติดต่อเจ้าหน้าที่เพื่อยืนยันก่อนดำเนินการ
เพจศูนย์: https://www.facebook.com/psuesportsphuket [S1]

### How much is half-day PS5 zone rental for an internal organization?

**PlayStation 5 Zone Internal Unit half_day**
• Package price: 500.00 THB [S1]
• audience id: Internal unit [S2]
• currency: THB [S3]
• period label: Half day [S4]

English translation is machine generated and has not been reviewed by the owner.

### เหมาทุกโซนเต็มวันหน่วยงานภายนอกราคาเท่าไหร่

**All Zones หน่วยงานภายนอก full_day**
• ราคาแพ็กเกจ: 12,000.00 THB [S1]
• เลือกกลุ่มผู้ใช้ที่ใช้ราคานี้: หน่วยงานภายนอก [S2]
• สกุลเงิน: THB [S3]
• ครึ่งวัน / เต็มวัน / ช่วงที่กำหนดเอง: เต็มวัน [S4]
• เช่น ค่าเจ้าหน้าที่นอกเวลา: ค่าตอบแทนของเจ้าหน้าที่ทำงานนอกเวลาเบิกตามระเบียบมหาวิทยาลัย [S5]

## ข้อจำกัดและข้อมูลที่ต้องถามเจ้าของ

1. ครึ่งวันและเต็มวันของการเหมาเริ่ม/สิ้นสุดกี่โมง และนับเป็นกี่ชั่วโมง? source ยังไม่ให้ข้อมูล ไม่กำหนด 4/8 ชั่วโมงเอง
2. ต้องการขายราคาเหมาต่อชั่วโมงด้วยหรือไม่? ถ้ามี ต้องระบุราคา/โซน/กลุ่มผู้ใช้/ขั้นต่ำจากเจ้าของ ไม่หารราคาเหมาวันเอง
3. ราคาเหมา 24 รายการนี้มีผลเริ่มวันไหนและสิ้นสุดวันไหน? validity ปัจจุบันยัง unknown ไม่เติมวันที่แทนเจ้าของ
4. การจองแบบเหมาทำช่องทางใด ชำระ/มัดจำ/เปลี่ยน/ยกเลิกอย่างไร และค่าเจ้าหน้าที่นอกเวลาคิดกับผู้ขอใช้แบบไหน? workbook มีเพียงข้อความเบิกตามระเบียบ ไม่สรุปว่าอยู่ในราคาหรือใครเป็นผู้จ่าย
5. ถ้ายอดเงินผิดหรือเอกสารตัวตนแนบผิด เจ้าหน้าที่ให้ดำเนินการอย่างไร? รอบนี้ตอบสถานะยังไม่ทราบอย่างจำเพาะ ไม่เพิ่มนโยบาย
6. เป็นชุดทดสอบเฉพาะจุด ไม่พิสูจน์ประโยคหลายเงื่อนไข/การปฏิเสธ/คำผิดทุกรูปแบบ ประเภทที่ไม่มี grammar ยังต้องใช้การถามยืนยัน/อ่าน source ตามกลไกเดิม ไม่มี claim ว่าแก้ NLP ครบทุกความหมาย
7. ข้อความอังกฤษที่เพิ่ม/แปลใหม่ยังเป็น machine/agent translated ตาม metadata ไม่อ้างว่าเจ้าของตรวจรอบนี้แล้ว

## การรักษาข้อมูลและหลักฐาน

- เปลี่ยนโค้ดเฉพาะ 8 ไฟล์ใน R78 มี before/candidate และ CHANGESET.patch ฐานข้อมูลไม่เปลี่ยน strict binding และ compact opening ไม่เปลี่ยน ตรวจไฟล์ app/UI อื่น 396 ไฟล์ไม่เปลี่ยน
- ไม่เขียนทับโครงการ Downloads, workbook, approvals, releases หรือ log รอบก่อน ผลทดลองที่ล้มและ candidate 1 ยังอยู่
- baseline_1 ยังไม่ถาม chatbot เพราะ model-list timeout 4 วินาที ตรวจซ้ำ endpoint ปกติภายใน 0.5 วินาที ไม่อ้างว่า timeout เป็นข้อผิดพลาดเนื้อหา และไม่ปิด LLM เพื่อให้คะแนนผ่าน

หลักฐาน:
- BASELINE_MANIFEST*.json, INSTALLATION.json, SOURCE_INVENTORY_BEFORE.json, CHANGESET.patch
- RENTAL_AUDIT.json, verification/unit_2/UNIT_RESULTS.json
- verification/baseline_2/SUMMARY.json และ TURNS.jsonl
- verification/candidate_1/SUMMARY.json และ verification/candidate_2/SUMMARY.json
- verification/qualified_final/RESULTS.json และ verification/rephrase_final/RESULTS.json
- เว็บจริง: C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r84_correction_scope_rental_20261017\web_results\20261017T084200Z-19ec21

เทสใหญ่ยังพักไว้จนกว่าผู้ใช้สั่งใหม่
