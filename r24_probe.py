from pathlib import Path
import json, sys, uuid, urllib.request, time, hashlib

ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
REPORT=ROOT/'reports'/('r24_competition_'+time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6])
REPORT.mkdir()
Path(__file__).with_name('r24_report_path.txt').write_text(str(REPORT),encoding='utf-8')
qs=['กฏตอนเเข่ง cs2 มีอะไรมั่ง','กฏตอนเเข่ง rov มีอะไรมั่ง','กฏตอนเเข่ง tekken 8 มีอะไรมั่ง','กฏตอนแข่งวาโลมีอะไรมั่ง']
records=[]
for path in (ROOT/'owner_local_delivery_20261001_available_equipment_r23/PSU_Esports_Chatbot_Local/data/logs').rglob('*.jsonl'):
    for line in path.open(encoding='utf-8'):
        try: row=json.loads(line)
        except ValueError: continue
        if row.get('question') in qs:
            records.append(row)
            print(json.dumps({'log':str(path.relative_to(ROOT)), 'question':row.get('question'),'mode':row.get('mode'),'input_quality':row.get('input_quality'), 'traces':[t for t in row.get('trace',[]) if t.get('stage') in {'preprocess','query_understanding','query_recovery','context_rewrite','competition_target_guard','retrieval','keyboard_neighbor_recovery','semantic_phrase_recovery','intent_cue_recovery','surface_recovery'}]},ensure_ascii=False))
(REPORT/'original_log_matches.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
fresh=[]
for q in qs:
    data={'question':q,'locale':'th','debug':True,'client_session_id':'r24-baseline-'+uuid.uuid4().hex,'recent_history':[], 'experimental_allow_llm':True,'experimental_rag_fallback':True}
    started=time.perf_counter()
    response=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8090/api/chat',json.dumps(data,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
    fresh.append({'question':q,'response':response,'elapsed':time.perf_counter()-started})
    print(json.dumps({'fresh_question':q,'answer':response.get('answer'),'mode':response.get('mode'),'quality':response.get('input_quality'),'stages':[{'stage':t['stage'],'decision':t.get('decision'),'detail':t.get('detail'),'metadata':t.get('metadata')} for t in response.get('trace',[]) if any(s in t['stage'] for s in ('recover','preprocess','target','retrieval','frame'))]},ensure_ascii=False))
(REPORT/'baseline_http.json').write_text(json.dumps(fresh,ensure_ascii=False,indent=2),encoding='utf-8')
print('REPORT='+str(REPORT))
