"""Focused guards on new typed state; in-memory metadata only, no DB writes."""
import copy,json,os,sys
from pathlib import Path
B=Path(__file__).resolve().parent;os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.path.insert(0,str(B/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.followup_scope import profile_followup,competition_question,price_selection
from app.knowledge.common.profile_confirmation import fingerprint
snap=MigratedView(B/'system/data/knowledge/common.sqlite').snapshot()['release'];records=snap['records'];names=snap['names'];RID='migrated_owner_claim_personal_keyboard_mouse';checks=[]
from app.knowledge.common.answer import derived_names,scoped_names
names=derived_names(scoped_names({'release':snap}),records)
def check(name,ok):checks.append({'case':name,'passed':bool(ok)})
def history(state,delivery='server_written'):return [{'role':'assistant','delivery_status':delivery,'common_read_state':{'schema_version':1,**state}}]
h=history({'profile_read_scope':{'record_id':RID,'routing_sha256':fingerprint(records[RID])}})
check('Untrusted client state cannot resume a profile',profile_followup('And my mouse?',history(h[0]['common_read_state'],'uncertain'),records) is None)
check('Complete new question keeps normal routing',profile_followup('How do I pay for booking?',h,records) is None)
check('Uncovered wireless property blocks source projection',profile_followup('And my wireless mouse?',h,records)['action']=='qualification_unconfirmed')
check('Changed ownership does not reuse personal policy',profile_followup("And the studio's mouse?",h,records)['action']=='qualification_unconfirmed')
check('Known subject uses current declared profile',profile_followup('And my mouse?',h,records)['action']=='qualified_selected')
changed=copy.deepcopy(records);changed[RID]['fields']['query_profile']['value']['context']='competition'
check('Changed routing invalidates profile continuation',profile_followup('And my mouse?',h,changed)['action']=='expired')
rows=[json.loads(s) for s in (B/'repair02/TURNS.jsonl').read_text(encoding='utf8').splitlines()]
wait=next(x['response']['common_read_state'] for x in rows if x['case']=='th-competition' and x['turn']==2)
ch=history(wait);r=competition_question('VALORANT',ch,records,names)
check('Competition continuation retains subject and ownership','personal keyboard, mouse' in r['question'])
studio=copy.deepcopy(wait);studio['pending_competition_scope']['scope']['ownership']='studio'
check('Studio ownership is not dropped in competition query','studio-owned keyboard, mouse' in competition_question('VALORANT',history(studio),records,names)['question'])
check('Competition state cannot trigger from client-only history',competition_question('VALORANT',history(wait,'uncertain'),records,names) is None)
check('Independent payment question bypasses competition state',competition_question('How do I pay?',ch,records,names) is None)
check('Stale competition origin expires',competition_question('VALORANT',ch,changed,names).get('expired'))
price=history({'price_scope_request':{'version':1,'audience_ids':[]}})
check('Negated all is not interpreted as all services',price_selection('not all',price,records,names) is None)
pr=price_selection('PC',price,records,names)
check('PC reply selects actual service relations',bool(pr) and len(pr['record_ids'])==2)
check('All covers eight source-backed service options',len(price_selection('all',price,records,names)['record_ids'])==8)
result={'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks,'data_mutated':False,'model_inference_verified':False}
with (B/'SCOPE_GUARDS_REVIEWED.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False));raise SystemExit(any(not x['passed'] for x in checks))
