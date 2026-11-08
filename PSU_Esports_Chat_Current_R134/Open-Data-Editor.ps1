param([switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
$taskSystem = Join-Path $PSScriptRoot 'system'
$taskDatabase = [IO.Path]::GetFullPath((Join-Path $taskSystem 'data\knowledge\common.sqlite'))
$taskSessionFile = Join-Path $taskSystem 'data\knowledge\owner-session.json'
function Find-CurrentOwnerEditor {
    if (-not (Test-Path -LiteralPath $taskSessionFile)) { return $null }
    try {
        $taskSession = Get-Content -LiteralPath $taskSessionFile -Raw | ConvertFrom-Json
        $taskUri = [Uri]$taskSession.url
        if ($taskUri.Host -ne '127.0.0.1' -or $taskUri.Port -ne 8116 -or $taskSession.db -ne $taskDatabase) { return $null }
        $taskToken = $taskUri.Fragment.Substring(1) -replace '^token=',''
        $taskRegistry = Invoke-RestMethod -Uri 'http://127.0.0.1:8116/api/registry' -Headers @{Authorization=('Bearer '+$taskToken)} -TimeoutSec 2
        if ([IO.Path]::GetFullPath($taskRegistry.db) -eq $taskDatabase) { return $taskSession }
    } catch {}
    return $null
}
$taskSession = Find-CurrentOwnerEditor
if (-not $taskSession) {
    if (Get-NetTCPConnection -State Listen -LocalPort 8116 -ErrorAction SilentlyContinue) { throw 'Port 8116 belongs to another editor. It was left running.' }
    $taskPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
    $taskSavedPythonPath = $env:PYTHONPATH
    $taskLog = Join-Path $PSScriptRoot 'runtime\logs\owner-editor'
    [IO.Directory]::CreateDirectory((Split-Path -Parent $taskLog)) | Out-Null
    try {
        $env:PYTHONPATH = $taskSystem
        $taskProcess = Start-Process -FilePath $taskPython -ArgumentList @('-B','-m','app.knowledge.common.owner_server','--db',('"'+$taskDatabase+'"'),'--port','8116','--no-browser') -WorkingDirectory $taskSystem -WindowStyle Hidden -PassThru -RedirectStandardOutput ($taskLog+'.out.log') -RedirectStandardError ($taskLog+'.err.log')
    } finally { $env:PYTHONPATH = $taskSavedPythonPath }
    for ($taskTry=0; $taskTry -lt 40; $taskTry++) {
        Start-Sleep -Milliseconds 500
        $taskSession = Find-CurrentOwnerEditor
        if ($taskSession) { break }
        $taskProcess.Refresh()
        if ($taskProcess.HasExited) { throw 'The data editor stopped. Check runtime/logs/owner-editor.err.log.' }
    }
    if (-not $taskSession) { throw 'The matching data editor has not passed its connection check.' }
}
if (-not $NoBrowser) { Start-Process $taskSession.url }
Write-Output 'R134 data editor is ready on port 8116 and uses the same database as the current chat.'
