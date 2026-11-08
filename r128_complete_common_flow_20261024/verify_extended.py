"""Shared boundaries, source additions/edits/withdrawals, and fourteen category receipts."""
import copy,hashlib,json,os,sys,time
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template,CATALOG,value,validate
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.dialogue_task import resolve
from app.knowledge.common.domain_flow.financial import audience_mentions
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.temporal import parse
OUT=R/('extended_'+str(time.time_ns()));OUT.mkdir();checks={};results=[]
snap=MigratedView(S/'data/knowledge/common.sqlite').snapshot();engine=Engine.from_snapshot(snap,cache_key=S);idx=engine.index;at=datetime.fromisoformat('2026-10-24T12:00:00+07:00')
groups,_=audience_mentions(idx,'นักศึกษา PSU 1 คนกับบุคคลทั่วไป 2 คน เล่น PC 2 ชั่วโมง รวมกี่บาท')
checks['thai_short_alias_not_inside_common_word']=len(groups)==2
checks['english_month_date']=parse('Is it open on October 26?',at.date())[0].isoformat()=='2026-10-26'
checks['thai_word_relative_date']=parse('อีกสามวันเปิดไหม',at.date())[0].isoformat()=='2026-10-27'
checks['next_weekday_resolved']=parse('วันจันทร์หน้าเข้าไปเล่นได้ไหม',at.date())[0].isoformat()=='2026-10-26'
checks['invalid_english_date_not_rolled']=parse('February 31',at.date())==(None,'invalid')
def history_for(context):return [{'role':'assistant','text':'delivered','delivery_status':'client_acknowledged','common_read_state':{'schema_version':1,'dialogue_task':context['task']}}]
original=resolve(idx,'นักศึกษา PSU 1 คนกับบุคคลทั่วไป 2 คน เล่น PC 2 ชั่วโมง ราคาเท่าไหร่',[],snap['active'],at)
resumed=resolve(idx,'แล้วสามชั่วโมงล่ะ',history_for(original),snap['active'],at)
checks['mixed_audience_followup_keeps_individual_counts']=sorted(resumed['task']['person_counts'].values())==[1,2] and '180' in resumed['execution_question']
simple=resolve(idx,'บุคคลทั่วไปเล่น PC 1 ชั่วโมง ราคาเท่าไหร่',[],snap['active'],at)
simple2=resolve(idx,'แล้วสองชั่วโมงล่ะ',history_for(simple),snap['active'],at)
simple3=resolve(idx,'เปลี่ยนเป็น PS5 ล่ะ',history_for(simple2),snap['active'],at)
checks['platform_entity_does_not_block_financial_followup']='120' in simple3['execution_question'] and bool(simple3['task']['audience_ids']) and simple3['task']['platforms']==['PS5']
changed=resolve(idx,'ไม่ใช่ PC เปลี่ยนเป็น PS5 ล่ะ',history_for(resumed),snap['active'],at)
checks['negated_platform_does_not_survive_replacement']=changed['task']['platforms']==['PS5'] and 'PC' not in changed['execution_question']
unrelated=resolve(idx,'PS5 มีปุ่มอะไรบ้าง',history_for(original),snap['active'],at)
checks['new_control_need_not_hijacked_by_previous_price']=not unrelated['execution_question'].startswith('ราคา ')
live=resolve(idx,'PC2 วันที่ 27 ตุลาคม 2026 เวลา 15:00-16:00 ว่างไหม',[],snap['active'],at)
other=resolve(idx,'แล้ว PC3 ล่ะ',history_for(live),snap['active'],at)
checks['live_replacement_keeps_date_and_window']='15:00-16:00' in other['execution_question'] and '2026-10-27' in other['execution_question'] and 'PC3' in other['execution_question']
rent=resolve(idx,'ราคาเหมา PC เต็มวัน หน่วยงานภายใน',[],snap['active'],at)
rent2=resolve(idx,'แล้วครึ่งวันล่ะ',history_for(rent),snap['active'],at)
checks['rental_followup_keeps_platform_and_replaces_period']='ครึ่งวัน' in rent2['execution_question'] and 'PC' in rent2['execution_question'] and 'เต็มวัน' not in rent2['execution_question']
mixed=engine.answer(resumed['execution_question'],'th',at=at,allow_llm=False,understanding=propose(idx,resumed['execution_question']))
checks['resumed_group_counts_reach_real_financial_reader']='420' in mixed['answer']
rent_result=engine.answer(rent['execution_question'],'th',at=at,allow_llm=False,understanding=propose(idx,rent['execution_question']))
checks['rental_intent_reaches_package_reader']=bool(rent_result['claims']) and all(c['facet']=='amount_thb' for c in rent_result['claims'])
q='PC กับ PS5 มีเกมอะไรบ้าง';u=propose(idx,q)
from app.knowledge.common.domain_flow.meaning_review import review
if u is None:u=review(q,idx,Understanding())
answer=engine.answer(q,'th',at=at,allow_llm=False,understanding=u);results.append({'question':q,'result':answer})
checks['coordinated_platforms_have_both_sources']={c['record_id'] for c in answer['claims']}=={f['record_id'] for p in ['PC','PS5'] for f in idx.bind('C04',p) if f['facet']=='game_catalog'}
compiled=compile_request(q,u,idx,{'release_id':snap['active'],'epoch':snap['epoch'],'reference_time':at.isoformat()})
tampered=copy.deepcopy(answer['needs'][0]);ps5={f['id'] for f in idx.bind('C04','PS5')};tampered['claims']=[c for c in tampered['claims'] if c['fact_id'] in ps5]
ledger=assess(idx,compiled.tasks[0],tampered,compiled.snapshot,q)
checks['dropping_pc_detected_despite_valid_ps5_refs']='explicit_target_not_delivered' in ledger['reason_codes'] and not ledger['all_obligations_fulfilled']
checks['folded_duplicate_game_keeps_zone_relations']=bool(engine.plan('C04','God of War Ragnarök เล่นได้ที่โซนไหน',at,meaning=MeaningTask('God of War Ragnarök เล่นได้ที่โซนไหน','games','C04','detail','zone')).ids)
# Actual save API, isolated empty database. No production approvals or real facts are changed.
store=CommonStore(OUT/'source_additions.sqlite');store.initialize(allow_demo=False)
def save_record(kind,rid,fields,aliases=None,revision=0):
 r=template(kind);r['record_id']=rid;r['aliases']=aliases or {'th':[],'en':[]}
 document={'fields':fields};text=json.dumps(document,ensure_ascii=False,sort_keys=True)
 sid='test_'+hashlib.sha256(text.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'controlled-test-only://'+sid,'sha256':hashlib.sha256(text.encode()).hexdigest(),'authority_for':list(CATALOG),'observed_at':'2026-10-24T12:00:00+07:00','trust':'internal_verified','public_url':None}
 store.add_source(source,text,actor='controlled-test')
 for key,v in fields.items():r['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/fields/'+key}],'note':''}
 return store.save(r,actor='controlled-test',expected_version=revision)
