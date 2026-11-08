"""Optimistic, backed-up code-only deployment. Never copies data or approvals."""
import sys,json,hashlib,shutil,os,tempfile
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;S=B/'system';ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data').resolve();tag=sys.argv[1]
out=B/('DEPLOY_'+tag+('' if '--apply' in sys.argv else '_preview'))
if out.exists():raise FileExistsError(out)
out.mkdir()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
status=json.loads((B/('FINAL_'+tag)/'STATUS.json').read_text(encoding='utf-8'));assert status.get('complete') and status.get('code_unchanged') and status.get('database_unchanged'),status
verified=json.loads((B/('VERIFIED_'+tag+'.json')).read_text(encoding='utf-8'))
assert verified.get('complete') and verified.get('common_only') and not verified.get('legacy_arm_run')
assert verified['database_sha256']==status['database_sha256']
tested=json.loads((B/('FINAL_'+tag)/'CODE_MANIFEST.json').read_text(encoding='utf-8'));baseline={r['path']:r['sha256'] for r in json.loads((B/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))}
planned=[];conflicts=[]
for row in tested:
 rel=row['path'];stage=(S/rel).resolve();target=(ROOT/rel).resolve()
 if not stage.is_relative_to(S.resolve()/'app') or not target.is_relative_to(ROOT/'app'):raise ValueError('Out-of-scope code path: '+rel)
 assert sha(stage)==row['sha256'],'Untested source changed: '+rel
 if row['sha256']==baseline.get(rel):continue
 before=sha(target)
 if before!=baseline.get(rel):conflicts.append({'path':rel,'expected_original':baseline.get(rel),'actual':before});continue
 planned.append({'path':rel,'before_sha256':before,'after_sha256':row['sha256'],'action':'replace' if before else 'new'})
protected=[ROOT/'data/knowledge/approved.sqlite',ROOT/'data/knowledge/migration_r63_20261013/approved.sqlite']
planned.sort(key=lambda r:(r['action']!='new',r['path'].endswith('/answer.py'),r['path']))
protected_before={str(p):sha(p) for p in protected}
(out/'PLAN.json').write_text(json.dumps({'files':planned,'conflicts':conflicts,'protected_databases':protected_before},ensure_ascii=False,indent=2),encoding='utf-8')
if conflicts:raise RuntimeError('Production source changed after initial snapshot; no code deployed. See PLAN.json')
if '--apply' not in sys.argv:print(json.dumps({'planned_files':len(planned),'dry_run':True}));raise SystemExit
done=[]
try:
 for row in planned:
  if row['before_sha256']:
   backup=out/'before'/row['path'];backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/row['path'],backup)
   assert sha(backup)==row['before_sha256'],'Concurrent edit before backup: '+row['path']
 for row in planned:
  target=ROOT/row['path'];backup=out/'before'/row['path']
  if sha(target)!=row['before_sha256']:raise RuntimeError('Concurrent production edit: '+row['path'])
  target.parent.mkdir(parents=True,exist_ok=True)
  fd,temp=tempfile.mkstemp(prefix='.r66-',suffix='.tmp',dir=target.parent)
  try:
   with os.fdopen(fd,'wb') as f:f.write((S/row['path']).read_bytes())
   if sha(target)!=row['before_sha256']:raise RuntimeError('Concurrent production edit before replacement: '+row['path'])
   os.replace(temp,target)
  finally:
   if Path(temp).is_file():Path(temp).unlink()
  assert sha(target)==row['after_sha256'];done.append({**row,'target':str(target),'backup':str(backup) if row['before_sha256'] else None})
except Exception:
 restored=[];left=[]
 for row in reversed(done):
  target=Path(row['target'])
  if sha(target)!=row['after_sha256']:left.append(row['path']);continue
  if row['backup']:shutil.copy2(row['backup'],target)
  else:target.unlink()
  restored.append(row['path'])
 (out/'PARTIAL_ERROR.json').write_text(json.dumps({'copied_files':done,'automatic_rollback_restored':restored,'later_edits_left_untouched':left},ensure_ascii=False,indent=2),encoding='utf-8');raise
after={str(p):sha(p) for p in protected}
manifest={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'project_root':str(ROOT),'tested_tag':tag,'files':done,'code_files':len(done),'production_data_modified':False,'protected_database_hashes_equal':after==protected_before,'protected_databases':after,'active_common_release_changed':False,'portable_packages_updated':False}
(out/'APPLIED.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'code_files':len(done),'production_data_modified':False,'backup_directory':str(out/'before')}))
