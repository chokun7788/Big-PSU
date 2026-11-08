"""Declarative, optional task/subject/scope selection. Facts stay in records."""
import re
from .query_contract import normalize,matches
from .registry import value

KINDS={'faq','policy','procedure'}
DEFAULT_FIELDS={'faq':['answer','scope_note'],'policy':['decision','details','conditions_all','exceptions','consequence'],'procedure':['steps','preconditions','required_documents']}
def tasks(question):
 q=normalize(question);found=set()
 # "The correct format" describes a property; "correct my record" is an
 # action. A positive adjective must not activate a correction procedure.
 error=bool(re.search(r'ผิด|แก้|\b(?:wrong|incorrect|mistak\w*|correction|correcting)\b',q))
 correct_verb=bool(re.search(r'^correct\b|\b(?:to|please|i|we|you)\s+correct\b|\bcorrect\s+(?:it|them|my|our|this|that)\b',q))
 if error or correct_verb:found.add('correction')
 permission=bool(re.search(r'อนุญาต|ห้าม|\b(?:allowed|permitted|permission)\b|\b(?:can|may|could) i\s+(?:bring|use)\b',q)) or bool(re.search(r'ใช้|นำ|เอา',q) and re.search(r'ได้ไหม|ได้มั้ย|ได้หรือเปล่า',q))
 if permission and not re.search(r'ซื้อ|ขาย|ซ่อม|เช่า|\b(?:buy|sell|repair|rent)\b',q):found.add('permission')
 return found
def phrase_match(question,term):
 # Standard English inflections only; Thai marks/numbers stay unchanged.
 if not term:return False
 if matches(question,term):return True
 if normalize(term)=='mouse':return matches(question,'mice')
 return False
def select(question,records):
 q=normalize(question);wanted=tasks(q)
 if not wanted:return None,{'method':'declared_question_profile','reason':'no_supported_task','candidate_ids':[]}
 competition=bool(re.search(r'แข่ง|กติกา|\b(?:competition|tournament|rulebook)\b',q))
 personal=bool(re.search(r'ส่วนตัว|ตัวเอง|ของผม|ของฉัน|\b(?:own|personal|mine)\b',q))
 studio_owned=bool(re.search(r'ของศูนย์|\b(?:studio|center|venue)(?:.s)?\s+(?:keyboard|mouse|equipment)\b',q))
 candidates=[];rejected=[]
 for rid,r in records.items():
  profile=value(r,'query_profile')
  if r['kind'] not in KINDS or not isinstance(profile,dict) or profile.get('task') not in wanted:continue
  if competition!=(profile.get('context')=='competition'):continue
  from .correction_scope import compatible
  if not compatible(question,profile):continue
  subjects=[s for s in profile.get('subjects',[]) if any(phrase_match(q,term) for term in s.values() if isinstance(term,str))]
  if not subjects:continue
  my_subject=any(re.search(r'\bmy\s+(?:own\s+|personal\s+|gaming\s+|wireless\s+)*'+re.escape(normalize(s.get('en','')))+r'(?:s)?\b',q) for s in subjects if s.get('en'))
  if profile.get('ownership')=='personal' and (studio_owned or not (personal or my_subject)):continue
  # Do not answer unknown coordinated objects from a matched first object.
  clauses=[c.strip() for c in re.split(r'และ|กับ|\band\b',q) if c.strip()]
  extra=[c for c in clauses[1:] if not any(phrase_match(c,term) for subject in profile['subjects'] for term in subject.values() if isinstance(term,str))]
  if extra:
   rejected.append({'record_id':rid,'reason':'uncovered_coordinated_subject','uncovered_spans':extra});continue
  candidates.append({'record_id':rid,'task':profile['task'],'matched_subjects':subjects,'ownership':profile['ownership'],'context':profile['context']})
 audit={'method':'declared_question_profile','candidate_ids':[x['record_id'] for x in candidates],'matches':candidates,'rejected':rejected,'human_intent_correctness_verified':False}
 if len(candidates)!=1:
  return None,{**audit,'reason':'ambiguous_profiles' if candidates else 'no_matching_profile'}
 return candidates[0]['record_id'],{**audit,'reason':'unique_declared_task_subject_scope'}

def composed_parts(question,records):
 """Only independently requested tasks; don't split noun coordinations."""
 from .query_contract import semantic_clauses
 from .request_roles import analyze
 from .unconfirmed_request import topic
 clauses=semantic_clauses(question)
 if not 2<=len(clauses)<=4:return []
 topics=[topic(c) for c in clauses]
 if all(topics) and len(set(topics))==1:return []
 tagged=[bool(analyze(c) or topic(c) or select(c,records)[0]) for c in clauses]
 return clauses if all(tagged) else []
