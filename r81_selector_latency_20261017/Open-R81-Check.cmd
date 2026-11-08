@echo off
setlocal
set "PYTHONUTF8=1"
set "PYTHONDONTWRITEBYTECODE=1"
set "taskPython=%~dp0..\PSU_Esports_Chat_New_R69\runtime\python\python.exe"
if not exist "%taskPython%" (
  echo Required bundled Python runtime is missing.
  pause
  exit /b 1
)
echo Checking R78 with R81 changes. No configuration will be changed.
"%taskPython%" -B "%~dp0check_live.py"
echo.
echo Keep the generated results folder for review.
pause
endlocal
