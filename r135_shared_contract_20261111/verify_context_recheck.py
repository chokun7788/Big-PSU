"""A fresh context review must recompute authority; old event tags are not proof."""
import json,time
from verification_support import R
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
v=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');snap=v.snapshot();i=Engine.from_snapshot(snap,cache_key=v.path.resolve()).index
q='Andaman Hotel อยู่ที่ไหน; จองยังไง'
u=Understanding([MeaningTask('Andaman Hotel อยู่ที่ไหน','contact','C01','detail','address'),MeaningTask('จองยังไง','reservation','C08','detail','owner_policy',target='PC')],True,'forced_test',{'context_scope_review':[{'action':'source_related_booking_ellipsis','task_quote':'จองยังไง','source_quote':'PC'}]})
u=apply(q,i,u)
checks={'unbound_target_removed':u.tasks[1].target=='','forged_audit_not_reused':not any(a.get('action')=='source_related_booking_ellipsis' and a.get('source_quote')=='PC' for a in u.event.get('context_scope_review',[]))}
u.tasks[1].target='PC';u.event['context_scope_review']=[{'action':'source_related_booking_ellipsis','task_quote':'จองยังไง','source_quote':'PC'}]
plan=compile_request(q,u,i,{'release_id':snap['active'],'epoch':snap['epoch']})
checks['compiler_still_rejects_target_absent_from_request']=bool(plan.tasks[1].errors) and plan.tasks[1].target_scope=='none'
out=R/('context_recheck_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'scope':'direct forced stale event/target controls, not a natural model or authority acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
