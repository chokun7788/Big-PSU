"""Restore scope metadata for retained answers; never replace answer values."""
import copy,hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision03_system';sys.path.insert(0,str(S))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now
from app.knowledge.records import canonical_json
audit=json.loads((R/'SOURCE_PROJECTION_AUDIT.json').read_text('utf8'))
# Engineering review of the source's topic/heading, not owner business facts.
review={
 'rule_en_checkin_natural':('C08','owner_policy'),
 'rule_en_payment_method_natural':('C09','owner_policy'),
 'rule_schedule_afternoon_time':('C11','bookable_periods'),
 'rule_schedule_morning_time':('C11','bookable_periods'),
 'rule_schedule_not_24_hours':('C11','bookable_periods'),
 'curated_damage_severe':('C10','owner_policy'),
 'curated_games_popular':('C04','summary'),
 'curated_penalty_appeal':('C10','owner_policy'),
 'curated_penalty_temp_suspension':('C10','owner_policy'),
 'curated_penalty_warning_suspension':('C10','owner_policy'),
 'curated_rule_food_drinks':('C10','owner_policy'),
 'curated_rule_lost_items':('C10','owner_policy'),
 'curated_rule_smoking_alcohol_drugs':('C10','owner_policy'),
 'curated_rule_weapons_gambling':('C10','owner_policy'),
 'curated_schedule_afternoon':('C11','bookable_periods'),
 'curated_schedule_morning':('C11','bookable_periods'),
 'curated_time_change_policy':('C08','owner_policy'),
 'curated_user_group_alias_general_adult':('C10','owner_policy'),
 'curated_user_group_alias_general_student':('C10','owner_policy'),
 'curated_knowledge_esports_definition':('C04','summary'),
 'curated_knowledge_esports_origin':('C04','summary'),
 'curated_knowledge_current_popular_games':('C04','summary'),
 'curated_knowledge_esports_careers':('C04','summary'),
 'curated_about_members_president':('C02','role'),
 'curated_about_members_club_president':('C02','role'),
 'curated_about_gallery_categories':('C01','description'),
 'owner_claim_membership':('C10','owner_policy'),
 'owner_claim_four_people':('C03','usage'),
}
old={}
for filename in ['curated_facts.jsonl','rule_patterns.jsonl']:
 for line in (R/'teacher/data/curated'/filename).read_text('utf8').splitlines():
  r=json.loads(line);old[r['id']]=r
store=CommonStore(S/'data/knowledge/common.sqlite');out=[]
with store.connect() as c:
 records=store.heads(c);before=c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0];sources=store.sources(c)
for row in audit['faq_answer_projection_gaps']:
 rid=row['record_id'];short=rid.removeprefix('migrated_faq_').removeprefix('migrated_')
 if short not in review:
  assert rid=='r114_rate_current_confirmation';continue
 record=copy.deepcopy(records[rid]);category,facet=review[short];question=value(record,'question');original=old.get(short)
 patterns=[]
 # Use original regex only when its answer identity still matches the draft.
 source_match=original is not None and re.sub(r'\s+','',original.get('answer_th',original.get('text','')))==re.sub(r'\s+','',value(record,'answer')['th'])
 if source_match:patterns+=original.get('patterns',[])
 patterns += [re.escape(s) for s in question.values() if s]
 profile={'route_category':category,'projected_facet':facet,'patterns':list(dict.fromkeys(patterns)),
  'priority':original.get('priority',0) if source_match else 0,'scope_basis':'original declared heading/topic; engineer reviewed routing only',
  'original_source_match':source_match,'historical_source_only':short.startswith('curated_knowledge_')}
 payload=canonical_json({'record_id':rid,'original_question':question,'original_answer_sha256':hashlib.sha256(canonical_json(value(record,'answer')).encode()).hexdigest(),
  'original_rule':original if source_match else None,'mapped_fields':{'legacy_search':profile},'business_answer_changed':False})
 sid='r124_faq_scope_'+hashlib.sha256(payload.encode()).hexdigest()[:24]
 if sid not in sources:store.add_source({'source_id':sid,'kind':'derived_curated','path':'R124 source projection audit and retained legacy query metadata',
  'sha256':hashlib.sha256(payload.encode()).hexdigest(),'authority_for':['faq'],'observed_at':now(),'trust':'internal_verified','public_url':None},payload,actor='r124_scope_restore')
 record['fields']['legacy_search']={'status':'known','value':profile,'evidence_refs':[{'source_id':sid,'locator':'/mapped_fields/legacy_search'}],
  'note':'Routing/search metadata only; original answer, authority and approvals preserved.'}
 original_answer=copy.deepcopy(record['fields']['answer'])
 saved=store.save(record,actor='r124_scope_restore',expected_version=record['revision'],change_note='Make retained source answer reachable from its declared scope')
 assert record['fields']['answer']==original_answer
 out.append({'record_id':rid,'category':category,'facet':facet,'source_id':sid,'original_source_match':source_match,'saved':saved,'answer_changed':False})
with store.connect() as c:assert c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0]==before
(R/'FAQ_SCOPE_RESTORATION.json').write_text(json.dumps({'records':out,'count':len(out),'approvals_unchanged':True,'answer_values_unchanged':True},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'scope_profiles_restored':len(out),'approvals_unchanged':True,'answer_values_unchanged':True}))
