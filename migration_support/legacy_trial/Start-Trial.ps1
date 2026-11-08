param([int]$Port = 8125, [switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
$destination = 'D:\CodexProjects\Big-PSU\r135_hybrid48_20261108\Start-Trial.ps1'
if (-not (Test-Path -LiteralPath $destination -PathType Leaf)) { throw "Migrated launcher missing: $destination" }
& $destination @PSBoundParameters
