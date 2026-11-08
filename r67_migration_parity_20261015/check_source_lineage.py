"""Check the original importer lineage and current source bytes independently."""
import collections,hashlib,json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import pointer,value,validate
original=B.parent/'r63_legacy_migration_20261013/round7'
store=CommonStore(B/'common.sqlite')
with store.connect() as c:rs=store.heads(c);sources=store.sources(c)
rows=[]
for item in json.loads((original/'FIELD_LINEAGE.json').read_text('utf8')):
 p=B/'source_snapshot'/item['source_path'];r=rs.get(item['record_id']);v=value(r,item['field']) if r else None
 row={k:item[k] for k in ('record_id','field','source_path','locator')}
 if not p.is_file():row['source_state']='missing_source_snapshot'
 else:
  row['source_sha_matches']=hashlib.sha256(p.read_bytes()).hexdigest()==item['source_sha256']
  try:
   text=p.read_text('utf-8-sig');document=[json.loads(line) for line in text.splitlines() if line.strip()] if p.suffix=='.jsonl' else json.loads(text)
   row['source_value_matches']=pointer(document,item['locator'])==item['source_value'];row['source_state']='checked'
  except Exception as e:row['source_state']='unreadable_json_pointer';row['exception']=repr(e)
 old=item['mapped_value']
 if v==old:row['target_state']='exact'
 elif isinstance(old,dict) and isinstance(v,dict) and set(old)=={'th','en'}:
  row['target_state']='localized_extended' if all(not old[k] or old[k]==v.get(k) for k in old) else 'changed_localized_review'
 elif isinstance(old,list) and isinstance(v,list) and all(item in v for item in old):row['target_state']='structured_extended'
 else:row['target_state']='changed_or_missing_review'
 rows.append(row)
err={rid:e for rid,r in rs.items() if (e:=validate(r,rs,sources))}
result={'mapped_fields_checked':len(rows),'target_counts':dict(collections.Counter(x['target_state'] for x in rows)),'source_counts':dict(collections.Counter(x['source_state'] for x in rows)),'changed_source_hashes':sum(not x.get('source_sha_matches',False) for x in rows),'changed_source_values':sum(not x.get('source_value_matches',False) for x in rows),'schema_errors':err,'rows':rows}
(B/('ORIGINAL_LINEAGE_AUDIT_'+(sys.argv[1] if len(sys.argv)>1 else 'initial')+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},ensure_ascii=False))
