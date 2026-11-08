"""Whitelisted FK traversal for explicitly requested related policy facts."""
from .registry import value
POLICY_LINKS={'game_service':'account_policy_id','closure':'resolution_policy_id'}
def linked_policies(records,record,requested):
    policy_fields={'decision','conditions_all','exceptions','details','consequence','procedure_id'}
    link=POLICY_LINKS.get(record['kind'])
    if not link or not set(requested)&(policy_fields|{link}):return []
    target=value(record,link)
    if target is None:return []
    child=records.get(target)
    if not child or child['kind']!='policy':return []
    # A request for the FK alone asks for identity, not the whole policy.
    keys=list(set(requested)&policy_fields)
    if not keys:return []
    return [(child,keys,{'from':record['record_id'],'via':link,'to':target})]
