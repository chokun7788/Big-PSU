"""R81 controlled selector tests. No real model/network accuracy claim."""
import hashlib,json,os,sys,time
from pathlib import Path
from unittest.mock import patch,Mock
from urllib.error import URLError
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_CHAT_LOG_DIR=str(T/'logs'))
sys.path.insert(0,str(S))
import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/('before' if 'baseline' in sys.argv else 'candidate')/'app/knowledge/common'))
from app.knowledge.common import entity_search as e
from app.knowledge.common.migrated_view import MigratedView
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.knowledge.common.dialogue import state_from_answer
release=MigratedView(db).snapshot()['release'];records=release['records'];names=release['names']
checks=[]
def check(name,ok,detail=None):
    row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
    with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
    print(json.dumps({'case':name,'passed':bool(ok)},ensure_ascii=False),flush=True)

# Gate and HTTP stubs deliberately do not measure real model latency.
class Response:
    def __init__(self,value):self.raw=json.dumps(value).encode()
    def __enter__(self):return self
    def __exit__(self,*args):return False
    def read(self,n):return self.raw[:n]

Q='Can I bring my own input peripheral?';RID='migrated_owner_claim_personal_keyboard_mouse'
if 'baseline' in sys.argv:
    with patch.object(e,'MODEL_WORK',Mock(acquire=Mock(return_value=True))),patch.object(e,'llm_call_allowed',return_value=(True,{})),patch.object(e,'record_llm_failure'),patch.object(e,'release_llm_slot'),patch.object(e.urllib.request,'urlopen',side_effect=TimeoutError('CONTROLLED timeout')) as http:
        r=answer(Q,locale=LocaleDecision('en','en','en',1,'fixture'),allow_llm=True)
    plan=r.decision_artifact['query_plan']
    check('Baseline waits for model before mandatory confirmation',http.call_count==1 and plan.get('method')=='profile_topic_clarification',{'plan':plan,'answer':r.answer})
