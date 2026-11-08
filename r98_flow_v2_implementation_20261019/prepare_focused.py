"""Fixed stratified development subset, not a random full-corpus estimate."""
from pathlib import Path
import collections,hashlib,json
R=Path(__file__).resolve().parent;B=R.parent/'r95_merged_flow_implementation_20261018'
groups=collections.defaultdict(list)
for line in (B/'FULL_JOBS.jsonl').open(encoding='utf8'):
 j=json.loads(line);d=j['r70_stratum']['domain'];loc=j['locale']
 if any(x in d for x in ('price','rental','compound','follow','competition','rule','calendar','schedule','faq','owner','game','opening','booking')):groups[(d,loc)].append(j)
# Keep broad group coverage while capping cost: hash order fixed before seeing R98.
selected=[]
for key,items in sorted(groups.items(),key=lambda kv:hashlib.sha256(str(kv[0]).encode()).hexdigest())[:48]:
 selected.extend(sorted(items,key=lambda j:j['key'])[:2])
out=R/'FOCUSED_JOBS.jsonl'
if out.exists():raise SystemExit('Selection exists; refusing overwrite')
out.write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in selected),'utf8')
(R/'FOCUSED_SELECTION.json').write_text(json.dumps({'requests':len(selected),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'selection':'2 lowest request hashes per deterministically hash-ordered relevant domain/locale group, max 48 groups','not_representative_accuracy_estimate':True,'groups':{str(k):sum(j['locale']==k[1] and j['r70_stratum']['domain']==k[0] for j in selected) for k in groups if any(j['locale']==k[1] and j['r70_stratum']['domain']==k[0] for j in selected)},'keys':[j['key'] for j in selected]},ensure_ascii=False,indent=2),'utf8')
print(len(selected))
