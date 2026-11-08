"""Create an additive candidate copy and freeze references before changes."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;S=B/'r106_complete_flow_20261020/system'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out=R/'system'
if out.exists():raise SystemExit('Candidate already exists; refusing overwrite')
shutil.copytree(S,out,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
refs={}
for folder in [S/'app',S/'data/knowledge',B/'r113_multi_flow_benchmark_20261021']:
 for p in folder.rglob('*'):
  if p.is_file() and p.suffix in {'.py','.json','.jsonl','.sqlite'} and '__pycache__' not in p.parts:
   refs[str(p.relative_to(B))]=sha(p)
(R/'BASELINE_HASHES.json').write_text(json.dumps(refs,indent=2),'utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'implementation','step':1,'steps_total':5,'candidate_system':str(out),'source_r106_unchanged':True,'production_installed':False},indent=2),'utf8')
print(json.dumps({'candidate':str(out),'reference_hashes':len(refs)}))
