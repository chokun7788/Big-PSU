from pathlib import Path
import json
W=Path(__file__).parent
cases=json.loads((W/'r37_holdout_cases.json').read_text(encoding='utf-8'))
questions=['มีเกมอะไรให้แข่งมั่ง','valorant','ขอกฏหนาอย','ขอกฏของเกมหน่อย','ขอกฏของเกม valo หน่อย','มีกฏอื่นไหม','ขอกฎหน่อยยย','มีข้ออื่นอีกป่าว']
cases.append(['repeated_requests','th',[{'q':q,'kind':'catalog' if i==0 else 'more' if i in (5,7) else 'overview','game':'valorant'} for i,q in enumerate(questions)]])
with (W/'r37_holdout_and_repeat_valid.json').open('x',encoding='utf-8') as f:json.dump(cases,f,ensure_ascii=False,indent=2)
print('Created 21 valid follow-up/holdout cases; kept the earlier harness-format error log.')
