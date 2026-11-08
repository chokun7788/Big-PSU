"""Freeze current common build and draw 1,000 unique retained large-corpus jobs."""
from pathlib import Path
import collections,hashlib,json,math,shutil
B=Path(__file__).resolve().parent;R=B/'r93_random_1000_common_on_20261018';R.mkdir(exist_ok=False)
S=B/'r78_web_session_check_20261016/system';F=R/'system';P=B/'r88_full_common_llm_20261017'
seed='psu-r93-1000-20261018-v1'
all_jobs=[json.loads(s) for s in (P/'SELECTED_JOBS.jsonl').read_text('utf8').splitlines() if s.strip()]
assert len(all_jobs)==len({j['key'] for j in all_jobs})==20554
groups=collections.defaultdict(list)
for j in all_jobs:groups[(j['locale'],j['r70_stratum']['domain'])].append(j)
# Cover every nonempty locale/domain cell, then allocate remaining slots by
# proportional largest remainder. Document this coverage-driven sampling.
n=1000;remaining=n-len(groups);alloc={k:1+int(remaining*len(v)/len(all_jobs)) for k,v in groups.items()}
remainders=sorted(groups,key=lambda k:(-(remaining*len(groups[k])/len(all_jobs)%1),str(k)))
for k in remainders[:n-sum(alloc.values())]:alloc[k]+=1
chosen=[]
for k,v in sorted(groups.items()):
 rank=lambda j:hashlib.sha256((seed+'|'+j['key']).encode()).hexdigest()
 chosen.extend(sorted(v,key=rank)[:alloc[k]])
chosen.sort(key=lambda j:hashlib.sha256((seed+'|run-order|'+j['key']).encode()).hexdigest())
assert len(chosen)==len({j['key'] for j in chosen})==1000
with (R/'SELECTED_JOBS.jsonl').open('x',encoding='utf8') as f:
 for j in chosen:f.write(json.dumps(j,ensure_ascii=False)+'\n')
manifest=[]
for folder in ['app','tools','booking_dashboard','web_chat','data']:
 for p in (S/folder).rglob('*'):
  if not p.is_file():continue
  rel=p.relative_to(S);parts=rel.parts
  if '__pycache__' in parts or p.suffix in {'.pyc','.log'} or '-wal' in p.name or '-shm' in p.name:continue
  if len(parts)>1 and parts[0]=='data' and parts[1] in {'eval','vector','common_test_tmp'}:continue
  dest=F/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
  manifest.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
for name in ['run_common.py','reference_grader.py','analyze.py']:
 shutil.copy2(P/name,R/name)
run=R/'run_common.py';text=run.read_text('utf8').replace('R88 controlled unavailable','R93 controlled unavailable').replace('r88-common-on-','r93-common-on-')
run.write_text(text,'utf8')
config={
 'created_date_th':'2026-10-18','sample_seed':seed,'population_requests':len(all_jobs),'selected_requests':len(chosen),
 'selected_grades':sum(len(j['entries']) for j in chosen),'fraction':len(chosen)/len(all_jobs),'llm_enabled':True,'only_format':'common',
 'profile':'r69-migration-preview','source_release':'R92 installed revision 3','source_installation':str(S.parent),
 'source_database_sha256':hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest(),
 'test_database_sha256':hashlib.sha256((F/'data/knowledge/common.sqlite').read_bytes()).hexdigest(),
 'population_jobs_sha256':hashlib.sha256((P/'SELECTED_JOBS.jsonl').read_bytes()).hexdigest(),
 'frozen_jobs_sha256':hashlib.sha256((R/'SELECTED_JOBS.jsonl').read_bytes()).hexdigest(),
 'selection':'Fixed seeded hash ranking in locale/domain strata; >=1 per nonempty cell, remainder proportional by largest remainder. No selection by pass/fail.',
 'strata_count':len(groups),'selected_locales':dict(collections.Counter(j['locale'] for j in chosen)),
 'execution':'actual frozen current engine; two isolated evaluator processes with one shared local-model slot; not an HTTP/load test',
 'booking':'controlled unavailable as in R88; no live occupancy oracle','reference_clock':'2026-10-16T12:00:00+07:00; per-job reference dates override, matches retained R88',
 'histories_in_population':0,'multi_turn_tested':False,'application_snapshot_changed':False,'source_manifest':manifest,
 'snapshot_exclusions':['data/eval (selected contracts retained in jobs)','data/vector (RAG fallback disabled)','data/common_test_tmp','__pycache__','*.pyc','*.log','SQLite WAL/SHM'],
}
(R/'CONFIG.json').write_text(json.dumps(config,ensure_ascii=False,indent=2),'utf8')
alloc_rows=[{'locale':k[0],'domain':k[1],'population':len(groups[k]),'selected':alloc[k]} for k in sorted(groups)]
(R/'SAMPLE_ALLOCATION.json').write_text(json.dumps(alloc_rows,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'output':str(R),'questions':len(chosen),'grades':config['selected_grades'],'locales':config['selected_locales'],'strata':len(groups),'snapshot_files':len(manifest),'snapshot_mb':round(sum(x['bytes'] for x in manifest)/1024**2,2)},ensure_ascii=False))
