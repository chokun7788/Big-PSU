"""Planner metrics only, independent of venue answer correctness."""
import collections,json
from context_contract import validate
def parse(raw):
 try:return json.loads(raw),False
 except (ValueError,TypeError):
  try:
   start=raw.index('{');end=raw.rindex('}');return json.loads(raw[start:end+1]),True
  except (ValueError,TypeError,AttributeError):return None,False
def score(raw,gold,question):
 p,cleaned=parse(raw);valid,why=validate(p,question)
 ts=p.get('tasks',[]) if isinstance(p,dict) and isinstance(p.get('tasks'),list) else []
 ts=[t for t in ts if isinstance(t,dict)]
 sig=lambda t:(t.get('domain'),t.get('operation'),t.get('facet'),t.get('ambiguous'))
 gs=gold['tasks'];desired={(c['slot'],c['quote']) for t in gs for c in t['constraints']}
 got={(c.get('slot'),c.get('quote')) for t in ts for c in t.get('constraints',[]) if isinstance(c,dict)}
 tp=len(desired&got)
 return {'json_object_parsed':p is not None,'json_cleanup_used':cleaned,'source_contract_valid':valid,'source_contract_reason':why,
 'focus_correct':isinstance(p,dict) and p.get('focus')==gold['focus'],
 'domains_correct':sorted(str(t.get('domain')) for t in ts)==sorted(t['domain'] for t in gs),
 'tasks_exact':valid and sorted(sig(t) for t in ts)==sorted(sig(t) for t in gs),
 'task_count_correct':len(ts)==len(gs),'domain_facet_correct':sorted((str(t.get('domain')),str(t.get('facet'))) for t in ts)==sorted((t['domain'],t['facet']) for t in gs),
 'constraint_true_positive':tp,'constraint_gold':len(desired),'constraint_predicted':len(got),'missing_constraints':sorted(desired-got),
 'parsed_plan':p}
def aggregate(rs):
 c=collections.Counter()
 for r in rs:
  s=r['metrics'];c['requests']+=1
  for k in ['json_object_parsed','json_cleanup_used','source_contract_valid','focus_correct','domains_correct','tasks_exact','task_count_correct','domain_facet_correct','constraint_true_positive','constraint_gold','constraint_predicted']:c[k]+=int(s[k])
 return {**dict(c),'constraint_recall':c['constraint_true_positive']/max(1,c['constraint_gold']),'constraint_precision':c['constraint_true_positive']/max(1,c['constraint_predicted'])}
