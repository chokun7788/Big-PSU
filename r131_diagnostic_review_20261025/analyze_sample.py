"""Exact selected-key comparison of one fresh run to saved outputs only."""
import collections,gzip,json,statistics,time
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;P=B/'r130_owner_context_completion_20261025'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def lines(p):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for line in f:yield json.loads(line)
assert load(R/'EXECUTION_COMPLETE.json')['complete']
jobs={x['key']:x for x in map(json.loads,(R/'SELECTED_JOBS.jsonl').open(encoding='utf8'))}
membership=load(R/'CATEGORY_MEMBERSHIP.json')['members'];allocation=load(R/'SAMPLE_ALLOCATION.json');identities={};eligible={}
for key,j in jobs.items():
 identities[key]={(e['file'],e['row'],e['variant']) for e in j['entries']}
 for e in j['entries']:
  c=e['case'];contract=c.get('answer_contract') or c
  eligible[(key,e['file'],e['row'],e['variant'])]=bool(c.get('required_clauses') or c.get('clauses') or any(contract.get(k) for k in ['must_contain','must_contain_any','must_contain_all_groups']))
arms={'R64_saved':[B/'r129_full_plan_completion_20261024/SAVED_LEGACY_ROWS.jsonl.gz'],'R95_saved':sorted((B/'r95_merged_flow_implementation_20261018/full01').glob('RESULTS_*.jsonl.gz')),'R130_saved':sorted((P/'full01').glob('RESULTS_*.jsonl.gz')),'R130_repeat_10pct':sorted((R/'sample01').glob('RESULTS_*.jsonl.gz'))}
locales={};categories={};flags={};answers={};responses={};coverage={};latencies=[];gateway=collections.Counter();gateway_errors=[];http=collections.Counter();new_rows={};actual_mechanisms=collections.defaultdict(set)
for arm,paths in arms.items():
 ls=collections.defaultdict(collections.Counter);cs=collections.defaultdict(collections.Counter);seen=set();f={};ans={};resp={}
 for p in paths:
  for row in lines(p):
   key=row['key']
   if key not in jobs:continue
   assert key not in seen,(arm,key);seen.add(key);j=jobs[key];loc=j['locale'];cats=membership[key]['categories'];actual=set()
   ls[loc]['requests']+=1
   for cat in cats:cs[cat]['requests']+=1
   for g in row['grades']:
    gid=g['file'],g['row'],g['variant'];assert gid not in actual;(actual.add(gid));full=(key,*gid);is_eligible=eligible[full]
    lit=None
    if is_eligible and not (row.get('exception') or any('pipeline_exception' in str(s) or 'grader_exception' in str(s) for s in g.get('failures',[]))):
     if isinstance(g.get('content_checks_passed'),bool):lit=g['content_checks_passed']
     elif isinstance(g.get('partitions'),dict):lit=not g['partitions'].get('content',[])
    f[full]={'strict':bool(g['passed']),'literal':lit,'eligible':is_eligible}
    for count in [ls[loc],*[cs[c] for c in cats]]:
     count['grades']+=1;count['strict_passed']+=int(g['passed'])
     if is_eligible:count['literal_eligible']+=1;count['literal_unassessed' if lit is None else 'literal_passed' if lit else 'literal_failed']+=1
   assert actual==identities[key],(arm,key,'grade_identity_mismatch')
   result=row.get('result') or {};a=result.get('decision_artifact') or {};ans[key]=result.get('answer');resp[key]=a.get('response_type',result.get('route',{}).get('answer_type'))
   if arm=='R130_repeat_10pct':
    new_rows[key]=row;latencies.append(row['elapsed_sec'])
    for c in row.get('observed_model_http_calls',[]):http['attempts']+=1;http['header_transport_ok']+=int(c['transport_ok'])
    for e in (a.get('request_context') or {}).get('events',[]):
     if e.get('stage')!='R129_model_gateway':continue
     gateway['attempts']+=1
     if not e.get('transport_ok'):actual_mechanisms['gateway_transport_failure'].add(key);continue
     gateway['transport_successes']+=1;prov=e.get('returned_provenance') or {};stage=e.get('model_stage');profile='retained' if stage=='context_understanding' else 'base';h=load(R/'MODEL_BEFORE.json')
     checks={'profile':prov.get('effective_profile')==profile,'adapter':prov.get('adapter_sha256')==h['profiles'][profile],'profile_digest':prov.get('profile_digest')==h['profile_digests'][profile],'base_revision':prov.get('base_revision')==h['base_revision'],'messages':prov.get('effective_messages_sha256')==e.get('wire_messages_sha256'),'schema':prov.get('effective_schema_sha256')==e.get('schema_sha256'),'stage':prov.get('stage')==stage,'precision':prov.get('quantization')==h['quantization'],'model':e.get('model')==h['model']}
     if not all(checks.values()):gateway_errors.append({'key':key,'checks':checks})
     else:gateway['verified_'+profile]+=1
    events=list((a.get('domain_flow') or {}).get('model_events',[]));u=(a.get('understanding') or {}).get('event')
    if u:events.append(u)
    for e in events:
     if 'model_admission_unavailable' in str(e.get('error')):actual_mechanisms['model_admission_denied'].add(key)
     if e.get('transport_ok') and e.get('schema_ok') is False:actual_mechanisms['schema_or_version_rejection'].add(key)
    for t in (a.get('execution_contract') or {}).get('tasks',[]):
     for code in t.get('reason_codes') or []:
      if code in ['requested_hardware_component_not_recorded','substantive_clause_not_delivered','requested_field_not_delivered']:actual_mechanisms[code].add(key)
    if a.get('live_booking'):actual_mechanisms['controlled_live_artifact'].add(key)
 for counts in [ls,cs]:
  for c in counts.values():
   c['strict_percent']=100*c['strict_passed']/c['grades'] if c['grades'] else None
   c['literal_percent_fixed_denominator']=100*c['literal_passed']/c['literal_eligible'] if c['literal_eligible'] else None
   assert c['literal_passed']+c['literal_failed']+c['literal_unassessed']==c['literal_eligible']
 assert seen==set(jobs),(arm,'missing_keys',set(jobs)-seen)
 locales[arm]=dict(ls);categories[arm]=dict(cs);flags[arm]=f;answers[arm]=ans;responses[arm]=resp;coverage[arm]={'unique_keys':len(seen),'grade_identities':len(f),'missing_or_duplicate_keys':0,'missing_or_duplicate_grade_identities':0}
