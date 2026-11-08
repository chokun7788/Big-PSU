import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
from app.knowledge.common.query_scope import same_platform
with CommonStore(B/'candidate06.sqlite').connect() as c:rs=CommonStore.heads(c)
sets=[r for r in rs.values() if r['kind']=='control_set'];out=[]
for p in sorted((B/'source_snapshot/data/control_game').rglob('*.json')):
 x=json.loads(p.read_text('utf-8-sig')).get('game_controls')
 if not x:continue
 candidates=[r for r in sets if same_platform(x['platform'],value(r,'platform'))]
 for i,row in enumerate(x.get('button_mappings') or []):
  buttons=[str(v) for k,v in row.items() if k.startswith('button') and isinstance(v,str)]
  matches=[]
  for r in candidates:
   for b in value(r,'bindings') or []:
    if row.get('action_th')!=(b.get('action') or {}).get('th'):continue
    if row.get('description_th') and row['description_th']!=(b.get('notes') or {}).get('th'):continue
    if buttons and not any(v==(b.get('button_label') or {}).get('th') for v in buttons):continue
    matches.append(r['record_id'])
  out.append({'source':p.relative_to(B/'source_snapshot').as_posix(),'game':x['game_name'],'platform':x['platform'],'row':i,'action_th':row.get('action_th'),'matches':list(dict.fromkeys(matches))})
(B/'RAW_CONTROL_ANCESTRY_CHECK.json').write_text(json.dumps({'rows':len(out),'unmatched':[x for x in out if not x['matches']],'details':out},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'rows':len(out),'matched':sum(bool(x['matches']) for x in out),'unmatched':[x for x in out if not x['matches']]},ensure_ascii=False))
