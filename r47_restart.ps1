$ErrorActionPreference='Stop'
$r47Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r47_current_path.txt') -Raw).Trim()
$r46Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r46_current_path.txt') -Raw).Trim()
$r47OldRoot=(Get-Content -LiteralPath (Join-Path $r46Out 'release_r46_1_path.txt') -Raw).Trim()
$r47Health=Invoke-RestMethod -Uri 'http://127.0.0.1:8091/health' -TimeoutSec 5
if ($r47Health.runtime.version -ne '2026.10.07-english-rental-r46.1') { throw 'Unexpected server identity; preserve it.' }
$r47Processes=@(Get-CimInstance Win32_Process)
$r47Server=@($r47Processes | Where-Object { $_.ProcessId -eq $r47Health.runtime.python.pid })
if ($r47Server.Count -ne 1) { throw 'Cannot establish previous server identity.' }
$r47Parent=@($r47Processes | Where-Object { $_.ProcessId -eq $r47Server[0].ParentProcessId })
if ($r47Parent.Count -ne 1 -or -not $r47Parent[0].CommandLine.Contains((Join-Path $r47OldRoot 'Open-PSU-Esports-Chatbot.ps1'))) { throw 'Parent does not belong to previous candidate.' }
$r47Ids=@([int]$r47Parent[0].ProcessId)
do {
    $r47Added=@($r47Processes | Where-Object { $r47Ids -contains [int]$_.ParentProcessId -and $r47Ids -notcontains [int]$_.ProcessId } | Select-Object -ExpandProperty ProcessId)
    $r47Ids+=@($r47Added)
} while ($r47Added.Count -gt 0)
$r47Processes | Where-Object { $r47Ids -contains [int]$_.ProcessId } | Select-Object ProcessId,ParentProcessId,CommandLine | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $r47Out 'STOP_OWN_R46_1_PROCESSES.json') -Encoding utf8
foreach ($r47ProcessId in @($r47Ids | Select-Object -Unique | Sort-Object -Descending)) {
    try { [System.Diagnostics.Process]::GetProcessById($r47ProcessId).Kill() } catch [System.ArgumentException] { }
}
$r47NewRoot=(Get-Content -LiteralPath (Join-Path $r47Out 'release_r47_1_path.txt') -Raw).Trim()
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $r47NewRoot 'Open-PSU-Esports-Background.ps1') -NoBrowser -Port 8091
if ($LASTEXITCODE -ne 0) { throw "New candidate launcher exit $LASTEXITCODE" }
