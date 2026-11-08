"""Executable required/alternative/optional field graphs over a pinned release.

This verifies typed facts, applicability and joins. It does not claim to solve
arbitrary prose entailment. Missing owner data stays missing.
"""
from dataclasses import dataclass,field,asdict
from .registry import value,CATALOG

@dataclass
class Node:
    op:str
    children:list=field(default_factory=list)
    record_id:str=''
    key:str=''
    reason:str=''

def fact(rid,key):return Node('field',record_id=rid,key=key)
def all_of(*nodes):return Node('all_of',list(nodes))
def any_of(*nodes):return Node('any_of',list(nodes))
def optional(node):return Node('optional',[node])
def not_applicable(reason):return Node('not_applicable',reason=reason)

# Each entry is alternative REQUIRED field sets. Context fields are optional.
# One local field is never made required just because it happens to exist.
REQUIRED={
 'game_overview':(('summary',),),'game_how_to_play':(('how_to_play',),),
 'game_platforms':(('supported_platforms',),),'game_at_studio':(('offered','service_id'),),
 'game_players':(('players_min','players_max'),),'game_controls':(('bindings',),('limitations',)),
 'game_account':(('decision','conditions_all','details'),),
 'game_version':(('game_version',),),'equipment_explain':(('name','device_type'),),
 'equipment_specs':(('specifications',),),'equipment_location':(('name',),),
 'equipment_list':(('name',),),'resource_capacity':(('capacity_min','capacity_max'),('capacity_persons',)),
 'service_duration':(('session_minutes',),),'center_operator':(('operator',),),
 'center_location':(('address',),('building','floor'),('map_url',)),
 'center_overview':(('name','description'),),'contact':(('channel','value'),),
 'facility':(('name','location'),),'people':(('display_name','role','public_scope'),),
 'audience':(('name','eligibility','required_proofs'),),
 'price':(('amount_minor','currency','unit','duration_minutes','calculation_rule'),),
 'rental':(('amount_minor','currency','duration_minutes','terms'),),
 'policy':(('decision','conditions_all','exceptions','details'),('answer',)),
 'procedure':(('steps','preconditions'),('answer',)), 'faq_content':(('answer',),),
 'competition_rules':(('text','completeness'),),
 'competition_metadata':(('event_name','rulebook_release'),),
 'schedule':(('open_periods',),),'news':(('title','body'),),
 'live_status':(('service_id','provider','external_resource_key','status_mapping','freshness_policy','freshness_max_age_seconds'),),
 'schema_attributes':(),
}
TARGETS={
 'game_players':{'game_mode'},'game_controls':{'control_set'},'game_account':{'policy'},
 'game_at_studio':{'game_service'},'game_version':{'game_service','control_set'},
 'competition_rules':{'competition_rule'},'price':{'rate'},'rental':{'rental_package'},
 'equipment_specs':{'equipment_model'},'resource_capacity':{'service','resource'},
 'equipment_location':{'zone'},'equipment_list':{'resource','equipment_model'},
}
def linked(records,roots,task):
    """Schema-declared FK paths only, forward + reverse, bounded and cycle-safe."""
    wanted=TARGETS.get(task);selected=[];seen=set(roots);front=list(roots);edges=[]
    if not wanted:return list(roots),[]
    if all(records.get(k,{}).get('kind') in wanted for k in roots):return list(roots),[]
    # Build the inverse index once, rather than scanning the full release at
    # every node. Only declared semantic paths are traversable.
    reverse={}
    for cid,c in records.items():
        for spec in CATALOG[c['kind']]['fields']:
            if not spec.get('reference_kind'):continue
            v=value(c,spec['key'])
            for target in v if isinstance(v,list) else [v]:
                if isinstance(target,str):reverse.setdefault(target,[]).append((cid,spec['key']))
    paths={
      'game_players':{('game','game_mode')},'game_controls':{('game','control_set')},
      'game_at_studio':{('game','game_service')},'game_version':{('game','game_service'),('game','control_set')},
      'game_account':{('game','game_service'),('game_service','policy')},
      'competition_rules':{('game','competition'),('competition','competition_rule')},
      'price':{('game','game_service'),('game_service','service'),('zone','resource'),('resource','service'),('audience','rate'),('service','rate')},
      'rental':{('service','resource'),('resource','zone'),('zone','rental_package'),('audience','rental_package')},
      'equipment_specs':{('service','resource'),('resource','equipment_model'),('zone','resource')},
      'equipment_location':{('equipment_model','resource'),('resource','zone')},
      'equipment_list':{('zone','resource'),('service','resource'),('resource','equipment_model')},
      'resource_capacity':{('zone','resource'),('resource','service')},
    }.get(task,set())
    for depth in range(4):
        nxt=[]
        for rid in front:
            r=records.get(rid)
            if not r:continue
            if r['kind'] in wanted:selected.append(rid)
            neighbors=[]
            for spec in CATALOG[r['kind']]['fields']:
                if not spec.get('reference_kind'):continue
                v=value(r,spec['key'])
                for target in v if isinstance(v,list) else [v]:
                    if target in records and (r['kind'],records[target]['kind']) in paths:neighbors.append((target,rid,spec['key'],target))
            # Only reverse to semantic children; do not traverse arbitrary
            # common zones back into unrelated games or competitions.
            for cid,key in reverse.get(rid,[]):
                c=records[cid]
                if (r['kind'],c['kind']) in paths:neighbors.append((cid,cid,key,rid))
            for target,parent,key,child in neighbors:
                # Avoid crossing from one game's offering to another game's
                # modes through a shared service/resource.
                if records[target]['kind']=='game' and target not in roots:continue
                if target not in seen:
                    seen.add(target);nxt.append(target);edges.append({'from':parent,'field':key,'to':child})
        front=nxt
        if not front:break
    return list(dict.fromkeys(selected)),edges

