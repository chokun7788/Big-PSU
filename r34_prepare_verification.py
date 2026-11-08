from pathlib import Path
W=Path(__file__).parent;version='2026.10.03-source-task-boundaries-r34'
for name in ['positive_http','partial_http','year_http','queue_diagnostic']:
 ext='.js' if name=='queue_diagnostic' else '.py'
 s=(W/('r33_'+name+ext)).read_text(encoding='utf-8').replace('r33_report_path.txt','r34_report_path.txt').replace('2026.10.02-usable-task-frames-r33',version)
 p=W/('r34_'+name+ext);assert not p.exists();p.write_text(s,encoding='utf-8')
s=(W/'r33_http_regression.py').read_text(encoding='utf-8').replace("r=Path(Path('r33_report_path.txt').read_text().strip());", "old=Path(Path('r33_report_path.txt').read_text().strip());r=Path(Path('r34_report_path.txt').read_text().strip());").replace('2026.10.02-usable-task-frames-r33',version)
a=s.index('tasks=');b=s.index('for name in',a);s=s[:a]+s[a:b].replace('(r/', '(old/')+s[b:]
p=W/'r34_http_regression.py';assert not p.exists();p.write_text(s,encoding='utf-8')
print('Verification helpers copied; previous fixtures read-only, new outputs only')
