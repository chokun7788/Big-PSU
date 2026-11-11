"""Check task ownership when identical wording occurs more than once."""
import json,time
from verification_support import R
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.context_bindings import compile_shared
from app.knowledge.common.domain_flow.request_verifier import supplement
v=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');s=v.snapshot();index=Engine.from_snapshot(s,cache_key=v.path.resolve()).index
q='PC นักศึกษา PSU ราคาเท่าไหร่; PC นักศึกษา PSU ราคาเท่าไหร่';part=q.split(';')[0]
tasks=[MeaningTask(part,'service_fee','C06','price_calculate','amount') for _ in range(2)]
u=Understanding(tasks,True,'controlled_repeated_full_need',{})
out=R/('quote_occurrences_'+str(time.time_ns()));out.mkdir();checks={};details={}
p=compile_request(q,u,index,{'release_id':s['active'],'epoch':s['epoch']})
spans=[t.source_span for t in p.tasks];details['compiled']=p.as_dict()
checks['second_task_binds_second_occurrence']=spans[0].start==0 and spans[1].start==q.rfind(part)
checks['all_task_offsets_exact']=all(t.validate(q) for t in spans)
shared=compile_shared(q,index,u)
details['shared']=shared.as_dict()
checks['explicit_second_audience_not_shared_from_first']=not any(b.get('target_task_id')=='t2' and b.get('slot_kind')=='audience' for b in shared.event.get('shared_bindings',[]))
correction=supplement(index,q,u)
checks['observer_does_not_add_phantom_third_task']=len(correction.tasks)==2
single=compile_request(q,Understanding([tasks[0]],True,'ambiguous_single_quote',{}),index,{'release_id':s['active'],'epoch':s['epoch']})
checks['ambiguous_repeated_quote_not_silently_first']=any('occurrence' in x for x in single.tasks[0].ambiguities+single.tasks[0].errors)
same_clause='PC นักศึกษา PSU ราคาเท่าไหร่'
multi=Understanding([MeaningTask(same_clause,'service_fee','C06','detail',f) for f in ['amount','duration_minutes']],True,'two_fields_one_clause',{})
mp=compile_request(same_clause,multi,index,{'release_id':s['active'],'epoch':s['epoch']})
checks['multiple_fields_one_clause_still_share_span']=all(t.source_span.start==0 and not any('occurrence' in x for x in t.ambiguities+t.errors) for t in mp.tasks)
report={'all_passed':all(checks.values()),'checks':checks,'scope':'controlled source-bound compiler/context/observer occurrence checks; not model interpretation or full semantic proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
