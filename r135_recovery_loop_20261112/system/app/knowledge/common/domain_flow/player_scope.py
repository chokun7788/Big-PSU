"""Source player bounds are a range, not a service capacity or price quantity."""
import re
from .projection import value

def count_request(index,question):
    from .named_spans import masked
    words={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'หนึ่ง':1,'สอง':2,'สาม':3,'สี่':4,'ห้า':5}
    text=masked(index,question)
    matches=list(re.finditer(r'(?<![\w.-])(-?\d+(?:\.\d+)?|'+'|'.join(words)+r')\s*(?:people\b|persons?\b|players?\b|คน)',text,re.I))
    counts=[words[m[1].casefold()] if m[1].casefold() in words else float(m[1]) for m in matches]
    error=None
    if len(set(counts))>1:error='multiple_player_counts_require_separate_roles'
    if counts and re.search(r'อย่างน้อย|ไม่เกิน|มากกว่า|น้อยกว่า|\b(?:at least|at most|more than|less than|up to|between|under|over)\b|\d+\s*[–—-]\s*\d+\s*(?:คน|people|persons?|players?)',text,re.I):error='player_count_bound_requires_clarification'
    return {'count':counts[0] if counts else None,'error':error}

def requested_count(index,question):return count_request(index,question)['count']

def selection(index,question):
    from .dialogue_task import mentions,platforms
    games=set(mentions(index,question,{'game'}));ps=set(platforms(index,question));request=count_request(index,question);count=request['count'];facts=[];proofs={}
    if request['error']:return {'facts':facts,'proofs':proofs,'requested_count':count,'error':request['error']}
    for f in index.bycat['C04']:
        if f['facet']!='players_max':continue
        r=index.records.get(f['record_id'],{});game=index.records.get(value(r,'game_id'),{})
        if r.get('kind')!='game_mode' or game.get('kind')!='game' or games and game['record_id'] not in games:continue
        if ps and not ps&set(platforms(index,str(value(r,'platform') or ''))):continue
        low,high=value(r,'players_min'),value(r,'players_max')
        if value(r,'studio_supported') is not True or type(high) is not int:continue
        if count is not None and (count<=0 or int(count)!=count or type(low) is not int or not low<=count<=high):continue
        mode=re.search(r'local|online|ออฟไลน์|ออนไลน์',question,re.I)
        if mode and not re.search(mode[0],str(value(r,'mode_name') or ''),re.I):continue
        facts.append(f);proofs[f['id']]={'fact_id':f['id'],'mode_record_id':r['record_id'],'mode_revision':r['revision'],'game_id':game['record_id'],'game_revision':game['revision'],'requested_count':count,'players_min':low,'players_max':high,'platform':value(r,'platform'),'mode_name':value(r,'mode_name'),'studio_supported':True,'evidence_refs':[ref for k in ['game_id','mode_name','platform','players_min','players_max','studio_supported'] for ref in r['fields'].get(k,{}).get('evidence_refs',[])]}
    return {'facts':facts,'proofs':proofs,'requested_count':count}
