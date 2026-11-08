"""Whole-task contracts over resolved common records; no business facts.

Names come from the current snapshot. Bounded recovery covers the complete
remaining task, never just a keyword inside an unhandled condition. This is
language interpretation, not an assertion that the record's facts are current.
"""
import re
from app.core.typo_similarity import osa_distance
from .query_contract import normalize

VERSION='common-task-contract-v1'
PROFILES=(
 {'task':'game_overview','kinds':{'game'},'operation':'game_overview','fields':['summary','genre','how_to_play'],
  'phrases':('คือเกมอะไร','เป็นเกมอะไร','เกมนี้คืออะไร','what is','what is this game','what kind of game is this','what type of game is this','tell me about this game','game overview')},
 {'task':'game_how_to_play','kinds':{'game'},'operation':'game_how_to_play','fields':['how_to_play'],
  'phrases':('เล่นยังไง','เล่นอย่างไร','วิธีเล่น','how to play','how do i play','how do you play','how does this game work')},
 {'task':'equipment_list','kinds':{'zone','service','resource'},'operation':'equipment','fields':['name'],
  'phrases':('อุปกรณ์','รายการอุปกรณ์','มีอุปกรณ์อะไรบ้าง','มีอุปกรณ์อะไรมั่ง','อุปกรณ์มีอะไรบ้าง','equipment','hardware','equipment list','what equipment is there','what equipment do you have','what equipment is available','list the equipment','which equipment is available')},
 {'task':'faq_content','kinds':{'faq'},'operation':None,'fields':['answer'],
  'phrases':('นโยบายคืออะไร','นโยบายว่าอย่างไร','มีนโยบายอย่างไร','มีรายละเอียดอย่างไร','คำตอบ','what is the policy','what is the studio policy','what is the studio policy for','what is the policy for','tell me about','what is','what does the policy say','answer')},
)
def _plain(value):
 return re.sub(r'\s+',' ',re.sub(r'[—–:?!.,]+',' ',normalize(value))).strip()

def _framing(q):
 # Remove only polite framing at edges; substantive words remain visible.
 q=re.sub(r'^(?:please\s+|could you\s+|can you\s+|ช่วย|ขอ)(?=\S)', '',q)
 q=re.sub(r'(?:\s+please|ครับ|ค่ะ|คะ|หน่อย|นะครับ|นะคะ)+$','',q)
 return q.strip()

def _safe_english_edit(observed,target):
 # Valid words such as "name", "time" and "price" cannot be spelling errors
 # merely because a known task is close. Keep English error channels concrete.
 if not re.search('[a-z]',observed):return True
 from .schema_language import PROTECTED,GRAMMAR
 a=re.findall('[a-z]+',observed);b=re.findall('[a-z]+',target)
 if len(a)!=len(b):return False
 for before,after in zip(a,b):
  if before==after:continue
  if before in PROTECTED or before in GRAMMAR:return False
  if abs(len(before)-len(after))==1 and osa_distance(before,after)==1:continue
  if len(before)==len(after):
   diff=[i for i,(x,y) in enumerate(zip(before,after)) if x!=y]
   if len(diff)==2 and diff[1]==diff[0]+1 and before[diff[0]]==after[diff[1]] and before[diff[1]]==after[diff[0]]:continue
  return False
 return True

def interpret(question,record_ids,records,names=None):
 ids=list(dict.fromkeys(record_ids))
 if not ids or any(rid not in records for rid in ids):return None
 kinds={records[rid]['kind'] for rid in ids}
 original=normalize(question);q=_plain(original);subjects=[]
 # Strip only literal current labels after punctuation normalization. Never
 # rewrite a new name to an existing record or copy facts from history.
 if names:
  labels=sorted({_plain(a) for rid in ids for a in names.get(rid,[]) if isinstance(a,str)},key=len,reverse=True)
  for label in labels:
   if len(label)<3:continue
   pattern=(r'(?<![a-z0-9])'+re.escape(label)+r'(?![a-z0-9])') if re.search('[a-z]',label) else re.escape(label)
   if re.search(pattern,q):subjects.append(label);q=re.sub(pattern,' ',q)
 q=_framing(re.sub(r'\s+',' ',q).strip())
 # Preserve numbers, negation, qualification and multiple tasks. These use
 # the normal typed/LLM path; a near-match must not erase their conditions.
 if not q or re.search(r'\d|ไม่|ห้าม|ยกเว้น|เฉพาะ|ถ้า|และ|แล้ว|หรือ|\b(?:not|no|never|without|except|only|if|unless|and|or|but|before|after)\b',q):return None
 candidates=[]
 for profile in PROFILES:
  if not kinds<=profile['kinds']:continue
  # Multiple FAQ scopes cannot silently turn into one policy answer.
  if profile['task']=='faq_content' and len(ids)!=1:continue
  for phrase in profile['phrases']:
   target=_plain(phrase);distance=osa_distance(q,target)
   if distance:
    if min(len(q),len(target))<6 or abs(len(q)-len(target))>2 or distance>2:continue
    if 1-distance/max(len(q),len(target))<.72:continue
    if not _safe_english_edit(q,target):continue
   candidates.append((distance,profile,target))
 if not candidates:return None
 best=min(x[0] for x in candidates);best_rows=[x for x in candidates if x[0]==best]
 if len({x[1]['task'] for x in best_rows})!=1:return None
 _,profile,target=best_rows[0]
 # A different task within one edit of the winner remains ambiguous.
 if best and any(x[1]['task']!=profile['task'] and x[0]<=best+1 for x in candidates):return None
 fields=[f for f in profile['fields'] if profile['task']=='equipment_list' or any(f in records[rid]['fields'] for rid in ids)]
 if not fields:return None
 return {'version':VERSION,'task':profile['task'],'operation':profile['operation'],
  'record_ids':ids,'requested_fields':fields,'original_task':original,'task_span':q,
  'matched_current_labels':subjects,'canonical_task':target,'edit_distance':best,
  'whole_task_covered':True,'method':'whole_task_exact' if best==0 else 'bounded_whole_task_recovery',
  'confidence_calibrated':False,'facts_source':'current_common_snapshot'}
