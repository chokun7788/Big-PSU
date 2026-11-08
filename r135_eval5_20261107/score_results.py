"""Offline literal-contract score of recorded trial answers, not semantic grading."""
import collections,json,sys
from datetime import datetime
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent
sys.path.insert(0,str(R/'r132_flow_repairs_20261025/system'))
from tools.eval_contract_v2 import contract_matches
jobs={x['key']:x for x in map(json.loads,(R/'r131_diagnostic_review_20261025/SELECTED_JOBS.jsonl').open(encoding='utf8'))}
members=json.loads((R/'r131_diagnostic_review_20261025/CATEGORY_MEMBERSHIP.json').read_text(encoding='utf8'))['members']
rows=[json.loads(s) for s in (O/'RESULTS.jsonl').open(encoding='utf8') if s.strip()]
totals=collections.Counter();scope=collections.Counter();questions=collections.Counter()
baseline_path=R/'r134_live_sample_20261031/RESULTS.jsonl'
baseline={r['key']:r for r in map(json.loads,baseline_path.open(encoding='utf8'))} if baseline_path.exists() else {}
paired=collections.Counter()
for row in rows:
 job=jobs[row['key']];checks=[]
 for entry in job['entries']:
  case=entry['case'];contract=case.get('answer_contract') or case
  if case.get('required_clauses') or case.get('clauses') or not any(contract.get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')):
   totals['not_scored_no_supported_literal']+=1;continue
  result=None if not row.get('transport_ok') else contract_matches(row['response'].get('answer',''),contract)[0]
  key='matched' if result is True else 'not_matched' if result is False else 'unassessed'
  totals[key]+=1;checks.append(result)
  prior=baseline.get(row['key'])
  if result is not None and prior and prior.get('transport_ok'):
   prev=contract_matches(prior['response'].get('answer',''),contract)[0]
   paired['both_match' if prev and result else 'trial_only' if result else 'r134_only' if prev else 'neither']+=1
  if set(members.get(row['key'],{}).get('categories',[]))&{'C01','C06','C08'}:scope[key]+=1
 if not checks:questions['no_supported_literal']+=1
 elif any(x is None for x in checks):questions['unassessed']+=1
 elif all(checks):questions['all_evaluated_literals_matched']+=1
 else:questions['one_or_more_not_matched']+=1
report={'generated_at':datetime.now().astimezone().isoformat(),'requests':len(rows),'grades':dict(totals),'paired_vs_r134_literals':dict(paired),'scope_center_price_booking_grade_subset':dict(scope),'questions':dict(questions),'scoring':'literal text matching only, no semantic correctness or source authority; clauses and cases without positive literal criteria unassessed','scope_note':'nested 1056-request subset of the 2111-request broad sample as R134; C01/C06/C08 is approximate input classification, overlaps other categories; no exclusive small-scope claim','baseline_limits':'trial copied data and isolated app; different runtime state/time and model health mean comparisons are observational'}
(O/'SCORES_LITERAL.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False))
