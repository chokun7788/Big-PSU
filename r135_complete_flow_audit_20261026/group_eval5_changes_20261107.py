"""Group saved matched literal changes without rerunning or regrading R132."""
import collections,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;O=R/'paired_eval5_groups_20261107';O.mkdir(exist_ok=False)
sys.path.insert(0,str(R/'system'))
from tools.eval_contract_v2 import contract_matches
jobs={x['key']:x for x in map(json.loads,(B/'r135_eval5_20261107/SELECTED_5_PERCENT_v2.jsonl').open(encoding='utf8'))}
trial={x['key']:x for x in map(json.loads,(B/'r135_eval5_20261107/RESULTS.jsonl').open(encoding='utf8'))}
old={x['key']:x for x in map(json.loads,(B/'r134_live_sample_20261031/RESULTS.jsonl').open(encoding='utf8')) if x['key'] in jobs}
membership=json.loads((B/'r131_diagnostic_review_20261025/CATEGORY_MEMBERSHIP.json').read_text(encoding='utf8'))['members']
assert len(jobs)==len(trial)==len(old)==1056
counts=collections.Counter();groups=collections.defaultdict(collections.Counter);rows=[]
for key,job in jobs.items():
 for entry in job['entries']:
  case=entry['case'];contract=case.get('answer_contract') or case
  if case.get('required_clauses') or case.get('clauses') or not any(contract.get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')):continue
  a,_=contract_matches(old[key]['response'].get('answer',''),contract);b,_=contract_matches(trial[key]['response'].get('answer',''),contract)
  outcome='both' if a and b else 'r135_only' if b else 'r134_only' if a else 'neither'
  counts[outcome]+=1
  for cat in membership.get(key,{}).get('categories',[]):groups[cat][outcome]+=1
  if outcome in {'r135_only','r134_only'}:rows.append({'key':key,'question':job['question'],'locale':job['locale'],'categories':membership.get(key,{}).get('categories',[]),'outcome':outcome,'identity':{k:entry[k] for k in ('file','row','variant')},'contract':contract,'r134_answer':old[key]['response'].get('answer'),'r135_answer':trial[key]['response'].get('answer'),'semantic_review':'required'})
report={'counts':dict(counts),'groups':{k:dict(v) for k,v in groups.items()},'changed_grade_rows':len(rows),'unique_questions':len({r['key'] for r in rows}),'limitations':'literal matches only, categories overlap, execution clocks and source/backend conditions differ; changed is not causal or semantic correctness'}
(O/'REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
(O/'ITEMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf8')
print(json.dumps({'path':str(O),**report},ensure_ascii=False))
