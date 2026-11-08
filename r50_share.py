import os,json,shutil,hashlib,subprocess
from pathlib import Path
import r50_probe as r
old=Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_20261003')
destination=Path(r'C:\Users\Chokhun\Documents\Codex')/('PSU_Esports_Share_R50_20261009_'+r.OUT.name.rsplit('_',1)[-1]);assert not destination.exists();destination.mkdir()
release=Path((r.OUT/'release_r50_2_path.txt').read_text());records=[];linked=[]
def sha(path):
    digest=hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda:stream.read(8*1024*1024),b''):digest.update(chunk)
    return digest.hexdigest()
def copy_file(source,target):
    source=Path(source);target=Path(target)
    if source.stat().st_size>1_000_000 and source.suffix.lower() in {'.dll','.exe','.pyd','.bin','.gguf',''}:
        os.link(source,target);linked.append(str(target.relative_to(destination)))
    else:shutil.copy2(source,target)
    return str(target)
for name in ['01_Download_Models','02_With_Models']:
    source=old/name;target=destination/name
    shutil.copytree(source,target,copy_function=copy_file,ignore=shutil.ignore_patterns('state','logs','__pycache__','*.pyc','.git'))
    inner=target/'system/PSU_Esports_Chatbot_Local'
    for directory in ['app','web_chat','data/curated','data/rules','data/competition_rules','data/locales','data/sources']:
        if (release/directory).exists():shutil.copytree(release/directory,inner/directory,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc','logs','state'))
    shutil.copy2(release/'package_manifest.json',inner/'package_manifest.json')
    manifest=json.loads((target/'ready_manifest.json').read_text(encoding='utf-8-sig'));manifest.update(runtime_version='2026.10.09-flow-r50.2',parent_runtime_version=manifest['runtime_version'])
    (target/'ready_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Verify from the recipient's bundled Python with no caller site packages.
    python=target/'runtime/python/python.exe'
    process=subprocess.run([str(python),'-I','-B','-c','import sys,sqlite3,ssl; print(sys.version); print(sqlite3.sqlite_version)'],capture_output=True,text=True)
    assert process.returncode==0,process.stderr
    checks={p.relative_to(release).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()==hashlib.sha256((inner/p.relative_to(release)).read_bytes()).hexdigest() for directory in ['app','web_chat','data/curated','data/rules','data/competition_rules','data/locales','data/sources'] for p in (release/directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    models=target/'runtime/ollama-models'
    # Use manifest-declared immutable blob hashes rather than sizes alone.
    blob_checks=[]
    for item in manifest['model_blobs']:
        matching=list(target.glob('runtime/**/sha256-'+item['sha256']))
        if name=='01_Download_Models':assert not matching,'Download variant unexpectedly contains full weights'
        else:
            assert len(matching)==1,(item,matching)
            actual=sha(matching[0]);assert actual==item['sha256']
            blob_checks.append(dict(label=item['label'],sha256=actual,bytes=matching[0].stat().st_size))
    private=[p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file() and (p.suffix in {'.sqlite3','.sqlite3-wal','.sqlite3-shm'} or 'logs' in p.parts or 'state' in p.parts)]
    assert not private,private
    with (target/'R50_BUILD_CHECKS.json').open('x',encoding='utf-8') as stream:json.dump(dict(version=manifest['runtime_version'],file_checks=checks,bundled_python=process.stdout,model_blob_checks=blob_checks,no_runtime_private_state=True),stream,ensure_ascii=False,indent=2)
    records.append(dict(folder=str(target),variant=manifest['variant'],source_equal_files=len(checks),python_ok=True,model_blob_checks=blob_checks,logical_bytes=sum(p.stat().st_size for p in target.rglob('*') if p.is_file()),runtime_private_state_included=False))
with (r.OUT/'R50_SHARE_BUILD.json').open('x',encoding='utf-8') as stream:json.dump(dict(folders=records,immutable_binary_hardlinks=linked,original_deliveries_untouched=True),stream,ensure_ascii=False,indent=2)
(r.OUT/'share_path.txt').write_text(str(destination));print(json.dumps(records,ensure_ascii=False),flush=True)
