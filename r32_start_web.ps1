param([int]$Port = 8091, [string]$PackageRoot = 'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\owner_local_delivery_20261001_competition_content_speed_r26_final\PSU_Esports_Chatbot_Local')
$ErrorActionPreference = 'Stop'
$package = (Resolve-Path -LiteralPath $PackageRoot).Path
$runName = 'r32_ready_' + $Port + '_' + [guid]::NewGuid().ToString('N').Substring(0, 10)
$logRoot = Join-Path $PSScriptRoot 'web_chat_runs'
New-Item -ItemType Directory -Force -Path $logRoot | Out-Null
$launcher = Join-Path $package 'Start-PSU-Esports-Chatbot.ps1'
$env:PYTHONDONTWRITEBYTECODE='1'
$process = Start-Process -FilePath (Get-Process -Id $PID).Path -ArgumentList @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', ('"' + $launcher + '"'), '-Port', $Port) -WorkingDirectory $package -WindowStyle Hidden -RedirectStandardOutput (Join-Path $logRoot ($runName + '.out.log')) -RedirectStandardError (Join-Path $logRoot ($runName + '.err.log')) -PassThru
$record = @{ port=$Port; pid=$process.Id; package=$package; launcher=$launcher; stdout=(Join-Path $logRoot ($runName + '.out.log')); stderr=(Join-Path $logRoot ($runName + '.err.log')) }
$record | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $logRoot ($runName + '.json')) -Encoding UTF8
$record | ConvertTo-Json -Compress
