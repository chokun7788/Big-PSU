param([string]$Candidate,[string]$ExpectedVersion,[string]$ExpectedLauncher,[string]$Label)
$ErrorActionPreference='Stop'
$out=Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r56_current_path.txt')
$h=Invoke-RestMethod http://127.0.0.1:8093/health -TimeoutSec 8
if($h.runtime.version -ne $ExpectedVersion){throw 'Unexpected runtime'}
$all=@(Get-CimInstance Win32_Process)
$server=$all | Where-Object ProcessId -eq $h.runtime.python.pid
$owner=$all | Where-Object ProcessId -eq $server.ParentProcessId
if(-not $owner.CommandLine.Contains($ExpectedLauncher)){throw 'Unexpected launcher'}
$ids=[System.Collections.Generic.HashSet[int]]::new();[void]$ids.Add([int]$owner.ProcessId)
do {$n=$ids.Count;foreach($p in $all){if($ids.Contains([int]$p.ParentProcessId)){[void]$ids.Add([int]$p.ProcessId)}}}while($ids.Count -gt $n)
$chosen=@($all|Where-Object {$ids.Contains([int]$_.ProcessId)})
$chosen|Select-Object ProcessId,ParentProcessId,CommandLine|ConvertTo-Json -Depth 3|Set-Content -LiteralPath (Join-Path $out ($Label+'_stopped_owned_processes.json')) -Encoding utf8
foreach($p in $chosen){Stop-Process -Id $p.ProcessId -Force -ErrorAction SilentlyContinue}
$launcher=Join-Path $Candidate 'Open-PSU-Esports-Chatbot.ps1'
Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$launcher+'"'),'-Port','8093','-NoBrowser','-PythonPath','"C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python\python.exe"') -WindowStyle Hidden -RedirectStandardOutput (Join-Path $out ($Label+'_start_stdout.txt')) -RedirectStandardError (Join-Path $out ($Label+'_start_stderr.txt'))
"Started $Label"
