"""Language topics and normative-clause checks; all rule values remain source data."""
import re
from .scope import norm

# These are linguistic concepts, not event-specific values, IDs or permissions.
TOPICS={
 'regulation_economy':(r'\b(?:starting money|bomb time)\b[^?.;]{0,70}\bregulation\b|\bregulation\b[^?.;]{0,70}\b(?:starting money|bomb time)\b|(?:เงินเริ่มต้น|เวลาระเบิด).{0,40}(?:รอบปกติ|ปกติ)',r'(?:initial (?:amount|money)|starting money)[^\n]{0,120}bomb time|เงินเริ่มต้น[^\n]{0,100}(?:เวลาของระเบิด|เวลาระเบิด)'),
 'overtime_configuration':(r'\bovertime\b[^?.;]{0,75}\b(?:rounds?|starting money)\b|ต่อเวลา.{0,40}(?:รอบ|เงิน)',r'\bovertime\b.{0,180}(?:\d+\s+rounds?\s+per\s+side|\bstarting money\b)|ต่อเวลา.{0,150}(?:ฝั่งละ\s*\d+\s*รอบ|เงินเริ่มต้น)'),
 'forfeit_sanctions':(r'ปรับแพ้|\bforfeits?\b|\b(?:forfeit|disqualif\w*)\b',r'ปรับแพ้|\bforfeits?\b|\bpenalt\w*.{0,40}\bloss\b|\bloss\b.{0,40}\b(?:round|match|map)\b|\bimmediate loss\b'),
 'lineup':(r'ผู้เล่นตัวจริง|ตัวสำรอง|starting players|starting roster|\bteam\b.{0,30}\b(?:must|field|have)\b|\bplayers\b.{0,45}\bteam\b',r'ผู้เล่นตัวจริง|ตัวสำรอง.{0,15}\d|starting (?:players|roster|lineup)|องค์ประกอบทีม|ทีมละ.{0,15}ผู้เล่น|team\s+(?:composition|consists)|(?:each|per)\s+team.{0,30}(?:has|must have|fields?).{0,15}\d+\s+players'),
 'format':(r'รูปแบบ|\bformat\b|\bhow many\s+(?:games?|rounds?)\b.{0,45}\b(?:matches|match|sets?|games?)\b|(?:กี่เกม|กี่รอบ).{0,20}(?:แมตช์|ต่อเกม|ต่อเซต)|(?:แมตช์|ต่อเซต).{0,20}(?:กี่เกม|กี่รอบ)',r'รูปแบบ|แข่งขันแบบ|ต่อเกม|ต่อรอบ|ผู้ชนะ|\bformat\b|\boffline\b|\bsingles\b|\brounds?\b|\bFT\d+\b'),
 'pause':(r'หยุดเกม|ขอพัก|\bpause[sd]?\b|technical pause',r'หยุดเกม|\bpauses?\b'),
 'settings':(r'ตั้งค่า|settings?|remap|ปรับปุ่ม|brightness|resolution|crosshair|ความสว่าง|ความละเอียดหน้าจอ|เป้าเล็ง',r'ตั้งค่า|settings?|remap|brightness|resolution|crosshair|ความสว่าง|ความละเอียดหน้าจอ|เป้าเล็ง'),
 'macro':(r'มาโคร|\bmacros?\b',r'มาโคร|\bmacros?\b'),
 'install':(r'ติดตั้ง|\binstall(?:ation|ing|ed)?\b',r'ติดตั้ง|\binstall(?:ation|ing|ed)?\b'),
 'watch_stream':(r'ดูสตรีม|\bwatch(?:ing)?\b.{0,25}\bstream|\blive streams?\b',r'ดูสตรีม|\bwatch(?:ing)?\b.{0,30}\bstream'),
 'bug':(r'ใช้บั[ค๊ก]|บั[ค๊ก].*แผนที่|\b(?:bugs?|exploits?)\b',r'บั[ค๊ก]|\b(?:bugs?|exploits?)\b'),
 'protest':(r'ประท้วง|ข้อพิพาท|\bprotest|\bappeal|\bdisputes?\b',r'ประท้วง|ข้อพิพาท|อำนาจตัดสิน|\bprotest|\bappeal|\bdisputes?\b|\bobjections?\b|judging authority|authority of judgment|decisions.{0,40}referees?'),
 'personal_equipment':(r'อุปกรณ์.*(?:ตัวเอง|ส่วนตัว|เข้าแข่ง)|(?:own|personal).{0,35}(?:equipment|devices|keyboard|mouse)|อุปกรณ์ของ|นำ.*(?:คีย์บอร์ด|เมาส์)|bring.{0,35}(?:equipment|devices|keyboard|mouse)',r'อุปกรณ์|คีย์บอร์ด|เมาส์|headphones?|keyboards?|\bmice\b|\bmouse\b|devices'),
 'equipment_responsibility':(r'ใคร.*(?:รับผิดชอบ|พร้อม)|responsib|quality|readiness|คุณภาพ|ความพร้อม',r'รับผิดชอบ|responsib|quality|readiness|คุณภาพ|ความพร้อม'),
 'food':(r'อาหาร|เครื่องดื่ม|กิน|\b(?:food|drinks?|eating|water|gum)\b',r'อาหาร|เครื่องดื่ม|น้ำดื่ม|หมากฝรั่ง|\b(?:food|drinks?|water|gum)\b'),
 'preparation':(r'เตรียม.*(?:แข่ง|แมตช์)|ช่วงเตรียมตัว|Match\s*Prep|match preparation|prep room|\bplayers\b.{0,30}\bprepare\b',r'เตรียม.*(?:แข่ง|แมตช์)|ช่วงเตรียมตัว|Match\s*Prep|match preparation|during preparation|prep room'),
}

