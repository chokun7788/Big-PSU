import json,sys
from pathlib import Path
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
rows=[json.loads(line) for line in (report/(sys.argv[1]+'_details.jsonl')).read_text(encoding='utf-8').splitlines() if line.strip()]
for row in rows:
 if row['failures'] and row['failures']!=['answer_without_substantive_source_content']:
  print(json.dumps(row,ensure_ascii=False))
