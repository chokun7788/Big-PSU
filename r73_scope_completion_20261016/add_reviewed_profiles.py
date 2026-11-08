"""Add routing metadata to 2 copied records; preserve every factual field."""
import copy,hashlib,json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now,value,validate
from app.knowledge.records import canonical_json
store=CommonStore(B/'system/data/knowledge/common.sqlite')
profiles={
 'migrated_owner_claim_personal_keyboard_mouse':{'task':'permission','subjects':[{'th':'คีย์บอร์ด','en':'keyboard'},{'th':'เมาส์','en':'mouse'}],'ownership':'personal','context':'studio'},
 'procedure_wrong_slip':{'task':'correction','subjects':[{'th':'สลิป','en':'slip'}],'ownership':'any','context':'studio'},
}
before={};after={};changes=[]
for rid,profile in profiles.items():
 record=store.get(rid)['record'];before[rid]=copy.deepcopy(record)
 if value(record,'query_profile') is not None:raise ValueError('Profile already migrated; refusing another data mutation')
 raw=canonical_json({'query_profile':profile,'basis':{'kind':'agent_routing_annotation','record_id':rid,'revision':record['revision'],'factual_source_fields':{key:record['fields'][key] for key in ('question','answer','name','steps','preconditions') if key in record['fields']},'owner_approval_created':False}})
 sid='r73_profile_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'migration-routing-review://r73/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[record['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
 store.add_source(source,raw,actor='r73-agent-routing-review')
 record['fields']['query_profile']={'status':'known','value':profile,'evidence_refs':[{'source_id':sid,'locator':'/query_profile'}],'note':'Agent routing annotation based on exact existing source; no new policy or owner approval.'}
 store.save(record,actor='r73-agent-routing-review',expected_version=record['revision'],change_note='Add query routing metadata only; preserve facts and evidence')
 saved=store.get(rid)['record'];after[rid]=saved
 assert {k:v for k,v in saved['fields'].items() if k!='query_profile'}==before[rid]['fields']
 changes.append({'record_id':rid,'from_revision':before[rid]['revision'],'to_revision':saved['revision'],'factual_fields_byte_equivalent':True,'profile':profile})
with store.connect() as c:
 rs=store.heads(c);sources=store.sources(c);errors={rid:validate(r,rs,sources) for rid,r in rs.items() if validate(r,rs,sources)}
 assert not errors,errors
 assert c.execute('select count(*) from cc_approvals').fetchone()[0]==0
 assert dict(c.execute('select key,value from cc_meta'))['active']==''
(B/'PROFILE_MIGRATION_AUDIT.json').write_text(json.dumps({'changes':changes,'before':before,'after':after,'records':len(rs),'schema_errors':errors,'approvals_created':False},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(changes,ensure_ascii=False,indent=2))
