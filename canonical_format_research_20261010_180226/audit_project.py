import json, hashlib
from pathlib import Path
from collections import Counter, defaultdict
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=Path(__file__).resolve().parent
paths=[p for p in (ROOT/'data').rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl') and not set(p.relative_to(ROOT/'data').parts)&{'eval','logs','vector','ground_truth','human_review'}]
paths += [ROOT/'booking_dashboard/center_schedule.json']
manifest=[]; counts=Counter(); kinds=Counter(); examples={}; errors=[]
for p in sorted(paths):
    raw=p.read_bytes(); rel=p.relative_to(ROOT).as_posix()
    manifest.append({'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
    try:
        text=raw.decode('utf-8-sig')
        values=[json.loads(x) for x in text.splitlines() if x.strip()] if p.suffix=='.jsonl' else [json.loads(text)]
    except Exception as e:
        errors.append({'path':rel,'error':str(e)}); continue
    group='/'.join(p.relative_to(ROOT/'data').parts[:2]) if p.is_relative_to(ROOT/'data') else 'booking_dashboard'
    counts[group]+=len(values)
    if group not in examples and values: examples[group]={'path':rel,'record':values[0]}
    for v in values:
        if isinstance(v,dict) and rel.startswith('data/content/') and not set(p.relative_to(ROOT/'data/content').parts)&{'review','projections','schema','releases'}:
            kinds[(str(v.get('category')),str(v.get('kind')))]+=1
    if any(x in rel for x in ('game_item_details','service_game_availability','user_service_facts','zone_rental_fees','canonical_content.schema','document.schema','competition_rule_submission_template','rulebook_registry','equipment_item_details','member_profiles','center_schedule')):
        examples[rel]={'path':rel,'record':values[0] if values else None}
(OUT/'PROJECT_DATA_INVENTORY.json').write_text(json.dumps({'root':str(ROOT),'files':len(paths),'records_by_path_group':dict(counts),'canonical_kinds':[{ 'category':a,'kind':b,'count':n} for (a,b),n in kinds.items()],'parse_errors':errors,'examples':examples},ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'SOURCE_HASHES_BEFORE.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files':len(paths),'parse_errors':errors,'groups':dict(counts),'canonical_kinds':[{ 'category':a,'kind':b,'count':n} for (a,b),n in kinds.items()]},ensure_ascii=False,indent=2))
