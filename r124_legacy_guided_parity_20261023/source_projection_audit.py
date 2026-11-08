"""Account for every active record and retained FAQ in executable projection."""
import collections,json,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/(sys.argv[1] if len(sys.argv)>1 else 'system');sys.path.insert(0,str(S))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.projection import value
snap=MigratedView(S/'data/knowledge/common.sqlite').snapshot();engine=Engine.from_snapshot(snap)
rows=[]
for rid,record in engine.index.records.items():
 facts=engine.index.byrecord[rid]
 refs=[f['id'] for f in engine.index.facts if rid in [engine.index.byid.get(x,{}).get('record_id') for x in f.get('corroborating_fact_ids',[])]]
 # Consolidated IDs remain source-correlated even when no separate fact exists.
 if not refs:refs=[f['id'] for f in engine.index.facts if any(':'+rid+':' in x for x in f.get('corroborating_fact_ids',[]))]
 confirmations=[f['id'] for f in engine.index.facts if f.get('confirmation_ref')==rid]
 rows.append({'record_id':rid,'kind':record['kind'],'topic':value(record,'topic'),'question':value(record,'question'),
  'has_known_answer':value(record,'answer') is not None,'fact_ids':[f['id'] for f in facts],
  'consolidated_into':refs,'categories':sorted({f['category'] for f in facts}),
  'confirmation_fact_ids':confirmations,
  'state':'projected' if facts else 'consolidated_exact_clause' if refs else 'attached_confirmation_metadata' if confirmations else 'relation_or_native_only' if record['kind'] in {'audience','live_binding','game_service','competition'} else 'not_projected'})
output={'generated_at':time.time(),'record_count':len(rows),'counts':dict(collections.Counter(x['state'] for x in rows)),
 'faq_answer_projection_gaps':[r for r in rows if r['kind']=='faq' and r['has_known_answer'] and r['state']=='not_projected'],'records':rows}
(R/('SOURCE_PROJECTION_AUDIT.json' if S.name=='system' else 'REVISION03_PROJECTION_AUDIT.json')).write_text(json.dumps(output,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in output.items() if k!='records'},ensure_ascii=False))
