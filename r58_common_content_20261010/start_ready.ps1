$ErrorActionPreference='Stop'
& (Join-Path $PSScriptRoot 'stop_fixture.ps1')
$package=Join-Path $PSScriptRoot 'ready_package\PSU_Esports_Chatbot_Local'
Remove-Item Env:PSU_KNOWLEDGE_DB -ErrorAction SilentlyContinue
Remove-Item Env:PSU_COMMON_ALLOW_DEMO -ErrorAction SilentlyContinue
$env:PYTHONIOENCODING='utf-8'
& (Join-Path $package 'Open-Owner-Content.ps1') -Port 8097 -NoBrowser
$launcher=Join-Path $package 'Open-PSU-Esports-Background.ps1'
$child=Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$launcher+'"'),'-NoBrowser','-Port','8098') -WorkingDirectory $package -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $PSScriptRoot 'ready_start.out.log') -RedirectStandardError (Join-Path $PSScriptRoot 'ready_start.err.log')
@{launcher_pid=$child.Id;package=$package;db=(Join-Path $package 'data\knowledge\approved.sqlite');chat_port=8098;owner_port=8097} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'ready_processes.json') -Encoding UTF8
Write-Host 'Started production-mode package; migration drafts remain unpublished; prior user services preserved.'
