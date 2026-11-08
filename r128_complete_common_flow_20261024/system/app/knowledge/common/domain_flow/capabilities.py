"""Versioned adapters for operators actually available in the inherited readers.

Adapter availability is not semantic validation or proof of set completeness.
Unknown operations cannot silently become a detail lookup.
"""
from .understanding import FACETS

VERSION='r123-capabilities-v1'
EXTRA={
 'C01':{'detail'},'C02':{'detail','role_lookup'},'C03':{'detail','list','count'},
 'C04':{'detail','availability','list','count','group_count','group_list'},
 'C05':{'control','list'},'C06':{'detail','price_calculate'},
 'C07':{'detail','price_calculate'},'C08':{'detail'},'C09':{'detail'},
 'C10':{'detail','list'},'C11':{'detail','list','availability'},'C12':{'availability'},
 'C13':{'rule_lookup','list'},'C14':{'detail'},
}

def resolve(category,operation,facet):
    allowed=operation in EXTRA.get(category,set()) and facet in FACETS.get(category,set())
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
    if operation in {'count','group_count','group_list'}:
        allowed=allowed and ((category=='C04' and facet=='game_catalog') or (category=='C03' and facet in {'quantity','capacity_persons','service_capacity','controllers','room_seats'}))
    if category=='C04' and operation=='group_list' and facet=='zone':allowed=True
    if category=='C03' and operation=='count' and allowed:canonical='field_lookup'
    return {'version':VERSION,'category':category,'legacy_operation':operation,'operation':canonical,'field':facet,
            'status':'adapter_available' if allowed else 'unsupported_operation','executor':'native_domain_reader' if allowed else None,
            'verification_level':'source_and_obligation_checks_required','complete_semantics_verified':False}

def matrix():
    result=[]
    for category in sorted(FACETS):
        rows=[resolve(category,op,facet) for op in sorted(EXTRA.get(category,set())|({'compare'} if category=='C06' else set())) for facet in sorted(FACETS[category])]
        result.append({'category':category,'adapter_rows':[r for r in rows if r['status']=='adapter_available'],
                       'remaining':['shared-prefix semantics not fully implemented','current native readers retain source/validity limitations'],
                       'all_operations_implemented':False,'unlisted_combinations':'unsupported_operation'})
    return result
