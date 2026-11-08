import collections,hashlib,json,shutil,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
stage=B/'system'
if stage.exists():raise SystemExit('Existing stage preserved')
stage.mkdir();files=[]
for folder in ['app','tools','tests','web_chat','booking_dashboard','data']:
 source=ROOT/folder
 for p in source.rglob('*'):
  if not p.is_file():continue
  rel=p.relative_to(ROOT)
  if any(x in rel.parts for x in ['__pycache__','logs','common_test_tmp','knowledge_inbox','human_review']):continue
  if rel.parts[:2]==('data','knowledge'):continue
  if p.suffix in {'.pyc','.sqlite','.sqlite-shm','.sqlite-wal','.db'}:continue
  dest=stage/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
  files.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
for p in ROOT.iterdir():
 if p.is_file() and p.suffix in {'.ps1','.cmd','.bat','.toml','.txt','.json','.ini'}:
  # Only public launch/config declarations; no credential-bearing .env copy.
  if p.name.startswith('.') or any(x in p.name.lower() for x in ['secret','credential','token']):continue
  shutil.copy2(p,stage/p.name)
for mode,source in [('legacy',ROOT/'data/knowledge/approved.sqlite'),('common',ROOT/'data/knowledge/migration_r63_20261013/approved.sqlite')]:
 db=B/(mode+'.sqlite')
 with sqlite3.connect(source.as_uri()+'?mode=ro',uri=True) as c,sqlite3.connect(db) as d:c.backup(d)
originaldata=stage/'data/knowledge';originaldata.mkdir(parents=True)
shutil.copy2(B/'legacy.sqlite',originaldata/'approved.sqlite')
(B/'SOURCE_MANIFEST.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf-8')
inventory=[];jobs={};sessions=[];guard=[];seen={}
def read(p):
 data=json.loads(p.read_text(encoding='utf-8-sig')) if p.suffix=='.json' else [json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
 return data if isinstance(data,list) else data.get('cases',[]) if isinstance(data,dict) else []
def key(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
paths=sorted([*(stage/'data/eval').glob('*.json'),*(stage/'data/eval').glob('*.jsonl'),*(stage/'data/ground_truth').glob('*.jsonl'),*(stage/'data/routing').glob('*eval*.jsonl')])
for p in paths:
 rows=read(p);relative=p.relative_to(stage).as_posix();record={'file':relative,'rows':len(rows),'question_grades':0,'sessions':0,'blank_questions':0,'guard_rows':0,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 if not rows:record['status']='metadata_not_questions';inventory.append(record);continue
 fingerprint=key(rows)
 if fingerprint in seen:record.update(status='exact_alias',alias_of=seen[fingerprint]);inventory.append(record);continue
 seen[fingerprint]=relative;record['status']='included'
 for idx,c in enumerate(rows):
  if not isinstance(c,dict):continue
  if c.get('turns') or c.get('kind')=='session':sessions.append({'file':relative,'row':idx,'case':c});record['sessions']+=1;continue
  if c.get('observed_input'):
   guard.append({'file':relative,'row':idx,'case':c});record['guard_rows']+=1;continue
  if 'noisy_question' in c:variants=[('clean',c.get('clean_question')),('noisy',c['noisy_question'])]
  elif 'noisy' in c:variants=[('clean',c.get('clean')),('noisy',c['noisy'])]
  else:variants=[('question',c.get('question_en') or c.get('question') or c.get('query'))]
  for variant,q in variants:
   if not isinstance(q,str) or not q.strip():record['blank_questions']+=1;continue
   locale=c.get('locale') or ('en' if 'question_en' in c or p.name.startswith('english_') else 'auto')
   ref=str((c.get('metadata') or {}).get('reference_date','')) if c.get('domain')=='weekday_live_slots' else ''
   h=key([q,locale,ref]);job=jobs.setdefault(h,{'key':h,'question':q,'locale':locale,'reference_date':ref,'entries':[]})
   job['entries'].append({'file':relative,'row':idx,'variant':variant,'case':dict(c,question=q,locale=locale)});record['question_grades']+=1
 inventory.append(record)
with (B/'JOBS.jsonl').open('x',encoding='utf-8') as f:
 for job in jobs.values():f.write(json.dumps(job,ensure_ascii=False)+'\n')
for name,rows in [('SESSIONS',sessions),('GUARDS',guard)]:
 (B/(name+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'files':inventory,'unique_requests':len(jobs),'case_grades':sum(len(j['entries']) for j in jobs.values()),'session_cases':len(sessions),'guard_cases':len(guard),'python_tests':len(list((stage/'tests').glob('test_*.py'))),'smoke_python_files':len(list((stage/'tests').glob('smoke_test*.py'))),'powershell_smokes':len(list((stage/'tests').glob('smoke_test*.ps1'))),'copied_bytes':sum(x['bytes'] for x in files)}
(B/'INVENTORY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='files'},ensure_ascii=False),flush=True)
