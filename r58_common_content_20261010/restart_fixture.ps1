$ErrorActionPreference='Stop'
& (Join-Path $PSScriptRoot 'stop_fixture.ps1')
$stamp=Get-Date -Format 'yyyyMMdd_HHmmss_ffff'
foreach($name in @('fixture_processes.json','fixture_chat_start.out.log','fixture_chat_start.err.log','fixture_owner_start.out.log','fixture_owner_start.err.log')){
    $p=Join-Path $PSScriptRoot $name
    if(Test-Path -LiteralPath $p){Move-Item -LiteralPath $p -Destination (Join-Path $PSScriptRoot ($stamp+'_'+$name))}
}
& (Join-Path $PSScriptRoot 'start_fixture.ps1')
