param([string]$Label='package_smoke7')
$ErrorActionPreference='Stop'
$out=Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r56_current_path.txt')
$root='C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_R56_20261010\02_With_Models'
try { $old=Invoke-RestMethod http://127.0.0.1:8096/health -TimeoutSec 2; throw 'Port 8096 already has a service; refusing to reuse' } catch { if($_.Exception.Message -like 'Port 8096*'){throw} }
$process=Start-Process -FilePath powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$root+'\Start-Chatbot.ps1"'),'-Port','8096','-NoBrowser','-ForceBundledOllama') -WindowStyle Hidden -RedirectStandardOutput (Join-Path $out ($Label+'_stdout.txt')) -RedirectStandardError (Join-Path $out ($Label+'_stderr.txt')) -PassThru
$record=[ordered]@{root=$root;port=8096;launcher_pid=$process.Id;meaning='Actual launch on developer Windows, not clean-machine certification'}
$deadline=(Get-Date).AddMinutes(4)
do {
    Start-Sleep -Seconds 2
    try {$health=Invoke-RestMethod http://127.0.0.1:8096/health -TimeoutSec 3} catch {$health=$null}
    if($health){break}
    if($process.HasExited){throw 'Portable launcher exited before health became available'}
} while((Get-Date) -lt $deadline)
if(-not $health){throw 'Portable health deadline expired'}
if($health.runtime.version -ne '2026.10.10-service-r56.7'){throw 'Portable version mismatch'}
$record.health=$health
$record | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $out ($Label+'_health.json')) -Encoding utf8
Write-Output ('PORTABLE_READY '+$health.runtime.version)
