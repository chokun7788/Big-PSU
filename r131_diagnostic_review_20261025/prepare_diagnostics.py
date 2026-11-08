"""Offline case/trace diagnosis and outcome-blind retained-input sampling.
No assistant inference, source edits, baseline execution, or semantic auto-score.
"""
import collections,gzip,hashlib,json,math,re,sqlite3,time,zlib
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;P=B/'r130_owner_context_completion_20261025';O=P/'full_analysis'
SEED='r131-item02-existing-full-per-domain-ten-percent-v1'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def lines(p):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for s in f:yield json.loads(s)
def state(phase,**kwargs):write('STATUS.json',{'phase':phase,'updated_at':time.time(),'complete':False,'diagnosis_before_retest':True,'production_installed':False,**kwargs})
state('offline_diagnosis_preparation')
source=load(O/'REVIEW_SOURCE_INDEX.json');records=source['records'];manual={c['key']:c for c in load(O/'AGENT_SOURCE_CASE_REVIEW.json')['cases']}
master=B/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl'
jobs=[json.loads(s) for s in master.open(encoding='utf8')];bykey={x['key']:x for x in jobs}
assert len(jobs)==len(bykey)==20554
NAMES={'C00':'ทั่วไป/กำกวม/นอกขอบเขต','C01':'ศูนย์/ติดต่อ','C02':'บุคลากร','C03':'อุปกรณ์','C04':'เกม','C05':'การควบคุม','C06':'ราคาปกติ','C07':'เหมา','C08':'จอง','C09':'ชำระเงิน','C10':'กฎศูนย์','C11':'ตาราง','C12':'สถานะจริง','C13':'แข่งขัน','C14':'ข่าว/กิจกรรม'}
DOMAIN={'game_controls':['C05'],'service_fee':['C06'],'games_catalog_availability':['C04'],'game_detail':['C04'],'competition_rules':['C13'],'reservation_policy':['C08'],'equipment':['C03'],'live_booking':['C12'],'studio_rules_penalties':['C10'],'schedule_calendar':['C11'],'members_overview_contact':['C01','C02'],'games':['C04'],'availability_game':['C04'],'competition':['C13'],'weekday_live_slots':['C11','C12'],'equipment_access_trap':['C03','C10'],'damage_responsibility':['C10'],'identity_typo':['C01'],'outsider_eligibility':['C10'],'food_bring_scope':['C10'],'food_consumption':['C10'],'booking_days_hours':['C08','C11'],'fee_without_service':['C06'],'booking':['C08'],'schedule':['C11'],'game_rules':['C13'],'equipment_game_inside':['C03','C04'],'members':['C02'],'reservation':['C08'],'rules_penalty':['C10'],'overview':['C01'],'members_about_contact':['C01','C02'],'availability_service':['C04'],'rules':['C10'],'games_list':['C04'],'price':['C06'],'contact':['C01'],'control':['C05'],'live_availability':['C12'],'identity':['C01'],'live_schedule':['C11','C12'],'penalty':['C10'],'personal_power':['C10'],'broad_eligibility':['C10'],'time_vs_access':['C11'],'food_bring':['C10'],'all_games_scope':['C04'],'membership_facet':['C10'],'booking_required':['C08'],'offsite_scope':['C07'],'age_scope':['C10'],'student_only_boundary':['C10'],'food_at_desk':['C10'],'return_equipment_rule':['C10'],'alcohol_bringing_scope':['C10'],'food_consume':['C10'],'visitor_fee':['C06'],'multi_studio_rules':['C10'],'document_facet':['C08'],'fee_vs_access':['C06','C10'],'fee_vs_booking':['C06','C08']}
ROUTES={'competition_rules':'C13','service_fee':'C06','equipment':'C03','members':'C02','overview':'C01','contact':'C01','reservation':'C08','schedule':'C11','rules':'C10','penalty':'C10','news':'C14','rental':'C07','payment':'C09','live_booking':'C12'}
def membership(j):
 cats=set();evidence=[];q=j['question'].casefold();domain=j['r70_stratum']['domain']
 for cat in DOMAIN.get(domain,[]):cats.add(cat);evidence.append('frozen_stratum:'+domain)
 for e in j['entries']:
  c=e['case'];d=c.get('domain') or c.get('group') or c.get('category') or ''
  if isinstance(d,str):cats.update(DOMAIN.get(d,[]))
  if c.get('expected_rulebook_ids') or c.get('expected_game_id') and c.get('rag_required'):cats.add('C13');evidence.append('frozen_rulebook_contract')
  if 'competition_' in Path(e['file']).name or str(c.get('source_id','')).startswith('competition_rules_'):
   cats.add('C13');evidence.append('frozen_competition_clause_corpus_or_source')
  rs=c.get('expected_route_categories') or [c.get('expected_category')]
  if isinstance(rs,str):rs=[rs]
  rs=[v for item in rs for v in (item if isinstance(item,list) else [item])]
  for route in rs:
   if route in ROUTES:cats.add(ROUTES[route]);evidence.append('frozen_allowed_route:'+route)
   if route=='games':cats.add('C05' if re.search(r'ปุ่ม|จอย|\b(?:buttons?|controls?|press)\b',q) else 'C04')
 # These cues only describe sampling coverage. They never change runtime routing
 # or serve as a semantic gold label for the saved answer.
 for cat,pat in [('C07',r'เหมา(?!ะ)|เช่า.*(?:กลับบ้าน|แล็ป|โน้ต|notebook)|\brental\b|rent (?:laptop|notebook)|half.day|full.day'),('C09',r'โอน|ชำระ|สลิป|คืนเงิน|ใบเสร็จ|ใบเสนอราคา|\b(?:refund|receipt|quotation|payer|slip|overpay|underpay|payment)\b'),('C14',r'ข่าว|ประกาศ|กิจกรรม|\b(?:news|announcement|event registration)\b')]:
  if re.search(pat,q):cats.add(cat);evidence.append('predeclared_sampling_topic:'+cat)
 if re.search(r'ปุ่ม|\b(?:buttons?|controls?)\b',q) and 'C13' not in cats:cats.add('C05')
 if not cats:cats.add('C00');evidence.append('sampling_topic_unresolved_or_general')
 return sorted(cats),sorted(set(evidence))
