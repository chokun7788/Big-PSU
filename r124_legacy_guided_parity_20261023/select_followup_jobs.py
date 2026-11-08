import json
from pathlib import Path
R=Path(__file__).resolve().parent
keys={'ef5c0b5a','e57f0296','00301c15','9813e160','3020765f','981fa8d4','69812416','5b2d0e13','83ff647f','88b3a23b','42582c1e','1cf7db38'}
rows=[json.loads(s) for s in (R/'ALL_RETAINED_JOBS.jsonl').read_text('utf8').splitlines()]
selected=[r for r in rows if r['key'][:8] in keys];assert len(selected)==len(keys)
(R/'FOLLOWUP_JOBS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in selected),'utf8')
print(json.dumps({'same_retained_questions':len(selected),'new_questions':0}))
