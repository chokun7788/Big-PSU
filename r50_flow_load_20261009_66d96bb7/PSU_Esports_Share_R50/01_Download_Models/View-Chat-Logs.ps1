$ErrorActionPreference = 'Stop'
$package = Join-Path $PSScriptRoot 'system\PSU_Esports_Chatbot_Local'
$python = Join-Path $PSScriptRoot 'runtime\python\python.exe'
$database = Join-Path $package 'data\logs\chat_history.sqlite3'
if (-not (Test-Path -LiteralPath $database)) { throw 'No chat history yet. Open the Chatbot and ask a question first.' }
$output = Join-Path $package ('data\logs\chat_history_report_' + (Get-Date -Format 'yyyyMMdd_HHmmss_fff') + '.html')
& $python (Join-Path $package 'tools\export_local_chat_logs.py') --database $database --output $output
if ($LASTEXITCODE -ne 0) { throw 'Could not export chat history.' }
Start-Process $output
