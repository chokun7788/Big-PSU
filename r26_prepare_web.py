from pathlib import Path
root=Path(__file__).parent
content=(root/'r25_web_check.py').read_text(encoding='utf-8').replace('r25_report_path.txt','r26_report_path.txt').replace('2026.10.01-competition-format-r25','2026.10.01-competition-content-speed-r26').replace("session='r25-web-'","session='r26-web-'")
with (root/'r26_web_check.py').open('x',encoding='utf-8') as f:f.write(content)
content=(root/'r25_start_web.ps1').read_text(encoding='utf-8').replace('competition_format_r25','competition_content_speed_r26_final').replace('r25_ready_','r26_ready_')
with (root/'r26_start_web.ps1').open('x',encoding='utf-8') as f:f.write(content)
