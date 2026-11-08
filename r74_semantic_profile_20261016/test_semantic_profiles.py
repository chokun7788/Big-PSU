"""Controlled model OUTPUTS, not model accuracy. Real selector and dispatcher."""
import copy,hashlib,json,os,sqlite3,sys
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch
from datetime import datetime
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parent;T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
db=T/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
source_db=B/'system/data/knowledge/common.sqlite';before=hashlib.sha256(source_db.read_bytes()).hexdigest()
a=sqlite3.connect(source_db.as_uri()+'?mode=ro',uri=True);z=sqlite3.connect(db)
try:a.backup(z)
finally:z.close();a.close()
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_CHAT_LOG_DIR=str(T/'logs'))
sys.path.insert(0,str(B/'system'))
from app.knowledge.common import migrated_view,entity_search
migrated_view.SYSTEM_ROOT=db.parents[2]
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.semantic_profile import validate_bindings
from app.knowledge.common.query_contract import semantic_clauses
from app.knowledge.common.registry import now
from app.knowledge.common.store import CommonStore
from app.knowledge.records import canonical_json
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.calendar import service_calendar
service_calendar.now_bangkok=lambda:datetime(2026,10,16,12,tzinfo=ZoneInfo('Asia/Bangkok'))
RID='procedure_wrong_slip';checks=[];calls=[]
def check(name,ok,detail=None):
    row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
    with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
    print(json.dumps({'case':name,'passed':bool(ok)},ensure_ascii=False),flush=True)
def snapshot():return MigratedView(db).snapshot()['release']
def proposed(q,rows,subject_span,task_span,*,rid=RID):
    i=next(i for i,row in enumerate(rows) if row['record_id']==rid)
    return {'indices':[i],'ambiguous':False,'profile_bindings':[{'index':i,'task':'correction','task_span':task_span,
        'subjects':[{'subject_index':0,'span':subject_span,'relation':'equivalent'}],
        'ownership':'unspecified','context':'studio','clauses':[{'id':j,'covered':True} for j,_ in enumerate(semantic_clauses(q))]}]}
q='I attached the incorrect proof of payment. How do I fix it?'
release=snapshot();records=release['records'];names=release['names'];rows=entity_search.candidates(q,records,names)
base=proposed(q,rows,'proof of payment','incorrect')
check('Original synonym remains absent from direct literal matching',__import__('app.knowledge.common.question_profiles',fromlist=['select']).select(q,records)[0] is None)
accepted,reason=validate_bindings(q,base,base['indices'],rows,records,True)
check('Valid grounded profile projection is accepted',RID in accepted and reason is None,accepted)

mutations=[
 ('Missing binding',lambda p:p.update(profile_bindings=[]),'missing_or_duplicate_profile_binding'),
 ('Duplicate binding',lambda p:p['profile_bindings'].append(copy.deepcopy(p['profile_bindings'][0])),'missing_or_duplicate_profile_binding'),
 ('Boolean candidate index',lambda p:p['profile_bindings'][0].update(index=True),'invalid_binding_shape'),
 ('Unrequested task',lambda p:p['profile_bindings'][0].update(task='permission'),'task_mismatch'),
 ('Made-up subject quote',lambda p:p['profile_bindings'][0]['subjects'][0].update(span='payment slip'),'unsupported_subject_span'),
 ('Made-up task quote',lambda p:p['profile_bindings'][0].update(task_span='wrong'),'unsupported_task_span'),
 ('Wrong subject index',lambda p:p['profile_bindings'][0]['subjects'][0].update(subject_index=11),'invalid_subject_index'),
 ('Boolean subject index',lambda p:p['profile_bindings'][0]['subjects'][0].update(subject_index=True),'invalid_subject_index'),
 ('Different concept',lambda p:p['profile_bindings'][0]['subjects'][0].update(relation='different'),'subject_not_equivalent'),
 ('Uncertain concept',lambda p:p['profile_bindings'][0]['subjects'][0].update(relation='uncertain'),'subject_not_equivalent'),
 ('Task word reused as subject',lambda p:p['profile_bindings'][0]['subjects'][0].update(span='incorrect'),'uninformative_subject_span'),
 ('Unsupported context',lambda p:p['profile_bindings'][0].update(context='competition'),'context_mismatch'),
 ('Missing coverage',lambda p:p['profile_bindings'][0].update(clauses=[]),'missing_clause_coverage'),
 ('Uncovered clause',lambda p:p['profile_bindings'][0]['clauses'][0].update(covered=False),'uncovered_request'),
 ('Boolean clause ID',lambda p:p['profile_bindings'][0]['clauses'][0].update(id=True),'invalid_clause_coverage'),
 ('Model-written answer',lambda p:p['profile_bindings'][0].update(answer='Invented policy'),'invalid_binding_shape'),
 ('Model-selected fields',lambda p:p['profile_bindings'][0].update(requested_fields=['amount_minor']),'invalid_binding_shape'),
]
for name,mutate,expected in mutations:
    p=copy.deepcopy(base);mutate(p);accepted,reason=validate_bindings(q,p,p['indices'],rows,records,True)
    check(name,not accepted and reason==expected,{'reason':reason,'expected':expected})

