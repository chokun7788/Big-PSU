"""Owner-data growth, relation and pending-scope contracts. Synthetic data only."""
import dataclasses,json,os,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
sys.path[:0]=[str(S),str(R)]
os.environ.update(PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0')
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.dialogue import state_from_answer
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult
store=CommonStore(T/'SYNTHETIC_ONLY.sqlite');store.initialize();checks=[]
def save(r,values,rev=None):
 for k,v in values.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':'SYNTHETIC ONLY; NOT REAL STUDIO POLICY'}
 return save_owner_record(store,r,r['revision'] if rev is None else rev,'synthetic_actor',source_title='R98 SYNTHETIC ONLY',change_note='Isolated test')['record']
def new(kind,rid,values,aliases=None):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 r['validity']={'state':'known','effective_from':'2020-01-01T00:00:00+07:00','effective_until':'2035-01-01T00:00:00+07:00'}
 if aliases:r['aliases']=aliases
 return save(r,values,0)
def pub(ids,key):
 for rid in ids:
  row=store.get(rid);store.approve(rid,row['record']['revision'],row['hash'],actor='synthetic_actor')
 store.publish(ids,actor='synthetic_actor',expected_active=store.snapshot()['active'],request_key=key)
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':dataclasses.asdict(detail) if dataclasses.is_dataclass(detail) else detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(name,bool(ok),flush=True)
def unavailable(q):
 return PipelineAnswer(answer='Live availability could not be checked.',hits=[],elapsed=0,mode='pipeline:live_booking_unavailable',confidence=0,route=PipelineRoute('booking','live',0,'live_unavailable','low','synthetic unavailable'),entities=EntityBundle(),validation=ValidationResult(True),decision_artifact={'response_type':'live_unavailable','live_booking':{'status':'unavailable','fixture':True}})
def ask(q,lang='en',h=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model network in source contracts')):
  return CommonAnswerer(store,external_executor=unavailable).answer(q,locale=lang,history=h or [])
def hist(q,r):return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
def bi(th,en):return {'th':th,'en':en}
z=new('zone','fixture_z',{'name':bi('โซนเนบิวลาทดลอง','Nebula Zone')})
resource=new('resource','fixture_resource',{'name':bi('เครื่องเนบิวลาทดลอง','Nebula Machine'),'zone_id':'fixture_z','physical_pool_key':'SYNTHETIC_POOL','operational_status':'in_service'})
a=new('audience','fixture_external',{'name':bi('ผู้เยี่ยมชมเนบิวลาทดลอง','Nebula Visitors'),'eligibility':bi('เงื่อนไขทดลองผู้เยี่ยมชม','Synthetic visitor eligibility')}, {'th':['บุคคลภายนอกทดลอง'],'en':['external fixture visitors']})
b=new('audience','fixture_members',{'name':bi('สมาชิกเนบิวลาทดลอง','Nebula Members'),'eligibility':bi('เงื่อนไขทดลองสมาชิก','Synthetic member eligibility')})
s=new('service','fixture_s',{'name':bi('บริการเนบิวลาทดลอง','Nebula Service'),'platform':'PC','resource_ids':['fixture_resource'],'session_minutes':60,'occupancy_minutes':60})
empty=new('service','fixture_empty',{'name':bi('บริการไร้อัตราทดลอง','Unpriced Fixture Service'),'platform':'VR','resource_ids':['fixture_resource'],'session_minutes':30,'occupancy_minutes':30})
def rate(rid,aid,amount):return new('rate',rid,{'service_id':s['record_id'],'audience_id':aid,'amount_minor':amount,'currency':'THB','unit':'per_hour','duration_minutes':60,'calculation_rule':'linear'})
r=rate('fixture_rate',a['record_id'],12300);r_other=rate('fixture_rate_other',b['record_id'],9900)
pub([x['record_id'] for x in (z,resource,a,b,s,empty,r,r_other)],'prices-v1')
for lang,q in [('en','All prices for external fixture visitors'),('th','ราคาบุคคลภายนอกทดลองทั้งหมด')]:
 result=ask(q,lang);p=result.decision_artifact['query_plan'];receipt=p.get('set_receipt',{})
 check('all service enumeration includes unpriced member '+lang,receipt.get('total_members')==2 and set(receipt.get('returned_members',[]))=={'fixture_s','fixture_empty'} and 'Unpriced' in result.answer if lang=='en' else receipt.get('total_members')==2 and 'ไร้อัตรา' in result.answer,result)
 check('explicit audience not broadened '+lang,p.get('audience_selection',{}).get('selected_ids')==['fixture_external'] and '123.00' in result.answer and '99.00' not in result.answer,result)
q='Prices for external fixture visitors for 2 hours';first=ask(q);h=hist(q,first)
check('missing service produces actionable pending selection',first.decision_artifact['response_type']=='clarification' and state_from_answer(first).get('price_scope_request',{}).get('duration_quote')=='2 hours',first)
follow=ask('Nebula Service',h=h)
check('short service preserves audience and duration',follow.decision_artifact['query_plan']['audience_selection']['selected_ids']==['fixture_external'] and '246' in follow.answer and '99.00' not in follow.answer,follow)
r=save(store.get('fixture_rate')['record'],{'amount_minor':15100});pub(['fixture_rate'],'prices-v2')
follow=ask('all',h=h)
check('all rereads edited source preserving pending selection','151.00' in follow.answer and '302' in follow.answer and '123.00' not in follow.answer,follow)
store.withdraw('fixture_rate',actor='synthetic_actor');follow=ask('all',h=h)
check('withdrawn rate not resurrected through pending state','151.00' not in follow.answer and '123.00' not in follow.answer and '99.00' not in follow.answer,follow)
g=new('game','fixture_game',{'title':bi('เส้นทางดาวทดลอง','Star Paths Fixture'),'summary':bi('ภาพรวม STAR_ONE','Overview STAR_ONE')})
g2=new('game','fixture_game_two',{'title':bi('เมฆทดลอง','Cloud Fixture'),'summary':bi('ภาพรวม CLOUD_TWO','Overview CLOUD_TWO')})
mode=new('game_mode','fixture_mode',{'game_id':g['record_id'],'mode_name':bi('ร่วมมือทดลอง','Co-op Fixture'),'platform':'PC','players_min':2,'players_max':4})
pub([x['record_id'] for x in (g,g2,mode)],'games-v1')
for lang,q in [('en','Star Paths Fixture how many players?'),('th','เส้นทางดาวทดลอง ใช้ผู้เล่นกี่คน')]:
 result=ask(q,lang)
 check('reverse game-mode join without optional support fact '+lang,result is not None and result.validation.ok and any(h.get('record_id')=='fixture_mode' and h.get('field')=='players_max' for h in result.hits) and not any(o.get('field')=='studio_supported' for o in result.decision_artifact.get('obligations',[])),result)
result=ask('What is Star Paths Fixture and what is Cloud Fixture?')
check('same-task subjects each retain answer',result is not None and 'STAR_ONE' in result.answer and 'CLOUD_TWO' in result.answer and len(result.decision_artifact.get('need_results',[]))==2,result)
rule_event=new('competition','fixture_event',{'game_id':g['record_id'],'event_name':bi('แข่งเส้นทางดาวทดลอง','Star Fixture Tournament'),'rulebook_release':'SYNTHETIC_V1','coverage':'complete'})
rule=new('competition_rule','fixture_rule',{'competition_id':'fixture_event','section_number':'1','facet':'in_match_operations','heading':bi('การหลุดทดลอง','Disconnection fixture'),'text':bi('หากเกมหลุด ให้แจ้งกรรมการ ห้ามเริ่มใหม่เอง เว้นแต่กรรมการอนุญาต RULE_EXCEPTION','On disconnection, notify the referee. Do not restart unless the referee permits it. RULE_EXCEPTION'),'depends_on_ids':[],'completeness':'complete'})
pub(['fixture_event','fixture_rule'],'rules-v1')
for lang,q,choice in [('th','เส้นทางดาวทดลอง ถ้าเกมหลุดทำยังไง','แข่ง'),('en','Star Paths Fixture what should I do if I disconnect?','competition')]:
 first=ask(q,lang);second=ask(choice,lang,hist(q,first))
 check('context choice reads exact game event clause '+lang,first.decision_artifact['response_type']=='clarification' and second is not None and 'RULE_EXCEPTION' in second.answer and any(h.get('record_id')=='fixture_rule' for h in second.hits),second)
 check('normal play does not invent competition policy '+lang,'RULE_EXCEPTION' not in ask('general play' if lang=='en' else 'ทั่วไป',lang,hist(q,first)).answer)
center=new('center','fixture_center',{'name':bi('ศูนย์ทดลอง','Fixture Center'),'operator':bi('ผู้ดูแลทดลอง','Synthetic operator'),'timezone':'Asia/Bangkok','address':bi('ที่อยู่ ADDRESS_ONLY','Address ADDRESS_ONLY')})
pub(['fixture_center'],'center-v1')
q='ศูนย์อยู่ที่ไหน แล้วราคาเท่าไร';first=ask(q,'th');second=ask('ทั้งหมด','th',hist(q,first))
check('partial location keeps price selector state','ADDRESS_ONLY' in first.answer and first.decision_artifact['response_type']=='partial_answer' and second.decision_artifact['query_plan'].get('set_receipt',{}).get('total_members')==2,first)
result=ask('PC ว่างไหม แล้วจองยังไง','th')
check('mixed live unavailable kept separate from missing procedure',len(result.decision_artifact.get('need_results',[]))==2 and result.decision_artifact['need_results'][0]['status']=='live_unavailable',result)
summary={'count':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x['case'] for x in checks if not x['passed']],'source_data':'synthetic isolated owner-form records','simulated_approvals_only':True,'model_calls':0,'full_test':False}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False));sys.exit(bool(summary['failed']))