assert not gateway_errors,gateway_errors
comp={}
for arm in ['R64_saved','R95_saved','R130_saved']:
 c=collections.Counter()
 for identity,new in flags['R130_repeat_10pct'].items():
  old=flags[arm][identity];c['strict_old_only']+=old['strict'] and not new['strict'];c['strict_repeat_only']+=not old['strict'] and new['strict'];c['strict_both']+=old['strict'] and new['strict']
  if new['eligible']:
   if old['literal'] is None or new['literal'] is None:c['literal_unassessed_in_either']+=1
   else:c['literal_old_only']+=old['literal'] and not new['literal'];c['literal_repeat_only']+=not old['literal'] and new['literal'];c['literal_both']+=old['literal'] and new['literal']
 comp[arm]=dict(c)
changes=[];same=0
for key in jobs:
 old=answers['R130_saved'][key];new=answers['R130_repeat_10pct'][key]
 if old==new:same+=1
 else:changes.append({'key':key,'question':jobs[key]['question'],'categories':membership[key]['categories'],'old_answer':old,'new_answer':new,'old_response':responses['R130_saved'][key],'new_response':responses['R130_repeat_10pct'][key],'semantic_change':'review_required','no_runtime_fix':True})
write('REPEAT_ANSWER_CHANGES.json',{'same_answer_count':same,'changed_answer_count':len(changes),'changes':changes,'changed_answer_does_not_imply_improvement':True})
reviews={c['key']:c for c in load(R/'INDIVIDUAL_SOURCE_REVIEW.json')['cases']};audit=[]
for key in sorted(set(reviews)&set(jobs)):
 old=reviews[key];exact=answers['R130_repeat_10pct'][key]==old['answer'];audit.append({'key':key,'question':jobs[key]['question'],'previous_decision':old['decision'],'previous_root_cause':old['root_cause_code'],'exact_answer_reproduced':exact,'source_unchanged':True,'new_semantic_status':'previous_source_review_applies_to_exact_same_answer_and_input' if exact else 'new_answer_review_required','answer':answers['R130_repeat_10pct'][key]})
