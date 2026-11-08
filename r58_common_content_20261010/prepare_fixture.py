import sys,json,copy
from pathlib import Path
OUT=Path(__file__).resolve().parent;CAND=OUT/'system/PSU_Esports_Chatbot_Local';sys.path.insert(0,str(CAND))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from tests.test_common_content_r58 import ORDER,record
db=OUT/'fixtures/chat_fixture.sqlite';store=CommonStore(db);store.initialize(allow_demo=True)
ids=[]
for k in ORDER:
    r=record(k);x=save_owner_record(store,r,0,'synthetic-fixture-only',translation_reviewed=True);store.approve(x['record_id'],x['version'],x['hash'],actor='synthetic-fixture-only');ids.append(x['record_id'])
release=store.publish(ids,actor='synthetic-fixture-only',expected_active='',request_key='fixture-setup')
print(json.dumps({'db':str(db),'release':release,'records':len(ids),'synthetic':True}))
