"""Bilingual duplicate identity and evidence-backed scoped supersession only."""
import json
from .projection import value
from .scope import norm,validity_allows
def signature(index,f):
 r=index.records.get(f['record_id'],{})
 scope={k:value(r,k) for k in ['topic','scope_note','conditions_all','exceptions','preconditions','service_id','audience_id','competition_id'] if value(r,k) is not None}
 return json.dumps({'th':norm(f['value'].get('th','')),'en':norm(f['value'].get('en','')),'scope':scope,'validity':r.get('validity')},ensure_ascii=False,sort_keys=True)
def resolve(index,facts,at=None):
 groups={};inactive=[]
 for f in facts:
  if at is not None and validity_allows(f,at) is False:inactive.append(f['id']);continue
  groups.setdefault(signature(index,f),[]).append(f)
 representatives=[sorted(fs,key=lambda f:f['id'])[0] for fs in groups.values()]
 # Supersession is allowed only with an explicit binding and authority refs in
 # the current record. A later timestamp or owner_confirmed bit alone is not it.
 superseded={};ids={f['record_id']:f for f in representatives}
 for f in representatives:
  record=index.records.get(f['record_id'],{})
  for binding in record.get('claim_bindings',[]):
   if not binding.get('authority_refs') or not binding.get('evidence_refs'):continue
   # Recheck mapping and authority locators against bodies pinned in the same
   # SQLite snapshot. Metadata/trust alone cannot authorize supersession.
   from ..claim_bindings import validate_bindings
   try:
    errors=validate_bindings({**record,'claim_bindings':[binding]},index.records,index.source_pairs,publish=False,demo=False)
   except (KeyError,ValueError,TypeError):continue
   if errors or binding.get('value_ref',{}).get('record_id')!=f['record_id']:continue
   from ..registry import aware
   app=binding.get('applicability',{})
   if at is None or app.get('status')!='known':continue
   if app.get('effective_from') and at<aware(app['effective_from']) or app.get('effective_until') and at>=aware(app['effective_until']):continue
   authorities=[index.sources.get(ref.get('source_id'),{}) for ref in binding['authority_refs']]
   if not authorities or any(src.get('trust') not in {'owner_confirmed','internal_verified'} or record.get('kind') not in src.get('authority_for',[]) for src in authorities):continue
   for ref in binding.get('supersedes_refs',[]):
    rid=ref.split('#',1)[0]
    prior=index.records.get(rid,{})
    old_binding=next((b for b in prior.get('claim_bindings',[]) if ref==rid+'#'+b['binding_id']),None)
    same_scope=bool(old_binding and all(binding.get(k)==old_binding.get(k) for k in ['subject_ref','predicate','unit','actor_scope','conditions_status','condition_refs','exceptions_status','exception_refs']))
    if rid in ids and same_scope and ids[rid]['category']==f['category'] and ids[rid]['facet']==f['facet']:
     superseded[rid]={'by':f['record_id'],'authority_refs':binding['authority_refs'],'scope_basis':'explicit_claim_binding'}
 chosen=[f for f in representatives if f['record_id'] not in superseded]
 return {'status':'equivalent' if len(chosen)==1 else 'conflict' if chosen else 'not_current','facts':chosen,
  'duplicates':[[f['id'] for f in fs] for fs in groups.values() if len(fs)>1],'superseded':superseded,'inactive':inactive,
  'basis':'bilingual_content_scope_conditions_validity_and_explicit_authority'}
