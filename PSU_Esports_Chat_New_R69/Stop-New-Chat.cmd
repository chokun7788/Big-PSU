@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Stop-New-Chat.ps1"
if errorlevel 1 pause
