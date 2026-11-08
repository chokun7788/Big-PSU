# R113 — รายละเอียด 140 แนวคิดและขอบเขตการพัฒนา

เอกสารนี้ขยายแนวคิดทุกหมวด พร้อมแยกสิ่งที่แนวคิดตั้งใจให้ทำกับความสามารถของ prototype ที่ทดสอบจริง ใช้อ่านคู่กับ 01_DESIGNS_AND_SELECTION_TH.md และ 02_BENCHMARK_REPORT_TH.md

## วิธีอ่านคะแนน

คะแนนออกแบบเดิมใช้ rubric correctness 30 / scope 25 / data-only updates 20 / feasibility 15 / latency 10 เป็น heuristic ล่วงหน้า ค่าประเมินผูกตาม family และลำดับไอเดีย จึงไม่ใช่การประเมินเชิงประจักษ์แยกราย 140 แบบ และไม่ใช้เป็นเปอร์เซ็นต์ความถูกต้อง การตัดสินคุณภาพตัวรันให้ใช้ผล 100 คำถามร่วมกันต่อหมวดเท่านั้น คะแนนไม่ใช่หลักฐานว่าแนวคิดที่ไม่ถูกเลือกด้อยกว่าแน่นอน

## โครงร่วมที่พัฒนาจริงก่อนทดสอบ

1. อ่าน common.sqlite แบบ read-only และคำยืนยันเจ้าของ → compiled read model มี fact IDs, entity/field/value, evidence refs และ fixture flags
2. แยก 14 source scopes แล้วส่งหมวดที่ทราบแล้วให้ตัวอ่าน; ยังไม่วัด global router
3. ทาง A: lexical ranking → top1 ต่อ need; ทาง B: subject/field contract → matching claims; ทาง C: ทาง B แล้ว local model เลือก evidence เมื่อ ambiguous
4. แยก coordinated needs, คำนวณจำนวนรอบด้วย code และ renderer ภาษาไทย/อังกฤษตามค่า locale
5. ตรวจด้วย oracle ที่แยกจาก answer engine: claims ครบ/ไม่เกิน, ค่าและหน่วย, source refs, answer state
6. ตรึง implementation/ข้อมูล/เกณฑ์ระหว่างชุดหลัก; เก็บ raw results และ model event ทุกครั้งที่บันทึกสำเร็จ ไม่มีการคัดเฉพาะคำตอบที่ดี

## C01 ข้อมูลศูนย์ สถานที่ และช่องทางติดต่อ

**Input ที่ควรแยก:** สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก
**เส้นทางข้อมูล:** center → facility/zone/contact
**เงื่อนไขคำตอบ:** แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม

### C01-F01 — ค้นฟิลด์ที่อยู่และช่องทางตรง

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C01-F02 — กราฟอาคาร–ชั้น–สิ่งอำนวยความสะดวก

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C01-F03 — FAQ ตรงคำถาม

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C01-F04 — จัดอันดับข้อความเฉพาะข้อมูลศูนย์

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C01-F05 — แยก map/address/contact ก่อนอ่าน

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C01-F06 — LLM เลือก record และ field

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C01-F07 — สรุปเอกสารข้อมูลศูนย์ทั้งชุด

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C01-F08 — ฟิลด์ก่อนและ semantic เมื่อกำกวม

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

### C01-F09 — ตอบแบบตารางข้อมูลศูนย์

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C01-F10 — ตรวจ claim กับจุดหมายก่อนส่ง

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน center → facility/zone/contact; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** ยังไม่ได้เดินกราฟอาคารจริงระหว่างรัน; อ่าน facts ที่ projection เตรียมไว้
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C02 บุคลากรและหน้าที่

**Input ที่ควรแยก:** ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ
**เส้นทางข้อมูล:** person → team/role/public display name
**เงื่อนไขคำตอบ:** ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว

