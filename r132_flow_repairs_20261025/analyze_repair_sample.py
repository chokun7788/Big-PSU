"""Join saved baseline grades; never rerun or regrade a baseline."""
import collections,gzip,json,math,time
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;D=B/'r131_diagnostic_review_20261025';P=B/'r130_owner_context_completion_20261025'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def lines(p):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for line in f:yield json.loads(line)
assert load(R/'EXECUTION_COMPLETE.json')['complete']
out=R/'sample_analysis';out.mkdir(exist_ok=False)
jobs={x['key']:x for x in map(json.loads,(D/'SELECTED_JOBS.jsonl').open(encoding='utf8'))};members=load(D/'CATEGORY_MEMBERSHIP.json')['members'];eligible={};wanted={}
for key,j in jobs.items():
 wanted[key]={(e['file'],e['row'],e['variant']) for e in j['entries']}
 for e in j['entries']:
  c=e['case'];a=c.get('answer_contract') or c;eligible[(key,e['file'],e['row'],e['variant'])]=bool(c.get('required_clauses') or c.get('clauses') or any(a.get(k) for k in ['must_contain','must_contain_any','must_contain_all_groups']))
assert len(jobs)==2111 and len(eligible)==5584
arms={'R64_saved':[B/'r129_full_plan_completion_20261024/SAVED_LEGACY_ROWS.jsonl.gz'],'R95_saved':sorted((B/'r95_merged_flow_implementation_20261018/full01').glob('RESULTS_*.jsonl.gz')),'R130_saved':sorted((P/'full01').glob('RESULTS_*.jsonl.gz')),'R131_repeat_saved':sorted((D/'sample01').glob('RESULTS_*.jsonl.gz')),'R132_post_fix':sorted((R/'sample01').glob('RESULTS_*.jsonl.gz'))}
scores={};coverage={};flags={};answers={};newrows={};lat=[];gateway=collections.Counter();identity_errors=[];health=load(R/'MODEL_BEFORE.json')
for arm,paths in arms.items():
 locs=collections.defaultdict(collections.Counter);cats=collections.defaultdict(collections.Counter);seen=set();fs={};ans={}
 for path in paths:
  for row in lines(path):
   key=row['key']
   if key not in jobs:continue
   assert key not in seen,(arm,'duplicate_key',key);seen.add(key);loc=jobs[key]['locale'];categories=members[key]['categories'];actual=set()
   for cnt in [locs[loc],*[cats[c] for c in categories]]:cnt['requests']+=1
   for g in row['grades']:
    gid=(g['file'],g['row'],g['variant']);assert gid not in actual;actual.add(gid);identity=(key,*gid);pos=eligible[identity];literal=None
    if pos and not row.get('exception') and not any('pipeline_exception' in str(s) or 'grader_exception' in str(s) for s in g.get('failures',[])):
     if isinstance(g.get('content_checks_passed'),bool):literal=g['content_checks_passed']
     elif isinstance(g.get('partitions'),dict):literal=not g['partitions'].get('content',[])
    fs[identity]={'strict':bool(g['passed']),'literal':literal,'eligible':pos}
    for cnt in [locs[loc],*[cats[c] for c in categories]]:
     cnt['grades']+=1;cnt['strict_passed']+=int(g['passed'])
     if pos:cnt['literal_eligible']+=1;cnt['literal_unassessed' if literal is None else 'literal_passed' if literal else 'literal_failed']+=1
   assert actual==wanted[key],(arm,'grade_mismatch',key)
   result=row.get('result') or {};a=result.get('decision_artifact') or {};ans[key]=result.get('answer')
   if arm=='R132_post_fix':
    newrows[key]=row;lat.append(row['elapsed_sec'])
    for e in (a.get('request_context') or {}).get('events',[]):
     if e.get('stage')!='R129_model_gateway':continue
     gateway['receipts']+=1
     if not e.get('transport_ok'):gateway['transport_or_identity_failure']+=1;continue
     prov=e.get('returned_provenance') or {};stage=e.get('model_stage');profile='retained' if stage=='context_understanding' else 'base'
     checks={'profile':prov.get('effective_profile')==profile,'adapter':prov.get('adapter_sha256')==health['profiles'][profile],'profile_digest':prov.get('profile_digest')==health['profile_digests'][profile],'base_revision':prov.get('base_revision')==health['base_revision'],'messages':prov.get('effective_messages_sha256')==e.get('wire_messages_sha256'),'schema':prov.get('effective_schema_sha256')==e.get('schema_sha256'),'stage':prov.get('stage')==stage,'precision':prov.get('quantization')==health['quantization'],'model':e.get('model',health['model'])==health['model']}
     if all(checks.values()):gateway['verified_'+profile]+=1
     else:identity_errors.append({'key':key,'checks':checks})
 for c in [*locs.values(),*cats.values()]:
  c['strict_percent']=100*c['strict_passed']/c['grades'] if c['grades'] else None;c['literal_percent_fixed_denominator']=100*c['literal_passed']/c['literal_eligible'] if c['literal_eligible'] else None
  assert c['literal_passed']+c['literal_failed']+c['literal_unassessed']==c['literal_eligible']
 assert seen==set(jobs),(arm,'missing_keys',len(set(jobs)-seen));coverage[arm]={'unique_keys':len(seen),'grade_identities':len(fs),'missing_or_duplicate_keys':0,'missing_or_duplicate_grade_identities':0};scores[arm]={'requested_locale':dict(locs),'input_category':dict(cats)};flags[arm]=fs;answers[arm]=ans