def snapshot():
 with store.connect() as c:
  records=store.heads(c);sources={k:v[0] for k,v in store.sources(c).items()};meta=dict(c.execute('SELECT key,value FROM cc_meta'));withdrawn=[r[0] for r in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')]
 return {'active':'controlled-r128-additions','epoch':int(meta['epoch']),'allow_demo':False,'evaluation_draft_only':True,'release':{'records':records,'sources':sources},'withdrawn':withdrawn}
class View:
 path=OUT/'source_additions.sqlite'
 def snapshot(self):return snapshot()
 def still_current(self,s):return s['epoch']==snapshot()['epoch']
save_record('game','fixture_game_alpha',{'title':{'th':'เกมทดสอบอัลฟา','en':'Fixture Alpha'},'summary':{'th':'คำอธิบายจากข้อมูลทดสอบ','en':'Controlled game description'}},{'th':['เกมทดสอบอัลฟา'],'en':['Fixture Alpha']})
save_record('game_mode','fixture_mode_alpha',{'game_id':'fixture_game_alpha','mode_name':{'th':'local co-op','en':'local co-op'},'platform':'PC','players_min':1,'players_max':4,'studio_supported':True})
e=Engine.from_snapshot(snapshot(),cache_key=View.path)
q='มีเกมอะไรบน PC เล่นพร้อมกัน 4 คนได้บ้าง';meaning=MeaningTask(q,'games','C04','list','players_max')
mode=e.answer(q,'th',at=at,allow_llm=False,understanding=Understanding([meaning],True));results.append({'question':q,'controlled_source_addition':True,'result':mode})
checks['owner_added_game_mode_selected_without_code_or_model']=bool(mode['claims']) and all(c['record_id']=='fixture_mode_alpha' for c in mode['claims'])
save_record('game_mode','fixture_mode_switch',{'game_id':'fixture_game_alpha','mode_name':{'th':'local co-op','en':'local co-op'},'platform':'Nintendo Switch','players_min':1,'players_max':4,'studio_supported':True})
natural=CommonAnswerer(View()).answer(q,locale='th',at=at,planner=None)
checks['new_mode_natural_question_uses_same_shared_flow']=bool(natural.decision_artifact.get('domain_flow',{}).get('typed_claims'))
checks['player_filter_does_not_leak_other_platform']=all(c['record_id']=='fixture_mode_alpha' for c in natural.decision_artifact.get('domain_flow',{}).get('typed_claims',[]))
save_record('game_mode','fixture_mode_alpha',{'game_id':'fixture_game_alpha','mode_name':{'th':'local co-op','en':'local co-op'},'platform':'PC','players_min':1,'players_max':2,'studio_supported':True},revision=1)
e2=Engine.from_snapshot(snapshot(),cache_key=View.path)
checks['owner_edit_invalidates_source_index']=not e2.answer(q,'th',at=at,allow_llm=False,understanding=Understanding([meaning],True))['claims']
save_record('faq','fixture_faq_alpha',{'question':{'th':'ข้อมูลทดสอบอัลฟามีเงื่อนไขอะไร','en':'What is the alpha test condition?'},'answer':{'th':'เงื่อนไขที่เพิ่มจากแบบฟอร์มทดสอบ','en':'Condition added through the test form'},'intent_key':'policy.alpha_test'})
res=CommonAnswerer(View()).answer('ข้อมูลทดสอบอัลฟามีเงื่อนไขอะไร',locale='th',at=at,planner=None)
checks['owner_added_faq_answers_without_new_parser']='เงื่อนไขที่เพิ่มจากแบบฟอร์มทดสอบ' in res.answer
store.withdraw('fixture_faq_alpha',actor='controlled-test')
res=CommonAnswerer(View()).answer('ข้อมูลทดสอบอัลฟามีเงื่อนไขอะไร',locale='th',at=at,planner=None)
checks['withdrawn_faq_not_replayed']=res is None or 'เงื่อนไขที่เพิ่มจากแบบฟอร์มทดสอบ' not in res.answer
save_record('equipment_model','fixture_device_alpha',{'name':{'th':'อุปกรณ์ทดสอบอัลฟา','en':'Fixture Device'},'device_type':'peripheral','usage':{'th':'ใช้สำหรับกรณีทดสอบ','en':'Used for a controlled test'}},{'th':['อุปกรณ์ทดสอบอัลฟา'],'en':['Fixture Device']})
res=CommonAnswerer(View()).answer('อุปกรณ์ทดสอบอัลฟาคืออะไร',locale='th',at=at,planner=None)
checks['owner_added_equipment_works_without_parser_change']='ใช้สำหรับกรณีทดสอบ' in res.answer
checks['real_data_not_used_as_fixture_output']=all(not r['record_id'].startswith('migrated') for r in snapshot()['release']['records'].values())
from app.knowledge.common.domain_flow.readers import policy
checks['english_food_words_do_not_match_game_titles']=all(policy(idx,'C10','Can I play '+name+' in the VR Zone?') is None for name in ['Beat Saber','Heavy Rain','Moving Out 2','Job Simulator'])
q='Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?'
clause=engine.plan('C13',q,at,MeaningTask(q,'competition_rules','C13','rule_lookup','rule_clause'))
checks['specific_rule_clause_contains_requested_settings']=bool(clause.ids) and all(s in ' '.join(idx.byid[k]['value']['en'] for k in clause.ids).lower() for s in ['brightness','resolution','crosshair'])
generic='อยากทราบลำดับการเริ่มใช้บริการ'
bound=engine.plan('C08',generic,at,MeaningTask(generic,'reservation','C08','detail','owner_policy',canonical_operation='policy.booking_steps'))
checks['canonical_operation_reads_without_reparsing_booking_keyword']=bool(bound.ids)
media_q='May I record video inside the studio?'
media=engine.plan('C10',media_q,at,propose(idx,media_q).tasks[0])
checks['physical_recording_not_inferred_from_game_capture']=bool(media.ids) and media.status=='partial' and media.metadata.get('media_scope_unconfirmed') is True
# Every category is exercised against its actual source adapter; privacy/source gaps are valid terminals.
domains={'C01':'contact','C02':'members','C03':'equipment','C04':'games','C05':'game_controls','C06':'service_fee','C07':'rental','C08':'reservation','C09':'payment','C10':'rules','C11':'schedule','C12':'live','C13':'competition_rules','C14':'news'}
lanes=[]
for cat,domain in domains.items():
 fs=idx.bycat[cat]
 if cat=='C12':lanes.append({'category':cat,'proof':'verify_live.py actual native bridge + unavailable/stale/mapping/unknown-resource checks'});continue
 f=next((f for f in fs if f['facet'] in {'role','summary','amount','amount_thb','owner_policy','service_periods','body'}),fs[0]);facet=f['facet']
 if cat=='C05':facet='input_bindings'
 if cat=='C11':facet='open_periods'
 op='list' if cat=='C05' else 'price_calculate' if cat in {'C06','C07'} else 'rule_lookup' if cat=='C13' else 'detail'
 query=f['record_id']+' '+f['label']['en'];u=Understanding([MeaningTask(query,domain,cat,op,facet,target=f['record_id'])],True)
 result=engine.answer(query,'en',at=at,allow_llm=False,understanding=u)
 lanes.append({'category':cat,'question':query,'status':result['status'],'claims':len(result['claims']),'contract':result.get('execution_contract')})
 checks[cat+'_source_adapter_bounded']=result['status'] in {'answer','partial','missing_source','missing_input','not_current','unavailable'} and not any(t.get('fatal') for t in result.get('execution_contract',{}).get('tasks',[]))
checks['all_14_categories_exercised']=len(lanes)==14
summary={'all_passed':all(checks.values()),'checks':checks,'controlled_database':str(store.path),'real_data_modified':False,'approvals_modified':False,'model_calls':0,'human_semantic_accuracy':None,'output':str(OUT)}
(OUT/'RESULTS.json').write_text(json.dumps({'summary':summary,'lanes':lanes,'results':results},ensure_ascii=False,indent=2,default=str),'utf8');print(json.dumps(summary,ensure_ascii=False,indent=2));assert summary['all_passed']
