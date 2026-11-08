import collections,json,re
from pathlib import Path
B=Path(__file__).resolve().parent
raw=[json.loads(s) for s in (B/'source_snapshot/data/curated/game_control_facts.jsonl').read_text('utf8').splitlines() if s.strip()]
audit=json.loads((B/'RAW_CONTROL_ANCESTRY_CHECK.json').read_text('utf8'));out=[]
for x in audit['unmatched']:
 g=json.loads((B/'source_snapshot'/x['source']).read_text('utf8'))['game_controls'];row=g['button_mappings'][x['row']]
 labels=[v for k,v in row.items() if k.startswith('button') and isinstance(v,str)]
 group=[r for r in raw if r.get('source_file')==Path(x['source']).name and r.get('game')==x['game'] and r.get('button')]
 exact=[r for r in group if r['button'] in labels and r.get('action_th')==row.get('action_th') and (not row.get('description_th') or r.get('description_th')==row['description_th'])]
 if exact:status='exact_row_retained_under_curated_platform_label'
 else:status='different_platform_or_button_variant_do_not_overwrite'
 out.append({**x,'classification':status,'curated_platforms':sorted({r['platform'] for r in group}),'curated_exact_ids':[r['id'] for r in exact]})
result={'counts':dict(collections.Counter(x['classification'] for x in out)),'rows':out,'scope':'Classify original platform variants without asserting venue installation or replacing curated button layouts'}
(B/'RAW_CONTROL_VARIANT_REVIEW.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result['counts']))
