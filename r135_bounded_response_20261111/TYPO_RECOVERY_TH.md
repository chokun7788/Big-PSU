# เชื่อมการฟื้นคำผิดกับ common Flow — 11 พฤศจิกายน 2026

## เปลี่ยนจริง

ใช้keyboard-neighbor, multi-error phraseและcontextual intent cue helpersที่มีในFlowเก่า ผ่าน common/typo_recovery.py แล้วเรียกก่อนnative/compat readersทั้งสองทางในCommonAnswerer.answer ไม่ได้เพียงเพิ่มaliasให้คำว่าเกส

- แป้นเกษมณี:คำนวณระยะของปุ่ม แล้วสร้างคำแนะนำเมื่อกรอบคำถามตรงกับintentที่รองรับ
- ตัวตก/เกิน/สลับ:ใช้bounded OSA/Damerau editและตัวสร้างกรอบคำถามเดิมร่วมกัน
- คำซ้ำ:ลบซ้ำเฉพาะintent tokenที่กำหนดในกรอบคำถาม ไม่ยุบตัวลากเสียงทุกข้อความ
- เรียงคำแนะนำด้วยต้นทุนerror channelที่กำหนดเอง ไม่ใช่confidenceที่ฝึกหรือcalibrateแล้ว
- ป้องกันชื่อจากsnapshot ตัวเลขURLคำปฏิเสธ/เงื่อนไข และเก็บraw text/edit spans
- คำสำคัญหายทั้งคำและเลือกได้หลายdomain เช่นมีอะไรบ้าง ให้ถามกลับ;ประวัติที่ผ่านnative delivered-state gateยังเข้าสู่ตัวresolveบริบทเดิมได้
- ตัวตรวจderived-inputจะคำนวณคำแนะนำซ้ำกับsource snapshotเพื่อเช็กการแปลง ไม่ใช่semantic proofอิสระ และไม่ได้ยืนยันคำตอบจากคำที่แก้ คำตอบยังต้องผ่านsource/receipt verifiersเดิม
- ไม่โหลดweightsใหม่ ไม่ติดตั้งแพ็กเกจ ไม่เปลี่ยนowner/live/frozen data

## ปัญหาที่เจอและแก้ระหว่างรอบ

1. เวอร์ชันแรกส่งคำว่า“จองยังงไ”ที่แก้แล้วเข้าเส้นทางใหม่ในcompoundราคา+จอง ทำให้ตัวตรวจปฏิเสธส่วนจองว่าunproven_cross_task_target แม้ราคายังตอบได้ เก็บ `bounded_response_1794400013587346800` ที่ล้มไว้ ไม่ผ่อนตัวตรวจหลักฐาน
2. ทดลองKEEPเมื่อraw nativeอ่านได้ แต่กว้างเกินไป:rawที่มีคำว่าเกสกับราคาเดิมรู้จักแค่ราคา จึงทำให้ความต้องการเกมหลุด เก็บ `typo_controls_1794400282174571800` ที่ล้มไว้
3. วิธีสุดท้ายเทียบโครงงานของrawกับcandidateทั้งcategory/operation/field/target/canonical operation ถ้าเหมือนกันและไม่ambiguousให้KEEP ถ้าcandidateทำให้พบงานที่rawตกหล่นจึงยังแก้ได้ เป็นbounded consistency check ไม่อ้างว่าพิสูจน์เจตนาทุกกรณี

4. พบว่ารักษาตัวอักษรคำว่าไม่ไว้ยังไม่พอ: คำถามไม่มีเกมอะไรบ้างเคยเข้ารายชื่อเกมที่มีอยู่ แพตช์ native facet อย่างเดียวก็ยังกัน compatibility ไม่ได้ (typo_controls_1794401254558854600 ล้ม) จึงถอนแนวทางนั้นและวาง explicit absence-catalog gate ก่อน readers ทั้งหมดใน CommonAnswerer ไม่สรุปรายชื่อเกมที่ไม่มีจากรายการเกมที่มี ส่วน typo ที่มีคำปฏิเสธให้ยืนยันก่อน ไม่อ้างแก้ negation ทุกประโยค

## ผลสุดท้าย

| หลักฐาน | ผล | ขอบเขต |
|---|---|---|
| typo_controls_1794401444422257500/RESULT.json |35checksผ่าน|แยก6กลไก,clean inputs,ชื่อ/ตัวเลข/คำปฏิเสธ,raw trace,forged execution,actual source readerและcompound |
| verified_sources_controls_1794401496524264400/RESULT.json |22checksผ่าน|source bindings,platformราคา,กฎ6sessions,actual isolated edit/withdraw |
| bounded_response_1794401482306713100/RESULT.json |6checksผ่าน|งบเวลาและtyped siblingsยังตอบได้|
| typo_http_1794401506338320500/RESULT.json |11HTTP requestsผ่าน|เกมคำปกติ/ปุ่มข้างเคียง/ตัวตก/ตัวเบิ้ล,คำหายถามกลับ,ราคา0,ราคา+จอง,Englishคู่clean/typo |

ตัวอย่างที่ผ่าน:มีเกสอะไรบ้าง→มีเกมอะไรบ้าง;มีเกอะไรบ้าง→มีเกมอะไรบ้าง;มีเกมมอะไรบ้าง→มีเกมอะไรบ้าง;Are drins allowwd→Are drinks allowed คำถามเกมที่แก้ให้answerและsource-hit identitiesตรงกับคำถามclean แต่catalogเดิมยังมีขอบเขตpartial จึงไม่ใช้ผลนี้อ้างว่ารายชื่อเกมทั้งหมดถูกต้อง

previewล่าสุด http://127.0.0.1:8142/ version R135-Typo-working โหลดโค้ดรอบสุดท้ายแล้ว เคยเปิดก่อนแพตช์KEEPเสร็จ จึงตรวจPID/commandlineและรีสตาร์ทเฉพาะpreview8142ของรอบนี้ก่อนHTTP checks รวมแพตช์คำปฏิเสธรอบสุดท้าย ไม่หยุดprotected model/แอปอื่น

## งานวิจัยและข้อจำกัด

ดู [งานวิจัยและวิธีนำมาใช้](typo_research_20261111/RESEARCH_TH.md) และreferences.json ตรวจต้นฉบับ5งาน ใช้แนวคิดerror channel/minimal edits/Thai misspelling semantics ตัวช่วยAPIของpaper-search-proหยุดเพราะconfigไม่ครบ จึงค้นprimary sourcesด้วยwebแทน ไม่อ้างPRISMAหรือcoverage

ชุดcontrolsนี้สร้างเพื่อตรวจกลไกและregression ไม่ใช่unseen benchmark ไม่ใช่accuracyของภาษาวิบัติทั่วไป ยังไม่รองรับทุกคำผิด คำหายทั้งคำไม่เติมชื่อคน/เกม/จำนวนเงินให้เอง ชื่อสะกดผิดที่ไม่ตรงsnapshotและประโยคผิดหลายจุดยังมีช่องว่าง

ไม่รัน200/2111ใหม่ในรอบนี้ คะแนน196/255เดิมไม่รวมการแก้คำผิดชุดนี้ ปัญหาtimeout/cooldownและงานR135เต็มยังไม่ปิด ไม่deployproductionก่อนgates/backupWAL
