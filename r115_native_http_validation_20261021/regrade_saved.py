"""Version 2: audit ALL actual claim packet formats against frozen sources.

Offline only. Never rewrites original responses, grades, expected or source files.
"""
import collections, copy, json, sys
from pathlib import Path
from native_grader import grade, normal

R=Path(__file__).resolve().parent
reference=json.loads((R/'NATIVE_SOURCE_REFERENCE.json').read_text('utf8'))
byrecord=collections.defaultdict(list)
for f in reference['facts']:byrecord[f['record_id']].append(f)
allowed={(p['source_id'],p['locator']) for f in reference['facts'] for p in f.get('evidence_refs',[])+f.get('confirmation_evidence_refs',[])}
for r in reference['records'].values():
    for field in r.get('fields',{}).values():allowed.update((p['source_id'],p['locator']) for p in field.get('evidence_refs',[]))
expected={x['id']:x for x in json.loads((R/'NATIVE_EXPECTATIONS.json').read_text('utf8'))['questions']}

def collect(response):
    art=response.get('decision_artifact') or {};packets=list((art.get('domain_flow') or {}).get('typed_claims') or [])
    packets+=art.get('claim_packets') or []
    for n in art.get('need_results',[]):packets+=n.get('claim_packets') or []
    out={}
    for c in packets:
        if not isinstance(c,dict):continue
        if c.get('fact_id'):mapped=c
        else:
            rid=c.get('record_id');field=c.get('field');raw=c.get('value')
            refs={(p.get('source_id'),p.get('locator')) for p in c.get('evidence_refs',[])}
            candidates=[f for f in byrecord[rid] if refs and refs=={(p['source_id'],p['locator']) for p in f['evidence_refs']}]
            if len(candidates)==1:
                f=candidates[0];lang='en' if (response.get('language') or {}).get('effective')=='en' else 'th'
                # Read the actual packet value. Do not silently replace a wrong
                # packet with expected/source text simply because refs match.
                v=raw.get(lang) or raw.get('th') or raw.get('en') if isinstance(raw,dict) else raw
                mapped={**c,'fact_id':f['id'],'value':str(v),'numeric':None,'facet':f['facet']}
            else:mapped={**c,'fact_id':'unmapped:'+str(rid)+':'+str(field),'value':str(raw),'numeric':None}
        out[(mapped['fact_id'],mapped.get('numeric'),mapped.get('value'))]=mapped
    return list(out.values())

def reassess(x):
    response=copy.deepcopy(x['response']);art=response.setdefault('decision_artifact',{});claims=collect(response)
    art['domain_flow']={**(art.get('domain_flow') or {}),'typed_claims':claims}
    if not art.get('response_type') and not (art.get('domain_flow') or {}).get('status'):
        if response.get('mode','').endswith('_clarification'):art['response_type']='clarification'
    g=grade(expected[x['question_id']],response,x['http_status'],allowed)
    # A typed artifact cannot prove the renderer showed the expected content.
    body=normal(response.get('answer',''))
    g['returned_claim_values_not_literal_in_body']=[c['fact_id'] for c in claims if normal(c.get('value','')) not in body]
    g['original_classification']=x['grade']['classification']
    g['metric_version']='r115_saved_native_contract_v2_all_packet_shapes'
    g['semantic_review_required']=bool(g['extra'] or g['returned_claim_values_not_literal_in_body'])
    return g

if __name__=='__main__':
    run=R/'runs'/sys.argv[1]
    complete=json.loads((run/'TEST_COMPLETE.json').read_text('utf8'));assert complete['complete'] and complete['unique_question_keys']==1400
    out=run/'review_v2';out.mkdir(exist_ok=False);counts=collections.defaultdict(collections.Counter);seen=set()
    with (out/'ALL_REVIEWED.jsonl').open('x',encoding='utf8') as f:
        for line in (run/'RESULTS.jsonl').open(encoding='utf8'):
            x=json.loads(line);qid=x['question_id'];assert qid not in seen;seen.add(qid);g=reassess(x)
            f.write(json.dumps({'question_id':qid,'category':x['category'],'grade_v2':g},ensure_ascii=False)+'\n')
            for key in [x['category'],'ALL']:
                c=counts[key];c['n']+=1;c['strict']+=g['passed'];c[g['classification']]+=1;c['safe_abstention']+=g['safe_abstention']
                c['positive_nonfixture']+=bool(expected[qid]['goals']) and not g['fixture_only_goal']
                c['positive_nonfixture_pass']+=bool(expected[qid]['goals']) and not g['fixture_only_goal'] and g['passed']
                c['claims_in_artifact_not_literal_in_body']+=bool(g['returned_claim_values_not_literal_in_body'])
    assert len(seen)==1400
    summary={'version':'v2','expected_unchanged':True,'original_results_unchanged':True,'new_queries':0,'groups':{k:dict(v) for k,v in counts.items()},
        'caveat':'Source identity/value/state checks, not independent human semantic accuracy. Valid extra source clauses require review.'}
    (out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False))