changes=[{'key':k,'question':jobs[k]['question'],'requested_locale':jobs[k]['locale'],'categories':members[k]['categories'],'old':answers['R130_saved'][k],'new':answers['R132_post_fix'][k],'semantic_status':'review_required'} for k in jobs if answers['R130_saved'][k]!=answers['R132_post_fix'][k]]
paired={}
for arm in arms:
 if arm=='R132_post_fix':continue
 c=collections.Counter()
 for identity,n in flags['R132_post_fix'].items():
  old=flags[arm][identity];c['strict_old_only']+=old['strict'] and not n['strict'];c['strict_new_only']+=n['strict'] and not old['strict']
  if n['eligible']:
   if old['literal'] is None or n['literal'] is None:c['literal_unassessed_in_either']+=1
   else:c['literal_old_only']+=old['literal'] and not n['literal'];c['literal_new_only']+=n['literal'] and not old['literal']
 paired[arm]=dict(c)
with gzip.open(out/'PER_REQUEST_ANALYSIS.jsonl.gz','wt',encoding='utf8') as f,gzip.open(out/'ALL_FAILURES.jsonl.gz','wt',encoding='utf8') as bad:
 for key,row in newrows.items():
  f.write(json.dumps({'key':key,'question':row['question'],'requested_locale':jobs[key]['locale'],'categories':members[key]['categories'],'answer':(row.get('result') or {}).get('answer'),'grades':row['grades'],'semantic_status':'review_required'},ensure_ascii=False)+'\n')
  for g in row['grades']:
   if not g['passed']:bad.write(json.dumps({'key':key,'question':row['question'],'requested_locale':jobs[key]['locale'],'grade':g,'semantic_status':'review_required; keyword/protocol failure alone is not content judgment'},ensure_ascii=False)+'\n')
write(out/'COVERAGE.json',coverage);write(out/'FIXED_DENOMINATOR_SCORES.json',{'arms':scores,'paired':paired,'semantic_accuracy':None,'baseline_inferences':0,'baseline_regrades':0});write(out/'ANSWER_CHANGES_REVIEW_REQUIRED.json',changes);write(out/'MODEL_AUDIT.json',{'counts':dict(gateway),'identity_errors':identity_errors,'identity_verified_for_successful_receipts':not identity_errors,'constrained_generation_active':False})
lat.sort();write(out/'LATENCY.json',{'mean':sum(lat)/len(lat),'p95':lat[math.ceil(.95*len(lat))-1],'max':lat[-1],'confounds':['shared model/backend load','source/backend/precision/clock/deadline differences from old baselines','superseded debug APIs closed during measurement'],'causal_flow_effect_claimed':False})
report=['# ผลวัดหลังแก้R132 — ชุดเดิม10%','',f'ครบ {len(jobs)}keys / {len(eligible)}grade identities; เทียบsaved gradesโดยไม่run/regradebaselineใหม่','', '**รุ่นติดตั้งคือR133 ซึ่งแก้เพิ่มหลังfreezeR132** ผลนี้ยังไม่ใช่fresh executionของR133 ต้องตรวจpaired replayและsource regressionsต่อก่อนปิดงาน','', '| แขน | requested locale | strictผ่าน/ทั้งหมด | positive literalผ่าน/eligible | unassessed |','|---|---|---:|---:|---:|']
for arm,x in scores.items():
 for locale,c in sorted(x['requested_locale'].items()):report.append(f"| {arm} | {locale} | {c['strict_passed']}/{c['grades']} | {c['literal_passed']}/{c['literal_eligible']} | {c['literal_unassessed']} |")
report+=['',f'คำตอบเปลี่ยนจากsavedR130 {len(changes)}keys ไม่ถือchanged=improved ต้องsource review แยกactual contentจากprotocol/keyword/first-line/complete-clause/validity/source gaps/model transport','', 'คง76requirements/14หมวด; C07sampleเพียง1จากประชากร6 และC14ไม่มีnewsจริง ไม่อ้าง100%semantic ไม่อ้างcausalFloweffectจากsavedR64/R95ที่source/backend/precision/clock/deadlineต่างกัน','', 'Model profile/adapter/messages/schema/stage/precision audit: MODEL_AUDIT.json; เวลามีภาระเครื่องร่วมและปิดdebug APIsระหว่างรัน','', 'R133ติดตั้งแล้วตามINSTALLATION_RECEIPT.json ไม่ควรรายงานcandidateยังไม่ติดตั้งทับR78อีก ตัวเปิดเดิมส่งต่อbundleใหม่และเก็บsystem/dataR78เดิมครบ']
(out/'SAVED_FLOW_COMPARISON_TH.md').write_text('\n'.join(report)+'\n','utf8');write(out/'ANALYSIS_COMPLETE.json',{'complete':True,'coverage_verified':True,'model_identity_audit_passed':not identity_errors,'semantic_review_complete':False,'r133_paired_review_complete':False,'root_review_and_final_delivery_pending':True,'baseline_inferences':0,'baseline_regrades':0,'completed_at':time.time()})
print(json.dumps({'coverage':coverage,'changed_answers':len(changes),'model_identity_errors':len(identity_errors)},ensure_ascii=False))
