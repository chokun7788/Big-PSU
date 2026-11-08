"""Map source facts into new drafts; never manufacture approval or write ROOT."""
import json,hashlib,sys
from pathlib import Path
OUT=Path(__file__).resolve().parent;CAND=OUT/'system/PSU_Esports_Chatbot_Local';sys.path.insert(0,str(CAND))
from app.knowledge.common.registry import template,now
from app.knowledge.common.store import CommonStore
from app.knowledge.common.importer import import_bundle
from app.knowledge.records import canonical_json
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
RESEARCH=OUT.parent/'canonical_format_research_20261010_180226'
bundle={'schema_version':'studio-content-3.0','sources':[],'records':[]};queue=[]
def add(r,originals,trust='legacy_unreviewed'):
    sid='migration_'+r['record_id'];mapped={k:f['value'] for k,f in r['fields'].items() if f['status']=='known'}
    payload={'mapped_fields':mapped,'lineage':originals,'transform':'exact field extraction or explicitly recorded THB × 100 conversion; no publication approval'}
    snapshot=canonical_json(payload)
    src={'source_id':sid,'kind':'derived_curated','path':'migration://'+sid,'sha256':hashlib.sha256(snapshot.encode('utf-8')).hexdigest(),'authority_for':[r['kind']],'observed_at':now(),'trust':trust,'public_url':None}
    for k,f in r['fields'].items():
        if f['status']=='known':f['evidence_refs']=[{'source_id':sid,'locator':'/mapped_fields/'+k}]
    bundle['sources'].append({'source':src,'snapshot':snapshot});bundle['records'].append(r)
for p in sorted((ROOT/'data/content').rglob('*.json')):
    if any(x in p.parts for x in ('schema','review','projections','releases')) or p.name=='manifest.json':continue
    row=json.loads(p.read_text(encoding='utf-8'))
    if 'content_id' not in row:continue
    queue.append({'legacy_id':row['content_id'],'category':row['category'],'source_file':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'migration':'draft_mapped' if row['category']=='games' else 'pending_typed_mapping','en_status':row.get('locales',{}).get('en',{}).get('status'),'notes':'Original runtime remains active until supported adapters and owner review replace it.'})
    if row['category']!='games':continue
    r=template('game');r['record_id']=row['content_id'];r['aliases']=row['aliases'];th=row['locales'].get('th',{}).get('fields',{});en=row['locales'].get('en',{}).get('fields',{})
    for key,legacy in [('title','title'),('summary','summary_th'),('how_to_play','how_to_play_th'),('genre','genre')]:
        val=th.get(legacy)
        if val:
            en_key={'summary_th':'summary_en','how_to_play_th':'how_to_play_en'}.get(legacy,legacy)
            translated=en.get(en_key)
            if row['locales'].get('en',{}).get('status') not in ('approved','reviewed','source'):translated=None
            r['fields'][key].update(status='known',value={'th':val,'en':translated},note='Imported from canonical source; field mapping needs factual review')
    if r['fields']['title']['status']!='known':
        name=row.get('facts',{}).get('game')
        if name:r['fields']['title'].update(status='known',value={'th':name,'en':None},note='Original game name')
    add(r,[queue[-1]])
actual=json.loads((RESEARCH/'examples/actual_source_drafts.bundle.json').read_text(encoding='utf-8'))
for r in actual['records']:
    if r['kind']=='game':continue
    r['schema_version']='studio-content-3.0'
    # Keep original source provenance and explicit missing validity. No invented date/hours.
    lineage=[s for s in actual['sources'] if any(ref['source_id']==s['source_id'] for f in r['fields'].values() for ref in f['evidence_refs'])]
    add(r,lineage,'legacy_unreviewed')
(OUT/'migration_drafts.bundle.json').write_text(json.dumps(bundle,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'migration_queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf-8')
db=CAND/'data/knowledge/approved.sqlite';store=CommonStore(db);store.initialize();result=import_bundle(store,bundle,actor='migration-tool-draft-only')
(OUT/'migration_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'legacy_records':len(queue),'drafts':len(bundle['records']),'saved':len(result['saved']),'errors':result['pending_errors'],'active_release':store.snapshot()['active']},ensure_ascii=False))
if result['pending_errors']:raise SystemExit(1)
