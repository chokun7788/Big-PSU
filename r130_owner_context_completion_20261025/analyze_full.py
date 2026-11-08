"""Streaming retained-workload audit. Literal mismatches are not semantic gold."""
import collections,gzip,hashlib,json,os,statistics,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;OUT=R/'full_analysis';OUT.mkdir(exist_ok=False)
def load(p):return json.loads(Path(p).read_text('utf-8-sig'))
def write(n,v):(OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
jobs=[json.loads(s) for s in (R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl').read_text('utf8').splitlines()]
expected={x['key']:collections.Counter((e['file'],e['row'],e['variant']) for e in x['entries']) for x in jobs};assert len(expected)==20554 and sum(sum(c.values()) for c in expected.values())==55811
def grade_id(g):return g['file'],g['row'],g['variant']
def rate(v,n):return round(100*v/n,4) if n else None
baseline={};base=R.parent/'r95_merged_flow_implementation_20261018/full01'
for path in sorted(base.glob('RESULTS_*.jsonl.gz')):
 with gzip.open(path,'rt',encoding='utf8') as f:
  for line in f:
   row=json.loads(line)
   baseline[row['key']]={grade_id(g):bool(g['passed']) for g in row.get('grades',[])}
seen=collections.Counter();missing_grades=[];extra_grades=[];scores=collections.defaultdict(collections.Counter);groups=collections.Counter();examples=collections.defaultdict(list);latencies=[];regressions=[];improvements=[];fatal_requests=[];model=collections.Counter();semantic=collections.Counter();actual=0;grade_total=0
def classify(reason):
 s=str(reason).casefold()
 if s.startswith(('route','intent','legacy_mode','forbidden_category','mode:')):return 'protocol_mismatch'
 if 'latency' in s or 'timeout' in s:return 'performance'
 if any(k in s for k in ['keyword','must_contain','required_clause','first_line','first-line','complete_clause','complete-clause','missing text','missing phrase','missing_clause','clause']):return 'keyword_firstline_clause_mismatch_review_required'
 if any(k in s for k in ['validation','pipeline_exception','grader_exception']):return 'execution_or_reference_validation'
 if any(k in s for k in ['source','evidence','retrieval','rulebook target']):return 'source_id_or_evidence_requirement_review_required'
 if s.startswith(('status','outcome')):return 'outcome_mismatch_review_required'
 return 'literal_or_reference_contract_review_required'
with gzip.open(OUT/'PER_REQUEST_ANALYSIS.jsonl.gz','xt',encoding='utf8') as per,gzip.open(OUT/'ALL_FAILURES.jsonl.gz','xt',encoding='utf8') as failures:
 for path in sorted((R/'full01').glob('RESULTS_*.jsonl.gz')):
  with gzip.open(path,'rt',encoding='utf8') as f:
   for line in f:
    row=json.loads(line);key=row['key'];seen[key]+=1;grade_total+=len(row.get('grades',[]));observed=collections.Counter(grade_id(g) for g in row.get('grades',[]));exp=expected.get(key,collections.Counter())
    if observed!=exp:
     missing_grades.extend({'key':key,'grade':list(k),'count':n} for k,n in (exp-observed).items());extra_grades.extend({'key':key,'grade':list(k),'count':n} for k,n in (observed-exp).items())
    result=row.get('result') or {};art=result.get('decision_artifact') or {};contract=art.get('execution_contract') or {};ledgers=contract.get('tasks',[]);response=result.get('answer','');category=','.join(art.get('domain_flow',{}).get('categories',[])) or str(result.get('route',{}).get('category','unknown'))
    language=row.get('requested_locale','unknown');counter=scores[language];counter['requests']+=1;reason_groups=set();positive_failed=False;strict_failed=False
    for g in row.get('grades',[]):
     counter['grades']+=1;counter['strict_passed']+=int(g['passed']);strict_failed|=not g['passed']
     if g.get('positive_text_contract'):
      counter['positive_literal_grades']+=1
      content=(g.get('partitions') or {}).get('content',[])
      passed=not content;counter['positive_literal_passed']+=int(passed);positive_failed|=not passed
     if not g['passed']:
      gs={classify(reason) for reason in g.get('failures',[])};reason_groups|=gs
      record={'key':key,'question':row['question'],'locale':language,'category':category,'answer':response,'grade':g,'groups':sorted(gs),'actual_content_failure_confirmed':False,'semantic_status':'review_required','source_receipts':ledgers}
      failures.write(json.dumps(record,ensure_ascii=False)+'\n')
     old=baseline.get(key,{}).get(grade_id(g))
     if old is not None:
      counter['paired_r95_grades']+=1;counter['r95_strict_passed']+=int(old)
      if old and not g['passed']:regressions.append({'key':key,'grade':list(grade_id(g)),'failures':g.get('failures',[])})
      if not old and g['passed']:improvements.append({'key':key,'grade':list(grade_id(g))})
    for ledger in ledgers:
     state=ledger.get('terminal_state','unknown');counter['terminal_'+state]+=1
     if ledger.get('fatal'):fatal_requests.append({'key':key,'fatal':ledger['fatal'],'delivered_answer':response,'blocked_output_not_automatically_wrong_answer':True});reason_groups.add('source_verifier_rejection')
     if state in {'missing_source','not_current','conflict'}:reason_groups.add('source_gap_validity_or_conflict_review_required')
     if state=='provider_unavailable':reason_groups.add('controlled_provider_unavailable')
     if state=='budget_exhausted':reason_groups.add('request_budget_exhausted')
     if state=='unsupported_operation':reason_groups.add('unsupported_operation')
    for call in row.get('observed_model_http_calls',[]):model['attempts']+=1;model['transport_successes']+=int(call['transport_ok'])
    for event in art.get('domain_flow',{}).get('model_events',[]):
     if event.get('transport_ok') and event.get('schema_ok') is False:model['transport_ok_protocol_failed']+=1;reason_groups.add('model_protocol_failure')
    if row.get('exception'):counter['execution_exceptions']+=1;reason_groups.add('execution_exception')
    if row.get('elapsed_sec') is not None:latencies.append(row['elapsed_sec'])
    # A fulfilled structural ledger does not prove semantic answer correctness.
    review=bool(reason_groups or strict_failed);semantic['review_required' if review else 'structural_checks_passed_semantics_unadjudicated']+=1
    for group in reason_groups:
     groups[group]+=1
     if len(examples[group])<12:examples[group].append({'key':key,'question':row['question'],'locale':language,'answer':response,'category':category,'source_receipts':ledgers,'query_plan':art.get('query_plan'),'understanding':art.get('understanding')})
    per.write(json.dumps({'key':key,'question':row['question'],'requested_locale':language,'effective_locale':row.get('effective_locale'),'category':category,'strict_failed':strict_failed,'positive_literal_failed':positive_failed,'groups':sorted(reason_groups),'semantic_status':'review_required' if review else 'unadjudicated','actual_content_failure_confirmed':False,'source_verifier_fatal':any(t.get('fatal') for t in ledgers),'actual_model_http_calls':len(row.get('observed_model_http_calls',[])),'raw_results_file':path.name},ensure_ascii=False)+'\n')
missing=sorted(set(expected)-set(seen));extra=sorted(set(seen)-set(expected));duplicates={k:n for k,n in seen.items() if n!=1};unchanged=all(sha(p)==h for p,h in load(R/'EXECUTION_FREEZE_R130.json').items())
identity=load(R/'MODEL_IDENTITY_BEFORE.json')['profile_digests']==load(R/'MODEL_IDENTITY_AFTER.json')['profile_digests']
logical_source_unchanged=load(R/'SOURCE_SNAPSHOT_BEFORE.json')==load(R/'SOURCE_SNAPSHOT_AFTER.json')
assert logical_source_unchanged,'Logical source changed, including potential WAL changes'
coverage={'expected_unique_requests':20554,'actual_unique_requests':len(seen),'expected_grades':55811,'actual_grades':grade_total,'missing_keys':missing,'extra_keys':extra,'duplicate_keys':duplicates,'missing_grades':missing_grades,'extra_or_duplicate_grades':extra_grades,'source_inputs_unchanged':unchanged,'model_identity_verified':identity}
complete=not any([missing,extra,duplicates,missing_grades,extra_grades]) and len(seen)==20554 and grade_total==55811 and unchanged and identity;coverage['complete']=complete;write('COVERAGE.json',coverage);assert complete,'Full coverage/source/model validation failed'
for locale,c in scores.items():c['strict_percent']=rate(c['strict_passed'],c['grades']);c['positive_literal_percent']=rate(c['positive_literal_passed'],c['positive_literal_grades']);c['paired_r95_strict_percent']=rate(c['r95_strict_passed'],c['paired_r95_grades'])
write('SCORES.json',dict(scores));write('FAILURE_GROUPS.json',{'request_groups_overlap':True,'groups':dict(groups),'examples':dict(examples),'semantic_status_counts':dict(semantic),'actual_content_failure_count':None,'source_verifier_rejections':fatal_requests,'not_all_keyword_failures_are_content_failures':True});write('REGRESSIONS_VS_R95.json',{'same_saved_keys_no_baseline_rerun':True,'source_data_versions_differ':True,'deadline_profiles_differ':True,'causal_flow_effect':False,'regressions':regressions,'improvements':improvements})
latencies.sort();write('MODEL_TRANSPORT_AND_LATENCY.json',{'model_http':dict(model),'requests':len(latencies),'median_sec':statistics.median(latencies),'p95_sec':latencies[min(len(latencies)-1,int(len(latencies)*.95))],'model_transport_is_not_answer_accuracy':True})
report=['# ผล Full Test R130 — Flow กลาง / LLM ON','','ครบ 20,554 unique request keys และ 55,811 grades; ไม่มี key/grade ขาดหรือซ้ำ ตรวจ source/input และ model identity แล้ว','', '## คะแนนตามเกณฑ์เดิม','','| ภาษา request | Strict ผ่าน/ทั้งหมด | Strict % | Positive literal ผ่าน/มีเกณฑ์ | Literal % | Saved R95 strict % |','|---|---:|---:|---:|---:|---:|']
for locale,c in sorted(scores.items()):report.append(f"| {locale} | {c['strict_passed']}/{c['grades']} | {c['strict_percent']} | {c['positive_literal_passed']}/{c['positive_literal_grades']} | {c['positive_literal_percent']} | {c['paired_r95_strict_percent']} |")
report+=['','Strict เป็นผล grader เดิม ส่วน positive literal ตรวจเฉพาะสัญญาข้อความด้านบวก ไม่ใช่ semantic accuracy ทั้งสองค่าไม่ยืนยันว่าตอบถูกครบทุกข้อ','', '## กลุ่มที่ต้องวิเคราะห์','','| กลุ่ม | Requests (ซ้อนทับได้) |','|---|---:|',*[f'| {k} | {v} |' for k,v in groups.most_common()],'','## ขอบเขตการเปรียบเทียบ','','- เทียบ saved R95 ด้วย keys และ grade identities เดียวกัน ไม่รัน baseline ใหม่','- ข้อมูลของ R130 กับ R95 ต่างรุ่น และ deadline ต่างกัน จึงไม่ใช่ causal effect ของ Flow หรือน้ำหนักโมเดลเพียงอย่างเดียว','- workload ควบคุม live provider เป็น unavailable; ไม่ใช่ผลยืนยันสถานะจริง WordPress','- candidate ยังไม่ติดตั้งทับ R78','- API readiness และการตรวจ source lifecycle เป็น implementation gates แยกจากผลความแม่นยำ','', '## การตรวจ semantic','','ยังต้องตรวจ ROOT_CAUSE_REVIEW_TH.md โดยอ้าง raw responses และ source evidence ทุกกลุ่ม ข้อที่ตัดสินไม่ได้คง review_required ไม่เหมารวม keyword/clause fail เป็นคำตอบผิดจริง','', '## หลักฐาน','','- COVERAGE.json','- SCORES.json','- ALL_FAILURES.jsonl.gz','- PER_REQUEST_ANALYSIS.jsonl.gz','- FAILURE_GROUPS.json','- REGRESSIONS_VS_R95.json','- MODEL_TRANSPORT_AND_LATENCY.json']
(OUT/'FINAL_REPORT_TH.md').write_text('\n'.join(report)+'\n','utf8')
review=['# Root cause review R130','','สถานะ: ต้อง adjudicate ตัวอย่างและ source ต่อหลัง streaming audit; ไฟล์นี้ไม่ใช่คำยืนยันว่าแก้ครบหรือ semantic ถูกครบ','', 'ทุก request และ grade ถูกอ่านแบบ streaming แล้ว กลุ่มด้านล่างอาจซ้อนทับกัน ไม่มีการใช้โมเดลผู้ตอบเป็น judge และไม่มีการแปลง keyword fail เป็น actual content failure อัตโนมัติ','']
for group,n in groups.most_common():
 review += [f'## {group} — {n} requests','','การวินิจฉัย semantic: review_required; ต้องเทียบ question/current source/execution plan ไม่ใช้คะแนนคำตรงเพียงอย่างเดียว','']
 for ex in examples[group][:4]:review += [f"### {ex['key']}",'',f"คำถาม: {ex['question']}",'','คำตอบที่เก็บไว้:','',ex['answer'],'','หลักฐาน source/receipts อยู่ใน FAILURE_GROUPS.json ภายใต้ key นี้ พร้อม raw RESULTS และ query plan','']
(OUT/'ROOT_CAUSE_REVIEW_TH.md').write_text('\n'.join(review),'utf8')
write('ANALYSIS_FINAL.json',{'streaming_audit_complete':True,'coverage_verified':True,'human_agent_root_cause_review_complete':False,'semantic_accuracy':None,'all_failure_groups_streamed':True,'full_test_complete':True,'overall_task_complete':False})
(R/'FULL_TEST_COMPLETE.json').write_text(json.dumps({'complete':True,'unique_request_keys':20554,'grades':55811,'source_inputs_unchanged':True,'model_identity_verified':True,'full_analysis':str(OUT),'root_cause_review_pending':True},indent=2),'utf8');print(json.dumps({'coverage_complete':True,'root_review_pending':True,'groups':dict(groups)}))
