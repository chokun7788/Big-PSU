"""Qualified reply contracts; separate fixture policy data and model transport."""
import copy,hashlib,io,json,os,sqlite3,sys,uuid
from pathlib import Path
from unittest.mock import patch
from datetime import datetime
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parent;T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
S=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else B;baseline=len(sys.argv)>3 and sys.argv[3]=='baseline'
original=S/'system/data/knowledge/common.sqlite';before=hashlib.sha256(original.read_bytes()).hexdigest()
db=T/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
a=sqlite3.connect(original.as_uri()+'?mode=ro',uri=True);z=sqlite3.connect(db)
try:a.backup(z)
finally:z.close();a.close()
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_PIPELINE_WARMUP='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0')
sys.path.insert(0,str(S/'system'))
from app.knowledge.common import migrated_view,entity_search
migrated_view.SYSTEM_ROOT=db.parents[2]
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.dialogue import state_from_answer
from app.knowledge.common.profile_confirmation import fingerprint
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template,now
from app.knowledge.records import canonical_json
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.calendar import service_calendar
service_calendar.now_bangkok=lambda:datetime(2026,10,16,12,tzinfo=ZoneInfo('Asia/Bangkok'))
RID='migrated_owner_claim_personal_keyboard_mouse';SLIP='procedure_wrong_slip';store=CommonStore(db);checks=[]
def check(name,ok,detail=None):
    row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
    with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
    print(json.dumps({'case':name,'passed':bool(ok)},ensure_ascii=False),flush=True)
def ask(q,lang='en',history=None):
    r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'explicit_test_locale'),history=history or [],allow_llm=True)
    return r,{'answer':r.answer,'mode':r.mode,'hits':r.hits,'artifact':r.decision_artifact,'validation_ok':r.validation.ok}
