import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R/'revision03_system';S=R/'revision04_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze=json.loads((R/'FINAL_SOURCE_FREEZE.json').read_text('utf8'))
assert all(sha(Path(p))==h for p,h in freeze.items())
assert not S.exists();shutil.copytree(P,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
(R/'REVISION04_PARENT_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
print('Revision03 preserved; revision04 prepared for confirmed final comparison regressions')
