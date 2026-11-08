"""Copy frozen R95 source into an isolated candidate, preserving original inputs."""
from pathlib import Path
import hashlib,json,shutil

OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
BASE=ROOT/'r95_merged_flow_implementation_20261018'
if (OUT/'system').exists():raise SystemExit('Candidate already exists; refusing to overwrite')
manifest=json.loads((BASE/'FULL_SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
bad=[p for p,h in manifest.items() if hashlib.sha256((BASE/'system'/p).read_bytes()).hexdigest()!=h]
if bad:raise SystemExit('Frozen R95 changed: '+repr(bad))
shutil.copytree(BASE/'system',OUT/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.sqlite-wal','*.sqlite-shm'))
for name in ['run_common.py','reference_grader.py','analyze.py','analyze_run.py','check_task_flow.py','flow_contracts.py','test_owner_lifecycle.py','test_existing_fixture.py','test_existing_competition_fixture.py']:
    shutil.copy2(BASE/name,OUT/name)
(OUT/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'copied_files':len(manifest),'base':'frozen R95','candidate':str(OUT),'installed_over_R78':False}))
