import dataclasses,json,os,sys,time
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';tag=sys.argv[1];T=B/'verification'/tag;T.mkdir(parents=True,exist_ok=False)
candidate='baseline' not in tag
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_CHAT_LOG_DIR=str(T/'logs'))
sys.path.insert(0,str(S));import app.knowledge.common as pkg
if candidate:pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import value
from app.knowledge.common.dialogue import state_from_answer
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
records=MigratedView(S/'data/knowledge/common.sqlite').snapshot()['release']['records'];checks=[]
def ask(q,lang='th',history=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model/network calls in deterministic contract suite')):
  return answer(q,locale=LocaleDecision(lang,lang,lang,1,'explicit'),history=history or [],allow_llm=False)
def record(case,q,r,ok):
 row={'case':case,'question':q,'passed':bool(ok),'result':dataclasses.asdict(r)};checks.append(row)
 with (T/'RESULTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(case, bool(ok), flush=True)
def hist(q,r):return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r) or {},'delivery_status':'server_written'}]
games=[r for r in records.values() if r['kind']=='game' and any(s in str(value(r,'title')) for s in ['Breath of the Wild','Animal Crossing: New Horizons','Beat Saber']) and value(r,'summary')]
assert len(games)==3,len(games)
for g in games:
 title=value(g,'title');summary=value(g,'summary')
 for lang,patterns in [('th',['{} คือเกมอะไร','{} คือกมอะๆร','{} เป็นเกมอะไร','{} คือเกเกมอะไร','{} คือเกมอะไ','{} เล่นยังไง']),('en',['What is {}?','{} what is this game?','{} what is this gmae?','{} game overview','{} how to play','{} how do you play?'])]:
  for j,fmt in enumerate(patterns):
   q=fmt.format(title[lang]);r=ask(q,lang);field='how_to_play' if j==5 and lang=='th' or j>=4 and lang=='en' else 'summary';expect=value(g,field)
   ok=r.validation.ok and any(h.get('record_id')==g['record_id'] and h.get('field')==field for h in r.hits)
   if isinstance(expect,dict) and expect.get(lang):ok=ok and expect[lang] in r.answer
   record(g['record_id']+'_'+lang+'_'+str(j),q,r,ok)
for lang,first,replies in [('th','PC มีอะไรบ้าง',['อุปกรณ์','รายการอุปกรณ์','มีอุปกรณ์อะไรบ้าง']),('en','What does PC have?',['equipment','hardware','equipment list','what equipment is there'])]:
 first_answer=ask(first,lang)
 for i,q in enumerate(replies):
  r=ask(q,lang,hist(first,first_answer));p=r.decision_artifact.get('query_plan') or {}
  record('followup_'+lang+'_'+str(i),q,r,r.validation.ok and p.get('operation')=='equipment' and len({h['record_id'] for h in r.hits if records[h['record_id']]['kind']=='equipment_model'})>=5)
for i,q in enumerate(['What is the studio policy for friday maintenance','What is the policy for Friday maintenance?','Friday maintenance what is the policy?']):
 r=ask(q,'en');record('faq_policy_'+str(i),q,r,r.validation.ok and any(h.get('record_id')=='migrated_faq_rule_schedule_friday_maintenance' and h.get('field')=='answer' for h in r.hits))
for i,(q,lang) in enumerate([('General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท','th'),('เหมา PC 5 ชั่วโมงเท่าไหร่','th'),('กติกา CS2 ต้องประท้วงภายในกี่นาที แล้วใช้ภาษาอะไร','th')]):
 r=ask(q,lang);a=r.decision_artifact;p=a.get('query_plan') or {}
 ok=(a.get('response_type')=='not_current' if i==0 else p.get('bridge_status')=='custom_package' if i==1 else 'common' in r.mode and 'cs2' in str(p.get('record_ids')).lower())
 record('safety_'+str(i),q,r,ok)
if candidate:
 from app.knowledge.common.task_interpretation import interpret
 gid=games[0]['record_id']
 negatives=['not a game overview','เกมนี้ไม่ใช่เกมอะไร','what is this game and its price','what is this game for children','what is this game in 2027','equipment without mouse','อุปกรณ์ที่เอามาเองได้ไหม','only equipment i can borrow','what is the policy for external visitors after maintenance','what is this name','what is this time','how to pay']
 for i,q in enumerate(negatives):
  ids=[gid] if i<5 or i>=9 else ['zone_pc'] if i<8 else ['migrated_faq_rule_schedule_friday_maintenance'];ok=interpret(q,ids,records) is None
  checks.append({'case':'negative_contract_'+str(i),'question':q,'passed':ok});print('negative',i,ok)
summary={'count':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[{'case':x['case'],'question':x['question'],'answer':(x.get('result') or {}).get('answer')} for x in checks if not x['passed']],'candidate':candidate,'real_model_calls':0,'full_test':False}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False));sys.exit(bool(summary['failed']))
