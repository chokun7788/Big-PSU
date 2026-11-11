"""Render complete typed field values with the original evidence pointers."""
import time
from .registry import value

def render(reader,snap,rows,lang,plan,*,response='answer',caption=''):
    from .answer import text,title
    records=snap['release']['records'];hits=[];obs=[];blocks=[]
    for rid,keys in rows:
        r=records[rid];lines=[]
        for key in keys:
            f=r['fields'].get(key,{})
            if f.get('status')!='known' or not f.get('evidence_refs'):continue
            content=text(f['value'],lang);labels=[]
            from .registry import CATALOG
            spec=next((x for x in CATALOG[r['kind']]['fields'] if x['key']==key),{})
            if spec.get('reference_kind'):
                refs=f['value'] if isinstance(f['value'],list) else [f['value']]
                content=', '.join(title(records[k],lang) for k in refs if k in records) or ('ไม่มีรายการอ้างถึง' if lang=='th' else 'No linked items')
            for ref in f['evidence_refs']:
                src=snap['release']['sources'].get(ref['source_id'])
                if src is None or r['kind'] not in src.get('authority_for',[]):
                    return reader.finish(snap,time.perf_counter(),'ยังยืนยันแหล่งข้อมูลสำหรับส่วนนี้ไม่ได้ครับ' if lang=='th' else 'The source authority for this part cannot be confirmed.',[],{'record_ids':[],'requested_fields':[],'method':'r106_source_boundary_failure','graph_result':{'status':'broken_relation','reason':'source_authority_scope_mismatch'}},[],response='unconfirmed')
                label='S'+str(len(hits)+1);labels.append('['+label+']')
                hits.append({'id':rid+':'+key+':'+label,'record_id':rid,'field':key,'title':title(r,lang),'text':content,'source_id':ref['source_id'],'snapshot_sha256':src['sha256'],'locator':ref['locator'],'citation_label':label,'source_url':src.get('public_url') or ''})
            if labels:
                obs.append({'record_id':rid,'field':key,'status':'known','evidence_refs':f['evidence_refs']})
                if not (r['kind']=='competition_rule' and key in {'competition_id','completeness','depends_on_ids'}):lines.append(content+' '+''.join(labels))
        if lines:blocks.append('**'+title(r,lang)+'**\n'+'\n'.join(lines))
    qp={**plan,'record_ids':list(dict.fromkeys(rid for rid,_ in rows)),'requested_fields':[],
        'response_projection':[{'record_id':rid,'fields':{k:'explicit' for k in keys}} for rid,keys in rows]}
    return reader.finish(snap,time.perf_counter(),(caption+'\n\n' if caption else '')+'\n\n'.join(blocks),hits,qp,obs,response=response)
