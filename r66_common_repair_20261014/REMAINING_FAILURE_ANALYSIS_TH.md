# อ่านผลที่ยังไม่ผ่านอย่างไร — สาเหตุระดับคำตอบและเกณฑ์ตรวจ

เอกสารนี้อธิบายสาเหตุที่พบจาก raw final16 และลูปแก้ K/L ก่อนรอบยืนยันใหม่ ผลตัวเลขล่าสุดต้องอ่าน R66_FINAL_REPORT_TH.md ตาม tag ที่ระบุ ไม่ใช้ final16 แทนโค้ดหลังแก้ L และไม่สรุปว่าข้อที่ไม่ผ่านทั้งหมดเป็นเพราะเกณฑ์ตรวจ

**สถานะหลังลูป M/N:** เติมคำแปล note ทั้ง 390 แถวแล้ว และ agent เทียบไทย/อังกฤษพร้อมแก้อีก 64 จุด เก็บ raw model proposals ทุกชุดไว้ fallback ไทยในลูป L ยังทดสอบเพื่อรองรับข้อมูลเก่า การอ่าน English notes ครบใน candidate นี้ไม่ใช่ human/owner approval และไม่รับรองข้อมูลแปลทุกช่องอื่นทั้งหมด เรื่อง power permission เปลี่ยนไปอ่าน source โดยตรงแล้ว ผล matrix ต้องดูรายงานล่าสุด

## 1. คำตอบผิดหัวข้อจริง แม้ฐานข้อมูลมีคำตอบ

| คำถาม | คำตอบก่อนแก้ | กลไกที่ทำให้เลือกผิด | ควรทำ | การแก้และหลักฐาน |
|---|---|---|---|---|
| ทำ PS5 เสียหาย ค่าปรับกี่บาท / how much is the fine | ค่าบริการ PS5 | price cue มาก่อน damage policy; จำนวนเงินอย่างเดียวบอกชนิดเงินไม่ได้ | เลือกเงื่อนไขความเสียหายพร้อมระดับค่าปรับ; ไม่ยืมค่าบริการ | ลูป K, intent_priority tests; คำตอบ before/after แยกไฟล์ |
| cancel a paid booking | กำหนดชำระเงิน 10 นาที | paid ชนะ cancel action | ขั้นตอนยกเลิก/เงื่อนไขจาก source ที่ตรงการกระทำ; ไม่รับรองคืนเงินหาก source ไม่บอก | แยก manual cancellation กับ unpaid timeout |
| PC #03 available for Warzone today at 15:00 | เกมที่ติดตั้งใน PC #03 | live regex ไม่รับคำคั่น และ installation reader ตอบก่อน | ให้ live adapter ตรวจสถานะเวลานั้น; ถ้า API ไม่พร้อมให้บอกยืนยันไม่ได้ | ลูป K: time + occupancy มาก่อน installation; static game catalog ยังเป็น static |
| What does A do in Moving Out 2 on Nintendo Switch? | ขอเลือก title/หัวข้อ | มีชื่อเกมแต่ไม่มีคำ controls/button ในรูปประโยคนี้ | อ่านปุ่ม A ใน control_set ที่ตรง platform เท่านั้น | ลูป L: กรอบ what does <controller key> do พร้อมตรวจ projection |

จุดร่วมคือ schema ที่ถูกต้องและ source ที่มีอยู่ยังไม่พอ ต้องยืนยัน operation, field และความสัมพันธ์ให้ตรงคำถามก่อน render LLM ที่เลือก ID ถูกชนิดก็ยังเลือกเอกสารผิดหัวข้อได้ จึงต้องตรวจ semantic guard แยกจาก JSON schema

## 2. คำตอบตกหล่นจากข้อมูลแปลจริง

### ค่าปรับ

Thai source มี minor 100–500 บาท, moderate ราคาจริงหรือ 500–2,000 บาท, severe ราคาทรัพย์สินเต็มจำนวน แต่ English FAQ ที่ถูกเลือกมีเพียง minor/severe กว้าง ๆ ไม่มีตัวเลขและ moderate condition นี่เป็น **content omission** จริง มิใช่แค่ต้องการคำว่า THB แทนบาท

แก้เป็น draft revision ใหม่โดยเทียบ Thai source กับ existing natural English FAQ ที่มีช่วงครบ รักษา original revision/source และไม่สร้าง owner approval ดู DAMAGE_TRANSLATION_REPAIR.json และ release audit ที่แยก intentional English revision

### Controls

36 records / 390 rows เก็บปุ่มกับชื่อ action อังกฤษ แต่ note column อังกฤษว่าง ขณะที่ไทยมีคำอธิบาย เช่น Mario Party Superstars มี 100 minigames; Moving Out 2 ใช้ปุ่มบ่าได้ 4 ปุ่ม การทดสอบชื่อปุ่มอย่างเดียวตรวจไม่เจอข้อมูลหายเหล่านี้

