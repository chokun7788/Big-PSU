@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0open_review.ps1" %*
pause
