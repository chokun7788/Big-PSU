import hashlib,json,statistics,sys
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';W=Path(sys.argv[1]).resolve()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
web=read(W/'SUMMARY.json');assert web['count']==web['passed']==web['expected_count']==51 and not web['model_failures'] and not web['obstacle']
baseline=read(B/'verification/baseline_1/SUMMARY.json');fixture=read(B/'verification/fixture_release/SUMMARY.json');installation=read(B/'INSTALLATION.json')
rows=[json.loads(l) for l in (W/'TURNS.jsonl').read_text(encoding='utf8').splitlines()];before=[json.loads(l) for l in (B/'verification/baseline_1/TURNS.jsonl').read_text(encoding='utf8').splitlines()]
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert all(digest(S/name)==sha for name,sha in installation['installed_files'].items())
assert digest(S/'data/knowledge/common.sqlite')==installation['database_sha256']
lines=['# R87 เชื่อมพฤติกรรมเดิมกับข้อมูล Format กลาง','',
'## สถานะ','',
'ติดตั้งในแชท R78 ที่ http://127.0.0.1:8115/ แล้ว เว็บโหลด fingerprint โค้ดล่าสุดและเปิด LLM ตรวจจริงก่อนเริ่ม ชุดใหญ่ยังพักไว้ ไม่มีการรัน legacy corpus หรือ LLM OFF','',
'| ชุด | ผ่าน | ความหมาย |','|---|---:|---|',
f"| คำถามเป้าหมายเดียวกันก่อนแก้ (R84) | {baseline['passed']}/{baseline['count']} | Candidate overlay แบบ before; โมเดลจริงเปิดและสร้างคำตอบได้ |",
'| Candidate หลังเชื่อม | 51/51 | เปิด LLM โมเดลจริง; ครอบคลุมคำตอบ/ขอบเขต/การถามต่อที่กำหนด |',
f"| เว็บที่ติดตั้งจริง | {web['passed']}/{web['count']} | HTTP จริง มี server session และ common_read_state |",
f"| เพิ่ม/แก้/ถอนข้อมูลและขอบเขตในฐานทดลอง | {fixture['passed']}/{fixture['count']} | source fixture ที่รู้ค่า; ควบคุม transport ไม่ใช่คะแนนโมเดล |",
'| Qualified replies | 41/41 | เปลี่ยน ownership/context/ข้อกำหนดเพิ่มเติม; transport ที่ควบคุม |',
'| Rejection/replacement | 34/34 | เปลี่ยนคำถาม/ไม่ใช่/ยกเลิก/ข้อมูลรุ่นใหม่; transport ที่ควบคุม |','',
'51 คือเทิร์นที่มีเป้าหมายตรวจ ไม่ใช่ accuracy ของคำถามจริงทั้งหมด และไม่ใช่ full 20,554 requests ชุด fixtures ไม่ใช่ข้อมูลหรือราคาใหม่ของศูนย์','',
'## 1. สิ่งที่เชื่อมจริง','',
'### 1.1 ราคาเหมาและบทสนทนา','',
'rental_bridge ใช้ pure grammar helpers ของตัวราคาเหมาเดิม ได้แก่ _selection, _periods, _asks และสัญญาณภาษา/การปฏิเสธ แต่ catalog โซน กลุ่มหน่วยงาน ราคา จำนวนที่นั่ง อุปกรณ์ และ source pointers มาจาก common snapshot ปัจจุบัน','',
'เพิ่ม request_contract ใน common state โดยเก็บ requests ที่ผูก zones/audiences/periods ต่อ clause, asks และ context_used ไม่เก็บตัวเลขราคาใน state คำถาม “แล้วครึ่งวันล่ะ” เปลี่ยน period โดยรักษา PC/กลุ่มเดิม ส่วนการถามเลือก VR จากคำถามผสมรักษาเฉพาะ tuple ของ VR','',
'ไม่เรียก load_zone_rental_data/build_zone_rental_answer เพื่อสร้างคำตอบ ไม่ใช้ TARGETS หรือรายการราคาตายตัวของเดิมเป็นแหล่งข้อมูลใหม่ โซนที่เพิ่มใน DB จึงเข้ารายการจาก snapshot ได้โดยไม่เพิ่มชื่อในโค้ด','',
'### 1.2 Routing patterns เดิม','',
'legacy_intent_bridge ใช้ compiler ของ RuleMatcher และ priority/category จาก trusted legacy routing configuration เพื่อระบุ intent แล้ว map ผ่าน intent_key ไปยัง FAQ ปัจจุบันที่มี answer พร้อม source','',
'ใช้เฉพาะ pattern ที่ครอบคลุมข้อความสาระทั้งคำถามตาม grammar ที่กำหนด และมี record ปัจจุบันตรงเพียงรายการเดียว กรณีไม่ตรงหรือกำกวมยังใช้กลไกกลาง/ถามเพิ่ม ไม่ compile aliases ทุกช่องเป็น regex และไม่ใช้ answer จาก rules เก่ามาตอบ','',
'เมื่อได้แผน intent ที่ครอบคลุมแล้ว จะรักษาทั้ง record และ field=answer ไปจนจบ ไม่ให้ขั้นเลือก FAQ ทั่วไปด้านหลังเปลี่ยนเป็น walk-in หรือถามชื่อ field อีก','',
'นี่เป็น bridge ของ routing configuration เดิม ไม่ใช่การเพิ่ม alias รายคำถามใหม่ Owner content ใหม่ยังใช้ชื่อ/fields/query_profile ของ Format กลาง ไม่ต้องเขียน regex ทั้งนี้ยังไม่อ้างว่าทุก pattern เดิมถูกย้ายได้สมบูรณ์ เพราะบางอันไม่ครอบคลุมคำถาม/ไม่ unique/ไม่มี common intent ที่ผูกไว้','',
'### 1.3 รายการอุปกรณ์ตามโซน','',
'equipment_bridge รักษางาน “แสดงอุปกรณ์ในโซน” แล้วอ่านผ่าน relations/source zone grouping ที่มีจริง โดยใช้ named zone ที่ผู้ใช้ระบุ เมื่อ service ไม่มี resource_ids ที่ยืนยันได้จะไม่สร้าง FK เดา','',
'Nintendo Switch Zone ในชุดตรวจคืน OLED, TV86 และ Sofa ตาม source ปัจจุบัน พร้อมจำนวนที่มี source ไม่ส่ง field specifications/usage ที่ service root ไม่มีจน validation ล้ม','',
'### 1.4 ข้อมูลที่เคย unknown เพิ่มใหม่แล้วต้องอ่านได้','',
'ก่อนตอบ specific-unconfirmed ตรวจ source-backed record ปัจจุบันที่ประกาศ intent_key หรือ query_profile ของเรื่องนั้น หากมี source ตรงและอยู่ใน context จะให้เข้าสู่การเลือก/ยืนยันข้อมูลใหม่ได้ ไม่ปิดทางด้วยคำว่า wrong_amount/identity correction ที่เคย unknown','',
'fixture ยืนยันเพิ่มวิธีแก้ยอดเงินผิด → ถามด้วย paraphrase → ยืนยันหัวข้อ → อ่านคำตอบ V1; แก้เป็น V2 → ได้ V2; ถอน record → กลับเป็น unconfirmed โดยไม่มี V1/V2 ค้างในคำตอบ','',
'### 1.5 กฎแข่ง ปุ่ม และคำบรรยายเกม','',
'รักษาตัวเลือก facet/clause/control projection ที่ common reader เชื่อมใช้ไว้แล้ว ไม่ย้ายกลับไปอ่าน facts เก่า ทดสอบคำถาม RoV สรุปกติกา, CS2 ข้อประท้วง, Mario Party controls และ Animal Crossing คืออะไร ในชุดเว็บจริงผ่านเกณฑ์เนื้อหาที่กำหนด รอบนี้ไม่ได้เขียน renderer ใหม่ทั้งหมดของหมวดเหล่านี้','',
'## 2. Loop ที่ทำและข้อผิดพลาดที่เจอ','',
'1. Candidate 1 49/51: คำย่อ PS5 ไม่ตรง source label PlayStation 5 และ equipment catalog เลือก service root ที่ resource FK ยัง unknown','2. เพิ่มคำย่อจาก label รุ่นใน source และใช้ explicit named zone อ่าน equipment grouping แทนการเดา resource mapping','3. Candidate 2 ตามเกณฑ์แรกผ่าน 50/51 แต่พบ oracle “มีเลข 1” อ่อนเกิน เพราะ citation [S1] ก็ทำให้ผ่าน จึงแก้ให้ต้องมี 1 ชั่วโมง/1 hour จริง เก็บเกณฑ์และผลเก่าทั้งหมด ไม่ใช้คะแนนเกณฑ์อ่อนเป็นผลสำเร็จ','4. Candidate 3 50/51: เลือก booking_advance_time ถูกแล้ว แต่ขั้นถัดไปยังถามว่าต้องการ field ไหน เพราะไม่รักษา task→answer contract แก้การใช้แผนเดียวต่อจนจบ โดยมี whole-query pattern coverage ก่อนยอมรับ','5. Candidate 4 51/51 จากนั้นตรวจเพิ่มในฐานทดลอง: tuple selection, unknown PS6, เวลาเหมา 5 ชั่วโมงที่ไม่มีราคา, cancel, ไม่เอา VR และ validity unknown สถานะราคาไม่ถูกตั้งเป็น fully confirmed','6. ติดตั้งเฉพาะไฟล์ที่ตรวจ hash ตรง แล้ว restart เว็บที่ระบุตัวตนได้และตรวจ fingerprint ก่อนทดสอบ 51 เทิร์นจริง','',
'Fixture ครั้งแรกหยุดเพราะ helper จับ exception ของ “ยังไม่มี record” ไม่ตรง CommonStore.get (ValueError) เป็นปัญหาตัวทดสอบ แก้ helper และเก็บผล setup failure ไว้ ไม่ใช่คำตอบของ chatbot','',
'## 3. การเปรียบเทียบทุกเทิร์นในชุดเดียวกัน','',
'| ภาษา | คำถาม | ก่อน | เว็บหลังติดตั้ง |','|---|---|---|---|']
for a,z in zip(before,rows):
 assert a['question']==z['question']
 lines.append('| '+a['locale']+' | '+a['question'].replace('|','/')+' | '+('ผ่าน' if a['passed'] else ', '.join(a['errors']))+' | '+('ผ่าน' if z['passed'] else ', '.join(z['errors']))+' |')