def topic_matches(topic,text,asked=False):
 text=norm(text)
 if topic=='settings':
  # Resolution of a dispute is a legal/procedural sense, not a display field.
  # Mask that phrase in BOTH the customer request and source candidates.
  text=re.sub(r'\bdisputes?\s+resolution\b|\bresolution\s+(?:of|for)\s+(?:disputes?|protests?|appeals?)\b',' ',text,flags=re.I)
 return bool(re.search(TOPICS[topic][0 if asked else 1],text,re.I))

def requested_topics(question):
 return [name for name in TOPICS if topic_matches(name,question,asked=True)]

def format_quantity_kind(question):
 if re.search(r'how many\s+games?\b|กี่เกม',question,re.I):return 'games_per_match'
 if re.search(r'how many\s+rounds?\b|กี่รอบ',question,re.I):return 'rounds_per_game'
 return None

def has_format_quantity(text,kind):
 if kind=='games_per_match':return bool(re.search(r'\b(?:FT|BO)\d+\b|best[- ]of[- ]\d|\b(?:win|wins|winning)\s+\d+\s+games?\b|ชนะ\s*\d+\s*เกม',text,re.I))
 if kind=='rounds_per_game':return bool(re.search(r'\bR\d+\b|\d+\s+rounds?\s+per\s+game|\d+\s*รอบต่อเกม',text,re.I))
 return True

TOPIC_LABELS={
 'regulation_economy':('เงินเริ่มต้นและเวลาระเบิดรอบปกติ','regulation starting money and bomb time'),
 'overtime_configuration':('การตั้งค่าช่วงต่อเวลา','overtime configuration'),
 'forfeit_sanctions':('เงื่อนไขการปรับแพ้','forfeit conditions'),
 'format':('รูปแบบการแข่งขัน','competition format'),'pause':('การหยุดเกม','pauses'),
 'settings':('การตั้งค่า','settings'),'macro':('การใช้มาโคร','macro use'),
 'install':('การติดตั้งโปรแกรม','program installation'),'watch_stream':('การดูสตรีม','watching streams'),
 'bug':('การใช้บัค','bug use'),'protest':('การประท้วง','protests'),
 'personal_equipment':('อุปกรณ์ส่วนตัว','personal equipment'),
 'equipment_responsibility':('ความรับผิดชอบต่ออุปกรณ์','equipment responsibility'),
 'food':('อาหารและเครื่องดื่ม','food and drinks'),'preparation':('การเตรียมแข่ง','match preparation'),
 'lineup':('ผู้เล่นตัวจริงและสำรอง','starting players and substitutes'),
}

