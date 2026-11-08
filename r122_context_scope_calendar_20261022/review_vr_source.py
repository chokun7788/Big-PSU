import json,os,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision03_system';os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.readers import policy
index=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot()).index
rates=[f for f in index.bycat['C06'] if re.search(r'\bVR\b',' '.join(f['subject'].values()),re.I)]
p=policy(index,'C08','how do i book it vr')
book=[index.byid[k] for k in (p.ids+p.candidates if p else [])]
out={'rate_facts':rates,'rate_records':{f['record_id']:index.records[f['record_id']] for f in rates},'booking_plan':p.__dict__ if p else None,'booking_facts':book,'booking_records':{f['record_id']:index.records[f['record_id']] for f in book},'new_model_calls':0}
(R/'VR_SOURCE_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'rate_duration_values':[f['value'] for f in rates if f['facet']=='duration_minutes'],'booking_reason':p.reason if p else None,'booking_ids':[f['id'] for f in book],'procedure_complete':[f.get('procedure_complete') for f in book]},ensure_ascii=False,indent=2))
