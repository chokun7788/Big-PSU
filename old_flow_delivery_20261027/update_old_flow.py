"""Offline, hash-checked old Flow update. No models, inference or process stops."""
import argparse,datetime,hashlib,json,os,shutil,subprocess,sys,uuid
from pathlib import Path,PurePosixPath

MANIFEST_SHA256='MANIFEST_SHA256_PLACEHOLDER'
HERE=Path(__file__).resolve().parent
APP='system/PSU_Esports_Chatbot_Local/'

def sha(path):
    with Path(path).open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()

def safe(root,relative):
    part=PurePosixPath(relative)
    if part.is_absolute() or any(p in {'','..','.'} or ':' in p for p in part.parts):raise ValueError('Unsafe update path')
    path=(root/Path(*part.parts)).resolve()
    if path==root or not path.is_relative_to(root):raise ValueError('Update path leaves selected folder')
    return path

def managed(relative):
    parts=PurePosixPath(relative).parts
    if relative.startswith('runtime/model_seed/'):return True
    if parts[0]=='runtime':return False
    if relative.startswith(APP):
        rest=parts[2:]
        if not rest:return False
        if rest[0]=='data':return len(rest)>2 and rest[1] in {'calendar','competition_rules','content','control_game','control_game_split','curated','intent','knowledge_inbox','locales','manifests','routing','rules','sources','style','vector'}
        return rest[0] in {'app','web_chat','booking_dashboard','tools'} or len(rest)==1
    return len(parts)==1 or parts[0] in {'tools','reports'}

def running(root):
    if os.name!='nt':return []
    command="[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false); Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'python|ollama|powershell|pwsh' } | Select-Object ProcessId,CommandLine | ConvertTo-Json -Depth 3 -Compress"
    p=subprocess.run(['powershell','-NoProfile','-Command',command],capture_output=True,text=True,encoding='utf-8',errors='replace',creationflags=0x08000000,timeout=30)
    if p.returncode:raise RuntimeError('Cannot check running program. Close this package before updating.')
    rows=json.loads(p.stdout) if p.stdout.strip() else []
    if isinstance(rows,dict):rows=[rows]
    markers=[str(root/p).casefold() for p in [APP,'runtime/models','runtime/python/python.exe','runtime/ollama/ollama.exe']];own=os.getpid();parent=os.getppid()
    return [{'pid':r['ProcessId']} for r in rows if r['ProcessId'] not in {own,parent} and r.get('CommandLine') and any(marker in r['CommandLine'].casefold() for marker in markers)]

def load_manifest():
    path=HERE/'UPDATE_MANIFEST.json'
    if sha(path)!=MANIFEST_SHA256:raise RuntimeError('Update manifest checksum failed. Extract the ZIP again.')
    return json.loads(path.read_text('utf-8'))

def preflight(root,manifest):
    if not (root/APP).is_dir() or not (root/'runtime/python/python.exe').is_file():raise RuntimeError('Select the old chatbot folder containing Start-Chatbot.cmd, runtime and system.')
    ready=root/'ready_manifest.json'
    original=json.loads(ready.read_text('utf-8-sig'))
    if original.get('runtime_version') not in manifest['supported_versions']:raise RuntimeError('This is not a supported old Flow version. No files were changed.')
    if original.get('models')!=manifest['models']:raise RuntimeError('This package uses different models. No files were changed.')
    variant='download_models' if original.get('variant')=='download_models' else 'with_models'
    conflicts=[];plan=[];checked=0
    entries={**manifest['files'],'ready_manifest.json':manifest['ready_manifests'][variant]}
    for relative,item in entries.items():
        if not managed(relative):raise ValueError('Protected path in update: '+relative)
        path=safe(root,relative);exists=path.exists()
        if exists and not path.is_file():conflicts.append(relative);continue
        actual=sha(path) if exists else None;checked+=1
        if actual==item['sha256']:continue
        if actual not in item['allowed_before']:conflicts.append(relative);continue
        if not item.get('payload'):conflicts.append(relative);continue
        source=safe(HERE,item['payload'])
        if sha(source)!=item['sha256']:raise RuntimeError('Update payload checksum failed: '+relative)
        plan.append({'path':relative,'before_sha256':actual,'after_sha256':item['sha256'],'payload':item['payload'],'action':'replace'})
    for relative,allowed in manifest['obsolete'].items():
        if not managed(relative):raise ValueError('Protected removal path')
        path=safe(root,relative)
        if not path.exists():continue
        if not path.is_file() or sha(path) not in allowed:conflicts.append(relative);continue
        plan.append({'path':relative,'before_sha256':sha(path),'after_sha256':None,'action':'remove'})
    if conflicts:
        return {'ok':False,'phase':'preflight_conflicts','files_unchanged':True,'conflicts':conflicts,'message':'Found local changes or missing files. They were preserved. Send this list to the package maintainer.'}
    active=running(root)
    if active:return {'ok':False,'phase':'program_running','files_unchanged':True,'processes':active,'message':'Open Stop-Chatbot.cmd in this old package, wait for it to stop, then run the updater again.'}
    return {'ok':True,'phase':'preflight','source_version':original['runtime_version'],'target_version':manifest['target_version'],'variant':variant,'checked_files':checked,'changes':plan,'files_unchanged':True}

