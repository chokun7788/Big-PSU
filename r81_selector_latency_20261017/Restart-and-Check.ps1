$ErrorActionPreference = 'Stop'
$taskChatRoot = Join-Path (Split-Path -Parent $PSScriptRoot) 'r78_web_session_check_20261016'
$taskPython = Join-Path (Split-Path -Parent $PSScriptRoot) 'PSU_Esports_Chat_New_R69\runtime\python\python.exe'
$taskStop = Join-Path $taskChatRoot 'Stop-New-Chat.ps1'
$taskStart = Join-Path $taskChatRoot 'Start-New-Chat.ps1'
# The existing stop script verifies installation identity, PID and launch token.
# It never force-kills a process whose ownership cannot be established.
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $taskStop
if ($LASTEXITCODE -ne 0) { throw 'R78 shutdown could not be verified. No other process will be stopped.' }
$taskEnded = $false
for ($taskAttempt = 0; $taskAttempt -lt 20; $taskAttempt++) {
    try { $null = Invoke-RestMethod -Uri 'http://127.0.0.1:8115/health' -TimeoutSec 1 }
    catch { $taskEnded = $true; break }
    Start-Sleep -Milliseconds 500
}
if (-not $taskEnded) { throw 'The previous endpoint is still responding. Restart stopped; no force termination was used.' }
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $taskStart
if ($LASTEXITCODE -ne 0) { throw 'R78 startup did not pass its connection check. Review the existing launcher logs.' }
& $taskPython -B (Join-Path $PSScriptRoot 'check_live.py')
if ($LASTEXITCODE -ne 0) { throw 'The targeted checker stopped. Keep the results for review.' }
