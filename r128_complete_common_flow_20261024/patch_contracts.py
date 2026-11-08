from pathlib import Path
R=Path(__file__).resolve().parent;D=R/'system/app/knowledge/common/domain_flow'
def edit(name,old,new):
 p=D/name;s=p.read_text('utf8');assert old in s,(name,old[:75]);p.write_text(s.replace(old,new,1),'utf8')
edit('date_context.py',"    if not service_date_question(q):return None", """    if not service_date_question(q):return None
    from .temporal import parse as parse_extra
    target,basis=parse_extra(q,base)
    if target is not None:return _resolved(question,target,basis,base)
    if basis=='invalid':return {'status':'clarification','reason':'invalid_explicit_date','prompt':{'th':'วันที่ระบุไม่ถูกต้องครับ กรุณาระบุวัน เดือน และปีอีกครั้ง','en':'That date is invalid. Please specify the day, month and year again.'}}""")
# English-only months are valid clarification replies as well.
edit('date_context.py',"    if not re.fullmatch(r'(?:เดือน)?", """    from .temporal import MONTHS
    english=re.fullmatch(r'('+'|'.join(MONTHS)+r')\\.?(?:\\s+(20\\d{2}))?',clean,re.I)
    if english:return (int(english[2]) if english[2] else base.year,MONTHS[english[1].lower()])
    if not re.fullmatch(r'(?:เดือน)?""")
# A target obligation is independent of field/list evidence receipts.
edit('obligation_verifier.py',"    if task.capability['operation']=='compare_durations' and claims:", """    from .dialogue_task import platforms
    expected_platforms=platforms(index,question) if task.category in {'C04','C06'} else []
    if len(expected_platforms)>1:
        for platform in expected_platforms:
            expected={f['record_id'] for f in index.bind(task.category,platform)}
            delivered={c['record_id'] for c in claims}
            if task.category=='C06':
                from .financial import rate_pool
                expected={f['record_id'] for f in rate_pool(index,platform)}
            fulfilled=bool(expected&delivered)
            obligations.append({'id':task.id+':target:'+platform,'kind':'explicit_target','expected':platform,'fulfilled':fulfilled,'reason':None if fulfilled else 'explicit_target_not_delivered','claim_refs':[c['fact_id'] for c in claims if c['record_id'] in expected]})
    if task.category=='C05' and claims and metadata.get('action_pattern'):
        pattern=metadata['action_pattern']
        fulfilled=all(re.search(pattern,' '.join([*index.byid[c['fact_id']]['label'].values(),*index.byid[c['fact_id']]['value'].values()]),re.I) for c in claims)
        obligations.append({'id':task.id+':action','kind':'requested_action','fulfilled':fulfilled,'reason':None if fulfilled else 'requested_action_not_delivered','claim_refs':[c['fact_id'] for c in claims]})
    if task.capability['operation']=='compare_durations' and claims:""")
# Action-family proofs are checked independently against native facts.
edit('obligation_verifier.py',"                elif metadata.get('operator')=='list':", """                elif metadata.get('operator')=='action_to_button':
                    from .source_operations import control_action
                    source_projection=control_action(index,question,index.bind('C05',question))
                    if source_projection and {c['fact_id'] for c in claims}<={*source_projection.ids}:acceptable.update(c['facet'] for c in claims)
                elif metadata.get('operator')=='list':""")
edit('engine.py',"        return {'answer':'\\n'.join(blocks),'status':status", """        if plan.metadata.get('procedure_steps') and len(selected)==1:
            from .source_operations import procedure_rows
            steps=procedure_rows(selected[0]['value'][lang])
            if steps:blocks=[('ขั้นตอนการจอง' if lang=='th' else 'Booking steps')]+[str(i)+'. '+line for i,line in enumerate(steps,1)]+['[S1]']
        return {'answer':'\\n'.join(blocks),'status':status""")
# Cache interpretation only while the exact source index survives; no answer facts cached.
p=D/'understanding.py';s=p.read_text('utf8');s+='''

# R128 cache identity includes the pinned index object and canonical resolved input.
import weakref,threading,copy
_INTERPRET_CACHE=weakref.WeakKeyDictionary()
_INTERPRET_LOCK=threading.RLock()
_interpret_uncached=interpret
def interpret(question,budget,allow_llm=True,transport=None,index=None):
    if index is None or transport is not None:return _interpret_uncached(question,budget,allow_llm,transport,index)
    key=(question,os.getenv('PSU_CHATBOT_OLLAMA_MODEL') or MODEL,bool(allow_llm))
    with _INTERPRET_LOCK:
        hit=_INTERPRET_CACHE.get(index,{}).get(key)
        if hit is not None:
            result=copy.deepcopy(hit);result.event={'method':'r128_index_bound_interpretation_cache','cache_hit':True,'http_attempted':False,'model_called':False,'original_reason':result.reason}
            return result
    result=_interpret_uncached(question,budget,allow_llm,transport,index)
    if result.accepted:
        with _INTERPRET_LOCK:
            cache=_INTERPRET_CACHE.setdefault(index,{})
            if len(cache)>=256:cache.pop(next(iter(cache)))
            cache[key]=copy.deepcopy(result)
    return result
''';p.write_text(s,'utf8')
print('Contracts patched')
