from pathlib import Path
import json
B=Path(__file__).resolve().parent;src=B.parent/'PSU_Esports_Chat_New_R69'
for name in ('Open-New-Chat.cmd','Start-New-Chat.ps1','Stop-New-Chat.cmd','Stop-New-Chat.ps1','Open-Data-Editor.cmd','Open-Data-Editor.ps1'):
    p=B/name
    if p.exists():raise FileExistsError(p)
    text=(src/name).read_text('utf-8-sig')
    if name.endswith('.ps1'):
        text=text.replace("Join-Path $taskRoot 'runtime\\python\\python.exe'","Join-Path (Split-Path -Parent $taskRoot) 'PSU_Esports_Chat_New_R69\\runtime\\python\\python.exe'")
        text=text.replace("Join-Path $PSScriptRoot 'runtime\\python\\python.exe'","Join-Path (Split-Path -Parent $PSScriptRoot) 'PSU_Esports_Chat_New_R69\\runtime\\python\\python.exe'")
        text=text.replace('8101','8103').replace('8102','8104').replace("'new-common-chat-r69'","'new-common-chat-r72'").replace("PSU_RUNTIME_VERSION = 'R69'","PSU_RUNTIME_VERSION = 'R72'")
    p.write_text(text,encoding='utf-8-sig' if name.endswith('.ps1') else 'utf8')
for folder in ('runtime/logs','runtime/state'):(B/folder).mkdir(parents=True,exist_ok=True)
p=B/'system/app/knowledge/common/build_info.py'
p.write_text(p.read_text('utf8').replace('common-r69-isolated-chat','common-r72-flow-repair'),encoding='utf8')
for p in (B/'system/web_chat').rglob('*.html'):
    text=p.read_text('utf8')
    if 'R69' in text:p.write_text(text.replace('R69','R72'),encoding='utf8')
print('Created separate R72 launchers, ports 8103/8104, shared existing Python runtime.')
