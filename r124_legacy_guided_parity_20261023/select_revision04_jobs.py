import json
from pathlib import Path
R=Path(__file__).resolve().parent
keys={'ef5c0b5a','e57f0296','9813e160','3cc3c5c3','9be5826b','2c110689','eafe23b9','9db7acd1','8acac2d3','5d18afc2','69812416','104194c2','4b0fb4a4','a603ab1a'}
rows=[json.loads(s) for s in (R/'ALL_RETAINED_JOBS.jsonl').read_text('utf8').splitlines()]
picked=[r for r in rows if r['key'][:8] in keys];assert len(picked)==len(keys)
(R/'REVISION04_JOBS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in picked),'utf8')
