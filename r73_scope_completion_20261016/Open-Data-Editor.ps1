$ErrorActionPreference = 'Stop'
$taskPython = Join-Path (Split-Path -Parent $PSScriptRoot) 'PSU_Esports_Chat_New_R69\runtime\python\python.exe'
$taskOldPythonPath = $env:PYTHONPATH
$env:PYTHONPATH = Join-Path $PSScriptRoot 'system'
try {
    & $taskPython -B -m app.knowledge.common.owner_server --db (Join-Path $PSScriptRoot 'system\data\knowledge\common.sqlite') --port 8106
    if ($LASTEXITCODE -ne 0) { throw 'The data editor could not start. Check that port 8106 is free.' }
} finally { $env:PYTHONPATH = $taskOldPythonPath }
