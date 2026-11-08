$ErrorActionPreference = 'Stop'
$questionnaireRoot = $PSScriptRoot
$questionnairePython = Join-Path (Split-Path $questionnaireRoot -Parent) 'PSU_Esports_Chat_New_R69\runtime\python\python.exe'
$questionnaireSession = Join-Path $questionnaireRoot 'session.json'
if (Test-Path -LiteralPath $questionnaireSession) {
    try {
        $questionnaireSaved = Get-Content -LiteralPath $questionnaireSession -Raw | ConvertFrom-Json
        $questionnaireHealth = Invoke-RestMethod -Uri ($questionnaireSaved.url + 'api/health') -TimeoutSec 2
        if ($questionnaireHealth.app -eq 'psu-owner-questions-r107') { Start-Process $questionnaireSaved.url; exit 0 }
    } catch { }
}
if (-not (Test-Path -LiteralPath $questionnairePython)) { throw 'Bundled Python not found. Keep this folder beside PSU_Esports_Chat_New_R69.' }
$questionnaireArgs = @('-B', '-X', 'utf8', 'server.py')
$questionnaireProcess = Start-Process -FilePath $questionnairePython -ArgumentList $questionnaireArgs -WorkingDirectory $questionnaireRoot -WindowStyle Hidden -RedirectStandardOutput (Join-Path $questionnaireRoot 'server.out.log') -RedirectStandardError (Join-Path $questionnaireRoot 'server.err.log') -PassThru
for ($questionnaireAttempt = 0; $questionnaireAttempt -lt 40; $questionnaireAttempt++) {
    Start-Sleep -Milliseconds 250
    if ($questionnaireProcess.HasExited) { throw 'Server stopped. See server.err.log.' }
    if (Test-Path -LiteralPath $questionnaireSession) {
        $questionnaireSaved = Get-Content -LiteralPath $questionnaireSession -Raw | ConvertFrom-Json
        if ($questionnaireSaved.pid -eq $questionnaireProcess.Id) { Start-Process $questionnaireSaved.url; Write-Host $questionnaireSaved.url; exit 0 }
    }
}
throw 'Server did not become ready. See server.err.log.'
