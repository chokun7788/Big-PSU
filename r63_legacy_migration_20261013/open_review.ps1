param([int]$Port=18103,[switch]$NoBrowser)
$ErrorActionPreference='Stop'
$runtimeRoot=Join-Path (Split-Path $PSScriptRoot -Parent) 'r58_common_content_20261010\system\PSU_Esports_Chatbot_Local'
$dbPath=Join-Path $PSScriptRoot 'round7\review\approved.sqlite'
$pythonPath=Join-Path $runtimeRoot 'runtime\python\python.exe'
if(-not (Test-Path -LiteralPath $dbPath)){throw 'Migrated draft database missing.'}
if(-not (Test-Path -LiteralPath $pythonPath)){throw 'Development review runtime missing; this review folder is not the standalone production package.'}
Set-Location -LiteralPath $runtimeRoot
# This draft editor does not start a model service or change the normal chat database.
# Set PSU_LOCAL_LLM_ASSIST_ENABLED=1 with a ready local model if semantic preview is desired.
$env:PSU_LOCAL_LLM_ASSIST_ENABLED='1'
$env:PSU_KNOWLEDGE_DB=$dbPath
$listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$Port)
try{$listener.Start()}finally{$listener.Stop()}
$arguments=@('-B','-m','app.knowledge.common.owner_server','--port',"$Port",'--db',$dbPath)
if($NoBrowser){$arguments+='--no-browser'}
Write-Host 'Opening migrated DRAFTS in a separate review database. Normal chat stays on its original data.'
& $pythonPath @arguments
