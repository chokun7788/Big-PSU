import sys,json
import r49_probe as r
sys.path.insert(0,str(r.old.p.ROOT))
from app.pipeline.user_service_facts import answer_user_service_facts
from app.pipeline.service_fact_query import recover_service_fact_query
for c in r.cases():
 if 'key' not in c:continue
 q=c['turns'][0];res=answer_user_service_facts(q,c['locale'])
 meta=res['trace'][0].metadata if res else {};keys=meta.get('claim_ids',[])
 if c['key'] not in keys:print(c['id'],json.dumps(dict(query=q,recovered=recover_service_fact_query(q),claims=keys),ensure_ascii=False))
