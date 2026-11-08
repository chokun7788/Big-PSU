"""Build a reviewable report from retained runs; do not rewrite any run."""
from pathlib import Path
import ast,collections,difflib,hashlib,json
B=Path(__file__).resolve().parent
def read(tag):return [json.loads(s) for s in (B/'results'/tag/'ANSWERS.jsonl').read_text('utf8').splitlines()]
target0=read('baseline01');target=read('candidate_final');risk0=read('risk_baseline01');risk=read('risk_candidate01');held=read('holdout01');explore=read('exploratory03')
summary=[]
for name,rows in [('Target baseline',target0),('Target R72',target),('Risk baseline',risk0),('Risk R72',risk),('Holdout raw',held),('Exploratory safety',explore)]:
 summary.append({'name':name,'count':len(rows),'passed':sum(r['passed'] for r in rows),'locales':{lang:{'count':sum(r['locale']==lang for r in rows),'passed':sum(r['locale']==lang and r['passed'] for r in rows)} for lang in ['th','en']},'positive_content_contracts':sum(bool(r['need']) for r in rows),'safety_only_contracts':sum(not r['need'] for r in rows),'modes':dict(collections.Counter(r['mode'] for r in rows))})
adjudication={'run':'holdout01','index':11,'question':held[11]['question'],'raw_pass':held[11]['passed'],'raw_error':held[11]['errors'],'answer':held[11]['answer'],'source_text':held[11]['hits'][0]['text'],'finding':'Literal oracle expected อาคาร 5; actual source and answer say หน้าตึก 5, equivalent building location. Content correct in this case. Raw result retained.','agent_adjudicated_content_pass':True,'owner_or_human_approval':False}
(B/'HOLDOUT_ADJUDICATION.json').write_text(json.dumps(adjudication,ensure_ascii=False,indent=2),encoding='utf8')
manifest=json.loads((B/'BASELINE_MANIFEST.json').read_text('utf8'));src=Path(manifest['source']);altered=[];sqlite_auxiliary=[]
for row in manifest['files']:
 p=src/'system'/row['path']
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
  if row['path'].endswith(('.sqlite-shm','.sqlite-wal')):sqlite_auxiliary.append({'path':row['path'],'exists_now':p.exists(),'note':'SQLite transient auxiliary file; source connection close removes WAL/SHM. Do not restore stale WAL/SHM. Main DB hash is checked separately.'})
  else:altered.append(row['path'])
