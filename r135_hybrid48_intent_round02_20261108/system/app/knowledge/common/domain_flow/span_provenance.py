"""Monotonic raw/derived alignment with explicit history/normalizer receipts."""
import difflib,re

def alignment(raw,execution,derivation=None,slot_provenance=None):
 segments=[]
 for block in difflib.SequenceMatcher(None,raw,execution,autojunk=False).get_matching_blocks():
  if block.size:
   segments.append({'execution_start':block.b,'execution_end':block.b+block.size,'origin':'current_user','raw_start':block.a,'raw_end':block.a+block.size,'raw_text':raw[block.a:block.a+block.size],'transform':'casefold' if raw[block.a:block.a+block.size]!=execution[block.b:block.b+block.size] else 'identity'})
 # Repeated exact source phrases are still traceable even if not in the
 # monotonic diff. Every alternative range is recorded; none is guessed.
 return {'version':'r129-span-map-v2','raw_question':raw,'execution_question':execution,'segments':segments,'derivation':derivation,'trusted_slot_provenance':slot_provenance or {},'business_facts_inherited':False}

def resolve_span(mapping,start,end):
 q=mapping['execution_question'];raw=mapping['raw_question'];text=q[start:end]
 if not 0<=start<end<=len(q):return {'status':'invalid_execution_span','sources':[]}
 if raw==q:return {'status':'exact_current_raw','sources':[{'origin':'current_user','start':start,'end':end,'text':text}]}
 exact=[{'origin':'current_user','start':m.start(),'end':m.end(),'text':m[0]} for m in re.finditer(re.escape(text),raw,re.I)]
 if exact:return {'status':'current_raw_quote' if len(exact)==1 else 'multiple_raw_occurrences','sources':exact}
 selected=[s for s in mapping['segments'] if s['execution_start']<end and start<s['execution_end']]
 inherited=[]
 for slot,ref in mapping['trusted_slot_provenance'].items():
  refs=ref if isinstance(ref,list) else [ref]
  for r in refs:
   if not isinstance(r,dict):continue
   value=str(r.get('execution_text') or r.get('quote') or '')
   if value and (value.casefold() in text.casefold() or text.casefold() in value.casefold()):inherited.append({'slot':slot,**r})
 transforms=mapping.get('derivation') or []
 verified=bool(inherited or transforms)
 return {'status':'derived_with_provenance' if verified else 'unresolved_derivation','sources':selected+inherited,'derivation':transforms,'exact_current_raw_quote':False,'transformation_requires_receipt':True,'semantic_transformation_verified':False}
