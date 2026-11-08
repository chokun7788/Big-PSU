"""C07 owner-added fields and joins, beyond the one sampled legacy request."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.scope import reference_time
out=R/('rental_fields_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled_rental.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};rows=[]
def known(value):return {'status':'known','value':value,'evidence_refs':[],'note':''}
def save(kind,rid,fields,version=0):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'}
 for k,v in fields.items():r['fields'][k]=known(v)
 return save_owner_record(store,r,version,'controlled-test')['record']
save('zone','controlled_blue_zone',{'name':{'th':'โซนบลูทดสอบ','en':'Blue test zone'}})
save('audience','controlled_blue_organization',{'name':{'th':'หน่วยงานบลูทดสอบ','en':'Blue test organization'}})
package=save('rental_package','controlled_blue_package',{'name':{'th':'แพ็กเกจบลูทดสอบ','en':'Blue package'},'zone_ids':['controlled_blue_zone'],'audience_id':'controlled_blue_organization','period_label':'custom','duration_minutes':240,'amount_minor':123400,'currency':'THB','equipment_included':{'th':'จอยทดสอบสองชุด','en':'Two controlled controllers'},'room_seats':7,'terms':{'th':'ใช้เฉพาะช่วงที่ยืนยันโดยเจ้าหน้าที่','en':'Only during a staff-confirmed interval'}})
def run(q,facet):
 e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);u=Understanding([MeaningTask(q,'rental','C07','detail',facet,'Blue package')],True,'controlled_rental_fields',{'model_called':False});r=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u);rows.append({'q':q,'result':r});return r
for facet,q,expected in [('zone','Which zones are included in Blue package?','Blue test zone'),('audience','Which organization is Blue package for?','Blue test organization'),('duration_minutes','What is the duration of Blue package?','240'),('amount_thb','What is the price of Blue package?','1234'),('equipment_included','What equipment is included in Blue package?','Two controlled controllers'),('room_seats','How many room seats does Blue package have?','7'),('terms','What terms apply to Blue package?','staff-confirmed interval')]:
 r=run(q,facet);checks[facet+'_owner_source_delivered']=any(c['facet']==facet and expected in c['value'] for c in r['claims']) and not any(n['execution_contract']['fatal'] for n in r['needs'])
 if facet in {'zone','audience'}:checks[facet+'_joins_have_both_source_sides']=any(len(c['evidence_refs'])>=2 for c in r['claims'] if c['facet']==facet)
bad=copy.deepcopy(package);bad['fields']['audience_id']=known('controlled_blue_zone')
try:save_owner_record(store,bad,1,'controlled-negative');checks['wrong_organization_foreign_kind_rejected']=False
except ValueError as error:checks['wrong_organization_foreign_kind_rejected']='wrong reference kind' in str(error)
edit=copy.deepcopy(package);edit['fields']['equipment_included']=known({'th':'จอยทดสอบสามชุด','en':'Three controlled controllers'});save_owner_record(store,edit,1,'controlled-test');r=run('What equipment is included in Blue package?','equipment_included');checks['owner_edit_changes_inclusions_without_new_weights']='Three controlled controllers' in r['answer'] and 'Two controlled controllers' not in r['answer']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_data_modified':False,'controlled_source_not_real_business_data':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
