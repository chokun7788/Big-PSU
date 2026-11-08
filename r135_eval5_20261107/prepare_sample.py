import collections,hashlib,json,sqlite3
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent
src=R/'r131_diagnostic_review_20261025/SELECTED_JOBS.jsonl'
jobs=[json.loads(s) for s in src.read_text(encoding='utf8').splitlines() if s.strip()]
members=json.loads((R/'r131_diagnostic_review_20261025/CATEGORY_MEMBERSHIP.json').read_text(encoding='utf8'))['members']
assert len(jobs)==2111 and len({x['key'] for x in jobs})==2111
def h(j):return hashlib.sha256(('r135-eval5-20261107:'+j['key']).encode()).hexdigest()
buckets=collections.defaultdict(list)
for j in jobs:buckets[(j['locale'],tuple(sorted(members[j['key']]['categories'])))].append(j)
ranked=[];selected=[]
for k,v in sorted(buckets.items()):
 v.sort(key=h);n=len(v)//2;selected+=v[:n]
 if len(v)%2:ranked.append(v[n])
ranked.sort(key=h);selected+=ranked[:1056-len(selected)]
assert len(selected)==1056 and len({x['key'] for x in selected})==1056
selected.sort(key=h)
dest=O/'SELECTED_5_PERCENT.jsonl'
with dest.open('x',encoding='utf8',newline='\n') as f:
 for j in selected:f.write(json.dumps(j,ensure_ascii=False)+'\n')
coverage=collections.Counter()
for j in selected:
 coverage['locale:'+j['locale']]+=1
 for c in members[j['key']]['categories']:coverage['category:'+c]+=1
manifest={'method':'nested deterministic half-sample of prior stratified 2111 keys, grouped by requested locale and category-set; SHA256-ranked with fixed seed','seed':'r135-eval5-20261107','count':len(selected),'sample_fraction_note':'approximately half prior 10% sample, approximate 5% of original universe; rounding may vary by stratum','input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'selected_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'counts':dict(coverage),'limitations':'same-request keys enable observational comparison, not identical execution conditions or guaranteed representation of all categories'}
(O/'SELECTION_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
srcdb=R/'r135_complete_flow_audit_20261026/system/data/knowledge/common.sqlite';dst=O/'system/data/knowledge/eval5.sqlite'
a=sqlite3.connect(srcdb.resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(dst);a.backup(b);b.close();a.close()
print(json.dumps({'selected':len(selected),'db_copy':str(dst),'categories':dict(coverage)},ensure_ascii=False))
