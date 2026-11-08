# R121 — วิเคราะห์ข้อผิดพลาดหลังฝึก context planner จริง

## 1. ข้อสรุปจากการวัด planner ที่ครบแล้ว

เปรียบเทียบ HF NF4 base เดียวกันกับ base + LoRA ที่ฝึกจริง 93 optimizer steps บนคำถามเดิม 30 ข้อ:

| ตัววัด | ก่อนฝึก | หลังฝึก |
|---|---:|---:|
| JSON อ่านได้ | 27/30 | 30/30 |
| ผ่าน source-quoted contract | 5/30 | 29/30 |
| focus ตรง label | 14/30 | 20/30 |
| ชุด domain ตรง label | 12/30 | 22/30 |
| domain + facet ตรง label | 5/30 | 19/30 |
| signature ของงานตรงและผ่าน contract | 2/30 | 17/30 |
| จำนวนงานตรง | 26/30 | 30/30 |
| typed constraints ที่ตรง label | 6/27 | 4/27 |

คะแนนดีขึ้นด้านโครงสร้างและการเลือกงาน แต่ **ยังไม่ยืนยันว่าเข้าใจบริบทครบ** และคะแนนทั้งหมดนี้ไม่ใช่ความถูกต้องของคำตอบปลายทาง การฝึกส่วนหนึ่งช่วยเรียนรู้ vocabulary/รูปแบบ JSON ของ contract ใหม่ ซึ่ง base ที่ยังไม่ฝึกไม่มี constrained decoding ช่วยบังคับ จึงห้ามตีความการเพิ่มจาก 5 เป็น 29 ว่าเป็น semantic accuracy

หลักฐาน raw และแผน gold/ก่อน/หลังครบทุกข้อ: `PLANNER_PER_REQUEST_TH.md`; ตัวเลขแยก locale และ paired regressions: `PLANNER_COMPARISON.json`

## 2. ปัญหาเงื่อนไข: โมเดลชอบปล่อยช่องว่าง

หลังฝึก 29 จาก 30 คำถามไม่มี typed constraints มีเพียงโจทย์ VR ที่มีสองระยะเวลาซึ่งสร้าง constraints 4 ตัว โมเดลส่วนใหญ่คืน `context_quotes: []` ด้วย แม้คำถามจะมีชื่อเครื่อง วัน หรือเวลา

### สิ่งที่พิสูจน์ได้

- ชุดสอนมี constraints ไม่ว่าง 115 จาก 244 ข้อ อีก 129 ข้อว่าง
- train มี time เพียง 5 occurrences, negation 3, requested_scope 4 และ condition 6 เทียบกับ service 75, platform 43, audience 37, duration 30
- loss เฉพาะ completion ลดลงได้มากจากการเรียน schema และ field ที่ซ้ำ การมี loss ต่ำจึงไม่ยืนยันว่าทุก slot ถูกแจกแจง
- ตัวตรวจปัจจุบันยอมให้ไม่มี typed slot ถ้าตัวเลขหรือคำปฏิเสธยังอยู่ใน task quote ดังนั้น whole-question quote ผ่านได้โดยไม่แจกแจง slot

### ขอบเขตของข้อสรุป

ข้อความใน task quote ของคำถามเดียวส่วนใหญ่ยังอยู่ครบ การไม่มี typed slot จึงไม่ได้พิสูจน์ว่าความหมายหายไปจากการคำนวณทั้งหมด ตัวอ่านเดิมยังอ่านข้อความนั้นได้ แต่เสียประโยชน์ของการผูกเงื่อนไขอย่างเป็นระบบ โดยเฉพาะงานหลายข้อและบริบทที่ต้องส่งข้ามงาน

### แนวแก้ที่ควรทำ

1. ให้ตัวดึง source spans เสนอวันเวลา จำนวน ระยะเวลา กลุ่มผู้ใช้ และชื่อบริการจากข้อความจริง แล้วให้ planner เลือกและผูกกับแต่ละงาน
2. ตรวจความครบของ critical slots ต่อ task ไม่ใช้เพียงการพบ token ที่ใดก็ได้ในคำถาม
3. เพิ่ม/ถ่วงน้ำหนักตัวอย่าง contrast ของเวลา ปฏิเสธ เงื่อนไข และ ambiguity จากคำถามที่มีอยู่แล้ว
4. วัด slot coverage และการผูกกับงานถูกข้อแยกจาก JSON/focus/domain
5. ถ้าปรับชุดสอนหรือ flow จากผล 30 ข้อนี้ รอบนี้ต้องถือเป็น development ต่อไป แล้วกัน fresh families สำหรับการยืนยันรอบใหม่

