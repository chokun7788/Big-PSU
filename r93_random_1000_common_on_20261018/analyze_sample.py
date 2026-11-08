"""Analyze every retained sample result; compare saved R88, no new requests."""
from pathlib import Path
import collections,gzip,hashlib,json,statistics,sys
R=Path(__file__).resolve().parent;B=R.parent;S=R/'system';sys.path[:0]=[str(S),str(R)]
from analyze import literal,bucket

def read_rows(root):
 for p in sorted(root.glob('RESULTS_*.jsonl.gz')):
  with gzip.open(p,'rt',encoding='utf8') as f:
   for line in f:
    if line.strip():yield json.loads(line)
def write(name,value):
 with (R/name).open('x',encoding='utf8') as f:
  if isinstance(value,str):f.write(value)
  else:json.dump(value,f,ensure_ascii=False,indent=2)
def link(label,p):return f'[{label}](<{p.as_posix()}>)'
def ratio(p,n):return f'{p:,}/{n:,} ({100*p/n:.2f}%)' if n else 'ไม่มีเกณฑ์ข้อความให้ตรวจ'
def audit_values(value):
 found=[]
 def visit(x):
  if isinstance(x,dict):
   if ('schema_accepted' in x or 'semantic_status' in x) and any(k in x for k in ('attempted','transport_ok','semantic_status')):found.append(x)
   for y in x.values():visit(y)
  elif isinstance(x,list):
   for y in x:visit(y)
 visit(value)
 return list({json.dumps(v,sort_keys=True,ensure_ascii=False,default=str):v for v in found}.values())
