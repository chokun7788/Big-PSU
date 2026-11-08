import json
from pathlib import Path

BASE = Path(__file__).parent
OUT = Path((BASE / 'competition_format_audit_path.txt').read_text(encoding='utf-8').strip())
audit = json.loads((OUT / 'data_format_audit.json').read_text(encoding='utf-8'))
schema = json.loads((OUT / 'queue_schema_validation.json').read_text(encoding='utf-8'))
answers = json.loads((OUT / 'current_http_answers.json').read_text(encoding='utf-8'))
assert len(answers) == 12 and all('response' in row for row in answers)
assert all(row['matches_current_source_import'] and row['curated_text_matches_chunks'] for row in audit['source_checks'])
assert schema['ok'] and schema['records'] == 104

ui = {'question': 'กติกา Tekken 8 มีอะไรบ้าง', 'version': '2026.10.01-competition-r24', 'strong_or_b_elements': 0, 'heading_elements': 0, 'list_item_elements': 0, 'literal_markdown_headings_visible': True, 'evidence': 'Observed DOM and screenshot of an agent-created temporary tab; web_chat/app.js assigns bubble.textContent = item.text.'}
with (OUT / 'ui_format_check.json').open('x', encoding='utf-8') as handle:
    json.dump(ui, handle, ensure_ascii=False, indent=2)

