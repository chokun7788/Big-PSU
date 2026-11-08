"""Controlled valid mixed audience billing through actual isolated engine."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
o=R/('multi_audience_positive_'+str(time.time_ns()));o.mkdir();store=CommonStore(o/'source.sqlite');store.initialize(allow_demo=False)
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
create('service','amber_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'session_minutes':60})
for rid,name,amount in [('amber','Amber visitors',1000),('sapphire','Sapphire visitors',2000)]:
 create('audience',rid+'_audience',{'name':{'th':name,'en':name}})
 create('rate',rid+'_rate',{'service_id':'amber_service','audience_id':rid+'_audience','amount_minor':amount,'currency':'THB','unit':'per_person','duration_minutes':60,'persons_min':1,'persons_max':1})
q='What is the total price for Amber service for Amber visitors 2 people and Sapphire visitors 3 people?'
e=Engine.from_snapshot(DraftSnapshotView(store).snapshot())
u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False})
r=e.answer(q,'en',at='2026-03-16T12:00:00+07:00',allow_llm=False,understanding=u)
checks={'two_audience_claims':len(r.get('claims',[]))==2,'correct_total':'Total: 80 THB' in r.get('answer',''),'not_invalid_plan':r.get('terminal_state')!='invalid_plan'}
old=copy.deepcopy(DraftSnapshotView(store).snapshot()['release']['records']['sapphire_rate'])
old['fields']['amount_minor']['value']=3000
save_owner_record(store,old,old['revision'],'controlled-owner-edit')
e2=Engine.from_snapshot(DraftSnapshotView(store).snapshot())
updated=e2.answer(q,'en',at='2026-03-16T12:00:00+07:00',allow_llm=False,understanding=u)
checks['owner_edit_recalculates_total']=bool('Total: 110 THB' in updated.get('answer','') and 'Total: 80 THB' not in updated.get('answer',''))
report={'checks':checks,'all_passed':all(checks.values()),'scope':'controlled source actual engine, no model/HTTP, no production authority'}
(o/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(o/'DETAILS.json').write_text(json.dumps({'before':r,'after_owner_edit':updated},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),**report}));assert report['all_passed']
