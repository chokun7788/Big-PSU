@echo off
setlocal
set "PYTHONUTF8=1"
set "PYTHONDONTWRITEBYTECODE=1"
set "taskPython=%~dp0..\PSU_Esports_Chat_New_R69\runtime\python\python.exe"
if not exist "%taskPython%" (
  echo Required runtime is missing: PSU_Esports_Chat_New_R69
  pause
  exit /b 1
)
"%taskPython%" -B "%~dp0check_connection.py"
echo.
echo Keep the generated results folder so the results can be reviewed.
pause
endlocal