def rollback(root,backup,receipt):
    for change in receipt['changes']:
        current=safe(root,change['path']);actual=sha(current) if current.exists() else None
        if actual!=change['after_sha256']:raise RuntimeError('Local change prevents rollback; backup preserved: '+change['path'])
        if change['before_sha256'] is not None and sha(safe(backup/'files',change['path']))!=change['before_sha256']:raise RuntimeError('Backup checksum failed')
    for change in reversed(receipt['changes']):
        dest=safe(root,change['path']);saved=safe(backup/'files',change['path'])
        if change['before_sha256'] is None:
            if dest.exists():
                if sha(dest)!=change['after_sha256']:raise RuntimeError('Local change prevents rollback: '+change['path'])
                dest.unlink()
        else:
            if sha(saved)!=change['before_sha256']:raise RuntimeError('Backup checksum failed')
            dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(saved,dest)

def update(root,check_only=False):
    manifest=load_manifest();result=preflight(root,manifest)
    if not result['ok'] or check_only:return result
    if not result['changes']:return {**result,'phase':'already_current','files_unchanged':True}
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8]
    backup=safe(root,'_OldFlow_Update_Backups/'+stamp);backup.mkdir(parents=True)
    # Back up every affected original before the first installation write.
    for change in result['changes']:
        source=safe(root,change['path'])
        if change['before_sha256'] is not None:
            dest=safe(backup/'files',change['path']);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest)
            if sha(dest)!=change['before_sha256']:raise RuntimeError('Backup verification failed; no update applied.')
    receipt={**result,'backup':str(backup),'manifest_sha256':MANIFEST_SHA256,'target_root':str(root),'phase':'backed_up','runtime_models_logs_and_user_state_overwritten':False}
    (backup/'RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),'utf-8')
    applied=[];temporaries=[]
    try:
        for change in sorted(result['changes'],key=lambda c:c['path']=='ready_manifest.json'):
            dest=safe(root,change['path'])
            if (sha(dest) if dest.exists() else None)!=change['before_sha256']:raise RuntimeError('A file changed after preflight: '+change['path'])
            if change['action']=='remove':dest.unlink()
            else:
                source=safe(HERE,change['payload']);dest.parent.mkdir(parents=True,exist_ok=True)
                temporary=dest.with_name(dest.name+'.'+stamp+'.update-tmp')
                if temporary.exists():raise RuntimeError('Unexpected update staging file')
                temporaries.append(temporary);shutil.copy2(source,temporary)
                if sha(temporary)!=change['after_sha256']:raise RuntimeError('Copy verification failed')
                os.replace(temporary,dest)
            applied.append(change)
        after=preflight(root,manifest)
        if not after['ok'] or after.get('changes'):raise RuntimeError('Post-update verification failed')
    except Exception:
        for temporary in temporaries:
            if temporary.exists() and temporary.resolve().is_relative_to(root):temporary.unlink()
        rollback(root,backup,{'changes':applied});receipt['phase']='rolled_back';(backup/'RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),'utf-8');raise
    receipt.update(phase='complete',files_unchanged=False,changed_files=len(applied),program_started=False,model_downloads=0)
    (backup/'RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),'utf-8')
    return {k:v for k,v in receipt.items() if k!='changes'}

def restore(root,backup):
    backup=backup.resolve();allowed=(root/'_OldFlow_Update_Backups').resolve()
    if not backup.is_relative_to(allowed):raise RuntimeError('Select a backup belonging to this old chatbot folder.')
    receipt=json.loads((backup/'RECEIPT.json').read_text('utf-8'))
    if receipt['phase']!='complete' or receipt['target_root']!=str(root):raise RuntimeError('Not a completed backup for this folder.')
    if running(root):raise RuntimeError('Stop this old package with Stop-Chatbot.cmd before restoring.')
    # Validate the complete rollback before the first restore write.
    for change in receipt['changes']:
        current=safe(root,change['path']);actual=sha(current) if current.exists() else None
        if actual!=change['after_sha256']:raise RuntimeError('Local change prevents rollback: '+change['path'])
        if change['before_sha256'] is not None and sha(safe(backup/'files',change['path']))!=change['before_sha256']:raise RuntimeError('Backup checksum failed')
    rollback(root,backup,receipt);receipt['phase']='restored';(backup/'RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),'utf-8')
    return {'ok':True,'phase':'restored','version':receipt['source_version'],'models_and_logs_preserved':True}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--target',required=True);parser.add_argument('--check-only',action='store_true');parser.add_argument('--restore');args=parser.parse_args();root=Path(args.target).resolve()
    result=restore(root,Path(args.restore)) if args.restore else update(root,args.check_only)
    print(json.dumps(result,ensure_ascii=False,indent=2),flush=True);return 0 if result['ok'] else 2

if __name__=='__main__':
    try:sys.exit(main())
    except Exception as exc:print(json.dumps({'ok':False,'error':str(exc)},ensure_ascii=False),file=sys.stderr);sys.exit(1)
