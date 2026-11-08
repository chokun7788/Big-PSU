"""Evidence-based delivery report; original records and run outputs stay intact."""
import ast,collections,difflib,hashlib,json,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
def load(name):return json.loads((B/name).read_text('utf8'))
def rows(tag):return [json.loads(s) for s in (B/'results'/tag/'ANSWERS.jsonl').read_text('utf8').splitlines()]
base=load('BASELINE_MANIFEST.json');src=Path(base['source']);source_changed=[]
for item in base['files']:
 p=src/'system'/item['path']
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:source_changed.append(item['path'])
def heads(path):
 c=sqlite3.connect(path.as_uri()+'?mode=ro',uri=True)
 try:
  records={rid:json.loads(payload) for rid,payload in c.execute('select h.record_id,r.payload from cc_heads h join cc_revisions r on r.record_id=h.record_id and r.version=h.head where h.withdrawn=0')}
  approvals=c.execute('select count(*) from cc_approvals').fetchone()[0];active=dict(c.execute('select key,value from cc_meta'))['active']
  revisions={(rid,v):hashlib.sha256(p.encode()).hexdigest() for rid,v,p in c.execute('select record_id,version,payload from cc_revisions')}
  return records,approvals,active,revisions
 finally:c.close()
old,oldapprovals,oldactive,oldrevs=heads(src/'system/data/knowledge/common.sqlite')
new,approvals,active,newrevs=heads(B/'system/data/knowledge/common.sqlite')
fact_changes=[];meta_changes=[]
for rid,r in old.items():
 after=new.get(rid)
 if after is None or {k:v for k,v in after['fields'].items() if k!='query_profile'}!={k:v for k,v in r['fields'].items() if k!='query_profile'}:fact_changes.append(rid)
 if after and after['fields'].get('query_profile')!=r['fields'].get('query_profile'):meta_changes.append(rid)
