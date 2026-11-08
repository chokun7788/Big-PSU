"""Protect source-bound entity labels without hiding ordinary quantities."""
import re
from .scope import norm
from .projection import title

KINDS={'game','equipment_model','resource','service','zone','rental_package','competition'}
def spans(index,question,target=None):
 hits=[]
 # A bare unit phrase in a price question is not automatically a game merely
 # because an owner has also used that phrase as a title.
 field_context=bool(re.search(r'แนวเกม|คำอธิบาย|วิธีเล่น|สเปก|\b(?:genre|summary|overview|specs?|specifications?|how to play|controls?)\b',question,re.I))
 if target is None and not field_context and not re.search(r'เกม|เครื่อง|อุปกรณ์|ชื่อ|["“\']|\b(?:game|device|machine|called|named)\b',question,re.I):return []
 query=norm(question)
 for rid,record in index.records.items():
  if record.get('kind') not in KINDS:continue
  labels=[*title(record).values(),*sum(record.get('aliases',{}).values(),[])]
  for label in labels:
   if not isinstance(label,str) or len(label.strip())<2:continue
   if norm(label) not in query:continue
   if target is not None and norm(label)!=norm(target):continue
   pattern=r'\s+'.join(re.escape(part) for part in label.split())
   if label[0].isascii() and label[0].isalnum():pattern=r'(?<![a-z0-9])'+pattern
   if label[-1].isascii() and label[-1].isalnum():pattern+=r'(?![a-z0-9])'
   for match in re.finditer(pattern,question,re.I):
    before=question[max(0,match.start()-35):match.start()]
    after=question[match.end():match.end()+35]
    explicit=bool(re.search(r'(?:เกม|เครื่อง|อุปกรณ์|ชื่อ|\b(?:game|device|machine|called|named))\s*["“\']?\s*$',before,re.I) or before.endswith(('"','“',"'")))
    field_target=field_context and bool(re.search(r'(?:genre|summary|overview|specs?|specifications?|controls?|how to play)(?:\s+(?:is|of|for|does|are|about))*\s*$',before,re.I) or re.match(r'^\s*(?:is\s+)?(?:what\s+)?(?:genre|summary|overview|specs?|specifications?)\b',after,re.I) or re.search(r'แนวเกม|คำอธิบาย|สเปก',before))
    if target is not None and re.search(r'(?:\b(?:price|cost|fee)(?:\s+(?:is|of|for|the))*|ราคา|ค่าบริการ)\s*$',before,re.I):field_target=True
    if target is not None or field_target or explicit:hits.append({'start':match.start(),'end':match.end(),'text':match[0],'record_id':rid,'basis':'source_bound_target' if target is not None else 'source_name_in_entity_field_context','marked_entity_position':bool(field_target or explicit)})
 if target is not None and any(h['marked_entity_position'] for h in hits):hits=[h for h in hits if h['marked_entity_position']]
 return [h for h in hits if not any(o['start']<=h['start'] and h['end']<=o['end'] and o['end']-o['start']>h['end']-h['start'] for o in hits)]

def masked(index,question,target=None):
 chars=list(question)
 for hit in spans(index,question,target):chars[hit['start']:hit['end']]=' '* (hit['end']-hit['start'])
 return ''.join(chars)

def outside(index,question,transform,target=None):
 ranges=sorted({(h['start'],h['end']) for h in spans(index,question,target)});out=[];cursor=0
 for start,end in ranges:
  if start<cursor:continue
  out.append(transform(question[cursor:start]));out.append(question[start:end]);cursor=end
 out.append(transform(question[cursor:]));return ''.join(out)

def quantity_in_name(index,question,quote,target=None):
 occurrences=list(re.finditer(re.escape(quote),question));protected=spans(index,question,target)
 return bool(occurrences) and all(any(h['start']<=m.start() and m.end()<=h['end'] for h in protected) for m in occurrences)

def range_in_name(index,question,start,end,target=None):
 return any(h['start']<=start and end<=h['end'] for h in spans(index,question,target))
