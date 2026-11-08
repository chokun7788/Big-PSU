param([switch]$SkipLock)
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$stateRoot = Join-Path $root 'runtime\state'
$statePath = Join-Path $stateRoot 'active.json'
$lock = $null
function Stop-OwnedTree($Item,[string]$ExpectedPath) {
    if (-not $Item -or -not $Item.pid) { return }
    $process = Get-Process -Id $Item.pid -ErrorAction SilentlyContinue
    if (-not $process) { return }
    $saved = [datetime]::Parse($Item.started_utc).ToUniversalTime()
    if ([math]::Abs(($process.StartTime.ToUniversalTime()-$saved).TotalSeconds) -gt 1) { throw 'Recorded process ID has been reused. Refusing to stop it.' }
    $all = @(Get-CimInstance Win32_Process)
    $info = @($all | Where-Object ProcessId -eq $Item.pid)[0]
    if (-not $info.CommandLine -or $info.CommandLine.IndexOf($ExpectedPath,[StringComparison]::OrdinalIgnoreCase) -lt 0) { throw 'Process path does not match this folder. Refusing to stop it.' }
    $ids = New-Object 'System.Collections.Generic.List[int]'
    $ids.Add([int]$Item.pid)
    for ($i=0; $i -lt $ids.Count; $i++) {
        foreach ($child in @($all | Where-Object ParentProcessId -eq $ids[$i])) { if (-not $ids.Contains([int]$child.ProcessId)) { $ids.Add([int]$child.ProcessId) } }
    }
    # Freeze ownership through creation time checks before stopping descendants.
    for ($i=$ids.Count-1; $i -ge 0; $i--) {
        $target = @($all | Where-Object ProcessId -eq $ids[$i])[0]
        $live = Get-CimInstance Win32_Process -Filter "ProcessId=$($ids[$i])"
        if ($live -and $target -and $live.CreationDate -eq $target.CreationDate) { Stop-Process -Id $ids[$i] -Force -ErrorAction SilentlyContinue }
    }
}
try {
    if (-not (Test-Path -LiteralPath $statePath)) { Write-Host 'This folder is not running.'; return }
    if (-not $SkipLock) { $lock = [System.IO.File]::Open((Join-Path $stateRoot 'launcher.lock'),'OpenOrCreate','ReadWrite','None') }
    $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
    if ($state.root -ne $root) { throw 'Runtime state belongs to a different folder. Refusing to stop another copy.' }
    Stop-OwnedTree $state.chat (Join-Path $root 'system\PSU_Esports_Chatbot_Local\Start-PSU-Esports-Chatbot.ps1')
    if ($state.ollama.owned) { Stop-OwnedTree $state.ollama (Join-Path $root 'runtime\ollama\ollama.exe') }
    $state.status = 'stopped'
    $json = $state | ConvertTo-Json -Depth 8
    $json | Set-Content -LiteralPath (Join-Path $stateRoot ('stopped_'+(Get-Date -Format 'yyyyMMdd_HHmmss_fff')+'.json')) -Encoding UTF8
    $json | Set-Content -LiteralPath $statePath -Encoding UTF8
    Write-Host 'This folder has stopped. Chat logs were kept. Other services were left running.'
} finally { if ($lock) { $lock.Dispose() } }
