import os,sys,json,time,uuid,urllib.request,urllib.error
from dataclasses import asdict
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r41_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def cases():
    rows=[]
    for lang in ('th','en'):
        en=lang=='en'
        control='What are the controls for VALORANT?' if en else 'VALORANT มีปุ่มอะไรบ้าง'
        price='PC prices for external users' if en else 'ราคา PC ของบุคคลภายนอก'
        rules='Competition rules for CS2' if en else 'กฎการแข่งขัน CS2'
        rows.extend([
          dict(id=lang+'-all-controls',locale=lang,turns=[control,'all of them' if en else 'ทั้งหมด'],kind='controls',required=['VALORANT','W']),
          dict(id=lang+'-resume-controls',locale=lang,turns=[control,price,'back to the controls' if en else 'กลับไปเรื่องปุ่มเมื่อกี้'],kind='controls',required=['VALORANT','W']),
          dict(id=lang+'-resume-price',locale=lang,turns=[price,rules,'back to the prices' if en else 'กลับไปเรื่องราคาเมื่อกี้'],kind='price',required=['PC']),
          dict(id=lang+'-resume-rules',locale=lang,turns=[rules,price,'back to the competition rules' if en else 'กลับไปกฎการแข่งขันเมื่อกี้'],kind='rules',required=['Counter-Strike 2']),
          dict(id=lang+'-resume-catalog',locale=lang,turns=['What games are available in PC?' if en else 'PC มีเกมอะไรบ้าง',rules,'back to the game list' if en else 'กลับไปเรื่องรายชื่อเกม'],kind='catalog',required=['PC Zone'],forbidden=['VR Zone','PlayStation 5 Zone']),
          dict(id=lang+'-new-target-after-controls',locale=lang,turns=[control,'Show PS5 prices' if en else 'ขอราคา PS5'],kind='price',required=['PlayStation 5']),
          dict(id=lang+'-ambiguous-ordinal-catalog',locale=lang,turns=['What games can I play?' if en else 'มีเกมอะไรให้เล่นบ้าง','the first one' if en else 'อันแรก'],kind='clarification'),
          dict(id=lang+'-no-context-all',locale=lang,turns=['all of them' if en else 'ทั้งหมด'],kind='clarification'),
          dict(id=lang+'-no-context-resume',locale=lang,turns=['back to the controls' if en else 'กลับไปเรื่องปุ่มเมื่อกี้'],kind='clarification'),
          dict(id=lang+'-partial-controls',locale=lang,turns=['Show me the game controls' if en else 'ขอดูปุ่มควบคุมเกม','VALORANT and Minecraft' if en else 'VALORANT กับ มายคราฟต์'],kind='partial',required=['VALORANT','W']),
          dict(id=lang+'-complete-multi-controls',locale=lang,turns=['Show me the game controls' if en else 'ขอดูปุ่มควบคุมเกม','VALORANT and Beat Saber' if en else 'VALORANT กับ Beat Saber'],kind='complete_multi',required=['VALORANT','Beat Saber']),
          dict(id=lang+'-all-after-compound',locale=lang,turns=[('What are the controls for VALORANT and what are PC prices?' if en else 'VALORANT มีปุ่มอะไรบ้าง และ PC ราคาเท่าไหร่'),'all of them' if en else 'ทั้งหมด'],kind='clarification'),
        ])
    rows.append(dict(id='explicit-all-zones',locale='en',turns=['What games are available in PC?','all zones'],kind='catalog',required=['PC Zone','PlayStation 5 Zone','Nintendo Switch Zone','Cockpit Zone','VR Zone']))
    return rows

