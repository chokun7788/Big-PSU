"""Independent behavior assertions. No expected renderer/answers fed to router."""
import sys,json,traceback
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
from app.knowledge.common.answer import CommonAnswerer,named,all_query,live_query
from app.knowledge.common.query_contract import resolve_fields
from app.knowledge.common.planner import checked_plan,plan_rejection,allowed_schema,semantic_guard
store=t.OneReleaseStore(t.DB).freeze();records=store.frozen['release']['records'];a=CommonAnswerer(store)
results=[]
def check(name,fn):
    try:fn();results.append({'id':name,'passed':True})
    except Exception:results.append({'id':name,'passed':False,'error':traceback.format_exc()})
def truth(x):assert x
def fields(k,lang,suffix,expected,forbidden=(),history=None):
    rid=t.rid(k,3);q=records[rid]['aliases'][lang][0]+' '+suffix if history is None else suffix
    ans=a.answer(q,locale=lang,history=history,at=t.AT);assert ans is not None
    d=ans.decision_artifact;obs={o['field'] for o in d['obligations'] if o['record_id']==rid}
    assert set(expected)<=obs,(q,obs,expected,d)
    assert not set(forbidden)&obs,(q,obs,forbidden)
    assert not d['query_plan']['all_fields'],q
    assert ans.validation.ok,ans.validation
for q in ['football','small room','install the game','all seats','ข้อมูลครบไหม','ไม่ต้องตอบทั้งหมด','not all information']:
    check('not_broad:'+q,lambda q=q:truth(not all_query(q)))
for q in ['ข้อมูลทั้งหมด','Show all information','all games','ทั้งหมด']:
    check('broad:'+q,lambda q=q:truth(all_query(q)))
for q in ['free to play','เล่นฟรี','free of charge']:
    check('price_not_live:'+q,lambda q=q:truth(not live_query(q)))
for q in ['PC available now','เครื่องว่างไหม','free at 15:00']:
    check('live:'+q,lambda q=q:truth(live_query(q)))
for k,lang,q,need,bad in [
 ('center','en','Which floor should I visit?',['floor'],['address']),
 ('center','th','ขอแผนที่และชั้นที่จะไป',['map_url','floor'],['description']),
 ('resource','en','How many players fit on this device?',['capacity_persons'],['physical_pool_key']),
 ('zone','en','How many seats in all?',['room_seats'],['description']),
 ('service','th','เล่นหนึ่งรอบกี่นาที แล้วกันช่องจองกี่นาที',['session_minutes','occupancy_minutes'],['amount_minor']),
 ('audience','en','Am I eligible and what proof should I bring?',['eligibility','required_proofs'],['amount_minor']),
 ('procedure','th','ขั้นตอนและเอกสารที่ต้องเตรียม',['steps','required_documents'],['deadline_minutes']),
 ('competition_rule','en','Give the full rule text; is its content complete?',['text','completeness'],['facet']),
 ('competition','en','Which version of the rules applies?',['rulebook_release'],['competition_dates']),
 ('closure','en','Why is it closed?',['state','reason'],['resolution_policy_id']),
 ('game','en','What is this game about?',['summary'],['age_rating']),
 ('game_mode','th','ขั้นต่ำกี่คนและสูงสุดกี่คน',['players_min','players_max'],['network_requirement']),
 ('live_binding','en','Explain the TTL and status mappings',['freshness_policy','status_mapping'],['external_resource_key']),
]:check(k+':'+lang+':'+q,lambda k=k,lang=lang,q=q,need=need,bad=bad:fields(k,lang,q,need,bad))
for lang,q in [('en','And what proof should I bring?'),('th','แล้วหลักฐานที่ต้องเอาไปล่ะ')]:
    history=[{'role':'user','content':records[t.rid('audience',3)]['aliases'][lang][0]+' details'}]
    check('followup:'+lang,lambda lang=lang,q=q,history=history:fields('audience',lang,q,['required_proofs'],history=history))
