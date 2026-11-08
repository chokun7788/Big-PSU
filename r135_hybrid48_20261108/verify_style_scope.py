"""Style modifiers cannot supply factual entities or dialogue references."""
import copy,json,os,time
from datetime import datetime
from unittest.mock import patch
from verification_support import R,index
out=R/('style_scope_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'conversation.sqlite')
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding,style_only_quote
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.request_verifier import observe
from app.knowledge.common.domain_flow.dialogue_task import resolve
i=index();checks={};details=[];clock='2026-10-26T12:00:00+07:00'
def compile(q,tail):
 ts=[MeaningTask('PC price','service_fee','C06','detail','amount','PC'),MeaningTask(tail,'games','C04','detail','genre')]
 u=apply(q,i,Understanding(ts,True,'controlled_style_scope',{'model_called':False}))
 c=compile_request(q,u,i,{'release_id':'controlled','epoch':1,'reference_time':clock})
 details.append({'question':q,'understanding':u.as_dict(),'compiled':c.as_dict()});return u,c
base='What is the genre?';u0,c0=compile('PC price; '+base,base)
for n,phrase in enumerate(['Answer only that point.','Please keep it brief.','Explain it briefly.','ตอบเฉพาะประเด็นนั้น','ตอบสั้น ๆ','ขอคำตอบแบบเดียวกัน']):
 tail=base+' '+phrase;u,c=compile('PC price; '+tail,tail)
 checks['style_does_not_create_target_'+str(n)]=u.tasks[1].target==u0.tasks[1].target and c.tasks[1].target_scope==c0.tasks[1].target_scope
 checks['style_does_not_create_factual_ambiguity_'+str(n)]=u.tasks[1].ambiguous==u0.tasks[1].ambiguous
 checks['style_has_no_factual_shared_edge_'+str(n)]=not any(b.target_task_id=='t2' for b in c.tasks[1].bindings)
 checks['complete_style_phrase_recognised_'+str(n)]=style_only_quote(phrase)
 checks['style_verifier_no_added_need_'+str(n)]=[(x['category'],x['facet']) for x in observe(i,tail)['needs']]==[(x['category'],x['facet']) for x in observe(i,base)['needs']]
tail='What genre is it? Answer only that point.';u,c=compile('PC price; '+tail,tail)
checks['actual_pronoun_outside_style_still_binds']=u.tasks[1].target=='PC' and c.tasks[1].target_scope=='shared'
tail='What is the genre?';q='PC price; PS5 price; '+tail+' Answer only that point.'
u=apply(q,i,Understanding([MeaningTask('PC price','service_fee','C06','detail','amount','PC'),MeaningTask('PS5 price','service_fee','C06','detail','amount','PS5'),MeaningTask(tail+' Answer only that point.','games','C04','detail','genre')],True,'controlled_two_sources',{'model_called':False}))
checks['style_does_not_manufacture_multiple_antecedent_ambiguity']=not u.tasks[-1].ambiguous and not u.tasks[-1].target
checks['factual_suffix_not_discarded_as_style']=not style_only_quote('Answer briefly: what is the price of PC?')
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.dialogue import state_from_answer
from app.session.conversation_store import ConversationStore
from app.knowledge.common.domain_flow.style_scope import masked
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False)
for rid,name in [('controlled_style_game','Amber game'),('controlled_style_named_game','Keep It Brief')]:
 r=template('game');r['record_id']=rid;r['localization']['en_status']='agent_translated'
 for key,value in {'title':{'th':'เกมทดสอบ '+name,'en':name},'genre':{'th':'แนวทดสอบ '+name,'en':'Controlled amber genre' if name=='Amber game' else 'Controlled brief genre'},'summary':{'th':'คำอธิบายอำพันทดสอบ','en':'Controlled amber summary'}}.items():r['fields'][key]={'status':'known','value':value,'evidence_refs':[],'note':''}
 save_owner_record(store,r,0,'controlled-test')