def grade(c,rs):
    b=rs[-1]['response'];mode=b.get('mode','');answer=b.get('answer','');kind=c['kind'];trace=b.get('trace') or []
    contract=b.get('task_contract') or next((t.get('metadata') for t in trace if t.get('stage')=='task_answer_contract'),{}) or {}
    checks={'transport':rs[-1]['status']==200 and b.get('ok') is True,
            'required_content':all(x.casefold() in answer.casefold() for x in c.get('required',[])),
            'forbidden_content':not any(x.casefold() in answer.casefold() for x in c.get('forbidden',[]))}
    if kind=='controls':checks['operation']='structured_game_controls' in mode
    if kind=='price':
        checks['operation']=b.get('route_category')=='service_fee'
        if 'resume-price' in c['id']:
            rows=(b.get('price_contract') or b.get('coverage') or {}).get('rows',[])
            if not rows:
                rows=next((t.get('metadata',{}).get('rows',[]) for t in trace if t.get('stage')=='conversation_contract'),[])
            checks['retained_external_groups']=bool(rows) and {r['group_id'] for r in rows}=={'general_student','general_adult'}
    if kind=='rules':checks['operation']=b.get('route_category')=='competition_rules' and 'clarification' not in mode and 'unconfirmed' not in mode
    if kind=='catalog':
        children=contract.get('tasks',[])
        checks['operation']='catalog' in mode or 'service_game_availability' in mode or (bool(children) and all(t['category']=='games' and ('catalog' in t['mode'] or 'service_game_availability' in t['mode']) for t in children))
    if kind=='clarification':checks['operation']=b.get('route_category')=='clarification' or 'clarification' in mode or 'missing' in mode
    if kind in ('partial','complete_multi'):
        checks['compound']='multi_question_splitter' in mode
        checks['outcome']=contract.get('outcome')==('answered_partial' if kind=='partial' else 'answered_complete')
        checks['task_ids_complete']=contract.get('expected_task_ids')==contract.get('executed_task_ids') and len(contract.get('tasks',[]))==2
        checks['child_statuses']=[t.get('status') for t in contract.get('tasks',[])]==(['answered','missing'] if kind=='partial' else ['answered','answered'])
    return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=mode,answer=answer,records=rs)

def run(kind,label):
    source=kind=='source';runid=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6];raw=OUT/f'{label}_{runid}_raw.jsonl';results=[]
    if source:
        sys.path.insert(0,str(ROOT));os.chdir(ROOT);os.environ.update(PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PSU_CANONICAL_KNOWLEDGE='0',PSU_CHAT_LOG_DIR=str(OUT/'source_logs'))
        from app.session.conversation_store import ConversationStore
        from app.session.context_resolver import ResolvedQuestion,resolve_question_with_context
        from app.pipeline.engine import answer_question_pipeline_debug as answer
    else:
        port=int(kind)
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=6) as r:health=json.load(r)
    for c in cases():
        session='r41-'+uuid.uuid4().hex;ack='';rs=[]
        if source:store=ConversationStore()
        for q in c['turns']:
            turn=uuid.uuid4().hex;start=time.perf_counter();payload=dict(question=q,locale=c['locale'],client_session_id=session,client_turn_id=turn,last_seen_response_id=ack,debug=True)
            if source:
                h=store.history(session);prepared=store.begin(session,turn,q,locale=c['locale'],history=h)
                if prepared.get('context_resolution'):resolved=ResolvedQuestion(**prepared['context_resolution'])
                elif prepared.get('plan'):
                    p=prepared['plan'];resolved=ResolvedQuestion(q,p['resolved_query'],p.get('context_used',False),context_domain='service_fee',context_operation='price_lookup')
                else:resolved=resolve_question_with_context(q,h,locale=c['locale'])
                p=prepared.get('plan') or resolved.to_selection_plan()
                r=answer(resolved.resolved_question,locale=c['locale'],request_plan=p,recent_history=h,experimental_allow_llm=False)
                ts=[asdict(t) for t in r.trace]
                b=dict(ok=True,answer=r.answer,mode=r.mode,route_category=r.route.category,route_intent=r.route.intent,request_id=turn,resolved_question=resolved.resolved_question,context_resolution=asdict(resolved),trace=ts,validation=asdict(r.validation),
                       task_contract=next((t['metadata'] for t in ts if t['stage']=='task_answer_contract'),None))
                store.complete(session,turn,prepared['revision'],b,plan=p);store.acknowledge(session,turn);b['conversation_state']=store.snapshot(session)
                rec=dict(status=200,response=b)
            else:
                try:
                    req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
                    with urllib.request.urlopen(req,timeout=40) as r:rec=dict(status=r.status,response=json.load(r))
                except Exception as e:rec=dict(status=0,response={},error=str(e))
            rec.update(case_id=c['id'],payload=payload,elapsed_sec=round(time.perf_counter()-start,4));rs.append(rec);ack=rec['response'].get('request_id','')
            with raw.open('a',encoding='utf-8') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
        result=grade(c,rs);results.append(result);print(c['id'],'PASS' if result['passed'] else 'FAIL',result['mode'],[k for k,v in result['checks'].items() if not v],flush=True)
    summary=dict(label=label,source=source,executed_cases=len(results),requests=sum(len(r['records']) for r in results),passed=sum(r['passed'] for r in results),raw_file=raw.name,results=results)
    if not source:summary['health']=health
    with (OUT/f'{label}_{runid}_summary.json').open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
    print('SUMMARY',summary['passed'],len(results),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2])
