"""Exhaustive data/operator contracts; customer question text is retained only."""
import collections,copy,json,os,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview'
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.projection import value,compile_snapshot
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.precision import controls,button_codes,button_text
data=compile_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot());e=Engine(data)
write=lambda n,v:(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
load=lambda n:json.loads((R/n).read_text('utf8'))
checks=[];cases=[]
def ck(name,ok,**details):checks.append({'name':name,'passed':bool(ok),**details})
records=data['records'];mapping={m['content_id']:m for m in load('RECORD_MAPPING.json')}
if (R/'CODE_ALIAS_MIGRATION.json').exists():
 for a in load('CODE_ALIAS_MIGRATION.json')['alias_decisions']:
  if a['disposition']=='added_search_alias_only':ck('legacy_code_alias_'+a['record_id']+'_'+a['alias'],a['alias'] in records[a['record_id']]['aliases'][a['locale']])
for item in load('LEGACY_RECORDS.json'):
 a=item['record'];m=mapping[a['content_id']];rid=m['native_record_id']
 if not rid:continue
 r=records[rid];fs=e.index.byrecord[rid]
 if a['kind']=='game_profile':
  want=set(value(r,'studio_zone_ids') or []);zone=[f for f in fs if f['facet']=='zone']
  ck('explicit_game_zone_'+rid,bool(zone) and want<=set(zone[0]['zone_ids']),expected=sorted(want))
 if a['kind']=='member':
  ck('published_public_profile_'+rid,r['fields']['public_scope']['status']=='known')
  for field in ['display_name','role','team','affiliation','period']:
   if value(r,field):ck('person_field_projected_'+rid+'_'+field,any(f['facet']==field for f in fs))
 if a['kind']=='control_map':
  ck('all_source_binding_rows_'+rid,len([f for f in fs if f['category']=='C05'])==a['facts']['control_count'])
 if a['kind']=='service_availability':
  ck('explicit_service_zone_'+rid,bool(value(r,'studio_zone_ids')))
for rid,r in records.items():
 if r['kind']=='game' and value(r,'official_description'):
  fs=[f for f in e.index.byrecord[rid] if f['facet']=='official_description']
  ck('full_description_and_source_scope_projected_'+rid,bool(fs) and fs[0].get('description_captured_at')==value(r,'description_captured_at') and bool(fs[0].get('description_scope_note')))
 if r['kind']=='service':
  fs=[f for f in e.index.byrecord[rid] if f['facet']=='service_capacity']
  ck('service_range_not_simultaneous_capacity_'+rid,bool(fs) and fs[0]['capacity_min']==value(r,'capacity_min') and fs[0]['capacity_max']==value(r,'capacity_max') and fs[0]['capacity_semantics']=='listed_service_participant_range_not_simultaneous_capacity')
 if r['kind']=='rate':ck('rate_declares_period_rounding_'+rid,value(r,'calculation_rule') is not None)
 if r['kind']=='schedule':
  slots=value(r,'service_slots');ck('weekday_play_periods_projected_'+rid,slots is not None and any(f['facet']=='service_periods' for f in e.index.byrecord[rid]))
  if slots is not None:ck('weekday_play_open_not_maintenance_'+rid,value(r,'service_closed')==(not any(s['state']=='open' for s in slots)))
for f in data['facts']:
 for p in (f.get('legacy_search') or {}).get('patterns',[]):
  try:re.compile(p);ok=True
  except re.error:ok=False
  ck('legacy_search_pattern_'+f['id']+'_'+str(len(checks)),ok)
jobs={j['key']:j for j in map(json.loads,(R.parent/'r118_precision_readers_20261021/SELECTED_JOBS.jsonl').open(encoding='utf8'))}
def run(key,domain,cat,op,facet):
 j=jobs[key];q=j['question'];u=review(q,e.index,Understanding([MeaningTask(q,domain,cat,op,facet)],True,'source_contract'))
 out=e.answer(q,j['locale'],at='2026-10-21T12:00:00+07:00',allow_llm=False,understanding=u)
 cases.append({'key':key,'question':q,'result':out});return out
for key in ['1f7c4f9acc3f321bb2f052679f405ebd9f9bae73ad634842a3e0f95afba60813','df43bd3875afe1ec13852f6a55eeaa9498f77bad85c26879dc068c595c49b556']:
 out=run(key,'games','C04','detail','zone');ck('native_nintendo_zone_reader_'+key[:8],bool(out['claims']) and all(c['facet']=='zone' and 'Nintendo Switch Zone' in c['value'] for c in out['claims']))
out=run('e869467170e02fba6c045d82f418e6fde8729870e12377a453b4d40e407a5c42','members','C02','role_lookup','role')
ck('inverse_chair_reader',bool(out['claims']) and all(c['facet']=='role' for c in out['claims']))
out=run('2ee7827caaaac21d3837cb4dd86c4e955dd51f018520dfc6f024a287bc9dd91e','members','C02','role_lookup','role')
ck('unique_source_surname_and_firstname_spelling',bool(out['claims']) and len({c['record_id'] for c in out['claims']})==1)
out=run('0f5e0fd0f7f40fed2280aa84538bf0cbe41bd47c2924eaeed55a495188465322','equipment','C03','detail','name')
ck('restored_Thai_mouse_alias_reaches_existing_equipment',bool(out['claims']) and all(c['record_id']=='equipment_gaming_mouse' for c in out['claims']))
for key in ['b32fb6babd0a86f30c5a9863fdc4e6cab54abe142a07ed3b5e3308a9034fb741','790d4406db2db9773074032f548a0c38b10f5a2874ea6e57bf911dede2d57b7e']:
 out=run(key,'schedule','C11','detail','open_periods');ck('play_maintenance_is_not_open_'+key[:8],bool(out['claims']) and 'บำรุงรักษา' in out['answer'] and 'ไม่เปิด' in out['answer'])
out=run('044f667114ab611667f0d97496b6ba029d49dfd88337fc90123cd7a189623458','service_fee','C06','price_calculate','amount')
ck('original_rounding_used_by_native_calculator',out['status']=='answer' and bool(out['needs'][0]['computations']) and out['needs'][0]['computations'][0]['total_thb']==300)
for key,domain,cat,facet in [('8acac2d360e8eac92ca9d4c4f51558a451fd9368afa41413edb043a5f783aac4','game_controls','C05','input_bindings'),('88b3a23be4d1646dfc07b79b19b6118016e431f6bb281f64facf06b6dc09b0bf','equipment','C03','specifications'),('83ff647fde496d6bf0fae1997991043856653dbb8db4f253c79c209ee335dce5','reservation','C08','owner_policy')]:
 out=run(key,domain,cat,'detail',facet)
 if cat=='C08':
  p=e.plan(cat,jobs[key]['question']);fs=[e.index.byid[k] for k in p.ids or p.candidates]
  ck('checkin_scoped_source_candidates_before_model_selection',bool(fs) and all(f['category']=='C08' and '30' in f['value']['en'] for f in fs))
 else:ck('retained_exact_reader_'+key[:8],bool(out['claims']) and all(c['fact_id'].startswith(cat+':') for c in out['claims']))
# Withdraw published scope in memory; the same retained query must stop using
# profile data. No writes to source or approval state occur.
clone=copy.deepcopy(data)
for r in clone['records'].values():
 if r['kind']=='person':r['fields']['public_scope']={'status':'unknown','value':None,'evidence_refs':[],'note':'contract-only withdrawal'}
tmp=Engine(clone);q=jobs['e869467170e02fba6c045d82f418e6fde8729870e12377a453b4d40e407a5c42']['question'];p=tmp.plan('C02',q);p=tmp.finish_plan('C02',q,p,reference_time('2026-10-21T12:00:00+07:00'))
ck('public_scope_withdrawal_blocks_same_query',not p.ids and p.reason=='person_public_scope_not_confirmed')
result={'passed':sum(c['passed'] for c in checks),'total':len(checks),'failed':[c for c in checks if not c['passed']],'checks':checks,'new_benchmark_questions':0,'network_calls':0}
write('READER_CONTRACTS.json',result);write('READER_CASES.json',cases);print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False));assert not result['failed']
