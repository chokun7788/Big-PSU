import json,collections
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());counts=collections.defaultdict(collections.Counter);fixes=[]
with (r/'http8091_G2_http_results_rescored.jsonl').open('x',encoding='utf-8') as out:
    for line in (r/'http8091_G2_http_results.jsonl').open(encoding='utf-8'):
        row=json.loads(line);raw=row['response'].get('raw',{})
        if row['case'].get('group')=='true_wrong_layout':
            assert row['failures']==['wrong_outcome:answer'],row
            assert raw.get('mode')=='input_guard_layout_retype' and 'keyboard_layout_mismatch' in raw.get('input_quality',{}).get('flags',[]),raw
            fixes.append({'case':row['case'],'original_failure':row['failures'],'correction':'generic pipeline status grader did not recognize the HTTP ingress guard mode; actual response asks retyping and has verified mismatch flag'})
            row['original_failures']=row['failures'];row['failures']=[];row['passed']=True
        counts[row['suite']]['total']+=1;counts[row['suite']]['passed']+=not row['failures'];out.write(json.dumps(row,ensure_ascii=False)+'\n')
with (r/'http8091_G2_http_summary_rescored.json').open('x',encoding='utf-8') as f:json.dump({'by_suite':counts,'grader_corrections':fixes,'raw_results_preserved':True},f,ensure_ascii=False,indent=2)
print(json.dumps(counts))
