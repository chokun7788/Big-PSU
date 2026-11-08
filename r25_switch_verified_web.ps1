$ErrorActionPreference = 'Stop'
$report = (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r25_report_path.txt') -Raw).Trim()
$units = Get-Content -LiteralPath (Join-Path $report 'round_C_unit.json') -Raw | ConvertFrom-Json
$http = Get-Content -LiteralPath (Join-Path $report 'http_candidate_B.json') -Raw | ConvertFrom-Json
$review = Get-Content -LiteralPath (Join-Path $report 'full_r25_B_source_presence_review.json') -Raw | ConvertFrom-Json
if (-not $units.success -or $http.passed -ne $http.total -or $review.total -ne 2000 -or $review.unresolved_ids.Count -gt 0) { throw 'Required verification is incomplete.' }
$owned = @(
    @{ ProcessId=12004; PackageName='owner_local_delivery_20261001_competition_r24_final'; Port=8090 },
    @{ ProcessId=15256; PackageName='owner_local_delivery_20261001_competition_format_r25'; Port=8091 },
    @{ ProcessId=20512; PackageName='owner_local_delivery_20261001_competition_format_r25_final'; Port=8092 }
)
$verified = @()
foreach ($record in $owned) {
    $targetProcessId = [int]$record.ProcessId
    $targetProcess = Get-CimInstance Win32_Process -Filter ('ProcessId = ' + $targetProcessId)
    if ($null -eq $targetProcess) { throw "Previously verified launcher is no longer present: $targetProcessId" }
    $expectedPath = 'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\' + $record.PackageName + '\PSU_Esports_Chatbot_Local\Start-PSU-Esports-Chatbot.ps1'
    if (-not $targetProcess.CommandLine.Contains($expectedPath) -or -not $targetProcess.CommandLine.Contains('-Port ' + $record.Port)) { throw "Launcher identity changed: $targetProcessId" }
    $verified += @{ ProcessId=$targetProcessId; CommandLine=$targetProcess.CommandLine }
}
$verified | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $report 'verified_stopped_launchers.json') -Encoding UTF8
foreach ($record in $owned) {
    $ownedProcess = [System.Diagnostics.Process]::GetProcessById([int]$record.ProcessId)
    $ownedProcess.Kill($true)
    $ownedProcess.WaitForExit(5000) | Out-Null
}
& (Join-Path $PSScriptRoot 'r25_start_web.ps1') -Port 8090 -PackageRoot 'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261001_competition_format_r25_final\PSU_Esports_Chatbot_Local'