else:
    for lang,q in [('en',Q),('th','ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม'),('en','I attached incorrect proof of payment. How do I fix it?'),('th','แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง')]:
        with patch.object(e,'MODEL_WORK') as work,patch.object(e,'llm_call_allowed',return_value=(True,{})),patch.object(e,'record_llm_failure'),patch.object(e,'release_llm_slot'),patch.object(e.urllib.request,'urlopen',side_effect=TimeoutError('CONTROLLED timeout')) as http:
            start=time.perf_counter();r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'fixture'),allow_llm=True);elapsed=time.perf_counter()-start
        p=r.decision_artifact['query_plan'];audit=p.get('entity_selection',{})
        actual_rows=e.candidates(q,records,names)
        compatible=__import__('app.knowledge.common.profile_confirmation',fromlist=['eligible']).eligible(q,records)
        shortcut=bool(actual_rows) and all(e.value(records[x['record_id']],'query_profile') and x['record_id'] in compatible for x in actual_rows)
        correct_path=(audit.get('model_call_avoided') is True and not audit['attempted'] and not work.acquire.called and not http.called) if shortcut else (http.called and audit.get('attempted') is True and not audit.get('model_call_avoided'))
        check('Explicit topic confirmation with bounded shortcut: '+q,p.get('method')=='profile_topic_clarification' and state_from_answer(r).get('profile_confirmation') and correct_path and not audit['intent_verified'],{'answer':r.answer,'plan':p,'internal_seconds':elapsed,'shortcut_eligible':shortcut,'candidate_ids':[x['record_id'] for x in actual_rows]})

    # Incompatible/new subjects may be offered as choices, never answered as
    # though synonym equivalence or policy coverage has been established.
    with patch.object(e,'MODEL_WORK',Mock(acquire=Mock(return_value=True))),patch.object(e,'llm_call_allowed',return_value=(True,{})),patch.object(e,'record_llm_failure'),patch.object(e,'release_llm_slot'),patch.object(e.urllib.request,'urlopen',side_effect=TimeoutError('CONTROLLED timeout')):
        r=answer('I attached incorrect proof of identity. How do I fix it?',locale=LocaleDecision('en','en','en',1,'fixture'),allow_llm=True)
    check('Identity proof is not asserted to be payment slip',r.decision_artifact['query_plan'].get('method')=='profile_topic_clarification' and 'facebook.com' not in r.answer,{'answer':r.answer,'plan':r.decision_artifact['query_plan']})

    rows=e.candidates(Q,records,names);one=[next(x for x in rows if x['record_id']==RID)]
    envelope={'response':json.dumps({'indices':[],'ambiguous':False,'profile_bindings':[]}), 'done':True,'total_duration':9_000_000,'load_duration':2_000_000,'prompt_eval_duration':3_000_000,'eval_duration':4_000_000,'prompt_eval_count':24,'eval_count':8}
    def select_fixture(*,rows_override=one,eligible_override=None,error=None,payload=envelope,deadline=6,prefer=False):
        work=Mock();work.acquire.return_value=True;release_slot=Mock()
        with patch.object(e,'candidates',return_value=rows_override),patch('app.knowledge.common.profile_confirmation.eligible',return_value=eligible_override if eligible_override is not None else [RID]),patch.object(e,'MODEL_WORK',work),patch.object(e,'llm_call_allowed',return_value=(True,{})),patch.object(e,'release_llm_slot',release_slot),patch.object(e,'record_llm_success'),patch.object(e,'record_llm_failure'),patch.object(e,'timeout_for_call',side_effect=deadline if isinstance(deadline,list) else None,return_value=deadline),patch.object(e.urllib.request,'urlopen',side_effect=error,return_value=Response(payload)) as http:
            choice,audit=e.select(Q,records,names,prefer_profile_confirmation=prefer)
        return choice,audit,work,http,release_slot

    choice,audit,work,http,slot=select_fixture()
    check('Default semantic selector still calls LLM',http.call_count==1 and audit.get('schema_accepted') is True and not audit.get('model_call_avoided'),audit)
    check('Nanoseconds converted to milliseconds and token counts retained',audit.get('model_metrics')=={'total_duration_ms':9.,'load_duration_ms':2.,'prompt_eval_duration_ms':3.,'eval_duration_ms':4.,'prompt_eval_count':24,'eval_count':8},audit)
    check('HTTP budget and stage timing visible',audit.get('model_request',{}).get('effective_timeout_seconds')==6 and {'retrieval_ms','model_work_wait_ms','admission_wait_ms','http_wait_and_read_ms','total_ms'}<=audit.get('timing_ms',{}).keys(),audit)
    check('Successful call releases both gates',work.release.call_count==slot.call_count==1)
    for label,err,expected in [('timeout',TimeoutError('fixture'),'timeout'),('wrapped timeout',URLError(TimeoutError('fixture')),'timeout'),('permission',URLError(OSError(10013,'fixture')),'transport')]:
        _,audit,work,http,slot=select_fixture(error=err)
        check('Classify '+label,audit.get('availability_failure')==expected and not audit['transport_ok'] and work.release.call_count==slot.call_count==1,audit)
    for label,payload in [('shape',{'response':'{}'}),('incomplete',{**envelope,'done':False}),('nonobject',[]),('bad JSON',{'response':'not JSON'})]:
        _,audit,work,http,slot=select_fixture(payload=payload)
        check('Responsive invalid '+label+' is schema failure',audit.get('availability_failure')=='schema' and audit['transport_ok'] and work.release.call_count==slot.call_count==1,audit)
    _,audit,work,http,slot=select_fixture(eligible_override=[],prefer=True)
    check('Ineligible profile does not bypass model',http.call_count==1 and not audit.get('model_call_avoided'),audit)
    other=next(rid for rid,r in records.items() if r['kind']=='faq' and not e.value(r,'query_profile'))
    mixed=one+[{'record_id':other,'kind':'faq','text':'fixture','score':.2}]
    _,audit,work,http,slot=select_fixture(rows_override=mixed,prefer=True)
    check('Mixed profile and ordinary candidates retain LLM',http.call_count==1 and not audit.get('model_call_avoided'),audit)
    _,audit,work,http,slot=select_fixture(deadline=[6,0])
    check('Deadline exhausted after lock does not call HTTP',not http.called and not audit['attempted'] and audit['availability_failure']=='deadline' and work.release.call_count==slot.call_count==1,audit)
    _,audit,work,http,slot=select_fixture(deadline=0)
    check('Deadline exhausted before lock acquires nothing',not work.acquire.called and not http.called and not slot.called and not audit['attempted'],audit)
    with patch.object(e,'MODEL_WORK') as work,patch.object(e.urllib.request,'urlopen') as http:
        _,audit=e.select(Q,records,names,prefer_profile_confirmation=True)
    check('Confirmation path does not claim model transport or semantic acceptance',not any(k in audit for k in ['transport_ok','schema_accepted','semantic_selection_accepted','availability_failure']) and not work.acquire.called and not http.called,audit)

check('Production database unchanged',before==hashlib.sha256(db.read_bytes()).hexdigest())
result={'count':len(checks),'passed':sum(c['passed'] for c in checks),'llm_enabled':True,'controlled_model_transport':True,'real_model_inference_verified':False,'tcp_verified':False,'database_sha256':before,'checks':checks}
(T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not c['passed'] for c in checks))
