"""Report existing R70 results without rerunning any question or editing answers."""
import argparse,collections,gzip,hashlib,json,re,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;R=B/'r70_half_common_llm_20261016';S=R/'system';sys.path.insert(0,str(S))
def bucket(s):
 if s.startswith(('route:','intent:','legacy_mode_prefix:','forbidden_category','route expected','route_mismatch','wrong_category')):return 'protocol'
 if s.startswith(('status:','outcome expected','outcome_mismatch','wrong_outcome:')):return 'outcome'
 if s.startswith(('missing rulebook target','retrieval evidence','wrong_game_evidence','wrong_game_source')):return 'evidence_identifier'
 if s.startswith('validation'):return 'validation'
 if 'latency' in s or 'timeout' in s:return 'performance'
 if s.startswith('grader_exception'):return 'grader'
 if s=='quality_score_or_required_gate_failed':return 'native_quality_composite'
 return 'content_or_format'
def rows(root):
 for path in sorted(root.glob('RESULTS_*.jsonl.gz')):
  try:
   with gzip.open(path,'rt',encoding='utf8') as f:
    for n,line in enumerate(f,1):
     try:yield path.name,n,json.loads(line)
     except ValueError:continue
  except EOFError:pass # Partial snapshots are explicitly labelled, never final.