view=DraftSnapshotView(store);engine=Engine.from_snapshot(view.snapshot(),cache_key=view.path);reader=CommonAnswerer(view)
with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 initial=reader.answer('What genre is Amber game?',locale='en',at=clock,planner=None)
 sessions=ConversationStore(persistence_path=None);turn=sessions.begin('controlled-style-session','t1','What genre is Amber game?',locale='en');sessions.complete('controlled-style-session','t1',turn['revision'],{'ok':True,'request_id':'style-source-response','answer':initial.answer,'common_read_state':state_from_answer(initial)});sessions.delivery('controlled-style-session','t1','server_written');history=sessions.history('controlled-style-session')
 for n,phrase in enumerate(['Please keep it brief.','Explain it briefly.','ตอบเฉพาะประเด็นนั้น']):
  context=resolve(engine.index,phrase,history,view.snapshot()['active'],datetime.fromisoformat(clock))
  checks['delivered_style_does_not_inherit_game_'+str(n)]=not context['inherited_slots'] and not context['task']['game_ids']
  checks['delivered_style_preserves_original_execution_'+str(n)]=context['execution_question']==phrase
  result=reader.answer('What genre is Amber game? '+phrase,locale='en',at=clock,planner=None)
  checks['normal_common_source_answer_survives_style_'+str(n)]='Controlled amber genre' in result.answer
  q='What genre is Amber game? '+phrase;u=Understanding([MeaningTask(q,'games','C04','detail','genre','Amber game')],True,'controlled_single',{'model_called':False});direct=engine.answer(q,'en',at=clock,allow_llm=False,understanding=u)
  checks['direct_engine_source_answer_survives_style_'+str(n)]='Controlled amber genre' in direct['answer']
 follow=resolve(engine.index,'What is its summary? Explain it briefly.',history,view.snapshot()['active'],datetime.fromisoformat(clock))
 details.append({'case':'delivered_factual_pronoun','resolved':follow})
 checks['delivered_factual_pronoun_survives_style']=bool(follow['task']['game_ids']) and 'Amber game' in follow['execution_question']
 plain=resolve(engine.index,'What is its summary?',history,view.snapshot()['active'],datetime.fromisoformat(clock));checks['delivered_factual_possessive_without_style_still_binds']=bool(plain['task']['game_ids']) and 'Amber game' in plain['execution_question']
 q='What genre is Keep It Brief?';checks['source_title_resembling_style_not_masked']=masked(q,engine.index)==q
 result=reader.answer(q,locale='en',at=clock,planner=None);checks['source_title_resembling_style_normal_answer']='Controlled brief genre' in result.answer
 from app.knowledge.common.domain_flow.integration import answer as integrated_answer
 q='What genre is Amber game? Please keep it brief.';u=Understanding([MeaningTask(q,'games','C04','detail','genre','Amber game')],True,'controlled_integrated_style',{'model_called':False})
 result=integrated_answer(reader,q,locale='en',at=clock,planner=None,_understanding=u);checks['public_integration_preserves_source_answer_with_style']='Controlled amber genre' in result.answer
 checks['stale_reader_attribute_ignored_with_current_source_ids']=bool(result.decision_artifact['domain_flow']['typed_claims']) and {c['record_id'] for c in result.decision_artifact['domain_flow']['typed_claims']}=={'controlled_style_game'}
 details.append({'case':'direct_integration','answer':result.answer,'artifact':result.decision_artifact})
 from app.knowledge.common.flow_context import request_context
 with request_context() as ctx:
  ctx.input={'raw_question':q,'requested_locale':'en','effective_locale':'en','dialogue_resolution':{'execution_question':'What genre is Keep It Brief?'}}
  result=integrated_answer(reader,q,locale='en',at=clock,planner=None,_understanding=u)
  checks['unregistered_request_dialogue_blob_cannot_redirect_source']='Controlled amber genre' in result.answer and 'Controlled brief genre' not in result.answer
 from app.knowledge.common.domain_flow.understanding import parse
 from app.knowledge.common.domain_flow.graph_protocol import VERSION
 factual='What genre is Amber game?';phrase='Answer only that point.';q=factual+' '+phrase
 value={'version':VERSION,'focus':'game_description','context_quotes':[],'shared_bindings':[],'tasks':[{'id':'t1','quote':factual,'domain':'games','operation':'detail','facet':'genre','target':'Amber game','constraints':[],'ambiguous':False},{'id':'t2','quote':phrase,'domain':'general','operation':'unknown','facet':'','target':'','constraints':[],'ambiguous':False}]}
 parsed=parse(json.dumps(value),q);checks['actual_wire_drops_separate_general_style_task']=parsed.accepted and len(parsed.tasks)==1
 u=Understanding([MeaningTask(factual,'games','C04','detail','genre','Amber game'),MeaningTask(phrase,'games','C04','detail','genre')],True,'controlled_misclassified_style',{'model_called':False});guarded=apply(q,engine.index,u)
 checks['compiler_drops_style_misclassified_as_factual_task']=len(guarded.tasks)==1 and guarded.tasks[0].quote==factual
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'semantic_accuracy_claimed':False}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
