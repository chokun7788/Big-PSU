"""Finish the schema/UI before freezing the final verification snapshot."""
import copy,json,hashlib,sys
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
catalog=json.loads((H/'catalog.json').read_text('utf8'));g=next(c for c in catalog if c['kind']=='game')
vs={'type':'array','items':{'type':'string','minLength':1},'uniqueItems':True}
g['fields'].append({'key':'source_listing_sections','meaning_th':'หมวดที่ระบุในหน้าเกมต้นฉบับ (ไม่ใช่สถานะติดตั้งสด)','publish_core':False,'reference_kind':None,'value_schema':vs})
write(H/'catalog.json',catalog)
p=H/'schemas/game.schema.json';s=json.loads(p.read_text('utf8'));field=copy.deepcopy(s['properties']['fields']['properties']['supported_platforms']);field['oneOf'][0]['properties']['value']=vs;s['properties']['fields']['properties']['source_listing_sections']=field;write(p,s)
p=H/'templates/game.draft.json';s=json.loads(p.read_text('utf8'));s['fields']['source_listing_sections']={'status':'unknown','value':None,'evidence_refs':[],'note':'ไม่ใช้หมวดในหน้าแนะนำเกมแทนข้อมูลติดตั้งรายเครื่องหรือสถานะจอง'};write(p,s)
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now
from app.knowledge.records import canonical_json
store=CommonStore(B/'common.sqlite');lineage=json.loads((B/'RAW_RECOVERY_LINEAGE.json').read_text('utf8'));source_map={x['locator']:x['record_id'] for x in lineage if x['field']=='official_description'}
raw=[json.loads(s) for s in (B/'source_snapshot/data/curated/our_games_scraped_details.jsonl').read_text('utf-8-sig').splitlines() if s.strip()]
saved=[]
for i,x in enumerate(raw):
 rid=source_map['/'+str(i)];r=store.get(rid)['record'];v=x['listed_under'] if isinstance(x['listed_under'],list) else [x['listed_under']]
 doc={'source_listing_sections':v,'source_path':'data/curated/our_games_scraped_details.jsonl','row':i,'scope':'literal source listing only; no live availability or installation assertion'};text=canonical_json(doc);sid='r67_listing_'+hashlib.sha256(text.encode()).hexdigest()[:24]
 store.add_source({'source_id':sid,'kind':'derived_curated','path':'migration://r67/listing/'+rid,'sha256':hashlib.sha256(text.encode()).hexdigest(),'authority_for':['game'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},text,actor='r67-source-listing')
 r['fields']['source_listing_sections']={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/source_listing_sections'}],'note':doc['scope']}
 saved.append(store.save(r,expected_version=r['revision'],actor='r67-source-listing',change_note='Preserve original page section without creating venue-offering links'))
write(B/'SOURCE_LISTING_MIGRATION.json',saved)
p=H/'query_contract.py';s=p.read_text('utf8').replace("CUES={'official_description':", "CUES={'source_listing_sections':['หน้าเกมอยู่หมวด','listed under','source listing sections'], 'official_description':");p.write_text(s,encoding='utf8')
p=H/'build_info.py';s=p.read_text('utf8').replace("'build_id':'common-r62'","'build_id':'common-r67-source-parity'");p.write_text(s,encoding='utf8')
p=H/'ui/owner.js';s=p.read_text('utf8');s=s.replace("function defaults(s)", "Object.assign(SUB_LABELS,{button_label:'ชื่อปุ่มตามต้นฉบับ เช่น A / B',notes:'คำอธิบายเพิ่มเติม',section:'หมวดในชุดปุ่ม',source_order:'ลำดับจากต้นฉบับ'});\nfunction defaults(s)");p.write_text(s,encoding='utf8')
manifest=[{'path':p.relative_to(B/'system').as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (B/'system/app').rglob('*') if p.is_file() and '__pycache__' not in p.parts]
write(B/'FROZEN_CODE_MANIFEST.json',manifest)
print('Frozen final format; listing fields',len(saved))