history_changed=[str(k) for k,v in oldrevs.items() if newrevs.get(k)!=v]
changed=[];syntax=[];manifest=[];diff=[]
for p in sorted((B/'system').rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.suffix not in {'.py','.json','.html','.js','.css'}:continue
 rel=p.relative_to(B/'system');previous=src/'system'/rel;sha=hashlib.sha256(p.read_bytes()).hexdigest();manifest.append({'path':rel.as_posix(),'sha256':sha})
 if not previous.is_file() or hashlib.sha256(previous.read_bytes()).hexdigest()!=sha:
  changed.append(rel.as_posix())
  if p.suffix=='.py':
   try:ast.parse(p.read_text('utf8'))
   except SyntaxError as e:syntax.append(str(e))
  if p.suffix=='.json':json.loads(p.read_text('utf8'))
  if p.suffix in {'.py','.js','.json','.html'}:diff.extend(difflib.unified_diff(previous.read_text('utf8').splitlines(True) if previous.is_file() else [],p.read_text('utf8').splitlines(True),fromfile='R72/'+rel.as_posix(),tofile='R73/'+rel.as_posix()))
qa={'source_files_checked':len(base['files']),'source_content_files_changed':source_changed,'head_count_old':len(old),'head_count_new':len(new),'factual_fields_changed':fact_changes,'routing_metadata_changed_records':meta_changes,'existing_revision_payloads_changed':history_changed,'approvals_before':oldapprovals,'approvals_after':approvals,'active_before':oldactive,'active_after':active,'syntax_errors':syntax,'changed_code_schema_ui_files':changed,'manifest':manifest,'database_sha256':hashlib.sha256((B/'system/data/knowledge/common.sqlite').read_bytes()).hexdigest(),'source_database_sha256':hashlib.sha256((src/'system/data/knowledge/common.sqlite').read_bytes()).hexdigest()}
assert not source_changed and not fact_changes and not history_changed and not syntax and len(new)==602 and approvals==oldapprovals==0 and active==oldactive==''
(B/'DELIVERY_QA.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2),encoding='utf8')
(B/'CHANGESET.patch').write_text(''.join(diff),encoding='utf8')
stats=[]
for tag in ['scope_baseline01','scope01','scope02','scope03','scope_final','ownership02','regression01','unseen01','unseen02']:
 rr=rows(tag);stats.append({'tag':tag,'count':len(rr),'passed':sum(r['passed'] for r in rr),'locales':{lang:{'total':sum(r['locale']==lang for r in rr),'passed':sum(r['passed'] and r['locale']==lang for r in rr)} for lang in ['th','en']},'modes':dict(collections.Counter(r['mode'] for r in rr)),'failures':[{'question':r['question'],'answer':r['answer'],'errors':r['errors'],'artifact':r['artifact']} for r in rr if not r['passed']]})
scope=rows('scope_final');groups=[]
for group in dict.fromkeys(r['group'] for r in scope):
 gg=[r for r in scope if r['group']==group];groups.append({'group':group,'total':len(gg),'passed':sum(r['passed'] for r in gg),'type':'safety_scope' if group in {'negative_scope','unknown_extra_object'} else 'unconfirmed_topic' if group in {'wrong_amount','overpayment','underpayment','installments','processing','age'} else 'source_content'})
api=load('verification/api01/RESULTS.json');fixtures=load('verification/profiles02/RESULTS.json')
analysis={'runs':stats,'scope_groups':groups,'api':{'count':api['cases'],'passed':api['passed']},'fixtures':{'count':fixtures['cases'],'passed':fixtures['passed']},'real_model_inference_verified':False,'owner_policies_decided_by_agent':False}
(B/'ANALYSIS_R73.json').write_text(json.dumps(analysis,ensure_ascii=False,indent=2),encoding='utf8')
prefix='C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r73_scope_completion_20261016/'
def link(label,path):return '['+label+']('+prefix+path+')'
lines=['# ผลพัฒนาต่อจาก R72 — R73','', '## สรุป','',
 'ลงมือแก้การเลือกคำตอบที่มี source ชัดอยู่แล้ว เพิ่ม optional query_profile สำหรับ FAQ/policy/procedure และปรับคำตอบที่ยังยืนยันนโยบายไม่ได้ให้ตรงเรื่อง ทดสอบเฉพาะ format กลาง เปิด LLM ทุกชุด ไม่รัน full/legacy/OFF','',
 '**ผลชุดหลัก 50 ข้อ: R72 7/50 → R73 50/50** แต่ 50 ข้อนี้ประกอบด้วยคำตอบจาก source, การแจ้งว่ายังยืนยันไม่ได้ และคู่ลบด้าน scope จึงไม่ใช่ accuracy ของทุกคำถามหรือทุกข้อมูลใหม่','',
 'ชุดถ้อยคำใหม่อีก 8 ข้อได้ 6/8 ก่อนปรับ และ 7/8 หลังปรับ ยังเหลือ 1 คำถามที่ใช้ proof of payment แทน slip การแก้ในรอบนี้ทำให้ procedure ที่ถูกเข้าชุด candidate แล้ว แต่ยังยืนยัน end-to-end ไม่ได้เพราะ socket เรียกโมเดลถูกปฏิเสธและ field planner ยังต้องตรวจแผนจริง การเพิ่ม candidate ไม่ถูกนับเป็นคำตอบที่ถูก','',
 link('Flow ที่ใช้และปรับจากผลจริง','FLOW_R73_TH.md')+' · '+link('วิธีเปิดและตัวอย่างกรอก','README_R73_TH.md')+' · '+link('ข้อมูลผลและ failures','ANALYSIS_R73.json'),'',
 '## 1. สิ่งที่เปลี่ยน','',
 '### 1.1 เลือกจาก metadata แทนการเพิ่มรหัสรายการใน router','',
 '- เพิ่ม query_profile แบบ optional ใน FAQ/policy/procedure: task, subjects ไทย/อังกฤษ, ownership และ context',
 '- รองรับสอง task: ถามสิทธิ์ใช้/นำมา และถามวิธีแก้สิ่งที่ผิด ไม่ได้อ้างว่าครอบคลุมทุกคำถามทุกหมวด',
 '- selector ใช้ task + subject + ownership + context ไม่อ่าน policy value จากโค้ด ถ้ามี profile ตรงกันหลายชิ้นจะถามเพิ่ม',
 '- metadata ไม่แสดงในคำตอบ “ทั้งหมด” และไม่ให้ field planner เลือกเป็นเนื้อหาคำตอบ',
 '- บันทึก metadata ให้เพียง 2 copied records ที่ตรวจชื่อ/คำตอบ/steps แล้ว: personal keyboard/mouse และ wrong slip ข้อเท็จจริงทุก field เดิมเท่ากันกับ R72 ไม่มี owner approval ใหม่','',
 '### 1.2 ให้คำตอบตาม source ที่มี','',
 '- “Can I bring my own keyboard?” / “เอาเมาส์ส่วนตัวมาใช้ได้ไหม” อ่านคำตอบห้ามนำอุปกรณ์ส่วนตัวมาใช้จาก FAQ เจ้าของเดิม',
 '- “I uploaded the wrong slip…” / “ส่งสลิปผิดไปแล้ว…” อ่านขั้นตอนและเพจจาก procedure เดิม',
 '- ภายในคำถามผสม เช่น วิธีจ่าย + keyboard / สลิปผิด / ผ่อนจ่าย แยกอ่านและแสดงสถานะแต่ละส่วน',
 '- preconditions ที่เป็นรหัส issue แสดงชื่อสถานการณ์จาก source ให้คนอ่าน โดยยังคงหลักฐาน/เงื่อนไขเดิมใน trace','',
 '### 1.3 ตอบตรงเรื่องเมื่อยังยืนยันไม่ได้','',
 '- โอนเกิน/โอนขาด/ยอดผิด/ผ่อน/ระยะเงินถึง/อายุผู้ใช้ แจ้งข้อจำกัดเฉพาะเรื่อง พร้อมเพจศูนย์จาก contact record จริง',
 '- ถ้าระบุเพียงยอดผิด ถามว่าเกินหรือขาด และไม่รับปากคืนเงิน/แก้รายการ/ให้โอนเพิ่มเอง',
 '- สถานะ unconfirmed ไม่ใช่ no_data ทั้งฐาน และไม่ใช่การอนุญาต/ห้าม เป็นสิ่งที่ข้อมูลซึ่งอ่านได้ยังยืนยันไม่ได้',
 '- การตรวจรูปแบบคำถามไม่ได้เติมคำตอบของเจ้าของลงไป คำถามให้เจ้าของตัดสินใจแยกไว้ท้ายรายงาน','',
 '### 1.4 ฟอร์มเจ้าของ','',
 '- เพิ่มชื่อช่อง ตัวเลือก และตัวอย่างเป็นภาษาคน กรอกเรื่องไทย/อังกฤษทีละแถว ไม่ต้องเขียนคำถามทุกประโยค',
 '- ข้อมูลเก่าที่ไม่มี field ใหม่ยัง validate ได้ และเมื่อเปิดใน editor ให้ unknown envelope ที่ถูก schema',
 '- ทดสอบ widget จริงด้วย DOM adapter ได้ 3/3 เป็นการตรวจค่าที่กรอก/ข้อความช่วย ไม่ใช่ visual/browser certification','',
 '## 2. ผลทดสอบแยกรอบ','',
 '| ชุด | ผ่าน/ทั้งหมด | ไทย | อังกฤษ |','|---|---:|---:|---:|']
for s in stats:
 th=s['locales']['th'];en=s['locales']['en'];lines.append(f"| {s['tag']} | {s['passed']}/{s['count']} | {th['passed']}/{th['total']} | {en['passed']}/{en['total']} |")
lines += ['', f"- Actual HTTP handler + pipeline แบบ connection ใน memory: **{api['passed']}/{api['cases']}** รวมบริบทสองรอบ ราคา เกม กฎ source ใหม่ที่ผูก profile และ live fixture", f"- เพิ่ม subject/ID ใหม่ แก้ revision ถอนข้อมูล conflict และ schema ใน SQLite fixture แยก: **{fixtures['passed']}/{fixtures['cases']}**",'- Candidate recall + ไม่ตอบเองเมื่อ noun ไม่ตรง: **2/2**', '- Owner editor widget: **3/3**; syntax JavaScript/PowerShell ผ่าน', '',
 'ไม่รวมผลทั้งหมดเป็น accuracy เดียว เพราะมีทั้งคำถาม ข้อกำหนดเนื้อหา fixture assertions และการตรวจ protocol ทดสอบ API แบบ memory ไม่ใช่ TCP/browser จริงหรือ WordPress สด','',
 '### องค์ประกอบชุด 50 ข้อ','', '| กลุ่ม | ผ่าน/ทั้งหมด | ประเภทเกณฑ์ |','|---|---:|---|']
for g in groups:lines.append(f"| {g['group']} | {g['passed']}/{g['total']} | {g['type']} |")
lines += ['', 'เกณฑ์ source_content ตรวจเนื้อหาและ source record จริง ไม่ใช้เพียงห้ามตอบข้อความเดิม เกณฑ์ unconfirmed ตรวจว่าระบุเรื่องที่ยังยืนยันไม่ได้ถูก พร้อมไม่รับปาก policy ส่วน safety_scope กันการเลือกข้อมูลผิดเรื่อง แต่ไม่ได้รับรองคำตอบเต็มของเรื่องอื่น','',
 '## 3. สิ่งที่ผิดระหว่างทำ และสาเหตุ','',
 '| จุดผิด | สาเหตุใน flow | สิ่งที่ปรับ |','|---|---|---|',
 '| ส่งสลิปผิดไปแล้วต้องทำอย่างไร | semantic_clauses แยก “แล้ว” แล้วคิดว่าส่วนท้ายเป็นสิ่งของอีกชิ้น | ตรวจ coordinated objects เฉพาะ และ/and แยก temporal connective |',
 '| โอนเงินกี่วันถึงบัญชี | alias โอนเงินเลือก FAQ ธนาคาร แม้ duration ไม่อยู่ใน source | เก็บ rejected scope plan และตอบ unconfirmed เฉพาะ processing แทน candidate ผิด รวมในคำถามผสม |',
 '| วิธีจ่าย + ผ่อน/สลิปผิด | exception ทั้งประโยคปิด role วิธีจ่ายก่อน composition | แยก independently requested tasks ก่อน filter ของแต่ละส่วน |',
 '| minimum age and guardian | ถูกแยกเป็นสอง unknown ซ้ำกัน แล้ว mode partial ผิด need เดียว | รวมเมื่อทั้งสองส่วนเป็น unconfirmed topic เดียว |',
 '| my booking กับ studio keyboard | personal เคยจับ my จากบริบทอื่น | ผูก my กับ subject และกัน studio-owned noun |',
 '| ซื้อ/ทำความสะอาด keyboard | can I อย่างเดียวไม่พิสูจน์ว่าเป็นสิทธิ์นำมาใช้ | permission task ใช้ action ที่ตรง use/bring/allowed ไม่ใช้ can I ทั่วไป |',
 '| แก้ข้อมูลเก่าหลังเพิ่ม optional field | editor สร้าง unknown note ว่าง ซึ่งไม่ผ่าน schema | default unknown envelope มี note ที่ถูกต้อง |',
 '| payment was too low | classifier รู้ underpaid/โอนขาด แต่ไม่รู้การเปรียบเทียบยอด | เพิ่ม semantic comparator low/high ภายใต้ payment/amount anchor; ยังคง unknown policy |',
 '| proof of payment | noun ไม่ตรง slip และ record ถูกตัดออกจาก candidates | เพิ่ม declared task เป็น recall backstop อย่างเดียว ห้ามตอบอัตโนมัติเมื่อ subject ไม่ตรง |','',
 'ความล้มเหลวของตัว fixture runner ครั้งแรกเกิดจากการเรียก get() บน ID ที่ยังไม่มี ซึ่งยก ValueError แก้เฉพาะ harness และเก็บโฟลเดอร์ profiles01 เดิมไว้ ไม่ใช่ production routing defect และไม่ใช้ผลที่รันไม่จบเป็นผลผ่าน','',
 '## 4. คำถามที่ยังไม่ผ่านจริง','']
for failure in next(s for s in stats if s['tag']=='unseen02')['failures']:
 lines+=['### '+failure['question'],'','- ควรตอบ: วิธีแก้แนบหลักฐานชำระผิดตาม procedure_wrong_slip และเพจศูนย์','- คำตอบจริง: '+failure['answer'],'- Stage ที่พบ: direct query_profile ไม่มี subject ตรง; recall backstop เพิ่ม procedure ถูกเข้าชุด candidate แล้ว; model selector เรียกไม่ได้ (transport ไม่สำเร็จ)','- ก่อนแก้ recall มีเพียง group check-in / CS2 ซึ่งไม่ใช่ข้อมูลที่ต้องการ จึงไม่ใช่ปัญหาโมเดลอย่างเดียว','- ยังต้องตรวจ semantic selection และ field planner เมื่อโมเดลเรียกได้จริง ไม่เพิ่ม alias ของประโยคทดสอบเพื่อทำให้คะแนนดูผ่าน','']
lines += ['## 5. Source/data preservation','',
 f"ตรวจไฟล์เนื้อหาต้นทาง R72 {qa['source_files_checked']} ไฟล์ เปลี่ยน {len(source_changed)} ไฟล์; heads เดิม/ใหม่ {len(old)}/{len(new)}; factual fields เปลี่ยน {len(fact_changes)} รายการ; immutable revision payload เดิมเปลี่ยน {len(history_changed)} รายการ",'',
 'R73 มี metadata field เพิ่มใน 2 ระเบียนและมี 2 revisions ใหม่ตาม audit จึงมี database hash ใหม่ตามคาด ไม่ได้อ้างว่า DB byte hash เท่า R72 แต่ค่าข้อเท็จจริง หลักฐานเดิม ราคา นโยบาย และ validity เท่าเดิมทั้งหมด', '',
 '- R72 database SHA256: `'+qa['source_database_sha256']+'`','- R73 database SHA256: `'+qa['database_sha256']+'`',f"- Approvals เดิม/ใหม่: {oldapprovals}/{approvals}; active release เดิม/ใหม่: ว่าง/ว่าง",'',
 link('Audit metadata ก่อน/หลัง','PROFILE_MIGRATION_AUDIT.json')+' · '+link('QA และ manifest','DELIVERY_QA.json')+' · '+link('Diff โค้ด/ฟอร์ม/schema','CHANGESET.patch'),'',
 '## 6. สิ่งที่ยังไม่ได้ยืนยัน','',
 '1. Real model inference/schema/semantic selection: เปิด LLM และมี actual attempts แต่ยัง WinError 10013 หลังขอสิทธิ์ผ่านระบบ ไม่มี success จากการสร้างคำตอบของโมเดลในรอบนี้',
 '2. Generic paraphrase ที่เปลี่ยน concept noun/เงื่อนไขซับซ้อน ยังต้องทำ planner/metadata ต่อ พร้อมโมเดลจริง ไม่ถือว่า profile สอง task แก้ครบทุกหมวด',
 '3. นโยบายโอนเกิน/ขาด ผ่อน ระยะเงินถึง และอายุ ยังต้องเจ้าของตัดสินใจ ไม่มี policy ใหม่ที่ agent ตัดสินแทน',
 '4. ข้อมูลร่าง คำแปลเดิมที่ยังไม่ผ่านเจ้าของ และ source ambiguity อื่นยังมีสถานะเดิม',
 '5. Browser/TCP/WordPress สดและ production publication gate ยังไม่ได้รับรองจากรอบนี้; live เป็น fixture ที่รู้ผลเท่านั้น',
 '6. query_profile ช่วยความแม่นเมื่อ metadata/เนื้อหากรอกตรง ไม่สามารถรับรองข้อมูลที่กรอกขัดกันหรือย้าย scope ผิดได้โดยอัตโนมัติทุกสถานการณ์','',
 link('คำถามเฉพาะที่ให้เจ้าของตอบ','OWNER_QUESTIONS_R73_TH.md'),'',
 '## 7. วิธีลองและ rollback','',
 'เปิด Open-New-Chat.cmd ของ R73 → พอร์ต8105 ป้ายR73 ใช้ runtime จาก R69 ข้างกัน เปิด editor ที่8106 เก็บ log/state และ DB ใน R73 ของตัวเอง',
 'กลับชุดก่อนหน้าโดยปิด R73 ด้วย Stop-New-Chat.cmd ของ R73 แล้วเปิด launcher R72 เดิม ข้อมูลของแต่ละสำเนาแยกกัน หากแก้ข้อมูลผ่าน editor ต้องเลือกสำเนาให้ถูก', '',
 'นี่เป็น working copy สำหรับลองบนเครื่องนี้ ยังไม่ได้แทนแพ็กเกจ production/portable เดิมโดยอัตโนมัติ','']
(B/'REPORT_R73_TH.md').write_text('\n'.join(lines),encoding='utf8')
print(json.dumps({'source_changed':source_changed,'factual_fields_changed':fact_changes,'metadata_changed':meta_changes,'preserved_history':not history_changed,'stats':[{k:v for k,v in s.items() if k not in {'failures','modes'}} for s in stats]},ensure_ascii=False,indent=2))
