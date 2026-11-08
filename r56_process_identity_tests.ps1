$ErrorActionPreference='Stop'
$out=Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r56_current_path.txt')
. 'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_R56_20261010\02_With_Models\Runtime-Process-Identity.ps1'
$prior=[Threading.Thread]::CurrentThread.CurrentCulture
$results=@()
try {
 foreach($culture in @('th-TH','en-US')) {
  [Threading.Thread]::CurrentThread.CurrentCulture=[Globalization.CultureInfo]::GetCultureInfo($culture)
  $utc=Get-RecordedProcessUtc '2026-10-10T10:05:41.8186471Z'
  if($utc.Year -ne 2026 -or $utc.Hour -ne 10 -or $utc.Kind -ne 'Utc'){throw 'ISO timestamp changed by culture'}
  $root='C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_R56_20261010\02_With_Models'
  $s=Get-Content -LiteralPath "$root\runtime\state\active.json" -Raw|ConvertFrom-Json
  foreach($item in @($s.chat,$s.ollama)) {
   $live=Get-Process -Id $item.pid; $saved=Get-RecordedProcessUtc $item.started_utc
   $delta=[math]::Abs(($live.StartTime.ToUniversalTime()-$saved).TotalSeconds)
   if($delta -gt 1){throw 'Actual owned PID failed time identity'}
   $wrong=$saved.AddSeconds(-60);if([math]::Abs(($live.StartTime.ToUniversalTime()-$wrong).TotalSeconds) -le 1){throw 'Wrong creation timestamp was accepted'}
   $results+=@{culture=$culture;pid=$item.pid;delta_sec=$delta;wrong_timestamp_rejected=$true}
  }
  $rejected=$false;try{Get-RecordedProcessUtc 'not a date' | Out-Null}catch{$rejected=$true};if(-not $rejected){throw 'Malformed timestamp accepted'}
 }
} finally { [Threading.Thread]::CurrentThread.CurrentCulture=$prior }
$results | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $out 'package_process_identity_tests.json') -Encoding utf8
Write-Output '4 live ownership checks passed across Thai/English; wrong/malformed dates rejected'
