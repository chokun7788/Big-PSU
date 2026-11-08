$ErrorActionPreference='Stop'
$r46Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r46_current_path.txt') -Raw).Trim()
$r45Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r45_current_path.txt') -Raw).Trim()
$r46OldRoot=(Get-Content -LiteralPath (Join-Path $r45Out 'release_r45_2_path.txt') -Raw).Trim()
$r46Health=Invoke-RestMethod -Uri 'http://127.0.0.1:8091/health' -TimeoutSec 5
if ($r46Health.runtime.version -ne '2026.10.07-rental-scope-r45.2') { throw 'Unexpected server identity; preserve it.' }
$r46Processes=@(Get-CimInstance Win32_Process)
$r46Server=@($r46Processes | Where-Object { $_.ProcessId -eq $r46Health.runtime.python.pid })
if ($r46Server.Count -ne 1) { throw 'Cannot establish previous server identity.' }
$r46Parent=@($r46Processes | Where-Object { $_.ProcessId -eq $r46Server[0].ParentProcessId })
if ($r46Parent.Count -ne 1 -or -not $r46Parent[0].CommandLine.Contains((Join-Path $r46OldRoot 'Open-PSU-Esports-Chatbot.ps1'))) { throw 'Parent does not belong to previous candidate.' }
$r46Ids=@([int]$r46Parent[0].ProcessId)
do {
    $r46Added=@($r46Processes | Where-Object { $r46Ids -contains [int]$_.ParentProcessId -and $r46Ids -notcontains [int]$_.ProcessId } | Select-Object -ExpandProperty ProcessId)
    $r46Ids+=@($r46Added)
} while ($r46Added.Count -gt 0)
$r46Processes | Where-Object { $r46Ids -contains [int]$_.ProcessId } | Select-Object ProcessId,ParentProcessId,CommandLine | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $r46Out 'STOP_OWN_R45_2_PROCESSES.json') -Encoding utf8
foreach ($r46ProcessId in @($r46Ids | Select-Object -Unique | Sort-Object -Descending)) {
    try { [System.Diagnostics.Process]::GetProcessById($r46ProcessId).Kill() } catch [System.ArgumentException] { }
}
$r46NewRoot=(Get-Content -LiteralPath (Join-Path $r46Out 'release_r46_1_path.txt') -Raw).Trim()
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $r46NewRoot 'Open-PSU-Esports-Background.ps1') -NoBrowser -Port 8091
if ($LASTEXITCODE -ne 0) { throw "New candidate launcher exit $LASTEXITCODE" }
