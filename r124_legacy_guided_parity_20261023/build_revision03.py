import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R/'system';S=R/'revision03_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert not S.exists()
freeze={str(p.resolve()):sha(p) for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
(R/'REVISION02_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
shutil.copytree(P,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
print(json.dumps({'candidate_revision03':str(S),'revision02_files_frozen':len(freeze)}))
