"""Shared concepts select source intents; neither prices nor policy values live here.

Missing/ambiguous concepts fall through to the established reader. It never
uses refusal templates as affirmative knowledge or reads arbitrary regexes.
"""
import re
from .registry import value
from .query_contract import normalize
CONCEPTS={
 'food':r'อาหาร|ข้าว|ขนม|\b(?:food|snacks?|meals?|eat|eating)\b',
 'drink':r'เครื่องดื่ม|น้ำดื่ม|\b(?:drinks?|beverages?)\b',
 'afternoon':r'รอบบ่าย|ช่วงบ่าย|ภาคบ่าย|\bafternoon\b',
 'morning':r'รอบเช้า|ช่วงเช้า|ภาคเช้า|\bmorning\b',
 'noise':r'เสียงดัง|\bnoise\b',
 'damage':r'เสียหาย|ทำ.*พัง|\bdamage\b'}
def select(question,records,operation):
 q=normalize(question)
 if operation in {'rules','controls','price','rental','games','game_presence'}:return []
 # The source's weekly definition does not prove today's real-time opening.
 dynamic=bool(re.search(r'วันนี้|พรุ่งนี้|ตอนนี้|\b(?:today|tomorrow|now|currently)\b|20\d\d-\d\d-\d\d',q))
 concepts={k for k,p in CONCEPTS.items() if re.search(p,q)}
 schedule=concepts&{'afternoon','morning'}
 if schedule:
  if dynamic or len(schedule)!=1:return []
  key='schedule_'+next(iter(schedule))+'_time'
  return [rid for rid,r in records.items() if r['kind']=='faq' and value(r,'intent_key')==key]
 if not concepts&{'food','drink'}:return []
 # Food-sale/delivery questions do not establish permission to consume food.
 if re.search(r'บุฟเฟต์|ส่งอาหาร|ขาย|ซื้อ|\b(?:sell|buy|buffet|delivery|menu|price)\b',q):return []
 candidates=[]
 for rid,r in records.items():
  if r['kind']!='faq':continue
  intent=value(r,'intent_key') or '';tokens=set(intent.split('_'))
  supported=tokens&set(CONCEPTS)
  if not supported&{'food','drink'}:continue
  if supported-{'food','drink'}-concepts:continue
  score=len(supported&concepts)
  candidates.append((score,-len(supported),rid))
 if not candidates:return []
 best=max((a,b) for a,b,_ in candidates)
 return [rid for a,b,rid in candidates if (a,b)==best]