## 3. พบข้อบกพร่องในตัวสร้าง annotation ของรอบนี้

`prepare_dataset.py` เรียก `constraints(whole, domain)` สำหรับทุก task ของคำถามหลายงาน ใช้ทั้งประโยคเพื่อเก็บ shared context แต่ยังไม่ได้แยกว่าบริบทใดเป็นของ task ไหนจริง ผลคือ constraint บางตัวรั่วข้ามงาน

ตัวอย่างคำถาม “What are the 8 buttons in Tekken 8, ans what is the PC price”:

- ฝั่งราคาได้รับ requested_scope “8 buttons” ซึ่งเป็นของคำถามปุ่ม
- ฝั่งราคาได้รับ service “Tekken 8” ทั้งที่ต้องอ่านราคา PC
- PC ถูกผูกไปฝั่งปุ่มด้วย โดยประโยคไม่ได้ระบุว่า Tekken เล่นบน PC

นี่เป็นข้อบกพร่องของการจัดทำชุดสอนของผม ไม่ใช่การย้ายข้อมูลธุรกิจไม่ครบ และไม่ควรสอนให้โมเดลเลียนแบบส่วนนี้ต่อ ต้องแก้เป็น **local task spans ก่อน แล้วส่ง shared context เฉพาะที่ความสัมพันธ์ในประโยคยืนยันได้**

เพื่อรักษาหลักฐาน ไม่แก้ label/source ของการฝึกที่เสร็จแล้ว และไม่แอบคำนวณคะแนนใหม่ด้วย gold ที่เปลี่ยนหลังเห็นผล ตัวเลขหลักข้างบนยังเป็นตัววัดเดิม ข้อแก้ annotation ต้องอยู่ใน revision ใหม่และผ่านการตรวจใหม่

## 4. เลือก calendar แทน live status

ตัวอย่างที่ตรวจพบจาก raw planner:

- “Is PC #03-#10 available right now Please keep the answer concise” → schedule/bookable_periods แทน live/live_status
- “is there any free slot from 14:00 to 15:00 ?” → schedule/bookable_periods และไม่ถามข้อมูลที่ขาด

การบอกช่วงเวลาที่เปิดให้จองไม่ยืนยันว่าช่วงนั้นยังว่าง ต้องแยก authority ของปฏิทินประจำกับสถานะจองจริง ในโจทย์ที่ไม่ระบุวัน/บริการ ไม่ควรเดาวันหรือเครื่อง

ชุดสอน live มีเพียง 3 tasks จึงเป็นความไม่สมดุลที่ตรวจนับได้ แต่ยังไม่มี ablation ยืนยันว่าเป็นสาเหตุเดียวของการผิด ต้องตรวจทั้งตัวตีความ ตัวผูกวันเวลา และ live provider แยกกัน

## 5. การแข่งขันกับวิธีเล่น/ปุ่มยังสับสน

“Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?” ถูกเลือกเป็น game_controls/input_bindings ทั้งที่มีบริบทการแข่งขันและถามข้ออนุญาตชัดเจน แม้สะกดผิดก็ยังต้องรักษาบริบทนั้น

สิ่งที่ควรเสริมคือ contrast ระหว่าง permission ในการแข่งขันกับ action ของปุ่ม ใช้ตัวอย่างสะกดผิด/ภาษาพูดที่มีอยู่แล้ว และเก็บ event scope ก่อนค้น rule clause ไม่ขยายกติกาหนึ่งรายการไปอีกปีหรืออีกเกม

ส่วน “Tekken 8 เลือกด่านยังไง” ไม่มีคำว่าการแข่งขันอยู่ในข้อความที่ส่งให้โมเดล แม้ retained benchmark ผูกกับกติกาแข่งขัน ข้อนี้ต้องระบุว่า **label อาศัยขอบเขตจากต้นกำเนิด benchmark มากกว่าข้อความที่มองเห็น** ไม่ควรนับว่าโมเดลผิดความหมายอย่างแน่นอนเพียงเพราะไม่เดาบริบทแฝง ควรถามให้ชัดเมื่อไม่มีประวัติที่ยืนยัน

## 6. ถามบริการที่มีเกม แต่เลือก rental

“What do you need to book to paly FINAL FANTASY XVI” ถูกเลือกเป็น rental/equipment_included แทน games/studio_services

โจทย์นี้ต้องไล่ relation เกม → บริการ/เครื่องที่มีเกม → สิ่งที่ต้องจอง ไม่ใช่เริ่มจากคำว่า book แล้วอ่านแพ็กเกจเช่าสถานที่ และต้องแยกจาก “ขั้นตอนจองทำอย่างไร” ซึ่งเป็น reservation การแก้ควรอาศัยชื่อเกมที่ผูกกับข้อมูลปัจจุบัน ไม่ hardcode ว่าเกมหนึ่งอยู่เครื่องใดในโมเดล

