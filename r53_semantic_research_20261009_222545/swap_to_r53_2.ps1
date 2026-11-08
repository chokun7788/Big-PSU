$ErrorActionPreference='Stop'
$out='C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r53_semantic_research_20261009_222545'
$h=Invoke-RestMethod http://127.0.0.1:8093/health -TimeoutSec 8
if($h.runtime.version -ne '2026.10.09-semantic-r53.1'){throw 'Unexpected runtime'}
$all=@(Get-CimInstance Win32_Process)
$server=$all | Where-Object ProcessId -eq $h.runtime.python.pid
$owner=$all | Where-Object ProcessId -eq $server.ParentProcessId
$expected='C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r53_semantic_research_20261009_222545\candidate\PSU_Esports_Chatbot_Local\Open-PSU-Esports-Chatbot.ps1'
if(-not $owner.CommandLine.Contains($expected)){throw 'Unexpected launcher'}
$ids=[System.Collections.Generic.HashSet[int]]::new();[void]$ids.Add([int]$owner.ProcessId)
do {$n=$ids.Count;foreach($p in $all){if($ids.Contains([int]$p.ParentProcessId)){[void]$ids.Add([int]$p.ProcessId)}}}while($ids.Count -gt $n)
$chosen=@($all|Where-Object {$ids.Contains([int]$_.ProcessId)})
$chosen|Select-Object ProcessId,ParentProcessId,CommandLine|ConvertTo-Json -Depth 3|Set-Content -LiteralPath (Join-Path $out 'STOP_OWN_R53_1_PROCESSES.json') -Encoding utf8
foreach($p in $chosen){Stop-Process -Id $p.ProcessId -Force -ErrorAction SilentlyContinue}
$launcher='C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r53_semantic_research_20261009_222545\candidate_r53_2\PSU_Esports_Chatbot_Local\Open-PSU-Esports-Chatbot.ps1'
Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$launcher+'"'),'-Port','8093','-NoBrowser','-PythonPath','"C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python\python.exe"') -WindowStyle Hidden -RedirectStandardOutput (Join-Path $out 'r53_2_start_stdout.txt') -RedirectStandardError (Join-Path $out 'r53_2_start_stderr.txt')
'Started r53.2'