write('KNOWN_CASE_REPRODUCTION.json',{'cases':audit,'reviewed_keys_in_random_sample':len(audit),'exact_answer_reproduced':sum(x['exact_answer_reproduced'] for x in audit),'semantic_accuracy':None})
latencies.sort();lat={'median_sec':statistics.median(latencies),'p95_sec':latencies[int(len(latencies)*.95)],'p99_sec':latencies[int(len(latencies)*.99)],'max_sec':max(latencies),'above_20_sec':sum(x>20 for x in latencies)}
write('SCORES.json',{'by_requested_locale':locales,'by_input_category_overlapping':categories,'same_grade_identity_comparison':comp,'semantic_accuracy':None,'baseline_inferences':0,'baseline_regrading':0,'runtime_fixes':0,'not_post_fix_improvement':True})
write('COVERAGE.json',{'complete':True,'expected_requests':len(jobs),'expected_grade_identities':len(eligible),'arms':coverage,'source_input_model_identity_verified':True})
write('MODEL_AND_MECHANISM_AUDIT.json',{'gateway':dict(gateway),'provenance_errors':gateway_errors,'observed_http':dict(http),'mechanisms':{k:{'unique_requests':len(v),'keys':sorted(v)} for k,v in actual_mechanisms.items()},'latency':lat,'counts_are_mechanisms_not_semantic_errors':True})
out=['# ผลทดสอบ10%หลังวินิจฉัยข้อ2 — R131','',f"วินิจฉัยก่อนทดสอบเสร็จแล้ว ตามDIAGNOSIS_PRETEST_COMPLETE.json รันคำถามเดิม{len(jobs)}keys/{len(eligible)}grade identities ครบทุกตัว ไม่มีขาดหรือซ้ำ source/input/code/prompt/weights/modelprovenanceไม่เปลี่ยน",'',
 'รอบนี้ใช้candidateR130เดิม ไม่มีการแก้Flowหรือฝึกโมเดลใหม่ จึงวัดการเกิดซ้ำและผลของเส้นทางทำงาน/คิว ไม่ใช่ผลปรับปรุงคุณภาพหลังfix ไม่ใช้คะแนนต่างจากsavedrunมาอ้างว่าระบบดีขึ้นเอง','',
 '## คะแนนภาษา — strictและpositive literalแยกจากsemantic','', '| แขน | ภาษา | Strict | Literal ผ่าน/eligible | Literal% | Unassessed |','|---|---|---:|---:|---:|---:|']
for arm,ls in locales.items():
 for loc,c in sorted(ls.items()):out.append(f"| {arm} | {loc} | {c['strict_passed']}/{c['grades']} ({c['strict_percent']:.2f}%) | {c['literal_passed']}/{c['literal_eligible']} | {c['literal_percent_fixed_denominator']:.2f} | {c['literal_unassessed']} |")
