"""Targeted controlled selector contracts; no real-model success claim."""
import copy,hashlib,json,os,sys
from pathlib import Path
from unittest.mock import patch,Mock
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
tag=sys.argv[1];T=B/'verification'/tag;T.mkdir(parents=True,exist_ok=False)
db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0')
sys.path.insert(0,str(S))
import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
import app.pipeline as pipeline_pkg
pipeline_pkg.__path__.insert(0,str(B/'candidate/app/pipeline'))
from app.knowledge.common import entity_search as e
from app.knowledge.common.semantic_profile import check_binding,profile
from app.knowledge.common.migrated_view import MigratedView
release=MigratedView(db).snapshot()['release'];records=release['records'];names=release['names']
RID='migrated_owner_claim_personal_keyboard_mouse';SLIP='procedure_wrong_slip';Q='Can I bring my own input peripheral?'
ordinary={'kind':'faq','fields':{'question':{'status':'known','value':{'en':Q}}}}
unrelated={'kind':'game','fields':{'title':{'status':'known','value':{'en':'ZZZUniqueGameTitle'}}}}
universe={**records,'fixture_ordinary':ordinary,'fixture_unrelated':unrelated}
one={'record_id':RID,'kind':'faq','text':'Fixture profile description','score':.5}
mix=[one,{'record_id':'fixture_ordinary','kind':'faq','text':'Fixture ordinary topic','score':.4}]
bad={'record_id':'fixture_unrelated','kind':'game','text':'Unrelated fixture game','score':.9}
checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(json.dumps({'case':name,'passed':bool(ok)}),flush=True)
class Response:
 def __init__(self,p):self.raw=json.dumps({'response':json.dumps(p),'done':True,'prompt_eval_count':100,'eval_count':10}).encode()
 def __enter__(self):return self
 def __exit__(self,*args):return False
 def read(self,n):return self.raw[:n]
def choose(rows=mix,p=None,prefer=True,error=None,eligible=None):
 work=Mock();work.acquire.return_value=True
 if p is None:p={'indices':[0],'ambiguous':False}
 with patch.object(e,'candidates',return_value=rows),patch('app.knowledge.common.profile_confirmation.eligible',return_value=[RID] if eligible is None else eligible),patch.object(e,'MODEL_WORK',work),patch.object(e,'llm_call_allowed',return_value=(True,{})),patch.object(e,'release_llm_slot'),patch.object(e,'record_llm_success'),patch.object(e,'record_llm_failure'),patch.object(e,'timeout_for_call',return_value=6),patch.object(e.urllib.request,'urlopen',side_effect=error,return_value=Response(p)) as http:
  choice,audit=e.select(Q,universe,names,prefer_profile_confirmation=prefer)
 return choice,audit,http,work

choice,audit,http,work=choose(rows=[one,bad])
check('Prune only an ordinary topic rejected by existing guard',audit.get('candidate_pruning',{}).get('rejected_ids')==['fixture_unrelated'] and audit['candidate_ids']==[RID],audit)
check('Pruning preserves immediate explicit profile confirmation',choice is None and audit.get('model_call_avoided') and not http.called and not work.acquire.called,audit)
choice,audit,http,work=choose(rows=[bad])
check('All unanchored records abstain before inference',choice is None and not http.called and audit.get('reason')=='no_independent_topic_anchor',audit)
choice,audit,http,work=choose()
payload=json.loads(http.call_args.args[0].data)
check('Mixed eligible topics use real selector protocol',http.call_count==1 and audit.get('topic_proposal_only') is True and audit.get('profile_protocol') is False,audit)
check('Proposal output is indices only, without free quotes',set(payload['format']['properties'])=={'indices','ambiguous'} and payload['options']['num_predict']==70 and payload['options']['num_ctx']==3072,payload)
check('Proposal returns explicit topic confirmation, no facts',choice=={'profile_confirmation':[RID]} and audit.get('requires_topic_confirmation') and not audit.get('profile_projections'),audit)
check('Proposal does not fabricate semantic binding approval','semantic_selection_accepted' not in audit and not audit.get('profile_binding_accepted') and not audit['intent_verified'],audit)
check('Model budget is unchanged',http.call_args.kwargs['timeout']==6 and audit['model_request']['timeout_cap_seconds']==6,audit)
choice,audit,http,work=choose(p={'indices':[1],'ambiguous':False})
check('Anchored ordinary topic remains selectable',choice==['fixture_ordinary'] and audit.get('semantic_selection_accepted') is True,audit)
choice,audit,http,work=choose(p={'indices':[0,1],'ambiguous':False})
check('Mixed selection cannot bypass profile confirmation',choice=={'profile_confirmation':[RID]} and audit.get('mixed_selection_requires_clarification') and not audit.get('profile_projections'),audit)
choice,audit,http,work=choose(p={'indices':[0],'ambiguous':True})
check('Ambiguous profile proposal still uses topic confirmation',choice=={'profile_confirmation':[RID]} and audit.get('ambiguous') is True,audit)
choice,audit,http,work=choose(p={'indices':[],'ambiguous':True})
check('Empty ambiguous proposal falls back to a real topic menu',choice is None and audit.get('topic_proposal_accepted') is False,audit)
choice,audit,http,work=choose(p={'indices':[0],'ambiguous':False,'profile_bindings':[]})
check('Unexpected binding fields in proposal protocol are rejected',choice is None and audit.get('availability_failure')=='schema',audit)
choice,audit,http,work=choose(p={'indices':[0],'ambiguous':False,'answer':'invented fact'})
check('Model-written facts are rejected',choice is None and audit.get('availability_failure')=='schema',audit)
choice,audit,http,work=choose(p={'indices':[True],'ambiguous':False})
check('Boolean selection index is rejected',choice is None and audit.get('availability_failure')=='schema',audit)
choice,audit,http,work=choose(error=TimeoutError('CONTROLLED'))
check('Remaining model timeout is still visible',choice is None and audit.get('availability_failure')=='timeout' and audit.get('attempted') is True,audit)