def substantive(text,labels=()):
 """A heading can itself be a complete rule; its equality is not a rejection."""
 text=str(text).strip()
 if not text:return False
 # Predicates, conditions, prohibitions and numerical bounds provide substance.
 predicate=r'(?:ห้าม|ต้อง|สามารถ|อนุญาต(?:ให้|เฉพาะ)|หาก|ถ้า|ผู้ชนะ|แข่งขันแบบ|ใช้เครื่อง).{3,}|(?:ทีมละ|ครั้งละ|ไม่เกิน|อย่างน้อย)\s*\d|\b(?:must|shall|may|can|cannot)\s+\w+|\b(?:is|are)\s+(?:prohibited|permitted|allowed|forbidden|used)|\b(?:unless|no more than|per team|winner|singles|offline competition)\b'
 if re.search(predicate,text,re.I):return True
 # A heading can be the complete numeric overtime clause itself. Preserve
 # source text and conditions; this detects substance, not source authority.
 if re.search(r'\d+\s+rounds?\s+per\s+side|ฝั่งละ\s*\d+\s*รอบ',text,re.I):return True
 if re.search(r'ประกอบด้วย.{0,25}ผู้เล่น\s*\d|\b(?:each|per)\s+team\s+(?:consists of|has|fields?)\s+\d+\s+(?:starting\s+)?players',text,re.I):return True
 if len(text.split())>=5 and re.search(r'\b(?:prohibited|forbidden)\b',text,re.I):return True
 # A labelled body is useful only when it contains content beyond an overview.
 if text.casefold() in {str(s).strip().casefold() for s in labels}:return False
 if re.search(r'ภาพรวมเอกสาร|Overview of Documents', ' '.join(str(s) for s in labels),re.I):return False
 return bool(re.search(r'[.:]\s*\S|[\n*•]',text)) and len(text.split())>=4

