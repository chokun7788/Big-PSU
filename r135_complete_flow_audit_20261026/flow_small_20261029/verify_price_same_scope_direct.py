import copy,json,time,sys
from pathlib import Path
from datetime import datetime
W=Path(__file__).resolve().parent;sys.path[:0]=[str(W/'system'),str(W)]
from verification_support import snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
O=W/('price_same_scope_direct_verifier_'+str(time.time_ns()));O.mkdir();checks={};details={}
clock=datetime.fromisoformat('2026-03-16T12:00:00+07:00')
def direct(s,q,rid,label,blocked):
 e=Engine.from_snapshot(s);u=Understanding([MeaningTask(q,'service_fee','C06','detail','amount')],True,'test',{'model_called':False});r=e.answer(q,'th',at=clock,allow_llm=False,understanding=u);snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);f=next(f for f in e.index.byid.values() if f['record_id']==rid and f['category']=='C06' and f['facet']=='amount');child['claims']=[{'fact_id':f['id'],'record_id':rid,'facet':'amount','value':f['value']['th'],'numeric':f['numeric'],'evidence_refs':copy.deepcopy(f['evidence_refs']),'status':'answer'}];child['status']='answer'
 a=assess(e.index,task,child,snap,q);details[label]=a;checks[label]=('source_receipt_person_rate_scope_overlap' in a['fatal']) if blocked else bool(a['receipts']) and not a['fatal']
 if blocked:
  e.index.byid[f['id']]['persons_min']=1;e.index.byid[f['id']]['persons_max']=1
  a=assess(e.index,task,child,snap,q);details[label+'_forged_projected_bounds']=a;checks[label+'_forged_projected_bounds']='source_receipt_person_rate_scope_overlap' in a['fatal']
v=DraftSnapshotView(CommonStore(W/'rate_bounds_same_scope_probe_1793305733715966500/source.sqlite'));rid='migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student';q='นักศึกษาต่างมหาลัย เล่น Nintendo Switch 1 ชั่วโมง เสียกี่บาท';direct(v.snapshot(),q,rid,'overlap_injected_claim',True)
report={'checks':checks,'all_passed':all(checks.values()),'scope':'direct verifier injection independent of planner removal; actual source snapshots and projected-bound forgery; no HTTP/model; not billing semantic proof'};(O/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'path':str(O),**report}));assert report['all_passed']
