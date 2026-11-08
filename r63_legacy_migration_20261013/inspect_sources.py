import json,sys,collections
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent
SYSTEM=BASE/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(SYSTEM))
from app.knowledge.common.registry import CATALOG,template
OUT=Path(__file__).resolve().parent
inventory=[]
for p in sorted((ROOT/'data/content').rglob('*.json')):
    if any(x in p.relative_to(ROOT/'data/content').parts for x in ('schema','review','projections','releases')):continue
    r=json.loads(p.read_text(encoding='utf-8-sig'))
    if 'content_id' not in r:continue
    inventory.append({'path':p.relative_to(ROOT).as_posix(),'id':r['content_id'],'category':r['category'],'kind':r['kind'],'facts':r.get('facts'), 'th':r.get('locales',{}).get('th'),'en':r.get('locales',{}).get('en'),'source':r.get('source')})
(OUT/'SOURCE_INVENTORY.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
print('COUNTS',dict(collections.Counter((r['category'],r['kind']) for r in inventory)))
for k,s in CATALOG.items():print('SCHEMA',k,[(x['key'],x['value_schema'],x['reference_kind'],x['publish_core']) for x in s['fields']])
for category in sorted(set(r['category'] for r in inventory)):
    rows=[r for r in inventory if r['category']==category]
    print('SAMPLE',category,json.dumps(rows[0],ensure_ascii=False)[:4500])
for d in ['knowledge','calendar','competition_rules','curated']:
    print('FILES',d,[p.relative_to(ROOT).as_posix() for p in (ROOT/'data'/d).iterdir() if p.is_file()][:35])
