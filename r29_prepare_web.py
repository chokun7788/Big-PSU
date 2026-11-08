from pathlib import Path
root=Path(__file__).parent
for source,target in [('r28_start_web.ps1','r29_start_web.ps1'),('r28_stop_owned_web.ps1','r29_stop_owned_web.ps1'),('r28_final_web_check.py','r29_final_web_check.py')]:
    text=(root/source).read_text(encoding='utf-8').replace('r28_ready_', 'r29_ready_').replace('r28_report_path.txt','r29_report_path.txt').replace('2026.10.02-competition-composition-r28-verified','2026.10.02-input-context-r29-verified')
    with (root/target).open('x',encoding='utf-8') as f:f.write(text)
print('Created separate r29 web helpers without altering r28 reports.')
