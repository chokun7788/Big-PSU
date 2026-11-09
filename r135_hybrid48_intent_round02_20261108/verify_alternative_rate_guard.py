"""Exercise independent arithmetic guard with captured source-backed rates."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.calculation_check import errors
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
folder=R/'pc_assessment_1794163037792720700'
rows=json.loads((folder/'DETAILS.json').read_text('utf8'))
idx=Engine.from_snapshot(DraftSnapshotView(CommonStore(folder/'source.sqlite')).snapshot()).index
checks={}
for row in rows:
 q=row['task_question'];base={'computations':row['computations'],'answer':''};name='compound' if 'Tekken' in row['outer_question'] else 'single'
 checks[name+'_separate_unit_rates_accepted']=not errors(idx,q,base)
 changed=copy.deepcopy(base);changed['computations'][0]['total_thb']=9999;checks[name+'_forged_rate_rejected']=bool(errors(idx,q,changed))
 changed=copy.deepcopy(base);changed['computations'][0]['billing_quantity']=2;checks[name+'_forged_quantity_rejected']=bool(errors(idx,q,changed))
 checks[name+'_requested_total_without_counts_rejected']=bool(errors(idx,q+' ราคารวมทั้งหมด',base))
 changed=copy.deepcopy(base);changed['answer']='รวม 9999 บาท';checks[name+'_rendered_total_rejected']=bool(errors(idx,q,changed))
 changed=copy.deepcopy(base);changed['answer']='ราคารวมเป็น 165 บาท';checks[name+'_thai_labeled_total_rejected']=bool(errors(idx,q,changed))
 changed=copy.deepcopy(base);changed['answer']='The total is 165 THB';checks[name+'_english_labeled_total_rejected']=bool(errors(idx,q,changed))
 changed=copy.deepcopy(base);changed['computations'][0]['fact_id']='unknown';checks[name+'_unknown_source_rejected']=bool(errors(idx,q,changed))
out=R/('alternative_rate_guard_'+str(time.time_ns()));out.mkdir()
report={'checks':checks,'all_passed':all(checks.values()),'model_calls':0,'scope':'direct guard replay, not answer delivery or business authority'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
