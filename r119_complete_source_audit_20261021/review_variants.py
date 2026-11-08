import collections,hashlib,json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system'
read=lambda p:json.loads(p.read_text('utf8'))
write=lambda n,x:(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
x=read(R/'EXTERNAL_SOURCE_AUDIT.json');root=Path(x['root']);rows=[]
for item in x['files']:
 p=item['path'];row=dict(item)
 if item.get('same_as_candidate_legacy'):status='identical_current_source'
 elif '/original_files/' in p:
  target=S/p.split('/original_files/',1)[1]
  status='duplicate_archived_source' if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest()==item.get('sha256') else 'archived_variant_needs_review'
 elif p.startswith('data/knowledge/migration_'):status='prior_migration_manifests_and_reports'
 elif p.startswith(('data/eval/','data/human_review/')):status='evaluation_or_human_review_not_business_authority'
 elif p.startswith('data/logs/'):status='runtime_logs_not_business_authority'
 elif p.startswith('data/vector/'):status='derived_search_index_not_new_source'
 elif p.startswith('data/knowledge_inbox/'):status='inbox_schema_and_example_not_published_venue_fact'
 elif item.get('disposition')=='external_runtime_database_not_mutated':status='runtime_database_not_business_document'
 else:status='unclassified'
 row['review_disposition']=status;rows.append(row)
write('EXTERNAL_VARIANT_REVIEW.json',{'files':rows,'counts':dict(collections.Counter(r['review_disposition'] for r in rows))})
db=sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
records={rid:json.loads(p) for rid,p in db.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
mapping={m['content_id']:m for m in read(R/'RECORD_MAPPING.json')};checks=[]
def val(r,k):return r.get('fields',{}).get(k,{}).get('value')
def strings(v):
 if isinstance(v,str):return [v]
 if isinstance(v,dict):return [s for x in v.values() for s in strings(x)]
 if isinstance(v,list):return [s for x in v for s in strings(x)]
 return []
def ck(cid,path,key,want,actual,mode='contains'):
 text='\n'.join(strings(actual))
 ok=want in text if isinstance(want,str) else want==actual
 checks.append({'content_id':cid,'source_field':path,'native_field':key,'passed':ok,'expected':want,'actual':actual})
for item in read(R/'LEGACY_RECORDS.json'):
 a=item['record'];cid=a['content_id'];m=mapping[cid]
 if not m['native_record_id']:continue
 b=records[m['native_record_id']];f=a['facts'];th=a['locales']['th']['fields'];kind=a['kind']
 if kind=='game_profile':
  for old,new in [('title','title'),('summary_th','summary'),('how_to_play_th','how_to_play'),('genre','genre')]:
   if th.get(old):ck(cid,'locales.th.'+old,new,th[old],val(b,new))
 elif kind=='member':
  for old,new in [('name','display_name'),('role','role'),('affiliation','affiliation')]:
   if th.get(old):ck(cid,'locales.th.'+old,new,th[old],val(b,new))
  ck(cid,'facts.group','team',f['group'],val(b,'team'))
  if f.get('period'):ck(cid,'facts.period','period',f['period'],val(b,'period'))
 elif kind=='equipment':
  ck(cid,'locales.th.item','name',th['item'],val(b,'name'))
  for key in ['what_th','how_to_use_th','note_th']:
   if th.get(key):ck(cid,'locales.th.'+key,'usage',th[key],val(b,'usage'))
  for i,v in enumerate(th.get('use_cases_th',[])):ck(cid,'locales.th.use_cases_th/'+str(i),'usage',v,val(b,'usage'))
 elif kind in {'knowledge_fact','policy_rule','service_fee_policy'}:
  v=th.get('text') or th.get('answer')
  if v:ck(cid,'locales.th.text_or_answer','answer',v,val(b,'answer'))
 elif kind=='competition_document':
  texts='\n'.join(s for r in records.values() if r['kind']=='competition_rule' and val(r,'competition_id')==b['record_id'] for s in strings(val(r,'text')))
  for i,sec in enumerate(th['sections']):ck(cid,'locales.th.sections/'+str(i)+'/text','competition_rule.text',sec['text'],texts)
 elif kind=='control_map':
  for i,c in enumerate(th['controls']):
   for k in ['button','action_th','description_th']:
    if c.get(k):ck(cid,'locales.th.controls/'+str(i)+'/'+k,'bindings_or_limitations',c[k],[val(b,'bindings'),val(b,'limitations')])
 elif kind=='service_availability':
  for k,n in [('service_label','name'),('duration_minutes','session_minutes')]:ck(cid,'facts.'+k,n,f[k],val(b,n))
  titles=[val(records[val(r,'game_id')],'title') for r in records.values() if r['kind']=='game_service' and val(r,'service_id')==b['record_id']]
  for i,t in enumerate(f['games']):ck(cid,'facts.games/'+str(i),'game_service.game_id',t,titles)
 elif kind=='service_closure':
  for k,n in [('date','local_date'),('status','state')]:ck(cid,'facts.'+k,n,f[k],val(b,n))
write('TYPED_VALUE_REVIEW.json',{'checks':checks,'total':len(checks),'passed':sum(c['passed'] for c in checks),'mismatches':[c for c in checks if not c['passed']]})
print(json.dumps({'external':dict(collections.Counter(r['review_disposition'] for r in rows)),'typed_checks':len(checks),'mismatches':len([c for c in checks if not c['passed']])}))
