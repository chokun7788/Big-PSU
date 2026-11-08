"""Sequential conversation replay with actual previous assistant answers."""
import sys,json
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
store=t.OneReleaseStore(t.DB).freeze();records=store.frozen['release']['records'];reader=t.CommonAnswerer(store)
out=B/'conversations_final';out.mkdir(exist_ok=False);rows=[]
with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f:
    for k in ('resource','service','rate','competition_rule'):
        for i in range(1,21):
            for lang in ('th','en'):
                r=records[t.rid(k,i)];other=records[t.rid(k,i%20+1)];history=[];spec=t.PROMPTS[k]
                questions=[(r['aliases'][lang][0]+(' ขอข้อมูลทั้งหมด' if lang=='th' else ' Show all information'),r,list(r['fields']),'first'),(('แล้ว' if lang=='th' else 'And ')+(spec[1] if lang=='th' else spec[2]),r,spec[0],'followup'),(('เปลี่ยนเป็น ' if lang=='th' else 'Switch to ')+other['aliases'][lang][0]+(' ขอข้อมูลทั้งหมด' if lang=='th' else ' Show all information'),other,list(other['fields']),'switch')]
                for q,target,keys,style in questions:
                    c={'id':str(len(rows)+1),'rid':target['record_id'],'expected_fields':keys,'lang':lang,'style':style,'kind':k,'question':q,'history':list(history)}
                    ans=reader.answer(q,locale=lang,history=history,at=t.AT);ok,why=t.prior.score(ans,c,records)
                    if style=='switch' and ans and r['record_id'] in ans.decision_artifact['query_plan']['record_ids']:ok=False;why.append('old_record_leak')
                    row={**c,'passed':ok,'reasons':why,'answer':ans.answer if ans else None,'decision':ans.decision_artifact if ans else None};rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n')
                    history.extend([{'role':'user','content':q},{'role':'assistant','content':ans.answer if ans else ''}])
                if len(rows)%120==0:f.flush();print('TURNS '+str(len(rows))+'/480',flush=True)
summary={'conversations':160,'turns':480,'passed':sum(r['passed'] for r in rows),'failed':[r['id'] for r in rows if not r['passed']],'real_prior_assistant_answers':True,'llm':False,'wordpress':False,'database_epoch_unchanged':store.still_current(store.frozen)}
(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(summary)
