import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.entity_search import candidates
from app.knowledge.common.question_profiles import select
snap=MigratedView(B/'system/data/knowledge/common.sqlite').snapshot();rs=snap['release']['records'];names=snap['release']['names']
q='I attached the incorrect proof of payment. How do I fix it?'
rows=candidates(q,rs,names);direct,audit=select(q,rs)
target=next((x for x in rows if x['record_id']=='procedure_wrong_slip'),None)
checks=[{'case':'Correct procedure reaches bounded candidate set without aliasing the new wording','passed':target is not None and target.get('requires_semantic_selection') is True and len(rows)<=8},
 {'case':'A missing lexical subject is not automatically asserted as a known source answer','passed':direct is None}]
result={'checks':checks,'candidates':rows,'direct_profile_selection':audit,'model_inference_certified':False}
(B/'RETRIEVAL_RECALL_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'passed':sum(c['passed'] for c in checks),'checks':len(checks),'model_inference_certified':False}))
raise SystemExit(any(not c['passed'] for c in checks))
