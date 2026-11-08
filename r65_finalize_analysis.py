import collections,hashlib,json,re,sqlite3
from pathlib import Path
BASE=Path(__file__).resolve().parent;O=BASE/'r65_detailed_failure_analysis_20261014';B=BASE/'r64_full_comparison_20261013'
c=sqlite3.connect(O/'evidence.sqlite');c.row_factory=sqlite3.Row
m=json.loads((O/'METRICS.json').read_text(encoding='utf-8'));ob=json.loads((O/'OBSERVATIONS.json').read_text(encoding='utf-8'));records=json.loads((O/'COMMON_RECORDS.json').read_text(encoding='utf-8'));guard=json.loads((O/'GUARD_REVIEW_COVERAGE.json').read_text(encoding='utf-8'))
def write(name,text):
 with (O/name).open('x',encoding='utf-8') as f:f.write(text)
def link(path,label=None,line=None):return '['+(label or Path(path).name)+']('+Path(path).as_posix()+(f':{line}' if line else '')+')'
kindcounts=collections.Counter(r['kind'] for r in records.values())
fl=['# ตรวจโครงสร้างข้อมูลที่ย้ายทุกkind','', 'นับheadที่อ่านจริงในR64 ไม่ใช่จำนวนpreparedrecords/revisionsในรายงานรอบก่อน','', '| kind | records | knownfields | unknownfields | conflictedfields |','|---|---:|---:|---:|---:|']
for kind,n in sorted(kindcounts.items()):
 fs=ob['field_status_by_kind'][kind];fl.append(f"| {kind} | {n} | {fs.get('known',0)} | {fs.get('unknown',0)} | {fs.get('conflicted',0)} |")
ex=json.loads((O/'EXTRA_METRICS.json').read_text(encoding='utf-8'))
for kind,rows in ex['field_status'].items():
 fl+=['',f'## {kind}: แต่ละfield','', '| field | สถานะ/จำนวน |','|---|---|']
 for f,statuses in rows.items():fl.append('| '+f+' | '+'; '.join(f'{s}={n}' for s,n in statuses.items())+' |')
fl+=['','## CS2 → service → rate: graphที่ตรวจจากข้อมูลจริง','', '```json',json.dumps(ex['cs2_join_graph'],ensure_ascii=False,indent=2),'```','', 'graphนี้พิสูจน์ว่ามีgame_serviceที่offered=trueแต่ต่อไปserviceIDที่ไม่มีrate ไม่ได้พิสูจน์ว่าศูนย์ไม่มีราคาPCจริง ต้องแปลงเส้นเชื่อมbilling/bookingจากsourceเดิมให้ถูก']
write('FORMAT_DATA_MAPPING_AUDIT.md','\n'.join(fl)+'\n')
reason=['# Failure reasonทุกชนิดที่พบ','', 'นับgradeevents ข้อหนึ่งมีได้หลายreason รายการนี้เก็บexactstrings ไม่ใช่เพียง8bucketของรายงานR64','']
for arm,d in m['arms'].items():
 reason+=['',f'## {arm}','', '| จำนวน | reasonตามraw |','|---:|---|']
 for s,n in sorted(d['exact_reasons'].items(),key=lambda x:(-x[1],x[0])):reason.append(f"| {n} | {s.replace('|',' / ').replace(chr(10),'<br>')} |")
write('ALL_FAILURE_REASON_TYPES.md','\n'.join(reason)+'\n')
sources=[('runtime NameError','app/pipeline/retrieval.py',900),('ownershipตัวแปรอยู่คนละfunction','app/pipeline/retrieval.py',679),('service guard scope','app/pipeline/user_service_facts.py',37),('map scope exclusion','app/pipeline/user_service_facts.py',43),('exact/fuzzy names','app/knowledge/common/answer.py',106),('fieldplanอ่านหลังเลือกentity','app/knowledge/common/answer.py',258),('childrenของcompetition','app/knowledge/common/answer.py',389),('confidence/validator','app/knowledge/common/answer.py',435),('semantic correctnessยังfalse','app/knowledge/common/read_contract.py',6),('schemaและsemanticguard','app/knowledge/common/planner.py',51),('sourceownership','app/knowledge/common/authority.py',20),('pricejoin','app/knowledge/common/relations.py',46),('entitycandidates','app/knowledge/common/entity_search.py',20),('typo candidate limits','app/knowledge/common/name_candidates.py',27),('oldgradeadapter','../grade_legacy.py',10),('outcomeclassifierwhitelist','tools/eval_contract_v2.py',18)]
code=['# Source codeที่ใช้ยืนยันสาเหตุ','', 'ลิงก์ไปsnapshotR64ที่ทดสอบจริง; lineเป็นจุดเริ่มอ่าน ตรวจSHAเมื่อเทียบกับproductionหรือpackage','']
for label,rel,line in sources:
 p=(B/'system'/rel).resolve();code.append('- '+link(p,label,line))
code+=['', '- '+link(BASE/'r63_legacy_migration_20261013/migrate.py','R63: controlsย้ายไปlimitations',160),'- '+link(BASE/'r63_legacy_migration_20261013/migrate.py','R63: facetยังpending',175),'- '+link(BASE/'r63_legacy_migration_20261013/migrate.py','R63: calculation_ruleไม่อนุมาน',270),'- '+link(B/'harness.py','R64: draftview/fixture/config',13),'- '+link(B/'grade_legacy.py','R64: การแยกgradebranch',10)]
write('SOURCE_CODE_INDEX.md','\n'.join(code)+'\n')
main=O/'R65_DETAILED_FAILURE_ANALYSIS_TH.md';text=main.read_text(encoding='utf-8')
addition='''
### 24.1 ข้อผิดพลาดของชุดทดสอบและตัวติดตามที่ต้องแยกจากproduct

- stageรอบแรกคัดไฟล์knowledgeไม่ครบจนapp/knowledgeหาย ต่อมาซ่อมจากsourceจริง ใช้SOURCE_MANIFEST_REPAIREDเป็นหลัก ไม่ใช้ImportErrorของstageที่ไม่ครบอธิบายchatbot
- unittest Temp/state pathโดนsandboxปฏิเสธ จึงรันtemp_fixedด้วยพื้นที่stateแยก; เก็บผลแรกไว้ แต่ใช้899functionsที่รันจบเป็นหลัก
- test HTMLขาดreferencefixture4ข้อ; rerun4/4ผ่านหลังcopyต้นฉบับ ไม่แก้คำตอบหรือexpectedของproduct
- HTTPsession IDไม่ผ่านvalidationในรอบแรก; รอบถัดมามีsocket10013จากenvironment; รอบprotocol_networkจึงเป็นข้อมูลหลัก
- supervisorเคยอ่านprocesshandleไม่ได้ในsandboxแล้วตีว่าprocessหยุด จึงเปิดrecoveryซ้ำชั่วคราว ภายหลังหยุดเฉพาะprocessที่เปิดเองและแก้การตรวจสิทธิ์ logยังอยู่ครบ; deduplicatefirst-resultตามkeyช่วยไม่ให้เพิ่มจำนวนcoverage แต่การรันซ้อนชั่วคราวอาจกระทบtiming/circuit จึงไม่ใช้ผลนี้เป็นSLA
- การสุ่มตัวอย่างด้วยkeywordไม่ใช่semanticlabel เช่น moneyในCS2กับงบเล่น หรือเหมาในเหมาะ ต้องใช้source/expecteddomainและmanualreviewประกอบ; casebookระบุชัดว่าtopicเป็นกลุ่มคำสำคัญ ไม่ใช่golddomain

### 24.2 ทำไมผลรอบก่อนผ่านแล้วรอบนี้ตกมาก

R62รายงานsemantic_release_final148/148จากfactsสมมุติ720รายการ มีqueryไทย74/อังกฤษ74 และOWNER_HTTP48/48แบบcanonicalfieldquestions สิ่งนี้พิสูจน์ความสามารถบางเส้นทางของschema/readerกับfixturesที่กรอกfieldไว้ ไม่รับรองการย้ายlegacydataที่ยังมีbindings/facet/calculation_ruleunknown

R63การรักษาข้อความและsourcepointer4922/4922เป็นคนละgateกับการตอบnaturalquestions ตัวverifyยังตรวจด้วยว่าbindingsต้องเป็นNoneเพื่อไม่fabricategesture ดังนั้นการผ่านgateนั้นกับการที่readerอ่านbindingsแล้วไม่พบข้อมูลเกิดพร้อมกันได้

R64จึงพบsemanticparityที่ยังไม่มีครบก่อนactivation การแก้ต้องมีgateข้อมูลย้าย→คำถามจริง→fieldที่ใช้→คำตอบ ไม่สรุปว่า148/148หรือ4922/4922เป็นaccuracyทั้งหมด และไม่เอาfixtureสมมุติไปกรอกเป็นfactsของศูนย์
'''
text=text.replace('## 25. Performance',addition+'\n## 25. Performance')
tail='\n\n## 31. ภาคผนวกเพิ่มเติมและผลตรวจทานเอกสาร\n\n'+link(O/'FORMAT_DATA_MAPPING_AUDIT.md','ทุกkind/fieldstatusและgraphราคาที่ขาด')+'\n\n'+link(O/'ALL_FAILURE_REASON_TYPES.md','failure reasonทุกชนิด')+'\n\n'+link(O/'SOURCE_CODE_INDEX.md','จุดในcodeที่ยืนยันสาเหตุ')+'\n\n'+link(O/'REPORT_VERIFICATION.json','ผลตรวจความครบและการรักษาไฟล์ต้นทาง')+'\n'
text+=tail;main.write_text(text,encoding='utf-8')
# Three concrete audit passes: coverage; counts/classification corrections; paths and source immutability.
checks=[]
assert c.execute('SELECT COUNT(*) FROM results').fetchone()[0]==82216
assert c.execute('SELECT COUNT(*) FROM grades').fetchone()[0]==223244
for arm in m['arms']:
 path=O/'all_failed_requests'/(arm+'.md');ids=set(re.findall(r'^## \d+\. ([a-f0-9]{64})$',path.read_text(encoding='utf-8'),re.M))
 gold={r[0] for r in c.execute('SELECT DISTINCT key FROM grades WHERE arm=? AND passed=0',(arm,))};assert ids==gold,(arm,len(ids),len(gold));checks.append({'pass':1,'arm':arm,'all_failed_requests_exported':len(ids)})
assert len(list((O/'by_corpus').glob('*.md')))==36
assert guard['guard_mismatches_exported_reviewed']==58
assert m['native']['legacy']['failure_events']+m['native']['legacy']['error_events']+m['native']['common']['failure_events']+m['native']['common']['error_events']==324
assert sum(m['oracle_inventory_per_arm'].values())==55811
checks.append({'pass':2,'corpora':36,'guard_mismatches':58,'native_events':324,'oracle_classes_sum':55811,'native_route_strings_normalized':True})
manifest=json.loads((O/'INPUT_MANIFEST.json').read_text(encoding='utf-8'));modified=[]
for f in manifest['files']:
 p=Path(f['path']);st=p.stat()
 if st.st_size!=f['bytes'] or st.st_mtime_ns!=f['mtime_ns']:modified.append(str(p))
assert not modified
assert not re.search(r'\{\{[A-Z_]+\}\}',text)
broken=[]
for target in re.findall(r'\]\((C:/[^)]+)\)',text):
 path=re.sub(r':\d+$','',target)
 if not Path(path).exists() and not path.endswith('REPORT_VERIFICATION.json'):broken.append(path)
assert not broken,broken
checks.append({'pass':3,'raw_files_mtime_size_unchanged':len(manifest['files']),'broken_main_links':broken,'unresolved_template_variables':False,'pipeline_calls':0,'production_writes':0})
write('REPORT_VERIFICATION.json',json.dumps({'checks':checks,'all_checks_passed':True,'semantic_manual_review_not_every_answer':True,'analysis_report_sha256':hashlib.sha256(main.read_bytes()).hexdigest()},ensure_ascii=False,indent=2))
write('lookup_case.py',"""import argparse,json,sqlite3,zlib\nfrom pathlib import Path\np=argparse.ArgumentParser();p.add_argument('key_prefix');p.add_argument('--arm',default='');a=p.parse_args()\nc=sqlite3.connect((Path(__file__).parent/'evidence.sqlite').as_uri()+'?mode=ro',uri=True)\nfor arm,key,raw in c.execute('SELECT arm,key,raw FROM results WHERE key LIKE ? AND (?=\"\" OR arm=?)',(a.key_prefix+'%',a.arm,a.arm)):\n print(arm,key);print(json.dumps(json.loads(zlib.decompress(raw)),ensure_ascii=False,indent=2))\n""")
print(json.dumps({'verified':True,'main_lines':len(text.splitlines()),'main_bytes':main.stat().st_size,'markdown_files':len(list(O.rglob('*.md'))),'all_failed_requests':sum(m['arms'][a]['failed_unique_requests'] for a in m['arms']),'all_failed_grades':sum(m['arms'][a]['counts']['failed'] for a in m['arms'])},ensure_ascii=False))
