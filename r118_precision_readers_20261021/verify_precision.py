"""Source contract verification, exclusively retained question text."""
import copy,json,sys,re,collections
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.contracts import Plan
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.precision import controls,coordinated_games,button_codes,button_text
from app.knowledge.common.domain_flow.projection import compile_snapshot
from app.knowledge.common.migrated_view import MigratedView
data=compile_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot());e=Engine(data)
rows=[json.loads(s) for s in (R.parent/'r116_retained_full_ten_percent_20261021/full01/RESULTS.jsonl').open(encoding='utf8')]
bykey={r['key']:r for r in rows};checks=[];details=[]
def check(name,ok,**extra):checks.append({'name':name,'passed':bool(ok),**extra})
def run(key,domain,cat,op,facet):
 r=bykey[key];q=r['question'];u=review(q,e.index,Understanding([MeaningTask(q,domain,cat,op,facet)],True,'contract_check'))
 out=e.answer(q,r['requested_locale'],allow_llm=False,understanding=u)
 details.append({'key':key,'question':q,'answer':out});return out
key='8acac2d360e8eac92ca9d4c4f51558a451fd9368afa41413edb043a5f783aac4'
q=bykey[key]['question'];out=run(key,'game_controls','C05','control','input_bindings')
check('R2_reverse_lookup_never_R3',len(out['claims'])==1 and out['claims'][0]['fact_id'].endswith('binding_8') and 'R2' in out['answer'])
bad=next(f for f in e.index.bycat['C05'] if 'god_of_war_ragnar' in f['record_id'] and button_text(f)=='r3')
p=e.finish_plan('C05',q,Plan(category='C05',ids=[bad['id']],status='answer'),__import__('datetime').datetime.now().astimezone())
check('final_validator_rejects_wrong_model_button',not p.ids and p.reason=='final_button_identity_mismatch')
exact_rows=[]
for r in rows:
 if r['domain']!='game_controls' or not button_codes(r['question']):continue
 p=controls(e.index,r['question'])
 if p and p.ids:
  want=button_codes(r['question']);found=set().union(*(button_codes(button_text(e.index.byid[k])) for k in p.ids))
  exact_rows.append({'key':r['key'],'requested':sorted(want),'selected':sorted(found),'status':p.status,'ids':p.ids})
  check('source_button_identity_'+r['key'][:10],found<=want and (p.status=='partial' or want<=found))
for k in ['6d26c7feeaf4f6aabd9d6dafc411b75359e43bfa789594941d80c2b94d7cd146','d502cb686f07b3bd58add13b1b775aae8ae5a8329e976e4317f36a17f89fd38e']:
 out=run(k,'reservation','C08','detail','owner_policy')
 check('customer_cancel_source_'+k[:8],bool(out['claims']) and all('cancel' in c['fact_id'] and not any(s in c['fact_id'] for s in ['invalid','suspension','checkin']) for c in out['claims']),answer=out['answer'])
out=run('e869467170e02fba6c045d82f418e6fde8729870e12377a453b4d40e407a5c42','members','C02','role_lookup','role')
check('inverse_role_finds_source_but_keeps_public_scope_guard',not out['claims'] and out['needs'][0]['reason']=='person_public_scope_not_confirmed' and out['needs'][0]['plan']['metadata'].get('source_match_exists'))
out=run('a1c90b6efa66d5a5dba8f4bd8559db108bf0254516e7929f37346ad730e6fd53','games','C04','detail','zone')
check('coordinated_editions_never_substitute_remastered_for_unqualified_II',out['status']=='partial' and len(out['claims'])==1 and out['claims'][0]['record_id']=='migrated_game_the_last_of_us_part_i' and bool(out['needs'][0]['plan']['metadata'].get('unanswered_targets')),answer=out['answer'])
out=run('1f7c4f9acc3f321bb2f052679f405ebd9f9bae73ad634842a3e0f95afba60813','games','C04','detail','zone')
check('unknown_nintendo_zone_not_inferred_from_name',out['status']=='partial' and all(c['facet']=='studio_services' for c in out['claims']))
for k in ['9813e160d170afb1642c7a117bdc3ab5253f5372ad62a7eb27ecdba7a283c1cb','b2ff4f05d34e5b2a82ae5cb5ede86f5a05bb022cf13531c682a39d936e4de5b7']:
 out=run(k,'game_controls','C05','list','input_bindings')
 check('complete_controls_'+k[:8],len(out['claims']) in {13,19},count=len(out['claims']))
