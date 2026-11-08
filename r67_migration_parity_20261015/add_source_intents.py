"""Preserve legacy semantic intent metadata as editable data, not question aliases."""
import copy,hashlib,json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
catalog=json.loads((H/'catalog.json').read_text('utf8'));faq=next(x for x in catalog if x['kind']=='faq')
spec={'key':'intent_key','meaning_th':'หัวข้อเชิงความหมายของคำถาม (ข้อมูลจัดหมวดจากต้นฉบับ)','publish_core':False,'reference_kind':None,'value_schema':{'type':'string','minLength':1}}
faq['fields'].append(spec);write(H/'catalog.json',catalog)
schema=json.loads((H/'schemas/faq.schema.json').read_text('utf8'));slot=copy.deepcopy(schema['properties']['fields']['properties']['topic']);slot['description']=spec['meaning_th'];slot['oneOf'][0]['properties']['value']=spec['value_schema'];schema['properties']['fields']['properties']['intent_key']=slot;write(H/'schemas/faq.schema.json',schema)
template=json.loads((H/'templates/faq.draft.json').read_text('utf8'));template['fields']['intent_key']={'status':'unknown','value':None,'evidence_refs':[],'note':'ไม่ต้องเดารหัสหัวข้อ หากยังไม่มีข้อมูลจัดหมวด'};write(H/'templates/faq.draft.json',template)
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now
from app.knowledge.records import canonical_json
from migrate_ids import sid
store=CommonStore(B/'common.sqlite');saved=[]
for p in sorted((B/'source_snapshot/data/content').rglob('*.json')):
 x=json.loads(p.read_text('utf-8-sig'))
 if x.get('kind')!='policy_rule' or x['facts'].get('route_category') in {'no_answer','english_support'}:continue
 rid='migrated_faq_'+sid(x['content_id']);r=store.get(rid)['record'];intent=x['facts']['intent']
 raw=canonical_json({'intent_key':intent,'source_path':p.relative_to(B/'source_snapshot').as_posix(),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'locator':'/facts/intent','derivation':'literal existing semantic classification; no generated facts'})
 source_id='r67_intent_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 store.add_source({'source_id':source_id,'kind':'derived_curated','path':'migration://r67/intent/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['faq'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='r67-intent-migration')
 r['fields']['intent_key']={'status':'known','value':intent,'evidence_refs':[{'source_id':source_id,'locator':'/intent_key'}],'note':'Existing intent metadata, not a new policy or question alias'}
 saved.append(store.save(r,actor='r67-intent-migration',expected_version=r['revision'],change_note='Preserve source intent metadata for reusable semantic lookup'))
write(B/'INTENT_METADATA_MIGRATION.json',saved)
p=H/'faq_topics.py';s=p.read_text('utf8');s=s.replace("q=normalize(question)\n", "q=normalize(question)\n    from .intent_index import select as source_intents\n    indexed=source_intents(question,records,operation)\n    if indexed:return indexed\n",1);p.write_text(s,encoding='utf8')
print('Preserved source intent metadata for',len(saved),'FAQs')
