import hashlib,json
from verification_support import R
def read(path):return json.loads(path.read_text('utf8'))
mutation=read(R/'compound_duration_1794131431498584000/RESULT.json')
natural=read(R/'NATURAL_DURATION_REVIEW.json')
batch=read(R/'FOCUSED_BATCH.json');assert batch['all_passed']
regressions=[]
for row in batch['rows']:
    log=R/row['stdout'].replace('\\','/').split(R.name+'/',1)[1]
    item=json.loads(log.read_text('utf8').strip().splitlines()[-1]);assert item['all_passed']
    regressions.append({'script':row['script'],'checks':len(item['checks']),'output':item.get('output',item.get('path'))})
assert mutation['all_passed'] and natural['all_passed']
files=['calculation_check.py','request_verifier.py']
report={'status':'bounded_candidate_fix_passed','root_cause':'complete-purchase prerequisite rejected partial rate authority, suppressing separately provable duration arithmetic','changed_files':{name:hashlib.sha256((R/'system/app/knowledge/common/domain_flow'/name).read_bytes()).hexdigest() for name in files},'positive_and_mutation_controls':len(mutation['checks']),'natural_TH_EN_saved_delivery_checks':len(natural['checks']),'affected_regressions':regressions,'total_bounded_checks':len(mutation['checks'])+len(natural['checks'])+sum(x['checks'] for x in regressions),'preserved_failures':['compound_duration.before.log','compound_duration.after.log','natural_compound.after.log'],'harness_corrections':['replay index now comes from actual saved draft view rather than differently named verification_support snapshot','English caveat assertion now checks the actual no-new-effective-interval sentence; saved responses were reviewed without rerunning inference'],'limitations':['no model or HTTP inference','draft/source arithmetic is not current owner authority','one rate and one explicit numeric duration only','TH/EN natural delivery uses saved generated outputs and final source verifier recheck','unknown controller input_device remains withheld','PC price plus game-controls compound still needs better missing-slot disclosure','no new 5% run and no deployment']}
(R/'INTENT_DURATION_FIX_20261108.json').write_text(json.dumps(report,indent=2)+'\n','utf8')
status=read(R/'STATUS.json');status.update({'latest_group':'compound price/booking duration evidence','latest_evidence':'INTENT_DURATION_FIX_20261108.json','latest_bounded_checks':report['total_bounded_checks'],'readiness':'source-only group passed; intent/output and model admission gates remain open','next_group':'missing-slot clarification in game-controls plus PC-price compound'})
(R/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n','utf8')
print(json.dumps(report),flush=True)
