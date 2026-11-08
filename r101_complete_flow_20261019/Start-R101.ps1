param([ValidateSet('Preview','Published','Owner')][string]$Mode='Preview',[int]$Port=0)
$ErrorActionPreference='Stop'
$candidateRoot=$PSScriptRoot
$workspaceRoot=Split-Path -Parent $candidateRoot
$pythonPath=Join-Path $workspaceRoot 'PSU_Esports_Chat_New_R69\runtime\python\python.exe'
$systemPath=Join-Path $candidateRoot 'system'
if(-not (Test-Path -LiteralPath $pythonPath)){throw 'Bundled Python not found. Keep this candidate inside the project folder.'}
$env:PYTHONPATH=$systemPath
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONUTF8='1'
$env:PSU_KNOWLEDGE_DB=Join-Path $systemPath 'data\knowledge\common.sqlite'
$env:PSU_COMMON_CHAT_PROFILE=if($Mode -eq 'Published'){'common-r101-published'}else{'r69-migration-preview'}
$env:PSU_LOCAL_LLM_ASSIST_ENABLED='1'
$env:PSU_EXPERIMENTAL_ALLOW_LLM='1'
$env:PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='25'
$env:PSU_LLM_MAX_CALLS='1'
$env:PSU_PIPELINE_WARMUP='0'
$env:PSU_LLM_PREFLIGHT='0'
$env:PSU_CHAT_LOG_DIR=Join-Path $candidateRoot 'local_run\logs'
$env:PSU_CHAT_LOG_SQLITE_PATH=Join-Path $candidateRoot 'local_run\logs\transcripts.sqlite'
$env:PSU_CONVERSATION_STATE_PATH=Join-Path $candidateRoot 'local_run\state.sqlite'
Remove-Item Env:PSU_ESPORTS_NOW -ErrorAction SilentlyContinue
Push-Location -LiteralPath $systemPath
try {
 if($Mode -eq 'Owner'){
  if($Port -eq 0){$Port=8122}
  & $pythonPath -B -X utf8 -m app.knowledge.common.owner_server --port $Port --db $env:PSU_KNOWLEDGE_DB
 }else{
  if($Port -eq 0){$Port=8121}
  Write-Host "R101 $Mode at http://127.0.0.1:$Port/ - Ollama must already be running."
  & $pythonPath -B -X utf8 -m app.web_api.server --host 127.0.0.1 --port $Port
 }
} finally {Pop-Location}
