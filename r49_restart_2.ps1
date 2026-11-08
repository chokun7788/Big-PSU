$ErrorActionPreference='Stop'
$r48Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r48_current_path.txt') -Raw).Trim()
$r47Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r47_current_path.txt') -Raw).Trim()
$r48OldRoot=(Get-Content -LiteralPath (Join-Path (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r49_current_path.txt') -Raw).Trim() 'release_r49_1_path.txt') -Raw).Trim()
$r48Health=Invoke-RestMethod -Uri 'http://127.0.0.1:8091/health' -TimeoutSec 5
if ($r48Health.runtime.version -ne '2026.10.09-service-dialogue-r49.1') { throw 'Unexpected server identity; preserve it.' }
$r48Processes=@(Get-CimInstance Win32_Process)
$r48Server=@($r48Processes | Where-Object { $_.ProcessId -eq $r48Health.runtime.python.pid })
if ($r48Server.Count -ne 1) { throw 'Cannot establish previous server identity.' }
$r48Parent=@($r48Processes | Where-Object { $_.ProcessId -eq $r48Server[0].ParentProcessId })
if ($r48Parent.Count -ne 1 -or -not $r48Parent[0].CommandLine.Contains((Join-Path $r48OldRoot 'Open-PSU-Esports-Chatbot.ps1'))) { throw 'Parent does not belong to previous candidate.' }
$r48Ids=@([int]$r48Parent[0].ProcessId)
do {
    $r48Added=@($r48Processes | Where-Object { $r48Ids -contains [int]$_.ParentProcessId -and $r48Ids -notcontains [int]$_.ProcessId } | Select-Object -ExpandProperty ProcessId)
    $r48Ids+=@($r48Added)
} while ($r48Added.Count -gt 0)
$r48Processes | Where-Object { $r48Ids -contains [int]$_.ProcessId } | Select-Object ProcessId,ParentProcessId,CommandLine | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r49_current_path.txt') -Raw).Trim() 'STOP_OWN_R49_1_PROCESSES.json') -Encoding utf8
foreach ($r48ProcessId in @($r48Ids | Select-Object -Unique | Sort-Object -Descending)) {
    try { [System.Diagnostics.Process]::GetProcessById($r48ProcessId).Kill() } catch [System.ArgumentException] { }
}
$r49Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r49_current_path.txt') -Raw).Trim()
$r48NewRoot=(Get-Content -LiteralPath (Join-Path $r49Out 'release_r49_2_path.txt') -Raw).Trim()
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $r48NewRoot 'Open-PSU-Esports-Background.ps1') -NoBrowser -Port 8091
if ($LASTEXITCODE -ne 0) { throw "New candidate launcher exit $LASTEXITCODE" }
