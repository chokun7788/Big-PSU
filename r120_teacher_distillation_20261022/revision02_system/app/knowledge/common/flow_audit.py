"""Per-need attribution from the actual accepted plan, not guessed from prose."""
from dataclasses import replace
from .flow_context import CURRENT

def event(stage,**details):
    ctx=CURRENT.get()
    if ctx is not None:ctx.event(stage,**details)

def finish(result):
    if result is None:return None
    art=dict(result.decision_artifact or {});ctx=CURRENT.get();rows=art.get('need_results',[])
    failures=[]
    for r in rows:
        status=r.get('status');reasons=r.get('reason_codes',[])
        if status in {'supported','interface','not_applicable'}:continue
        stage={'needs_user_slot':'state_binding','ambiguous_interpretation':'task_interpretation','broken_relation':'relation_read',
          'not_current':'applicability_validity','conflict':'authority_conflict','live_unavailable':'live_transport',
          'temporary_failure':'processing_or_transport','unsupported':'capability_or_scope','missing_source':'evidence_insufficient',
          'partial_supported':'rendering_or_source_undercoverage'}.get(status,'adjudication_uncertain')
        audits=ctx.audits if ctx else []
        transport=next((a for a in reversed(audits) if a.get('reason') in {'model_transport_failure','model_schema_failure','model_admission','model_busy','deadline'}),None)
        if status=='temporary_failure' and transport:stage='model_body_schema' if transport.get('reason')=='model_schema_failure' else 'model_queue_transport'
        if art.get('owner_data_issues') or str((art.get('query_plan') or {}).get('bridge_status','')).startswith('owner_'):stage='owner_data_missing'
        failures.append({'need_id':r.get('need_id'),'task':r.get('task'),'status':status,'first_stage':stage,'reason_codes':reasons})
    if ctx:
        ctx.event('S11_dependencies',unmet=[r.get('unmet_dependencies',[]) for r in rows if r.get('unmet_dependencies')])
        ctx.event('S12_gap_resolution',issues=failures)
        ctx.event('S13_render',characters=len(result.answer),source_hit_count=len(result.hits))
        ctx.event('S15_finalizer',outcome=art.get('response_type'),need_statuses=[{'id':r.get('need_id'),'status':r.get('status')} for r in rows])
        art['request_context']=ctx.public()
    art['flow_audit']={'version':'r102','needs':len(rows),'issues':failures,'data_profile':art.get('content_view'),
      'source_snapshot':art.get('request_plan_snapshot') or art.get('knowledge_snapshot'),
      'attribution_basis':'terminal contracts and model audits; not independent root-cause proof','interpretation_verified_by_human':False,'model_accuracy_from_transport':False}
    return replace(result,decision_artifact=art)
