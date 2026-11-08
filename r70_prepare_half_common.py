"""Freeze the new common-format installation and choose 50% of existing jobs."""
import collections,hashlib,json,math,shutil,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
SRC=B/'PSU_Esports_Chat_New_R69';OUT=B/'r70_half_common_llm_20261016'
OUT.mkdir(exist_ok=False)
def ignore(folder,names):
 skip={n for n in names if n=='__pycache__' or n.endswith('.pyc')}
 if Path(folder).name=='data':skip.update(set(names)&{'logs','state','knowledge'})
 return skip
shutil.copytree(SRC/'system',OUT/'system',ignore=ignore)
db=OUT/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
with sqlite3.connect((SRC/'system/data/knowledge/common.sqlite').as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as z:a.backup(z)
shutil.copyfile(B/'r64_full_comparison_20261013/grade_legacy.py',OUT/'reference_grader.py')
source_jobs=B/'r64_full_comparison_20261013/JOBS.jsonl'
jobs=[json.loads(s) for s in source_jobs.read_text('utf8').splitlines() if s.strip()]
def stratum(j):
 c=j['entries'][0]['case']
 domain=next((c.get(k) for k in ['domain','group','expected_category','expected_intent','category','topic','kind'] if c.get(k)),'unclassified')
 if not isinstance(domain,str):domain=json.dumps(domain,ensure_ascii=False,sort_keys=True)
 style=next((c.get(k) for k in ['noise','mutation','question_style','question_style','case_type'] if c.get(k)),j['entries'][0]['variant'])
 if not isinstance(style,str):style=json.dumps(style,ensure_ascii=False,sort_keys=True)
 return j['locale'],j['entries'][0]['file'],domain,style
groups=collections.defaultdict(list)
for job in jobs:groups[stratum(job)].append(job)
target=len(jobs)//2
allocation={k:len(v)//2 for k,v in groups.items()}
remainders=sorted([k for k,v in groups.items() if len(v)%2],key=lambda k:hashlib.sha256(('r70-half-v1|'+str(k)).encode()).hexdigest())
for key in remainders[:target-sum(allocation.values())]:allocation[key]+=1
selected=[]
for key,group in groups.items():
 ordered=sorted(group,key=lambda j:hashlib.sha256(('r70-half-v1|'+j['key']).encode()).hexdigest())
 for job in ordered[:allocation[key]]:
  job['r70_stratum']={'locale':key[0],'corpus':key[1],'domain':key[2],'style':key[3]};selected.append(job)
selected.sort(key=lambda j:hashlib.sha256(('r70-execution-v1|'+j['key']).encode()).hexdigest())
assert len(selected)==target and len({j['key'] for j in selected})==target
with (OUT/'SELECTED_JOBS.jsonl').open('x',encoding='utf8') as f:
 for job in selected:f.write(json.dumps(job,ensure_ascii=False)+'\n')
with (OUT/'STRATA.json').open('x',encoding='utf8') as f:json.dump([{'stratum':key,'population':len(group),'selected':allocation[key]} for key,group in groups.items()],f,ensure_ascii=False,indent=2)
manifest=[]
for p in sorted((SRC/'system').rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc':continue
 rel=p.relative_to(SRC/'system')
 if rel.parts[:2] in [('data','knowledge'),('data','logs'),('data','state')]:continue
 manifest.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
config={'population_requests':len(jobs),'selected_requests':target,'fraction':target/len(jobs),'selected_grades':sum(len(j['entries']) for j in selected),'llm_enabled':True,'only_format':'common','profile':'r69-migration-preview','source_installation':str(SRC),'source_database_sha256':hashlib.sha256((SRC/'system/data/knowledge/common.sqlite').read_bytes()).hexdigest(),'test_database_sha256':hashlib.sha256(db.read_bytes()).hexdigest(),'population_jobs_sha256':hashlib.sha256(source_jobs.read_bytes()).hexdigest(),'selection_seed':'r70-half-v1','selection':'deterministic proportional allocation by locale, corpus, domain, style; largest remainders with seeded tie order','selected_locales':dict(collections.Counter(j['locale'] for j in selected)),'population_strata':len(groups),'selected_strata':len({stratum(j) for j in selected}),'execution':'actual new-chat engine in isolated subprocesses; no TCP/browser/load certification','booking':'controlled unavailable, no real occupancy oracle','reference_clock':'2026-10-16T12:00:00+07:00; reference_date jobs preserve their own date','application_snapshot_changed':False,'source_manifest':manifest}
(OUT/'CONFIG.json').write_text(json.dumps(config,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in config.items() if k!='source_manifest'},ensure_ascii=False,indent=2))