### C02-F01 — อ่าน role พร้อมขอบเขตชื่อสาธารณะ

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C02-F02 — ค้นรายชื่อแบบ lexical

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C02-F03 — เดินทีมไปหารายชื่อ

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C02-F04 — แยกชื่อ–ตำแหน่งแล้วเลือกฟิลด์

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C02-F05 — FAQ บุคลากรเฉพาะคน

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C02-F06 — LLM จัดชื่อกับหน้าที่

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C02-F07 — แสดง directory ทั้งชุด

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C02-F08 — เปรียบเทียบคนสองคนผ่านกราฟ

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C02-F09 — อ่านฟิลด์ก่อนแล้ว semantic แก้ชื่อกำกวม

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

### C02-F10 — อ่านเฉพาะรายชื่อที่ public ครบทุกฟิลด์

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน person → team/role/public display name; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** ตัว typed จับชื่อ subject และ facet ตามข้อความ ยังไม่มี name disambiguation ข้ามหลาย alias เต็มรูปแบบ
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C03 อุปกรณ์ เครื่อง และความจุ

**Input ที่ควรแยก:** รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก
**เส้นทางข้อมูล:** equipment_model → resource → zone
**เงื่อนไขคำตอบ:** แยก physical units, simultaneous players และ room seats

### C03-F01 — ค้นคำอธิบายรุ่นอุปกรณ์

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C03-F02 — กราฟ model–resource–zone

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C03-F03 — สรุปสเปกทุกฟิลด์

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C03-F04 — ค้น FAQ อุปกรณ์

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C03-F05 — ตีความจำนวน/หน่วย/ที่ตั้งก่อนอ่าน

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C03-F06 — LLM เลือกชนิดอุปกรณ์

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C03-F07 — ค้นด้วยชื่อโซนก่อนชื่อรุ่น

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C03-F08 — เปรียบเทียบสเปกระหว่างรุ่น

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C03-F09 — นับ physical inventory แบบชุด

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C03-F10 — กราฟตาม predicate พร้อม semantic fallback

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน equipment_model → resource → zone; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยก physical units, simultaneous players และ room seats; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** relations ถูก compile บางส่วนเป็น facts; ยังไม่มี runtime graph query/aggregation ทุกรูปแบบ
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C04 เกมที่มี ข้อมูลเกม และรูปแบบเล่น

**Input ที่ควรแยก:** ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น
**เส้นทางข้อมูล:** game_service.offered → game/service
**เงื่อนไขคำตอบ:** catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม

### C04-F01 — enumerate offerings ตามโซน

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C04-F02 — ค้นเกมจากคำในชื่อ

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C04-F03 — FAQ เกมที่ติดตั้ง

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C04-F04 — สรุปเกมจาก root record

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C04-F05 — แยก catalog/overview/how-to ก่อนอ่าน

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C04-F06 — LLM เลือกกลุ่มเกม

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C04-F07 — ค้นตามจำนวนผู้เล่นจาก modes

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C04-F08 — รวม source ที่เกี่ยวกับเกมทุกชิ้น

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C04-F09 — กราฟ offering กับตัวกรองครบชุด

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C04-F10 — typed game reader และ semantic แก้เจตนา

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน game_service.offered → game/service; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** compile offering lists และ game details แล้ว แต่ตัวเลือกยังมี lexical top1/subject–facet เป็นหลัก
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C05 ปุ่มควบคุมและการใช้อินพุต

**Input ที่ควรแยก:** เกม/แพลตฟอร์ม/preset/action/context
**เส้นทางข้อมูล:** control_set → binding[action]
**เงื่อนไขคำตอบ:** คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน

### C05-F01 — exact action-to-button

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C05-F02 — ค้นข้อความปุ่มใกล้คำถาม

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C05-F03 — แสดงผังปุ่มทั้งชุด

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C05-F04 — ผูกเกม–platform–preset ก่อน action

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C05-F05 — FAQ วิธีควบคุม

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C05-F06 — LLM อ่านคำอธิบายแล้วเลือก binding

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C05-F07 — แยก action กับ gesture/context

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C05-F08 — binding ตรงก่อนแล้ว semantic rerank

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

