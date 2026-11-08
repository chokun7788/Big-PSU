# ลำดับแก้จากผลวินิจฉัยข้อ 2 และเกณฑ์ตรวจรับ

เอกสารนี้เป็นข้อเสนอแก้ที่อ้างอิงสาเหตุที่ตรวจพบ ยังไม่มีการนำรายการเหล่านี้ไปแก้ runtime ในรอบทดสอบ 10% นี้ การตัดสิน semantic รายข้ออยู่ใน CONSOLIDATED_SOURCE_REVIEW.json และไฟล์หลักฐานต้นทาง ไม่ใช้คะแนน keyword เป็นคำตัดสินแทน source

## 1. แก้การผูกสิ่งที่ถามและรักษาขอบเขต ก่อนเปลี่ยนโมเดล

- **D01 — GPU/จอง/จอ:** แยกชนิด entity และสิ่งที่ต้องการอ่าน อุปกรณ์ที่ match บางส่วนแต่ผิดชนิดต้องไม่ทำให้ pool ของ PC ถูกทิ้ง ตรวจ alias ไทยที่เกิดเป็นส่วนหนึ่งของคำอื่น และการเลือก alias ยาวที่กลบ record ถูกชนิด ไม่แก้เพียง hardcode ประโยคตัวอย่าง
- **D02 — ชดเชย/public:** รักษา actor/action/target แล้วจึงเลือก reader การพบ mouse/chair ต้องไม่ลบ need เรื่องความรับผิดชอบ และคำว่าบุคคลทั่วไปต้องไม่ถูกใช้เป็นชื่อบุคคล
- **D03/D07 — กติกาแข่งขันและหลายประเด็น:** ผูก event/game/edition ไปยังทุก need ที่อยู่ภายใต้บริบทเดียวกัน ให้ local override ที่ผู้ใช้ระบุมีผล แยก watching จาก broadcasting และ macro จากการติดตั้งโปรแกรม ก่อนอนุญาตใช้ policy ศูนย์ทั่วไป
- **D06/D09 — คำอ้างกลับและบริการ:** หลัง resolve it ต้องปรับ ambiguity ที่แก้ได้แล้ว; ต้องเก็บ offsite/onsite และ item ที่เช่าถึง reader ไม่แทน notebook ด้วยราคาเหมาโซน

**ตรวจรับ:** ใช้คำถามเดิมทุก key ที่ตรวจ source ไว้ในกลุ่มนั้น แผนต้องรักษา needs/constraints และชี้ reader กับ record ถูกชนิด คำตอบต้องตอบสิ่งที่ถาม พร้อมบอกส่วนที่ยังไม่ยืนยัน การมี typed receipt อย่างเดียวไม่ผ่าน ต้องตรวจว่า receipt พิสูจน์ predicate ของคำถามจริง

## 2. แก้การอ่านและการตรวจว่าตอบครบ

- **D04 — substantive clause:** ยอมรับประโยคกติกาที่มีสาระครบแม้ text เท่ากับ heading; ห้ามเปลี่ยนเป็นรับ heading ทุกชนิด ตรวจ pause/settings/macro/protest ทั้ง 13 keys ที่มีหลักฐาน โดยรักษาเงื่อนไข จำนวน และเวลา
- **D05 — Tekken format:** เลือก section ที่มีสาระรูปแบบ FT2/R3/60S แทน section ชื่อเอกสาร รักษา parent/child และข้อที่ต้องอ่านร่วมกัน ตรวจ 29 keys ที่อ่าน source ไว้
- **D07 — need ledger:** เทียบคำตอบกลับคำถามต้นฉบับ ไม่ตรวจเฉพาะ tasks ที่ planner สร้างมาแล้ว ต้องเห็น need ที่ถูกทิ้งก่อนถึง reader เช่น macro+install และ equipment+responsibility
- **D08/D15 — จำนวนและการแสดงคำตอบ:** แยกเลขในชื่อเกมออกจากจำนวนที่ผู้ใช้ขอ ถ้า source ไม่ระบุ subset ให้บอกข้อจำกัด เริ่มด้วยสาระคำตอบและแยก label เงื่อนไขราคา/ช่วงเวลา ไม่เริ่มด้วยชื่อเอกสารหรือบันทึกแก้ข้อมูลโดยไม่จำเป็น

**ตรวจรับ:** ให้ผู้ตรวจอ่านคำถาม คำตอบ และ source revision/locator คู่กัน แยก “สาระตรงแต่ source ผิด scope” ออกจาก “สาระผิด/ตก” และ “ยังตัดสินไม่ได้” ไม่บังคับ wording ให้ตรง golden answer ถ้าสาระและเงื่อนไขครบ

