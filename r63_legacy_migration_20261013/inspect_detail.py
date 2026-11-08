exec((__import__('pathlib').Path(__file__).parent/'inspect_sources.py').read_text(encoding='utf-8').split("print('COUNTS'")[0])
for k,s in CATALOG.items():
    print('KIND',k,[(x['key'],x['value_schema'].get('enum') or x['value_schema'].get('type'),x['reference_kind']) for x in s['fields']])
for kind in ['competition_document','equipment','member','policy_rule']:
    r=next(r for r in inventory if r['kind']==kind)
    print('SAMPLE',kind,json.dumps(r,ensure_ascii=False)[:6000])
for r in inventory:
    if r['kind']=='service_availability':print('AVAILABLE',r['id'],json.dumps(r['facts'],ensure_ascii=False))
for f in ['data/curated/zone_rental_fees_20261006.json','data/curated/user_service_facts_20261008.json','data/sources/user_service_answers_20261008.json','data/curated/service_policy_answers.json','booking_dashboard/center_schedule.json']:
    p=ROOT/f
    print('EXTRA',f,p.read_text(encoding='utf-8-sig')[:9000])
print('COMPETITION CARDS', (ROOT/'data/competition_rules/competition_rule_fact_cards.jsonl').read_text(encoding='utf-8-sig').splitlines()[0][:6000])
