"""Create two clean Windows deliveries without modifying the source or old logs."""
from pathlib import Path
import hashlib,json,shutil,urllib.request

W=Path(__file__).parent
OLD=Path(r'C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003')
OUT=Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_20261003')
OUT.mkdir(exist_ok=False)
original=json.loads((OLD/'ready_manifest.json').read_text(encoding='utf-8'))
blobs=[]
for item in original['files']:
    if item.get('sha256') and item['bytes']>100_000_000:
        namespace='scb10x/typhoon2.5-qwen3-4b' if item['bytes']>2_000_000_000 else 'library/bge-m3'
        blobs.append({'label':'Typhoon chat model' if item['bytes']>2_000_000_000 else 'BGE-M3 embedding model','sha256':item['sha256'],'bytes':item['bytes'],'url':f"https://registry.ollama.ai/v2/{namespace}/blobs/sha256:{item['sha256']}"})

ignore=shutil.ignore_patterns('__pycache__','*.pyc','logs','state','verification')
for variant,folder in [('download_models','01_Download_Models'),('with_models','02_With_Models')]:
    root=OUT/folder
    root.mkdir()
    print(f'Copying {folder}...',flush=True)
    shutil.copytree(OLD/'system',root/'system',ignore=ignore)
    package=root/'system'/'PSU_Esports_Chatbot_Local'
    (package/'data/logs').mkdir(parents=True)
    (package/'data/logs/.gitkeep').write_text('',encoding='utf-8')
    for part in ['python','ollama']:
        shutil.copytree(OLD/'runtime'/part,root/'runtime'/part,ignore=ignore)
    seed=root/'runtime/model_seed'
    seed.mkdir()
    seed_records=[]
    for src in (OLD/'runtime/models').rglob('*'):
        if not src.is_file() or src.stat().st_size>100_000_000: continue
        rel=src.relative_to(OLD/'runtime/models')
        dst=seed/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)
        seed_records.append({'path':rel.as_posix(),'bytes':dst.stat().st_size,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
    if variant=='with_models':
        shutil.copytree(OLD/'runtime/models',root/'runtime/models')
    else: (root/'runtime/models').mkdir()
    version='2026.10.03-share-r37.2-'+variant
    manifest={'runtime_version':version,'variant':variant,'python':original['python'],'ollama':original['ollama'],
        'models':original['models'],'model_blobs':blobs,'model_seed_files':seed_records,'startup_timeout_sec':600,
        'supported_os':'Windows 10 22H2 / Windows 11 x64','original_app_version':'r37.2'}
    (root/'ready_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (root/'tools').mkdir()
    shutil.copyfile(W/'share_ensure_models.py',root/'tools/ensure_models.py')
    start=(OLD/'Start-Chatbot.ps1').read_text(encoding='utf-8-sig')
    start=start.replace('[switch]$ForceBundledOllama)', '[switch]$ForceBundledOllama, [switch]$SetupOnly)')
    start=start.replace("$root = $PSScriptRoot", "$root = $PSScriptRoot\nif (-not [Environment]::Is64BitOperatingSystem) { throw 'This package requires Windows x64.' }\nif ([Environment]::OSVersion.Version.Build -lt 19045) { throw 'This package requires Windows 10 22H2 or Windows 11.' }")
    start=start.replace("    if ($prior -and (Test-Owned $prior.chat $appLauncher)) {", "    if ($prior -and $prior.root -eq $root -and (Test-Owned $prior.chat $appLauncher)) {")
    marker="    if ($Port -eq 0) {"
    setup='''    $bundledPython = Join-Path $root 'runtime\\python\\python.exe'
    & $bundledPython -I (Join-Path $root 'tools\\ensure_models.py')
    if ($LASTEXITCODE -ne 0) { throw 'Model setup did not complete. See the message above and try again.' }
    if ($SetupOnly) { Write-Host 'Model setup complete. Open Start-Chatbot.cmd to use the Chatbot.'; return }
'''
    start=start.replace(marker,setup+marker)
    # Every delivery runs its own bundled service. No installed Python/Ollama is used.
    start=start.replace("} elseif (-not $ForceBundledOllama -and (Test-Models 'http://127.0.0.1:11434')) {", "} elseif ($false) {")
    start=start.replace('AddSeconds(150)','AddSeconds([int]$manifest.startup_timeout_sec)')
    start=start.replace("    if ($health.llm_preflight -and $health.llm_preflight.ok -eq $false)","    if (-not $health.warmup.ok) { throw 'Chatbot warmup failed. Check the launcher logs.' }\n    if ($health.llm_preflight -and $health.llm_preflight.ok -eq $false)")
    (root/'Start-Chatbot.ps1').write_text(start,encoding='utf-8-sig')
    for name in ['Stop-Chatbot.ps1','View-Chat-Logs.ps1']:
        shutil.copyfile(OLD/name,root/name)
    for name in ['Start-Chatbot','Stop-Chatbot','View-Chat-Logs']:
        (root/(name+'.cmd')).write_text('@echo off\r\n"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -ExecutionPolicy Bypass -File "%~dp0'+name+'.ps1" %*\r\nif errorlevel 1 pause\r\n',encoding='utf-8',newline='')
    (root/'Setup-Models.cmd').write_text('@echo off\r\n"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-Chatbot.ps1" -SetupOnly -NoBrowser\r\nif errorlevel 1 pause\r\n',encoding='utf-8',newline='')
    launcher=package/'Start-PSU-Esports-Chatbot.ps1'
    text=launcher.read_text(encoding='utf-8-sig').replace(original['runtime_version'],version).replace('$env:PSU_PIPELINE_WORKER_STARTUP_TIMEOUT_SEC = "45"','$env:PSU_PIPELINE_WORKER_STARTUP_TIMEOUT_SEC = "180"')
    launcher.write_text(text,encoding='utf-8-sig')
    (root/'licenses').mkdir()
    for item in seed_records:
        if item['path'].startswith('blobs/'):
            raw=(seed/item['path']).read_bytes()
            if b'Apache License' in raw or b'MIT License' in raw:
                (root/'licenses'/Path(item['path']).name).write_bytes(raw)
    shutil.copy2(root/'runtime/python/LICENSE.txt',root/'licenses/Python_LICENSE.txt')
    with urllib.request.urlopen('https://raw.githubusercontent.com/ollama/ollama/main/LICENSE',timeout=20) as response:
        (root/'licenses/Ollama_LICENSE.txt').write_bytes(response.read())
    (root/'licenses/README.md').write_text('Runtime dependency licenses are also preserved under runtime/ollama/lib/ollama and Python/tzdata metadata.\nOllama source: https://github.com/ollama/ollama\nChat model: https://ollama.com/scb10x/typhoon2.5-qwen3-4b\nEmbedding model: https://ollama.com/library/bge-m3\n',encoding='utf-8')
    hint='เปิดครั้งแรกต้องใช้อินเทอร์เน็ตเพื่อดาวน์โหลดโมเดลประมาณ 3.65 GB อัตโนมัติ มีตัวแสดงความคืบหน้า หากขาดช่วงให้เปิดซ้ำเพื่อต่อจากไฟล์ที่เก็บไว้' if variant=='download_models' else 'โมเดลอยู่ในชุดนี้แล้ว เปิดได้โดยไม่ดาวน์โหลดโมเดล และไม่มีการดาวน์โหลดแบบเงียบเมื่อไฟล์โมเดลหาย'
    readme=f'''# PSU Esports Chatbot — {'ดาวน์โหลดโมเดลครั้งแรก' if variant=='download_models' else 'มีโมเดลครบ'}

## ใช้งาน

1. คัดลอกหรือแตก ZIP ทั้งโฟลเดอร์ไปไว้ในที่เขียนไฟล์ได้ เช่น Documents หรือ D: อย่าเปิดจากใน ZIP
2. ดับเบิลคลิก **Start-Chatbot.cmd**
3. {hint}
4. รอระบบเตรียมโมเดลและเปิดเว็บเอง แล้วพิมพ์คำถามไทยหรืออังกฤษได้

รวม Python และ Ollama แล้ว ไม่ต้องติดตั้งเอง ไม่ใช้โปรแกรมที่ติดตั้งในเครื่องผู้รับ
ไม่ต้องเปิด start-dashboard.bat ถ้าใช้การดึง WordPress โดยตรงตาม flow เดิม
ถ้ามี Dashboard เจ้าของที่ตรวจตัวตนได้ที่ 8080 ระบบจะอ่าน Dashboard นั้น
การจองสดต้องใช้อินเทอร์เน็ตและแหล่ง WordPress พร้อมเสมอ แม้เป็นชุดมีโมเดล
แชทบอทตอบข้อมูล/สถานะ ไม่กดจองหรือชำระเงินแทนผู้ใช้

## หยุดและประวัติ

- **Stop-Chatbot.cmd** หยุดเฉพาะโปรเซสของชุดนี้ เก็บประวัติไว้
- **View-Chat-Logs.cmd** เปิดรายงานประวัติที่เกิดในชุดนี้ เก็บเป็นไฟล์ใหม่ทุกครั้ง
- **Setup-Models.cmd** เตรียมหรือตรวจโมเดลล่วงหน้า โดยไม่เปิดเว็บ
- ปิดแท็บเว็บไม่หยุดเซิร์ฟเวอร์ เปิด Start ซ้ำจะกลับเข้าโปรเซสเดิม
- เลือกพอร์ตว่าง 8090–8099 อัตโนมัติ ไม่ปิดบริการอื่น
- Log อยู่ที่ `system/PSU_Esports_Chatbot_Local/data/logs/` เก็บไว้เฉพาะในเครื่อง

## เครื่องที่รองรับ

Windows 10 22H2 หรือ Windows 11 **64 บิต x64** (ไม่ใช่ Windows ARM, macOS หรือ Linux)
มีตัวรัน CPU และชุดรองรับ NVIDIA/AMD/Vulkan อยู่แล้ว GPU ต้องมี driver ที่รองรับ
แนะนำ RAM 16 GB ขึ้นไป เป็นคำแนะนำการใช้งาน ยังไม่ได้ benchmark ทุกเครื่อง
เครื่องไม่มี GPU ใช้ CPU ได้ แต่การตอบผ่านโมเดลอาจช้าหรือเกินเวลารอ 20 วินาทีของแชท
เริ่มครั้งแรกอาจใช้เวลาหลายนาที ตัวเปิดรอความพร้อมสูงสุด 10 นาทีหลังเริ่มเซิร์ฟเวอร์
{'หลังดาวน์โหลดครบขนาดจะเพิ่มประมาณ 3.65 GB ควรมีพื้นที่ว่างอย่างน้อย 4.2 GB เพิ่มจากขนาดชุดนี้' if variant=='download_models' else 'ต้องมีพื้นที่สำหรับแตกไฟล์ทั้งโฟลเดอร์ประมาณ 6.7 GB และพื้นที่เพิ่มสำหรับ log'}
ใช้ไดรฟ์ NTFS/exFAT สำหรับไฟล์ ZIP ขนาดใหญ่ หลีกเลี่ยง FAT32 ที่จำกัดไฟล์ละ 4 GB
หยุดก่อนย้ายทั้งโฟลเดอร์ เส้นทางที่มีช่องว่างใช้ได้ ห้ามย้ายเฉพาะ .cmd

## ถ้าเปิดไม่ได้

ดูข้อความในหน้าต่างก่อนปิด และ log ล่าสุดใน `data/logs/launcher/`
ไฟล์โมเดลที่ตรวจ SHA-256 ไม่ผ่านจะไม่ถูกนำมาใช้ ไม่เปลี่ยนเป็นโมเดลรุ่นอื่นเอง
ชุดดาวน์โหลด: หากไฟล์ pinned ที่ registry ทางการไม่มีแล้ว ต้องสร้างแพ็กเกจรุ่นใหม่ ไม่เดารุ่นทดแทน
ถ้าเครื่ององค์กรบล็อกการรัน .cmd/.ps1/.exe ให้ส่งเหตุผลจากระบบให้ผู้ดูแล ไม่จำเป็นต้องปิดระบบความปลอดภัยของเครื่อง

## ขอบเขตผลตรวจ

ชุดนี้ใช้โค้ด/ข้อมูล r37.2 ตามแหล่งเดิม ไม่เปลี่ยนนโยบาย ข้อมูลเจ้าของ หรือ Ground Truth
เก็บข้อสังเกตเดิม: `Which games have competition rules?` ยังถามให้เลือกเกมแทนสรุปรายการ
เป็นเว็บแชท local ของผู้รับแต่ละคน ไม่ใช่บริการออนไลน์ร่วมกัน เครื่องต้องเปิดระหว่างใช้
ผลทดสอบผู้จัดทำอยู่ใน TEST_RESULTS_TH.md และไม่ได้รับรองว่านโยบาย/กติกาทุกข้อถูกเจ้าของอนุมัติแล้ว
คู่มือ runtime ทางการ: https://docs.ollama.com/windows
หลักการตำแหน่ง blobs/download: https://github.com/ollama/ollama/blob/main/server/download.go
'''
    (root/'README_TH.md').write_text(readme,encoding='utf-8')
    files=[{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size} for p in root.rglob('*') if p.is_file()]
    (root/'build_inventory.json').write_text(json.dumps({'files':files,'bytes':sum(x['bytes'] for x in files),'old_logs_included':False},indent=2),encoding='utf-8')
    print(json.dumps({'folder':folder,'bytes':sum(x['bytes'] for x in files),'model_weights_included':variant=='with_models'}),flush=True)
print('Two clean folders created.',flush=True)
