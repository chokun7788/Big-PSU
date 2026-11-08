"""Explicit package/rule comparison over source-bound options, never top-K."""
import re
from .scope import contains,validity_allows
from .projection import title
from .readers import confirmed,blocked

def names(index,kind,question):
 from ..answer import named
 directory={rid:[*title(r).values(),*sum(r.get('aliases',{}).values(),[])] for rid,r in index.records.items() if r['kind']==kind}
 return named(question,directory,allow_fuzzy=False)[0]

def execute(index,category,question,meaning,at):
 if meaning is None or meaning.operation!='compare' or category not in {'C07','C13'}:return None
 if meaning.ambiguous:return blocked(category,'comparison_scope_ambiguous','missing_input')
 if category=='C07':
  options=names(index,'rental_package',question)
  if len(options)<2:
   from .financial import rental_pool
   scoped=rental_pool(index,question)
   options=list(dict.fromkeys(f['record_id'] for f in scoped))
  if len(options)<2:return blocked(category,'comparison_requires_named_package_options','missing_input')
  fields={meaning.facet} if meaning.facet else {'amount_thb','duration_minutes','equipment_included','room_seats','terms'}
  chosen=[f for rid in options for f in index.byrecord[rid] if f['facet'] in fields and validity_allows(f,at) is not False]
  missing=[rid for rid in options if not any(f['record_id']==rid for f in chosen)]
 else:
  options=names(index,'competition',question)
  if len(options)<2:return blocked(category,'comparison_requires_explicit_event_editions','missing_input')
  from .readers import rules_reader
  neutral=question
  for rid in options:
   r=index.records[rid]
   for s in sorted([*title(r).values(),*sum(r.get('aliases',{}).values(),[])],key=len,reverse=True):
    if s:neutral=re.sub(re.escape(s),' ',neutral,flags=re.I)
  chosen=[];missing=[]
  for rid in options:
   query=neutral+' '+next(s for s in title(index.records[rid]).values() if s)
   plan=rules_reader(index,query,at)
   fs=[index.byid[f] for f in plan.ids if index.byid[f].get('event_id')==rid]
   if plan.ambiguous or not fs:missing.append(rid)
   else:chosen+=fs
 if not chosen:return blocked(category,'comparison_source_fields_missing')
 result=confirmed(category,chosen,'explicit_source_option_comparison',operator='compare',comparison_option_ids=options,comparison_missing_option_ids=missing,complete_set=not missing)
 if missing:result.status='partial'
 return result
