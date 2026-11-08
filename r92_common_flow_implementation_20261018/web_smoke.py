"""Small installed HTTP contract check; never launches a full corpus."""
import hashlib,json,sys,uuid
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(B.parent/'r82_automatic_llm_check_20261017'))
from auto_test import Runner,c
runner=Runner(T);db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
health=runner.get('installed_health','http://127.0.0.1:8115/health')
assert health['http_ok'] and c.verify_health(health['body'],c.fingerprint()),'Installed fingerprint / LLM ON is not verified'
assert health['body']['common_loaded_build']['build_id']=='common-r92-task-contracts'
rows=[];sessions={'pc':'r92-'+uuid.uuid4().hex}
cases=[
 ('typo-overview','th','The Legend of Zelda: Breath of the Wild คือกมอะๆร','summary',None),
 ('how-to','en','Beat Saber how do you play?','how_to_play',None),
 ('new-wording','en','Could you please give me a beginner-friendly introduction to Beat Saber?','summary',None),
 ('compound','en','Beat Saber game overview and price','compound',None),
 ('pc-clarification','th','PC มีอะไรบ้าง','pc_menu','pc'),
 ('pc-followup','th','อุปกรณ์','equipment','pc'),
 ('faq-policy','en','What is the policy for Friday maintenance?','answer',None),
]
for name,lang,q,expect,session in cases:
 response=runner.get('chat_'+name,'http://127.0.0.1:8115/api/chat',payload={'question':q,'locale':lang,'client_session_id':sessions[session] if session else 'r92-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'debug':True},timeout=35)
 body=response.get('body') or {};art=body.get('decision_artifact') or {};plan=art.get('query_plan') or {};ledger=art.get('need_ledger') or {};a=body.get('answer','')
 errors=[]
 if not response['http_ok'] or not body.get('validation_ok'):errors.append('http_or_validation_failure')
 if expect=='equipment':ok=plan.get('operation')=='equipment' and len(plan.get('record_ids',[]))>=5
 elif expect=='pc_menu':ok='อุปกรณ์และสเปก' in a and 'เวลาเล่นต่อรอบ' not in a
 elif expect=='compound':ok=ledger.get('total_needs')==2 and ledger.get('answered_needs')>=1 and 'rhythm' in a.lower() and art.get('response_type')=='partial_answer'
 else:ok=expect in plan.get('requested_fields',[]) and any(o.get('field')==expect and o.get('status')=='known' for o in art.get('obligations',[]))
 if not ok:errors.append('answer_contract_failed')
 rows.append({'case':name,'language':lang,'question':q,'passed':not errors,'errors':errors,**response})
 with (T/'TURNS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(rows[-1],ensure_ascii=False)+'\n')
 print(json.dumps({'case':name,'passed':not errors,'seconds':response['elapsed_seconds'],'answer':a[:220]},ensure_ascii=False),flush=True)
summary={'count':len(rows),'passed':sum(r['passed'] for r in rows),'failed':[r['case'] for r in rows if not r['passed']],'installed_build_verified':True,'llm_enabled':True,'full_test':False,'database_unchanged':hashlib.sha256(db.read_bytes()).hexdigest()==before,'loaded_fingerprint':health['body']['common_loaded_build']['loaded_source_sha256']}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf-8');print(json.dumps(summary));sys.exit(bool(summary['failed']))