### C05-F09 — ค้นปุ่มกลับไปหา action

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C05-F10 — เทียบหลาย preset แล้วถามตัวเลือก

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/แพลตฟอร์ม/preset/action/context จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน control_set → binding[action]; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** ใช้ subject เกมรวม platform และ binding facts; ยังไม่ได้ทดสอบ preset conflicts และอุปกรณ์ที่ผู้ใช้ตั้งเองครบ
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C06 ราคาใช้บริการรายคนและการคำนวณ

**Input ที่ควรแยก:** บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่
**เส้นทางข้อมูล:** rate(service,audience,validity,unit) → amount
**เงื่อนไขคำตอบ:** คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน

### C06-F01 — ตีความบริการ–กลุ่ม–รอบแบบเดิม

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C06-F02 — ค้นตารางราคาจากชื่อ

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C06-F03 — LLM คำนวณจากข้อความราคา

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลตีความและคำนวณ
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: อ่านข้อความราคา/หน่วย → ให้โมเดลสร้างรายการคำนวณ → ตรวจซ้ำด้วยเครื่องคิดเลขก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: โมเดลคำนวณเองตรวจสอบยาก ต้องส่ง arithmetic ให้ code จึงจะเหมาะใช้งานจริง

### C06-F04 — typed rate/unit/audience calculator

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C06-F05 — แสดงทุกกลุ่มเมื่อถามราคา

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C06-F06 — FAQ ราคาตรงบริการ

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C06-F07 — กราฟ game→service→rate

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C06-F08 — แจกแจงราคาตามงบ

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C06-F09 — แก้ slot จากประวัติก่อนคำนวณ

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C06-F10 — calculator แบบ typed พร้อม semantic plan

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่ จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน rate(service,audience,validity,unit) → amount; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** รองรับ integer sessions ต่อคน; ยังไม่มี mixed-audience cart/proration และชื่อ duration บางส่วนเป็น ID ภายใน
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C07 เช่าเหมาโซน ห้อง และกิจกรรมส่วนตัว

**Input ที่ควรแยก:** โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา
**เส้นทางข้อมูล:** package → price/duration/equipment/terms
**เงื่อนไขคำตอบ:** แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay

### C07-F01 — เลือกแพ็กเกจแล้วอ่านราคา

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C07-F02 — FAQ เหมาโซน

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C07-F03 — แสดงตารางทุก package

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C07-F04 — tuple zone–audience–period

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C07-F05 — กรองจาก equipment ที่ต้องการ

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C07-F06 — LLM สรุป terms ทั้งเล่ม

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C07-F07 — เปรียบเทียบครึ่งวันกับเต็มวัน

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C07-F08 — กราฟจำนวนที่นั่งและอุปกรณ์

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C07-F09 — package contract พร้อม semantic fallback

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

### C07-F10 — ถามทุก slot ก่อนอ่านราคา

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน package → price/duration/equipment/terms; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** typed ยังจับชื่อแพ็กเกจแบบ literal; terms/หลายเงื่อนไขยังไม่เป็น solver เต็มรูปแบบ
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C08 การจอง การมาถึง และการเปลี่ยนรายการ

**Input ที่ควรแยก:** action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง
**เส้นทางข้อมูล:** owner procedure + conditions → action steps
**เงื่อนไขคำตอบ:** อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง

### C08-F01 — FAQ จองที่ใกล้ที่สุด

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C08-F02 — action-first จอง/ยกเลิก/เช็กอิน

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C08-F03 — ต้นไม้สถานะการใช้งาน

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C08-F04 — ค้นขั้นตอนจากชื่อ procedure

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C08-F05 — LLM สรุป FAQ ทั้งหมวด

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C08-F06 — อ่าน policy/procedure เฉพาะเงื่อนไข

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C08-F07 — เลือกตามช่องทางอีเมล/เพจ

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C08-F08 — กราฟเอกสารและผู้เล่น

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C08-F09 — ตอบขั้นตอนเต็มทุกครั้ง

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C08-F10 — action contract และ semantic correction

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน owner procedure + conditions → action steps; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** มี policy text facts 9 ชุด แต่ยังไม่มี state machine ที่ bind เงื่อนไขจากสำนวนทั้งหมด
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C09 การชำระเงิน สลิป เอกสาร และเงินคืน

