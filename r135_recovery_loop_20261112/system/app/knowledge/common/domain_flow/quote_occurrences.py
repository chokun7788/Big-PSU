"""Resolve exact task-quote occurrences without silently picking the first.

Whole repeated needs can be assigned in order when every semantic task family
has exactly one member per occurrence. Other repeated substrings stay ambiguous.
This is offset provenance, not proof of the task's intent or source authority.
"""
import collections,json

VERSION='whole-need-quote-occurrences-v1'

def task_quote_spans(question,tasks,index=None):
    from .routing import need_spans
    boundaries=need_spans(question,index)
    get=lambda task,key,default='':task.get(key,default) if isinstance(task,dict) else getattr(task,key,default)
    groups=collections.defaultdict(list)
    for n,task in enumerate(tasks):groups[get(task,'quote')].append(n)
    result=[None]*len(tasks)
    for quote,indices in groups.items():
        if not quote:continue
        occurrences=[];start=0
        while len(occurrences)<=32:
            pos=question.find(quote,start)
            if pos<0:break
            occurrences.append({'start':pos,'end':pos+len(quote),'text':quote});start=pos+1
        if not occurrences:continue
        if len(occurrences)==1:
            for n in indices:result[n]={**occurrences[0],'basis':'unique_exact_quote','ambiguous':False}
            continue
        full=[p for p in boundaries if p['text']==quote]
        families=collections.defaultdict(list)
        for n in indices:
            signature=tuple(get(tasks[n],k) for k in ['domain','category','operation','facet','target','canonical_operation'])
            signature+= (json.dumps(get(tasks[n],'constraints',[]),sort_keys=True,ensure_ascii=False),)
            families[signature].append(n)
        if len(full)==len(occurrences) and all(len(ns)==len(full) for ns in families.values()):
            for ns in families.values():
                for n,p in zip(ns,full):result[n]={**p,'basis':'ordered_repeated_whole_need','ambiguous':False}
        else:
            for n in indices:result[n]={**occurrences[0],'basis':'unresolved_repeated_quote','ambiguous':True,'candidate_count':len(occurrences)}
    return result
