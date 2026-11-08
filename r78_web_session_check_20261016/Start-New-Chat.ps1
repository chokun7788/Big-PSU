param([int]$Port=8115,[switch]$NoBrowser)
$ErrorActionPreference='Stop'
& (Join-Path (Split-Path -Parent $PSScriptRoot) 'PSU_Esports_Chat_Current_R134\Start-New-Chat.ps1') -Port $Port -NoBrowser:$NoBrowser
