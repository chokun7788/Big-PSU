"""Observable teacher behaviors, never teacher business answers or test keys."""
import json,math,os,re
from functools import lru_cache
from pathlib import Path

def tokens(s):
 s=s.casefold();words=re.findall(r'[a-z0-9]+|[\u0e00-\u0e7f]+',s)
 return set(words+['~'+s[i:i+3] for i in range(max(0,len(s)-2)) if ' ' not in s[i:i+3]])

@lru_cache(maxsize=1)
def lessons():
 p=Path(__file__).with_name('teacher_lessons.json')
 raw=json.loads(p.read_text('utf8'))
 if raw.get('business_answers_included') is not False:raise ValueError('Teacher examples cannot supply business answers')
 return raw

def demonstrations(question,limit=2):
 if os.getenv('PSU_TEACHER_DEMONSTRATIONS','1')!='1':return []
 qt=tokens(question);ranked=[]
 for e in lessons()['examples']:
  et=tokens(e['question']);score=len(qt&et)/math.sqrt(max(1,len(qt))*max(1,len(et)))
  if score>=.12:ranked.append((score,e))
 ranked.sort(key=lambda x:(-x[0],x[1]['id']))
 return [{'example_id':e['id'],'example_question':e['question'],'task_plan':e['plan'],'transfer':'task structure only; all quotes and slots must come from the new customer request'} for _,e in ranked[:limit]]

def normalize_tasks(raw):
 # Empty general placeholders carry no customer need. Other malformed tasks
 # still fail the normal parser instead of being silently discarded.
 if not isinstance(raw,list):return raw
 filtered=[t for t in raw if not (isinstance(t,dict) and t.get('domain')=='general' and t.get('quote')=='' and t.get('target')=='' and t.get('constraints')==[] and t.get('facet')=='' and t.get('operation')=='unknown')]
 return filtered or raw

def retain_context(question,result,index):
 if not result.accepted or len(result.tasks)!=1:return result
 from .routing import split_needs
 if len(split_needs(question,index))!=1:return result
 task=result.tasks[0]
 if task.quote!=question:
  result.event.setdefault('distilled_context',{})['prior_quote']=task.quote
  task.quote=question
  result.event['distilled_context']['basis']='whole single need retains the source-quoted game, event and conditions'
 return result

def requested_frame(question,index):
 # The teacher's structured price path separates the price operation from a
 # mentioned game. Only current native service/rate relations authorize it.
 from .financial import rate_pool
 price=bool(re.search(r'ราคา|กี่บาท|ค่าบริการ|ค่าเล่น|how much|\b(?:costs?|prices?|fees?)\b',question,re.I))
 other=re.search(r'ซ่อม|เสียหาย|ค่าปรับ|คืนเงิน|เหมา|repair|damage|penalt|refund|rental|deposit',question,re.I)
 if price and not other and rate_pool(index,question):return ('service_fee','C06','price_calculate','amount')
 return None

def broad_rule_family(index,question,pool):
 if not re.search(r'บทลงโทษ|penalt(?:y|ies)|punishments?|sanctions?',question,re.I):return None
 if re.search(r'ถ้า|กรณี|\bif\b|\bwhen\b|โกง|cheat|pause|บั๊ก|\bbug\b',question,re.I):return None
 from .projection import value
 from .readers import confirmed
 primary=[f for f in pool if index.records.get(f['record_id'],{}).get('kind')=='competition_rule']
 parents=[]
 for f in primary:
  source_heading=(value(index.records[f['record_id']],'heading') or {}).get('th','')
  if re.match(r'^\s*\d+[.)]\s',source_heading):continue
  if re.search(r'บทลงโทษ|penalt(?:y|ies)|punishments?|sanctions?',source_heading,re.I):parents.append(f)
 if not parents:return None
 events={f.get('event_id') for f in parents}
 if len(events)!=1:return None
 thai=bool(re.search('[\u0e00-\u0e7f]',question))
 def original_thai(f):return bool(re.search('[\u0e00-\u0e7f]',(value(index.records[f['record_id']],'heading') or {}).get('th','')))
 localized=[f for f in parents if original_thai(f)==thai] or parents
 order=lambda f:value(index.records[f['record_id']],'source_order') or 0
 parent=min(localized,key=order);selected=[parent];last=order(parent)
 sequence=sorted([f for f in primary if f.get('event_id')==parent.get('event_id') and order(f)>last],key=order)
 expected=1
 for f in sequence:
  heading=(value(index.records[f['record_id']],'heading') or {}).get('th','')
  m=re.match(r'^\s*(\d+)[.)]\s',heading)
  if not m or int(m[1])!=expected:break
  selected.append(f);expected+=1
 result=confirmed('C13',selected,'distilled_source_section_family',coverage='recorded_topic_family_only',complete_event_rulebook=False,source_family_member_count=len(selected),teacher_business_answers_used=False)
 result.locked=True;return result
