"""Validate model routing bindings; never accept model-written facts/fields.

Quoted spans prove provenance of a routing proposal, not its semantic truth.
Equivalence is still a model judgement and needs real contrast-set evaluation.
"""
import re
from .registry import value
from .question_profiles import KINDS, tasks
from .query_contract import normalize, semantic_clauses

SYSTEM = '''For candidates with query_profile, a record may be selected only if the
whole request asks its declared task about an equivalent subject in the SAME
context and ownership. Return a profile_binding for every selected profile.
Copy task_span and each subject span verbatim from the QUESTION, never from the
candidate. subject_index indexes query_profile.subjects; equivalent means the
same object/concept, not just a related payment, document or equipment.
A wrong payment amount is different from a wrong payment image. Identity proof
is different from payment proof. Asking a document format/deadline is different
from asking the steps to correct a wrong attachment. Do not expand a profile to
answer an extra object, exception or request. Give every clause ID exactly once
with covered=true only if the profile answers that clause. Uncovered clauses,
uncertain meanings or ownership must abstain. No answers or factual values.'''

def profile(record):
    p=value(record,'query_profile')
    return p if record['kind'] in KINDS and isinstance(p,dict) else None

def extend_schema(schema,rows,records,question):
    """Only extend model protocol where a declared profile is actually present."""
    indices=[i for i,row in enumerate(rows) if profile(records[row['record_id']])]
    if not indices:return False
    clauses=semantic_clauses(question)
    binding={'type':'object','properties':{
        'index':{'type':'integer','enum':indices},
        'task':{'type':'string','enum':['permission','correction']},
        'task_span':{'type':'string','minLength':1,'maxLength':240},
        'subjects':{'type':'array','minItems':1,'maxItems':12,'items':{
            'type':'object','properties':{'subject_index':{'type':'integer','minimum':0,'maximum':11},
                'span':{'type':'string','minLength':1,'maxLength':240},
                'relation':{'type':'string','enum':['equivalent','different','uncertain']}},
            'required':['subject_index','span','relation'],'additionalProperties':False}},
        'ownership':{'type':'string','enum':['personal','studio','unspecified']},
        'context':{'type':'string','enum':['studio','competition','uncertain']},
        'clauses':{'type':'array','minItems':len(clauses),'maxItems':len(clauses),'items':{
            'type':'object','properties':{'id':{'type':'integer','enum':list(range(len(clauses)))},'covered':{'type':'boolean'}},
            'required':['id','covered'],'additionalProperties':False}}},
        'required':['index','task','task_span','subjects','ownership','context','clauses'],'additionalProperties':False}
    schema['properties']['profile_bindings']={'type':'array','maxItems':4,'items':binding}
    schema['required'].append('profile_bindings')
    return True

def quoted_span(question,span):
    # Exact input substrings only. Normalisation must not invent quote evidence.
    return isinstance(span,str) and bool(span.strip()) and len(span)<=240 and span in question

def check_binding(question,binding,index,record):
    p=profile(record);q=normalize(question)
    required={'index','task','task_span','subjects','ownership','context','clauses'}
    if not isinstance(binding,dict) or set(binding)!=required:return 'invalid_binding_shape'
    if type(binding['index']) is not int or binding['index']!=index:return 'invalid_binding_index'
    if binding['task']!=p['task'] or p['task'] not in tasks(question):return 'task_mismatch'
    if not quoted_span(question,binding['task_span']) or p['task'] not in tasks(binding['task_span']):return 'unsupported_task_span'
    competition=bool(re.search(r'แข่ง|กติกา|\b(?:competition|tournament|rulebook)\b',q))
    expected_context='competition' if competition else 'studio'
    if binding['context']!=p['context'] or binding['context']!=expected_context:return 'context_mismatch'
    if binding['ownership'] not in {'personal','studio','unspecified'}:return 'invalid_ownership'
    if p['ownership']=='personal':
        # Semantic ownership alone cannot override explicit venue ownership.
        if binding['ownership']!='personal' or not re.search(r'ส่วนตัว|ตัวเอง|ของผม|ของฉัน|\b(?:own|personal|my|mine)\b',q):return 'ownership_mismatch'
        if re.search(r'ของศูนย์|\b(?:studio|center|venue)[’\x27]?s\b',q):return 'ownership_mismatch'
    subjects=binding['subjects']
    if not isinstance(subjects,list) or not 1<=len(subjects)<=12:return 'invalid_subjects'
    seen=set()
    for subject in subjects:
        if not isinstance(subject,dict) or set(subject)!={'subject_index','span','relation'}:return 'invalid_subject_shape'
        i=subject['subject_index']
        if type(i) is not int or not 0<=i<len(p['subjects']) or i in seen:return 'invalid_subject_index'
        seen.add(i)
        if subject['relation']!='equivalent':return 'subject_not_equivalent'
        if not quoted_span(question,subject['span']):return 'unsupported_subject_span'
        # A bare grammatical word is not evidence of the subject's meaning.
        if len(normalize(subject['span']))<3 or normalize(subject['span'])==normalize(binding['task_span']):return 'uninformative_subject_span'
    clauses=binding['clauses'];expected=set(range(len(semantic_clauses(question))))
    if not isinstance(clauses,list) or len(clauses)!=len(expected):return 'missing_clause_coverage'
    if any(not isinstance(c,dict) or set(c)!={'id','covered'} or type(c['id']) is not int or type(c['covered']) is not bool for c in clauses):return 'invalid_clause_coverage'
    if {c['id'] for c in clauses}!=expected or not all(c['covered'] for c in clauses):return 'uncovered_request'
    return None

def validate_bindings(question,selected,indices,rows,records,enabled):
    """Return a projection only after all bindings passed. Rejection is atomic."""
    if not enabled:return {},None
    bindings=selected.get('profile_bindings')
    if not isinstance(bindings,list) or len(bindings)>4:return {},'invalid_profile_bindings'
    if any(not isinstance(b,dict) or type(b.get('index')) is not int for b in bindings):return {},'invalid_binding_shape'
    wanted={i for i in indices if profile(records[rows[i]['record_id']])}
    if len(bindings)!=len(wanted) or {b['index'] for b in bindings}!=wanted:return {},'missing_or_duplicate_profile_binding'
    accepted={}
    for b in bindings:
        i=b['index'];r=records[rows[i]['record_id']]
        reason=check_binding(question,b,i,r)
        if reason:return {},reason
        accepted[r['record_id']]={'record_id':r['record_id'],'revision':r['revision'],
            'binding':b,'task':profile(r)['task'],'context':profile(r)['context'],
            'meaning_basis':'model_equivalence_with_quoted_input',
            'independent_semantic_verification':False}
    # One profile is a whole-request projection, not authority for mixing in
    # another unplanned answer. Multiple interpretations require clarification.
    if accepted and len(indices)>1 and not selected['ambiguous']:return {},'mixed_or_multiple_profile_selection'
    return accepted,None
