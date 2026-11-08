import json,shutil,subprocess,difflib,ast
from pathlib import Path
from prepare import B,SYSTEM,ROOT,PACK,sha,dbhash
before=json.loads((B/'BEFORE.json').read_text());extra=json.loads((B/'EXTRA_BEFORE.json').read_text())
for label in before['files']:before['files'][label].update(extra[label])
existing=list(before['files']['candidate'])
changed=[n for n in existing if sha(SYSTEM/n)!=before['files']['candidate'][n]]
allcommon=[str(p.relative_to(SYSTEM)).replace('\\','/') for p in (SYSTEM/'app/knowledge/common').iterdir() if p.suffix in {'.py','.json'}]
new=[n for n in allcommon if n not in existing]+['app/knowledge/model_gate.py','tests/test_common_r61.py']
for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
 for name,h in before['files'][label].items():
  if label=='candidate' and name in changed:continue
  assert sha(root/name)==h,'Concurrent edit: '+str(root/name)
 for name in new:
  if label!='candidate' and (root/name).exists():raise RuntimeError('Unexpected file: '+str(root/name))
 assert not (root/'docs/common_content_r61_20261013').exists()
for p,h in before['dbs'].items():assert dbhash(Path(p))==h,'Database changed: '+p
for name in changed+new:
 if name.endswith('.py'):ast.parse((SYSTEM/name).read_text(encoding='utf-8'))
diff=B/'diffs';diff.mkdir(exist_ok=False)
for name in changed+new:
 old=B/'before/candidate'/name;oldtext=old.read_text(encoding='utf-8') if old.exists() else ''
 patch=''.join(difflib.unified_diff(oldtext.splitlines(True),(SYSTEM/name).read_text(encoding='utf-8').splitlines(True),fromfile='before/'+name,tofile='r61/'+name))
 (diff/(name.replace('/','__')+'.diff')).write_text(patch,encoding='utf-8')
for label,root in [('project',ROOT),('package',PACK)]:
 for name in new+changed:
  dest=root/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SYSTEM/name,dest)
for root in [SYSTEM,ROOT,PACK]:
 d=root/'docs/common_content_r61_20261013';d.mkdir(parents=True)
 for name in ['Flow.md','RESULTS_TH.md']:shutil.copy2(B/name,d/name)
hashes={label:{n:sha(root/n) for n in new+changed} for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]}
assert hashes['candidate']==hashes['project']==hashes['package']
for p,h in before['dbs'].items():assert dbhash(Path(p))==h
git=subprocess.check_output(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],text=True,encoding='utf-8')
with (B/'GIT_AFTER.txt').open('x',encoding='utf-8') as f:f.write(git)
oldlines=(B/'GIT_BEFORE.txt').read_text(encoding='utf-8').splitlines();assert all(line in git.splitlines() for line in oldlines),'Old Git status entry changed'
receipt={'source_hashes':hashes,'dbs_unchanged':True,'before_db_hashes':before['dbs'],'all_old_git_status_entries_retained':True,'old_git_entries':len(oldlines),'new_files':new,'changed_files':changed,'new_diff_backup_only':True,'facts_approved_or_published':False,'user_processes_restarted':False,'archives_rebuilt':False}
with (B/'DELIVERY_RECEIPT.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print('Delivered',len(changed),'updated and',len(new),'new files; databases and prior Git entries preserved')
