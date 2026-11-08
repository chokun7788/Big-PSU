"""Person bounds: separate service identity, competing amounts and direct forgery."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.domain_flow.plan_contract import compile_request
out=R/('hybrid_ranges_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store)
def put(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'range-fixture')['record']
for sid in ['Amber','Cobalt']:put('service',sid.lower(),{'name':{'th':sid+' play','en':sid+' play'},'platform':'PC','resource_ids':[],'session_minutes':60})
put('audience','visitors',{'name':{'th':'Amber visitors','en':'Amber visitors'}})
def rate(rid,sid,amount,lo,hi):return put('rate',rid,{'service_id':sid,'audience_id':'visitors','amount_minor':amount,'currency':'THB','unit':'per_session','duration_minutes':60,'persons_min':lo,'persons_max':hi})
rate('amber_small','amber',1000,1,2);upper=rate('amber_large','amber',2000,3,4);rate('cobalt_other','cobalt',9000,1,4)
q='What is the total price for Amber play for Amber visitors 4 people, 60 minutes per session?';u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False})
def run():
 e=Engine.from_snapshot(view.snapshot());r=e.answer(q,'en',at='2026-11-08T12:00:00+07:00',allow_llm=False,understanding=u);return e,r
e,r=run();checks={};details=[r];child=r['needs'][0];snapshot=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,snapshot).tasks[0]
(out/'FIRST_RESULT.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),'utf8')
checks['same_platform_other_service_does_not_block']={c['record_id'] for c in r['claims']}=={'amber_small','amber_large'}
checks['ranges_labelled_no_invented_total']='1–2' in r['answer'] and '3–4' in r['answer'] and not child['computations'] and 'total is not confirmed' in r['answer'].lower()
for name,change in [('forged_projected_bounds',lambda idx:idx.byid[r['claims'][0]['fact_id']].update(persons_min=1,persons_max=1))]:
 idx=copy.deepcopy(e.index);change(idx);checks[name]=bool(assess(idx,task,child,snapshot,q)['fatal'])
bad=copy.deepcopy(child);bad['claims'][0]['evidence_refs']=[x for x in bad['claims'][0]['evidence_refs'] if not x['locator'].endswith('/persons_min')]
checks['removed_bounds_locator_rejected']=bool(assess(e.index,task,bad,snapshot,q)['fatal'])
rate('amber_conflict','amber',9900,1,2);conflicted,new=run();details.append(new)
checks['identical_bounds_different_amount_withheld']=not any(c['record_id'] in {'amber_small','amber_conflict'} and c['facet']=='amount' for c in new['claims'])
checks['direct_injection_competing_source_rejected']=bool(assess(conflicted.index,task,child,snapshot,q)['fatal'])
store.withdraw('amber_conflict',actor='range-withdraw');edit=copy.deepcopy(upper);edit['fields']['persons_max']={'status':'unknown','value':None,'evidence_refs':[],'note':'fixture unknown bound'}
save_owner_record(store,edit,upper['revision'],'range-owner-edit');_,missing=run();details.append(missing)
checks['unknown_one_bound_cannot_be_delivered']=not any(c['record_id']=='amber_large' and c['facet']=='amount' for c in missing['claims'])
report={'all_passed':all(checks.values()),'checks':checks,'scope':'controlled source; labels not proof of group allocation; no model/HTTP'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