**Input ที่ควรแยก:** ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน
**เส้นทางข้อมูล:** payment policy → required evidence/contact/next step
**เงื่อนไขคำตอบ:** แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร

### C09-F01 — แยก action โอน/สลิป/เอกสาร

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C09-F02 — FAQ ชำระเงินอันดับแรก

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C09-F03 — อ่านข้อความชำระทุกข้อ

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C09-F04 — สถานการณ์ผู้โอน–ยอด–หลักฐาน

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C09-F05 — LLM สรุปเรื่องเงิน

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C09-F06 — กราฟวิธีชำระกับเอกสาร

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C09-F07 — จับ keyword คืนเงินแล้วค้น

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C09-F08 — เลือก policy ตามสถานะจ่ายแล้ว

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C09-F09 — typed payment policy และ semantic correction

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

### C09-F10 — ผสานทุกข้อที่มีจำนวนเงิน

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน payment policy → required evidence/contact/next step; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** policy facts 7 ชุด; ตัว typed ยังไม่ผูกสถานการณ์ภาษาธรรมชาติเข้า subject ของนโยบาย
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C10 สิทธิ์ใช้บริการ กฎศูนย์ และปัญหาระหว่างใช้

**Input ที่ควรแยก:** การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น
**เส้นทางข้อมูล:** permission policy → condition/exception/remedy
**เงื่อนไขคำตอบ:** allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว

### C10-F01 — FAQ permission ทั่วไป

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C10-F02 — action–subject permission matcher

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C10-F03 — ค้นกฎจากอุปกรณ์ที่พูดถึง

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C10-F04 — LLM จัดสถานการณ์ผู้ใช้

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C10-F05 — condition/exception policy graph

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C10-F06 — ต้นไม้สถานะใช้บริการ

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C10-F07 — อ่านข้อความกฎทั้งหมดก่อนตอบ

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C10-F08 — เลือกกฎจาก channel ติดต่อ

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C10-F09 — จับตามคำห้าม/ได้

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C10-F10 — policy contract พร้อม semantic ในขอบเขต

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน permission policy → condition/exception/remedy; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** ไม่มี condition graph traversal จริง; lexical ใช้ชื่อ/ข้อความ ส่วน typed ใช้ subject–facet
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C11 ตารางเปิด ช่วงจอง และวันปิดพิเศษ

**Input ที่ควรแยก:** วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure
**เส้นทางข้อมูล:** dated closure → regular schedule → requested interval
**เงื่อนไขคำตอบ:** ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด

### C11-F01 — อ่านตารางวัน/ช่วงเวลาตรง

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C11-F02 — ค้น FAQ เปิดปิด

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C11-F03 — LLM สรุปตารางสัปดาห์

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C11-F04 — แยก opening/bookable/maintenance/closure

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C11-F05 — แสดงทั้งสัปดาห์ทุกคำถาม

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C11-F06 — ต้นไม้วันหยุดก่อนวันธรรมดา

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C11-F07 — กราฟโซนและข้อยกเว้น

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C11-F08 — คำนวณเฉพาะ weekday

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C11-F09 — calendar contract พร้อม semantic dates

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

### C11-F10 — ค้นประกาศล่าสุดแทน schedule

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated closure → regular schedule → requested interval; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** ชุดนี้ทดสอบ fact reads มากกว่าปฏิทินเต็ม; ยังไม่มี calendar interval resolver รวมทุก exception
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C12 สถานะเครื่องหรือรายการจองจากระบบสด

**Input ที่ควรแยก:** resource/วันที่/ช่วงเวลา/freshness/provider state
**เส้นทางข้อมูล:** resource binding → controlled provider snapshot
**เงื่อนไขคำตอบ:** unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง

### C12-F01 — อ่าน provider ตาม resource/time

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C12-F02 — ค้นข้อความสถานะใน cache

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ตัดสินใจจากสถานการณ์
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว

