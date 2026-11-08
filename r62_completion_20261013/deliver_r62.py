"""Hash-guarded additive delivery. Facts/approvals/logs are not replaced."""
import json,shutil,subprocess,difflib,ast
from pathlib import Path
from prepare import B,SYSTEM,ROOT,PACK,sha,dbhash
before=json.loads((B/'BEFORE.json').read_text(encoding='utf-8'))
for file in ['EXTRA_BEFORE.json','EXTRA2_BEFORE.json']:
 extra=json.loads((B/file).read_text(encoding='utf-8'))
 for label,items in extra.items():before['files'][label].update(items)
# This wrapper was omitted from the initial backup list. Root/package originals
# are still untouched and are backed up before any delivery. Preserve this caveat.
late={}
wrapper='Open-PSU-Esports-Chatbot.ps1'
for label,root in [('project',ROOT),('package',PACK)]:
 if (root/wrapper).exists():
  late[label]={wrapper:sha(root/wrapper)}
  dest=B/'before'/label/wrapper;dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists():raise RuntimeError('Late backup already exists')
  shutil.copy2(root/wrapper,dest);before['files'][label].update(late[label])
if (PACK/wrapper).exists() and wrapper not in before['files']['candidate']:
 original=PACK/wrapper;dest=B/'before/candidate'/wrapper
 shutil.copy2(original,dest);before['files']['candidate'][wrapper]=sha(original)
 (B/'LATE_BACKUP_NOTE.json').write_text(json.dumps({'wrapper':wrapper,'target_originals':late,'candidate_original_recovered_from_untouched_package':True,'not_initial_candidate_hash_proof':True},indent=2),encoding='utf-8')
existing=list(before['files']['candidate'])
changed=[name for name in existing if sha(SYSTEM/name)!=before['files']['candidate'][name]]
common=[p.relative_to(SYSTEM).as_posix() for p in (SYSTEM/'app/knowledge/common').iterdir() if p.suffix in {'.py','.json'}]
new=[name for name in common if name not in existing]
new+=['Portable-Models.ps1','Model-Manifest-Check.py','PRODUCTION_OPERATION_TH.md','tests/test_common_r62.py']
names=list(dict.fromkeys(changed+new))
for label,root in [('project',ROOT),('package',PACK)]:
 for name,h in before['files'][label].items():
  assert sha(root/name)==h,'Concurrent edit: '+str(root/name)
 for name in names:
  if (root/name).exists() and name not in before['files'][label]:
   assert sha(root/name)==sha(SYSTEM/name),'Unbacked existing file: '+str(root/name)
 # Do not replace differing unbacked wrapper customizations.
 if (root/wrapper).exists() and sha(root/wrapper)!=before['files']['candidate'][wrapper]:
  raise RuntimeError('Wrapper differs from preserved candidate baseline; merge explicitly: '+str(root/wrapper))
for path,h in before['dbs'].items():assert dbhash(Path(path))==h,'Owner or fixture database changed: '+path
diffdir=B/'diffs';diffdir.mkdir(exist_ok=False)
for name in names:
 if name.endswith('.py'):ast.parse((SYSTEM/name).read_text(encoding='utf-8'))
 old=B/'before/candidate'/name
 patch=''.join(difflib.unified_diff((old.read_text(encoding='utf-8') if old.exists() else '').splitlines(True),(SYSTEM/name).read_text(encoding='utf-8').splitlines(True),fromfile='before/'+name,tofile='r62/'+name))
 (diffdir/(name.replace('/','__')+'.diff')).write_text(patch,encoding='utf-8')
for root in [ROOT,PACK]:
 for name in names:
  target=root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SYSTEM/name,target)
for root in [SYSTEM,ROOT,PACK]:
 docs=root/'docs/common_content_r62_20261013';docs.mkdir(parents=True,exist_ok=False)
 for name in ['FLOW_PRODUCTION_TH.md','RESULTS_TH.md']:shutil.copy2(B/name,docs/name)
hashes={label:{name:sha(root/name) for name in names} for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]}
assert hashes['candidate']==hashes['project']==hashes['package']
for path,h in before['dbs'].items():assert dbhash(Path(path))==h
git=subprocess.check_output(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],text=True,encoding='utf-8')
(B/'GIT_AFTER.txt').write_text(git,encoding='utf-8')
old=(B/'GIT_BEFORE.txt').read_text(encoding='utf-8').splitlines()
assert all(line in git.splitlines() for line in old),'Prior Git status entry lost'
receipt={'changed_files':changed,'new_files':new,'source_hashes':hashes,'databases_unchanged':True,'db_hashes':before['dbs'],'old_git_entries':len(old),'all_prior_git_entries_retained':True,'facts_approved_or_published_by_agent':False,'original_logs_replaced':False,'late_wrapper_backup_caveat':'see LATE_BACKUP_NOTE.json'}
(B/'DELIVERY_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print('Delivered',len(changed),'updated and',len(new),'new files. Prior Git entries:',len(old),'Databases unchanged.')
