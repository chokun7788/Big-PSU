"""Execute the equipment-list operation through current common relations."""
import re
from .registry import value
from .query_contract import normalize

def answer(reader,snap,started,question,lang,records,roots,at,*,task_contract=None):
    q=normalize(question)
    contracted=bool(task_contract and task_contract.get('task')=='equipment_list' and task_contract.get('whole_task_covered'))
    if not contracted and not re.search(r'อุปกรณ์อะไร|อุปกรณ์.{0,12}บ้าง|\b(?:what|which|list)\b.{0,35}\b(?:equipment|hardware)\b',q):return None
    if not roots or any(records[rid]['kind'] not in {'zone','service','resource'} for rid in roots):return None
    from .relations import related_attributes
    from .answer import title,text,effective
    selected={};edges=[]
    for rid in roots:
        for child,keys,edge in related_attributes(records,records[rid],['name','specifications','device_type']):
            if child['kind']=='equipment_model' and effective(child,at,records):selected[child['record_id']]=child;edges.append(edge)
    if not selected:return None
    hits=[];obs=[];lines=[];projection=[]
    for rid,r in selected.items():
        fields={};name=title(r,lang);specs=value(r,'specifications') or []
        quantity=[str(s.get('value')) for s in specs if s.get('key')=='quantity'];display=name+(' — '+', '.join(quantity) if quantity else '')
        labels=[]
        for key in ['name']+(['specifications'] if quantity else []):
            f=r['fields'][key]
            if f['status']!='known':continue
            fields[key]='explicit';obs.append({'record_id':rid,'field':key,'status':'known','evidence_refs':f['evidence_refs']})
            for ref in f['evidence_refs']:
                src=snap['release']['sources'][ref['source_id']];label='S'+str(len(hits)+1);labels.append('['+label+']')
                hits.append({'id':rid+':'+key+':'+label,'record_id':rid,'field':key,'title':name,'text':text(f['value'],lang),'source_id':ref['source_id'],'snapshot_sha256':src['sha256'],'locator':ref['locator'],'source_url':src.get('public_url') or '', 'citation_label':label})
        lines.append('• '+display+' '+' '.join(labels));projection.append({'record_id':rid,'fields':fields})
    plan={'record_ids':list(selected),'scope_ids':roots,'operation':'equipment','method':'common_equipment_catalog_bridge','requested_fields':['name'],'response_projection':projection,'related_edges':edges,'legacy_fact_fallback_used':False}
    if contracted:plan['task_contract']=task_contract
    caption=('อุปกรณ์ตามโซนที่ถาม' if lang=='th' else 'Equipment in the selected zone(s)')
    return reader.finish(snap,started,caption+'\n'+'\n'.join(lines),hits,plan,obs,response='list')
