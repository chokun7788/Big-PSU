from pathlib import Path
import json,sys
r=Path(Path('r30_report_path.txt').read_text().strip())
for line in (r/(sys.argv[1]+'_focused_details.jsonl')).read_text(encoding='utf-8').splitlines():
    row=json.loads(line)
    if row['failures']:print(json.dumps({k:row[k] for k in ['case','answer','mode','failures']}|{'validation': [t for t in row['trace'] if t['stage']=='closed_query_improvement']},ensure_ascii=False,indent=2))
