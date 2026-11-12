# รอบ 03 — audit planner, ทดลองทบทวนแผน และแก้ตัวตรวจบริบท

## ข้อสรุปที่ตรวจได้จริง

ทำตามแผนแล้ว แต่ **ยังแก้โมเดลให้เข้าใจสองข้อเดิมได้ไม่สำเร็จ** จึงไม่เปิด adapter หรือการทบทวนซ้ำเป็นค่าเริ่มต้น ส่วนที่แก้ได้และนำเข้า preview ทดลองคือการตรวจข้อขัดแย้ง การแยกข้อผิดโมเดลออกจากข้อมูลขาด และการไม่ยืมหลักฐานเงื่อนไขข้ามบริการ

แชต 8145 เป็น `R135-Model-first-trial03` ใช้ compact base planner หนึ่งครั้งและ guard-only ไม่มี second inference โดยปริยาย ส่วน retained wire และ one-review ยังเป็นเส้นทาง opt-in สำหรับการวิจัย รุ่น parent recovery-loop02/owner/live/frozen ไม่แก้ และไม่มีการโหลดน้ำหนักใหม่ หยุด protected model หรือฝึกจาก eval holdout

## 1. Audit ที่พบจากโค้ด ชุดฝึก และ serving provenance

- stage `model_first_plan` เรียก **base** จริง ไม่ใช่ retained adapter
- retained adapter ที่โหลดอยู่ฝึกด้วย root `focus/context_quotes/tasks` จำนวน 244 training rows ส่วน adapter new ฝึก root graph ที่มี version/shared_bindings จำนวน 154 rows
- system message ของ `context_contract.SYSTEM` ใน candidate ตรงกับ hash ของข้อความ system ในชุดฝึก retained ทั้งชุด ไม่ใช่เดาจากชื่อรุ่น
- เส้นทาง context_understanding เดิมใช้ graph wire รุ่นใหม่ร่วมกับการเลือก retained ได้ จึงต้องระบุ protocol/profile แยกกัน ไม่สรุปว่าการเปลี่ยนชื่อ stage อย่างเดียวจะทำให้ตีโจทย์ดีขึ้น
- สร้าง parser/schema เส้นทาง retained ตรงกับ wire เก่า ตรวจ exact quote, target, constraints, duplicate keys และไม่เรียก native correction แก้ category แทนโมเดล

รายละเอียด hash/profile อยู่ `TRAINED_PLANNER_AUDIT.json` ไม่ได้เปลี่ยนข้อมูลหรือชุดฝึก

## 2. ทดลองจริงและสิ่งที่ถอนจาก default

ตรึงคำถาม 6 ข้อก่อนรัน: สองข้อพัฒนาเดิม และสี่ข้อใหม่ต่อ prompt ซึ่งตรวจ normalised exact text แล้วว่าไม่ซ้ำสองไฟล์ train และ saved eval10 ไม่ใช่การรับรอง semantic-family holdout ทั้งสี่ข้อไม่ได้ถูกเพิ่มเป็นตัวอย่าง prompt แล้วใช้ชุดเดียวกันเทียบสองเส้นทางแบบทีละคำถาม

| เส้นทาง | งานตรงคู่ category/field ที่ประกาศไว้ | ผลที่ต้องตีความ |
|---|---:|---|
| retained adapter + wire ตรงชุดฝึก | 0/6 กรณี | ส่วนมาก JSON ไม่จบภายในงบ generation; มีหนึ่งกรณีได้งานรายชื่อเกมแต่ยังตกงานจอง การเรียก adapter ถูกต้องไม่ได้แปลว่าตอบได้ |
| compact base + ทบทวนได้หนึ่งครั้ง | 4/6 กรณี | ข้อเดิม static/controls และ typo+booking ยังผิด; ผล 4/6 เป็นเพียงชนิดงาน ไม่ใช่คำตอบครบหรือ semantic accuracy |

retained ใช้ประมาณ 59–68 วินาทีต่อคำถามในชุดนี้ การตั้ง analysis budget 60 วินาที **ไม่ใช่หลักฐาน hard wall-clock deadline** เพราะเวลาที่วัดยังมีเกิน 60 วินาที การทบทวนแบบสั้นถูกเรียกใน 3/6 คำถาม แต่ไม่มีกรณีใดเปลี่ยนเป็นแผนที่ผ่านตัวตรวจ จึงไม่เปิด second inference เป็นค่าเริ่มต้น

