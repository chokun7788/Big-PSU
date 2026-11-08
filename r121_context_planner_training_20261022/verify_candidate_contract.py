"""Check that the integration accepts the frozen labels; no model or API calls."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.understanding import parse
out={}
for name in ['train','validation','test']:
 xs=list(map(json.loads,(R/(name+'.jsonl')).open(encoding='utf8')));failures=[]
 for x in xs:
  result=parse(json.dumps(x['label'],ensure_ascii=False),x['question'])
  if not result.accepted:failures.append({'key':x['key'],'reason':result.reason})
 out[name]={'checked':len(xs),'accepted':len(xs)-len(failures),'rejected':failures}
(R/'NATIVE_CONTRACT_COMPATIBILITY.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(out,ensure_ascii=False,indent=2))
assert all(not s['rejected'] for s in out.values())
