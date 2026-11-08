param([int]$Port = 0, [switch]$NoBrowser, [switch]$ForceBundledOllama, [switch]$SetupOnly)
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
if (-not [Environment]::Is64BitOperatingSystem) { throw 'This package requires Windows x64.' }
if ([Environment]::OSVersion.Version.Build -lt 19045) { throw 'This package requires Windows 10 22H2 or Windows 11.' }
$package = Join-Path $root 'system\PSU_Esports_Chatbot_Local'
$stateRoot = Join-Path $root 'runtime\state'
$logRoot = Join-Path $package 'data\logs\launcher'
New-Item -ItemType Directory -Force -Path $stateRoot,$logRoot | Out-Null
$manifest = Get-Content -LiteralPath (Join-Path $root 'ready_manifest.json') -Raw | ConvertFrom-Json
$statePath = Join-Path $stateRoot 'active.json'
$run = (Get-Date -Format 'yyyyMMdd_HHmmss_fff') + '_' + [guid]::NewGuid().ToString('N').Substring(0,8)
$lock = $null
$appChild = $null
$ollamaChild = $null

function Get-Health([int]$ChatPort) {
    try { return Invoke-RestMethod "http://127.0.0.1:$ChatPort/health" -TimeoutSec 2 } catch { return $null }
}
function Test-Port([int]$TestPort) {
    $client = New-Object System.Net.Sockets.TcpClient
    try { $client.Connect('127.0.0.1',$TestPort); return $true } catch { return $false } finally { $client.Dispose() }
}
function Test-Owned($Item, [string]$ExpectedPath) {
    if (-not $Item -or -not $Item.pid) { return $false }
    try {
        $p = Get-Process -Id $Item.pid -ErrorAction Stop
        $saved = [datetime]::Parse($Item.started_utc).ToUniversalTime()
        if ([math]::Abs(($p.StartTime.ToUniversalTime()-$saved).TotalSeconds) -gt 1) { return $false }
        $info = Get-CimInstance Win32_Process -Filter "ProcessId=$($Item.pid)"
        return $info.CommandLine -and ($info.CommandLine.IndexOf($ExpectedPath,[StringComparison]::OrdinalIgnoreCase) -ge 0)
    } catch { return $false }
}
function Test-Models([string]$BaseUrl) {
    try {
        $tags = Invoke-RestMethod "$BaseUrl/api/tags" -TimeoutSec 3
        foreach ($needed in $manifest.models) {
            $found = @($tags.models | Where-Object { $_.name -eq $needed.name -and $_.digest -eq $needed.digest })
            if ($found.Count -eq 0) { return $false }
        }
        return $true
    } catch { return $false }
}
function Save-State($State) {
    $text = $State | ConvertTo-Json -Depth 8
    $text | Set-Content -LiteralPath (Join-Path $stateRoot ($run + '_' + $State.status + '.json')) -Encoding UTF8
    $temporary = Join-Path $stateRoot ('active_' + $run + '.tmp')
    $text | Set-Content -LiteralPath $temporary -Encoding UTF8
    Move-Item -LiteralPath $temporary -Destination $statePath -Force
}
function Test-Ready($Health) {
    return $Health -and $Health.ok -and $Health.service -eq 'psu-esports-chat-web' -and
        $Health.runtime.version -eq $manifest.runtime_version -and
        $Health.pipeline_workers.workers.Count -gt 0 -and
        @($Health.pipeline_workers.workers | Where-Object { -not $_.alive -or -not $_.ready }).Count -eq 0
}

