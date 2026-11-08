"""Create a reviewable patch; --apply checks original dirty files before writing."""
import json,hashlib,shutil,sqlite3,sys,difflib
from pathlib import Path
OUT=Path(__file__).resolve().parent;CAND=OUT/'system/PSU_Esports_Chatbot_Local'
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');STAGE=OUT/'source_patch';STAGE.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((OUT/'source_hashes_before.json').read_text(encoding='utf-8'))
existing=['app/pipeline/engine.py','app/web_api/pipeline_supervisor.py','tools/build_owner_local_package.ps1','app/web_api/server.py']
if '--apply' not in sys.argv:
    for rel in existing:
        p=ROOT/rel
        if sha(p)!=before[rel]:raise SystemExit('Source changed since initial inspection: '+rel)
        backup=OUT/'before'/rel;backup.parent.mkdir(parents=True,exist_ok=True)
        if not backup.exists():shutil.copy2(p,backup)
    for rel in [*existing[:2],existing[3]]:
        dest=STAGE/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(CAND/rel,dest)
    ui=CAND/'app/knowledge/common/ui/owner.js';s=ui.read_text(encoding='utf-8')
    s=s.replace('new Option(r.record_id,r.record_id)',"new Option((r.label||r.record_id)+' ['+r.record_id+']',r.record_id)")
    s=s.replace("r.record_id.toLowerCase().includes(q)","(r.record_id+' '+(r.label||'')).toLowerCase().includes(q)")
    s=s.replace("node('button',r.record_id+' • '","node('button',(r.label||r.record_id)+' ['+r.record_id+'] • '")
    ui.write_text(s,encoding='utf-8')
    shutil.copytree(CAND/'app/knowledge/common',STAGE/'app/knowledge/common',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    (STAGE/'tests').mkdir(exist_ok=True);shutil.copy2(CAND/'tests/test_common_content_r58.py',STAGE/'tests/test_common_content_r58.py')
    (STAGE/'deployment_templates').mkdir(exist_ok=True)
    for name in ('Open-Owner-Content.ps1','Open-Owner-Content.cmd','Stop-Owner-Content.ps1','Stop-Owner-Content.cmd','OWNER_CONTENT_GUIDE_TH.md'):shutil.copy2(CAND/name,STAGE/'deployment_templates'/name)
    shutil.copytree(OUT/'docs',STAGE/'docs/common_content_r58',dirs_exist_ok=True)
    for name in ('migration_queue.json','migration_drafts.bundle.json'):shutil.copy2(OUT/name,STAGE/'docs/common_content_r58'/name)
    builder=(ROOT/existing[2]).read_text(encoding='utf-8-sig')
    builder=builder.replace('[switch]$CreateZip','[string]$PythonRuntimeRoot = "",\n    [switch]$CreateZip',1)
    builder=builder.replace('2026.09.29-multi-error-recovery-r15",\n    [string]$PythonRuntimeRoot','2026.10.10-common-r58.2",\n    [string]$PythonRuntimeRoot',1)
    anchor='# Runtime data only.'
    addition="""# Common-content packages include a pinned CPython 3.12 x64 runtime.
if (-not $PythonRuntimeRoot) { $PythonRuntimeRoot = Join-Path $projectRoot "runtime\\python" }
$runtimePython = Join-Path $PythonRuntimeRoot "python.exe"
if (-not (Test-Path -LiteralPath $runtimePython -PathType Leaf)) { throw "Pass -PythonRuntimeRoot with a verified Python 3.12 x64 runtime directory." }
$identity = & $runtimePython -B -c "import sys,struct; print(str(sys.version_info.major)+'.'+str(sys.version_info.minor)+':'+str(struct.calcsize('P')*8))"
if ($LASTEXITCODE -ne 0 -or $identity -ne '3.12:64') { throw 'Common-content runtime must be Python 3.12 x64.' }
$runtimeTarget = Join-Path $packageRoot "runtime\\python"
New-Item -ItemType Directory -Force -Path $runtimeTarget | Out-Null
& robocopy $PythonRuntimeRoot $runtimeTarget /E /XD __pycache__ /XF *.pyc | Out-Null
if ($LASTEXITCODE -gt 7) { throw 'Bundled Python copy failed.' }
$knowledgePath = Join-Path $projectRoot "data\\knowledge\\approved.sqlite"
if (Test-Path -LiteralPath $knowledgePath) {
    $knowledgeTarget = Join-Path $packageRoot "data\\knowledge\\approved.sqlite"
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $knowledgeTarget) | Out-Null
    # backup() includes committed WAL data; capability/session files are excluded.
    $backupCode = "import sqlite3,sys; a=sqlite3.connect(sys.argv[1]); demo=a.execute('SELECT value FROM cc_meta WHERE key=?',('demo',)).fetchone(); assert demo and demo[0]=='0','Only production knowledge databases may be packaged'; b=sqlite3.connect(sys.argv[2]); a.backup(b); b.close(); a.close()"
    & $runtimePython -B -c $backupCode $knowledgePath $knowledgeTarget
    if ($LASTEXITCODE -ne 0) { throw 'Knowledge database backup failed.' }
}
$ownerDocsSource = Join-Path $projectRoot "docs\\common_content_r58"
$ownerDocsTarget = Join-Path $packageRoot "owner_content_docs"
New-Item -ItemType Directory -Force -Path $ownerDocsTarget | Out-Null
& robocopy $ownerDocsSource $ownerDocsTarget /E | Out-Null
if ($LASTEXITCODE -gt 7) { throw 'Owner docs copy failed.' }

"""
    assert builder.count(anchor)==1;builder=builder.replace(anchor,addition+anchor,1)
    start=builder.index('$launcherPath = Join-Path')
    end=builder.index('New-Item -ItemType Directory -Force -Path (Join-Path $packageRoot "tools")',start)
    builder=builder[:start]+'# Start launcher reads runtime_version from package_manifest.json.\n\n'+builder[end:]
    builder=builder.replace('    "README_TH.md",','    "Runtime-Readiness.ps1",\n    "OWNER_CONTENT_GUIDE_TH.md",\n    "Open-Owner-Content.ps1",\n    "Open-Owner-Content.cmd",\n    "Stop-Owner-Content.ps1",\n    "Stop-Owner-Content.cmd",\n    "README_TH.md",',1)
    builder=builder.replace('    package_name = $packageName','    python_runtime = @{path="runtime/python/python.exe";scope="bundled-windows-x64";required="3.12"}\n    common_content = @{version="studio-content-3.0";kinds=24;fields=155;database="data/knowledge/approved.sqlite"}\n    package_name = $packageName',1)
    (STAGE/existing[2]).parent.mkdir(parents=True,exist_ok=True);(STAGE/existing[2]).write_text(builder,encoding='utf-8-sig')
    diff=[]
    for rel in existing:diff+=list(difflib.unified_diff((OUT/'before'/rel).read_text(encoding='utf-8-sig').splitlines(True),(STAGE/rel).read_text(encoding='utf-8-sig').splitlines(True),fromfile='before/'+rel,tofile='after/'+rel))
    (OUT/'source_changes.diff').write_text(''.join(diff),encoding='utf-8')
    plan={'existing_files':{rel:{'before':before[rel],'after':sha(STAGE/rel)} for rel in existing},'new_files':{p.relative_to(STAGE).as_posix():sha(p) for p in STAGE.rglob('*') if p.is_file() and p.relative_to(STAGE).as_posix() not in existing}}
    (OUT/'source_apply_plan.json').write_text(json.dumps(plan,indent=2),encoding='utf-8');print('Patch staged, '+str(len(plan['new_files']))+' new files; no ROOT writes.');raise SystemExit
plan=json.loads((OUT/'source_apply_plan.json').read_text())
for rel,h in plan['existing_files'].items():
    if sha(ROOT/rel)!=h['before']:raise SystemExit('Refusing to overwrite changed source '+rel)
for rel,h in plan['new_files'].items():
    if (ROOT/rel).exists():raise SystemExit('New path already exists; refusing overwrite '+rel)
for rel in {**plan['existing_files'],**plan['new_files']}:
    dst=ROOT/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(STAGE/rel,dst)
sys.path.insert(0,str(ROOT))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.importer import import_bundle
db=ROOT/'data/knowledge/approved.sqlite'
if db.exists():
    with sqlite3.connect(db) as a,sqlite3.connect(OUT/'before_knowledge.sqlite') as b:a.backup(b)
store=CommonStore(db);store.initialize()
if store.snapshot()['allow_demo']:raise SystemExit('Existing demo DB preserved; not importing production drafts.')
result=import_bundle(store,json.loads((OUT/'migration_drafts.bundle.json').read_text(encoding='utf-8')),actor='migration-tool-draft-only')
(OUT/'root_migration_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
report={'changed_existing':[],'unexpected_changes':[],'missing':[],'new_files':len(plan['new_files']),'draft_import':{'saved':len(result['saved']),'errors':result['pending_errors'],'active':store.snapshot()['active']}}
for rel,h in before.items():
    p=ROOT/rel
    if not p.is_file():report['missing'].append(rel)
    elif sha(p)!=h:report['changed_existing' if rel in plan['existing_files'] else 'unexpected_changes'].append(rel)
(OUT/'source_preservation_after.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False))
if report['unexpected_changes'] or report['missing'] or result['pending_errors']:raise SystemExit(1)
