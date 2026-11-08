"""C10 typed source decisions, conditions, exceptions and action boundaries."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.scope import reference_time
out=R/('studio_policy_matrix_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite');store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};details=[];bi=lambda s:{'th':s,'en':s}
cases=[
 ('installation','Can I install my own game?','Installing software requires staff approval; owning the game does not authorize installation.'),
 ('steam_account','Do I need my own Steam account?','The player must use their own account; the booking customer account cannot substitute for every player.'),
 ('logout_data','Does the studio keep my login data after logout?','The source requires the player to log out; no promise that the studio retains passwords is recorded.'),
 ('update_compensation','Can a game update earn extra play time?','An update does not automatically extend the paid session; staff must verify any compensation.'),
 ('game_failure_switch','The game cannot run; can I change service?','Staff must check the game failure before approving a different machine; the booking does not switch automatically.'),
 ('installed_version','Can you confirm the installed game version?','Ask staff to check the installed build; the catalog title alone does not establish the installed version.'),
 ('network_fault','What should I do about a network fault?','Report a network fault to staff; no automatic refund or time credit is established by this clause.'),
 ('equipment_compensation','What if I damage equipment?','For user-caused equipment damage, staff assess actual damage; a spontaneous equipment fault is a separate situation.'),
 ('peripheral_fault','Can staff replace a faulty peripheral?','Report a faulty peripheral and wait for staff replacement; do not disconnect shared equipment yourself.'),
 ('guardian','Does a minor need signed parental consent?','The actual minor player needs guardian consent; an adult booking customer does not remove that requirement.'),
 ('capture','Can I take screenshots in the game?','In-game screenshots may be captured for personal use; filming people or the premises is not established here.'),
 ('streaming','Can I stream my gameplay?','Streaming requires staff permission and consent from identifiable participants; a gameplay capture permission alone is insufficient.'),
 ('external_visitor','Can an external visitor use general studio services?','An external visitor may request service after identity verification; this does not confirm a free machine or a booking.'),
 ('personal_accessories','Can I use my own keyboard and mouse?','A personal keyboard or mouse requires staff approval before connecting; permission to bring it does not authorize plugging it in.'),
 ('food_consumption','Can I eat food in the designated area?','Food may be consumed only in the designated lobby; a permission to carry a sealed bag is not a permission to eat at a desk.'),
 ('food_bring','Can I bring food into the studio?','Only sealed food bags may be carried through to the lobby; opening or eating them at play desks is prohibited.'),
 ('personal_power','Can I bring my own power strip?','A personal power strip must be inspected by staff; bringing one does not authorize connecting it.'),
]
records={}
for intent,q,text in cases:
 r=template('policy');r['record_id']='scope_'+intent;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in {'topic':intent,'subject':bi('Controlled '+intent+' policy'),'decision':'conditional','conditions_all':[{'field':'staff_approval','operator':'eq','value':True}],'exceptions':bi('Only the stated exception applies; no implied permission for other situations.'),'details':bi(text),'consequence':bi('Ask staff before proceeding.')}.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 records[intent]=save_owner_record(store,r,0,'controlled-test')['record']
def run(q,intent='',op='detail'):
 e=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,'rules','C10',op,'owner_policy',canonical_operation='policy.'+intent if intent else '')],True,'controlled_studio_policy',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):r=e.answer(q,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=u)
 details.append({'question':q,'intent':intent,'result':r});return r,e,u
for intent,q,text in cases:
 r,_,_=run(q,intent);checks['source_action_'+intent]=bool(r['claims']) and {c['record_id'] for c in r['claims']}=={'scope_'+intent} and text in r['answer'];checks['conditions_exceptions_not_silently_permission_'+intent]=all(c['value'].startswith('Conditional;') and 'staff_approval eq True' in c['value'] and 'Only the stated exception' in c['value'] for c in r['claims']) and bool(r['claims'])
r,e,u=run('Can I bring food into the studio?','food_bring');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0]
for key in ['topic','subject']:
 child=copy.deepcopy(r['needs'][0]);refs=e.index.records['scope_food_bring']['fields'][key]['evidence_refs'];child['claims'][0]['evidence_refs']=[v for v in child['claims'][0]['evidence_refs'] if v not in refs];checks['studio_policy_scope_locator_'+key]=bool(assess(e.index,task,child,snap,details[-1]['question'])['fatal'])
child=copy.deepcopy(r['needs'][0]);f=next(f for f in e.index.byrecord['scope_food_consumption'] if f['category']=='C10');child['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}];child['plan']['metadata']['policy_intents']=['food_consumption'];checks['valid_consumption_source_cannot_prove_bring_permission']=bool(assess(e.index,task,child,snap,details[-1]['question'])['fatal'])
for intent in ['food_bring','food_consumption','guardian','personal_power','personal_accessories']:
 q,text=next((q,t) for i,q,t in cases if i==intent)
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):natural=CommonAnswerer(view).answer(q,locale='en',at=reference_time('2026-10-26T12:00:00+07:00'),planner=None)
 details.append({'natural_question':q,'answer':natural.answer,'artifact':natural.decision_artifact});checks['natural_Common_'+intent]=text in natural.answer
unknown=copy.deepcopy(records['guardian']);unknown['fields']['exceptions']={'status':'unknown','value':None,'evidence_refs':[],'note':'Exception scope not established'};save_owner_record(store,unknown,unknown['revision'],'controlled-test');r,_,_=run('Does a minor need signed parental consent?','guardian');checks['unknown_exceptions_not_unrestricted_permission']=not r['claims']
r,_,_=run('Does a minor need signed parental consent?');checks['unknown_exceptions_cannot_bypass_guard_by_omitting_canonical_action']=not r['claims']
na=copy.deepcopy(records['installation']);na['fields']['decision']['value']='prohibited';na['fields']['conditions_all']={'status':'not_applicable','value':None,'evidence_refs':[],'note':'No condition applies to this prohibition'};na['fields']['exceptions']={'status':'not_applicable','value':None,'evidence_refs':[],'note':'No exception applies'};save_owner_record(store,na,na['revision'],'controlled-test');r,_,_=run('Can I install my own game?','installation');checks['explicit_not_applicable_not_treated_unknown']=bool(r['claims']) and all(c['value'].startswith('Prohibited') for c in r['claims'])
expired=copy.deepcopy(records['streaming']);expired['validity']['effective_until']='2026-02-01T00:00:00+07:00';save_owner_record(store,expired,expired['revision'],'controlled-test');r,_,_=run('Can I stream my gameplay?','streaming');checks['expired_studio_permission_not_current']=not r['claims'] and r['terminal_state']=='not_current'
legacy=template('faq');legacy['record_id']='legacy_carry_variant';legacy['localization']['en_status']='agent_translated';legacy['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
for k,v in {'topic':'service_policy','question':bi('food_bring / general'),'answer':bi('Legacy carry rule requires staff to inspect the sealed bag.')}.items():legacy['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
save_owner_record(store,legacy,0,'controlled-test')
with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):natural=CommonAnswerer(view).answer('Can I bring food into the studio?',locale='en',at=reference_time('2026-10-26T12:00:00+07:00'),planner=None)
details.append({'natural_question':'retained registry plus new owner carry variant','answer':natural.answer,'artifact':natural.decision_artifact});checks['legacy_shortcut_does_not_hide_new_owner_variant']='Only sealed food bags' in natural.answer and 'Legacy carry rule' in natural.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
