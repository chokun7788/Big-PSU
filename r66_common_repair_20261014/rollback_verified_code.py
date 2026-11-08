"""Restore only R66-owned code changes while protecting later user edits."""
import sys,json,hashlib,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1];m=json.loads((B/('DEPLOY_'+tag)/'APPLIED.json').read_text(encoding='utf-8'));root=Path(m['project_root']).resolve();plan=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
for row in m['files']:
 target=Path(row['target']).resolve()
 if not target.is_relative_to(root/'app'):raise ValueError('Out-of-scope rollback path')
 if sha(target)!=row['after_sha256']:raise RuntimeError('Later edit exists, leave untouched: '+str(target))
 if row['backup'] and sha(Path(row['backup']))!=row['before_sha256']:raise RuntimeError('Backup hash mismatch')
 plan.append(row)
if '--apply' not in sys.argv:print(json.dumps({'dry_run':True,'files':len(plan),'data_or_approvals_modified':False}));raise SystemExit
for row in reversed(plan):
 target=Path(row['target'])
 if sha(target)!=row['after_sha256']:raise RuntimeError('Concurrent later edit: '+str(target))
 if row['backup']:shutil.copy2(row['backup'],target)
 else:target.unlink() # One exact, hash-verified R66-created file; no recursive delete.
print(json.dumps({'restored_files':len(plan),'data_or_approvals_modified':False}))
