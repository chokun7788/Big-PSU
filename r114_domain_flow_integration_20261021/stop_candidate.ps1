$ErrorActionPreference = 'Stop'
$candidateRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$runtimeRoot = Join-Path $candidateRoot 'runtime'
$runs = Get-ChildItem -LiteralPath $runtimeRoot -Directory | Sort-Object LastWriteTime -Descending
foreach ($run in $runs) {
    $manifestPath = Join-Path $run.FullName 'SERVERS.json'
    $stoppedPath = Join-Path $run.FullName 'STOPPED.json'
    if (-not (Test-Path -LiteralPath $manifestPath) -or (Test-Path -LiteralPath $stoppedPath)) { continue }
    $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    if (-not $manifest.candidate_only -or [IO.Path]::GetFullPath($manifest.db) -ne (Join-Path $candidateRoot 'system\data\knowledge\common.sqlite')) { throw 'Unexpected candidate manifest; no process stopped.' }
    foreach ($item in $manifest.processes) {
        $taskProcess = Get-CimInstance Win32_Process -Filter ('ProcessId=' + [int]$item.pid)
        if (-not $taskProcess) { continue }
        $expectedModule = if ($item.name -eq 'chat') { 'app.web_api.server.*--port 8134' } else { 'app.knowledge.common.owner_server.*--port 8135' }
        if ($taskProcess.CommandLine -notmatch $expectedModule) { throw 'Process identity changed; no further processes stopped.' }
        Stop-Process -Id ([int]$item.pid) -ErrorAction Stop
    }
    @{ stopped=$true; at=(Get-Date -Format o); verified_processes=$manifest.processes } | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $stoppedPath -Encoding utf8
    Write-Output 'R114 preview and owner editor stopped.'
    exit 0
}
Write-Output 'No managed R114 preview is running.'
