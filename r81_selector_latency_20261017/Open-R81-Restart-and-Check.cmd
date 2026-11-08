@echo off
setlocal
set "PYTHONUTF8=1"
set "PYTHONDONTWRITEBYTECODE=1"
echo Restarting only the recorded R78 chat, then running a small related check.
echo Keep the Ollama window running. Existing logs will be retained.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Restart-and-Check.ps1"
if errorlevel 1 echo Restart or check stopped. Keep this output for review.
pause
endlocal
