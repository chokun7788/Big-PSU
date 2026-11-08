"""Build the final delivery report from retained evidence, without rerunning tests."""
import hashlib,importlib.util,json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';W=Path(sys.argv[1]).resolve()
read=lambda p:json.loads(p.read_text(encoding='utf8'))
web=read(W/'SUMMARY.json');install=read(B/'INSTALLATION_2.json');fixture=read(B/'verification/fixture_release/SUMMARY.json');competition=read(B/'verification/competition_fixture_release/SUMMARY.json')
assert web['count']==web['expected_count']==web['passed']==55 and not web['model_failures'] and not web['obstacle']
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert all(digest(S/name)==sha for name,sha in install['installed_files'].items())
assert digest(S/'data/knowledge/common.sqlite')==install['database_sha256']
rows=[json.loads(line) for line in (W/'TURNS.jsonl').read_text(encoding='utf8').splitlines()]
baseline=[json.loads(line) for line in (B/'verification/baseline_1/TURNS.jsonl').read_text(encoding='utf8').splitlines()]
# Compare the same 51 archived questions using the retained V1 checker. The
# stronger competition checks and four new requests are reported separately.
spec=importlib.util.spec_from_file_location('retained_v1',B/'contracts_v1.py');v1=importlib.util.module_from_spec(spec);spec.loader.exec_module(v1)
lookup={(row['case'],row['question']):row for row in rows}
paired=[]
for old in baseline:
 new=lookup[(old['case'],old['question'])]
 paired.append({'case':old['case'],'question':old['question'],'locale':old['locale'],'before_passed':old['passed'],'after_passed_same_v1_check':not v1.check(new['body'],old['expect'])})
