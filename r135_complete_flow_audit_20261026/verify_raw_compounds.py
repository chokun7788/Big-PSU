"""Literal source spans, bounded partial compounds and positive public reads."""
import json,os,time
from types import SimpleNamespace
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.routing import split_needs
O=R/('raw_compounds_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated.sqlite');checks={};details=[]
for text,label,expected in [('What genre is AMBER game?; How do I book?','Amber game',['What genre is AMBER game?','How do I book?']),('What genre is Amber   game?; How do I book?','Amber game',['What genre is Amber   game?','How do I book?']),('What genre is Copper; And Also Game?; How do I book?','Copper; And Also Game',['What genre is Copper; And Also Game?','How do I book?']),('What genre is STRASSE; Game?; How do I book?','Straße; Game',['What genre is STRASSE; Game?','How do I book?'])]:
 result=split_needs(text,SimpleNamespace(subject_labels={'C04':{label}}));checks['raw_'+label+text[:25]]=result==expected and all(p in text for p in result);details.append({'raw_question':text,'source_label':label,'parts':result})
store=CommonStore(O/'source.sqlite');store.initialize(allow_demo=False);bi=lambda x:{'th':x,'en':x}
q='What genre is Copper and what games?';checks['fallback_conjunction_in_source_title_not_split']=split_needs(q,SimpleNamespace(subject_labels={'C04':{'Copper and what games'}}))==[q]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'isolated-compound-source')['record']
create('game','amber_game',{'title':bi('Amber game'),'genre':bi('Amber source genre')});create('game','separator_game',{'title':bi('Copper; And Also Game'),'genre':bi('Separator source genre')});create('faq','booking',{'question':bi('How to book'),'answer':bi('Submit the source booking form.'),'topic':'C08','intent_key':'booking_steps'});view=DraftSnapshotView(store)
for query,key,genre in [('What genre is AMBER game?; How do I book?','known_siblings','Amber source genre'),('What genre is AMBER game?; What is quantum confetti?; How do I book?','unknown_middle','Amber source genre'),('What genre is Copper; And Also Game?; How do I book?','source_separator','Separator source genre')]:
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):r=CommonAnswerer(view).answer(query,locale='en',at='2026-10-27T10:00:00+07:00',planner=None)
 a=r.decision_artifact;contract=a.get('execution_contract',{});tasks=contract.get('request_plan',{}).get('tasks',[]);checks[key+'_positive_sources_preserved']=genre in r.answer and 'Submit the source booking form.' in r.answer;checks[key+'_literal_task_spans']=bool(tasks) and all(query[t['source_span']['start']:t['source_span']['end']]==t['source_span']['text'] for t in tasks);checks[key+'_independent_task_count']=len(tasks)==(3 if key=='unknown_middle' else 2)
 if key=='unknown_middle':checks['unresolved_sibling_explicit_and_no_invented_claim']=any(t['category'] is None and t['ambiguities'] for t in tasks) and 'quantum confetti' not in json.dumps(a.get('domain_flow',{}).get('typed_claims',[]))
 details.append({'question':query,'answer':r.answer,'artifact':a})
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'owner_data_modified':False,'semantic_accuracy_benchmark':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(O),**report}));assert report['all_passed']
