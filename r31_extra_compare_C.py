import json,collections
from pathlib import Path
r=Path(Path('r31_report_path.txt').read_text().strip());old=Path(Path('r30_report_path.txt').read_text().strip());base={}
for line in (old/'FINAL_G6_EXTRA_CORPUS_RESULTS.jsonl').open(encoding='utf-8'):
    x=json.loads(line);base[x['question']]={g['corpus']+':'+str(g['id'] if 'id' in g else g.get('row_index')):g['passed'] for g in x['grades']}
counts=collections.defaultdict(collections.Counter);failures=collections.Counter();new=[];examples={}
for line in (r/'R31_C_EXTRA_CORPUS_RESULTS.jsonl').open(encoding='utf-8'):
    x=json.loads(line)
    for g in x['grades']:
        if g['observation_only']:continue
        name=g['corpus'];hard=[s for s in g['failures'] if not s.startswith('legacy_mode_prefix:')]
        counts[name]['total']+=1;counts[name]['legacy_passed']+=g['passed'];counts[name]['diagnostic_without_mode_passed']+=not hard;failures.update(g['failures'])
        identity=name+':'+str(g['id'] if 'id' in g else g.get('row_index'))
        if base[x['question']][identity] and not g['passed']:new.append(dict(question=x['question'],grade=g,result=x['result']))
        if hard and name not in examples:examples[name]=dict(question=x['question'],grade=g,result=x['result'])
with (r/'R31_C_EXTRA_CORPUS_ANALYSIS.json').open('x',encoding='utf-8') as out:json.dump(dict(counts=counts,failure_counts=failures,new_failed_grades=new,examples=examples,scope='Legacy raw scores unchanged. Diagnostic exclusion of mode gate does not prove semantic equivalence. Human review observations are not human-approved answers.'),out,ensure_ascii=False,indent=2)
print(json.dumps(dict(counts=counts,new_failed_grades=len(new)),ensure_ascii=False),flush=True)
