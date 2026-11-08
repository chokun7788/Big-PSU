"""Isolated R74 code copy; preserve R73 records and all earlier logs."""
from pathlib import Path
import hashlib,json,shutil,sqlite3
B=Path(__file__).resolve().parent
src=B/'r73_scope_completion_20261016'; out=B/'r74_semantic_profile_20261016'
out.mkdir(exist_ok=False)
def skip(folder,names):
    result={n for n in names if n=='__pycache__' or n.endswith('.pyc')}
    if Path(folder).name=='data':result.update(set(names)&{'logs','state','knowledge'})
    return result
shutil.copytree(src/'system',out/'system',ignore=skip)
db=out/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
a=sqlite3.connect((src/'system/data/knowledge/common.sqlite').as_uri()+'?mode=ro',uri=True);z=sqlite3.connect(db)
try:a.backup(z)
finally:z.close();a.close()
for name in ('test_new_chat.py','target_cases.py','risk_cases.py','run_targeted.py','scope_cases.py','ownership_cases.py','holdout_cases.py','test_new_profiles.py','test_data_updates.py','test_risk_fixtures.py','Open-New-Chat.cmd','Start-New-Chat.ps1','Stop-New-Chat.cmd','Stop-New-Chat.ps1','Open-Data-Editor.cmd','Open-Data-Editor.ps1'):
    shutil.copyfile(src/name,out/name)
manifest=[]
for p in sorted((src/'system').rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc' or p.name.endswith(('.sqlite-shm','.sqlite-wal')):continue
    rel=p.relative_to(src/'system')
    if rel.parts[:2] in [('data','logs'),('data','state')]:continue
    manifest.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(out/'BASELINE_MANIFEST.json').write_text(json.dumps({'source':str(src),'files':manifest},ensure_ascii=False,indent=2),encoding='utf8')
for name in ('Start-New-Chat.ps1','Stop-New-Chat.ps1','Open-Data-Editor.ps1'):
    p=out/name;s=p.read_text(encoding='utf8').replace('8105','8107').replace('8106','8108').replace('r73','r74').replace('R73','R74');p.write_text(s,encoding='utf8')
for p in (out/'system/app/web_api').glob('*'):
    if p.is_file() and p.suffix in {'.py','.html','.js'}:
        s=p.read_text(encoding='utf8')
        if 'R73' in s:p.write_text(s.replace('R73','R74'),encoding='utf8')
print(out)