def hist(r):return [{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
def sources(r):return {h.get('record_id') for h in r.hits}
def pending(rid):
    rec=store.get(rid)['record']
    return [{'role':'assistant','text':'Source-backed topic menu, fixture server state','delivery_status':'server_written','common_read_state':{'schema_version':1,'record_ids':[],'requested_fields':[],'profile_confirmation':{'version':1,'options':[{'record_id':rid,'routing_sha256':fingerprint(rec)}],'page':0,'page_size':6}}}]
def audit(d):
    p=d['artifact'].get('query_plan',{})
    return p.get('qualified_reply',{}).get('audit',{}) or p.get('question_profile',{}).get('qualification',{}).get('audit',{})
CASES=[
 ("Yes, but it is the studio's keyboard.",'en','scope','studio'),
 ('ใช่ครับ แต่เป็นคีย์บอร์ดของศูนย์','th','scope','studio'),
 ("Yes, but it is not mine; it belongs to the studio.",'en','scope','studio'),
 ('ใช่ แต่ไม่ใช่ของผม เป็นของศูนย์','th','scope','studio'),
 ("Yes, but it is my own keyboard.",'en','personal',None),
 ('ใช่ แต่เป็นเมาส์ของผม','th','personal',None),
 ('Yes, but it is for a tournament.','en','context','competition'),
 ('ใช่ แต่ใช้ตอนแข่ง','th','context','competition'),
 ('Yes, but it is not mine.','en','unknown','negated_scope_without_replacement'),
 ('Yes, but it is mine and wireless.','en','unknown','uncovered_qualification'),
 ("Yes, but it is mine and the studio's.",'en','unknown','conflicting_slots'),
 ('ใช่ แต่เป็นของผมและของศูนย์','th','unknown','conflicting_slots'),
 ('Yes, but it costs 500 baht.','en','unknown','uncovered_qualification'),
 ('ใช่ แต่ผมอายุ 12 ปี','th','topic','age_guardian'),
 ('Yes, but can I pay in installments?','en','topic','installments'),
 ('ใช่ แต่ผ่อนชำระได้ไหม','th','topic','installments'),
 ('Yes, but how do I pay for my booking?','en','new_request','795-276244-1'),
 ('ใช่ แต่หลังจองต้องจ่ายภายในกี่นาที','th','new_request','10'),
 ('Yes, but','en','unknown','uncovered_qualification'),
 ('Yes, but not a tournament, regular use.','en','personal',None),
 ('Yes, but not for a tournament, regular use.','en','personal',None),
 ('ใช่ แต่ไม่ได้ใช้แข่ง แต่เล่นทั่วไป','th','personal',None),
 ("Yes, but not the studio's; it is my keyboard.",'en','personal',None),
 ('ใช่ แต่ไม่ใช่ของศูนย์ เป็นเมาส์ของผม','th','personal',None),
 ('Yes, but it is my wireless keyboard.','en','unknown','uncovered_qualification'),
 ('Yes, but it is my gaming keyboard.','en','unknown','uncovered_qualification'),
]
with patch.object(entity_search.urllib.request,'urlopen',side_effect=OSError('CONTROLLED model transport unavailable')):
    initial,detail=ask('Can I bring my own input peripheral?')
    first_state=state_from_answer(initial) or {};h=hist(initial) if first_state.get('profile_confirmation') else pending(RID)
    check('Normal input creates a permission topic clarification',RID in {o['record_id'] for o in first_state.get('profile_confirmation',{}).get('options',[])},detail)
    for q,lang,kind,expected in (CASES[:8] if baseline else CASES):
        r,d=ask(q,lang,h);a=audit(d);errors=[];p=d['artifact'].get('query_plan',{})
        if not r.validation.ok:errors.append('validation_rejected')
        if kind=='personal':
            if RID not in sources(r) or ('not allowed' if lang=='en' else 'ไม่อนุญาต') not in r.answer:errors.append('missing_personal_source')
            if p.get('method')!='qualified_declared_profile':errors.append('wrong_selection_method')
        else:
            if RID in sources(r):errors.append('unqualified_rule_used')
            if kind in {'scope','context'} and a.get('qualified_scope',{}).get('ownership' if kind=='scope' else 'context')!=expected:errors.append('wrong_qualified_scope')
            if kind=='unknown' and a.get('reason')!=expected:errors.append('wrong_qualification_reason')
            if kind=='topic' and p.get('unconfirmed_topic')!=expected:errors.append('wrong_unconfirmed_topic')
            if kind=='new_request' and (expected not in r.answer or d['artifact'].get('dialogue_repair',{}).get('method')!='qualified_reply_new_request'):errors.append('new_request_not_answered')
        check(q,not errors,{**d,'errors':errors})
    if not baseline:
        r,d=ask("Yes, but it is the studio's keyboard.",history=h)
        r2,d2=ask('yes',history=hist(r))
        check('Yes cannot drop an unresolved ownership condition',RID not in sources(r2),d2)
        r,d=ask('yes',history=h)
        check('Plain yes still reads the original declared topic',RID in sources(r),d)
        r,d=ask('Yes, but how do I pay for my booking?',history=h)
        r2,d2=ask('And when?',history=hist(r))
        check('Independent new request retains its new follow-up context','10' in r2.answer and '795-276244-1' not in r2.answer,d2)
        spoof=copy.deepcopy(h);spoof[0]['delivery_status']='uncertain'
        r,d=ask("Yes, but it's the studio's keyboard.",history=spoof)
        check('Client-only or undelivered pending cannot trigger qualification',not audit(d),d)

        def save(rec,values):
            try:rev=store.get(rec['record_id'])['record']['revision']
            except ValueError:rev=0
            raw=canonical_json(values);sid='fixture_r77_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
            store.add_source({'source_id':sid,'kind':'derived_curated','path':'isolated-fixture://'+sid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[rec['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='isolated-fixture')
            for key,v in values.items():rec['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/'+key}],'note':'ISOLATED FIXTURE, not production policy'}
            store.save(rec,actor='isolated-fixture',expected_version=rev,change_note='R77 fixture');return store.get(rec['record_id'])['record']
        base=store.get(RID)['record'];p=copy.deepcopy(base['fields']['query_profile']['value']);p['ownership']='any'
        rec=template('faq');rec['record_id']='fixture_r77_scope_general';rec['aliases']={'th':[],'en':[]};rec['localization']['en_status']='agent_translated'
        rec=save(rec,{'question':{'th':'ตัวอย่างอุปกรณ์ของศูนย์','en':'Isolated studio-device scope'},'answer':{'th':'ข้อมูลแยก STUDIO_V1','en':'ISOLATED STUDIO_V1'},'topic':'r77_fixture','query_profile':p})
        r,d=ask("Yes, but it is the studio's keyboard.",history=h)
        check('New declared scope data answers without changing router IDs','STUDIO_V1' in r.answer and rec['record_id'] in sources(r) and RID not in sources(r),d)
        rec=save(rec,{'answer':{'th':'ข้อมูลแยก STUDIO_V2','en':'ISOLATED STUDIO_V2'}})
        r,d=ask('ใช่ แต่เป็นคีย์บอร์ดของศูนย์','th',h)
        check('Qualified selection reads current source revision','STUDIO_V2' in r.answer and 'STUDIO_V1' not in r.answer,d)
        r,d=ask('Yes, but it is my own keyboard.',history=h)
        check('Overlapping qualified policies require clarification',RID not in sources(r) and rec['record_id'] not in sources(r) and audit(d).get('reason')=='ambiguous_qualified_profiles',d)
        store.withdraw(rec['record_id'],actor='isolated-fixture')
        r,d=ask("Yes, but it is the studio's keyboard.",history=h)
        check('Withdrawn qualified scope does not revert to personal policy','STUDIO_V2' not in r.answer and RID not in sources(r),d)
        comp=template('faq');comp['record_id']='fixture_r77_scope_competition';comp['aliases']={'th':[],'en':[]};comp['localization']['en_status']='agent_translated';p['context']='competition'
        comp=save(comp,{'question':{'th':'กฎแข่งข้อมูลแยก','en':'Isolated competition scope'},'answer':{'th':'ข้อมูลแยก COMP_SCOPE','en':'ISOLATED COMP_SCOPE'},'topic':'r77_fixture_comp','query_profile':p})
        r,d=ask('Yes, but it is for a tournament.',history=h)
        check('Competition qualification uses competition source only','COMP_SCOPE' in r.answer and comp['record_id'] in sources(r) and RID not in sources(r),d)
        # An unseen subject proves selection is driven by metadata, not keyboard aliases.
        new=template('faq');new['record_id']='fixture_r77_new_subject';new['aliases']={'th':[],'en':[]};new['localization']['en_status']='agent_translated'
        pp={'task':'permission','subjects':[{'th':'แผงฟ้าข้อมูลแยก','en':'cobaltpad'}],'ownership':'personal','context':'studio'}
        new=save(new,{'question':{'th':'หัวข้อทดสอบแผงฟ้า','en':'Isolated cobalt topic'},'answer':{'th':'ข้อมูลแยก COBALT_SCOPE','en':'ISOLATED COBALT_SCOPE'},'topic':'r77_cobalt','query_profile':pp})
        nh=pending(new['record_id']);r,d=ask('Yes, but it is my own cobaltpad.',history=nh)
        check('Unseen subject reads declared scope without new aliases','COBALT_SCOPE' in r.answer and new['record_id'] in sources(r),d)
        r,d=ask('ใช่ แต่เป็นแผงฟ้าข้อมูลแยกของผม','th',nh)
        check('Unseen Thai subject uses the same qualifier mechanism','COBALT_SCOPE' in r.answer and new['record_id'] in sources(r),d)
        stale=copy.deepcopy(h);changed=copy.deepcopy(base['fields']['query_profile']['value']);changed['context']='competition';save(base,{'query_profile':changed})
        r,d=ask('Yes, but it is my own keyboard.',history=stale)
        check('Changed origin routing invalidates qualified acknowledgement',RID not in sources(r) and d['artifact'].get('query_plan',{}).get('method')=='profile_confirmation_expired',d)

        from app.web_api import server
        class Conn:
            def __init__(self,raw):self.input=io.BytesIO(raw);self.output=bytearray()
            def makefile(self,*a,**kw):return self.input
            def sendall(self,data):self.output.extend(data)
        class FakeServer:chat_jobs=None;job_ttl_sec=None;server_port=8113
        def api(q,sid):
            body=json.dumps({'question':q,'locale':'en','client_session_id':sid,'client_turn_id':uuid.uuid4().hex,'debug':True}).encode()
            raw=('POST /api/chat HTTP/1.1\r\nHost: 127.0.0.1:8113\r\nContent-Type: application/json\r\nContent-Length: '+str(len(body))+'\r\nConnection: close\r\n\r\n').encode()+body
            c=Conn(raw);server.ChatHandler(c,('127.0.0.1',11000),FakeServer());_,_,data=bytes(c.output).partition(b'\r\n\r\n');return json.loads(data)
        sid='r77-api-'+uuid.uuid4().hex;first=api('I attached incorrect proof of payment. How do I fix it?',sid);second=api('Yes, but can I pay in installments?',sid)
        check('HTTP handler respects added payment condition',second.get('decision_artifact',{}).get('query_plan',{}).get('unconfirmed_topic')=='installments' and SLIP not in {h.get('record_id') for h in second.get('hits',[])},{'first':first,'second':second})
check('Actual source database unchanged',before==hashlib.sha256(original.read_bytes()).hexdigest())
result={'count':len(checks),'passed':sum(r['passed'] for r in checks),'source_code':str(S),'llm_enabled':True,'controlled_model_transport':True,'real_model_inference_verified':False,'tcp_browser_wordpress_verified':False,'checks':checks}
(T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not r['passed'] for r in checks))
