"""Retire copied duplicate rental tuples only after exact source reconciliation."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.domain_flow.projection import value
store=CommonStore(R/'system/data/knowledge/common.sqlite')
imports=json.loads((R/'CANDIDATE_DATA_IMPORT.json').read_text('utf8'))
new_ids={x['record_id'] for x in imports['imports'] if x['kind']=='rental_package'}
with store.connect() as c:records=CommonStore.heads(c)
def key(r):
    zone=value(r,'zone_ids');audience=value(r,'audience_id');period=value(r,'period_label')
    return (tuple(sorted(zone)),audience,period) if zone and audience and period else None
new={}
for rid in new_ids:
    k=key(records[rid])
    if k is None:raise ValueError('New rental has incomplete identity '+rid)
    if k in new:raise ValueError('New rental tuple is not unique')
    new[k]=records[rid]
retired=[];holds=[]
for rid,r in records.items():
    if r['kind']!='rental_package' or rid in new_ids:continue
    successor=new.get(key(r))
    if successor is None:continue
    if value(successor,'amount_minor')!=value(r,'amount_minor'):
        holds.append({'old':rid,'new':successor['record_id'],'reason':'price differs; no automatic supersession'});continue
    retired.append({'old':rid,'new':successor['record_id'],'same_tuple':key(r),'same_price_minor':value(r,'amount_minor'),
      'new_duration_minutes':value(successor,'duration_minutes'),'basis':'owner reaffirmed original rental prices and supplied actual half/full-day durations; exact zone/audience/period identity'})
for x in retired:store.withdraw(x['old'],actor='codex_candidate_source_reconciliation')
(R/'RENTAL_RECONCILIATION.json').write_text(json.dumps({'candidate_only':True,'retired_copied_duplicates':retired,'holds':holds,
 'original_R106_and_production_unchanged':True,'approvals_created':0,'old_revisions_preserved_in_candidate_history':True},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'retired_candidate_duplicates':len(retired),'holds':len(holds)}))
