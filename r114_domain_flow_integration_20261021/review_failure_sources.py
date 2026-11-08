"""Check source identity/heading for strict failures without changing the judge."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;out=R/'verification'/sys.argv[1]/'analysis';B=R.parent/'r113_multi_flow_benchmark_20261021'
facts={f['id']:f for f in json.loads((B/'COMMON_READ_MODEL.json').read_text('utf8'))['facts']};reviews=[]
for x in map(json.loads,(out/'ALL_FAILURES.jsonl').read_text('utf8').splitlines()):
    g=x['grade']
    if x['category']=='C12':
        assert not any(g[k] for k in ['missing_claims','unrequested_claims','wrong_values','evidence_mismatches'])
        states={c['status'] for c in x['result']['claims']};assert states=={'answer','unavailable'} and x['result']['status']=='partial'
        reviews.append({'arm':x['arm'],'id':x['question_id'],'classification':'expected_state_mismatch','all_source_claim_checks_passed':True,
          'claim_states':sorted(states),'expected_status':g['expected_status'],'actual_status':g['actual_status']})
    else:
        assert x['category']=='C13' and x['arm']=='reserved_automatic'
        expected={c['fact_id'] for c in x['expected']['claims']};wanted=[facts[k] for k in expected];returned=[facts[c['fact_id']] for c in x['result']['claims']]
        canonical=lambda x:json.dumps(x,sort_keys=True,ensure_ascii=False)
        headings={canonical(f['label']) for f in wanted};documents={canonical(f['subject']) for f in wanted}
        same_heading=all(canonical(f['label']) in headings for f in returned);same_document=all(canonical(f['subject']) in documents for f in returned)
        assert same_heading and same_document
        reviews.append({'arm':x['arm'],'id':x['question_id'],'classification':'heading_granularity_requires_semantic_review',
          'same_source_heading':same_heading,'same_source_document':same_document,'expected_paragraphs':len(expected),'returned_paragraphs':len(returned),
          'missing':g['missing_claims'],'wrong_values':g['wrong_values'],'evidence_mismatches':g['evidence_mismatches']})
(out/'SOURCE_BASED_FAILURE_REVIEW.json').write_text(json.dumps({'reviews':reviews,'raw_strict_results_retained':True,'human_semantic_adjudication':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'reviewed':len(reviews),'state_only':sum(x['classification']=='expected_state_mismatch' for x in reviews),
 'same_heading_granularity':sum(x['classification']=='heading_granularity_requires_semantic_review' for x in reviews)}))
