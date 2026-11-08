"""Freeze focused existing contracts + source assertions; no old gold rewrites."""
import json,hashlib,collections,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;OLD=B.parent/'r64_full_comparison_20261013'
rows=[json.loads(line) for line in (OLD/'JOBS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
# Deterministic stratification across all corpus, locale and clean/noisy variants.
groups=collections.defaultdict(list)
for row in rows:
 for entry in row['entries']:
  groups[(entry['file'],row['locale'],entry['variant'])].append(row)
selected={}
for group,candidates in sorted(groups.items()):
 ordered=sorted(candidates,key=lambda row:row['key'])
 for index in range(min(5,len(ordered))):
  row=ordered[(index*len(ordered))//min(5,len(ordered))];selected[row['key']]=row
out=B/'COMMON_STRATIFIED_JOBS.jsonl'
with out.open('x',encoding='utf-8') as f:
 for row in selected.values():f.write(json.dumps(row,ensure_ascii=False)+'\n')
(B/'COMMON_STRATIFIED_INVENTORY.json').write_text(json.dumps({'requests':len(selected),'grades':sum(len(x['entries']) for x in selected.values()),'strata':len(groups),'corpora':len(set(k[0] for k in groups)),'source_inventory_sha256':hashlib.sha256((OLD/'JOBS.jsonl').read_bytes()).hexdigest(),'sampling':'5 deterministic quantiles per corpus/locale/variant; content assertions and protocol-only both retained','all_original_contracts_preserved':True,'not_full_20554_sweep':True},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'focused_requests':len(selected),'grades':sum(len(x['entries']) for x in selected.values()),'strata':len(groups)}))
