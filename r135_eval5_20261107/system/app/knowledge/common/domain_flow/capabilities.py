"""Versioned adapters for operators actually available in the inherited readers.

Adapter availability is not semantic validation or proof of set completeness.
Unknown operations cannot silently become a detail lookup.
"""
from .understanding import FACETS

VERSION='r135-capabilities-v2'
# A finite field/operation dispatch table. A list adapter never advertises all
# fields merely because a scalar field reader exists for that category.
SUPPORTED={
 'C01':{'detail':FACETS['C01']},
 'C02':{'detail':FACETS['C02'],'role_lookup':{'role','display_name'}},
 'C03':{'detail':FACETS['C03'],'list':{'name'},'count':{'quantity','capacity_persons','service_capacity','controllers','room_seats'}},
 'C04':{'detail':FACETS['C04'],'availability':{'studio_services','zone'},'list':{'game_catalog','players_max','zone'},'count':{'game_catalog'},'group_list':{'game_catalog','zone'},'group_count':{'game_catalog','zone'}},
 'C05':{'control':{'input_bindings'},'list':{'input_bindings'}},
 'C06':{'detail':{'amount','duration_minutes'},'price_calculate':{'amount'},'compare':{'amount','duration_minutes'}},
 'C07':{'detail':FACETS['C07'],'price_calculate':{'amount_thb'},'compare':FACETS['C07']},
 'C08':{'detail':{'owner_policy'}},'C09':{'detail':{'owner_policy','payer'}},
 'C10':{'detail':{'owner_policy'},'list':{'owner_policy'}},
 'C11':{'detail':FACETS['C11'],'list':{'open_periods','bookable_periods','maintenance_periods','service_periods'},'availability':{'open_periods','bookable_periods'}},
 'C12':{'availability':{'live_status'}},
 'C13':{'rule_lookup':{'rule_clause'},'list':{'rule_clause'},'compare':{'rule_clause'}},
 'C14':{'detail':FACETS['C14']},
}
EXTRA={cat:set(operations) for cat,operations in SUPPORTED.items()}

def resolve(category,operation,facet):
    allowed=facet in SUPPORTED.get(category,{}).get(operation,set())
    canonical={'detail':'field_lookup','availability':'relation_lookup','control':'action_lookup','role_lookup':'relation_lookup',
               'price_calculate':'calculate_total','rule_lookup':'rule_dependency_lookup'}.get(operation,operation)
    if category in {'C08','C09','C10'} and operation=='detail':canonical='condition_lookup'
    if category=='C12':canonical='resource_availability'
    if category=='C11' and operation=='availability' and facet in {'open_periods','bookable_periods'}:
        allowed=True;canonical='recorded_calendar_state'
    if category=='C06' and operation=='compare' and facet=='amount':allowed=True;canonical='compare_services'
    if category=='C04' and operation=='list' and facet=='players_max':allowed=True;canonical='filter_game_modes'
    if category=='C06' and operation=='compare' and facet=='duration_minutes':allowed=True;canonical='compare_durations'
    if category=='C06' and operation=='detail' and facet=='amount':canonical='unit_rate'
    if category=='C07' and operation=='compare':canonical='compare_packages'
    if category=='C07' and operation=='price_calculate':canonical='unit_rate'
    if category=='C13' and operation=='compare':canonical='compare_rules'
    if operation in {'count','group_count','group_list'}:
        allowed=allowed and ((category=='C04' and facet in {'game_catalog','zone'}) or (category=='C03' and facet in {'quantity','capacity_persons','service_capacity','controllers','room_seats'}))
    if category=='C04' and operation=='group_list' and facet=='zone':allowed=True
    if category=='C03' and operation=='count' and allowed:canonical='field_lookup'
    return {'version':VERSION,'category':category,'legacy_operation':operation,'operation':canonical,'field':facet,
            'status':'adapter_available' if allowed else 'unsupported_operation','executor':'capabilities.dispatch' if allowed else None,
            'implementation_entrypoint':'engine.Engine.plan' if allowed else None,'native_live_entrypoint':'integration._answer' if category=='C12' and allowed else None,
            'verification_level':'source_and_obligation_checks_required','complete_semantics_verified':False}

def matrix():
    result=[]
    for category in sorted(FACETS):
        rows=[resolve(category,op,facet) for op,fields in sorted(SUPPORTED[category].items()) for facet in sorted(fields)]
        result.append({'category':category,'adapter_rows':rows,
                       'remaining':['per-request semantic coverage needs source and obligation review','current native readers retain source/validity limitations'],
                       'all_registered_contracts_have_dispatch':True,'arbitrary_operations_supported':False,'behavior_acceptance_required_per_contract':True,'unlisted_combinations':'unsupported_operation'})
    return result

def dispatch(engine,task,meaning,question,at):
    """The actual typed-read boundary used by the compiled task executor."""
    from .readers import blocked
    capability=resolve(task.category,task.operation,task.facet)
    if capability['status']=='unsupported_operation':return blocked(task.category,'unsupported_operation')
    plan=engine.plan(task.category,question,at,meaning=meaning)
    plan.metadata['capability_dispatch']={'version':VERSION,'category':task.category,'operation':task.operation,'field':task.facet,'executor':capability['implementation_entrypoint'],'unsupported_fallback_to_detail':False}
    return plan

def catalog_for(index):
    """Combine registered operations with this exact snapshot's source inputs.

    Recorded candidates do not prove applicability to a user's question,
    currentness, public scope or semantic correctness; executors check those.
    """
    aliases={'C14':{'description':{'body'},'date':{'event_start'},'registration':{'registration_url'}},'C11':{'closing_time':{'open_periods','service_periods'},'open_periods':{'open_periods','service_periods'}}}
    result=[]
    for category in matrix():
        rows=[]
        for registered in category['adapter_rows']:
            field=registered['field'];cat=category['category'];fields=aliases.get(cat,{}).get(field,{field})
            facts=[f for f in index.bycat[cat] if f['facet'] in fields or cat=='C05' and field=='input_bindings' and f['facet'].startswith('binding_')]
            native_bindings=[rid for rid,r in index.records.items() if cat=='C12' and r.get('kind')=='live_binding']
            rows.append({**registered,'source_inputs':{'state':'external_read_required' if native_bindings else 'recorded_candidates' if facts else 'missing_source',
                'candidate_fact_count':len(facts),'source_record_ids':sorted({f['record_id'] for f in facts}|set(native_bindings)),
                'source_kinds':sorted({index.records[f['record_id']]['kind'] for f in facts}|({'live_binding'} if native_bindings else set())),
                'currentness_public_scope_and_requested_scope_checked_at_execution':True,'semantic_answer_readiness_claimed':False}})
        result.append({**category,'adapter_rows':rows})
    return {'version':VERSION,'snapshot_scope':'same_request_fact_index','categories':result,'operation_registration_not_source_completeness':True}