def compile(task,ids,records,*,fields=(),predicate=None):
    targets,edges=linked(records,ids,task)
    groups=REQUIRED[task]
    if task=='schedule':
        groups=(({'bookable_period':'bookable_periods','maintenance_period':'maintenance_periods'}.get(predicate,'open_periods'),),)
    nodes=[]
    for rid in targets:
        r=records[rid]
        alternatives=[all_of(*(fact(rid,key) for key in keys)) for keys in groups if all(key in r['fields'] for key in keys)]
        required=any_of(*alternatives) if alternatives else Node('missing',reason='required_task_fields_or_relation_missing')
        extras=[optional(fact(rid,key)) for key in fields if key in r['fields'] and not any(key in keys for keys in groups)]
        if task=='schema_attributes':required=all_of(*(fact(rid,key) for key in fields))
        nodes.append(all_of(required,*extras))
    relation_nodes=[fact(e['from'],e['field']) for e in edges if e['from'] in records and e['field'] in records[e['from']]['fields']]
    return all_of(*nodes,*relation_nodes) if nodes else Node('missing',reason='required_relation_missing'),targets,edges

def evaluate(node,snapshot,at,need_id='n1',predicate='',_seen=None):
    records=snapshot['release']['records'];sources=snapshot['release']['sources']
    if node.op=='not_applicable':return {'status':'not_applicable','reason':node.reason,'receipts':[]}
    if node.op=='missing':return {'status':'missing_source','reason':node.reason,'receipts':[]}
    if node.op=='field':
        r=records.get(node.record_id)
        if r is None or node.record_id in snapshot.get('withdrawn',[]):return {'status':'broken_relation','reason':'record_withdrawn_or_missing','receipts':[]}
        from .answer import effective
        if not effective(r,at,records):return {'status':'not_current','reason':'record_or_dependency_not_effective','receipts':[]}
        if r['kind'] in {'game_mode','control_set'}:
            game=records.get(value(r,'game_id'))
            if game is None:return {'status':'broken_relation','reason':'game_reference_missing','receipts':[]}
            platform=value(r,'platform');supported=value(game,'supported_platforms')
            if platform and supported:
                from .query_scope import same_platform
                if not any(same_platform(platform,p) for p in supported):return {'status':'broken_relation','reason':'platform_outside_game_scope','receipts':[]}
        f=r['fields'].get(node.key,{})
        if r['kind']=='person':
            import re
            if r['fields'].get('public_scope',{}).get('status')!='known':return {'status':'unsupported','reason':'public_scope_not_confirmed','receipts':[]}
            if re.search(r'private|internal|not public|ภายใน|ห้ามเผยแพร่',str(value(r,'public_scope') or ''),re.I):return {'status':'unsupported','reason':'not_public','receipts':[]}
        status=f.get('status','unknown')
        if status!='known':return {'status':{'conflicted':'conflict','not_applicable':'not_applicable'}.get(status,'missing_source'),'reason':'field_'+status,'receipts':[]}
        refs=f.get('evidence_refs') or []
        if not refs or any(ref.get('source_id') not in sources for ref in refs):return {'status':'broken_relation','reason':'missing_evidence_pointer','receipts':[]}
        if any(r['kind'] not in sources[ref['source_id']].get('authority_for',[]) for ref in refs):return {'status':'broken_relation','reason':'source_authority_scope_mismatch','receipts':[]}
        spec=next((s for s in CATALOG[r['kind']]['fields'] if s['key']==node.key),{})
        v=f.get('value')
        if spec.get('reference_kind'):
            for rid in v if isinstance(v,list) else [v]:
                if rid not in records or rid in snapshot.get('withdrawn',[]):return {'status':'broken_relation','reason':'referenced_record_missing','receipts':[]}
                if spec['reference_kind']!='*' and records[rid]['kind']!=spec['reference_kind']:return {'status':'broken_relation','reason':'wrong_reference_kind','receipts':[]}
        if r['kind'] in {'rate','rental_package'} and r['validity']['state']!='known':return {'status':'missing_source','reason':'effective_period_unconfirmed','receipts':[]}
        return {'status':'supported','receipts':[{'need_id':need_id,'subject':node.record_id,'record_id':node.record_id,
          'predicate':predicate,'field':node.key,'value':v,'revision':r['revision'],
          'units':value(r,'currency') if node.key=='amount_minor' else None,
          'applicability':r['validity'],'release_id':snapshot['active'],'epoch':snapshot['epoch'],
          'evidence_refs':refs,'sources':[{'source_id':ref['source_id'],'sha256':sources[ref['source_id']]['sha256'],
           'authority_for':sources[ref['source_id']].get('authority_for',[]),'locator':ref['locator']} for ref in refs],
          'verification':'typed_value_and_relation','prose_entailment_verified':False}]}
    rows=[evaluate(c,snapshot,at,need_id,predicate) for c in node.children]
    good=lambda r:r['status'] in {'supported','not_applicable'}
    if node.op=='optional':return {'status':'supported','optional_status':rows[0]['status'],'receipts':rows[0]['receipts']}
    if node.op=='any_of':
        selected=next((i for i,r in enumerate(rows) if good(r)),None)
        if selected is not None:return {**rows[selected],'selected_branch':selected}
    if rows and all(good(r) for r in rows):return {'status':'supported','receipts':[p for r in rows for p in r['receipts']]}
    priority=('conflict','broken_relation','unsupported','not_current','missing_source')
    status=next((s for s in priority if any(r['status']==s for r in rows)),'missing_source')
    return {'status':status,'reason':'dependency_not_supported','unmet':[r for r in rows if not good(r)],'receipts':[]}
