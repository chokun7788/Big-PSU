import json
from pathlib import Path
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
for line in (R/'novel_D_usage_results.jsonl').open(encoding='utf-8'):
    x=json.loads(line)
    if x['passed']:continue
    print(x['case']['id'],x['case']['question'])
    for t in x['response'].get('trace',[]):
        if t['stage'] in ('preprocess','intent_cue_preflight','closed_query_improvement','query_planner','query_split','compound_plan','bilingual_route'):
            print(json.dumps(t,ensure_ascii=False))
