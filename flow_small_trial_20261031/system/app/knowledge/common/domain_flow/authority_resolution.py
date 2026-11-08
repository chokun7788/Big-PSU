"""Bilingual duplicate identity and evidence-backed scoped supersession only."""
import json
from .projection import value
from .scope import norm,validity_allows
def semantic_scope_note(record):
 """Separate the existing import provenance envelope from applicability prose.

 Only the exact documented machine envelope is nonsemantic. Arbitrary JSON,
 extra keys and human scope text remain constraints; source data is not edited.
 """
 field=record.get('fields',{}).get('scope_note');raw=value(record,'scope_note')
 if isinstance(raw,dict) and set(raw)<={'th','en'} and raw:
  try:
   parsed=[json.loads(s) for s in raw.values() if s]
   allowed={'category','facet','subject','label','section_number','english_translation_missing','source_record_id'}
   if parsed and all(isinstance(x,dict) and set(x)=={'r114_fact'} and isinstance(x['r114_fact'],dict) and set(x['r114_fact'])<=allowed and {'category','facet','subject','source_record_id'}<=set(x['r114_fact']) for x in parsed):return None
  except (ValueError,TypeError):pass
 return field

def scope_signature(record):
 """Unknown, not-applicable and known-empty conditions are not equivalent."""
 scope={}
 for key in ['topic','intent_key','scope_note','conditions_all','exceptions','preconditions','service_id','audience_id','competition_id']:
  field=semantic_scope_note(record) if key=='scope_note' else record.get('fields',{}).get(key)
  scope[key]={'status':field.get('status'),'value':field.get('value') if field.get('status')=='known' else None} if field is not None else {'status':'absent','value':None}
 return {'fields':scope,'validity':record.get('validity')}

def signature(index,f):
 r=index.records.get(f['record_id'],{})
 return json.dumps({'category':f['category'],'facet':f['facet'],'policy_intent':f.get('policy_intent'),'th':norm(f['value'].get('th','')),'en':norm(f['value'].get('en','')),'scope':scope_signature(r),'translation_missing':bool(f.get('english_translation_missing'))},ensure_ascii=False,sort_keys=True)

def binding_covers_fact(index,binding,fact):
 """A field/fragment mapping is not authority over every field in a record."""
 from .projection import bilingual
 from ..claim_bindings import _project
 from decimal import Decimal
 ref=binding.get('value_ref',{});record=index.records.get(fact['record_id'],{})
 if ref.get('record_id')!=fact['record_id']:return False
 field=record.get('fields',{}).get(ref.get('field'),{});refs=field.get('evidence_refs',[])
 if field.get('status')!='known' or not refs or any(r not in fact.get('evidence_refs',[]) for r in refs):return False
 try:
  projected=_project(ref,index.records)
  if fact.get('numeric') is not None:
   if ref.get('projection')=='currency_literal' or ref.get('field')=='amount_minor':projected=Decimal(str(projected))/100
   return fact.get('facet') in {'amount','amount_thb'} and Decimal(str(projected))==Decimal(str(fact['numeric']))
  if ref.get('projection','identity')!='identity' or ref.get('path','') or ref.get('quote') is not None:return False
  if record.get('kind')=='faq' and fact.get('facet')=='owner_policy' and ref.get('field')!='answer':return False
  return all(norm(bilingual(projected).get(lang,''))==norm(fact['value'].get(lang,'')) for lang in ['th','en'])
 except (KeyError,ValueError,TypeError,ArithmeticError):return False
