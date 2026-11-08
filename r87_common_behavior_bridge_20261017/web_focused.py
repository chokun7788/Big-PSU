"""Installed common/LLM ON HTTP checks only. Never runs a full corpus."""
import ast,hashlib,json,statistics,sys,time,uuid
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
sys.path.insert(0,str(B.parent/'r82_automatic_llm_check_20261017'))
from auto_test import Runner,selected_audit,binding_rejection
from contracts import CASES,check

def main():
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]
 T=B/'web_results'/stamp;T.mkdir(parents=True,exist_ok=False);runner=Runner(T)
 install=json.loads((B/('INSTALLATION_2.json' if (B/'INSTALLATION_2.json').exists() else 'INSTALLATION.json')).read_text(encoding='utf8'))
 if not all(hashlib.sha256((S/name).read_bytes()).hexdigest()==digest for name,digest in install['installed_files'].items()):raise RuntimeError('Installed source changed after verification')
 db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
 rows=[];obstacle=None
 try:
  health=runner.ensure_chat()
  tags=runner.get('model_list','http://127.0.0.1:11434/api/tags')
  runner.ensure_model(tags,health['body']['runtime']['local_llm']['model'])
  for case,lang,turns in CASES:
   sid='r87-'+uuid.uuid4().hex
   for question,expect in turns:
    response=runner.get('chat_'+str(len(rows)+1),'http://127.0.0.1:8115/api/chat',payload={'question':question,'locale':lang,'client_session_id':sid,'client_turn_id':uuid.uuid4().hex,'debug':True},timeout=30)
    body=response.get('body') if isinstance(response.get('body'),dict) else {};audit=selected_audit(body)
    errors=check(body,expect) if response.get('http_ok') else ['http_failure']
    model_errors=[x for x in [audit.get('availability_failure'),binding_rejection(body)] if x]
    row={'case':case,'locale':lang,'question':question,'expect':expect,'passed':not errors,'errors':errors,'model_errors':model_errors,**response};rows.append(row)
    with (T/'TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(json.dumps({'case':case,'passed':not errors,'errors':errors,'model_errors':model_errors,'seconds':response['elapsed_seconds'],'proposal_only':audit.get('topic_proposal_only')},ensure_ascii=False),flush=True)
    if not response.get('http_ok'):raise RuntimeError('Chat request failed; partial results retained')
 except Exception as error:obstacle={'type':type(error).__name__,'message':str(error)};print(str(error),flush=True)
 result={'count':len(rows),'expected_count':sum(len(turns) for _,_,turns in CASES),'passed':sum(x['passed'] for x in rows),'llm_on':True if not obstacle else None,'real_model_generation_verified':any(p.get('step')=='real_model_generation' and p.get('http_ok') for p in runner.steps),'full_corpus':False,'database_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest(),'model_calls':sum(selected_audit(x.get('body') or {}).get('attempted') is True for x in rows),'proposal_calls':sum(bool(selected_audit(x.get('body') or {}).get('topic_proposal_only')) for x in rows),'model_failures':[{'case':x['case'],'question':x['question'],'errors':x['model_errors']} for x in rows if x['model_errors']],'answer_failures':[{'case':x['case'],'question':x['question'],'errors':x['errors']} for x in rows if x['errors']],'obstacle':obstacle}
 result['by_language']={lang:{'count':sum(x['locale']==lang for x in rows),'passed':sum(x['locale']==lang and x['passed'] for x in rows),'median_seconds':statistics.median([x['elapsed_seconds'] for x in rows if x['locale']==lang]) if any(x['locale']==lang for x in rows) else None} for lang in ('th','en')}
 with (T/'SUMMARY.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
 print(json.dumps({'result':result,'output':str(T)},ensure_ascii=False))
 return 0 if not obstacle and result['count']==result['expected_count']==result['passed'] and not result['model_failures'] else 1
if __name__=='__main__':raise SystemExit(main())