lines = ['# ตรวจข้อมูลและ Format กติกาการแข่งขันอีกครั้ง', '', 'วันที่ 1 ตุลาคม 2026 | เว็บที่ตรวจ: http://127.0.0.1:8090/ | เวอร์ชัน r24', '',
'''## สรุป

มีการแบ่ง format ไว้แล้วจริง ทั้งโครงข้อมูลกลาง รายละเอียดกฎย่อย และรูปแบบคำตอบ แต่บางส่วนยังเป็น template/คิวรอตรวจ และตัวตอบที่ใช้งานจริงยังไม่ได้ทำตาม format อย่างสม่ำเสมอ

รอบนี้ตรวจต้นฉบับทั้ง 4 ไฟล์ด้วยการนำเข้าซ้ำในหน่วยความจำ เทียบกับ chunks และ curated เดิม ตรวจ schema ของคิว 104 records และทดลองคำถามจริง 12 ข้อไทย/อังกฤษ รวมทั้งดู DOM และภาพหน้าจอคำตอบ Tekken บนเว็บ

ไม่ได้แก้ไฟล์ต้นฉบับ ข้อมูลอนุมัติ canonical queue หรือโค้ดในรอบตรวจนี้ ผลบันทึกเป็นไฟล์ใหม่ในโฟลเดอร์งาน ตรวจ HTTP และ UI ทำให้เกิด test exchange/log ใหม่ตามการทำงานปกติของเว็บ ไม่ทับ log เดิม

## 1. Format ที่มีอยู่จริง

### A. โครงหัวข้อกลางของข้อมูล

ไฟล์ `data/competition_rules/canonical/competition_rule_submission_template.json` แบ่ง 10 ส่วน:

| ส่วน | ใช้เก็บอะไร | หน้าตาที่ควรใช้ตอนตอบ |
|---|---|---|
| ข้อมูลเอกสารและขอบเขต | เกม รายการ ปี วันที่เริ่มใช้ source/release | ชื่อเกมและชื่อรายการ; ไม่เอาชื่อเอกสารมาตอบแทนเนื้อหากฎ |
| คุณสมบัติและลงทะเบียน | ผู้สมัครได้/ไม่ได้ รายชื่อทีม ตัวจริง/สำรอง เงื่อนไขสมัคร | ใครสมัครได้ → เงื่อนไข/หลักฐาน; แยกผู้ลงเล่นจาก roster รวม |
| รูปแบบการแข่งขัน | Single Elimination, BO3, FT2, เงื่อนไขชนะ | รูปแบบและเงื่อนไขชนะก่อน แล้วค่อยขยายรอบต่าง ๆ |
| การตั้งค่าแมตช์ | เวอร์ชัน โหมด เวลา รอบ แผนที่/การเลือกฝั่ง | รายการ `ค่า: จำนวน/หน่วย` หรือตาราง; อย่าปนวิธีเล่นทั่วไป |
| ก่อนแข่ง/หน้างาน | เวลาเข้าพื้นที่ รายงานตัว อุปกรณ์ การเตรียม | ขั้นตอนเรียงลำดับ พร้อมเวลาและผู้รับผิดชอบที่ source ระบุ |
| ระหว่างการแข่งขัน | แจ้งกรรมการ pause disconnect rematch | เหตุการณ์ → ทำอะไรได้/ไม่ได้ → ข้อยกเว้น/โควตา |
| ความเป็นธรรม/พฤติกรรม | ข้อห้าม cheat bug การสื่อสาร มารยาท | ข้อห้ามชัดเจน → เงื่อนไข/ข้อยกเว้น → โทษถ้ามีหลักฐาน |
| บทลงโทษ | การละเมิดและโทษ | หนึ่งแถวต่อ `การละเมิด ↔ บทลงโทษ`; รักษาความสัมพันธ์ |
| ประท้วง/ข้อพิพาท | แจ้งใคร เมื่อใด ขั้นตอนและผู้ตัดสิน | ขั้นตอนและเงื่อนไขตาม source; ห้ามแต่ง deadline ที่ไม่มี |
| อ้างอิง/ประวัติแก้ไข | ต้นทาง ส่วน/หน้าของเอกสาร version/วันที่ | ท้ายคำตอบ ระบุรายการและ evidence section; แยกข้อมูลไฟล์จากกฎปัจจุบัน |

หัวข้อกลางเป็นโครงร่วม ไม่ได้แปลว่า source ทุกเกมมีข้อมูลครบทั้ง 10 ส่วน ช่องว่างห้ามเติมด้วยกฎของอีกเกม

มีโมดูลเฉพาะเกมเพิ่มเติม เช่น CS2 map veto/overtime, RoV hero/skin/break time, Tekken character/stage และ VALORANT agent selection/pause taxonomy จึงไม่ควรบังคับให้กฎเฉพาะเกมสูญเสียรายละเอียดเพื่อเข้าหมวดกลาง

### B. Format ของกฎย่อย V2/V2.1

อ้างอิง `docs/86_competition_rag_claim_format_v2_20260922.md`:

- `source`: เอกสาร เกม หัวข้อ ข้อความต้นฉบับและ hash
- `claim`: ประเด็นที่ตอบได้ คำตอบไทย/อังกฤษ และค่าที่มีโครงสร้าง
- `retrieval`: เกม หมวด/facet และคำถามที่เกี่ยวข้อง
- `evidence`: อ้างถึงข้อที่รองรับคำตอบ
- `quality`: ตรวจว่าเป็นกฎย่อยที่ตอบได้ ไม่ใช่แค่ heading
- `approval/lifecycle`: ใครยืนยัน ใช้กับรายการใดและช่วงใด มีข้อขัดแย้งหรือไม่

หลักคือ **หนึ่งประเด็นกติกาต่อหนึ่ง claim พร้อมเงื่อนไขของประเด็นนั้น** แยก heading จากข้อกำหนดจริง ตัวเลขและเงื่อนไขเช่น `2 ครั้ง / ครั้งละ 10 นาที` ต้องอยู่ด้วยกัน ไม่ย่อจนกลายเป็น `รวม 10 นาที`

Schema review กับ schema approved runtime เป็นคนละสัญญา `competition_rule_claim_v2.schema.json` รุ่นแรกเป็นเอกสารอ้างอิงเดิม ต้องใช้ `competition_rule_claim_v2_review.schema.json` ตรวจ queue และ `competition_rule_claim_v2_1_runtime.schema.json` สำหรับ runtime ที่อนุมัติแล้ว

### C. Format คำตอบที่เคยกำหนดไว้

`docs/24_competition_ground_truth_v2_answer_style_audit.md` และ `docs/14_competition_rules_ingestion.md` กำหนด:

```text
คำตอบ: <ตอบจำนวน / ได้หรือไม่ได้ / เวลา / บทลงโทษที่ถามทันที>

รายละเอียดที่เกี่ยวข้อง:
• <เงื่อนไขหรือข้อยกเว้นของคำตอบ>

อ้างอิงจากกติกา: <เกม / รายการ>
แหล่งข้อมูล: <เอกสารและส่วนที่รองรับ>
```

อังกฤษควรใช้โครงเดียวกัน:

```text
Answer: <direct answer to the question>

Details:
• <relevant conditions or exceptions>

Rulebook: <game / tournament>
Source: <evidence reference>
```

คำถามกว้าง เช่น “กติกามีอะไรบ้าง” ใช้สรุปแบ่งหมวด ส่วนคำถามเฉพาะไม่ควรส่งทุกหมวดมารวมกัน คำถามเปรียบเทียบควรแยกต่อเกมหรือทำตารางตรงหัวข้อเดียวกัน

## 2. สถานะข้อมูลจริง
''']
lines.extend(['| เกม | ส่วนข้อมูลที่นำเข้า | เทียบไฟล์ต้นทางปัจจุบัน | Curated ตรงกับ chunk |', '|---|---:|---|---|'])
for row in audit['source_checks']:
    lines.append(f"| {row['game']} | {row['chunks']} | {'ตรง' if row['matches_current_source_import'] else 'ไม่ตรง'} | {'ตรง' if row['curated_text_matches_chunks'] else 'ไม่ตรง'} |")
