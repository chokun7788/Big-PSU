param([switch]$NoBrowser)
$ErrorActionPreference = "Stop"
$packageRoot = $PSScriptRoot
. (Join-Path $packageRoot "Booking-Dashboard-Probe.ps1")
$ownerDashboardAt8080 = Test-BookingDashboardIdentity -BaseUrl "http://127.0.0.1:8080"
$manifestPath = Join-Path $packageRoot 'package_manifest.json'
if (-not (Test-Path -LiteralPath $manifestPath)) { throw 'Missing package_manifest.json. Use a complete Chatbot package.' }
$expectedVersion = (Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json).runtime_version
$hasher = [System.Security.Cryptography.SHA256]::Create()
try {
    $rootBytes = [System.Text.Encoding]::UTF8.GetBytes(([System.IO.Path]::GetFullPath($packageRoot)).ToLowerInvariant())
    $expectedInstallation = ([System.BitConverter]::ToString($hasher.ComputeHash($rootBytes))).Replace('-','').ToLowerInvariant().Substring(0,16)
} finally { $hasher.Dispose() }

function Test-LocalPortInUse([int]$ListenPort) {
    $client = [System.Net.Sockets.TcpClient]::new()
    try {
        $client.Connect("127.0.0.1", $ListenPort)
        return $true
    } catch {
        return $false
    } finally {
        $client.Dispose()
    }
}

function Test-ThisPackage($Health) {
    return ($Health.service -eq 'psu-esports-chat-web' -and $Health.runtime.version -eq $expectedVersion -and $Health.runtime.installation_id -eq $expectedInstallation)
}
$chatbotPort = $null
foreach ($candidatePort in 8090..8099) {
    if (Test-LocalPortInUse $candidatePort) {
        try {
            $health = Invoke-RestMethod -Uri "http://127.0.0.1:$candidatePort/health" -TimeoutSec 1
            if (Test-ThisPackage $health) {
                $chatbotUrl = "http://127.0.0.1:$candidatePort/"
                Write-Host "This Chatbot package is already running: $chatbotUrl"
                if (-not $NoBrowser) { Start-Process $chatbotUrl }
                return
            }
        } catch { }
    } elseif ($null -eq $chatbotPort) {
        $chatbotPort = $candidatePort
    }
}
if ($null -eq $chatbotPort) { throw 'Ports 8090..8099 are in use. Close an unused Chatbot instance first.' }
$chatbotUrl = "http://127.0.0.1:$chatbotPort/"

$logs = Join-Path $packageRoot "data\logs\launcher"
New-Item -ItemType Directory -Force -Path $logs | Out-Null
$runId = (Get-Date -Format "yyyyMMdd_HHmmss_fff") + "_" + [guid]::NewGuid().ToString("N").Substring(0, 8)
$scriptPath = Join-Path $packageRoot "Open-PSU-Esports-Chatbot.ps1"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Missing package launcher: $scriptPath"
}
$child = Start-Process -FilePath "PowerShell.exe" `
    -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ('"' + $scriptPath + '"'), "-Port", "$chatbotPort", "-NoBrowser") `
    -WorkingDirectory $packageRoot -WindowStyle Hidden -PassThru `
    -RedirectStandardOutput (Join-Path $logs "chatbot_$runId.out.log") `
    -RedirectStandardError (Join-Path $logs "chatbot_$runId.err.log")
Write-Host "Starting Chatbot in the background (process $($child.Id))."
Write-Host "Chatbot: $chatbotUrl"
Write-Host "Dashboard: http://127.0.0.1:$(if ($ownerDashboardAt8080) { 8080 } else { 8091 })/"
Write-Host "Startup logs: $logs"
Write-Host "The window can now close. The computer must remain on for local answers."
for ($attempt = 0; $attempt -lt 60; $attempt++) {
    if ($child.HasExited) { throw "Chatbot stopped during startup. Read the startup logs in $logs." }
    try {
        $health = Invoke-RestMethod -Uri "http://127.0.0.1:$chatbotPort/health" -TimeoutSec 1
        if (Test-ThisPackage $health) {
            if (-not $NoBrowser) { Start-Process $chatbotUrl }
            return
        }
    } catch { }
    Start-Sleep -Seconds 1
}
throw "Chatbot did not become ready within 60 seconds. Read the startup logs in $logs."
