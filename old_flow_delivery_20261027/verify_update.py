"""Real installer on isolated old-file copies; no model or server start."""
import ast,hashlib,importlib.util,json,os,shutil,sqlite3,subprocess,sys,time
from pathlib import Path
from unittest.mock import patch

W=Path(__file__).resolve().parent;ROOT=Path('C:/Users/Chokhun/Documents/Codex');OUT=ROOT/'PSU_Old_Flow_Update_R57_20261027';TEST=ROOT/('_R57Tests_'+str(time.time_ns()));TEST.mkdir()
spec=importlib.util.spec_from_file_location('old_updater',OUT/'update_old_flow.py');u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u);manifest=u.load_manifest();checks={};details=[]
audit=json.loads((W/'BUILD_AUDIT.json').read_text('utf8'));baselines=[Path(p) for p in audit['source_packages']]
paths=set(manifest['files'])|set(manifest['obsolete'])|{'ready_manifest.json','runtime/python/python.exe'}
def fixture(label,base=baselines[0]):
 p=(TEST/label).resolve();assert p.is_relative_to(TEST.resolve());p.mkdir()
 for name in paths:
  src=base/name
  if src.is_file():dest=p/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
 for name,body in [('runtime/models/PRESERVE_MODEL.test',b'model preservation sentinel'),('runtime/state/active.test',b'old runtime state'),('settings/owner-local.txt',b'local notes')]:
  f=p/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(body)
 log=p/'system/PSU_Esports_Chatbot_Local/data/logs/boss-history.sqlite';log.parent.mkdir(parents=True,exist_ok=True)
 with sqlite3.connect(log) as c:c.execute('CREATE TABLE history(note TEXT)');c.execute('INSERT INTO history VALUES (?)',('preserved trial history',))
 return p
def hashes(p):return {n:u.sha(p/n) if (p/n).is_file() else None for n in paths}
def preserved(p):return {str(f.relative_to(p)):u.sha(f) for folder in ['runtime/models','runtime/state','settings','system/PSU_Esports_Chatbot_Local/data/logs'] for f in (p/folder).rglob('*') if f.is_file()}
first=None
for n,base in enumerate(baselines):
 p=fixture('case'+str(n)+' ไทย',base);before=hashes(p);keep=preserved(p)
 result=u.update(p,check_only=True);checks['baseline'+str(n)+'_check_only_no_changes']=result['ok'] and hashes(p)==before
 result=u.update(p);checks['baseline'+str(n)+'_real_update_complete']=result['ok'] and result['phase']=='complete' and json.loads((p/'ready_manifest.json').read_text('utf8'))['runtime_version']=='2026.10.10-service-r57.4'
 checks['baseline'+str(n)+'_models_logs_state_preserved']=preserved(p)==keep
 second=u.update(p);checks['baseline'+str(n)+'_repeat_update_idempotent']=second['phase']=='already_current' and second['files_unchanged']
 checks['baseline'+str(n)+'_all_target_source_and_data_hashes_match']=all(u.sha(p/k)==v['sha256'] for k,v in manifest['files'].items())
 restored=u.restore(p,Path(result['backup']));checks['baseline'+str(n)+'_rollback_restores_exact_original_files']=restored['ok'] and hashes(p)==before and preserved(p)==keep
 details.append({'baseline':str(base),'target':str(p),'check_only':{k:v for k,v in result.items() if k!='changes'},'restored':restored})
 if first is None:first=p
for kind,name in [('owner_data','system/PSU_Esports_Chatbot_Local/data/curated/zone_rental_fees_20261006.json'),('code','system/PSU_Esports_Chatbot_Local/app/pipeline/engine.py')]:
 p=fixture('conflict_'+kind);f=p/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes((f.read_bytes() if f.exists() else b'')+b'\nLOCAL CHANGE\n');before=hashes(p);result=u.update(p);checks[kind+'_local_change_blocks_before_any_write']=not result['ok'] and result['phase']=='preflight_conflicts' and name in result['conflicts'] and hashes(p)==before and not (p/'_OldFlow_Update_Backups').exists()