try {
    try { $lock = [System.IO.File]::Open((Join-Path $stateRoot 'launcher.lock'),'OpenOrCreate','ReadWrite','None') }
    catch { throw 'Chatbot is already starting or stopping. Wait a moment, then open Start-Chatbot.cmd again.' }
    $prior = $null
    if (Test-Path -LiteralPath $statePath) { $prior = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json }
    $appLauncher = Join-Path $package 'Start-PSU-Esports-Chatbot.ps1'
    if ($prior -and $prior.root -eq $root -and (Test-Owned $prior.chat $appLauncher)) {
        if ($Port -ne 0 -and $Port -ne $prior.port) { throw 'This folder is already running on another port. Stop it first.' }
        $health = Get-Health $prior.port
        if (Test-Ready $health) {
            if ($ForceBundledOllama -and -not $prior.ollama.owned) { throw 'Stop this folder before switching to bundled Ollama.' }
            Write-Host "Chatbot is ready: $($prior.url)"
            if (-not $NoBrowser) { Start-Process $prior.url }
            return
        }
        throw 'This folder has a running process that is not ready. Open Stop-Chatbot.cmd, then start again. Logs are in system\PSU_Esports_Chatbot_Local\data\logs\launcher.'
    }
    $bundledPython = Join-Path $root 'runtime\python\python.exe'
    & $bundledPython -I (Join-Path $root 'tools\ensure_models.py')
    if ($LASTEXITCODE -ne 0) { throw 'Model setup did not complete. See the message above and try again.' }
    if ($SetupOnly) { Write-Host 'Model setup complete. Open Start-Chatbot.cmd to use the Chatbot.'; return }
    if ($Port -eq 0) {
        $Port = @(8090..8099 | Where-Object { -not (Test-Port $_) } | Select-Object -First 1)[0]
        if (-not $Port) { throw 'Ports 8090-8099 are occupied. Use Start-Chatbot.ps1 -Port with a free port.' }
    }
    if ($Port -lt 1024 -or $Port -gt 65535 -or (Test-Port $Port)) { throw "Port $Port is not available. No existing service was stopped." }
    $python = Join-Path $root 'runtime\python\python.exe'
    $ollamaExe = Join-Path $root 'runtime\ollama\ollama.exe'
    foreach ($file in @($python,$ollamaExe,$appLauncher)) {
        if (-not (Test-Path -LiteralPath $file)) { throw "Missing bundled file: $file. Keep the entire folder together." }
    }
    # Do not inherit unrelated Python or remote database configuration.
    Remove-Item Env:PYTHONHOME,Env:PYTHONPATH,Env:PSU_CHAT_LOG_POSTGRES_URL -ErrorAction SilentlyContinue
    $env:PSU_CHAT_LOG_POSTGRES = '0'
    Remove-Item Env:PSU_CHAT_LOG_WEBHOOK_URL,Env:PSU_CHAT_LOG_WEBHOOK_TOKEN -ErrorAction SilentlyContinue
    $env:PYTHONNOUSERSITE = '1'
    $env:PYTHONDONTWRITEBYTECODE = '1'
    $env:PYTHONUTF8 = '1'
    $env:PYTHONIOENCODING = 'utf-8'
    $ollamaState = $null
    if ($prior -and $prior.ollama.owned -and (Test-Owned $prior.ollama $ollamaExe) -and (Test-Models $prior.ollama.url)) {
        $ollamaState = $prior.ollama
    } elseif ($false) {
        $ollamaState = @{ owned=$false; url='http://127.0.0.1:11434'; mode='existing_local_verified_model_digests' }
    } else {
        $ollamaPort = @(11435..11444 | Where-Object { -not (Test-Port $_) } | Select-Object -First 1)[0]
        if (-not $ollamaPort) { throw 'No free local Ollama port in 11435-11444.' }
        $env:OLLAMA_HOST = "127.0.0.1:$ollamaPort"
        $env:OLLAMA_MODELS = Join-Path $root 'runtime\models'
        $env:OLLAMA_NO_CLOUD = '1'
        Write-Host 'Starting bundled Ollama and models...'
        $ollamaChild = Start-Process -FilePath $ollamaExe -ArgumentList 'serve' -WorkingDirectory (Split-Path $ollamaExe) -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $logRoot ($run+'_ollama.out.log')) -RedirectStandardError (Join-Path $logRoot ($run+'_ollama.err.log'))
        $ollamaState = @{ owned=$true; url="http://127.0.0.1:$ollamaPort"; pid=$ollamaChild.Id; started_utc=$ollamaChild.StartTime.ToUniversalTime().ToString('o'); mode='bundled' }
        Save-State @{root=$root;version=$manifest.runtime_version;run=$run;port=$Port;url="http://127.0.0.1:$Port/";status='ollama_starting';ollama=$ollamaState;chat=$null}
        $deadline = (Get-Date).AddSeconds(40)
        while (-not (Test-Models $ollamaState.url)) {
            if ($ollamaChild.HasExited -or (Get-Date) -gt $deadline) { throw 'Bundled Ollama failed to become ready. Check the latest launcher logs.' }
            Start-Sleep -Milliseconds 500
        }
    }
    $env:OLLAMA_URL = $ollamaState.url
    $env:PSU_EMBEDDING_OLLAMA_URL = $ollamaState.url
    Write-Host 'Starting Chatbot. Please wait for the browser to open...'
    $appChild = Start-Process -FilePath (Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe') -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$appLauncher+'"'),'-Port',"$Port") -WorkingDirectory $package -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $logRoot ($run+'_chat.out.log')) -RedirectStandardError (Join-Path $logRoot ($run+'_chat.err.log'))
    $state = @{root=$root;version=$manifest.runtime_version;run=$run;port=$Port;url="http://127.0.0.1:$Port/";status='starting';ollama=$ollamaState;chat=@{pid=$appChild.Id;started_utc=$appChild.StartTime.ToUniversalTime().ToString('o');launcher=$appLauncher}}
    Save-State $state
    $deadline = (Get-Date).AddSeconds([int]$manifest.startup_timeout_sec)
    $health = $null
    while (-not (Test-Ready $health)) {
        if ($appChild.HasExited -or (Get-Date) -gt $deadline) { throw 'Chatbot did not become ready. Check the latest launcher logs, then stop and start again.' }
        Start-Sleep -Milliseconds 700
        $health = Get-Health $Port
    }
    if (-not $health.warmup.ok) { throw 'Chatbot warmup failed. Check the launcher logs.' }
    if ($health.llm_preflight -and $health.llm_preflight.ok -eq $false) { throw 'Local language model preflight failed. Check the launcher logs.' }
    $health | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $stateRoot ($run+'_health.json')) -Encoding UTF8
    $state.status = 'ready'
    Save-State $state
    Write-Host "Chatbot is ready: $($state.url)"
    Write-Host 'Runs in the background. Use Stop-Chatbot.cmd when finished.'
    if (-not $NoBrowser) { Start-Process $state.url }
} catch {
    $_ | Out-String | Set-Content -LiteralPath (Join-Path $logRoot ($run+'_launcher_error.log')) -Encoding UTF8
    if ($appChild -or $ollamaChild) {
        # Stop only this folder's recorded process trees; preserve external Ollama.
        & (Join-Path $root 'Stop-Chatbot.ps1') -SkipLock
    }
    throw
} finally { if ($lock) { $lock.Dispose() } }