## 7. ambiguity ยังไม่ถูกบังคับพอ

- “General Adult เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท” เก็บทั้งสองระยะเวลาได้ แต่ตั้ง ambiguous=false การตีความอาจเป็นสองระยะเวลาที่ขัดกันหรือหน่วยรอบกับเวลารวม ต้องไม่เลือกอันใดอันหนึ่งเงียบ ๆ
- “Where can I play it?” ไม่มี antecedent ในข้อความทดสอบ แต่ตั้ง target=it, ambiguous=false การที่ quote ตรงกับต้นฉบับไม่ได้ทำให้ it เป็น entity ที่รู้ว่าเป็นเกมใด

ต้องตรวจ native reader/clarifier ต่อ ก่อนสรุปว่าเกิดราคาผิดหรือเลือกเกมผิดจริง เพราะตัวผูก entity และ financial guards อาจป้องกันได้อีกชั้น

## 8. ขอบเขตบางข้อมีหลายคำตอบที่ยอมรับได้

- “When can I play on Monday afternoon” ได้ bookable_periods แทน open_periods: ถ้าคำตอบครอบคลุมเวลาให้บริการ/maintenance ถูกต้อง อาจตอบเจตนาได้ ต้องตรวจเนื้อหาจริง
- “How to book Cockpit and what days is it open?” แยกสองงานถูก แต่เลือก bookable_periods ในงานวันเปิด จึงเป็น facet discrepancy ที่ต้องดูผลตอบ
- “PC ช้กาดจอรุ่นอะไร” focus เป็น equipment_definition แต่ domain/equipment + facet/specifications ถูก: focus ผิดไม่ได้แปลว่าตัวอ่านจะตอบสเปกผิด
- “นายเปนคัยแล้วทำไรไดบ้าง” focus general แทน identity แต่ native task เป็น general ถูกเช่นกัน

ต้องแยก auxiliary focus error, taxonomy/facet mismatch และ actual answer failure ไม่รวมเป็นก้อนเดียว

## 9. Protocol/vocabulary ที่ยังผิดจริง

โจทย์ “What ID does an external visitor need to use the studio?” สร้าง domain=identity ซึ่งไม่มีใน domain vocabulary ทำให้ source contract ไม่ผ่าน ต้องเข้า reservation/owner_policy ตามข้อมูลเอกสารแสดงตัว ไม่ใช่เรื่องตัวตนของศูนย์

แนวแก้คือแยก contrast ระหว่าง identity ของศูนย์กับ identification documents และใช้ grammar/schema decoding เป็นชั้นป้องกัน vocabulary โดยไม่ถือว่าการบังคับ enum ทำให้เลือกความหมายถูกเอง

## 10. การเปรียบเทียบกับระบบเดิมต้องระวัง

- ก่อน/หลังรอบนี้ใช้ HF NF4 checkpoint เดียวกันเพื่อวัด adapter
- ไม่ใช่การเทียบตรงกับ Ollama GGUF + retrieved examples ของ R120
- ไม่ได้วัด accuracy ของ Full 20,554 requests หรือ 55,811 grades
- 30 ข้อมี 13 domains; rental/news ไม่มี fresh test ในรอบนี้
- labels เป็น agent-authored และมีข้อบกพร่องตามข้อ 3 จึงยังไม่ใช่ gold ที่เจ้าของยืนยันทุก field
- การทดสอบนี้ไม่ยืนยัน multi-turn understanding ครบทุกแบบ

## 11. สถานะการนำไปใช้

มี adapter ที่ฝึกจริงและ candidate ที่ต่อ inference ได้แล้ว แต่ **ยังไม่ควรติดตั้งทับ R78 หรือประกาศว่าเข้าใจคำถามครบแล้ว** ต้องอ่านผล API ที่แยกไว้ใน `API_PER_REQUEST_TH.md` ประกอบ ตัวเลือกหลักฐานใช้ base ไม่เปิด context adapter เพื่อไม่เอา schema งานตีโจทย์ไปปนกับ schema เลือกหลักฐาน

ผล API, model transport, ความเร็ว และข้อผิดพลาดปลายทางจะสรุปใน `FINAL_REPORT_TH.md` หลังวัดครบ ทุกครั้งที่รันเพิ่มเพราะตัวประเมิน/ระบบปฏิบัติการผิดพลาดเก็บรอบเดิมไว้ ไม่แก้คำตอบหรือ log เดิม
