param([int]$LauncherPid,[int]$Port,[string]$PackageRoot)
$ErrorActionPreference='Stop'
$package=(Resolve-Path -LiteralPath $PackageRoot).Path
$expected=Join-Path $package 'Start-PSU-Esports-Chatbot.ps1'
$all=@(Get-CimInstance Win32_Process)
$launcher=$all | Where-Object ProcessId -eq $LauncherPid
if ($null -eq $launcher -or $launcher.CommandLine -notlike ('*'+$expected+'*') -or $launcher.CommandLine -notmatch ('\-Port\s+'+$Port+'(?:\s|$)')) {throw 'Launcher identity differs; leave it untouched.'}
$descendants=@($LauncherPid)
do {
    $new=@($all | Where-Object { $_.ParentProcessId -in $descendants -and $_.ProcessId -notin $descendants } | Select-Object -ExpandProperty ProcessId)
    $descendants+= $new
} while ($new.Count -gt 0)
$listeners=@(Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction Stop)
if (@($listeners | Where-Object OwningProcess -notin $descendants).Count -gt 0) {throw 'Port belongs to another process; leave it untouched.'}
$report=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r33_report_path.txt') -Raw).Trim()
$record=@{launcherPid=$LauncherPid;port=$Port;package=$package;commandLine=$launcher.CommandLine;descendantPids=$descendants;listeners=@($listeners | Select-Object LocalAddress,LocalPort,OwningProcess);reason='replace verified task-owned test/chatbot launcher';time=(Get-Date).ToString('o')}
$recordPath=Join-Path $report ('stopped_owned_'+$Port+'_'+[guid]::NewGuid().ToString('N')+'.json')
if(Test-Path -LiteralPath $recordPath){throw 'Record already exists.'}
$record | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $recordPath -Encoding UTF8
[System.Diagnostics.Process]::GetProcessById($LauncherPid).Kill($true)
$record | ConvertTo-Json -Depth 6 -Compress
