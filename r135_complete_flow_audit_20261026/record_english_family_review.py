"""Record the separately reviewed English split risk without rewriting data."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
def read(p):return json.loads(p.read_text('utf8'))
def ref(p):return {'path':str(p.relative_to(R)),'sha256':file_sha(p)}
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8')
family=R/'training_review_workbench_1793037663397671000/semantic_amendments_round014/FAMILY_EN_PRICE_BOOKING_141_282.json';control=R/'english_price_booking_family_controls_1793125264347249100/RESULT.json';f=read(family);c=read(control);assert c['all_passed'] and len(c['checks'])==10 and not f['current_cohorts_modified']
g=read(R/'AUDIT_GAPS.json');item={'id':'G133','requirements':['PHASE-08','CONTRACT-15'],'finding':'Individually reviewed English price-for-audience/duration/service followed by booking questions141 and282 share a phrase frame across train/development; their audience, service, duration and factual answers differ. The relationship risks overstating generalization to new phrasing.','state':'conservative_semantic_family_and_split_correction_staged_not_compiled','evidence':ref(family),'controls':ref(control),'remaining':'Incorporate the staged development grouping with other actual amendments; preserve original source/split/exposure and block historical evaluation moving into train. Other semantic and cross-language families/eight-strata coverage and original Flow acceptance are unproven.'};old=next((x for x in g['gaps'] if x['id']=='G133'),None)
if old:assert old==item
else:g['gaps'].append(item)
g['last_recorded_at']=time.time();save(R/'AUDIT_GAPS.json',g)
s=read(R/'STATUS.json');s['latest_staged_english_family']={'evidence':ref(family),'controls':ref(control),'member_rows':[141,282],'proposed_train_to_development':1,'compiled':False,'no_extra_unique_reviews':True};s['last_recorded_at']=time.time();save(R/'STATUS.json',s);print(json.dumps({'family_staged':True,'cohort_changed':False,'controls':10,'whole_flow_complete':False}))
