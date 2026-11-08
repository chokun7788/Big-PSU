import json,collections
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());counts=collections.defaultdict(collections.Counter);examples={};failurecounts=collections.Counter()
for line in (r/'FINAL_G_EXTRA_CORPUS_RESULTS.jsonl').read_text(encoding='utf-8').splitlines():
    row=json.loads(line)
    for g in row['grades']:
        if g['observation_only']:continue
        key=g['corpus'];hard=[x for x in g['failures'] if not x.startswith('legacy_mode_prefix:')]
        counts[key]['total']+=1;counts[key]['legacy_passed']+=g['passed'];counts[key]['without_mode_gate_passed']+=not hard
        failurecounts.update(g['failures'])
        if hard and key not in examples:
            examples[key]={'question':row['question'],'expected':g['case'],'answer':row['result']['answer'],'mode':row['result']['mode'],'failures':hard,'trace':row['result']['trace']}
with (r/'FINAL_G_EXTRA_CORPUS_ANALYSIS.json').open('x',encoding='utf-8') as f:json.dump({'counts':counts,'examples':examples,'failure_counts':failurecounts,'mode_removed_grade_scope':'diagnostic only; content keyword grade still does not establish semantic equivalence'},f,ensure_ascii=False,indent=2)
print(json.dumps({'counts':counts,'examples':{k:{v:x[v] for v in ['question','answer','mode','failures']} for k,x in examples.items()}},ensure_ascii=False,indent=2))
