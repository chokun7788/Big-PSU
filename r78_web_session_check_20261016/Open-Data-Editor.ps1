param([switch]$NoBrowser)
$ErrorActionPreference='Stop'
& (Join-Path (Split-Path -Parent $PSScriptRoot) 'PSU_Esports_Chat_Current_R134\Open-Data-Editor.ps1') -NoBrowser:$NoBrowser
