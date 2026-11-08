"""Read-only retained C03 source variants; no saved sample regrade/inference."""
import copy,json,time,os
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.projection import value,title
from app.knowledge.common.domain_flow.scope import reference_time
data=snapshot();e=Engine.from_snapshot(data);out=R/('retained_inventory_'+str(time.time_ns()));out.mkdir();checks={};details=[];at=reference_time('2026-10-26T12:00:00+07:00')
os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite')
def run(q,facet='name',op='list',engine=e):
 u=Understanding([MeaningTask(q,'equipment','C03',op,facet)],True,'retained_source_inventory',{'model_called':False});r=engine.answer(q,'en',at=at,allow_llm=False,understanding=u);details.append({'question':q,'result':r});return r
records=data['release']['records'];zones=[r for r in records.values() if r['kind']=='zone' and r['record_id']!='zone_all_zones'];models=[r for r in records.values() if r['kind']=='equipment_model'];expected={}
for zone in zones:
 labels={s.casefold() for s in title(zone).values()};members=set()
 for model in models:
  rows=[x for x in value(model,'specifications') or [] if x.get('key')=='zone']
  if len(rows)==1 and labels&{s.strip().casefold() for s in rows[0]['value'].split('/')} :members.add(model['record_id'])
 expected[zone['record_id']]=sorted(members)
 r=run('List all equipment in '+title(zone)['en']);checks['actual_zone_members_'+zone['record_id']]={c['record_id'] for c in r['claims']}==members and r['needs'][0]['execution_contract']['collection_proof']['verified']
 paths=r['needs'][0]['execution_contract']['collection_proof']['source_scope_refs'];checks['actual_zone_join_refs_'+zone['record_id']]={p['equipment_record_id'] for p in paths}==members and all(p['zone_record_id']==zone['record_id'] and p['equipment_revision']==records[p['equipment_record_id']]['revision'] and p['zone_revision']==zone['revision'] and all(ref in p['evidence_refs'] for ref in [*records[p['equipment_record_id']]['fields']['specifications']['evidence_refs'],*zone['fields']['name']['evidence_refs']]) for p in paths)
r=run('List all PS5 equipment');checks['PS5_alias_uses_source_zone_not_entire_inventory']={c['record_id'] for c in r['claims']}==set(expected['zone_ps5'])
for m in models:
 rows=[x for x in value(m,'specifications') or [] if x.get('key')=='quantity']
 if not rows:continue
 r=run('How many machines of '+m['record_id']+' are recorded?','quantity','count');checks['actual_quantity_literal_'+m['record_id']]=any(c['record_id']==m['record_id'] and c['facet']=='quantity' and c['value']==rows[0]['value'] for c in r['claims'])
# A compound location with an unrecognized token is not a proven zone join.
changed=copy.deepcopy(data);model=next(r for r in changed['release']['records'].values() if r['record_id']=='equipment_playstation_5_slim');next(x for x in model['fields']['specifications']['value'] if x['key']=='zone')['value']='PlayStation 5 Zone / Unconfirmed Annex';r=run('List all equipment in PlayStation 5 Zone',engine=Engine.from_snapshot(changed));checks['unknown_compound_location_not_falsely_confirmed_member']=all(c['record_id']!='equipment_playstation_5_slim' for c in r['claims'])
from app.knowledge.common.answer import CommonAnswerer
from unittest.mock import patch
class MemoryView:
 path=out/'readonly-view'
 def snapshot(self):return data
 def still_current(self,s):return s is data
with patch('urllib.request.urlopen',side_effect=AssertionError('no model/provider HTTP')):a=CommonAnswerer(MemoryView()).answer('List all equipment in VR Zone',locale='en',at=at,planner=None)
contract=a.decision_artifact['execution_contract'];claims=[c for child in contract['executor_results'] for c in child['claims']];checks['actual_Common_inventory_list_keeps_source_zone_members']={c['record_id'] for c in claims}==set(expected['zone_vr']);checks['actual_Common_inventory_has_registered_list_operation']=any(t['operation']=='list' and t['facet']=='name' for t in contract['request_plan']['tasks']);details.append({'mode':'common','answer':a.answer,'artifact':a.decision_artifact})
report={'all_passed':all(checks.values()),'checks':checks,'expected_actual_zone_members':expected,'actual_source_models_readonly':len(models),'controlled_memory_variant_only_for_negative_case':True,'actual_model_inferences':0,'sample_regrade':False,'actual_http_calls':0,'source_data_modified':False,'empirical_accuracy_claimed':False};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
