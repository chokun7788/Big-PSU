$ErrorActionPreference='Stop'
$r26ReportPath=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r26_report_path.txt') -Raw).Trim()
$tasks=@(
 @{Id=1732;Port=8090;Package='owner_local_delivery_20261001_competition_content_speed_r26_final_ui'},
 @{Id=39832;Port=8092;Package='owner_local_delivery_20261001_competition_content_speed_r26_final'}
)
$verified=@()
foreach($task in $tasks) {
 $process=Get-CimInstance Win32_Process -Filter ('ProcessId='+$task.Id)
 if($null -eq $process -or $process.CommandLine -notlike ('*\'+$task.Package+'\PSU_Esports_Chatbot_Local\Start-PSU-Esports-Chatbot.ps1*') -or $process.CommandLine -notmatch ('\-Port\s+'+$task.Port+'(?:\s|$)')) {throw ('Task launcher no longer matches: '+$task.Id)}
 $verified+=@{pid=$task.Id;commandLine=$process.CommandLine;port=$task.Port}
}
foreach($task in $tasks) {[System.Diagnostics.Process]::GetProcessById($task.Id).Kill($true)}
$verified | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $r26ReportPath 'verified_replaced_r26_launchers.json') -Encoding UTF8
& (Join-Path $PSScriptRoot 'r26_start_web.ps1') -Port 8090 -PackageRoot 'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261001_competition_content_speed_r26_ready\PSU_Esports_Chatbot_Local'
