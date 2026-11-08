"""Bounded total and notice checks against an isolated controlled source."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
o=R/('total_notice_fixture_'+str(time.time_ns()));o.mkdir()
store=CommonStore(o/'source.sqlite');store.initialize(allow_demo=False)
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
create('service','amber_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'session_minutes':30})
create('audience','amber_audience',{'name':{'th':'กลุ่มอำพัน','en':'Amber visitors'}})
rate=create('rate','amber_rate',{'service_id':'amber_service','audience_id':'amber_audience','amount_minor':12300,'currency':'THB','unit':'per_person','duration_minutes':30,'persons_min':1,'persons_max':1})
view=DraftSnapshotView(store);rows=[]
def run(q,lang):
 e=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'controlled',{'model_called':False})
 r=e.answer(q,lang,at='2026-03-16T12:00:00+07:00',allow_llm=False,understanding=u);rows.append({'q':q,'result':r});return r
x=run('What is the total price for 2 people for Amber service for Amber visitors?','en')
y=run('What is the price for Amber service for Amber visitors?','en')
checks={'true_total_shown_without_unconfirmed_notice':'Total: 246 THB' in x['answer'] and 'requested total cannot' not in x['answer'].lower(),'ordinary_price_has_no_unconfirmed_notice':'requested total cannot' not in y['answer'].lower()}
z=run('ราคารวม 2 คน บริการอำพัน กลุ่มอำพัน เท่าไหร่','th')
checks['thai_true_total_no_false_notice']='รวม 246 บาท' in z['answer'] and 'ยังคำนวณยอดรวมที่ถามไม่ได้' not in z['answer']
z=run('ราคารวม บริการอำพัน กลุ่มอำพัน เท่าไหร่','th')
checks['thai_total_without_quantity_disclosed']='ยังคำนวณยอดรวมที่ถามไม่ได้' in z['answer']
edited=copy.deepcopy(rate);edited['fields']['amount_minor']['value']=12400
save_owner_record(store,edited,edited['revision'],'controlled-owner-edit')
z=run('What is the total price for 2 people for Amber service for Amber visitors?','en')
checks['edited_rate_total_refreshed']='Total: 248 THB' in z['answer'] and 'Total: 246 THB' not in z['answer']
report={'checks':checks,'all_passed':all(checks.values()),'scope':'controlled source, positive total and ordinary price only; no authority or transaction'}
(o/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(o/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),**report}));assert report['all_passed']
