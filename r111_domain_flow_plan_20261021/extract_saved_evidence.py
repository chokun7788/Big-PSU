"""Read retained results to plan domain repairs; no chatbot/model calls."""
import collections,gzip,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent
def read(p):return json.loads((B/p).read_text('utf8'))
base=read('r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json')['by_domain']
current=read('r95_merged_flow_implementation_20261018/full_analysis/ANALYSIS_FINAL.json')['by_domain']
counters=collections.defaultdict(collections.Counter);methods=collections.defaultdict(collections.Counter);examples=collections.defaultdict(list);keys=set()
raw_paths=sorted((B/'r106_complete_flow_20261020/full01').glob('RESULTS_*.jsonl.gz'))
for p in raw_paths:
 with gzip.open(p,'rt',encoding='utf8') as f:
  for line in f:
   a=json.loads(line);assert a['key'] not in keys;keys.add(a['key'])
   domain=a.get('stratum',{}).get('domain') or 'unclassified';c=counters[domain];c['requests']+=1
   result=a.get('result') or {};art=result.get('decision_artifact') or {};qp=art.get('query_plan') or {}
   methods[domain][qp.get('method') or result.get('mode') or 'exception']+=1
   posfail=False
   for g in a['grades']:
    c['grades']+=1;c['strict_passed']+=bool(g['passed'])
    if g.get('positive_text_contract'):
     c['positive_checked']+=1
     good=not any(g.get('partitions',{}).get(k) for k in ['content','evidence','validation','grader'])
     c['positive_passed']+=good;posfail=posfail or not good
   if (posfail or qp.get('method') in ['r103_rule_dependency_gap','r102_price_effective_dates_missing']) and len(examples[domain])<3:
    examples[domain].append({'key':a['key'],'question':a['question'],'answer':result.get('answer'),'method':qp.get('method'),'need_results':art.get('need_results'),'query_plan':qp,'grades':[{'file':g['file'],'row':g['row'],'positive_text_contract':g.get('positive_text_contract'),'failures':g.get('failures')} for g in a['grades']]})
assert len(keys)==20554
assert sum(c['positive_checked'] for c in counters.values())==24891
assert sum(c['positive_passed'] for c in counters.values())==17238
domains=['equipment','games_catalog_availability','game_detail','game_controls','service_fee','reservation_policy','schedule_calendar','booking_days_hours','competition_rules','competition','compound_context_boundary','members_overview_contact']
rows=[]
for name in domains:
 old=base.get(name,{});new=current.get(name,{});latest=counters.get(name,{})
 def score(p,n):return {'passed':p,'checked':n,'percent':round(p*100/n,2) if n else None}
 rows.append({'domain':name,'legacy':score(old.get('old_positive_passed',0),old.get('positive_checked',0)),'r88':score(old.get('new_positive_passed',0),old.get('positive_checked',0)),'r95':score(new.get('positive_passed',0),new.get('positive_checked',0)),'r106_reported_metric':score(latest.get('positive_passed',0),latest.get('positive_checked',0)),'r106_requests':latest.get('requests',0),'r106_methods':methods[name].most_common(8),'limits':'R106 follows its saved partition-based metric, whose taxonomy differs from literal checker used by Legacy/R88/R95. Not a semantic accuracy ranking.'})
(R/'DOMAIN_EVIDENCE.json').write_text(json.dumps({'rows':rows,'all_r106_domains':{k:dict(v) for k,v in counters.items()},'raw_source_paths':[str(p.relative_to(B)) for p in raw_paths],'raw_source_sha256':{str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in raw_paths},'new_requests':0,'llm_calls':0},ensure_ascii=False,indent=2),'utf8')
(R/'SAVED_CASES.json').write_text(json.dumps(dict(examples),ensure_ascii=False,indent=2),'utf8')
for v in rows:print(v['domain'],{k:v[k]['percent'] for k in ['legacy','r88','r95','r106_reported_metric']})
