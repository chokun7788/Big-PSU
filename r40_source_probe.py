import os, sys, json, time, uuid
from dataclasses import asdict
from pathlib import Path
from r40_targeted_probe import OUT, cases, grade
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0',PSU_CHAT_LOG_DIR=str(OUT/'source_logs'))
from app.pipeline.engine import answer_question_pipeline_debug as answer
from app.session.context_resolver import resolve_question_with_context, ResolvedQuestion
from app.session.conversation_store import ConversationStore
label=sys.argv[1] if len(sys.argv)>1 else 'round_A_B_source'
runid=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]
raw=OUT/f'{label}_{runid}_raw.jsonl';results=[]
for c in cases():
    store=ConversationStore();session='s-'+uuid.uuid4().hex;records=[]
    for i,q in enumerate(c['turns']):
        history=store.history(session); turn=str(i)
        prepared=store.begin(session,turn,q,locale=c['locale'],history=history)
        if prepared.get('plan'):
            plan=prepared['plan']
            resolved=ResolvedQuestion(q,plan['resolved_query'],plan.get('context_used',False),context_domain='service_fee',context_operation='price_lookup',reason='parent_typed_request_plan')
        else:
            resolved=resolve_question_with_context(q,history,locale=c['locale'])
        start=time.perf_counter();r=answer(resolved.resolved_question,locale=c['locale'],request_plan=prepared.get('plan') or resolved.to_selection_plan(),recent_history=history,experimental_allow_llm=False)
        b=dict(ok=True,answer=r.answer,mode=r.mode,route_category=r.route.category,route_intent=r.route.intent,request_id=turn,
               resolved_question=resolved.resolved_question,trace=[asdict(t) for t in r.trace],validation=asdict(r.validation),
               universal_intent=asdict(r.universal_intent) if r.universal_intent else None)
        store.complete(session,turn,prepared['revision'],b);store.acknowledge(session,turn)
        record=dict(case_id=c['id'],payload=dict(question=q,locale=c['locale']),response=b,status=200,elapsed_sec=round(time.perf_counter()-start,4),context=asdict(resolved))
        records.append(record)
        with raw.open('a',encoding='utf-8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
    result=grade(c,records);results.append(result)
    print(c['id'],'PASS' if result['passed'] else 'FAIL',result['mode'],[k for k,v in result['checks'].items() if not v],flush=True)
file=OUT/f'{label}_{runid}_summary.json'
with file.open('x',encoding='utf-8') as f:json.dump(dict(label=label,model_enabled=False,semantic_retrieval=False,planned_cases=len(cases()),executed_cases=len(results),passed=sum(r['passed'] for r in results),failed=sum(not r['passed'] for r in results),raw_file=raw.name,results=results),f,ensure_ascii=False,indent=2)
print('SUMMARY',str(file),sum(r['passed'] for r in results),'/',len(results),flush=True)
