@echo off
setlocal
"C:\Users\Chokhun\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -B -X utf8 "%~dp0start_candidate.py"
if errorlevel 1 pause
