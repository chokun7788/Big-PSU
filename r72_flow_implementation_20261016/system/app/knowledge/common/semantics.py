"""Developer meanings and presentation rules, separate from approved facts."""
import json
from pathlib import Path
from .registry import CATALOG
HOME=Path(__file__).resolve().parent
SEMANTICS=json.loads((HOME/'schema_descriptions.json').read_text(encoding='utf-8'))
PROFILES=json.loads((HOME/'answer_profiles.json').read_text(encoding='utf-8'))
def meaning(kind,key,lang):
    spec=next(f for f in CATALOG[kind]['fields'] if f['key']==key)
    item=SEMANTICS.get('kinds',{}).get(kind,{}).get(key,SEMANTICS['fields'].get(key,{}))
    return item.get('description_'+lang) or (spec['meaning_th'] if lang=='th' else key.replace('_',' '))
def label(kind,key,lang):
    return PROFILES.get('labels',{}).get(kind,{}).get(key,{}).get(lang) or (next(f['meaning_th'] for f in CATALOG[kind]['fields'] if f['key']==key) if lang=='th' else key.replace('_',' '))
def project(record,requested,*,full=False):
    """Keep necessary scope/conditions without expanding the whole record."""
    fields=record['fields'];kind=record['kind']
    if full:
        # These fields support search/order/review rather than customer facts.
        hidden={'source_order','facets','intent_key','source_variants','profile_role'}
        if kind=='procedure' and fields.get('name',{}).get('status')=='known':hidden.add('topic')
        keys=[k for k in fields if k not in hidden]
        if kind=='control_set' and fields.get('bindings',{}).get('status')=='known' and fields.get('limitations',{}).get('status')=='known':
            rows=fields['bindings']['value'];old=fields['limitations']['value']
            def table(lang):
                def cell(v):return v.get(lang) or '' if isinstance(v,dict) else ''
                return '\n'.join(' | '.join((cell(r.get('button_label')),cell(r['action']),cell(r.get('notes')),cell(r.get('section')))) for r in rows)
            # Hide only a byte-equivalent old representation, not new limitations.
            if isinstance(old,dict) and all((old.get(lang) or '')==table(lang) for lang in ('th','en')):keys.remove('limitations')
        return keys,{k:'explicit_all' for k in keys}
    keys=[k for k in requested if k in fields];basis={k:'explicit' for k in keys}
    profile=PROFILES['kinds'].get(kind,{})
    for rule in profile.get('context',[]):
        if '*' not in rule['when'] and not set(keys)&set(rule['when']):continue
        for key in rule['include']:
            if key in fields and key not in keys and fields[key]['status'] not in {'unknown','not_applicable'}:keys.append(key);basis[key]='necessary_context'
    return keys,basis
