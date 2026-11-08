"""Bounded common-only operation composition with explicit clause coverage."""
import re
from .query_contract import semantic_clauses,live_request
from .query_scope import operation

def parts(question,record_ids=None,records=None):
    if live_request(question):return []
    clauses=semantic_clauses(question)
    if not 2<=len(clauses)<=4:return []
    ops=[operation(q) for q in clauses]
    if record_ids and records:
        from .task_interpretation import interpret
        game_ids=[rid for rid in record_ids if records[rid]['kind']=='game']
        for i,clause in enumerate(clauses):
            task=interpret(clause,game_ids,records)
            if task:ops[i]=task['operation']
    # Noun coordinations (minimum and maximum, keyboard and mouse) are not tasks.
    concrete={op for op in ops if op}
    if len(concrete)<2 or concrete&{'rules'}:return []
    return clauses

def compose(reader,snap,started,clauses,ids,*,lang,history,at,planner):
    records=snap['release']['records']
    roots=[rid for rid in ids if records[rid]['kind'] not in {'faq','policy','procedure'}] or list(ids)
    context={'role':'assistant','common_read_state':{'schema_version':1,'record_ids':roots,'requested_fields':[],'all_fields':False,'release_id':snap['active']}}
    blocks=[];hits=[];obligations=[];children=[];incomplete=[]
    for i,clause in enumerate(clauses,1):
        result=reader.answer(clause,locale=lang,history=[*(history or []),context],at=at,planner=planner,_composing=True,_snapshot=snap)
        if result is None:
            children.append({'clause':clause,'response_type':'unconfirmed','need_status':'missing_fact','query_plan':None,'need_ledger':{}})
            blocks.append(str(i)+'. '+clause+'\n'+('ยังไม่มีคำตอบที่ยืนยันได้สำหรับส่วนนี้' if lang=='th' else 'No verified answer is available for this part.'));incomplete.append(i);continue
        art=result.decision_artifact or {}
        if not result.validation.ok:
            children.append({'clause':clause,'response_type':'clarification','need_status':'ambiguous','query_plan':art.get('query_plan'),'coverage_errors':art.get('coverage_errors',[]),'need_ledger':art.get('need_ledger',{})})
            blocks.append(str(i)+'. '+clause+'\n'+('ยังยืนยันคำตอบสำหรับเงื่อนไขส่วนนี้ไม่ได้ กรุณาระบุเพิ่ม' if lang=='th' else 'I cannot confirm an answer under these conditions. Please clarify this part.'));incomplete.append(i);continue
        response=art.get('response_type')
        status='answered' if response in {'answer','list'} else 'partial' if response=='partial_answer' else {'not_current':'not_current','unconfirmed':'missing_fact','clarification':'ambiguous','retry':'retry'}.get(response,'unknown')
        nested_statuses={n['status'] for n in art.get('need_ledger',{}).get('needs',[]) if n.get('status')!='answered'}
        if response=='clarification' and len(nested_statuses)==1:status=next(iter(nested_statuses))
        children.append({'clause':clause,'response_type':response,'need_status':status,'query_plan':art.get('query_plan'),'coverage_errors':art.get('coverage_errors',[]),'need_ledger':art.get('need_ledger',{})})
        if art.get('response_type') not in {'answer','list'} or not result.validation.ok:incomplete.append(i)
        rename={}
        for hit in result.hits:
            old=hit.get('citation_label');new='S'+str(len(hits)+1)
            if old:rename[old]=new
            hits.append({**hit,'citation_label':new})
        text=re.sub(r'\[(S\d+)\]',lambda m:'['+rename.get(m[1],m[1])+']',result.answer)
        blocks.append(str(i)+'. '+clause+'\n'+text);obligations.extend(art.get('obligations',[]))
    plan={'record_ids':roots,'scope_ids':roots,'requested_fields':[],'all_fields':False,'method':'common_compound_operations','operation':'compound','clauses':children,'incomplete_clause_numbers':incomplete}
    return reader.finish(snap,started,'\n\n'.join(blocks),hits,plan,obligations,response='partial_answer' if incomplete else 'answer')