class Response:
    def __init__(self,p):self.p=json.dumps({'response':json.dumps(p,ensure_ascii=False)}).encode()
    def __enter__(self):return self
    def __exit__(self,*args):return False
    def read(self,n):return self.p[:n]
@contextmanager
def controlled(subject,task,*,rid=RID,change=None):
    def respond(req,timeout=None):
        payload=json.loads(req.data);prompt=json.loads(payload['prompt'])
        if 'profile_bindings' not in payload['format']['properties']:raise AssertionError('Unexpected model call outside profile selector')
        current=snapshot();actual_rows=entity_search.candidates(prompt['question'],current['records'],current['names'])
        p=proposed(prompt['question'],actual_rows,subject,task,rid=rid)
        if change:change(p)
        calls.append({'payload':payload,'controlled_response':p,'real_model_inference':False})
        return Response(p)
    with patch.object(entity_search.urllib.request,'urlopen',side_effect=respond):yield
def ask(question,lang='en'):
    loc=LocaleDecision(lang,lang,lang,1,'explicit_test_locale')
    # No second semantic interpretation may override a validated task profile.
    with patch('app.knowledge.common.planner.plan_fields',side_effect=AssertionError('Unexpected second field-planner call')):
        r=answer(question,locale=loc,allow_llm=True)
    return r,{'answer':r.answer,'hits':r.hits,'artifact':r.decision_artifact,'mode':r.mode,'validation_ok':r.validation.ok}
for question,lang,subject,task in [
 (q,'en','proof of payment','incorrect'),
 ('I uploaded an incorrect bank transfer image. How do I fix it?','en','bank transfer image','incorrect'),
 ('แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง','th','หลักฐานชำระเงิน','ผิด')]:
    with controlled(subject,task):r,d=ask(question,lang)
    plan=d['artifact'].get('query_plan',{})
    check('Source-backed procedure for controlled semantic plan: '+lang+' '+subject,
        'facebook.com/psuesportsphuket' in r.answer and RID in {h.get('record_id') for h in r.hits} and r.validation.ok
        and plan.get('method')=='semantic_question_profile' and 'steps' in plan.get('requested_fields',[])
        and not plan.get('semantic_review_needed'),d)

for label,question,span in [
 ('identity proof','I attached incorrect proof of identity. How do I fix it?','proof of identity'),
 ('amount','The payment amount was incorrect. How do I fix it?','payment amount')]:
    with controlled(span,'incorrect',change=lambda p:p['profile_bindings'][0]['subjects'][0].update(relation='different')):
        choice,audit=entity_search.select(question,records,names)
    check('Reject controlled non-equivalence: '+label,choice is None and audit.get('semantic_selection_accepted') is False and audit.get('schema_accepted') is True,audit)

with controlled('proof of payment','incorrect',change=lambda p:p['profile_bindings'][0]['clauses'][0].update(covered=False)):
    r,d=ask(q)
