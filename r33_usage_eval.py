import json,sys,time,re,urllib.request,uuid,collections
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r33_report_path.txt').read_text().strip());run=sys.argv[1];port=int(sys.argv[2]) if len(sys.argv)>2 else 0
import r33_full as runner
from app.core.intent_cue_recovery import recover_intent_cues
fixture=sys.argv[3] if len(sys.argv)>3 else 'R33_INDEPENDENT_USAGE_ORACLE.json'
cases=json.loads((R/fixture).read_text(encoding='utf-8'))['cases']
negative=[
'PS5 ราคาเท่าไร','PC Zone รอบละกี่นาที','VR Zone รอบละกี่นาที','PS5 3 ชั่วโมงราคาเท่าไหร่',
'PC3 10:00 ไม่ว่างไหม','PC1 12:00-13:00 ว่างไหม','2026-10-03 PC1 ว่างไหม',
'What is the cost for PC2 at 10:00','Can I pay for VALORANT','rice','march','Who are the Embers',
'What position does Mr. Gaming Person hold','VALORANT ไม่ได้อนุญาต macros ใช่ไหม',
'VR 30 นาทีไม่ใช่ 60 นาที ราคาเท่าไหร่','VR รอบละกี่นาที','ไม่เอาอาหารเข้าได้ไหม',
'Roblox เล่นไม่ได้ใช่ไหม','Who is Mr. Studio Man','not a PSU student PC 2 hours price',
'PS5 ราคา 150 บาทถูกไหม','เทียบ PC1 กับ PC2 ตอน 13:00','Can I book this','What are the studio rules',
]
start=time.perf_counter();records=[]
if port:
    for attempt in range(20):
        try:
            health=json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=3))
            assert health['runtime']['version']=='2026.10.02-usable-task-frames-r33'
            break
        except Exception:
            if attempt==19:raise
            print('Waiting for the verified test server to be ready',flush=True);time.sleep(3)
with (R/(run+'_usage_results.jsonl')).open('x',encoding='utf-8') as out:
    for c in cases:
        t=time.perf_counter()
        if port:
            payload=dict(question=c['question'],locale=c['locale'],recent_history=[],client_session_id='r33-usage-'+uuid.uuid4().hex,debug=True,experimental_allow_llm=True,experimental_rag_fallback=True)
            try:
                raw=json.load(urllib.request.urlopen(urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30));answer=raw['answer'];mode=raw['mode'];valid=raw.get('validation_ok',True)
            except Exception as e:raw=dict(exception=str(e));answer='';mode='';valid=False
        else:
            x=runner.execute(dict(key=c['id'],question=c['question'],locale=c['locale'],reference_date='',entries=[]));raw=x.get('result',{});answer=raw.get('answer','');mode=raw.get('mode','');valid=raw.get('validation',{}).get('ok',False)
        errors=[]
        for group in c['groups']:
            if not any(word.casefold() in answer.casefold() for word in group):errors.append('missing_content:'+str(group))
        for word in c['forbidden']:
            if word.casefold() in answer.casefold():errors.append('forbidden_content:'+word)
        if c['mode'] and not mode.startswith(c['mode']):errors.append('wrong_mode:'+mode)
        if not valid:errors.append('validation_or_transport')
        rec=dict(case=c,response=raw,elapsed=time.perf_counter()-t,passed=not errors,failures=errors);records.append(rec);out.write(json.dumps(rec,ensure_ascii=False)+'\n');out.flush()
        print(json.dumps(dict(id=c['id'],passed=not errors,errors=errors,answer=answer[:210]),ensure_ascii=False),flush=True)
controls=[dict(question=q,recovered=recover_intent_cues(q)) for q in negative]
for c in controls:c['unchanged']=c['question']==c['recovered']
with (R/(run+'_negative_literal_controls.json')).open('x',encoding='utf-8') as out:json.dump(controls,out,ensure_ascii=False,indent=2)
summary=dict(total=len(records),passed=sum(x['passed'] for x in records),negative_total=len(controls),negative_unchanged=sum(x['unchanged'] for x in controls),elapsed=time.perf_counter()-start,port=port,scope='source/content assertions plus separate literal preservation; assistant-written, not owner-approved')
with (R/(run+'_usage_summary.json')).open('x',encoding='utf-8') as out:json.dump(summary,out,ensure_ascii=False,indent=2)
print(summary)
