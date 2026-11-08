import json,hashlib,collections,subprocess
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
W=Path(__file__).parent;R=Path((W/'r33_report_path.txt').read_text().strip())
read=lambda name:json.loads((R/name).read_text(encoding='utf-8'))
write=lambda name,text:(R/name).open('x',encoding='utf-8').write(text)
metrics=read('composed_H_SUMMARY.json');unit=read('final_I_unit_all.json');freeze=read('final_I_runtime_freeze.json')
assert unit['success'] and unit['tests']==472
before=read('before_manifest.json');protected=read('protected_manifest.json');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old_tests=[k for k in before if k.startswith('tests/')]
assert all(sha(P/k)==before[k] for k in old_tests)
assert all(sha(P/k)==v for k,v in protected.items())
scope=dict(full_runtime='candidate_D',full_unique_requests=20327,full_grades=55583,
          final_G_replay=read('final_G_replay_scope.json'),final_H_replay=read('final_H_replay_scope.json'),
          final_I_change='Thai compound contact index binds approved source IDs to canonical content_id and checks answer text. No frozen-corpus compound email+phone inputs were present (H replay selected zero); I verified with 8 regression tests and actual HTTP compound contact. Do not claim a fresh final I full sweep.',
          installed_package='owner_local_delivery_20261002_usable_task_frames_r33_finalI/PSU_Esports_Chatbot_Local',
          preserved_owner_gold_hashes=len(protected),preserved_existing_test_files=len(old_tests),
          additional_test_file='tests/test_usable_task_frames_r33_20261002.py',
          provenance='Every composed record retains candidate_D, final_G or final_H execution generation. Full D and final G source hashes are separately frozen.',
          real_occupancy='paused_by_user; known synthetic fixture does not establish real occupancy correctness',
          legacy_metrics=metrics)
with (R/'FINAL_EXECUTION_SCOPE.json').open('x',encoding='utf-8') as f:json.dump(scope,f,ensure_ascii=False,indent=2)

# Preserve compact reasons for every failed unique frozen-corpus input. This is
# automatic triage, not a claim that every legacy expected answer is correct.
counts=collections.Counter();rows=[]
for line in (R/'composed_H_FAILURES.jsonl').open(encoding='utf-8'):
 x=json.loads(line);z=x.get('result',{});mode=z.get('mode','');failed=[g for g in x['grades'] if not g['passed']]
 if x.get('exception'):bucket='execution_exception'
 elif 'personal_peripheral_policy' in mode:bucket='missing_general_policy_old_oracle_expected_answer'
 elif 'live_booking_status_unavailable' in mode:bucket='live_source_fixture_unavailable_or_legacy_route'
 elif 'localization' in mode:bucket='english_source_or_translation_boundary'
 elif 'source_conflict' in mode or 'partial_source' in mode:bucket='source_gap_conflict_or_partial_outcome'
 elif 'clarification' in mode:bucket='clarification_needs_semantic_review'
 elif any('source' in str(g['failures']) or 'rulebook' in str(g['failures']) for g in failed):bucket='source_identity_or_rulebook_contract_review'
 elif any('missing' in str(g['failures']) for g in failed):bucket='literal_content_or_missing_answer_review'
 else:bucket='route_outcome_or_intent_contract_review'
 counts[bucket]+=1
 rows.append(dict(key=x['key'],question=x['question'],locale=x['locale'],mode=mode,
                  category=z.get('route',{}).get('category'),answer=z.get('answer',''),
                  priority_bucket=bucket,classification='automatic triage requiring source/semantic review',
                  failures=[dict(corpus=g['corpus'],id=g['id'],variant=g['variant'],errors=g['failures'],evidence_level=g.get('evidence_level')) for g in failed],
                  trace_reference='final_H_all_results.jsonl key='+x['key']))
with (R/'ALL_REMAINING_FAILURE_TRIAGE.jsonl').open('x',encoding='utf-8') as f:
 for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
with (R/'ALL_REMAINING_FAILURE_TRIAGE_COUNTS.json').open('x',encoding='utf-8') as f:json.dump(dict(total=len(rows),counts=counts,classification='automatic grouping, not human factual adjudication'),f,indent=2)

