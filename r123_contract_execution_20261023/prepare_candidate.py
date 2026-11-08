"""Create isolated P0/P1 implementation; preserve all preceding experiments."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;OLD=ROOT/'r122_context_scope_calendar_20261022';S=R/'system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert not S.exists()
frozen=json.loads((OLD/'comparison01/RUN_FREEZE.json').read_text('utf8'))
assert all(sha(Path(p))==h for p,h in frozen.items())
parent={str(p.resolve()):sha(p) for p in (OLD/'revision04_system').rglob('*') if p.is_file() and '__pycache__' not in p.parts}
shutil.copytree(OLD/'revision04_system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'))
assert sha(S/'data/knowledge/common.sqlite')==sha(OLD/'revision04_system/data/knowledge/common.sqlite')
(R/'PARENT_FREEZE.json').write_text(json.dumps({**frozen,**parent},indent=2),'utf8')
(R/'LINEAGE.json').write_text(json.dumps({'parent':'R122 revision04','design':'r123_plan_distillation_architecture_20261023','candidate':str(S),'database_sha256':sha(S/'data/knowledge/common.sqlite'),'new_training':False,'production_installed':False,'implementation_scope':'P0/P1 contracts, graph, source/option verification and typed-first scheduler; bounded legacy reader adapters, not all R123 capabilities'},indent=2),'utf8')
print('R123 isolated candidate created; database unchanged')
