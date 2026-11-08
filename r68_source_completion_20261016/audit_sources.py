"""Inspect source structure and semantic coverage; no data writes."""
import collections,json,re,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
def read(rel):
 p=B/'source_snapshot'/rel
 if p.suffix=='.jsonl':return [json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()]
 return json.loads(p.read_text('utf-8-sig'))
db=B/(sys.argv[1] if len(sys.argv)>1 else 'before.sqlite')
tag=sys.argv[2] if len(sys.argv)>2 else 'before'
with CommonStore(db).connect() as c:rs=CommonStore.heads(c)
def norm(s):return re.sub(r'[^\w]','',str(s).casefold())
def game(name):
 exact=[r for r in rs.values() if r['kind']=='game' and norm(name) in [norm(v) for v in (value(r,'title') or {}).values() if v]]
 return exact[0] if len(exact)==1 else None
out={}
descriptions=[]
for i,x in enumerate(read('data/sources/our_games_raw.jsonl')):
 r=game(x['game']);v=value(r,'official_description') if r else None
 original=x.get('description','');language='th' if re.search('[\u0e00-\u0e7f]',original) else 'en';existing=(v or {}).get(language) or ''
 descriptions.append({'row':i,'game':x['game'],'record_id':r['record_id'] if r else None,'raw_len':len(original),'current_len':len(existing),'exact':original==existing,'prefix':original.startswith(existing.removesuffix('...')),'description':original,'current':v})
out['descriptions']=descriptions
aliases=[]
for x in read('data/curated/game_title_aliases.jsonl'):
 r=game(x['game']);known=set((r['aliases']['th']+r['aliases']['en']) if r else [])
 aliases.append({'game':x['game'],'record_id':r['record_id'] if r else None,'missing':[a for a in x['aliases'] if a not in known],'note':x.get('notes')})
out['aliases']=aliases
structures={}
for folder in ['curated','rules','sources','calendar','competition_rules']:
 for p in sorted((B/'source_snapshot/data'/folder).glob('*')):
  if p.suffix not in {'.json','.jsonl'}:continue
  rel=p.relative_to(B/'source_snapshot').as_posix()
  try:x=read(rel)
  except Exception as e:structures[rel]={'error':str(e)};continue
  rows=x if isinstance(x,list) else [x]
  structures[rel]={'rows':len(rows),'keys':dict(collections.Counter(k for r in rows if isinstance(r,dict) for k in r))}
out['structures']=structures
out['unknown_fields']=dict(collections.Counter(r['kind']+'.'+k for r in rs.values() for k,f in r['fields'].items() if f['status']=='unknown'))
out['fact_card_coverage']=[]
texts=[(r['record_id'],(value(r,'text') or {}).get('th','')) for r in rs.values() if r['kind']=='competition_rule']
for p in sorted((B/'source_snapshot/data/competition_rules').glob('*fact_cards*.jsonl')):
 for x in read(p.relative_to(B/'source_snapshot').as_posix()):
  answer=x.get('answer','');evidence=x.get('evidence','')
  matches=[rid for rid,t in texts if answer in t or (len(evidence)>20 and evidence in t)]
  out['fact_card_coverage'].append({'source':p.name,'id':x['id'],'game':x.get('game'),'answer':answer,'evidence':evidence,'exact_match':matches,'answer_type':x.get('answer_type')})
(B/('AUDIT_SOURCE_STRUCTURE_'+tag+'.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'descriptions':len(descriptions),'full_text_differences':sum(not x['exact'] for x in descriptions),'prefix_differences':sum(not x['exact'] and x['prefix'] for x in descriptions),'alias_missing':sum(len(x['missing']) for x in aliases),'aliases_unmatched':[x['game'] for x in aliases if not x['record_id']],'raw_files':len(structures),'fact_cards':len(out['fact_card_coverage']),'fact_cards_nonverbatim':sum(not x['exact_match'] for x in out['fact_card_coverage'])},ensure_ascii=False))
print(json.dumps(structures,ensure_ascii=False,indent=2))
print('UNKNOWN',json.dumps(out['unknown_fields'],ensure_ascii=False))