flow='''# Flow ตรวจและแก้จากการใช้งานจริง — PSU Esports Chatbot r33

วันที่ 2 ตุลาคม 2026 เวลาไทย • แพ็กเกจ finalI • runtime `2026.10.02-usable-task-frames-r33`

## 1. ผลที่ส่งมอบ

เว็บทดสอบใช้งานอยู่ที่ http://127.0.0.1:8090/ แพ็กเกจใหม่อยู่ใน `owner_local_delivery_20261002_usable_task_frames_r33_finalI/PSU_Esports_Chatbot_Local`

ใช้ launcher ของแพ็กเกจนี้เมื่อต้องเปิดใหม่ กระบวนการเว็บต้องทำงานอยู่เพื่อรับคำถาม สถานะจองถูกดึงจาก WordPress เมื่อคำถามต้องใช้ข้อมูลสดตาม flow เดิม; การอ่านสถานะไม่สร้างรายการจอง งานเก็บ occupancy จริงยังพักตามคำสั่งผู้ใช้

## 2. Flow จาก input ถึง output

```mermaid
flowchart TD
 A[ข้อความดิบ ภาษา ประวัติ] --> B[ตรวจแป้นและตัวอักษรเบิ้ล]
 B --> C[กู้คำบอกงานในกรอบบริบท]
 C --> D[คงชื่อ เลข เวลา คำปฏิเสธ และคำเชื่อม]
 D --> E{ต้องใช้สถานะจองสดหรือไม่}
 E -- ใช่ --> F[อ่าน WordPress ตามวัน เครื่อง และช่วงเวลา]
 F --> G{ข้อมูลครอบคลุมและอ่านสำเร็จหรือไม่}
 G -- ไม่ --> H[แจ้งว่ายังยืนยันสถานะสดไม่ได้]
 G -- ใช่ --> I[ตอบจำนวนว่างและเครื่องตามขอบเขตคำถาม]
 E -- ไม่ --> J{กติกาการแข่งขันหรือไม่}
 J -- ใช่ --> K[ล็อกเกม รายการ ปี และทุกประเด็น]
 K --> L[อ่านข้อกฎ พร้อมเลขและข้อยกเว้น]
 L --> M{ข้อมูลครบและไม่ขัดกันหรือไม่}
 M -- ไม่ --> N[ตอบส่วนที่มี แสดงส่วนขาดหรือขัดกัน]
 M -- ใช่ --> O[จัดคำตอบจากข้อกฎที่ตรง]
 J -- ไม่ --> P[เลือกบริการ ราคา ติดต่อ สมาชิก เกม หรือความรู้]
 P --> Q[ผูกค่าคำตอบกับแหล่งจริง]
 H --> R[ตรวจเนื้อหา ภาษา ขอบเขต และหลักฐาน]
 I --> R
 N --> R
 O --> R
 Q --> R
 R --> S{ผ่านเงื่อนไขหรือไม่}
 S -- ไม่ --> T[ถามกลับหรือแจ้งข้อมูลที่ยังขาด]
 S -- ใช่ --> U[ส่งคำตอบและเก็บ trace]
```

## 3. การกู้คำผิด

1. เก็บ input เดิมและแต่ละข้อความระหว่างแก้ใน trace เสมอ
2. ใช้ OSA/edit distance กับศัพท์งานที่ระบบรองรับ เช่น ราคา การจอง กฎ การติดต่อ มี syntax/topic ที่ยังอ่านได้เป็นหลักฐาน
3. อังกฤษ: จำกัดตำแหน่งคำ เช่น modifier ก่อน hardware noun; ไม่แก้ house เป็น mouse เพียงเพราะประโยคมีคำว่า gaming
4. ไทยไม่มีช่องว่าง: เทียบ span ของคำบอกงานกับบริบทอุปกรณ์/เกม/รูปคำถามและขอบหลังคำ เช่น ก่อน/ภายใน
5. หลายคำผิด: เลือกการแก้ทีละ span หากต่างตำแหน่งกัน; ถ้าคำตอบหลายคำแข่งขันใน span เดียวกันและคะแนนเท่ากัน ให้คงคำเดิม
6. ใช้ budget เดิม 3 spans / 4 edits รวมในการกู้คำบอกงาน ไม่ขยายการแก้ให้ไม่มีขอบเขต
7. คำจริงที่กำกวม เช่น pay, rice, embers, march ต้องรักษาความหมายหรือถามเพิ่ม ชื่อหลัง Mr./Ms./Dr./called/named ไม่เป็นคำบอกงานให้สะกดแก้เอง
8. ข้อจำกัดของตัวกู้ใหม่: ประโยคยาวเกิน 180 อักษร/URL/@ ข้ามตัวกู้กรอบงานนี้ แต่ยังผ่านส่วนอื่นของ pipeline ตามเดิม ไม่ได้แก้การพิมพ์ผิดทุกคำทั่วไป

## 4. คำตอบที่ผูกกับข้อมูล

- ราคาเปรียบเทียบ: อ่าน SERVICE_FEES ของทุกบริการที่ระบุ แสดงระยะเวลา ความจุ และราคาแต่ละกลุ่ม ไม่เลือกถูกกว่าโดยสมมุติกลุ่ม/จำนวนผู้เล่น
- เกมไปบริการจอง: ต้องมีเกมและภาคตรงรายการ จึงแสดงบริการที่มีเกมนั้น พร้อมขั้นตอนจอง; catalog ไม่ใช่การยืนยัน Slot สด
- รายการสมาชิก: ถามคนใดต้องพบชื่อที่ยืนยันได้ ไม่ตอบ directory ทั้งหมดแทนคนที่ไม่รู้จัก; จำนวนหมวดคำนวณจากรายการจริง
- อีเมลพร้อมโทรศัพท์: อ่านกฎเดิมทั้งสองช่อง ผูก source ID กับ canonical content_id แล้วเก็บ projected evidence ID เดิม ตรวจข้อความตรงแหล่งก่อนตอบ
- คำว่า transfer booking: ใช้กฎไม่ให้โอนสิทธิ์จอง; bank/money/payment transfer ใช้กฎวิธีชำระ
- วันภาษาอังกฤษ: พหูพจน์ใช้เฉพาะชื่อวันเต็ม Sundays/Saturdays; ไม่เติม s หลัง thu แล้วทำให้ thus กลายเป็นวันพฤหัส
- เกมที่ไม่ปรากฏในรายการ: ตรวจ catalog ปัจจุบันก่อนตอบว่า “ยังไม่พบในรายการที่ยืนยันได้” ไม่กล่าวว่าไม่มีเกมแน่นอน และไม่เปลี่ยนคำถามแนวเกมเป็นสถานะสตูดิโอ
- อุปกรณ์ส่วนตัว/ส่งเครื่องถึงบ้าน: ไม่ยืมกฎเฉพาะการแข่งขันมาอนุญาตการใช้บริการทั่วไป ถ้าไม่พบหลักฐานต้องแจ้งช่องว่าง

## 5. ตรวจ flow และลงมือหลายรอบ

| รอบ | พบอะไร | แก้และหลักฐาน |
|---|---|---|
| A | คำบอกงานหาย/หลายคำผิด; การกู้ไทยไปกินคำกี่นาที | เพิ่มกรอบงาน; unit พบข้อผิดพลาด 7 และ dependency error 1 เก็บผลเดิม |
| B | กู้คำจนเปลี่ยนระยะเวลา/ความหมาย | ล็อกคำจริงและคำปฏิเสธ แยก Thai competition recovery; focus 88/107 |
| C | ชื่ออังกฤษถูกตัดตรงจุดหลัง Mr.; ข้อความ overnight ไม่ครบเกณฑ์ | แก้ขอบเขตชื่อและแจ้งขาดข้อมูล; focus 93/107 |
| D | เกมก่อนคำถามมี/ไหมและบริบทบริการยังตก | แก้กรอบงาน; unit 464/464; full 20,327 requests |
| E | 5/24 ประโยคใหม่ผิด: ก่อน/ภายใน, reservatoin, contact สองช่อง, house→mouse | จำกัดตำแหน่ง noun และเพิ่มขอบหลังคำ; ใหม่ 24/24 ผ่านเว็บเมื่อพร้อม |
| F | contact source ใช้ registry ผิดประเภท; Minecraft ผ่าน retrieval ช้า | อ่าน curated sources และเพิ่ม catalog absence path แต่ยังพบ id ของแถวไม่ครบ |
| G | thus→Thursday; transfer booking→บัญชีธนาคาร; หลาย span ผิดทำให้ abstain ทั้งประโยค | จำกัด weekday plurals แยกความหมาย transfer และยอมแก้คนละ span; replay 7,177 |
| H | แถว metadata ไม่มี id ทำให้ worker เริ่มใหม่ | ข้ามแถวไม่ใช่ record; crash หาย แต่ helper ยังไม่ผูก canonical content_id |
| I | canonical projection ID ต่างจาก source ID | ผูก content_id และตรวจ source text; unit 472/472, contact HTTP ตรง 2 ช่อง |

แต่ละรอบใช้ผลก่อนหน้าเป็นหลักฐาน ไม่เปลี่ยน owner data หรือ Gold เดิม ผล failed/transport/startup/interrupted ถูกเก็บไว้ด้วย

## 6. เกณฑ์ทดสอบและขอบเขตหลักฐาน

1. unit ตรวจข้อผิดพลาดการทำงานและขอบเขต; ไม่รับรองข้อเท็จจริงทุกคำถาม
2. source/content oracle ตรวจคำตอบจริงและแหล่งที่ตรง; route/status ผ่านอย่างเดียวไม่พอ
3. ชุดพิมพ์ผิดใช้ scorer v2 เดียวกับ r32: 2,000 คู่ มี positive content contract 894 คู่เท่านั้น
4. full D สด 20,327 inputs / 55,583 grades จากนั้น G replay 7,177; ผลรวมเป็น composite ที่เก็บ generation รายข้อ ไม่เรียกว่า finalI fresh full sweep
5. I เปลี่ยนเฉพาะ compound contact source mapping; corpus เก่าไม่มีคำถาม email+phone ที่เข้า guard นี้ จึงใช้ 8 regression tests และ HTTP คำถามใหม่เพิ่ม
6. HTTP ใช้ runtime ที่เปิดจริงพร้อม LLM/semantic profile ของแพ็กเกจ; full offline ใช้ LLM OFF/semantic OFF และ controlled live-unavailable fixture จึงเป็นคนละสภาพทดสอบ
7. ชุด 24 ประโยคใหม่เริ่ม D ได้ 19/24 หลังนำ failure มาแก้ จึงเป็น regression set ไม่ถือเป็น holdout ใหม่หลังแก้
8. เชื่อม API สำเร็จ ≠ สถานะว่าง/จองถูกต้อง: synthetic booking 31/31 เป็นข้อมูลรู้ผลจำลอง; occupancy จริงยังไม่ยืนยัน

## 7. ผลที่ตรวจแล้ว

- finalI unit 472/472; usage source assertions ไทย/อังกฤษ 56/56; literal preservation 24/24 input ไม่ซ้ำ
- finalI HTTP กฎตรวจเนื้อหา 30/30; partial 8/8; ฉบับปี 24/24
- G actual HTTP regression 935/937: 2 เคสอายุ/คุณสมบัติคาด no_answer ทั้งคำถาม แต่ระบบตอบส่วนที่มีและบอกอายุที่ขาด ชุด partial ตรวจแยกผ่าน
- finalI browser helper พร้อมกัน 10/10 ทั้ง test port และ 8090; เป็น catalog/simple requests ไม่ใช่ SLA ของ LLM/WordPress
- production smoke literal 9/10; อีกเคส oracle ใช้คำว่า ราคา แต่คำตอบมาตรฐานใช้ ค่าบริการ และตอบเหมือน clean ทุกตัวอักษร มี adjudication แยก ไม่เขียนทับผล 9/10
- frozen corpus composite ผ่านเกณฑ์เก่า 52,015/55,583; 1,807 unique inputs มี failed grade อย่างน้อยหนึ่ง เกณฑ์เหล่านี้ยังมี expected status/route/ชื่อแหล่งเก่าและ source gaps ไม่เท่ากับ 1,807 คำตอบผิดจริง
- typo v2 clean 1,760/2,000, noisy 1,760/2,000; clean-pass/noisy-fail 9 คู่ เทียบ r32 107 คู่ noisy เดิม 1,676 ไม่แปลว่าถูกเนื้อหา 88% ทุกคำถาม

## 8. งานที่เหลือ เรียงลำดับ

### P1: 4 กรณีพิมพ์ผิดที่มีประเด็นต้องแก้ต่อ

1. คำขึ้นต้น “จอสอบถาม…” ทำให้ validator มอง equipment แม้แก้ “พงกว่า” เป็น “แพงกว่า” และสร้างราคา PC+VR ที่ถูกจาก source แล้ว: แก้การจัดน้ำหนัก question frame/ส่วนคำนำ โดยคงการตรวจแหล่ง ไม่ปิด validator
2. “จ่ายเงินยังไงตอนของ” เสียคำ จอง; task grammar จึงไม่จับ reservation: ใช้กรอบวิธีชำระที่มีหลักฐานอิสระและคำตอบธนาคารเดิม พร้อม negative controls โอนสิทธิ์/โอนเงิน/ยอดราคา
3. “คำพูไดม่เหมาะสม” ทำให้คำบอกงานและ negation เสียพร้อมกัน: ต้องแก้กู้ span ที่รักษาปฏิเสธ ห้ามลด threshold จนคำพูดเหมาะสมถูกเปลี่ยนเป็นไม่เหมาะสม
4. “อ้างอิงติกา … จำนวยผู้เล่นต่อทีม”: เสียทั้งคำกติกาและจำนวน; ต้องกู้ operation ก่อน target/source ranking แล้วตรวจ exact edition/ครบข้อกฎ

การลงมือรอบต่อไป: oracle เนื้อหาจาก source → เก็บ clean/noisy/คำปฏิเสธ/คำจริงควบคุม → แก้ทีละประเภท → source/negative/replay → hash/package/HTTP ไม่เพิ่ม alias ของทั้งคำถามเพื่อให้เคสผ่าน

### P2: 5 คู่ที่ไม่ควรบังคับแก้เป็นเจตนาเดียว

- Wherw can you pay VALORANT: กู้ where แล้วถามว่าจะเล่นหรือจ่ายเงิน
- rice: เป็นคำจริง อย่าบังคับ price
- in-march procedure: march เป็นคำจริง อย่าบังคับ in-match
- Who are the embers: embers เป็นคำจริง ยังขาดกรอบว่าเป็น members ของศูนย์
- นาย้ปนไค อ: ข้อความหายหลายส่วนและ candidate ต่ำ จึงถามกลับก่อน

### P2: ตรวจเกณฑ์ชุดใหญ่กับ source ทีละกลุ่ม

ดู ALL_REMAINING_FAILURE_TRIAGE.jsonl และ counts; การจัดกลุ่มเป็น automatic triage ไม่ใช่ owner factual review ควรเริ่ม positive content failures แล้วจึง source identity/route-only failures ห้ามแก้ Gold เงียบ ๆ เพื่อเพิ่มคะแนน

### ข้อมูลและการใช้งานที่ยังต้องยืนยัน

- นโยบายอุปกรณ์ส่วนตัวและถ่ายภาพ; เพิ่มข้อมูลจริงแล้วต้องปรับ missing-policy guards ไม่ให้บังนโยบายใหม่
- Tekken pause ขัดกัน; RoV 6.1.5.1 จบไม่ครบ; ค่าสมัคร อายุ roster รวมสำรอง ฉบับปี และการตรวจคำแปล
- ชื่อสมาชิกภาษาอังกฤษที่ไม่มี mapping ยืนยัน: ใช้ชื่อไทยใน directory หรือต้องให้เจ้าของยืนยันการเชื่อมชื่อ
- control mappings ที่มาจาก secondary source ต้องตรวจเกม/จอยที่ติดตั้งจริงตามคำเตือนเดิม
- occupancy และ workload มากกว่า burst ที่ตรวจยังไม่รับรอง; งาน occupancy พักตามผู้ใช้

## 9. การรักษาไฟล์และ provenance

ไม่ reset/stash/commit/ลบแพ็กเกจหรือ log เก่า owner/Gold hashes 584 ตรงเดิม ไฟล์ tests ที่มีใน snapshot ตรงเดิมทั้งหมด เพิ่มเฉพาะ regression file ใหม่ แพ็กเกจ finalI กับ project app/UI ตรงกัน 129 files

full D freeze มี note เก่าที่ไม่ตรงคำอธิบาย generation อยู่ใน artifact แรก ให้ใช้ FINAL_EXECUTION_SCOPE.json และ generation ของแต่ละ raw record เป็นหลัก ไม่แก้ทับ artifact ประวัติ

API run E ก่อน server พร้อมเป็น connection refused; E/G compound contact เคยเกิด worker restart; H HTTP regression ถูกขัดจังหวะตอนเปลี่ยน packageและมี mixed transport จึงไม่นับเป็นคะแนน finalI ใช้ G complete regression กับ I final checks แยกกัน

ดู FINAL_RESULTS_TH.md, REMAINING_9_SOURCE_REVIEW.jsonl, ALL_REMAINING_FAILURE_TRIAGE.jsonl, OWNER_QUESTIONS_FINAL_TH.md และ FINAL_EXECUTION_SCOPE.json ใน report r33 สำหรับรายละเอียด
'''
write('FLOW_R33_FINAL_TH.md',flow)
doc=P/'docs/134_usable_task_frames_r33_verified_flow_20261002.md'
with doc.open('x',encoding='utf-8') as f:f.write(flow)
owner='''# คำถามที่ต้องให้เจ้าของ/ผู้จัดยืนยัน — r33

## นโยบายใช้บริการทั่วไป

1. นำ keyboard/mouse/controller ส่วนตัวมาเปลี่ยนอุปกรณ์ของศูนย์ได้หรือไม่? อุปกรณ์ใดอนุญาต ต้องขอเจ้าหน้าที่ก่อนหรือไม่ ใช้พอร์ต/driver ใดได้ และมีเงื่อนไขความเสียหายอะไร? โปรดให้ข้อความนโยบายและวันที่มีผล กฎ VALORANT แข่งขันอนุญาตอุปกรณ์ส่วนตัวไม่เพียงพอสำหรับการใช้ทั่วไป
2. ถ่ายภาพ/วิดีโอได้หรือไม่ พื้นที่ใด ต้องขอความยินยอมใคร และข้อจำกัดการเผยแพร่คืออะไร?
3. มีบริการส่งเครื่องถึงบ้านหรือพักค้างคืนจริงหรือไม่? หากมี ขอประเภทบริการ/เงื่อนไข/ช่องทางอ้างอิง ระบบปัจจุบันแจ้งว่าไม่พบข้อมูลยืนยัน ไม่ได้ประกาศว่าไม่มีบริการแน่นอน

## กติกาการแข่งขัน

4. Tekken 8: ข้อห้าม pause หลังเริ่ม กับข้ออนุญาตเมื่อทุกฝ่ายยินยอม ใช้ร่วมกันอย่างไร? ต้องได้รับอนุญาตจากกรรมการด้วยหรือไม่? ทำผิดแพ้รอบ เกม หรือแมตช์? ขอฉบับข้อกฎและวันที่มีผล
5. ขอ RoV Blueket 2025 ทีมชาย ข้อ 6.1.5.1 ฉบับเต็ม (`competition_rules_rov_blueket_2025_men_s08_c01`) ที่จบ “ดังกล่าวออกจาก” พร้อมไฟล์ต้นฉบับ
6. แต่ละรายการมีค่าสมัคร อายุขั้นต่ำ และ roster รวมสำรองกี่คน? เปลี่ยนรายชื่อได้ถึงเมื่อไร? แยกคุณสมบัตินักศึกษาจากอายุให้ชัด
7. โปรดยืนยันฉบับที่จะใช้จริงของ CS2 2026, VALORANT 2026, RoV Blueket 2025 ทีมชาย และ Tekken 8; ฉบับที่ยังไม่มีระบบจะไม่ยืมกติกาคนละปีตอบแทน

## ภาษาและตัวตน

8. English names Mr. Kanokchai Siripanthisaraworn และ Mr. Naphat Chuea Lekwanich เชื่อมกับ record ไทยใดใน directory? ขอ spelling/mapping ยืนยัน ไม่ใช้ความคล้ายในการเดา identity
9. ขอผู้ตรวจไทย/อังกฤษยืนยันศัพท์ ตัวเลข ข้อยกเว้น และความหมายทุกข้อกฎจากต้นฉบับเดียวกัน machine registry/source hash ไม่ใช่การอนุมัติจากผู้จัด
10. ปุ่มควบคุมจาก secondary source ตรงกับเกม/edition/controller settings ที่ติดตั้งจริงหรือไม่?

## การจองจริง — พักตามคำสั่งผู้ใช้

11. เมื่อพร้อมเท่านั้นจึงส่งตัวอย่างวันที่/เวลาไทย/เครื่อง/ช่วงเวลา/สถานะที่เจ้าหน้าที่รู้จริงและเวลาเก็บข้อมูล โดยไม่ส่งข้อมูลส่วนตัวลูกค้า เพื่อแยก API transport จาก occupancy correctness ตอนนี้ยังไม่เก็บสถานะจริงและไม่สร้างรายการจอง
'''
write('OWNER_QUESTIONS_FINAL_TH.md',owner)
result=f'''# ผลส่งมอบ r33 finalI

## ใช้งาน

เว็บ: http://127.0.0.1:8090/ รุ่น `2026.10.02-usable-task-frames-r33`

เปิดใหม่จาก `{scope['installed_package']}/Open-PSU-Esports-Chatbot.cmd`

## แก้แล้ว

- กู้คำบอกงานหลายคำตามบริบททั้งไทย/อังกฤษ และจำกัดขอบไม่แก้ชื่อ/เลข/คำจริงเป็นอุปกรณ์ผิด
- ตอบราคาเปรียบเทียบ PC/VR ครบทุกแพ็กเกจ เกมไปบริการจอง จำนวนหมวดสมาชิก และชื่อบุคคลจากหลักฐาน
- อีเมลพร้อมเบอร์โทรไทย/อังกฤษตอบครบ; แก้ source ID/canonical ID ที่เคยทำให้ worker restart
- thus ไม่เป็นวันพฤหัส; transfer booking ไม่เป็น bank transfer
- Minecraft availability แบบระบุศูนย์ใช้ catalog ที่มีและแจ้ง absence อย่างระมัดระวัง HTTP finalI ประมาณ 0.28–0.70 วินาทีใน probes; คำถามแนวเกมไม่ถูกเปลี่ยนเป็นสถานะสตูดิโอ

## หลักฐานอัตโนมัติ

| ชุด | ผล | ขอบเขต |
|---|---|---|
| finalI unit | 472/472 | existing 464 + new 8, ไม่รับรองทุกข้อเท็จจริง |
| finalI usage source assertions | 56/56 | ไทย/อังกฤษ; 24 เคสถูกใช้แก้แล้ว ไม่ใช่ holdout หลังแก้ |
| literal preservation | 24/24 | input ไม่ซ้ำ; ไม่ใช่การรับรองว่าคำกำกวมถูกทุกครั้ง |
| finalI competition source | 30/30 | เนื้อหาและแหล่งที่ตรง |
| finalI partial | 8/8 | ส่วนที่มี/ส่วนขาด |
| finalI editions | 24/24 | TH/EN ปีตรงและปีที่ขาด |
| G full HTTP regression | 935/937 | 2 frozen age partial outcome differences; ไม่อ้างว่ารัน I สดทุกข้อ |
| browser helper 8091 และ 8090 | 10/10 ต่อพอร์ต | simple catalog burst; ไม่ใช่ WordPress/LLM SLA |
| release 8090 | literal 9/10, source review 10/10 | ราคา/ค่าบริการ synonym; เก็บ failed literal กับ adjudication แยก |
| known booking D fixtures | 31/31 | synthetic known states, ไม่ใช่ occupancy จริง |
| D sessions | 12/12, 24 turns | controlled live unavailable, ไม่ใช่ production chat human review |

## ชุดใหญ่และที่มาคะแนน

Full D รันใหม่ครบ 20,327 unique inputs / 55,583 grades จากนั้น G replay 7,177 inputs ทุกคู่ typo + failed + affected vocabulary; H compound replay 0 เพราะไม่มีคำถามทั้ง email/phone ใน corpus เก่า I ตรวจ guard นี้ด้วย unit/HTTP ใหม่

Composite frozen-grader ผ่าน 52,015/55,583 และมี 1,807 unique inputs ที่ failed grade อย่างน้อยหนึ่ง ยังไม่ใช่ accuracy factual เพราะ expected route/status/IDs/translation เก่าบางส่วนไม่ตรง source boundary ปัจจุบัน ดู FINAL_EXECUTION_SCOPE.json และ raw generation

Typo scorer v2 เดียวกับ r32: clean 1,760/2,000; noisy 1,760/2,000 (เดิม 1,676); clean-pass/noisy-fail 9 คู่ (เดิม 107) มี positive content oracle 894 คู่ ส่วนอีก 1,106 คู่ยังไม่ยืนยันเนื้อหาครบ

Old107 focus F: 94/107 และกลุ่ม positive42 ผ่าน42/42 แต่มีกรณีใหม่ thus ในชุดใหญ่จึงแก้ G และทดสอบ finalI จริง ไม่ใช้คะแนน old focus กลบ regression ใหม่

99 newly failed legacy grades: 94 เกี่ยวกับการนำอุปกรณ์ส่วนตัวที่ไม่มีนโยบายทั่วไป, 2 unknown English identity, 3 holiday-date/multi-zone price clarifications; เป็น source/scope review ของ assistant ไม่ใช่การอนุมัติ owner ว่าทุกคำตอบถูก

## ยังเหลือ

4 noise cases มีงานพัฒนาต่อ: คำนำ จอสอบถาม บัง price validator; จ่ายเงินยังไงตอนของ ไม่เข้า payment frame; คำพูด/ปฏิเสธเสียพร้อมกัน; กติกา/จำนวนผู้เล่นเสียพร้อมกัน อีก 5 คู่เป็นคำจริงกำกวมหรือข้อความขาดที่ควรถามเพิ่ม

Source gaps/conflicts/English identity/secondary controls/owner policy/human translation review และ real occupancy ยังไม่ยืนยัน รายละเอียดและคำถามเจาะจงอยู่ใน OWNER_QUESTIONS_FINAL_TH.md

## การรักษาของเดิม

owner/Gold 584 hashes ตรงเดิม; existing tests {len(old_tests)} files ตรงเดิม; package app/UI 129 files ตรง project; เก็บ snapshotก่อนแก้ code {len(before)} files ไม่มี reset/stash/commit และไม่ทับผล/package/log ประวัติ

ผล E startup refused, E/G contact exceptions, H partial HTTP ที่ถูกขัดจังหวะยังคงอยู่ ไม่ใช้คะแนนเหล่านั้นแทน finalI verification

ดู FLOW_R33_FINAL_TH.md สำหรับ flow ฉบับตรวจหลังลงมือ และ ALL_REMAINING_FAILURE_TRIAGE.jsonl สำหรับรายการ failed ทุก input พร้อม key ไป trace จริง
'''
write('FINAL_RESULTS_TH.md',result)
write('ARTIFACT_PROVENANCE_NOTES.md','''# Corrections and incomplete runs preserved

- candidate_D_runtime_freeze.json has an inherited note mentioning an earlier C6 runtime. Its manifest is D; FINAL_EXECUTION_SCOPE.json and D/G/I manifests identify actual runs. The historical file is retained unchanged.
- api8091_E_novel: before readiness, 14 connection-refused responses. api8091_E_ready is the content rerun; neither is a human approval.
- E contact unknown_source_id exception; G id exception; H contact fell back because canonical projection ID was confused with content_id. I adds content_id binding, text equality and regression test source_ids rather than projected chunk IDs.
- api8091_H_http_results.jsonl was interrupted during package replacement and overlapped subsequent I requests; it contains transport failures and mixed runtime traffic, no completed summary. It is not a clean H or I regression score. Complete G regression and final I focused HTTP records are separate.
- Release literal 9/10 is preserved. The tenth answer uses ค่าบริการ rather than the provisional oracle's ราคา. Source/clean-control adjudication is saved separately; no runtime or legacy Gold change was made for this lexical mismatch.
- Initial test dependency import errors are retained. A new test-only dependency directory was used; old dependency files were not overwritten.
''')
status=subprocess.run(['git','status','--short'],cwd=P,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8').stdout
write('git_status_after.txt',status)
print(json.dumps(dict(report=str(R),flow=str(doc),preserved_tests=len(old_tests),snapshot_files=len(before),remaining_triage=len(rows),counts=counts),ensure_ascii=False))
