@echo off
setlocal
set "PYTHONUTF8=1"
set "PYTHONDONTWRITEBYTECODE=1"
set "taskPython=%~dp0..\PSU_Esports_Chat_New_R69\runtime\python\python.exe"
if not exist "%taskPython%" (
  echo Bundled Python runtime is missing.
  pause
  exit /b 1
)
echo Focused R83 common-format check: 24 messages with LLM ON.
echo Full corpus testing is on hold until the user requests it.
"%taskPython%" -B "%~dp0web_focused.py"
if errorlevel 1 echo A focused check needs attention. Review the new web_results folder.
pause
endlocal
