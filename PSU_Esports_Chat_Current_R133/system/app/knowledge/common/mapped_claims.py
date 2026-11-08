"""Execute explicitly mapped claims with source receipts and dependencies."""
import time,json
from dataclasses import replace
from .registry import value
from .claim_bindings import current_claims,_project

def render(reader,need,claims,snap,at,lang,scope=None):
    from .read_graph import fact,evaluate
    records=snap['release']['records'];all_claims={c['claim_id']:c for c in current_claims(snap,at)}
    selected={c['claim_id']:c for c in claims};pending=list(selected)
    while pending:
        c=selected[pending.pop()]
        for dep in c['dependency_refs']:
            if dep not in all_claims:return None
            if dep not in selected:selected[dep]=all_claims[dep];pending.append(dep)
    hits=[];obs=[];packets=[];blocks=[]
    for c in selected.values():
        refs=[c['value_ref'],*c['condition_refs'],*c['exception_refs']];pieces=[];receipts=[]
        for ref in refs:
            r=records[ref['record_id']];f=r['fields'][ref['field']]
            evaluated=evaluate(fact(r['record_id'],ref['field']),snap,at,need.id,need.predicate)
            if evaluated.get('status')!='supported':return None
            receipts.extend(evaluated['receipts'])
            try:x=_project(ref,records)
            except (KeyError,TypeError,ValueError,IndexError):return None
            if c['predicate']=='current_rate' and ref==c['value_ref'] and isinstance(x,int):text=f'{x/100:,.2f} THB / '+str(c['unit'])
            elif isinstance(x,dict):text=x.get(lang) or x.get('th') or x.get('en')
            elif isinstance(x,bool):text=('อนุญาต' if x else 'ไม่อนุญาต') if lang=='th' else ('Allowed' if x else 'Not allowed')
            else:text=str(x)
            if not text:return None
            labels=[]
            for source_ref in f['evidence_refs']:
                src=snap['release']['sources'].get(source_ref['source_id'])
                if not src:return None
                label='S'+str(len(hits)+1);labels.append('['+label+']')
                hits.append({'id':r['record_id']+':'+ref['field']+':'+label,'record_id':r['record_id'],'field':ref['field'],'title':r['record_id'],
                  'text':str(text),'source_id':source_ref['source_id'],'snapshot_sha256':src['sha256'],'locator':source_ref['locator'],'citation_label':label,'source_url':src.get('public_url') or ''})
            obs.append({'record_id':r['record_id'],'field':ref['field'],'status':'known','evidence_refs':f['evidence_refs']})
            pieces.append(str(text)+' '+''.join(labels))
        from .answer import title
        subject=title(records[c['subject_ref']],lang)
        blocks.append(subject+'\n'+'\n'.join(pieces));packets.append({**c,'need_id':need.id,'receipts':receipts})
    qp={'record_ids':list(dict.fromkeys(c['record_id'] for c in selected.values())),'requested_fields':[],
      'method':'r102_mapped_claims','task_plan':{'task':need.task,'predicate':need.predicate},'mapped_claims':list(selected),'scope_receipt':scope}
    result=reader.finish(snap,time.perf_counter(),'\n\n'.join(blocks),hits,qp,obs,response='answer')
    return replace(result,decision_artifact={**result.decision_artifact,'mapped_claim_packets':packets,
      'need_results':[{'need_id':need.id,'task':need.task,'predicate':need.predicate,'status':'supported','reason_codes':[],
        'record_ids':qp['record_ids'],'receipts':[r for p in packets for r in p['receipts']],'claim_ids':list(selected)}]})
