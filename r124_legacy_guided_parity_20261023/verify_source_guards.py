"""Regression probes for retained intents, source edits and native scheduling."""
import copy,hashlib,json,os,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'revision03_system';sys.path.insert(0,str(S))
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.contracts import RequestBudget,Plan
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.flow_context import request_context
jobs={r['key'][:8]:r for r in (json.loads(s) for s in (R/'ALL_RETAINED_JOBS.jsonl').read_text('utf8').splitlines())}
store=MigratedView(S/'data/knowledge/common.sqlite');snap=store.snapshot();at=reference_time('2026-10-21T12:00:00+07:00')
OUT=R/('source_guard_verification_'+str(time.time_ns()));OUT.mkdir();checks={};outputs=[]
class MemoryView:
 path=store.path
 def __init__(self,s):self.data=s
 def snapshot(self):return self.data
 def still_current(self,s):return s is self.data
def forbidden(*args,**kwargs):raise AssertionError('No model/provider allowed in controlled source checks')
def run(key,view=store):
 job=jobs[key]
 with patch('urllib.request.urlopen',forbidden),patch('app.booking.live_status.get_live_booking_status',forbidden):
  result=answer(CommonAnswerer(view),job['question'],locale=job['locale'],at=at,planner=None)
 assert result is not None
 outputs.append({'key':job['key'],'question':job['question'],'answer':result.answer,'artifact':result.decision_artifact})
 return result
def categories(r):return [x.get('category') for x in r.decision_artifact.get('need_results',[])]
r=run('69812416');checks['centre_open_now_is_calendar_not_live']=categories(r)==['C11'] and 'unsupported_operation' not in r.answer
r=run('eafe23b9');checks['controls_not_overridden_by_game_presence']=categories(r)==['C05'] and len(r.decision_artifact['need_results'][0]['claim_packets'])>1
r=run('9db7acd1');checks['single_button_before_word_button_resolved']=categories(r)==['C05'] and len(r.decision_artifact['need_results'][0]['claim_packets'])==1
r=run('5d18afc2');checks['generic_controller_question_is_control_scope']=categories(r)==['C05']
r=run('f683a42c');checks['device_for_named_game_is_offering_relation']=categories(r)==['C04'] and bool(r.decision_artifact['need_results'][0]['claim_packets'])
r=run('aefe9911');checks['food_area_fragment_uses_consumption_policy']=categories(r)==['C10'] and bool(r.decision_artifact['need_results'][0]['claim_packets'])
r=run('3020765f');checks['address_keeps_building_and_floor']='อาคาร 5 ชั้น 1' in r.answer
from app.knowledge.common.domain_flow.precision import center_location
engine=Engine.from_snapshot(snap,cache_key=store.path.resolve())
checks['unknown_named_location_not_replaced_by_studio']=center_location(engine.index,'Dota 999 อยู่ที่ไหน') is None
rid=next(k for k,r in snap['release']['records'].items() if r['kind']=='faq' and r.get('fields',{}).get('question',{}).get('value',{}).get('en')=='food_bring / general')
changed=copy.deepcopy(snap);changed['active']='controlled_source_edit';changed['epoch']+=100000
edit=changed['release']['records'][rid];edit['revision']+=1
edit['fields']['answer']['value']={'th':'CONTROLLED SOURCE EDIT','en':'CONTROLLED SOURCE EDIT'}
sid='r124_controlled_edit';changed['release']['sources'][sid]={'source_id':sid,'kind':'derived_curated','sha256':hashlib.sha256(b'CONTROLLED SOURCE EDIT').hexdigest(),'trust':'internal_verified','authority_for':['faq'],'path':'verification-only://memory'}
edit['fields']['answer']['evidence_refs']=[{'source_id':sid,'locator':'/answer'}]
r=run('e57f0296',MemoryView(changed));checks['source_edit_visible_without_parser_edit']='CONTROLLED SOURCE EDIT' in r.answer
removed=copy.deepcopy(changed);removed['epoch']+=1;removed['withdrawn']=[rid]
r=run('e57f0296',MemoryView(removed));checks['withdrawn_source_not_served_from_cached_index']='CONTROLLED SOURCE EDIT' not in r.answer
# Controlled two-need schedule fixture: force a price interpretation pending,
# and prove calendar reads finish before any fallback phase. No fake rate is
# returned and the model budget is zero.
q='How much does Beat Saber cost; what days is it open?'
u=Understanding([MeaningTask('How much does Beat Saber cost','service_fee','C06','detail','amount'),MeaningTask('what days is it open?','schedule','C11','detail','open_periods')],True,'controlled_scheduler_probe',{})
native=Engine.plan
def pending_price(self,cat,question,at=None,meaning=None):
 if cat=='C06':return Plan(category=cat,status='missing_source',reason='semantic_interpretation_needed',ambiguous=True,candidates=[f['id'] for f in self.index.bycat[cat] if f['facet']=='amount'],facets=['amount'])
 return native(self,cat,question,at,meaning)
with patch.object(Engine,'plan',pending_price),patch('urllib.request.urlopen',forbidden):
 r=answer(CommonAnswerer(store),q,locale='en',at=at,planner=object(),_understanding=u,_budget=RequestBudget(max_model_calls=0))
contract=r.decision_artifact['execution_contract'];phases=[x['phase'] for x in contract['schedule']]
checks['native_compounds_complete_typed_reads_before_fallback']=phases[:2]==['native_typed_read']*2 and contract['typed_reads_before_fallback']
checks['native_compounds_defer_eligible_selection']='native_deferred_evidence_selection' in phases
checks['calendar_survives_exhausted_price_budget']=contract['tasks'][1]['terminal_state'] in {'supported','partial'} and 'Monday' in r.answer
outputs.append({'question':q,'controlled_scheduler_probe':True,'answer':r.answer,'artifact':r.decision_artifact})
summary={'all_passed':all(checks.values()),'checks':checks,'actual_network_calls':0,'model_calls':0,'memory_only_data_edits':True,'output':str(OUT)}
(OUT/'RESULTS.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2),'utf8');(OUT/'VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2));assert summary['all_passed']
