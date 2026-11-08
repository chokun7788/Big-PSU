"""Append source-bound R66 draft revisions after agent review; never publish."""
import sys,json,re,hashlib,copy
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now
from app.knowledge.common.translation import protected
from app.knowledge.records import canonical_json
s=CommonStore(B/'common.sqlite')
with s.connect() as c:records=s.heads(c);active=dict(c.execute('SELECT * FROM cc_meta'))['active']
reviewed={
 ('competition_competition_rules_cs2_psu_phuket_2026_section_053','heading'):'4. Only drinking water in sealed containers and chewing gum are permitted.',
 ('competition_competition_rules_cs2_psu_phuket_2026_section_053','text'):'4. Only drinking water in sealed containers and chewing gum are permitted.',
 ('competition_competition_rules_cs2_psu_phuket_2026_section_027','heading'):'5. Overtime: 3 rounds per side (6 in total). The first team to win 4 of the 6 rounds wins. Starting money: $10,000. There is no limit on the number of overtimes.',
 ('competition_competition_rules_cs2_psu_phuket_2026_section_027','text'):'5. Overtime: 3 rounds per side (6 in total). The first team to win 4 of the 6 rounds wins. Starting money: $10,000. There is no limit on the number of overtimes.',
 ('competition_competition_rules_cs2_psu_phuket_2026_section_041','heading'):'1. Players may bring their own keyboard (wired/wireless), mouse (wired/wireless), mouse bungee, mouse pad, wired in-ear headphones, and wired headset.',
 ('competition_competition_rules_tekken8_psu_esports','event_name'):'PSU Esports ปะทะมันส์ สนั่นจอ',
 ('rental_all_zones_internal_full_day','name'):'All Zones, internal university units, full_day',
 ('rental_all_zones_internal_half_day','name'):'All Zones, internal university units, half_day',
 ('migrated_faq_curated_overview_identity','answer'):'PSU Esports Studio - Phuket is the Phuket branch of an esports learning and development center for excellence and economic development in southern Thailand. It is a gaming and esports learning center of Prince of Songkla University.',
}
changes=[];saved=[]
for rid,r0 in records.items():
 r=copy.deepcopy(r0);changed={};lineage=[]
 def walk(v,path,field):
  if isinstance(v,dict):
   if set(v)=={'th','en'} and isinstance(v.get('en'),str):
    old=v['en'];new=reviewed.get((rid,field)) if not path else None;reason='agent_review_against_Thai_source'
    if new is None:
     try:wrapped=json.loads(old)
     except ValueError:wrapped=None
     if isinstance(wrapped,dict) and set(wrapped)=={'kind','field','text'} and wrapped['kind']==r['kind'] and wrapped['field']==field and isinstance(wrapped['text'],str):new=wrapped['text'];reason='remove_verified_prompt_envelope_from_translation'
    if new is not None and new!=old:
     if protected(v['th'])!=protected(new):raise ValueError('Protected literals differ: '+rid+':'+field)
     v['en']=new;changed[field]=r['fields'][field]['value'];entry={'record_id':rid,'field':field,'path':path,'th':v['th'],'previous_en':old,'en':new,'reason':reason,'original_field_evidence':r0['fields'][field]['evidence_refs'],'owner_reviewed':False};changes.append(entry);lineage.append(entry)
   else:
    for k,x in v.items():walk(x,path+[k],field)
  elif isinstance(v,list):
   for i,x in enumerate(v):walk(x,path+[i],field)
 for field,f in r['fields'].items():
  if f['status']=='known':walk(f['value'],[],field)
 if not changed:continue
 raw=canonical_json({'mapped_fields':changed,'translation_lineage':lineage,'human_semantics_reviewed':False,'agent_semantics_reviewed':True});sid='r66_en_review_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'translation://r66-review/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[r['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None}
 s.add_source(source,raw,actor='r66-agent-translation-review')
 for field in changed:r['fields'][field]['evidence_refs']=[{'source_id':sid,'locator':'/mapped_fields/'+field}]
 r['localization'].update(en_status='agent_translated',source_revision_hash=None)
 saved.append(s.save(r,actor='r66-agent-translation-review',expected_version=r0['revision'],change_note='Agent-reviewed mistranslation or envelope correction; source Thai unchanged; no approval/publication'))
with s.connect() as c:assert dict(c.execute('SELECT * FROM cc_meta'))['active']==active
out=B/('REVIEWED_TRANSLATION_REPAIRS_'+str(len(list(B.glob('REVIEWED_TRANSLATION_REPAIRS_*.json')))+1)+'.json');out.write_text(json.dumps({'changes':changes,'revisions':len(saved),'published':False,'owner_reviewed':False},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'changes':len(changes),'revisions':len(saved),'published':False}))
