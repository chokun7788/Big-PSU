"""Verify historical frozen source against retained snapshots, no tests run."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;S=(R/'system').resolve();out=[]
archives={'baseline01':R/'baseline01/FROZEN_SYSTEM','student01':R/'revision01_system','regression01':R/'revision01_system','student02':R/'revision02_system'}
for name,archive in archives.items():
 freeze=json.loads((R/name/'RUN_FREEZE.json').read_text('utf8'))['files'];failed=[];checked=0
 for original,want in freeze.items():
  p=Path(original)
  try:relative=p.relative_to(S)
  except ValueError:continue
  target=archive/relative;checked+=1
  if not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest()!=want:failed.append(str(relative))
 out.append({'run':name,'archive':str(archive),'checked_files':checked,'failed':failed,'passed':not failed})
(R/'HISTORICAL_SNAPSHOT_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(out,ensure_ascii=False));assert all(r['passed'] for r in out)