out+=['','## ทุกหมวดตามinput — คำถามหลายหมวดซ้อนทับได้','', '| หมวด | จำนวนคำถาม | Strict% | Literal ผ่าน/eligible | Literal% |','|---|---:|---:|---:|---:|']
for a in allocation['categories']:
 c=categories['R130_repeat_10pct'][a['category']];pct=f"{c['literal_percent_fixed_denominator']:.2f}" if c['literal_percent_fixed_denominator'] is not None else 'ไม่มีกติกาข้อความด้านบวก'
 out.append(f"| {a['category']} {a['name_th']} | {c['requests']} | {c['strict_percent']:.2f} | {c['literal_passed']}/{c['literal_eligible']} | {pct} |")
out+=['','C07มีประชากรในFullเดิม6คำถาม เลือก1ตามceil10% และส่วนใหญ่เป็นoffsite ยังสรุปราคาเหมาonsiteทุกoperationไม่ได้ C14ข้อมูลnewsจริงไม่มี sourcegapต้องแยกจากruntimefailure ไม่เอาจำนวนsampleน้อยไปอ้างหมวดผ่าน100%','',
 f"คำตอบเหมือนsavedR130เดิม{same}keys เปลี่ยน{len(changes)}keys ดูREPEAT_ANSWER_CHANGES.json ทุกความต่างยังต้องตรวจความหมาย ไม่ถือchanged=ดีขึ้น",'',
 '## Model/latency/กลไกที่เกิดซ้ำ','',json.dumps({'gateway':dict(gateway),'http':dict(http),'latency':lat,'mechanisms':{k:len(v) for k,v in actual_mechanisms.items()}},ensure_ascii=False,indent=2),'',
 'ใช้contextretained R121adapterบนengine/dataR130 ส่วนselector/genericใช้base Modelpsu-r129:latestคือTyphoon2.5Qwen3-4B HFNF4BF16 ไม่มีการpromoteadapterใหม่ controlledliveunavailableไม่ใช่providerจริงไม่พร้อม','',
 'การเทียบsavedR64/R95มีsource/backend/precision/clock/deadlineconfoundsและไม่ใช่causalFloweffect ไม่มีbaselineinference/regradingใหม่ sourcecaseที่ยังไม่ตัดสินคงreview_required Candidateไม่ติดตั้งทับR78','',
 '## หลักฐาน','', '- ITEM02_DETAILED_DIAGNOSIS_TH.md / INDIVIDUAL_SOURCE_REVIEW.json','- CASE_DIAGNOSTICS_REVIEWED.jsonl.gz / ROOT_CAUSE_REGISTER.json','- SOURCE_CAUSAL_EVIDENCE.json / DETERMINISTIC_CAUSAL_PROBES.json','- SELECTION_FREEZE.json / SAMPLE_ALLOCATION.json / RUN_FREEZE.json','- sample01/RESULTS_*.jsonl.gz / COVERAGE.json / SCORES.json','- EXECUTION_COMPLETE.json / MODEL_AND_MECHANISM_AUDIT.json / KNOWN_CASE_REPRODUCTION.json']
(R/'SAMPLE10_FINAL_REPORT_TH.md').write_text('\n'.join(out)+'\n','utf8')
write('ANALYSIS_COMPLETE.json',{'complete':True,'sample_coverage_verified':True,'source_input_weights_unchanged':True,'actual_gateway_provenance_verified':True,'baseline_reruns':0,'runtime_fixes':0,'semantic_accuracy':None,'changed_answer_semantic_review_pending':True,'flow_quality_acceptance_complete':False,'completed_at':time.time()})
write('STATUS.json',{'phase':'sample_execution_and_mechanism_analysis_complete_changed_answer_review_pending','complete':False,'diagnosis_complete':True,'sample_complete':True,'sample_requests':len(jobs),'sample_grades':len(eligible),'production_installed':False,'updated_at':time.time()})
print(json.dumps({'coverage':coverage,'repeat_answer_changes':len(changes),'same':same,'mechanisms':{k:len(v) for k,v in actual_mechanisms.items()},'latency':lat},ensure_ascii=False))
