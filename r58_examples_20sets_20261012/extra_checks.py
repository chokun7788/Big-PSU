"""Focused real LLM and true sequential chat histories; no product changes."""
import experiment as t
import os,json,time,collections,urllib.request,functools
from app.knowledge.common import answer as mod
os.environ['PSU_KNOWLEDGE_DB']=str(t.DB);os.environ['PSU_COMMON_ALLOW_DEMO']='1'
def main():
    mode=t.sys.argv[1];store=t.OneReleaseStore(t.DB).freeze();records=store.frozen['release']['records'];reader=t.CommonAnswerer(store)
    fixed=store.frozen['release']['names'];originalnamed=mod.named
    @functools.lru_cache(maxsize=10000)
    def cached(q):
        ids,method=originalnamed(q,fixed);return tuple(ids),method
    def names(q,m):
        if m!=fixed:raise RuntimeError('Name map changed')
        ids,method=cached(q);return list(ids),method
    mod.named=names
    if mode=='llm':
        from app.knowledge.common.planner import plan_fields,checked_plan
        from app.pipeline.llm_health import preflight_ollama,llm_health_snapshot
        model=os.getenv('PSU_KNOWLEDGE_LLM_MODEL','scb10x/typhoon2.5-qwen3-4b')
        warm=preflight_ollama(model=model,kind='demo20_preflight',timeout_sec=30,num_predict=1,num_ctx=3072);t.filejson('LLM_PREFLIGHT.json',warm)
        focus={'audience','resource','service','game_mode','competition_rule','closure'}
        qs=[c for c in t.cases(records) if c['rid'].startswith('demo20_') and c['rid'].endswith('_03') and c['kind'] in focus and c['style'] in {'natural','paraphrase','followup','multi_field'}]
        raw=[];real_urlopen=urllib.request.urlopen
        class Proxy:
            def __init__(self,r):self.r=r
            def __enter__(self):self.r.__enter__();return self
            def __exit__(self,*args):return self.r.__exit__(*args)
            def read(self,*args):
                b=self.r.read(*args)
                try:raw.append(json.loads(b)['response'])
                except (ValueError,KeyError):raw.append('not a planner response')
                return b
        def observed(*a,**kw):return Proxy(real_urlopen(*a,**kw))
        urllib.request.urlopen=observed
        rows=[]
        with (t.B/'LLM_RESULTS.jsonl').open('x',encoding='utf-8') as f:
            for n,c in enumerate(qs,1):
                raw.clear();attempts=[]
                def planner(q,recs,ids):
                    p=plan_fields(q,recs,ids)
                    attempts.append({'checked_plan':p,'raw_responses':list(raw),'record_ids':ids});return p
                ans=reader.answer(c['question'],locale=c['lang'],history=c['history'],at=t.AT,planner=planner);ok,why=t.prior.score(ans,c,records)
                row={**c,'passed':ok,'reasons':why,'answer':ans.answer if ans else None,'decision':ans.decision_artifact if ans else None,'planner_attempts':attempts}
                rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush();print(f'LLM {n}/{len(qs)} pass={ok}',flush=True)
        urllib.request.urlopen=real_urlopen
        t.filejson('LLM_SUMMARY.json',{'queries':len(rows),'pass':sum(r['passed'] for r in rows),'fail':sum(not r['passed'] for r in rows),'planner_attempts':sum(bool(r['planner_attempts']) for r in rows),'accepted_plans':sum(any(a['checked_plan'] for a in r['planner_attempts']) for r in rows),'model':model,'health':llm_health_snapshot(),'isolated_demo':True,'llm_real_not_mock':True,'not_full_pipeline':'CommonAnswerer plus actual bounded LLM planner'})
    elif mode=='conversations':
        rows=[]
        with (t.B/'CONVERSATION_RESULTS.jsonl').open('x',encoding='utf-8') as f:
            for k in ('resource','service','rate','competition_rule'):
                for i in range(1,21):
                    for lang in ('th','en'):
                        record=records[t.rid(k,i)];other=records[t.rid(k,i%20+1)];history=[]
                        spec=t.PROMPTS[k];alias=record['aliases'][lang][0]
                        questions=[(alias+(' ขอข้อมูลทั้งหมด' if lang=='th' else ' Show all information'),record,list(record['fields']),'first'),(('แล้ว' if lang=='th' else 'And ')+(spec[1] if lang=='th' else spec[2]),record,spec[0],'followup'),(('เปลี่ยนเป็น ' if lang=='th' else 'Switch to ')+other['aliases'][lang][0]+(' ขอข้อมูลทั้งหมด' if lang=='th' else ' Show all information'),other,list(other['fields']),'switch_record')]
                        for q,r,keys,turn in questions:
                            c={'id':f'conversation-{len(rows)+1:04}','rid':r['record_id'],'kind':k,'lang':lang,'style':turn,'question':q,'expected_fields':keys,'history':list(history)}
                            ans=reader.answer(q,locale=lang,history=history,at=t.AT);ok,why=t.prior.score(ans,c,records)
                            plan=ans.decision_artifact.get('query_plan',{}) if ans else {};targets=plan.get('record_ids',[])
                            if turn=='switch_record' and record['record_id'] in targets:ok=False;why.append('old_record_leaked_into_switch')
                            row={**c,'passed':ok,'reasons':why,'answer':ans.answer if ans else None,'decision':ans.decision_artifact if ans else None}
                            rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n')
                            history.extend([{'role':'user','content':q},{'role':'assistant','content':ans.answer if ans else '[no common answer]'}])
                        if len(rows)%60==0:f.flush();print('CONVERSATIONS '+str(len(rows))+'/480',flush=True)
        styles={}
        for style in {'first','followup','switch_record'}:
            rs=[r for r in rows if r['style']==style];styles[style]={'pass':sum(r['passed'] for r in rs),'fail':sum(not r['passed'] for r in rs)}
        t.filejson('CONVERSATION_SUMMARY.json',{'conversations':160,'turns':480,'pass':sum(r['passed'] for r in rows),'fail':sum(not r['passed'] for r in rows),'styles':styles,'actual_prior_assistant_answers_in_history':True,'llm':False,'legacy_fallback':False,'isolated_demo':True,'epoch_unchanged':store.still_current(store.frozen)})
    else:raise RuntimeError('llm or conversations')
if __name__=='__main__':main()
