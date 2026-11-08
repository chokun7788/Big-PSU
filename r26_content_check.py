"""Independent proposition checks: source conditions, units, scope and absence.

Fixture assertions are explicit; they are not computed from the answer renderer.
The source snapshot and raw answers remain available for review.
"""
import hashlib, json, os, sys, time, urllib.request
from pathlib import Path

project = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report = Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
sys.path.insert(0, str(project))
os.environ['PSU_BILINGUAL_EN_ENABLED'] = '1'
os.environ['PSU_SEMANTIC_RETRIEVAL'] = '0'
from app.pipeline.engine import answer_question_pipeline_debug

anchors = [
 ('team-th', 'th', 'กติกา CS2 ทีมหนึ่งมีผู้เล่นกี่คน', 'cs2_psu_phuket_2026', ['5 คน'], [], ['5 คน']),
 ('team-en', 'en', 'How many players are in a CS2 team?', 'cs2_psu_phuket_2026', ['5 players'], [], ['5 players']),
 ('format-th', 'th', 'กติกา Tekken 8 รูปแบบการแข่งขันเป็นอย่างไร', 'tekken8_psu_esports', ['FT2','2 เกม'], ['VALORANT'], []),
 ('format-en', 'en', 'What is the Tekken 8 tournament format?', 'tekken8_psu_esports', ['FT2','two games'], ['VALORANT'], []),
 ('settings-th', 'th', 'กติกา Tekken 8 การตั้งค่าเกมเป็นยังไง', 'tekken8_psu_esports', ['3','60 วินาที'], ['VALORANT'], ['3']),
 ('settings-en', 'en', 'What are the Tekken 8 in-game settings?', 'tekken8_psu_esports', ['3','60 seconds'], ['VALORANT'], ['3']),
 ('ipad-th', 'th', 'กติกา RoV ใช้ Tablet หรือ iPad ได้ไหม', 'rov_blueket_2025_men', ['ไม่อนุญาต','ตัดสิทธิ์'], ['Global Ban'], []),
 ('ipad-en', 'en', 'Can I use a tablet or iPad in the RoV tournament?', 'rov_blueket_2025_men', ['may not be used','disqualification'], ['Global Ban'], ['may not be used','disqualification']),
 ('comm-th', 'th', 'VALORANT technical pause สื่อสารได้ไหม', 'valorant_psu_phuket_2026', ['ห้าม','สื่อสาร','เว้นแต่ได้รับอนุญาต'], ['60','Tactical','Major Bug','10 นาที','10 minutes'], ['ห้าม','เว้นแต่ได้รับอนุญาต']),
 ('comm-en', 'en', 'Can players communicate during a VALORANT technical pause?', 'valorant_psu_phuket_2026', ['may not communicate','unless permitted'], ['60','Tactical','Major Bug','10 minutes'], ['may not communicate','unless permitted']),
 ('duration-th', 'th', 'VALORANT technical pause ได้กี่นาที', 'valorant_psu_phuket_2026', ['ยังไม่พบข้อกฎ'], ['60','2 timeouts','Tactical','10 นาที','10 minutes'], []),
 ('duration-en', 'en', 'How long is a VALORANT technical pause?', 'valorant_psu_phuket_2026', ['could not find a clause'], ['60','2 timeouts','Tactical','10 minutes'], []),
 ('table-th', 'th', 'ขอตารางบทลงโทษ CS2', 'cs2_psu_phuket_2026', ['| การหมิ่นศาสนา | แบนถาวร |','| ดูสตรีมระหว่างแข่ง | ปรับแพ้ในแมตช์นั้น |','| หยุดเกมโดยไม่ได้รับอนุญาต | ปรับแพ้ในรอบนั้น |'], [], []),
 ('table-en', 'en', 'Show the CS2 penalty table', 'cs2_psu_phuket_2026', ['| Offensive religious remarks | Permanent ban |','| Watching streams during gameplay | Loss in that match |','| Stopping the game without permission | Loss in that round |'], [], []),
 ('penalties-th', 'th', 'กติกา VALORANT มีบทลงโทษประเภทไหนบ้าง', 'valorant_psu_phuket_2026', ['Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit','ระบุเจตนาไม่ได้','เจตนาใช้ช่องโหว่','ความผิดครั้งแรก','ความผิดซ้ำ','ล็อกผล'], [], []),
 ('penalties-en', 'en', 'What do the VALORANT tournament rules say about penalties?', 'valorant_psu_phuket_2026', ['Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit','intent cannot be determined','intentional','first','repeated','Match fixing'], [], []),
]

