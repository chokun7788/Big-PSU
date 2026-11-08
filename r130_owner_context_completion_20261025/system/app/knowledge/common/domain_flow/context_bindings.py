"""Source-quoted shared prefixes, typed anaphora and explicit slot ownership.

This compiler produces graph edges, never venue answers. A prefix is shared
only when it is linguistically leading and the receiving capability accepts it.
"""
import copy,re
from .scope import contains,norm

APPLIES={
 'audience':{'C06','C07','C08','C09','C10'},'persons':{'C04','C06','C07'},
 'duration':{'C06','C07'},'sessions':{'C06','C07'},'date':{'C06','C07','C08','C11','C12','C13','C14'},
 'time':{'C08','C11','C12'},'platform':{'C03','C04','C05','C06','C07','C08','C12'},
 'service':{'C03','C04','C06','C07','C08','C12'},'event':{'C13','C14'},
 'negation':{'C06','C07','C08','C09','C10'},'condition':{'C08','C09','C10','C13'},
}
ASK=re.compile(r'ราคา|ค่าบริการ|เสียกี่|อยาก(?:ทราบ|รู้)|ต้องการ(?:ทราบ|รู้)|จอง|เปิดไหม|ว่างไหม|มีเกม|เล่นเกม|\b(?:what|which|how|compare|price|cost|can|is|are|list|show)\b',re.I)
ANAPHOR=re.compile(r'\b(?:it|its|same service|same game|that game|that machine|those)\b|เครื่องเดิม|เกมเดิม|เครื่องนั้น|เกมนั้น|โซนเดิม|บริการเดิม|แล้วมัน|มันมี|มันเล่น|อันเดิม|อันนั้น',re.I)

def locate(q,quote):
 p=q.find(quote)
 return {'start':p,'end':p+len(quote),'text':quote} if p>=0 and quote else None

def compile_shared(question,index,proposal):
 result=copy.deepcopy(proposal)
 if not result.accepted or not result.tasks:return result
 from .context_guard import PATTERNS,named_targets
 positions=[locate(question,t.quote) for t in result.tasks]
 if any(p is None for p in positions):return result
 first=result.tasks[0];start=positions[0]['start'];ask=ASK.search(first.quote)
 stop=start+ask.start() if ask else start
 prefix=question[:stop]
 # A leading source-named group/date is a common request frame. Never treat
 # an arbitrary earlier task's trailing duration as a shared prefix.
 marked=bool(re.match(r'^\s*(?:สำหรับ|ในกรณี|วันนี้|พรุ่งนี้|วันที่|for\b|as\b|on\b|today\b|tomorrow\b)',prefix,re.I))
 from .financial import audience_mentions
 positive,negative=audience_mentions(index,prefix)
 prefix_ok=bool(prefix.strip() and (marked or positive or negative))
 shared=[];superseded=[];audits=[]
 candidates=[]
 if prefix_ok:
  for kind,pattern in PATTERNS:
   candidates.extend({'slot':kind,'quote':m[0],'source_record_id':''} for m in re.finditer(pattern,prefix,re.I))
  for rid in positive|negative:
   r=index.records[rid]
   from .projection import title
   labels=[*title(r).values(),*sum(r.get('aliases',{}).values(),[])]
   matches=[(len(s),s) for s in labels if contains(prefix,s)]
   if matches:
    label=max(matches)[1];m=re.search(re.escape(label),prefix,re.I)
    if m:candidates.append({'slot':'negation' if rid in negative else 'audience','quote':m[0],'source_record_id':rid})
 for i,task in enumerate(result.tasks):
  tid=f't{i+1}';local=task.quote;local_span=positions[i]
  for c in candidates:
   kind=c['slot'];source=locate(question,c['quote'])
   if task.category not in APPLIES.get(kind,set()) or source is None:continue
   if local_span['start']<=source['start'] and source['end']<=local_span['end']:continue
   owned=[x for x in task.constraints if x['slot']==kind and x['quote'] in local]
   if kind in {'audience','negation'}:
    lp,ln=audience_mentions(index,local)
    if lp or ln:
     superseded.append({'task_id':tid,'slot':kind,'source_span':source,'reason':'local_audience_override'});continue
   elif owned:
    superseded.append({'task_id':tid,'slot':kind,'source_span':source,'reason':'local_slot_override'});continue
   origin='t1' if positions[0]['start']<=source['start'] and source['end']<=positions[0]['end'] else 'request'
   edge={'id':f'prefix_{len(shared)+1}','basis':'shared_prefix','source_task_id':origin,'target_task_id':tid,'source_span':source,'slot_kind':kind,'entity_refs':([c['source_record_id']] if c['source_record_id'] else []),'execution_dependency':False,'validated':True}
   shared.append(edge)
   if not any(x['slot']==kind and x['quote']==c['quote'] for x in task.constraints):task.constraints.append(copy.deepcopy(c))
  if ANAPHOR.search(local) and not named_targets(index,local):
   names=[]
   for j in range(i):
    for name in named_targets(index,result.tasks[j].quote):
     if task.category and index.bind(task.category,name):names.append((j,name))
   unique={norm(name) for _,name in names}
   if len(unique)==1 and names:
    j,name=names[-1];task.target=name
    if any(a.get('action')=='unresolved_referent' and a.get('task_quote')==local for a in result.event.get('context_scope_review',[])):
     task.ambiguous=False
    shared.append({'id':f'anaphor_{i+1}','basis':'explicit_anaphor','source_task_id':f't{j+1}','target_task_id':tid,'source_span':locate(question,name),'slot_kind':'target','entity_refs':sorted({f['record_id'] for f in index.bind(task.category,name)}),'execution_dependency':False,'validated':True})
   elif len(unique)>1:
    task.target='';task.ambiguous=True;audits.append({'task_id':tid,'reason':'multiple_typed_antecedents','candidates':sorted(unique)})
 result.event['shared_bindings']=shared
 result.event['superseded_slots']=superseded
 result.event['binding_ambiguities']=audits
 result.event['binding_contract']='r129-shared-context-v2'
 result.event['model_edges_review']=[{'proposed':edge,'compiler_correspondence':any(b['target_task_id']==edge['target_task_id'] and b['source_span']['text']==edge['quote'] and b['slot_kind']==edge['slot'] for b in shared),'model_edge_is_evidence':False} for edge in result.event.get('proposed_shared_bindings',[])]
 return result
