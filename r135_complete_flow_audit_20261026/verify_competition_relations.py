"""Owner-added rules keep game/event/edition and dependency identity."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template,validate,release_errors
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.scope import reference_time
out=R/('competition_relations_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};rows=[]
def known(v):return {'status':'known','value':v,'evidence_refs':[],'note':''}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 for k,v in fields.items():r['fields'][k]=known(v)
 return save_owner_record(store,r,0,'controlled-test')['record']
game=create('game','controlled_rule_game',{'title':{'th':'เกมโทแพซทดสอบ','en':'Controlled Topaz'}})
events={};rules={}
for year in [2025,2026]:
 events[year]=create('competition','controlled_cup_'+str(year),{'game_id':game['record_id'],'event_name':{'th':'โทแพซคัพ','en':'Topaz Cup'},'rulebook_release':str(year),'coverage':'complete'})
 rules[year]=create('competition_rule','controlled_rule_'+str(year),{'competition_id':events[year]['record_id'],'section_number':'1','facet':'competition_format','heading':{'th':'รูปแบบการแข่งขัน','en':'Competition format'},'text':{'th':'ต้องแข่งขันแบบ FT'+('2' if year==2025 else '3'),'en':'Matches must use FT'+('2' if year==2025 else '3')+' format.'},'completeness':'complete','depends_on_ids':[]})
with store.connect() as c:records=store.heads(c);sources=store.sources(c)
checks['valid_event_and_rule_foreign_keys_accepted']=not validate(events[2026],records,sources) and not validate(rules[2026],records,sources)
bad=copy.deepcopy(rules[2026]);bad['fields']['competition_id']['value']=game['record_id'];checks['rule_cannot_link_game_as_event']=any('wrong reference kind' in e for e in validate(bad,records,sources))
bad=copy.deepcopy(events[2026]);bad['fields']['game_id']['value']=rules[2026]['record_id'];checks['event_cannot_link_rule_as_game']=any('wrong reference kind' in e for e in validate(bad,records,sources))
cross=copy.deepcopy(rules[2026]);cross['fields']['depends_on_ids']=known([rules[2025]['record_id']]);checks['cross_edition_rule_dependency_rejected']=any('Cross-competition rule dependency' in e for e in release_errors({**records,cross['record_id']:cross},sources))
cycle=copy.deepcopy(rules[2026]);cycle['fields']['depends_on_ids']=known([cycle['record_id']]);checks['cyclic_rule_dependency_rejected']=any('Cyclic competition dependency' in e for e in release_errors({**records,cycle['record_id']:cycle},sources))
view=DraftSnapshotView(store);e=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
for year,expected,wrong in [(2025,'FT2','FT3'),(2026,'FT3','FT2')]:
 q='What is the competition format of Topaz Cup '+str(year)+'?';u=Understanding([MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause','Topaz Cup')],True,'controlled_rule_edition',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);rows.append({'q':q,'result':r})
 checks['edition_'+str(year)+'_source_delivered_only']=any(c['record_id']==rules[year]['record_id'] and expected in c['value'] for c in r['claims']) and all(wrong not in c['value'] for c in r['claims'])
q='What is the competition format of Topaz Cup?';u=Understanding([MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause','Topaz Cup')],True,'controlled_rule_ambiguity',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);rows.append({'q':q,'result':r});checks['ambiguous_edition_not_arbitrarily_latest']=not r['claims'] and r['status']!='answer'
event=create('competition','controlled_cup_alpha',{'game_id':game['record_id'],'event_name':{'th':'โทแพซคัพ','en':'Topaz Cup'},'rulebook_release':'vAlpha','coverage':'complete'})
rule=create('competition_rule','controlled_rule_alpha',{'competition_id':event['record_id'],'section_number':'1','facet':'competition_format','heading':{'th':'รูปแบบการแข่งขัน','en':'Competition format'},'text':{'th':'ต้องแข่งขันแบบ FT4','en':'Matches must use FT4 format.'},'completeness':'complete','depends_on_ids':[]})
e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);q='What is the competition format of Topaz Cup vAlpha?';u=Understanding([MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause','Topaz Cup')],True,'controlled_named_release',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);rows.append({'q':q,'result':r});checks['nonnumeric_rulebook_release_is_source_bound']=len(r['claims'])==1 and r['claims'][0]['record_id']==rule['record_id'] and 'FT4' in r['claims'][0]['value']
from app.knowledge.common.domain_flow.receipt_scope import check
from types import SimpleNamespace
t=SimpleNamespace(category='C13',target_span=SimpleNamespace(text='Topaz Cup'))
wrong=next(f for f in e.index.bycat['C13'] if f['record_id']==rules[2026]['record_id']);checks['other_edition_receipt_rejected_independently']='source_receipt_event_edition_mismatch' in check(e.index,t,wrong,q)['errors']
checks['rule_projection_carries_edition_relation_source']=any(ref in e.index.byrecord[rule['record_id']][0]['evidence_refs'] for ref in event['fields']['rulebook_release']['evidence_refs'])
q='Compare competition format of Topaz Cup 2025 and Topaz Cup 2026';u=Understanding([MeaningTask(q,'competition_rules','C13','compare','rule_clause','Topaz Cup')],True,'controlled_compare_releases',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);rows.append({'q':q,'result':r});checks['explicit_two_editions_compare_both_without_unasked_release']={c['record_id'] for c in r['claims']}=={rules[2025]['record_id'],rules[2026]['record_id']} and not any(n['execution_contract']['fatal'] for n in r['needs'])
checks['comparison_display_distinguishes_actual_release_labels']='Topaz Cup — 2025' in r['answer'] and 'Topaz Cup — 2026' in r['answer']
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
context=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,context).tasks[0];child=copy.deepcopy(r['needs'][0]);child['claims']=child['claims'][:1]
proof=assess(e.index,task,child,context,q);checks['one_compared_edition_cannot_complete_both_options']=any(o['kind']=='comparison_event_option' and not o['fulfilled'] for o in proof['obligations'])
wrong=next(f for f in e.index.bycat['C13'] if f['record_id']==rule['record_id']);checks['unasked_third_edition_rejected_in_compare']='source_receipt_comparison_event_mismatch' in check(e.index,task,wrong,q)['errors']
q='What is the competition format of Topaz Cup 2099?';u=Understanding([MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause','Topaz Cup')],True,'controlled_absent_edition',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);checks['absent_edition_not_replaced_by_available_rules']=not r['claims']
game=save_owner_record(store,{**game,'fields':{**game['fields'],'title':known({'th':'เกมแข่งรถทดสอบ 2025','en':'Controlled Racer 2025'})}},1,'controlled-test')['record'];e=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
q='What is the competition format of Controlled Racer 2025?';u=Understanding([MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause','Controlled Racer 2025')],True,'controlled_game_edition_year',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);checks['game_title_year_does_not_choose_event_release']=not r['claims'] and r['status']=='missing_input'
q='What is the competition format of Controlled Racer 2025 in Topaz Cup 2026?';u=Understanding([MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause','Controlled Racer 2025')],True,'controlled_game_and_event_year',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);checks['explicit_event_year_survives_game_title_year_mask']={c['record_id'] for c in r['claims']}=={rules[2026]['record_id']}
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_data_modified':False,'controlled_source_not_real_business_data':True};(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
