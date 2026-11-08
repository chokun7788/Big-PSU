param([switch]$CheckOnly)
$ErrorActionPreference = 'Stop'
$taskPython = 'D:\CodexTraining\psu-r121-20261022\venv\Scripts\python.exe'
$taskProbe = Join-Path $PSScriptRoot 'system\tools\check_selected_model_environment.py'
if (-not (Test-Path -LiteralPath $taskPython)) { throw 'The selected local model environment is missing.' }
if ($CheckOnly) {
    & $taskPython -B $taskProbe --accelerator
    if ($LASTEXITCODE -ne 0) { throw 'The selected local model environment failed its dependency check.' }
    return
}
function Get-SelectedModelHealth {
    try { return Invoke-RestMethod -Uri 'http://127.0.0.1:12921/health' -TimeoutSec 3 } catch { return $null }
}
function Assert-SelectedModel($taskHealth) {
    if ($taskHealth.model -ne 'psu-r129:latest' -or $taskHealth.profiles.retained -ne 'e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8' -or $taskHealth.base_revision -ne 'ce0a7416fe82d4404b2b4a253ce3ac095ab1252c' -or $taskHealth.quantization -ne 'NF4 double quant BF16' -or $taskHealth.other_stages -ne 'base') { throw 'The model endpoint does not match the selected retained weights and precision. No process was stopped.' }
}
$taskHealth = Get-SelectedModelHealth
if ($taskHealth) { Assert-SelectedModel $taskHealth; return }
$taskListener = Get-NetTCPConnection -State Listen -LocalPort 12921 -ErrorAction SilentlyContinue
if ($taskListener) { throw 'Port 12921 is occupied but the selected model is unavailable. No process was stopped.' }
& $taskPython -B $taskProbe --accelerator
if ($LASTEXITCODE -ne 0) { throw 'The selected local model environment failed its dependency check. No model process was launched.' }
$taskWorkspace = Split-Path -Parent $PSScriptRoot
$taskScript = Join-Path $taskWorkspace 'r129_full_plan_completion_20261024\serve_model.py'
$taskName = 'model_retained_' + (Get-Date -Format 'yyyyMMddHHmmssfff')
$taskLogFolder = Join-Path $PSScriptRoot 'runtime\model-start'
[IO.Directory]::CreateDirectory($taskLogFolder) | Out-Null
$taskProc = Start-Process -FilePath $taskPython -ArgumentList @('-B','-u',('"'+$taskScript+'"'),'--port','12921','--output-name',$taskName) -WorkingDirectory $taskWorkspace -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $taskLogFolder ($taskName+'.out.log')) -RedirectStandardError (Join-Path $taskLogFolder ($taskName+'.err.log'))
for ($taskTry=0; $taskTry -lt 300; $taskTry++) {
    Start-Sleep -Seconds 1
    $taskProc.Refresh()
    if ($taskProc.HasExited) { throw "Selected model startup failed. See $taskLogFolder" }
    $taskHealth = Get-SelectedModelHealth
    if ($taskHealth) { Assert-SelectedModel $taskHealth; return }
}
throw "Selected model startup has not passed health checks. See $taskLogFolder"