def fixture():
    rows=[]
    for key,locale,q,game,required,forbidden,first in anchors:
        variants = [q, 'สอบถามหน่อยครับ '+q+' ครับ', 'อยากทราบว่า '+q+' หน่อย', 'ขอถาม '+q+' นะครับ', 'สอบถามหน่อยครับ '+q.replace('กติกา','กติกกา')+' ครับ'] if locale=='th' else [q, 'Hello, '+q, 'Could you help me? '+q, 'Please explain: '+q, 'Hi, '+q.replace('rules','ruls').replace('tournament','tournamment')]
        for index,question in enumerate(variants):
            rows.append(dict(id=f'{key}-{index}',anchor=key,locale=locale,question=question,game=game,required=required,forbidden=forbidden,first=first))
    return rows

def evaluate(case, answer, mode, category, hits, validation):
    failures=[]
    first=answer.splitlines()[0] if answer else ''
    for term in case['required']:
        if term.casefold() not in answer.casefold():failures.append('missing:'+term)
    for term in case['first']:
        if term.casefold() not in first.casefold():failures.append('missing_first:'+term)
    for term in case['forbidden']:
        if term.casefold() in answer.casefold():failures.append('wrong_scope:'+term)
    if category!='competition_rules':failures.append('wrong_category')
    if not hits or any(case['game'] not in str(h.get('id',''))+str(h.get('url','')) for h in hits):failures.append('wrong_source')
    if not validation:failures.append('validation_rejected')
    if case['anchor'].startswith('table'):
        if len([line for line in answer.splitlines() if line.startswith('|')])!=11:failures.append('table_not_nine_pairs')
    if case['anchor'].startswith('penalties'):
        for term in ('Warning','Round Rollback','Round Loss','Map Forfeit','Match Forfeit'):
            if answer.count(term)!=1:failures.append('type_missing_or_duplicate:'+term)
    if case['anchor'].startswith('duration') and 'no_answer' not in mode:
        failures.append('absence_answer_has_fact_mode')
    if case['anchor'].startswith('format') and not any(term in first for term in ('1v1','FT2')):
        failures.append('format_first_sentence_not_format')
    return failures

if __name__=='__main__':
    run=sys.argv[1];port=sys.argv[2] if len(sys.argv)>2 else None
    cases=fixture()
    fixture_path=report/'proposition_fixture_80_v3.json'
    if not fixture_path.exists():
        sources=[json.loads(line) for line in (project/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
        with fixture_path.open('x',encoding='utf-8') as f:json.dump({'scope':'80 constructed regression cases, 16 anchors; explicit source assertions; assistant review, not owner approval','cases':cases,'source_snapshot':[dict(row,sha256=hashlib.sha256(row['text'].encode()).hexdigest()) for row in sources]},f,ensure_ascii=False,indent=2)
    records=[]
    for case in cases:
        started=time.perf_counter()
        if port:
            payload={'question':case['question'],'locale':case['locale'],'recent_history':[],'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
            response=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:'+port+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
            answer=response['answer'];mode=response['mode'];category=response['route_category'];hits=response.get('sources',[]);validation=response.get('validation_ok',True)
        else:
            result=answer_question_pipeline_debug(case['question'],locale=case['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=12)
            response={'answer':result.answer,'mode':result.mode,'route_category':result.route.category,'hits':result.hits,'trace':[vars(item) for item in result.trace],'validation':vars(result.validation)}
            answer=result.answer;mode=result.mode;category=result.route.category;hits=result.hits;validation=result.validation.ok
        failures=evaluate(case,answer,mode,category,hits,validation)
        record={'case':case,'elapsed_sec':round(time.perf_counter()-started,4),'failures':failures,'response':response}
        records.append(record)
        print(json.dumps({'id':case['id'],'elapsed':record['elapsed_sec'],'failures':failures},ensure_ascii=False),flush=True)
    summary={'run':run,'http_port':port,'total':len(records),'passed':sum(not r['failures'] for r in records),'cases':records}
    with (report/(run+'_content.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
    print(json.dumps({k:v for k,v in summary.items() if k!='cases'},ensure_ascii=False))
    sys.exit(summary['passed']!=summary['total'])