members={j['key']:membership(j) for j in jobs}
population=collections.defaultdict(list)
for j in jobs:
 for cat in members[j['key']][0]:population[cat].append(j)
# First guarantee 10% in each ORIGINAL frozen stratum, including tiny strata.
strata=collections.defaultdict(list)
for j in jobs:strata[j['r70_stratum']['domain']].append(j)
def rank(j,tag):return hashlib.sha256((SEED+'|'+tag+'|'+j['key']).encode()).hexdigest()
def pick(group,n,tag):
 locales=collections.defaultdict(list)
 for j in group:locales[j['locale']].append(j)
 alloc={k:n*len(v)//len(group) for k,v in locales.items()}
 for k in sorted(locales,key=lambda k:(-(n*len(locales[k])/len(group)%1),k))[:n-sum(alloc.values())]:alloc[k]+=1
 return [j for k,v in sorted(locales.items()) for j in sorted(v,key=lambda x:rank(x,tag))[:alloc[k]]]
chosen={};allocations=[]
for d,group in sorted(strata.items()):
 n=math.ceil(len(group)*.1);picks=pick(group,n,'stratum:'+d)
 chosen.update({j['key']:j for j in picks});allocations.append({'stratum':d,'population':len(group),'quota':n,'chosen_keys':[j['key'] for j in picks]})
topups=[]
for cat,group in sorted(population.items()):
 n=math.ceil(len(group)*.1);have=sum(j['key'] in chosen for j in group)
 if have<n:
  added=sorted([j for j in group if j['key'] not in chosen],key=lambda j:rank(j,'category_topup:'+cat))[:n-have]
  chosen.update({j['key']:j for j in added});topups.extend({'category':cat,'key':j['key']} for j in added)
selected=sorted(chosen.values(),key=lambda j:rank(j,'execution_order'))
with (R/'SELECTED_JOBS.jsonl').open('w',encoding='utf8') as f:
 for j in selected:f.write(json.dumps(j,ensure_ascii=False)+'\n')
write('CATEGORY_MEMBERSHIP.json',{'sampling_labels_not_semantic_gold':True,'input_only_no_candidate_predictions':True,'members':{k:{'categories':v[0],'evidence':v[1]} for k,v in members.items()}})
category_allocation=[{'category':cat,'name_th':NAMES[cat],'population':len(group),'quota_ceil_10pct':math.ceil(len(group)*.1),'actual_selected':sum(j['key'] in chosen for j in group),'selected_percent':100*sum(j['key'] in chosen for j in group)/len(group)} for cat,group in sorted(population.items())]
assert set('C'+str(i).zfill(2) for i in range(1,15))<=set(population)
assert all(x['actual_selected']>=x['quota_ceil_10pct'] for x in category_allocation)
write('SAMPLE_ALLOCATION.json',{'seed':SEED,'selection_before_new_execution':True,'based_on_results_or_pass_flags':False,'original_strata':allocations,'categories':category_allocation,'topups':topups,'overlapping_memberships_not_added_as_unique_requests':True,'sample_requests':len(selected),'sample_grades':sum(len(j['entries']) for j in selected),'population_requests':20554,'new_questions':0,'note':'Original-stratum 10% with locale allocation; input-topic category topups ensure every C01-C14 reaches ceil(10%). Rounding and overlapping categories can produce >10% in some groups. Category labels are sampling metadata, not an adjudicated intent oracle.'})
write('SELECTION_FREEZE.json',{'seed':SEED,'master_sha256':sha(master),'sample_sha256':sha(R/'SELECTED_JOBS.jsonl'),'sample_keys':[j['key'] for j in selected],'category_membership_sha256':sha(R/'CATEGORY_MEMBERSHIP.json'),'candidate':'unchanged R130 retained/base','runtime_fixes':0,'source_changes':0,'new_baseline_inferences':0,'test_purpose':'confirm repeat behavior and diagnostics on an outcome-blind subset; not post-fix improvement','clock':'same R130 fixed default/per-job reference date','live':'same controlled unavailable fixture','workers':2,'stage_profiles':'context=retained; others=base','frozen_parent_manifest':str(P/'EXECUTION_FREEZE_R130.json')})
state('offline_full_case_ledger',sample_requests=len(selected),sample_grades=sum(len(j['entries']) for j in selected))
issues=collections.defaultdict(set);reason_examples=collections.defaultdict(list);by_category=collections.defaultdict(collections.Counter);signatures={};count=0
comparison_keys={x['key'] for x in lines(O/'REVIEW_SPECIMENS.jsonl.gz')}|set(manual)
with gzip.open(R/'CASE_DIAGNOSTICS.jsonl.gz','wt',encoding='utf8') as ledger,gzip.open(R/'DEEP_REVIEW_CASES.jsonl.gz','wt',encoding='utf8') as deep:
 for path in sorted((P/'full01').glob('RESULTS_*.jsonl.gz')):
  for row in lines(path):
   key=row['key'];job=bykey[key];res=row.get('result') or {};art=res.get('decision_artifact') or {};contract=art.get('execution_contract') or {};tasks=contract.get('tasks',[]);ctx=art.get('request_context') or {};domain=art.get('domain_flow') or {};under=art.get('understanding') or {}
   found=[]
   def issue(code,stage,confidence,proof,causal_status='observed_mechanism_not_automatic_content_failure'):
    found.append({'code':code,'stage':stage,'confidence':confidence,'proof':proof,'causal_status':causal_status});issues[code].add(key)
   failures=[f for g in row['grades'] for f in g['failures']]
   if any(f.startswith(('route','intent','legacy_mode')) for f in failures):issue('legacy_protocol_identity_mismatch','evaluation_contract','confirmed_assertion',sorted(set(f for f in failures if f.startswith(('route','intent','legacy_mode'))))[:8])
   events=[*domain.get('model_events',[])]
   if under.get('event') and under['event'] not in events:events.append(under['event'])
   for e in events:
    if e.get('transport_ok') and e.get('schema_ok') is False:
     issue('model_schema_or_version_rejection','context' if e.get('stage')=='context_understanding' else 'evidence_selection','confirmed_mechanism',{'reason':e.get('reason'),'error':e.get('error'),'profile':(e.get('model_provenance') or {}).get('effective_profile'),'raw_excerpt':e.get('raw_content','')[:650]})
    if 'model_admission_unavailable' in str(e.get('error')):
     admission=e.get('admission') or {}
     code='model_concurrency_admission_busy' if admission.get('llm_concurrency_allowed') is False else 'model_admission_denied_reason_not_fully_logged'
     issue(code,'model_admission','confirmed_event',{'error':e['error'],'http_attempted':e.get('http_attempted'),'admission':admission})
   for call in row.get('observed_model_http_calls',[]):
    if not call.get('transport_ok'):issue('actual_http_timeout_or_transport_failure','model_transport','confirmed_event',{k:v for k,v in call.items() if k!='url'})
   for t in tasks:
    codes=t.get('reason_codes') or [];terminal=t.get('terminal_state')
    if 'substantive_clause_not_delivered' in codes:issue('substantive_clause_guard_rejected_claim','verifier','confirmed_mechanism',{'task_id':t['task_id'],'receipts':t.get('receipts'),'obligations':t.get('obligations')})
    if 'requested_field_not_delivered' in codes:issue('requested_field_not_delivered','reader_or_projection','confirmed_terminal_not_root_cause',{'task_id':t['task_id'],'obligations':t.get('obligations')})
    if 'r103_rule_dependency_gap' in codes:issue('rule_dependency_reader_gap','rule_reader','confirmed_terminal_source_absence_unproven',{'reason_codes':codes})
    if terminal=='missing_source':issue('missing_source_report_requires_source_audit','reader','review_required',{'reason_codes':codes})
    if terminal=='provider_unavailable':issue('provider_unavailable_terminal_needs_attribution','dependency','confirmed_terminal',{'reason_codes':codes,'live_artifact_present':bool(art.get('live_booking'))})
    if terminal=='invalid_plan':issue('compiled_scope_rejected','compiler','confirmed_mechanism',{'reason_codes':codes})
    if 'policy_source_scope_or_revision_conflict' in codes:issue('policy_equivalence_or_authority_unresolved','source_authority','review_required',{'receipts':t.get('receipts')})
   if art.get('live_booking'):issue('controlled_live_artifact','live','confirmed_fixture_path',{'status':art['live_booking'].get('status'),'note':'Controlled unavailable in measured workload; real provider status not inferred.'})
   if any('latency' in f for f in failures):issue('latency_assertion_failed','performance','confirmed_assertion',{'elapsed_sec':row.get('elapsed_sec')})
   if any('missing_complete_clause' in f or 'first_line' in f for f in failures):issue('literal_clause_or_first_line_assertion','evaluation_contract','semantic_review_required',sorted(set(f for f in failures if 'missing_complete_clause' in f or 'first_line' in f))[:6])
   reviewed=manual.get(key)
   if reviewed:issue('agent_source_adjudicated_case','source_semantic_review','agent_adjudicated',{'decision':reviewed['decision'],'diagnosis_th':reviewed['diagnosis_th'],'source_record_ids':reviewed['source_record_ids']},'see_individual_source_adjudication')
   cats=members[key][0]
   for cat in cats:
    by_category[cat]['population']+=1;by_category[cat]['selected']+=int(key in chosen);by_category[cat]['prior_source_adjudicated']+=int(bool(reviewed))
    for code in {x['code'] for x in found}:by_category[cat][code]+=1
   gold={'domains':sorted({str(e['case'].get('domain','')) for e in job['entries']}),'facets':sorted({str(e['case'].get('expected_facet','')) for e in job['entries']}),'targets':sorted({str(e['case'].get('expected_target','')) for e in job['entries']}),'rulebook_ids':sorted({x for e in job['entries'] for x in e['case'].get('expected_rulebook_ids',[])})}
   needs={'raw_question':row['question'],'planned_tasks':(contract.get('request_plan') or {}).get('tasks',[]),'task_list_exhaustive_semantics_verified':False,'frozen_reference_metadata_not_current_source_authority':gold}
   expected_sources={'agent_confirmed_source_records':reviewed['source_record_ids'] if reviewed else [],'delivered_source_hits':[{'record_id':h.get('record_id'),'field':h.get('field'),'source_id':h.get('source_id'),'locator':h.get('locator')} for h in res.get('hits',[])],'remaining_expected_source_resolution':'individually_reviewed' if reviewed else 'review_required'}
   item={'key':key,'question':row['question'],'requested_locale':row['requested_locale'],'sampling_categories':cats,'selected_for_10pct':key in chosen,'question_needs':needs,'delivered_answer':res.get('answer'),'expected_and_delivered_sources':expected_sources,'observed_issues':found,'first_failing_stage':'agent_review_required' if not reviewed else 'see_agent_diagnosis','upstream_cause_not_inferred_from_terminal_label':True,'semantic_adjudication':reviewed['decision'] if reviewed else 'review_required','confirmed_actual_content_failure':reviewed['confirmed_actual_content_failure'] if reviewed else None,'raw_results_file':path.name,'grade_count':len(row['grades']),'grade_identities':[[g['file'],g['row'],g['variant']] for g in row['grades']]}
   ledger.write(json.dumps(item,ensure_ascii=False)+'\n')
   sig=tuple(sorted({x['code'] for x in found}));signatures[key]=sig
   if key in comparison_keys:deep.write(json.dumps(row,ensure_ascii=False)+'\n')
   for code in {x['code'] for x in found}:
    if len(reason_examples[code])<8:reason_examples[code].append({'key':key,'question':row['question'],'answer':res.get('answer'),'individual_semantic_status':item['semantic_adjudication']})
   count+=1
   if count%2500==0:print(json.dumps({'offline_cases_processed':count}),flush=True)
write('ISSUE_COUNTS.json',{'requests_read':count,'mechanism_groups_overlap':True,'groups':{k:{'unique_requests':len(v),'keys':sorted(v),'examples':reason_examples[k]} for k,v in issues.items()},'by_input_category':dict(by_category),'confirmed_mechanism_is_not_confirmed_semantic_failure':True,'individual_source_adjudications':len(manual),'semantic_accuracy':None})
assert count==20554
state('saved_teacher_trace_comparison',sample_requests=len(selected))
legacy_path=B/'r65_detailed_failure_analysis_20261014/evidence.sqlite'
legacy=sqlite3.connect(legacy_path.resolve().as_uri()+'?mode=ro',uri=True)
saved_old={}
with gzip.open(R/'SAVED_LEGACY_DEEP_CASES.jsonl.gz','wt',encoding='utf8') as f:
 for key in sorted(comparison_keys):
  raw=legacy.execute("select raw from results where arm='legacy_llm' and key=?",(key,)).fetchone()
  assert raw is not None,key
  row=json.loads(zlib.decompress(raw[0]));assert row['question']==bykey[key]['question'];f.write(json.dumps(row,ensure_ascii=False)+'\n')
  result=row.get('result') or {}
  saved_old[key]={'answer':result.get('answer'),'route':result.get('route'),'mode':result.get('mode'),'hits':result.get('hits'),'trace':result.get('trace'),'elapsed_wall':row.get('elapsed_wall'),'exception':row.get('exception')}
saved_r95={}
for p in sorted((B/'r95_merged_flow_implementation_20261018/full01').glob('RESULTS_*.jsonl.gz')):
 for row in lines(p):
  if row['key'] in comparison_keys:
   res=row.get('result') or {};saved_r95[row['key']]={'answer':res.get('answer'),'mode':res.get('mode'),'route':res.get('route'),'hits':res.get('hits'),'elapsed_sec':row.get('elapsed_sec')}
write('SAVED_DEEP_COMPARISON.json',{'legacy':saved_old,'r95':saved_r95,'baseline_new_inferences':0,'baseline_regrading':0,'same_keys':sorted(comparison_keys),'source_backend_clock_versions_differ':True,'not_causal_flow_effect':True})
state('offline_ledger_ready_source_causal_review_pending',sample_requests=len(selected),sample_grades=sum(len(j['entries']) for j in selected),offline_cases_processed=count,source_cases_before=34,raw_deep_cases=len(comparison_keys),end_to_end_retest_started=False)
print(json.dumps({'offline_cases':count,'sample_requests':len(selected),'sample_grades':sum(len(j['entries']) for j in selected),'categories':category_allocation,'deep_cases':len(comparison_keys)},ensure_ascii=False),flush=True)
