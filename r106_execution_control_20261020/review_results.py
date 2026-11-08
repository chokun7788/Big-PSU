"""Post-run read-only streaming review; never invokes chatbot or model."""
import collections,gzip,hashlib,json,re,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent.parent
R=B/'r106_complete_flow_20261020'; O=R/'full_analysis'
def dump(name,data):
 (O/name).write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str),'utf8')
def stream(folder):
 for p in sorted(folder.glob('RESULTS_*.jsonl.gz')):
  with gzip.open(p,'rt',encoding='utf8') as f:
   for line in f:
    if line.strip():yield json.loads(line)
def identity(g):return (g.get('file'),g.get('row'),g.get('variant'),g.get('id'))
jobs={}
for line in (B/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl').open(encoding='utf8'):
 j=json.loads(line);jobs[j['key']]=j
stats=collections.Counter();patterns=collections.Counter();exact=collections.Counter();groups=collections.Counter();samples={};keycounts=collections.Counter();gm=[];raw_index={};byfile={};parts=collections.Counter();positive_failure_keys=set();protocol_only_keys=set();task_samples={}
for x in stream(R/'full01'):
 key=x['key'];keycounts[key]+=1;stats['requests']+=1;gs=x.get('grades',[]);stats['grades']+=len(gs)
 expected=collections.Counter((e['file'],e['row'],e['variant'],e['case'].get('id')) for e in jobs[key]['entries'])
 actual=collections.Counter(identity(g) for g in gs)
 if expected!=actual:gm.append(key)
 res=x.get('result') or {};art=res.get('decision_artifact') or {};failed=[g for g in gs if not g.get('passed')]
 flags=set();allcats=set()
 for g in gs:
  p=g.get('partitions') or {};cats={k for k,v in p.items() if v};allcats|=cats
  if cats:groups['+'.join(sorted(cats))]+=1
  for cat in cats:parts[cat]+=1
  row=byfile.setdefault(g['file'],collections.Counter());row['grades']+=1;row['pass']+=bool(g.get('passed'))
  if g.get('positive_text_contract'):
   row['positive']+=1;row['positive_pass']+=not any(p.get(c) for c in ('content','evidence','validation','grader'))
   if any(p.get(c) for c in ('content','evidence','validation','grader')):positive_failure_keys.add(key)
  for cat,values in p.items():
   for v in values:
    exact[cat+' | '+str(v)]+=1
    # retain type, independent of expected words/routes
    typ=str(v).split(':',1)[0];pattern=cat+' | '+typ
    patterns[pattern]+=1;flags.add(pattern)
 if failed:stats['failed_requests']+=1
 if allcats=={'protocol'}:protocol_only_keys.add(key)
 for n in art.get('need_results') or []:
  task=n.get('task') or n.get('task_id') or n.get('need_id') or 'unknown';status=n.get('status') or n.get('outcome') or 'unknown'
  label=str(task)+' | '+str(status);stats['need:'+label]+=1
  if failed and len(task_samples.setdefault(label,[]))<2:task_samples[label].append(key)
 if x.get('exception'):flags.add('EXECUTION_EXCEPTION')
 for c in x.get('observed_model_http_calls',[]):
  if not c.get('transport_ok'):flags.add('MODEL_TRANSPORT_FAILURE')
 for label in flags:
  if len(samples.setdefault(label,[]))<4:
   samples[label].append({'key':key,'question':x['question'],'answer':res.get('answer'),'mode':res.get('mode'),'route':res.get('route'),'validation':res.get('validation'),'need_results':art.get('need_results'),'query_plan':art.get('query_plan'),'request_plan':art.get('request_plan'),'claim_packets':art.get('claim_packets'),'grades':failed,'exception':x.get('exception'),'model_calls':x.get('observed_model_http_calls',[]),'job':jobs[key]})
 raw_index[key]={'locale':x.get('requested_locale'),'strict':{identity(g):bool(g.get('passed')) for g in gs},'positive':{identity(g):not any((g.get('partitions') or {}).get(c) for c in ('content','evidence','validation','grader')) for g in gs if g.get('positive_text_contract')}}
stats['positive_failure_requests']=len(positive_failure_keys);stats['protocol_only_requests']=len(protocol_only_keys)
dump('REVIEW_STREAM_COUNTS.json',{'stats':stats,'failure_patterns':patterns.most_common(),'exact_failures':exact.most_common(),'partition_combinations':groups.most_common(),'by_eval_file':byfile,'grade_identity_mismatches':gm,'key_duplicates':{k:v for k,v in keycounts.items() if v!=1}})
dump('REVIEW_GROUP_SAMPLES.json',samples);dump('REVIEW_TASK_SAMPLE_KEYS.json',task_samples)
# Saved baseline only. Compare both automated metrics on identical grade identities.
comp={};diff=[]
for x in stream(B/'r95_merged_flow_implementation_20261018/full01'):
 a=raw_index.get(x['key'])
 if a is None:continue
 loc=a['locale'];c=comp.setdefault(loc,collections.Counter());c['shared_requests']+=1
 for g in x.get('grades',[]):
  ident=identity(g)
  if ident not in a['strict']:continue
  c['shared_grades']+=1;c['r95_strict']+=bool(g.get('passed'));c['r106_strict']+=a['strict'][ident]
  if bool(g.get('passed'))!=a['strict'][ident]:c['strict_improved' if a['strict'][ident] else 'strict_regressed']+=1
  if g.get('positive_text_contract') and ident in a['positive']:
   old=not any((g.get('partitions') or {}).get(t) for t in ('content','evidence','validation','grader'));new=a['positive'][ident]
   c['shared_positive']+=1;c['r95_positive']+=old;c['r106_positive']+=new
   if old!=new:
    c['positive_improved' if new else 'positive_regressed']+=1
    diff.append({'key':x['key'],'question':x['question'],'grade':ident,'r95_pass':old,'r106_pass':new,'r95_answer':(x.get('result') or {}).get('answer')})
dump('REVIEW_R95_COMPARISON.json',{'by_locale_same_grade_identities':comp,'positive_changes':diff,'caveat':'Different data versions, not a causal estimate of Flow alone; transport rows have positive_text_contract false, comparison uses intersection.'})
# Hash source and inputs independently after full run.
source=json.loads((R/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'));inputs=json.loads((R/'FROZEN_INPUTS.json').read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
observed={p.relative_to(R/'system').as_posix():sha(p) for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
changes=[k for k in source.keys()|observed.keys() if source.get(k)!=observed.get(k)]
input_changes=[k for k,v in inputs.items() if sha(R/k)!=v]
full_input=json.loads((B/'r106_execution_control_20261020/FULL_INPUT.json').read_text('utf8'))
dump('INDEPENDENT_POSTRUN_VERIFICATION.json',{'unique_keys':len(keycounts),'requests':stats['requests'],'grades':stats['grades'],'missing':sorted(set(jobs)-set(keycounts)),'extra':sorted(set(keycounts)-set(jobs)),'duplicate_keys':{k:v for k,v in keycounts.items() if v!=1},'per_key_grade_identity_counter_mismatches':gm,'source_files_verified':len(source),'source_changes':changes,'frozen_input_files_verified':len(inputs),'frozen_input_changes':input_changes,'full_jobs_sha256_matches':sha(Path(full_input['path']))==full_input['sha256'],'model_before':json.loads((B/'r106_execution_control_20261020/MODEL_IDENTITY_BEFORE.json').read_text('utf8')),'model_after':json.loads((B/'r106_execution_control_20261020/MODEL_IDENTITY_AFTER.json').read_text('utf8'))})
print(json.dumps({'requests':stats['requests'],'grades':stats['grades'],'failed_requests':stats['failed_requests'],'positive_failure_requests':len(positive_failure_keys),'patterns':patterns.most_common(35),'combinations':groups.most_common(10),'source_changes':changes,'input_changes':input_changes,'comparison':comp},ensure_ascii=False,indent=2))
