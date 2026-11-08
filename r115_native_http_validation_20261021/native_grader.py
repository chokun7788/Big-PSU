"""Saved-source contracts for native HTTP output; no model judge or new queries."""
import re
STATE={'answer':'answer','list':'answer','partial_answer':'partial','unconfirmed':'missing_source','clarification':'missing_input','not_current':'not_current','live_unavailable':'unavailable','unavailable':'unavailable','retry':'unavailable'}
def normal(x):return re.sub(r'\s+',' ',str(x)).strip().casefold()
def claims_from(response):
    art=response.get('decision_artifact') or {};claims=list((art.get('domain_flow') or {}).get('typed_claims') or [])
    for need in art.get('need_results',[]):claims.extend(c for c in need.get('claim_packets',[]) if isinstance(c,dict) and c.get('fact_id'))
    return list({(c['fact_id'],c.get('numeric'),c.get('value')):c for c in claims if isinstance(c,dict) and c.get('fact_id')}.values())
def grade(expect,response,http_status,allowed_refs):
    art=response.get('decision_artifact') or {};claims=claims_from(response);got={c['fact_id']:c for c in claims}
    state=STATE.get(art.get('response_type'),(art.get('domain_flow') or {}).get('status','unclassified'))
    goals=expect['goals'];mapped=[g for g in goals if g['alignment_kind']=='aligned'];wanted={g['native_fact_id']:g for g in mapped}
    missing=sorted(wanted.keys()-got.keys());extra=sorted(got.keys()-wanted.keys());wrong=[];evidence=[];literal=[];reference_gap=[]
    for g in goals:
        if g['alignment_kind']!='aligned':reference_gap.append(g['legacy_fact_id'])
        expected=g['legacy_expected'];v=expected.get('value')
        if v is not None and normal(v) in normal(response.get('answer','')):literal.append(g['legacy_fact_id'])
    for fid,g in wanted.items():
        c=got.get(fid)
        if c is None:continue
        if g.get('numeric') is not None:
            if c.get('numeric')!=g['numeric']:wrong.append(fid+':numeric')
        elif normal(c.get('value'))!=normal(g['value']):wrong.append(fid+':value')
        refs={(r.get('source_id'),r.get('locator')) for r in c.get('evidence_refs',[])}
        expected_refs={(r.get('source_id'),r.get('locator')) for r in g['evidence_refs']}
        if not expected_refs<=refs or not refs<=allowed_refs:evidence.append(fid)
    unknown_refs=[c['fact_id'] for c in claims if any((r.get('source_id'),r.get('locator')) not in allowed_refs for r in c.get('evidence_refs',[]))]
    valid=response.get('validation_ok') is True and (response.get('validation') or {}).get('ok',True)
    transport=200<=http_status<300 and isinstance(response.get('answer'),str)
    content_exact=not(missing or extra or wrong or evidence or reference_gap or unknown_refs)
    state_ok=state==expect['expected_status']
    passed=transport and valid and content_exact and state_ok
    safe_abstention=transport and not claims and state in {'missing_source','missing_input','not_current','unavailable'}
    matched=sum(fid in got and not any(w.startswith(fid+':') for w in wrong) for fid in wanted)
    if expect['fixture_only_goal']:classification='fixture_not_in_native_source'
    elif not transport:classification='http_or_response_failure'
    elif unknown_refs or evidence:classification='source_pointer_mismatch'
    elif not valid:classification='delivery_validation_failure'
    elif reference_gap:classification='source_alignment_or_projection_gap'
    elif passed:classification='source_contract_pass'
    elif content_exact and not state_ok:classification='expected_state_mismatch'
    elif expect['category']=='C11' and safe_abstention:classification='calendar_source_scope_or_applicability_gap'
    elif extra:classification='additional_or_wrong_scope_claims'
    elif wrong:classification='value_or_presentation_mismatch'
    elif missing:classification='required_claims_missing'
    else:classification='requires_review'
    return {'passed':passed,'content_exact':content_exact,'state_ok':state_ok,'expected_status':expect['expected_status'],'actual_status':state,
       'expected_claims':len(goals),'mapped_expected_claims':len(mapped),'returned_claims':len(claims),'matched_claims':matched,
       'missing':missing,'extra':extra,'wrong':wrong,'evidence_mismatches':evidence,'unknown_refs':unknown_refs,'reference_gaps':reference_gap,
       'literal_goal_spans_present':literal,'validation_ok':valid,'http_ok':transport,'safe_abstention':safe_abstention,'classification':classification,
       'fixture_only_goal':expect['fixture_only_goal'],'metric':'saved-source identity/value/state checks against pre-frozen native projection; not human semantic accuracy'}
