import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
e=Engine.from_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot())
food=next(x for x in map(json.loads,(R/'student01/RESULTS.jsonl').open(encoding='utf8')) if x['key'].startswith('d7158a36'))
ids={f['record_id'] for n in food['response']['decision_artifact']['need_results'] for f in n.get('claim_packets',[])}
facts=[f for f in e.index.facts if f['record_id'] in ids or f['category']=='C02' and 'developer' in str(f.get('value')).lower()]
out=[{'fact':f,'record':e.index.records[f['record_id']]} for f in facts]
(R/'REGRESSION_SOURCE_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps([{'id':f['id'],'value':f['value'],'policy_intent':f.get('policy_intent')} for f in facts],ensure_ascii=False))
