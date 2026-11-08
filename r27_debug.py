import json,sys
from r27_fixture import PROJECT,REPORT
sys.path.insert(0,str(PROJECT))
from app.pipeline.competition_detail import lookup_competition_detail, requested_detail_concepts
from app.pipeline.competition_targets import resolve_competition_targets
rows=[json.loads(x) for x in (REPORT/(sys.argv[1]+'_details.jsonl')).read_text(encoding='utf-8').splitlines()]
seen=set()
for r in rows:
    if r['passed'] or r['anchor'] in seen:continue
    seen.add(r['anchor'])
    if len(sys.argv)>2 and not r['anchor'].startswith(sys.argv[2]):continue
    print(json.dumps({'id':r['id'],'question':r['question'],'trace':[t for t in r['response'].get('trace',[]) if t['stage'] in ('competition_detail','preprocess')],'direct_concepts':[c.name for c in requested_detail_concepts(r['question'],resolve_competition_targets(r['question']).targets[0].game_id)]},ensure_ascii=False))
