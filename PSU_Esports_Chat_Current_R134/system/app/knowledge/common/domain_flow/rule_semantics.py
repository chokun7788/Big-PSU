"""Language topics and normative-clause checks; all rule values remain source data."""
import re
from .scope import norm

# These are linguistic concepts, not event-specific values, IDs or permissions.
TOPICS={
 'lineup':(r'ผู้เล่นตัวจริง|ตัวสำรอง|starting players|starting roster|\bteam\b.{0,30}\b(?:must|field|have)\b|\bplayers\b.{0,45}\bteam\b',r'ผู้เล่นตัวจริง|ตัวสำรอง.{0,15}\d|starting (?:players|roster|lineup)|องค์ประกอบทีม|ทีมละ.{0,15}ผู้เล่น|team\s+(?:composition|consists)|(?:each|per)\s+team.{0,30}(?:has|must have|fields?).{0,15}\d+\s+players'),
 'format':(r'รูปแบบ|\bformat\b',r'รูปแบบ|แข่งขันแบบ|ต่อเกม|ต่อรอบ|ผู้ชนะ|\bformat\b|\boffline\b|\bsingles\b|\brounds?\b|\bFT\d+\b'),
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

TOPIC_LABELS={
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
 selected=[];covered=[]
 for topic in topics:
  pattern=TOPICS[topic][1]
  matches=[]
  for f in primary:
   topic_label=any(topic_matches(topic,s) for s in f['label'].values())
   topic_body=any(topic_matches(topic,s) for s in f['value'].values())
   distinct_body=any(s.strip() and s.strip().casefold() not in {label.strip().casefold() for label in f['label'].values()} for s in f['value'].values())
   if (topic_body or topic_label) and any(substantive(s,f['label'].values()) for s in f['value'].values()):matches.append(f)
  # Prefer the complete typed clause only when it literally contains both a
  # legacy fragment's heading and its body in the same event/game scope.
  # This is containment, not supersession or inferred policy equivalence.
  resolved=[]
  for f in matches:
   parents=[]
   if index.records.get(f['record_id'],{}).get('kind')!='competition_rule':
    langs=['th'] if f.get('english_translation_missing') else ['th','en']
    for parent in matches:
     if index.records.get(parent['record_id'],{}).get('kind')!='competition_rule' or parent.get('event_id')!=f.get('event_id') or parent.get('game_id')!=f.get('game_id'):continue
     if all(norm(f['value'].get(l,'')) in norm(parent['value'].get(l,'')) and norm(f['label'].get(l,'')) in norm(parent['value'].get(l,'')) for l in langs):parents.append(parent)
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
 return {'facts':list({f['id']:f for f in selected}.values()),'requested':topics,'covered':covered,'missing':[t for t in topics if t not in covered]}

def explicit_competition(question,index=None):
 if re.search(r'กฎศูนย์|กติกาศูนย์|studio rules',question,re.I):return False
 if index is not None and re.search(r'\bplayers\b.{0,45}\bteam\b',question,re.I) and index.bind('C04',question):return True
 return bool(re.search(r'แข่ง|tourn[a-z]*|competition|rulebook|\bmatch\b|starting players|\bteam\b.{0,30}\b(?:must|field)\b',question,re.I)) or bool(index is not None and re.search(r'กติกา|\brules?\b|\bplayers\b.{0,45}\bteam\b',question,re.I) and index.bind('C13',question))
