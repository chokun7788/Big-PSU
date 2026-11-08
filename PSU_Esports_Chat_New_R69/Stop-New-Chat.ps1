$ErrorActionPreference = 'Stop'
$taskRunFile = Join-Path $PSScriptRoot 'runtime\chat-process.json'
if (-not (Test-Path -LiteralPath $taskRunFile)) { Write-Output 'No new chat process has been recorded.'; exit 0 }
$taskRecord = Get-Content -LiteralPath $taskRunFile -Raw | ConvertFrom-Json
$taskUri = [Uri]$taskRecord.url
if ($taskUri.Host -ne '127.0.0.1' -or $taskUri.Scheme -ne 'http') { throw 'Invalid local launcher record.' }
$taskHealth = $null
try { $taskHealth = Invoke-RestMethod -Uri ($taskRecord.url + 'health') -TimeoutSec 2 } catch {}
if (-not $taskHealth) {
    $taskRecordedProcess = Get-Process -Id $taskRecord.pid -ErrorAction SilentlyContinue
    if ($taskRecordedProcess -and $taskRecordedProcess.StartTime.ToUniversalTime().ToString('o') -eq $taskRecord.started_utc) {
        throw 'The recorded process is still alive, but its local connection could not be checked. Shutdown has not been confirmed.'
    }
    Write-Output 'The recorded new chat process has ended.'
    exit 0
}
if ($taskHealth.runtime.installation_id -ne $taskRecord.installation_id -or $taskHealth.runtime.knowledge_profile -ne 'r69-migration-preview' -or $taskHealth.runtime.python.pid -ne $taskRecord.pid) { throw 'The port is now used by another process; it was left running.' }
Invoke-RestMethod -Uri ($taskRecord.url + 'api/shutdown') -Method Post -Headers @{'X-PSU-Launch-Token'=$taskRecord.token} -ContentType 'application/json' -Body '{}' -TimeoutSec 4 | Out-Null
Write-Output 'The new chat is stopping. Existing chat installations were not changed.'
