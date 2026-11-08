"""Give typed procedures/contacts editable bilingual names rather than code headings."""
import copy,hashlib,json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
cat=json.loads((H/'catalog.json').read_text('utf8'));by={x['kind']:x for x in cat}
local=copy.deepcopy(next(f['value_schema'] for f in by['game']['fields'] if f['key']=='title'))
for kind in ['procedure','contact']:
 assert not any(f['key']=='name' for f in by[kind]['fields'])
 by[kind]['fields'].insert(0,{'key':'name','meaning_th':'ชื่อที่แสดงให้ผู้ใช้เห็น','publish_core':False,'reference_kind':None,'value_schema':local})
 p=H/'schemas'/f'{kind}.schema.json';s=json.loads(p.read_text('utf8'));slot=copy.deepcopy(next(iter(s['properties']['fields']['properties'].values())));slot['description']='ชื่อที่แสดงให้ผู้ใช้เห็น';slot['oneOf'][0]['properties']['value']=local;s['properties']['fields']['properties']['name']=slot;p.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf8')
 p=H/'templates'/f'{kind}.draft.json';t=json.loads(p.read_text('utf8'));t['fields']['name']={'status':'unknown','value':None,'evidence_refs':[],'note':'กรอกชื่อเรื่องที่คนอ่านเข้าใจได้'};p.write_text(json.dumps(t,ensure_ascii=False,indent=2),encoding='utf8')
(H/'catalog.json').write_text(json.dumps(cat,ensure_ascii=False,indent=2),encoding='utf8')
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now
from app.knowledge.records import canonical_json
db=B/'candidate06.sqlite'
if db.exists():raise SystemExit('Existing candidate06 preserved')
with sqlite3.connect((B/'candidate05.sqlite').as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as b:a.backup(b)
store=CommonStore(db)
with store.connect() as c:rs=store.heads(c)
lineage=json.loads((B/'MIGRATION_LINEAGE.json').read_text('utf8'))
rel='data/curated/user_service_facts_20261008.json';p=B/'source_snapshot'/rel;raw=json.loads(p.read_text('utf8'))
for rid,key in [('procedure_change_machine','change_machine'),('procedure_change_time','change_time'),('procedure_wrong_slip','wrong_slip'),('contact_studio_facebook','contact')]:
 r=copy.deepcopy(rs[rid]);v={lang:r['aliases'][lang][0] for lang in ('th','en')}
 row={'record_id':rid,'field':'name','source_path':rel,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'locator':'/claims/'+key,'source_value':raw['claims'][key],'mapped_value':v,'transform':'human-readable bilingual topic label derived from the existing claim, no new service policy'}
 body=canonical_json({'mapped_fields':{'name':v},'field_lineage':[row],'status':'draft_only_not_owner_approved'});sid='r68_name_'+hashlib.sha256(body.encode()).hexdigest()[:24]
 store.add_source({'source_id':sid,'kind':'derived_curated','path':'migration://r68/'+rid+'/display-name','sha256':hashlib.sha256(body.encode()).hexdigest(),'authority_for':[r['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},body,actor='r68-owner-names')
 r['fields']['name']={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/mapped_fields/name'}],'note':'Source-bound bilingual label, not owner approval'}
 store.save(r,expected_version=r['revision'],actor='r68-owner-names',change_note='Use an editable bilingual display name instead of a machine topic code')
 lineage.append(row)
(B/'MIGRATION_LINEAGE_final.json').write_text(json.dumps(lineage,ensure_ascii=False,indent=2),encoding='utf8')
p=H/'semantics.py';s=p.read_text('utf8');needle="        keys=[k for k in fields if k not in hidden]"
assert needle in s;s=s.replace(needle,"        if kind=='procedure' and fields.get('name',{}).get('status')=='known':hidden.add('topic')\n"+needle);p.write_text(s,encoding='utf8')
print('Added bilingual display names to 3 procedures and 1 contact')
