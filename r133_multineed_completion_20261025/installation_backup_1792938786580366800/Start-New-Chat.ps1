param([int]$Port = 8115, [switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
if ($Port -lt 1024 -or $Port -gt 65535) { throw 'Port must be between 1024 and 65535.' }
$taskRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$taskSystem = Join-Path $taskRoot 'system'
foreach ($taskFolder in @('runtime\logs','runtime\state')) {
    [IO.Directory]::CreateDirectory((Join-Path $taskRoot $taskFolder)) | Out-Null
}
$taskPython = Join-Path (Split-Path -Parent $taskRoot) 'PSU_Esports_Chat_New_R69\runtime\python\python.exe'
$taskDatabase = Join-Path $taskSystem 'data\knowledge\common.sqlite'
if (-not (Test-Path -LiteralPath $taskPython) -or -not (Test-Path -LiteralPath $taskDatabase)) { throw 'The bundled runtime or migrated database is missing.' }
$taskUrl = "http://127.0.0.1:$Port/"
$taskRunFile = Join-Path $taskRoot 'runtime\chat-process.json'
$taskIdentity = (& $taskPython -B -c 'import hashlib,os,sys; print(hashlib.sha256(os.path.normcase(os.path.realpath(sys.argv[1])).encode()).hexdigest()[:16])' $taskSystem).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Bundled Python could not start.' }
$taskExisting = $null
try { $taskExisting = Invoke-RestMethod -Uri ($taskUrl + 'health') -TimeoutSec 2 } catch {}
if ($taskExisting) {
    if ($taskExisting.runtime.installation_id -ne $taskIdentity -or $taskExisting.runtime.knowledge_profile -ne 'r69-migration-preview') { throw 'This port belongs to another app. Use a different -Port; no existing process was stopped.' }
    if (-not $NoBrowser) { Start-Process $taskUrl }
    Write-Output "New chat is already running: $taskUrl"
    exit 0
}
$taskOverrides = @{
    PYTHONPATH = $taskSystem
    PYTHONDONTWRITEBYTECODE = '1'
    PYTHONUTF8 = '1'
    PSU_COMMON_CHAT_PROFILE = 'r69-migration-preview'
    PSU_RUNTIME_PROFILE = 'new-common-chat-r78'
    PSU_RUNTIME_VERSION = 'R78'
    PSU_KNOWLEDGE_DB = $taskDatabase
    PSU_CHAT_LOG_DIR = (Join-Path $taskRoot 'runtime\logs')
    PSU_CHAT_LOG_SQLITE_PATH = (Join-Path $taskRoot 'runtime\logs\transcripts.sqlite')
    PSU_CONVERSATION_STATE_PATH = (Join-Path $taskRoot 'runtime\state\conversations.sqlite')
    PSU_CHAT_LOG_WEBHOOK_URL = ''
    PSU_CHAT_LOG_POSTGRES = '0'
    PSU_CHAT_LOG_SQLITE = '1'
    PSU_CHAT_LOG_LOCAL_JSONL = '1'
    PSU_BILINGUAL_EN_ENABLED = '1'
    PSU_LOCAL_LLM_ASSIST_ENABLED = '1'
    PSU_EXPERIMENTAL_ALLOW_LLM = '1'
    PSU_SEMANTIC_RETRIEVAL = '1'
    PSU_LLM_PREFLIGHT = '0'
    PSU_PIPELINE_WARMUP = '0'
    PSU_PIPELINE_WORKER_SUPERVISOR = '1'
    PSU_PIPELINE_WORKERS = '2'
    PSU_PIPELINE_WORKER_WARMUP_EMBEDDING = '0'
    PSU_PIPELINE_WORKER_WARMUP_LLM = '0'
    PSU_CHAT_JOBS_ENABLED = '1'
    PSU_CHAT_JOB_DISPATCHERS = '2'
    PSU_MAX_ACTIVE_REQUESTS = '8'
    PSU_PRODUCT_BACKEND_TIMEOUT_SEC = '20'
    PSU_PIPELINE_GLOBAL_TIMEOUT_SEC = '18'
    PSU_QUERY_PLANNER_TIMEOUT_SEC = '2.5'
    PSU_INPUT_QUALITY_GUARD_MODE = 'enforce'
    PSU_INPUT_QUALITY_REPEAT_POLICY = 'warn_and_continue'
    PSU_LIVE_BOOKING_ENABLED = '1'
    PSU_LIVE_BOOKING_FETCH_MODE = 'wordpress'
    PSU_LIVE_BOOKING_CACHE_SEC = '10'
    PSU_R69_LAUNCH_TOKEN = ([Guid]::NewGuid().ToString('N') + [Guid]::NewGuid().ToString('N'))
}
$taskSavedEnvironment = @{}
$taskStamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$taskRunLog = Join-Path $taskRoot ("runtime\logs\server-$taskStamp-$([Guid]::NewGuid().ToString('N').Substring(0,8))")
try {
    foreach ($taskKey in $taskOverrides.Keys) { $taskSavedEnvironment[$taskKey] = [Environment]::GetEnvironmentVariable($taskKey, 'Process'); [Environment]::SetEnvironmentVariable($taskKey, $taskOverrides[$taskKey], 'Process') }
    $taskProcess = Start-Process -FilePath $taskPython -ArgumentList @('-B','-m','app.web_api.server','--host','127.0.0.1','--port',"$Port") -WorkingDirectory $taskSystem -WindowStyle Hidden -PassThru -RedirectStandardOutput ($taskRunLog + '.out.log') -RedirectStandardError ($taskRunLog + '.err.log')
    $taskRecord = @{ pid=$taskProcess.Id; started_utc=$taskProcess.StartTime.ToUniversalTime().ToString('o'); installation_id=$taskIdentity; url=$taskUrl; token=$taskOverrides.PSU_R69_LAUNCH_TOKEN; stdout=($taskRunLog+'.out.log'); stderr=($taskRunLog+'.err.log') }
    if (Test-Path -LiteralPath $taskRunFile) { Copy-Item -LiteralPath $taskRunFile -Destination (Join-Path $taskRoot ("runtime\chat-process-$taskStamp.json")) }
    $taskRecord | ConvertTo-Json | Set-Content -LiteralPath $taskRunFile -Encoding UTF8
    $taskReady = $false
    $taskHealthError = ''
    for ($taskAttempt = 0; $taskAttempt -lt 50; $taskAttempt++) {
        Start-Sleep -Milliseconds 500
        $taskProcess.Refresh()
        if ($taskProcess.HasExited) { throw "The new chat server stopped. See $taskRunLog.err.log" }
        try {
            $taskHealth = Invoke-RestMethod -Uri ($taskUrl + 'health') -TimeoutSec 1
            if ($taskHealth.runtime.installation_id -eq $taskIdentity -and $taskHealth.runtime.knowledge_profile -eq 'r69-migration-preview') { $taskReady = $true; break }
        } catch { $taskHealthError = $_.Exception.Message }
    }
    if (-not $taskReady) { throw "The new chat did not pass the connection check. Last connection error: $taskHealthError. See $taskRunLog.err.log or use Stop-New-Chat.cmd." }
    if (-not $NoBrowser) { Start-Process $taskUrl }
    Write-Output "New chat is ready: $taskUrl"
} finally {
    foreach ($taskKey in $taskSavedEnvironment.Keys) { [Environment]::SetEnvironmentVariable($taskKey, $taskSavedEnvironment[$taskKey], 'Process') }
}
