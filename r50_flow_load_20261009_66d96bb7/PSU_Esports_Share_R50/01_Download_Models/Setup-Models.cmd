@echo off
"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-Chatbot.ps1" -SetupOnly -NoBrowser
if errorlevel 1 pause