สิ่งที่แก้แล้ว: จับคู่เฉพาะจำนวนแถวและป้ายปุ่มตรงกัน กู้ note ไทยเข้าคำตอบพร้อม Translation pending เลือกเฉพาะแถวที่ถาม และบันทึก localization_gaps/partial status ไม่เปลี่ยน stored source

งานที่ต้องทำหลังพบปัญหา: แปล EN notes ทั้ง 390 แถวและทบทวน fidelity ซึ่งลูป M ได้ทำเป็น draft revisions แล้ว พบ model proposals ที่ literal guard ยอมรับแต่ผิดความหมายอีก 64 จุดจึงแก้จากไทย เก็บหลักฐานใน CONTROL_NOTE_AGENT_REVIEW.json ไม่เรียกการตรวจนี้ว่า English ทั้งระบบได้รับอนุมัติแล้ว

## 3. เนื้อหาตรง แต่ literal contract ต้องการประโยคอังกฤษแบบเดียวเท่านั้น

ตัวอย่าง CS2 protests: actual answer ใช้ Objections, within 15 minutes after the match ends, by only the team captain or coach ส่วน grader ต้องการ Protests must be submitted ... by the team captain or coach only แบบเต็มประโยค ตัวเลข ผู้มีสิทธิ์ และเงื่อนไขเวลาตรงกัน แต่ clause string ไม่ตรง

ตัวอย่าง VALORANT forfeit: source-backed answer มี 13-0 แต่ syntax ไม่ตรงประโยค gold; macros/food มี macros prohibited และ sealed drinking water/chewing gum แต่ gold ไม่รับคำต่างรูป; Tekken 1-1 tie มี deciding game แต่ phrasing ต่าง

ต้องอ่าน full answer และต้นฉบับครบ ไม่แก้ source หรือเปลี่ยนคะแนนย้อนหลังเพียงเพื่อให้ string ตรง ความหมายที่กำกวม เช่น readiness/availability ของอุปกรณ์ ยังควรอยู่ในรายการ translation review ไม่เหมารวมว่าทุก synonym เท่ากันแน่นอน

## 4. ตัวเลขตรง แต่หน่วยหรือรูปเขียนทำให้ไม่ผ่าน

PC 2 ชั่วโมง: actual แสดง 120 นาที, 2 รอบ, 140.00 THB และฐาน 70.00 THB ต่อ 60 นาที ส่วน gold ต้องการ 2 ชั่วโมง, 2 session, 140 บาท, 70 บาท/session จึงตกหลาย required strings การยืนยันว่าคำนวณถูกต้องมาจาก source algorithm และ boundary oracle แยก ไม่ได้มาจากการนับ strings ที่มีตัวเลขตรงกัน

guests comparison: actual Please specify the service and both audience groups... แต่ gold ต้องการ Which service แม้เป็นการถาม slot เดียวกัน ยังต้องดูว่ามี typed state และถามต่อ PC/กลุ่มได้จริง ไม่ใช้ประโยคคล้ายกันเป็นหลักฐานว่าบทสนทนาผ่าน

## 5. Gold ต้องการราคาที่พ้นวันมีผล

คำถาม VR บุคคลภายนอก/PS5 staff/PS5 games+price/Tekken price ต้องการ 525/1,050/0/150 บาทจากตารางที่ระบุถึง 31 มีนาคม 2026 ขณะ test clock อยู่ตุลาคม 2026 ระบบจึงไม่ควรแสดงตัวเลขนั้นเป็นราคาปัจจุบันเพียงเพื่อผ่าน test

คำตอบที่ควรได้: แยกส่วนเกมที่ตอบได้ออกจากราคาปัจจุบันที่ยังยืนยันไม่ได้ ระบุอายุ source และกลุ่มบริการที่ตรงคำถาม ราคา PC ที่กู้จาก local update มีตัวเลขเดิมยืนยัน แต่วันมีผลยัง unknown เช่นกัน จึงเป็น recorded-rate calculation พร้อมข้อจำกัด มิใช่ current-price guarantee

ต้องขอ **ตารางล่าสุดและช่วงมีผล** จากเจ้าของ ส่วนเรื่องคำนวณ/ชนิดกลุ่ม/เลือกบริการแก้ทางเทคนิคได้เอง

## 6. Source คนละระดับให้รายละเอียดไม่เท่ากัน

VR without booking: owner walk-in FAQ ยืนยันว่าต้องจองผ่านระบบ แต่ไม่มีเวลาอย่างน้อย 1 ชั่วโมง ส่วน published-policy text อีก record ระบุ 1 ชั่วโมง คำตอบที่เลือก FAQ จึงยืนยัน booking required ได้ แต่ยังไม่ตอบ timing condition ที่ gold ต้องการครบ

