"""Targeted code checks on existing queries; no HTTP/model or new questions."""
import copy,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.routing import route,split_needs
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.readers import guard
from app.pipeline.chatbot_identity import is_chatbot_identity_query,_IDENTITY_TERMS
data=json.loads((R/'NATIVE_SOURCE_REFERENCE.json').read_text('utf8'));engine=Engine(data)
jobs={j['id']:j for j in map(json.loads,(R/'EXISTING_QUESTIONS_1400.jsonl').read_text('utf8').splitlines())}
expects={x['id']:x for x in json.loads((R/'NATIVE_EXPECTATIONS.json').read_text('utf8'))['questions']}
baseline=[json.loads(l) for l in (R/'runs/http01/RESULTS.jsonl').open(encoding='utf8')]
checks=[]
def check(name,passed,**evidence):
    checks.append({'check':name,'passed':bool(passed),**evidence})
for x in baseline:
    j=jobs[x['question_id']];qid=j['id'];q=j['question'];at=reference_time(j['reference_time'])
    if j['category']=='C02' and not x['grade']['passed']:
        check(qid+':not_bot_identity',not is_chatbot_identity_query(q))
    if j['category']=='C06' and re.search(r'migrated_rate_|rate_recovered_',q):
        out=engine.answer(q,j['locale'],at=at,allow_llm=False)
        wanted={f['native_fact_id'] for f in expects[qid]['goals']}
        check(qid+':opaque_rate_binding',{c['fact_id'] for c in out['claims']}==wanted,actual=[c['fact_id'] for c in out['claims']],expected=sorted(wanted))
    if j['category'] in {'C03','C08','C09','C10'} and not expects[qid]['goals']:
        cat=route(engine.index,q)
        if re.search(r'ประกัน|ชื่อบริษัท|คริปโต|ถ่ายใบหน้า',q):
            p=engine.plan(cat,q,at) if cat else None
            check(qid+':missing_predicate_terminal',p is not None and p.locked and p.status=='missing_source' and cat==j['category'])
    if j['category']=='C11' and any(g.get('facet')=='bookable_periods' or ':bookable_periods' in g.get('native_fact_id','') for g in expects[qid]['goals']):
        out=engine.answer(q,j['locale'],at=at,allow_llm=False)
        check(qid+':recorded_period_not_current_claim',any(n['plan']['metadata'].get('calendar_source_limits') for n in out['needs']) and out['status']=='partial')
    if j['category']=='C12' and expects[qid]['goals']:
        check(qid+':live_need_not_static_inventory',all(route(engine.index,p)=='C12' for p in split_needs(q,engine.index)))
    if j['category']=='C14' and expects[qid]['goals']:
        out=engine.answer(q,j['locale'],at=at,allow_llm=False)
        check(qid+':unknown_event_not_other_source',route(engine.index,q)=='C14' and not out['claims'])
# Existing interface phrase constants still need to function.
for phrase in _IDENTITY_TERMS:
    check('existing_identity:'+phrase,is_chatbot_identity_query(phrase))
# Verify a guard opens if the same existing warranty question gains a declared
# source. This is an in-memory source extension, never a DB/data write.
j=next(j for j in jobs.values() if j['category']=='C03' and 'ประกัน' in j['question'])
d=copy.deepcopy(data);f=copy.deepcopy(next(f for f in d['facts'] if f['category']=='C03'))
f.update(id='verification-only-declared-field',label={'th':'ประกัน','en':'warranty'},faq_question={'th':j['question'],'en':j['question']})
d['facts'].append(f);other=Engine(d)
check('owner_declared_warranty_not_permanently_blocked',guard(other.index,'C03',j['question'],reference_time(j['reference_time'])) is None)
out=R/(sys.argv[1] if len(sys.argv)>1 else 'CODE_CHECKS.json');assert not out.exists();out.write_text(json.dumps({'new_questions':0,'model_calls':0,'http_calls':0,'checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks)},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'passed':sum(x['passed'] for x in checks),'total':len(checks),'failures':[x for x in checks if not x['passed']]},ensure_ascii=False))
assert all(x['passed'] for x in checks)
