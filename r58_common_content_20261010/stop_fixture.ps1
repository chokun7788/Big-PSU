$ErrorActionPreference='Stop'
$meta=Get-Content -LiteralPath (Join-Path $PSScriptRoot 'fixture_processes.json') -Raw | ConvertFrom-Json
$all=@(Get-CimInstance Win32_Process)
$root=$all | Where-Object ProcessId -eq $meta.chat_launcher_pid
if($root){
    if(-not $root.CommandLine.Contains((Join-Path $meta.candidate 'Open-PSU-Esports-Chatbot.ps1'))){throw 'Fixture chat process identity mismatch'}
    $ids=[System.Collections.Generic.HashSet[int]]::new();[void]$ids.Add([int]$root.ProcessId)
    do{$count=$ids.Count;foreach($p in $all){if($ids.Contains([int]$p.ParentProcessId)){[void]$ids.Add([int]$p.ProcessId)}}}while($ids.Count -gt $count)
    foreach($p in $all | Where-Object {$ids.Contains([int]$_.ProcessId) -and $_.ProcessId -ne $root.ProcessId}){Stop-Process -Id $p.ProcessId -Force -ErrorAction SilentlyContinue}
    Stop-Process -Id $root.ProcessId -Force -ErrorAction SilentlyContinue
}
$owner=$all | Where-Object ProcessId -eq $meta.owner_pid
if($owner){
    if(-not $owner.CommandLine.Contains('app.knowledge.common.owner_server') -or -not $owner.CommandLine.Contains($meta.db)){throw 'Fixture owner process identity mismatch'}
    Stop-Process -Id $owner.ProcessId -Force -ErrorAction SilentlyContinue
}
Write-Host 'Stopped only owned fixture servers; preserved all fixture data and logs.'
