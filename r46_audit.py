import json,hashlib,difflib,subprocess
from pathlib import Path
import r46_probe as r
root=r.prior.r.p.ROOT
before=json.loads((r.OUT/'before_manifest.json').read_text())
changed=[key for key,value in before.items() if not (root/key).is_file() or hashlib.sha256((root/key).read_bytes()).hexdigest()!=value]
assert changed==['app/pipeline/zone_rental.py'],changed
release=Path((r.OUT/'release_r46_1_path.txt').read_text())
checks={}
for folder in ('app','web_chat','data/curated'):
    for p in (root/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            rel=p.relative_to(root);checks[rel.as_posix()]=(release/rel).is_file() and p.read_bytes()==(release/rel).read_bytes()
assert all(checks.values()),[k for k,v in checks.items() if not v]
evidence=dict(changed_existing_files=changed,source_release_file_checks=checks,passed_file_checks=sum(checks.values()),total_file_checks=len(checks),data_curated_unchanged=all(k not in changed for k in before if k.startswith('data/curated/')))
with (r.OUT/'SOURCE_AND_RELEASE_AUDIT_R46.json').open('x',encoding='utf-8') as f:json.dump(evidence,f,indent=2)
diff=''.join(difflib.unified_diff((r.OUT/'before/app/pipeline/zone_rental.py').read_text(encoding='utf-8').splitlines(True),(root/'app/pipeline/zone_rental.py').read_text(encoding='utf-8').splitlines(True),fromfile='before/zone_rental.py',tofile='after/zone_rental.py'))
with (r.OUT/'SOURCE_CHANGE_R46.diff').open('x',encoding='utf-8') as f:f.write(diff)
for args,label in [(['status','--short'],'GIT_STATUS_R46.txt'),(['diff','--check'],'GIT_DIFF_CHECK_R46.txt')]:
    p=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','-C',str(root),*args],capture_output=True,text=True,encoding='utf-8')
    with (r.OUT/label).open('x',encoding='utf-8') as f:f.write(f'exit_code={p.returncode}\n'+p.stdout+p.stderr)
    assert p.returncode==0
print(json.dumps({k:v for k,v in evidence.items() if k!='source_release_file_checks'}))