lines.extend(['', '''รวม 4 เอกสารและ 104 chunks ข้อความยังตรงกับผล parser ปัจจุบัน ไม่พบข้อความหายเพิ่มจากขั้นตอนนำเข้าในรอบตรวจนี้ **การตรงกับ parser ไม่พิสูจน์ว่า parser แบ่งหัวข้อหรือกฎย่อยถูกความหมายแล้ว**

คิว V2 ปัจจุบัน:

- ตรวจ JSON review schema ผ่าน 104/104, errors 0, warnings 0
- `needs_owner_review` 104/104 และ `atomicity=review_required` 104/104
- `claim.answer_th` ยังว่าง 104/104; ข้อความไทยจริงอยู่ใน `source.clause_th` ไม่ใช่ฐานความรู้ทั้งหมดไม่มีข้อมูลไทย
- English ของคิวนี้เป็น draft 104/104; เป็นคนละชั้นกับ approved localization ที่เว็บ r24 ใช้
- หัวข้อกับ clause เท่ากัน 65/104; บางรายการเป็นกฎตัวเลขเต็มประโยค จึงห้ามสรุปว่า 65 รายการนี้ผิดหรือไร้เนื้อหาทั้งหมด
- Source clause hash ตรงทั้ง 104
- canonical release ทั้ง 4 ยัง inactive และ active canonical competition release IDs เป็นชุดว่าง

ดังนั้น **ผ่าน schema ≠ เป็นกฎย่อยที่จัดหมวดถูก ≠ ได้รับอนุมัติ ≠ ถูกใช้โดยตัวตอบแล้ว**

Runtime ตอนนี้ยังตอบจาก curated source เดิม/translation overlay และ renderer หลายตัว ตัว `competition_claim_store.py` และ claim completeness contract มีอยู่ แต่ไม่พบการเรียกใช้ V2 claim store/completeness validator จาก engine ปัจจุบัน จึงไม่อ้างว่าระบบย้ายมาใช้ atomic V2 ครบแล้ว

## 3. ผลตรวจคำตอบจริง 12 ข้อ

ตารางนี้แสดง first line และ route ที่ระบบส่งกลับ ไม่ได้ให้คะแนนใหม่ว่าเคสทั้งหมดถูกต้อง
''', '| ID | คำถาม | First line | Mode |', '|---|---|---|---|'])
for row in answers:
    values = [row['id'], row['question'], row['first_line'], row['mode']]
    lines.append('| ' + ' | '.join(value.replace('|', '\\|').replace('\n', ' ') for value in values) + ' |')
