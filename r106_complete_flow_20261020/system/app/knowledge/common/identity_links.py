"""Reviewed migration read links; no data merge or fuzzy identity inference."""
import hashlib,json
from pathlib import Path
from .query_contract import resolve_fields
def digest(record):
 return hashlib.sha256(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def resolve(question,ids,records,names):
 path=Path(__file__).with_suffix('.json');audit=[]
 if not path.is_file():return ids,names,audit
 requested=resolve_fields(question,{'game'})[0]
 if not requested:return ids,names,audit
 for link in json.loads(path.read_text('utf8')).get('links',[]):
  source=link['source_record_id'];target=link['target_record_id']
  if source not in ids:continue
  reason=None
  if not set(requested)<=set(link['fields']):reason='field_outside_reviewed_scope'
  elif source not in records or target not in records:reason='record_missing_or_withdrawn'
  elif digest(records[source])!=link['source_record_sha256'] or digest(records[target])!=link['target_record_sha256']:reason='record_revision_changed'
  audit.append({'source_record_id':source,'target_record_id':target,'requested_fields':requested,'applied':reason is None,'reason':reason or 'reviewed_immutable_migration_link','owner_identity_approval':False})
  if reason:continue
  ids=list(dict.fromkeys(target if rid==source else rid for rid in ids))
  names={**names,target:list(dict.fromkeys(names.get(target,[])+names.get(source,[])))}
 return ids,names,audit
