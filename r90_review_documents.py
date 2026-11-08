"""Document-only review, link checks and immutable-source verification."""
import collections,hashlib,json,re,sqlite3
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent;R=B/'r90_full_flow_analysis_20261018'
primary=[R/'README_TH.md']+sorted(R.glob('0[1-6]_*.md'))
assert len(primary)==7,len(primary)
# Improve prose boundaries, preserving quoted answers, JSON, inline code and link targets.
replacements={
'field-plannerfinalaccepted':'field-planner final accepted',
'schemaผ่าน':'schema ผ่าน','finalรับ':'final รับ','validityunknown':'validity unknown',
'literal23':'literal 23','positivecontract12':'positive contract 12',
'HTTPsessionhead-to-head':'HTTP session head-to-head','modelHTTP':'model HTTP',
'Sourcehashes':'Source hashes','sourceepoch':'source epoch',
'schemafieldmenu':'schema field menu','exactsubject':'exact subject',
'typedfieldrefs':'typed field refs','taskcontract':'task contract',
'sourcecontract':'source contract','needcontract':'need contract',
'source-lineageanalysis':'source-lineage analysis','confidence_calibratedFalse':'confidence_calibrated=False',
'Positivepaired':'Positive paired','Positive literalตัวตรวจ':'Positive literal ตัวตรวจ',
'raw-failedrequests':'raw-failed requests','knownneed':'known need',
'samecriteria/samekeys':'same criteria / same keys','perclause':'per clause',
'strongneeds':'strong needs','extrasunaskedfields':'extra unasked fields',
'newdata-onlyfixtures':'new data-only fixtures','sharednormalization':'shared normalization',
'relationprojection':'relation projection','qualifiedfollowup':'qualified follow-up',
'guardvalidation':'guard validation','source-lineageanalysis':'source-lineage analysis',
'packagemanifest':'package manifest','taskstate':'task state','scopePC':'scope PC',
'readcontract':'read contract','sourceversion':'source version','sourcepointer':'source pointer',
'recordใหม่visible':'record ใหม่ visible','productionapproval':'production approval',
'beforeearlyreturn':'before early return','sourcefields':'source fields',
'wording/protocol/testfixture':'wording / protocol / test fixture',
'schema/transport/semantic/source/ownerapproval':'schema / transport / semantic / source / owner approval',
'ทุกpositive':'ทุก positive','semanticswrong':'semantics wrong',
}
changed=[]
for p in primary:
 old=p.read_text('utf8');out=[];fenced=False
 for line in old.splitlines(keepends=True):
  if line.lstrip().startswith('```'):fenced=not fenced;out.append(line);continue
  if fenced:out.append(line);continue
  # Keep code spans and markdown destinations exactly as written.
  chunks=re.split(r'(`[^`]*`|\]\([^\n]*?\))',line)
  for i,s in enumerate(chunks):
   if i%2:continue
   for a,b in replacements.items():s=s.replace(a,b)
   s=re.sub(r'(?<=[\u0e00-\u0e7f])(?=[A-Za-z0-9])',' ',s)
   s=re.sub(r'(?<=[A-Za-z0-9])(?=[\u0e00-\u0e7f])',' ',s)
   s=re.sub(r'(?<=\d)(?=requests\b|records\b|events\b|calls\b|checks\b|grades\b|fields\b|objects\b|clauses\b)',' ',s)
   chunks[i]=s
  out.append(''.join(chunks))
 new=''.join(out)
 if old!=new:p.write_text(new,'utf8');changed.append(p.name)
manifest=json.loads((R/'SOURCE_MANIFEST.json').read_text('utf8'));source_checks={};source_errors=[]
for mode,root in manifest['roots'].items():
 checked=0
 for rel,expected in manifest['files'][mode].items():
  p=Path(root)/rel;actual=hashlib.sha256(p.read_bytes()).hexdigest();checked+=1
  if actual!=expected:source_errors.append(str(p))
 source_checks[mode]={'python_source_files_checked':checked,'changed':sum(1 for s in source_errors if str(root) in s)}
