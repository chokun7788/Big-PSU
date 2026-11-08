$ErrorActionPreference='Stop'
$demoPython=Join-Path (Split-Path -Parent $PSScriptRoot) 'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/runtime/python/python.exe'
$demoSessionPath=Join-Path $PSScriptRoot 'demo-owner-session.json'
$demoScript=Join-Path $PSScriptRoot 'demo_owner_server.py'
if(Test-Path -LiteralPath $demoSessionPath){
    $demoSession=Get-Content -LiteralPath $demoSessionPath -Raw|ConvertFrom-Json
    $demoProcess=Get-CimInstance Win32_Process -Filter ('ProcessId='+$demoSession.pid)
    if($demoProcess -and $demoProcess.CommandLine.Contains($demoScript)){Start-Process $demoSession.url;return}
}
$demoLogId=Get-Date -Format 'yyyyMMdd_HHmmss_ffff'
Start-Process -FilePath $demoPython -ArgumentList @('-B',('"'+$demoScript+'"')) -WorkingDirectory $PSScriptRoot -WindowStyle Hidden -RedirectStandardOutput (Join-Path $PSScriptRoot ($demoLogId+'.demo.out.log')) -RedirectStandardError (Join-Path $PSScriptRoot ($demoLogId+'.demo.err.log'))
Write-Host 'Opened DEMO ONLY. This cannot edit the production database.'
