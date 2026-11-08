"""Actual HTTP handler and pipeline in memory; no socket/network transport claim."""
import hashlib,io,json,os,sqlite3,sys,time,uuid
from pathlib import Path
B=Path(__file__).resolve().parent;S=B/'system';tag=sys.argv[1] if len(sys.argv)>1 else 'initial';llm=(len(sys.argv)>2 and sys.argv[2]=='1')
T=B/'verification'/tag;T.mkdir(parents=True,exist_ok=False)
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_BILINGUAL_EN_ENABLED='1',PSU_LOCAL_LLM_ASSIST_ENABLED='1' if llm else '0',PSU_EXPERIMENTAL_ALLOW_LLM='1' if llm else '0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_R69_LAUNCH_TOKEN='fixture-launch-token',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='20',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='18',PSU_RUNTIME_PROFILE='new-common-chat-r69-test')
os.environ.update(PSU_INPUT_QUALITY_GUARD_MODE='enforce',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue')
sys.path.insert(0,str(S))
from app.web_api import server
from app.session.conversation_store import STORE
from app.booking import live_status as live
from app.runtime import fast_answer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import validate
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
server.INPUT_QUALITY_GUARD=RuntimeInputQualityGuard.from_environment()

db=S/'data/knowledge/common.sqlite'
original_hash=hashlib.sha256(db.read_bytes()).hexdigest();oldseed_hash=hashlib.sha256((B/'seed_R68_preserved.sqlite').read_bytes()).hexdigest()
class MemoryConnection:
 def __init__(self,raw):self.input=io.BytesIO(raw);self.output=bytearray()
 def makefile(self,mode,*args,**kwargs):return self.input
 def sendall(self,data):self.output.extend(data)
class FakeServer:
 chat_jobs=None;job_ttl_sec=None;server_port=8101
 def __init__(self):self.stopped=False
 def shutdown(self):self.stopped=True
fake_server=FakeServer()
def request(path,payload=None,*,method='POST',headers=None):
 body=json.dumps(payload or {},ensure_ascii=False).encode('utf8') if method=='POST' else b''
 hs={'Host':'127.0.0.1:8101','Content-Type':'application/json','Content-Length':str(len(body)),'Connection':'close',**(headers or {})}
 wire=(f'{method} {path} HTTP/1.1\r\n'+''.join(k+': '+v+'\r\n' for k,v in hs.items())+'\r\n').encode()+body
 conn=MemoryConnection(wire);server.ChatHandler(conn,('127.0.0.1',12345),fake_server)
 head,_,data=bytes(conn.output).partition(b'\r\n\r\n');status=int(head.split(b' ',2)[1])
 return status,json.loads(data) if 'application/json' in head.decode('latin1') else data.decode('utf8')
rows=[]
def check(name,ok,detail=None):rows.append({'case':name,'passed':bool(ok),'detail':detail});print(json.dumps({'case':name,'passed':bool(ok)},ensure_ascii=False),flush=True)
def ask(q,lang='th',session=None,need=(),forbid=()):
 session=session or 'session-'+uuid.uuid4().hex
 payload={'question':q,'locale':lang,'client_session_id':session,'client_turn_id':'turn-'+uuid.uuid4().hex,'debug':True}
 status,r=request('/api/chat',payload);txt=r.get('answer','')
 errors=[]
 if status!=200 or not r.get('ok'):errors.append('HTTP:'+str(status))
 if not r.get('validation_ok'):errors.append('validation_rejected')
 for n in need:
  if n.casefold() not in txt.casefold():errors.append('missing:'+n)
 for f in forbid:
  if f.casefold() in txt.casefold():errors.append('forbidden:'+f)
 migration=r.get('knowledge',{})
 # Scope refusals can happen before the knowledge dispatcher, by design.
 if r.get('route_intent')!='studio_information_scope':
  if migration.get('profile')!='r69-migration-preview':errors.append('wrong_profile')
  if migration.get('legacy_fallback_used') is not False:errors.append('fallback_not_excluded')
  if migration.get('production_publication_verified') is not False:errors.append('incorrect_publication_claim')
 check(q,not errors,{'request':payload,'status':status,'errors':errors,'response':r})
 return session,r

status,h=request('/health',method='GET');check('health identifies new installation',status==200 and h['runtime']['knowledge_profile']=='r69-migration-preview',h)
status,html=request('/',method='GET');check('chat page and draft-data banner',status==200 and 'migration-banner' in html and 'R69' in html)
for path in ['/app.js','/chat_request.js','/styles.css']:
 status,body=request(path,method='GET');check('static asset '+path,status==200 and bool(body))
with CommonStore(db).connect() as c:
 rs=CommonStore.heads(c);sources=CommonStore.sources(c)
 check('copied dataset has 602 heads',len(rs)==602)
 check('dataset source/schema validates',not any(validate(r,rs,sources) for r in rs.values()))
 check('no approvals fabricated',c.execute('select count(*) from cc_approvals').fetchone()[0]==0)
 check('no release silently activated',dict(c.execute('select key,value from cc_meta')).get('active')=='')
ask('สวัาดี',need=['PSU Esports'])
ask('Hello',lang='en',need=['PSU Esports'])
ask('PS5 มีเกมอะไรบ้าง',need=['17','God of War'],forbid=['Animal Crossing'])
ask('List all games on PC',lang='en',need=['6','Counter-Strike'],forbid=['Mario Kart'])
ask('Animal Crossing: New Horizons คำบรรยายต้นฉบับ',need=['เซอร์ไพรส์ใหม่ ๆ ได้ตลอดทั้งปี'])
ask('What is the official description of Animal Crossing: New Horizons?',lang='en',need=['throughout the year'])
ask('Gaming PC รุ่น MSI MAG Infinite S3 14th สเปกอะไรบ้าง',need=['Intel Core i5-14400','DDR5 32GB','RTX 5060 8GB'])
ask('กฏตอนเเข่ง cs2 มีอะไรมั่ง',need=['Counter-Strike'],forbid=['VALORANT'])
ask('TEKKEN 8 การแก้ข้อพิพาททำยังไง',need=['กรรมการ','สิ้นสุด'],forbid=['VALORANT'])
ask('Parking location',lang='en',need=['Building 5'])
ask('Change a wrongly booked machine steps',lang='en',need=['Cancel','email','new booking'])
ask('ศูนย์อยู่ timezone อะไร',need=['Asia/Bangkok'])
sid,r=ask('PC มีหมายเหตุอะไรบ้าง',need=['Warzone'])
ask('แล้ว PS5 ล่ะ',session=sid,need=['PlayStation 5 #01 และ #02'],forbid=['PC #03'])
sid,r=ask('General Adult PC 2 ชั่วโมงกี่บาท',need=['140.00'])
ask('ถ้าเป็นศิษย์เก่าล่ะ',session=sid,need=['50.00'],forbid=['140.00'])
sid,r=ask('List all controls for eFootball on PlayStation / PS5.',lang='en',need=['Dash'])
ask('What does R2 do?',lang='en',session=sid,need=['Dash'],forbid=['Low Pass'])
ask('เย็นนี้กินอะไรดี',need=[],forbid=['อาหารแนะนำ','Pizza','พิซซ่า'])
ask('ลืมออกจาก Steam ศูนย์รับผิดชอบคืนเงินทั้งหมดไหม',need=[],forbid=['คืนเงินเต็มจำนวน','full refund guaranteed'])
# Existing validated read-only live adapter with a deterministic status fixture.
original_getter=fast_answer.get_live_booking_status
snapshot=live.LiveBookingSnapshot(ok=True,date='2026-10-20',now='2026-10-20T10:00:00+07:00',generated_at='2026-10-20T10:00:00+07:00',source='fixture_only',center_open=True,center_reason='fixture open',open_periods=(('09:00','12:00'),('13:00','16:00')),resources=(live.LiveResource('pc_1','PC #1',1,'available',1,(live.LiveSlot('10:00','11:00','available',0,0,1),)),live.LiveResource('pc_2','PC #2',1,'booked',0,(live.LiveSlot('10:00','11:00','booked',1,0,0),))),transport='fixture')
fast_answer.get_live_booking_status=lambda selected:snapshot
ask('PC1 วันที่ 2026-10-20 เวลา 10:00 ว่างไหม',need=['ว่าง'])
ask('Is PC2 available at 10:00 on 2026-10-20?',lang='en',need=['not available','10:00-11:00'],forbid=['is available for'])
fast_answer.get_live_booking_status=lambda selected:live._unavailable(selected,'controlled transport unavailable',error_code='fixture_offline')
ask('PC1 วันที่ 2026-10-20 เวลา 10:00 ว่างไหม',need=['ยังยืนยัน'],forbid=['ว่าง 1/1'])
fast_answer.get_live_booking_status=original_getter
status,r=request('/api/chat',{'question':''});check('empty input rejected',status==400 and r.get('error')=='question_required',r)
status,r=request('/api/chat/jobs',{'question':'hello'});check('disabled queue uses existing fallback protocol',status==404 and r.get('error')=='jobs_disabled',r)
status,r=request('/api/shutdown',{},headers={'X-PSU-Launch-Token':'wrong-token'});check('other launcher cannot stop this chat',status==403 and not fake_server.stopped,r)
status,r=request('/api/shutdown',{},headers={'X-PSU-Launch-Token':'fixture-launch-token'});time.sleep(.05);check('own launcher graceful stop',status==200 and fake_server.stopped,r)
check('chat did not modify knowledge DB',original_hash==hashlib.sha256(db.read_bytes()).hexdigest())
check('preserved R68 seed unchanged',oldseed_hash==hashlib.sha256((B/'seed_R68_preserved.sqlite').read_bytes()).hexdigest())
summary={'cases':len(rows),'passed':sum(r['passed'] for r in rows),'failed':[r['case'] for r in rows if not r['passed']],'llm_flag':llm,'scope':'Actual HTTP request handler + real pipeline, in-memory connection; no TCP listener, browser, real WordPress or successful model transport claim','details':rows}
(T/'RESULTS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,default=str),encoding='utf8')
print(json.dumps({k:v for k,v in summary.items() if k!='details'},ensure_ascii=False))
raise SystemExit(bool(summary['failed']))
