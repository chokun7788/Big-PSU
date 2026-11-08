"""Explicit package/rule comparison over source-bound options, never top-K."""
import re
from .scope import contains,validity_allows
from .projection import title,value
from .readers import confirmed,blocked

def names(index,kind,question):
 from ..answer import named
 directory={rid:[*title(r).values(),*sum(r.get('aliases',{}).values(),[])] for rid,r in index.records.items() if r['kind']==kind}
 return named(question,directory,allow_fuzzy=False)[0]

def rule_options(index,question):
 from .scope import rule_edition_events,norm
 candidates=names(index,'competition',question)
 facts=[f for f in index.bycat['C13'] if f.get('event_id') in candidates]
 editions=rule_edition_events(index,question,facts)
 if editions is not None:candidates=[rid for rid in candidates if rid in editions]
 elif len({tuple(norm(s) for s in title(index.records[rid]).values()) for rid in candidates})!=len(candidates):return []
 return candidates

PACKAGE_SCOPE_FIELDS=('zone','audience','duration_minutes','terms','equipment_included','room_seats')
PACKAGE_LABELS={'zone':('โซนในแพ็กเกจ','package zones'),'audience':('กลุ่มหน่วยงานของแพ็กเกจ','package organization group'),'duration_minutes':('ระยะเวลาเป็นนาที','duration in minutes'),'terms':('เงื่อนไขแพ็กเกจ','package terms'),'equipment_included':('อุปกรณ์ที่รวม','included equipment'),'room_seats':('ที่นั่งห้อง','room seats'),'amount_thb':('ราคาแพ็กเกจ','package price')}

def package_options(index,question):
 options=names(index,'rental_package',question)
 if len(options)<2:
  from .financial import rental_pool
  options=list(dict.fromkeys(f['record_id'] for f in rental_pool(index,question)))
 return options

def package_scope(index,question,facet,at):
 options=package_options(index,question);fields=list(dict.fromkeys(([facet] if facet else ['amount_thb'])+list(PACKAGE_SCOPE_FIELDS)))
 facts=[f for rid in options for f in index.byrecord[rid] if f['category']=='C07' and f['facet'] in fields and validity_allows(f,at) is not False]
 missing=[{'record_id':rid,'facet':field} for rid in options for field in fields if not any(f['record_id']==rid and f['facet']==field for f in facts)]
 return {'options':options,'fields':fields,'facts':facts,'missing':missing}

def execute(index,category,question,meaning,at):
 if meaning is None or meaning.operation!='compare' or category not in {'C07','C13'}:return None
 if meaning.ambiguous:return blocked(category,'comparison_scope_ambiguous','missing_input')
 if category=='C07':
  scope=package_scope(index,question,meaning.facet,at);options=scope['options']
  if len(options)<2:return blocked(category,'comparison_requires_named_package_options','missing_input')
  chosen=scope['facts']
  missing=[rid for rid in options if not any(f['record_id']==rid for f in chosen)]
 else:
  options=rule_options(index,question)
  if len(options)<2:return blocked(category,'comparison_requires_explicit_event_editions','missing_input')
  from .readers import rules_reader
  neutral=question
  for rid in options:
   r=index.records[rid]
   for s in sorted([*title(r).values(),*sum(r.get('aliases',{}).values(),[])],key=len,reverse=True):
    if s:neutral=re.sub(re.escape(s),' ',neutral,flags=re.I)
   release=str(value(r,'rulebook_release') or '')
   if release:neutral=re.sub(r'(?<![a-z0-9])'+re.escape(release)+r'(?![a-z0-9])',' ',neutral,flags=re.I)
  chosen=[];missing=[]
  for rid in options:
   query=neutral+' '+next(s for s in title(index.records[rid]).values() if s)+' '+str(value(index.records[rid],'rulebook_release') or '')
   plan=rules_reader(index,query,at)
   fs=[index.byid[f] for f in plan.ids if index.byid[f].get('event_id')==rid]
   if plan.ambiguous or not fs:missing.append(rid)
   else:chosen+=fs
 if not chosen:return blocked(category,'comparison_source_fields_missing')
 result=confirmed(category,chosen,'explicit_source_option_comparison',operator='compare',comparison_option_ids=options,comparison_missing_option_ids=missing,complete_set=not missing)
 if category=='C07':
  result.metadata.update(package_comparison_fields=scope['fields'],package_comparison_missing_fields=scope['missing'],package_scope_basis='current_named_package_and_source_conditions')
  if scope['missing']:result.status='partial';result.metadata['package_conditions_unconfirmed']=True
 if missing:result.status='partial'
 return result
