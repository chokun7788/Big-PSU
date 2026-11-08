"""Prove collection membership separately from source-set completeness."""
def verify(index,task,result,question=None,at=None):
    meta=result.get('plan',{}).get('metadata',{});claims=result.get('claims',[])
    facts=[index.byid.get(c.get('fact_id')) for c in claims]
    if not facts or any(f is None for f in facts):
        return {'verified':False,'kind':'unknown_coverage','member_ids':[],'reason':'collection_members_not_proven'}
    records={c['record_id'] for c in claims};member_ids=sorted(records);membership=True;scope_verified=True;groups={};group_verified=None
    from .controller_catalog import selection as controller_selection,scope_identity,FACET as CONTROLLER_FACET
    controller=controller_selection(index,question,at) if task.category=='C04' and question else None
    if controller is not None and task.facet in {'game_catalog','zone'}:
        expected={f['id'] for f in controller['facts']};members={f.get('game_id') for f in facts}
        membership=all(f['facet']==CONTROLLER_FACET and index.records.get(f.get('game_id'),{}).get('kind')=='game' for f in facts)
        scope_verified={c['fact_id'] for c in claims}==expected and scope_identity(meta.get('controller_catalog_scope'))==scope_identity(controller)
        member_ids=sorted(members) if membership else []
        membership=membership and set(member_ids)==set(meta.get('catalog_member_ids',[]))
        if controller['request']['group_by']:
            groups=controller['groups'];group_verified=bool(groups) and meta.get('catalog_group_members')==groups
            membership=membership and group_verified
    elif task.category=='C04' and task.facet=='game_catalog':
        members={rid for f in facts for rid in f.get('member_ids',[])}
        membership=all(f['facet']=='game_catalog' for f in facts) and all(index.records.get(rid,{}).get('kind')=='game' for rid in members)
        if 'catalog_member_ids' in meta:membership=membership and members==set(meta['catalog_member_ids'])
        if meta.get('operator') in {'group_count','group_list'}:
            from .projection import value
            for f in facts:
                key=str(value(index.records.get(f['record_id'],{}),'platform') or f['subject']['en'])
                groups.setdefault(key,set()).update(f.get('member_ids',[]))
            groups={key:sorted(members) for key,members in groups.items()}
            group_verified=groups==meta.get('catalog_group_members')
            membership=membership and group_verified
        member_ids=sorted(members)
        span=getattr(task,'target_span',None) or getattr(task,'source_span',None)
        bound=index.bind('C04',span.text) if span is not None else []
        expected=[f for f in (bound or index.bycat['C04']) if f['facet']=='game_catalog']
        scope_verified={c['fact_id'] for c in claims}=={f['id'] for f in expected}
    elif task.category=='C04' and task.facet=='zone' and meta.get('grouping_kind')=='zone':
        for f in facts:
            for zid in f.get('zone_ids',[]):groups.setdefault(zid,set()).add(f['record_id'])
        groups={key:sorted(members) for key,members in groups.items()}
        group_verified=bool(groups) and groups==meta.get('group_member_ids') and all(index.records.get(zid,{}).get('kind')=='zone' for zid in groups)
        membership=group_verified
    elif task.category=='C05':
        from .control_scope import candidates,requested_button_count,physical_subset
        span=getattr(task,'source_span',None);q=question if question is not None else span.text if span else ''
        full={f['id'] for f in candidates(index,q)}
        membership=len(records)==1 and {c['fact_id'] for c in claims}==full
        if requested_button_count(index,q) is not None:
            subset=physical_subset(index,q,facts);membership=bool(subset['verified']);scope_verified=subset['verified'];full=set(subset['source_fact_ids'])
        member_ids=sorted(full)
    elif task.category=='C11' and task.facet=='service_periods':
        from .period_scope import plan,verify as verify_period
        expected=plan(index,question,at)
        membership=bool(expected and expected.ids) and all(f['facet']=='service_periods' for f in facts)
        scope_verified=membership and verify_period(index,task,claims,meta,question,at)
        member_ids=sorted(f['record_id'] for f in facts) if membership else []
    elif task.category=='C11' and type(meta.get('weekday_count')) is int:
        from .calendar_sets import source_set,weekly_requested,requested_weekdays
        from .projection import value
        span=getattr(task,'source_span',None);q=question if question is not None else span.text if span is not None else ''
        facet='service_periods' if meta.get('calendar_semantics')=='play_service_only_not_physical_building_hours_or_live_occupancy' and task.facet=='open_periods' else task.facet
        try:expected=source_set(index,facet,q,at)['facts']
        except ValueError:expected=[]
        days=requested_weekdays(q)
        weekdays=[value(index.records[f['record_id']],'weekday') for f in facts]
        membership=(weekly_requested(q) or getattr(task,'operation',None)=='list') and sorted(weekdays)==sorted(days) and meta.get('weekday_count')==len(days) and meta.get('requested_weekdays')==days and all(f['facet']==facet for f in facts)
        scope_verified={c['fact_id'] for c in claims}=={f['id'] for f in expected}
        member_ids=[str(day) for day in weekdays]
    elif 'member_ids' in meta:
        membership=set(meta['member_ids'])==records
        from .collection_scopes import expected as source_expected
        source_span=getattr(task,'source_span',None)
        full=source_expected(index,task,source_span.text if source_span is not None else '')
        scope_verified=full is not None and {c['fact_id'] for c in claims}=={f['id'] for f in full}
    scope_refs=[]
    if task.category=='C03' and task.facet=='name':
        from .collection_scopes import inventory_refs
        span=getattr(task,'source_span',None)
        scope_refs=inventory_refs(index,question if question is not None else span.text if span else '',facts)
    # A populated member list proves a subset, never exhaustiveness by itself.
    exact=bool(meta.get('complete_set') is True and membership and scope_verified)
    return {'verified':exact,'kind':'exact_set' if exact else 'confirmed_subset' if membership else 'unknown_coverage',
            'member_ids':member_ids if membership else [],'membership_verified':membership,
            'scope_verified':scope_verified,'source_completeness_declared':meta.get('complete_set') is True,
            'groups':groups,'group_membership_verified':group_verified,'source_scope_refs':scope_refs,
            'reason':'declared_complete_source_set_and_members_verified' if exact else 'collection_completeness_not_proven' if membership else 'collection_member_identity_mismatch',
            'physical_world_completeness_claimed':False}
