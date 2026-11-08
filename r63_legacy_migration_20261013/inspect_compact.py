exec((__import__('pathlib').Path(__file__).parent/'inspect_sources.py').read_text(encoding='utf-8').split("print('COUNTS'")[0])
for r in inventory:
 if r['kind']=='competition_document':
  print('COMP',r['id'],'factkeys',list(r['facts']), 'thkeys',list(r['th']['fields']), 'sections',len(r['th']['fields'].get('sections',[])), 'en',r['en']['status'],list(r['en']['fields']))
  print(json.dumps(r['facts'],ensure_ascii=False)[:1200]);print(json.dumps(r['th']['fields'].get('sections',[])[:3],ensure_ascii=False))
for rel in ['data/curated/user_service_facts_20261008.json','data/sources/user_service_answers_20261008.json']:
 r=json.loads((ROOT/rel).read_text(encoding='utf-8-sig'));print('JSON',rel,list(r))
 if 'claims' in r:
  for k,v in r['claims'].items(): print('CLAIM',k,v.get('status'),json.dumps(v.get('answers'),ensure_ascii=False))
 elif 'items' in r:print('ITEM',r['items'][:2])
for rel in ['data/curated/curated_facts.jsonl','data/curated/curated_facts_data_fix_2026-06-29.jsonl','data/curated/curated_facts_service_fee_2026_aliases.jsonl']:
 rows=[json.loads(x) for x in (ROOT/rel).read_text(encoding='utf-8-sig').splitlines() if x.strip()];print('JSONL',rel,len(rows));print(json.dumps(rows[0],ensure_ascii=False))
for k in ['bindings','steps','conditions_all','status_mapping']:
 for kind,s in CATALOG.items():
  for f in s['fields']:
   if f['key']==k:print('VALUE',kind,k,json.dumps(f['value_schema'],ensure_ascii=False))
