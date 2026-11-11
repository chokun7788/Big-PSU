"""Create one isolated recovery-loop candidate; refuse existing targets."""
import datetime,hashlib,json,shutil,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'r135_shared_contract_20261111';D=R/'r135_recovery_loop_20261112'
if D.exists():raise SystemExit('Candidate exists; refuse overwrite')
D.mkdir()
def ignore(directory,names):
 result=[]
 for name in names:
  p=Path(directory)/name;code='app' in p.relative_to(S/'system').parts
  if p.is_symlink() or p.is_junction() or name in {'__pycache__','.git'} or (not code and name in {'logs','runtime','state'}) or name.endswith(('.sqlite','.sqlite-wal','.sqlite-shm','.pyc')):result.append(name)
 return result
shutil.copytree(S/'system',D/'system',ignore=ignore)
for p in S.glob('verify_*.py'):shutil.copy2(p,D/p.name)
for name in ['verification_support.py','run_robustness_matrix.py','ROBUSTNESS_MATRIX_MANIFEST.json','Start-Shared-Preview.ps1']:shutil.copy2(S/name,D/name)
for name in ['common.sqlite','verified_sources.sqlite']:
 with sqlite3.connect((S/'system/data/knowledge'/name).resolve().as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(D/'system/data/knowledge'/name) as dst:src.backup(dst)
hashes={str(p.relative_to(S/'system')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (S/'system/app').rglob('*.py')}
(D/'BASELINE_MANIFEST.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parent':str(S),'app_sha256':hashes,'database_backup':'SQLite backup API, read-only source; no parent writes','model_changed':False},ensure_ascii=False,indent=2),encoding='utf8')
(D/'STATUS.json').write_text(json.dumps({'phase':'baseline_diagnosis','parent':S.name,'report':'../r135_log_analysis_20261112/REPORT_TH.md','deployed':False,'full_eval_running':False},indent=2),encoding='utf8')
(D/'flow.md').write_text('# Recovery loop candidate\n\nParent shared-contract round02. Preserve its snapshots and logs. Read RESEARCH_AND_LOOP_PLAN_TH.md; baseline actual failure before changing code; one grouped patch then positive/negative/affected regressions. No owner/live/frozen changes, no installs or model changes.\n',encoding='utf8')
print(json.dumps({'candidate':str(D),'parent_app_files':len(hashes)}))
