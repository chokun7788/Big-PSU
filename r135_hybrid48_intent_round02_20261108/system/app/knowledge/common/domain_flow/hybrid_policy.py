"""Predeclared reader selection. Rejected evidence never triggers a retry."""
import hashlib, json
from pathlib import Path

VERSION = 'r135-hybrid48-routing-v1'
_PATH = Path(__file__).with_name('hybrid_routes.json')

def policy():
    raw = _PATH.read_bytes()
    result = json.loads(raw)
    result['sha256'] = hashlib.sha256(raw).hexdigest()
    return result

def choose(category, operation, field):
    data = policy(); key = '|'.join((category or '', operation or '', field or ''))
    entry = data['routes'].get(key)
    return {'version': VERSION, 'key': key, 'reader': entry['reader'] if entry else 'withhold',
            'policy_sha256': data['sha256'], 'predeclared': entry is not None,
            'acceptance': entry.get('acceptance', 'pending') if entry else 'unregistered',
            'shared_renderer_and_verifier': True, 'fallback_after_rejection': False}

def plan(engine, category, question, at, meaning, native):
    # An unresolved legacy frame is kept in the existing bounded compatibility
    # contract; it cannot gain a validated operation from the routing table.
    if meaning is None:
        result = native(category, question, at, meaning)
        result.metadata['hybrid_route'] = {'version': VERSION, 'reader':'r135',
            'key':None, 'acceptance':'unresolved_frame_requires_existing_receipt_checks',
            'fallback_after_rejection':False}
        return result
    decision = choose(category, meaning.operation, meaning.facet)
    if decision['reader'] == 'r134_compat':
        from .r134_reader import plan as legacy
        result = legacy(engine, category, question, at, meaning)
    elif decision['reader'] == 'r135':
        result = native(category, question, at, meaning)
    else:
        from .readers import blocked
        result = blocked(category, 'unsupported_operation')
    result.metadata['hybrid_route'] = decision
    return result

def attach(artifact):
    contract = artifact.get('execution_contract') or {}
    routes = [e['reader_route'] for e in contract.get('executor_results', []) if e.get('reader_route')]
    artifact['hybrid'] = {'version':VERSION, 'experimental':True, 'policy_sha256':policy()['sha256'],
        'reader_routes':routes, 'native_special_paths_use_existing_contract':True,
        'full_48_acceptance_claimed':False, 'full_76_complete':False}
    return artifact
