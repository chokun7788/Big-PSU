"""R75 isolated development copy; no old data/log replacement."""
from pathlib import Path
import hashlib,json,shutil,sqlite3
B=Path(__file__).resolve().parent;src=B/'r74_semantic_profile_20261016';out=B/'r75_profile_confirmation_20261016'
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
for name in ('run_targeted.py','target_cases.py','scope_cases.py','risk_cases.py','ownership_cases.py','holdout_cases.py','payment_boundary_cases.py','semantic_acceptance_cases.py','Open-New-Chat.cmd','Start-New-Chat.ps1','Stop-New-Chat.cmd','Stop-New-Chat.ps1','Open-Data-Editor.cmd','Open-Data-Editor.ps1'):
    shutil.copyfile(src/name,out/name)
for name in ('Start-New-Chat.ps1','Open-Data-Editor.ps1'):
    p=out/name;p.write_text(p.read_text(encoding='utf8').replace('8107','8109').replace('8108','8110').replace('r74','r75').replace('R74','R75'),encoding='utf8')
manifest=[]
for p in sorted((src/'system').rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc' or p.name.endswith(('.sqlite-shm','.sqlite-wal')):continue
    rel=p.relative_to(src/'system')
    if rel.parts[:2] in [('data','logs'),('data','state')]:continue
    manifest.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(out/'BASELINE_MANIFEST.json').write_text(json.dumps({'source':str(src),'files':manifest},ensure_ascii=False,indent=2),encoding='utf8')
print(out)