ไม่ควรแต่งว่า walk-in ได้ยกเว้นหนึ่งชั่วโมง หรือเอาตารางนโยบายคนละบริบทมารวมเป็นข้อยืนยันโดยไม่ตรวจ authority/validity กรณีเผยแพร่จริงต้องเก็บความแตกต่างนี้ใน source conflict review และถามให้ชัดว่าการ walk-in จองแล้วใช้ทันทีได้หรือไม่ หรือยังต้องรอหนึ่งชั่วโมง

PS5 daily limit: source บอก 3 sessions **ต่อการจอง** ไม่ใช่ **ต่อวัน** การตอบว่าไม่มี daily cap ที่ยืนยันพร้อมแสดง per-booking limit จึงปลอดภัยกว่าการคูณ/สรุป 3 ชั่วโมงต่อวัน

## 7. Source IDs และ protocol ของระบบเก่า

Common route knowledge/common_read แตกต่างจากเดิม competition_rules/service_fee/games เป็นต้น และอาจมี common IDs แทน legacy chunk IDs การตก route หรือ canonical evidence ID ไม่พิสูจน์ว่าข้อเท็จจริงผิด แต่ก็ไม่ใช่เหตุให้ลบ grader ออก

adapter ทำ canonical lineage ได้เฉพาะ exact document/chunk/hash ที่ตรวจได้ ชื่อคล้ายกันไม่เพียงพอ ถ้ายังจัด source alignment ไม่ได้ต้องรายงานว่า evidence-contract ไม่ผ่าน ห้ามปลอม ID ให้ตรง gold

## 8. Presentation ไม่ใช่ข้อเดียวกับ correctness

first_line_off_topic อาจเกิดจาก caption ชื่อรายการ/หัวข้อก่อนประโยคที่ gold คาด ต้องตรวจว่าคำตอบเกี่ยวกับเรื่องที่ถามจริงและไม่บังเงื่อนไข ไม่อ้างว่าตกหัวข้อบรรทัดแรกเท่ากับตอบผิดทุกครั้ง

พบ regex .* จาก FAQ ที่ย้ายข้อมูลถูกแสดงเป็นหัวข้อ ลูป L แก้ display caption โดยคง source เดิม ตัวข้อความกติกาที่ซ้ำใน heading/text และตารางราคาหลายกลุ่มยังอาจยาวเกินต้องการ ควรปรับ projection จาก needs ที่ถาม รักษาข้อยกเว้น ไม่ตัดเนื้อหาเพื่อให้สั้นอย่างเดียว

## 9. Model transport กับความถูกต้อง

ตัวอย่าง own laptop ใน final16 ON ได้ข้อความ model เลือกข้อมูลไม่ทัน ไม่มีคำตัดสินว่าทำได้/ไม่ได้ เป็นความล้มเหลวด้านการให้คำตอบและ latency แม้ไม่สร้างนโยบายเท็จ ไม่ควรนับเป็น correct answer เพียงเพราะ abstain

trace แยก attempted, transport_ok, schema_accepted, semantic selection, final plan แล้วคำตอบยังต้องตรวจ source/coverage อีกชั้น หมายเลขเหล่านี้ไม่ใช่ accuracy; trace ที่เปิดเผยอาจไม่ใช่ traffic counter ครบทุก request

## 10. ลำดับงานที่เหลือ

1. อย่า publish อัตราหมดอายุ/unknown effective dates และ contradictions เป็น current policy รอ facts ที่ระบุเฉพาะใน OWNER_CONFIRMATION_REQUIRED_TH.md
2. 390 control-note translations มี fidelity review และ source lineage แล้ว; ขยาย semantic review แบบมี error taxonomy ไปช่องแปลอื่นที่ยังไม่ได้อ่านเป็นรายช่อง ไม่ถือว่า literal guards รับรองทั้งหมด
3. ใช้ raw residual content/source failures เลือกเคสที่ผิดความหมายจริง เพิ่ม behavioral tests เฉพาะส่วนนั้น ไม่ใช้ route mismatch ทั้งหมดเป็น semantic errors
4. model timeout/selection coverage: เก็บ fault + latency evidence และประเมิน semantic fallback ตาม schema; ไม่เพิ่มคำตอบที่ไม่มี source เพื่อให้ availability metric สูง
5. publication, restart และ portable packages เป็น deployment surfaces แยกกัน ต้องตรวจ hash/version และ release status; code copied ไม่เท่ากับ data published หรือเว็บที่เปิดค้างโหลดโค้ดใหม่แล้ว

รายการนี้เป็น known residual risks และงานค้าง ไม่ใช่ผลรับรอง production ทุกหมวด ในรายงานหลักต้องเก็บทั้ง raw strict scores ที่ลดลงและผล targeted gates ที่ผ่านไว้คู่กัน
