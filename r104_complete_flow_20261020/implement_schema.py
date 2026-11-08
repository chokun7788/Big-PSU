"""Add revision-bound mapping metadata; keep approved 3.0 payloads untouched."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent/'system/app/knowledge/common'
def obj(properties,required=None):return {'type':'object','properties':properties,'required':required or list(properties),'additionalProperties':False}
s={'type':'string','minLength':1};arr=lambda x:{'type':'array','items':x,'uniqueItems':True}
evidence=obj({'source_id':s,'locator':s})
ref=obj({'record_id':s,'field':s,'path':{'type':'string'},'projection':{'enum':['identity','currency_literal']},'quote':{'type':['string','null']}},['record_id','field'])
scope=obj({'status':{'enum':['known','unknown']},'value':{'type':['array','null'],'items':s,'uniqueItems':True}})
app=obj({'status':{'enum':['known','unknown']},'service_ids':arr(s),'duration_minutes':{'type':['integer','null'],'minimum':1},'platform':{'type':['string','null']},'effective_from':{'type':['string','null'],'format':'date-time'},'effective_until':{'type':['string','null'],'format':'date-time'}})
binding=obj({'binding_id':{'type':'string','pattern':'^[a-z][a-z0-9_:-]{1,79}$'},'predicate':s,'subject_ref':s,'unit':{'type':['string','null']},'actor_scope':scope,'value_ref':ref,'condition_refs':arr(ref),'exception_refs':arr(ref),'applicability':app,'authority_refs':arr(evidence),'dependency_refs':arr(s),'supersedes_refs':arr(s),'evidence_refs':arr(evidence)})
(R/'schemas/claim_binding.schema.json').write_text(json.dumps(binding,ensure_ascii=False,indent=2),'utf8')
catalog=json.loads((R/'catalog.json').read_text('utf8'))
for c in catalog:
 p=R/'schemas'/f"{c['kind']}.schema.json";x=json.loads(p.read_text('utf8'))
 x['properties']['schema_version']={'enum':['studio-content-3.0','studio-content-3.1']};x['properties']['claim_bindings']=arr(binding)
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
 p=R/'templates'/f"{c['kind']}.draft.json";x=json.loads(p.read_text('utf8'));x['schema_version']='studio-content-3.1';x['claim_bindings']=[];p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def edit(name,old,new):
 p=R/name;t=p.read_text('utf8')
 if t.count(old)!=1:raise ValueError((name,old[:70],t.count(old)))
 p.write_text(t.replace(old,new),'utf8')
edit('registry.py',"VERSION='studio-content-3.0'","VERSION='studio-content-3.1'\nSUPPORTED_VERSIONS={'studio-content-3.0',VERSION}")
edit('registry.py',"    kind=record['kind']; fields=record['fields']; v=record['validity']", "    kind=record['kind']; fields=record['fields']; v=record['validity']\n    if record.get('claim_bindings') and record['schema_version']!=VERSION:errors.append('Claim mappings require schema 3.1')\n    from .claim_bindings import validate_bindings\n    errors.extend(validate_bindings(record,records,sources,publish=publish,demo=demo))")
edit('registry.py',"    rates=[r for r in records.values() if r['kind']=='rate']", "    from .claim_bindings import release_binding_errors\n    errors.extend(release_binding_errors(records))\n    rates=[r for r in records.values() if r['kind']=='rate']")
p=R/'store.py';t=p.read_text('utf8');t=t.replace('from .registry import ', 'from .registry import SUPPORTED_VERSIONS, ',1)
t=t.replace("data['schema_version']!=VERSION","data['schema_version'] not in SUPPORTED_VERSIONS").replace("release['schema_version']!=VERSION","release['schema_version'] not in SUPPORTED_VERSIONS").replace("p['schema_version']!=VERSION","p['schema_version'] not in SUPPORTED_VERSIONS")
old="            used={ref['source_id'] for r in records.values() for f in r['fields'].values() for ref in f['evidence_refs']}"
new="""            from .claim_bindings import references, index as claim_index
            for rid,r in records.items():
                for target in references(r):refs.setdefault(target,[]).append(rid)
            used={ref['source_id'] for r in records.values() for f in r['fields'].values() for ref in f['evidence_refs']}
            used.update(ref['source_id'] for r in records.values() for b in r.get('claim_bindings',[]) for ref in b['evidence_refs']+b['authority_refs'])"""
assert t.count(old)==1;t=t.replace(old,new)
old="'sources':{k:sources[k][0] for k in used}}";assert t.count(old)==1;t=t.replace(old,"'sources':{k:sources[k][0] for k in used},'claim_index':claim_index(records)}")
p.write_text(t,'utf8')
edit('snapshot_provider.py',"  return {'active':'owner-draft-preview'", "  from .claim_bindings import references,index as claim_index\n  for rid,r in records.items():\n   for target in references(r):refs.setdefault(target,[]).append(rid)\n  return {'active':'owner-draft-preview'")
edit('snapshot_provider.py',"'reverse_refs':refs,'text_index':index}","'reverse_refs':refs,'text_index':index,'claim_index':claim_index(records)}")
edit('owner_server.py',"    snapshot=canonical_json({k:f['value'] for k,f in record.get('fields',{}).items() if f.get('status')=='known'})", "    values={k:f['value'] for k,f in record.get('fields',{}).items() if f.get('status')=='known'}\n    if record.get('claim_bindings'):\n        record['schema_version']=VERSION\n        values['_claim_bindings']=[{k:v for k,v in b.items() if k not in {'evidence_refs','authority_refs'}} for b in record['claim_bindings']]\n    snapshot=canonical_json(values)")
edit('owner_server.py',"    record.update(revision=expected_version+1", "    for i,b in enumerate(record.get('claim_bindings',[])):\n        b['evidence_refs']=[{'source_id':sid,'locator':'/_claim_bindings/'+str(i)}]\n    record.update(revision=expected_version+1")
print('Schema 3.1, source-bound mapping review/release/index/FKs installed; no chatbot calls')
