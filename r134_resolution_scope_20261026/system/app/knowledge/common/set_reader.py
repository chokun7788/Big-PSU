"""Explicit source-declared inventory sets, including known empty scopes."""
import re,time
from dataclasses import replace
from .claim_bindings import current_claims
from .read_graph import fact,evaluate

def answer(reader,need,snap,at,lang):
    kind=None
    if re.search(r'อุปกรณ์|\bequipment\b',need.query,re.I):kind='equipment_inventory'
    if not kind or need.task not in {'equipment_list','unresolved'}:return None
    records=snap['release']['records'];roots=set(need.record_ids)
    candidates=[c for c in current_claims(snap,at) if c['predicate']==kind and not c['condition_refs'] and not c['exception_refs'] and isinstance(c['value'],list)
      and (c['subject_ref'] in roots if roots else records.get(c['subject_ref'],{}).get('kind')=='center')]
    if len(candidates)!=1:return None
    c=candidates[0];members=list(dict.fromkeys(c['value']));ref=c['value_ref']
    if any(k not in records or records[k]['kind'] not in {'resource','equipment_model'} or k in snap.get('withdrawn',[]) for k in members):return None
    proof=evaluate(fact(ref['record_id'],ref['field']),snap,at,need.id,kind)
    if proof['status']!='supported':return None
    from .answer import title
    scope=title(records[c['subject_ref']],lang)
    body=((scope+' — รายการอุปกรณ์ที่ยืนยันแล้ว: '+', '.join(title(records[k],lang) for k in members)) if members else ('ในขอบเขต '+scope+' ไม่มีอุปกรณ์ในรายการที่ยืนยันแล้วครับ')) if lang=='th' else ((scope+' — confirmed equipment: '+', '.join(title(records[k],lang) for k in members)) if members else ('No equipment is listed in the confirmed inventory for '+scope+'.'))
    f=records[ref['record_id']]['fields'][ref['field']];hits=[]
    for er in f['evidence_refs']:
        src=snap['release']['sources'][er['source_id']];label='S'+str(len(hits)+1)
        hits.append({'id':c['claim_id']+label,'record_id':ref['record_id'],'field':ref['field'],'text':body,'title':scope,
          'source_id':er['source_id'],'locator':er['locator'],'snapshot_sha256':src['sha256'],'citation_label':label,'source_url':src.get('public_url') or ''})
        body+=' ['+label+']'
    receipt={'scope':kind,'subject_ref':c['subject_ref'],'release_id':snap['active'],'epoch':snap['epoch'],'member_ids':members,
      'total_members':len(members),'returned_members':len(members),'completeness':'explicit_source_declared','claim_id':c['claim_id']}
    result=reader.finish(snap,time.perf_counter(),body,hits,{'record_ids':[c['record_id']],'requested_fields':[],
      'method':'r102_declared_set','scope_receipt':receipt,'task_plan':{'task':'equipment_list'}},[{'record_id':ref['record_id'],'field':ref['field'],'status':'known','evidence_refs':f['evidence_refs']}],response='answer')
    return replace(result,decision_artifact={**result.decision_artifact,'mapped_claim_packets':[{**c,'need_id':need.id,'receipts':proof['receipts']}],
      'need_results':[{'need_id':need.id,'task':'equipment_list','predicate':kind,'status':'supported','reason_codes':[],
        'record_ids':[c['record_id']],'receipts':proof['receipts']}],'scope_receipt':receipt})