## 3. จัดสัญญาระหว่าง prompt/weights/backend/parser และงบการเรียกโมเดล

- **D12 — protocol:** ส่ง version และโครงสร้างที่ระบุชัดในข้อความที่ backend ใช้จริง ตรวจว่า format/schema ถูกบังคับโดย serving backend หรือเป็นเพียง metadata ให้ adapter แต่ละรุ่นมี parser ที่ประกาศชัด ตรวจ input echo/quote binding ไม่ลด guard เพื่อรับ JSON ที่ผิดความหมาย
- **D11 — admission:** บันทึก reserved/attempted/spent กับ busy/cooldown/budget/transport แยกกัน กำหนดเวลารอคิวให้สอดคล้อง deadline และ generation limit ก่อนตัดสินใจว่าจะคืน reservation เมื่อไม่ได้ยิง HTTP หรือไม่
- **D15 — เวลา:** ลดการเรียก context ในคำถามที่ local fact/field และ scope ชัดได้อย่างมีหลักฐาน โดยไม่บังคับเรียกโมเดลทุกคำถาม ตรวจ tail latency ควบคู่ omission และ wrong-scope ไม่วัดเพียง HTTP 200

**ตรวจรับ:** ทดสอบ wire contract โดยไม่เรียก inference ใหม่ก่อน จากนั้นใช้การทดสอบ candidate ถัดไปที่ freeze ไว้ ตรวจ returned model/profile/adapter/input/schema/stage/precision จริง ไม่ใช้ alias ชื่อโมเดลยืนยัน weights และไม่ใช้ schema ผ่านเป็น semantic ผ่าน

## 4. ปิดช่องว่างข้อมูลและความน่าเชื่อถือเป็นราย record

- **D10/D14:** ทำรายการ known / unknown / conflicted / not-current / reader-gap พร้อม authority และ effective interval แยกต่างหาก GPU และหลายกติกามีข้อมูลอยู่แล้ว จึงไม่ต้องขอเจ้าของกรอกซ้ำ
- ข้อมูลที่ยังไม่ยืนยัน เช่น game mode/version/ข่าวปัจจุบัน ให้ถามหรือรับ source เฉพาะ field ที่ขาด ไม่เติมค่าจากความคุ้นเคยของโมเดล
- การไม่พบ PC10 relation ไม่พิสูจน์ว่าเครื่องจริงไม่มีเกม; ต้องตอบว่า scope นั้นยังไม่ยืนยัน ข้อมูลสเปกในโครงการก็ไม่ใช่การตรวจอุปกรณ์จริงทุกเครื่อง

**ตรวจรับ:** คำตอบต้องแยกข้อเท็จจริงที่มีจากสิ่งที่ยังไม่ทราบ และการปฏิเสธต้องตรง need ที่ถาม การเตือน conflict ต้องชี้คู่ record/เงื่อนไขที่ขัดกันจริง ไม่ปิดคำตอบที่ source ยืนยันได้เพราะ label รวม

## 5. วัด candidate ที่แก้แล้วและรักษา scope เดิม

เมื่ออนุมัติทำการแก้ ให้สร้าง candidate ถัดไปจาก frozen R130 เก็บผล R130/R131 เดิมไว้ ไม่แก้ผลย้อนหลัง เริ่มตรวจ regression กลุ่มที่รู้ต้นเหตุและ critical domains ด้วย source review แล้วจึงใช้ชุดเดิมที่ freeze ไว้สำหรับการวัด เปรียบ strict กับ positive-literal แยกจาก semantic และคง unknown/unassessed ใน denominator เดิม

ชุด 10% รอบนี้มี 2,111 unique request keys/5,584 grade identities ครบ membership C01–C14 แต่ C07 เดิมมีเพียง6คำถามและเลือก1 จึงยังไม่ครอบคลุม rental onsite ทุก operation ส่วน C14 ไม่มี source ข่าวจริง การผ่าน sample จึงไม่ปิดคุณภาพ76requirements และไม่ใช้ปรับเป็นเปอร์เซ็นต์ความเสร็จของ Flow

การเปลี่ยนเป็นโมเดลใหญ่ขึ้นหรือฝึกเพิ่มยังไม่มีหลักฐานว่าแก้ D01–D09 ได้ เพราะส่วนหนึ่งผิดก่อนเรียกโมเดลหรือหลังเลือก reader ให้แก้จุดที่พิสูจน์แล้วและตรวจผลก่อนตัดสินใจเรื่อง weights โดย new adapter ที่ไม่ผ่าน critical review ยังไม่ควรถูก promote