lines.extend(['', '''### ปัญหาที่พบชัดเจน

#### P0: คำตอบ Technical Pause ปนข้อของ Tactical Timeout

คำถาม `VALORANT technical pause สื่อสารได้ไหม`

บรรทัดแรกจริง: `คำตอบ: 2. การหยุดเกมทางเทคนิค (Technical Pause)`

รายละเอียดมีข้อห้ามสื่อสารที่เกี่ยวข้องอยู่ แต่ยังแสดง Tactical Timeout `2 ครั้ง/แผนที่, 60 วินาที` และ Major Bug ปนด้วย คำตอบควรขึ้นต้นว่า **ห้ามสื่อสารทั้งเสียงและข้อความ เว้นแต่ได้รับอนุญาต** แล้วขยายเฉพาะเงื่อนไข Technical Pause ที่ source รองรับ

สาเหตุที่ตรวจในโค้ด: `_format_competition_answer` รวบรวม candidate lines จากหลาย hits และ `_best_focus_lines` ให้คะแนนกับคำ pause/time/technical ได้ แต่ยังไม่บังคับว่าแต่ละบรรทัดต้องเป็น subtype และประเด็น communication เดียวกัน บรรทัด heading จึงยังเป็น answer_first ได้

#### P0: ตารางภาษาอังกฤษเสียความสัมพันธ์การละเมิดกับโทษ

`What is the CS2 tournament penalty matrix?` ได้ย่อหน้าที่รวมชื่อการละเมิดและบทลงโทษเข้าด้วยกัน และจบที่ `Offensive religious remarks` โดยไม่แสดงโทษคู่กันในคำตอบที่บันทึก

สาเหตุที่พบ: English path compact excerpt ตามจำนวนอักษร และไม่ได้รักษาแถวตารางแบบ Thai penalty_matrix path การตัดข้อความทำให้คู่สุดท้ายขาด ส่วนเกณฑ์ source overlap ยอมรับข้อความอื่นที่ถูกในย่อหน้าได้อยู่แล้ว

ควรแสดงเป็นตารางสองคอลัมน์หรือหนึ่ง bullet ต่อคู่ครบถ้วน ห้ามตัดกลางคู่หรือทำให้ผู้อ่านเดาว่าโทษใดเป็นของข้อใด

#### P1: อังกฤษยังไม่ตอบตรงคำถามบรรทัดแรก

คำถามเฉพาะอังกฤษทั้ง 5 ข้อในตัวอย่างขึ้นต้น `Verified ... competition rules:` แทนคำตอบจำนวน/ข้อห้าม/ค่าตั้งต้น แม้เนื้อหาที่เกี่ยวข้องอาจอยู่ bullet ถัดไป

เช่น `How many starting players can a CS2 team have?` ควรเริ่ม `Answer: Each team has 5 starting players.` แล้วให้รายการ/source ท้ายคำตอบ

คำถาม pause อังกฤษยังแสดงข้อเดียวกันซ้ำในสองสำนวน การตัดซ้ำด้วย token overlap จึงยังไม่เพียงพอในเคสนี้

#### P1: ธรรมชาติของคำถามไทยกับอังกฤษไม่สมมาตร

`Tekken 8 การตั้งค่าเกมเป็นยังไง` เข้า games และตอบคำอธิบายเกม/วิธีเล่น แต่ `What are the Tekken 8 in-game settings?` เข้ากติกาและตอบ 3 รอบ/60 วินาที

ไทยไม่ได้ระบุการแข่งขันชัด จึงมีความกำกวมว่าต้องการตั้งค่าทั่วไปหรือค่าที่รายการกำหนด แต่นโยบายเข้าใจคำถามไทย/อังกฤษในเรื่องนี้ไม่เหมือนกัน ต้องเลือกให้สม่ำเสมอว่าจะถามกลับหรือใช้ competition context ไม่ควรเติมกฎการแข่งขันจากการเดาในคำถามที่อาจหมายถึงอย่างอื่น

#### P1: หน้าเว็บไม่ render Markdown

ตรวจ DOM และ screenshot ของ `กติกา Tekken 8 มีอะไรบ้าง`:

- เห็น `**ข้อตกลงและข้อปฏิบัติ**` และ `**การหยุดเกม**` เป็นตัวอักษรจริง
- ภายใน bubble มี `strong/b=0`, heading elements=0 และ list items=0
- `web_chat/app.js` ใช้ `bubble.textContent = item.text`

Backend แทรก Markdown แต่ frontend อ่านเป็น plain text จึงยังไม่ได้ตัวหนาหรือรายการ HTML ตามที่ format สื่อไว้ หากพัฒนาต่อให้ render เฉพาะชุดรูปแบบที่ต้องใช้ด้วยการสร้าง DOM อย่างปลอดภัย แทนการนำข้อความตอบไปใส่เป็น HTML โดยตรง

#### P1: สรุปยังเรียงตาม source/selector มากกว่าโครงหัวข้อกลาง

Overview เลือกไม่เกิน 8 sections และไม่เกิน 2 clauses ต่อ section หัวข้อ CS2 มักเป็นประโยคกฎเต็มและยาว จึงไม่ถูกแสดงเป็น heading แบบเดียวกับ Tekken

Tekken สรุปขึ้นต้นข้อตกลงก่อนรูปแบบการแข่งขัน และในหัวข้อ pause เลือกข้อออกจากเกมก่อนข้อ Pause จริง ทั้งหมดเป็น source ที่มีอยู่ แต่ไม่ทำให้ผู้ใช้ได้ภาพรวมตามหมวดกลางอย่างครบถ้วน

ควรจัด outline จากข้อมูลเกม/รายการ → รูปแบบ → ผู้เล่น/คุณสมบัติ → อุปกรณ์/ตั้งค่า → ระหว่างเกม → โทษ/ข้อพิพาท และแสดงเฉพาะส่วนที่มีหลักฐาน หรือใช้ 10 หัวข้อกลางเมื่อผู้ใช้ขอรายละเอียดเอกสารทั้งหมด ต้องไม่เรียกสรุปบางข้อว่า “ครบทุกกฎ”

## 4. หน้าตาคำตอบที่ควรใช้แยกตามประเภท

### จำนวนหรือค่าตัวเลข

```text
คำตอบ: CS2 ลงแข่งพร้อมกันทีมละ 5 คนครับ

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: ส่วนองค์ประกอบทีมในเอกสาร
```

ไม่ตีความว่า roster รวมตัวสำรองได้แค่ 5 คนจากข้อมูลผู้ลงเล่น 5 คน

### อนุญาตหรือข้อห้าม

```text
คำตอบ: ไม่อนุญาตให้ใช้ Tablet หรือ iPad แข่ง RoV ในรายการนี้ครับ

รายละเอียด:
• ต้องใช้อุปกรณ์ประเภทโทรศัพท์มือถือ
• ตามเอกสาร หากตรวจพบจะถูกตัดสิทธิ์

อ้างอิงจากกติกา: RoV / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: ส่วนชุดแข่งขันและอุปกรณ์การแข่งขัน ข้อ 5.3
```

### Pause / timeout

```text
คำตอบ: ระหว่าง VALORANT Technical Pause ห้ามผู้เล่นสื่อสารกัน
ทั้งเสียงและข้อความ เว้นแต่ได้รับอนุญาตครับ

รายละเอียด:
• ข้อนี้เป็น Technical Pause; เงื่อนไขขอเวลานอก Tactical Timeout เป็นอีกประเภท

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: ส่วน Technical Pause
```

ไม่ใส่โควตา Tactical Timeout ในคำตอบเรื่องสิทธิ์การสื่อสารระหว่าง Technical Pause

### ตารางบทลงโทษ

```text
บทลงโทษจากเอกสาร CS2 รายการที่ระบุ:

การละเมิด                     บทลงโทษ
<ข้อจาก source>               <โทษคู่กับข้อเดียวกัน>
<ข้อจาก source>               <โทษคู่กับข้อเดียวกัน>

อ้างอิงจากกติกา: เกม / รายการ
แหล่งข้อมูล: ส่วนตารางบทลงโทษ
```

ตัวอย่างนี้เป็น layout ไม่มีการแต่งโทษใหม่ หากแสดงเพียงบางแถวต้องบอกจำนวนและขอบเขตที่แสดง และเก็บคู่ข้อมูลให้ครบแต่ละแถว

### คำถามกว้าง

```text
สรุปกติกา <เกม> — <ชื่อรายการ>
เป็นสรุปบางประเด็นจากเอกสาร

1. รูปแบบการแข่งขัน
• <รูปแบบและเงื่อนไขชนะ>

2. ผู้เล่นและคุณสมบัติ
• <ข้อมูลที่ source ระบุ>

3. อุปกรณ์และการตั้งค่า
• <ข้อกำหนด / ค่าตั้งต้น / หน่วย>

4. ระหว่างเกมและการหยุดเกม
• <เงื่อนไขแยกตามประเภท>

5. ข้อห้าม บทลงโทษ และข้อพิพาท
• <ข้อที่ source รองรับ>

แหล่งข้อมูล: <เอกสารและส่วนที่ใช้>
```

หัวข้อที่ไม่มีข้อมูลให้เว้นหรือแจ้งว่าข้อมูลส่วนนี้ยังไม่มีในเอกสาร ไม่เติมด้วยกฎเกมอื่น

## 5. ทำไมคะแนน Ground Truth รอบก่อนยังผ่าน

รอบ r24 ตรวจ route, game/source, facet evidence, outcome, source overlap และเวลา รวมทั้งตัวอย่าง numeric/negative clauses บางข้อ แต่ไม่ได้บังคับว่า:

1. คำตอบ direct ต้องอยู่บรรทัดแรก โดยเฉพาะอังกฤษ
2. ทุก detail line ต้องตอบ proposition/subtype เดียวกัน เช่น Technical communication แยกจาก Tactical allowance
3. ทุกคู่ในตารางต้องครบหลัง compact excerpt
4. Frontend ต้องสร้างตัวหนา/list จริง

ดังนั้นการมี `ห้ามสื่อสาร` อยู่ในรายละเอียดทำให้เคสผ่านได้ ทั้งที่ answer_first ยังเป็นหัวข้อและมีโควตาอีกประเภทปน ผลผ่านอัตโนมัติเดิมไม่ใช้เป็นหลักฐานว่ารูปแบบและการตีความทุกส่วนสมบูรณ์แล้ว

## 6. ลำดับการพัฒนาที่ตรงกับหลักฐาน

1. คัด clause ให้ตรงคำถามระดับประเด็นและ subtype ก่อนจัดหน้าตา โดยเพิ่ม negative expectations ห้ามข้อมูลอื่นปนในคำตอบ specific
2. รักษาตาราง/structured values พร้อมเงื่อนไขและหน่วย; หยุดตัดข้อความกลางคู่ข้อมูล
3. ใช้รูปแบบ direct → details → source ร่วมกันไทย/อังกฤษ และไม่เปิดด้วย heading เมื่อผู้ใช้ถามตัวเลข/อนุญาต/โทษ
4. เชื่อมการแสดงหัวข้อ/list ของหน้าเว็บกับชนิดคำตอบที่ backend ส่ง และตรวจทั้งข้อความกับ DOM
5. ปรับ outline ของ overview ให้หัวข้อเดียวกันมีหน้าตาคงที่และไม่อ้างครบถ้วนเกินหลักฐาน
6. เตรียม atomic child claims ที่แยก heading/ข้อกำหนดจริงให้ตรวจได้ แล้วจัดการ owner approval ของ release แยกจากงาน formatter

การแก้ presentation/selector/test ทำจากหลักฐานที่มีได้ ไม่จำเป็นต้องรอให้ผู้จัดแก้นโยบายทุกข้อ ส่วนการเปิดใช้ owner-approved V2 release หรือเลือกข้อยกเว้นนโยบายแทนผู้จัดเป็นคนละการตัดสินใจ

## 7. สิ่งที่ยังต้องยืนยันโดยผู้จัด

Tekken ส่วน s03 ห้าม pause และหยุดโดยเจตนาแพ้ 1 รอบ; s07 ยอมให้ pause เมื่อผู้เล่นทุกคนตกลงและมีเหตุเหมาะสม พร้อมโทษแบบออกจากเกมเมื่อ pause ไม่จำเป็น ต้องยืนยันขอบเขตข้อยกเว้น ผู้ให้อนุญาต และโทษต่อ round/game/match ก่อนสรุปเป็นนโยบายเดียว

การตรง source/hash และผ่าน schema ในรายงานนี้ไม่เปลี่ยนสถานะ owner review ข้อมูลอังกฤษ draft ของ V2 ไม่ใช่ข้อความอังกฤษ active overlay ของเว็บ จึงไม่เหมารวมว่าส่วนอังกฤษไม่มีข้อมูลทั้งหมด

## หลักฐานในโฟลเดอร์เดียวกับรายงาน

- `data_format_audit.json`: counts, source checks, active release และ queue status
- `queue_schema_validation.json`: ผลตรวจ schema 104 records
- `current_http_answers.json` / `.jsonl`: คำถามและคำตอบจริง 12 ข้อจากเว็บ r24
- `ui_format_check.json`: ผลตรวจ DOM และสิ่งที่เห็นใน screenshot

ไฟล์อ้างอิงในโปรเจกต์: submission template, docs/14, docs/24, docs/86, app/pipeline/retrieval.py, app/pipeline/bilingual_english.py, app/pipeline/competition_overview.py และ web_chat/app.js
'''])
with (OUT / 'COMPETITION_FORMAT_AUDIT_20261001.md').open('x', encoding='utf-8') as handle:
    handle.write('\n'.join(lines) + '\n')
print(str(OUT / 'COMPETITION_FORMAT_AUDIT_20261001.md'))
