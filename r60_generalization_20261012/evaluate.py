"""Evaluate new phrasing against typed fixture facts. No gold enters runtime."""
import sys,json,time,urllib.request,collections,traceback,os
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.planner import plan_fields,NUM_CTX
from app.pipeline.request_deadline import request_deadline
LABEL={'game':'title','center':'name','zone':'name','resource':'name','service':'name','audience':'name','equipment_model':'name','facility':'name','rental_package':'name','contact':'value','procedure':'topic','policy':'subject','competition':'event_name','competition_rule':'heading','news':'title','person':'display_name','faq':'question','game_mode':'mode_name'}
def leaves(v,key,lang,records):
    if isinstance(v,dict) and set(v)=={'th','en'}:return [v.get(lang) or v.get('en' if lang=='th' else 'th')]
    if key.endswith('_id') or key.endswith('_ids'):
        out=[]
        for target in v if isinstance(v,list) else [v]:
            if target is None:continue
            r=records[target];f=r['fields'].get(LABEL.get(r['kind'],''),{})
            if f.get('status')=='known':out+=leaves(f['value'],'label',lang,records)
            else:out+=[r['aliases'][lang][0] if r.get('aliases',{}).get(lang) else target]
        return out
    if key=='amount_minor':return [f'{v//100:,}.{v%100:02d}']
    if type(v) is bool:return [('Yes' if v else 'No') if lang=='en' else ('มี/ใช่' if v else 'ไม่มี/ไม่ใช่')]
    if isinstance(v,dict):return [z for k,x in v.items() for z in leaves(x,k,lang,records)]
    if isinstance(v,list):return [z for x in v for z in leaves(x,'item',lang,records)]
    return [] if v is None else [str(v)]
def score(ans,c,records):
    if ans is None:return False,['no_common_answer'],{}
    art=ans.decision_artifact or {};obs=art.get('obligations',[]);errors=[]
    if art.get('response_type') not in ('answer','list'):errors.append('response_'+str(art.get('response_type')))
    for key in c['expected_fields']:
        f=records[c['rid']]['fields'][key];matches=[o for o in obs if o['record_id']==c['rid'] and o['field']==key]
        if not matches:errors.append('missing_field:'+key);continue
        if matches[0]['status']!=f['status']:errors.append('wrong_status:'+key)
        if f['status']=='known':
            if any(v and v not in ans.answer for v in leaves(f['value'],key,c['lang'],records)):errors.append('missing_content:'+key)
            if not any(h.get('source_id')==e['source_id'] and h.get('locator')==e['locator'] for h in ans.hits for e in f['evidence_refs']):errors.append('missing_source_pointer:'+key)
        else:
            wanted=('Not applicable' if f['status']=='not_applicable' else 'Not yet confirmed') if c['lang']=='en' else ('ไม่เกี่ยวข้อง' if f['status']=='not_applicable' else 'ยังไม่มีข้อมูลยืนยัน')
            if wanted not in ans.answer:errors.append('missing_status_wording:'+key)
    actual={o['field'] for o in obs if o['record_id']==c['rid']}
    for key in c.get('forbidden_fields',[]):
        if key in actual or any(o['field']==key for o in obs):errors.append('rejected_need_answered:'+key)
    extras=sorted(actual-set(c['expected_fields']))
    return not errors,errors,{'extra_fields':extras,'exact_required_fields':actual==set(c['expected_fields']),'validation_ok':ans.validation.ok}
def main():
    name,source,mode=sys.argv[1:4];out=B/name;out.mkdir(exist_ok=False)
    store=t.OneReleaseStore(t.DB).freeze();records=store.frozen['release']['records'];reader=CommonAnswerer(store)
    rows=json.loads((B/source).read_text(encoding='utf-8'))
    if mode=='llm':
        payload={'model':'scb10x/typhoon2.5-qwen3-4b','stream':False,'think':False,'keep_alive':'10m','prompt':'OK','options':{'num_ctx':NUM_CTX,'num_predict':1}}
        start=time.time()
        req=urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=60) as r:pre=json.load(r)
        (out/'PREFLIGHT.json').write_text(json.dumps({'warm':True,'seconds':time.time()-start,'load_duration_ns':pre.get('load_duration')}),encoding='utf-8')
    results=[]
    with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f:
        for n,c in enumerate(rows,1):
            c=dict(c);rid=t.rid(c['kind'],c['profile']);c['rid']=rid;alias=records[rid]['aliases'][c['lang']][0]
            c['question']=c['phrase'] if c.get('history') else alias+' '+c['phrase']
            c['history']=[{'role':'user','content':alias+(' ขอข้อมูลทั้งหมด' if c['lang']=='th' else ' Show all information')}] if c.get('history') else []
            audit=[]
            def planner(q,recs,ids):return plan_fields(q,recs,ids,diagnostic=audit.append)
            try:
                start=time.perf_counter()
                with request_deadline(30):ans=reader.answer(c['question'],locale=c['lang'],history=c['history'],at=t.AT,planner=planner if mode=='llm' else None)
                ok,why,quality=score(ans,c,records)
                r={**c,'passed':ok,'reasons':why,'quality':quality,'answer':ans.answer if ans else None,'decision':ans.decision_artifact if ans else None,'planner_audits':audit,'elapsed':time.perf_counter()-start}
            except Exception:r={**c,'passed':False,'reasons':['exception'],'exception':traceback.format_exc()}
            f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush();results.append(r)
            if n%20==0:print(f'{n}/{len(rows)} pass={sum(x["passed"] for x in results)}',flush=True)
    sums=collections.defaultdict(collections.Counter)
    for r in results:
        for key in ['overall','language/'+r['lang'],'style/'+r['style'],'kind/'+r['kind']]:sums[key]['pass' if r['passed'] else 'fail']+=1
    summary={'cases':len(rows),'counts':dict(sums),'no_gold_in_runtime':True,'llm':mode=='llm','synthetic_new_phrasing':True,'actual_human_holdout':False,'db_epoch_unchanged':store.still_current(store.frozen),'not_latency_benchmark':True}
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
