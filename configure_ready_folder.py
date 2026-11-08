from pathlib import Path
import json, hashlib, shutil

W = Path(__file__).parent
R = Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Chatbot_Ready_20261003')
P = R / 'system' / 'PSU_Esports_Chatbot_Local'
SOURCE = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')

def new(name, text):
    with (R / name).open('x', encoding='utf-8', newline='') as f:
        f.write(text)

new('Start-Chatbot.ps1', (W / 'ready_start_template.ps1').read_text(encoding='utf-8'))
new('Stop-Chatbot.ps1', (W / 'ready_stop_template.ps1').read_text(encoding='utf-8'))
for name in ['Start-Chatbot', 'Stop-Chatbot', 'View-Chat-Logs']:
    new(name + '.cmd', '@echo off\r\n"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -ExecutionPolicy Bypass -File "%~dp0' + name + '.ps1"\r\nif errorlevel 1 pause\r\n')

launcher = P / 'Start-PSU-Esports-Chatbot.ps1'
text = launcher.read_text(encoding='utf-8-sig')
before = text.index('$python = Get-Command python')
after = text.index('try {\n    $models =', before)
text = text[:before] + '''$readyRoot = Split-Path (Split-Path $projectRoot -Parent) -Parent
$python = [pscustomobject]@{ Source = (Join-Path $readyRoot "runtime\\python\\python.exe") }
if (-not (Test-Path -LiteralPath $python.Source)) { throw "Bundled Python is missing. Keep the entire ready folder together." }
$ollamaBase = $env:OLLAMA_URL
if (-not $ollamaBase) { throw "Open Start-Chatbot.cmd from the ready folder." }

''' + text[after:]
text = text.replace('"http://127.0.0.1:11434/api/tags"', '"$ollamaBase/api/tags"')
text = text.replace('Ollama API is not running at 127.0.0.1:11434. Open Ollama first, then start the chatbot again.', 'Local Ollama is not ready. Open Start-Chatbot.cmd from the ready folder.')
# Only the freshly built delivery launcher is edited; source and old packages stay intact.
launcher.write_text(text, encoding='utf-8-sig')

new('View-Chat-Logs.ps1', '''$ErrorActionPreference = 'Stop'
$package = Join-Path $PSScriptRoot 'system\\PSU_Esports_Chatbot_Local'
$python = Join-Path $PSScriptRoot 'runtime\\python\\python.exe'
$database = Join-Path $package 'data\\logs\\chat_history.sqlite3'
if (-not (Test-Path -LiteralPath $database)) { throw 'No chat history yet. Open the Chatbot and ask a question first.' }
$output = Join-Path $package ('data\\logs\\chat_history_report_' + (Get-Date -Format 'yyyyMMdd_HHmmss_fff') + '.html')
& $python (Join-Path $package 'tools\\export_local_chat_logs.py') --database $database --output $output
if ($LASTEXITCODE -ne 0) { throw 'Could not export chat history.' }
Start-Process $output
''')

