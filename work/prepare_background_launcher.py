from pathlib import Path


project = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")


def replace_once(relative: str, old: str, new: str) -> None:
    path = project / relative
    content = path.read_text(encoding="utf-8")
    if content.count(old) != 1:
        raise RuntimeError(f"Expected one matching block in {path}, got {content.count(old)}")
    path.write_text(content.replace(old, new), encoding="utf-8")


replace_once(
    "booking_dashboard/server.py",
    '''        if path in ("/api/center-schedule", "/api/center-schedule/"):
            send_json(self, {"ok": True, "schedule": load_center_schedule(), "admin_pin_hint": "default 1234; set PSU_ADMIN_PIN before hosting"})
            return
''',
    '''        if path == "/health":
            send_json(self, {"ok": True, "service": "psu-booking-dashboard", "calendar_contract": "lunch-closed-v1"})
            return

        if path in ("/api/center-schedule", "/api/center-schedule/"):
            send_json(self, {"ok": True, "schedule": load_center_schedule(), "admin_pin_hint": "default 1234; set PSU_ADMIN_PIN before hosting"})
            return
''',
)

replace_once(
    "deployment_templates/Start-PSU-Esports-Chatbot.ps1",
    '''$env:PSU_RUNTIME_VERSION = "2026.09.25-owner-review-candidate"''',
    '''$env:PSU_RUNTIME_VERSION = "2026.09.26-owner-review-candidate"''',
)
replace_once(
    "deployment_templates/Start-PSU-Esports-Chatbot.ps1",
    '''function Test-BookingDashboard {
    try {
        (Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:8091/" -TimeoutSec 2).StatusCode -eq 200
    } catch {
        $false
    }
}

if ((Test-Path $bookingDashboardRoot) -and -not (Test-BookingDashboard)) {
    $bookingLogDir = Join-Path $projectRoot "data\\logs"
    New-Item -ItemType Directory -Force -Path $bookingLogDir | Out-Null
    Start-Process -FilePath $python.Source -ArgumentList @("server.py", "--no-browser", "--port", "8091") `
        -WorkingDirectory $bookingDashboardRoot -WindowStyle Hidden `
        -RedirectStandardOutput (Join-Path $bookingLogDir "booking_dashboard_8091.out.log") `
        -RedirectStandardError (Join-Path $bookingLogDir "booking_dashboard_8091.err.log")
    for ($attempt = 1; $attempt -le 10 -and -not (Test-BookingDashboard); $attempt++) {
        Start-Sleep -Milliseconds 500
    }
}
''',
    '''function Test-BookingDashboard {
    try {
        $health = Invoke-RestMethod -Uri "http://127.0.0.1:8091/health" -TimeoutSec 2
        return $health.ok -eq $true -and $health.service -eq "psu-booking-dashboard" -and $health.calendar_contract -eq "lunch-closed-v1"
    } catch {
        return $false
    }
}

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

if ((Test-Path $bookingDashboardRoot) -and -not (Test-BookingDashboard)) {
    if (Test-LocalPortInUse 8091) {
        throw "Port 8091 is used by another service or an older Dashboard. Stop that process before starting this package."
    }
    $bookingLogDir = Join-Path $projectRoot "data\\logs"
    New-Item -ItemType Directory -Force -Path $bookingLogDir | Out-Null
    $runId = (Get-Date -Format "yyyyMMdd_HHmmss_fff") + "_" + [guid]::NewGuid().ToString("N").Substring(0, 8)
    Start-Process -FilePath $python.Source -ArgumentList @("server.py", "--no-browser", "--port", "8091") `
        -WorkingDirectory $bookingDashboardRoot -WindowStyle Hidden `
        -RedirectStandardOutput (Join-Path $bookingLogDir "booking_dashboard_8091_$runId.out.log") `
        -RedirectStandardError (Join-Path $bookingLogDir "booking_dashboard_8091_$runId.err.log")
    for ($attempt = 1; $attempt -le 10 -and -not (Test-BookingDashboard); $attempt++) {
        Start-Sleep -Milliseconds 500
    }
    if (-not (Test-BookingDashboard)) {
        throw "Dashboard did not become ready on port 8091. Check the new booking_dashboard_8091 log files."
    }
}
''',
)
replace_once(
    "deployment_templates/Start-PSU-Esports-Chatbot.ps1",
    '''Write-Host $(if ($env:PSU_LIVE_BOOKING_ENABLED -eq "1") { "Live booking status: ready (Dashboard on port 8091)" } else { "Live booking status: unavailable; static schedule remains available" })''',
    '''Write-Host $(if ($env:PSU_LIVE_BOOKING_ENABLED -eq "1") { "Dashboard connection: ready on port 8091; live CSV data is checked for each question" } else { "Dashboard connection: unavailable; live availability cannot be confirmed" })''',
)