assert not source_errors,source_errors
# Check installed application still matches frozen R88 app sources.
installed=B/'r78_web_session_check_20261016/system';parity=[]
for rel,expected in manifest['files']['common'].items():
 p=installed/rel
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:parity.append(rel)
dbs={}
for root in [Path(manifest['roots']['common']),installed]:
 p=root/'data/knowledge/common.sqlite';dbs[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
assert len(set(dbs.values()))==1,dbs
assert next(iter(dbs.values()))=='4bffab309215faca927e5ef8477944659558f3bcfe7b8e1c0faccad12953cd0d',dbs
links=0;errors=[];fences={};linecache={}
for p in primary:
 s=p.read_text('utf8');fences[p.name]=s.count('```');assert fences[p.name]%2==0,p
 for target in re.findall(r'\]\(([^\n]*?)\)',s):
  if target.startswith(('https://','http://','#')):continue
  path=re.sub(r':\d+$','',target);path=path.strip('<>');q=Path(path);links+=1
  # Review report is generated below.
  if q.name in ['DOCUMENT_REVIEW.md','DELIVERY_QA.json'] and q.parent==R:continue
  if not q.is_file():errors.append({'document':p.name,'target':target,'reason':'missing file'});continue
  m=re.search(r':(\d+)$',target)
  if m:
   if path not in linecache:linecache[path]=len(q.read_text('utf-8-sig').splitlines())
   if not 1<=int(m.group(1))<=linecache[path]:errors.append({'document':p.name,'target':target,'reason':'line out of range'})
assert not errors,errors
catalog=json.loads((R/'PROBLEM_CATALOG_REVIEWED.json').read_text('utf8'));assert len(catalog)==37
assert len(re.findall(r'^### P\d\d ',(R/'03_PROBLEM_ANALYSIS_ALL_TH.md').read_text('utf8'),re.M))==37
inventory=json.loads((R/'DATA_INVENTORY.json').read_text('utf8'));assert sum(inventory['inventory']['by_kind'].values())==602
assert len(inventory['missing_en_known_values'])==11 and len(inventory['conflicts'])==5
counts={}
for name,expected in [('COMMON_FAILURE_INDEX_ALL.md',18824),('LEGACY_FAILURE_INDEX_ALL.md',5689)]:
 n=sum(1 for l in (R/name).read_text('utf8').splitlines() if re.match(r'^\| [a-f0-9]{64} \|',l));assert n==expected,(name,n);counts[name]=n
paired=json.loads((B/'r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json').read_text('utf8'))
metrics=json.loads((R/'DETAILED_METRICS.json').read_text('utf8'))
assert metrics['pipeline_counts']['requests']==20554
audit=metrics['field_planner_audit_events'];assert audit['schema_pass_but_final_rejected']==2494
cases=json.loads((R/'CASE_EVIDENCE.json').read_text('utf8'));assert len(cases)==10 and len(cases['K02']['session_turns'])==2
report='''# ผลตรวจทานเอกสารก่อนส่ง

งานนี้ตรวจเอกสารและหลักฐานที่มีอยู่ ไม่มีการส่งคำถามใหม่เข้าบอท ไม่มี model generation และไม่มีการรัน full/targeted chatbot test

## รอบที่ 1 — ตรงกับโค้ดที่มีจริงหรือไม่

- แยก legacy R64 snapshot ออกจาก common R88/R87 และจากโฟลเดอร์ Downloads ต้นฉบับ
- ตรวจ early return ของ common: ตัวตอบเดิมด้านล่างยังอยู่ใน source แต่ไม่ได้หมายความว่า profile ใหม่เดินผ่านทั้งหมด
- แยกภาพรวม branch families ออกจากลำดับ return จริง เพิ่มตาราง retrieval ที่ระบุว่า general fallback อาจจบก่อน final curated/vector
- ตรวจ owner preview, published CommonStore และ migration draft reader ว่าเป็นคนละเส้นทาง
- พบ reference ของ draft catalog ชี้ชื่อ resolve_date ซึ่งไม่มีใน open_day.py จึงเก็บ draft เดิมไว้และสร้าง PROBLEM_CATALOG_REVIEWED.json ที่ชี้ function answer จริง เอกสารฉบับส่งใช้รุ่นตรวจทาน

## รอบที่ 2 — ไม่กล่าวเกินผลทดสอบหรือไม่

- ใช้คะแนน positive จากตัวตรวจเดียวกัน 94.41%/72.10% ไม่ใช้คนละ denominator ของรายงานเก่า
- แยก strict protocol, literal content, meaning/source correctness และ owner review
- แยก request/grade/call/audit event โดยเฉพาะ schema-pass แต่ rejected 2,494 เป็น audit events
- แยก runtime exceptions เดิม 2,692 NameError + 2 timeout จากใหม่ 2 watchdog และ 36 model transport timeout calls
- ไม่เปรียบ engine sessions ใหม่ 23/24 กับ HTTP sessions เดิม 22/24 เหมือนเป็นการทดลองเดียวกัน
- ตัวอย่างราคาเดิมมี expiry caveat จริง จึงระบุใน casebook และไม่กล่าวว่าเดิมอ้างเป็นราคาปัจจุบันโดยไม่มีคำเตือน
- R88 controlled booking unavailable ไม่ถูกใช้เป็นหลักฐานว่า WordPress จริงเสีย
- 116 missing localization metadata ไม่ถูกแปลงเป็น 116 records ไม่มีค่าอังกฤษ; 11 known section values และ 32 Thai-character flags แยกไว้
- Unknown optional fields ไม่ถูกนับเป็นข้อเท็จจริงที่ย้ายตกหล่นทั้งหมด และไม่ถามเจ้าของซ้ำเรื่องที่ผู้ใช้ยืนยันแล้ว

## รอบที่ 3 — อ่าน ใช้ และตรวจย้อนกลับได้หรือไม่

- ทำ README พร้อมลำดับอ่านและคำศัพท์ ให้ใช้สอง Full Flows แยกกันได้
- เพิ่ม casebook 12 กรณี พร้อมคำตอบเดิม/ใหม่และ trace ที่เก็บไว้แล้ว; 10 กลุ่มตัวอย่างมี raw subset ส่วน legacy NameError และ controlled booking ใช้ aggregate/source evidence
- เพิ่มบัญชีข้อมูลกับคำถามเจ้าของแบบ conditional ไม่โยนงานตีความโค้ดให้เจ้าของ
- ตรวจลิงก์ไฟล์/เลขบรรทัด จุดอ้างอิงโค้ด fences, จำนวน 37 sections และดัชนี failed requests ครบตามหลักฐาน
- เพิ่มช่องว่างไทย–อังกฤษใน prose โดยคง quoted raw answers, JSON, code spans และ link destinations
- ตรวจ hashes source ของทั้งสอง snapshots ไม่เปลี่ยน; ตรวจ installed R78 เทียบ R88 และ hash ฐานกลางที่บันทึกไว้

## สิ่งที่ผลตรวจนี้ไม่รับรอง

- ไม่ใช่การแก้ runtime หรือรับรองว่าทุกคำถาม 20,554 ข้อได้รับ human semantic review แล้ว
- ไม่ใช่การอนุมัติเผยแพร่ข้อมูล draft หรือรับรองแพ็กเกจ portable หลังแก้ล่าสุด
- ไม่ตัดสินคำแปลต่างสำนวนว่าถูกครบทุกเงื่อนไขจาก literal mismatch อย่างเดียว
- กลุ่มปัญหาอัตโนมัติยังเป็นสมมติฐาน; ตัวอย่างที่พิสูจน์สาเหตุแล้วไม่ใช้แทน root cause ของทุกข้อในกลุ่ม
- ข้อเสนอ target flow ในเอกสาร 04 ยังไม่ได้ติดตั้ง ต้องแยกผลทดสอบใหม่ในอนาคตจากหลักฐานเดิมชุดนี้

ผลตรวจเชิงเครื่องอ่านและ manifest เอกสารอยู่ใน DELIVERY_QA.json
'''
with (R/'DOCUMENT_REVIEW.md').open('x',encoding='utf8') as f:f.write(report.strip()+'\n')
qa={'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'read-only source and retained-result analysis; new documents only','chatbot_requests_executed':0,'model_calls_made':0,'production_code_data_approval_or_logs_written':False,'source_preservation':source_checks,'source_hash_mismatches':source_errors,'installed_r78_vs_r88_app_mismatches':parity,'knowledge_database_hashes':dbs,'local_markdown_links_checked':links,'link_errors':errors,'code_fence_counts':fences,'problem_categories':len(catalog),'failed_request_index_counts':counts,'casebook_sections':12,'case_raw_groups':len(cases),'fixture_session_turns_in_casebook':2,'prose_files_polished':changed,'limitations':['Automatic diagnosis is not individual human semantic verification.','Snapshot comparison does not isolate the causal effect of data schema alone.','No production approval/cutover or portable package recertification.'],'documents':{p.name:{'bytes':p.stat().st_size,'lines':len(p.read_text('utf8').splitlines()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in primary}}
with (R/'DELIVERY_QA.json').open('x',encoding='utf8') as f:json.dump(qa,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in qa.items() if k not in ['knowledge_database_hashes','documents','limitations']},ensure_ascii=False,indent=2))
