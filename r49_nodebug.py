import sys,json,re,time,uuid,urllib.request
import r49_probe as r
all_cases=r.cases
def cases():return [c for c in all_cases() if c['family'] in {'followup','ambiguity'} or c['id'].endswith('topic-reset')]
def grade(c,rs):
 b=rs[-1]['response'];a=b.get('answer','');contract=b.get('task_contract') or {}
 expected=c.get('claims',[]);required=[v for key in expected for v in r.old.CONTENT[key][c['locale']=='en']]
 checks=dict(transport=all(x['status']==200 and x['response'].get('ok') for x in rs),debug_is_off=all(x['payload']['debug'] is False for x in rs),private_trace_not_exposed='trace' not in b and 'context_resolution' not in b,content=all(x.casefold() in a.casefold() for x in required),english_no_thai=not re.search('[\u0e00-\u0e7f]',a) if c['locale']=='en' else True,no_timeout=not b.get('timed_out'))
 if c.get('missing'):
  checks['missing_is_explicit']=bool(re.search(r'ยังไม่ได้|ยังต้องยืนยัน|not[^\n]*(?:confirmed|specified)|need[^\n]*clarification',a,re.I))
  checks['not_complete']=contract.get('outcome') in {'answered_partial','no_answer'}
 if c.get('scope_kind')=='clarification':checks['clarification']=b.get('route_category')=='clarification'
 if c.get('scope_kind')=='not_user_facts':checks['no_parking_replay']='Building 5' not in a and 'หน้าตึก 5' not in a
 return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=b.get('mode'),answer=a,records=rs)
if __name__=='__main__':
 port=int(sys.argv[1]);label=sys.argv[2];runid=time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]
 raw=r.OUT/f'{label}_{runid}_raw.jsonl';results=[]
 with urllib.request.urlopen(f'http://127.0.0.1:{port}/health',timeout=6) as response:health=json.load(response)
 for c in cases():
  session='r49-public-'+uuid.uuid4().hex;ack='';records=[]
  for q in c['turns']:
   start=time.perf_counter();payload=dict(question=q,locale=c['locale'],client_session_id=session,client_turn_id=uuid.uuid4().hex,last_seen_response_id=ack,debug=False)
   try:
    req=urllib.request.Request(f'http://127.0.0.1:{port}/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=40) as response:rec=dict(status=response.status,response=json.load(response))
   except Exception as error:rec=dict(status=0,response={},error=str(error))
   rec.update(case_id=c['id'],payload=payload,elapsed_sec=round(time.perf_counter()-start,4));records.append(rec);ack=rec['response'].get('request_id','')
   with raw.open('a',encoding='utf-8') as stream:stream.write(json.dumps(rec,ensure_ascii=False)+'\n')
  result=grade(c,records);results.append(result);print(c['id'],'PASS' if result['passed'] else 'FAIL',result['mode'],[key for key,value in result['checks'].items() if not value],flush=True)
 summary=dict(label=label,source=False,debug=False,executed_cases=len(results),requests=sum(len(x['records']) for x in results),passed=sum(x['passed'] for x in results),raw_file=raw.name,results=results,health=health)
 with (r.OUT/f'{label}_{runid}_summary.json').open('x',encoding='utf-8') as stream:json.dump(summary,stream,ensure_ascii=False,indent=2)
 print('SUMMARY',summary['passed'],len(results),flush=True)