background_ps1 = project / "deployment_templates" / "Open-PSU-Esports-Background.ps1"
if background_ps1.exists():
    raise RuntimeError(f"Will not overwrite {background_ps1}")
background_ps1.write_text('''$ErrorActionPreference = "Stop"
$packageRoot = $PSScriptRoot
$chatbotUrl = "http://127.0.0.1:8080/"

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

if (Test-LocalPortInUse 8080) {
    try {
        $health = Invoke-RestMethod -Uri "http://127.0.0.1:8080/health" -TimeoutSec 2
        if ($health.service -eq "psu-esports-chat-web") {
            Write-Host "Chatbot is already running: $chatbotUrl"
            Start-Process $chatbotUrl
            return
        }
    } catch { }
    throw "Port 8080 is already in use. If the original start-dashboard.bat is running, close it; this package serves its Dashboard at http://127.0.0.1:8091/."
}

$logs = Join-Path $packageRoot "data\\logs\\launcher"
New-Item -ItemType Directory -Force -Path $logs | Out-Null
$runId = (Get-Date -Format "yyyyMMdd_HHmmss_fff") + "_" + [guid]::NewGuid().ToString("N").Substring(0, 8)
$scriptPath = Join-Path $packageRoot "Open-PSU-Esports-Chatbot.ps1"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Missing package launcher: $scriptPath"
}
$child = Start-Process -FilePath "PowerShell.exe" `
    -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ('"' + $scriptPath + '"')) `
    -WorkingDirectory $packageRoot -WindowStyle Hidden -PassThru `
    -RedirectStandardOutput (Join-Path $logs "chatbot_$runId.out.log") `
    -RedirectStandardError (Join-Path $logs "chatbot_$runId.err.log")
Write-Host "Starting Chatbot in the background (process $($child.Id))."
Write-Host "Chatbot: $chatbotUrl"
Write-Host "Dashboard: http://127.0.0.1:8091/"
Write-Host "Startup logs: $logs"
Write-Host "The window can now close. The computer must remain on for local answers."
''', encoding="utf-8")

background_cmd = project / "deployment_templates" / "Open-PSU-Esports-Background.cmd"
if background_cmd.exists():
    raise RuntimeError(f"Will not overwrite {background_cmd}")
background_cmd.write_text('''@echo off
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Open-PSU-Esports-Background.ps1"
if errorlevel 1 pause
''', encoding="utf-8")

replace_once(
    "tools/build_owner_local_package.ps1",
    '''    "Open-PSU-Esports-Chatbot.cmd",
''',
    '''    "Open-PSU-Esports-Chatbot.cmd",
    "Open-PSU-Esports-Background.ps1",
    "Open-PSU-Esports-Background.cmd",
''',
)
replace_once(
    "tools/build_owner_local_package.ps1",
    '''    runtime_version = "2026.09.25-owner-review-candidate"''',
    '''    runtime_version = "2026.09.26-owner-review-candidate"''',
)
print("Added Dashboard health contract, preserved startup logs, and prepared background launcher.")
