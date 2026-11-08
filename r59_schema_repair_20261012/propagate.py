"""Copy only reviewed logic after checking exact preexisting hashes."""
from prepare import B,SYSTEM,PACK,ROOT,sha,dbhash
import json,shutil,difflib,subprocess
receipt=json.loads((B/'BEFORE_RECEIPT.json').read_text(encoding='utf-8'))
FILES=['app/knowledge/common/answer.py','app/knowledge/common/planner.py','app/knowledge/common/query_contract.py','tests/test_common_query_contract_r59.py']
changes=[]
for label,root in [('project',ROOT),('package',PACK)]:
    for name in FILES:
        dest=root/name
        old=receipt['source_hashes'][label].get(name)
        if old:
            if sha(dest)!=old:raise RuntimeError('Preexisting file changed since backup: '+str(dest))
        elif dest.exists():raise RuntimeError('New destination already exists: '+str(dest))
for label,root in [('project',ROOT),('package',PACK)]:
    for name in FILES:
        dest=root/name;src=SYSTEM/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
        changes.append({'target':str(dest),'sha256':sha(dest),'preserved_before':receipt['source_hashes'][label].get(name),'source':str(src)})
patch=[]
for name in FILES:
    before=B/'before/project'/name
    old=before.read_text(encoding='utf-8').splitlines(keepends=True) if before.exists() else []
    patch.extend(difflib.unified_diff(old,(SYSTEM/name).read_text(encoding='utf-8').splitlines(keepends=True),fromfile='before/'+name,tofile='after/'+name))
(B/'SOURCE_DIFF.patch').write_text(''.join(patch),encoding='utf-8')
checks={p:dbhash(__import__('pathlib').Path(p))==h for p,h in receipt['database_logical_hashes'].items()}
assert all(checks.values()),checks
for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
    for name in ['app/knowledge/common/catalog.json','app/knowledge/common/owner_server.py','app/pipeline/engine.py']:
        assert sha(root/name)==receipt['source_hashes'][label][name],(label,name)
subprocess.run(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],stdout=(B/'GIT_STATUS_AFTER.txt').open('x',encoding='utf-8'),check=True)
result={'copied':changes,'databases_unchanged':checks,'catalog_owner_server_engine_unchanged':True,'before_backups':str(B/'before'),'no_git_reset_clean_commit_or_publish':True}
(B/'PROPAGATION_RECEIPT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
