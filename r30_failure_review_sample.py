import json,collections
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());selected=collections.defaultdict(list)
for l in (r/'VERIFIED_FAILURE_INVENTORY.jsonl').open(encoding='utf-8'):
    x=json.loads(l)
    for g in x['grade_failures']:
        if 'master_ground_truth_bilingual_10000_v2' in g['corpus']:
            d=g['expected']['domain'];bucket=(d,g['expected']['locale'])
            if len(selected[bucket])<2:selected[bucket].append({'q':x['question'],'answer':x['result']['answer'],'mode':x['result']['mode'],'expected':g['expected'],'failures':g['failures']})
for (d,loc),rows in selected.items():
    print(json.dumps({'domain':d,'locale':loc,'examples':rows},ensure_ascii=False)[:3600])
