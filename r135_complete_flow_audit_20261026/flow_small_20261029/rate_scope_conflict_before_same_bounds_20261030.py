"""Conservative source-only competing rate check; no semantic or authority claim."""
from .projection import value

def overlapping(index, record):
 service=index.records.get(value(record,'service_id'),{});platform=value(service,'platform');audience=value(record,'audience_id');duration=value(record,'duration_minutes');lo=value(record,'persons_min');hi=value(record,'persons_max')
 if not platform or not audience or not isinstance(lo,int) or not isinstance(hi,int):return False
 for other in index.records.values():
  if other.get('kind')!='rate' or other.get('record_id')==record.get('record_id') or other.get('lifecycle')=='withdrawn':continue
  svc=index.records.get(value(other,'service_id'),{});a=value(other,'persons_min');b=value(other,'persons_max')
  if value(svc,'platform')!=platform or value(other,'audience_id')!=audience or value(other,'duration_minutes')!=duration:continue
  if not isinstance(a,int) or not isinstance(b,int) or (a,b)==(lo,hi):continue
  if max(lo,a)<=min(hi,b):return True
 return False
