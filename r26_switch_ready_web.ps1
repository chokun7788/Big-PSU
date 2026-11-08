$ErrorActionPreference='Stop'
$r26ReportPath=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r26_report_path.txt') -Raw).Trim()
$expectedOldLauncher='C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261001_competition_format_r25_final\PSU_Esports_Chatbot_Local\Start-PSU-Esports-Chatbot.ps1'
$oldLauncher=Get-CimInstance Win32_Process -Filter 'ProcessId=10716'
if ($null -eq $oldLauncher -or $oldLauncher.CommandLine -notlike ('*'+$expectedOldLauncher+'*') -or $oldLauncher.CommandLine -notmatch '\-Port\s+8090(?:\s|$)') { throw 'Old launcher no longer matches this task; leave it untouched.' }
$saved=@{pid=10716;commandLine=$oldLauncher.CommandLine;reason='replace this task r25 demo with verified r26 package'}
[System.Diagnostics.Process]::GetProcessById(10716).Kill($true)
$saved | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $r26ReportPath 'verified_replaced_r25_launcher.json') -Encoding UTF8
& (Join-Path $PSScriptRoot 'r26_start_web.ps1') -Port 8090 -PackageRoot 'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261001_competition_content_speed_r26_final_ui\PSU_Esports_Chatbot_Local'
