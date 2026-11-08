"""Reconstruct registered display projections from pinned source and request.

Metadata naming a projection is not evidence that its output was computed.
Validate customer-facing derived text as well as the claim retained for audit.
"""
from .projection import value,bilingual


def check(index,fact,claim,metadata,snapshot,question):
    if fact['facet']=='specifications' and metadata.get('specification_keys'):
        from .precision import equipment
        expected=equipment(index,question)
        if not expected or fact['id'] not in expected.ids:return None
        keys=expected.metadata.get('specification_keys')
        if keys!=metadata.get('specification_keys'):return None
        entries=[x for x in value(index.records[fact['record_id']],'specifications') or [] if isinstance(x,dict) and str(x.get('key','')).upper() in keys]
        values={'; '.join(str(x['key'])+': '+bilingual(x['value'])[lang] for x in entries) for lang in ('th','en')}
        if entries and claim.get('value') in values:return 'registered_specification_projection_recomputed'
    if fact['category']=='C11' and fact['id']==metadata.get('calendar_service_fact_id'):
        from .service_calendar import plan
        from .scope import reference_time
        try:expected=plan(index,question,reference_time(snapshot['reference_time']))
        except (KeyError,ValueError,TypeError):return None
        if not expected or fact['id'] not in expected.ids:return None
        fields=('calendar_service_fact_id','calendar_service_answer','customer_calendar_answer','calendar_semantics','local_date','weekday','calendar_window_evaluation','calendar_source_limits','unconfirmed_closure_record_ids')
        if any(metadata.get(k)!=expected.metadata.get(k) for k in fields):return None
        if claim.get('value') in expected.metadata.get('calendar_service_answer',{}).values():return 'registered_calendar_projection_recomputed'
    return None
