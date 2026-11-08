import json,collections
from pathlib import Path
R=Path(Path(__file__).with_name('r34_report_path.txt').read_text().strip())
old=[json.loads(l) for l in (R/'baseline_results.jsonl').read_text(encoding='utf-8').splitlines()]
fixture={x['id']:x for x in json.loads((R/'R34_SOURCE_REVIEWED_FIXTURE.json').read_text(encoding='utf-8'))['cases']}
counts=collections.defaultdict(collections.Counter);review=[]
for row in old:
 c=fixture[row['case']['id']];z=row['response'];a=z.get('answer','');errors=[]
 for group in c['required']:
  if not any(w.casefold() in a.casefold() for w in group):errors.append('missing:'+str(group))
 if not any(w in str(z.get('hits',[])) for w in c['source']):errors.append('wrong_source')
 errors+=['forbidden:'+w for w in c['forbidden'] if w.casefold() in a.casefold()]
 counts[c['group']]['total']+=1;counts[c['group']]['passed']+=not errors
 review.append(dict(id=c['id'],original_grade_passed=row['passed'],source_review_passed=not errors,remaining_errors=errors))
with (R/'BASELINE_SOURCE_REVIEW_SIDECAR.json').open('x',encoding='utf-8') as f:json.dump(dict(groups=counts,total=len(old),passed=sum(x['passed'] for x in counts.values()),rows=review,scope='Regrade preserved baseline output against original source-derived correction, not a new execution and not an edit of Gold.'),f,ensure_ascii=False,indent=2)
text='''# วิเคราะห์สาเหตุและคะแนน — r34

## ข้อมูลมีครบ แต่หลายขั้นตอนยังตกลงกันไม่ได้

ระบบไม่ได้เลือกคำตอบจากคะแนนเดียว มีตัวแก้คำผิด ตัวแยกคำถาม router ตัววิเคราะห์ความต้องการ ตัวเลือกเครื่องมือ ตัวดึงข้อมูล และตัวตรวจสัญญาคำตอบ เมื่อแต่ละขั้นมองคำถามคนละความหมาย จึงมีข้อมูลถูกต้องแต่คำตอบถูกทิ้งได้ ค่า confidence ใน log เป็นคะแนนของขั้นนั้น ไม่ใช่โอกาสที่ข้อเท็จจริงถูกต้อง

## P0 เทียบราคาแต่ validator มองเป็นอุปกรณ์

ตัวอย่าง `จอสอบถาม... PC กับ VR อันไหนพงกว่า`:

1. preflight แก้ `อันไหนพงกว่า` เป็น `อันไหนแพงกว่า` ได้ ระยะแก้ 1 ตัว
2. router เห็นคำ `จอ` และอุปกรณ์ จัดเป็น equipment คะแนน 0.94; universal intent equipment/compare 0.86
3. เครื่องมือปิดเฉพาะงานสร้างคำตอบ PC+VR ตามตารางครบ คะแนน 0.98
4. question frame กลับเป็น equipment_lookup คะแนน 0.92 คาดคำตอบ equipment/list และแหล่ง equipment
5. ตรวจคำตอบแล้วปฏิเสธ เพราะคำตอบเป็น price/calculation และแหล่ง service_fee/official_image/local_fact_update
6. ต่อมามีการเลือก fast.price_calculator คะแนน 0.606 เทียบ structured.service_fee 0.503 แต่ข้อตกลงชนิดคำตอบยังไม่ตรง จึงลงท้ายว่าไม่พบข้อมูล

**คำตอบที่ควรได้:** ราคาแพ็กเกจของ PC และ VR ทุกระยะตามตารางที่บันทึกไว้ พร้อมแยกกลุ่มผู้ใช้ ระยะเวลา และจำนวนคน ไม่เลือกผู้ชนะจากกลุ่มหรือระยะเวลาที่ผู้ใช้ยังไม่ได้ให้

**แก้:** ใช้สัญญาณเทียบราคาเดียวกันระหว่างคำตอบกับ validator ต้องมีบริการที่ระบุจริงอย่างน้อย 2 บริการ รักษาลำดับกฎการแข่งขันก่อน และไม่ปิด validator

## P1 ชำระเงินถูกตีความเป็น how-to ทั่วไปหรือวิธีจอง

ตัวอย่าง `จ่ายเงินยังไงตอนของ`:

- กฎธนาคารมีอยู่ แต่ตัวตรวจวิธีชำระเดิมมี `จ่ายยังไง` ไม่มีวลีที่มีคำ `เงิน` แทรก
- `ของ` เป็นคำจริง จึงไม่ควรเปลี่ยนทั้งระบบเป็น `จอง` เพื่อเพิ่มคะแนน
- baseline universal intent general/how_to 0.74; เมื่อไม่เข้าเครื่องมือชำระเงิน จึงหาเนื้อหาทั่วไปไม่เจอ ผลท้าย no_answer 0.42
- บางคำถามที่มี `จอง` ถูกตอบเป็นขั้นตอนจอง แม้ถามวิธีจ่าย จึงมีคำว่าโอน/สลิปแต่ไม่ครบธนาคารและบัญชี

**คำตอบที่ควรได้:** ข้อความ `rule_payment_bank` จาก rule ที่โหลดจริง ระบุธนาคาร เลขบัญชี และแนบสลิป ไม่ใช้กฎห้ามโอนสิทธิ์การจองตอบเรื่องโอนเงิน

**แก้:** รองรับกรอบวิธีชำระทั้งไทย/อังกฤษโดยตรง และกรอบคำผิด 1 ตัวตาม syntax ไม่ต้องมีคำว่าจองจึงตอบวิธีจ่ายได้ ตรวจ rule ที่ถูกโหลด; ถ้าไม่มี rule ห้ามสร้างบัญชีเอง

## P1 คำพูดและคำปฏิเสธเสียหายพร้อมกัน

ตัวอย่าง `คำพูไดม่เหมาะสม`:

- ตาม OSA เป็นการสลับอักษรเพียง 1 ครั้งเมื่อเทียบกับ `คำพูดไม่เหมาะสม` ไม่ใช่หลายคำที่ต้องเดาแยกกัน
- ตัวเดิมอาศัยคำ `คำพูด` ที่สมบูรณ์เป็นจุดเริ่ม จึงไม่เข้าเส้นทางนี้
- ข้อความเต็มมีคำ `อธิบาย` จึงไป general concept/detail คะแนน 0.94 ต่อให้ค้นพบข้อกฎ ตัวตรวจคาด fact/summary ไม่ยอมรับ competition_rule ที่หยิบมาใกล้เคียง
- English `insults`, `mocking ... people` และ typo `offenssive` เดิมไม่เข้า topic แบบเดียวกัน

**คำตอบที่ควรได้:** กฎทั่วไปเรื่องงดเสียงดังและห้ามดูหมิ่น/เสียดสีจาก `rule_noise_language` ไม่สร้างบทลงโทษเพิ่ม

**แก้:** ใช้ชิ้นคำศัพท์งาน `คำพูดไม่` เฉพาะระยะ 1 ตัวและมี `เหมาะสม` เป็นหลักยึด คำยืนยัน `คำพูดเหมาะสม` ต่างจากคำปฏิเสธ 3 ตัว จึงไม่ถูกเติม `ไม่` ให้; คงชื่อคนและคำถามตัวตน ไม่ให้ topic ในชื่อคนแย่งเส้นทาง

## P1 กติกาและหัวข้อผิดพร้อมกันทำให้ bootstrap ไม่ได้

ตัวอย่าง `อ้างอิงติกา อารีน่าออฟเวเลอร์ ... จำนวยผู้เล่นต่อทีม`:

- ชื่อไทย AoV อยู่ในทะเบียนกติกาและตรงจริง แต่ฐานเกมที่เปิดให้เล่นไม่ใช่ทะเบียนกติกา จึงไม่ควรใช้ความสำเร็จของตัวหาเกมแทนกัน
- กติกาขาด ก; จำนวนผิด ย; ตัวแก้ facet ต้องเห็นกติกาก่อน ส่วนตัวแก้กติกาเดิมต้องขึ้นด้วย กต จึงไม่มีขั้นไหนเริ่มได้
- universal intent general/unknown 0.45, router general 0.55; candidate retrieval.hybrid_guarded 0.433 เทียบ clarification 0.322 แต่คะแนนตัวที่ดีที่สุดยังต่ำเกณฑ์ (`abstain_low_score`)
- ข้อความตอบว่า candidates too close เป็นคำอธิบายกว้าง เหตุที่ log ระบุจริงในเคสนี้คือคะแนนต่ำ ไม่ใช่แค่ส่วนต่างคะแนน

**คำตอบที่ควรได้:** ข้อความ RoV Blueket 2025 ของทะเบียนนั้น เรื่องรูปแบบ 5v5; ไม่อ้างว่า roster รวมสำรองมี 5 คน และไม่ยืม VALORANT/CS2 คนละเกมหรือปี

**แก้:** ชื่อเกมตรงจริง+คำอ้างอิงเป็นหลักยึด แก้ operation ระยะ 1 ตัวก่อน แล้วรอบถัดไปแก้ facet จากทะเบียน ไม่เปลี่ยนชื่อ เลขปี จำนวน หรือคำปฏิเสธ

## สิ่งที่พบเพิ่มจากการวนทดสอบ

1. คำ `และ` ในการเทียบราคาถูกแยกเป็น 2 งานจนขาดราคา VR → รักษา operands ในคำถามเดียว แต่คำถามที่มีงานจอง/เวลา/ปุ่มแยกต่อได้
2. คำตอบ clean บางแบบยังตอบไม่ได้ เช่น mocking → topic ภาษาอังกฤษต้องรองรับรูปคำ ไม่ใช่เพิ่มเฉพาะคำผิด
3. `อย่า` เป็น prefix ของ `อย่างไร` → ขอบเขตคำปฏิเสธผิดทำให้ไม่กล้าแก้ interrogative
4. แม้ source-content ผ่าน 125/125 แต่ตัวแก้กิน ค ใน ครับ → เพิ่มขอบเขตคำลงท้ายและ test ข้อความที่แก้ต้องตรง
5. เกณฑ์ทดสอบใหม่ผิดเอง: VR 60 นาที General Student แหล่งระบุ 375 ไม่ใช่ 380; เก็บ baseline เดิมและ sidecar แยก ไม่แก้ราคาในระบบ/Gold

## ต้องแยกชนิดคำตอบและหลักฐาน

- `validation.ok=True` ของคำตอบสุดท้ายหมายถึงคำตอบสุดท้ายผ่านเงื่อนไข เช่นตอบว่าหาข้อมูลไม่เจอ ไม่ได้แปลว่าตอบคำถามผู้ใช้สำเร็จ
- HTTP 200 แปลว่ารับส่งสำเร็จ ไม่ยืนยันว่าเนื้อหา ราคา ภาษา เกม และแหล่งถูกต้อง
- source id ตรงอย่างเดียวไม่พอ ต้องตรวจ clauses/ตัวเลข/ข้อยกเว้นร่วมด้วย
- การแก้คำผิดตรงและรักษาคำปฏิเสธเป็นคนละ gate จาก content; unit พบข้อผิดพลาดที่ content test ไม่เห็น
- เกณฑ์ route/status เก่าที่ไม่ตรวจเนื้อหา ไม่ใช่คะแนนความถูกต้องจริงทั้งหมด
- fixture และเกณฑ์ที่ผู้ช่วยสร้าง/แปลไม่ใช่การรับรองจากเจ้าของ ข้อมูลจองจริงยังพักตามคำสั่งผู้ใช้
'''
with (R/'CAUSE_ANALYSIS_TH.md').open('x',encoding='utf-8') as f:f.write(text)
originals={c['case']['id']:c for c in old if c['case']['id'] in ['price-01','payment-01','speech-01','competition-01']}
with (R/'ORIGINAL_FOUR_BASELINE_TRACE_EXTRACTS.json').open('x',encoding='utf-8') as f:json.dump(originals,f,ensure_ascii=False,indent=2)
print(dict(source_reviewed_baseline_passed=sum(x['passed'] for x in counts.values()),groups=counts))