new('README_TH.md', '''# PSU Esports Studio – Phuket Chatbot พร้อมใช้

## เปิดใช้งาน

1. ดับเบิลคลิก **Start-Chatbot.cmd** ในโฟลเดอร์นี้
2. รอระบบเริ่มและโหลดโมเดล เว็บแชทจะเปิดเองเมื่อพร้อม
3. พิมพ์คำถามได้ทั้งไทยและอังกฤษ

หลังเปิดสำเร็จ ระบบทำงานเบื้องหลัง ปิดหน้าต่างตัวเปิดได้ ปิดแท็บเว็บอย่างเดียวจะยังไม่หยุดระบบ
เปิด Start-Chatbot.cmd อีกครั้งเพื่อกลับเข้าแชทเดิมที่กำลังรัน โดยไม่เปิดเซิร์ฟเวอร์ซ้ำ
ถ้าชุดเดิมใช้พอร์ต 8090 อยู่ ชุดนี้จะเลือกพอร์ตว่างถัดไปให้ URL จริงแสดงในตัวเปิด

## หยุดและดูประวัติ

- **Stop-Chatbot.cmd**: หยุดเฉพาะแชทและ Ollama ที่โฟลเดอร์นี้เริ่มเอง เก็บ log ไว้
- **View-Chat-Logs.cmd**: เปิดรายงานบทสนทนาที่เกิดในชุดนี้ เก็บรายงานแต่ละครั้งเป็นไฟล์ใหม่
- ประวัติใหม่อยู่ที่ `system/PSU_Esports_Chatbot_Local/data/logs/`
- ถ้าเริ่มไม่สำเร็จ หน้าต่างจะแสดงเหตุผล และมี log ใน `data/logs/launcher/`

## รวมอะไรไว้แล้ว

- โค้ดและเว็บแชทปัจจุบัน r37.2 พร้อมข้อมูลบริการ เกม กติกา และคำตอบไทย/อังกฤษจากโปรเจกต์
- Python 3.12 พร้อมคลังมาตรฐานและข้อมูลเขตเวลา
- Ollama 0.34.4 พร้อมตัวรัน CPU/GPU และใบอนุญาตที่มากับตัวรัน
- โมเดล `scb10x/typhoon2.5-qwen3-4b` และ `psu-bge-m3:q8_0` ที่มีจริงในเครื่อง พร้อมตรวจ SHA-256 ของทุก model blob
- ตัวเริ่มเบื้องหลัง ตัวหยุด และตัวดู log

ไม่ต้องติดตั้ง Python/Ollama หรือดาวน์โหลดโมเดลใหม่เพื่อเปิดชุดนี้
ถ้า Ollama เดิมในเครื่องมีโมเดลที่ digest ตรงกัน ตัวเปิดจะใช้บริการนั้นได้
ถ้าไม่มี ตัวเปิดจะใช้ Ollama และโมเดลในโฟลเดอร์นี้เอง
ชื่อ `psu-bge-m3:q8_0` เป็นชื่อ profile เดิม: โมเดลจริงที่ Ollama รายงานเป็น F16 ไม่ใช่การรับรองว่าเป็น quantization Q8

## การจองและอินเทอร์เน็ต

ถามสถานะว่างแล้วระบบดึงข้อมูล WordPress ขณะถาม ไม่จำเป็นต้องเปิด start-dashboard.bat แยก
ถ้ามี Dashboard เจ้าของที่ตรวจตัวตนได้บนพอร์ต 8080 ระบบจะใช้ Dashboard นั้นตาม flow เดิม
สถานะจองสดต้องใช้อินเทอร์เน็ตและแหล่ง WordPress ต้องพร้อม ถ้าดึงไม่ได้ ระบบจะบอกว่ายืนยันไม่ได้
ชุดนี้ตอบข้อมูลและสถานะจอง ไม่ได้กดจอง ยกเลิก หรือจ่ายเงินแทนผู้ใช้

## ย้ายโฟลเดอร์

หยุดด้วย Stop-Chatbot.cmd ก่อน แล้วย้ายหรือคัดลอก **ทั้งโฟลเดอร์** รวม runtime และ system
ใช้ชื่อโฟลเดอร์และเส้นทางที่มีช่องว่างได้ ตัวเปิดอ้างไฟล์จากโฟลเดอร์ของตัวเอง
อย่าคัดลอกเฉพาะไฟล์ .cmd หรือย้ายตอนโปรแกรมกำลังรัน
ชุดนี้ตรวจบน Windows 64 บิตเครื่องนี้ การย้ายไปเครื่องอื่นยังต้องตรวจ RAM/GPU/driver และสิทธิ์ของเครื่องปลายทาง
เป็นเว็บแชทในเครื่อง (`127.0.0.1`) เครื่องต้องเปิดอยู่ขณะใช้งาน ไม่ใช่เว็บสาธารณะที่รันได้เมื่อเครื่องปิด

## ขอบเขตการตรวจ

ผลตรวจการประกอบและการเปิดชุดนี้อยู่ใน `DELIVERY_CHECK_TH.md`
การเปิดระบบผ่านไม่ได้หมายความว่าเจ้าของรับรองนโยบาย กติกาทุกข้อ หรือสถานะจองทุกช่องแล้ว
ไม่รวมประวัติแชทเดิม ข้อมูลผู้จองจริง คีย์ Ollama ส่วนตัว หรือโมเดลอื่นที่ไม่ได้ใช้
โค้ด ข้อมูลเจ้าของ และ log ของชุดเดิมคงอยู่ที่เดิม
''')

checks = []
for part in ['app', 'web_chat', 'booking_dashboard', 'data']:
    for dst in (P / part).rglob('*'):
        if not dst.is_file() or '__pycache__' in dst.parts or 'logs' in dst.relative_to(P).parts:
            continue
        src = SOURCE / dst.relative_to(P)
        if src.is_file():
            a = hashlib.sha256(src.read_bytes()).hexdigest()
            b = hashlib.sha256(dst.read_bytes()).hexdigest()
            checks.append({'path': str(dst.relative_to(P)), 'sha256': b, 'same_as_source': a == b})
if not all(x['same_as_source'] for x in checks):
    raise RuntimeError('Runtime/data copies differ from current source')
new('runtime_source_checks.json', json.dumps(checks, ensure_ascii=False, indent=2))
print(json.dumps({'root': str(R), 'source_files_verified': len(checks), 'all_match': True}), flush=True)