def literal(c,answer):
 from tools.eval_contract_v2 import contract_matches
 contract=c.get('answer_contract') or {k:c[k] for k in ('must_contain','must_contain_any','must_contain_all_groups','must_not_contain') if k in c}
 positive=bool(c.get('required_clauses') or c.get('clauses') or any(contract.get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')))
 if not positive and not contract.get('must_not_contain'):return None,[],False
 _,errors=contract_matches(answer,contract)
 required=c.get('required_clauses') or c.get('clauses') or []
 body=re.sub(r'\s+',' ',answer.split('แหล่งข้อมูล:')[0].split('Source:')[0].casefold())
 from tools.run_competition_contract_r27 import outline_normalized
 for clause in required:
  if outline_normalized(clause) not in body:errors.append('missing_complete_clause:'+clause)
 return not errors,errors,positive
def main():
 p=argparse.ArgumentParser();p.add_argument('--run',default='full01');p.add_argument('--partial',action='store_true');p.add_argument('--tag',default='FINAL');args=p.parse_args()
 root=R/args.run;config=json.loads((R/'CONFIG.json').read_text('utf8'))
 selected={j['key']:j for j in (json.loads(s) for s in (R/'SELECTED_JOBS.jsonl').read_text('utf8').splitlines() if s.strip())}
 seen=set();duplicates=[];unknown=[];totals=collections.Counter();locales=collections.defaultdict(collections.Counter);domains=collections.defaultdict(collections.Counter);corpora=collections.defaultdict(collections.Counter);modes=collections.Counter();failures=collections.Counter();parts=collections.Counter();models=collections.Counter();times=[];sample_groups=collections.defaultdict(list);sample_seen=collections.defaultdict(set);evidence_samples=[];wrong_lang=[];model_retest_keys=set()
 for file,line,row in rows(root):
  key=row['key']
  if key in seen:duplicates.append(key);continue
  seen.add(key)
  if key not in selected:unknown.append(key);continue
  job=selected[key];result=row.get('result',{});answer=result.get('answer','');language=row.get('effective_locale',row['requested_locale']);domain=job['r70_stratum']['domain'];mode=result.get('mode','execution_exception')
  totals['requests']+=1;locales[language]['requests']+=1;domains[domain]['requests']+=1;modes[mode]+=1
  if row.get('elapsed_sec') is not None:times.append(row['elapsed_sec'])
  if row.get('exception'):totals['execution_exceptions']+=1
  if not answer:totals['empty_answers']+=1
  if result.get('validation',{}).get('ok') is False:totals['validation_rejected_requests']+=1
  if 'clarification' in mode:totals['clarification_requests']+=1
  if 'retry' in mode:totals['retry_requests']+=1
  if 'not_current' in mode:totals['not_current_requests']+=1
  if 'live_booking_status_unavailable' in mode:totals['live_unavailable_requests']+=1
  migration=(result.get('decision_artifact') or {}).get('migration',{})
  if migration.get('legacy_fallback_used') is True:totals['legacy_fallback_used']+=1
  elif migration.get('profile')=='r69-migration-preview':totals['explicit_new_common_profile']+=1
  elif mode.startswith(('input_guard','pipeline:studio_scope')):totals['input_or_scope_guard']+=1
  else:totals['unclassified_profile_result']+=1
  if row['requested_locale']=='en' and language!='en':wrong_lang.append({'key':key,'question':row['question'],'effective':language})
  if language=='en':
   from app.core.locale import contains_thai_prose
   if contains_thai_prose(answer):totals['english_thai_prose_flags']+=1;locales[language]['thai_prose_flags']+=1
  for call in row.get('observed_model_http_calls',[]):
   models['http_attempts']+=1;models['http_transport_successes']+=int(call.get('transport_ok',False));models['http_transport_failures']+=int(not call.get('transport_ok',False));models['error:'+str(call.get('error_type','none'))]+=int(not call.get('transport_ok',False))
   if not call.get('transport_ok'):model_retest_keys.add(key)
  audits=[]
  def walk(value):
   if isinstance(value,dict):
    if ('attempted' in value or 'transport_ok' in value) and ('schema_accepted' in value or 'reason' in value or 'error_stage' in value):audits.append(value)
    for child in value.values():walk(child)
   elif isinstance(value,list):
    for child in value:walk(child)
  walk(result.get('decision_artifact',{}))
  unique={json.dumps(v,sort_keys=True,ensure_ascii=False,default=str):v for v in audits}
  for audit in unique.values():
   models['distinct_audit_records']+=1;models['audit_schema_accepted']+=int(audit.get('schema_accepted') is True);models['audit_attempted']+=int(audit.get('attempted') is True)
   if audit.get('reason'):models['audit_reason:'+str(audit['reason'])]+=1
   if audit.get('reason') in {'model_busy','circuit breaker cooldown active'} or audit.get('error_stage')=='transport':model_retest_keys.add(key)
  if 'retry' in mode:model_retest_keys.add(key)
  grade_map={(g['file'],g['row'],g['variant']):g for g in row.get('grades',[])}
  row_positive=[];row_raw=[]
  for entry in job['entries']:
   grade=grade_map.get((entry['file'],entry['row'],entry['variant']))
   ctrs=[totals,locales[language],domains[domain],corpora[entry['file']]]
   for counter in ctrs:counter['grades']+=1
   if grade is None:
    for counter in ctrs:counter['missing_grade_results']+=1
    row_raw.append(False)
    continue
   row_raw.append(bool(grade['passed']))
   for counter in ctrs:counter['raw_passed']+=int(grade['passed'])
   errors=grade.get('failures',[]);categories={bucket(str(e)) for e in errors}
   for category in categories:
    parts[category]+=1
    for counter in ctrs:counter['failure_'+category]+=1
   failures.update(errors)
   if categories=={'protocol'}:
    for counter in ctrs:counter['protocol_only_failures']+=1
   ok,lit_errors,positive=literal(entry['case'],answer)
   if ok is not None:
    for counter in ctrs:counter['text_contract_checked']+=1;counter['text_contract_passed']+=int(ok)
    if positive:
     row_positive.append(ok)
     for counter in ctrs:counter['positive_text_checked']+=1;counter['positive_text_passed']+=int(ok)
   else:
    for counter in ctrs:counter['text_not_asserted']+=1
   if row.get('exception'):sample_type='execution_exception'
   elif lit_errors:sample_type='text_contract_failure'
   elif 'evidence_identifier' in categories:sample_type='evidence_identifier_mismatch'
   elif categories=={'protocol'}:sample_type='protocol_only'
   elif 'retry' in mode:sample_type='model_retry'
   elif 'not_current' in mode:sample_type='not_current'
   elif 'clarification' in mode:sample_type='clarification'
   elif ok is True:sample_type='text_contract_pass'
   else:sample_type='not_content_asserted'
   if len(sample_groups[sample_type])<24 and key not in sample_seen[sample_type]:
    sample_seen[sample_type].add(key)
    sample_groups[sample_type].append({'result_file':file,'result_line':line,'key':key,'question':row['question'],'locale':language,'domain':domain,'mode':mode,'answer':answer,'case_id':entry['case'].get('id'),'corpus':entry['file'],'expected_contract':entry['case'].get('answer_contract') or {k:entry['case'][k] for k in ['must_contain','must_contain_any','must_contain_all_groups','must_not_contain','required_clauses','clauses','expected_answer_status'] if k in entry['case']},'raw_failures':errors,'text_failures':lit_errors,'decision_artifact':result.get('decision_artifact',{}),'source_hits':result.get('hits',[])})
  for counter in [totals,locales[language],domains[domain]]:
   counter['raw_passed_requests']+=int(bool(row_raw) and all(row_raw))
   if row_positive:counter['positive_text_checked_requests']+=1;counter['positive_text_passed_requests']+=int(all(row_positive))
 missing=sorted(set(selected)-seen);done=(root/'RUN_FINISHED.json').exists()
 complete=done and not missing and not duplicates and not unknown and totals['requests']==config['selected_requests'] and totals['grades']==config['selected_grades'] and not totals['missing_grade_results']
 if not args.partial and not complete:raise RuntimeError(f'Cannot write final report: complete={complete}, requests={len(seen)}, missing={len(missing)}')
 times.sort()
 def pct(n):return times[min(len(times)-1,int((len(times)-1)*n))] if times else None
 source=Path(config['source_installation']);db=source/'system/data/knowledge/common.sqlite'
 source_unchanged=hashlib.sha256(db.read_bytes()).hexdigest()==config['source_database_sha256']
 code_unchanged=all(hashlib.sha256((source/'system'/row['path']).read_bytes()).hexdigest()==row['sha256'] for row in config['source_manifest'])
 snapshot_unchanged=all(hashlib.sha256((S/row['path']).read_bytes()).hexdigest()==row['sha256'] for row in config['source_manifest'])
 test_db_unchanged=hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()==config['test_database_sha256']
 summary={'complete':complete,'only_format':'common','llm_enabled':True,'actual_model_inference_confirmed':models['http_transport_successes']>0 and models['audit_schema_accepted']>0,'selection':{k:v for k,v in config.items() if k!='source_manifest'},'totals':dict(totals),'by_effective_locale':dict(locales),'by_domain':dict(domains),'by_corpus':dict(corpora),'modes':dict(modes),'failed_grade_partitions':dict(parts),'model_transport_and_audits':dict(models),'model_retest_request_count':len(model_retest_keys),'wrong_explicit_english_locale':wrong_lang,'timing':{'scope':'four evaluator processes; includes grading; not single-user response SLA','p50_sec':pct(.5),'p95_sec':pct(.95),'p99_sec':pct(.99),'max_sec':times[-1] if times else None},'coverage':{'unique_result_keys':len(seen),'missing':missing,'duplicates':duplicates,'unknown_keys':unknown},'preservation':{'source_database_unchanged':source_unchanged,'source_application_files_unchanged':code_unchanged,'evaluation_application_matches_frozen_source':snapshot_unchanged,'evaluation_database_unchanged':test_db_unchanged}}
 report_json=R/('ANALYSIS_'+args.tag+'.json');samples_json=R/('FAILURE_SAMPLES_'+args.tag+'.json')
 with report_json.open('x',encoding='utf8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
 with samples_json.open('x',encoding='utf8') as f:json.dump(sample_groups,f,ensure_ascii=False,indent=2)
 with (R/('FAILURE_COUNTS_'+args.tag+'.json')).open('x',encoding='utf8') as f:json.dump(failures.most_common(),f,ensure_ascii=False,indent=2)
 with (R/('MODEL_RETEST_JOBS_'+args.tag+'.jsonl')).open('x',encoding='utf8') as f:
  for key in sorted(model_retest_keys):f.write(json.dumps(selected[key],ensure_ascii=False)+'\n')
 def ratio(c,n,d):return f"{c[n]:,}/{c[d]:,} ({100*c[n]/c[d]:.2f}%)" if c[d] else 'ไม่มีเกณฑ์ให้ตรวจ'
 lines=['# ผลทดสอบครึ่งชุด — Format กลาง / เปิด LLM / R70','',f"สถานะ: {'ครบชุดที่เลือก' if complete else 'ผลบางส่วน ยังไม่ครบ'}",'',f"เลือก {config['selected_requests']:,}/{config['population_requests']:,} คำถาม (50%) แบบแบ่งตามภาษา คลัง หมวด และรูปแบบคำถาม เก็บทุกเกณฑ์ที่ผูกกับคำถามที่เลือก รวม {config['selected_grades']:,} grades",'', '## ขอบเขต','', '- ใช้สำเนาแชทใหม่ R69 กับข้อมูล 602 รายการ เปิด LLM assistance ตลอดรอบ ไม่มีแขน Format เดิมหรือปิด LLM', '- เรียก pipeline จริงผ่าน subprocess ที่แยกกัน 4 ตัว จำกัดช่องเรียกโมเดลร่วมกัน 1 ช่อง ไม่มีการเร่งด้วยการแทนค่าคำตอบหรือเปลี่ยนตัวเลือกข้อมูล', '- สถานะจองเป็น controlled unavailable ไม่มีการยืนยันสถานะ WordPress สดหรือ browser/TCP ในรอบนี้', '- เกณฑ์เดิมยังอยู่ครบ การแยก protocol และตรวจข้อความเพิ่มเติมเป็นการวิเคราะห์ผล ไม่แก้ oracle เดิมให้คะแนนสูงขึ้น','', '## สรุปผล','',f"- คำถามที่ได้ผล: {totals['requests']:,}; grades: {totals['grades']:,}",f"- ผ่านเกณฑ์เดิมทุกข้อ: {ratio(totals,'raw_passed','grades')}",f"- ข้อสอบที่มีข้อความเชิงบวกต้องปรากฏและผ่าน: {ratio(totals,'positive_text_passed','positive_text_checked')}",f"- ข้อสอบที่ไม่ตรวจข้อความโดยตรง: {totals['text_not_asserted']:,} grades — ไม่นับเป็นหลักฐานว่าตอบครบ",f"- ไม่ผ่านเฉพาะชื่อ route/intent/protocol: {totals['protocol_only_failures']:,} grades",f"- exception: {totals['execution_exceptions']:,} คำถาม; คำตอบว่าง: {totals['empty_answers']:,}",'', '## แยกภาษา','', '| ภาษาในคำตอบ | คำถาม | ผ่านทุกเกณฑ์เดิม | ผ่านข้อความเชิงบวกที่กำหนด |','|---|---:|---:|---:|']
 for language,c in sorted(locales.items()):lines.append(f"| {language} | {c['requests']:,} | {ratio(c,'raw_passed','grades')} | {ratio(c,'positive_text_passed','positive_text_checked')} |")
 lines+=['','การผ่านข้อความเป็น literal/source contract ตามชุดทดสอบ ไม่ใช่การตรวจความหมายทุกประโยคโดยมนุษย์ ตัวเลข route mismatch ไม่เท่ากับจำนวนคำตอบผิดเนื้อหา และ literal mismatch บางรายการอาจเป็นตัวเลข/ถ้อยคำ/นโยบายใน oracle ที่ต้องตรวจเทียบแหล่งอีกครั้ง','', '## โมเดล','',f"- HTTP model attempts ที่สังเกตได้: {models['http_attempts']:,}",f"- transport สำเร็จ: {models['http_transport_successes']:,}; ล้มเหลว: {models['http_transport_failures']:,}",f"- audit ที่รับ schema ของโมเดล: {models['audit_schema_accepted']:,}",'- หาก transport/schema ยังไม่สำเร็จ ผลรอบนี้เป็น ON ภายใต้โมเดลไม่พร้อมใช้งาน ห้ามใช้รับรองคุณภาพ inference/การแปลของ LLM','', '## ประเภทความไม่ผ่าน','', '| ประเภท | grades ที่พบ |','|---|---:|']
 for name,count in parts.most_common():lines.append(f'| {name} | {count:,} |')
 lines+=['','แต่ละ grade อาจอยู่ได้หลายประเภท evidence_identifier เป็นการเทียบรหัสอ้างอิงตามชุดเดิม ต้องตรวจ lineage ก่อนสรุปว่าอ้างเกมผิดจริง ส่วน outcome ต้องแยกการจำแนก mode เก่าจากการปฏิเสธ/ขอรายละเอียดที่ผู้ใช้ได้รับจริง','', '## หมวดที่ควรตรวจต่อ','', '| หมวดจากชุดคำถาม | คำถาม | ผ่านข้อความเชิงบวก | ไม่ตรวจข้อความ |','|---|---:|---:|---:|']
 for name,c in sorted(domains.items(),key=lambda x:x[1]['positive_text_checked']-x[1]['positive_text_passed'],reverse=True):lines.append(f"| {name.replace('|','/')} | {c['requests']:,} | {ratio(c,'positive_text_passed','positive_text_checked')} | {c['text_not_asserted']:,} |")
 lines+=['','## การรักษาไฟล์','',f'- ฐานต้นทาง R69 ไม่เปลี่ยน: {source_unchanged}',f'- โค้ดต้นทาง R69 ไม่เปลี่ยน: {code_unchanged}',f'- โค้ดชุดทดสอบตรง snapshot: {snapshot_unchanged}',f'- ฐานชุดทดสอบไม่เปลี่ยน: {test_db_unchanged}','', '## หลักฐานอ่านต่อ','',f'- ANALYSIS_{args.tag}.json: คะแนนแยกภาษา/หมวด/คลังและ model diagnostics',f'- FAILURE_SAMPLES_{args.tag}.json: คำถาม คำตอบจริง เกณฑ์ที่คาด เหตุผลที่ไม่ผ่าน แผนเลือกข้อมูล และ sources',f'- FAILURE_COUNTS_{args.tag}.json: เหตุผลไม่ผ่านทั้งหมดพร้อมจำนวน',f'- {args.run}/RESULTS_*.jsonl.gz: คำตอบและ trace ของทุกคำถามที่รัน', '- SELECTED_JOBS.jsonl / STRATA.json / CONFIG.json: รายการเลือก วิธีแบ่ง และ hash ของข้อมูล/โค้ด']
 insert_at=lines.index('## แยกภาษา')
 lines[insert_at:insert_at]=['## นับระดับคำถามแยกจากจำนวนเกณฑ์','',f"- ผ่านทุกเกณฑ์เดิมของคำถามนั้น: {ratio(totals,'raw_passed_requests','requests')}",f"- คำถามที่มีเกณฑ์ข้อความเชิงบวก และผ่านเกณฑ์ข้อความเชิงบวกทุกแถวที่ผูกไว้: {ratio(totals,'positive_text_passed_requests','positive_text_checked_requests')}",'- คำถามเดียวอาจมีหลาย oracle/เกณฑ์จากหลายคลัง การนับ grades ให้น้ำหนักคำถามที่มีเกณฑ์ซ้ำมากกว่า จึงไม่ใช้ grades ผ่านแทนจำนวนคำถามที่ตอบถูก','- ทุกคำถามในรอบนี้เริ่มด้วย history ว่าง จึงไม่ได้รับรองการถามต่อหลายรอบจากผลชุดนี้','']
 insert_at=lines.index('## โมเดล')
 lines[insert_at:insert_at]=[f"จำนวนคำตอบอังกฤษที่พบอักษรไทย: {totals['english_thai_prose_flags']:,} คำถาม เป็น flags สำหรับตรวจ โดยรวมทั้งชื่อเฉพาะ หน่วยในชื่อบริการ และข้อความสถานะสองภาษา ไม่ใช่จำนวนประโยคที่แปลผิดทั้งหมด",'']
 lines+=['','## วิเคราะห์กรณีที่ตรวจย้อนกับฐานแล้ว','', '- อ่าน VERIFIED_FAILURE_ANALYSIS_R70_TH.md สำหรับกรณีวิธีจ่าย/เส้นตายชำระ ระเบียนชื่อเกมต่างการสะกด candidate ของกฎศูนย์ ช่วงวันปิด และภาษาอังกฤษที่ปนไทย',f"- MODEL_RETEST_JOBS_{args.tag}.jsonl มี {len(model_retest_keys):,} คำถามที่มีหลักฐาน transport/gate/retry ของโมเดลให้ตรวจต่อเมื่อเข้าถึงโมเดลได้ รายการนี้ไม่ได้ครอบคลุมทุกคำถามที่อาจได้ประโยชน์จาก LLM"]
 lines=[line.replace('ข้อสอบที่ไม่ตรวจข้อความโดยตรง:', 'ข้อสอบที่ไม่มี literal contract สำหรับตัวตรวจข้อความเพิ่มเติม:').replace('ไม่นับเป็นหลักฐานว่าตอบครบ','ยังไม่นับเป็นหลักฐานว่าตอบครบ แม้ native grader อาจตรวจ source/outcome หรือเงื่อนไขอื่นอยู่').replace('ไม่ตรวจข้อความ |','ไม่มี literal เพิ่มเติม |') for line in lines]
 with (R/('REPORT_'+args.tag+'_TH.md')).open('x',encoding='utf8') as f:f.write('\n'.join(lines)+'\n')
 print(json.dumps({'complete':complete,'totals':totals,'models':models,'preservation':summary['preservation']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
