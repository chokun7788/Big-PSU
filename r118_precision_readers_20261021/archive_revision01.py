import json,hashlib,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;run=R/'http01';S=R/'system'
assert json.loads((run/'TEST_COMPLETE.json').read_text('utf8'))['complete']
shutil.copytree('\\\\?\\'+str(S.resolve()),'\\\\?\\'+str((run/'FROZEN_SYSTEM').resolve()),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
freeze=json.loads((run/'RUN_FREEZE.json').read_text('utf8'))['files'];checked=0
for name,h in freeze.items():
 p=Path(name)
 if p.is_relative_to(S):
  archive=run/'FROZEN_SYSTEM'/p.relative_to(S)
  assert hashlib.sha256(archive.read_bytes()).hexdigest()==h;checked+=1
(run/'ARCHIVED_CODE_VERIFIED.json').write_text(json.dumps({'verified':True,'files':checked,'revision':'R118 revision01','run_freeze_paths_resolve_via':'FROZEN_SYSTEM for system/*'}),'utf8')
script=(R/'run_http.py').read_text('utf8').replace("OUT=R/'http01'","OUT=R/'http02'").replace("'run_http.py','BASELINE_CHECK_V2.json'","'run_http.py','run_http02.py','BASELINE_CHECK_V2.json'")
(R/'run_http02.py').write_text(script,'utf8')
print(checked)
