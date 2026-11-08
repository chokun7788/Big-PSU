import json,hashlib,difflib,subprocess
from pathlib import Path
import r49_probe as r
root=r.old.p.ROOT;before=json.loads((r.OUT/'before_manifest.json').read_text())
changed=[k for k,v in before.items() if not (root/k).is_file() or hashlib.sha256((root/k).read_bytes()).hexdigest()!=v]
expected={'app/pipeline/engine.py','app/pipeline/user_service_facts.py','app/session/conversation_store.py','app/session/context_resolver.py','app/web_api/server.py','tests/test_user_service_facts_r48.py'}
assert set(changed)==expected,changed
release=Path((r.OUT/'release_r49_2_path.txt').read_text());checks={};new=[]
for folder in ('app','tests','web_chat','data/curated','data/rules'):
 for p in (root/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:
   rel=p.relative_to(root).as_posix()
   if rel not in before:new.append(rel)
   if folder!='tests':checks[rel]=(release/rel).is_file() and p.read_bytes()==(release/rel).read_bytes()
raw='data/sources/user_service_answers_20261008.json'
checks[raw]=(root/raw).read_bytes()==(release/raw).read_bytes()
assert all(checks.values()),[k for k,v in checks.items() if not v]
evidence=dict(changed_existing_files=changed,new_files=new,source_release_file_checks=checks,passed_file_checks=sum(checks.values()),total_file_checks=len(checks),previous_data_rules_curated_unchanged=all(k not in changed for k in before if k.startswith('data/')),all_other_snapshotted_existing_files_unchanged=len(before)-len(changed))
with (r.OUT/'SOURCE_AND_RELEASE_AUDIT_R49_2.json').open('x',encoding='utf-8') as f:json.dump(evidence,f,indent=2)
diff=''.join(''.join(difflib.unified_diff((r.OUT/'before'/k).read_text(encoding='utf-8').splitlines(True),(root/k).read_text(encoding='utf-8').splitlines(True),fromfile='before/'+k,tofile='after/'+k)) for k in changed)
with (r.OUT/'SOURCE_CHANGE_R49_2.diff').open('x',encoding='utf-8') as f:f.write(diff)
for args,label in [(['status','--short'],'GIT_STATUS_R49_2.txt'),(['diff','--check'],'GIT_DIFF_CHECK_R49_2.txt')]:
 p=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','-C',str(root),*args],capture_output=True,text=True,encoding='utf-8')
 with (r.OUT/label).open('x',encoding='utf-8') as f:f.write(f'exit_code={p.returncode}\n'+p.stdout+p.stderr)
 assert p.returncode==0,p.stderr
print(json.dumps({k:v for k,v in evidence.items() if k!='source_release_file_checks'}))
