"""Supplemental source reconciliation, streaming saved evidence only."""
import collections,gzip,json,re,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent.parent;R=B/'r106_complete_flow_20261020';O=R/'full_analysis'
def dump(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str),'utf8')
samples=json.loads((O/'REVIEW_GROUP_SAMPLES.json').read_text('utf8'))
c=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
records={k:json.loads(p) for k,p in c.execute('select h.record_id,r.payload from cc_heads h join cc_revisions r on r.record_id=h.record_id and r.version=h.head where h.withdrawn=0')}
sources={k:{'payload':json.loads(p),'snapshot':s} for k,p,s in c.execute('select source_id,payload,snapshot from cc_sources')}
methods=collections.Counter();statuses=collections.Counter();reason_keys=collections.defaultdict(set);method_samples={};ambiguous=[];selected={x['key'] for v in samples.values() for x in v}
part_keys=collections.defaultdict(set);wrong_evidence_zero=collections.Counter();failure_rows=0
with gzip.open(O/'ALL_FAILURES.jsonl.gz','rt',encoding='utf8') as f:
 for line in f:
  x=json.loads(line);failure_rows+=1;key=x['key'];q=x['query_plan'] or {};method=q.get('method') or 'none';methods[method]+=1
  for n in x['need_results'] or []:
   status=n.get('status') or 'unknown';task=n.get('task') or 'unresolved';statuses[task+' | '+status]+=1
   for reason in n.get('reason_codes') or []:reason_keys[reason].add(key)
  for g in x['grades']:
   for part,values in (g.get('partitions') or {}).items():
    if values:part_keys[part].add(key)
  if len(method_samples.setdefault(method,[]))<2:
   method_samples[method].append({'key':key,'q':x['question'],'a':(x['answer'] or '')[:2000],'record_ids':q.get('record_ids'),'needs':[{'task':n.get('task'),'status':n.get('status'),'reasons':n.get('reason_codes')} for n in x['need_results'] or []]});selected.add(key)
  if any(any(t in str(v) for t in ('wrong_game_source','wrong_game_evidence')) for g in x['grades'] for v in g.get('failures',[])):
   selected.add(key) if len(ambiguous)<4 else None
   if len(ambiguous)<4:ambiguous.append(key)
