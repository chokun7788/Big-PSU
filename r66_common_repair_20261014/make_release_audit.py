"""Read-only release readiness and preservation audit of the R66 candidate."""
import sys,json,collections,sqlite3,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import validate,value
original=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\knowledge\migration_r63_20261013\approved.sqlite')
with sqlite3.connect(original.as_uri()+'?mode=ro',uri=True) as c:
 c.row_factory=sqlite3.Row;old=CommonStore.heads(c);oldmeta=dict(c.execute('SELECT * FROM cc_meta'));oldsources=CommonStore.sources(c)
 oldrevisions={(r['record_id'],r['version']):dict(r) for r in c.execute('SELECT * FROM cc_revisions')}
store=CommonStore(B/'common.sqlite')
with store.connect() as c:
 new=store.heads(c);sources=store.sources(c);meta=dict(c.execute('SELECT * FROM cc_meta'))
 newrevisions={(r['record_id'],r['version']):dict(r) for r in c.execute('SELECT * FROM cc_revisions')}
errors=[];checks=collections.Counter();gates=[];draft_errors=[]
for k,row in oldrevisions.items():
 checks['original_revisions_checked']+=1
 if newrevisions.get(k)!=row:errors.append(str(k)+': original revision changed or missing')
intentional=[];allowed={}
repair=B/'DAMAGE_TRANSLATION_REPAIR.json'
if repair.exists():
 d=json.loads(repair.read_text(encoding='utf-8'));rid=d['record_id'];before=value(old[rid],'answer');after=value(new[rid],'answer')
 # An explicit, source-bound correction is a new revision, not an exception
 # permitting deletion or mutation of any original revision/source.
 assert before['en']==d['old_en'] and after['en']==d['new_en'] and before['th']==after['th']
 assert new[rid]['revision']>old[rid]['revision']
 refs=new[rid]['fields']['answer']['evidence_refs'];assert len(refs)==1
 src,raw=sources[refs[0]['source_id']];payload=json.loads(raw)
 assert src['path']=='translation://r66-damage-fines/'+rid and hashlib.sha256(raw.encode()).hexdigest()==src['sha256']
 assert payload['mapped_fields']['answer']==after and payload['owner_reviewed'] is False
 allowed[rid+'/answer/en']=(d['old_en'],d['new_en'])
note_repair=B/'CONTROL_NOTE_TRANSLATION_REPAIRS.json'
if note_repair.exists():
 d=json.loads(note_repair.read_text(encoding='utf-8'));assert d['records']==36 and d['notes']==390 and not d['owner_approved'] and not d['published']
 for item in d['changes']:
  rid=item['record_id'];before=value(old[rid],'limitations');after=value(new[rid],'limitations')
  assert before['en']==item['old_en'] and after['en']==item['new_en'] and before['th']==after['th']
  assert new[rid]['revision']>old[rid]['revision']
  refs=new[rid]['fields']['limitations']['evidence_refs'];assert refs==[{'source_id':item['source_id'],'locator':'/mapped_fields/limitations'}]
  src,raw=sources[item['source_id']];payload=json.loads(raw)
  assert src['path']=='translation://r66-control-notes/'+rid and hashlib.sha256(raw.encode()).hexdigest()==src['sha256']==item['source_sha256']
  assert payload['mapped_fields']['limitations']==after and payload['owner_reviewed'] is False
  proposal=B/'CONTROL_NOTE_REVIEWED'/(rid+'.json');assert hashlib.sha256(proposal.read_bytes()).hexdigest()==item['proposal_sha256']
  allowed[rid+'/limitations/en']=(item['old_en'],item['new_en'])
def preserve(before,after,path):
 if before is None:return
 if isinstance(before,dict):
  for key,v in before.items():
   if key=='en' and v is None:continue
   if not isinstance(after,dict) or key not in after:errors.append(path+'/'+key+': missing')
   else:preserve(v,after[key],path+'/'+key)
 elif isinstance(before,list):
  for i,v in enumerate(before):
   if not isinstance(after,list) or i>=len(after):errors.append(path+'/'+str(i)+': missing')
   else:preserve(v,after[i],path+'/'+str(i))
 else:
  checks['known_leaf_values_checked']+=1
  if before!=after:
   if allowed.get(path)==(before,after):intentional.append({'path':path,'reason':'Source-bound English correction in a new draft revision; original revision/source retained','repair_artifact':str(note_repair if path.endswith('/limitations/en') else repair)})
   else:errors.append(path+': changed')
for rid,r in old.items():
 if rid not in new:errors.append(rid+': missing record');continue
 checks['original_records_retained']+=1
 for key,f in r['fields'].items():
  if f['status']=='known':preserve(f['value'],new[rid]['fields'][key]['value'],rid+'/'+key)
for sid,(src,raw) in oldsources.items():
 checks['original_sources_checked']+=1
 if sid not in sources or sources[sid]!=(src,raw):errors.append(sid+': original immutable source changed')
for rid,r in new.items():
 draft=validate(r,new,sources,publish=False)
 if draft:draft_errors.append({'record_id':rid,'errors':draft})
 issues=validate(r,new,sources,publish=True)
 if issues:gates.append({'record_id':rid,'kind':r['kind'],'publication_blockers':issues})
stats={'original_records':len(old),'candidate_records':len(new),'checks':dict(checks),'intentional_source_bound_translation_revisions':intentional,'preservation_errors':errors,'draft_schema_or_evidence_errors':draft_errors,'original_active_release':oldmeta.get('active'),'candidate_active_release':meta.get('active'),'active_release_unchanged':oldmeta.get('active')==meta.get('active'),'record_kinds':dict(collections.Counter(r['kind'] for r in new.values())),'records_blocked_from_publication':len(gates),'publication_error_types':dict(collections.Counter(e for g in gates for e in g['publication_blockers'])),'publication_blockers':gates,'new_owner_approvals_created':False,'english_owner_review_performed':False}
out=B/('RELEASE_AUDIT_'+str(len(list(B.glob('RELEASE_AUDIT_*.json')))+1)+'.json');out.write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in stats.items() if k not in {'publication_blockers','publication_error_types','record_kinds'}},ensure_ascii=False,indent=2))
