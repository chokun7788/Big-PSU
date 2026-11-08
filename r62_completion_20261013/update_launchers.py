from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
def write(name,text): (ROOT/name).write_text(text,encoding='utf-8')
p=ROOT/'Start-PSU-Esports-Chatbot.ps1';s=p.read_text(encoding='utf-8-sig')
a=s.index('try {\n    $models');z=s.index('$env:PSU_RUNTIME_PROFILE',a)
s=s[:a]+". (Join-Path $projectRoot 'Portable-Models.ps1')\nAssert-PSUModels $projectRoot\n\n"+s[z:]
write(p.name,s)
p=ROOT/'Open-PSU-Esports-Chatbot.ps1';s=p.read_text(encoding='utf-8-sig')
a=s.index('function Test-OllamaReady');z=s.index('& (Join-Path $projectRoot "Start-PSU-',a)
s=s[:a]+". (Join-Path $projectRoot 'Portable-Models.ps1')\nAssert-PSUModels $projectRoot -DownloadMissing\n\n"+s[z:]
write(p.name,s)
write('Setup-Local-Models.ps1',"""$ErrorActionPreference='Stop'
$projectRoot=$PSScriptRoot
. (Join-Path $projectRoot 'Portable-Models.ps1')
Initialize-PSUModels $projectRoot
Write-Host 'Downloading models into this package. Internet is needed only for setup and live booking.'
& $script:PSUOllamaExe pull 'scb10x/typhoon2.5-qwen3-4b'
if ($LASTEXITCODE -ne 0) { throw 'Typhoon download failed. Retry Setup-Local-Models.cmd.' }
& $script:PSUOllamaExe pull 'bge-m3'
if ($LASTEXITCODE -ne 0) { throw 'BGE-M3 download failed. Retry Setup-Local-Models.cmd.' }
& $script:PSUOllamaExe create 'psu-bge-m3:q8_0' -f (Join-Path $projectRoot 'models\Modelfile.bge-m3-1024')
if ($LASTEXITCODE -ne 0) { throw 'Creating embedding profile failed.' }
Write-Host 'Setup complete. Open Open-PSU-Esports-Background.cmd or Open-Owner-Content.cmd.'
""")
p=ROOT/'Open-Owner-Content.ps1';s=p.read_text(encoding='utf-8-sig')
s=s.replace("$python=Get-ChatbotPython $packageRoot $PythonPath","$python=Get-ChatbotPython $packageRoot $PythonPath\n. (Join-Path $packageRoot 'Portable-Models.ps1')\nAssert-PSUModels $packageRoot -DownloadMissing\n$env:PSU_LOCAL_LLM_ASSIST_ENABLED='1'\n$expectedBuild=(& $python.Path -B -c \"from app.knowledge.common.build_info import LOADED_BUILD;print(LOADED_BUILD['loaded_source_sha256'])\").Trim()",1)
# PowerShell 5.1 strips nested double quotes; the Python literal is single quoted.
s=s.replace("if(-not $NoBrowser){Start-Process $existing.url}\n        Write-Host", """$token=($existing.url -split '#token=')[1]
        try { $status=Invoke-RestMethod ("http://127.0.0.1:"+$existing.port+'/api/status') -Headers @{Authorization=('Bearer '+$token)} -TimeoutSec 3 } catch { $status=$null }
        if($status -and $status.build.loaded_source_sha256 -eq $expectedBuild) {
        if(-not $NoBrowser){Start-Process $existing.url}
        Write-Host""",1)
s=s.replace("return\n    }\n}", "return\n        }\n    }\n}",1)
insert="""# Preserve other processes and select a free local owner port.
foreach($candidate in $Port..($Port+9)){
    $listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$candidate)
    try{$listener.Start();$Port=$candidate;break}catch{}finally{$listener.Stop()}
}
"""
s=s.replace("$runId=Get-Date",insert+"$runId=Get-Date",1)
write(p.name,s)
p=ROOT/'Open-PSU-Esports-Background.ps1';s=p.read_text(encoding='utf-8-sig')
s=s.replace("$python = Get-ChatbotPython $packageRoot $PythonPath","$python = Get-ChatbotPython $packageRoot $PythonPath\n$env:PSU_EXPECTED_SOURCE_SHA256=(& $python.Path -B -c \"from app.knowledge.common.build_info import LOADED_BUILD;print(LOADED_BUILD['loaded_source_sha256'])\").Trim()",1)
s=s.replace("$Health.runtime.installation_id -eq $expectedInstallation)", "$Health.runtime.installation_id -eq $expectedInstallation -and $Health.common_loaded_build.loaded_source_sha256 -eq $env:PSU_EXPECTED_SOURCE_SHA256)",1)
write(p.name,s)
p=ROOT/'Runtime-Readiness.ps1';s=p.read_text(encoding='utf-8-sig')
s=s.replace("$reasons = @()\n    if ($Health.ok", "$reasons = @()\n    if ($env:PSU_EXPECTED_SOURCE_SHA256 -and $Health.common_loaded_build.loaded_source_sha256 -ne $env:PSU_EXPECTED_SOURCE_SHA256) { $reasons += 'loaded_source_stale' }\n    if ($Health.ok",1)
write(p.name,s)
p=ROOT/'app/knowledge/common/build_info.py'
write(str(p.relative_to(ROOT)),'''"""Fingerprint captured at module import; excludes databases, logs and tokens."""
from pathlib import Path
import hashlib
def _capture():
 root=Path(__file__).resolve().parents[3];digest=hashlib.sha256()
 files=[]
 for folder in ('app','web_chat'):
  files.extend(p for p in (root/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix in {'.py','.json','.js','.html','.css'})
 files.extend(root.glob('*.ps1'))
 for p in sorted(files):
  digest.update(p.relative_to(root).as_posix().encode());digest.update(p.read_bytes())
 return {'build_id':'common-r62','loaded_source_sha256':digest.hexdigest(),'fingerprint_scope':'application, web UI and launchers at module import'}
LOADED_BUILD=_capture()
''')
manifest=json.loads((ROOT/'package_manifest.json').read_text(encoding='utf-8-sig'))
manifest['runtime_version']='2026.10.13-common-r62'
manifest['python_runtime']={'path':'runtime/python/python.exe','minimum_version':'3.12','bits':64}
manifest['local_runtime_features']+=['owner_unique_record_ids','draft_preview','published_legacy_game_union','historical_name_authority','typed_common_dialogue','package_model_service']
write('package_manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Updated launchers and loaded-source identity.')
