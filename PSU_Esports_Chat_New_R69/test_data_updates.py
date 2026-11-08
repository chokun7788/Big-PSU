"""Isolated data edits through CommonStore, then normal chat HTTP handler.

Only verification/update01 gets test records. The actual copied DB is never edited.
No owner attestation, approval or production publication is fabricated.
"""
import hashlib,io,json,os,sqlite3,sys,uuid
from pathlib import Path

B=Path(__file__).resolve().parent
S=B/'system'
T=B/'verification'/sys.argv[1]
T.mkdir(parents=True,exist_ok=False)
test_system=T/'system'
db=test_system/'data/knowledge/common.sqlite'
db.parent.mkdir(parents=True)
real_db=S/'data/knowledge/common.sqlite'
before=hashlib.sha256(real_db.read_bytes()).hexdigest()
with sqlite3.connect(real_db) as src,sqlite3.connect(db) as dest:src.backup(dest)
os.environ.update(PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_EXPERIMENTAL_ALLOW_LLM='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_BILINGUAL_EN_ENABLED='1')
sys.path.insert(0,str(S))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template,now
from app.knowledge.records import canonical_json
from app.knowledge.common import migrated_view
from app.web_api import server
# The fixture is a complete isolated installation root. Keep the path guard.
migrated_view.SYSTEM_ROOT=test_system.resolve()
store=CommonStore(db)
rows=[]
def check(name,ok,detail=None):
 rows.append({'case':name,'passed':bool(ok),'detail':detail})
 print(json.dumps({'case':name,'passed':bool(ok)},ensure_ascii=False),flush=True)
class Connection:
 def __init__(self,raw):self.input=io.BytesIO(raw);self.output=bytearray()
 def makefile(self,*a,**kw):return self.input
 def sendall(self,b):self.output.extend(b)
class Host:
 chat_jobs=None;job_ttl_sec=None;server_port=8101
def ask(q,lang,expected,forbid=None):
 body=json.dumps({'question':q,'locale':lang,'client_session_id':uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'debug':True},ensure_ascii=False).encode()
 raw=(f'POST /api/chat HTTP/1.1\r\nHost: 127.0.0.1:8101\r\nContent-Type: application/json\r\nContent-Length: {len(body)}\r\nConnection: close\r\n\r\n').encode()+body
 conn=Connection(raw);server.ChatHandler(conn,('127.0.0.1',12345),Host())
 header,_,data=bytes(conn.output).partition(b'\r\n\r\n');result=json.loads(data)
 text=result.get('answer','')
 check(q,int(header.split(b' ',2)[1])==200 and result.get('validation_ok') and expected in text and (not forbid or forbid not in text) and result.get('knowledge',{}).get('legacy_fallback_used') is False,result)
 return result
record=template('faq')
record.update(record_id='fixture_r69_arrival_info',aliases={'th':['คู่มือมาใช้ศูนย์ครั้งแรก R69'],'en':['R69 first visit guide']})
record['localization'].update(en_status='agent_translated')
def save(revision,answer):
 values={'question':{'th':'คู่มือมาใช้ศูนย์ครั้งแรก R69','en':'R69 first visit guide'},'answer':answer,'topic':'visitor_information','scope_note':{'th':'ตัวอย่างทดสอบแยก ไม่ใช้เป็นข้อมูลศูนย์จริง','en':'Isolated test fixture, not production center information'}}
 snapshot=canonical_json(values);sid='fixture_r69_arrival_v'+str(revision)
 source={'source_id':sid,'kind':'derived_curated','path':'verification-fixture://'+sid,'sha256':hashlib.sha256(snapshot.encode()).hexdigest(),'authority_for':['faq'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
 store.add_source(source,snapshot,actor='automated-isolated-fixture')
 for key,val in values.items():record['fields'][key]={'status':'known','value':val,'evidence_refs':[{'source_id':sid,'locator':'/'+key}],'note':'Isolated fixture only'}
 return store.save(record,actor='automated-isolated-fixture',expected_version=revision-1,change_note='Fixture revision only; no production changes')
save(1,{'th':'ศูนย์อยู่ที่อาคาร 5 ชั้น 1','en':'The studio is in Building 5, floor 1.'})
ask('คู่มือมาใช้ศูนย์ครั้งแรก R69','th','อาคาร 5 ชั้น 1')
ask('R69 first visit guide','en','Building 5, floor 1')
old_snapshot=migrated_view.MigratedView(db).snapshot()
save(2,{'th':'จอดรถยนต์และมอเตอร์ไซค์ได้หน้าตึก 5','en':'Car and motorcycle parking is available in front of Building 5.'})
check('read view invalidates previous epoch',not migrated_view.MigratedView(db).still_current(old_snapshot))
ask('คู่มือมาใช้ศูนย์ครั้งแรก R69','th','หน้าตึก 5','ชั้น 1')
ask('R69 first visit guide','en','in front of Building 5','floor 1')
check('stable ID has new revision and preserves previous revision',store.get(record['record_id'])['record']['revision']==2 and store.revision(record['record_id'],1)['record']['fields']['answer']['value']['th']=='ศูนย์อยู่ที่อาคาร 5 ชั้น 1')
with store.connect() as c:
 check('fixture did not fabricate approvals or active release',c.execute('select count(*) from cc_approvals').fetchone()[0]==0 and dict(c.execute('select key,value from cc_meta'))['active']=='')
check('real new-chat DB unchanged',before==hashlib.sha256(real_db.read_bytes()).hexdigest())
result={'cases':len(rows),'passed':sum(r['passed'] for r in rows),'scope':'Isolated fixture DB; actual chat HTTP handler in memory; no real socket or owner approval claim','details':rows}
(T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='details'},ensure_ascii=False))
raise SystemExit(any(not r['passed'] for r in rows))
