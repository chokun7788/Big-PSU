import json,collections,sys
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());counts=collections.defaultdict(collections.Counter);examples={};n=0
with (r/((sys.argv[1] if len(sys.argv)>1 else 'sweep_A')+'_all_results.jsonl')).open(encoding='utf-8') as f:
    for line in f:
        try:row=json.loads(line)
        except json.JSONDecodeError:break
        n+=1
        for g in row['grades']:
            counts[g['corpus']]['total']+=1;counts[g['corpus']]['failed']+=not g['passed']
            if not g['passed']:
                key=g['corpus']
                if key not in examples and 'master_ground_truth_' not in key:
                    result=row.get('result',{});examples[key]={'q':row['question'],'expected':g['expected'].get('expected_answer_status'),'fails':g['failures'],'answer':result.get('answer','')[:800],'mode':result.get('mode'),'trace_tail':[t for t in result.get('trace',[]) if t.get('stage') in ('closed_query_improvement','semantic_route','universal_intent','answer_validation','game_entity_resolution')][-4:]}
print(json.dumps({'finished_requests':n,'corpora':counts,'examples':examples},ensure_ascii=False,indent=2))