comparison={'count':len(paired),'before_passed':sum(x['before_passed'] for x in paired),'after_passed_same_v1_check':sum(x['after_passed_same_v1_check'] for x in paired),'same_saved_criteria':True,'new_legacy_run':False,'comparison_limit':'V1 competition oracle checks domain/keywords, not sufficient summary quality','pairs':paired}
with (B/'PAIRED_COMPARISON.json').open('x',encoding='utf8') as f:json.dump(comparison,f,ensure_ascii=False,indent=2)
lines=['# R87 ผลเชื่อม Flow เดิมเข้ากับข้อมูลกลาง','',
'## สถานะส่งมอบ','',
'ติดตั้งในแชททดสอบ R78 ที่ http://127.0.0.1:8115/ แล้ว ตรวจ API จริงหลัง restart และตรวจ loaded source fingerprint เปิด LLM และยืนยันการสร้างข้อความจากโมเดลจริงก่อนเริ่ม ข้อมูลยังเป็น migration draft 602 รายการ ไม่ได้สร้าง owner approval หรือเผยแพร่ production','',
'## 1. ผลตรวจที่แยกตามความหมาย','',
'| ชุด | ผ่าน | สิ่งที่พิสูจน์ |','|---|---:|---|',
f"| ก่อนแก้ R84: คำถามเป้าหมายเดิม | {comparison['before_passed']}/{comparison['count']} | ผลเก็บเดิม เปิด LLM ไม่รันก่อนแก้ซ้ำ |",
f"| หลังแก้: 51 เทิร์นเดียวกัน/เกณฑ์เดิม | {comparison['after_passed_same_v1_check']}/{comparison['count']} | ตรวจผลเว็บรอบล่าสุดด้วยเกณฑ์ V1 ที่เก็บไว้ |",
'| Candidate: เกณฑ์เข้มขึ้น + เพิ่มเคสกติกา | 55/55 | โมเดลจริงเปิด; ตรวจเนื้อหา ขอบเขต และหลายเทิร์น |',
f"| เว็บที่ติดตั้งจริง: เกณฑ์เข้มขึ้น | {web['passed']}/{web['count']} | HTTP จริง ผ่าน session และ common_read_state |",
f"| ฐานทดลองราคา/ข้อมูลใหม่ | {fixture['passed']}/{fixture['count']} | เพิ่ม แก้ ถอนข้อมูล และขอบเขต tuple; ควบคุม transport |",
f"| ฐานทดลองกติกา | {competition['passed']}/{competition['count']} | เปลี่ยน source เพิ่มข้อใหม่ ถอนข้อ และ block legacy loader |",
'| Qualified replies | 41/41 | regression ที่เกี่ยวข้องกับ ownership/context; ควบคุม transport |',
'| Rejection/replacement | 34/34 | ปฏิเสธ เปลี่ยนคำถาม และ context; ควบคุม transport |','',
'36→51 เป็นผลใน 51 เทิร์นเดิมตามเกณฑ์เดิม ไม่ใช่ accuracy ของผู้ใช้ทุกคน เกณฑ์กติกาเดิมอ่อนเกิน จึงมีการอ่านคำตอบและแก้ oracle เพิ่ม รายงานผล 55/55 แยกต่างหาก ไม่รวมจำนวนจากชุดซ้ำให้เป็นคะแนนใหญ่ และไม่อ้างว่า full test ผ่าน','',
'### ภาษาและโมเดล','',
'| ภาษา | เว็บผ่าน | มัธยฐาน HTTP (วินาที) |','|---|---:|---:|']
for lang,x in web['by_language'].items():lines.append(f"| {lang} | {x['passed']}/{x['count']} | {x['median_seconds']:.3f} |")
lines += ['',f"Preflight generation จริง: {web['real_model_generation_verified']}; selector calls ที่ query_plan นับ: {web['model_calls']}; proposal calls: {web['proposal_calls']}; model transport/selection failures ที่ตัวตรวจพบ: {len(web['model_failures'])}",'',
'เปิด LLM ไม่ได้บังคับให้ทุกคำถามเรียกโมเดล คำถามที่มี task contract ชัดอ่าน source ตรงได้ ส่วนที่กำกวมยังใช้ตัวเลือกของโมเดลพร้อมตรวจแผนและขอความชัดเจนตามเดิม ตัวเลขนี้ไม่ใช่จำนวน HTTP ทุกชนิด และเวลาชุดเล็กหลังเตรียมโมเดลไม่ใช่ load benchmark','',
'## 2. สิ่งที่แก้และเหตุผล','',
'### 2.1 ตีความเดิม แต่อ่านข้อเท็จจริงจากข้อมูลกลาง','',
'legacy_intent_bridge ใช้ compiler/priority/category/pattern จาก trusted routing configuration เดิม เฉพาะกรณีครอบคลุมสาระคำถามและ map ไป intent_key ปัจจุบันได้รายการเดียว ไม่อ่าน answer ของ RuleMatcher และไม่ compile owner aliases เป็น regex เอง เมื่อเลือก task แล้วรักษาทั้ง record และ field=answer จนจบ แก้กรณีต้องจองล่วงหน้ากี่ชั่วโมงที่เคยถูกเปลี่ยนเป็น walk-in/ถาม field อีก','',
'### 2.2 ราคาเหมาจ่ายและการถามต่อ','',
'rental_bridge ใช้ pure _selection/_periods/_asks ของเดิม แต่โซน กลุ่ม ราคา ที่นั่ง อุปกรณ์ และหลักฐานมาจาก snapshot กลาง เก็บ request_contract เป็น tuple ต่อ clause ไม่เก็บราคาใน history จึงถาม PC/ภายนอก/เต็มวัน → ครึ่งวัน → ภายใน ได้ และคำถามผสม PC/ภายนอก/เต็มวัน + VR/ภายใน/ครึ่งวันไม่จับเงื่อนไขข้ามฝั่ง','',
'ไม่ใช้ load_zone_rental_data/build_zone_rental_answer เป็นแหล่งคำตอบ ทดสอบแก้ราคาและโซนสมมุติ Aurora โดย block loader เก่าแล้ว ยังอ่านค่า revision ใหม่ได้ ถอนรายการแล้วไม่คืนค่าจาก history เงื่อนไข unknown รุ่น PS6, เหมา 5 ชั่วโมง, ชุดปรับเอง, รายชั่วโมง และขั้นตอนจองแบบเหมายังไม่ถูกเดาเป็นนโยบาย','',
'### 2.3 รายการอุปกรณ์','',
'equipment_bridge อ่านอุปกรณ์ผ่าน relations/source grouping ของโซนที่ถาม แก้ Nintendo Switch ที่เคยเลือก service root ซึ่งไม่มี resource FK ไม่สร้างความสัมพันธ์เดา OLED/TV86/Sofa และจำนวนมาจาก source ปัจจุบัน','',
'### 2.4 ข้อมูลใหม่แทนหัวข้อที่เคยไม่มี','',
'ก่อน specific-unconfirmed ตรวจ source-backed record ปัจจุบันที่ประกาศ intent_key/query_profile ว่าครอบคลุมคำถามหรือไม่ Fixture เพิ่มขั้นตอนแก้ยอดชำระเงิน → ยืนยันหัวข้อ → อ่าน V1 → แก้เป็น V2 → ถอนแล้วกลับเป็น unconfirmed ได้ ไม่แก้ข้อมูลศูนย์จริง และไม่ได้เอาวิธีแก้สลิปมาใช้กับการยืนยันตัวตน/ยอดเงิน','',
'### 2.5 สรุปกติกาและข้อประท้วง','',
'competition_bridge ใช้ pure clause/facet/detail predicates ของเดิม อ่านเฉพาะ competition_rule ปัจจุบันของ parent เล่มเดียว ไม่เรียก legacy overview/detail builders หรือ load_curated_rows สรุปเลือกข้อเต็มไม่เกิน 6 facet บอกว่าเป็นบางข้อ ไม่หั่นกลางเงื่อนไข ไม่เลือกบรรทัด “Occurrence 1: warning” ที่ขาดเหตุแห่งโทษ และแนบ dependency ถ้ามี ถ้าขอทั้งหมดจะกลับไปอ่านครบตาม source order','',
'ข้อประท้วงเลือก proposition ที่ตรงคำถาม จึงมีครบว่า 15 นาทีหลังจบแมตช์ และกัปตันหรือโค้ชเท่านั้น โดยไม่แถมทั้งหมวดภาษา/อำนาจตัดสิน หากถามภาษาเพิ่มต้องตอบด้วย ไม่ตัดคำถามเหลือข้อประท้วงเพียงอย่างเดียว','',
'English objection/protest เป็นถ้อยคำคนละแบบใน source กลาง จึงใช้ vocabulary สำหรับเลือก clause ร่วมกับ predicate เดิม ไม่ฝังตัวเลขหรือคำตอบลงโค้ด Fixture เปลี่ยน 15→23 เฉพาะฐานทดลอง แล้วตอบ 23 ทั้งไทย/อังกฤษได้ รวมทั้งเพิ่มข้ออุปกรณ์ใหม่และถอนข้อกติกาได้โดยไม่แก้ routing','',
'## 3. สิ่งที่พบระหว่าง loop และการแก้ตัวทดสอบ','',
'1. Candidate 1 49/51: PS5 ไม่ผูก source label PlayStation 5 และ equipment list เลือก root ผิด แก้คำย่อจากหมายเลขรุ่นใน label และใช้ named zone ที่มีจริง','2. Candidate 2 50/51 ตามเกณฑ์แรก แต่ oracle เลข 1 ยอมรับ [S1] จึงเปลี่ยนเป็นต้องมี “1 ชั่วโมง/1 hour” จริง เก็บผลเดิมไว้','3. Candidate 3 50/51: เลือก booking_advance_time ถูกแล้ว แต่ขั้น field/FAQ ด้านหลังเปลี่ยน task แก้การส่ง contract ให้ครบจน render; Candidate 4 51/51','4. เว็บครั้งแรก 51/51 แต่ manual source inspection พบ RoV สรุปยาว 2,729 ตัวอักษร และ CS2 ประท้วงยาว 1,417 ตัวอักษร เพราะตรวจเพียง domain/มี keyword จึงเพิ่ม oracle ความหลากหลายหัวข้อ ขอบเขต และข้อห้าม dump หัวข้ออื่น','5. competition_1 และ _2 ยังไม่รับ summary เพราะไม่ได้ใช้ derived acronym RoV; แก้ให้ใช้ derived_names เดียวกับตัวกลาง แก้ full-rules oracle ให้ตรวจ selected source IDs จริง ไม่ใช้ parent projection เป็นจำนวนข้อ','6. Fixture competition ครั้งแรกใช้ facet/source_order ผิด schema เป็น setup error; ไม่ลด validator ครั้งที่สองพบ English generic equipment ไม่ตรงศัพท์ predicate เก่า จึงใช้ singleton facet ที่ owner ระบุร่วมกับ clause predicate เพื่อรับ source ใหม่ โดยยังไม่ฝังคำตอบ','7. competition_fixture_release 7/7 และ Candidate release 55/55; ติดตั้งสองระยะ เก็บ before_stage2/CHANGESET_2.patch แล้วตรวจเว็บจริงใหม่ด้วย fingerprint ล่าสุด','',
'## 4. ตัวอย่างผลเว็บจริง','']
for case in ['th-rental-followup','rules-cs2','rules-cs2-en','rules-rov','rules-rov-en','th-routing-advance','equipment-switch']:
 for row in [x for x in rows if x['case']==case]:lines+=['### '+row['question'],'',row['body']['answer'],'']
