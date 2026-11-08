"""Create an isolated revision. Never modify the verified revision03 tree."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent
P=R/'revision03_system';S=R/'revision04_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
prior=json.loads((R/'verification_1792693569208529000/RUN_FREEZE.json').read_text('utf8'))
assert all(sha(Path(p))==h for p,h in prior.items()),'Parent freeze changed'
assert not S.exists(),'Refuse to overwrite an existing revision'
shutil.copytree(P,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'))
(R/'REVISION04_PARENT_FREEZE.json').write_text(json.dumps(prior,indent=2),'utf8')
(R/'REVISION04_BUILD.json').write_text(json.dumps({'parent':str(P),'candidate':str(S),'parent_frozen_unchanged':True,'database_sha256':sha(S/'data/knowledge/common.sqlite'),'scope':'Native calendar/live bridge and request provenance; no new training or production install'},indent=2),'utf8')
print(S)
