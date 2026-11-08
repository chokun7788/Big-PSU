"""Revision-bound, source-attested claim links; no model facts or sidecar store."""
import json,re
from .registry import value,pointer,aware

VERSION='common-claims-1'
def references(record):
    out=set()
    for b in record.get('claim_bindings',[]):
        out.add(b['subject_ref'])
        for r in [b['value_ref'],*b['condition_refs'],*b['exception_refs']]:out.add(r['record_id'])
        out.update(b['actor_scope'].get('value') or [])
        out.update(b['applicability'].get('service_ids') or [])
        out.update(s.split('#',1)[0] for s in b['dependency_refs']+b['supersedes_refs'])
    return out-{record['record_id']}

def _project(ref,records):
    r=records[ref['record_id']];f=r['fields'][ref['field']]
    if f['status']!='known':raise ValueError('Claim field is not known')
    x=pointer(f['value'],ref.get('path',''))
    quote=ref.get('quote')
    if quote is not None:
        if not isinstance(x,str) or x.count(quote)!=1:raise ValueError('Claim quote must occur exactly once')
        x=quote
    if ref.get('projection','identity')=='currency_literal':
        if not isinstance(x,str):raise ValueError('Currency literal requires source text')
        matches=re.findall(r'(?<![\d.,])((?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{1,2})?)\s*(?:THB|baht|บาท)(?!\w)',x,re.I)
        if len(matches)!=1 or re.search(r'\d\s*[-–]\s*\d',x):raise ValueError('Ambiguous currency literal')
        from decimal import Decimal
        x=int(Decimal(matches[0].replace(',',''))*100)
    return x

def validate_bindings(record,records,sources,*,publish=False,demo=False):
    errors=[];seen=set()
    for b in record.get('claim_bindings',[]):
        bid=b['binding_id'];prefix='claim_bindings.'+bid+': '
        if bid in seen:errors.append(prefix+'duplicate binding id')
        seen.add(bid)
        if b['actor_scope']['status']=='known' and not isinstance(b['actor_scope']['value'],list):errors.append(prefix+'known actor scope requires explicit list')
        if b['actor_scope']['status']=='unknown' and b['actor_scope']['value'] is not None:errors.append(prefix+'unknown actor scope cannot assert audience IDs')
        for target in references({**record,'claim_bindings':[b]}):
            if target not in records:errors.append(prefix+'missing reference '+target)
        for ref in [b['value_ref'],*b['condition_refs'],*b['exception_refs']]:
            try:
                _project(ref,records)
                if not records[ref['record_id']]['fields'][ref['field']].get('evidence_refs'):errors.append(prefix+'claim value has no source evidence')
            except (KeyError,IndexError,TypeError,ValueError):errors.append(prefix+'invalid value/condition/exception reference')
        origin=records.get(b['value_ref']['record_id'],{})
        if b['predicate']=='game_access' and (origin.get('kind')!='policy' or b['value_ref']['field']!='decision'):errors.append(prefix+'game access requires a policy decision, not offering/capacity')
        if origin.get('kind')=='policy':
            for source_field,refs_key,state_key in [('conditions_all','condition_refs','conditions_status'),('exceptions','exception_refs','exceptions_status')]:
                if b.get(state_key)=='known' and value(origin,source_field):
                    if not any(x['record_id']==origin['record_id'] and x['field']==source_field for x in b[refs_key]):errors.append(prefix+'required policy '+source_field+' would be dropped')
        for full in b['dependency_refs']+b['supersedes_refs']:
            rid,_,target=full.partition('#')
            other=records.get(rid,{})
            typed_amount=other.get('kind')=='rate' and target=='amount_minor' and value(other,'amount_minor') is not None
            if not typed_amount and not any(x['binding_id']==target for x in other.get('claim_bindings',[])):errors.append(prefix+'missing claim reference '+full)
            if full==record['record_id']+'#'+bid:errors.append(prefix+'self claim dependency')
        for a in b['actor_scope'].get('value') or []:
            if a in records and records[a]['kind']!='audience':errors.append(prefix+'actor must reference audience')
        app=b['applicability']
        try:
            start,end=[aware(app[k]) if app[k] else None for k in ('effective_from','effective_until')]
            if start and end and start>=end:errors.append(prefix+'inverted applicability interval')
        except (ValueError,TypeError):errors.append(prefix+'invalid applicability date')
        if publish and (b['actor_scope']['status']!='known' or app['status']!='known'):errors.append(prefix+'claim scope needs confirmation before publication')
        if publish and any(b.get(k)!='known' for k in ('conditions_status','exceptions_status')):errors.append(prefix+'claim conditions and exceptions need confirmation')
        if b['predicate']=='current_rate' and (not app['effective_from'] or not b['unit'] or not app['duration_minutes']):errors.append(prefix+'current rate needs date, billing unit and duration')
        # The mapping itself has evidence, distinct from the referred value.
        for ref in b['evidence_refs']+b['authority_refs']:
            pair=sources.get(ref['source_id'])
            if pair is None:errors.append(prefix+'missing mapping source');continue
            src,body=pair
            from .registry import source_errors
            errors.extend(prefix+e for e in source_errors(src,body,demo=demo))
            if record['kind'] not in src['authority_for']:errors.append(prefix+'mapping source authority mismatch')
            if ref in b['authority_refs']:
                for target in b['supersedes_refs']:
                    other=records.get(target.split('#',1)[0],{})
                    if other.get('kind') not in src['authority_for']:errors.append(prefix+'authority source does not cover replaced claim kind')
            if publish and src['trust'] not in ({'official','internal_verified','owner_confirmed','synthetic'} if demo else {'official','internal_verified','owner_confirmed'}):errors.append(prefix+'mapping source needs review')
            try:
                actual=pointer(json.loads(body),ref['locator'])
                if ref in b['evidence_refs'] and actual!={k:v for k,v in b.items() if k not in {'evidence_refs','authority_refs'}}:errors.append(prefix+'mapping does not match source pointer')
                if ref in b['authority_refs'] and (not isinstance(actual,dict) or any(actual.get(k)!=b[k] for k in ('subject_ref','predicate','supersedes_refs','applicability'))):errors.append(prefix+'authority source does not confirm supersession scope')
            except (KeyError,IndexError,ValueError,TypeError):errors.append(prefix+'invalid mapping evidence pointer')
        if not b['evidence_refs']:errors.append(prefix+'mapping requires evidence')
    return errors