lines+=['## 5. รายการคำถามที่ตรวจผ่าน API จริง','', '| ภาษา | คำถาม | ผล |','|---|---|---|']
for row in rows:lines.append('| '+row['locale']+' | '+row['question'].replace('|','/')+' | '+('ผ่าน' if row['passed'] else ', '.join(row['errors']))+' |')
lines+=['','## 6. ขอบเขตที่ยังต้องแยกจากผลอัตโนมัติ','',
'- ยังไม่ใช่การรับรองทุก pattern/ทุกหมวด/ทุก paraphrase เทียบ legacy ทั้งระบบ และไม่ได้รัน full corpus, legacy corpus หรือ LLM OFF รอบใหม่','- Routing bridge รับเฉพาะ coverage ที่ตรวจได้และ unique current intent; เคสที่อยู่นอกขอบเขตยังใช้ตัวกลางหรือถามเพิ่ม ไม่บังคับให้ตอบด้วยข้อเท็จจริงเก่า','- Competition bridge รอบนี้เน้นสรุปภาพรวมและข้อประท้วงที่ระบุได้ ส่วน proposition อื่นยังใช้ common selector เดิม ไม่อ้างว่า summary follow-up “ขออีก” หลายรอบผ่านครบทุกบริบท','- ยังไม่มีข้อมูลเจ้าของเรื่องจำนวนชั่วโมงครึ่งวัน/เต็มวัน ราคาเหมารายชั่วโมง ชุดปรับเอง หลายวัน และขั้นตอน/มัดจำ/ยกเลิกแบบเหมา รวมทั้งวันมีผลของราคา ระบบแจ้ง unknown เฉพาะเรื่อง ไม่หารราคาเองหรือแปลง room seats เป็นจำนวนผู้เล่นพร้อมกัน','- การตรวจภาษาอังกฤษอัตโนมัติไม่เปลี่ยน agent_translated เป็น owner-reviewed การอนุมัติความหมาย/นโยบายยังแยกต่างหาก','- ข้อมูลกลางยังเป็น draft preview ไม่ใช่ production approval; รอบนี้ไม่ได้ rebuild โฟลเดอร์ portable ที่แจกเครื่องอื่น ต้องใส่โมดูลและ routing dependencies ที่ใช้อยู่ให้ครบเมื่อแพ็กเกจรอบถัดไป','- ไม่ตรวจ WordPress live ground truth/load หลายคนใหม่ ความถูกต้องสถานะจริงที่ผู้ใช้เคยยืนยันยังแยกจาก fixture ของรอบนี้','',
'## 7. การรักษาไฟล์และหลักฐาน','',
f"แก้/เพิ่มโค้ด 6 ไฟล์ใน R78; ตรวจไฟล์ app/UI/routing อื่น {install['other_application_ui_routing_files_unchanged']} ไฟล์ไม่เปลี่ยน strict validator, compact opening และ legacy grammar/matcher source ไม่ถูกแก้",
'', 'ฐานความรู้เดิม SHA256: `'+install['database_sha256']+'` — ไม่แก้ราคา ข้อมูลเจ้าของ approvals หรือ releases เพื่อให้ผ่าน test โครงการ Downloads และ workbook ไม่ถูกแก้ เก็บ before/, before_stage2/, candidate/, logs และผลทุก attempt ไว้แยก','',
'หลักฐานในโฟลเดอร์นี้:','',
'- FLOW_R87_TH.md, BASELINE_MANIFEST.json','- INSTALLATION.json / INSTALLATION_2.json, CHANGESET.patch / CHANGESET_2.patch และ inventories ก่อนติดตั้ง','- PAIRED_COMPARISON.json: 51 เทิร์นเดียวกันจากผลที่มี ไม่รันเดิมซ้ำ','- verification/baseline_1, candidate_1..4, candidate_release','- verification/fixture_release (19/19), competition_fixture_release (7/7)','- verification/qualified_hardened และ rephrase_hardened','- ผล API ล่าสุด: '+str(W),'',
'**เทสใหญ่ยังพักไว้จนกว่าผู้ใช้สั่งใหม่**']
with (B/'REPORT_R87_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines)+'\n')
qa={'web':web,'paired_comparison':{k:v for k,v in comparison.items() if k!='pairs'},'source_hashes_verified':True,'database_unchanged':True,'full_test_executed':False,'production_publication_created':False,'fixture_checks':19,'competition_fixture_checks':7,'report':str(B/'REPORT_R87_TH.md')}
with (B/'DELIVERY_QA.json').open('x',encoding='utf8') as f:json.dump(qa,f,ensure_ascii=False,indent=2)
print(json.dumps(qa,ensure_ascii=False))
