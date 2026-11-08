"""Copy the verified R98 runtime; never overwrite any existing candidate."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r98_flow_v2_implementation_20261019'
manifest=json.loads((B/'final_on02/SOURCE_AFTER.json').read_text('utf8'))
changed=[p for p,h in manifest.items() if not (B/'system'/p).is_file() or hashlib.sha256((B/'system'/p).read_bytes()).hexdigest()!=h]
if changed:raise SystemExit('R98 differs from frozen final source: '+repr(changed))
if (R/'system').exists():raise SystemExit('Refusing to overwrite existing candidate')
shutil.copytree(B/'system',R/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.sqlite-wal','*.sqlite-shm'))
for name in ['run_common.py','reference_grader.py','probe.py','flow_contracts.py','test_flow_v2.py','test_owner_lifecycle.py','test_existing_fixture.py','test_existing_competition_fixture.py']:
 shutil.copy2(B/name,R/name)
(R/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),'utf8')
print(json.dumps({'source_files':len(manifest),'source':'R98 frozen final','copied_runtime':str(R/'system'),'production_install':False}))
