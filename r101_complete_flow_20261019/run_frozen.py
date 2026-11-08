"""Run one authorized subset with immutable before/after source receipts."""
import hashlib,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parent;tag=sys.argv[1]
if not tag.replace('_','').isalnum():raise SystemExit('Invalid run tag')
def manifest():return {p.relative_to(R/'system').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
frozen=json.loads((R/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'));before=manifest()
if frozen!=before:raise SystemExit('Candidate differs from frozen source')
with (R/(tag+'_SOURCE_BEFORE.json')).open('x',encoding='utf8') as f:json.dump(before,f,indent=2)
with (R/(tag+'_RUN.log')).open('x',encoding='utf8') as log:
 result=subprocess.run([sys.executable,'-B','-X','utf8',str(R/'run_common.py'),'--workers','2','--tag',tag,'--jobs',str(R.parent/'r98_flow_v2_implementation_20261019/FOCUSED_JOBS.jsonl')],cwd=R.parent,stdout=log,stderr=subprocess.STDOUT)
after=manifest();(R/(tag+'_SOURCE_AFTER.json')).write_text(json.dumps(after,indent=2),'utf8')
report={'exit_code':result.returncode,'source_unchanged':before==after,'frozen_source_matched':before==frozen,'full_test':False}
(R/(tag+'_INTEGRITY.json')).write_text(json.dumps(report,indent=2),'utf8');print(report);sys.exit(result.returncode or (before!=after))
