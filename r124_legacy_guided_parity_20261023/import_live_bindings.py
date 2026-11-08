"""Derive draft bindings from the current public WordPress service catalogue.

Only the new candidate database is written. No approvals/publication created.
"""
import hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
from app.knowledge.common.registry import template,value,now
from app.knowledge.common.store import CommonStore
from app.knowledge.records import canonical_json
from app.knowledge.common.domain_flow.scope import canonical_resource,norm
from app.knowledge.common.domain_flow.projection import title
from app.booking.live_status import _cache_sec
probe=json.loads((R/'LIVE_CONNECTION_PROBE.json').read_text('utf8'));assert probe['results']['wordpress']['snapshot']['ok']
catalog=probe['catalog'];store=CommonStore(S/'data/knowledge/common.sqlite')
with store.connect() as c:
 records=store.heads(c);approvals=c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0];registered=store.sources(c)
services={rid:r for rid,r in records.items() if r['kind']=='service'};resources={rid:r for rid,r in records.items() if r['kind']=='resource'}
mapped=[]
for row in catalog:
 name=row['name'];q=norm(name);m=re.search(r'(pc|cockpit|ps5|playstation\s*5)\s*#\s*(\d+)',q)
 resource=None
 if m:
  family={'playstation 5':'ps5','ps5':'ps5','pc':'pc','cockpit':'cockpit'}[m[1]];number=int(m[2]);needle=f'{family}{number}'
  matches=[rid for rid,r in resources.items() if any(canonical_resource(a)==needle for a in [*title(r).values(),*sum(r['aliases'].values(),[])])]
  assert len(matches)==1,(name,matches);resource=matches[0]
  choices=[rid for rid,r in services.items() if resource in (value(r,'resource_ids') or [])]
 else:
  maxpersons=re.search(r'1\s*-\s*(\d+)\s*persons?',q);maxpersons=int(maxpersons[1]) if maxpersons else None
  choices=[rid for rid,r in services.items() if (('nintendo' in q and value(r,'platform')=='Nintendo Switch' and value(r,'capacity_max')==maxpersons)
    or ('vr station' in q and value(r,'platform')=='VR' and value(r,'session_minutes')==int(row['duration'])))]
 assert len(choices)==1,(name,choices)
 sid=choices[0];rid='live_wordpress_'+row['id'];record=template('live_binding');record['record_id']=rid
 record['aliases']={'th':[name],'en':[name]};record['localization'].update(source_language='en',en_status='agent_translated')
 record['validity']={'state':'known','effective_from':now(),'effective_until':None}
 fields={'service_id':sid,'provider':'wordpress_booking','external_resource_key':row['id'],
  'physical_pool_key':resource or 'wordpress_resource_'+row['id'],
  'status_mapping':[{'raw':'available','normalized':'free'},{'raw':'partial','normalized':'free'},{'raw':'busy','normalized':'occupied'},
    {'raw':'closed','normalized':'unavailable'},{'raw':'unknown','normalized':'unknown'}],
  'timezone':'Asia/Bangkok','freshness_max_age_seconds':max(1,int(_cache_sec())),
  'freshness_policy':{'th':'อ่านเมื่อมีคำถาม ใช้ cache อายุไม่เกินนโยบาย transport เดิม และคงจำนวนว่างของ partial',
    'en':'Read on demand; freshness follows the existing transport cache policy; partial retains its available count.'}}
 snapshot=canonical_json({'provider_catalogue_row':row,'mapping_basis':'legacy service family/ordinal/capacity/session identity matched against current common records',
   'matching_internal_resource':resource,'mapped_fields':fields,'engineering_policy_not_owner_business_approval':True})
 sourceid='r124_binding_'+hashlib.sha256(snapshot.encode()).hexdigest()[:24]
 source={'source_id':sourceid,'kind':'derived_curated','path':'WordPress public services catalogue + existing legacy transport configuration',
   'sha256':hashlib.sha256(snapshot.encode()).hexdigest(),'authority_for':['live_binding'],'observed_at':now(),'trust':'internal_verified',
   'public_url':'https://esports.computing.psu.ac.th/wp-content/uploads/powerbi-exports/wbk_services.csv'}
 if sourceid not in registered:store.add_source(source,snapshot,actor='r124_legacy_binding_migration')
 for key,v in fields.items():record['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':sourceid,'locator':'/mapped_fields/'+key}],
    'note':'Derived from observed provider catalogue and existing runtime policy; candidate draft, no owner approval created.'}
 if rid in records:
  assert all(value(records[rid],k)==v for k,v in fields.items());saved={'record_id':rid,'version':records[rid]['revision'],'resumed_existing_identical':True}
 else:saved=store.save(record,actor='r124_legacy_binding_migration',expected_version=0,change_note='Restore legacy on-demand provider mapping in isolated candidate')
 mapped.append({'external_id':row['id'],'external_name':name,'binding_id':rid,'service_id':sid,'resource_id':resource,'source_id':sourceid,'save':saved})
with store.connect() as c:assert c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0]==approvals
(R/'LIVE_BINDING_MIGRATION.json').write_text(json.dumps({'bindings':mapped,'count':len(mapped),'approvals_unchanged':True,'production_installed':False,'no_runtime_occupancy_stored':True},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'bindings_imported':len(mapped),'approvals_unchanged':True,'production_installed':False},ensure_ascii=False))
