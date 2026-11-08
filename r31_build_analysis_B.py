"""Compare immutable grades and answers; never turn legacy failures into passes."""
import json,collections,statistics,sys
from pathlib import Path
root=Path(__file__).parent;r=Path((root/'r31_report_path.txt').read_text().strip());old=Path((root/'r30_report_path.txt').read_text().strip())
summary=json.loads((r/'final_B_all_summary.json').read_text());old_summary=json.loads((old/'FINAL_G6_FULL_ANALYSIS_SUMMARY.json').read_text())
sys.path.insert(0,r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
from tools.eval_contract_v2 import rescore_pair
overlay={x['id']:x for x in map(json.loads,Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\typo_r16_contract_overlay_20260930.jsonl').read_text(encoding='utf-8').splitlines())}
def identity(g):return g['corpus'],g['id'],g['variant'],g['row_index']
def signature(x):
    z=x.get('result',{})
    return (z.get('answer'),z.get('mode'),z.get('route',{}).get('category'),z.get('validation',{}).get('ok'))
baseline={}
for line in (old/'final_G6_all_results.jsonl').open(encoding='utf-8'):
    x=json.loads(line);baseline[x['key']]={'signature':signature(x),'grades':{identity(g):g['passed'] for g in x['grades']}}
counts=collections.Counter();types=collections.Counter();evidence=collections.Counter();by_locale=collections.defaultdict(collections.Counter);pairs={};seen=set();latencies=[];examples={};validation_errors=collections.Counter()
with (r/'R31_B_FAILURE_INVENTORY.jsonl').open('x',encoding='utf-8') as failures_out,(r/'R31_B_NEW_GRADE_FAILURES.jsonl').open('x',encoding='utf-8') as regressions_out,(r/'R31_B_CHANGED_ANSWERS.jsonl').open('x',encoding='utf-8') as changed_out:
    for name in summary['raw_parts']:
        for lineno,line in enumerate((r/name).open(encoding='utf-8'),1):
            x=json.loads(line);key=x['key'];assert key not in seen;seen.add(key);assert key in baseline
            result=x.get('result',{});latencies.append(float(result.get('elapsed',0)));mode=result.get('mode','exception')
            validation_errors.update(result.get('validation',{}).get('errors',[]))
            failed=[g for g in x['grades'] if not g['passed']];new=[]
            if failed:
                counts['failed_unique']+=1;failures_out.write(json.dumps(dict(key=key,question=x['question'],locale=x['locale'],result=result,failed_grades=failed,raw_part=name,raw_line=lineno),ensure_ascii=False)+'\n')
            answer_changed=signature(x)!=baseline[key]['signature']
            if answer_changed:
                counts['changed_answers']+=1;changed_out.write(json.dumps(dict(key=key,question=x['question'],locale=x['locale'],previous_signature=baseline[key]['signature'],new_result=result,grades=x['grades']),ensure_ascii=False)+'\n')
            for g in x['grades']:
                counts['grades']+=1;before=baseline[key]['grades'][identity(g)];counts['grade_passed']+=g['passed']
                counts['grade_improved']+=g['passed'] and not before
                if before and not g['passed']:
                    new.append(g);counts['grade_new_failed']+=1
                    counts['new_failed_answer_unchanged']+=not answer_changed
                evidence[g.get('evidence_level','unknown')]+=1;by_locale[g['expected'].get('locale','auto')]['total']+=1;by_locale[g['expected'].get('locale','auto')]['passed']+=g['passed']
                if not g['passed']:
                    failures=' '.join(g['failures'])
                    if 'legacy_mode_prefix' in failures or failures.startswith('intent:'):bucket='legacy_mode_or_intent_assertion'
                    elif 'live_booking_status_unavailable' in mode:bucket='controlled_live_dependency_unavailable'
                    elif 'retrieval evidence did not match' in failures:bucket='evidence_ids_need_source_review'
                    elif 'latency' in failures:bucket='latency_gate'
                    elif any(t in mode for t in ['clarification','no_current_game','no_data','unsupported','no_source']):bucket='abstention_vs_gold_or_missing_data_review'
                    else:bucket='route_content_source_review'
                    types[bucket]+=1
                    examples.setdefault(bucket,dict(question=x['question'],answer=result.get('answer'),mode=mode,route=result.get('route'),confidence=result.get('confidence'),trace=result.get('trace'),expected=g['expected'],failures=g['failures'],raw_part=name,raw_line=lineno,cause_confirmation='triage hint; not confirmed for every case'))
                if g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl':
                    pair=pairs.setdefault(g['id'],{'expected':g['expected']});pair[g['variant']]=dict(actual_route=result.get('route',{}).get('category',''),mode=mode,answer=result.get('answer',''),latency_ok=result.get('elapsed',0)<=g['expected'].get('latency_ceiling_sec',20),passed=g['passed'])
            if new:regressions_out.write(json.dumps(dict(key=key,question=x['question'],locale=x['locale'],answer_changed=answer_changed,new_failed_grades=new,result=result,raw_part=name,raw_line=lineno),ensure_ascii=False)+'\n')
assert seen==set(baseline) and len(seen)==20327 and counts['grades']==55583
paired=[]
with (r/'R31_B_PAIRED_TYPO_V2.jsonl').open('x',encoding='utf-8') as out:
    for id,pair in pairs.items():
        row=dict(**pair['expected'],clean=pair['clean'],noisy=pair['noisy'],regression=pair['clean']['passed'] and not pair['noisy']['passed'])
        z=rescore_pair(row,overlay.get(id));paired.append(z);out.write(json.dumps(z,ensure_ascii=False)+'\n')
pair_summary=dict(pairs=len(paired),v2_clean_passed=sum(x['v2']['clean']['passed'] for x in paired),v2_noisy_passed=sum(x['v2']['noisy']['passed'] for x in paired),v2_regressions=sum(x['v2']['regression'] for x in paired),scope='strict outcome/overlay; some rows lack positive content oracle; no owner or real booking confirmation')
audit=dict(unique_requests=len(seen),counts=counts,previous_failed_unique=old_summary['failed_unique_requests'],paired_typo=pair_summary,previous_paired_typo=old_summary['paired_typo'],evidence_levels=evidence,by_locale=by_locale,triage_hints=types,validation_errors=validation_errors,latency_loaded_direct_sec=dict(median=statistics.median(latencies),p95=sorted(latencies)[int(.95*(len(latencies)-1))],max=max(latencies)),same_inputs_and_grade_count=True,execution_provenance=dict(reexecuted_B=summary['reexecuted_requests'],retained_A=summary['retained_A_requests']),scope='All input keys retained; 4370 competition/CS2/pause inputs replayed on B and other rows retained from complete A. B is not a new full execution. LLM/semantic off, HTTP locale binding; direct pipeline guard short circuit separate; controlled booking unavailable. Do not aggregate as answer accuracy.')
for name,data in [('R31_B_FULL_ANALYSIS_SUMMARY.json',audit),('R31_B_FAILURE_EXAMPLES.json',examples)]:
    with (r/name).open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2)
print(json.dumps(audit,ensure_ascii=False),flush=True)