def resolve(index,facts,at=None):
 groups={};inactive=[]
 for f in facts:
  if at is not None and validity_allows(f,at) is False:inactive.append(f['id']);continue
  groups.setdefault(signature(index,f),[]).append(f)
 representatives=[sorted(fs,key=lambda f:f['id'])[0] for fs in groups.values()]
 # Supersession is allowed only with an explicit binding and authority refs in
 # the current record. A later timestamp or owner_confirmed bit alone is not it.
 superseded={};superseded_fact_ids=set();ids={}
 for f in representatives:ids.setdefault(f['record_id'],[]).append(f)
 review=[]
 from ..claim_bindings import release_binding_errors
 chain_validation_ok=True
 try:invalid_chains={e.split(': ',1)[0] for e in release_binding_errors(index.records)}
 except (KeyError,TypeError,ValueError):invalid_chains=set();chain_validation_ok=False;review.append('authority_chain_validation_unavailable')
 for f in representatives:
  record=index.records.get(f['record_id'],{})
  for binding in record.get('claim_bindings',[]):
   if not chain_validation_ok:continue
   if record['record_id']+'#'+binding.get('binding_id','') in invalid_chains:
    review.append('cyclic_or_excessive_authority_chain:'+record['record_id']+'#'+binding['binding_id']);continue
   if not binding.get('authority_refs') or not binding.get('evidence_refs'):continue
   # Recheck mapping and authority locators against bodies pinned in the same
   # SQLite snapshot. Metadata/trust alone cannot authorize supersession.
   from ..claim_bindings import validate_bindings
   try:
    errors=validate_bindings({**record,'claim_bindings':[binding]},index.records,index.source_pairs,publish=False,demo=False)
   except (KeyError,ValueError,TypeError):continue
   if errors or binding.get('value_ref',{}).get('record_id')!=f['record_id']:continue
   if not binding_covers_fact(index,binding,f):
    review.append('authority_mapping_not_for_projected_fact:'+f['id']);continue
   from ..registry import aware
   app=binding.get('applicability',{})
   if at is None or app.get('status')!='known' or binding.get('actor_scope',{}).get('status')!='known' or any(binding.get(k)!='known' for k in ['conditions_status','exceptions_status']):continue
   if app.get('effective_from') and at<aware(app['effective_from']) or app.get('effective_until') and at>=aware(app['effective_until']):continue
   authorities=[index.sources.get(ref.get('source_id'),{}) for ref in binding['authority_refs']]
   if not authorities or any(src.get('trust') not in {'owner_confirmed','internal_verified'} or record.get('kind') not in src.get('authority_for',[]) for src in authorities):continue
   for ref in binding.get('supersedes_refs',[]):
    rid=ref.split('#',1)[0]
    prior=index.records.get(rid,{})
    old_binding=next((b for b in prior.get('claim_bindings',[]) if ref==rid+'#'+b['binding_id']),None)
    old_app=old_binding.get('applicability',{}) if old_binding else {}
    same_scope=bool(old_binding and old_app.get('status')=='known' and all(binding.get(k)==old_binding.get(k) for k in ['subject_ref','predicate','unit','actor_scope','conditions_status','condition_refs','exceptions_status','exception_refs']) and sorted(app.get('service_ids') or [])==sorted(old_app.get('service_ids') or []) and all(app.get(k)==old_app.get(k) for k in ['duration_minutes','platform']))
    if rid in ids and same_scope:
     for prior_fact in ids[rid]:
      if prior_fact['category']!=f['category'] or prior_fact['facet']!=f['facet']:continue
      if not binding_covers_fact(index,old_binding,prior_fact):
       review.append('superseded_mapping_not_for_projected_fact:'+prior_fact['id']);continue
      superseded_fact_ids.add(prior_fact['id'])
      receipt=superseded.setdefault(rid,{'by':f['record_id'],'authority_refs':binding['authority_refs'],'scope_basis':'explicit_claim_binding_for_actual_projected_field','fact_ids':[]})
      if prior_fact['id'] not in receipt['fact_ids']:receipt['fact_ids'].append(prior_fact['id'])
 chosen=[f for f in representatives if f['id'] not in superseded_fact_ids]
 conflicts=[]
 if len(chosen)>1:
  # Different wording/unknown scope does not prove logical contradiction.
  # Reuse only the source-attested, typed subject/predicate/unit/actor/time
  # conflict contract; prose variants require owner/source review.
  if at is not None:
   from ..claim_bindings import conflicts as mapped_conflicts
   try:
    conflicts=mapped_conflicts([f['record_id'] for f in chosen],{'active':'request-pinned','epoch':0,'release':{'records':index.records},'withdrawn':[]},at)
   except (KeyError,ValueError,TypeError) as exc:review.append('typed_conflict_proof_unavailable:'+type(exc).__name__)
  if not conflicts:review.append('prose_or_applicability_variants_need_source_review')
 return {'status':'equivalent' if len(chosen)==1 else 'conflict' if conflicts else 'source_variants' if chosen else 'not_current','facts':chosen,
  'duplicates':[[f['id'] for f in fs] for fs in groups.values() if len(fs)>1],'superseded':superseded,'inactive':inactive,
  'confirmed_conflicts':conflicts,'review_required':review,
  'basis':'bilingual_content_scope_conditions_validity_and_explicit_authority'}
