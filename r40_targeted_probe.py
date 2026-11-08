import json, sys, time, uuid, urllib.request, urllib.error, os
from pathlib import Path
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r40_current_path.txt').read_text(encoding='utf-8'))

def cases():
    if os.getenv('R40_CASE_FILE'):
        return json.loads((BASE/os.environ['R40_CASE_FILE']).read_text(encoding='utf-8'))
    result=[]
    for lang, questions in {
        'th':['ขอดูปุ่มควบคุมเกม','ขอดูปุ่มทั้งหมด','ช่วยบอกปุ่มเกมหน่อยครับ','เกมมีปุ่มอะไรบ้าง','ปุ่มควบคุมต้องกดยังไง','อยากรู้วิธีบังคับเกม'],
        'en':['Show me the game controls','Can I see the game controls?','What buttons can I use?','Tell me the keyboard controls please','How do I control the game?','List all game buttons','I need the controls']}.items():
        for i,q in enumerate(questions):
            result.append(dict(id=f'clarify-{lang}-{i}',locale=lang,turns=[q],kind='missing_controls'))
    result.extend([
      dict(id='multi-controls-th',locale='th',turns=['ขอดูปุ่มควบคุมเกม','VALORANT กับ Mario Kart 8 Deluxe'],kind='multi_controls',required=['VALORANT','Mario Kart 8 Deluxe']),
      dict(id='multi-controls-en',locale='en',turns=['Show me the game controls','VALORANT and Mario Kart 8 Deluxe'],kind='multi_controls',required=['VALORANT','Mario Kart 8 Deluxe']),
      dict(id='multi-controls-typo-en',locale='en',turns=['Show me the game controls','Valoant and Beat Saber please'],kind='multi_controls',required=['VALORANT','Beat Saber']),
      dict(id='multi-catalog-th',locale='th',turns=['มีเกมอะไรให้เล่นบ้าง','PC กับ PS5'],kind='multi_catalog',required=['PC Zone','PlayStation 5 Zone'],forbidden=['Nintendo Switch Zone','Cockpit Zone','VR Zone']),
      dict(id='multi-catalog-en',locale='en',turns=['What games can I play?','PC and PS5'],kind='multi_catalog',required=['PC Zone','PlayStation 5 Zone'],forbidden=['Nintendo Switch Zone','Cockpit Zone','VR Zone']),
      dict(id='multi-catalog-typo-en',locale='en',turns=['What games can I play?','PC and cockpik please'],kind='multi_catalog',required=['PC Zone','Cockpit Zone'],forbidden=['Nintendo Switch Zone','PlayStation 5 Zone','VR Zone']),
      dict(id='roman-edition-en',locale='en',turns=['Show me the game controls','TEKKEN IX'],kind='wrong_edition'),
      dict(id='roman-edition-th',locale='th',turns=['ขอดูปุ่มควบคุมเกม','TEKKEN IX'],kind='wrong_edition'),
      dict(id='new-operation-en',locale='en',turns=['Show me the game controls','What is VALORANT?'],kind='new_detail',required=['VALORANT']),
      dict(id='new-operation-th',locale='th',turns=['ขอดูปุ่มควบคุมเกม','VALORANT คืออะไร'],kind='new_detail',required=['VALORANT']),
      dict(id='unknown-latin-en',locale='en',turns=['Show me the game controls','Minecraft'],kind='unknown_controls'),
      dict(id='unknown-thai-th',locale='th',turns=['ขอดูปุ่มควบคุมเกม','มายคราฟต์'],kind='unknown_controls'),
      dict(id='known-controls-en',locale='en',turns=['What are the controls for VALORANT?'],kind='single_controls',required=['VALORANT','W']),
      dict(id='known-controls-th',locale='th',turns=['VALORANT มีปุ่มอะไรบ้าง'],kind='single_controls',required=['VALORANT','W']),
      dict(id='hardware-not-game-en',locale='en',turns=['What controller model does the PS5 zone use?'],kind='not_generic_controls'),
      dict(id='booking-button-not-controls-en',locale='en',turns=['Where is the booking button?'],kind='not_generic_controls'),
      dict(id='equipment-damage-th',locale='th',turns=['คีย์บอร์ดพังต้องทำยังไง'],kind='not_generic_controls'),
      dict(id='explicit-reject-th',locale='th',turns=['ไม่เอาปุ่ม ขอราคาของ PC'],kind='not_generic_controls'),
    ])
    return result

