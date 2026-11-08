"""Actual handler/state/source checks in memory; no model mock, no TCP claim."""
import hashlib,io,json,os,sys,time,uuid,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
S=Path(sys.argv[1]).resolve();T=B/sys.argv[2];T.mkdir(exist_ok=False)
db=S/'system/data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_PIPELINE_WARMUP='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_CHAT_LOG_SQLITE='1',PSU_CHAT_LOG_LOCAL_JSONL='1')
sys.path.insert(0,str(S/'system'))
from app.web_api import server
from app.pipeline.llm_health import llm_health_snapshot
from app.knowledge.common.store import CommonStore
with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as c:kinds=dict(c.execute('select record_id,kind from cc_heads'))
class Conn:
 def __init__(self,raw):self.input=io.BytesIO(raw);self.output=bytearray()
 def makefile(self,*a,**kw):return self.input
 def sendall(self,data):self.output.extend(data)
class FakeServer:chat_jobs=None;job_ttl_sec=None;server_port=8113
def api(q,lang,sid):
 body=json.dumps({'question':q,'locale':lang,'client_session_id':sid,'client_turn_id':uuid.uuid4().hex,'debug':True}).encode()
 raw=('POST /api/chat HTTP/1.1\r\nHost: 127.0.0.1:8113\r\nContent-Type: application/json\r\nContent-Length: '+str(len(body))+'\r\nConnection: close\r\n\r\n').encode()+body
 conn=Conn(raw);t=time.perf_counter();server.ChatHandler(conn,('127.0.0.1',12000),FakeServer());headers,_,data=bytes(conn.output).partition(b'\r\n\r\n')
 return json.loads(data),round(time.perf_counter()-t,3),headers.decode().splitlines()[0]
RID='migrated_owner_claim_personal_keyboard_mouse'
# Each turn states its expected user goal before observing output.
CASES=[
 ('en-personal','en',[("Can I bring my own input peripheral?",'pending'),("Yes, but it is my own keyboard.",'personal'),('And my mouse?','personal')]),
 ('th-personal','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ใช่ แต่เป็นเมาส์ของผม','personal'),('คีย์บอร์ดด้วยได้ไหม','personal')]),
 ('en-studio','en',[("Can I bring my own input peripheral?",'pending'),("Yes, but it is the studio\'s keyboard.",'not_personal'),('yes','not_personal'),('Can I bring my own keyboard?','personal')]),
 ('th-competition','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ใช่ แต่ใช้ตอนแข่ง','competition_clarify'),('VALORANT','competition')]),
 ('en-payment-new','en',[("Can I bring my own input peripheral?",'pending'),('Yes, but how do I pay for my booking?','payment'),('And when?','deadline')]),
 ('th-payment-new','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ใช่ แต่หลังจองต้องจ่ายภายในกี่นาที','deadline')]),
 ('en-rejection','en',[('I attached incorrect proof of payment. How do I fix it?','pending'),('No, I mean how do I pay?','payment'),('And when?','deadline')]),
 ('th-unknown','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ใช่ แต่ผ่อนชำระได้ไหม','installments'),('ใช่','not_personal')]),
 ('en-condition','en',[("Can I bring my own input peripheral?",'pending'),('Yes, but it is my wireless keyboard.','not_personal')]),
 ('prices-th','th',[('ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก','price_scope'),('ทั้งหมด','all_rates'),('PC','pc_rate')]),
 ('prices-en','en',[('What are the service prices for visitors?','price_scope'),('all','all_rates'),('PC','pc_rate')]),
 ('en-competition','en',[("Can I bring my own input peripheral?",'pending'),('Yes, but it is for a tournament.','competition_clarify'),('VALORANT','competition')]),
 ('en-follow-property','en',[("Can I bring my own input peripheral?",'pending'),('Yes, but it is my own keyboard.','personal'),('And my wireless mouse?','not_personal')]),
]
rows=[]
for case,lang,turns in CASES:
 sid='r78-'+uuid.uuid4().hex
 for turn,(q,expect) in enumerate(turns,1):
  r,elapsed,status=api(q,lang,sid);a=r.get('answer','');art=r.get('decision_artifact') or {};p=art.get('query_plan') or {};ids=set(p.get('record_ids',[]))|{x['record_id'] for x in p.get('response_projection',[]) if x.get('fields')};ks={kinds.get(i) for i in ids};state=r.get('common_read_state') or {};errors=[]
  if '200' not in status or not a:errors.append('http_or_empty')
  if expect=='pending' and not state.get('profile_confirmation'):errors.append('missing_pending')
  if expect=='personal' and (RID not in ids or not any(x in a for x in ['ไม่อนุญาต','not allowed'])):errors.append('missing_personal_rule')
  if expect in {'not_personal','competition_clarify','installments'} and RID in ids:errors.append('unqualified_personal_rule')
  if expect=='competition_clarify' and not ('แข่งขัน' in a or 'tournament' in a):errors.append('missing_competition_clarification')
  if expect=='competition' and not ks.intersection({'competition','competition_rule'}):errors.append('lost_competition_context')
  if expect=='payment' and '795-276244-1' not in a:errors.append('missing_payment_source')
  if expect=='deadline' and ('10' not in a or '795-276244-1' in a):errors.append('wrong_deadline_projection')
  if expect=='installments' and p.get('unconfirmed_topic')!='installments':errors.append('wrong_unknown_topic')
  if expect=='price_scope' and not ('rate' in ks or state.get('pending_selection') or state.get('profile_confirmation') or 'PC' in a):errors.append('missing_price_scope')
  if expect=='all_rates' and (not {'PC','VR','Cockpit'}.issubset({x for x in ['PC','VR','Cockpit'] if x in a}) or 'rate' not in ks):errors.append('missing_all_rate_scope')
  if expect=='all_rates' and ('525.00' in a or '150.00' in a or not any(x in a for x in ['หมดอายุ','not effective'])):errors.append('expired_rate_asserted_or_omitted')
  if expect=='pc_rate' and ('rate' not in ks or 'PC' not in a):errors.append('missing_pc_rate')
  row={'case':case,'turn':turn,'question':q,'locale':lang,'expect':expect,'passed':not errors,'errors':errors,'seconds_internal_only':elapsed,'http_status_internal':status,'response':r};rows.append(row)
  with (T/'TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
  print(json.dumps({k:v for k,v in row.items() if k!='response'},ensure_ascii=False),flush=True)
health=llm_health_snapshot();(T/'MODEL_HEALTH.json').write_text(json.dumps(health,ensure_ascii=False,indent=2),encoding='utf8')
summary={'count':len(rows),'passed':sum(x['passed'] for x in rows),'failed':[{k:v for k,v in x.items() if k!='response'} for x in rows if not x['passed']],'llm_enabled':True,'model_mocked':False,'tcp_browser_verified':False,'wordpress_verified':False,'source':str(S),'data_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest(),'database_sha256':before}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(summary,ensure_ascii=False));raise SystemExit(any(not x['passed'] for x in rows))
