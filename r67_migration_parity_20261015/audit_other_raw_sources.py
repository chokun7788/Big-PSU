"""Check the remaining raw business sources, independently of record counts."""
import json,re,sys,collections,unicodedata
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
from migrate_ids import stable,sid
with CommonStore(B/'common.sqlite').connect() as c:records=CommonStore.heads(c)
def norm(s):return re.sub(r'\s+',' ',unicodedata.normalize('NFC',str(s))).strip().casefold()
def strings(v):
 if isinstance(v,dict):
  for k,x in v.items():
   if k in {'value','th','en'} or isinstance(x,(dict,list)):yield from strings(x)
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,str):yield norm(v)
rows=[]
for folder in ['curated','rules']:
 for p in sorted((B/'source_snapshot/data'/folder).glob('*.jsonl')):
  if p.name in ['game_control_facts.jsonl','our_games_scraped_details.jsonl','game_title_aliases.jsonl']:continue
  for index,x in enumerate(json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()):
   identity=x.get('id');category=x.get('category');targets=[]
   if identity:
    targets=[r for key,r in records.items() if key in {stable(identity),'migrated_faq_'+sid(identity)}]
   if p.name=='curated_competition_rules.jsonl':targets=[r for r in records.values() if r['kind']=='competition_rule' and (value(r,'text') or {}).get('th')==x['text']]
   if p.name=='member_profiles.jsonl':targets=[r for r in records.values() if r['kind']=='person' and (value(r,'display_name') or {}).get('th')==x['name']]
   if p.name=='game_item_details.jsonl':keys=['genre','summary_th','how_to_play_th']
   elif p.name=='equipment_item_details.jsonl':keys=['item','what_th','how_to_use_th','note_th']
   elif p.name=='member_profiles.jsonl':keys=['name','role','affiliation','period']
   elif p.name=='service_game_availability.jsonl':keys=['service_label'] # Full game/resource membership is checked through the original FK lineage.
   else:keys=['text','answer_th','answer_en']
   texts=[s for r in targets for s in strings(r['fields'])]
   for key in keys:
    original=x.get(key)
    if not isinstance(original,str) or not original:continue
    present=any(norm(original) in text for text in texts)
    if category in {'no_answer','english_support'} and not targets:status='engine_configuration_archived'
    elif present:status='readable_exact'
    elif any(v.get('text')==original for r in targets for v in (value(r,'source_variants') or [])):status='retained_source_variant_not_active_policy'
    elif identity in {'rule_booking_steps','rule_en_booking_steps_natural'} and key=='answer_en' and all(any(term in norm((value(r,'answer') or {}).get('en') or '') for r in targets) for term in ['select a service','date and time','user information','review','bank transfer','payment slip']):status='reviewed_equivalent_six_steps'
    else:status='not_verbatim_in_current_head'
    rows.append({'source':p.relative_to(B/'source_snapshot').as_posix(),'row':index,'id':identity,'field':key,'value':original,'targets':[r['record_id'] for r in targets],'status':status})
result={'counts':dict(collections.Counter(r['status'] for r in rows)),'rows':rows}
(B/'OTHER_RAW_TEXT_AUDIT_REVIEWED.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result['counts']))
for r in rows:
 if r['status']=='not_verbatim_in_current_head':print(json.dumps(r,ensure_ascii=False)[:700])