config=json.loads((R/'CONFIG.json').read_text('utf8'))
done=json.loads((R/'sample01/RUN_FINISHED.json').read_text('utf8'))
jobs={j['key']:j for j in (json.loads(x) for x in (R/'SELECTED_JOBS.jsonl').read_text('utf8').splitlines())}
results=list(read_rows(R/'sample01'));keys=[x['key'] for x in results]
assert len(results)==len(set(keys))==len(jobs)==1000 and set(keys)==set(jobs) and done['coverage_complete']
old={x['key']:x for x in read_rows(B/'r88_full_common_llm_20261017/full01') if x['key'] in jobs}
assert len(old)==1000
tot=collections.Counter();langs=collections.defaultdict(collections.Counter);domains=collections.defaultdict(collections.Counter);modes=collections.Counter();reasons=collections.Counter();diagnostic=collections.Counter();models=collections.Counter();timings=[];request_rows=[];examples=collections.defaultdict(list)
for row in results:
 key=row['key'];job=jobs[key];result=row.get('result',{});art=result.get('decision_artifact') or {};plan=art.get('query_plan') or {};answer=result.get('answer','');before=old[key];old_answer=before.get('result',{}).get('answer','');domain=job['r70_stratum']['domain'];lang=job['locale'];cs=[tot,langs[lang],domains[domain]]
 mode=result.get('mode','execution_exception');modes[mode]+=1;timings.append(row.get('elapsed_sec',0));audits=audit_values(art)
 signal=[]
 effective=row.get('effective_locale',lang)
 if lang=='en' and effective!='en':signal.append('explicit_english_effective_locale_changed')
 if effective=='en':
  from app.core.locale import contains_thai_prose
  if contains_thai_prose(answer):signal.append('english_thai_prose_flag_requires_review')
 if row.get('exception'):signal.append('execution_error')
 if not answer:signal.append('empty_answer')
 if result.get('validation',{}).get('ok') is False:signal.append('validation_rejected')
 if 'not_current' in mode:signal.append('not_current_needs_validity_review')
 if 'live_booking_status' in mode or art.get('live_booking'):signal.append('controlled_live_no_occupancy_oracle')
 if plan.get('record_ids') and not plan.get('requested_fields') and 'clarification' in mode:signal.append('known_subject_unresolved_task')
 rejected=art.get('rejected_candidate') or {}
 if 'unresolved_query_clause' in rejected.get('validation_errors',[]):signal.append('unresolved_clause_veto')
 for a in audits:
  models['distinct_audit_records']+=1
  if a.get('schema_accepted') is True:models['schema_accepted_audit_records']+=1
  if a.get('final_plan_accepted') is True or a.get('semantic_selection_accepted') is True:models['accepted_plan_audit_records']+=1
  status=(a.get('semantic') or {}).get('semantic_status') or a.get('semantic_status')
  if status=='rejected_unverified_intent':signal.append('semantic_unverified_intent')
  if a.get('error_stage')=='transport' or a.get('availability_failure'):signal.append('model_availability_or_body_failure')
 for call in row.get('observed_model_http_calls',[]):
  models['http_attempts']+=1
  models['http_response_opened']+=int(call.get('transport_ok') is True)
  models['http_open_failure']+=int(call.get('transport_ok') is not True)
  if not call.get('transport_ok'):signal.append('model_http_open_failure')
 for s in set(signal):diagnostic[s]+=1
 for c in cs:c['requests']+=1;c['exceptions']+=bool(row.get('exception'));c['empty_answers']+=not bool(answer)
 grades={(g['file'],g['row'],g['variant']):g for g in row.get('grades',[])}
 old_grades={(g['file'],g['row'],g['variant']):g for g in before.get('grades',[])}
 positive=[];old_positive=[];row_failures=[];raw_pass=[]
 for entry in job['entries']:
  g=grades[(entry['file'],entry['row'],entry['variant'])];og=old_grades[(entry['file'],entry['row'],entry['variant'])]
  for c in cs:c['grades']+=1;c['strict_passed']+=bool(g['passed']);c['old_strict_passed']+=bool(og['passed'])
  raw_pass.append(bool(g['passed']));failures=g.get('failures',[]);reasons.update(failures);groups={bucket(str(f)) for f in failures}
  for c in cs:
   for group in groups:c['failure_'+group]+=1
  if groups=={'protocol'}:
   for c in cs:c['protocol_only_grades']+=1
  ok,errs,pos=literal(entry['case'],answer);old_ok,old_errs,old_pos=literal(entry['case'],old_answer)
  assert pos==old_pos and (ok is None)==(old_ok is None)
  if ok is not None:
   for c in cs:c['text_checked']+=1;c['text_passed']+=bool(ok);c['old_text_passed']+=bool(old_ok)
  if pos:
   positive.append(bool(ok));old_positive.append(bool(old_ok))
   for c in cs:
    c['positive_checked']+=1;c['positive_passed']+=bool(ok);c['old_positive_passed']+=bool(old_ok)
    c['positive_improved_grades']+=bool(ok and not old_ok);c['positive_regressed_grades']+=bool(old_ok and not ok)
  if failures or errs:row_failures.append({'case_id':entry['case'].get('id'),'file':entry['file'],'row':entry['row'],'variant':entry['variant'],'strict_failures':failures,'text_failures':errs,'positive_contract':pos,'text_passed':ok,'old_text_passed':old_ok,'case':entry['case']})
 for c in cs:
  c['strict_all_pass_requests']+=bool(raw_pass and all(raw_pass))
  if positive:
   c['positive_checked_requests']+=1;c['all_positive_pass_requests']+=all(positive);c['old_all_positive_pass_requests']+=all(old_positive)
 summary={'key':key,'question':job['question'],'locale':lang,'domain':domain,'mode':mode,'answer':answer,'old_answer':old_answer,'has_positive_content_contract':bool(positive),'all_positive_pass':all(positive) if positive else None,'old_all_positive_pass':all(old_positive) if old_positive else None,'signals':sorted(set(signal)),'query_plan':plan,'need_ledger':art.get('need_ledger'),'rejected_candidate':rejected,'source_hits':result.get('hits',[]),'failures':row_failures,'model_http':row.get('observed_model_http_calls',[]),'elapsed_sec':row.get('elapsed_sec')}
 request_rows.append(summary)
 label='positive_content_failure' if positive and not all(positive) else 'improved_content' if positive and all(positive) and not all(old_positive) else 'regressed_content' if positive and not all(positive) and all(old_positive) else 'protocol_or_outcome_without_content_failure' if row_failures else 'passed'
 # Retain regressions separately even when they also belong to failure group.
 labels=[label]+(['regressed_content'] if positive and not all(positive) and all(old_positive) else [])
 for label in set(labels):
  if len(examples[label])<20 and (not examples[label] or sum(e['domain']==domain for e in examples[label])<3):examples[label].append(summary)
