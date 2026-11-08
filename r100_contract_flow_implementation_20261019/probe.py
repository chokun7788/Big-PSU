"""Focused real-pipeline probes in the copied candidate; no production writes."""
import argparse,dataclasses,hashlib,json,os,time,urllib.request
from pathlib import Path
from run_common import configure

R=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--tag',required=True);parser.add_argument('--llm',action='store_true');args=parser.parse_args()
out=R/args.tag;out.mkdir(exist_ok=False);os.environ['PSU_R88_RUN_TAG']=args.tag;configure('probe')
def manifest():return {p.relative_to(R/'system').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
before=manifest();(out/'SOURCE_BEFORE.json').write_text(json.dumps(before,indent=2),'utf8')
calls=[];native_urlopen=urllib.request.urlopen
def observed(req,*a,**kw):
    url=getattr(req,'full_url',str(req));model=':11434/' in url;entry={'url':url,'response_opened':False};t=time.perf_counter()
    if model:calls.append(entry)
    try:
        response=native_urlopen(req,*a,**kw);entry['response_opened']=True;return response
    except Exception as exc:entry.update(error_type=type(exc).__name__,error=str(exc));raise
    finally:entry['elapsed_sec']=time.perf_counter()-t
urllib.request.urlopen=observed
from app.pipeline.engine import answer_question_pipeline_debug
from app.knowledge.common.dialogue import state_from_answer
from app.booking import live_status
from app.runtime import fast_answer
def unavailable(d):return live_status._unavailable(d,'R98 focused fixture; no live occupancy oracle',error_code='fixture_offline')
live_status.get_live_booking_status=unavailable;fast_answer.get_live_booking_status=unavailable
qs=[('en','I am planning a visit and would like to know: Please tell me: Can I get a refund'),
    ('th','ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ตอนเย็นเปิดถึงกี่โมง'),
    ('th','VALORANT ใช้ผู้เล่นกี่คน'),('th','ROV ถ้าเกมหลุดทำยังไง'),
    ('th','ศูนย์อยู่ที่ไหน แล้วราคาเท่าไร'),('th','ต้องการทราบราคาบุคคลภายนอกทั้งหมด'),
    ('en','What are all the prices for external visitors?'),
    ('th','Animal Crossing: New Horizons กับ FINAL FANTASY XVI คือเกมอะไร'),
    ('en','What is Animal Crossing: New Horizons and what is FINAL FANTASY XVI?'),
    ('th','PC มีอุปกรณ์อะไรบ้าง'),('en','What equipment is available in the PC Zone?'),
    ('th','วันนี้เปิดไหม'),('th','PC ว่างไหม แล้วจองยังไง'),
    ('en','Can I bring my own food into the studio?'),
    ('th','อยากทราบวันและเวลาที่ศูนย์ให้บริการสำหรับการจอง'),
    ('en','A question about the studio: Can I book Monday morning, or only the afternoon?'),
    ('en','Before visiting, I need to know: On which days can I book morning and afternoon slots?')]
rows=[]
def ask(q,locale,history=None):
    calls.clear();t=time.perf_counter();result=answer_question_pipeline_debug(q,locale=locale,experimental_rag_fallback=False,experimental_allow_llm=args.llm,global_timeout_sec=20,recent_history=history or [])
    row={'question':q,'locale':locale,'history':history or [],'elapsed':time.perf_counter()-t,'result':dataclasses.asdict(result),'observed_model_http_calls':list(calls)};rows.append(row)
    with (out/'ANSWERS.jsonl').open('a',encoding='utf-8') as h:h.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
    print(json.dumps({'question':q,'mode':result.mode,'answer':result.answer[:650],'errors':result.validation.errors},ensure_ascii=False),flush=True)
    return result
for locale,q in qs:ask(q,locale)
for locale,q,choices in [('th','ต้องการทราบราคาบุคคลภายนอก',['PC','ทั้งหมด']),('en','I want prices for external visitors',['PC','all'])]:
    first=ask(q,locale)
    hist=[{'role':'user','text':q},{'role':'assistant','text':first.answer,'common_read_state':state_from_answer(first),'delivery_status':'server_written'}]
    for choice in choices:ask(choice,locale,hist)
after=manifest();(out/'SOURCE_AFTER.json').write_text(json.dumps(after,indent=2),'utf8')
(out/'RESULT.json').write_text(json.dumps({'requests':len(rows),'llm':args.llm,'source_unchanged':before==after,'model_attempts':sum(len(r['observed_model_http_calls']) for r in rows),'model_response_opened':sum(c['response_opened'] for r in rows for c in r['observed_model_http_calls']),'scope':'focused probes; answers require source review, not accuracy score'},indent=2),encoding='utf-8')
