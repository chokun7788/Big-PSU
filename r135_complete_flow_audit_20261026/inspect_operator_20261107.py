import sys,json
sys.path.insert(0,'.');from verification_support import snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.contact_scope import candidates,generic
from datetime import datetime
q='Who operates PSU Esports Studio? Could you check this for me';e=Engine.from_snapshot(snapshot());b=e.index.bind('C01',q);print('bound',[(x['record_id'],x['facet']) for x in b]);print('candidates',[(x['record_id'],x['facet']) for x in candidates(e.index,q,'')]);print('generic',generic(q));p=e.plan('C01',q,datetime.fromisoformat('2026-10-31T12:00:00+07:00'));print('plan',p);x=e._legacy_answer(q,'en','C01',datetime.fromisoformat('2026-10-31T12:00:00+07:00'),False);print(json.dumps({'answer':x.get('answer'),'claims':x.get('claims')},ensure_ascii=False)[:4000])
