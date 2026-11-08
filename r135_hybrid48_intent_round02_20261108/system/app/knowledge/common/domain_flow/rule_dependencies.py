"""Current-source transitive clause closure, separate from topical entailment."""
from .projection import value

def scope_refs(index,fact):
    record=index.records[fact['record_id']];refs=[]
    keys=['text','competition_id','depends_on_ids','completeness','heading','facet','section_number'] if record['kind']=='competition_rule' else ['answer','question','topic','scope_note','legacy_search']
    for key in keys:refs.extend(record.get('fields',{}).get(key,{}).get('evidence_refs',[]))
    event=index.records.get(fact.get('event_id'),{})
    for key in ['event_name','game_id','rulebook_release']:refs.extend(event.get('fields',{}).get(key,{}).get('evidence_refs',[]))
    return [ref for i,ref in enumerate(refs) if ref not in refs[:i]]

def expected(index,question,operation,at):
    if operation=='list':
        from .collection_scopes import rules
        return [f['id'] for f in rules(index,question)]
    if operation=='compare':
        from .comparison_executor import execute
        from .understanding import MeaningTask
        plan=execute(index,'C13',question,MeaningTask(question,'competition_rules','C13','compare','rule_clause'),at)
    else:
        from .readers import rules_reader
        plan=rules_reader(index,question,at)
    return list(plan.ids) if plan is not None else []

def proof(index,question,operation,at,delivered):
    roots=expected(index,question,operation,at);required=set(roots)|set(delivered);nodes={};errors=[];limits=[];visiting=set();visited=set()
    if not roots:limits.append({'reason':'requested_clause_selection_not_source_determined'})
    def visit(fid):
        if fid in visiting:errors.append('cyclic_rule_dependency');return
        if fid in visited:return
        f=index.byid.get(fid)
        if not f or f.get('category')!='C13':errors.append('required_rule_fact_not_recorded');return
        visiting.add(fid);r=index.records[f['record_id']]
        known=r.get('fields',{}).get('depends_on_ids',{}).get('status')=='known' if r['kind']=='competition_rule' else False
        dependencies=value(r,'depends_on_ids') or [] if r['kind']=='competition_rule' else f.get('depends_on_ids',[])
        if not known:limits.append({'fact_id':fid,'reason':'dependency_set_unconfirmed'})
        complete=value(r,'completeness') if r['kind']=='competition_rule' else None
        if complete!='complete':limits.append({'fact_id':fid,'reason':'clause_completeness_unconfirmed','recorded_completeness':complete})
        nodes[fid]={'record_id':r['record_id'],'record_revision':r['revision'],'event_id':f.get('event_id'),'game_id':f.get('game_id'),'dependency_set_known':known,'depends_on_record_ids':dependencies,'completeness':complete,'evidence_refs':scope_refs(index,f)}
        for rid in dependencies:
            linked=[d for d in index.byrecord.get(rid,[]) if d['category']=='C13' and d.get('event_id')==f.get('event_id') and d.get('game_id')==f.get('game_id')]
            if not linked:errors.append('required_same_event_game_dependency_missing');continue
            for dep in linked:required.add(dep['id']);visit(dep['id'])
        visiting.remove(fid);visited.add(fid)
    for fid in sorted(required):visit(fid)
    return {'expected_fact_ids':sorted(roots),'delivered_fact_ids':sorted(delivered),'required_fact_ids':sorted(required),'missing_fact_ids':sorted(required-set(delivered)),'nodes':nodes,'errors':sorted(set(errors)),'limits':limits,'basis':'actual_request_clause_selection_and_source_dependency_closure','semantic_entailment_verified':False}
