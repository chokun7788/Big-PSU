import json, sys
from collections import Counter
from pathlib import Path
report = Path(Path(__file__).with_name('r25_report_path.txt').read_text(encoding='utf-8').strip())
run = sys.argv[1]
rows = [json.loads(line) for line in (report/(run+'_details.jsonl')).read_text(encoding='utf-8').splitlines() if line.strip()]
failed = [row for row in rows if not row['passed']]
groups = {}
for row in failed:
    key = (row['locale'], row.get('game'), row.get('expected_facet'), tuple(row['failures']), row['answer'])
    groups.setdefault(key, []).append(row)
result = [{'count':len(items),'locale':key[0],'game':key[1],'facet':key[2],'failures':list(key[3]),'answer':key[4], 'queries':[row['question'] for row in items[:4]], 'source_ids':items[0]['source_ids']} for key,items in groups.items()]
print(json.dumps({'total':len(rows),'failed':len(failed),'groups':result},ensure_ascii=False,indent=2), flush=True)
with (report/(run+'_failure_groups.json')).open('x',encoding='utf-8') as handle:json.dump(result,handle,ensure_ascii=False,indent=2)
