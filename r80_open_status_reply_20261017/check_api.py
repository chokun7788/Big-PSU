import io,json,os,sys,uuid,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;T=B/'api01';T.mkdir(exist_ok=False);S=B.parent/'r78_web_session_check_20261016/system';db=S/'data/knowledge/common.sqlite'
before=hashlib.sha256(db.read_bytes()).hexdigest()
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_ESPORTS_NOW='2026-10-17T13:30:00+07:00',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_PIPELINE_WARMUP='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0')
sys.path.insert(0,str(S));from app.web_api import server
class Conn:
 def __init__(self,raw):self.input=io.BytesIO(raw);self.output=bytearray()
 def makefile(self,*a,**kw):return self.input
 def sendall(self,data):self.output.extend(data)
class FakeServer:chat_jobs=None;job_ttl_sec=None;server_port=8115
rows=[];sid='r80-'+uuid.uuid4().hex
for q,lang,expected in [('วันนี้เปิดไหม','th','วันนี้วันที่ 17 ตุลาคม 2569 ไม่เปิดให้บริการครับ'),('พรุ่งนี้เปิดไหม','th','วันที่ 18 ตุลาคม 2569 ไม่เปิดให้บริการครับ'),('Is the studio open today?','en','Today, 17 October 2026, the studio is closed.')]:
 payload={'question':q,'locale':lang,'client_session_id':sid if lang=='th' else sid+'-en','client_turn_id':uuid.uuid4().hex,'debug':True};body=json.dumps(payload).encode()
 raw=('POST /api/chat HTTP/1.1\r\nHost: 127.0.0.1:8115\r\nContent-Type: application/json\r\nContent-Length: '+str(len(body))+'\r\nConnection: close\r\n\r\n').encode()+body
 c=Conn(raw);server.ChatHandler(c,('127.0.0.1',12000),FakeServer());header,_,data=bytes(c.output).partition(b'\r\n\r\n');r=json.loads(data)
 rows.append({'question':q,'passed':r.get('answer')==expected and r.get('validation_ok') is True and (r.get('decision_artifact') or {}).get('query_plan',{}).get('method')=='common_calendar_open_status','response':r})
 with (T/'TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(rows[-1],ensure_ascii=False,default=str)+'\n')
result={'count':len(rows),'passed':sum(x['passed'] for x in rows),'data_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest(),'handler_in_memory':True,'running_browser_server_verified':False}
(T/'SUMMARY.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result));raise SystemExit(any(not x['passed'] for x in rows))
