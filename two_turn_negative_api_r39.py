import json,uuid,time,urllib.request
from two_turn_grader_r39 import OUT
port=8094;records=[];results=[]
stamp=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]
raw=OUT/f'negative_api_{stamp}.jsonl'
def ask(q,lang,session,ack=''):
    payload=dict(question=q,locale=lang,client_session_id=session,client_turn_id=str(uuid.uuid4()),last_seen_response_id=ack,debug=True)
    request=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(request,timeout=40) as response:r=json.load(response)
    with raw.open('a',encoding='utf-8') as f:f.write(json.dumps(dict(payload=payload,response=r),ensure_ascii=False)+'\n')
    return r
for lang in ('th','en'):
    for choice in ('TEKKEN 9','Minecraft'):
        session='negative-'+uuid.uuid4().hex
        a=ask('ขอดูปุ่มควบคุมเกม' if lang=='th' else 'Show me the game controls',lang,session)
        b=ask(choice,lang,session,a['request_id'])
        passed='structured_game_controls' not in b.get('mode','') and 'games_catalog' not in b.get('mode','')
        if choice=='TEKKEN 9':
            passed=passed and b.get('resolved_question')==choice and 'TEKKEN 8' not in b.get('answer','') and b.get('mode')=='pipeline:game_edition_unconfirmed'
        else:
            passed=passed and choice.casefold() in b.get('resolved_question','').casefold()
            passed=passed and 'missing_game_context' not in b.get('mode','')
        results.append(dict(id=lang+'-'+choice,passed=passed,mode=b.get('mode'),resolved=b.get('resolved_question'),answer=b.get('answer')))
for choice in ('PS55','PS6'):
    session='negative-'+uuid.uuid4().hex;a=ask('What games can I play?','en',session);b=ask(choice,'en',session,a['request_id'])
    passed=b.get('resolved_question')==choice and 'games_catalog' not in b.get('mode','') and 'service_game_availability' not in b.get('mode','')
    results.append(dict(id='invalid-zone-'+choice,passed=passed,mode=b.get('mode'),resolved=b.get('resolved_question'),answer=b.get('answer')))
session='negative-'+uuid.uuid4().hex;a=ask('Show me the game controls','en',session)
b=ask('VALORANT','en','other-'+uuid.uuid4().hex)
results.append(dict(id='session-isolation',passed=b.get('route_intent')=='game_detail_lookup',mode=b.get('mode'),answer=b.get('answer')))
session='negative-'+uuid.uuid4().hex;a=ask('Show me the game controls','en',session)
b=ask('When does the studio open?','en',session,a['request_id']);c=ask('VALORANT','en',session,b['request_id'])
results.append(dict(id='intervening-topic-change',passed=c.get('route_intent')=='game_detail_lookup',mode=c.get('mode'),answer=c.get('answer')))
report=dict(raw=raw.name,cases=len(results),requests=17,passed=sum(x['passed'] for x in results),results=results)
(OUT/f'negative_summary_{stamp}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for r in results:print(r['id'],'PASS' if r['passed'] else 'FAIL',r['mode'],flush=True)
print('PASS',report['passed'],'/',len(results),flush=True)