dump('REVIEW_FAILURE_METHODS.json',{'failed_requests':failure_rows,'methods':methods.most_common(),'task_statuses':statuses.most_common(),'distinct_requests_by_partition':{k:len(v) for k,v in part_keys.items()},'distinct_requests_by_need_reason':{k:len(v) for k,v in reason_keys.items()},'samples':method_samples})
selected_rows=[];latency=[];missing_positive_exceptions=[];jobs={}
for line in (B/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl').open(encoding='utf8'):
 j=json.loads(line);jobs[j['key']]=j
def positive(case):
 con=case.get('answer_contract') or case
 return bool(case.get('required_clauses') or case.get('clauses') or any(con.get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')))
cohorts=collections.defaultdict(collections.Counter);out_scope=collections.Counter();out_examples=[];model_errors=collections.Counter();needs_samples={}
for path in sorted((R/'full01').glob('RESULTS_*.jsonl.gz')):
 with gzip.open(path,'rt',encoding='utf8') as f:
  for line in f:
   x=json.loads(line);res=x.get('result') or {};art=res.get('decision_artifact') or {};hits=res.get('hits') or [];key=x['key'];gs=x.get('grades',[])
   for call in x.get('observed_model_http_calls',[]):
    if not call.get('transport_ok'):model_errors[(call.get('error_type') or 'unknown')+' | '+str(call.get('error'))]+=1
   if key in selected:
    ids=list(dict.fromkeys((art.get('query_plan') or {}).get('record_ids',[])+[h.get('record_id') for h in hits if isinstance(h,dict) and h.get('record_id')]))
    selected_rows.append({'key':key,'question':x['question'],'answer':res.get('answer'),'mode':res.get('mode'),'route':res.get('route'),'validation':res.get('validation'),'elapsed_sec':x.get('elapsed_sec'),'hit_count':len(hits),'hits':hits,'records':{k:records.get(k) for k in ids},'query_plan':art.get('query_plan'),'needs':[{'task':n.get('task'),'status':n.get('status'),'reason_codes':n.get('reason_codes')} for n in art.get('need_results') or []],'request_plan':art.get('request_plan'),'grades':gs,'model_calls':x.get('observed_model_http_calls',[]),'job':jobs[key]})
   if any(any(v=='latency_ceiling' for v in g.get('failures',[])) for g in gs):latency.append({'key':key,'q':x['question'],'elapsed':x.get('elapsed_sec'),'grade_fail_count':sum('latency_ceiling' in g.get('failures',[]) for g in gs)})
   for g,e in zip(gs,jobs[key]['entries']):
    tag=e['case'].get('group') or e['case'].get('domain') or e['case'].get('suite') or e['file'];row=cohorts[tag];row['grades']+=1;row['strict_pass']+=bool(g.get('passed'))
    pos=positive(e['case']);row['positive_expected']+=pos
    row['positive_pass_including_execution_failures']+=pos and not x.get('exception') and not any((g.get('partitions') or {}).get(t) for t in ('content','evidence','validation','grader'))
    if x.get('exception') and pos:missing_positive_exceptions.append({'key':key,'grade_id':g.get('id'),'locale':x.get('requested_locale')})
   if any((e['case'].get('group') or '')=='general_llm' for e in jobs[key]['entries']):
    out_scope[res.get('mode') or 'exception']+=1
    if len(out_examples)<8:out_examples.append({'key':key,'q':x['question'],'a':(res.get('answer') or '')[:700]})
dump('REVIEW_SELECTED_RAW_AND_SOURCES.json',selected_rows)
dump('REVIEW_ADDITIONAL_COUNTS.json',{'cohorts':cohorts,'general_llm_request_modes':out_scope,'general_llm_examples':out_examples,'model_transport_error_types':model_errors,'actual_latency_ceiling_requests':latency,'positive_execution_failures_excluded_by_original_metric':missing_positive_exceptions})
# Explicit source records relevant to reviewed defects/gaps, with their source payloads.
ids=['competition_competition_rules_cs2_psu_phuket_2026_section_034','competition_competition_rules_cs2_psu_phuket_2026_section_043','competition_competition_rules_cs2_psu_phuket_2026_section_046','competition_competition_rules_cs2_psu_phuket_2026_section_047','competition_competition_rules_valorant_psu_phuket_2026_section_006','member_1d884f11f3890dea','migrated_rate_vr_60_1_5_psu_student_staff','rate_recovered_pc_availability_pc_01_02_psu_student_staff','migrated_schedule_0','migrated_schedule_4','equipment_gaming_pc','controls_ps5_it_takes_two']
sourceids={ref['source_id'] for rid in ids if rid in records for field in records[rid]['fields'].values() for ref in field.get('evidence_refs',[])}
dump('REVIEW_SOURCE_EVIDENCE.json',{'database':'system/data/knowledge/common.sqlite (read only)','records':{k:records.get(k) for k in ids},'sources':{k:sources[k] for k in sourceids if k in sources},'all_rule_completeness':collections.Counter(str(r['fields'].get('completeness',{}).get('status')) for r in records.values() if r['kind']=='competition_rule'),'approvals':c.execute('select count(*) from cc_approvals').fetchone()[0],'releases':c.execute('select count(*) from cc_releases').fetchone()[0]})
print(json.dumps({'methods':methods.most_common(18),'need_reasons':{k:len(v) for k,v in reason_keys.items()},'distinct_partition_requests':{k:len(v) for k,v in part_keys.items()},'model_errors':model_errors,'latency_requests':len(latency),'positive_exception_grades':len(missing_positive_exceptions),'out_scope_modes':out_scope},ensure_ascii=False,indent=2))