assert tot['grades']==config['selected_grades'] and not tot['failure_grader']
timings.sort();pct=lambda f:timings[int((len(timings)-1)*f)]
source=Path(config['source_installation'])/'system'
preservation={'frozen_application_and_inputs_unchanged':all(hashlib.sha256((S/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in config['source_manifest']),
 'original_application_and_inputs_unchanged':all(hashlib.sha256((source/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in config['source_manifest']),
 'original_database_unchanged':hashlib.sha256((source/'data/knowledge/common.sqlite').read_bytes()).hexdigest()==config['source_database_sha256']}
analysis={'complete':True,'requests':1000,'grades':tot['grades'],'seed':config['sample_seed'],'llm_enabled':True,'format':'common','build':'R92 installed revision 3','totals':dict(tot),'by_requested_locale':dict(langs),'by_domain':dict(domains),'diagnostic_signals_per_request':dict(diagnostic),'model_transport_and_audits':dict(models),'modes':dict(modes),'timing':{'p50_sec':pct(.5),'p95_sec':pct(.95),'p99_sec':pct(.99),'max_sec':max(timings),'scope':'two evaluator processes, one model slot, grading included; not an HTTP/concurrency SLA'},'coverage':{'unique_keys':len(set(keys)),'missing':[],'duplicates':[],'multi_turn_tested':False},'comparison':'same selected request keys and same text checker against retained R88 results; no old model requests','preservation':preservation}
assert all(preservation.values())
write('ANALYSIS_FINAL.json',analysis);write('FAILURE_COUNTS.json',reasons.most_common());write('EXAMPLE_CASES.json',dict(examples))
with (R/'PER_REQUEST_ANALYSIS.jsonl').open('x',encoding='utf8') as f:
 for row in request_rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
lines=['# ผลสุ่ม 1,000 คำถามจากชุดใหญ่ — Format กลาง R92 / เปิด LLM','',
 'รันครบ 1,000 request keys ไม่ซ้ำจาก 20,554 ข้อ รวม '+str(tot['grades'])+' grades ใช้ seed `'+config['sample_seed']+'` ไม่มีการสุ่มใหม่ตามผลผ่าน/ผิด','',
 '## ผลหลัก','',
 '- ผ่าน positive content contracts: **'+ratio(tot['positive_passed'],tot['positive_checked'])+'**; common R88 ที่บันทึกไว้สำหรับข้อเดียวกัน: '+ratio(tot['old_positive_passed'],tot['positive_checked']),
 '- ผ่าน strict contracts เดิม: '+ratio(tot['strict_passed'],tot['grades'])+'; R88: '+ratio(tot['old_strict_passed'],tot['grades']),
 '- ผ่าน positive contracts ทุกข้อที่ผูกกับคำถาม: '+ratio(tot['all_positive_pass_requests'],tot['positive_checked_requests'])+'; คำถามที่ไม่มี positive assertion ไม่ถูกนับเป็นคำตอบถูกทางความหมาย',
 '- Positive grades ดีขึ้น '+str(tot['positive_improved_grades'])+' และแย่ลง '+str(tot['positive_regressed_grades'])+' เทียบผล R88 ของข้อเดียวกัน',
 '- ไม่ผ่านเฉพาะ protocol '+str(tot['protocol_only_grades'])+' grades; execution exceptions '+str(tot['exceptions'])+' requests; grader errors '+str(tot['failure_grader'])+' grades','',
 '## แยกภาษา requested locale','',
 '| ภาษา | คำถาม | Positive content R92 | Positive content R88 | Strict R92 |','|---|---:|---:|---:|---:|']
for locale,c in sorted(langs.items()):lines.append(f"| {locale} | {c['requests']} | {ratio(c['positive_passed'],c['positive_checked'])} | {ratio(c['old_positive_passed'],c['positive_checked'])} | {ratio(c['strict_passed'],c['grades'])} |")
lines+=['','## หมวดที่มี positive contracts','', '| หมวดจาก corpus | คำถาม | R92 | R88 |','|---|---:|---:|---:|']
for domain,c in sorted(domains.items(),key=lambda kv:(-(kv[1]['positive_checked']-kv[1]['positive_passed']),kv[0])):
 if c['positive_checked']:lines.append(f"| {domain.replace('|','/')} | {c['requests']} | {ratio(c['positive_passed'],c['positive_checked'])} | {ratio(c['old_positive_passed'],c['positive_checked'])} |")
lines+=['','## สัญญาณวินิจฉัยจาก trace — นับคำถาม และทับซ้อนกันได้','',json.dumps(dict(diagnostic),ensure_ascii=False,indent=2),'',
 'known_subject_unresolved_task หมายถึงพบ target แต่ field/task ยังไม่ลงตัว; semantic_unverified_intent หมายถึง guard ไม่รับ intent ของแผน; not_current ต้องตรวจ validity และ oracle ประกอบ ไม่ถือว่าผิดหรือถูกโดยอัตโนมัติ','',
 '## LLM และเวลา','',
 '- Model preflight สร้าง response จบแล้วก่อนเริ่มชุดสุ่ม เปิดสิทธิ์ LLM ทุกคำถาม แต่ typed paths ไม่จำเป็นต้องเรียกโมเดล',
 '- HTTP model attempts '+str(models['http_attempts'])+', response opened '+str(models['http_response_opened'])+', open failures '+str(models['http_open_failure'])+' — response opened เป็นหลักฐานระดับเปิด HTTP ไม่รับรอง body/schema/เนื้อหา',
 '- Distinct audit records ต่อ request: schema accepted '+str(models['schema_accepted_audit_records'])+', accepted plans '+str(models['accepted_plan_audit_records'])+'; audit records ไม่เท่ากับจำนวน model calls',
 '- p50 '+f'{pct(.5):.2f}'+'s / p95 '+f'{pct(.95):.2f}'+'s / p99 '+f'{pct(.99):.2f}'+'s; รวมการตรวจเกณฑ์และข้อจำกัดคิวสอง workers ไม่ใช่เวลาตอบผู้ใช้พร้อมกันที่รับรอง','',
 '## ขอบเขตการแปลผล','',
 '- เป็นการสุ่มแบบกระจาย locale/domain อย่างน้อยหนึ่งต่อ 156 cells; rare cells ถูกเพิ่มสัดส่วนเพื่อ coverage คะแนน sample จึงไม่ใช่ estimate แบบ simple-random ของทั้ง population',
 '- ใช้วันอ้างอิงเดิม 16 ต.ค. 2026 และ per-job dates ตาม corpus เพื่อเทียบ retained R88; ไม่เลื่อนเวลาให้ราคาเก่ากลับมามีผล',
 '- Booking provider เป็น controlled unavailable เหมือน R88 ไม่มี live occupancy oracle จึงไม่ใช้คะแนนนี้วินิจฉัยความถูกต้อง WordPress สด',
 '- ทั้ง 1,000 เป็น single-turn เพราะ corpus jobs ไม่มี history ไม่รับรอง multi-turn ทั้งระบบจากชุดนี้',
 '- Positive literal/complete-clause contracts ยังอาจมี false mismatch จากคำแปลหรือสำนวน และบาง contract อ่อนเกินตรวจทุก claim; strict รวม route/mode/source protocol เดิม ไม่ใช่ semantic accuracy',
 '- ไม่แก้ code/data/approval ระหว่างรัน และไม่รัน Flow เดิมซ้ำ','',
 '## หลักฐาน','',
 '- '+link('ผลตัวเลขทั้งหมด',R/'ANALYSIS_FINAL.json'),'- '+link('วิเคราะห์ทุกคำถามและเกณฑ์ที่พลาด',R/'PER_REQUEST_ANALYSIS.jsonl'),'- '+link('ตัวอย่างพร้อม old/new answers และ plans',R/'EXAMPLE_CASES.json'),'- '+link('จำนวนเหตุที่ไม่ผ่านทั้งหมด',R/'FAILURE_COUNTS.json'),'- '+link('สัดส่วนการสุ่มและ seed',R/'SAMPLE_ALLOCATION.json'),'- '+link('รายการโจทย์ที่สุ่ม',R/'SELECTED_JOBS.jsonl'),'- '+link('ผลดิบ worker 0',R/'sample01/RESULTS_0.jsonl.gz'),'- '+link('ผลดิบ worker 1',R/'sample01/RESULTS_1.jsonl.gz')]
write('REPORT_FINAL_TH.md','\n'.join(lines)+'\n')
write('TEST_COMPLETE.json',{'complete':True,'requests':1000,'grades':tot['grades'],'analysis':'REPORT_FINAL_TH.md','preservation':preservation})
print(json.dumps({'complete':True,'positive_passed':tot['positive_passed'],'positive_checked':tot['positive_checked'],'old_positive_passed':tot['old_positive_passed'],'strict_passed':tot['strict_passed'],'grades':tot['grades'],'diagnostics':dict(diagnostic)},ensure_ascii=False))
