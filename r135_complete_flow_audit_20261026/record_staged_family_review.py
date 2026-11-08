"""Record a verified risk and staged split correction, without closing P5."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
def read(p):return json.loads(p.read_text('utf8'))
def ref(p):return {'path':str(p.relative_to(R)),'sha256':file_sha(p)}
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8')
family=R/'training_review_workbench_1793037663397671000/semantic_amendments_round014/FAMILY_PSU_PRICE_BOOKING_104_133_134_135.json';control=R/'shared_template_family_controls_1793125131222348400/RESULT.json';f=read(family);c=read(control);assert c['all_passed'] and len(c['checks'])==11 and not f['current_cohorts_modified']
g=read(R/'AUDIT_GAPS.json');item={'id':'G132','requirements':['PHASE-08','CONTRACT-15'],'finding':'Four individually reviewed PSU-student price-and-booking requests share the same Thai frame and differ in service/duration; three are in train and one in development under distinct original families. They are not identical factual questions, but the shared frame can overstate generalization to new phrasing.','state':'conservative_semantic_family_and_split_correction_staged_not_compiled','evidence':ref(family),'controls':ref(control),'remaining':'Incorporate the staged development grouping in a new cohort without overwriting original memberships; re-run split/negative exposure checks. Review other semantic and cross-language families, all eight strata, sparse limits, metrics and full original Flow acceptance.'};old=next((x for x in g['gaps'] if x['id']=='G132'),None)
if old:assert old==item
else:g['gaps'].append(item)
g['last_recorded_at']=time.time();save(R/'AUDIT_GAPS.json',g)
s=read(R/'STATUS.json');s['latest_staged_semantic_family']={'evidence':ref(family),'controls':ref(control),'member_rows':[104,133,134,135],'proposed_train_to_development':3,'compiled':False,'no_extra_unique_reviews':True};s['last_recorded_at']=time.time();save(R/'STATUS.json',s);print(json.dumps({'family_staged':True,'cohort_changed':False,'controls':11,'whole_flow_complete':False}))
