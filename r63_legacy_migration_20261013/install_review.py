"""Install an additional review folder; never replace production DB or logs."""
import hashlib,json,shutil,sqlite3,sys
from pathlib import Path
OUT=Path(__file__).resolve().parent;source=OUT/'round7'
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
target=ROOT/'data/knowledge/migration_r63_20261013'
if target.exists():raise SystemExit('Existing review delivery preserved; will not overwrite')
if not (source/'VERIFICATION.json').exists():raise SystemExit('Verification required before install')
report=json.loads((source/'VERIFICATION.json').read_text(encoding='utf-8'))
if report['failures']:raise SystemExit('Migration preservation checks failed')
target.mkdir()
for p in source.iterdir():
 if p.is_dir() and p.name=='review':continue
 if p.is_dir():shutil.copytree(p,target/p.name)
 elif p.is_file():shutil.copy2(p,target/p.name)
with sqlite3.connect((source/'review/approved.sqlite').as_uri()+'?mode=ro',uri=True) as c,sqlite3.connect(target/'approved.sqlite') as d:c.backup(d)
runtime=OUT.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/runtime/python/python.exe'
launcher=r'''param([int]$Port=18103,[switch]$NoBrowser)
$ErrorActionPreference='Stop'
$projectRoot=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..'))
$python=Join-Path $projectRoot 'runtime\python\python.exe'
if(-not (Test-Path -LiteralPath $python)){$python='__RUNTIME__'}
if(-not (Test-Path -LiteralPath $python)){throw 'Python 3.12 runtime missing. Put this migration review folder inside a complete chatbot package.'}
$db=Join-Path $PSScriptRoot 'approved.sqlite'
Set-Location -LiteralPath $projectRoot
$env:PSU_KNOWLEDGE_DB=$db
$env:PSU_LOCAL_LLM_ASSIST_ENABLED='1'
$listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$Port)
try{$listener.Start()}finally{$listener.Stop()}
$args=@('-B','-m','app.knowledge.common.owner_server','--port',"$Port",'--db',$db)
if($NoBrowser){$args+='--no-browser'}
Write-Host 'Migrated draft review: separate database. Normal chat is unchanged.'
& $python @args
'''.replace('__RUNTIME__',str(runtime).replace("'","''"))
(target/'Open-Migrated-Drafts.ps1').write_text(launcher,encoding='utf-8-sig')
(target/'Open-Migrated-Drafts.cmd').write_text('@echo off\r\npowershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Open-Migrated-Drafts.ps1" %*\r\npause\r\n',encoding='ascii')
for name in ['RESULTS_TH.md','FLOW_MIGRATION_TH.md','WORKBOOK_REVIEWED.json']:
 if (OUT/name).exists():shutil.copy2(OUT/name,target/name)
receipt={'target':str(target),'mode':'additional draft database','normal_chat_db_replaced':False,'published':False,'copied_files':len(list(target.rglob('*'))),'sha256_db':hashlib.sha256((target/'approved.sqlite').read_bytes()).hexdigest()}
(OUT/'INSTALL_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(receipt,ensure_ascii=False))
