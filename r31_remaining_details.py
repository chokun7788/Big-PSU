import json,collections
from pathlib import Path
r=Path(Path('r31_report_path.txt').read_text().strip());paired={x['id']:x for x in map(json.loads,(r/'R31_C_PAIRED_TYPO_V2.jsonl').read_text(encoding='utf-8').splitlines())};remaining={k:v for k,v in paired.items() if v['v2']['regression']};requests={}
for line in (r/'final_C_all_results.jsonl').open(encoding='utf-8'):
    row=json.loads(line)
    for g in row['grades']:
        if g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl' and g['id'] in remaining:
            record=requests.setdefault(g['id'],{'assessment':remaining[g['id']]});record[g['variant']]=dict(question=row['question'],locale=row['locale'],expected=g['expected'],result=row['result'],legacy_failures=g['failures'])
assert len(requests)==111
counts=collections.Counter();by_lang=collections.Counter();positive=0;examples={}
with (r/'R31_REMAINING_PAIRED_DETAILS.jsonl').open('x',encoding='utf-8') as out:
    for id,record in requests.items():
        v=record['assessment']['v2']['noisy'];positive+=v['positive_contract_present'];by_lang[record['assessment']['locale']]+=1
        if not v['route_ok']:bucket='route_mismatch'
        elif not v['content_ok']:bucket='content_contract_failure'
        elif not v['latency_ok']:bucket='latency_failure'
        elif v['outcome']=='clarification':bucket='clarification_vs_expected_answer'
        elif v['outcome'] in ['no_answer','localization_pending','live_unavailable']:bucket='abstention_or_dependency_vs_expected'
        elif v['outcome']=='unknown':bucket='outcome_classification_gap'
        else:bucket='other_status_mismatch'
        counts[bucket]+=1;record['triage_hint']=bucket;record['not_a_confirmed_single_cause']=True
        examples.setdefault(bucket,dict(id=id,clean_question=record['clean']['question'],noisy_question=record['noisy']['question'],clean_answer=record['clean']['result']['answer'],noisy_answer=record['noisy']['result']['answer'],noisy_mode=record['noisy']['result']['mode'],v2=v))
        out.write(json.dumps(dict(id=id,**record),ensure_ascii=False)+'\n')
summary=dict(remaining_clean_pass_noisy_fail=111,by_locale=by_lang,triage_hints=counts,with_positive_content_contract=positive,without_positive_content_contract=111-positive,all_pairs_positive_contract=sum(x['v2']['noisy']['positive_contract_present'] for x in paired.values()),examples=examples,scope='Failed pair records with full question, clean/noisy answer, expected contract and trace. Triage counts are candidates, not verified causes for every row. Do not call all 111 wrong factual answers.')
with (r/'R31_REMAINING_PAIRED_SUMMARY.json').open('x',encoding='utf-8') as out:json.dump(summary,out,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in summary.items() if k!='examples'},ensure_ascii=False),flush=True)
print(json.dumps(examples,ensure_ascii=False,indent=2),flush=True)