def select_topics(index,question,pool):
 topics=requested_topics(question)
 if not topics:return None
 primary=[f for f in pool if f.get('facet')=='rule_clause' and (f.get('event_id') or index.records.get(f['record_id'],{}).get('kind')=='competition_rule')]
 selected=[];covered=[];fragment_selections=[];heading_body_mismatches=[]
 for topic in topics:
  pattern=TOPICS[topic][1]
  matches=[]
  for f in primary:
   topic_label=any(topic_matches(topic,s) for s in f['label'].values())
   topic_body=any(topic_matches(topic,s) for s in f['value'].values())
   distinct_body=any(s.strip() and s.strip().casefold() not in {label.strip().casefold() for label in f['label'].values()} for s in f['value'].values())
   if (topic_body or topic_label) and any(substantive(s,f['label'].values()) for s in f['value'].values()):matches.append(f)
  if topic=='format':
   quantity_kind=format_quantity_kind(question)
   if quantity_kind:matches=[f for f in matches if any(has_format_quantity(s,quantity_kind) for s in f['value'].values())]
  # Prefer the complete typed clause only when it literally contains both a
  # legacy fragment's heading and its body in the same event/game scope.
  # This is containment, not supersession or inferred policy equivalence.
  direct_typed=[f for f in matches if index.records.get(f['record_id'],{}).get('kind')=='competition_rule' and any(topic_matches(topic,s) for s in f['value'].values())]
  if direct_typed:
   # Imported headings can be attached to the following, unrelated paragraph.
   # A matching heading alone cannot compete with a complete typed clause whose
   # BODY addresses the requested topic. Keep the source issue in diagnostics.
   unrelated=[f for f in matches if not any(topic_matches(topic,s) for s in f['value'].values())]
   heading_body_mismatches.extend(f['id'] for f in unrelated)
   matches=[f for f in matches if f not in unrelated]
  resolved=[]
  for f in matches:
   parents=[]
   if index.records.get(f['record_id'],{}).get('kind')!='competition_rule':
    langs=['th'] if f.get('english_translation_missing') else ['th','en']
    for parent in matches:
     if index.records.get(parent['record_id'],{}).get('kind')!='competition_rule' or parent.get('event_id')!=f.get('event_id') or parent.get('game_id')!=f.get('game_id'):continue
     def body(text):return norm(re.sub(r'^\s*\d+[.)]\s*','',text))
     # Selecting a complete body that literally contains a source fragment is
     # not deduplication or authority supersession. Do not suppress fragments
     # with an extra recorded condition/exception or a translated disagreement.
     keys=['conditions_all','exceptions','preconditions','scope_note']
     from .projection import value as source_value
     from .authority_resolution import semantic_scope_note
     old=index.records.get(f['record_id'],{});new=index.records.get(parent['record_id'],{})
     def scope_val(record,key):
      if key!='scope_note':return source_value(record,key)
      field=semantic_scope_note(record)
      return field.get('value') if field and field.get('status')=='known' else None
     extra_condition=any(scope_val(old,k) is not None and scope_val(old,k)!=scope_val(new,k) for k in keys)
     if not extra_condition and all(body(f['value'].get(l,'')) and body(f['value'].get(l,'')) in body(parent['value'].get(l,'')) for l in langs):parents.append(parent)
   if parents:fragment_selections.append({'fragment_fact_id':f['id'],'selected_complete_fact_ids':[p['id'] for p in parents],'basis':'literal_fragment_containment_same_event_game','global_equivalence_or_supersession_claimed':False,'translation_missing':bool(f.get('english_translation_missing'))})
   resolved.extend(parents or [f])
  matches=list({f['id']:f for f in resolved}.values())
  # Prefer a heading about this topic, but a full labelled list remains source
  # evidence when an edition stores all its rules in one complete clause.
  headed=[f for f in matches if any(topic_matches(topic,s) for s in f['label'].values())]
  chosen=headed or matches
  if topic=='format' and matches:
   explicit=[f for f in matches if any(re.search(r'รูปแบบ|\bformat\b|\bFT\d+\b',s,re.I) for s in f['label'].values()) or any(re.search(r'(?:^|\n)\s*(?:\*\s*)?(?:รูปแบบการแข่งขัน|competition format|format)\s*[:：]',s,re.I) for s in f['value'].values())]
   if explicit:chosen=explicit
  if chosen:
   covered.append(topic);selected.extend(chosen)
 return {'facts':list({f['id']:f for f in selected}.values()),'requested':topics,'covered':covered,'missing':[t for t in topics if t not in covered],
         'source_fragment_selections':fragment_selections,'source_heading_body_mismatches':sorted(set(heading_body_mismatches))}

def explicit_competition(question,index=None):
 if re.search(r'กฎศูนย์|กติกาศูนย์|studio rules',question,re.I):return False
 if index is not None and re.search(r'\bplayers\b.{0,45}\bteam\b',question,re.I) and index.bind('C04',question):return True
 if re.search(r'แข่ง|tourn[a-z]*|competition|rulebook|\bmatch\b|starting players|\bteam\b.{0,30}\b(?:must|field)\b|\bmap\s*pool\b',question,re.I):return True
 if index is None or not re.search(r'กติกา|\brules?\b|\bplayers\b.{0,45}\bteam\b',question,re.I):return False
 if index.bind('C13',question):return True
 # Imported rule subjects can lack the game's aliases. An explicit typed
 # game/event relation supplies that binding, without using rule body guesses.
 from .projection import title,value
 from .scope import contains
 games={rid for rid,r in index.records.items() if r.get('kind')=='game' and any(contains(question,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])])}
 return any(r.get('kind')=='competition' and value(r,'game_id') in games for r in index.records.values())
