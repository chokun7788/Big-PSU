"""Retain the tested implementation before making a new candidate revision."""
import hashlib,json,shutil,sys,os
from pathlib import Path
R=Path(__file__).resolve().parent;out=R/'verification'/sys.argv[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
complete=(out/'TEST_COMPLETE.json').exists()
assert complete or (out/'ABORTED_FOR_FIX.json').exists()
if complete:
    done=json.loads((out/'TEST_COMPLETE.json').read_text('utf8'));assert done['complete']
freeze=json.loads((out/'RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in freeze['files'].items())
target=out/'frozen_system_app'
def extended(p):return '\\\\?\\'+str(p.resolve()) if os.name=='nt' else str(p)
shutil.copytree(extended(R/'system/app'),extended(target),ignore=shutil.ignore_patterns('__pycache__','*.pyc'),dirs_exist_ok=True)
archive=Path(extended(target));manifest={str(p.relative_to(archive)):sha(p) for p in archive.rglob('*') if p.is_file()}
(out/'FROZEN_CODE_ARCHIVE.json').write_text(json.dumps({'before_further_edits':True,'test_complete':complete,'files':manifest,'benchmark_source_remains_R113_frozen':True},indent=2),'utf8')
print('Archived completed revision '+sys.argv[1])
