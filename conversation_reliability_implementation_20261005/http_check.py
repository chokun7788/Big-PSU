import json,urllib.request,urllib.error,uuid,time,sys
from pathlib import Path
PORT=int(sys.argv[1]) if len(sys.argv)>1 else 8093
HERE=Path(__file__).resolve().parent
STAMP=time.strftime('%H%M%S');OUTPUT=HERE/f'http_results_{PORT}_{STAMP}.jsonl'
records=[];checks=[]
def ask(q,session,locale='th',ack='',turn=None):
    payload={'question':q,'client_session_id':session,'client_turn_id':turn or 'turn-'+str(uuid.uuid4()),'last_seen_response_id':ack,'locale':locale,'debug':True,'experimental_rag_fallback':True}
    started=time.perf_counter()
    request=urllib.request.Request(f'http://127.0.0.1:{PORT}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(request,timeout=45) as response:status=response.status;body=json.load(response)
    except urllib.error.HTTPError as response:status=response.code;body=json.load(response)
    record={'payload':payload,'status':status,'wall_sec':round(time.perf_counter()-started,4),'response':body}
    records.append(record)
    with OUTPUT.open('a',encoding='utf-8') as stream:stream.write(json.dumps(record,ensure_ascii=False)+'\n')
    print(locale,q,status,body.get('mode'),round(record['wall_sec'],2),flush=True)
    return body,payload
def check(name,truth,details=None):checks.append({'check':name,'passed':bool(truth),'details':details})
def session():return 'flow-'+str(uuid.uuid4())
def groups(r):return {x.rsplit(':',1)[1] for x in r.get('coverage',{}).get('returned_ids',[])}
for locale,initial,allq in [('th','ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก','ทั้งหมด'),('en','Service prices for external users','all of them')]:
    s=session();r,_=ask(initial,s,locale);check(locale+'_pending',r.get('route_intent')=='price_missing_service')
    r,p=ask('PC',s,locale,r.get('request_id',''));check(locale+'_PC',r.get('route_category')=='service_fee' and groups(r)=={'general_student','general_adult'})
    retry,_=ask('PC',s,locale,turn=p['client_turn_id']);check(locale+'_same_turn_retry',retry.get('request_id')==r.get('request_id'))
    conflict,_=ask('VR',s,locale,turn=p['client_turn_id']);check(locale+'_turn_conflict',conflict.get('error')=='client_turn_conflict')
    r,_=ask('แล้ว VR ล่ะ' if locale=='th' else 'what about VR',s,locale,r.get('request_id',''));check(locale+'_VR_retains_group',r.get('request_plan',{}).get('tasks',[{}])[0].get('targets')==['vr'] and groups(r)=={'general_student','general_adult'})
    s=session();r,_=ask(initial,s,locale);r,_=ask(allq,s,locale,r.get('request_id',''));check(locale+'_all_scope',len(r.get('coverage',{}).get('returned_ids',[]))==14)
    r,_=ask('ไม่ใช่นักศึกษานะ' if locale=='th' else 'not a student',s,locale,r.get('request_id',''));check(locale+'_negative_group',groups(r)=={'general_adult'})
    s=session();r,_=ask(initial+(' และวิธีจอง' if locale=='th' else ' and how to book'),s,locale);r,_=ask('PC',s,locale,r.get('request_id',''))
    outcomes=r.get('coverage',{}).get('task_outcomes',[]);check(locale+'_two_tasks',len(outcomes)==2 and all(t.get('outcome')=='answered_complete' for t in outcomes),outcomes)
    # Omit browser history deliberately: parent memory must survive recycling.
    s=session();r,_=ask(initial,s,locale);r,_=ask('เอาคอมก่อน' if locale=='th' else 'the desktop station please',s,locale,r.get('request_id',''))
    check(locale+'_natural_choice',r.get('route_category')=='service_fee' and (r.get('request_plan') or {}).get('tasks',[{}])[0].get('targets')==['pc'],r.get('mode'))
    r,_=ask('ไก่กับไข่อะไรเกิดก่อนกัน' if locale=='th' else 'Which came first, the chicken or the egg?',s,locale,r.get('request_id',''))
    check(locale+'_general_not_generic_clarification',r.get('mode')!='pipeline:candidate_margin_clarification',r.get('mode'))
    check(locale+'_general_answer_available','general_llm' in r.get('mode',''),r.get('answer'))
    s=session();r,_=ask('กติกาการแข่งขัน CS2' if locale=='th' else 'CS2 competition rules',s,locale)
    r,_=ask('ขอรายละเอียดทั้งหมด' if locale=='th' else 'all details please',s,locale,r.get('request_id',''))
    cov=r.get('rule_coverage') or {};check(locale+'_rules_full_scope',cov.get('detail_level')=='full_sections',r.get('mode'))
    first=set(cov.get('returned_ids',[]));r,_=ask('ต่อ' if locale=='th' else 'continue',s,locale,r.get('request_id',''))
    nextcov=r.get('rule_coverage') or {};check(locale+'_rules_continue',bool(nextcov.get('returned_ids')) and not first.intersection(nextcov.get('returned_ids',[])),r.get('mode'))
    check(locale+'_acknowledged', 'client_acknowledged' in (r.get('conversation_state') or {}).get('delivery',{}).values())
s=session();r,_=ask('ต้องการรู้ราคาของการใช้บริการของบุคคลภายนอก',s,'auto')
r,p=ask('PC',s,'auto',r.get('request_id',''));check('auto_parent_language',r.get('language',{}).get('effective')=='th')
original_id=r.get('request_id');ask('VR prices for general adults',s,'en',original_id)
retry,_=ask('PC',s,'auto',turn=p['client_turn_id']);check('auto_stable_retry_fingerprint',retry.get('request_id')==original_id and retry.get('language',{}).get('effective')=='th')
summary={'port':PORT,'requests':len(records),'passed':sum(x['passed'] for x in checks),'checks':checks,'raw_file':OUTPUT.name}
(HERE/f'http_summary_{PORT}_{STAMP}.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'requests':len(records),'passed':summary['passed'],'failed':[x for x in checks if not x['passed']]},ensure_ascii=False,indent=2))
