"""Bounded intent-only edit channel, using the existing Thai keyboard helpers.

Scores are engineering costs, not learned probabilities or calibrated confidence.
Never infer a missing entity, quantity, polarity or business fact.
"""
from dataclasses import dataclass,asdict
from difflib import SequenceMatcher
import re
from app.core.keyboard_neighbor_recovery import detect_keyboard_neighbor_recovery,adjacent_key_substitution
from app.core.multi_error_phrase_recovery import detect_multi_error_phrase_recovery
from app.core.intent_cue_recovery import recover_intent_cue_sequence
from app.core.typo_similarity import osa_distance

VERSION='bounded-intent-edit-channel-v1'
ENTITY_KINDS={'game','equipment_model','resource','service','zone','audience','person','center','competition','rental_package','facility'}
GUARDED=re.compile(r'https?://\S+|[\w.+-]+@[\w.-]+|["“][^"”]*["”]|\d+(?:[:./-]\d+)*|ไม่|ห้าม|ยกเว้น|เฉพาะ|ก่อน|หลัง|\b(?:not|no|never|except|unless|only|before|after|without)\b',re.I)

@dataclass
class Recovery:
    original:str
    execution:str
    status:str
    candidates:list
    edits:list
    protected:list
    reason:str
    version:str=VERSION
    calibrated_confidence:bool=False
    def public(self):return asdict(self)

def protected_spans(text,records):
    spans=[{'start':m.start(),'end':m.end(),'text':m[0],'kind':'literal_constraint'} for m in GUARDED.finditer(text)]
    for r in records.values():
        if r.get('kind') not in ENTITY_KINDS:continue
        labels=sum(r.get('aliases',{}).values(),[])
        for key in ('title','name','display_name','event_name'):
            f=r.get('fields',{}).get(key,{})
            if f.get('status')=='known':
                v=f.get('value');labels+=list(v.values()) if isinstance(v,dict) else [v]
        for label in set(s for s in labels if isinstance(s,str) and len(s.strip())>=2):
            pattern=(r'(?<![a-z0-9])' if label[0].isascii() and label[0].isalnum() else '')+re.escape(label)+(r'(?![a-z0-9])' if label[-1].isascii() and label[-1].isalnum() else '')
            spans.extend({'start':m.start(),'end':m.end(),'text':m[0],'kind':'source_entity','record_id':r['record_id']} for m in re.finditer(pattern,text,re.I))
    return spans

def edits_between(raw,candidate):
    return [{'start':a,'end':b,'observed':raw[a:b],'replacement':candidate[c:d],'operation':tag}
            for tag,a,b,c,d in SequenceMatcher(None,raw,candidate,autojunk=False).get_opcodes() if tag!='equal']

def edits_allowed(edits,protected):
    for e in edits:
        for s in protected:
            if e['start']<s['end'] and s['start']<e['end']:return False
            if e['start']==e['end'] and s['start']<=e['start']<=s['end'] and e['replacement'].strip():return False
    return True

def channel_cost(a,b):
    # Weighted Damerau edits: nearby substitution and duplicate-key deletion are
    # cheaper than unrelated replacements. Includes insertion/deletion for gaps.
    d=[[0.]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)+1):d[i][0]=float(i)
    for j in range(len(b)+1):d[0][j]=float(j)
    for i,x in enumerate(a,1):
        for j,y in enumerate(b,1):
            sub=0. if x==y else .6 if adjacent_key_substitution(x,y) else 1.2
            deletion=.35 if i>1 and a[i-1]==a[i-2] else 1.
            d[i][j]=min(d[i-1][j]+deletion,d[i][j-1]+1.,d[i-1][j-1]+sub)
            if i>1 and j>1 and a[i-1]==b[j-2] and a[i-2]==b[j-1]:d[i][j]=min(d[i][j],d[i-2][j-2]+.8)
    return round(d[-1][-1],3)

def propose(text,records):
    text=str(text)
    if len(text)>240:return Recovery(text,text,'unchanged',[],[],[],'long_input_not_rewritten')
    protected=protected_spans(text,records)
    # A whole missing content word has several meanings; do not choose a domain.
    if re.fullmatch(r'\s*(?:มี|มีอะไร|มีไร)(?:อะไร)?บ้าง[?？\s]*',text):
        return Recovery(text,text,'clarify',[{'text':s} for s in ('มีเกมอะไรบ้าง','มีอุปกรณ์อะไรบ้าง','มีบริการอะไรบ้าง')],[],protected,'missing_content_word_multiple_domains')
    candidates={}
    def add(candidate,method):
        if candidate and candidate!=text:
            candidates.setdefault(candidate,set()).add(method)
    k=detect_keyboard_neighbor_recovery(text)
    if k:add(k.candidate,'kedmanee_neighbor_context')
    m=detect_multi_error_phrase_recovery(text)
    if m:add(m.candidate,'legacy_bounded_phrase_insert_delete')
    cue,steps=recover_intent_cue_sequence(text)
    if steps:add(cue,'legacy_contextual_intent_edits')
    for word in ('อะไร','บ้าง','ราคา','จอง','เกม','อุปกรณ์'):
        candidate=re.sub(re.escape(word)+r'\s*'+re.escape(word),word,text,count=1)
        if candidate!=text and re.search(r'มี.*อะไร.*บ้าง|ราคา.*เท่า|จอง.*(?:ไง|อย่างไร)',candidate):add(candidate,'repeated_intent_token_delete')
    accepted=[]
    for candidate,methods in candidates.items():
        edits=edits_between(text,candidate)
        if osa_distance(text,candidate)>4 or len(edits)>3 or not edits_allowed(edits,protected):continue
        cost=channel_cost(text,candidate)
        if cost>3.:continue
        accepted.append({'text':candidate,'methods':sorted(methods),'cost':cost,'edits':edits})
    accepted.sort(key=lambda c:(c['cost'],c['text']))
    if not accepted:return Recovery(text,text,'unchanged',[],[],protected,'no_unambiguous_safe_intent_edit')
    if len(accepted)>1 and accepted[1]['cost']-accepted[0]['cost']<.75:
        return Recovery(text,text,'clarify',accepted,[],protected,'competing_intent_candidates')
    if re.search(r'ไม่|ห้าม|ยกเว้น|\b(?:not|no|never|except|unless|without)\b',text,re.I):
        return Recovery(text,text,'clarify',accepted,[],protected,'polarity_sensitive_recovery_requires_confirmation')
    best=accepted[0]
    return Recovery(text,best['text'],'accepted',accepted,best['edits'],protected,'context_and_bounded_edit_channel')
