$ErrorActionPreference='Stop'
$taskPythonDir='C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python'
if (-not (Test-Path -LiteralPath (Join-Path $taskPythonDir 'python.exe'))) {throw 'The verified local Python runtime is missing. This launcher is for this computer.'}
$env:Path=$taskPythonDir+';'+$env:Path
& 'C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r42_domain_resume_20261006_152553_b21f30\release_r42_4\PSU_Esports_Chatbot_Local\Open-PSU-Esports-Background.ps1'
