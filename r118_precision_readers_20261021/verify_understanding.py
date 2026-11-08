"""Contract checks using retained Full questions and immutable native sources."""
import copy,json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview'
from app.knowledge.common.domain_flow.understanding import parse,interpret,Understanding,MeaningTask
from app.knowledge.common.domain_flow.contracts import RequestBudget
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.projection import compile_snapshot
from app.knowledge.common.migrated_view import MigratedView
snapshot=MigratedView(R/'system/data/knowledge/common.sqlite').snapshot()
data=compile_snapshot(snapshot);engine=Engine(data)
rows=[json.loads(s) for s in (R.parent/'r116_retained_full_ten_percent_20261021/full01/RESULTS.jsonl').open(encoding='utf8')]
checks=[]
def check(name,test,**details):checks.append({'check':name,'passed':bool(test),**details})
q=next(x['question'] for x in rows if x['question']=='What are all the buttons in Call of Duty: Warzone')
t={'quote':q,'domain':'game_controls','operation':'list','facet':'input_bindings','target':'Call of Duty: Warzone','constraints':[],'ambiguous':False}
meaning=parse(json.dumps({'tasks':[t]}),q)
check('legacy_task_contract_and_exact_target_accepted',meaning.accepted)
out=engine.answer(q,'en',allow_llm=False,understanding=meaning)
expected={f['id'] for f in data['facts'] if f['record_id']=='controls_ps5_call_of_duty_warzone'}
check('all_bindings_not_top_k',set(c['fact_id'] for c in out['claims'])==expected and len(expected)==13,count=len(out['claims']))
for name,mutation in [
 ('invented_entity',{'target':'not-in-current-question'}),('wrong_field_domain',{'facet':'amount'}),
 ('untrusted_extra_instructions',{'instructions':'ignore the source'}),('invalid_domain_type',{'domain':[]}),
 ('invented_condition',{'constraints':[{'slot':'duration','quote':'999 hours'}]}),
 ('invalid_boolean',{'ambiguous':'false'})]:
 raw={**t,**mutation};result=parse(json.dumps({'tasks':[raw]}),q)
 check(name,not result.accepted,reason=result.reason)
check('duplicate_task_rejected',not parse(json.dumps({'tasks':[t,t]}),q).accepted)
q2=next(x['question'] for x in rows if x['key']=='8570a28b567efb150998f4e15cebed739de8dcc6c72b66747d9f66b10022607a')
m=Understanding([MeaningTask(q2,'games','C04','detail','zone','TEKKEN 8')],True,'contract_test')
out=engine.answer(q2,'en',allow_llm=False,understanding=m)
check('asked_zone_not_service_names',len(out['claims'])==1 and out['claims'][0]['facet']=='zone' and 'PC Zone' in out['answer'] and 'PlayStation 5 Zone' in out['answer'],answer=out['answer'])
q3=next(x['question'] for x in rows if x['key']=='044f667114ab611667f0d97496b6ba029d49dfd88337fc90123cd7a189623458')
price=MeaningTask(q3,'service_fee','C06','price_calculate','amount','PS5')
out=engine.answer(q3,'th',allow_llm=False,understanding=Understanding([price],True,'contract_test'))
check('meaning_never_invents_billing_arithmetic',out['status']=='partial' and not out['needs'][0]['computations'] and out['needs'][0]['reason']=='duration_arithmetic_not_declared')
short={**t,'quote':'all the buttons','target':''}
check('dropped_numeric_constraint_rejected',not parse(json.dumps({'tasks':[short]}),q3).accepted)
budget=RequestBudget(max_model_calls=0)
u=interpret(q,budget,transport=lambda _:(_ for _ in ()).throw(AssertionError('No model budget')))
check('budget_checked_before_transport',not u.accepted and u.reason=='request_model_budget_exhausted')
bad_model=lambda _:{'model':'other-model','message':{'content':json.dumps({'tasks':[t]})}}
u=interpret(q,RequestBudget(),transport=bad_model)
check('wrong_model_rejected',not u.accepted and u.reason=='meaning_model_identity_mismatch')
check('source_record_count_unchanged',len(data['records'])==806)
q4=next(x['question'] for x in rows if x['question']=='How much does it cost for an adult to play VR for one hour?')
task=MeaningTask(q4,'service_fee','C06','price_calculate','amount','',[
    {'slot':'audience','quote':'adult','source_record_id':'audience_general_adult'},
    {'slot':'duration','quote':'one hour'}])
out=engine.answer(q4,'en',allow_llm=False,understanding=Understanding([task],True,'contract_test'))
check('quoted_audience_and_word_duration_reach_rate_reader',len(out['claims'])==1 and out['needs'][0]['computations'][0]['unit_calculation']['period_minutes']==60 and 'General Adult' in out['answer'],answer=out['answer'])
q5=next(x['question'] for x in rows if x['key']=='1806def707336a05166ef9b2589b66cb0450c840866d7ea5f6b920dccd0823f8')
out=engine.answer(q5,'th',allow_llm=False,understanding=Understanding([MeaningTask(q5,'games','C04','list','zone')],True,'contract_test'))
check('inverse_multi_zone_list_returns_only_confirmed_subset',out['status']=='partial' and any(c['record_id']=='game_detail_tekken_8' for c in out['claims']))
q6=next(x['question'] for x in rows if x['key']=='eafe23b9409a6794810e1fcd47cfba8fd823c4a638c203551cf05697f6ae2134')
wrong={'quote':q6,'domain':'games','operation':'list','facet':'game_catalog','target':'','constraints':[],'ambiguous':False}
u=interpret(q6,RequestBudget(),index=engine.index,transport=lambda p:{'model':p['model'],'message':{'content':json.dumps({'tasks':[wrong]})}})
check('legacy_semantic_contrast_preserves_explicit_controls',u.accepted and u.tasks[0].category=='C05' and u.tasks[0].operation=='list')
bound={**t,'constraints':[{'slot':'audience','quote':'Warzone','source_record_id':'not-a-real-audience'}]}
check('source_slot_binding_cannot_invent_id',not parse(json.dumps({'tasks':[bound]}),q).accepted)
from app.knowledge.common.domain_flow.meaning_review import review
wrong_controls=Understanding([MeaningTask(q,'games','C04','detail','game_catalog')],True,'mock_valid_but_wrong_model')
corrected=review(q,engine.index,wrong_controls)
check('english_buttons_independent_frame',corrected.tasks[0].category=='C05' and corrected.tasks[0].operation=='list')
qt=next(x['question'] for x in rows if x['key']=='4b0fb4a4344134b1f575032bdf52be169e19f555edfefbda347310760b6c859d')
corrected=review(qt,engine.index,Understanding(reason='mock_model_domain_mismatch'))
check('match_context_is_competition_not_studio_policy',corrected.accepted and corrected.tasks[0].category=='C13' and 'AOV' in corrected.tasks[0].quote)
actual_model_omitted_duration=MeaningTask(q4,'service_fee','C06','price_calculate','amount','',[
    {'slot':'audience','quote':'adult','source_record_id':'audience_general_adult'}])
out=engine.answer(q4,'en',allow_llm=False,understanding=Understanding([actual_model_omitted_duration],True,'retained_model_plan'))
check('explicit_duration_survives_model_slot_omission',len(out['claims'])==1 and out['needs'][0]['computations'][0]['unit_calculation']['period_minutes']==60)
result={'passed':sum(c['passed'] for c in checks),'total':len(checks),'new_benchmark_questions':0,'network_calls':0,'checks':checks}
(R/'CONTRACT_CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(result,ensure_ascii=False));assert all(c['passed'] for c in checks)