changed=[];diff=[];syntax_errors=[];files=[]
for p in sorted((B/'system').rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.suffix not in {'.py','.json','.html','.js','.css'}:continue
 rel=p.relative_to(B/'system');old=src/'system'/rel
 sha=hashlib.sha256(p.read_bytes()).hexdigest();files.append({'path':rel.as_posix(),'sha256':sha})
 if not old.exists() or hashlib.sha256(old.read_bytes()).hexdigest()!=sha:
  changed.append(rel.as_posix())
  if p.suffix in {'.py','.json','.html'}:
   diff.extend(difflib.unified_diff(old.read_text('utf8').splitlines(True) if old.exists() else [],p.read_text('utf8').splitlines(True),fromfile='R69/'+rel.as_posix(),tofile='R72/'+rel.as_posix()))
  if p.suffix=='.py':
   try:ast.parse(p.read_text('utf8'))
   except SyntaxError as e:syntax_errors.append(str(e))
  if p.suffix=='.json':json.loads(p.read_text('utf8'))
(B/'CHANGESET.patch').write_text(''.join(diff),encoding='utf8')
db=B/'system/data/knowledge/common.sqlite';dbhash=hashlib.sha256(db.read_bytes()).hexdigest()
dbsrc=next(r['sha256'] for r in manifest['files'] if r['path']=='data/knowledge/common.sqlite')
qa={'source_files_checked':len(manifest['files']),'source_content_files_changed':altered,'sqlite_transient_auxiliary_changes':sqlite_auxiliary,'candidate_changed_files':changed,'syntax_errors':syntax_errors,'database_sha256':dbhash,'database_matches_preserved_source':dbhash==dbsrc,'seed_matches_preserved_source':hashlib.sha256((B/'seed_R68_preserved.sqlite').read_bytes()).hexdigest()==hashlib.sha256((src/'seed_R68_preserved.sqlite').read_bytes()).hexdigest(),'candidate_manifest':files}
(B/'DELIVERY_QA.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2),encoding='utf8')
(B/'ANALYSIS_R72.json').write_text(json.dumps({'suites':summary,'holdout_agent_adjudication':adjudication,'exploratory_remaining':[{'question':r['question'],'answer':r['answer'],'mode':r['mode'],'safety_contract_passed':r['passed'],'source_answer_completeness_not_proven':True} for r in explore]},ensure_ascii=False,indent=2),encoding='utf8')
prefix='C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r72_flow_implementation_20261016/'
def link(label,path):return '['+label+']('+prefix+path+')'
lines=['# วิเคราะห์ผลการใช้ Flow และแก้ไข R72','', 'วันที่ 16 ตุลาคม 2026','',
 '## สรุปสถานะ','',
 'ปรับ Flow จาก R71 ตรวจความเสี่ยงสามรอบ แล้วลงมือแก้ในสำเนา R72 มีการรันทดสอบและตรวจคำตอบซ้ำจนพบข้อผิดพลาดที่ตัวตรวจอัตโนมัติชุดแรกยังจับไม่ครบ การแก้รอบนี้ทำให้กลุ่มปัญหาที่ตรวจเจาะจงดีขึ้น แต่ยังไม่ได้พิสูจน์ว่าทุกคำถามใน R70 หรือทุกข้อมูลใหม่จะตอบถูกทั้งหมด','',
 'เปิด LLM ทุกชุดที่รันในรอบนี้ ใช้เฉพาะ format กลาง การตอบจาก fields ไม่จำเป็นต้องเรียกโมเดล ส่วน model selector ที่พยายามเรียกจริงยังถูกปฏิเสธ socket ด้วย WinError 10013 หลังขอสิทธิ์เครือข่ายผ่านระบบแล้วยังไม่ได้รับ grant จึงไม่รับรอง model inference, browser/TCP หรือสถานะ WordPress จริงจากผลนี้','',
 link('Flow ที่ปรับและใช้ลงมือ','FLOW_R72_TH.md')+' · '+link('วิธีลองชุด R72','README_R72_TH.md')+' · '+link('ข้อมูลผลแบบเครื่องอ่าน','ANALYSIS_R72.json'),'',
 '## 1. เทียบก่อน/หลังโดยไม่รัน legacy','',
 'Baseline ในตารางคือแชท format กลาง R69 ก่อนแก้ ไม่ใช่ format เก่า legacy ใช้คำถาม ข้อมูล เวลาอ้างอิง และเกณฑ์เดียวกันกับ R72','',
 '| ชุด | ผ่าน/ทั้งหมด | ไทย | อังกฤษ | ความหมายของคะแนน |','|---|---:|---:|---:|---|']
for item in summary:
 loc=item['locales'];note='มีทั้งข้อกำหนดเนื้อหาและคู่ลบ' if 'Target' in item['name'] else 'ตรวจเนื้อหา/ขอบเขต/การไม่ยืนยันเกิน source ตามแต่ละเคส' if 'Risk' in item['name'] else 'มี false failure จากคำเทียบเท่า 1 รายการ' if 'Holdout' in item['name'] else 'ผ่าน safety contract ไม่เท่ากับตอบปัญหาได้ครบ'
 lines.append(f"| {item['name']} | {item['passed']}/{item['count']} | {loc['th']['passed']}/{loc['th']['count']} | {loc['en']['passed']}/{loc['en']['count']} | {note} |")
lines += ['', '**ห้ามนำคะแนนชุดเล็กนี้ไปเทียบเป็นเปอร์เซ็นต์รวมกับ R70 10,277 คำถาม** เพราะ corpus และเกณฑ์ต่างกัน ไม่มีการทดสอบ full suite ใหม่ในรอบนี้ และไม่ได้แก้ route/category เพื่อไล่คะแนน protocol เก่า','',
 'ชุด API สุดท้าย `verification/api_final/RESULTS.json` ผ่าน 46/46 (ตัวรับ HTTP จริงและ pipeline จริงแบบ memory connection) รวม 8 รายการบทสนทนาที่เพิ่มใหม่; ชุดแก้ร่างผ่าน `verification/updates_on01/RESULTS.json` 8/8; adversarial fixtures ผ่าน `results/fixtures02/RESULTS.json` 8/8 แต่ละชุดมีการตรวจชนิดต่างกัน จึงไม่รวมเป็นตัวเลข accuracy เดียว','',
 '## 2. Loop ที่ทำและผลที่พบจริง','',
 '| รอบ | ผล/สิ่งที่พบ | การแก้ |','|---|---|---|',
 '| ก่อนแก้ | Target 12/43 | เก็บคำตอบเต็มเป็น baseline |',
 '| รอบ 1 | 42/43; ไม่จ่าย…จะเป็นยังไง ดึงบัญชีเกินคำถาม | แยก consequence ออกจาก method |',
 '| รอบ 2 | 43/43; holdout raw 11/12 | ตรวจคำตอบเต็ม พบหน้าตึก 5 ถูก oracle นับผิด |',
 '| รอบ 3 | Risk จาก 5/18 เป็น 18/18; fixtures 8/8; API 46/46 | identity แบบล็อก hash, holiday-date clarification, missing-source, retrieval tail, follow-up |',
 '| รอบอ่านคำตอบเพิ่ม | when I paid wrong amount / transfer take to arrive ถูกตอบ 10 นาที | จำกัด deadline grammar และ exception scope |',
 '| รอบทบทวนตัวตรวจ | กัน 10 นาทีแล้ว แต่ผิดยอดยังตอบ booking steps; safety-only ให้ผ่าน | กัน payment exception ก่อน generic procedure เพิ่ม forbidden และเก็บผลเก่าทั้งหมด |','',
 'ผลของ exploratory02 ที่ raw ผ่าน 7/7 ไม่ใช่หลักฐานว่าทั้งหมดตอบถูก: จากการอ่านคำตอบจริง เคส wrong amount ยังได้ booking steps จึงแก้ต่อและเก็บ exploratory03 แยก ไม่แก้ผลเดิมย้อนหลัง','',
 '## 3. สาเหตุหลักและสิ่งที่แก้','',
 '### 3.1 เลือก source ถูกฐานแต่ผิดคำถาม','',
 '- เดิม `booking + pay` ถูกจับเป็น payment timeout ก่อนวิเคราะห์ how/when ทำให้ตัวตรวจเห็น field answer และ citation ครบทั้งที่ตอบ deadline แทนบัญชี',
 '- แก้ `request_roles.py` ให้แยก method/deadline/quota/studio_rules ก่อนเลือก facts โดยใช้ `intent_key` ที่มีอยู่ ไม่ใช้เลขบัญชี ราคา หรือ record ID เป็นคำตอบใน router',
 '- เพิ่ม request_needs, role_selection และ task_coverage แยกจาก selected-field validation; source_answer_rendered หมายถึงมี source ถูกนำมาแสดง ไม่ใช่รับรองความเข้าใจทุกบริบท','',
 '### 3.2 คำถามหลายส่วนถูกตัดเหลือ FAQ แรก','',
 '- เดิมเลือก candidates แล้วใช้ [:1] กับทั้งประโยค',
 '- แก้เลือกต่อ role และประกอบหลาย sources; ถ้าขาดหนึ่ง role ระบุ missing source และ partial_answer',
 '- คำถามข้ามหัวข้อ เช่น จ่ายยังไงและจอดรถที่ไหน ใช้ composition และมีสถานะของแต่ละส่วน',
 '- ยังไม่รับรอง compound ซับซ้อนทุกแบบ โดยเฉพาะ noun coordination หรือเงื่อนไขที่ grammar ยังไม่รู้จัก','',
 '### 3.3 ตัวตนเกมแยกเพราะ accent','',
 '- Ragnarök ตรง stub ที่มีแค่ title ส่วน Ragnarok ตรง detail ที่มี genre/วิธีเล่น',
 '- ตรวจชื่อเต็มทั้งสองและ summary ที่ระบุ Ragnarök จริง แล้วทำ read link เฉพาะ genre/summary/how_to_play ของคู่นี้ใน identity_links.json',
 '- ล็อก SHA256 ของระเบียนทั้งคู่ ถ้าเจ้าของแก้ revision/ถอน record จะหยุด link เอง fixtures ยืนยันว่าข้อมูลที่ถอนหรือเปลี่ยนเป็น unknown ไม่ถูกฟื้นกลับ',
 '- ไม่ merge ฐาน ไม่เชื่อม controls/platform/ราคา และไม่รับรอง alias ที่เป็นภาค/edition คนละตัว','',
 '### 3.4 วันหยุดที่ไม่ได้ระบุวัน','',
 '- เดิมมีเส้นทาง list closure เก่าแม้คำถามเป็นวันหยุดทั่วไป',
 '- เพิ่มขอวันที่ให้ชัดก่อนเช็ก exception ปฏิทิน ไม่เพิ่มวันปิดจากปฏิทินวันหยุดชาติ และไม่แตะกฎพัก 12–13/VR occupancy','',
 '### 3.5 ค้นข้อมูลช่วงท้ายไม่เจอ','',
 '- เดิมตัดข้อความ 1,800 ตัวก่อนคำนวณ candidate และ 650 ตัวแรกก่อนเข้าโมเดล ทำให้ tail หายตั้งแต่ต้น',
 '- ปรับ index ให้รวม known fields เต็ม แล้วเลือกหน้าต่างที่เกี่ยวข้องภายใต้ budget 650 ตัวต่อ candidate',
 '- Fixture ยืนยันว่า tail เข้า candidate และ model excerpt ได้ แต่ไม่ได้ยืนยันว่าโมเดลจริงเลือกถูก; topic guard ยังอาจปฏิเสธ record ที่หัวข้อคลุมเครือ ต้องทำ semantic metadata ต่อ','',
 '### 3.6 อังกฤษและบทสนทนา','',
 '- แยก retry/unavailable ตาม locale ไม่ให้ template ไทยปนอังกฤษโดยไม่จำเป็น; ชื่อบริการแปลงเฉพาะหน่วยตัวเลข นาที/ชั่วโมง ไม่แปลชื่อเฉพาะ',
 '- Follow-up And when?/แล้วเมื่อไหร่ สืบทอดหัวข้อจาก server state IDs และ metadata ปัจจุบัน แล้วเลือก source ใหม่ ไม่ใช้ข้อความคำตอบเดิมเป็น facts',
 '- ยังไม่ตรวจคำแปลทุก record โดยมนุษย์; สถานะ agent_translated ยังแสดงตามจริง','',
 '### 3.7 คำเมื่อ/when/how long ไม่ได้หมายถึง deadline เสมอ','',
 '- when I paid the wrong amount เป็นเงื่อนไขของปัญหา, transfer take to arrive เป็นเวลาที่เงินถึง ไม่ใช่เส้นตายจ่าย',
 '- จำกัด time grammar และกัน exceptional_payment ก่อน fallback ของ procedure; paid เดิมไม่อยู่ในตัวกรอง pay/payment ทำให้หลุดไป booking steps',
 '- หลังแก้ไม่ตอบ source คนละเรื่องแล้ว แต่คำถามพิเศษบางข้อยังเป็น retry/clarification เพราะเลือก source ผ่านโมเดลไม่ได้ ไม่ถือว่าแก้คำตอบครบแล้ว','',
 '## 4. คำตอบที่ยังไม่ครบจากชุดสำรวจ','',
 'ตารางนี้แสดงคำตอบจริงหลังแก้ล่าสุด ตัดเฉพาะเพื่ออ่านในรายงาน คำตอบเต็มและ trace อยู่ใน exploratory03/ANSWERS.jsonl ผ่าน forbidden contract หมายถึงไม่ตอบตามข้อผิดที่กำหนด ไม่ใช่ content completion','',
 '| คำถาม | ผลตอบ | ข้อจำกัด |','|---|---|---|']
for r in explore:
 ans=r['answer'].replace('\n',' ').replace('|','/')[:240]
 lines.append('| '+r['question'].replace('|','/')+' | '+r['mode']+' — '+ans+' | ต้องแยก safety pass จากการตอบครบ |')
lines += ['', '## 5. Holdout และความผิดของ oracle','',
 'Holdout เขียนก่อนเริ่มแก้ 12 ข้อ ผล raw 11/12; ข้อที่ไม่ผ่านถามที่จอดรถ คำตอบและ source ตรงกันว่า “หน้าตึก 5” แต่เกณฑ์รอ “อาคาร 5” ตรวจเทียบ source แล้วเป็นคำตอบที่ถูก จึงได้ agent-adjudicated content 12/12 โดยคง raw 11/12 ไว้ นี่ไม่ใช่ owner/human approval และไม่ใช่ held-out benchmark ภายนอกขนาดใหญ่','',
 link('หลักฐานวินิจฉัยเกณฑ์','HOLDOUT_ADJUDICATION.json'),'',
 '## 6. สิ่งที่ทดสอบผ่าน กับสิ่งที่ยังไม่ยืนยัน','',
 '| ประเด็น | หลักฐานอัตโนมัติ | ยังไม่ยืนยัน |','|---|---|---|',
 '| คำถามเป้าหมาย | Target/Risk พร้อม source contracts และคู่ลบ | ทุก paraphrase/ทุกข้อมูลใหม่ |',
 '| บริบทสองรอบ | actual handler เก็บ server state, ไทย/อังกฤษ | session จริงผ่าน browser/TCP |',
 '| แก้ข้อมูลเดิม | isolated DB บันทึก revision ใหม่ เก่าอยู่ epoch เปลี่ยน คำตอบอ่านค่ารุ่นใหม่ | owner กรอกใช้งานจริง/อนุมัติจริง |',
 '| สถานะจอง | fixture available/booked/unavailable ใน API suite | WordPress occupancy สดในรอบนี้ |',
 '| โมเดล | flag ON; selector พยายามเรียกจริง | generation/schema/semantic selection สำเร็จ |',
 '| ภาษาอังกฤษ | เคสที่ระบุและ locale templates | คำแปลทุกแถวโดยเจ้าของ |',
 '| เอกสาร/ข้อมูลเดิม | hash ตรวจไม่เปลี่ยน | factual approval ที่เดิมยังไม่มี |','',
 'MODEL_HEALTH ของ exploratory03 พบ common_entity_select ล้ม 2 ครั้ง successes=0 มี WinError 10013 ตรง error จริง สถานะ model-wide ok ที่ failures=0/successes=0 ไม่ใช่หลักฐานว่าโมเดลทำงานสำเร็จ เป็น bucket ที่ยังไม่มี probe ผ่าน','',
 link('หลักฐาน model transport','results/exploratory03/MODEL_HEALTH.json'),'',
 '## 7. งานคงเหลือเรียงตามผลกระทบ','',
 '1. ตรวจ real model generation/schema/semantic selection บนสภาพแวดล้อมที่อนุญาต socket แล้ว replay เฉพาะเคสที่พึ่งโมเดล ห้ามสรุปว่า model path ผ่านจาก flag ON',
 '2. ทำ semantic role/heading metadata และ owner form ให้ครอบคลุมหัวข้อใหม่ ไม่ต้องเพิ่ม alias/record ID ใน router; ขณะนี้เพิ่มเฉพาะสี่ role ที่พิสูจน์ปัญหาแล้ว',
 '3. เพิ่ม coverage ของเงื่อนไขพิเศษ เช่น โอนยอดผิด ระยะเงินถึง สิทธิ์ช่องทางจ่าย จำนวนคน การยกเลิกหลายส่วน ด้วย source ที่ตรงเรื่อง; source ไม่ชัดให้ถามเจาะจง',
 '4. ปรับ generic selector/field planner และ topic guard ให้ยอมรับ paraphrase ใหม่อย่างปลอดภัย โดยต้องมีผลโมเดลจริง ไม่ถอด guard เพื่อให้มีคำตอบเสมอ',
 '5. ทำ conflict/identity audit ที่เหลือตามหลักฐาน ห้าม auto merge ทั้งฐาน; คู่ที่ทำในรอบนี้มีเพียงหนึ่งคู่และสาม fields',
 '6. R71 งาน pagination ของกฎทั้งหมด/24 หมวด/production release ยังไม่ครบทุกข้อ คง backlog และการตรวจ browser/worker model จริงเป็น gate',
 '7. ข้อมูลที่เจ้าของยังไม่ยืนยัน เช่น validity ราคาหลังช่วงเดิม ระยะเหมา เงื่อนไขนโยบายบางข้อและคำแปลที่ต่างกัน ยังคงสถานะเดิม ไม่แก้โดยเดา','',
 '## 8. การรักษางานเดิมและสิ่งที่ส่งมอบ','',
 f"ตรวจ source manifest {qa['source_files_checked']} ไฟล์ เนื้อหาโค้ด/ข้อมูลเปลี่ยน {len(altered)} ไฟล์; ฐาน R72 เท่ากับต้นทาง: {qa['database_matches_preserved_source']}; seed เท่ากัน: {qa['seed_matches_preserved_source']}",
 '', f"พบไฟล์ SQLite ชั่วคราว WAL/SHM หายหลัง connection ปิด {len(sqlite_auxiliary)} รายการ แยกไว้ใน QA เป็น runtime auxiliary changes ไม่ใช่โค้ด/ข้อมูลถูกแก้ และไม่คืน WAL/SHM เก่าทับกลับเพราะอาจทำให้ฐานเสียหาย Hash ของไฟล์ฐานหลักเท่าเดิม", 
 '', 'SHA256 ฐานข้อมูล: `'+dbhash+'`','',
 'ระบบอ่าน 602 heads; approvals/active release ยังคงตาม baseline (API suite ตรวจจำนวน approvals=0 และ active ว่าง) ข้อมูลตัวอย่างอยู่ใน fixture แยก การแก้ทั้งหมดอยู่ในสำเนา R72 มี launcher แยกพอร์ต 8103/editor8104 ใช้ runtime R69 ที่มีอยู่ จึงเป็น working copy ที่ลองในเครื่องนี้ได้ ไม่ใช่ portable production package ใหม่','',
 link('QA และ manifest','DELIVERY_QA.json')+' · '+link('diff โค้ดจาก R69','CHANGESET.patch'),'',
 '### ไฟล์ที่เปลี่ยนในระบบ R72','']
lines += ['- `'+x+'`' for x in changed]
lines += ['', '### ข้อสรุป','', 'รอบนี้นำ Flow มาใช้จริงและแก้กลุ่มสาเหตุที่ตรวจพบพร้อมคู่ลบแล้ว ส่วนที่ยังตอบไม่ได้ถูกแยกไว้ตามหลักฐาน ผลชุดเล็กที่ผ่านไม่ได้แปลว่า production พร้อมทุกด้าน และไม่ใช่เหตุให้เปลี่ยนข้อมูลที่เจ้าของยังไม่ยืนยัน','']
(B/'REPORT_R72_TH.md').write_text('\n'.join(lines),encoding='utf8')
print(json.dumps({'source_changed':altered,'candidate_changed_files':len(changed),'syntax_errors':syntax_errors,'database_unchanged':qa['database_matches_preserved_source'],'suites':summary},ensure_ascii=False,indent=2))