check('Rejected whole-request coverage cannot leak procedure steps',RID not in {h.get('record_id') for h in r.hits} and 'facebook.com' not in r.answer,d)
with patch.object(entity_search.urllib.request,'urlopen',side_effect=OSError('CONTROLLED transport failure')):
    r,d=ask(q)
check('Transport failure is a connection retry, not absent facts or a timeout',r.mode=='pipeline:common_retry' and 'cannot connect' in r.answer and d['artifact']['query_plan']['entity_selection'].get('availability_failure')=='transport',d)
with patch.object(entity_search.urllib.request,'urlopen',return_value=Response({'indices':[], 'ambiguous':False})):
    r,d=ask(q)
check('Missing output contract is distinct from a connection failure',r.mode=='pipeline:common_retry' and 'reliably interpret' in r.answer and d['artifact']['query_plan']['entity_selection'].get('availability_failure')=='schema',d)
with patch.object(entity_search,'llm_call_allowed',return_value=(False,{'llm_health_reason':'CONTROLLED cooldown'})):
    r,d=ask(q)
check('Health gate keeps a retry instead of claiming no source',r.mode=='pipeline:common_retry' and d['artifact']['query_plan']['entity_selection'].get('availability_failure')=='model_gate',d)

# Expose a limitation instead of pretending quote validation is a semantic
# oracle: an incorrect equivalence claim with real quotes can pass contracts.
limit_q='I attached incorrect proof of identity. How do I fix it?'
limit_rows=entity_search.candidates(limit_q,records,names)
limit_p=proposed(limit_q,limit_rows,'proof of identity','incorrect')
limit_accepted,limit_reason=validate_bindings(limit_q,limit_p,limit_p['indices'],limit_rows,records,True)
(T/'SEMANTIC_LIMITATION.json').write_text(json.dumps({'question':limit_q,'controlled_false_equivalence_claim':limit_p,
    'contract_accepts_claim':bool(limit_accepted),'rejection_reason':limit_reason,
    'real_model_result':None,'meaning':'Quoted-span validity is NOT independent proof of equivalence; real contrast-set inference remains required.'},ensure_ascii=False,indent=2),encoding='utf8')

# Ensure the source projection reads the current revision, never model facts.
store=CommonStore(db);record=store.get(RID)['record'];old_revision=record['revision']
values={'steps':[{'order':1,'instruction':{'th':'ข้อมูลตัวอย่างแยก STEP_R74_V2','en':'ISOLATED FIXTURE STEP_R74_V2'},'contact_id':None}]}
raw=canonical_json(values);sid='fixture_r74_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
store.add_source({'source_id':sid,'kind':'derived_curated','path':'isolated-fixture://'+sid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['procedure'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='isolated-fixture')
for key,val in values.items():record['fields'][key]={'status':'known','value':val,'evidence_refs':[{'source_id':sid,'locator':'/'+key}],'note':'ISOLATED fixture only'}
store.save(record,actor='isolated-fixture',expected_version=old_revision,change_note='Controlled semantic update fixture')
with controlled('proof of payment','incorrect'):r,d=ask(q)
check('Semantic plan reads updated revision rather than cached steps','STEP_R74_V2' in r.answer and d['artifact']['query_plan']['question_profile']['projection']['revision']==old_revision+1,d)
check('Old source revision preserved',store.revision(RID,old_revision)['record']['fields']['steps']['value']!=values['steps'])
store.withdraw(RID,actor='isolated-fixture')
fresh=snapshot();newrows=entity_search.candidates(q,fresh['records'],fresh['names'])
check('Withdrawn procedure removed from candidate/projection universe',RID not in fresh['records'] and RID not in {r['record_id'] for r in newrows})
check('Actual R74 data unchanged',before==hashlib.sha256(source_db.read_bytes()).hexdigest())
result={'count':len(checks),'passed':sum(c['passed'] for c in checks),'llm_enabled':True,'controlled_model_responses':True,
    'real_model_inference_verified':False,'format':'common','checks':checks}
(T/'MODEL_FIXTURES.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2),encoding='utf8')
(T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not c['passed'] for c in checks))
