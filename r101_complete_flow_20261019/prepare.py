"""Create an isolated working copy of the frozen R100 source."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parent
B=R.parent/'r100_contract_flow_implementation_20261019'
m=json.loads((B/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'))
assert isinstance(m,dict)
bad=[p for p,h in m.items() if not (B/'system'/p).is_file() or hashlib.sha256((B/'system'/p).read_bytes()).hexdigest()!=h]
if bad:raise SystemExit('Frozen source changed: '+repr(bad))
if (R/'system').exists():raise SystemExit('Candidate already exists')
shutil.copytree(B/'system',R/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.sqlite-wal','*.sqlite-shm'))
for name in ['run_common.py','reference_grader.py','probe.py','flow_contracts.py','test_flow_v2.py','test_owner_lifecycle.py','test_existing_fixture.py','test_existing_competition_fixture.py','test_contract_flow.py']:
 shutil.copy2(B/name,R/name)
(R/'BASELINE_MANIFEST.json').write_text(json.dumps(m,indent=2),'utf8')
print('Copied',len(m),'verified source files; production unchanged')