binding={'index':0,'task':'permission','task_span':'Can I bring','subjects':[{'subject_index':0,'span':'input peripheral','relation':'equivalent'}],'ownership':'personal','context':'studio','clauses':[{'id':0,'covered':True}]}
choice,audit,http,work=choose(prefer=False,p={'indices':[0],'ambiguous':False,'profile_bindings':[binding]})
payload=json.loads(http.call_args.args[0].data)
check('Direct callers retain strict binding protocol',audit.get('profile_protocol') is True and payload['options']['num_predict']==420 and not audit.get('topic_proposal_only'),audit)
choice,audit,http,work=choose(eligible=[])
payload=json.loads(http.call_args.args[0].data)
check('Incompatible profile cannot opt into weak proposal mode',audit.get('profile_protocol') is True and not audit.get('topic_proposal_only'),audit)

base_q='I attached incorrect proof of payment. How do I fix it?'
base={'index':0,'task':'correction','task_span':'incorrect','subjects':[{'subject_index':0,'span':'proof of payment','relation':'equivalent'}],'ownership':'unspecified','context':'studio','clauses':[{'id':0,'covered':True}]}
check('Existing quoted-input binding remains valid',check_binding(base_q,base,0,records[SLIP]) is None)
for name,modify,expected in [
 ('Invented subject copied from candidate',lambda p:p['subjects'][0].update(span='slip'),'unsupported_subject_span'),
 ('Invented task quote',lambda p:p.update(task_span='correct my slip'),'unsupported_task_span'),
 ('Explicitly different subject',lambda p:p['subjects'][0].update(relation='different'),'subject_not_equivalent'),
 ('Uncovered additional request',lambda p:p['clauses'][0].update(covered=False),'uncovered_request'),
 ('Competition scope cannot become studio scope',lambda p:p.update(context='competition'),'context_mismatch'),
]:
 mutated=copy.deepcopy(base);modify(mutated);reason=check_binding(base_q,mutated,0,records[SLIP])
 check(name,reason==expected,{'reason':reason,'expected':expected})
check('Source database unchanged',before==hashlib.sha256(db.read_bytes()).hexdigest())
from app.pipeline import migrated_chat as backend
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult
from app.core.locale import LocaleDecision
from app.knowledge.common.dialogue import state_from_answer
q_recovery='ผมอัปโหลดรูปหลักฐานโอนเงินผิด ต้องแก้ยังไง'
def rejected_answer(error='unresolved_query_clause'):
 return PipelineAnswer(answer='REJECTED_FACT_MUST_NOT_LEAK',hits=[],elapsed=0,mode='pipeline:common_partial_answer',confidence=0,route=PipelineRoute('knowledge','common_read',0,'fixture','medium','fixture'),entities=EntityBundle(),validation=ValidationResult(False,errors=[error]),decision_artifact={'query_plan':{'record_ids':['migrated_faq_rule_payment_bank']}})
loc=LocaleDecision('th','th','th',1,'controlled_fixture')
with patch.object(backend.CommonAnswerer,'answer',return_value=rejected_answer()):
 recovered=backend.answer(q_recovery,locale=loc,allow_llm=True)
state=state_from_answer(recovered) or {}
check('Failed FAQ coverage recovers an explicit current topic menu',state.get('profile_confirmation') and recovered.decision_artifact['query_plan']['entity_selection']['reason']=='named_source_failed_request_coverage',recovered.decision_artifact)
check('Rejected FAQ facts stay rejected and auditable','REJECTED_FACT' not in recovered.answer and recovered.decision_artifact.get('rejected_candidate',{}).get('validation_errors')==['unresolved_query_clause'])
with patch.object(e.urllib.request,'urlopen',side_effect=AssertionError('Unexpected model call for explicit confirmed source')):
 confirmed=backend.answer('ใช่',locale=loc,history=[{'role':'assistant','text':recovered.answer,'common_read_state':state,'delivery_status':'server_written'}],allow_llm=True)
check('Recovered menu supports the next yes from current procedure','facebook.com/psuesportsphuket' in confirmed.answer and confirmed.validation.ok,confirmed.answer)
with patch.object(backend.CommonAnswerer,'answer',return_value=rejected_answer('fixture_other_validation_failure')):
 unrecovered=backend.answer(q_recovery,locale=loc,allow_llm=True)
check('Other validation failures do not gain authority from recovery',not (state_from_answer(unrecovered) or {}).get('profile_confirmation') and 'REJECTED_FACT' not in unrecovered.answer)
with patch.object(backend.CommonAnswerer,'answer',return_value=rejected_answer()):
 no_topic=backend.answer('Where is the unidentified fixture item?',locale=loc,allow_llm=True)
check('No eligible declared topic keeps clarification without invented facts',not (state_from_answer(no_topic) or {}).get('profile_confirmation') and 'REJECTED_FACT' not in no_topic.answer)
check('Database remains unchanged after recovery checks',before==hashlib.sha256(db.read_bytes()).hexdigest())
result={'count':len(checks),'passed':sum(c['passed'] for c in checks),'controlled_model_outputs':True,'real_model_inference_verified':False,'checks':checks}
with (T/'RESULTS.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not c['passed'] for c in checks))
