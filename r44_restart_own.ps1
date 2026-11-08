$ErrorActionPreference='Stop'
$r44Out=Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r44_current_path.txt') -Raw
$r44OldRoot=Get-Content -LiteralPath (Join-Path $r44Out 'release_r44_2_path.txt') -Raw
$r44Health=Invoke-RestMethod -Uri 'http://127.0.0.1:8091/health' -TimeoutSec 5
if ($r44Health.runtime.version -ne '2026.10.06-zone-rental-r44.2') { throw 'Not the previous r44 candidate; preserve it.' }
$r44Processes=@(Get-CimInstance Win32_Process)
$r44Server=@($r44Processes | Where-Object { $_.ProcessId -eq $r44Health.runtime.python.pid })
if ($r44Server.Count -ne 1) { throw 'Cannot establish previous server identity.' }
$r44Parent=@($r44Processes | Where-Object { $_.ProcessId -eq $r44Server[0].ParentProcessId })
if ($r44Parent.Count -ne 1 -or -not $r44Parent[0].CommandLine.Contains((Join-Path $r44OldRoot 'Open-PSU-Esports-Chatbot.ps1'))) { throw 'Parent does not belong to this candidate.' }
$r44Ids=@([int]$r44Parent[0].ProcessId)
do {
  $r44Added=@($r44Processes | Where-Object { $r44Ids -contains [int]$_.ParentProcessId -and $r44Ids -notcontains [int]$_.ProcessId } | Select-Object -ExpandProperty ProcessId)
  $r44Ids+=@($r44Added)
} while ($r44Added.Count -gt 0)
$r44Processes | Where-Object { $r44Ids -contains [int]$_.ProcessId } | Select-Object ProcessId,ParentProcessId,CommandLine | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $r44Out 'STOP_OWN_R44_2_PROCESSES.json') -Encoding utf8
foreach ($r44ProcessId in @($r44Ids | Select-Object -Unique | Sort-Object -Descending)) {
  try { [System.Diagnostics.Process]::GetProcessById($r44ProcessId).Kill() } catch [System.ArgumentException] { }
}
$r44NewRoot=Get-Content -LiteralPath (Join-Path $r44Out 'release_r44_3_path.txt') -Raw
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $r44NewRoot 'Open-PSU-Esports-Background.ps1') -NoBrowser -Port 8091
if ($LASTEXITCODE -ne 0) { throw "New candidate launcher exit $LASTEXITCODE" }
