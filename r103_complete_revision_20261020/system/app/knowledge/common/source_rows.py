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
            for ref in f['evidence_refs']:
                src=snap['release']['sources'].get(ref['source_id'])
                if src is None:continue
                label='S'+str(len(hits)+1);labels.append('['+label+']')
                hits.append({'id':rid+':'+key+':'+label,'record_id':rid,'field':key,'title':title(r,lang),'text':content,'source_id':ref['source_id'],'snapshot_sha256':src['sha256'],'locator':ref['locator'],'citation_label':label,'source_url':src.get('public_url') or ''})
            if labels:
                obs.append({'record_id':rid,'field':key,'status':'known','evidence_refs':f['evidence_refs']})
                lines.append(content+' '+''.join(labels))
        if lines:blocks.append('**'+title(r,lang)+'**\n'+'\n'.join(lines))
    qp={**plan,'record_ids':list(dict.fromkeys(rid for rid,_ in rows)),'requested_fields':[],
        'response_projection':[{'record_id':rid,'fields':{k:'explicit' for k in keys}} for rid,keys in rows]}
    return reader.finish(snap,time.perf_counter(),(caption+'\n\n' if caption else '')+'\n\n'.join(blocks),hits,qp,obs,response=response)
