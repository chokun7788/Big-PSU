$ErrorActionPreference='Stop'
$out=Join-Path $PSScriptRoot 'r52_research_flow_20261009_191123'
$h=Invoke-RestMethod http://127.0.0.1:8093/health -TimeoutSec 8
if($h.runtime.version -ne '2026.10.09-research-flow-r52.3'){throw 'Unexpected runtime'}
$all=@(Get-CimInstance Win32_Process)
$server=$all | Where-Object ProcessId -eq $h.runtime.python.pid
$owner=$all | Where-Object ProcessId -eq $server.ParentProcessId
$expected=Join-Path $out 'candidate_r52_3\PSU_Esports_Chatbot_Local\Open-PSU-Esports-Chatbot.ps1'
if(-not $owner.CommandLine.Contains($expected)){throw 'Unexpected launcher'}
$ids=[System.Collections.Generic.HashSet[int]]::new();[void]$ids.Add([int]$owner.ProcessId)
do {$n=$ids.Count;foreach($p in $all){if($ids.Contains([int]$p.ParentProcessId)){[void]$ids.Add([int]$p.ProcessId)}}}while($ids.Count -gt $n)
$chosen=@($all|Where-Object {$ids.Contains([int]$_.ProcessId)})
$chosen|Select-Object ProcessId,ParentProcessId,CommandLine|ConvertTo-Json -Depth 3|Set-Content -LiteralPath (Join-Path $out 'STOP_OWN_R52_3_PROCESSES.json') -Encoding utf8
foreach($p in $chosen){Stop-Process -Id $p.ProcessId -Force -ErrorAction SilentlyContinue}
$launcher=Join-Path $out 'candidate_r52_4\PSU_Esports_Chatbot_Local\Open-PSU-Esports-Chatbot.ps1'
Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$launcher+'"'),'-Port','8093','-NoBrowser','-PythonPath','"C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python\python.exe"') -WindowStyle Hidden -RedirectStandardOutput (Join-Path $out 'r52_4_start_stdout.txt') -RedirectStandardError (Join-Path $out 'r52_4_start_stderr.txt')
'Started r52.4'
