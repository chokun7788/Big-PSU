"""Isolated model-first trial; no source or active model modifications."""
import datetime,hashlib,json,shutil,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'r135_recovery_loop_20261112';D=R/'r135_model_first_20261112'
if D.exists():raise SystemExit('Candidate exists; refusing overwrite')
D.mkdir()
def ignore(directory,names):
 excluded=[]
 for name in names:
  p=Path(directory)/name;code='app' in p.relative_to(S/'system').parts
  if p.is_symlink() or p.is_junction() or name in {'__pycache__','.git'} or (not code and name in {'runtime','logs','state'}) or name.endswith(('.sqlite','.sqlite-wal','.sqlite-shm','.pyc')):excluded.append(name)
 return excluded
shutil.copytree(S/'system',D/'system',ignore=ignore)
for name in ['verification_support.py','Start-Shared-Preview.ps1']:shutil.copy2(S/name,D/name)
for name in ['common.sqlite','verified_sources.sqlite']:
 with sqlite3.connect((S/'system/data/knowledge'/name).resolve().as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(D/'system/data/knowledge'/name) as dst:src.backup(dst)
hashes={str(p.relative_to(S/'system')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (S/'system/app').rglob('*.py')}
(D/'BASELINE_MANIFEST.json').write_text(json.dumps({'client_date':'2026-11-12','parent':str(S),'app_sha256':hashes,'source_backup':'read-only SQLite backup API','model_changed':False},ensure_ascii=False,indent=2),encoding='utf8')
(D/'STATUS.json').write_text(json.dumps({'phase':'implementing_model_first_trial','parent':S.name,'deployed':False,'full_eval_running':False},indent=2),encoding='utf8')
(D/'flow.md').write_text('# Model-first trial\n\nRaw whole request → one actual model planning call → validate literal task quotes/targets/schema → source readers and existing verifier per need → retain verified answers and explicit missing/ambiguity → aggregate and log raw plan/execution.\n\nNo legacy native answer may silently bypass the planner. A model failure is reported as a model failure. Rendering initially retains verified source blocks; free model paraphrasing is not accepted without a content verifier. Parent, owner and frozen sources unchanged. No new weights/install/subagents.\n',encoding='utf8')
print(json.dumps({'candidate':str(D),'parent_app_files':len(hashes)}))