หลังพบ truncated JSON เพิ่ม guard ให้เส้นทาง retained หยุดเมื่อได้ object ที่ยังไม่จบ แทนการเรียกซ้ำแบบเดิม ทดสอบด้วย supplied response แล้ว ไม่ได้รัน retained 6 ข้อใหม่หรืออ้างว่าเวลาชุดเดิมเป็นเวลาหลังเพิ่ม guard

เส้นทาง opt-in one-review จำกัดเพียงหนึ่งครั้ง มี budget gate ก่อนเรียก และยังผ่าน gateway/request call cap เดิม ถ้าทบทวนไม่ผ่านจะเก็บแผนเดิมเฉพาะส่วนที่ยังตรวจได้ ไม่เพิ่มงานจากกฎแทนโมเดล ไม่เอา source facts/คำตอบเดิมเป็น gold ส่งให้โมเดล

## 3. อ่านคำตอบจริงแยกจากคะแนนชนิดงาน

| คำถาม | เจตนา | ข้อจำกัดคำตอบจริง |
|---|---|---|
| Tekken โซน + เครื่องที่มีเกม | โมเดลเลือก controls ผิดสำหรับส่วนเครื่อง | ยังไม่ตอบส่วนเครื่อง แม้มีข้อมูล; final guard ระบุเป็น model-plan conflict และรักษาคำตอบโซน |
| มีเกสอะไรบ้าง แล้วจองยังงไ | เหลือ game_catalog งานเดียว | ยังตกงานจอง ตัวตรวจยังแสดงงานที่ขาด ไม่ถือว่าตอบครบ |
| English zone + services | ชนิดงานสองส่วนถูก | ช่วงข้อความงานที่สองตัดเลข edition 8 ออก แม้ตอบจาก relation ปัจจุบันได้ จึงยังไม่รับรองการรักษา edition/บริบททั่วไป |
| Nintendo 30 นาที + วิธีจอง | ชนิดงานสองส่วนถูก | แสดงอัตราต้นทาง 60 นาที พร้อมข้อจำกัด ยังไม่ได้ยอดสำหรับ 30 นาที; หน่วย/ช่วงคนต้องตรวจความหมายเพิ่ม ไม่รับเป็น full answer acceptance |
| PC นักศึกษา 30 นาที + PS5 บุคคลทั่วไป 30 นาที | งานราคาสองส่วนถูก | PC ใช้เงื่อนไขได้ แต่ PS5 ยังยืนยัน 30 นาทีไม่ได้; พบข้อผิดในตัวตรวจที่เคยยืม proof PC ไปยืนยัน PS5 แล้วแก้ในรอบนี้ |
| Tekken โซน + ปุ่มโจมตี + วิธีจอง | แยกสามชนิดงานได้ | โซนและวิธีจองตอบได้ แต่ส่วนปุ่มถูกระงับ ต้องตรวจ action/reader ต่อ ไม่สรุปว่าต้นทางไม่มีข้อมูล |

ดังนั้น **ไม่ใช้ 4/6 เป็นคะแนนความถูกต้องของคำตอบ และเทียบตรงกับ 2/4 รอบก่อนเพื่ออ้าง improvement ไม่ได้** เป็นคนละชุดและยังมีปัจจัยเวลา/backend

## 4. ข้อผิดตัวตรวจที่พบและแก้สาเหตุร่วม

### 4.1 “ทั่วไป” ถูกตีเป็นการเปลี่ยนบริการ

regex เดิม `(?:pc|ps5).*(?:ไป|เป็น).*(?:pc|ps5)` จับคำว่า “ไป” ภายใน “ทั่วไป” ระหว่าง PC กับ PS5 ทำให้คำถามราคาสองบริการถูกเพิ่ม observed intent `policy.change_service` แล้วแจ้งขาดงานที่ผู้ใช้ไม่ได้ถาม

แก้เฉพาะ transition predicate ให้ต้องมีคำเปลี่ยน/ย้าย/ไปที่ติดกับชื่อบริการตามรูปประโยคที่รองรับ รักษาคำถามจริงเช่น “PC ไป PS5 ได้ไหม”, “จาก PC ไปเป็น PS5”, “เปลี่ยนเครื่องระหว่างเล่น” ไม่ปิดการตรวจ policy ทั้งหมวด

### 4.2 หลักฐานเงื่อนไขข้ามงาน

observer แบ่งคำถามราคาสองบริการเป็น coarse clause เดียว เดิมดึงทุก task ที่ทับ clause มาตรวจ duration ทำให้ proof ของ PC 30 นาทีผ่านให้ PS5 30 นาทีด้วย แม้ PS5 แสดง source rate 60 นาที

