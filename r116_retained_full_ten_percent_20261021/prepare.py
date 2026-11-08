"""Freeze an unbiased 10% of each ORIGINAL full-corpus domain, plus R115."""
import collections,gzip,hashlib,json,math,os,shutil,sqlite3,zlib
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent;B=R.parent;S=B/'r115_native_http_validation_20261021/system';F=R/'system'
SEED='psu-r116-original-full-per-domain-10pct-20261021-v1'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def ext(p):return '\\\\?\\'+str(p.resolve()) if os.name=='nt' else str(p)
def write(p,v):
 with p.open('x',encoding='utf8') as f:json.dump(v,f,ensure_ascii=False,indent=2)
assert not F.exists(),'Refuse to overwrite candidate'
population=B/'r88_full_common_llm_20261017/SELECTED_JOBS.jsonl'
legacy_jobs=B/'r64_full_comparison_20261013/JOBS.jsonl'
jobs=[json.loads(l) for l in population.open(encoding='utf8')]
old={j['key']:j for j in map(json.loads,legacy_jobs.open(encoding='utf8'))}
assert len(jobs)==len(old)==20554 and len({j['key'] for j in jobs})==20554
for j in jobs:
 o=old[j['key']]
 assert all(j[k]==o[k] for k in ['question','locale','reference_date','entries'])
groups=collections.defaultdict(list)
for j in jobs:groups[j['r70_stratum']['domain']].append(j)
chosen=[];allocation=[]
for domain,group in sorted(groups.items()):
 n=math.ceil(len(group)/10);bylocale=collections.defaultdict(list)
 for j in group:bylocale[j['locale']].append(j)
 alloc={l:int(n*len(v)/len(group)) for l,v in bylocale.items()}
 remainder=sorted(bylocale,key=lambda l:(-(n*len(bylocale[l])/len(group)%1),l))
 for l in remainder[:n-sum(alloc.values())]:alloc[l]+=1
 selected=[]
 for l,v in sorted(bylocale.items()):
  selected+=sorted(v,key=lambda j:hashlib.sha256((SEED+'|'+domain+'|'+j['key']).encode()).hexdigest())[:alloc[l]]
 assert len(selected)==n
 chosen+=selected
 allocation.append({'domain':domain,'population':len(group),'selected':n,'fraction':n/len(group),'selected_by_locale':alloc,'population_by_locale':{l:len(v) for l,v in bylocale.items()}})
chosen.sort(key=lambda j:(j.get('reference_date',''),hashlib.sha256((SEED+'|order|'+j['key']).encode()).hexdigest()))
assert len(chosen)==len({j['key'] for j in chosen})==2108
with (R/'SELECTED_JOBS.jsonl').open('x',encoding='utf8') as f:
 for j in chosen:f.write(json.dumps(j,ensure_ascii=False)+'\n')
write(R/'SAMPLE_ALLOCATION.json',allocation)
reference_files={str(p.resolve()):sha(p) for p in [population,legacy_jobs,B/'r89_saved_full_comparison_20261018/PER_REQUEST_COMPARISON.jsonl.gz',B/'r115_native_http_validation_20261021/COMPARISON_FINAL.json']}
files=[p for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm'))]
reference_files.update({str(p.resolve()):sha(p) for p in files})
shutil.copytree(ext(S),ext(F),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.sqlite-wal','*.sqlite-shm','owner-session.json'))
# SQLite backup ensures a consistent independent DB without changing approvals.
with sqlite3.connect((S/'data/knowledge/common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(F/'data/knowledge/common.sqlite') as dst:src.backup(dst)
shutil.copy2(B/'r88_full_common_llm_20261017/reference_grader.py',R/'reference_grader.py')
shutil.copy2(B/'r88_full_common_llm_20261017/analyze.py',R/'retained_literal.py')
evidence=B/'r65_detailed_failure_analysis_20261014/evidence.sqlite'
with sqlite3.connect(evidence.as_uri()+'?mode=ro',uri=True) as c,(R/'SAVED_LEGACY_LLM.jsonl').open('x',encoding='utf8') as f:
 c.row_factory=sqlite3.Row
 assert c.execute("select count(*) from results where arm='legacy_llm'").fetchone()[0]==20554
 for j in chosen:
  row=c.execute("select raw from results where arm='legacy_llm' and key=?",(j['key'],)).fetchone();assert row is not None
  raw=json.loads(zlib.decompress(row['raw']));assert raw['question']==j['question'] and raw['requested_locale']==j['locale']
  assert len(raw['grades'])==len(j['entries'])
  f.write(json.dumps(raw,ensure_ascii=False)+'\n')
keys={j['key'] for j in chosen};r89={}
with gzip.open(B/'r89_saved_full_comparison_20261018/PER_REQUEST_COMPARISON.jsonl.gz','rt',encoding='utf8') as f:
 for line in f:
  x=json.loads(line)
  if x['key'] in keys:r89[x['key']]=x
assert set(r89)==keys
write(R/'SAVED_R89_COHORT.json',r89)
write(R/'REFERENCE_HASHES.json',reference_files)
write(R/'SELECTION_MANIFEST.json',{'seed':SEED,'population':20554,'categories':len(groups),'requests':len(chosen),'grades':sum(len(j['entries']) for j in chosen),
 'fraction':len(chosen)/20554,'new_questions':0,'sample_sha256':sha(R/'SELECTED_JOBS.jsonl'),'population_sha256':sha(population),
 'legacy_population_sha256':sha(legacy_jobs),'selection':'ceil(0.10*N) per ORIGINAL retained domain; proportional requested-locale allocation by largest remainder; seeded hash ranking, no response/pass-based filtering',
 'locales':dict(collections.Counter(j['locale'] for j in chosen)),'reference_date_overrides':dict(collections.Counter(j.get('reference_date','') for j in chosen)),
 'baseline':'Saved R64 legacy_llm results only; no baseline rerun','candidate':'Frozen R115, no fixes during benchmark',
 'default_reference_clock':'2026-10-21T12:00:00+07:00','historical_clock_policy':'Retain per-job reference_date; old saved results have older source/runtime dates, so differences are not flow-only causal effects',
 'execution':'real /api/chat serial requests; one new session per original request key; LLM ON; no category hint',
 'booking':'Controlled unavailable as in original full workload, no customer occupancy oracle; no fake booking/news facts inserted',
 'snapshot_source_files':len(files),'reference_files':len(reference_files),'created_at':datetime.now().astimezone().isoformat()})
write(R/'STATUS.json',{'phase':'prepared','complete':False,'requests_target':len(chosen),'new_questions':0,'production_installed':False})
assert all(sha(Path(p))==h for p,h in reference_files.items())
print(json.dumps({'requests':len(chosen),'grades':sum(len(j['entries']) for j in chosen),'domains':len(groups),'locales':dict(collections.Counter(j['locale'] for j in chosen)),'new_questions':0},ensure_ascii=False))
