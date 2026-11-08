$ErrorActionPreference = 'Stop'
$taskRuntime = Join-Path $PSScriptRoot '..\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\python.exe'
if (-not (Test-Path -LiteralPath $taskRuntime)) { throw 'Bundled Python was not found. Keep this folder beside r58_common_content_20261010.' }
$taskOldPythonPath = $env:PYTHONPATH
$taskOldLlmFlag = $env:PSU_LOCAL_LLM_ASSIST_ENABLED
$env:PYTHONPATH = Join-Path $PSScriptRoot 'system'
$env:PSU_LOCAL_LLM_ASSIST_ENABLED = '1'
try {
    & $taskRuntime -B -m app.knowledge.common.owner_server --db (Join-Path $PSScriptRoot 'common.sqlite') --port 8099
    if ($LASTEXITCODE -ne 0) { throw 'Draft editor could not start. Check that port 8099 is free and read the error above.' }
} finally {
    $env:PYTHONPATH = $taskOldPythonPath
    $env:PSU_LOCAL_LLM_ASSIST_ENABLED = $taskOldLlmFlag
}