def release_binding_errors(records):
    edges={r['record_id']+'#'+b['binding_id']:b['dependency_refs']+b['supersedes_refs'] for r in records.values() for b in r.get('claim_bindings',[])}
    def visit(k,stack):
        if k in stack or len(stack)>20:raise ValueError('Cyclic or excessive claim dependency')
        for other in edges.get(k,[]):visit(other,stack|{k})
    errors=[]
    for k in edges:
        try:visit(k,set())
        except ValueError as e:errors.append(k+': '+str(e))
    return errors

def index(records):
    return {'version':VERSION,'claims':[{'claim_id':rid+'#'+b['binding_id'],'record_id':rid,'revision':r['revision'],'binding':b} for rid,r in records.items() for b in r.get('claim_bindings',[])]}

def current_claims(snapshot,at):
    from .answer import effective
    records=snapshot['release']['records'];withdrawn=set(snapshot.get('withdrawn',[]));out=[]
    for rid,r in records.items():
        if rid in withdrawn or not effective(r,at,records):continue
        for b in r.get('claim_bindings',[]):
            a=b['applicability'];actors=b['actor_scope']
            if a['status']!='known' or actors['status']!='known':continue
            if any(b.get(k)!='known' for k in ('conditions_status','exceptions_status')):continue
            if (a['effective_from'] and at<aware(a['effective_from'])) or (a['effective_until'] and at>=aware(a['effective_until'])):continue
            ids={b['subject_ref'],*[ref['record_id'] for ref in [b['value_ref'],*b['condition_refs'],*b['exception_refs']]]}
            if ids & withdrawn or any(k not in records or not effective(records[k],at,records) for k in ids):continue
            try:val=_project(b['value_ref'],records)
            except (KeyError,IndexError,ValueError,TypeError):continue
            if b['predicate']=='game_access':
                if records[b['value_ref']['record_id']]['kind']!='policy' or b['value_ref']['field']!='decision':continue
                val={'allowed':True,'prohibited':False}.get(val,val)
            ref=b['value_ref'];field=records[ref['record_id']]['fields'][ref['field']]
            out.append({'claim_id':rid+'#'+b['binding_id'],'record_id':rid,'revision':r['revision'],'subject_ref':b['subject_ref'],
              'predicate':b['predicate'],'value':val,'unit':b['unit'],'actors':actors['value'],'applicability':a,
              'condition_refs':b['condition_refs'],'exception_refs':b['exception_refs'],'dependency_refs':b['dependency_refs'],
              'supersedes_refs':b['supersedes_refs'],'authority_refs':b['authority_refs'],'mapping_evidence':b['evidence_refs'],
              'value_ref':ref,'value_evidence':field['evidence_refs'],'release_id':snapshot['active'],'epoch':snapshot['epoch']})
    return out

def conflicts(selected,snapshot,at):
    from .answer import effective
    claims=current_claims(snapshot,at);records=snapshot['release']['records'];selected=set(selected)
    # Include structured prices so a mapped FAQ and rate share one claim key.
    for rid,r in records.items():
        if r['kind']!='rate' or rid in snapshot.get('withdrawn',[]) or r['validity']['state']!='known' or not effective(r,at,records):continue
        keys=('service_id','audience_id','amount_minor','unit','duration_minutes')
        if any(value(r,k) is None for k in keys):continue
        claims.append({'claim_id':rid+'#amount_minor','record_id':rid,'subject_ref':value(r,'service_id'),'predicate':'current_rate','value':value(r,'amount_minor'),
          'unit':value(r,'unit'),'actors':[value(r,'audience_id')],'applicability':{'service_ids':[value(r,'service_id')],'duration_minutes':value(r,'duration_minutes'),'platform':None},
          'condition_refs':[],'exception_refs':[],'dependency_refs':[],'supersedes_refs':[],'authority_refs':[],'revision':r['revision']})
    buckets={}
    for c in claims:
        a=c['applicability'];key=(c['subject_ref'],c['predicate'],c['unit'],tuple(sorted(c['actors'])),tuple(sorted(a['service_ids'])),a['duration_minutes'],a['platform'])
        # Different explicit conditions do not prove a contradiction.
        if c['condition_refs'] or c['exception_refs']:continue
        buckets.setdefault(key,[]).append(c)
    result=[]
    for key,rows in buckets.items():
        if not any(c['record_id'] in selected or c['subject_ref'] in selected for c in rows):continue
        superseded={s for c in rows if c['authority_refs'] for s in c['supersedes_refs']}
        remaining=[c for c in rows if c['claim_id'] not in superseded]
        if len({json.dumps(c['value'],sort_keys=True,ensure_ascii=False) for c in remaining})>1:
            result.append({'predicate_key':key,'alternatives':remaining,'authority_resolution':'unresolved','reason':'mapped_current_claims_disagree'})
    return result
