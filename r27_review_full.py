import json,sys
from r27_fixture import PROJECT, REPORT
sys.path.insert(0,str(PROJECT))
from app.knowledge.localization import approved_localization
from tools.competition_content_grader_r27 import rescore
run=sys.argv[1]
rows=[json.loads(x) for x in (REPORT/(run+'_details.jsonl')).read_text(encoding='utf-8').splitlines() if x.strip()]
source={r['id']:r for r in (json.loads(x) for x in (PROJECT/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines())}
records,summary=rescore(rows,source,approved_localization)
with (REPORT/(run+'_atomic_source_rescore.json')).open('x',encoding='utf-8') as f:json.dump({'summary':summary,'records':records},f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False))
seen=set()
for record,row in zip(records,rows):
    if record['source_grade_passed']:continue
    key=tuple(record['remaining_failures'])
    if key in seen:continue
    seen.add(key)
    print(json.dumps({'id':row['id'],'q':row['question'],'fail':record['remaining_failures'],'answer':row['answer']},ensure_ascii=False))
