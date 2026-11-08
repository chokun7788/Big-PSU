import os,sys,json,time
from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=Path((Path(__file__).parent/'two_turn_current_path.txt').read_text(encoding='utf-8'))
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0',PSU_CHAT_LOG_DIR=str(OUT/'source_logs'))
from app.pipeline.engine import answer_question_pipeline_debug as answer
from app.session.conversation_store import ConversationStore
from app.session.context_resolver import resolve_question_with_context

records=[]
stamp=time.strftime('%H%M%S')
def run(q,locale,store,session,turn,history):
    prepared=store.begin(session,turn,q,locale=locale,history=history)
    resolved=resolve_question_with_context(q,history,locale=locale)
    result=answer(resolved.resolved_question,locale=locale,request_plan=prepared.get('plan'),recent_history=history,experimental_allow_llm=False)
    rule=next((t.metadata for t in result.trace if t.stage=='competition_full_coverage'),None)
    response=dict(ok=True,answer=result.answer,mode=result.mode,route_category=result.route.category,route_intent=result.route.intent,universal_intent=result.universal_intent,request_id=turn,resolved_question=resolved.resolved_question,rule_coverage=rule)
    response['price_contract']=next((t.metadata for t in result.trace if t.stage=='conversation_contract'),None)
    store.complete(session,turn,prepared['revision'],response)
    store.acknowledge(session,turn)
    response['universal_intent']=vars(result.universal_intent) if result.universal_intent else None
    return response
from two_turn_grader_r39 import grade
for case in json.loads((OUT/os.getenv('PSU_CASE_FILE','cases.json')).read_text(encoding='utf-8')):
    store=ConversationStore();session=case['id']
    first=run(case['initial'],case['locale'],store,session,'first',[])
    second=run(case['choice'],case['locale'],store,session,'second',store.history(session))
    mode=second['mode'];valid_category=second['route_category']==case['expected_category'] or 'controls-' in case['id'] and second['route_intent']=='game_control_lookup'
    content=all(s.casefold() in second['answer'].casefold() for s in case['expected_contains'])
    scope=not case['full_detail'] or (second.get('rule_coverage') or {}).get('detail_level')=='full_sections'
    first_ok=not case['requires_clarification'] or (first['route_category']=='clarification' or 'clarification' in first['mode'] or 'missing_game_context' in first['mode'] or 'service_broad_choice' in first['mode'] or 'games_family' in first['mode'])
    if '-pc-domain-games' in case['id']:
        content=content and 'Nintendo Switch Zone' not in second['answer'] and 'PlayStation 5 Zone' not in second['answer']
    if '-cod-' in case['id']:
        valid_category=valid_category and second['route_intent']=='game_detail_lookup'
        first_ok=first_ok and 'games_family' in first['mode']
    graded=grade(case,first,second)
    ok=graded['passed']
    records.append(dict(case=case,first=first,second=second,passed=ok,checks=graded['checks']))
    with (OUT/f'source_records_{stamp}.jsonl').open('a',encoding='utf-8') as stream:
        stream.write(json.dumps(records[-1],ensure_ascii=False)+'\n')
    print(case['id'],first['mode'],'->',second['mode'],'PASS' if ok else 'FAIL',flush=True)
(OUT/f'source_results_{stamp}.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS',sum(r['passed'] for r in records),'/',len(records))
