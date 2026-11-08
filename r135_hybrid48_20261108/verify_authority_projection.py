"""Controlled source mutations verify compiler and resolver, no real data edits."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.projection import attach_rule_scope
from app.knowledge.common.domain_flow.authority_resolution import signature
checks={}
base={'category':'C13','facet':'rule_clause','record_id':'probe_a','id':'C13:probe_a:rule_clause','event_id':'event_probe','game_id':'game_probe','subject':{'th':'รายการทดลอง','en':'Controlled event'},'label':{'th':'1. ต้องใช้รูปแบบที่กำหนด','en':'1. Players must use the declared format'},'value':{'th':'1. ต้องใช้รูปแบบที่กำหนด','en':'1. Players must use the declared format'},'evidence_refs':[{'source_id':'probe_source_a','locator':'/clause'}],'validity':{'state':'unknown'},'english_translation_missing':False}
def record(rid):return {'record_id':rid,'kind':'competition_rule','fields':{},'validity':{'state':'unknown'}}
def test(name,mutate,expected):
 a=copy.deepcopy(base);b=copy.deepcopy(base);b.update(record_id='probe_b',id='C13:probe_b:rule_clause',evidence_refs=[{'source_id':'probe_source_b','locator':'/clause'}]);records={'probe_a':record('probe_a'),'probe_b':record('probe_b')};mutate(b,records['probe_b']);facts=[a,b];attach_rule_scope(facts,records);checks[name]=len(facts)==expected
 if expected==1:checks[name+'_both_sources_retained']={r['source_id'] for r in facts[0]['evidence_refs']}=={'probe_source_a','probe_source_b'}
test('true_bilingual_duplicate',lambda b,r:None,1)
test('english_disagreement_preserved',lambda b,r:b['value'].update(en='Players may use any format'),2)
test('different_heading_preserved',lambda b,r:b['label'].update(th='เวลาในการเล่น',en='Duration'),2)
test('different_validity_preserved',lambda b,r:r.update(validity={'state':'known','effective_from':'2027-01-01T00:00:00+07:00'}),2)
test('different_conditions_preserved',lambda b,r:r['fields'].update(conditions_all={'status':'known','value':['only if registered']}),2)
test('different_game_preserved',lambda b,r:b.update(game_id='other_game'),2)
test('translation_status_preserved',lambda b,r:b.update(english_translation_missing=True),2)
class Index:pass
i=Index();i.records={'probe_a':record('probe_a'),'probe_b':record('probe_b')};i.records['probe_a']['fields']['exceptions']={'status':'unknown','value':None};i.records['probe_b']['fields']['exceptions']={'status':'not_applicable','value':None};b=copy.deepcopy(base);b['record_id']='probe_b'
checks['unknown_not_applicable_not_same_scope']=signature(i,base)!=signature(i,b)
out=R/('authority_projection_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'inferences':0,'real_data_changes':0,'controlled_source_fixtures':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(R/'AUTHORITY_PROJECTION_LATEST.json').write_text(json.dumps({'output':str(out),'all_passed':report['all_passed'],'checks':len(checks)},indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