lines+=['','## 4. เวลาและ model transport','',
f"- โมเดลสร้างคำตอบ preflight จริง: {web['real_model_generation_verified']}",
f"- Selector/model calls ที่นับใน query_plan: {web['model_calls']}; proposal calls {web['proposal_calls']}; model failure {len(web['model_failures'])}",
'- จำนวนนี้ไม่ใช่การนับ HTTP ทุกประเภทของทุก planner ในระบบ และการเปิด LLM ไม่ได้บังคับให้คำถามที่อ่าน source ตรงได้ต้องเรียกโมเดล','',
'| ภาษา | ผ่าน | มัธยฐาน HTTP วินาที |','|---|---:|---:|']
for lang,x in web['by_language'].items():lines.append(f"| {lang} | {x['passed']}/{x['count']} | {x['median_seconds']:.3f} |")
lines+=['','เป็นชุดเล็กหลังเตรียมโมเดล ไม่ใช่การรับประกัน latency/load capacity และไม่เทียบเป็น speedup benchmark กับภาระเครื่องของรอบก่อน','',
'## 5. ตัวอย่างคำตอบและความต่อเนื่อง','']
for case in ['th-rental-followup','en-rental-compound','th-routing-advance','equipment-switch']:
 for row in [x for x in rows if x['case']==case]:lines+=['### '+row['question'],'',row['body']['answer'],'']
