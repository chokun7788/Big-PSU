from pathlib import Path
import json,shutil,difflib,subprocess,sqlite3
from prepare import B,SYSTEM,ROOT,PACK,sha,dbhash
OLD=json.loads((B/'BEFORE.json').read_text());EXTRA=json.loads((B/'EXTRA_BEFORE.json').read_text())
CHANGED=['app/knowledge/common/answer.py','app/knowledge/common/planner.py','app/knowledge/common/query_contract.py','app/pipeline/engine.py','app/knowledge/common/owner_server.py']
NEW=['app/knowledge/common/schema_descriptions.json','app/knowledge/common/schema_language.py','tests/test_common_generalization_r60.py']
DOCS=['Flow.md','RESULTS_TH.md','ANALYSIS_TH.md']
if (B/'DELIVERY_RECEIPT.json').exists():raise RuntimeError('Already delivered; no repeat mutation')
for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
 expected={**OLD['files'][label],**EXTRA[label]}
 for name,h in expected.items():
  if label=='candidate' and name in CHANGED:continue
  if sha(root/name)!=h:raise RuntimeError(f'Concurrent edit detected: {label}/{name}')
 for name in NEW:
  if label!='candidate' and (root/name).exists() and sha(root/name)!=sha(SYSTEM/name):raise RuntimeError('Unexpected existing file: '+str(root/name))
 if (root/'docs/common_content_r60_20261012').exists():raise RuntimeError('Documentation destination exists')
for path,h in OLD['dbs'].items():
 if dbhash(Path(path))!=h:raise RuntimeError('Database changed since baseline: '+path)
diff=B/'diffs';diff.mkdir(exist_ok=False)
for name in CHANGED+NEW:
 before=B/'before/candidate'/name
 txt=before.read_text(encoding='utf-8') if before.exists() else ''
 change=''.join(difflib.unified_diff(txt.splitlines(True),(SYSTEM/name).read_text(encoding='utf-8').splitlines(True),fromfile='before/'+name,tofile='r60/'+name))
 (diff/(name.replace('/','__')+'.diff')).write_text(change,encoding='utf-8')
for label,root in [('project',ROOT),('package',PACK)]:
 # New dependencies first; process reload still requires a normal restart.
 for name in NEW+CHANGED:
  dest=root/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SYSTEM/name,dest)
for root in [SYSTEM,ROOT,PACK]:
 d=root/'docs/common_content_r60_20261012';d.mkdir(parents=True)
 for name in DOCS:shutil.copy2(B/name,d/name)
 # Keep the referenced paper report beside each delivered document collection.
 shutil.copy2(B.parent/'r59_schema_repair_20261012/Research.md',d/'RESEARCH_R59.md')
receipts={}
for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
 receipts[label]={name:sha(root/name) for name in CHANGED+NEW}
 assert receipts[label]==receipts['candidate']
afterdb={p:dbhash(Path(p)) for p in OLD['dbs']};assert afterdb==OLD['dbs']
git=subprocess.check_output(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],text=True,encoding='utf-8')
with (B/'GIT_AFTER.txt').open('x',encoding='utf-8') as f:f.write(git)
beforelines=(B/'GIT_BEFORE.txt').read_text(encoding='utf-8').splitlines();afterlines=git.splitlines()
missing=[s for s in beforelines if s not in afterlines]
if missing:raise RuntimeError('Old Git entries changed unexpectedly: '+repr(missing))
with sqlite3.connect('file:'+ (ROOT/'data/knowledge/approved.sqlite').as_posix()+'?mode=ro',uri=True) as c:
 tables=[r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cc_%'")]
 counts={t:c.execute('SELECT count(*) FROM '+t).fetchone()[0] for t in tables}
res={'hashes':receipts,'db_logical_hashes_unchanged':True,'db_hashes':afterdb,'all_before_git_status_entries_retained':True,'old_git_entries':len(beforelines),'new_git_entries':len(afterlines)-len(beforelines),'production_common_table_counts':counts,'backups':'before/','diffs':'diffs/','restarted_user_servers':False,'demo_not_copied_to_production':True,'compressed_archives_updated':False}
with (B/'DELIVERY_RECEIPT.json').open('x',encoding='utf-8') as f:json.dump(res,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in res.items() if k not in ['hashes','db_hashes']},ensure_ascii=False,indent=2))