qt=bykey['c178dbffcc336dbc23f659433245da5c9b82524b8f24b0afd874bf19d999c223']['question']
u=review(qt,e.index,Understanding([MeaningTask(qt,'competition_rules','C13','rule_lookup','rule_clause')],True,'contract_check'))
check('tournament_games_count_not_catalog_count',u.tasks[0].category=='C13')
# Data edits are in-memory verification only. The same retained question must
# observe a withdrawn binding immediately, never a stale cached answer.
cloned=copy.deepcopy(data);cloned['facts']=[f for f in cloned['facts'] if f['id']!='C05:controls_ps5_god_of_war_ragnar_k:binding_8']
check('withdrawn_binding_not_replaced_with_nearby_button',controls(Engine(cloned).index,q).reason=='exact_button_not_recorded')
for r in rows:
 if r['question'] not in ['Do I need to check in before playing VALORANT?','Counter-Strike 2 map pool ในกติกาคืออะไร','กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ']:continue
 u=review(r['question'],e.index,Understanding([MeaningTask(r['question'],'games','C04','detail','summary')],True,'retained_bad_proposal'))
 cat='C13' if 'map pool' in r['question'] else 'C08'
 check('procedural_context_overrides_game_description_'+r['key'][:8],u.accepted and u.tasks[0].category==cat)
 p=e.plan(cat,r['question'],meaning=u.tasks[0])
 fs=[e.index.byid[k] for k in p.ids or p.candidates]
 if cat=='C13':check('map_pool_reads_current_cs2_clause',bool(fs) and any('ANCIENT' in f['value']['en'] and 'TRAIN' in f['value']['en'] for f in fs) and all(f['category']=='C13' and 'CS2' in str(f['subject']) for f in fs),ids=p.ids)
 elif 'check in' in r['question']:check('checkin_candidates_are_not_game_or_luggage_facts',bool(fs) and all(f['category']=='C08' and '30' in f['value']['en'] and 'luggage' not in str(f).lower() for f in fs))
 else:check('booking_procedure_candidates_have_steps',bool(fs) and all(f['category']=='C08' and ('book' in f['value']['en'].lower() or 'จอง' in f['value']['th']) for f in fs))
from app.knowledge.common.domain_flow.understanding import parse,style_only_quote
old_run=[json.loads(s) for s in (R/'http01/RESULTS.jsonl').open(encoding='utf8')]
for r in old_run:
 if not any(s in r['question'] for s in ['วันจันทร์เช้าเปิดหรือปิด','ศุกร์บ่ายเปิดไหม']):continue
 raw=r['response']['decision_artifact']['understanding']['event']['raw_content']
 u=parse(raw,r['question'])
 check('polite_framing_is_not_a_second_factual_need_'+r['key'][:8],u.accepted and len(u.tasks)==1 and u.tasks[0].category=='C11')
check('factual_clauses_never_removed_as_style',all(not style_only_quote(r['question']) for r in rows if 'map pool' in r['question'] or 'cancel my booking' in r['question'] or 'check in before playing' in r['question']))
gpu=next(r for r in rows if 'What GPU model is inside the PCs' in r['question'])
out=run(gpu['key'],'equipment','C03','detail','specifications')
check('component_reads_exact_GPU_value_from_structured_source',len(out['claims'])==1 and 'NVIDIA GeForce RTX 5060 8GB' in out['claims'][0]['value'] and 'Intel Core' not in out['claims'][0]['value'],answer=out['answer'])
result={'passed':sum(c['passed'] for c in checks),'total':len(checks),'new_benchmark_questions':0,'network_calls':0,'checks':checks,'source_exact_button_cases':exact_rows}
(R/'PRECISION_CONTRACTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
(R/'CONTRACT_CASES.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'passed':result['passed'],'total':len(checks),'failed':[c for c in checks if not c['passed']]} ,ensure_ascii=False));assert all(c['passed'] for c in checks)