p=fixture('unknown_version');f=p/'ready_manifest.json';m=json.loads(f.read_text('utf8'));m['runtime_version']='R135-new-flow';f.write_text(json.dumps(m),'utf8');before=hashes(p)
try:u.update(p);checks['new_flow_version_rejected']=False
except RuntimeError:checks['new_flow_version_rejected']=hashes(p)==before
p=fixture('running_program');before=hashes(p)
with patch.object(u,'running',return_value=[{'pid':12345}]):r=u.update(p)
checks['running_program_blocks_without_kill_or_write']=r['phase']=='program_running' and hashes(p)==before
p=fixture('copy_failure_rollback');before=hashes(p);keep=preserved(p);original_replace=u.os.replace;calls=[]
def fail_third(src,dest):
 calls.append(str(dest))
 if len(calls)==3:raise OSError('Controlled copy interruption')
 return original_replace(src,dest)
try:
 with patch.object(u.os,'replace',side_effect=fail_third):u.update(p)
 checks['interrupted_copy_rolls_back']=False
except OSError:checks['interrupted_copy_rolls_back']=hashes(p)==before and preserved(p)==keep and not list(p.rglob('*.update-tmp'))
p=fixture('tampered_bundle');broken=TEST/'broken_bundle';shutil.copytree(OUT,broken);name=next(v['payload'] for v in manifest['files'].values() if v.get('payload') and v['payload'].endswith('.py'));f=broken/name;f.write_bytes(f.read_bytes()+b'\n# corrupted\n');prior_here=u.HERE;u.HERE=broken;before=hashes(p)
try:u.update(p);checks['corrupt_payload_rejected_before_any_write']=False
except RuntimeError:checks['corrupt_payload_rejected_before_any_write']=hashes(p)==before and not (p/'_OldFlow_Update_Backups').exists()
(broken/'UPDATE_MANIFEST.json').write_text('{}','utf8')
try:u.update(p);checks['corrupt_manifest_rejected_before_any_write']=False
except RuntimeError:checks['corrupt_manifest_rejected_before_any_write']=hashes(p)==before
u.HERE=prior_here
p=fixture('restore_conflict');result=u.update(p);f=p/'system/PSU_Esports_Chatbot_Local/app/pipeline/engine.py';f.write_bytes(f.read_bytes()+b'\n# user edit after update\n');before=hashes(p)
try:u.restore(p,Path(result['backup']));checks['rollback_does_not_overwrite_later_local_changes']=False
except RuntimeError:checks['rollback_does_not_overwrite_later_local_changes']=hashes(p)==before
# Run the shipped wrapper with the real original bundled Python in read-only
# check mode. This imports no app/model and changes no original files.
command=['powershell','-NoProfile','-ExecutionPolicy','Bypass','-File',str(OUT/'Update-Old-Flow.ps1'),'-TargetRoot',str(baselines[0]),'-CheckOnly'];original_before={n:u.sha(baselines[0]/n) if (baselines[0]/n).is_file() else None for n in paths};run=subprocess.run(command,capture_output=True,text=True,encoding='utf8',errors='replace',timeout=90)
checks['real_original_bundled_python_and_shipped_wrapper_check_only']=run.returncode==0 and '"ok": true' in run.stdout
checks['original_ready_managed_files_unchanged_after_wrapper']=original_before=={n:u.sha(baselines[0]/n) if (baselines[0]/n).is_file() else None for n in paths}
(TEST/'ORIGINAL_WRAPPER_CHECK.json').write_text(json.dumps({'command':command,'exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr},ensure_ascii=False,indent=2),'utf8')
# Compile the delivered app's Python syntax without importing servers/providers.
ast_files=[]
for path in (baselines[-1]/'system/PSU_Esports_Chatbot_Local/app').rglob('*.py'):
 ast.parse(path.read_text('utf-8-sig'));ast_files.append(str(path))
checks['retained_old_application_ast_valid']=bool(ast_files)
checks['payload_contains_no_weights_or_python_ollama_state_or_logs']=all(not n.startswith(('runtime/models/','runtime/python/','runtime/ollama/','runtime/state/')) and '/data/logs/' not in n and '/data/common/' not in n for n,v in manifest['files'].items() if v.get('payload'))
report={'all_passed':all(checks.values()),'checks':checks,'cases':details,'frozen_r57_source_files':151,'app_python_ast_files':len(ast_files),'actual_models_loaded_or_downloaded':0,'actual_servers_started':0,'process_stop_or_kill':False,'clean_windows_or_boss_computer_tested':False,'original_packages_modified':False}
(TEST/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(TEST),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
