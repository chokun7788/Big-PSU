"""Bounded rejection of an explicit foreign location for center-bound policies.

Uses source-attested related_ids. Location patterns detect possible mismatches;
they do not establish general semantic entailment or resolve unnamed entities.
"""
import hashlib,json,re
from .projection import value
from ..registry import pointer

def norm(s):return re.sub(r'[\W_]+','',str(s).casefold())

NOTICE={'th':'กฎที่พบเป็นของศูนย์นี้ ยังใช้ยืนยันกฎของสถานที่ที่คุณระบุไม่ได้ กรุณายืนยันว่าหมายถึง PSU Esports Studio – Phuket หรือสถานที่อื่นครับ',
        'en':'The recorded policy belongs to this studio and does not establish the policy of the place you named. Do you mean PSU Esports Studio – Phuket or another place?'}

def check(index,question,record_ids,*,composed=False):
 records=[index.records[rid] for rid in record_ids if rid in index.records and index.records[rid].get('kind')=='faq']
 def declared(r):
  for ref in r.get('fields',{}).get('answer',{}).get('evidence_refs',[]):
   pair=index.source_pairs.get(ref.get('source_id'))
   if not pair:continue
   try:
    ids=json.loads(pair[1]).get('mapped_records',{}).get(r['record_id'],{}).get('related_ids',[])
    if ids:return True
   except (ValueError,TypeError):pass
  return False
 scoped=[r for r in records if declared(r) or value(r,'related_ids') and any(index.records.get(k,{}).get('kind')=='center' for k in value(r,'related_ids'))]
 if not scoped:return {'applicable':False,'errors':[]}
 if composed:
  from .routing import split_needs
  if len(split_needs(question))>1:return {'applicable':True,'errors':[],'deferred_to_leaf_requests':True}
 errors=[];centers=set()
 for r in scoped:
  field=r['fields']['related_ids'];refs=field.get('evidence_refs',[])
  try:
   if not refs:raise ValueError('missing relationship evidence')
   for ref in refs:
    src,body=index.source_pairs[ref['source_id']]
    if hashlib.sha256(body.encode()).hexdigest()!=src['sha256'] or pointer(json.loads(body),ref['locator'])!=field['value']:raise ValueError('unproven relationship')
   centers.update(k for k in field['value'] if index.records.get(k,{}).get('kind')=='center')
  except (ValueError,TypeError,KeyError,IndexError):errors.append('policy_subject_relationship_unproven')
 if not centers:errors.append('policy_subject_center_unresolved')
 labels={'studio','the studio','center','the center','centre','the centre','ศูนย์','สตูดิโอ'}
 for rid in centers:
  r=index.records[rid]
  labels.update(sum(r.get('aliases',{}).values(),[]))
  for key in ('name','title'):
   v=value(r,key)
   if isinstance(v,dict):labels.update(s for s in v.values() if s)
 allowed={norm(s) for s in labels}
 targets=[]
 # Keep quoted/named games and devices out of the location detector.
 from .named_spans import masked
 text=masked(index,question)
 for match in re.finditer(r'\b(?:[A-Z][\w\'-]*\s+){1,4}(?:Hotel|School|Company)\b',text):targets.append(match[0])
 for match in re.finditer(r'\bat\s+(?:the\s+)?([^?!.;,\n]+)',text,re.I):
  target=re.split(r'\b(?:and|but|can|do|does|is|are|book|reserve|pay)\b',match[1],maxsplit=1,flags=re.I)[0].strip()
  if not re.match(r'^(?:most|least|once|a time|one time|the same time|\d)',target,re.I):targets.append(target)
 for match in re.finditer(r'(?:โรงแรม|โรงเรียน|บริษัท|ร้านค้า|ศูนย์|สตูดิโอ)[^\s,?;\n]*',text):
  target=re.split(r'จอง|ราคา|ต้อง|เปิด|ปิด|ได้|มี|กี่|และ|แล้ว|คือ',match[0],maxsplit=1)[0].strip()
  targets.append(target)
 # Source labels in a negative clause cannot establish the requested subject.
 for label in sorted(labels,key=len,reverse=True):
  if len(norm(label))<4:continue
  if re.search(r'(?:ไม่ใช่|ไม่ได้หมายถึง|\bnot(?:\s+the)?)\s*'+re.escape(label),question,re.I):errors.append('policy_requested_subject_negated')
 rejected=[t for t in targets if norm(t) not in allowed]
 if rejected:errors.append('policy_requested_subject_not_source_center')
 return {'applicable':True,'errors':sorted(set(errors)),'source_center_ids':sorted(centers),'explicit_location_spans':targets,
         'unresolved_locations':rejected,'scope':'bounded explicit-location rejection; not full natural-language target resolution'}