lines+=['## 6. ขอบเขตที่ยังไม่ควรกล่าวว่าเสร็จทั้งหมด','',
'- เป็นการเชื่อมความสามารถที่ตรวจได้ในรอบนี้ ยังไม่ใช่ behavioral parity ทุก pattern/ทุกหมวดของ legacy ทุกคำถาม และยังไม่ใช่ production release approval','- ตัวยึด grammar/routing เดิมยังมีขอบเขต กรณีที่ไม่ครอบคลุมหรือหลาย intent ตรงกันยังต้องใช้ตัวกลาง/ถามเพิ่ม ไม่บังคับเอาคำตอบเดิมมาให้ได้ทุกครั้ง','- ยังไม่มี owner facts เรื่องจำนวนชั่วโมงครึ่งวัน/เต็มวัน ราคาเหมารายชั่วโมง ราคาชุดที่ปรับเอง ช่องทาง/มัดจำ/ยกเลิกแบบเหมา และวันมีผลของราคา ระบบจึงแจ้ง unknown อย่างจำเพาะ','- ไม่คำนวณส่วนลดรายวัน/หลายวัน/รายเครื่องเอง และไม่ถือ room_seats เป็นจำนวนผู้เล่นพร้อมกัน','- ไม่ได้ตรวจ WordPress live ground truth ใหม่หรือ load test หลายคน ความถูกต้องสดที่ผู้ใช้เคยยืนยันไม่ถูกแทนด้วย fixture รอบนี้','- ภาษาอังกฤษที่ source ระบุ agent_translated ยังไม่กลายเป็น owner-reviewed เพราะผ่าน automated tests','- ถ้าจะส่ง package ไปเครื่องอื่น ต้องใส่ routing configuration และ module dependencies ที่ interpreter ใช้ด้วย รอบนี้ติดตั้งเฉพาะระบบทดสอบ R78 ไม่ได้ rebuild portable packages ที่เคยแจก','',
'## 7. การรักษาข้อมูล','',
f"- แก้/เพิ่มโค้ด {len(installation['installed_files'])} ไฟล์ใน R78 เท่านั้น มี before/ และ candidate/ พร้อม CHANGESET.patch",
f"- ตรวจไฟล์ app/UI/routing เดิมอื่น {installation['other_application_ui_routing_files_unchanged']} ไฟล์ไม่เปลี่ยน",
'- DB เดิม SHA256 ยังเป็น `'+installation['database_sha256']+'`; ไม่มีการแก้ราคา/owner content/approvals/releases เพื่อผ่าน test','- Old rental parser/RuleMatcher source, strict binding validator และ compact opening module ไม่เปลี่ยน','- โครงการ Downloads, workbook และ log รอบก่อนยังอยู่ ผล fixtures แยกใน verification/ ของรอบนี้','',
'## หลักฐาน','',
'- FLOW_R87_TH.md และ BASELINE_MANIFEST.json','- CHANGESET.patch, SOURCE_INVENTORY_BEFORE.json, INSTALLATION.json','- verification/baseline_1/SUMMARY.json และ TURNS.jsonl','- verification/candidate_1..4/ พร้อมผลทุก attempt','- verification/fixture_release/SUMMARY.json และ CHECKS.jsonl (ข้อมูลทดลองเท่านั้น)','- verification/qualified_hardened/RESULTS.json และ rephrase_hardened/RESULTS.json','- เว็บจริง: '+str(W),'',
'เทสใหญ่ยังพักไว้จนกว่าผู้ใช้สั่งใหม่']
with (B/'REPORT_R87_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines)+'\n')
qa={'actual_web_summary':web,'installed_source_hashes_verified':True,'database_unchanged':True,'full_test_executed':False,'before_count':baseline['count'],'before_passed':baseline['passed'],'fixture_checks':fixture['count'],'fixture_passed':fixture['passed'],'report':str(B/'REPORT_R87_TH.md')}
with (B/'DELIVERY_QA.json').open('x',encoding='utf8') as f:json.dump(qa,f,ensure_ascii=False,indent=2)
print(json.dumps(qa,ensure_ascii=False))
