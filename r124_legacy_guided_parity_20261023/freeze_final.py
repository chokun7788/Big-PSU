import hashlib,json,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/(sys.argv[1] if len(sys.argv)>1 else 'revision03_system');revision04=S.name=='revision04_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze={str(p.resolve()):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
target=R/('FINAL_SOURCE_REVISION04.json' if revision04 else 'FINAL_SOURCE_FREEZE.json');assert not target.exists();target.write_text(json.dumps(freeze,indent=2),'utf8')
protected={}
for name in ['PARENT_FREEZE.json','TEACHER_FREEZE.json','REVISION02_FREEZE.json']+(['REVISION04_PARENT_FREEZE.json'] if revision04 else []):
 original=json.loads((R/name).read_text('utf8'));changed=[p for p,h in original.items() if not Path(p).is_file() or sha(Path(p))!=h]
 protected[name]={'files':len(original),'changed':changed}
with sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as c:
 stats={name:c.execute('SELECT count(*) FROM '+name).fetchone()[0] for name in ['cc_sources','cc_heads','cc_approvals']}
output={'candidate_files':len(freeze),'candidate_system':str(S),'protected':protected,'database':stats,'all_protected_unchanged':all(not x['changed'] for x in protected.values()),'production_installed':False}
if revision04:output['database_identical_to_revision03']=sha(S/'data/knowledge/common.sqlite')==sha(R/'revision03_system/data/knowledge/common.sqlite')
(R/('FINAL_PACKAGE_REVISION04.json' if revision04 else 'FINAL_PACKAGE_CHECK.json')).write_text(json.dumps(output,ensure_ascii=False,indent=2),'utf8');print(json.dumps(output,ensure_ascii=False,indent=2));assert output['all_protected_unchanged']
