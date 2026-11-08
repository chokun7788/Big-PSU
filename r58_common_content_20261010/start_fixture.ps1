$ErrorActionPreference='Stop'
$out=$PSScriptRoot
$candidate=Join-Path $out 'system\PSU_Esports_Chatbot_Local'
$python='C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python\python.exe'
$env:PSU_KNOWLEDGE_DB=Join-Path $out 'fixtures\chat_fixture.sqlite'
$env:PSU_COMMON_ALLOW_DEMO='1'
$env:PYTHONIOENCODING='utf-8'
$launcher=Join-Path $candidate 'Open-PSU-Esports-Chatbot.ps1'
$args=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$launcher+'"'),'-Port','8098','-NoBrowser','-PythonPath',('"'+$python+'"'))
$child=Start-Process -FilePath powershell.exe -ArgumentList $args -WorkingDirectory $candidate -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $out 'fixture_chat_start.out.log') -RedirectStandardError (Join-Path $out 'fixture_chat_start.err.log')
$owner=Start-Process -FilePath $python -ArgumentList @('-B','-m','app.knowledge.common.owner_server','--port','8099','--db',('"'+$env:PSU_KNOWLEDGE_DB+'"'),'--no-browser') -WorkingDirectory $candidate -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $out 'fixture_owner_start.out.log') -RedirectStandardError (Join-Path $out 'fixture_owner_start.err.log')
@{chat_launcher_pid=$child.Id;owner_pid=$owner.Id;candidate=$candidate;db=$env:PSU_KNOWLEDGE_DB;ports=@(8098,8099)} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $out 'fixture_processes.json') -Encoding UTF8
Write-Host 'Started isolated fixture chat 8098 and owner editor 8099.'
