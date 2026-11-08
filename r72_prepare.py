"""Create an isolated implementation copy; existing installations stay intact."""
from pathlib import Path
import hashlib,json,shutil,sqlite3
B=Path(__file__).resolve().parent
src=B/'PSU_Esports_Chat_New_R69';out=B/'r72_flow_implementation_20261016'
out.mkdir(exist_ok=False)
def ignore(folder,names):
    skip={n for n in names if n=='__pycache__' or n.endswith('.pyc')}
    if Path(folder).name=='data':skip.update(set(names)&{'logs','state','knowledge'})
    return skip
shutil.copytree(src/'system',out/'system',ignore=ignore)
db=out/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
with sqlite3.connect((src/'system/data/knowledge/common.sqlite').as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as z:a.backup(z)
shutil.copyfile(src/'seed_R68_preserved.sqlite',out/'seed_R68_preserved.sqlite')
for name in ('test_new_chat.py','test_data_updates.py'):
    shutil.copyfile(src/name,out/name)
manifest=[]
for p in sorted((src/'system').rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc':continue
    rel=p.relative_to(src/'system')
    if rel.parts[:2] in [('data','logs'),('data','state')]:continue
    manifest.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(out/'BASELINE_MANIFEST.json').write_text(json.dumps({'source':str(src),'files':manifest,'runtime':str(src/'runtime/python/python.exe'),'existing_data_unchanged':True},ensure_ascii=False,indent=2),encoding='utf8')
print(out)
