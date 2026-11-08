"""Copy the verified R101 candidate without touching its source or data."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r101_complete_flow_20261019'
m=json.loads((B/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'))
bad=[p for p,h in m.items() if not (B/'system'/p).is_file() or hashlib.sha256((B/'system'/p).read_bytes()).hexdigest()!=h]
if bad:raise SystemExit('R101 differs from frozen source: '+repr(bad))
if (R/'system').exists():raise SystemExit('Refusing to overwrite candidate')
shutil.copytree(B/'system',R/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
for p in B.glob('test_*.py'):shutil.copy2(p,R/p.name)
for name in ['flow_contracts.py','reference_grader.py','run_common.py','probe.py','Start-R101.ps1']:
 shutil.copy2(B/name,R/name)
(R/'BASELINE_MANIFEST.json').write_text(json.dumps(m,indent=2),'utf8')
print('Copied',len(m),'verified files; R101 and production unchanged')
