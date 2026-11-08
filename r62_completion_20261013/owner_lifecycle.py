"""Owner HTTP lifecycle over a dedicated DEMO database; no real owner approvals."""
import sys,json,threading,os,uuid,copy,time
from pathlib import Path
from http.server import ThreadingHTTPServer
from urllib.request import Request,urlopen
B=Path(__file__).resolve().parent;SYSTEM=B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
sys.path.insert(0,str(SYSTEM))
from tests.test_common_content_r58 import record,ORDER
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import make_handler
from app.knowledge.common.registry import CATALOG
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.planner import plan_fields
from app.pipeline.request_deadline import request_deadline
DB=B/'OWNER_HTTP_DEMO_ONLY_2.sqlite'
store=CommonStore(DB)
if DB.exists():raise SystemExit('Use a new output; never overwrite earlier demo.')
store.initialize(allow_demo=True)
server=ThreadingHTTPServer(('127.0.0.1',18097),make_handler(store,'r62-fixture-only','r62-fixture',18097))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
def api(path,body=None):
 req=Request('http://127.0.0.1:18097'+path,data=json.dumps(body).encode() if body is not None else None,headers={'Authorization':'Bearer r62-fixture-only','Content-Type':'application/json'})
 with urlopen(req,timeout=30) as response:return json.load(response)
saved={};mapping={};results=[]
for kind in ORDER:mapping['fixture_'+kind]=api('/api/template?kind='+kind)['record_id']
for kind in ORDER:
 r=record(kind,mapping['fixture_'+kind]);r['aliases']={'th':['เดโมใหม่ '+kind],'en':['R62 demo '+kind]}
 for spec in CATALOG[kind]['fields']:
  if spec['reference_kind']:
   f=r['fields'][spec['key']]
   if f['status']=='known':
    f['value']=[mapping[x] for x in f['value']] if isinstance(f['value'],list) else mapping.get(f['value'],f['value'])
 if kind=='faq':
  r['fields']['question']['value']={'th':'เดโม: ให้เพื่อนมารับบัตรทดลองแทนได้ไหม','en':'DEMO: Can a friend collect my trial pass?'}
  r['fields']['answer']['value']={'th':'DEMO เท่านั้น: ผู้รับต้องแสดงบัตรทดลองของตนเอง','en':'DEMO ONLY: The collector must show their own trial pass.'}
  r['fields']['scope_note'].update(status='known',value={'th':'ใช้เฉพาะการรับบัตรทดลองสมมุติ','en':'Applies only to fictional trial-pass collection'})
 x=api('/api/save',{'record':r,'expected_version':0,'attest':True,'translation_reviewed':True});saved[kind]=x
before=api('/api/preview',{'question':'R62 demo game how_to_play','locale':'en'})
draft=api('/api/preview',{'question':'R62 demo game how_to_play','locale':'en','draft':True})
assert before['trace'] is None and 'DRAFT PREVIEW' in draft['answer']
for x in saved.values():api('/api/approve',{'id':x['record_id'],'version':x['version'],'hash':x['hash'],'confirm':True})
published=api('/api/publish',{'ids':list(mapping.values()),'expected_active':api('/api/status')['active'],'request_key':uuid.uuid4().hex})
reader=CommonAnswerer(store)
KEYS={'center':'name','zone':'room_seats','equipment_model':'name','resource':'operational_status','service':'session_minutes','game':'how_to_play','audience':'required_proofs','contact':'value','procedure':'steps','policy':'decision','facility':'name','game_service':'offered','game_mode':'players_max','control_set':'bindings','rate':'amount_minor','rental_package':'equipment_included','schedule':'bookable_periods','closure':'state','competition':'rulebook_release','competition_rule':'text','news':'body','person':'role','faq':'answer','live_binding':'freshness_policy'}
with (B/'OWNER_HTTP_RESULTS.jsonl').open('x',encoding='utf-8') as log:
 for kind,key in KEYS.items():
  for lang in ['th','en']:
   a=reader.answer(('เดโมใหม่ ' if lang=='th' else 'R62 demo ')+kind+' '+key,locale=lang)
   obs=a.decision_artifact['obligations'] if a else []
   ok=any(x['record_id']==mapping['fixture_'+kind] and x['field']==key for x in obs)
   row={'kind':kind,'lang':lang,'passed':ok,'answer':a.answer if a else None,'artifact':a.decision_artifact if a else None}
   results.append(row);log.write(json.dumps(row,ensure_ascii=False)+'\n');log.flush()
 # Editing uses the same ID, creates a new immutable revision and keeps the old
 # published answer until publish. Reader was created before the edits.
 r=copy.deepcopy(saved['game']['record']);r['fields']['how_to_play']['value']['en']='DEMO revised: find the coral exit'
 x=api('/api/save',{'record':r,'expected_version':1,'attest':True,'translation_reviewed':True})
 assert 'Collect pearls' in reader.answer('R62 demo game how_to_play',locale='en').answer
 api('/api/approve',{'id':x['record_id'],'version':x['version'],'hash':x['hash'],'confirm':True})
 api('/api/publish',{'ids':[x['record_id']],'expected_active':published['release_id'],'request_key':uuid.uuid4().hex})
 assert 'find the coral exit' in reader.answer('R62 demo game how_to_play',locale='en').answer
summary={'created_kinds':24,'queries':48,'passed':sum(r['passed'] for r in results),'draft_not_published':True,'same_reader_sees_new_release':True,'revision_preserved':True,'real_owner_data_changed':False,'actual_authenticated_http':True,'semantics_test':'canonical field names, not a natural-language accuracy claim'}
(B/'OWNER_HTTP_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(summary,flush=True)
# Leave the fixture editor available for browser inspection while parent works.
(B/'OWNER_FIXTURE_READY.json').write_text(json.dumps({'port':18097,'database':str(DB),'url':'http://127.0.0.1:18097/#token=r62-fixture-only'}),encoding='utf-8')
if '--serve' in sys.argv:
 while not (B/'STOP_OWNER_FIXTURE').exists():time.sleep(.5)
server.shutdown();server.server_close()