### C12-F03 — LLM เลือกสถานะจากข้อความ

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C12-F04 — typed binding + freshness + status mapping

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C12-F05 — ตรวจ resource ผ่าน schedule ก่อน

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C12-F06 — เรียก provider ทุกเครื่องแล้วกรอง

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C12-F07 — อ่าน snapshot เก่าเมื่อ provider ไม่พร้อม

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C12-F08 — ถาม input ทุกช่องก่อนเรียก

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C12-F09 — กราฟ resource/zone รวมช่วงว่าง

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C12-F10 — live contract หลาย needs และ bounded interpretation

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก resource/วันที่/ช่วงเวลา/freshness/provider state จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน resource binding → controlled provider snapshot; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** ใช้ fixture snapshots เท่านั้น ไม่มีการเรียก provider ลูกค้าจริง และยังไม่มี production binding/freshness pipeline ครบ
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C13 รายการแข่งขันและข้อกติกา

**Input ที่ควรแยก:** เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies
**เส้นทางข้อมูล:** event-specific rule clauses + owner clarifications
**เงื่อนไขคำตอบ:** อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง

### C13-F01 — ค้นทั้ง rulebook ตามชื่อเกม

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C13-F02 — retrieval ข้อกติกาตามคำถาม

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C13-F03 — สรุป overview ทุกคำถาม

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C13-F04 — FAQ กติกาตามเกม

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C13-F05 — event–facet–dependency clause graph

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C13-F06 — LLM เลือกข้อแล้วสรุป

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: โมเดลเลือกข้อมูลในขอบเขต
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว

### C13-F07 — exact heading/section lookup

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C13-F08 — เลือกบทลงโทษจาก keyword

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C13-F09 — อ่านข้อทั้งหมดแล้วตัดข้อความ

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C13-F10 — clause contract และ semantic clause selection

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน event-specific rule clauses + owner clarifications; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** clause facts ยังไม่เดิน dependency graph ระหว่างข้อ; ภาษาอังกฤษบางข้อยังเป็นต้นฉบับไทย
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

## C14 ข่าว กิจกรรม ประกาศ และโปรโมชัน

**Input ที่ควรแยก:** งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา
**เส้นทางข้อมูล:** dated event → registration/status/source
**เงื่อนไขคำตอบ:** แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง

### C14-F01 — กรองกิจกรรมตามวันที่ที่ถาม

- คะแนน heuristic เดิม: 80.0/100; คัดมาทดลองด้วย family `lexical`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C14-F02 — ค้นข่าวล่าสุดจากชื่อ

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

### C14-F03 — แสดงทุกข่าวใน snapshot

- คะแนน heuristic เดิม: 61.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านเป็นชุดและกรอง
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง

### C14-F04 — อ่าน news clause ตาม scope และวัน

- คะแนน heuristic เดิม: 92.0/100; คัดมาทดลองด้วย family `typed`
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C14-F05 — LLM สรุปข่าวทั้งหมด

- คะแนน heuristic เดิม: 65.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: สรุปเอกสารในหมวด
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป

### C14-F06 — กราฟงาน–ช่องทางสมัคร

- คะแนน heuristic เดิม: 53.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นตามความสัมพันธ์และเงื่อนไข
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้

### C14-F07 — ค้น headline ก่อนวันที่

- คะแนน heuristic เดิม: 63.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C14-F08 — เลือกเฉพาะข่าวที่มี registration URL

- คะแนน heuristic เดิม: 57.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: อ่านข้อมูลแบบ typed
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source

### C14-F09 — event contract พร้อม semantic fallback

- คะแนน heuristic เดิม: 93.0/100; คัดมาทดลองด้วย family `hybrid`
- แนวทาง: typed ก่อนแล้วโมเดลช่วยตีความ
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ

### C14-F10 — FAQ กิจกรรมทั่วไป

- คะแนน heuristic เดิม: 55.0/100; แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก
- แนวทาง: ค้นข้อความ/FAQ ในหมวด
- Step 1: แยก งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need
- Step 2: normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข
- Step 3: ใช้ข้อมูลผ่าน dated event → registration/status/source; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด
- Step 4: แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง
- จุดบกพร่องที่ต้องคุม: คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ

**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** ไม่มี news records จริงใน source projection จึงใช้ synthetic fixtures; ยังวัด real announcement lifecycle ไม่ได้
ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว

