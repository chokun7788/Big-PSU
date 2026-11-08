import collections,hashlib,json,re,sqlite3,zlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;B=BASE/'r64_full_comparison_20261013';O=BASE/'r65_detailed_failure_analysis_20261014'
c=sqlite3.connect(O/'evidence.sqlite');c.row_factory=sqlite3.Row
m=json.loads((O/'METRICS.json').read_text(encoding='utf-8'));ob=json.loads((O/'OBSERVATIONS.json').read_text(encoding='utf-8'));ex=json.loads((O/'EXTRA_METRICS.json').read_text(encoding='utf-8'));old=json.loads((B/'ANALYSIS_LATEST.json').read_text(encoding='utf-8'));paired=json.loads((B/'PAIRED_COMPARISON.json').read_text(encoding='utf-8'))
def write(name,text):
 p=O/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x',encoding='utf-8') as f:f.write(text)
 return p
def link(p,label=None):return '['+(label or Path(p).name)+']('+Path(p).as_posix()+')'
def cell(s):return str(s).replace('|','\\|').replace('\n','<br>')
def pct(a,b):return f'{a/b:.1%}' if b else 'N/A'
def short(s,n):
 s=str(s or '')
 return s if len(s)<=n else s[:n]+f' … [ย่อจาก{len(s):,}ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]'
def raw(row):return json.loads(zlib.decompress(row['raw']))
arms=('legacy_offline','common_offline','legacy_llm','common_llm')
coverage=['| รอบ | คำขอ | เกณฑ์ | ผ่านstrict | failureไม่ซ้ำตามคำขอ |','|---|---:|---:|---:|---:|']
partition=['| รอบ | เกณฑ์ที่ตก | protocolอย่างเดียว | protocol/outcomeอย่างเดียว | เนื้อหา/source/language/validation/อื่น |','|---|---:|---:|---:|---:|']
exception=['| รอบ | exception/watchdog จำนวนคำขอ |','|---|---|']
for arm in arms:
 a=m['arms'][arm];co=a['counts'];coverage.append(f"| {arm} | 20,554 | 55,811 | {co['strict_pass']:,} ({pct(co['strict_pass'],55811)}) | {a['failed_unique_requests']:,} |")
 partition.append(f"| {arm} | {co['failed']:,} | {co.get('protocol_only_failure',0):,} | {co.get('protocol_or_outcome_only_failure',0):,} | {co.get('content_or_gate_failure',0):,} |")
 exception.append('| '+arm+' | '+cell('; '.join(f'{k}={v:,}' for k,v in a['exceptions_by_message'].items()))+' |')
coverage+=['','ผลทั้งหมด82,216คำขอ/223,244เกณฑ์ ถูกทำดัชนีจากrawเดิมครบ รักษาfirst-result precedenceเหมือนR64; duplicateattemptsไม่ได้แทนผลผิดเดิมด้วยผลใหม่','',
'คะแนนแยกภาษา (เป็นstrict compatibility รวมroute/mode; autoจากexceptionยังรวมในคะแนนรวม):','',
'| รอบ | ไทย | อังกฤษ | รวม |','|---|---:|---:|---:|']
for arm in arms:
 r=old[arm];th=r['by_language']['th'];en=r['by_language']['en'];coverage.append(f"| {arm} | {pct(th['passed'],th['total'])} | {pct(en['passed'],en['total'])} | {pct(r['counts']['passed'],55811)} |")
coverage+=['','Content contractในคู่ที่ทั้งสองformatตรวจได้ (ไม่รวมหลายexception; รวมnegative-onlyด้วย):','',
'| รอบ | denominatorคู่ | เดิม | กลาง |','|---|---:|---:|---:|']
for arm in ('offline','llm'):
 x=paired[arm]['counts'];n=x['paired_content_contracts'];coverage.append(f"| {arm} | {n:,} | {pct(x['old_content_pass'],n)} | {pct(x['common_content_pass'],n)} |")
lang=['| kind | localized slotที่value.enว่าง |','|---|---:|']
la=json.loads((B/'COMMON_SOURCE_AUDIT.json').read_text(encoding='utf-8'))
for k,v in la['missing_english_by_kind'].items():lang.append(f'| {k} | {v} |')
lang+=['','| รอบcommon | responseอังกฤษที่มีmarker [Thai source] |','|---|---:|']
for arm in ('common_offline','common_llm'):lang.append(f"| {arm} | {ob[arm]['answer_observations'].get('english_with_Thai_source_marker',0):,} |")
lang.append('\nจำนวนmarkerเป็นการสังเกตรูปแบบข้อความ ไม่ใช่จำนวนคำตอบที่แปลผิดทั้งหมด ต้องตรวจproper names/ต้นฉบับที่เป็นอังกฤษ/การมีThai proseแยก')
length=['| รอบ | >2,000ตัวอักษร | >10,000ตัวอักษร |','|---|---:|---:|']
for arm in arms:
 x=ob[arm]['answer_observations'];length.append(f"| {arm} | {x.get('over_2000_chars',0):,} | {x.get('over_10000_chars',0):,} |")
audit=old['common_llm']['common_planner_model_audit'];changes=ex['llm_grade_changes'];reg=sum(changes['regressed_strict'].values());imp=sum(changes['improved_strict'].values())
llm=[f"Common strict: ปิดLLM16,998pass → เปิดLLM12,517pass; มีเกณฑ์ที่เคยผ่านแล้วตก{reg:,} และเคยตกแล้วผ่าน{imp:,}; net-4,481",
f"ในเกณฑ์ที่regressมี{changes['regressed_strict'].get('protocol',0):,}ข้อที่failureเฉพาะprotocolหลังเปิดLLM ที่เหลือยังต้องแยกoutcome/source/content/validation ไม่เหมาว่าเป็นsemanticregressionทั้งหมด",'',
'| common planner audit event | จำนวน |','|---|---:|']
for k in ('attempted','transport_ok','schema_accepted','final_plan_accepted','error:TimeoutError','error:HTTPError','gate:circuit breaker cooldown active'):llm.append(f"| {k} | {audit.get(k,0):,} |")
llm.append(f"\nresponseที่semantic_statusเป็นschema_only_unverified_intentจริง{ex['response_diagnostics']['common_llm']['schema_only_unverified_intent_responses']:,} คำขอ; มีconfidence0.8และcontract/source/gatefailure{ex['response_diagnostics']['common_llm']['confidence_0_8_with_contract_or_gate_failure']:,}คำขอ ตัวเลขเหล่านี้ไม่เท่ากับจำนวนข้อเท็จจริงที่พิสูจน์ว่าเท็จโดยมนุษย์")
oracle=['| ชนิดoracleต่อหนึ่งรอบ | จำนวนgrade | ความหมาย |','|---|---:|---|']
descs={'positive_text_or_clause':'มีrequiredข้อความหรือclause/qualitygate','route_outcome_only':'ไม่มีpositive/negative content assertionที่adapterใช้งาน','evidence_id_only':'ใช้IDหลักฐานเป็นเกณฑ์ ไม่ตรวจข้อความanswerครบทุกข้อ','negative_only':'ห้ามข้อความบางอย่าง ยังไม่พิสูจน์ว่าตอบเนื้อหาครบ'}
for k,v in m['oracle_inventory_per_arm'].items():oracle.append(f'| {k} | {v:,} | {descs.get(k,"ข้อสังเกตadapter")} |')
oracle+=['','| รอบ | strictpassแต่strong_outcome diagnosticเป็นfalse |','|---|---:|']
for arm in arms:oracle.append(f"| {arm} | {ex['response_diagnostics'][arm]['passed_despite_false_strong_outcome_diagnostic']:,} |")
oracle.append('\nจึงต้องตรวจoutcomeclassifierและการนำdiagnosticไปใช้ร่วมกัน ตัวเลขนี้ไม่ใช่จำนวนfalsepositiveเชิงความหมายที่ยืนยันแล้วทั้งหมด')
native=['| รูปแบบ | functionsรัน | failureevents | errorevents | functionsที่มีeventผิด |','|---|---:|---:|---:|---:|']
for arm in ('legacy','common'):
 a=m['native'][arm];native.append(f"| {arm} | {a['tests_run']} | {a['failure_events']} | {a['error_events']} | {a['affected_functions']} |")
http=['| รอบprotocolถูก | pass/24turn | failedturn |','|---|---:|---|']
for mode in ('legacy','common'):
 rs=ob['failed_http_turns'][mode];http.append(f"| {mode} | {24-len(rs)}/24 | "+cell('; '.join(f"S{x['session']+1}T{x['turn']+1}: {x['q']}" for x in rs))+' |')
# Export every failed request once per arm, including all original grade reasons and source locations.
registries=[];export_counts={}
for arm in arms:
 p=O/'all_failed_requests'/f'{arm}.md';p.parent.mkdir(exist_ok=True)
 count=0;grades=0
 with p.open('x',encoding='utf-8') as f:
  f.write(f'# ทุกคำขอที่มีเกณฑ์ไม่ผ่าน: {arm}\n\nคำขอไม่ซ้ำในรอบนี้; คำตอบในหน้านี้เป็นexcerpt250ตัวอักษร มีฉบับเต็มในSQLite/rawเดิม ทุกfailure reasonของคำขอนี้เก็บครบ ไม่เลือกเฉพาะreasonแรก\n\n')
  for row in c.execute('SELECT r.* FROM results r WHERE arm=? AND EXISTS(SELECT 1 FROM grades g WHERE g.arm=r.arm AND g.key=r.key AND g.passed=0) ORDER BY r.key',(arm,)):
   gs=c.execute('SELECT file,rownum,variant,reasons_json FROM grades WHERE arm=? AND key=? AND passed=0',(arm,row['key'])).fetchall();count+=1;grades+=len(gs)
   reasons=list(dict.fromkeys(s for g in gs for s in json.loads(g['reasons_json'])))
   f.write(f"## {count}. {row['key']}\n\n**คำถาม:** {row['question']}\n\n**จริง:** {row['mode'] or row['exception']}; locale={row['locale']}; confidence={row['confidence']}\n\n{short(row['answer'],250)}\n\n**เหตุไม่ผ่าน:** "+'; '.join(reasons)+'\n\n')
   f.write('**เกณฑ์อ้างอิง:** '+ '; '.join(f"{g['file']} row0={g['rownum']} variant={g['variant']}" for g in gs)+'\n\n')
   f.write(f"**raw:** {row['source_file']} JSONL record1={row['source_line']}\n\n")
  f.write(f'\nรวม{count:,}คำขอ/{grades:,}failedgrades\n')
 assert count==m['arms'][arm]['failed_unique_requests'] and grades==m['arms'][arm]['counts']['failed']
 registries.append(p);export_counts[arm]={'requests':count,'grades':grades};print('registry',arm,count,flush=True)
# Every corpus is represented, not just first 30 failures.
corpus_index=['# คะแนนและตัวอย่างแยกทุกcorpus','', '| corpus | จำนวนเกณฑ์ต่อรอบ | รายละเอียด |','|---|---:|---|']
files=[r[0] for r in c.execute('SELECT DISTINCT file FROM expected ORDER BY file')]
for file in files:
 slug=Path(file).stem+'_'+hashlib.sha256(file.encode()).hexdigest()[:8];p=O/'by_corpus'/(slug+'.md');lines=['# '+file,'','รายการนี้คงexpectedเดิมไว้ การจัดหมวดreasonใช้R65 normalization ไม่เปลี่ยนpass/failเดิม','', '| รอบ | pass | fail | protocol-only | content/source/language/gate |','|---|---:|---:|---:|---:|']
 total=c.execute('SELECT COUNT(*) FROM expected WHERE file=?',(file,)).fetchone()[0]
 for arm in arms:
  gs=c.execute('SELECT * FROM grades WHERE arm=? AND file=?',(arm,file)).fetchall();passed=sum(g['passed'] for g in gs);proto=sum(g['issues']=='protocol' for g in gs if not g['passed']);content=sum(any(k in g['issues'] for k in ('missing_content','source_target','language','forbidden_content','validation','other')) for g in gs if not g['passed'])
  lines.append(f'| {arm} | {passed}/{len(gs)} | {len(gs)-passed} | {proto} | {content} |')
  representatives=[g for g in gs if not g['passed'] and g['issues']!='protocol'][:2] or [g for g in gs if not g['passed']][:1]
  for g in representatives:
   row=c.execute('SELECT * FROM results WHERE arm=? AND key=?',(arm,g['key'])).fetchone();er=c.execute('SELECT case_json FROM expected WHERE key=? AND file=? AND rownum=? AND variant=?',(g['key'],file,g['rownum'],g['variant'])).fetchone();r=raw(row);resp=r.get('result') or {};art=resp.get('decision_artifact') or {};plan=art.get('query_plan') or {}
   lines+=['',f"## ตัวอย่าง {arm}: {g['key']}",'',f"คำถาม: {row['question']}",'','Expectedเดิม (excerpt; ฉบับเต็มในexpected.case_json):','```json',short(er[0],1400),'```','',f"Actual mode/category/confidence: {row['mode']} / {row['category']} / {row['confidence']}",'',short(row['answer'] or row['exception'],1100),'', 'Failures: '+g['reasons_json'],'','แผนที่เลือก:','```json',json.dumps({k:plan.get(k) for k in ('record_ids','requested_fields','all_fields','method','platform','unresolved_clauses','semantic_plan_accepted')},ensure_ascii=False,indent=2),'```','',f"raw source: {row['source_file']} record1={row['source_line']}"]
 write('by_corpus/'+p.name,'\n'.join(lines)+'\n');corpus_index.append(f'| {cell(file)} | {total} | {link(p)} |')
write('ALL_CORPUS_INDEX.md','\n'.join(corpus_index)+'\n')
# Human-readable trace samples; do not invent an answer where oracle only has evidence IDs.
samples=json.loads((O/'REVIEW_SAMPLES.json').read_text(encoding='utf-8'));sl=['# ตัวอย่างเชื่อม question → expected → actual → plan → trace','', 'ตัวอย่างคัดแบบคำสำคัญ ไม่ถือว่าkeywordgroupเป็นgold domain และไม่ใช้แทนทะเบียนทุกfailure มีsourcepath/keyทุกข้อ; expectedเป็นcontractเดิม ไม่ใช่คำตอบใหม่ที่แต่งขึ้น','']
for i,s in enumerate(samples,1):
 plan=(s.get('artifact') or {}).get('query_plan') or {};sl+= [f"## {i}. {s['arm']} / {s['topic']} / {s['key']}",'',f"**ถาม:** {s['question']}",'',f"**ตอบจริง:** mode={s.get('mode')}; confidence={s.get('confidence')}; exception={s.get('exception')}",'',short(s.get('answer'),2200),'', '**Expectedและfailure:**','```json',short(json.dumps(s.get('grades'),ensure_ascii=False,indent=2),2200),'```','', '**แผน:**','```json',short(json.dumps(s.get('artifact'),ensure_ascii=False,indent=2),2800),'```','', '**traceที่มีคะแนน/การตัดสิน:**']
 for t in s.get('trace',[]):
  if t.get('stage')!='timing':sl+= ['```json',short(json.dumps(t,ensure_ascii=False),1200),'```']
 sl+=['',f"raw {s['source']} JSONL record1={s['line']}",'']
write('QUESTION_ANSWER_TRACE_CASEBOOK.md','\n'.join(sl))
# All native failure events and all smoke outcomes.
nl=['# Native unit failures/errors ทุกevent','', 'ข้อมูลจากtemp_fixedทั้ง899functionsต่อformat; subtesteventsอาจซ้ำfunction; fixture4ข้อrerunผ่านแยกในR64; stackฉบับเต็มยังอยู่ในJSON/logเดิม',''];events=0
for mode in ('legacy','common'):
 d=json.loads((B/(mode+'_test_all.py_temp_fixed.json')).read_text(encoding='utf-8'))
 for typ in ('failures','errors'):
  for name,trace in d[typ]:events+=1;nl+= [f'## {events}. {mode} / {typ} / {name}','', '```text',short(trace,1800),'```','',link(B/(mode+'_test_all.py_temp_fixed.json')),'']
assert events==324
write('NATIVE_ALL_FAILURE_EVENTS.md','\n'.join(nl))
sm=['# Smokeทั้งหมดและเหตุที่ต้องตรวจ','', 'exitcode0รับรองว่าสคริปต์ผ่านเกณฑ์ของตัวเอง; exitcode1ต้องอ่านassertionและconfig ไม่เท่ากับคำตอบผิดทุกครั้ง',''];smcount=0
for mode in ('legacy','common'):
 rows=json.loads((B/(mode+'_smokes')/'SUMMARY.json').read_text(encoding='utf-8'))
 for r in rows:
  smcount+=1;p=B/(mode+'_smokes')/(Path(r['file']).stem+'.log');tail='\n'.join(p.read_text(encoding='utf-8',errors='replace').splitlines()[-10:]) if p.exists() else 'รันผ่านactual HTTP suiteแยก'
  sm += [f"## {smcount}. {mode} / {r['file']}",'',json.dumps(r,ensure_ascii=False),'',link(p) if p.exists() else link(B/(mode+'_http_protocol_network')/'SUMMARY.json')]
  if r['status']!='passed':sm+=['','```text',short(tail,1800),'```']
write('SMOKE_ALL_RESULTS.md','\n'.join(sm)+'\n')
# Guard mismatches from current policy.
gd=['# Input guard mismatches','', 'จัดเก็บเฉพาะ mismatchของpolicyปัจจุบัน; เป็นdetector/action test ไม่ใช่answercorrectness test',''];guardcount=0
for mode in ('legacy','common'):
 rows=json.loads((B/(mode+'_GUARD_RESULTS.json')).read_text(encoding='utf-8'))
 for r in rows:
  if any(r.get(k) is False for k in r if k.endswith(('_correct','_matches','_ok'))):guardcount+=1;gd+=['```json',json.dumps(r,ensure_ascii=False,indent=2),'```','']
write('INPUT_GUARD_CASES.md','\n'.join(gd))
ht=['# HTTP failuresที่ใช้protocolถูก','', 'อ่านผลจริงทุกturnที่ไม่ผ่าน แยกliteral expectation/transport/เนื้อหา; serverstateอยู่ในOBSERVATIONS.json','']
for mode,rows in ob['failed_http_turns'].items():
 for r in rows:ht+= [f"## {mode} session{r['session']+1} turn{r['turn']+1}: {r['q']}",'','```json',short(json.dumps(r,ensure_ascii=False,indent=2),6500),'```','']
write('HTTP_FAILED_TURNS.md','\n'.join(ht))
artifacts=['| เอกสาร/ข้อมูล | ใช้ทำอะไร |','|---|---|',f'| {link(O/"ALL_CORPUS_INDEX.md")} | ทุกcorpusและตัวอย่างexpected/actual/plan |',f'| {link(O/"QUESTION_ANSWER_TRACE_CASEBOOK.md")} | ตัวอย่าง{len(samples)}รายการพร้อมtrace/คะแนน/field |',f'| {link(O/"NATIVE_ALL_FAILURE_EVENTS.md")} | unit324failure/erroreventsทั้งหมด |',f'| {link(O/"SMOKE_ALL_RESULTS.md")} | smoke170รายการทั้งสองformat |',f'| {link(O/"HTTP_FAILED_TURNS.md")} | actualHTTPที่ไม่ผ่านทั้งหมด |',f'| {link(O/"INPUT_GUARD_CASES.md")} | guardmismatchและlabel/action |',f'| {link(O/"METRICS.json")} / {link(O/"EXTRA_METRICS.json")} / {link(O/"OBSERVATIONS.json")} | จำนวนที่ใช้วิเคราะห์และdiagnostic |',f'| {link(O/"evidence.sqlite")} | rawresponseเต็มแบบcompressed + ทุกexpected/grade/sourcepointer |']
for p in registries:artifacts.append(f'| {link(p)} | ทุกคำขอที่มีfailureในรอบนี้ |')
sections={'COVERAGE':coverage,'FAILURE_PARTITION':partition,'EXCEPTIONS':exception,'LANGUAGE_AND_FIELDS':lang,'LENGTH_METRICS':length,'LLM_METRICS':llm,'ORACLE_AUDIT':oracle,'NATIVE_SUMMARY':native,'HTTP_FAILURES':http,'ARTIFACT_INDEX':artifacts}
text=(BASE/'r65_report_sections.md').read_text(encoding='utf-8')
for k,v in sections.items():text=text.replace('{{'+k+'}}','\n'.join(v))
assert not re.search(r'\{\{[A-Z_]+\}\}',text)
write('R65_DETAILED_FAILURE_ANALYSIS_TH.md',text)
write('README.md','# R65 เริ่มอ่านที่นี่\n\n'+link(O/'R65_DETAILED_FAILURE_ANALYSIS_TH.md','รายงานวิเคราะห์ฉบับหลัก 30ส่วน')+'\n\n'+link(O/'ALL_CORPUS_INDEX.md','คะแนนและรายละเอียดทุกcorpus')+'\n\n'+link(O/'QUESTION_ANSWER_TRACE_CASEBOOK.md','ตัวอย่างคำถาม/คำตอบ/trace')+'\n\nข้อมูลทั้งหมดมาจากR64ที่รันแล้ว ไม่มีการรันfulltestใหม่หรือแก้production\n')
manifest={'failed_registries':export_counts,'failed_grades_exported':sum(v['grades'] for v in export_counts.values()),'corpora':len(files),'trace_samples':len(samples),'native_events':events,'smoke_records':smcount,'guard_mismatches_exported':guardcount,'source_result_rows':82216,'grade_rows':223244,'pipeline_calls':0,'production_writes':0}
write('EXPORT_COVERAGE.json',json.dumps(manifest,ensure_ascii=False,indent=2));print(json.dumps(manifest),flush=True)
c.close()
