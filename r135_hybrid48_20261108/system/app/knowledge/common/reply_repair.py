"""Parse a rejected suggestion plus replacement query without inventing context.

Return raw substrings. Negation, quantities, names and dates in the replacement
are retained; routing/answer facts are never taken from assistant prose.
"""
import re

SEPARATORS=' \t\r\n,;:!?…。．.!—–-'
HEADER=re.compile(r'^\s*(?:(?P<en>none of these|not that|nope|no)(?=$|[,;:!?.—–\-\n]|\s+(?:i\s+mean(?:t)?\b|i[’\x27]m\s+asking\b|i\s+am\s+asking\b|what\s+i\s+mean\b))|(?P<th>ไม่ใช่(?:อันนี้|เรื่องนี้|หัวข้อนี้)?(?:ครับ|ค่ะ)?|ไม่มีในนี้)(?=$|[\s,;:!?.—–\-]|หมายถึง|ผมหมายถึง|ฉันหมายถึง|อยากถาม|ขอถาม)|ไม่เอา(?=$))',re.I)
FRAMING=re.compile(r'^(?:(?:(?:ผม|ฉัน|เรา)\s*)?หมายถึง|อยาก(?:ถาม|รู้)(?:เรื่อง)?|ขอถาม(?:เรื่อง)?|i\s+mean(?:t)?\b|what\s+i\s+mean\s+is\b|i(?:[’\x27]m|\s+am)\s+asking(?:\s+about)?\b)\s*[,;:—–\-]?\s*',re.I)

def rejection(question):
    if not isinstance(question,str):return None
    m=HEADER.match(question)
    if not m:return None
    tail=question[m.end():].lstrip(SEPARATORS)
    wrapper=FRAMING.match(tail)
    if wrapper:tail=tail[wrapper.end():].lstrip(SEPARATORS)
    # Keep sentence-ending question marks and all interior characters intact.
    tail=tail.strip()
    if not tail.strip(SEPARATORS) or len(tail.strip(SEPARATORS))<3:
        return {'replacement':None,'reason':'rejection_without_new_query'}
    return {'replacement':tail,'reason':'explicit_replacement_after_rejection'}

def declined_from_history(history):
    for turn in reversed((history or [])[-8:]):
        if not isinstance(turn,dict) or turn.get('role')!='assistant':continue
        if turn.get('delivery_status') not in {'server_written','client_acknowledged'}:return set()
        state=turn.get('common_read_state')
        if not isinstance(state,dict) or state.get('schema_version')!=1:return set()
        ids=state.get('declined_profile_ids',[])
        if not isinstance(ids,list) or len(ids)>2000 or any(not isinstance(x,str) for x in ids):return set()
        return set(ids)
    return set()

def barrier(record_ids):
    return [{'role':'assistant','delivery_status':'server_written','common_read_state':{
        'schema_version':1,'record_ids':[],'requested_fields':[],'profile_confirmation_closed':True,
        'declined_profile_ids':sorted(record_ids)}}]
