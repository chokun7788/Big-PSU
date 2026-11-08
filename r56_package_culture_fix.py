import json,shutil,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());READY=BASE.parents[1]/'PSU_Esports_Share_R56_20261010';rows=[]
helper='''# Stored process timestamps are ISO Gregorian UTC, independent of Windows culture.
function Get-RecordedProcessUtc($Recorded) {
    if ($Recorded -is [datetime]) { return $Recorded.ToUniversalTime() }
    if ($Recorded -is [datetimeoffset]) { return $Recorded.UtcDateTime }
    return [datetime]::ParseExact([string]$Recorded, 'o', [Globalization.CultureInfo]::InvariantCulture, [Globalization.DateTimeStyles]::RoundtripKind).ToUniversalTime()
}
'''
for variant in ('01_Download_Models','02_With_Models'):
 d=READY/variant;(d/'Runtime-Process-Identity.ps1').write_text(helper,encoding='utf-8-sig')
 for name in ('Start-Chatbot.ps1','Stop-Chatbot.ps1'):
  p=d/name;backup=OUT/(variant+'_'+name+'.before_culture_fix');shutil.copy2(p,backup);t=p.read_text(encoding='utf-8-sig');old='[datetime]::Parse($Item.started_utc).ToUniversalTime()';assert old in t;t=t.replace(old,'Get-RecordedProcessUtc $Item.started_utc',1);needle="$ErrorActionPreference = 'Stop'";assert needle in t;t=t.replace(needle,needle+"\n. (Join-Path $PSScriptRoot 'Runtime-Process-Identity.ps1')",1);p.write_text(t,encoding='utf-8-sig')
  rows.append(dict(variant=variant,file=name,before_sha256=hashlib.sha256(backup.read_bytes()).hexdigest(),after_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
with (OUT/'package_culture_fix.json').open('x',encoding='utf-8') as f:json.dump(rows,f,indent=2)
print('ISO process ownership date parsing fixed; time/path checks retained')