def grade(case, records):
    r=records[-1]; b=r.get('response',{}); answer=b.get('answer',''); mode=b.get('mode','')
    trace=b.get('trace') or []
    if isinstance(trace,dict): trace=trace.get('stages',[])
    checks={'http_success':r.get('status')==200 and b.get('ok') is True}
    kind=case['kind']
    if kind=='missing_controls':
        checks['asks_game']=('game_control_missing_game_context' in mode)
        checks['no_catalog']='games_catalog' not in mode
    elif kind in {'single_controls','multi_controls'}:
        checks['control_operation']=('structured_game_controls' in mode or 'multi_question_splitter' in mode and any('control' in str(t) for t in trace))
        checks['all_targets']=all(x.casefold() in answer.casefold() for x in case['required'])
        checks['not_missing_target']='missing_game_context' not in mode
    elif kind=='multi_catalog':
        checks['all_selected_zones']=all(x.casefold() in answer.casefold() for x in case['required'])
        checks['no_unselected_zones']=not any(x.casefold() in answer.casefold() for x in case['forbidden'])
        checks['catalog_operation']='game' in mode or 'multi_question_splitter' in mode
    elif kind=='wrong_edition':
        checks['not_other_edition']='structured_game_controls' not in mode and not ('TEKKEN 8 controls:' in answer or 'TEKKEN 8 มีปุ่ม' in answer)
        checks['not_missing_target']='missing_game_context' not in mode
        checks['not_catalog']='catalog' not in mode
        checks['source_status']=any(x in answer.casefold() for x in ['not','unverified','could not','ยัง','ไม่พบ'])
    elif kind=='new_detail':
        checks['new_operation']='game_detail' in mode and 'controls' not in mode
    elif kind=='partial_controls':
        checks['known_target_answered']=all(x.casefold() in answer.casefold() for x in case['required'])
        checks['partial_explicit']='multi_question_splitter' in mode and any(x in answer.casefold() for x in ['not have verified','could not','ไม่พบ','ยังไม่'])
        checks['not_substituted_edition']='TEKKEN 8 controls:' not in answer
    elif kind=='unresolved_selection':
        checks['not_partial_silently']='structured_games_catalog' not in mode and 'structured_service_game_availability' not in mode
        checks['explicit_clarification']='selection_clarification' in mode
    elif kind=='selected_requests':
        checks['expected_requests']=all(x.casefold() in answer.casefold() for x in case.get('required',[]))
        checks['no_dropped_parts']='multi_question_splitter' in mode
        children=[t for t in trace if t.get('stage')=='multi_question_child']
        wanted=case.get('expected_domains', ['reservation','service_fee'] if 'booking' in case['id'] else ['games','service_fee'])
        checks['child_operations']={t.get('decision','').split('/')[0] for t in children}==set(wanted)
        checks['no_missing_known_target']=all('missing_game_context' not in t.get('metadata',{}).get('mode','') for t in children)
    elif kind=='selection_limit':
        checks['safe_limit']='selection_clarification' in mode
        checks['explicit_limit']=any(x in answer.casefold() for x in ['at most 4','up to 4','ไม่เกิน 4'])
    elif kind=='resume_catalog':
        checks['selected_zones']=all(x in answer for x in case['required'])
        checks['no_extra_zone']=not any(x in answer for x in case.get('forbidden',[]))
    elif kind=='unknown_controls':
        checks['no_substitute']='structured_game_controls' not in mode and 'catalog' not in mode
        checks['received_name']='missing_game_context' not in mode
        checks['keeps_operation']='control' in mode
    elif kind=='not_generic_controls':
        checks['not_generic_controls']='missing_game_context' not in mode
        if case['id']=='booking-button-not-controls-en':
            checks['booking_not_game']='control' not in mode and 'booking' in mode
        if case['id']=='explicit-reject-th':
            checks['price_selected_pc']=('service_fee' in mode and 'PC' in answer)
    return dict(id=case['id'],kind=kind,passed=all(checks.values()),checks=checks,mode=mode,answer=answer,latency=[x.get('elapsed_sec') for x in records],records=records)

def run(port,label):
    runid=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]
    raw=OUT/f'{label}_{runid}_raw.jsonl'; results=[]
    with urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=5) as r: health=json.load(r)
    for c in cases():
        session='r40-'+str(uuid.uuid4()); ack=''; records=[]
        for q in c['turns']:
            payload=dict(question=q,locale=c['locale'],client_session_id=session,client_turn_id=str(uuid.uuid4()),last_seen_response_id=ack,debug=True)
            start=time.perf_counter(); record=dict(case_id=c['id'],payload=payload)
            try:
                req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
                with urllib.request.urlopen(req,timeout=40) as r: record.update(status=r.status,response=json.load(r))
            except urllib.error.HTTPError as e:
                record.update(status=e.code,response=json.loads(e.read().decode('utf-8')))
            except Exception as e:
                record.update(status=0,response={},error=type(e).__name__+': '+str(e))
            record['elapsed_sec']=round(time.perf_counter()-start,4)
            with raw.open('a',encoding='utf-8') as f: f.write(json.dumps(record,ensure_ascii=False)+'\n')
            ack=record['response'].get('request_id','');records.append(record)
        result=grade(c,records);results.append(result)
        print(c['id'],'PASS' if result['passed'] else 'FAIL',result['mode'],[k for k,v in result['checks'].items() if not v],flush=True)
    summary=dict(label=label,port=port,health=health,planned_cases=len(cases()),executed_cases=len(results),requests=sum(len(r['records']) for r in results),passed=sum(r['passed'] for r in results),failed=sum(not r['passed'] for r in results),raw_file=raw.name,results=results)
    file=OUT/f'{label}_{runid}_summary.json'
    with file.open('x',encoding='utf-8') as f: json.dump(summary,f,ensure_ascii=False,indent=2)
    print('SUMMARY',str(file),summary['passed'],'/',summary['executed_cases'],flush=True)

if __name__=='__main__':
    run(int(sys.argv[1]),sys.argv[2])
