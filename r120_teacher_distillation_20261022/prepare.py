"""Prepare isolated teacher/student snapshots and disjoint retained workloads."""
import collections,hashlib,json,re,shutil,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent;OLD=P/'r119_complete_source_audit_20261021';S=R/'system';T=R/'teacher_system';LEG=P/'r64_full_comparison_20261013'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def write(n,v):(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def readlines(p):return list(map(json.loads,p.open(encoding='utf8')))
protected={str(p.resolve()):sha(p) for root in [OLD/'system',LEG/'system'] for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith(('-wal','-shm'))}
for p in [LEG/'legacy.sqlite',OLD/'http03/RESULTS.jsonl',OLD/'http03/TEST_COMPLETE.json']:protected[str(p.resolve())]=sha(p)
write('PROTECTED_INPUTS.json',protected)
for origin,target in [(OLD/'system',S),(LEG/'system',T)]:
 shutil.copytree('\\\\?\\'+str(origin.resolve()),'\\\\?\\'+str(target.resolve()),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.pyo','*-wal','*-shm','owner-session.json'))
with sqlite3.connect((OLD/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(S/'data/knowledge/common.sqlite') as dst:src.backup(dst)
with sqlite3.connect((LEG/'legacy.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(R/'teacher.sqlite') as dst:src.backup(dst)
jobs=readlines(P/'r116_retained_full_ten_percent_20261021/SELECTED_JOBS.jsonl');teacher={r['key']:r for r in readlines(P/'r116_retained_full_ten_percent_20261021/BASELINE_SCORED_V2.jsonl')};dev=readlines(OLD/'SELECTED_JOBS.jsonl')
# Connected components of shared source case/origin IDs prevent corpus/typo
# variants of the same retained case crossing teaching and evaluation splits.
parent={j['key']:j['key'] for j in jobs};owners={}
def root(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
def union(a,b):parent[root(a)]=root(b)
def identities(j):
 out=set()
 for e in j['entries']:
  c=e['case']
  for k in ['id','origin_id']:
   v=c.get(k)
   if v:out.add(k+':'+str(v).replace('-TH-','-LANG-').replace('-EN-','-LANG-'))
 return out
for j in jobs:
 for ident in identities(j):
  if ident in owners:union(j['key'],owners[ident])
  else:owners[ident]=j['key']
groups={j['key']:root(j['key']) for j in jobs};devgroups={groups[j['key']] for j in dev}
route_map={'service_fee':'service_fee','reservation':'reservation','rules':'rules','penalty':'rules','competition_rules':'competition_rules','games':'games','game_controls':'game_controls','equipment':'equipment','schedule':'schedule','overview':'contact','contact':'contact'}
eligible=[]
for j in jobs:
 b=teacher[j['key']];a=b.get('result') or {};route=(a.get('route') or {}).get('category');domain=route_map.get(route)
 if not domain or groups[j['key']] in devgroups or not a.get('answer') or not (a.get('validation') or {}).get('ok'):continue
 if any(g['positive_literal'] and not g['literal_passed'] for g in b['grades']):continue
 if a.get('confidence',0)<.85 or 'unavailable' in a.get('mode','') or 'no_answer' in a.get('mode',''):continue
 eligible.append((hashlib.sha256(('r120:'+j['key']).encode()).hexdigest(),j,domain))
eligible.sort();holdout=[];heldgroups=set();counts=collections.Counter()
for _,j,domain in eligible:
 if counts[domain]>=3 or groups[j['key']] in heldgroups:continue
 holdout.append(j);heldgroups.add(groups[j['key']]);counts[domain]+=1
 if len(holdout)>=30:break
train=[];used=set();tc=collections.Counter()
for _,j,domain in eligible:
 if groups[j['key']] in heldgroups or groups[j['key']] in used or tc[domain]>=8:continue
 train.append(j);used.add(groups[j['key']]);tc[domain]+=1
 if len(train)>=64:break
assert len(train)>=40 and len(holdout)>=24 and not used&heldgroups and not (used|heldgroups)&devgroups
for name,rows in [('TEACHING_JOBS.jsonl',train),('HOLDOUT_JOBS.jsonl',holdout),('DEVELOPMENT_JOBS.jsonl',dev)]:
 (R/name).write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in rows),'utf8')
(R/'SAVED_TEACHER_TEACHING.jsonl').write_text(''.join(json.dumps(teacher[j['key']],ensure_ascii=False)+'\n' for j in train),'utf8')
write('SPLIT_MANIFEST.json',{'teaching':len(train),'evaluation':len(holdout),'development':len(dev),'teaching_domains':dict(tc),'evaluation_domains':dict(counts),'source_case_family_overlap':0,'teaching_keys':[j['key'] for j in train],'evaluation_keys':[j['key'] for j in holdout], 'new_questions':0,'clock':'2026-10-21T12:00:00+07:00','grouping':'connected components of retained case IDs and origin IDs, with TH/EN ID prefixes normalized','limitation':'Semantic near-duplicates with unrelated source IDs may remain. Evaluation is a small retained development pilot, not a new real-user or Full accuracy estimate.'})
for n in ['evaluation.py','reference_grader.py','retained_literal.py','serve_frozen.py']:
 shutil.copy2(OLD/n,R/n)
write('STATUS.json',{'phase':'prepared_teacher_student_distillation','complete':False,'weights_changed':False,'production_installed':False})
print(json.dumps({'teaching':len(train),'evaluation':len(holdout),'development':len(dev),'protected_files':len(protected),'family_overlap':0}))