check('repeat_unique',lambda:truth(named('Cloud Ggarden how to play',{'a':['Cloud Garden'],'b':['Cloud Garden Plus']})==(['a'],'unique_repeat_edit')))
check('repeat_nested_longer',lambda:truth(named('Cloud Ggarden Plus how to play',{'a':['Cloud Garden'],'b':['Cloud Garden Plus']})==(['b'],'unique_repeat_edit')))
check('digit_not_corrected',lambda:truth(named('Game 88',{'a':['Game 8']})[0]==[]))
check('exact_before_correction',lambda:truth(named('Game 88',{'a':['Game 8'],'b':['Game 88']})[0]==['b']))
check('substring_not_intent',lambda:truth(resolve_fields('operating requirements',{'resource'})[0]==[]))
check('casefold_label',lambda:truth('external_resource_key' in resolve_fields('EXTERNAL_RESOURCE_KEY',{'live_binding'})[0]))
check('status_not_opening_times',lambda:truth(set(resolve_fields('What is the opening status on that date and why?',{'closure'})[0])=={'state','reason'}))
ids=[t.rid('service',3)]
for prop,reason in [({'requested_fields':['session_minutes'],'all_fields':False,'platform':ids[0]},'invalid_platform'),({'requested_fields':['random'],'all_fields':False,'platform':None},'invalid_fields'),({'requested_fields':[[]],'all_fields':False,'platform':None},'invalid_fields'),({'requested_fields':[],'all_fields':False,'platform':None},'abstained')]:
    check('planner_reject:'+reason+str(prop),lambda prop=prop,reason=reason:truth(plan_rejection(prop,ids,records)==reason))
check('planner_accept_null',lambda:truth(checked_plan({'requested_fields':['session_minutes'],'all_fields':False,'platform':None},ids,records) is not None))
def guard_extra():
    ids=[t.rid('audience',3)];clean=checked_plan({'requested_fields':['name','eligibility','required_proofs'],'all_fields':False,'platform':None},ids,records)
    result,why=semantic_guard('What proof is required?',clean,ids,records)
    assert result['requested_fields']==['required_proofs'],(result,why)
check('semantic_guard_removes_extra',guard_extra)
def guard_broad():
    ids=[t.rid('audience',3)];clean=checked_plan({'requested_fields':['required_proofs'],'all_fields':True,'platform':None},ids,records)
    result,why=semantic_guard('What proof is required?',clean,ids,records)
    assert result is None and why['semantic_status']=='rejected_unrequested_all_fields'
check('semantic_guard_rejects_all',guard_broad)
def list_fields():
    ans=a.answer('List all games and supported platforms',locale='en',at=t.AT)
    assert ans is not None and ans.decision_artifact['query_plan']['list_scope']
    obs=ans.decision_artifact['obligations']
    for rid,r in records.items():
        if r['kind']=='game':assert any(o['record_id']==rid and o['field']=='supported_platforms' for o in obs),rid
    assert not any(o['field']=='age_rating' for o in obs)
check('list_all_records_requested_fields',list_fields)
def contact_reference():
    ans=a.answer(records[t.rid('procedure',3)]['aliases']['en'][0]+' steps',locale='en',at=t.AT)
    actual=records[t.rid('contact',3)]['fields']['value']['value']
    assert actual in ans.answer,(actual,ans.answer)
    assert t.rid('contact',3) not in ans.answer
check('nested_contact_independent_gold',contact_reference)
def switch():
    history=[{'role':'user','content':records[t.rid('audience',1)]['aliases']['en'][0]+' proof'}]
    fields('audience','en',records[t.rid('audience',3)]['aliases']['en'][0]+' proof',['required_proofs'],history=history)
check('explicit_new_record_wins_history',switch)
def partial_gate():
    ans=a.finish(store.frozen,0,'test',[],{'requested_fields':['capacity_persons']},[])
    assert not ans.validation.ok and ans.decision_artifact['response_type']=='partial_answer'
check('coverage_gate_missing_field',partial_gate)
out=B/sys.argv[1];out.mkdir(exist_ok=False)
(out/'RESULTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'total':len(results),'passed':sum(r['passed'] for r in results),'failed':[r for r in results if not r['passed']]},ensure_ascii=False,indent=2))
