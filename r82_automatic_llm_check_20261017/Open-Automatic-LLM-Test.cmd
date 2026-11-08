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
echo Automatic local LLM and R78 chatbot check.
echo This will check/start local services and run the related Thai/English cases.
echo Existing data and logs will be retained. No model downloads.
"%taskPython%" -B "%~dp0auto_test.py"
if errorlevel 1 echo Review RESULTS.json: a service, selector or answer check needs attention.
pause
endlocal
