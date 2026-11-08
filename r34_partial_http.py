import json,sys,re,urllib.request,uuid
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r34_report_path.txt').read_text().strip());base='http://127.0.0.1:'+sys.argv[1];run=sys.argv[2];oracle=json.loads((Path((ROOT/'r32_report_path.txt').read_text().strip())/'R32_POSITIVE_SOURCE_ORACLE.json').read_text(encoding='utf-8'));records=[]
with (R/(run+'_partial_http.jsonl')).open('x',encoding='utf-8') as f:
 for l in ['th','en']:
  source=next(c for c in oracle['cases'] if c['id']==f'cs2-17-{l}-0')
  clauses=[c for c in source['clauses'] if re.search(r'เปิดรับเฉพาะ|General eligibility',c,re.I)]
  cases=[('กติกา CS2 คุณสมบัติและอายุขั้นต่ำคืออะไร',True),('กติกา CS2 คุณสมบัตและอายุขั้นต่ำคืออะไร',True),('กติกา CS2 อายุขั้นต่ำคืออะไร',False),('กติกา CS2 คุณสมบัติ ค่าสมัคร และอายุขั้นต่ำคืออะไร',True)] if l=='th' else [('What are CS2 tournament eligibility and minimum age requirements?',True),('What are CS2 tournament eligibiliyt and minimum age requirements?',True),('What is the CS2 tournament minimum age?',False),('What are CS2 tournament eligibility, registration fee and minimum age requirements?',True)]
  for q,partial in cases:
   payload=dict(question=q,locale=l,recent_history=[],client_session_id='r32-partial-'+uuid.uuid4().hex,experimental_allow_llm=True,experimental_rag_fallback=True,debug=True)
   raw=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30));errors=[];answer=raw['answer'];flat=lambda x:re.sub(r'\s+',' ',x).casefold()
   if partial:
    if 'partial_source' not in raw.get('mode',''):errors.append('not_partial')
    for c in clauses:
     if flat(c) not in flat(answer):errors.append('missing_complete_eligibility_clause')
    if not any(h['id'].endswith('s17_c01') for h in raw.get('sources',[])):errors.append('eligibility_source_missing')
   elif raw.get('sources'):errors.append('age_only_invented_evidence')
   if not ('ยังไม่พบข้อมูลอายุขั้นต่ำ' in answer or 'could not find a verified minimum-age' in answer):errors.append('missing_age_gap_disclosure')
   if ('fee' in q or 'ค่าสมัคร' in q) and not ('registration-fee' in answer or 'ยังไม่พบข้อมูลค่าสมัคร' in answer):errors.append('missing_fee_gap_disclosure')
   if re.search(r'minimum age is|อายุขั้นต่ำคือ\s*\d',answer,re.I):errors.append('invented_age')
   row=dict(question=q,locale=l,partial_expected=partial,expected_source_clauses=clauses if partial else [],passed=not errors,errors=errors,response=raw);records.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
with (R/(run+'_partial_http_summary.json')).open('x',encoding='utf-8') as f:json.dump(dict(total=len(records),passed=sum(x['passed'] for x in records),scope='Source-derived complete eligibility clause plus explicit age/fee gap, not an invented age threshold',failures=[dict(question=x['question'],errors=x['errors']) for x in records if not x['passed']]),f,ensure_ascii=False,indent=2)
print(json.dumps({'total':len(records),'passed':sum(x['passed'] for x in records),'failures':[x['errors'] for x in records if not x['passed']]}),flush=True)
