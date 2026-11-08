"""Related opening-status checks. Candidate overlay; real common DB read-only."""
import hashlib,json,os,sys,time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parent;T=B/sys.argv[1];T.mkdir(exist_ok=False)
S=B.parent/'r78_web_session_check_20261016/system';db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0')
sys.path.insert(0,str(S))
if len(sys.argv)>2 and sys.argv[2]=='candidate':
 import app.knowledge.common as pkg
 pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
from app.calendar import service_calendar
from app.core.locale import LocaleDecision
from app.pipeline.migrated_chat import answer
cases=[
 ('2026-10-17T13:30:00+07:00','วันนี้เปิดไหม','th','closed','วันนี้วันที่ 17 ตุลาคม 2569 ไม่เปิดให้บริการครับ'),
 ('2026-10-17T13:30:00+07:00','Is the studio open today?','en','closed','Today, 17 October 2026, the studio is closed.'),
 ('2026-10-17T13:30:00+07:00','วันนี้ปิดไหมครับ','th','closed',None),
 ('2026-10-17T13:30:00+07:00','วันนี้เปิดให้บริการไหม','th','closed',None),
 ('2026-10-17T13:30:00+07:00','Are you closed today?','en','closed',None),
 ('2026-10-17T13:30:00+07:00','พรุ่งนี้เปิดไหม','th','closed','วันที่ 18 ตุลาคม 2569 ไม่เปิดให้บริการครับ'),
 ('2026-10-17T13:30:00+07:00','Are you open tomorrow?','en','closed','On 18 October 2026, the studio is closed.'),
 ('2026-10-19T09:00:00+07:00','วันนี้เปิดไหม','th','open',None),
 ('2026-10-19T13:00:00+07:00','Is the studio open today?','en','open',None),
 ('2026-10-20T12:30:00+07:00','วันนี้เปิดไหม','th','open',None),
 ('2026-10-23T13:30:00+07:00','วันนี้เปิดไหม','th','open',None),
 ('2026-10-17T13:30:00+07:00','วันที่ 2026-07-28 เปิดไหม','th','closed','วันที่ 28 กรกฎาคม 2569 ไม่เปิดให้บริการครับ'),
 ('2026-10-17T13:30:00+07:00','Is the studio open on 2026-07-29?','en','closed',None),
 ('2026-10-17T13:30:00+07:00','วันที่ 2026-07-30 เปิดไหม','th','closed',None),
 ('2026-10-17T13:30:00+07:00','วันจันทร์เปิดไหม','th','open',None),
 ('2026-10-17T13:30:00+07:00','Is the studio open on Monday?','en','open',None),
 ('2026-10-16T16:59:00+00:00','วันนี้เปิดไหม','th','open','วันนี้วันที่ 16 ตุลาคม 2569 เปิดให้บริการครับ'),
 ('2026-10-16T17:01:00+00:00','วันนี้เปิดไหม','th','closed','วันนี้วันที่ 17 ตุลาคม 2569 ไม่เปิดให้บริการครับ'),
]
rows=[]
for at,q,lang,status,exact in cases:
 frozen=datetime.fromisoformat(at);service_calendar.now_bangkok=lambda:frozen
 r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'test'),history=[],allow_llm=True);p=(r.decision_artifact or {}).get('query_plan',{});errors=[]
 if p.get('day_status')!=status:errors.append('wrong_status_or_method')
 if exact and r.answer!=exact:errors.append('wrong_display')
 if len(r.answer)>160 or '\n' in r.answer:errors.append('not_concise')
 if not r.validation.ok or not r.hits:errors.append('validation_or_evidence')
 row={'question':q,'locale':lang,'now':at,'expected_status':status,'passed':not errors,'errors':errors,'answer':r.answer,'plan':p,'hits':r.hits};rows.append(row)
 with (T/'ANSWERS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(json.dumps({k:v for k,v in row.items() if k not in {'plan','hits'}},ensure_ascii=False),flush=True)
result={'count':len(rows),'passed':sum(r['passed'] for r in rows),'data_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest(),'llm_enabled':True,'model_inference_verified':False,'tcp_browser_verified':False}
(T/'SUMMARY.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result));raise SystemExit(any(not r['passed'] for r in rows))
