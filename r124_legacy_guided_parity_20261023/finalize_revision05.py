"""Freeze final candidate and verify every protected tree without editing it."""
import hashlib,json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision05_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze={str(p.resolve()):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
target=R/'FINAL_SOURCE_REVISION05.json'
if target.exists():assert json.loads(target.read_text('utf8'))==freeze,'Candidate changed after freeze'
else:target.write_text(json.dumps(freeze,indent=2),'utf8')
protected={}
for name in ['PARENT_FREEZE.json','TEACHER_FREEZE.json','REVISION02_FREEZE.json','REVISION04_PARENT_FREEZE.json','REVISION05_PARENT_FREEZE.json']:
 original=json.loads((R/name).read_text('utf8'))
 protected[name]={'files':len(original),'changed':[p for p,h in original.items() if not Path(p).is_file() or sha(Path(p))!=h]}
with sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as c:
 stats={t:c.execute('SELECT count(*) FROM '+t).fetchone()[0] for t in ['cc_sources','cc_heads','cc_approvals']}
out={'candidate_system':str(S),'candidate_files':len(freeze),'protected':protected,'all_protected_unchanged':all(not x['changed'] for x in protected.values()),'database':stats,'database_identical_to_revision04':sha(S/'data/knowledge/common.sqlite')==sha(R/'revision04_system/data/knowledge/common.sqlite'),'production_installed':False}
(R/'FINAL_PACKAGE_REVISION05.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(out,ensure_ascii=False,indent=2));assert out['all_protected_unchanged'] and out['database_identical_to_revision04']
