import collections,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent;OLD=P/'r120_teacher_distillation_20261022'
jobs=list(map(json.loads,(P/'r116_retained_full_ten_percent_20261021/SELECTED_JOBS.jsonl').open(encoding='utf8')))
parent={j['key']:j['key'] for j in jobs};owners={}
def root(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
def identities(j):
 return {k+':'+str(e['case'][k]).replace('-TH-','-LANG-').replace('-EN-','-LANG-') for e in j['entries'] for k in ['id','origin_id'] if e['case'].get(k)}
for j in jobs:
 for ident in identities(j):
  if ident in owners:parent[root(j['key'])]=root(owners[ident])
  else:owners[ident]=j['key']
groups={j['key']:root(j['key']) for j in jobs}
seen={j['key'] for name in ['TEACHING_JOBS.jsonl','HOLDOUT_JOBS.jsonl','DEVELOPMENT_JOBS.jsonl'] for j in map(json.loads,(OLD/name).open(encoding='utf8'))};used={groups[k] for k in seen}
inventory=[];freshgroups=set();counts=collections.Counter()
ordered=sorted(jobs,key=lambda j:hashlib.sha256(('r121-fresh:'+j['key']).encode()).hexdigest())
for j in ordered:
 g=groups[j['key']];s=j['r70_stratum'];domain=s['domain'];loc=j['locale'];slot=(domain,loc)
 if g in used or g in freshgroups or counts[slot]>=3:continue
 if len(j['question'])>450:continue
 freshgroups.add(g);counts[slot]+=1
 inventory.append({'key':j['key'],'question':j['question'],'locale':loc,'stratum':domain,'family':g,
 'reference_fields':[{k:e['case'].get(k) for k in ['expected_route_categories','expected_intent','expected_facet','expected_target','domain']} for e in j['entries'][:1]]})
(R/'FRESH_CANDIDATES.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),'utf8')
(R/'FAMILY_GROUPS.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2),'utf8')
(R/'ALL_RETAINED_JOBS.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in jobs),'utf8')
paths=[p for p in (OLD/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith(('-wal','-shm'))]
paths += [OLD/n for n in ['TEACHER_LESSONS.json','TEACHER_MAPPING_REVIEW.json','SPLIT_MANIFEST.json','ANALYSIS_FINAL.json','FINAL_REPORT_TH.md']]
(R/'PROTECTED_INPUTS.json').write_text(json.dumps({str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2),'utf8')
print(json.dumps({'retained_jobs':len(jobs),'families':len(set(groups.values())),'previously_used_keys':len(seen),'used_families':len(used),'fresh_candidates':len(inventory),'strata':dict(collections.Counter(j['stratum'] for j in inventory))},ensure_ascii=False))
for i,j in enumerate(inventory):print(f'{i:03} {j["key"][:8]} [{j["stratum"]}] {j["question"]}')
