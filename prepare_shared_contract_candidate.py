"""Create an isolated code/static-data copy and SQLite backups, never move data."""
from pathlib import Path
import hashlib,json,shutil,sqlite3,datetime
P=Path(__file__).resolve().parent
S=P/'r135_bounded_response_20261111'
D=P/'r135_shared_contract_20261111'
if D.exists():raise SystemExit('Candidate exists; refusing to overwrite')
D.mkdir()
def ignore(directory,names):
 out=[]
 for name in names:
  p=Path(directory)/name
  code_tree='app' in p.relative_to(S/'system').parts
  if name in {'__pycache__','.git'} or (not code_tree and name in {'logs','runtime','state'}) or p.is_symlink() or p.is_junction() or name.endswith(('.sqlite','.sqlite-wal','.sqlite-shm','.pyc')):out.append(name)
 return out
shutil.copytree(S/'system',D/'system',ignore=ignore)
for name in ['verification_support.py','verify_bounded_response.py','verify_verified_sources.py','verify_typo_recovery.py','verify_typo_http.py','Start-Typo-Preview.ps1']:
 shutil.copy2(S/name,D/name)
for name in ['common.sqlite','verified_sources.sqlite']:
 src=S/'system/data/knowledge'/name;dst=D/'system/data/knowledge'/name
 with sqlite3.connect(src.resolve().as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(dst) as b:a.backup(b)
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parent':str(S),'candidate':str(D),'app_sha256':{str(p.relative_to(S/'system')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (S/'system/app').rglob('*.py')},'database_backup':{'method':'SQLite backup API; read-only source connection','source_untouched':True},'runtime_changed':False,'scope':'isolated shared-contract experiment; not production or full acceptance'}
(D/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
(D/'STATUS.json').write_text(json.dumps({'phase':'baseline_diagnosis','parent':S.name,'deployed':False,'full_eval_started':False},indent=2),encoding='utf8')
(D/'flow.md').write_text('# Shared-contract candidate\n\nParent: r135_bounded_response_20261111.\n\nAudit raw need boundaries and independent coverage before changing code. Preserve source/receipt verification and successful typed siblings. No full sample before focused gates.\n',encoding='utf8')
print(json.dumps({'candidate':str(D),'app_files':len(manifest['app_sha256'])}))
