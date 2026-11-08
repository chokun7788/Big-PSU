import json,sys,urllib.request,uuid,time
from pathlib import Path
R=Path(Path(__file__).with_name('r34_report_path.txt').read_text().strip());base='http://127.0.0.1:'+sys.argv[1];run=sys.argv[2];records=[]
health=json.load(urllib.request.urlopen(base+'/health',timeout=10))
with (R/(run+'_edition_http.jsonl')).open('x',encoding='utf-8') as f:
 for game,have in [('CS2',2026),('RoV',2025),('VALORANT',2026)]:
  for locale in ['th','en']:
   for want in [have,2027,2024,have-1]:
    q=f'กติกา {game} ปี {want} มีอะไรบ้าง' if locale=='th' else f'What are the {game} tournament rules for {want}?'
    payload=dict(question=q,locale=locale,recent_history=[],client_session_id='r32-year-'+uuid.uuid4().hex,debug=True,experimental_allow_llm=True,experimental_rag_fallback=True)
    start=time.perf_counter();raw=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30));errors=[]
    if want==have:
     if not raw.get('sources'):errors.append('matching_year_missing_source')
     if ('ยังยืนยันกติกาฉบับปี' in raw.get('answer','') or 'does not verify the requested' in raw.get('answer','')):errors.append('matching_year_rejected')
    else:
     if raw.get('sources'):errors.append('wrong_edition_rule_claims')
     if str(have) not in raw.get('answer','') or str(want) not in raw.get('answer',''):errors.append('edition_disclosure_missing')
     if not ('ยังยืนยัน' in raw.get('answer','') or 'does not verify' in raw.get('answer','')):errors.append('mismatch_not_disclosed')
    if raw.get('language',{}).get('effective')!=locale:errors.append('locale')
    x=dict(question=q,locale=locale,recorded_year=have,requested_year=want,passed=not errors,errors=errors,response=raw,elapsed=time.perf_counter()-start);records.append(x);f.write(json.dumps(x,ensure_ascii=False)+'\n');f.flush()
with (R/(run+'_edition_http_summary.json')).open('x',encoding='utf-8') as f:json.dump(dict(health=health,total=len(records),passed=sum(x['passed'] for x in records),cases=[{k:v for k,v in x.items() if k!='response'} for x in records]),f,ensure_ascii=False,indent=2)
print(json.dumps({'total':len(records),'passed':sum(x['passed'] for x in records),'failures':[x['errors'] for x in records if not x['passed']]}),flush=True)
