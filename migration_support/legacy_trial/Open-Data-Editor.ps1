param([switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
$destination = 'D:\CodexProjects\Big-PSU\r135_hybrid48_20261108\Open-Data-Editor.ps1'
if (-not (Test-Path -LiteralPath $destination -PathType Leaf)) { throw "Migrated launcher missing: $destination" }
& $destination @PSBoundParameters
