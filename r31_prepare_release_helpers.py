from pathlib import Path
for source,dest in [('r30_start_web.ps1','r31_start_web.ps1'),('r30_stop_owned_web.ps1','r31_stop_owned_web.ps1'),('r30_live_path_and_guard.py','r31_live_path_and_guard.py')]:
    text=Path(source).read_text(encoding='utf-8').replace('r30_report_path.txt','r31_report_path.txt').replace('r30_ready_','r31_ready_')
    with Path(dest).open('x',encoding='utf-8') as out:out.write(text)
