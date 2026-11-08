import json, os, sys, time, urllib.request
from pathlib import Path
from r27_fixture import PROJECT, REPORT, check
sys.path.insert(0,str(PROJECT))
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
from app.pipeline.engine import answer_question_pipeline_debug
cases=json.loads((REPORT/'content_contract_fixture_v2.json').read_text(encoding='utf-8'))['cases']
run=sys.argv[1]; port=sys.argv[2] if len(sys.argv)>2 else None
records=[]
with (REPORT/(run+'_details.jsonl')).open('x',encoding='utf-8') as output:
    for n,case in enumerate(cases,1):
        start=time.perf_counter()
        if port:
            payload={'question':case['question'],'locale':case['locale'],'recent_history':[],'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
            data=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:'+port+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
            response={'answer':data['answer'],'mode':data['mode'],'category':data['route_category'],'hits':data.get('sources',[]),'valid':data.get('validation_ok',True),'raw':data}
        else:
            result=answer_question_pipeline_debug(case['question'],locale=case['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
            response={'answer':result.answer,'mode':result.mode,'category':result.route.category,'hits':result.hits,'valid':result.validation.ok,'trace':[vars(t) for t in result.trace]}
        failures=check(case,response)
        record={'id':case['id'],'anchor':case['anchor'],'question':case['question'],'locale':case['locale'],'mutation':case['mutation'],'elapsed':round(time.perf_counter()-start,4),'failures':failures,'passed':not failures,'response':response}
        records.append(record);output.write(json.dumps(record,ensure_ascii=False)+'\n');output.flush()
        if n%50==0:print(json.dumps({'completed':n,'failed':sum(not r['passed'] for r in records)},ensure_ascii=False),flush=True)
summary={'total':len(records),'passed':sum(r['passed'] for r in records),'failed':sum(not r['passed'] for r in records),'failed_anchors':sorted({r['anchor'] for r in records if not r['passed']}),'max_elapsed':max(r['elapsed'] for r in records),'port':port}
with (REPORT/(run+'_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False),flush=True)
