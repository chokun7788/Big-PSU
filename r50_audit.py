import json,hashlib,difflib,subprocess
from pathlib import Path
import r50_probe as r
root=r.old.old.p.ROOT;before=json.loads((r.OUT/'before_manifest.json').read_text());release=Path((r.OUT/'release_r50_2_path.txt').read_text())
changed=[k for k,v in before.items() if not (root/k).is_file() or hashlib.sha256((root/k).read_bytes()).hexdigest()!=v]
assert set(changed)=={'app/session/conversation_store.py','app/session/task_memory.py','app/session/service_fact_dialogue.py','app/pipeline/service_fact_query.py','app/pipeline/user_service_facts.py','app/pipeline/competition_targets.py','app/pipeline/competition_taxonomy.py','app/pipeline/competition_detail.py','tests/test_service_fact_dialogue_r49.py'},changed
checks={}
for folder in ('app','web_chat','data/curated','data/rules','data/competition_rules','data/locales','data/sources'):
 for p in (root/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:
   rel=p.relative_to(root).as_posix();checks[rel]=(release/rel).is_file() and p.read_bytes()==(release/rel).read_bytes()
assert all(checks.values()),[k for k,v in checks.items() if not v]
with (r.OUT/'SOURCE_RELEASE_AUDIT_R50.json').open('x') as f:json.dump(dict(changed_existing_files=changed,new_source_files=['app/session/state_persistence.py','tests/test_state_persistence_r50.py'],all_other_before_files_unchanged=len(before)-len(changed),data_files_unchanged=not any(k.startswith('data/') for k in changed),passed_file_checks=sum(checks.values()),total_file_checks=len(checks),checks=checks),f,indent=2)
with (r.OUT/'SOURCE_CHANGES_R50.diff').open('x',encoding='utf-8') as f:f.write(''.join(''.join(difflib.unified_diff((r.OUT/'before'/k).read_text(encoding='utf-8').splitlines(True),(root/k).read_text(encoding='utf-8').splitlines(True),fromfile='before/'+k,tofile='after/'+k)) for k in changed))
for args,label in [(['status','--short'],'GIT_STATUS_R50.txt'),(['diff','--check'],'GIT_DIFF_CHECK_R50.txt')]:
 p=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','-C',str(root),*args],capture_output=True,text=True,encoding='utf-8')
 with (r.OUT/label).open('x',encoding='utf-8') as f:f.write(f'exit_code={p.returncode}\n'+p.stdout+p.stderr)
 assert p.returncode==0
print('files',sum(checks.values()),'/',len(checks),'existing changed',len(changed),'data unchanged',flush=True)