สำหรับ numeric constraints ที่มี literal owner ในหลายงานและไม่มี shared binding ให้เลือก task ที่ครอบ raw span ของตัวเลขนั้นจริง หลังแก้ PC duration ยังผ่าน ส่วน PS5 duration เป็น `review_required` และมีข้อความแจ้ง ส่วน shared/anaphoric bindings คงตัวตรวจเดิม ไม่อ้างว่ารอบนี้พิสูจน์ shared scope ทุกแบบ

### 4.3 แผน controls ผิด ไม่ใช่หลักฐานว่าข้อมูลไม่มี

guard ใช้ control predicate ที่มีอยู่กับชื่อเกมต้นทาง เมื่อโมเดลเลือก controls แต่คำถามไม่มี predicate ควบคุม ให้ถือว่าแผนขัดแย้ง ไม่สลับ category ไป services เอง ไม่ส่ง claims ของงานนั้น และแจ้งว่าโมเดลตีความไม่ผ่านการตรวจ แยกจาก source gap

## 5. ผลก่อน–หลังและ regression

- source replay ก่อนแก้ change_service/numeric owner ผ่าน **12/18** หลังแก้ **18/18**
- final supplied-wire/budget/review controls **20/20**
- final compact review/guard/source controls **13/13**
- affected context/contract regression **21/21**
- currency/source evidence **12/12**
- alternative-duration/source mutation **20/20**

รวม 6 ชุดเป็น 104 checks ที่อาจมีพฤติกรรมทับซ้อนกัน ทั้งหมด source/mock/replay **ไม่ใช่ 104 inference และไม่ใช่ semantic accuracy** เก็บ initial harness error ของ compact review ไว้: ตัว observer ไม่เห็น static need จึงไม่เรียก review ตามที่ harness คาด ตรวจเพิ่มด้วย source-bound control predicate จึงตรวจ conflict นี้ได้ ไม่อ้างว่า observer เข้าใจภาษาทั่วไปครบ

## 6. HTTP สุดท้ายหลังแก้ รวม 2 requests ตามลำดับ

1. ราคาสองบริการ **12.50 วินาที**: เก็บสอง tasks/claims, ไม่แจ้งงานจองเทียม, PC 0 บาทยังอยู่, PS5 ไม่ยืม PC proof และยังแจ้งเงื่อนไข 30 นาทีที่ยืนยันไม่ได้
2. Tekken สองส่วน **6.40 วินาที**: ตอบโซนได้ ส่วนเครื่องยังเป็นข้อผิดเจตนาของโมเดล แต่แจ้งตรงสาเหตุและไม่มี claims จาก invalid-plan part

ทั้งสองใช้หนึ่ง model call ต่อ request พร้อม persisted trace ผ่าน 15 checks ทั้งหมด เป็นการตรวจ guard/delivery สองกรณี **ไม่ได้หมายความว่าเจตนา Tekken ถูกแก้แล้ว** เวลาสองตัวอย่างนี้ไม่ใช่ latency benchmark ทั้งระบบ

## 7. สถานะและขั้นถัดไป

เปิดเฉพาะ preview ทดลอง trial03 แบบ compact + guard-only ส่วน retained/review เป็น opt-in ที่ยังไม่ผ่าน ไม่ติดตั้งจริง ไม่รัน 200/2111 ไม่แก้ R132 ไม่ claim 48/76 completion

งานเจตนาที่ยังเปิด: static services vs controls, typo secondary need, edition/context ที่หลุด, same-question shared scopes และ action binding ของปุ่มเกม งาน semantics ข้อมูลที่ยังเปิด: หน่วย/ช่วงคนราคา, duration ที่ไม่ตรงต้นทาง, authority/currentness, owner editor HTTP lifecycle และ attachments; cooldown/hard deadline ยังไม่ปิด

หยุดวนการเปลี่ยน prompt/review แบบเดิมหลังผลจริงไม่ช่วย ขั้นถัดไปใช้กรณีล้มเหล่านี้ audit output contract และ relation/action binding เพื่อเลือก source-grounded operation proposal หรือการฝึกแผน compact แยกในอนาคต โดยยังไม่เริ่มฝึก/เปลี่ยน protected weights และไม่ใช้ eval holdout เป็นชุดฝึก ต้องตรวจทั้ง positive, wrong-entity, omitted-need และคำถามใหม่ก่อน promote

หลักฐาน raw/DB/logs อยู่ D แบบ private; code, audit hashes, summary และรายงานเข้า Git ได้ รายการ hash อยู่ ROUND03_MANIFEST.json รุ่นก่อนทุกชุดยังเก็บอยู่
